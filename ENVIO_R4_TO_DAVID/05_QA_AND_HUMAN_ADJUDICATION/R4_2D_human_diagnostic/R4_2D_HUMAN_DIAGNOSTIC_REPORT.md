# R4.2D — Human diagnostic report

**Status:** `R4_2D_HUMAN_DIAGNOSTIC_COMPLETE_REPAIR_RULES_PENDING`  
**Reviewer:** Igor Caires Machado  
**Human decisions:** 12/12 `REVIEWED`; 0 pending.  
**Scope:** purposive cross-model diagnostic sample only; no population-prevalence inference.

## Descriptive results

- Human cases: 12.
- `HUMAN_PATTERN_CONFIRMED`: YES = 12; PARTIALLY = 0; NO = 0.
- Original sample composition retained: 6 `COUNTERPART_RECIPIENT_OVERATTRIBUTION`, 6 `ACTOR_ACTION_FRAGMENTATION`; each pattern has 2 cases per act.
- Case `R4_2D-QA2B-089` additionally records `COUNTERPART_RECIPIENT_OVERATTRIBUTION` as the researcher-specified secondary selection pattern. This does not alter the original sample pattern or gate denominators.

| Field correctness marked NO | Cases |
|---|---:|
| HUMAN_ACTOR_CORRECT | 6 |
| HUMAN_ACTION_CORRECT | 10 |
| HUMAN_OBJECT_CORRECT | 9 |
| HUMAN_COUNTERPART_CORRECT | 12 |
| HUMAN_RECIPIENT_CORRECT | 12 |

Human diagnostic candidate-class frequencies (non-exclusive; labels preserved as candidate classes, not a definitive ontology):

| Candidate class | Cases |
|---|---:|
| ACTOR_ACTION_FRAGMENTATION | 2 |
| ACTOR_SPAN_TRUNCATION | 1 |
| COORDINATED_PROPOSITION_CONFLATION | 1 |
| COUNTERPART_RECIPIENT_OVERATTRIBUTION | 2 |
| CROSS_PROPOSITION_CONTAMINATION | 3 |
| CROSS_SENTENCE_CONTAMINATION | 1 |
| DISTANT_RELATIONAL_CONTAMINATION | 1 |
| EMBEDDED_ACTOR_ACTION_STRUCTURE | 1 |
| EMBEDDED_SOURCE_RELATION_PROMOTION | 1 |
| MODALITY_LOSS | 3 |
| MULTI_PROPOSITION_CONTAMINATION | 1 |
| NON_ACTOR_COMPLEMENT_MISCLASSIFICATION | 1 |
| NON_ACTOR_PREPOSITIONAL_COMPLEMENT_MISCLASSIFICATION | 1 |
| NORMATIVE_COMPLEMENT_MISCLASSIFICATION | 1 |
| OBJECT_SPAN_MISALLOCATION | 1 |
| OBJECT_SPAN_OVEREXTENSION | 1 |
| PASSIVE_ACTOR_INVENTION | 1 |
| PREDICATE_FRAGMENTATION | 1 |
| PROPOSITION_ANCHOR_FAILURE | 1 |
| PROPOSITION_BOUNDARY_FAILURE | 2 |
| RELATIONAL_OMISSION | 2 |
| SEMANTIC_SUBSTITUTION | 1 |
| SPAN_BOUNDARY_FAILURE | 1 |
| SPAN_FRAGMENTATION | 1 |

## Predefined gate assessment

Gate rule: confirmation in all three acts, at least 4/6 YES or PARTIALLY, and at least 3/6 YES. The gate uses the original `PATTERN` used to select the sample, not human subclasses. Every sampled case was adjudicated YES; both patterns therefore pass: 6/6 YES overall and 2/2 YES in each act.

| Act | Cases | Pattern A confirmed | Pattern B confirmed |
|---|---:|---:|---:|
| D1_GDPR | 4 | 2/2 YES | 2/2 YES |
| D2_DSA | 4 | 2/2 YES | 2/2 YES |
| D3_AI_ACT | 4 | 2/2 YES | 2/2 YES |

- A. `COUNTERPART_RECIPIENT_OVERATTRIBUTION`: `HUMAN_CONFIRMED_SYSTEMATIC_DEFECT` — PASS (6/6 YES; present and confirmed in GDPR, DSA and AI Act).
- B. `ACTOR_ACTION_FRAGMENTATION`: `HUMAN_CONFIRMED_SYSTEMATIC_DEFECT` — PASS (6/6 YES; present and confirmed in GDPR, DSA and AI Act).
- Gate counts are descriptive of this purposive sample, not estimates of corpus-wide prevalence.

## Interpretation and next gate

Cross-model detection and human root-cause diagnosis are distinct. Luna/Terra agreement identified records warranting review; human adjudication shows heterogeneous causes, including relational overattribution, proposition-boundary and cross-proposition failures, multi-proposition contamination, normative-complement misclassification, embedded structures, semantic substitution, relational omission, passive-actor invention, modality loss, span/predicate fragmentation, coordinated-proposition conflation, object-span misallocation and non-actor-complement misclassification. These remain `HUMAN_DIAGNOSTIC_CANDIDATE_CLASSES`, not a finalized ontology.

Because Pattern A passes, record `COUNTERPART_RECIPIENT = VARIABLE_PARSIMONY_CANDIDATE`. This is a candidate for dataset-design parsimony review only: do not remove or merge the fields now. Because Pattern B passes, record `ACTOR_ACTION_EXTRACTION_RULE_REPAIR_REQUIRED`; this concerns extraction/segmentation, not a change to intermediation theory.

The next phase may be proposed as `R4.2E — CONTROLLED STRUCTURAL REPAIR`, but it is not started here. No corpus-wide repair, automatic recoding, R/I/T coding, mechanism coding, ROTEM consultation or R4.3 work was performed. The original Luna extraction, Terra V2 review, frozen sample and source text are preserved.

## Firewall state

- `RIT_CODING = NOT_STARTED`
- `MECHANISM_CODING = NOT_STARTED`
- `ROTEM_CODING_CONSULTED = NO`
- `R4_3 = NOT_STARTED`
- `CORPUS_WIDE_REPAIR = NOT_EXECUTED`
- `R4_2_COMPLETE = NO`; `READY_FOR_R4_3 = NO`.

## Integrity

- Frozen original sample SHA-256: `A3503D8B8F1879071C401946A867B8EAA6A6323FCD89A715FF5B02A18130B718`
- Completed human decisions SHA-256: `CB5178FEE6A3C7739C434DA56FCF2970DFD355E4CD64D086B8EFA6CA5B48883E`
- Human summary SHA-256: `8521F696D6B7D6FC3A954A7F25BE5F228D2E88B32612FB3A5F308E9F0D08370C`

Full row-level decisions and notes are in `R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv`; the sample itself remains unchanged.