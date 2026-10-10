# RGAM — BLINDNESS AND ACCESS POLICY v1.0 (frozen before case execution)

**Purpose:** keep the RGAM arm methodologically separate from the V8 arm and from historical analytical results, and keep the four RGAM cases independent of one another.

## 1. Execution model (future; not launched)

Each case is analysed in a **fresh, sequential subcontext** (one subagent or one new session per case), in the fixed order of the capsule register: `RGAM_C1_SCF` → `RGAM_C2_CBAM` → `RGAM_AI_AI_ACT` → `RGAM_O_DIR_86_361`. No parallel execution. Each subcontext receives only the five frozen method documents, its own capsule (frozen controlling source, neutral metadata, blank templates) and write access to its own output directory. The orchestrator must not paste, summarize or hint at one case's results in another case's brief, and must not read case outputs between runs other than for schema/ID-integrity validation.

## 2. Strict allow-list (reads)

1. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md`, `RGAM_PAIRED_DECISION_RULES_v1_0.md`, `RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`, `RGAM_CASE_OUTPUT_SCHEMA.md`, `RGAM_BLINDNESS_AND_ACCESS_POLICY.md`.
2. `11_RGAM_PROTOCOL_FREEZE/CAPSULES/<own capsule>/` only.
3. Writes: `12_RGAM_EXECUTION/<own capsule>/` only.

Everything else is outside the allow-list, including the other capsules, the original common corpus directory and every directory below.

## 3. Deny-list (never provided, never read)

V8 outputs, counts, conclusions, uncertainty records, cross-case summaries and QA reports; R2, R3 and R4 outputs; historical relationship extractions and pilot results; case-selection rankings and universe tables; results of other RGAM cases; `RGAM/V8_ACTIVE/`; the earlier V8-comparison material; the drafting prompt; foundational-paper review material. Directories: `NEW TEST 3x3/09_V8_BASELINE_EXECUTION/`, `NEW TEST 3x3/01_…06_*`, `NEW TEST 3x3/08_STRICT_AI_PREPARATION/AI_ACT_R3_*`, `NEW TEST 3x3/LOGS/`, `RGAM/V8_ACTIVE/`, `COMPARATIVE_PILOTS/`, `R4_CROSS_DOMAIN_VALIDATION/`, `ENVIO_R4_TO_DAVID/`, `RELATIONAL_LEXIMETRICS_PILOT/`, `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/`, `CODEX_ROTEM_SHARE_PACKAGE_20260930_2153/`, `Before_R2/dataset-eurlex/{cases,03_human,outputs}`, `Enviados/`, `WORK_2_1/`, the extraction/reconstruction/assessment folders of the earlier relational pilot, `AUDIT_RESEARCH_HISTORY/`, `FOUNDATIONAL_PAPER_REVIEW/`.

## 4. Technical read-deny: status

| Item | Status |
|---|---|
| Mechanism | project-level Claude Code permission rules `permissions.deny` → `Read(<path>)` in `.claude/settings.local.json` (33 rules covering the deny-list; also added to `.gitignore`) |
| File written | `Prf-David/.claude/settings.local.json` (valid JSON, 33 deny rules) |
| **Active in the construction session?** | **NO.** The settings directory did not exist when the session started, so the settings watcher did not load it; a test read of a denied administrative file succeeded (3 lines read, see authority register). The rules are expected to apply only after the session/editor is restarted or the settings are reloaded. |
| Coverage limits | `Read` deny rules apply to the Read tool and, best-effort, to Grep/Glob; they do **not** block shell commands (`cat`, `type`, PowerShell) or sub-processes run through the Bash/PowerShell tools, and they do not restrict a subagent's shell. The `Edit(...)` side is not denied. |
| Sibling-capsule isolation | cannot be expressed as a static deny (each run needs its own capsule); it relies on the allow-list in the executor brief and a post-run path audit |
| Verdict | **Technical read-deny is configured but not verified active and not complete (shell bypass). Execution must therefore use the strict allow-list below as the primary control, and record this as a limitation.** |

**Pre-launch checklist (to be completed before any case run):** (1) restart the session or reload settings; (2) test that a Read of a denied path is refused; (3) additionally disable or deny the shell tools for the subagent if possible, or run the subagent with only Read/Write on the allow-listed paths; (4) re-verify the source hash; (5) record the model identifier and every parameter the interface exposes (`NOT EXPOSED` otherwise) in RUN_METADATA.

## 5. Executor brief (template for the future subcontext)

> You are executing the RGAM arm for capsule `<ID>`. Read only the five frozen method documents and your capsule. Verify the source SHA-256 against `CASE_METADATA.json`; stop if it differs. Follow `RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md` P0–P9 using `RGAM_PAIRED_DECISION_RULES_v1_0.md` and `RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`; copy the blank templates to `12_RGAM_EXECUTION/<ID>/` and fill only machine columns. Do not read any other file, directory, prior result, V8 material or any other case. Do not compare with any other method. Do not fill human-review decision columns. Stop at P9. Record every file you read in RUN_METADATA.

## 6. Post-run audit

After each run: (a) compare the files-read list in RUN_METADATA with the transcript's tool calls; (b) confirm no path outside the allow-list was read and record any attempt; (c) validate schema/ID integrity (data dictionary §4) without reading analytical content into the orchestrator's briefs for later cases; (d) freeze the case output with a SHA-256 manifest before the next capsule starts.

## 7. Known limitations (recorded, not resolved)

1. Technical read-deny not active in the construction session and not shell-proof; allow-list is instruction-based.
2. The author of this protocol operated in a session that had previously encountered historical relational content and V8-comparison filenames during earlier stages of the experiment (exposures listed in `RGAM_SOURCE_AUTHORITY_REGISTER.md`). Case-independence of the **protocol** is secured by construction and by the automated checks in `RGAM_PROTOCOL_QA_REPORT.md`, not by the author's ignorance; future **executors** must be fresh contexts.
3. The V8 arm's actual use of the designated common source files was not verified (its directory was not opened); equality is a designation at the corpus-register level plus capsule hash verification.
4. The capsule copies of the legal sources sit beside the originals; the original common-corpus directory also holds the other cases' sources and is therefore outside the allow-list.
5. Model, version and parameters of future executors are not fixed by this protocol and must be decided and recorded before launch.
