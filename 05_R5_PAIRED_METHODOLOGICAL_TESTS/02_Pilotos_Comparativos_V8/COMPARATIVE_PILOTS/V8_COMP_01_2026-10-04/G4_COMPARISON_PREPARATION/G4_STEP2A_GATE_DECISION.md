# G4 Step 2A — gate decision

**Date:** 2026-10-04 · **Prepared by:** Claude Code (Sonnet 5.5) · **Authority for any further step:** Igor Caires Machado

## Status

**`G4_STEP2A_FROZEN / STEP2B_NOT_STARTED`**

Step 2A (candidate claim correspondence, grouping and documentary traceability) is complete and frozen. No agreement score, improvement or regression label, quality ranking, superiority assessment or legal-validity adjudication was produced; the original five-category outcome scheme was not assigned and not altered; the seven working labels were not used. **G4 Step 2B has not been started and is not authorised by this document.**

## Results

| Required item | Result |
|---|---|
| Correspondence groups | **26**: relation 16 · configuration 6 · position 2 · architecture-level decision 2. Types (candidate only): same proposition 16 · same proposition with different segmentation 2 · overlapping proposition 6 · same subject, same kind of determination 1 (CG-025, P03) · same subject, different kind of determination 1 (CG-026, P04) |
| Original units matched / unmatched per cell | Codex A **24 / 0** (of 24) · Codex B **27 / 2** (of 29; unmatched TB-O5-P03-01, TB-O5-P04-02) · Claude A **24 / 4** (of 28; unmatched R-P03-02, R-P03-03, R-P03-04, CL-P03-03) · Claude B **26 / 5** (of 31; unmatched R-P04-05, R-P04-13, R-P04-16, CL-P04-07, CL-P04-08). Total **101 matched / 11 unmatched** of 112. Unmatched means only that no corresponding register unit was identified at the same level; it is not an omission, failure or improvement. The two STEP0_DERIVED cores are attached to groups and are not counted as original claims |
| One-to-many / many-to-one | **Many-to-one by segmentation:** CG-001 (P03 notification: Codex A and Codex B two relations per cell, Claude A and Claude B one joined relation; Claude B also a relation-level restatement) and CG-011 (P04 agent notification: Codex B two relations, other cells one). **One-to-many:** Claude A CL-P04-04 (relation-level claim) belongs to CG-015 and CG-016 and counts once. Memberships: 102 for 101 grouped original units |
| Evidence-scope conflicts | **3 groups** whose members have different Step 0 classes: CG-018 (Claude A CL-P03-02 SC-C vs three SC-A), CG-019 (Claude B CL-P04-02 SC-C vs three SC-A), CG-022 (Claude B CL-P04-04 SC-B vs two SC-A). The five material-dependency units are all preserved: two grouped (CL-P03-02 in CG-018, CL-P04-02 in CG-019), three unmatched (R-P03-04, CL-P03-03, R-P04-05). Flags are propagated to the architecture-level groups (CG-025 from CG-018; CG-026 from CG-019 and CG-022). Seven groups carry peripheral observations (CG-002, CG-016, CG-018, CG-021, CG-022, CG-025, CG-026). Nothing was removed or relabelled |
| Granularity differences | Statement segmentation (CG-001, CG-011, CG-015/016); relation-level versus configuration-level treatment of the same statements (Claude B CL-P03-01; Claude A CL-P04-04); membership breadth in six overlapping configuration/positional groups (CG-017, CG-018, CG-019, CG-021, CG-022, CG-024); different kinds of architecture-level determination (CG-026). Detail is not treated as merit. Full list in `G4_STEP2A_GRANULARITY_AND_SCOPE_REGISTER.md` |
| Provisional groups requiring human review | **13** of 26: 9 `YES` (CG-017, CG-018, CG-019, CG-021, CG-022, CG-023, CG-024, CG-025, CG-026) and 4 `SPOT_CHECK` (CG-001, CG-006, CG-011, CG-013); 13 groups are `NO_LOW_RISK_AI_PRELIMINARY` (screened by the same AI executor only). The reviewer package has 13 anonymised cards with exact frozen excerpts; identity is in a separate sealed key. **The seven P1 items remain pending actual human adjudication** (two in groups CG-018/CG-019 with their attached derived cores; three unmatched: R-P03-04, CL-P03-03, R-P04-05); no human decision exists or was simulated |
| Integrity | Step 1 manifest `0DEC88FF…DD0B` re-verified (27 of 27 non-register rows; the four registers appended after QA by design); four cells (35 outputs), common register, official HTML and Step 0 files unchanged; QA **32 PASS, 0 FAIL**; Git HEAD `ae1af32`, 0 tracked changes |

## What was and was not decided

Decided (candidate level): which register units are about the same institutional proposition, how segmentation and level differ, and how scope flags travel.
**Not decided:** whether any two corresponding propositions are equivalent, consistent, contradictory or better; whether a difference stems from model, prompt, supporting documents or the eight operations (CONFOUNDED_INPUT, decision C4); legal validity; any outcome label.

## Open conditions carried forward (none blocks the freeze)

1. Human adjudication of the seven P1 items and of the groups marked `YES`/`SPOT_CHECK` before any definitive legal-validity scoring; no reviewers have been named.
2. Confirmation of the two SC-B units and the two derived cores before they enter a primary comparison set.
3. Provenance questions UPQ-01…UPQ-05 unchanged; sampling parameters of both systems `NOT_DOCUMENTED`.
4. External specification unavailable (waiver in force); relayed E0–E3 description not mapped.
5. The matching was done by one AI executor with an acknowledged role conflict (D-15); the 13 low-risk groups are unvalidated screening results.
6. The read-only attribute observed lost after the reboot (recovery report) was not re-applied; Step 2A outputs are frozen by hash and re-marked read-only at freeze time.

## What Step 2B would need (not started)

An explicit authorisation by Igor; a decision on whether it follows the P1 adjudication; the registered five-category scheme as the only outcome vocabulary for A-to-B contrasts (model-to-model contrasts, outside the registered design, need their own agreed vocabulary); eligibility from the Step 1 register as filter (SC-C units only in a separately labelled sensitivity analysis); human review of the contested groups.

## Provenance of this stage

Step 2A was authorised after the verified recovery checkpoint (`G4_RECOVERY_AFTER_SHUTDOWN_2026-10-04.md`, recorded as a later provenance event; the Step 1 freeze is not altered). Guardrails in force: no agreement, improvement, regression or superiority calculation; Codex A's missing rejected/deferred candidates are not negative decisions; no commit, push, reset or branch change.
