# R4.2B — Human QA and Structural Extraction Calibration Report

**Date:** 2026-09-26
**Status:** `R4_2B_QA_REQUIRES_HUMAN_REVIEW`
**Original Luna artifact:** preserved and hash-frozen before QA
**R/I/T classification:** not performed
**Mechanism classification:** not performed
**Rotem coding:** not consulted
**Terra escalations:** 0

## 1. Scope

R4.2B prepares and calibrates a human QA of the frozen R4.2 structural extraction. The original `R4_STRUCTURAL_EXTRACTION.csv` was not overwritten. The QA package is separate under `03_extraction/qa/`.

The review scope is limited to whether actor, action, object, counterpart, recipient, source pointer, excerpt and ambiguity flag faithfully represent the frozen legal text. No regulator, intermediary, target, R–I–T or mechanism judgment is permitted.

## 2. Sample design

A deterministic stratified sample of 90 records was created: 30 GDPR, 30 DSA and 30 AI Act. The quotas balance confidence and ambiguity status and include operative articles, recitals and AI Act annexes. Selection rotates across structural-complexity strata: single actor/action, multiple actors, multiple actions, cross-referenced provisions, actor-normalization cases and counterpart/recipient cases where available.

Distribution:

| Dimension | Distribution |
|---|---:|
| GDPR / DSA / AI Act | 30 / 30 / 30 |
| HIGH / MEDIUM / LOW confidence | 36 / 14 / 40 |
| Ambiguous / non-ambiguous | 40 / 50 |
| Operative article / recital / annex | 57 / 30 / 3 |

The sample is stored in `03_extraction/qa/R4_2B_HUMAN_QA_SAMPLE.csv`.

## 3. Human-review procedure

The runtime prepared the sample and performed only mechanical checks: all 90 source pointers matched a structure-index entry; 70 excerpts matched the normalized source exactly; 20 matched after removing the extraction truncation suffix. These checks are not human accuracy judgments.

No human researcher reviewed and signed the sample during this run. Accordingly, actor, action, object, counterpart, recipient, excerpt, ambiguity justification and error-type fields remain `PENDING_HUMAN_REVIEW`. The `HUMAN_REVIEWER` field remains `UNASSIGNED`.

## 4. Overall extraction quality

A human-reviewed accuracy rate cannot be reported yet. The prepared sample contains 90 records, but no record has been marked as fully correct or erroneous by a human reviewer. The required metrics are present as pending fields in `R4_2B_QA_METRICS.csv`.

The mechanical source-pointer check passed for all 90 sampled rows. This does not establish actor/action accuracy.

## 5. Quality by case

Each case has 30 sampled records. Case-level accuracy, field error rates and fully-correct counts remain pending human source review. The original extraction totals remain 485 GDPR rows, 424 DSA rows and 495 AI Act rows.

## 6. Quality by confidence level

The sample contains 36 HIGH, 14 MEDIUM and 40 LOW-confidence records. `R4_2B_CONFIDENCE_CALIBRATION.csv` records the counts and leaves correctness/error rates pending. No conclusion about under-confidence, appropriate caution or over-confidence is justified before human review.

## 7. Quality by source type

The sample contains 57 operative-article records, 30 recital records and 3 AI Act annex records. Source-type accuracy remains pending human review. Recitals and annexes remain structurally distinct from operative provisions.

## 8. Ambiguity analysis

All 1,002 original ambiguity records were typed without theoretical adjudication. The typology is in `03_extraction/qa/R4_2B_AMBIGUITY_TYPOLOGY.csv`.

| Ambiguity type | Count |
|---|---:|
| `ACTION_OBJECT_AMBIGUITY` | 307 |
| `CROSS_REFERENCE_AMBIGUITY` | 208 |
| `MULTI_ACTOR_PROVISION` | 149 |
| `MULTI_ACTION_PROVISION` | 148 |
| `COUNTERPART_AMBIGUITY` | 99 |
| `PRONOUN_REFERENCE_AMBIGUITY` | 59 |
| `ACTION_SCOPE_AMBIGUITY` | 32 |
| **Total** | **1,002** |

The provisional typology classifies all 1,002 as primarily `STRUCTURAL` and none as `INTERPRETIVE`. This describes the source of the original flags; it is not a human finding that every ambiguity is correctly flagged. No Terra run was performed.

## 9. Error taxonomy

No human error classification has been made. The correction register is intentionally empty rather than populated by inference. The allowed error taxonomy is available for the researcher to apply during review.

## 10. Systematic issues

Two provisional recurring patterns require human review:

1. `CONFIDENCE_AMBIGUITY_COUPLING`: all 1,002 ambiguity flags are paired with LOW confidence by the original extraction logic. This may reflect conservative flagging rather than extraction failure.
2. `TRUNCATED_SOURCE_EXCERPT`: 376 of 1,404 original rows were limited by the extraction excerpt-length rule. The original Luna artifact must remain unchanged; human QA should determine whether the truncated wording is adequate and whether a validated copy needs full-sentence excerpts.

These patterns are recorded in `03_extraction/qa/R4_2B_SYSTEMATIC_ERROR_AUDIT.csv` and are not silently propagated as corrections.

## 11. Corrections proposed

No corrections are accepted or proposed from human review because human review has not occurred. `R4_2B_EXTRACTION_CORRECTION_REGISTER.csv` is empty by design. No `R4_STRUCTURAL_EXTRACTION_QA_VALIDATED.csv` was created.

## 12. Limitations

This package is a QA preparation and AI-assisted pre-review artifact, not a completed human validation. The runtime cannot supply the researcher’s authoritative judgment. Mechanical pointer/excerpt checks do not establish semantic extraction accuracy. The underlying Luna/Terra variant remains unexposed by the runtime.

## 13. Implications for model-sensitivity test

The dataset is not yet ready for a controlled Luna × Terra sensitivity test. Human review must first determine whether the ambiguity flags and excerpt truncation pattern represent acceptable conservative behavior or a repairable extraction defect. Terra remains unused and must not be introduced as a replacement coder at this stage.

## 14. Readiness for R4.2C

`R4_2C = NOT_READY_PENDING_HUMAN_QA`

The next gate requires researcher review of the 90-record sample, error classification, confirmation of the ambiguity typology and a decision on whether a separate QA-validated extraction copy is warranted.

## Key questions

- Q1–Q3: human accuracy and field-level reliability cannot yet be claimed; metrics remain pending.
- Q4: the provisional typology is entirely structural, but human confirmation is required.
- Q5: confidence calibration is not yet determined.
- Q6: two recurring patterns require review: confidence/ambiguity coupling and truncated excerpts.
- Q7: readiness for Luna × Terra comparison is not established; human QA is the blocking gate.

## Completion status

`R4_2B_QA_REQUIRES_HUMAN_REVIEW`

Stop here. Do not begin R4.2C or R4.3.
