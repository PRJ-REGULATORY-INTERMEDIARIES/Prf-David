# R4.2E-B1 — Advanced structural validation method report

**Status:** `R4_2E_B1_ADVANCED_VALIDATION_COMPLETE_PENDING_REPAIR_DECISION`
**Cases reconciled:** 143 / 143
**Corpus repair:** `CORPUS_WIDE_REPAIR = NOT_EXECUTED`

## 1. Purpose and position in the pipeline

R4.2E-B1 is the advanced-model validation stage of the R4 digital structural extraction. It does not
code regulator, intermediary or target roles, and it does not code mechanisms. It asks a narrower
question: does the frozen structural extraction correctly represent the legal proposition it claims
to represent, and can the defects be repaired by a small number of falsifiable templates rather than
by 1,404 individual human judgements.

## 2. Case set

B0 compressed 1,404 structural records into 211 repair families and reduced the advanced-review
workload from 524 to 131 cases. B1 added 12 hidden NO_REPAIR controls, giving 143 cases:

| Component | Count |
| --- | --- |
| Family representatives | 99 |
| Individual advanced cases | 32 |
| Hidden NO_REPAIR controls | 12 |
| **Total** | **143** |

Reconciliation across the four frozen batch outputs returns exactly these counts.

## 3. Batches, provenance and integrity

| Batch | Cases | Reviewing model | Authoritative output SHA-256 |
| --- | --- | --- | --- |
| B1-01 | 36 | GPT-5.6 Terra High | `1D03CD4514CF08D80963985470DDF4B509AA30049C69F2C58C302FC03415D4EC` |
| B1-02 | 36 | GPT-5.6 Terra High | `CDC843471CDD0A20D5838936D3F106740CDE203B42F3BCCCE4D1C04CED9F7D3C` |
| B1-03 | 36 | GPT-5.6 Terra High | `FA82AAC4924FA82C1BC0BF8F181D734C73F61A3E1B9B24C1F35CDE552F6E497F` |
| B1-04 | 35 | Claude Opus 5.5 Extra High (researcher-selected; runtime reported Claude Opus 5) | `253D80E305A21444343B5A5893AC5A4871FB415E561BA802E957CE94435A5BD1` |

B1-01 also has a preserved schema-defective first export,
SHA-256 `5CD40A975BCF642DE4941BA8F7FC28877BFB6BC4F2309CFC0EA9C94AEA66F4E0`, retained as historical
provenance only.

B1-04 was executed in Claude Code after Codex/Terra reached its usage limit. No earlier batch was
rerun, reopened or relabelled. Per-row model provenance is carried in every output file.

## 4. Combined results across 143 cases

### Defect decisions

| Value | Count |
| --- | --- |
| YES | 111 |
| PARTIALLY | 15 |
| NO | 17 |
| ABSTAIN | 0 |

### Proposition anchor confidence

| Value | Count |
| --- | --- |
| HIGH | 124 |
| MEDIUM | 12 |
| LOW | 7 |

### Field corrections (`*_CORRECT = NO`)

| Field | Corrections |
| --- | --- |
| Actor | 47 |
| Action | 87 |
| Object | 83 |
| Counterpart | 88 |
| Recipient | 98 |

### Relational field differentiation

| Value | Count |
| --- | --- |
| NEITHER | 95 |
| RECIPIENT_ONLY | 27 |
| COUNTERPART_ONLY | 14 |
| UNCERTAIN | 7 |
| BOTH_SAME_ENTITY_JUSTIFIED | 0 |
| DIFFERENT_ENTITIES | 0 |

### Family template status (99 family representatives)

| Value | Count |
| --- | --- |
| VALIDATED_WITH_CONDITIONS | 64 |
| REQUIRES_MORE_REPRESENTATIVES | 16 |
| HUMAN_REVIEW_REQUIRED | 9 |
| REJECTED | 8 |
| N/A | 2 |
| VALIDATED | 0 |

No template reached unconditional `VALIDATED`.

### Individual advanced case routes (32 cases)

| Value | Count |
| --- | --- |
| HUMAN_ADJUDICATION_REQUIRED | 16 |
| MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA | 11 |
| NO_REPAIR | 2 |
| N/A | 3 |

## 5. Potential template repair coverage

Counting only families whose reviewed representatives are all `VALIDATED` or
`VALIDATED_WITH_CONDITIONS`:

| Metric | Value |
| --- | --- |
| Families with at least one reviewed representative | 83 |
| Conditionally validated repair families | 50 |
| Families with disagreeing representatives | 6 |
| `POTENTIAL_TEMPLATE_REPAIR_COVERAGE` | 296 corpus records |
| Records in mixed-status families (excluded) | 141 |

**Terminology.** All 50 qualifying families qualify solely on `VALIDATED_WITH_CONDITIONS`
representatives; recomputation confirms that not one rests on an unconditional `VALIDATED`
decision, of which there are zero corpus-wide. They are therefore described as *conditionally
validated repair families*. Earlier wording in this project that called them "fully validated" was
inaccurate and is corrected here. The 296 figure is unchanged on recomputation.

This is a descriptive eligibility ceiling, not an applied repair. No template was executed against
the corpus.

## 6. The 12-control diagnostic

**Designation.** These twelve records are `NO_REPAIR` **diagnostic controls**. They must no longer
be described as *blind controls*. They were selected before review as NO_REPAIR diagnostic probes,
but the implementation did not guarantee reviewer blinding. They therefore provide diagnostic
evidence about compression coverage rather than a blinded estimate of false-negative performance.
No formal false-negative rate is reported from them, here or anywhere downstream.

All twelve are now unblinded. Each was frozen before revelation, and no individual control
adjudication is changed by this redesignation.

| Result | Count |
| --- | --- |
| CLEAN_CONFIRMED | 5 |
| DEFECT_FOUND | 7 |
| PARTIAL_DEFECT | 0 |
| ABSTAIN | 0 |

| Record | Batch | Model | Type | Severity |
| --- | --- | --- | --- | --- |
| EXT-000085 | B1-01 | Terra | not classified at time of unblinding | LOCAL |
| EXT-000919 | B1-02 | Terra | not classified at time of unblinding | not classified |
| EXT-000163 | B1-03 | Terra | PREDICATE_RECONSTRUCTION_ERROR | MODERATE |
| EXT-000660 | B1-03 | Terra | RELATIONAL_FIELD_ERROR | MODERATE |
| EXT-000093 | B1-04 | Claude Opus 5.5 Extra High | PREDICATE_RECONSTRUCTION_ERROR | MODERATE |
| EXT-000777 | B1-04 | Claude Opus 5.5 Extra High | CROSS_SENTENCE_CONTAMINATION | MODERATE |
| EXT-000937 | B1-04 | Claude Opus 5.5 Extra High | PREDICATE_RECONSTRUCTION_ERROR | MODERATE |

No control was classified SERIOUS. The defect-type and severity taxonomy was introduced for the
B1-03 unblinding, so the two earlier defective controls carry no formal codes and were not
retro-adjudicated.

These controls are a purposive diagnostic device. No accuracy, sensitivity, specificity,
false-negative rate or corpus-wide error rate is computed from them.

## 7. `B0_COMPRESSION_SAFETY` decision

**`B0_COMPRESSION_SAFETY = B0_COMPRESSION_REASSESSMENT_REQUIRED`**

The decision does not rest on the count alone.

Supporting the reassessment:

- Seven of twelve controls drawn from the `NO_REPAIR` route contain structural defects. The route
  asserts that no repair is needed; for the majority of its sampled members that assertion did not
  hold.
- The same failure type recurs across batches and across both reviewing models.
  `PREDICATE_RECONSTRUCTION_ERROR` appears three times; contamination across a sentence or
  proposition boundary appears in at least three further controls.
- Within-family heterogeneity is demonstrated, which is the specific assumption compression relies
  on. Family `RF-098E1C096964` contributed three controls: two CLEAN_CONFIRMED and one
  DEFECT_FOUND. Family `RF-4EAB0DF25480` contributed two controls and both were defective. Among
  family representatives, six families returned disagreeing representative verdicts, covering 141
  corpus records.

Limiting the severity of the finding:

- No control showed a `PROPOSITION_ANCHOR_FAILURE` and none was graded SERIOUS. The anchored legal
  proposition remained identifiable in every defective control.
- No systematic `ACTOR_INVENTION` was observed in any control. Actor fields were truncated or
  mis-spanned, not fabricated.
- Defects are concentrated in span boundaries and in relational-field copying rather than in the
  identification of which provision is being represented.

The conclusion is therefore about coverage and representativeness, not about corpus corruption. The
`NO_REPAIR` route of 698 records cannot be treated as validated-clean on the present evidence, and
one representative per family is not sufficient where representatives disagree. B0 should be
reassessed before any corpus-wide repair is designed. Nothing in this evidence licenses the claim
that a known proportion of the corpus is defective.

## 8. Review-design findings

Three findings concern the validation instrument rather than the corpus.

1. **Hidden-control blinding is structurally leaky after B1-01.**
   `R4_2E_B1_NO_REPAIR_CONTROL_SAMPLE.csv` lists all twelve controls with no batch column. The
   protocol requires reading it to unblind each batch, so any later batch reviewed by an agent that
   has performed a previous unblinding is exposed. This is confirmed for B1-04 and structurally
   possible for B1-02 and B1-03. Recorded as
   `B1_04_CONTROL_BLINDING = COMPROMISED_BY_REQUIRED_SEQUENTIAL_FILE_ACCESS`.

2. **The blind review input under-exposes the extraction schema.** The input presents
   `LEGAL_ACTION` as the action field. The frozen extraction also holds `LEGAL_VERB` and
   `MODALITY`. Corpus-wide, `LEGAL_VERB` contains an explicit modal in 1,370 of 1,404 records while
   `LEGAL_ACTION` contains one in 5. A reviewer working only from the input will judge deontic
   modality to have been lost when it is in fact recorded in a sibling column. Recorded as
   `B1_REVIEW_INPUT_UNDER_EXPOSES_SCHEMA = CONFIRMED`.

3. **Cross-model threshold calibration differs.** B1-04 treats coordinated predicates absorbed into
   the object, and mis-coded `MODALITY` values, as defects. At least one control adjudicated
   CLEAN_CONFIRMED in B1-03 contains a coordinated predicate inside its own proposed object. Batch
   defect proportions are therefore not directly poolable and must not be read as comparative model
   accuracy. Recorded as `CROSS_MODEL_THRESHOLD_CALIBRATION_DIFFERENCE = OBSERVED`.

## 9. Operational redundancies observed in the frozen extraction

Read-only inspection of all 1,404 records, performed without modifying the corpus:

Full detail is in `08_reports/R4_VARIABLE_REDUNDANCY_AUDIT.csv`, which recomputes every figure at
run time.

| Pair | Observation | Exactness |
| --- | --- | --- |
| `COUNTERPART_TEXT` / `RECIPIENT_TEXT` | identical in 1,404/1,404 rows (995 both populated, 409 both empty); counterpart-only 0; recipient-only 0 | exact textual equality |
| `ACTION_OBJECT` / `INFORMATION_OR_MATERIAL_OBJECT` | identical in 1,404/1,404 rows (1,394 both populated, 10 both empty); neither ever populated alone | exact textual equality |
| `STRUCTURAL_AMBIGUITY` / `EXTRACTION_CONFIDENCE` | `LOW` ↔ `YES` exactly, but `NO` splits into `HIGH` (263) and `MEDIUM` (139) | deterministic one-way transformation |
| `LEGAL_ACTION` / `LEGAL_VERB` | never identical (0/1,404); `LEGAL_ACTION` is a substring of `LEGAL_VERB` in only 991/1,404 | complementary, not redundant |
| `MODALITY` / `LEGAL_VERB` | `LEGAL_VERB` carries an explicit modal in 1,370/1,404 | partial functional overlap |

**Correction to an earlier statement.** The third pair was previously described in this project as
"perfectly coextensive", implying mutual redundancy. That was wrong in one direction.
`EXTRACTION_CONFIDENCE` fully determines `STRUCTURAL_AMBIGUITY` by the rule `LOW → YES`, otherwise
`NO`; the reverse does not hold, because `AMBIGUITY = NO` covers both `HIGH` and `MEDIUM`.
`STRUCTURAL_AMBIGUITY` is therefore derivable and droppable; `EXTRACTION_CONFIDENCE` is not.

Each observation is an operational property of the current extraction. None establishes theoretical
equivalence and no field was merged or deleted.

Advanced review nevertheless returned 27 `RECIPIENT_ONLY` and 14 `COUNTERPART_ONLY` adjudications,
and zero `BOTH_SAME_ENTITY_JUSTIFIED`, so the counterpart and recipient positions are separable in
at least some legal propositions even though the extraction never separated them. The two object
fields, by contrast, produced no reviewed case in which the distinction was realised, which is why
only that pair is marked a strong redundancy candidate.

`EXTRACTION_CONFIDENCE` did not separate defective from non-defective records within the B1 review
set: of the 25 reviewed cases rated `HIGH`, advanced review returned 18 YES and 5 PARTIALLY against
2 NO. Because the B1 set was deliberately enriched for suspected defects, this is **not** a
validated predictive-performance result and cannot be used to estimate corpus accuracy. The
defensible statement is only that the flag did not reliably separate the two classes within this
enriched set, and so cannot be used to decide what to skip.

## 10. New structural diagnostic candidates

Recorded in `R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv`. The fifteen frozen R4.2D rules were
not modified.

## 11. R4.2E-B1S — Action representation sensitivity audit

**Status:** `R4_2E_B1_ACTION_SENSITIVITY_AUDIT_COMPLETE`
**Audit provenance:** `EXECUTION_ENVIRONMENT = Claude Code / VS Code extension`;
`RESEARCHER_SELECTED_MODEL = Claude Opus 5.5 Extra High`;
`RUNTIME_REPORTED_MODEL = Claude Opus 5`; `RUNTIME_MODEL_ID = claude-opus-5`;
`MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE`. The runtime did not verify the researcher
selection and the two labels are not asserted to be equivalent. This audit is distinct from Terra
B1-01 to B1-03 and from Claude B1-04, and it relabels none of them.

### Why it was run

The B1 blind review input presented `ORIGINAL_ACTION` populated from `LEGAL_ACTION` alone. The
frozen extraction also holds `LEGAL_VERB` and `MODALITY`, which the input did not show. Verified
deterministically: an explicit modal appears in `LEGAL_VERB` in **1,370 of 1,404** records and in
`LEGAL_ACTION` in **5 of 1,404**. `LEGAL_VERB` and `LEGAL_ACTION` are never identical, and
`LEGAL_ACTION` is not even a substring of `LEGAL_VERB` in 413 records, confirming that
`LEGAL_ACTION` is a controlled-vocabulary label rather than a source span.

### Scope and rule

All 143 cases; the Action judgment only. Actor, Object, Counterpart and Recipient were not
re-adjudicated. For each case the question was solely whether the composite
`LEGAL_ACTION` + `LEGAL_VERB` + `MODALITY` preserves, for the anchored proposition, the lexical
legal verb, the modality, the deontic construction and the predicate. Over-extension of
`LEGAL_VERB` into object or recipient material was treated as a span matter belonging to the
Object judgment and was not counted against the Action judgment.

### Results

| Outcome | Count |
| --- | --- |
| `B1_ACTION_JUDGMENT_STABLE` | 66 |
| `B1_ACTION_JUDGMENT_CHANGES` | 26 |
| `B1_ACTION_JUDGMENT_PARTIALLY_CHANGES` | 16 |
| `ACTION_REPRESENTATION_NOT_MATERIAL` | 35 |
| `UNCERTAIN_REQUIRES_HUMAN` | 0 |

| Metric | Value |
| --- | --- |
| `ORIGINAL_B1_ACTION_CORRECTION_COUNT` | **87** (historical, not overwritten) |
| `SENSITIVITY_ADJUSTED_ACTION_CORRECTION_COUNT` | **63** (descriptive recount) |
| Decisions changed | 26 (25 NO→YES, 1 YES→NO) |
| Terra B1-01..03 | 57 → 33 |
| Claude B1-04 | 30 → 30 (unchanged) |

B1-04 is unaffected because it was scored against `LEGAL_VERB` and `MODALITY` at review time.

The single reverse flip is EXT-000220: the reviewer recorded `ACTION_CORRECT = YES` while proposing
"shall have the right to lodge", although `LEGAL_VERB` lacks "shall" and `MODALITY` is `UNCLEAR` —
the same pattern the reviewer marked defective in EXT-000019, EXT-000025 and EXT-000341. Full
representation exposes an internal inconsistency rather than a representational artefact.

### Effect on overall defect decisions

`DEFECT_DECISION_STABLE` = **142 / 143**.
`DEFECT_DECISION_POTENTIALLY_AFFECTED` = **1 / 143** — EXT-000840 only, where Action was the sole
basis for a `PARTIALLY` decision and the reviewer note states explicitly that "the source modal is
lost" when `LEGAL_VERB` shows it was not. In the other 24 flipped cases the record was defective on
other fields as well, so the defect decision stands.

Sensitivity-adjusted defect counts, reported **separately** from the frozen historical counts and
not replacing them:

| | Historical (frozen) | Sensitivity-adjusted (descriptive) |
| --- | --- | --- |
| YES | 111 | 111 |
| PARTIALLY | 15 | 14 |
| NO | 17 | 18 |

### What survives the audit

Two Action-related defect classes are confirmed as real rather than representational:

- **Entitlement constructions.** `LEGAL_VERB` records "have the right to …" without "shall", with
  `MODALITY = UNCLEAR`. The deontic construction is genuinely incomplete in both action fields.
- **Coordinated predicates.** Where a provision imposes two obligations, the second is frequently
  absent from `LEGAL_VERB` and buried in the object.

### Effect on the B0 gate

`B0_COMPRESSION_SAFETY = B0_COMPRESSION_REASSESSMENT_REQUIRED` is **preserved**, and
`B0_COMPRESSION_SAFETY_REQUIRES_REINTERPRETATION_AFTER_ACTION_AUDIT` is **not** invoked.

Checked directly against all seven defective controls: not one was defective on Action grounds
alone, and not one has its Action judgment flip under the full representation.

| Control | Action original → full | Other defective fields |
| --- | --- | --- |
| EXT-000085 | NO → NO | Object, Counterpart, Recipient |
| EXT-000919 | YES → YES | Counterpart, Recipient |
| EXT-000163 | NO → NO | Counterpart, Recipient |
| EXT-000660 | YES → YES | Object, Counterpart, Recipient |
| EXT-000093 | NO → NO | Object |
| EXT-000777 | NO → NO | Object |
| EXT-000937 | NO → NO | Object, Counterpart, Recipient |

Two of the seven were never Action-based at all. The original rationale — recurrent defect classes,
seven defective controls out of twelve, and six families whose representatives disagree — is
therefore unaffected by the Action representation issue.

Only 2 of the 64 conditionally validated templates invoke modality restoration in their text, and
both originate in B1-04, which already used the full representation. The template set is therefore
not premised on the artefact.

### Outputs

`R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv` — all 143 cases
`R4_2E_B1_ACTION_SENSITIVITY_SUMMARY.csv` — aggregate metrics
`08_reports/R4_VARIABLE_REDUNDANCY_AUDIT.csv` — the five variable pairs

## 12. Firewalls

`RIT_CODING = NOT_STARTED`
`MECHANISM_CODING = NOT_STARTED`
`ROTEM_CODING_CONSULTED = NO`
`R4_3 = NOT_STARTED`
`CORPUS_WIDE_REPAIR = NOT_EXECUTED`
