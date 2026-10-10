# G4 recovery verification after computer shutdown

**Date:** 2026-10-04 · **Verification run:** 2026-10-04T20:42:53 -03:00 · **Executor:** Claude Code (Sonnet 5.5), new session, **read-only** (no file was modified, regenerated or re-attributed; this is the only file created)
**Result:** **`RECOVERY_VERIFIED / G4_STEP1_FROZEN / STEP2_AWAITING_AUTHORIZATION`**

The experiment was **not restarted**. G4 Step 0 and Step 1 were not rerun; G4 Step 2 was not started; no claim matching, scoring or cross-model comparison was performed; no Git commit, push, reset or branch change.

## 1. Last completed stage

G4 Step 1 (claim extraction, normalisation, eligibility, freeze), frozen 2026-10-04T19:31:12 -03:00 with status `G4_STEP1_FROZEN / STEP2_NOT_STARTED` (documents read in this session: `G4_STEP1_GATE_DECISION.md`, `G4_STEP1_QA_REPORT.md`, `G4_STEP1_FREEZE_MANIFEST.csv`, `G4_STEP1_FREEZE_MANIFEST_SHA256.txt`, `G4_AUTHORIZATION_DECISION.md`). The last file written in the project tree was the freeze manifest pair at 19:31:12; **no project file was modified after that moment** (modification-time scan, excluding `.git`).

## 2. File-integrity results after reboot

| Check | Result |
|---|---|
| Step 1 freeze manifest SHA-256 recalculated | `0DEC88FFF9CF9D5B53DAC593AA54368FA7E59DED55D7AFE9E186A3AB7150DD0B` = expected value **MATCH**; equals the value in `G4_STEP1_FREEZE_MANIFEST_SHA256.txt` **MATCH** |
| Manifest rows recalculated | **31 of 31 MATCH, 0 mismatches, 0 missing** (7 Step 1 outputs; 4 appended registers; 9 reference inputs; 11 frozen cell source files) |
| Seven analytical outputs of Step 1 | All **present** and hash-verified: `G4_STEP1_NORMALIZED_CLAIMS.csv` (`EFFCD825…9FB6`), `G4_STEP1_DATA_DICTIONARY.md` (`94A1033A…EDAD`), `G4_STEP1_NORMALIZATION_DECISION_LOG.md` (`1745BF17…54F9`), `G4_STEP1_ELIGIBILITY_REGISTER.csv` (`68672E8A…1095`), `G4_STEP1_HUMAN_REVIEW_QUEUE.csv` (`4769B548…DC9B`), `G4_STEP1_QA_REPORT.md` (`042915C0…FCD9`), `G4_STEP1_GATE_DECISION.md` (`B455B7CE…3E08`); plus the manifest and its SHA-256 file |
| Claude Track A (7 outputs) and Track B (11 outputs) | **18 of 18 MATCH** their freeze manifests; both manifests match their SHA-256 files |
| Codex Track A (6 outputs) and Track B (11 outputs) | **17 of 17 MATCH** their freeze manifests; Codex A manifest matches its SHA-256 file |
| Common statement register | `417A35A3…EF3E77F` **MATCH** (expected) |
| Official legal HTML | P03 `01D5BDB1…6888` **MATCH**; P04 `62AFB4DD…1449` **MATCH** |
| Step 0 files | All 21 listed in the Step 0 manifest present; the only differences from Step 0 values are the four register-type files that Step 1 appended to (`G4_AUTHORIZATION_DECISION.md`, `EXECUTION_LOG.md`, `UPDATED_RESPONSE_REGISTER.md`, `RESPONSE_LOG.csv`); their **current hashes equal the post-append values recorded in the Step 1 manifest** |
| Older G3C manifest | Differs only for the five files that were legitimately appended after it (pending-items register, authorisation decision and the three main registers), as expected |
| Unexpected files in `G4_COMPARISON_PREPARATION/` | None (28 files; no temporary or hidden leftovers) |

## 3. Missing or altered artifacts

- **Missing:** none among the manifest files.
- **Altered content:** none.
- **Known historical absence (unchanged, accepted under C2):** Codex Track B `TRACK_B_FREEZE_MANIFEST_SHA256.txt` is still absent; the Codex B manifest hash as it stands is `5204962C…962F` (an observation, not an original record).
- **Metadata observation (not a content alteration):** the **read-only attribute** that was set on the Step 1 outputs and on the Claude cell outputs at freeze time is **no longer set** (the nine Step 1 files and all 18 Claude cell files are writable). Hashes are intact, so the content is unchanged. The most likely cause is the cloud-drive synchronisation or the reboot (not established). **Not corrected** in this read-only task; re-applying the attribute is a metadata-only action that Igor may authorise, and it would not change any hash.
- **Session notices:** the editor reported several documents as "changed on disk" at session start. All affected files are ones appended or corrected by the previous session; each was hash-verified against its manifest (the Step 1 manifest for appended registers; the Step 0 manifest for the Step 0 documents), and none differs.

## 4. Git working-tree status (read-only commands)

| Item | Value |
|---|---|
| Branch | `main` |
| HEAD | `ae1af320b1f952a0e2fdd0d2142caf5d3886db46` ("Document V6 foundational scientific review and empirical protocol") — unchanged since the first session of the day |
| Tracked-file changes | **0** |
| Untracked entries | **26** — the same 26 entries as in the initial git status snapshot of the session (including `COMPARATIVE_PILOTS/`) |
| Stashes | 0 |
| Merge / rebase / cherry-pick / revert markers; lock files | none |

No commit, push, reset or branch operation was made at any stage of V8-COMP-01 by this agent.

## 5. Outstanding methodological questions (carried unchanged from the Step 1 gate)

1. **Human adjudication** of the 7 priority-1 items (5 SC-C units and 2 `STEP0_DERIVED` cores) before any final comparative scoring; no reviewers have been named; no human decision exists.
2. Confirmation of the **2 SC-B units** (Claude B CL-P04-04, CL-P04-07): does the Art. 23(1) second sentence only resolve a referent or supply the operative coupling? (UPQ-02).
3. Whether the negative stopping decisions **SR-P03** (Claude A) and **AD-P04** (Claude B) depend only peripherally on SC-C configurations (judgement preserved from Step 0; flagged for review).
4. Provenance of the **'continuity' purpose label** in the Codex escrow configuration and architecture claims (UPQ-01); cell-level provenance gaps UPQ-03, UPQ-04, UPQ-05.
5. **External specification** unavailable (waiver in force); the E0–E3 description relayed through ChatGPT is unauthenticated and not mapped; reconciliation only if the authenticated file is supplied.
6. Sampling parameters of both Codex and Claude remain `NOT_DOCUMENTED`; the crossed comparison remains `CONFOUNDED_INPUT` and exploratory.
7. The normalisation was produced by one AI executor and has not been independently reviewed.
8. Open decision: whether a future Step 2 should run before or after the P1 adjudication.

## 6. Handling of the main registers

This recovery entry was **deliberately not appended** to `EXECUTION_LOG.md`, `UPDATED_RESPONSE_REGISTER.md` or `RESPONSE_LOG.csv`: appending would change their hashes, which the Step 1 manifest records, and the task required a read-only recovery. If Igor wishes a register entry, it should be added as a separate, dated, append-only step with the new hashes recorded.

## 7. Exact next authorised step

**None beyond awaiting Igor's decision.** The recovery confirms that G4 Step 1 can be safely resumed from its frozen state. The next step requires an explicit authorisation by Igor of one of:

- **G4 Step 2** (pairing and classification under the matching rules as reconciled with the original registered criteria, with the eligibility register as filter; SC-C units only in a separately labelled sensitivity analysis), with the decision on its ordering relative to the P1 human adjudication; or
- **Preparatory actions that do not touch frozen content**: naming human reviewers and running the P1 adjudication; re-applying the read-only attribute to the Step 1 outputs and Claude cell outputs; supplying the authenticated external specification.

Until then the state is `G4_STEP1_FROZEN / STEP2_AWAITING_AUTHORIZATION`.
