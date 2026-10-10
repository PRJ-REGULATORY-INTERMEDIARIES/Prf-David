# G4 authorization decision

**Experiment:** V8-COMP-01 · **Date:** 2026-10-04 · **Prepared by:** Claude Code (Sonnet 5.5) at G3C closeout
**Decision-maker:** Igor Caires Machado — **confirmation fields below are intentionally blank; this document records a recommendation, not Igor's decision.**

## Gate status

`G3C_CONDITIONAL_PASS` / `G4_PENDING_DOCUMENTARY_RESOLUTION`

G4 substantive comparison (cross-arm claim matching, classification, merit judgement) is **not authorized by this document and has not been started.**

## Basis (summary)

Integrity of the four cells confirmed by local recalculation (Codex A 6/6, Codex B 11/11, Claude A 7/7, Claude B 11/11); common register and legal HTML unchanged; identical 20 statement IDs. Open: P-01 external package and spec draft absent; P-02 Codex Track B auxiliary self-hash file absent; P-04 evidence-scope decision; P-06 method-input non-identity; P-07 Codex model undocumented. Details: `G3C_CLOSEOUT_REPORT.md`, `DOCUMENTARY_PENDING_ITEMS_REGISTER.md`.

## Conditions to move to `G4_READY` (each is an append-only decision by Igor)

| # | Condition | Options | Default if Igor only says "proceed" |
|---|---|---|---|
| C1 | External G3C package and G4 spec draft | (a) supply the zip → register with hashes and reconcile; (b) proceed without it | (b), with the finalised rules prevailing and the absence stated in any report |
| C2 | Codex Track B `…_SHA256.txt` (P-02) | (a) supply original; (b) accept as an unresolved auxiliary-chain limitation | (b) |
| C3 | Uniform evidence-scope rule E1/E1x/E2/E3 (P-04) | (a) confirm; (b) amend | (a) |
| C4 | Method-input non-identity (P-06) | (a) treat as documented limitation with `CONFOUNDED_INPUT` tagging; (b) authorise harmonised re-run (new artifacts, new freeze) | (a) |
| C5 | Codex model/version (P-07) | supply, or leave `NOT_DOCUMENTED` | leave |
| C6 | Evaluator plan (deviation D-15) | AI-assisted pass labelled preliminary + human review of flagged items, or human-first | AI-assisted preliminary, then human review |

If C1–C6 are resolved by defaults, no further documentary work is needed before G4 step 0.

## What would be authorized once conditions are met (G4, in order)

1. **Step 0 — scope tagging** of every cited relationship/claim in the four cells (E1/E1x/E2/E3/`SCOPE_NOT_DETERMINABLE`). No label comparison.
2. **Step 0.5** — reconcile with the external spec draft if supplied.
3. **Step 1–2 — claim extraction and normalisation** (Tier 2 added to the human instrument).
4. **Steps 3–6 — pairing, classification, human review queue**, per `G4_CLAIM_MATCHING_RULES.md`, results reported per case, per contrast family, per dimension, with `CROSS_MODEL_PROTOCOL_DEVIATIONS.md` attached.
5. Human review: at least two named reviewers; Tier 1 instrument ready now.

## Explicitly not authorized

Any composite score; use of relationship counts or length as merit; pooling P03 and P04; claims of legal validity from AI agreement; modification of any frozen artifact (including re-coding of R-P04-05); regeneration of the missing Codex self-hash file; commit, push, reset or branch change.

## Reporting rules for any G4 output

State: exploratory, two microcases, not blind prospective preregistration, evaluator role conflict, scope confounds, non-comparable counts, Codex model undocumented, no human validation unless collected.

## Confirmation (to be completed by Igor)

| Field | Value |
|---|---|
| Decision-maker | |
| Date | |
| C1 | |
| C2 | |
| C3 | |
| C4 | |
| C5 | |
| C6 | |
| Reviewers named | |
| Authorized next step | |

---
## Decision entry — 2026-10-04 (G3C decision registration and G4 Step 0; append-only)

**Source:** Igor's operational decisions C1–C6 as stated in the G3C decision-registration instruction of this session; registered by Claude Code (Sonnet 5.5). The confirmation table above (fields left blank at G3C closeout) is **not edited**; these entries supersede its default column.

| # | Decision | Status |
|---|---|---|
| C1 | External audit package: `INCORPORATE_AND_RECONCILE` | decided; **not executable**: package not found, hash `686E322F…FA99` unverifiable |
| C2 | Missing historical auxiliary SHA file: `ACCEPT_WITH_DOCUMENTED_LIMITATION` | executed |
| C3 | Common legal-evidence boundary: `APPROVED`, subject to semantic reconciliation of labels | approved; reconciliation pending the external definitions |
| C4 | Different prompts and method-support documents: `CONFOUNDED_INPUT`; no strong causal attribution to model or to the eight operations | in force |
| C5 | Codex model/version: final read-only provenance search | executed; found `gpt-5.6-terra`, reasoning effort high, Codex VS Code CLI 0.159.2, one session for Track A and Track B (external to cell artifacts) |
| C6 | Preliminary AI assessment authorised; human review for contested evidence, central architectural claims and final legal-validity conclusions | in force |

These decisions authorise preparation and evidence classification only. They are not approval of any conclusion favouring Track B.

**Outcome:** G4 Step 0 executed; gate status `G4_STEP0_CONDITIONAL` (see `G4_STEP0_GATE_DECISION.md`). **G4 Step 1 is not authorised by this entry.** The gate conditions S1–S3 in `G4_STEP0_GATE_DECISION.md` replace C1/C3/C6 defaults for the next decision.

---
## Decision entry — 2026-10-04 (G4 Step 1 authorisation; append-only)

**Source:** Igor's operational decisions C1–C6 as stated in the G4 Step 1 instruction of this session; registered by Claude Code (Sonnet 5.5). Earlier entries are not edited.

| # | Decision as given | Registration / status |
|---|---|---|
| C1 | External audit: attempt to incorporate the previously supplied external G4 operational specification if available; if unavailable proceed under `DOCUMENTED_SUPPLEMENTARY_AUDIT_WAIVER`. The locally registered original comparison criteria remain authoritative. Do not claim to have imported or reviewed an unavailable file. | **Attempt made 2026-10-04 19:20 -03:00 and failed**: `G3C_AUDIT_AND_G4_PREPARATION_2026-10-04.zip` (expected SHA-256 `686E322F7451B3050C85FCA394459FC1757AC09C0B7DBE7E5B39676FB102FA99`) and its three documents are absent from Downloads, the project tree and `G4_COMPARISON_PREPARATION/`. **`DOCUMENTED_SUPPLEMENTARY_AUDIT_WAIVER` is in force.** No external file was imported or read. |
| C2 | Missing Codex B auxiliary hash: `ACCEPT_WITH_DOCUMENTED_LIMITATION`; preserve individual file-integrity checks and the historical absence of the original auxiliary record. | Registered; `TRACK_B_FREEZE_MANIFEST_SHA256.txt` remains absent and is not regenerated. |
| C3 | Evidence-scope dictionary: `APPROVE` the local SC-A…SC-D dictionary for Step 1, preserving its exact registered definitions; keep unresolved classifications and borderline materiality questions flagged for adjudication. | Approved. Dictionary file `G4_EVIDENCE_SCOPE_DICTIONARY.md` unchanged (hash unchanged). |
| C3 (note) | The supplementary audit proposed, **as relayed through ChatGPT (not an authenticated incorporation of the unavailable file)**: E0 direct support from frozen evidence; E1 neighbouring official text used solely to resolve syntax or references without adding a legally operative premise; E2 additional substantive actor, authority, obligation, condition, counterpart, action or relationship obtained outside the frozen scope; E3 missing, unverifiable or unresolved provenance. | Recorded verbatim. Semantic correspondence **verified before any mapping** in `G4_STEP1_NORMALIZATION_DECISION_LOG.md` (decision N-14): correspondence is partial; **no mapping adopted**. |
| C4 | Different prompts and methodological materials: `CONFIRMED_AS_CONFOUNDED_INPUT`. Crossed comparison exploratory; do not attribute observed differences exclusively to model or procedure. | In force. |
| C5 | Codex provenance: model `gpt-5.6-terra`; reasoning effort High; environment Codex VS Code extension; CLI version `0.159.2`; unavailable parameters `NOT_DOCUMENTED`; preserve Claude Sonnet 5.5's separately reported configuration. | Updated in the provenance field of the Step 1 register: Codex = those values, other parameters `NOT_DOCUMENTED`; Claude = `claude-sonnet-5-5` as self-reported by orchestrator and each subagent, sampling parameters not exposed (`NOT_DOCUMENTED`). |
| C6 | Preliminary normalization and AI-assisted screening authorised; all priority-1 legal-validity issues remain pending human adjudication before final comparative scoring; no human assessment may be simulated. | In force. |

These decisions authorise Step 1 (extraction, normalisation, eligibility, freeze). They do not authorise claim matching, scoring, agreement, improvement, regression or superiority judgements, nor Step 2.

---
## Decision entry — 2026-10-04 (G4 Step 2A authorisation; append-only)

**Source:** Igor's authorisation of G4 Step 2A, given in the Step 2A instruction of this session after the verified recovery checkpoint (`RECOVERY_VERIFIED / G4_STEP1_FROZEN / STEP2_AWAITING_AUTHORIZATION`); registered by Claude Code (Sonnet 5.5). Earlier entries are not edited.

| Item | Decision / status |
|---|---|
| Authorised | G4 Step 2A **exclusively** for claim correspondence, grouping and documentary traceability, using `G4_STEP1_NORMALIZED_CLAIMS.csv` and the claim-matching rules. |
| Not authorised | Comparative scoring; superiority assessment; agreement scores; improvement, regression or any outcome label of the original five-category scheme; final legal-validity adjudication; cross-model or Track A/B conclusions; G4 Step 2B. |
| Controls | SC-A…SC-D classification and materiality restrictions preserved (5 material dependencies, 4 provisional units incl. 2 STEP0_DERIVED cores, UPQ-01…UPQ-05, original review priorities); `CONFOUNDED_INPUT` (C4) preserved; the seven P1 items remain pending actual human adjudication; no human assessment may be simulated. |
| Provenance | The recovery checkpoint (`G4_RECOVERY_AFTER_SHUTDOWN_2026-10-04.md`) is recorded as a later provenance event; the Step 1 freeze (manifest `0DEC88FF…DD0B`) is not altered. |
| Outcome | `G4_STEP2A_FROZEN / STEP2B_NOT_STARTED` (see `G4_STEP2A_GATE_DECISION.md`). Step 2B is **not** authorised by this entry. |
