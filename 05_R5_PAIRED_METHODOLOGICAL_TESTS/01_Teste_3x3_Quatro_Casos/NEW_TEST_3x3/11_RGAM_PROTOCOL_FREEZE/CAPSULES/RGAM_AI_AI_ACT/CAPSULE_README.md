# Execution capsule RGAM_AI_AI_ACT — INPUT ONLY (no analytical field populated)

**Status:** frozen input. Do not execute until separately authorized.

## Allowed reads (strict allow-list)
1. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md`
2. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DECISION_RULES_v1_0.md`
3. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`
4. `11_RGAM_PROTOCOL_FREEZE/RGAM_CASE_OUTPUT_SCHEMA.md`
5. `11_RGAM_PROTOCOL_FREEZE/RGAM_BLINDNESS_AND_ACCESS_POLICY.md`
6. This capsule directory only: `CASE_METADATA.json`, `LEGAL_SOURCE/32024R1689_official_en.xhtml`, `OUTPUT_TEMPLATES/`.

## Allowed writes
`12_RGAM_EXECUTION/RGAM_AI_AI_ACT/` only (copy the blank templates there and fill the machine columns).

## Source verification
Expected SHA-256 of the controlling legal source: `8f0b656302f9864cc87e040c371f209a9d65ae1a6cecc25ca5eb737e872d721a` (identical to the hash designated for the V8 arm in `08_STRICT_AI_PREPARATION/FINAL_COMMON_EVIDENCE_EQUALITY_CHECK.csv`). Verify before analysis; stop on mismatch (RGAM-DR-03).

## Not provided and not to be read
Any V8 output, count or conclusion; any R2/R3/R4 or historical relationship extraction; case-selection rankings; results of any other RGAM case; `09_V8_BASELINE_EXECUTION/`; `RGAM/V8_ACTIVE/`; any other directory of the repository.
