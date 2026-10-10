"""Compare future G0/G1/G2 runs using the same locked-reference matcher."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from _common import ROOT, assert_reference_locked, build_comparison, load_records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, default=ROOT / "03_human" / "reference_benchmark.json")
    parser.add_argument("--g0", type=Path, required=True)
    parser.add_argument("--g1", type=Path, required=True)
    parser.add_argument("--g2", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    assert_reference_locked(ROOT)
    reference = load_records(args.reference)
    result = {condition: build_comparison(reference, load_records(path)) for condition, path in (("G0", args.g0), ("G1", args.g1), ("G2", args.g2))}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

