# R4.2E-B1 — Partial advanced structural validation report

**Scientific status:** R4_2E_B1_PARTIAL_ADVANCED_VALIDATION_COMPLETE  
**Completed batch:** B1-01 (36 of 143 records)  
**Requested/selected model:** GPT-5.6 Terra High  
**Runtime model variant:** MODEL_VARIANT_NOT_EXPOSED

## Evidence separation

- R4.2D remains a purposive human diagnostic, not a corpus error rate.
- R4.2E-A remains deterministic triage.
- R4.2E-B0 remains family/workload compression.
- This file reports only the first completed B1 advanced-validation batch; it does not combine those layers into accuracy or prevalence.

## B1-01 results

- Composition: 25 template representatives; 8 individual advanced cases; 3 hidden NO_REPAIR controls.
- Defect decisions: NO=5; PARTIALLY=6; YES=25.
- Proposition-anchor confidence: HIGH=30; LOW=1; MEDIUM=5.
- Template statuses in this partial batch: HUMAN_REVIEW_REQUIRED=3; REJECTED=3; REQUIRES_MORE_REPRESENTATIVES=5; VALIDATED_WITH_CONDITIONS=14.
- Batch output SHA-256: $hash.

The three controls were unblinded only after B1-01 decisions were written. Two were CLEAN_CONFIRMED; EXT-000085 was DEFECT_FOUND, reflecting a local source-proposition error. This is one control observation and does not permit a B0 compression-safety conclusion; nine controls remain pending.

No corpus-wide repair was applied. No R/I/T or mechanism coding occurred; Rotem was not consulted. The remaining three batches must preserve their frozen manifests and be reviewed before any global template-coverage or compression-safety assessment.