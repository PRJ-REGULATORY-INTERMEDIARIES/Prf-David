"""Shared helpers for the AUTONOMOUS_ROTEM_COMPARISON run.

All helpers are read-only with respect to source files; they only write inside RUN_ROOT.
"""
import csv
import datetime as _dt
import hashlib
import os
from pathlib import Path

RUN_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = RUN_ROOT.parent
RUN_ID = RUN_ROOT.name


def sha256(path, lf_normalize=False):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        data = f.read()
    if lf_normalize:
        data = data.replace(b"\r\n", b"\n")
    h.update(data)
    return h.hexdigest().upper()


def now_iso():
    return _dt.datetime.now().astimezone().isoformat(timespec="seconds")


def rel_to_project(path):
    p = Path(path).resolve()
    try:
        return p.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return p.as_posix()


def write_csv(path, header, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            if isinstance(r, dict):
                w.writerow([r.get(h, "") for h in header])
            else:
                w.writerow(r)


def read_csv(path, encoding="utf-8-sig"):
    with open(path, newline="", encoding=encoding) as f:
        return list(csv.DictReader(f))


def append_log(line):
    log = RUN_ROOT / "RUN_LOG.md"
    with open(log, "a", encoding="utf-8") as f:
        f.write(f"- {now_iso()} — {line}\n")
