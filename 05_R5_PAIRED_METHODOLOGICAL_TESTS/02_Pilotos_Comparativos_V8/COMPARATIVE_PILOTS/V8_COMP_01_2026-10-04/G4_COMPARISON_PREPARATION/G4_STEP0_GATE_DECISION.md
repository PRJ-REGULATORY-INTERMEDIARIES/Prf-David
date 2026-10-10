# G4 Step 0 — gate decision

**Date:** 2026-10-04 · **Prepared by:** Claude Code (Sonnet 5.5) · **Decision-maker for any change of status:** Igor Caires Machado

## Status

**`G4_STEP0_CONDITIONAL`** — G4 Step 1 **cannot begin yet** under the existing authorisation.

The expected status `G4_STEP0_COMPLETE / STEP1_PENDING_AUTHORIZATION` is not reported because an essential protocol input remains unresolved: the external audit package and its G4 specification draft were not found, so decision C1 (incorporate and reconcile) and the semantic reconciliation required by C3 are not executed.

## What is complete

| Required result | Value |
|---|---|
| Claims classified per cell | Codex A **24** · Codex B **29** · Claude A **28** · Claude B **31** (total **112** units; plus 2 derived core units) |
| Claims with material evidence-scope deviations (SC-C / load-bearing SC-D) | **5** — Claude A: R-P03-04, CL-P03-02, CL-P03-03; Claude B: R-P04-05, CL-P04-02. None in Codex A or Codex B as verified; no load-bearing SC-D |
| Borderline referent identification (SC-B, provisional) | 2 (Claude B CL-P04-04, CL-P04-07) |
| Peripheral outside/unresolved elements | 13 flagged units (11 SC-A + the 2 SC-B) |
| Unresolved provenance questions | **5** (UPQ-01 'continuity' label, 4 Codex units; UPQ-02 list referent, 2 Claude B units; UPQ-03/04/05 cell-level) |
| Human-review requirements | 28 queue items: 7 P1, 14 P2, 7 P3; all 8 central architecture decisions; all contested scope items; derived-core confirmations. No human review has been performed |
| Status of external audit reconciliation | **Partial.** Package not found (hash `686E322F…FA99` unverifiable; last check 2026-10-04 18:08 -03:00). Local matrix reconciled against the original registered criteria (equivalences, additions, one label-set disagreement resolved in favour of the registered set); external E0–E3 definitions and the G4 spec draft not reconciled |
| C5 | Codex provenance found: `gpt-5.6-terra`, reasoning effort high, Codex VS Code extension CLI 0.159.2, same session for Track A and Track B (external to cell artifacts) |

The classification and eligibility rules are final under the local dictionary and the original registered criteria. They are **provisional with respect to the external specification**.

## Why conditional rather than complete

1. **External package absent** → C1 not executed; C3 reconciliation (labels E0–E3) not done.
2. **SC-B borderline and SC-C items need human confirmation** before the primary comparison set is frozen (2 SC-B units; 2 derived cores; 5 SC-C units' sensitivity-only treatment).
3. **Cell-level provenance gaps** (UPQ-03/04/05) are accepted as limitations but remain open.

None of these indicates an integrity failure; none blocks the preparatory work already done. They block starting systematic claim matching on a basis that might later need re-labelling.

## Conditions to move to `G4_STEP0_COMPLETE / STEP1_PENDING_AUTHORIZATION`

| # | Condition | Alternative |
|---|---|---|
| S1 | Package located; ZIP hash verified; three documents imported unchanged; spec draft reconciled (procedure in `EXTERNAL_AUDIT_RECONCILIATION.md` §4) | Igor records an append-only decision to proceed without the package; the finalised local rules then prevail and the absence is stated in every G4 output |
| S2 | Igor confirms the uniform dictionary or states changes (C3 reconciliation) | If S1 is waived, confirm the dictionary as final |
| S3 | Human confirmation of the P1 items (SC-C classification and derived cores) — may be deferred if Igor accepts the AI-assisted classification as preliminary (C6) | Mark items as `PRELIMINARY_AI_ASSISTED` in the Step 1 table |

If S1 and S2 are resolved by waiver and S3 is deferred as preliminary, Step 1 (claim extraction and normalisation with the registered rubric columns) could be authorised by Igor; **this document does not authorise it.**

## What Step 1 would cover (not started)

Claim extraction and normalisation per cell using the registered columns (common evidence; conclusion A; conclusion B; difference; legal support; claimed gain; error avoided or introduced; sensitivity to cut; added cost; human review), with the Step 0 scope fields attached; pairing only after extraction. SC-C units go to the separately labelled sensitivity analysis; none may support an improvement label.

## Guardrails that remain in force

No claim matching; no superiority judgement; no improvement label for B over A; CONFOUNDED_INPUT (C4); counts and length are not merit; agreement between AI systems is not legal validity; all four cells and every original SHA-256 unchanged; no commit, push, reset or branch change.
