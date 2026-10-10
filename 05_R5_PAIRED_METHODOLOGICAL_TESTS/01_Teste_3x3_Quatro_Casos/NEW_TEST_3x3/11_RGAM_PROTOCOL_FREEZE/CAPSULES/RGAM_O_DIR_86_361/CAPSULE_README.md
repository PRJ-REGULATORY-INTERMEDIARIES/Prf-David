# Execution capsule RGAM_O_DIR_86_361 — INPUT ONLY (no analytical field populated)

**Status:** frozen input. Do not execute until separately authorized.

## Allowed reads (strict allow-list)
1. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md`
2. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DECISION_RULES_v1_0.md`
3. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`
4. `11_RGAM_PROTOCOL_FREEZE/RGAM_CASE_OUTPUT_SCHEMA.md`
5. `11_RGAM_PROTOCOL_FREEZE/RGAM_BLINDNESS_AND_ACCESS_POLICY.md`
6. This capsule directory only: `CASE_METADATA.json`, `LEGAL_SOURCE/31986L0361_official_en.html`, `OUTPUT_TEMPLATES/`.

## Allowed writes
`12_RGAM_EXECUTION/RGAM_O_DIR_86_361/` only (copy the blank templates there and fill the machine columns).

## Source verification
Expected SHA-256 of the controlling legal source: `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57` (identical to the hash designated for the V8 arm in `08_STRICT_AI_PREPARATION/FINAL_COMMON_EVIDENCE_EQUALITY_CHECK.csv`). Verify before analysis; stop on mismatch (RGAM-DR-03).

## Not provided and not to be read
Any V8 output, count or conclusion; any R2/R3/R4 or historical relationship extraction; case-selection rankings; results of any other RGAM case; `09_V8_BASELINE_EXECUTION/`; `RGAM/V8_ACTIVE/`; any other directory of the repository.
