# -*- coding: utf-8 -*-
"""
Throwaway validation driver for Claude_R2_output_raw.json.
Step 3 of the preservation protocol:
 (a) load Claude_R2_output_raw.json
 (b) validate each record's structure against reference_coding_schema.json (jsonschema)
 (c) import and call validate_relational_logic from validate_reference_logic.py on each
     record, catching and logging any ValueError per candidate_id.
Does NOT modify validate_reference_logic.py or Claude_R2_output_raw.json.
"""
import json
import sys
import os

BASE = r"C:\Users\Adm\OneDrive\PROJETOS\GITHUB\git-cairesmachado-svg--ICM-PMO\10_PROGRAMAS\GP5_JRG\Prf-David\dataset-eurlex"
RAW = os.path.join(BASE, r"03_human\stage4_attempt_02\claude_replication_01\Claude_R2_output_raw.json")
SCHEMA = os.path.join(BASE, r"methodology\v1.1.0\reference_coding_schema.json")
VALLOGIC_DIR = os.path.join(BASE, r"03_human\stage4_attempt_02")

sys.path.insert(0, VALLOGIC_DIR)
import validate_reference_logic as vrl  # noqa: E402

import jsonschema  # noqa: E402

with open(RAW, encoding="utf-8") as f:
    records = json.load(f)

with open(SCHEMA, encoding="utf-8") as f:
    schema = json.load(f)

print(f"Loaded {len(records)} records from raw output.")

validator = jsonschema.Draft202012Validator(schema)

schema_errors = {}
logic_errors = {}

for rec in records:
    cid = rec.get("candidate_id", "<unknown>")
    errs = sorted(validator.iter_errors(rec), key=lambda e: list(e.path))
    if errs:
        schema_errors[cid] = [f"{list(e.path)}: {e.message}" for e in errs]

for rec in records:
    cid = rec.get("candidate_id", "<unknown>")
    try:
        vrl.validate_relational_logic(rec)
    except ValueError as e:
        logic_errors[cid] = str(e)
    except Exception as e:  # unexpected
        logic_errors[cid] = f"UNEXPECTED {type(e).__name__}: {e}"

print(f"\nSchema validation errors: {len(schema_errors)} record(s)")
for cid, errs in schema_errors.items():
    print(f"  {cid}:")
    for e in errs:
        print(f"    - {e}")

print(f"\nRelational-logic validation errors: {len(logic_errors)} record(s)")
for cid, e in logic_errors.items():
    print(f"  {cid}: {e}")

# duplicate id check
ids = [r["candidate_id"] for r in records]
dupes = set(x for x in ids if ids.count(x) > 1)
if dupes:
    print("\nDUPLICATE candidate_ids:", dupes)

print("\nSummary counts (from raw, pre-correction):")
from collections import Counter
print("screening_status:", Counter(r["screening_status"] for r in records))
print("relational_result:", Counter(r["relational_result"] for r in records))
print("confidence:", Counter(r["confidence"] for r in records))
print("I != null count:", sum(1 for r in records if r.get("I") not in (None, [])))
print("condition_C == YES count:", sum(1 for r in records if r["relational_test"]["condition_C"]["result"] == "YES"))
print("condition_D == YES count:", sum(1 for r in records if r["relational_test"]["condition_D"]["result"] == "YES"))

# dump errors to json for downstream correction script
with open(os.path.join(os.path.dirname(RAW), "_r2_validation_errors.json"), "w", encoding="utf-8") as f:
    json.dump({"schema_errors": schema_errors, "logic_errors": logic_errors}, f, ensure_ascii=False, indent=2)

print("\nDone.")
