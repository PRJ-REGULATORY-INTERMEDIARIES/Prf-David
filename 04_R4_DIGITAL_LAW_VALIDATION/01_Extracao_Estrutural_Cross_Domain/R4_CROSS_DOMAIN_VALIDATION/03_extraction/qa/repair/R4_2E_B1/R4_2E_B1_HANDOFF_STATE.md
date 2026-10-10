# R4.2E-B1 handoff state

**Status:** `R4_2E_B1_ADVANCED_VALIDATION_COMPLETE_PENDING_REPAIR_DECISION`
**Sensitivity audit:** `R4_2E_B1_ACTION_SENSITIVITY_AUDIT_COMPLETE`
**David-facing package:** `R4_DIGITAL_STRUCTURAL_VALIDATION_READY_FOR_DAVID`

All 143 B1 cases are reviewed, frozen and reconciled. All 12 hidden controls are unblinded.
No corpus repair was applied.

## Provenance by batch

| Batch | Cases | Model | Environment | Output SHA-256 |
| --- | --- | --- | --- | --- |
| B1-01 | 36 | GPT-5.6 Terra High | OpenAI Codex | `1D03CD4514CF08D80963985470DDF4B509AA30049C69F2C58C302FC03415D4EC` |
| B1-02 | 36 | GPT-5.6 Terra High | OpenAI Codex | `CDC843471CDD0A20D5838936D3F106740CDE203B42F3BCCCE4D1C04CED9F7D3C` |
| B1-03 | 36 | GPT-5.6 Terra High | OpenAI Codex | `FA82AAC4924FA82C1BC0BF8F181D734C73F61A3E1B9B24C1F35CDE552F6E497F` |
| B1-04 | 35 | Claude Opus 5.5 Extra High (researcher-selected) | Claude Code / VS Code extension | `253D80E305A21444343B5A5893AC5A4871FB415E561BA802E957CE94435A5BD1` |

`MODEL_RUNTIME_VARIANT` for the Terra batches remains `MODEL_VARIANT_NOT_EXPOSED`. No Terra row was
relabelled as Claude and no Claude row was relabelled as Terra.

**Claude provenance, corrected and final.** The researcher selected `Claude Opus 5.5 Extra High` in
the VS Code Claude agent UI; the execution environment reported `Claude Opus 5`, id
`claude-opus-5`. The relationship cannot be independently verified, so:
`EXECUTION_ENVIRONMENT = Claude Code / VS Code extension`;
`RESEARCHER_SELECTED_MODEL = Claude Opus 5.5 Extra High`;
`RUNTIME_REPORTED_MODEL = Claude Opus 5`; `RUNTIME_MODEL_ID = claude-opus-5`;
`MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE`. The runtime did not verify the researcher
selection and the two labels are not asserted to be equivalent. The correction rewrote only the
provenance columns of the Claude artifacts; re-verification confirmed zero differences in every
other cell. Pre-correction versions are preserved as
`R4_2E_B1_ADVANCED_VALIDATION_B1_04_v1_PROVENANCE_SUPERSEDED.csv`
(SHA-256 `8651E54BB033FC5F2AD5C2594F2B355FFCA6189777FF436E11C73574545E2D22`) and
`R4_2E_B1_ACTION_SENSITIVITY_AUDIT_v1_PROVENANCE_SUPERSEDED.csv`
(SHA-256 `9F00B47BF7217E38697F48E36ABB3AC5B0ADD442AF0E5CE8F0653BBDB5D2184B`).

B1-01 v1 is preserved as `SCHEMA_DEFECTIVE_PRESERVED`,
SHA-256 `5CD40A975BCF642DE4941BA8F7FC28877BFB6BC4F2309CFC0EA9C94AEA66F4E0`. It is historical
provenance only; v2 is authoritative.

## Completed

- B1-01, B1-02, B1-03 completed by Terra and not rerun, reopened or modified in this continuation.
- B1-03 controls unblinded after its freeze: EXT-000163 DEFECT_FOUND
  (PREDICATE_RECONSTRUCTION_ERROR, MODERATE); EXT-000660 DEFECT_FOUND (RELATIONAL_FIELD_ERROR,
  MODERATE); EXT-000986 CLEAN_CONFIRMED. Results file SHA-256
  `8DBEA6968A834B7B07543146BDEF7D776E688D9B80E3E64F745977577EED3439`.
- B1-04 completed in Claude Code: 35 cases, 33-column v2 schema, all ID and schema gates passed.
- B1-04 controls unblinded after its freeze: EXT-000093, EXT-000777 and EXT-000937 all
  DEFECT_FOUND, all MODERATE. Results file SHA-256
  `E0494AA69C004A36EC4586CB6BE312737236A89BD747925C0A28DA32D4EF1D02`.
- 143/143 reconciled: 99 family representatives, 32 individual advanced cases, 12 controls.
- Consolidated outputs: `R4_2E_B1_FINAL_SUMMARY.csv`,
  `R4_2E_B1_CONTROL_DIAGNOSTIC_CONSOLIDATED.csv`,
  `R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv`, `R4_2E_B1_METHOD_REPORT.md`.

## Combined results (143 cases)

- Defects: YES 111, PARTIALLY 15, NO 17, ABSTAIN 0.
- Anchor confidence: HIGH 124, MEDIUM 12, LOW 7.
- Field corrections: Actor 47, Action 87, Object 83, Counterpart 88, Recipient 98.
- Relational differentiation: NEITHER 95, RECIPIENT_ONLY 27, COUNTERPART_ONLY 14, UNCERTAIN 7,
  BOTH_SAME_ENTITY_JUSTIFIED 0, DIFFERENT_ENTITIES 0.
- Family templates (99 representatives): VALIDATED_WITH_CONDITIONS 64,
  REQUIRES_MORE_REPRESENTATIVES 16, HUMAN_REVIEW_REQUIRED 9, REJECTED 8, N/A 2, VALIDATED 0.
- Individual routes (32): HUMAN_ADJUDICATION_REQUIRED 16,
  MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA 11, NO_REPAIR 2, N/A 3.
- `POTENTIAL_TEMPLATE_REPAIR_COVERAGE` = 296 corpus records across **50 conditionally validated
  repair families**. Recomputation confirms none rests on an unconditional `VALIDATED` decision,
  of which there are zero; earlier "fully validated" wording was inaccurate and is corrected.
  141 further records sit in 6 families whose representatives disagree and are excluded.

## Action representation sensitivity audit (R4.2E-B1S)

Audit provenance as above; `MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE`. Corrected audit
SHA-256 `74CABE78A77DC47728C17FAAC7BCA24C54E26FB492DD74ED0B39681A73CC6604`.

Verified deterministically: explicit modal in `LEGAL_VERB` 1,370/1,404; in `LEGAL_ACTION` 5/1,404;
the two fields are never identical and `LEGAL_ACTION` is not a substring of `LEGAL_VERB` in 413
records.

- `ORIGINAL_B1_ACTION_CORRECTION_COUNT` = **87** (historical, not overwritten).
- `SENSITIVITY_ADJUSTED_ACTION_CORRECTION_COUNT` = **63** (descriptive).
- Decisions changed: 26 (25 NO→YES, 1 YES→NO, the latter EXT-000220).
- Outcomes: STABLE 66, CHANGES 26, PARTIALLY_CHANGES 16, NOT_MATERIAL 35, UNCERTAIN 0.
- `DEFECT_DECISION_STABLE` = 142/143; `DEFECT_DECISION_POTENTIALLY_AFFECTED` = 1 (EXT-000840).
- Terra 57 → 33; Claude B1-04 30 → 30 (already used the full representation).
- Presented only as `POST_HOC_ACTION_REPRESENTATION_SENSITIVITY_RESULT`; the frozen historical B1 counts are not overwritten.
- Confirmed real, not representational: entitlement constructions missing "shall" with
  `MODALITY = UNCLEAR`, and coordinated predicates buried in the object.

No frozen batch output was modified. Outputs: `R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv`,
`R4_2E_B1_ACTION_SENSITIVITY_SUMMARY.csv`.

## Control diagnostic (12/12)

Designation corrected: these are **NO_REPAIR diagnostic controls**, not blind controls. They were
selected before review as NO_REPAIR diagnostic probes, but the implementation did not guarantee
reviewer blinding. They provide diagnostic evidence about compression coverage rather than a
blinded estimate of false-negative performance. No false-negative rate is reported. Individual
adjudications are unchanged.

CLEAN_CONFIRMED 5, DEFECT_FOUND 7, PARTIAL_DEFECT 0, ABSTAIN 0, SERIOUS 0.

Defective controls: EXT-000085 (B1-01, LOCAL), EXT-000919 (B1-02, not classified),
EXT-000163 and EXT-000660 (B1-03, MODERATE), EXT-000093, EXT-000777 and EXT-000937
(B1-04, MODERATE).

## B0 compression safety

`B0_COMPRESSION_SAFETY = B0_COMPRESSION_REASSESSMENT_REQUIRED`

Rationale is in section 7 of `R4_2E_B1_METHOD_REPORT.md`. In short: seven of twelve controls drawn
from the `NO_REPAIR` route are defective, the same failure types recur across batches and both
models, and six families returned disagreeing representatives, which is the assumption compression
depends on. No control was SERIOUS, none showed proposition-anchor failure and none showed actor
invention, so the finding concerns coverage and representativeness rather than corpus corruption.

## Review-design limitations recorded

- `B1_04_CONTROL_BLINDING = COMPROMISED_BY_REQUIRED_SEQUENTIAL_FILE_ACCESS` — the control sample
  file lists all twelve controls with no batch column, so unblinding B1-03 necessarily disclosed
  the B1-04 controls. Structurally possible for B1-02 and B1-03 too; not verifiable from the
  repository.
- `B1_REVIEW_INPUT_UNDER_EXPOSES_SCHEMA = CONFIRMED` — the blind input shows `LEGAL_ACTION` only,
  hiding `LEGAL_VERB` and `MODALITY`. `LEGAL_VERB` carries an explicit modal in 1,370 of 1,404
  records; `LEGAL_ACTION` in 5.
- `CROSS_MODEL_THRESHOLD_CALIBRATION_DIFFERENCE = OBSERVED` — batch defect proportions are not
  directly poolable and must not be read as comparative model accuracy.

## Unresolved scientific questions

1. Reassess B0 compression before designing any corpus-wide repair.
2. Resolve the 6 families whose representatives disagree (141 corpus records) with additional
   representatives.
3. Adjudicate the 9 `HUMAN_REVIEW_REQUIRED` and 16 `REQUIRES_MORE_REPRESENTATIVES` family templates,
   and the 16 individual cases routed to `HUMAN_ADJUDICATION_REQUIRED`.
4. Decide the passive-with-explicit-by-agent coding convention before any passive construction is
   repaired.
5. Review the `MODALITY` enum for absence-of-obligation and for conditional over-assignment.
6. Audit the 181 corpus records with an empty `SOURCE_EXCERPT`.
7. The 185 `HUMAN_ONLY` cases remain untouched; their burden is still reserved.

## Firewalls and limits

- `RIT_CODING = NOT_STARTED`
- `MECHANISM_CODING = NOT_STARTED`
- `ROTEM_CODING_CONSULTED = NO`
- `R4_3 = NOT_STARTED`
- `CORPUS_WIDE_REPAIR = NOT_EXECUTED`

No corpus record was repaired. `R4_STRUCTURAL_EXTRACTION.csv` was read only and is unmodified. No
Git operation was performed in this continuation; the researcher reviews before versioning.
