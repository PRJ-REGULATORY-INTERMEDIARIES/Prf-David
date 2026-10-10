# CLAUDE_REPLICATION_COMPLETION_REPORT

**Experiment:** V8-COMP-01 / Cross-Model Replication — Claude arm
**Date:** 2026-10-04 · **Report written:** 14:3x -03:00
**Status:** `CLAUDE_TRACK_A = FROZEN` · `CLAUDE_TRACK_B = FROZEN` · cross-model comparison **NOT performed** (stopped as instructed)

Folder: `COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04/CROSS_MODEL_REPLICATION/CLAUDE/`

## 1. Model and configuration

| Item | Value |
|---|---|
| Model (self-identification from system prompt) | Claude Sonnet 5.5, `claude-sonnet-5-5` |
| Further version/build | unknown (not exposed) |
| Harness | Claude Code, VS Code native extension, Claude Agent SDK, Windows 11 Pro |
| Sampling parameters (temperature, top-p, seed) | not exposed; not controlled; not recorded |
| Orchestrator | main Claude Code session |
| Track A executor | fresh subagent `ab19befdf44971c05`, same model as reported in its own log |
| Track B executor | fresh subagent `a68b796a1560a4bc8`, same model as reported in its own log |
| Human interventions | The user supplied the replication prompt and one additional methodological instruction mid-run (documentation of context and contamination). No human edit of any analytic output. |
| Prompts | saved verbatim: `PROMPTS_AND_LOGS/01_TRACK_A_AGENT_PROMPT.md`, `02_TRACK_B_AGENT_PROMPT.md` |
| Git | HEAD `ae1af320b1f952a0e2fdd0d2142caf5d3886db46`, unchanged; no commit/push/reset/branch operation |

## 2. Inputs and source hashes (verified by orchestrator and by each subagent)

| Input | SHA-256 | Result |
|---|---|---|
| `COMMON_STATEMENT_REGISTER.csv` | `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F` | MATCH expected |
| P03 `31991L0263.html` (FE-001) | `01D5BDB117B370AE9DAD7F3ABB151583A75519CBAD0E7808EFC9040C8D656888` | MATCH |
| P04 `32004R0874.html` (FE-003) | `62AFB4DDCCAE5E7157590B1386040AA8D160701D7194DBD2F2403AC4B6781449` | MATCH |
| V8 baseline `.docx` (FE-010) | `AC48C456B9AC0C0C162D0F882ABC645CAAA03FF1D94812C13DCBFD8DF1AD5074` | MATCH |
| V8 codebook / inference rules / relational model (FE-011) | `5DAC252E…FDAE` / `4A5DFE2D…7110` / `CC1AB37B…6F89` | MATCH |

Scope: 20 statements (P03 = 6, P04 = 14); P04 Art. 22(7) excluded. Register and sources unmodified.

## 3. Completion status

### Track A (V8 only) — **COMPLETE, FROZEN 2026-10-04T14:09:29-03:00**
Executed 13:54–≈14:08. Eight-operation protocol not used (declared in its log; its prompt excluded the protocol files).

| File | SHA-256 |
|---|---|
| CLAUDE_TRACK_A_CODING.csv | D844B68C436953B7243E8E254C8E77EDF498698377EE1AAF2803A1948CE5C3BB |
| CLAUDE_TRACK_A_RELATIONSHIPS.csv | 1D5C0301343A2054D626C289EE3EF25A78A93B2BA78F141E02BA18BD3F538915 |
| CLAUDE_TRACK_A_CONFIGURATIONS.md | EF39CCA5E12E38D437A81C0D9CC2D70540045B92C73F6B3B6A4E2BC97E0C4F80 |
| CLAUDE_TRACK_A_ARCHITECTURAL_INFERENCES.md | 482F2369900831858F2010AE9701741CF9D3AFD953ED4E9F159DFDB13227C548 |
| CLAUDE_TRACK_A_UNCERTAINTY_REGISTER.csv | 857619A9EC8AEE71FBF840B569CB98F9987B0FCA699D4E0CBC498AFF0D6CCC64 |
| CLAUDE_TRACK_A_QA_REPORT.md | 4EFDA7F6139E8E02ACD7A070E477675B1B62A86308CDC972149A7F2A60DDBB82 |
| CLAUDE_TRACK_A_EXECUTION_LOG.md | 546EE9BCE14D3D2D145E78C0F467BA5D60A61C0CB4FDB9164E32F45E1D7B6FC9 |
| CLAUDE_TRACK_A_FREEZE_MANIFEST.csv | 6756277B9BA129396CAAA4BF4C23CC3C66A79279794DDD6DF47467D50F1110E9 |

Manifest-of-manifest: `CLAUDE_TRACK_A_FREEZE_MANIFEST_SHA256.txt`. Files set read-only. Re-verified after Track B: all match.

### Track B (V8 + eight operations) — **COMPLETE, FROZEN 2026-10-04T14:30:36-03:00**
Executed 14:10:22–14:30:10, started only after Track A was frozen. All of O1–O8 recorded in `CLAUDE_TRACK_B_OPERATION_REGISTER.csv` (8 rows).

| File | SHA-256 |
|---|---|
| CLAUDE_TRACK_B_CODING.csv | E337B62EFC39DB6FED5FF8F6D7836AFF92C28AB7DE16CD407E038B72BA724095 |
| CLAUDE_TRACK_B_RELATIONSHIPS.csv | 7E86AF26A929B4111220309CC68C0F23B3BD4C1DD0FCD674B886E53A3125B24F |
| CLAUDE_TRACK_B_OPERATION_REGISTER.csv | F0C5993D19AB06A4B5D6D443FF57C9DB179906BCF1866CE25E0C789BA149A8C4 |
| CLAUDE_TRACK_B_CONFIGURATIONS.md | 066415156174D435152CA99237F2FB363F83DACE07334DE3E3C62216DFD7738F |
| CLAUDE_TRACK_B_POSITIONAL_ANALYSIS.md | 64CACD91045612DF94848F05753A8C99C59099C1DED6BAAD209D6004E73D8642 |
| CLAUDE_TRACK_B_PART_WHOLE_ANALYSIS.md | A1BB78D688724B538DF02FD80C513566A798935FC858B598D1020E669C38EB8E |
| CLAUDE_TRACK_B_SENSITIVITY_ANALYSIS.md | 4A302EC365BCCA837B2BAE185E9CBCC9B3602803F1B0D6D6416085C953F05C4C |
| CLAUDE_TRACK_B_ARCHITECTURAL_INFERENCES.md | AF987497C979EA61A1C4147A8470403111B916EA16F9841BD80D7484E34115C8 |
| CLAUDE_TRACK_B_UNCERTAINTY_REGISTER.csv | 83CE72B86BDEFFC13F937AB8EECFD9941C3223356D6C8CDD30664312B576B8E2 |
| CLAUDE_TRACK_B_QA_REPORT.md | EA09FD337ED856019C1BFE8CD866D62CA064550A36701474F128D2B06ED40C11 |
| CLAUDE_TRACK_B_EXECUTION_LOG.md | B45CA5B60A7A79804B386ACB203CC6130C0BAC9E2ECF439F5164B4B883AEE734 |
| CLAUDE_TRACK_B_FREEZE_MANIFEST.csv | BD1708B0E0FD5D6B65513F7373F782D231BB8BA4A658D3056C2E703A8D926F1A |

Manifest-of-manifest: `CLAUDE_TRACK_B_FREEZE_MANIFEST_SHA256.txt`. Files set read-only.

### Structural counts (descriptive only, no interpretation)
| | Track A | Track B |
|---|---|---|
| Statements coded | 20 | 20 |
| Candidate relationships | 34 (19 accepted / 8 rejected / 7 deferred) | 32 (19 / 8 / 5) |
| Statement-level decisions | 18 accepted, 2 deferred | 17 accepted, 1 assignment-only, 2 deferred |
| Uncertainty entries | 30 | 34 |
| Execution time (subagent clock) | ≈ 14–16 min | ≈ 20 min |

These counts are **not** evidence of method superiority (see criteria: length and category count are not merit).

## 4. Protocol deviations and process errors

1. **Isolation is by fresh subagent contexts, not by manually opened separate sessions** (see §5).
2. **Orchestrator error — C4:** the Track B subagent saw the *folder name* `CLAUDE_TRACK_A` in its environment header because my shell working directory was inside it when launched. No Track A content was opened (self-reported; Track A files were read-only and hash-verified unchanged afterwards).
3. **Orchestrator error — A-1:** first Track A freeze manifest (14:09:10) listed itself by glob mistake and the read-only step failed; corrected at 14:09:29. All 7 analytic hashes identical in both. No analytic file changed.
4. Subagents wrote scratch files (V8 manuscript text extraction, CSV-builder scripts) in the session scratchpad, outside the project.
5. Both subagents saw text beyond the 20 statements in allowed official texts (e.g., Art. 22(7) neighbouring 22(5)–(6)); none was used to code. Track A did not read the manuscript's regime/governance-logic sections in full.
6. Track B log: sensitivity (O8) results were used to correct relation counts in the operation-register *text*; no analytic decision changed after O8 (self-reported).
7. Orchestrator read, after Track A finished and before launching Track B, only that log's contamination/model lines and CSV row counts; the Track B prompt was written from the pre-existing protocol and contains no Track A content. This is a weak but real route of orchestrator-level contact; disclosed in addendum 1.
8. `.git/FETCH_HEAD` changed during the session without any fetch by me (editor background activity presumed). No tracked file or HEAD change.
9. Files of the Codex experiment: I opened none of `TRACK_A/`, `TRACK_B/`, `01_MDR/`, `QA/`, `RUN_LOGS/`, historical PILOT_03 Model A/B/adjudications. I saw their **file names** in two directory listings (C1–C3 in the disclosure). No file under the experiment folder other than my own CLAUDE folder was created or modified (checked by modification-time scan).

## 5. Limitations of execution independence

- **Context independence only.** Both tracks and the orchestrator are the same model. Track B's independence from Track A is that of a cold-start context; nothing prevents shared latent habits of the same model.
- **Self-reported compliance.** Allow-list compliance of each subagent rests on its own log; filesystem access could not be technically blocked.
- **Shared frozen input steering.** The common register includes `segmentation_rationale`, `uncertainty_flag` and `human_review_status` fields with cautionary wording; both tracks (and presumably the Codex arm) received them. They may reduce variance across executors.
- **V8 support documents contain method-layer elements.** The V8 codebook/baseline mention a property-bearer / boundary-sensitivity layer (`METHOD_HYPOTHESIS`). Track A was told to use V8-defined and operational elements only and not to run it as a procedure. Whether Track A is a "pure V8" arm is therefore an interpretation to examine at comparison time.
- **Track B's operation register** records contribution *as observed within Track B*; it cannot establish the counterfactual relative to Track A (Track B did not see A).
- **Not human validation.** Nothing here is independent human legal validation, and no claim of superiority of either method is made.
- Orchestrator-written prompts for A and B are structurally parallel but not identical; differences (allow-list, deliverables) follow the protocol and are visible in the saved files.

## 6. Readiness for subsequent cross-model comparison

Ready on the Claude side: both tracks frozen, hash manifests present, logs retained, contamination disclosed, source integrity confirmed.

Preconditions still open (outside this report's scope): (a) verify Codex Track B completion and hashes; (b) agree the comparison matrix (agreement, legal validity, traceability, analytic cost, independent human review); (c) decide how to treat contamination C1–C6 in the comparison (recommended: keep as a covariate note); (d) if stronger independence is wanted, re-run each Claude track in manually opened, separate sessions using the saved prompts and compare with these runs as a test–retest of the Claude arm.

**STOPPED. No comparison of Claude results with Codex results, or with each other beyond the structural counts above, was performed.**

## 7. Index of retained records

- `PROMPTS_AND_LOGS/00_PRE_EXECUTION_CONTEXT_AND_CONTAMINATION_DISCLOSURE.md` (with Addendum 1)
- `PROMPTS_AND_LOGS/01_TRACK_A_AGENT_PROMPT.md`, `02_TRACK_B_AGENT_PROMPT.md`
- `CLAUDE_TRACK_A/…_EXECUTION_LOG.md`, `CLAUDE_TRACK_B/…_EXECUTION_LOG.md`
- `CLAUDE_REPLICATION_MANIFEST.csv` (hashes of this report, the prompts and the disclosure)
