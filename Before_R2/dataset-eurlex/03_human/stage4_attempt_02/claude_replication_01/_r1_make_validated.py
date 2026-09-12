# -*- coding: utf-8 -*-
"""
Step 4: produce the validated copy Claude_R1_output.json from Claude_R1_output_raw.json,
applying only the two corrections identified by validate_reference_logic.py, each logged.
Does NOT modify Claude_R1_output_raw.json.
"""
import json
import hashlib
import importlib.util

BASE = r"C:\Users\Adm\OneDrive\PROJETOS\GITHUB\git-cairesmachado-svg--ICM-PMO\10_PROGRAMAS\GP5_JRG\Prf-David\dataset-eurlex"
RAW_PATH = BASE + r"\03_human\stage4_attempt_02\claude_replication_01\Claude_R1_output_raw.json"
OUT_PATH = BASE + r"\03_human\stage4_attempt_02\claude_replication_01\Claude_R1_output.json"
SCHEMA_PATH = BASE + r"\methodology\v1.1.0\reference_coding_schema.json"
LOGIC_PATH = BASE + r"\03_human\stage4_attempt_02\validate_reference_logic.py"

data = json.load(open(RAW_PATH, encoding="utf-8"))
by_id = {r["candidate_id"]: r for r in data}

corrections_log = []

# --- Correction 1: CAND2-D64B4FFA6C04 (Article 4(4)) ---
cid = "CAND2-D64B4FFA6C04"
rec = by_id[cid]
before_I = rec["I"]
rec["I"] = [{"label": "Advisory Board",
             "role": "provides advice taken into account by the Commission when setting the projected indicative Union greenhouse gas budget",
             "evidence_refs": ["E1"]}]
for item in rec["evidence_items"]:
    if item["evidence_id"] == "E1" and "I" not in item["supports"]:
        item["supports"].append("I")
corrections_log.append({
    "candidate_id": cid, "field": "I",
    "original_value": before_I, "corrected_value": rec["I"],
    "rule_violated": "validate_relational_logic: condition_C == 'YES' requires record['I'] to be populated",
    "explanation": "The raw record already judged condition_C = YES (the Advisory Board is a distinct third actor named in Article 4(4)) but left the I field empty because no target (T) was established for it to mediate towards (condition_B = NO). This was an internal inconsistency between the C-condition judgment and the I field, not a re-evaluation of the merits of condition_C or condition_D (which remains UNCLEAR) or of relational_result (which remains negative, driven by condition_B = NO regardless of this fix).",
})

# --- Correction 2: CAND2-8607C66ECE11 (Article 8(3)(d)) ---
cid = "CAND2-8607C66ECE11"
rec = by_id[cid]
before_I = rec["I"]
before_status = rec["screening_status"]
rec["I"] = [
    {"label": "IPCC", "role": "international scientific body whose reports are cited as evidence but not tasked with a regulatory function by this Regulation", "evidence_refs": ["E1"]},
    {"label": "IPBES", "role": "international scientific body whose reports are cited as evidence but not tasked with a regulatory function by this Regulation", "evidence_refs": ["E1"]},
]
rec["screening_status"] = "candidate"
for item in rec["evidence_items"]:
    if item["evidence_id"] == "E1" and "I" not in item["supports"]:
        item["supports"].append("I")
corrections_log.append({
    "candidate_id": cid, "field": "I",
    "original_value": before_I, "corrected_value": rec["I"],
    "rule_violated": "validate_relational_logic: condition_C == 'YES' requires record['I'] to be populated",
    "explanation": "The raw record judged condition_C = YES (IPCC and IPBES are analytically distinct actors named in the text) but left I empty because their function was judged not to mediate a regulatory relation under this Act (condition_D = NO, unchanged). The I field is corrected to identify them, consistent with the C = YES judgment already made; relational_result remains negative, driven by condition_D = NO.",
})
corrections_log.append({
    "candidate_id": cid, "field": "screening_status",
    "original_value": before_status, "corrected_value": rec["screening_status"],
    "rule_violated": "validate_relational_logic: screening_status == 'direct_relationship' requires record['I'] to be empty/None",
    "explanation": "A direct consequence of the I-field correction above: once a distinct third party (IPCC/IPBES) is identified in I, the relation is no longer a pure dyadic 'direct_relationship' by the reference validator's own definition, even though that third party does not mediate a regulatory function (condition_D = NO). screening_status is corrected to 'candidate', which is the mechanically consistent status for a candidate with an identified but non-mediating third party. relational_result (negative) is unchanged.",
})

# --- write validated copy ---
with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# --- re-validate the corrected copy ---
import jsonschema
schema = json.load(open(SCHEMA_PATH, encoding="utf-8"))
validator = jsonschema.Draft202012Validator(schema)
schema_errors = {}
for rec in data:
    errs = list(validator.iter_errors(rec))
    if errs:
        schema_errors[rec["candidate_id"]] = [f"{e.message} @ {'/'.join(str(x) for x in e.absolute_path)}" for e in errs]

spec = importlib.util.spec_from_file_location("validate_reference_logic", LOGIC_PATH)
vrl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vrl)
logic_errors = {}
for rec in data:
    try:
        vrl.validate_relational_logic(rec)
    except ValueError as exc:
        logic_errors[rec["candidate_id"]] = str(exc)

print("post-fix schema errors:", len(schema_errors))
for cid, e in schema_errors.items():
    print(cid, e)
print("post-fix logic errors:", len(logic_errors))
for cid, e in logic_errors.items():
    print(cid, e)

print()
print("CORRECTIONS LOG (JSON):")
print(json.dumps(corrections_log, ensure_ascii=False, indent=2))

raw_hash = hashlib.sha256(open(RAW_PATH, "rb").read()).hexdigest()
out_hash = hashlib.sha256(open(OUT_PATH, "rb").read()).hexdigest()
print()
print("raw sha256:", raw_hash)
print("validated sha256:", out_hash)
print("records in validated copy:", len(data))
