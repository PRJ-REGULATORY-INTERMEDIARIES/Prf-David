# V8-COMP-01 — G3C closeout report

**Date:** 2026-10-04 · **Mode:** sequential, no parallel agents · **Git:** no commit, push, reset or branch change
**G3C status: `G3C_CONDITIONAL_PASS` · G4 status: `G4_PENDING_DOCUMENTARY_RESOLUTION`**
**G4 substantive comparison: NOT started.** No cross-arm claim matching, classification or merit judgement was made.

## 1. Result in one paragraph

All four frozen cells exist, their individual analytic-output hashes were recalculated locally and match their own freeze manifests (Codex A 6/6, Codex B 11/11, Claude A 7/7, Claude B 11/11), they use the same 20 statement IDs (P03 = 6, P04 = 14), and the shared register and both official legal HTML files are unchanged. Local verification therefore reproduces the external audit's reference counts. The closeout is a **conditional** pass because three documentary conditions remain open: the external G3C package (and the G4 spec draft) could not be located; the Codex Track B auxiliary self-hash file is absent; and two scope/method confounds (evidence boundary; differing method-input documents) require recorded decisions before systematic matching.

## 2. Task-by-task

| Task | Outcome |
|---|---|
| 1 Locate and register the audit package | **Not located** (project root to depth 8, Downloads, Desktop, Documents, OneDrive, all zips in Downloads). Folder `G4_COMPARISON_PREPARATION/` created; nothing recreated as if external. Limitation recorded (P-01). |
| 2 Verify the four cells | Done. See §3 and `FOUR_CELL_FINAL_INTEGRITY_MANIFEST.csv` (one row per file: registered vs recalculated hash, status, size, modification time). |
| 3 Documentary pendencies | A: unresolved auxiliary-chain limitation, separately recorded (P-02). B: resolved (P-03). C: registered; uniform evidence-scope rule fixed (P-04, matrix §1). |
| 4 Execution limitations | Consolidated in `CROSS_MODEL_PROTOCOL_DEVIATIONS.md` (15 items; Claude C1–C6 preserved; exposure categories distinguished; not treated as covariates). |
| 5 G4 evaluation rules | `G4_FINAL_EVALUATION_MATRIX.md` (dimensions A–I, evidence-scope rule) and `G4_CLAIM_MATCHING_RULES.md` (procedure, seven labels, decision order, protocol mapping). Finalised before matching; not blind (see deviations §6). |
| 6 Human review | `G4_HUMAN_REVIEW_TEMPLATE.csv` (Tier 1: 8 anonymised case-level architecture decisions, shuffled with seed 20261004, identical legal evidence per case), `G4_HUMAN_REVIEW_INSTRUCTIONS.md`, and `G4_HUMAN_REVIEW_MAPPING_KEY_SEALED.csv` held separately. No human evaluation was generated. |

## 3. Four-cell verification (local recalculation, 2026-10-04)

| Cell | Analytic outputs | Registered = recalculated | Manifest control | Statement IDs |
|---|---|---|---|---|
| Codex Track A | 6 | **6/6 MATCH** | manifest hash = `TRACK_A_FREEZE_MANIFEST_SHA256.txt` (`695AC62F…E0D8`) ✔ | 20 = register |
| Codex Track B | 11 | **11/11 MATCH** | manifest self-hash file **absent** (P-02); current manifest hash `5204962C…962F` is an observation only | 20 = register |
| Claude Track A | 7 | **7/7 MATCH** | manifest hash = SHA256 file (`6756277B…10E9`) ✔ | 20 = register |
| Claude Track B | 11 | **11/11 MATCH** | manifest hash = SHA256 file (`BD1708B0…6F1A`) ✔ | 20 = register |

Also verified: the register (`417A35A3…EF3E77F`), P03 HTML (`01D5BDB1…6888`) and P04 HTML (`62AFB4DD…1449`) match the expected values; the Codex manifests' input rows (V8 baseline, codebook, inference rules, relational model, G2/G3 prompts, criteria) match, except TBF-010, which was recorded as `UNVERSIONED_SUPPORT_READ` (no hash at the time; hash now `9CBFF38C…00EC`) — see P-06. The `TRACK_A.zip` / `TRACK_B.zip` entries are byte-identical to the current files, which is a weak independent anchor. Source-file modification times place all four cells' outputs after the register (12:45) and in the order Codex A → Codex B → Claude A → Claude B (A frozen before B inside each arm).

## 4. Evidence for the selected status

**Supports closing:**
- All 35 analytic outputs across the four cells (6 + 11 + 7 + 11) re-verified; no mismatch.
- Common input identical and unchanged; legal HTML identity/version consistent with registration.
- Track A frozen before Track B in both arms; Claude Track A re-verified after Track B.
- Limitations are documented by the executors themselves (Codex: non-blind; Claude: context-only isolation, contamination log).

**Why it is not `G3C_CLOSED / G4_READY`:**
1. The external audit package and G4 spec draft are missing, so the required supplementary-evidence registration and the reconciliation of the draft with the finalised rules cannot be done (P-01).
2. The Codex Track B freeze chain has an unresolved auxiliary-file gap (P-02). It does not affect individual file hashes, but it leaves the manifest unanchored by its original self-hash.
3. The evidence-scope ambiguity (P-04) and method-input non-identity (P-06) can change how individual claims are classified; both need an explicit decision by Igor (uniform rule confirmed; confounds treated as limitation or re-run) before systematic matching, although defaults are specified.

**Why it is not `G4_BLOCKED`:** no integrity failure, no source mismatch, no ID mismatch, no unrecoverable gap; every open item has a stated resolution or an explicit "accept as limitation" path.

## 5. Remaining limitations (carried into G4)

Exploratory design with two microcases; no causal identification of model or method; not blind or preregistered in the strict sense; cell outputs differ in schema and candidate-listing policy, so counts are non-comparable; evaluator role conflict (the Claude-arm orchestrator is also the closeout agent); Codex model/version undocumented; Claude sampling parameters not exposed; no human reviewers named and no human ratings exist; agreement between systems is not legal validity.

## 6. Register updates

Append-only entries added to `EXECUTION_LOG.md`, `UPDATED_RESPONSE_REGISTER.md` and `RESPONSE_LOG.csv` (see their tails). Previous contents and the hashes of all frozen cell artifacts are unchanged.

## 7. Files produced (this folder)

`G3C_CLOSEOUT_REPORT.md` · `FOUR_CELL_FINAL_INTEGRITY_MANIFEST.csv` · `DOCUMENTARY_PENDING_ITEMS_REGISTER.md` · `CROSS_MODEL_PROTOCOL_DEVIATIONS.md` · `G4_FINAL_EVALUATION_MATRIX.md` · `G4_CLAIM_MATCHING_RULES.md` · `G4_HUMAN_REVIEW_TEMPLATE.csv` · `G4_AUTHORIZATION_DECISION.md` · supporting: `G4_HUMAN_REVIEW_INSTRUCTIONS.md`, `G4_HUMAN_REVIEW_MAPPING_KEY_SEALED.csv`, `G4_PREPARATION_HASH_MANIFEST.csv`.
