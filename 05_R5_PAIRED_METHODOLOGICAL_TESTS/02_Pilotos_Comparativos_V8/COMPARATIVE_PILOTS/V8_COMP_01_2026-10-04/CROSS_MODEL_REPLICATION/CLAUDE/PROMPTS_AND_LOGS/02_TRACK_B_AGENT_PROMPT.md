# V8-COMP-01 / Cross-Model Replication — CLAUDE TRACK B (V8 + eight operations)

You are an independent analyst executing **one methodological track** of a legal-text replication study. You have no prior conversation history. Everything you may use is listed below. Work autonomously, do not ask questions, and finish all deliverables.

Project root (call it ROOT): `G:\Meu Drive\PRJ-David\Prf-David`
Experiment folder (EXP): `ROOT\COMPARATIVE_PILOTS\V8_COMP_01_2026-10-04`
Your output folder (OUT): `EXP\CROSS_MODEL_REPLICATION\CLAUDE\CLAUDE_TRACK_B\` (already exists; write only here)

## 0. Purpose and honesty rule

The aim is scientific reproducibility of an independent analysis, **not agreement with any other system**, and **not demonstrating that the additional protocol is useful**. The eight-operation protocol is a *method hypothesis*: it may help, add nothing, or make the analysis worse (jargon, false precision, over-segmentation). Apply it faithfully and then report honestly what each operation actually contributed — including "no material contribution". Do not treat output length or number of categories as merit. Report "not supported", "deferred", "stop here" where the evidence requires it. A smaller, well-bounded result is valid.

## 1. Your track: V8 + the eight operations

Analyse the 20 frozen statements using **V8** (inference ladder, three levels, codebook, quality states `coding_status`/`claim_level`, inference rules incl. the stopping rule, traceability requirement) **plus** the following eight-operation architectural-reconstruction protocol (`METHOD_HYPOTHESIS`, from `EXP\RESEARCH_PROTOCOL_v0_1.md` §5), executed as explicit, separately recorded steps in this order:

- **O1 Delimitation:** object, jurisdiction, version, time, problem, boundary.
- **O2 Decomposition:** separate institutional statements; keep modality, condition and context.
- **O3 Relational reconstruction:** recognise only actor–actor links qualified by text or a stated cross-reference.
- **O4 Configurational reconstruction:** group actors, relations, functions, mechanisms and instruments in an explicitly justified way.
- **O5 Position and sequence:** distinguish gateway, order, option, obligatoriness, substitutability, conditional authority.
- **O6 Part–whole:** distinguish attribute of actor, relation, position, configuration, law and regime (state the bearer of every property claimed).
- **O7 Architectural inference:** declare evidence, warrant, counter-evidence and stopping rule.
- **O8 Sensitivity:** test alternative plausible cuts and readings; record the effect.

Do the work on the evidence itself. You have **no access to, and must not seek, any other analysis of these statements** (other tracks, other systems, historical classifications). Your analytical conclusions must come from the frozen evidence, V8 and the protocol only.

## 2. Allowed inputs (allow-list — read ONLY these)

1. `EXP\COMMON_STATEMENT_REGISTER.csv` — the frozen evidence: 20 statements (P03 = 6, P04 = 14). Expected SHA-256 `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F`. **Verify the hash first.** If it differs, stop and write `BLOCKED_SOURCE_INTEGRITY` in the log.
2. `EXP\COMMON_STATEMENT_DATA_DICTIONARY.md`
3. `EXP\COMMON_STATEMENT_FREEZE_MANIFEST.csv`, `EXP\FROZEN_EVIDENCE_MANIFEST.csv`, `EXP\SOURCE_INTEGRITY_RECHECK.csv` (hash/provenance only)
4. `EXP\COMPARISON_EVALUATION_CRITERIA.md` (pre-registered criteria — your QA self-check should address them)
5. `EXP\RESEARCH_PROTOCOL_v0_1.md` (shared protocol; the eight operations are in §5)
6. V8 framework:
   - `ROOT\RGAM\V8_ACTIVE\00_PROJECT_CONTROL\V8_CONCEPTUAL_BASELINE.md`
   - `ROOT\RGAM\V8_ACTIVE\01_THEORETICAL_FRAMEWORK\V8_ANALYTICAL_STRUCTURE.md`
   - `ROOT\RGAM\V8_ACTIVE\02_CODING_ONTOLOGY\V8_CODEBOOK.md`
   - `ROOT\RGAM\V8_ACTIVE\02_CODING_ONTOLOGY\INFERENCE_RULES.md`
   - `ROOT\RGAM\V8_ACTIVE\02_CODING_ONTOLOGY\RELATIONAL_MODEL.md`
   - `ROOT\RGAM\V8_ACTIVE\05_CONCEPTUAL_ARTICLE\FOUNDATIONAL_PREPAPER_V8.md` (method description of the eight operations; its GDPR example is a different case — do not import its conclusions)
   - `ROOT\RGAM\source_context\david_v8_2026-10-03\draft v8   Law_and_Governance_Architectures_Revised.docx` (the V8 manuscript; extract text by unzipping and reading `word/document.xml`, or with python-docx if available)
7. Primary legal text (to resolve cross-references and wording only; **do not widen the scope**):
   - `ROOT\AUTONOMOUS_ROTEM_COMPARISON_20260930_2047\01_BASELINES\official_texts\31991L0263.txt` (and `.html`, SHA-256 `01D5BDB117B370AE9DAD7F3ABB151583A75519CBAD0E7808EFC9040C8D656888`)
   - `ROOT\AUTONOMOUS_ROTEM_COMPARISON_20260930_2047\01_BASELINES\official_texts\32004R0874.txt` (and `.html`, SHA-256 `62AFB4DDCCAE5E7157590B1386040AA8D160701D7194DBD2F2403AC4B6781449`)

## 3. FORBIDDEN (do not read, list, grep, glob, open, or "peek" at any of these, even for verification, comparison or inspiration)

- `EXP\CROSS_MODEL_REPLICATION\CLAUDE\CLAUDE_TRACK_A\` and anything else under `EXP\CROSS_MODEL_REPLICATION\` other than your own OUT folder.
- Anything under `EXP\TRACK_A\`, `EXP\TRACK_B\`, `EXP\01_MDR\`, `EXP\QA\`, `EXP\RUN_LOGS\`, `EXP\TEAM_FEEDBACK\`, `EXP\02_DSA\`, `EXP\03_LEI_13848\`.
- `EXP\EXECUTION_LOG.md`, `EXP\README.md`, `EXP\UPDATED_RESPONSE_REGISTER.md`, `EXP\RESPONSE_*`, `EXP\V8_COMP_01_NEXT_GATE_REPORT.md`, `EXP\G1B_*`, `EXP\CASE_*`, `EXP\AMENDMENT_*`, `EXP\PILOT03_TO_V8_CROSSWALK.csv`, `EXP\G2_TRACK_A_EXECUTION_PROMPT.md`.
- Any file whose name contains `TRACK_A_`, `TRACK_B_` or `MDR_A_B` outside your own OUT folder.
- `ROOT\RELATIONAL_LEXIMETRICS_PILOT\` (historical PILOT_03 Model A/B and human adjudications).
- `ROOT\CODEX_*`, `ROOT\AUTONOMOUS_ROTEM_COMPARISON_*` **except the four files named in allow-list item 7**, `ROOT\ENVIO_*`, `ROOT\AUDIT_*`, `ROOT\R4_*`, `ROOT\Before_R2`, `ROOT\Post_R2`, `ROOT\validation`, `ROOT\WORK_2_1`, `ROOT\RELATORIOS_*`.
- `EXP\CROSS_MODEL_REPLICATION\CLAUDE\PROMPTS_AND_LOGS\` (except this prompt file, which you have already read).
- Do **not** run a directory listing or glob of `EXP\`, `ROOT\`, `COMPARATIVE_PILOTS\` or `EXP\CROSS_MODEL_REPLICATION\`. Open only the exact paths above. If you accidentally see a forbidden file or folder name, write it in the "contamination events" section of your log; do not open it.
- Do not modify any file outside OUT. Do not run any git command that changes state; no commit, push, reset, branch change.

## 4. Scope controls

- Exactly the 20 statements in the register. P04 Article 22(7) is excluded context. No new provisions, laws or inferred actors absent from the text. O1 delimitation must stay within this scope; in O8 you may test alternative *readings and cuts* of the same 20 statements, but must not bring in additional statements to the dataset.
- Do not edit the register or sources.
- A normative assignment without an identifiable counterparty is a **statement/assignment, not automatically a relationship** (O3). Reporting alone is information, not automatically accountability. Do not infer discretion from a job title. Do not infer implementation, practice or effectiveness from formal text. Graph connectivity, shared actors, co-occurrence, naming or membership of the same instrument are not architecture.
- You may consult wider provisions of the same two instruments only to resolve a cross-reference quoted in a statement or a wording ambiguity; record each consultation in the log.

## 5. Deliverables (write to OUT; UTF-8; CSV with header, quoted fields where needed)

All filenames prefixed `CLAUDE_TRACK_B_`.

1. `CLAUDE_TRACK_B_CODING.csv` — one row per statement (20 rows): `statement_id, case_id, provision_anchor, actor_coded, actor_expression (expressed|not_expressed|grammatical_subject), governance_object, function, mechanism, instrument, modality, direct_text_elements, inferred_elements, coding_status, claim_level, authority_note, discretion_note, accountability_note, position_note, relationship_decision (ACCEPTED|REJECTED|DEFERRED|ASSIGNMENT_ONLY), relationship_ids, decision_reason, uncertainty_ids`.
2. `CLAUDE_TRACK_B_RELATIONSHIPS.csv` — every candidate relationship considered, including rejected and deferred: `relationship_id, case_id, actor_a, actor_b, relationship_type (typed), direction, modality, condition, supporting_statement_ids, cross_provisions_used, coding_status, claim_level, authority, discretion, accountability, decision (ACCEPTED|REJECTED|DEFERRED), decision_reason, human_review_needed (TRUE|FALSE)`.
3. `CLAUDE_TRACK_B_OPERATION_REGISTER.csv` — one row per operation O1–O8: `operation, evidentiary_basis (statement/relationship IDs), what_was_done, output_artifacts, contribution_type (made_explicit|blocked_a_claim|changed_a_grouping|added_uncertainty|no_material_contribution), concrete_contribution (the specific thing this operation made you see, drop, block or qualify — or "none"), risk_or_cost_observed (e.g. redundancy, over-segmentation, false precision), effort_note`. Describe contribution only from what you observe while doing this track; you have not seen any analysis without the protocol and must not speculate about one.
4. `CLAUDE_TRACK_B_CONFIGURATIONS.md` — O4: candidate configurations with members, justification of grouping, theoretical pattern, overlap, what is not established, `claim_level`.
5. `CLAUDE_TRACK_B_POSITIONAL_ANALYSIS.md` — O5: gateway, order, option, obligatoriness, substitutability, conditional authority, per configuration, grounded in textual modality/condition; mark every point where the text does not support a positional claim.
6. `CLAUDE_TRACK_B_PART_WHOLE_ANALYSIS.md` — O6: for every property claimed anywhere in the track, its bearer (actor / relation / position / configuration / law / regime) and the boundary; list property claims you refused to lift to a higher level.
7. `CLAUDE_TRACK_B_SENSITIVITY_ANALYSIS.md` — O8: alternative cuts/readings tested (each with its effect on relationships, configurations and inferences), which claims survive, which do not.
8. `CLAUDE_TRACK_B_ARCHITECTURAL_INFERENCES.md` — O7: per case, the highest level actually supported; any architecture-level claim with problem and scale, qualified coupling, configurational consequence and bearer, significance factors, warrant, counter-evidence, alternatives, boundary limitations — **or an explicit statement that no architecture-level claim is warranted**; claims considered and declined; stopping-rule decision per case; full traceability chain for every claim (claim → configuration → relationships/elements → statements → provision → source/hash). No regime claim unless a separate regime-boundary decision is made and justified; default is to stop below regime.
9. `CLAUDE_TRACK_B_UNCERTAINTY_REGISTER.csv` — `uncertainty_id, case_id, statement_or_relationship_ids, type (grammar|scope|segmentation|cross_level|unsupported_relation|modality|boundary|position|part_whole|other), description, treatment, status (deferred|human_review_needed|resolved_by_text|accepted_ambiguity)`.
10. `CLAUDE_TRACK_B_QA_REPORT.md` — self-QA against `COMPARISON_EVALUATION_CRITERIA.md` (traceability, inferential defensibility/errors, unsupported-relationship attribution, cross-level errors, structural clarification, uncertainty/stopping compliance, effort). Include count checks (20 statements coded; every relationship has ≥1 supporting statement; every claim traceable). **Do not compare with any other track or system and do not claim the protocol is better.**
11. `CLAUDE_TRACK_B_EXECUTION_LOG.md` — chronological log: start/end time (system clock), model identification **as you know it** ("unknown" if you do not know), every file opened (exact paths), every wider-text consultation, SHA-256 verification results, per-operation record (what was done, which statements were used), inferential and stopping-rule decisions, effort estimate, protocol deviations, **a "contamination events" section** (any forbidden or non-listed file or name you saw; "none" if none), and an explicit statement that you did not access any other analysis of these statements.

Do not compute the freeze manifest; the orchestrator will freeze your outputs by SHA-256. Do not write a cross-track or cross-model comparison.

## 6. Final message

Return a short message (under 200 words): the files written, any blocked or deviated step, and confirmation that you stayed within the allow-list. Do not summarise your analytical conclusions in the final message.
