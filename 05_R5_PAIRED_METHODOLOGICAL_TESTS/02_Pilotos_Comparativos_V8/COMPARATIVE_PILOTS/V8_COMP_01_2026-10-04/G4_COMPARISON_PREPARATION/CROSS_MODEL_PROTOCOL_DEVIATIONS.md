# Cross-model protocol deviations and execution limitations

**Experiment:** V8-COMP-01 · **Stage:** G3C closeout · **Date:** 2026-10-04 · **Append-only**
**Principle:** these are documented limitations of an **exploratory, two-microcase** study. They are **not** automatically treated as statistical covariates, and they do not support causal identification of model or method effects. This stage is **not** a fully blind prospective preregistration (see §6).

## 1. Deviation index

| ID | Deviation / limitation | Arm | Evidence |
|---|---|---|---|
| D-01 | Same researcher/computational environment executed Track A and Track B; Track B "procedurally separated at the document-input level but not genuinely blind" | Codex | `TRACK_B_EXECUTION_LOG.md`; `TRACK_B_QA_REPORT.md` |
| D-02 | Track A and Track B run by two fresh subagents of the same model, one orchestrator; isolation is context isolation; allow-list compliance self-reported and not technically enforced | Claude | disclosure file, completion report |
| D-03 | Orchestrator exposure events C1–C6 and process errors A-1…A-3 (§3) | Claude | disclosure file + Addendum 1 |
| D-04 | Codex Track B `…_FREEZE_MANIFEST_SHA256.txt` absent (auxiliary chain unresolved) | Codex | pending register P-02 |
| D-05 | Codex Track A: no execution/independence log | Codex | pending register P-08 |
| D-06 | Ambiguous evidence-scope rule in the original task statement; Claude Track B R-P04-05 uses non-frozen text; Claude cells carry other cross-provision uses; Codex scope not determinable from structure | both | pending register P-04 |
| D-07 | **Method-input non-identity**: different documents specified the eight operations and V8 support in the two environments | both | pending register P-06 |
| D-08 | **Prompt non-identity**: original G2/G3 prompts (Codex) vs orchestrator-written prompts with explicit allow/forbid lists (Claude); the Claude Track A prompt instructed not to run the method-hypothesis layer as a procedure | both | prompt files and manifests |
| D-09 | Codex model identity/version/parameters not documented in examined files; Claude sampling parameters not exposed | both | P-07 |
| D-10 | **Candidate-listing policy and schema differ**: Codex Track A relationship table contains accepted relations only (16 rows, no decision column); Codex Track B lists candidates with a disposition (23); Claude tables list every candidate with decision (34 and 32). Column schemas differ. Counts of relationships are **not comparable** | both | CSV headers |
| D-11 | Chronology: Codex A frozen 13:11, Codex B 13:43 (manifest times); Claude A 14:09, Claude B 14:30. Claude orchestration began after the Codex cells were frozen, but its orchestrator had received a description of the design | both | file times, manifests |
| D-12 | Shared interpretive metadata in the frozen register (`segmentation_rationale`, `uncertainty_flag`, `human_review_status`) | both | register |
| D-13 | Aggregate outcomes and audit findings known before the G4 matrix was finalised | G3C | §6 |
| D-14 | External G3C audit package and G4 spec draft unavailable | G3C | P-01 |
| D-15 | **Evaluator role conflict**: the session that orchestrated the Claude replication is also the G3C closeout session and has read all four cells' architecture-level text | G3C | §5 |

## 2. Codex environment — documented

- **Execution record:** Track A frozen 13:09:44 (manifest) / 13:11:02 (self-hash file); Track B frozen 13:42:38 (manifest timestamp), manifest file written 13:43:12.
- **Independence (from its own documents):** Track A analytic outputs were not opened by Track B; Track A freeze verified by manifest self-hash only; the same researcher/environment retained general project context; no claim of fully independent blinded replication.
- **Inputs recorded in manifests:** register, both official HTMLs, V8 manuscript, V8 codebook/inference rules/relational model; Track A also the G2 prompt; Track B also `ARCHITECTURAL_THEORY_AND_METHOD.md`, `CONFIGURATION_RECONSTRUCTION.md` (unversioned), `COMPARISON_EVALUATION_CRITERIA.md`, and the G3 prompt (attachment path under `.codex`). Historical PILOT_03 Model A/B and adjudications are reported as not used (QA report).
- **Not documented:** model identity/version/parameters; Track A process log; knowledge of the Claude arm (the Codex cells were frozen before the Claude run began).
- **Limitations claimed by Codex itself:** non-blind; separate folder does not eliminate it.

## 3. Claude environment — original C1–C6 preserved

The definitions below are quoted from `PROMPTS_AND_LOGS/00_PRE_EXECUTION_CONTEXT_AND_CONTAMINATION_DISCLOSURE.md` (SHA-256 of the file as recorded in `CLAUDE_REPLICATION_MANIFEST.csv`: `C71B3E1ADD9734909DB5E2DF50FBEE20174EB7C3CE3E5D6447D03E93B69CB4AA`; recalculated 2026-10-04: identical). They are **not** rewritten.

| # | Original definition (condensed without altering meaning) | Original assessment |
|---|---|---|
| C1 | `find COMPARATIVE_PILOTS -maxdepth 3`: file **names** of Codex Track A / Track B outputs and `01_MDR/…` files; no file opened | Reveals existence and deliverable structure of Codex Track B; low risk; recorded |
| C2 | `find … -iname "*V8*"`: names of MDR files and `PILOT03_TO_V8_CROSSWALK.csv` | Names only |
| C3 | Directory listing of the project root | Names only |
| C4 | Track B subagent saw the folder name `CLAUDE_TRACK_A` in the environment header (orchestrator's working directory) | Orchestrator error; names the existence of Track A, not content; low risk |
| C5 | Both subagents saw, inside allowed files, names of PILOT_03 Model A/B/adjudication files and of the eight-operation protocol, and the register's `human_review_status` labels; Track A also saw "Track B" and "eight-operation" by name | Names only |
| C6 | Both subagents saw text beyond the 20 statements in allowed official texts (e.g. Article 22(7) near 22(5)–(6)); neither used it to code | Recorded in each log |

Process errors: A-1 first Track A manifest listed itself, corrected 14:09:29 with no analytic file changed; A-2 blocked `Remove-Item` attempt (nothing removed); A-3 `.git/FETCH_HEAD` changed without a fetch by the agent.

### Classification of Claude exposure history (required distinction)

| Category | What | Where |
|---|---|---|
| **Confirmed content exposure** (Claude arm) | (i) The orchestrator and each subagent read the register, V8 materials, shared protocol, criteria and parts of the official texts; Track B also read `FOUNDATIONAL_PREPAPER_V8.md`, which contains a **worked example for a different case (GDPR)**; (ii) both subagents saw official text outside the 20 statements (C6), incl. Article 22(7); (iii) the Track B subagent read Article 12(5) third sentence and used it (P-04); (iv) the orchestrator, **before launching Track B**, read the Claude Track A log's contamination/model lines and CSV row counts only | logs, disclosure |
| **Folder-name exposure only** | C1, C2, C3 (Codex outputs names); C4 (`CLAUDE_TRACK_A` name to the Track B subagent); C5 (PILOT_03 and protocol names in manifests) | disclosure |
| **Potential procedural contamination** | Same orchestrator wrote both prompts and knew both methods; orchestrator read Track A log lines before writing the Track B prompt (the Track B prompt was authored from the pre-existing protocol and contains no Track A content, but this cannot be proved from the artifacts alone); shared session and filesystem; allow-lists self-reported | disclosure, prompts |
| **Shared interpretive metadata** | Register's `segmentation_rationale` / `uncertainty_flag` / `human_review_status` (cautionary wording identical for all four cells) | register |
| **Uncontrolled model parameters** | Claude: sampling parameters not exposed; subagent model ID self-reported as Sonnet 5.5; Codex: not documented | logs |
| **Execution environment limitations** | Claude Code in VS Code on Windows 11; subagents have no separate machine; Google-Drive-hosted workspace (modification times are mutable); no technical enforcement of read/write permissions between cells; read-only attributes set on Claude outputs only after each freeze | completion report |

### This G3C session's own exposure (disclosed now)
For integrity checks and claim extraction the G3C orchestrator opened: Codex freeze manifests and Track B execution log; limitation lines of both Codex QA reports; the two Codex method-specification files; CSV headers and cross-provision fields of the four relationship tables; the architecture-level inference text of **all four cells**; both Claude R-P04-05 relationship rows. The **headline architecture-level status of each cell is therefore known to this session**. No substantive comparison is made in G3C.

## 4. Non-comparabilities that must travel with any G4 result

- Relationship counts, acceptance rates, uncertainty counts and report length are **not comparable** across cells (D-10, D-07). They are descriptive only.
- Track B outputs include unit types (positional, part–whole, sensitivity) with no Track A counterpart by design.
- Claude A→B contrast is a within-model, same-orchestrator contrast with identical register; Codex A→B is a same-environment contrast; cross-model contrasts additionally differ in method documents (D-07) and prompts (D-08).
- Scope issues (D-06) can alter classification of individual claims; see matching rules (E3 → no improvement label).

## 5. Evaluator role conflict (D-15)

The Claude arm's orchestrator is also the G3C closeout agent. Any AI-assisted matching of Claude vs Codex claims by this session is therefore not independent of the Claude arm. Mitigations specified: AI-assisted classification is `PRELIMINARY_AI_ASSISTED`; evaluator exposure is logged; contested, regressive, improving and unresolved items go to human review; the human instrument keeps system identity in a sealed key.

## 6. Epistemic status of G4 preparation

- Before the evaluation matrix was finalised, the following were known to people involved: aggregate structure (counts) of Claude cells; the external audit's findings (via task text); Codex's non-blind statement; R-P04-05 issue; names of all cell files. The matrix and matching rules were then written **before** pairwise matching and before reading the architecture-level claims for extraction, but **not** before the above knowledge.
- Therefore: **not a fully blind prospective preregistration.** The design remains useful for transparency and constraint of researcher degrees of freedom, not as confirmatory testing.
- Two microcases, four executions: exploratory; no statistical inference; agreement between systems ≠ legal validity; shared training-family effects cannot be excluded within the Claude arm.
