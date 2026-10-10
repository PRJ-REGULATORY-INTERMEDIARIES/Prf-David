# R2 human validation dataset

Two consolidated CSVs, generated from the three cases' `PRIMARY_INTERPRETIVE_READER_PROPOSAL_R2.json` files (the second, independent primary-coding reading), for row-by-row researcher review. Encoding is UTF-8 with BOM (opens correctly in Excel).

- `R2_HUMAN_VALIDATION_relations.csv` — 20 rows, one per R-I-T relation record across Case 01 (6), Case 02 (8), Case 03 (6). Actor arrays (R/I/T) are flattened as `label (role); label (role)`; the five-dimension third-actor test is flattened as `distinction:YES; function:YES; ...`.
- `R2_HUMAN_VALIDATION_uncertainties.csv` — 28 rows, one per boundary-case / uncertainty-log entry across the same three cases (considered-and-rejected candidates, recital-only candidates, external-influence exclusions, cross-case notes, etc.).

Both files carry the same three trailing columns for the researcher to fill in, following this project's existing convention (`03_human/stage4_attempt_01/human_review.csv`):

- `PESQUISADOR: APPROVE / CHANGE / EXCLUDE / UNRESOLVED`
- `correction` — if CHANGE, what the corrected value should be
- `researcher_note` — free text

These are a *derived, human-readable export* of the R2 JSON proposals only — they do not merge, average, or adjudicate between R1 and R2, and they are not the project's formal `secondary_review` or `researcher_review` pipeline stage output. They exist to give the researcher a flat, spreadsheet-native surface for validating the R2 reading reported in this session. The authoritative source remains each case's `primary_coding/PRIMARY_INTERPRETIVE_READER_PROPOSAL_R2.json`.
