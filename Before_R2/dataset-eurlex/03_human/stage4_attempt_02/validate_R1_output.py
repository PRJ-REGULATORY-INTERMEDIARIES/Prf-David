from __future__ import annotations

"""Validate the preserved R1 raw output without changing substantive decisions."""

import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from validate_reference_logic import run_abstract_tests, validate_relational_logic


OUT = Path(__file__).resolve().parent
RAW = OUT / "R1_output_raw.json"
VALIDATED = OUT / "R1_output.json"
LOG = OUT / "R1_validation_log.md"
INPUT = OUT / "R1_coding_input.json"
SCHEMA = OUT.parents[1] / "methodology" / "v1.1.0" / "reference_coding_schema.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    raw_bytes = RAW.read_bytes()
    records = json.loads(raw_bytes)
    inputs = json.loads(INPUT.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    input_by_id = {item["candidate_id"]: item for item in inputs}
    output_ids = [record.get("candidate_id") for record in records]
    if output_ids != [item["candidate_id"] for item in inputs]:
        errors.append("Output candidate order or IDs differ from the authorized R1 input packet.")
    if len(records) != len(inputs):
        errors.append(f"Record count differs: output={len(records)}, input={len(inputs)}.")
    for index, record in enumerate(records, start=1):
        candidate_id = record.get("candidate_id", f"index-{index}")
        for error in validator.iter_errors(record):
            path = "/".join(str(part) for part in error.absolute_path) or "$"
            errors.append(f"{candidate_id}: schema {path}: {error.message}")
        try:
            validate_relational_logic(record)
        except ValueError as exc:
            errors.append(f"{candidate_id}: relational logic: {exc}")
        source = input_by_id.get(candidate_id, {}).get("source_location", {})
        expected_location = {key: source.get(key) for key in ("celex", "article", "paragraph", "point", "subparagraph", "recital")}
        if record.get("source_location") != expected_location:
            errors.append(f"{candidate_id}: source_location differs from the authorized R1 input packet.")
        if record.get("candidate_origin") != input_by_id.get(candidate_id, {}).get("candidate_origin"):
            errors.append(f"{candidate_id}: candidate_origin differs from the authorized R1 input packet.")
    try:
        run_abstract_tests()
        abstract_tests = "PASS"
    except Exception as exc:  # validation must be documented before stopping
        errors.append(f"Abstract logic tests failed: {exc}")
        abstract_tests = "FAIL"

    status = "PASS" if not errors else "FAIL"
    raw_hash = sha256(RAW)
    lines = [
        "# R1 validation log",
        "",
        f"- Status: **{status}**",
        f"- Raw output: `R1_output_raw.json`",
        f"- Raw SHA-256: `{raw_hash}`",
        f"- Records: {len(records)}",
        f"- JSON Schema (reference_coding_schema.json): {'PASS' if not any(': schema ' in error for error in errors) else 'FAIL'}",
        f"- Reference logical consistency: {'PASS' if not any(': relational logic:' in error for error in errors) else 'FAIL'}",
        f"- Abstract reference-logic tests: {abstract_tests}",
        "- Substantive corrections applied after raw output: none.",
        "",
    ]
    if errors:
        lines.extend(["## Failures requiring explicit correction", ""])
        lines.extend(f"- {error}" for error in errors)
        lines.extend(["", "No corrected output was produced; `R1_output_raw.json` remains the preserved decision record."])
        LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
        raise SystemExit("R1 validation failed; see R1_validation_log.md")

    shutil.copyfile(RAW, VALIDATED)
    validated_hash = sha256(VALIDATED)
    lines.extend([
        "## Result",
        "",
        "The validated output is an exact byte-for-byte copy of the preserved raw R1 decision output; no post-hoc substantive correction was made.",
        f"- Validated SHA-256: `{validated_hash}`",
        f"- Raw and validated hashes identical: `{raw_hash == validated_hash}`",
        "",
        "## Distribution",
        "",
    ])
    for field in ("screening_status", "relational_result", "confidence", "primary_mechanism"):
        counts = Counter(record[field] for record in records)
        lines.append(f"- `{field}`: " + ", ".join(f"{key}={counts[key]}" for key in sorted(counts)))
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "records": len(records), "raw_sha256": raw_hash, "validated_sha256": validated_hash}, ensure_ascii=False))


if __name__ == "__main__":
    main()
