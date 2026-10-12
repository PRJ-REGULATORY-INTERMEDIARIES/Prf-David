#!/usr/bin/env python3
"""Institutional sweep: one capture of each page listed in a sweep registry.

Reads mapping/protocol/INSTITUTIONAL_SWEEP_G2_ROUND<n>.csv and captures every URL once with
scripts/capture_evidence.py (record_id = sweep_id), skipping sweep ids already captured.
It does not follow links: a second step, if one is needed, is a new row in the registry.
The registry columns `found_resources` and `result_note` are filled by a person after
reading the captures; the build joins them with the capture outcome.
"""
import argparse
import csv
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import capture_evidence  # noqa: E402

CAPTURE_DIR = ROOT / 'mapping' / 'evidence' / 'captures'


def read_registry(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))


def captured_ids(out_dir=CAPTURE_DIR):
    log = Path(out_dir) / capture_evidence.LOG_NAME
    if not log.exists():
        return set()
    return {json.loads(x)['record_id'] for x in log.read_text(encoding='utf-8').splitlines() if x.strip()}


def run(registry, out_dir=CAPTURE_DIR, pause=4.0, capture=capture_evidence.capture):
    done = captured_ids(out_dir)
    out = []
    for row in read_registry(registry):
        if row['sweep_id'] in done:
            continue
        if out:
            time.sleep(pause)
        out.append(capture(row['url'], row['sweep_id'], out_dir=out_dir,
                           purpose=f"G2 round 2 institutional sweep: {row['purpose']} (single GET)", pause=3.0))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--registry', required=True)
    args = ap.parse_args()
    for rec in run(args.registry):
        last = rec['attempts'][-1] if rec.get('attempts') else {}
        print(rec['record_id'], rec['outcome'], rec.get('http_status') or last.get('http_status') or last.get('error', '')[:60],
              rec.get('bytes'), (rec.get('final_url') or '')[:80])


if __name__ == '__main__':
    main()
