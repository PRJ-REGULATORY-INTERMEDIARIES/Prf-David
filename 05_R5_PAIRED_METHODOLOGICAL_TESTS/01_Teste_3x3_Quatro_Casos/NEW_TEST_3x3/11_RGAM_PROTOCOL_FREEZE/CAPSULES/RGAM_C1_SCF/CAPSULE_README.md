# Execution capsule RGAM_C1_SCF — INPUT ONLY (no analytical field populated)

**Status:** frozen input. Do not execute until separately authorized.

## Allowed reads (strict allow-list)
1. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md`
2. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DECISION_RULES_v1_0.md`
3. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`
4. `11_RGAM_PROTOCOL_FREEZE/RGAM_CASE_OUTPUT_SCHEMA.md`
5. `11_RGAM_PROTOCOL_FREEZE/RGAM_BLINDNESS_AND_ACCESS_POLICY.md`
6. This capsule directory only: `CASE_METADATA.json`, `LEGAL_SOURCE/32023R0955_official_en.html`, `OUTPUT_TEMPLATES/`.

## Allowed writes
`12_RGAM_EXECUTION/RGAM_C1_SCF/` only (copy the blank templates there and fill the machine columns).

## Source verification
Expected SHA-256 of the controlling legal source: `cf8c60fc233311436dfdd3ee236d0c8399eda55fea174610e91b5594f84a0408` (identical to the hash designated for the V8 arm in `08_STRICT_AI_PREPARATION/FINAL_COMMON_EVIDENCE_EQUALITY_CHECK.csv`). Verify before analysis; stop on mismatch (RGAM-DR-03).

## Not provided and not to be read
Any V8 output, count or conclusion; any R2/R3/R4 or historical relationship extraction; case-selection rankings; results of any other RGAM case; `09_V8_BASELINE_EXECUTION/`; `RGAM/V8_ACTIVE/`; any other directory of the repository.
