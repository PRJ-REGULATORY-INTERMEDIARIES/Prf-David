# R4.2E-B1 Batch 04 freeze record

**Freeze ID:** `R4_2E_B1_BATCH_04_FREEZE_001`
**Status:** `R4_2E_B1_ADVANCED_VALIDATION_COMPLETE_PENDING_REPAIR_DECISION`

## Provenance (corrected)

`EXECUTION_ENVIRONMENT = Claude Code / VS Code extension`
`RESEARCHER_SELECTED_MODEL = Claude Opus 5.5 Extra High`
`RUNTIME_REPORTED_MODEL = Claude Opus 5`
`RUNTIME_MODEL_ID = claude-opus-5`
`MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE`

The researcher selected `Claude Opus 5.5 Extra High` in the VS Code Claude agent UI. The execution
environment reported `Claude Opus 5` with identifier `claude-opus-5`. The relationship between the
two labels cannot be independently verified from inside the session. Both are recorded. The runtime
did **not** verify `Claude Opus 5.5 Extra High`, and the two labels are **not** asserted to be
equivalent.

B1-04 is the only B1 batch reviewed outside GPT-5.6 Terra High. The transition followed the
Codex/Terra usage-limit interruption and is a continuity fallback, not a methodological restart.
B1-01, B1-02 and B1-03 were not rerun, reopened or modified. Their Terra provenance
(`GPT-5.6 Terra High`, `MODEL_VARIANT_NOT_EXPOSED`) is unchanged and was re-verified after this
correction.

## Authoritative output

`R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv`
SHA-256 `253D80E305A21444343B5A5893AC5A4871FB415E561BA802E957CE94435A5BD1`
(provenance-corrected authoritative version)

The pre-correction export is preserved as
`R4_2E_B1_ADVANCED_VALIDATION_B1_04_v1_PROVENANCE_SUPERSEDED.csv`,
SHA-256 `8651E54BB033FC5F2AD5C2594F2B355FFCA6189777FF436E11C73574545E2D22`.
It is historical provenance only.

The correction rewrote **only** the three model columns. The correction script asserted, and
re-verification confirmed, **zero** differences in any other cell across all 35 rows, including
`RUN_TIMESTAMP`. No substantive adjudication was altered.

Build script: `09_logs/build_r4_2e_b1_batch04_validation.py` (Python `csv` module, `QUOTE_ALL`).
Correction script: `09_logs/apply_r4_claude_provenance_correction.py`.

## Schema validation before freeze

| Gate | Result |
| --- | --- |
| Expected IDs | 35 |
| Actual IDs | 35 |
| Unique IDs | 35 |
| Missing IDs | 0 |
| Extra IDs | 0 |
| Duplicate IDs | 0 |
| Column count | 33 (authoritative v2 order) |
| Round-trip reparse | 35 rows, column order and ID order identical |
| Embedded newlines | 0 |
| Blank reasoning notes | 0 |
| Shifted or truncated fields | none detected |

No malformed intermediate export was produced, so no defective variant needed preservation.
The B1-01 separator defect did not recur because every field is written through a CSV library
with full quoting.

## Composition

- 24 family representatives
- 8 individual advanced cases
- 3 hidden NO_REPAIR controls

## Substantive results

Defect decisions: YES 34, PARTIALLY 1, NO 0, ABSTAIN 0.
Proposition anchor confidence: HIGH 31, MEDIUM 4, LOW 0.
Field corrections (`*_CORRECT = NO`): Actor 15, Action 30, Object 34, Counterpart 22, Recipient 24.
Relational differentiation: NEITHER 26, COUNTERPART_ONLY 5, RECIPIENT_ONLY 4.
Family template status (24 representatives): VALIDATED_WITH_CONDITIONS 22,
REQUIRES_MORE_REPRESENTATIVES 1, HUMAN_REVIEW_REQUIRED 1.
Individual routes (8): MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA 6, HUMAN_ADJUDICATION_REQUIRED 2.

B1-04 was drawn from the advanced-review queue, so a high defect rate is expected by construction
and is not a corpus prevalence estimate.

## Review-design limitations recorded at freeze

1. **Control blinding was not fully preserved.** Section 20 of the continuation brief required
   reading `R4_2E_B1_NO_REPAIR_CONTROL_SAMPLE.csv` to identify the three B1-03 controls. That file
   lists all twelve controls and carries no batch column, so identifying the B1-03 controls
   necessarily disclosed the B1-04 controls before B1-04 substantive review began. The identical
   protocol applies to every batch after B1-01, so the same exposure is structurally possible for
   B1-02 and B1-03; whether it occurred there cannot be verified from the repository. All 35 B1-04
   cases were reviewed under one protocol and control membership was not used to alter any decision,
   but the blinding claim is recorded as
   `B1_04_CONTROL_BLINDING = COMPROMISED_BY_REQUIRED_SEQUENTIAL_FILE_ACCESS`.

2. **The blind review input under-exposes the extraction schema.** `ORIGINAL_ACTION` in
   `R4_2E_B1_BLIND_SUBSTANTIVE_REVIEW_INPUT.csv` carries only `LEGAL_ACTION`. The frozen extraction
   also holds `LEGAL_VERB` and `MODALITY`, which the input does not show. Corpus-wide, `LEGAL_VERB`
   contains an explicit modal in 1,370 of 1,404 records while `LEGAL_ACTION` does so in 5. Judged
   from the input alone, deontic modality appears absent; judged against the full record it is
   present in a sibling column. B1-04 was scored against the full frozen record. This affects the
   comparability of all four batches and is recorded as
   `B1_REVIEW_INPUT_UNDER_EXPOSES_SCHEMA = CONFIRMED`.

3. **Cross-model threshold calibration differs.** B1-04 treats a coordinated predicate absorbed into
   the object, and a mis-coded `MODALITY` value, as action or object defects. At least one Terra
   control adjudicated CLEAN_CONFIRMED in B1-03 contains a coordinated predicate inside its own
   proposed object. The two thresholds are therefore not identical. Batch-level defect proportions
   must not be pooled naively or read as comparative model accuracy, which the continuation brief
   also prohibits. Recorded as `CROSS_MODEL_THRESHOLD_CALIBRATION_DIFFERENCE = OBSERVED`.

## Control unblinding

The three B1-04 controls were revealed only after this freeze and after schema validation and hash
calculation. Results are in `R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_04.csv`,
SHA-256 `E0494AA69C004A36EC4586CB6BE312737236A89BD747925C0A28DA32D4EF1D02`.
No substantive B1-04 decision was altered after unblinding; the unblinding script asserts that each
control result matches the frozen adjudication.

| Record | Result | Type | Severity |
| --- | --- | --- | --- |
| EXT-000093 | DEFECT_FOUND | PREDICATE_RECONSTRUCTION_ERROR | MODERATE |
| EXT-000777 | DEFECT_FOUND | CROSS_SENTENCE_CONTAMINATION | MODERATE |
| EXT-000937 | DEFECT_FOUND | PREDICATE_RECONSTRUCTION_ERROR | MODERATE |

## Firewalls unchanged

`RIT_CODING = NOT_STARTED`
`MECHANISM_CODING = NOT_STARTED`
`ROTEM_CODING_CONSULTED = NO`
`R4_3 = NOT_STARTED`
`CORPUS_WIDE_REPAIR = NOT_EXECUTED`

No corpus record was repaired. `R4_STRUCTURAL_EXTRACTION.csv` was read only and is unmodified.
No Git operation was performed.
