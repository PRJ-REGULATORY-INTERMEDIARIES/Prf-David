# G4 Step 1 — gate decision

**Date:** 2026-10-04 · **Prepared by:** Claude Code (Sonnet 5.5) · **Authority for any further step:** Igor Caires Machado

## Status

**`G4_STEP1_FROZEN / STEP2_NOT_STARTED`**

Step 1 (claim extraction, normalisation, eligibility classification and freeze) is complete. Nothing in Step 1 matches claims across cells, calculates agreement, assigns an improvement or regression label, or compares Codex with Claude or Track A with Track B. **G4 Step 2 has not been started and is not authorised by this document.**

No significant source-boundary or normalisation inconsistency prevents completion, so `G4_STEP1_CONDITIONAL` is not reported. Conditions that remain open are carried forward below; none blocks the freeze.

## Results

| Required item | Result |
|---|---|
| Units extracted per cell | Codex A **24** · Codex B **29** · Claude A **28** · Claude B **31** (112 original units) + **2 `STEP0_DERIVED`** units (one per Claude cell) = 114 rows. Of the 112: 71 accepted relations, 23 configuration-level claims, 2 relation-level claims, 8 positional claims, 2 positive architecture claims, 6 stopping decisions |
| Units eligible for primary comparison | **105** (SC-A: 94 `YES`, 11 `YES_WITH_PERIPHERAL_FLAG`) |
| Eligible provisionally, pending human confirmation | **4** (2 SC-B: Claude B CL-P04-04, CL-P04-07; 2 `STEP0_DERIVED` core units) |
| Restricted to sensitivity analysis | **5** SC-C units — Claude A: R-P03-04, CL-P03-02, CL-P03-03; Claude B: R-P04-05, CL-P04-02. They cannot support a primary-comparison improvement claim |
| Material evidence-scope dependency | 5 (= the SC-C units); no unit inherits a material dependency from another; 11 `PERIPHERAL_INHERITED`, 1 `BORDERLINE_INHERITED` (CL-P04-07) |
| Peripheral observations preserved | 13 (including 4 'continuity' purpose-label units in Codex A/B: UPQ-01) |
| Unresolved provenance questions | **5**: UPQ-01 'continuity' label (4 Codex units); UPQ-02 referent of 'the list' (2 Claude B units); UPQ-03 Codex A no consultation record; UPQ-04 Codex B no consultation record; UPQ-05 Claude A/B reading beyond the frozen statements |
| Materiality questions flagged for adjudication | the 2 borderline referent units (does the Art. 23(1) second sentence only resolve a reference, or supply the operative coupling?); whether the stopping decisions SR-P03 and AD-P04 depend only peripherally on SC-C configurations; the derived cores; the peripheral 'continuity' label |
| Human-review requirements | Queue of **28** preserved: **7 priority-1** (5 SC-C units and 2 derived cores), 14 priority-2 (incl. all 8 central architecture decisions), 7 priority-3. P1 items carry exact frozen excerpts, the original and normalised claim, uncertainty, the non-frozen sentences in question (marked not frozen evidence) and the reason human judgement is required. **All P1 legal-validity issues remain pending human adjudication before final comparative scoring. No human decision exists or was simulated.** |
| Normalisation QA | 25 PASS, 0 FAIL, 1 informational (lexical coverage; mean 0.84; 6 units below 0.75 read manually; no meaning change found) — `G4_STEP1_QA_REPORT.md` |
| Freeze and integrity | The Step 1 outputs are frozen in `G4_STEP1_FREEZE_MANIFEST.csv` (SHA-256, read-only). The four experimental cells (Codex A 6 + Codex B 11 + Claude A 7 + Claude B 11 outputs), the common register and all Step 0 files were re-verified: **0 mismatches**, apart from `G4_AUTHORIZATION_DECISION.md`, which received the append-only Step 1 decision entry (its previous hash is recorded in the manifest) |

## Decisions applied

C1 `DOCUMENTED_SUPPLEMENTARY_AUDIT_WAIVER` (attempt failed 19:20 -03:00; no external file imported or reviewed; locally registered criteria authoritative) · C2 accepted limitation (Codex B auxiliary hash absent, individual hashes verified) · C3 local SC-A…SC-D dictionary approved with exact definitions preserved; relayed E0–E3 description compared and **not mapped** (partial correspondence; decision log N-14) · C4 `CONFOUNDED_INPUT` · C5 provenance recorded (Codex `gpt-5.6-terra`, effort High, Codex VS Code extension, CLI 0.159.2, other parameters `NOT_DOCUMENTED`; Claude `claude-sonnet-5-5` as separately self-reported) · C6 preliminary normalisation and screening only.

## Open conditions carried forward (not blockers for the freeze)

1. Human adjudication of the 7 P1 items before final comparative scoring; confirmation of the 2 SC-B units and 2 derived cores before they enter the primary set.
2. If the authenticated external specification is later supplied: verify its hash, import it unchanged, compare its definitions with the SC dictionary, and reconcile in a new, separately hashed file (the E0–E3 columns are kept apart for this purpose).
3. Codex sampling parameters and Claude sampling parameters remain `NOT_DOCUMENTED`.
4. The normalisation was performed by one AI executor and is not independently reviewed.

## What Step 2 would need (not started)

An explicit authorisation by Igor; a decision on whether Step 2 proceeds before or after the P1 adjudication; the pairing and classification rules of `G4_CLAIM_MATCHING_RULES.md` as reconciled with the original registered criteria (the five-category A-to-B scheme prevails for the reported outcome); the eligibility register as the filter (SC-C units only in a separately labelled sensitivity analysis).

## Guardrails that remain in force

No matching across cells; no agreement, improvement, regression or superiority calculation; no improvement label; Codex A's missing rejected/deferred candidates are not negative decisions; counts and length are not merit; agreement between AI systems is not legal validity; all frozen experimental artifacts and original SHA-256 values unchanged; no commit, push, reset or branch change.
