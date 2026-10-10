"""Validate a future experimental response after the reference-lock gate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from _common import ROOT, assert_reference_locked, load_records


def validate_node(value: Any, schema: dict[str, Any], path: str) -> list[str]:
    errors: list[str] = []
    types = schema.get("type", [])
    if isinstance(types, str):
        types = [types]
    actual = "null" if value is None else "boolean" if isinstance(value, bool) else "array" if isinstance(value, list) else "object" if isinstance(value, dict) else "string" if isinstance(value, str) else "number"
    if actual not in types:
        return [f"type:{path}:{actual}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"enum:{path}:{value}")
    if actual == "string" and len(value) < schema.get("minLength", 0):
        errors.append(f"minLength:{path}")
    if actual == "object":
        properties = schema.get("properties", {})
        errors.extend(f"missing:{path}.{field}" for field in sorted(set(schema.get("required", [])) - value.keys()))
        if schema.get("additionalProperties") is False:
            errors.extend(f"unknown:{path}.{field}" for field in sorted(set(value) - set(properties)))
        for field, definition in properties.items():
            if field in value:
                errors.extend(validate_node(value[field], definition, f"{path}.{field}"))
    if actual == "array" and "items" in schema:
        for index, item in enumerate(value):
            errors.extend(validate_node(item, schema["items"], f"{path}[{index}]"))
    return errors


def validate_record(record: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    return validate_node(record, schema, "record")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--schema", type=Path, default=ROOT / "methodology" / "v1.1.2" / "experimental_output_schema.json")
    args = parser.parse_args()
    assert_reference_locked(ROOT)
    records = load_records(args.input)
    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    errors = [(index, error) for index, record in enumerate(records) for error in validate_record(record, schema)]
    if errors:
        for index, error in errors:
            print(f"record[{index}]: {error}")
        return 1
    print(f"VALID: {len(records)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
