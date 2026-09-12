from __future__ import annotations

"""R2-only validation: schema and logic checks without reading other coders."""

import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from validate_reference_logic import run_abstract_tests, validate_relational_logic


OUT = Path(__file__).resolve().parent
RAW = OUT / "R2_output_raw.json"
VALIDATED = OUT / "R2_output.json"
LOG = OUT / "R2_validation_log.md"
INPUT = OUT / "R2_coding_input.json"
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
    expected_ids = [item["candidate_id"] for item in inputs]
    if [record.get("candidate_id") for record in records] != expected_ids:
        errors.append("Output candidate order or IDs differ from the authorized R2 input packet.")
    if len(records) != len(inputs):
        errors.append(f"Record count differs: raw={len(records)}, input={len(inputs)}.")
    input_by_id = {item["candidate_id"]: item for item in inputs}
    location_keys = ("celex", "article", "paragraph", "point", "subparagraph", "recital")
    for record in records:
        candidate_id = record.get("candidate_id", "<missing>")
        for error in validator.iter_errors(record):
            field = "/".join(str(part) for part in error.absolute_path) or "$"
            errors.append(f"{candidate_id}: schema {field}: {error.message}")
        try:
            validate_relational_logic(record)
        except ValueError as exc:
            errors.append(f"{candidate_id}: relational logic: {exc}")
        expected = input_by_id.get(candidate_id)
        if expected:
            location = {key: expected["source_location"].get(key) for key in location_keys}
            if record.get("source_location") != location:
                errors.append(f"{candidate_id}: source location differs from authorized R2 input.")
            if record.get("candidate_origin") != expected.get("candidate_origin"):
                errors.append(f"{candidate_id}: candidate origin differs from authorized R2 input.")
    try:
        run_abstract_tests()
        abstract_status = "PASS"
    except Exception as exc:
        errors.append(f"Abstract logic tests failed: {exc}")
        abstract_status = "FAIL"

    raw_hash = sha256(RAW)
    status = "PASS" if not errors else "FAIL"
    lines = [
        "# R2 validation log",
        "",
        f"- Status: **{status}**",
        "- Validation inputs: `R2_output_raw.json`, `R2_coding_input.json`, `reference_coding_schema.json`, and `validate_reference_logic.py`.",
        "- Isolation: no R1, RA, attempt-01, G0/G1/G2, strings, or benchmark artifact was read by this validation.",
        f"- Records: {len(records)}",
        f"- Raw SHA-256: `{raw_hash}`",
        f"- JSON Schema: {'PASS' if not any(': schema ' in error for error in errors) else 'FAIL'}",
        f"- A-E logical consistency: {'PASS' if not any(': relational logic:' in error for error in errors) else 'FAIL'}",
        f"- Abstract logic tests: {abstract_status}",
        "",
    ]
    if errors:
        lines.extend(["## Detected incompatibilities", ""])
        lines.extend(f"- {error}" for error in errors)
        lines.extend(["", "No substantive correction was applied automatically. The preserved raw output remains authoritative pending an explicit, documented correction."])
        LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
        raise SystemExit("R2 validation failed; see R2_validation_log.md")

    shutil.copyfile(RAW, VALIDATED)
    validated_hash = sha256(VALIDATED)
    lines.extend([
        "## Result",
        "",
        "The validated output is an exact byte-for-byte copy of the raw output. No post-hoc substantive correction was necessary.",
        f"- Validated SHA-256: `{validated_hash}`",
        f"- Raw and validated hashes identical: `{raw_hash == validated_hash}`",
        "",
        "## Final counts",
        "",
    ])
    for field in ("relational_result", "confidence"):
        values = Counter(record[field] for record in records)
        lines.append(f"- `{field}`: " + ", ".join(f"{key}={values[key]}" for key in sorted(values)))
    lines.extend([
        f"- `I != null`: {sum(record['I'] not in (None, []) for record in records)}",
        f"- `condition_C = YES`: {sum(record['relational_test']['condition_C']['result'] == 'YES' for record in records)}",
        f"- `condition_D = YES`: {sum(record['relational_test']['condition_D']['result'] == 'YES' for record in records)}",
    ])
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": status,
        "records": len(records),
        "raw_sha256": raw_hash,
        "validated_sha256": validated_hash,
        "I_not_null": sum(record["I"] not in (None, []) for record in records),
        "condition_C_yes": sum(record["relational_test"]["condition_C"]["result"] == "YES" for record in records),
        "condition_D_yes": sum(record["relational_test"]["condition_D"]["result"] == "YES" for record in records),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
