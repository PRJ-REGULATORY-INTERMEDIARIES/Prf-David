# G4 — Claim extraction and matching rules

**Experiment:** V8-COMP-01 · **Date:** 2026-10-04 · **Status:** `FINALIZED_BEFORE_SYSTEMATIC_MATCHING`
Companion to `G4_FINAL_EVALUATION_MATRIX.md` (§1 evidence-scope rule and dimensions A–I apply here).

## 1. Principles

1. The unit is a **claim with its evidence and warrant**, not a file, a count or a section.
2. Counts of accepted relationships, number of configurations, report length and number of categories are **never** evidence of superiority.
3. Agreement between AI systems is **not** legal validity.
4. Matching is performed on **propositions**, not wording; the join key is the set of **statement IDs** (CS-P03-001…006, CS-P04-001…014) plus bearer and level.
5. Execution is **sequential**; no parallel agents. Anything produced by an AI is labelled `PRELIMINARY_AI_ASSISTED`; unresolved items go to human review. No human judgement is simulated.
6. Evidence-scope tagging (matrix §1) comes **before** any label is assigned.

## 2. Procedure

| Step | Action | Output |
|---|---|---|
| 0 | **Scope tagging.** For every claim and every accepted/deferred/rejected relationship that cites a cross-provision, tag E1 / E1x / E2 / E3 / `SCOPE_NOT_DETERMINABLE`. Cells without a cross-provision field are tagged by checking each cited anchor against the register excerpt. | scope table |
| 0.5 | Reconcile with the external draft `G4_OPERATIONAL_COMPARISON_SPEC_DRAFT.md` once available; log differences; the rules in this file prevail unless Igor decides otherwise (append-only decision). | reconciliation note |
| 1 | **Extract claims** from each cell: relation-level, configuration-level, architecture-level, positional, part–whole, boundary; each with `claim_id` (cell prefix), proposition in one sentence, level, bearer, scope (case, statements), status (accepted/deferred/rejected/no-claim), warrant, counter-evidence, stopping decision, scope tag. Use the cell's own words in an auxiliary column; do not harmonise vocabulary at this stage. | claim table |
| 2 | **Normalise** each proposition to the template *"[bearer] — [property/relation] — [scope] — [condition]"* without changing meaning; keep the original. | normalised claim table |
| 3 | **Candidate pairing** inside each contrast family (matrix §2) by overlapping statement IDs and same case; a claim can pair with several claims or none (many-to-many allowed). | pairing table |
| 4 | **Classify** each pair with the labels in §3 using the decision order in §4. | classification table |
| 5 | **Unpaired claims**: a claim without a counterpart is labelled `UNMATCHED_ADDITIONAL` (present in one cell only) — still tagged for scope and level; it is *not* automatically an improvement. | list |
| 6 | **Human review queue**: every pair labelled `UNRESOLVED_NON_COMPARABLE`, every `CONTRADICTORY`, every `INFERENTIAL_REGRESSION` and every `SUBSTANTIVELY_IMPROVED`, plus a random 20 % of `EQUIVALENT` pairs (seeded, seed recorded). | review queue |

## 3. Classification labels

Labels apply to an **ordered pair (reference → comparator)**. For method contrasts (family 1) the reference is the A cell. For model contrasts (family 2) there is **no reference arm**: use only the symmetric labels (`EQUIVALENT`, `BROADER`/`NARROWER`, `CONTRADICTORY`, `UNRESOLVED_NON_COMPARABLE`) plus `INFERENTIAL_REGRESSION` where one claim demonstrably violates a criterion that the other satisfies (state the criterion). Improvement labels are not used across models.

| Label | Rule (all conditions must hold) |
|---|---|
| **EQUIVALENT** | Same proposition, same bearer and level, same case; same or overlapping statement anchors; same status (accepted/deferred/rejected) and same stopping level. Differences in wording, order, jargon, number of fields or extra explanation are ignored. |
| **SUBSTANTIVELY_IMPROVED** | The comparator's proposition differs from the reference in a way that **corrects or avoids a defect in the reference**, verifiable on E1/E1x evidence only: e.g. removes or declines an unsupported edge (dim. C); demotes a promoted claim to the supported level (D); correctly identifies a legally evidenced relation, position or part–whole bearer that the reference missed or mis-bore; or replaces an unsupported statement of status with a defensible one. The reference defect and the corrected state must both be citable by statement ID. Never assigned if the comparator relies on E3 or `SCOPE_NOT_DETERMINABLE`. |
| **PROCEDURALLY_IMPROVED** | Same proposition, level and status as the reference, but the comparator makes the warrant, bearer, counter-evidence, sequence or stopping rule explicit, or fixes a traceability gap (dim. E), **without changing what is claimed**. |
| **BROADER** / **NARROWER** | The comparator's proposition contains (BROADER) or is contained in (NARROWER) the reference's: more or fewer actors/stages/statements, a higher or lower claim level, or a different epistemic status short of contradiction (accepted vs deferred; configuration vs no-architecture). The label records direction only. A second tag states whether the extra breadth is supported on E1/E1x (`SUPPORTED_BREADTH` / `UNSUPPORTED_BREADTH`). Narrower is not worse and broader is not better. |
| **CONTRADICTORY** | The two propositions cannot both hold on the same E1 evidence: e.g. relation accepted vs rejected for the same parties and action; opposite direction; different bearer for the same property; architecture-level claim vs an explicit finding that none is warranted **where both are stated as findings, not as deferrals**. Deferral vs acceptance is *not* contradiction (use BROADER/NARROWER). |
| **INFERENTIAL_REGRESSION** | The comparator's claim is less defensible than the reference on a named criterion: unsupported edge (C), actor inferred from a passive/unexpressed actor (C), promotion beyond the stopping rule or across levels without bearer (D), reliance on E3 evidence (A), loss of a traceability link (E), suppression of an uncertainty the reference preserved (F). Name the criterion and cite the anchors. |
| **UNRESOLVED_NON_COMPARABLE** | The pair cannot be classified: units not mappable (different segmentation, relation typology without a one-to-one translation), evidence scope cannot be established, the judgement needs legal expertise not available, or the reference cell does not contain the unit (e.g. a Track B operation output with no Track A counterpart). Reported as such; never forced into another label. |

## 4. Decision order (first rule that applies wins)

1. Scope tag unresolved for either claim → `UNRESOLVED_NON_COMPARABLE` (record why).
2. No mappable proposition → `UNRESOLVED_NON_COMPARABLE`; unmatched single-cell claim → `UNMATCHED_ADDITIONAL`.
3. Comparator relies on E3 or violates a named criterion the reference satisfies → `INFERENTIAL_REGRESSION` (family 1 and 2).
4. Propositions cannot both hold on E1 → `CONTRADICTORY`.
5. Same proposition, level, status, stop → `EQUIVALENT`; if the only difference is explicitness of warrant/bearer/trace → `PROCEDURALLY_IMPROVED` (method contrasts only; otherwise `EQUIVALENT`).
6. Comparator corrects a citable reference defect on E1/E1x → `SUBSTANTIVELY_IMPROVED` (method contrasts only; otherwise report the difference as `BROADER`/`NARROWER` with the defect note).
7. Otherwise `BROADER` or `NARROWER` (+ supported/unsupported breadth tag).

## 5. Mapping to protocol vocabulary (family 1, dimension I)

| Matching label | Protocol label |
|---|---|
| EQUIVALENT | `B_EQUIVALENT` |
| PROCEDURALLY_IMPROVED | `B_CLARIFIES_ONLY` |
| SUBSTANTIVELY_IMPROVED | `B_IMPROVES` |
| INFERENTIAL_REGRESSION | `B_WORSE` |
| BROADER / NARROWER / CONTRADICTORY / UNRESOLVED_NON_COMPARABLE / UNMATCHED_ADDITIONAL | `UNRESOLVED` unless a reviewer assigns one of the four labels |

## 6. Specific safeguards

- **Candidate-listing policies differ** between cells (some tables list only accepted relations; others list rejected and deferred candidates). Do **not** compare relation counts or acceptance rates. Compare matched propositions only. See deviation D-10.
- **Extra material in B** (positional, part–whole, sensitivity) has no A counterpart by design; an `UNMATCHED_ADDITIONAL` B item is evaluated for scope and level and, where it modifies an A-matched claim, through that claim.
- **Same-model contrast** (Claude A vs Claude B) may share model habits; **cross-model contrast** may be driven by input differences (D-07, D-08). Differences attributable to those are tagged `CONFOUNDED_INPUT` and not interpreted as method or model effects.
- **Evaluator role conflict:** the AI session that orchestrated the Claude replication must not be the sole matcher of Claude vs Codex claims. If an AI-assisted pass is run, it is reported as preliminary, the evaluator's exposure is recorded (dimension rule 6), and contested labels go to human review.
- **Randomisation for review:** claim order in the human instrument is shuffled with a recorded seed; model/track identity is held only in the separate mapping key.
- Nothing in this file authorises a statement about legal validity from agreement.
