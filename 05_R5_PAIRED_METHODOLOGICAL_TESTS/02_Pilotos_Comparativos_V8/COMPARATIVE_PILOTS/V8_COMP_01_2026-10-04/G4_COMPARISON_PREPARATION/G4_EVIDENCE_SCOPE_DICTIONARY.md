# G4 evidence-scope dictionary (authoritative, provisional on external reconciliation)

**Date:** 2026-10-04 · **Status:** `AUTHORITATIVE_FOR_STEP0` · `EXTERNAL_RECONCILIATION_PENDING` (the external specification could not be read; see `EXTERNAL_AUDIT_RECONCILIATION.md`)
Applies identically to Codex A, Codex B, Claude A and Claude B. It operationalises decision C3 of Igor ("approved, subject to semantic reconciliation of classification labels").

## 1. Frozen boundary

*Frozen primary evidence* = for the statements a claim cites: `exact_legal_excerpt` and the register fields `actor`, `legal_modality`, `action`, `object_or_recipient`, `explicit_condition`, `provision_anchor` of the 20 statements in `COMMON_STATEMENT_REGISTER.csv` (SHA-256 `417A35A3…EF3E77F`), plus other frozen statements of the same register to which a quoted anaphor points. Article 22(7) of P04 is excluded. The official HTML/text of P03 and P04 is **not** inside the boundary except as provenance material.

## 2. Classes

| Class | Name | Definition | Test | Primary-comparison eligibility |
|---|---|---|---|---|
| **SC-A** | `DIRECT_FROZEN` | Every substantive element of the claim (parties, act, modality, object, condition/timing, direction, stated purpose or consequence) is found in frozen primary evidence. Reading non-frozen text for verification, wording or context that is **not relied on** leaves the claim in SC-A and is recorded as a flag. | Element-by-element check against the cited statements; anaphors resolved to frozen statements stay in SC-A. | YES (`YES_WITH_PERIPHERAL_FLAG` if a peripheral flag exists) |
| **SC-B** | `CONTEXT_NO_NEW_PREMISE` | Non-frozen text is used **only to identify what an expression quoted in the frozen excerpt refers to** (cross-reference, anaphor, defined term). The claim adds no party, act, object, purpose, condition, consequence or modality that the frozen statements or the quoted expression itself do not already designate. | After removing the non-frozen sentence, the claim's propositions are unchanged; only the identity of the referent is lost. If removing it changes membership, coupling or conclusion, the class is SC-C. | YES, **provisional** pending human confirmation when borderline |
| **SC-C** | `MATERIAL_EXTERNAL_DEPENDENCE` | The claim's acceptance depends on a substantive element (party, act, object, purpose, condition, consequence, modality, or coupling premise) taken from non-frozen text. | Load-bearing element not found in frozen content **and** outside source recorded or demonstrable from the cell's own record. | **NO** — ineligible to substantiate an incremental improvement; kept for a separately labelled sensitivity analysis. |
| **SC-D** | `UNRESOLVED_PROVENANCE` | A substantive element is not found in frozen content and its source cannot be established from the recorded evidence (no outside source recorded; no frozen support). Also used for cell-level provenance gaps. | As SC-C but without a recorded source. Never resolved by assuming compliance. | HOLD until resolved (human review); load-bearing SC-D is excluded from the primary comparison. |

Absence of a record is **not** compliance. A Codex claim is SC-A in Step 0 only because its elements were *checked* against the frozen text, not because the cell recorded no outside use.

## 3. Materiality (load-bearing vs peripheral)

An element is **load-bearing** if removing it changes the claim's configuration membership, coupling, positional or property assertion, or conclusion. A **peripheral** element appears in a problem statement, label, supporting reason or alternative but its removal changes none of these. Rules:

1. Load-bearing outside element → SC-C (source recorded) or SC-D (source not recorded).
2. Peripheral outside or unresolved element → class by the load-bearing content (normally SC-A), with `peripheral_flags` populated, eligibility `YES_WITH_PERIPHERAL_FLAG` and human review recommended. Peripheral elements are **counted separately** from material deviations.
3. A *mixed claim* (an SC-C element and a separable frozen-text core) is classed SC-C **as stated**; the frozen-text core is registered as a separate `DERIVED_CORE_UNIT` row (eligible for primary comparison) and labelled as derived by Step 0, not asserted by the cell.
4. A negative decision (no architecture claim) is classified by whether the *decision* depends on outside text; supporting reasons that use it are peripheral if the stop would stand without them.

## 4. What is not a scope question

Interpretive architectural vocabulary (for example *delegated*, *gateway*, *necessary stage*, *hub*, *centered*, *coordinating*, *third-party assurance pattern*) is **not** an evidence-scope issue unless it asserts a legal fact (party, act, purpose, consequence) absent from frozen content. These are recorded in `interpretive_label_note` and referred to G4 dimension D (cross-level justification) and to human review. Likewise whether a relation is *defensibly* typed (dimension B) is not decided at Step 0.

## 5. Crosswalk to labels in use

| This dictionary | Local G3C label (matrix §1) | External label (E0–E3) |
|---|---|---|
| SC-A | E1 (and E2 when context was read but not relied on) | **Not determinable**: definitions of E0–E3 were not available; labels preserved in column `external_label_E0_E3` as `PENDING_EXTERNAL_SPEC_NOT_AVAILABLE` |
| SC-B | E1x | pending |
| SC-C | E3 | pending |
| SC-D | `SCOPE_NOT_DETERMINABLE` | pending |

Known differences to test when the external definitions are available, **without assuming equivalence**:
- whether external `E0` (if it denotes a claim needing no contextual reading) corresponds to SC-A or to a subset of it;
- whether the external scheme treats the referent identification of a cross-reference (SC-B) as the same level as non-relied reading (the local E2) or as a separate level;
- whether the external scheme has a class for load-bearing premises without recorded source (SC-D) or folds them into its highest-risk class;
- whether the external scheme classifies by the element used or by the claim; local rule: by claim, weakest load-bearing element, with core split.
If definitions materially conflict, both labels stay in their columns and no mapping is forced; the dictionary here controls Step 0 output until Igor decides otherwise.

## 6. Eligibility rules (used in the classification file)

`YES` · `YES_WITH_PERIPHERAL_FLAG` · `YES_PROVISIONAL_PENDING_HUMAN_CONFIRMATION` (SC-B borderline) · `NO_SENSITIVITY_ONLY` (SC-C) · `HOLD_UNRESOLVED` (SC-D load-bearing). Sensitivity-only claims are never used to support `B_IMPROVES`, `SUBSTANTIVELY_IMPROVED` or any improvement label; they feed a **separately labelled** sensitivity analysis (for example "with scope-extended claims included").

## 7. Relationship to the original registered criteria

The original criteria in `COMPARISON_EVALUATION_CRITERIA.md` and protocol §6 remain authoritative. This dictionary implements their "traceability / unsupported relation / inferential defensibility" concerns for the frozen-evidence boundary and does not alter any of their labels or procedures.
