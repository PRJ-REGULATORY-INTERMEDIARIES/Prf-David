# Pre-execution context and contamination disclosure — Claude replication

**Experiment:** V8-COMP-01 / Cross-Model Replication (Claude)
**Written:** 2026-10-04T13:5x-03:00, before any Claude Track A or Track B analytical work.
**Status:** append-only. Later events are added below as dated addenda; nothing here is retrospectively edited.

## 1. Executing agent

- Orchestrating agent: Claude Code (VS Code native extension, Windows 11 Pro), model self-identification from the system prompt: **Sonnet 5.5, model ID `claude-sonnet-5-5`**.
- No temperature, seed, top-p or other sampling parameter is exposed in this environment; they are therefore **not recorded and not controlled**.
- Git HEAD at start: `ae1af320b1f952a0e2fdd0d2142caf5d3886db46`, branch `main`. No commit/push/reset/branch operation is performed by this replication.

## 2. Codex results or summaries present in my initial context

Items present before I opened any project file:

1. **Git status snapshot** (system-provided): names of untracked top-level folders/files, including `V8_COMP_01_2026-10-04/`, `COMPARATIVE_PILOTS/`, `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/`, `R4_CROSS_DOMAIN_VALIDATION/`, `RGAM/`. Names only.
2. **Last five commit subjects** (e.g. "Document V6 foundational scientific review and empirical protocol"). None contains V8-COMP-01 analytical content.
3. **The user's pasted message** (a message from another AI assistant to the user). It states the 2×2 design and the replication prompt. It says Codex Track A is "concluded and frozen" and asks to "verify whether Codex Track B finished". It contains **no Codex finding, coding, relationship, configuration or inference**. It also contains design-level speculation (e.g. that the eight operations might increase cross-model convergence) which I treat as a hypothesis, not a result.
4. **Persistent-memory directory**: I did not read it in this session; I am not aware of any memory entry about V8-COMP-01.

Conclusion for item 2: **no Codex analytical result, conclusion or summary was available in my initial context.**

## 3. Contamination events that have already occurred (transparent record)

All events occurred in this orchestrating session before the subagents below are launched.

| # | Event | Content exposed | Assessment |
|---|---|---|---|
| C1 | `find COMPARATIVE_PILOTS -maxdepth 3` listing | **File names only** of the Codex outputs: `TRACK_A/TRACK_A_CODING.csv`, `…_RELATIONSHIPS.csv`, `…_UNCERTAINTY_REGISTER.csv`, `…_CONFIGURATIONS.md`, `…_ARCHITECTURAL_INFERENCES.md`, `…_QA_REPORT.md`, freeze manifests; and for Track B: `TRACK_B_OPERATION_REGISTER.csv`, `…_POSITIONAL_ANALYSIS.md`, `…_PART_WHOLE_ANALYSIS.md`, `…_SENSITIVITY_ANALYSIS.md`, `…_EXECUTION_LOG.md` etc.; also `01_MDR/MDR_TRACK_A_V8_ONLY.md`, `MDR_TRACK_B_V8_PLUS_8OPS.md`, `MDR_A_B_COMPARISON.md`. | Reveals that Codex Track B exists and its deliverable structure (which mirrors the eight operations of the shared protocol anyway). No file content was opened. Low contamination risk; recorded. |
| C2 | `find … -iname "*V8*"` | Names of the same MDR files plus `PILOT03_TO_V8_CROSSWALK.csv`. | Names only. |
| C3 | Directory listing of the whole project root | Names of historical folders. | Names only. |

**Files whose contents I did NOT open:** everything under `TRACK_A/`, `TRACK_B/`, `01_MDR/`, `QA/`, `RUN_LOGS/`, `TEAM_FEEDBACK/`; `EXECUTION_LOG.md`, `README.md`, `UPDATED_RESPONSE_REGISTER.md`, `V8_COMP_01_NEXT_GATE_REPORT.md`, `RESPONSE_AND_DECISION_REGISTER.md`; the PILOT_03 historical Model A/B and adjudication files; the `CODEX_ROTEM_SHARE_PACKAGE_*` and `ENVIO_R4_*` folders.

## 4. Files whose contents I did open (authorised inputs only)

| File | Role |
|---|---|
| `COMMON_STATEMENT_REGISTER.csv` | frozen common evidence (SHA-256 verified = `417A35A3…EF3E77F`) |
| `COMMON_STATEMENT_FREEZE_MANIFEST.csv`, `FROZEN_EVIDENCE_MANIFEST.csv`, `SOURCE_INTEGRITY_RECHECK.csv` | hash/provenance |
| `COMMON_STATEMENT_DATA_DICTIONARY.md` | shared protocol |
| `RESEARCH_PROTOCOL_v0_1.md` | shared protocol, contains the eight-operation specification |
| `COMPARISON_EVALUATION_CRITERIA.md` | pre-registered evaluation criteria |
| `G2_TRACK_A_EXECUTION_PROMPT.md` | the original *prompt* for Track A (instruction, not output) |
| `RGAM/V8_ACTIVE/00_PROJECT_CONTROL/V8_CONCEPTUAL_BASELINE.md`, `01_THEORETICAL_FRAMEWORK/V8_ANALYTICAL_STRUCTURE.md`, `02_CODING_ONTOLOGY/V8_CODEBOOK.md`, `INFERENCE_RULES.md`, `RELATIONAL_MODEL.md` | V8 conceptual framework and operational support |
| `RGAM/V8_ACTIVE/05_CONCEPTUAL_ARTICLE/FOUNDATIONAL_PREPAPER_V8.md` | project method hypothesis article (describes the eight operations; includes a GDPR worked trace, a different case) |
| `AUTONOMOUS_ROTEM…/01_BASELINES/official_texts/31991L0263.txt` (partial, grep) and hash-checks of `.html`/`.txt` for P03, P04 | primary legal text |

## 5. Residual contamination routes to be noted

- **R1 — input-level steering.** The frozen register's `segmentation_rationale`, `uncertainty_flag` and `human_review_status` columns contain interpretive cautions (e.g. "no designation relationship is inferred"). They are part of the shared frozen input and are identical for every executor; they may nevertheless steer any model toward conservative coding. Both tracks receive them. To be assessed at comparison time.
- **R2 — protocol-level knowledge shared across tracks.** The orchestrating context has read both the V8 material and the eight-operation specification. Tracks are executed by fresh subagents whose prompts I write; the Track B prompt will contain **no Track A content**.
- **R3 — same-model dependence.** Track A, Track B and the orchestrator are instances of the same model family; track independence is *context* independence, not *model* independence. This is inherent to the within-Claude contrast.
- **R4 — orchestrator knowledge of design hypotheses.** I know the cross-model convergence hypothesis from the pasted message. The prompts will not mention it.
- **R5 — filesystem visibility.** Subagents can technically list directories containing Codex outputs. Prompts forbid it and give explicit allow-lists, but compliance is self-reported by the subagent and checked only through its log. It cannot be technically enforced here.

## 6. Isolation plan

1. Track A: executed by a **fresh subagent** (no conversation history), explicit allow-list, forbidden-path list, writes only to `CLAUDE_TRACK_A/`.
2. Orchestrator hashes and freezes Track A (SHA-256 manifest), without feeding Track A content into any later prompt.
3. Track B: executed by a **second fresh subagent**, allow-list excludes `CLAUDE_TRACK_A/`, writes only to `CLAUDE_TRACK_B/`.
4. Orchestrator hashes and freezes Track B, writes the completion report, and **stops before any cross-model comparison**. The orchestrator will read the Claude outputs only to verify file presence, schema and hash, not to compare them with Codex.

**Limitation stated in advance:** a single physical Claude Code session cannot guarantee the separation of separate sessions; the subagent design is the best available approximation here. A user wanting stronger isolation can re-run each track in a manually opened new session using the saved prompts in this folder.

---
## Addendum 1 — 2026-10-04T14:31-03:00 (written after both tracks were executed; append-only)

**Execution events**

- 13:54–14:08 Track A executed by fresh subagent `ab19befdf44971c05` using `01_TRACK_A_AGENT_PROMPT.md`. Frozen 14:09:29 (second manifest, see A-1).
- 14:10–14:30 Track B executed by a second fresh subagent `a68b796a1560a4bc8` using `02_TRACK_B_AGENT_PROMPT.md`. Frozen 14:30:36.
- Before and after Track B, Track A hashes were re-verified: all 7 outputs and the manifest matched. Track A was not modified by Track B.
- The orchestrator did not open the content of any Track A or Track B analytical file before the Track B prompt was written and the Track B subagent had finished (it opened only the Track A execution log's "contamination events" and "model identification" lines, plus CSV row counts, after Track A finished; the Track B prompt was written afterwards but contains no Track A content and was authored from the pre-existing protocol only). After both tracks finished the orchestrator read only the deviation/contamination/timing lines of the two logs and structural counts of the CSVs, for the completion report.

**Additional contamination events (C4–C6)**

| # | Event | Assessment |
|---|---|---|
| C4 | **Track B subagent saw the folder name `CLAUDE_TRACK_A`** in the environment header (the orchestrator's shell working directory was `…\CLAUDE_TRACK_A` when the subagent was launched). Name only; the subagent reports it did not open, list or write there. | Orchestrator error. Names the existence of Track A, not content. Low risk for analytic independence; it should be weighed by readers. Track A files were read-only and hash-verified unchanged afterwards. |
| C5 | Track A and Track B subagents both saw, inside allowed files, the *names* of historical PILOT_03 Model A/B and adjudication files and of the eight-operation protocol (manifests, data dictionary, G2 prompt) and the register's `human_review_status` labels. Track A also saw the names of "Track B" and "eight-operation". Neither opened any of them. | Names only. |
| C6 | Both subagents saw text beyond the 20 statements inside the allowed official texts (e.g. Article 22(7) text near 22(5)–(6)); neither used it to code. | Recorded in each execution log. |

**Process errors by the orchestrator (disclosed, no retroactive change to any analytic file)**

- A-1: The first Track A freeze manifest (14:09:10) wrongly listed itself because of a shell-glob error, and the read-only attribute step failed. I overwrote the two manifest files at 14:09:29 with a correct manifest (7 analytic files; manifest excluded from its own list). The 7 analytic outputs' hashes were identical in both versions. No analytic file was changed.
- A-2: A `Remove-Item` attempt in PowerShell was blocked by the harness (path-parsing); it removed nothing.
- A-3: `.git/FETCH_HEAD` was modified during the session; I ran no git fetch. I attribute this to the editor's background fetch. HEAD (`ae1af32…`) and tracked files unchanged.

**Not guaranteed**

- Isolation between the tracks is context isolation of fresh subagents of the same model; it is not equal to two separately opened human-operated sessions.
- Subagent compliance with the allow-list is self-reported in each log and cannot be technically verified here.
