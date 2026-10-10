# R4 Digital Structural Validation — final freeze record

**Freeze ID:** `R4_DIGITAL_STRUCTURAL_VALIDATION_FREEZE_001`

**Final scientific status:**
`R4_2E_B1_ACTION_SENSITIVITY_AUDIT_COMPLETE`
`R4_DIGITAL_STRUCTURAL_VALIDATION_READY_FOR_DAVID`

This record freezes the R4 **digital structural validation round**. It is not R4 completion, not
R4.3, and not a Green × Digital governance comparison.

---

## 1. Corpus

Frozen original texts, no consolidated substitution.

| Instrument | CELEX | Structure |
| --- | --- | --- |
| GDPR, Regulation (EU) 2016/679 | 32016R0679 | 99 articles, 173 recitals |
| Digital Services Act, Regulation (EU) 2022/2065 | 32022R2065 | 93 articles, 156 recitals |
| AI Act, Regulation (EU) 2024/1689 | 32024R1689 | 113 articles, 180 recitals, 13 annexes |

## 2. Structural dataset

**1,404 records** on the unit *legal provision × actor × legal action*:
GDPR 485, DSA 424, AI Act 495. By source: operative articles 842, recitals 546, annexes 16 (AI Act
only).

`R4_STRUCTURAL_EXTRACTION.csv` is immutable and was read only throughout. It is unmodified.

## 3. B1 design and completion

B0 compressed the corpus into 211 repair families and reduced advanced review from 524 to 131
cases. B1 added 12 NO_REPAIR diagnostic controls.

| Component | Count |
| --- | --- |
| Family representatives | 99 |
| Individual advanced cases | 32 |
| NO_REPAIR diagnostic controls | 12 |
| **Total** | **143** |

**`TOTAL_B1_CASES = 143`, reconciled 143/143** across the four frozen batch outputs.

## 4. Provenance

### Terra — B1-01, B1-02, B1-03 (unchanged)

`MODEL_REQUESTED = GPT-5.6 Terra High`
`MODEL_RESEARCHER_SELECTED = GPT-5.6 Terra High`
`MODEL_RUNTIME_VARIANT = MODEL_VARIANT_NOT_EXPOSED`
Environment: OpenAI Codex.

### Claude — B1-04 and the B1S sensitivity audit (corrected)

`EXECUTION_ENVIRONMENT = Claude Code / VS Code extension`
`RESEARCHER_SELECTED_MODEL = Claude Opus 5.5 Extra High`
`RUNTIME_REPORTED_MODEL = Claude Opus 5`
`RUNTIME_MODEL_ID = claude-opus-5`
`MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE`

The researcher selected `Claude Opus 5.5 Extra High` in the VS Code Claude agent UI. The execution
environment reported `Claude Opus 5` with identifier `claude-opus-5`. The relationship between the
two labels cannot be independently verified from inside the session. The runtime did **not** verify
`Claude Opus 5.5 Extra High`. The two labels are **not** asserted to be equivalent. Both are
recorded, and the researcher's selection was not replaced by the runtime label.

The correction rewrote **only** provenance columns in the Claude artifacts. Re-verification
confirmed **zero** differences in every other cell, including `RUN_TIMESTAMP`. Pre-correction
exports are preserved as historical provenance. No Terra row was relabelled as Claude and no Claude
row was relabelled as Terra.

## 5. Batch hashes

| Batch | Cases | Model | Authoritative SHA-256 |
| --- | --- | --- | --- |
| B1-01 | 36 | GPT-5.6 Terra High | `1D03CD4514CF08D80963985470DDF4B509AA30049C69F2C58C302FC03415D4EC` |
| B1-02 | 36 | GPT-5.6 Terra High | `CDC843471CDD0A20D5838936D3F106740CDE203B42F3BCCCE4D1C04CED9F7D3C` |
| B1-03 | 36 | GPT-5.6 Terra High | `FA82AAC4924FA82C1BC0BF8F181D734C73F61A3E1B9B24C1F35CDE552F6E497F` |
| B1-04 | 35 | Claude (see section 4) | `253D80E305A21444343B5A5893AC5A4871FB415E561BA802E957CE94435A5BD1` |

Preserved superseded versions, historical provenance only:

- B1-01 v1 schema-defective: `5CD40A975BCF642DE4941BA8F7FC28877BFB6BC4F2309CFC0EA9C94AEA66F4E0`
- B1-04 v1 provenance-superseded: `8651E54BB033FC5F2AD5C2594F2B355FFCA6189777FF436E11C73574545E2D22`
- B1S v1 provenance-superseded: `9F00B47BF7217E38697F48E36ABB3AC5B0ADD442AF0E5CE8F0653BBDB5D2184B`

## 6. Frozen B1 results (historical, not overwritten)

| Defect decision | Count |
| --- | --- |
| YES | 111 |
| PARTIALLY | 15 |
| NO | 17 |
| ABSTAIN | 0 |

Proposition anchor confidence: HIGH 124, MEDIUM 12, LOW 7.
Field corrections (`*_CORRECT = NO`): Actor 47, Action 87, Object 83, Counterpart 88, Recipient 98.

These proportions describe a review set purposively selected to concentrate suspected defects. They
are **not** corpus prevalence.

## 7. B1S post-hoc action representation sensitivity audit

The B1 review input exposed `ORIGINAL_ACTION` from `LEGAL_ACTION` alone, while the frozen
extraction also holds `LEGAL_VERB` and `MODALITY`. Verified deterministically: an explicit modal
appears in `LEGAL_VERB` in **1,370 / 1,404** records and in `LEGAL_ACTION` in **5 / 1,404**; the
two fields are never identical; `LEGAL_ACTION` is not even a substring of `LEGAL_VERB` in 413
records.

Scope: the Action judgment only, across all 143 cases. No case was rerun and no frozen adjudication
was modified.

| Outcome | Count |
| --- | --- |
| `B1_ACTION_JUDGMENT_STABLE` | 66 |
| `B1_ACTION_JUDGMENT_CHANGES` | 26 |
| `B1_ACTION_JUDGMENT_PARTIALLY_CHANGES` | 16 |
| `ACTION_REPRESENTATION_NOT_MATERIAL` | 35 |
| `UNCERTAIN_REQUIRES_HUMAN` | 0 |

`ORIGINAL_B1_ACTION_CORRECTION_COUNT = 87`
`SENSITIVITY_ADJUSTED_ACTION_CORRECTION_COUNT = 63`
Action decisions changed: **26** (25 NO→YES, 1 YES→NO).
Terra 57 → 33. Claude B1-04 30 → 30, already scored against the full representation.

**Overall defect decisions materially affected: 1 / 143** (EXT-000840 only).
`DEFECT_DECISION_STABLE = 142 / 143`.

`POST_HOC_ACTION_REPRESENTATION_SENSITIVITY_RESULT` — descriptive only, presented beside and never
in place of the frozen counts:

| | Frozen historical | Sensitivity-adjusted |
| --- | --- | --- |
| YES | 111 | 111 |
| PARTIALLY | 15 | 14 |
| NO | 17 | 18 |

Two Action defect classes are confirmed **real, not representational**: entitlement constructions
recorded without "shall" and with `MODALITY = UNCLEAR`, and coordinated predicates buried in the
object.

## 8. Variable parsimony findings

| Pair | Overlap | Exactness | Status |
| --- | --- | --- | --- |
| `COUNTERPART_TEXT` / `RECIPIENT_TEXT` | 1,404 / 1,404 | exact textual equality | retain both; repair the population rule |
| `ACTION_OBJECT` / `INFORMATION_OR_MATERIAL_OBJECT` | 1,404 / 1,404 | exact textual equality | `STRONG_REDUNDANCY_CANDIDATE` |
| `STRUCTURAL_AMBIGUITY` / `EXTRACTION_CONFIDENCE` | one-way derivable | deterministic transformation | `DROP_STRUCTURAL_AMBIGUITY_CANDIDATE` |
| `LEGAL_ACTION` / `LEGAL_VERB` | never identical | complementary, not redundant | retain both as structural components |
| `MODALITY` / `LEGAL_VERB` | partial overlap | partial functional overlap | retain pending codebook audit |

**Counterpart / Recipient.** Exact equality across the 1,404 rows as represented in the dataset
(995 both populated, 409 both empty), counterpart-only 0, recipient-only 0. Advanced B1
differentiation: NEITHER 95, RECIPIENT_ONLY 27, COUNTERPART_ONLY 14, UNCERTAIN 7,
BOTH_SAME_ENTITY_JUSTIFIED 0, DIFFERENT_ENTITIES 0. The initial extraction operationally collapsed
the two fields, while advanced legal review demonstrates that they can encode distinct relational
positions. **Automatic merger is not recommended.**

**Structural ambiguity / Extraction confidence.** `CONFIDENCE = LOW` corresponds to
`AMBIGUITY = YES`; `AMBIGUITY = NO` contains HIGH 263 and MEDIUM 139. `STRUCTURAL_AMBIGUITY` is
derivable from `EXTRACTION_CONFIDENCE`, which carries additional information. The fields are **not**
perfectly equivalent.

Within the enriched B1 set, `EXTRACTION_CONFIDENCE` did not separate defective from non-defective
records: of 25 cases rated HIGH, review returned 18 YES and 5 PARTIALLY against 2 NO. This is not a
validated predictive-performance result and cannot estimate corpus accuracy.

## 9. Templates

| Status | Count |
| --- | --- |
| Unconditional `VALIDATED` | **0** |
| `VALIDATED_WITH_CONDITIONS` | 64 |
| `REQUIRES_MORE_REPRESENTATIVES` | 16 |
| `HUMAN_REVIEW_REQUIRED` | 9 |
| `REJECTED` | 8 |
| `N/A` | 2 |

Fifty families qualify on `VALIDATED_WITH_CONDITIONS` representatives alone and are therefore
called **50 conditionally validated repair families**. The term *fully validated families* is
inaccurate and is not used.

`POTENTIAL_TEMPLATE_REPAIR_COVERAGE = 296 records`, confirmed on recomputation. A further 141
records sit in 6 families whose representatives disagree and are excluded. This is an eligibility
ceiling. **No corpus repair is authorized and none was executed.**

## 10. NO_REPAIR diagnostic controls

| Result | Count |
| --- | --- |
| CLEAN_CONFIRMED | 5 |
| DEFECT_FOUND | 7 |
| PARTIAL_DEFECT | 0 |
| ABSTAIN | 0 |
| SERIOUS | 0 |

These are **NO_REPAIR diagnostic controls**, never *blind controls*. They were selected before
review as NO_REPAIR diagnostic probes, but the implementation did not guarantee reviewer blinding:
the control sample file lists all twelve with no batch column, and the protocol requires reading it
to unblind each batch in turn. They therefore provide diagnostic evidence about compression
coverage rather than a blinded estimate of false-negative performance. **No formal false-negative
rate is calculated.**

Defective controls: EXT-000085 (B1-01, LOCAL), EXT-000919 (B1-02, not classified — predates the
taxonomy), EXT-000163 and EXT-000660 (B1-03, MODERATE), EXT-000093, EXT-000777 and EXT-000937
(B1-04, MODERATE).

## 11. B0 compression safety

**`B0_COMPRESSION_SAFETY = B0_COMPRESSION_REASSESSMENT_REQUIRED`** — preserved.

The result concerns **coverage and family representativeness**, not evidence that the corpus is
broadly corrupted. Seven of twelve controls drawn from the `NO_REPAIR` route are defective; the
same failure types recur across batches and both models; and six families returned disagreeing
representatives, which is the assumption compression depends on. Against that, no control was
graded SERIOUS, none showed proposition-anchor failure, and none showed actor invention.

Checked against the B1S audit: not one of the seven defective controls was defective on Action
grounds alone, and not one has its Action judgment flip under the full representation. Two were
never Action-based at all. `B0_COMPRESSION_SAFETY_REQUIRES_REINTERPRETATION_AFTER_ACTION_AUDIT` is
therefore **not** invoked.

## 12. Limitations

1. B1 proportions describe a purposively enriched review set, not corpus prevalence.
2. The controls are diagnostic probes, not a blinded test; no false-negative rate is derived.
3. The B1 review input under-exposed the extraction schema for the Action variable
   (`B1_REVIEW_INPUT_UNDER_EXPOSES_SCHEMA = CONFIRMED`); section 7 quantifies the effect.
4. The two reviewing models applied different thresholds for action and object defects
   (`CROSS_MODEL_THRESHOLD_CALIBRATION_DIFFERENCE = OBSERVED`). Batch defect proportions are not
   directly poolable and no comparative model accuracy is computed.
5. The Claude model selection could not be verified against the runtime
   (`MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE`).
6. 181 of 1,404 corpus records carry an empty `SOURCE_EXCERPT`, a provenance gap not yet audited.
7. Passive constructions with an explicit by-agent have no coding convention in the frozen rule set.
8. The 3 known R4.2E-A heuristic blind spots remain (`R4_2D-QA2B-026`, `-056`, `-089`).
9. The 185 `HUMAN_ONLY` cases remain untouched.

## 13. Scientific firewalls

`RIT_CODING = NOT_STARTED`
`MECHANISM_CODING = NOT_STARTED`
`ROTEM_CODING_CONSULTED = NO`
`R4_3 = NOT_STARTED`
`CORPUS_WIDE_REPAIR = NOT_EXECUTED`

## 14. David-facing outputs

- `08_reports/R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md`
- `08_reports/R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv`
- `08_reports/R4_EMAIL_TO_DAVID_DRAFT.md`
- `08_reports/R4_VARIABLE_REDUNDANCY_AUDIT.csv`

Claim boundaries observed: the package does not state that R4 as a whole is complete, that R/I/T or
mechanism coding is complete, that a Green × Digital governance comparison has been made, that the
controls estimate a population error rate, that 111/143 represents corpus prevalence, that repair
templates are unconditionally validated, that counterpart and recipient are redundant, or that
Rotem's coding has been consulted. The framing throughout is
**R4 DIGITAL STRUCTURAL VALIDATION ROUND**.

## 15. Integrity manifest

See `08_reports/R4_DIGITAL_STRUCTURAL_VALIDATION_MANIFEST.csv` for the SHA-256 manifest of all
final artifacts.
