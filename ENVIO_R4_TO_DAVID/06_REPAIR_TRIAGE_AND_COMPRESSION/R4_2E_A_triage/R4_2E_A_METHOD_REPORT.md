# R4.2E-A — Controlled structural repair candidate identification

**Status:** `R4_2E_A_REPAIR_CANDIDATES_IDENTIFIED_PENDING_TERRA_REPAIR`  
**Starting checkpoint:** `R4_2D_FROZEN_READY_FOR_R4_2E_A` (the preceding R4.2D record remains preserved).  
**Execution provenance:** requested model `GPT-5.6 Luna High`; this Codex runtime cannot independently expose or verify that model variant. Detection below is deterministic heuristic triage, not a model repair run.  
**Scope:** identification before repair. The original 1,404-row extraction was verified against its freeze SHA-256 and was not modified.

## Three evidence layers kept separate

- **Human evidence:** 12 purposively selected, adjudicated R4.2D cases. They are frozen references, not a later independent validation sample.
- **Cross-model evidence:** paired Luna self-review and independent Terra V2 records. The source comparisons cover a subset only; uncovered records are `NOT_ASSESSED`. Agreement is supporting evidence, not ground truth.
- **Rule-based detection:** deterministic review triggers applied across all 1,404 rows. A trigger means `CANDIDATE_FOR_REVIEW`, never `ERROR_CONFIRMED`. No corpus accuracy or prevalence rate is estimated.

## Candidate disposition

| Repair candidate | Records |
|---|---:|
| YES | 713 |
| NO | 345 |
| UNCERTAIN | 346 |

| Complexity | Records |
|---|---:|
| NONE | 345 |
| SIMPLE | 160 |
| MODERATE | 514 |
| COMPLEX | 385 |

| Recommended handler | Records |
|---|---:|
| NONE | 357 |
| DETERMINISTIC_RULE | 159 |
| TERRA_HIGH | 524 |
| HUMAN | 364 |

| Priority | Records |
|---|---:|
| P1 | 18 |
| P2 | 536 |
| P3 | 315 |
| P4 | 535 |

Top rule-trigger counts (non-exclusive heuristic hits):

| Rule | Rows |
|---|---:|
| PREPOSITION_DOES_NOT_IMPLY_RECIPIENT | 645 |
| OBJECT_MUST_NOT_FUNCTION_AS_RESIDUAL_BUCKET | 570 |
| TEMPORAL_SPATIAL_MANNER_MODIFIERS_ARE_NOT_CORE_ACTION_OR_OBJECT | 351 |
| PROPOSITION_BOUNDARIES_MUST_BE_PRESERVED | 330 |
| RELATIONAL_ENTITY_MUST_BE_ACTOR_CAPABLE | 303 |
| COORDINATED_PREDICATES_MUST_REMAIN_DISTINCT | 224 |
| EXPLICIT_RELATIONAL_ACTOR_MUST_NOT_BE_DROPPED | 31 |
| PRESERVE_LEGAL_MODALITY | 25 |
| PRESERVE_MODAL_DEONTIC_LEXICAL_CONSTRUCTION | 25 |
| STRUCTURAL_EXTRACTION_MUST_PRESERVE_LEGAL_VERB | 15 |

Candidate dispositions by act are in the summary CSV. These figures describe triage outputs only and are not error-rate estimates.

| Act | Total records | YES | UNCERTAIN | NO |
|---|---:|---:|---:|---:|
| D1_GDPR | 485 | 267 | 105 | 113 |
| D2_DSA | 424 | 195 | 121 | 108 |
| D3_AI_ACT | 495 | 251 | 120 | 124 |

## Human-case known-defect rediscovery

- Rediscovered: 9 / 12 known human-adjudicated defects (`KNOWN_DEFECT_REDISCOVERY`; not population recall).
- A missed known defect means the fixed deterministic trigger mapping did not match its original model-selection family; it does not negate the human adjudication.
- False simplifications: 0 case(s) assigned SIMPLE despite a human-known complex class.
- Other underclassifications: 1 human-complex case(s) assigned MODERATE.
- Complex cases incorrectly assigned SIMPLE: 0.
- Missed known-defect cases: R4_2D-QA2B-026 [PROPOSITION_BOUNDARY_FAILURE; CROSS_PROPOSITION_CONTAMINATION]; R4_2D-QA2B-056 [CROSS_PROPOSITION_CONTAMINATION; EMBEDDED_ACTOR_ACTION_STRUCTURE]; R4_2D-QA2B-089 [MULTI_PROPOSITION_CONTAMINATION; PROPOSITION_ANCHOR_FAILURE].
- Per-case triggers, complexity defensibility and handler are in `R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv`.

## Cross-model evidence coverage

- Both flagged: 60; Luna only: 9; Terra only: 0; neither flagged: 18; not assessed in paired model comparison: 1317.
- Only the records present in the paired comparison are assigned model flags. Flags are not used as human truth.

## Counterpart/recipient burden audit

- Counterpart populated: 995 / 1,404.
- Recipient populated: 995 / 1,404.
- Both populated: 995; values identical: 995; counterpart only: 0; recipient only: 0.
- At least one human-derived relational heuristic triggered: 729 records.

| Act | Records | Counterpart populated | Recipient populated | Identical values | Relational rule trigger |
|---|---:|---:|---:|---:|---:|
| D1_GDPR | 485 | 351 | 351 | 351 | 245 |
| D2_DSA | 424 | 299 | 299 | 299 | 226 |
| D3_AI_ACT | 495 | 345 | 345 | 345 | 258 |

This audit informs later parsimony analysis only. No variable was deleted, merged, or redefined.

## Actor/action candidate audit

The row-level audit flags possible actor truncation/complement assignment, modality metadata mismatch, predicate fragmentation, discourse-only action, passive/no-explicit-actor risk, proposition-boundary risk, and coordinated predicates. It contains candidate indicators only; the fields themselves were not changed.

| Indicator | Records |
|---|---:|
| ACTOR_SPAN_TRUNCATION_CANDIDATE | 3 |
| ACTOR_COMPLEMENT_CANDIDATE | 37 |
| MISSING_MODAL_CANDIDATE | 25 |
| PREDICATE_FRAGMENTATION_CANDIDATE | 15 |
| DISCOURSE_ONLY_ACTION | 2 |
| PASSIVE_NO_EXPLICIT_ACTOR_CANDIDATE | 7 |
| PROPOSITION_BOUNDARY_CONTAMINATION_CANDIDATE | 330 |
| COORDINATED_PREDICATE_CANDIDATE | 224 |

## Rule governance and new rules

All 15 human-derived rule IDs were kept intact. `MODEL_DETECTION_PATTERN_DOES_NOT_EQUAL_HUMAN_ROOT_CAUSE` was applied as an interpretation firewall by retaining separate `MODEL_SELECTION_PATTERN` and `HUMAN_DIAGNOSTIC_DEFECT_CLASS` columns; it is not a lexical trigger. The screen produced no separately adjudicated new rule. `R4_2E_A_NEW_RULE_CANDIDATES.csv` records that no new rule is formally proposed in this heuristic screen; investigate emerging signals during human/Terra review rather than silently expanding the rule set.

## No-repair declaration and firewalls

No `REPAIRED_*` columns were created. No record values were corrected, no 1,404-row extraction was regenerated, and no automatic repair was run. The original Luna extraction, source corpus and model QA artifacts remain frozen.

- `RIT_CODING = NOT_STARTED`
- `MECHANISM_CODING = NOT_STARTED`
- `ROTEM_CODING_CONSULTED = NO`
- `R4_3 = NOT_STARTED`
- `CORPUS_WIDE_REPAIR = NOT_EXECUTED`
- `R4_2E_COMPLETE = NO`; `R4_2_COMPLETE = NO`.

## Output integrity

| Output | SHA-256 |
|---|---|
| R4_2E_A_REPAIR_CANDIDATE_REGISTER.csv | A317A82B70DF009FE9EF2C56399F6FBACA70F30BA60BAE46F5E4D6431030F03D |
| R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv | 3056073F3E72DBCFB885EDEC5FDE086CD41E2CDF486374DBA412E54EE1594F33 |
| R4_2E_A_COUNTERPART_RECIPIENT_BURDEN_AUDIT.csv | 808BDB8FA69655E01FFCEF34296CD50204EB475FF83135DFFAB2BA022EFDD255 |
| R4_2E_A_ACTOR_ACTION_REPAIR_AUDIT.csv | B65AB09D6ABEE0845B2CAACD611A0C022EE87130E72A958DE383319847442626 |
| R4_2E_A_REPAIR_CANDIDATE_SUMMARY.csv | 6198C9CC2123E87D138EF3B79B0F8A7C9111A32851D2DCFE10B44C1D8E1AE600 |
| R4_2E_A_NEW_RULE_CANDIDATES.csv | 30C9EA66BB78CD144184DA83ED6AA1C50F8167BD5F79AC3E3A2DC3A7EB9546A0 |

Next stage remains pending Terra repair/review; this report does not authorize or initiate that phase.