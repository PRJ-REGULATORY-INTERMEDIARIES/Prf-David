#!/usr/bin/env python3
"""Structural QA for the future blinded human-adjudication delivery.

This program never opens an identity key and never evaluates the meaning of a
decision or justification.  It validates only the delivery contract described
in POST_ADJUDICATION_EXECUTION_PROTOCOL.md.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Iterable


EXPECTED_CARD_IDS = frozenset(
    [
        *(f"HQ-AI-{n:02d}" for n in range(1, 22)),
        *(f"HQ-CBAM-{n:02d}" for n in range(1, 17)),
        *(f"HQ-DIR-{n:02d}" for n in range(1, 8)),
        *(f"HQ-SCF-{n:02d}" for n in range(1, 13)),
    ]
)
REQUIRED_COLUMNS = (
    "card_id",
    "human_decision",
    "human_confidence",
    "human_justification",
    "reviewer",
    "adjudication_date",
)
ALLOWED_DECISIONS = frozenset(
    {"SUPPORTED_READING", "COMPETING_READING", "UNRESOLVED_UNCERTAINTY"}
)


def nonempty(value: str | None) -> bool:
    return value is not None and bool(value.strip())


def parse_iso_date(value: str) -> bool:
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_rows(rows: list[dict[str, str]], fieldnames: Iterable[str] | None,
                  min_confidence: float, max_confidence: float) -> dict[str, object]:
    """Return structural QA results without exposing row content in the report."""
    fields = set(fieldnames or [])
    errors: list[str] = []
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in fields]
    if missing_columns:
        errors.append("missing_required_columns=" + ",".join(missing_columns))
        return {"valid": False, "row_count": len(rows), "errors": errors}

    ids = [row["card_id"].strip() for row in rows]
    duplicates = sorted(card_id for card_id, count in Counter(ids).items() if count > 1)
    missing_ids = sorted(EXPECTED_CARD_IDS - set(ids))
    additional_ids = sorted(set(ids) - EXPECTED_CARD_IDS)
    blank_decisions = 0
    invalid_decisions = 0
    invalid_confidence = 0
    missing_justifications = 0
    missing_reviewers = 0
    missing_dates = 0
    invalid_dates = 0

    for row in rows:
        decision = row["human_decision"].strip()
        if not decision:
            blank_decisions += 1
        elif decision not in ALLOWED_DECISIONS:
            invalid_decisions += 1
        try:
            confidence = float(row["human_confidence"].strip())
            if not min_confidence <= confidence <= max_confidence:
                invalid_confidence += 1
        except (TypeError, ValueError):
            invalid_confidence += 1
        if not nonempty(row["human_justification"]):
            missing_justifications += 1
        if not nonempty(row["reviewer"]):
            missing_reviewers += 1
        date_value = row["adjudication_date"].strip()
        if not date_value:
            missing_dates += 1
        elif not parse_iso_date(date_value):
            invalid_dates += 1

    checks = {
        "expected_card_count": len(EXPECTED_CARD_IDS),
        "observed_row_count": len(rows),
        "duplicate_id_count": len(duplicates),
        "missing_id_count": len(missing_ids),
        "additional_card_count": len(additional_ids),
        "blank_decision_count": blank_decisions,
        "invalid_decision_count": invalid_decisions,
        "invalid_confidence_count": invalid_confidence,
        "missing_justification_count": missing_justifications,
        "missing_reviewer_count": missing_reviewers,
        "missing_date_count": missing_dates,
        "invalid_date_count": invalid_dates,
        "confidence_range": [min_confidence, max_confidence],
    }
    valid = all(
        checks[key] == 0
        for key in (
            "duplicate_id_count", "missing_id_count", "additional_card_count",
            "blank_decision_count", "invalid_decision_count", "invalid_confidence_count",
            "missing_justification_count", "missing_reviewer_count", "missing_date_count",
            "invalid_date_count",
        )
    ) and len(rows) == len(EXPECTED_CARD_IDS)
    return {"valid": valid, "checks": checks, "errors": errors}


def validate_file(path: Path, min_confidence: float, max_confidence: float) -> dict[str, object]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        return validate_rows(rows, reader.fieldnames, min_confidence, max_confidence)


def run_self_test() -> int:
    """Exercise parser and structural rules using generated fictitious rows only."""
    with tempfile.TemporaryDirectory() as directory:
        fixture = Path(directory) / "synthetic_adjudication.csv"
        with fixture.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS)
            writer.writeheader()
            for card_id in sorted(EXPECTED_CARD_IDS):
                writer.writerow({
                    "card_id": card_id,
                    "human_decision": "SUPPORTED_READING",
                    "human_confidence": "3",
                    "human_justification": "synthetic structural test",
                    "reviewer": "synthetic-reviewer",
                    "adjudication_date": "2000-01-01",
                })
        result = validate_file(fixture, 1, 5)
    if result["valid"]:
        print("SELF_TEST_PASS: synthetic structural fixture accepted")
        return 0
    print("SELF_TEST_FAIL: synthetic structural fixture rejected", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a future blinded adjudication CSV structurally.")
    parser.add_argument("adjudication_csv", nargs="?", type=Path)
    parser.add_argument("--min-confidence", type=float, default=1)
    parser.add_argument("--max-confidence", type=float, default=5)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if args.adjudication_csv is None:
        parser.error("adjudication_csv is required unless --self-test is used")
    if args.min_confidence > args.max_confidence:
        parser.error("--min-confidence cannot exceed --max-confidence")
    if not args.adjudication_csv.is_file():
        parser.error("adjudication_csv must be an existing file")
    result = validate_file(args.adjudication_csv, args.min_confidence, args.max_confidence)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
