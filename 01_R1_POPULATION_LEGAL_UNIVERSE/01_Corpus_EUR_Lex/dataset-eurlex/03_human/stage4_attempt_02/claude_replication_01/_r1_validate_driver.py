# -*- coding: utf-8 -*-
"""
Step 3 validation driver for Claude_R1_output_raw.json.
(a) loads the raw output
(b) validates structure against reference_coding_schema.json via jsonschema
(c) imports and calls validate_relational_logic from validate_reference_logic.py on each record,
    catching and logging any ValueError per candidate_id.
Does not modify validate_reference_logic.py. Read-only with respect to the raw file.
"""
import json
import sys
import importlib.util

BASE = r"C:\Users\Adm\OneDrive\PROJETOS\GITHUB\git-cairesmachado-svg--ICM-PMO\10_PROGRAMAS\GP5_JRG\Prf-David\dataset-eurlex"
RAW_PATH = BASE + r"\03_human\stage4_attempt_02\claude_replication_01\Claude_R1_output_raw.json"
SCHEMA_PATH = BASE + r"\methodology\v1.1.0\reference_coding_schema.json"
LOGIC_PATH = BASE + r"\03_human\stage4_attempt_02\validate_reference_logic.py"

# --- load validate_reference_logic.py as a module without modifying it ---
spec = importlib.util.spec_from_file_location("validate_reference_logic", LOGIC_PATH)
vrl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vrl)

# --- (b) jsonschema structural validation ---
import jsonschema
schema = json.load(open(SCHEMA_PATH, encoding="utf-8"))
data = json.load(open(RAW_PATH, encoding="utf-8"))
validator = jsonschema.Draft202012Validator(schema)

schema_errors = {}
for rec in data:
    errs = list(validator.iter_errors(rec))
    if errs:
        schema_errors[rec["candidate_id"]] = [
            f"{e.message} @ {'/'.join(str(x) for x in e.absolute_path)}" for e in errs
        ]

# --- (c) relational logic validation via validate_reference_logic.py ---
logic_errors = {}
for rec in data:
    try:
        vrl.validate_relational_logic(rec)
    except ValueError as exc:
        logic_errors[rec["candidate_id"]] = str(exc)

print("=== SCHEMA ERRORS ===")
print("count:", len(schema_errors))
for cid, errs in schema_errors.items():
    print(cid)
    for e in errs:
        print("   ", e)

print()
print("=== RELATIONAL LOGIC ERRORS (validate_reference_logic.py) ===")
print("count:", len(logic_errors))
for cid, msg in logic_errors.items():
    print(cid, "->", msg)

print()
print("records processed:", len(data))
