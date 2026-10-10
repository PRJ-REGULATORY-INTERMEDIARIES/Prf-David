"""Append issues/decisions to ISSUES_AND_DECISIONS.csv (idempotent on ISSUE_ID)."""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT  # noqa: E402

F = RUN_ROOT / "ISSUES_AND_DECISIONS.csv"
HDR = ["ISSUE_ID", "ROUND", "TYPE", "SEVERITY", "DESCRIPTION", "EVIDENCE", "DECISION_OR_RESOLUTION", "STATUS"]


def upsert(items):
    rows = []
    if F.exists():
        with open(F, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    by = {r["ISSUE_ID"]: r for r in rows}
    for it in items:
        by[it["ISSUE_ID"]] = {h: it.get(h, by.get(it["ISSUE_ID"], {}).get(h, "")) for h in HDR}
    with open(F, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HDR)
        w.writeheader()
        for k in sorted(by):
            w.writerow(by[k])
