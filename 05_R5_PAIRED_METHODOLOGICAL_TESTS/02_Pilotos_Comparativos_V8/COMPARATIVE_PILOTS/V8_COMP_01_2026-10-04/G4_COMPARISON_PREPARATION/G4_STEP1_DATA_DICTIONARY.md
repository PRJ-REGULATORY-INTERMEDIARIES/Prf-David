# G4 Step 1 — neutral data dictionary

**Date:** 2026-10-04 · Applies to `G4_STEP1_NORMALIZED_CLAIMS.csv`, `G4_STEP1_ELIGIBILITY_REGISTER.csv` and `G4_STEP1_HUMAN_REVIEW_QUEUE.csv`.
**Purpose of the registers:** a single, neutral, structurally standardised inventory of what the four frozen cells recorded. They contain **no** cross-cell matching, agreement, improvement, regression, scoring or superiority information.

## 1. General conventions

| Convention | Meaning |
|---|---|
| `NOT_APPLICABLE` | The field has no meaning for this unit type (for example `direction` of an architecture-level decision). |
| `NONE` | The field applies and there is nothing to record. |
| `NONE_RECORDED_FOR_THIS_UNIT` | The cell's own uncertainty register contains no entry linked to this unit by the joining rules in decision N-10 (not a statement that no uncertainty exists). |
| `NOT_DOCUMENTED` | A parameter or provenance item that no examined record documents (for example Codex sampling parameters). |
| `AGGREGATE` | The field summarises member relations of a configuration or decision; the member list is in the text. |
| Quotation | Fields marked *verbatim* reproduce the cell's own words. Normalised fields restate structure and never add or drop substantive meaning (decisions N-04, N-05). |
| Language | Original formulations are kept in their original language and vocabulary (English); no vocabulary is harmonised across cells (N-06). |
| Frozen boundary | Frozen evidence = `COMMON_STATEMENT_REGISTER.csv` (SHA-256 `417A35A3…EF3E77F`), 20 statements, P04 Art. 22(7) excluded. |

## 2. Unit types

| `claim_type` | Meaning | Count |
|---|---|---|
| `RELATION` | An **accepted** relationship record of a cell. | 71 |
| `CONFIGURATION_LEVEL_CLAIM` | A configuration claim as recorded by the cell (Codex configurations; Claude configuration claims). | 23 (Codex A 6, Codex B 6, Claude A 6, Claude B 5) |
| `RELATION_LEVEL_CLAIM` | A claim that the cell itself states at relation level (Claude A CL-P04-04; Claude B CL-P03-01). | 2 |
| `POSITIONAL_CLAIM` | A positional or sequence claim **accepted** by the cell (Codex B O5 rows; Claude B CL-P04-05…08). | 8 |
| `ARCHITECTURE_LEVEL_CLAIM` | A positive architecture-level claim (Codex A and B, P04). | 2 |
| `ARCHITECTURE_LEVEL_STOPPING_DECISION` | A cell's recorded decision that the highest supported level is below architecture. | 6 |
| `STEP0_DERIVED_CORE` | A unit **constructed by G4 Step 0**, never an original claim of Codex or Claude. | 2 |

Totals: 112 original units + 2 derived = 114 rows. Only accepted relationships and the claims listed above are extracted; rejected and deferred candidates, declined architecture claims, sensitivity items and uncertainty entries are **not** claim units (N-21).

## 3. `G4_STEP1_NORMALIZED_CLAIMS.csv`

The first 24 columns are the specified fields, in the specified order. The remaining columns are provenance and bookkeeping.

| Field | Definition / domain |
|---|---|
| `source_cell` | `CODEX_A` (V8 only), `CODEX_B` (V8 + eight operations), `CLAUDE_A`, `CLAUDE_B`. |
| `original_claim_id` | The cell's own ID, or an ID assigned at Step 0 where the cell did not label the unit (`TB-O5-*`, `AD-P03`, `AD-P04`); `…#CORE` for derived units. |
| `claim_type` | See section 2. |
| `original_claim_text` | *Verbatim.* Relations: every field of the cell's relationship record in the form `field: value; …`. Other units: the cell's own section, table row(s) or bullet(s), exactly as in the frozen file (several lines may be joined with a line break). Derived units: `NOT_APPLICABLE`. |
| `normalized_claim_text` | Neutral restatement. Relations: built from the record's own actor strings, relation label, modality, condition and statement IDs. Other units: a single restatement paragraph that keeps the cell's own labels in quotation marks, its stated limits and its disclaimers, and annotates (without adding to the claim) where the cell relied on text outside the frozen statements. |
| `legal_case` | `P03` (Directive 91/263/EEC, CELEX 31991L0263) or `P04` (Regulation (EC) No 874/2004, CELEX 32004R0874). |
| `frozen_statement_ids` | Common statement IDs the unit cites or is anchored to (`CS-P03-001…006`, `CS-P04-001…014`). |
| `primary_legal_anchors` | Provision locators recomputed from the register (`provision_anchor` second part). |
| `actors` | Parties as recorded (relations); union of the parties of member relations (configurations, decisions); named parties (positional). Cell wording kept. |
| `action_or_relation` | Relation: the cell's type (Codex adds function, mechanism, instrument). Aggregates: list of member relation IDs and types. Positional: the stated position or order. |
| `modality` | Relations: as recorded. Other units: union of `legal_modality` of the cited frozen statements (register field). |
| `direction` | Relations: as recorded or `actor_from → actor_to`. Aggregates: list per member relation. Positional: sequence or dependency direction. Decisions: `NOT_APPLICABLE_AGGREGATE_DECISION`. |
| `condition` | Relations: as recorded. Aggregates: conditions of member relations. Positional: stated conditions. Decisions: stopping rule and boundary pointer. |
| `analytical_level` | `relation`; `configuration`; `position`; `architecture claim (positive)`; `architecture-level stopping decision (negative; highest level stated: configuration/relation)`; `configuration (derived core)`. This is a descriptive level, not a quality rating. |
| `property_bearer` | What carries the property the unit asserts (V8 requirement): relation; configuration; position of an actor within a configuration; order or dependency inside a configuration; configuration set of the case; none asserted at architecture level. |
| `inferential_warrant` | *Verbatim* extract of the cell's stated warrant: warrant/reason text (relations); selected labelled lines (membership, coupling, attributes, boundary, significance, alternatives) or the cell's positional row (other units). |
| `uncertainty` | Entries of the cell's own uncertainty register linked to the unit (ID, type/status, first 170 characters of the description). See N-10. |
| `evidence_scope_class` | **Exact Step 0 value, unchanged:** `SC-A`, `SC-B`, `SC-C`, `SC-D` (definitions in `G4_EVIDENCE_SCOPE_DICTIONARY.md`, approved under C3). |
| `evidence_scope_justification` | Step 0 justification, verbatim. |
| `material_external_dependency` | `NONE`; `NONE_MATERIAL; context consulted, not relied on: …`; `NONE_MATERIAL; PERIPHERAL: …`; `REFERENT_IDENTIFICATION (borderline): …`; `MATERIAL: …`. |
| `primary_comparison_eligibility` | `YES`; `YES_WITH_PERIPHERAL_FLAG`; `YES_PROVISIONAL_PENDING_HUMAN_CONFIRMATION` (SC-B); `NO_SENSITIVITY_ONLY` (SC-C); `PROVISIONAL_PENDING_P1_HUMAN_CONFIRMATION (STEP0_DERIVED; Step 0 value was YES)`; `HOLD_UNRESOLVED` (none used). |
| `sensitivity_analysis_eligibility` | `INCLUSIVE_AND_RESTRICTED_VARIANTS` (unit enters both variants); `SENSITIVITY_ANALYSIS_ONLY_INCLUSIVE_VARIANT` (SC-C); `INCLUSIVE_VARIANT_AND_RESTRICTED_VARIANT_IF_CONFIRMED_SC-B`; `INCLUSIVE_AND_RESTRICTED_VARIANTS_AFTER_CONFIRMATION` (derived). "Inclusive variant" = analysis with scope-extended units included, separately labelled; "restricted variant" = primary comparison set. |
| `human_review_priority` | `P1`, `P2`, `P3` from the preserved 28-item queue; `NONE` if the unit is not in the queue. |
| `provenance_status` | Origin of the unit and the executing configuration: Codex = model `gpt-5.6-terra`, reasoning effort High, Codex VS Code extension, CLI 0.159.2, other parameters `NOT_DOCUMENTED`; Claude = `claude-sonnet-5-5` self-reported by the orchestrator and the executing subagent, sampling parameters `NOT_DOCUMENTED`. |
| `unit_id` | `S1-001…114`. |
| `unit_origin` | `ORIGINAL_CELL_CLAIM`; `ORIGINAL_CELL_CLAIM_ID_ASSIGNED_AT_STEP0`; `STEP0_DERIVED`. |
| `step0_row_id` | Row in `G4_STEP0_EVIDENCE_CLASSIFICATION.csv` (`S0-001…114`). |
| `step0_local_label_and_flags` | Step 0 local G3C label (E1/E1x/E3/…) and peripheral flags, verbatim. Local labels use different meanings from the external E0–E3 (see N-14). |
| `inherited_dependency_assessment` | Propagation result (N-12): `MATERIAL_DIRECT`; `MATERIAL_INHERITED`; `BORDERLINE_INHERITED`; `PERIPHERAL_INHERITED`; `NO_INHERITED_DEPENDENCY`; `NOT_APPLICABLE_DERIVED_FROM_PARENT`. |
| `human_review_queue_id` | `HRQ-01…28` or `NONE`. |
| `interpretive_label_note` | Step 0 note on interpretive vocabulary (routed to later review of cross-level justification, not a scope matter). |
| `source_location`, `source_file`, `source_file_sha256` | Where the original is, and the recalculated SHA-256 of that frozen file. |
| `cell_model_record` | Model/configuration of the cell's executor. |
| `external_label_status` | Always `NOT_MAPPED; E0-E3 description unauthenticated`. |

## 4. `G4_STEP1_ELIGIBILITY_REGISTER.csv`

| Field | Definition |
|---|---|
| `unit_id`, `source_cell`, `original_claim_id`, `unit_origin`, `legal_case`, `claim_type`, `step0_row_id` | As above. |
| `step0_scope_class`, `step0_eligibility_value` | The Step 0 values, kept so that no relabelling is silent. |
| `evidence_scope_class`, `material_external_dependency` | As in the claims register. |
| `propagation_assessment` | `MATERIAL_DIRECT` (5, the SC-C units); `MATERIAL_INHERITED` (0); `BORDERLINE_INHERITED` (1); `PERIPHERAL_INHERITED` (11); `NONE`; `NOT_APPLICABLE_DERIVED`. |
| `primary_comparison_eligibility`, `sensitivity_analysis_eligibility` | As above. |
| `peripheral_flags`, `human_review_priority`, `human_review_queue_id` | As above. |
| `candidate_external_label_UNAUTHENTICATED_NOT_ADOPTED` | The nearest class of the ChatGPT-relayed E0–E3 description **by definition wording**, listed for later reconciliation only. Not a mapping; it is not used in any eligibility decision. |
| `candidate_label_reservation` | Where the definitions may diverge for this unit (N-14). |
| `eligibility_basis` | Fixed explanation of the basis. |

## 5. `G4_STEP1_HUMAN_REVIEW_QUEUE.csv`

The 28 items of `G4_STEP0_HUMAN_REVIEW_QUEUE.csv` with unchanged IDs, priorities and order, enriched with: `step1_unit_id`; `legal_validity_issue_pending_human_adjudication` (`YES` for P1, central architecture claims and borderline referents); `original_claim_text`; `normalized_claim_text`; `exact_frozen_excerpts` (register excerpts, verbatim); `non_frozen_official_text_in_question_NOT_FROZEN_EVIDENCE` (the exact sentences of the official text that the cell relied on or read; **not frozen evidence**, shown only so that a reviewer can judge); `uncertainty`; `reason_requiring_human_judgment`; `ai_assisted_preliminary_observation` (a restatement of the Step 0 classification, explicitly not a decision); and empty `human_decision_field`, `human_reviewer_id`, `human_decision_date`. **No human decision has been entered or simulated.**

## 6. Protocol outcome scheme (preserved, not applied)

The original five-category A-to-B scheme of the research protocol — `B_IMPROVES`, `B_CLARIFIES_ONLY`, `B_EQUIVALENT`, `B_WORSE`, `UNRESOLVED` — remains the only permitted scheme for the reported A-to-B outcome. The seven provisional working labels of the matching rules are **not** used or replaced in Step 1. No field in these registers holds an improvement, agreement, regression or equivalence label (QA check Q20).
