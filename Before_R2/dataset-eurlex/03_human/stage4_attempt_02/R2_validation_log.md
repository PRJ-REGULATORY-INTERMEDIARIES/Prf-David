# R2 validation log

- Status: **PASS**
- Validation inputs: `R2_output_raw.json`, `R2_coding_input.json`, `reference_coding_schema.json`, and `validate_reference_logic.py`.
- Isolation: no R1, RA, attempt-01, G0/G1/G2, strings, or benchmark artifact was read by this validation.
- Records: 90
- Raw SHA-256: `18855B2053447D061BE3C1FCFAE9EBDBD579620D922A6394223F57B0F21AD2F6`
- JSON Schema: PASS
- A-E logical consistency: PASS
- Abstract logic tests: PASS

## Result

The validated output is an exact byte-for-byte copy of the raw output. No post-hoc substantive correction was necessary.
- Validated SHA-256: `18855B2053447D061BE3C1FCFAE9EBDBD579620D922A6394223F57B0F21AD2F6`
- Raw and validated hashes identical: `True`

## Final counts

- `relational_result`: conditional=1, insufficient_evidence=7, negative=80, positive=2
- `confidence`: high=71, low=8, medium=11
- `I != null`: 3
- `condition_C = YES`: 3
- `condition_D = YES`: 3
