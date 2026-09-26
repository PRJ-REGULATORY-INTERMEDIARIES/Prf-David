# R4.2C-R — Model provenance correction

## Researcher decision

- RESEARCHER_MODEL_CORRECTION = CONFIRMED
- PREVIOUS_R4_2C_REQUESTED_MODEL = GPT-5.6_TERRA_HIGH
- PREVIOUS_R4_2C_ACTUAL_USER_SELECTED_MODEL = GPT-5.6_LUNA_HIGH
- PREVIOUS_R4_2C_RUNTIME_VARIANT = MODEL_VARIANT_NOT_EXPOSED
- PROVENANCE_ERROR_TYPE = MODEL_SELECTION_MISMATCH
- CORRECTION_DATE = 2026-09-26

The researcher's direct statement is authoritative for the previously selected model. Runtime telemetry did not independently expose the model variant.

## Consequence

The historical file named R4_2C_TERRA_CALIBRATED_REVIEW.csv is preserved without change but is analytically reclassified as LUNA_CALIBRATED_SELF_REVIEW. Its 87-record results are diagnostic self-review evidence, not independent Terra findings. The prior systematic-defect conclusions are therefore downgraded to Luna self-review defect hypotheses pending this V2 independent review.

## Corrective action

This rerun uses the unchanged three-case human seed and unchanged 87-record set. It prepares a blind input that excludes prior self-review decisions and original Luna confidence/ambiguity metadata. The new V2 output is frozen before model comparison.
