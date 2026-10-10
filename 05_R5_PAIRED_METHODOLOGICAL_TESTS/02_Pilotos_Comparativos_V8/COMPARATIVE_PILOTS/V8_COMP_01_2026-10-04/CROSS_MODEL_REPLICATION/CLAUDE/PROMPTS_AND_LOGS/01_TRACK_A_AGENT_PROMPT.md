# V8-COMP-01 / Cross-Model Replication — CLAUDE TRACK A (V8 only)

You are an independent analyst executing **one methodological track** of a legal-text replication study. You have no prior conversation history. Everything you may use is listed below. Work autonomously, do not ask questions, and finish all deliverables.

Project root (call it ROOT): `G:\Meu Drive\PRJ-David\Prf-David`
Experiment folder (EXP): `ROOT\COMPARATIVE_PILOTS\V8_COMP_01_2026-10-04`
Your output folder (OUT): `EXP\CROSS_MODEL_REPLICATION\CLAUDE\CLAUDE_TRACK_A\` (already exists; write only here)

## 0. Purpose and honesty rule

The aim is scientific reproducibility of an independent analysis, **not agreement with any other system**. Report what the evidence supports, including "not supported", "deferred" and "stop here". Do not pad. Output length, number of categories or number of configurations is not a merit. A smaller, well-bounded result is a valid result. Do not use any prior knowledge of what a "desirable" answer would be.

## 1. Your track: V8 ONLY

Apply David Levi-Faur's V8 relational-leximetric framework competently and completely, to the 20 frozen statements. Use:
- the V8 inference ladder: legal text → institutional statements → governance relationships → governance configurations → legal architectures → governance regimes;
- the three V8 levels (I elements: objects, actors, functions, mechanisms, instruments, relationships; II attributes: authority, discretion, accountability; III higher-order constructs);
- the V8 codebook rules, quality states (`coding_status`, `claim_level`), the inference rules (including the stopping rule: stop at the highest level actually supported; record `deferred` / `human_review_needed` rather than promote a claim), and the traceability requirement (architectural claim → configuration → relationships/elements → statements → legal units → source/version/hash).

You must **NOT** apply any additional multi-step "eight-operation architectural reconstruction" protocol. Concretely, do **not** run separate named analytical phases for delimitation, decomposition, relational reconstruction, configurational reconstruction, positional/sequence analysis, part–whole analysis, architectural inference and boundary/sensitivity analysis as a procedure, and do not produce positional-analysis, part–whole-analysis or sensitivity-analysis deliverables. You are simply applying V8 as a careful analyst would, using its own rules. If a V8 rule itself requires you to note an alternative reading or a bearer of a property, do so inside the normal deliverables. (Note: some V8 support documents mention a "property bearer" and "boundary/sensitivity" layer labelled `METHOD_HYPOTHESIS` or `OPERATIONAL_SPECIFICATION`; use the V8_DEFINED and operational-specification elements; do not turn the METHOD_HYPOTHESIS layer into a procedure.)

## 2. Allowed inputs (allow-list — read ONLY these)

1. `EXP\COMMON_STATEMENT_REGISTER.csv` — the frozen evidence: 20 statements (P03 = 6, P04 = 14). Expected SHA-256 `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F`. **Verify the hash first.** If it differs, stop and write `BLOCKED_SOURCE_INTEGRITY` in the log.
2. `EXP\COMMON_STATEMENT_DATA_DICTIONARY.md`
3. `EXP\COMMON_STATEMENT_FREEZE_MANIFEST.csv`, `EXP\FROZEN_EVIDENCE_MANIFEST.csv`, `EXP\SOURCE_INTEGRITY_RECHECK.csv` (hash/provenance only)
4. `EXP\COMPARISON_EVALUATION_CRITERIA.md` (pre-registered criteria — your QA self-check should address them)
5. `EXP\G2_TRACK_A_EXECUTION_PROMPT.md` (the original Track A task statement)
6. V8 framework: 
   - `ROOT\RGAM\V8_ACTIVE\00_PROJECT_CONTROL\V8_CONCEPTUAL_BASELINE.md`
   - `ROOT\RGAM\V8_ACTIVE\01_THEORETICAL_FRAMEWORK\V8_ANALYTICAL_STRUCTURE.md`
   - `ROOT\RGAM\V8_ACTIVE\02_CODING_ONTOLOGY\V8_CODEBOOK.md`
   - `ROOT\RGAM\V8_ACTIVE\02_CODING_ONTOLOGY\INFERENCE_RULES.md`
   - `ROOT\RGAM\V8_ACTIVE\02_CODING_ONTOLOGY\RELATIONAL_MODEL.md`
   - `ROOT\RGAM\source_context\david_v8_2026-10-03\draft v8   Law_and_Governance_Architectures_Revised.docx` (the V8 manuscript; extract text by unzipping and reading `word/document.xml`, or with python-docx if available)
7. Primary legal text (to resolve cross-references and wording only; **do not widen the scope**): 
   - `ROOT\AUTONOMOUS_ROTEM_COMPARISON_20260930_2047\01_BASELINES\official_texts\31991L0263.txt` (and `.html`, SHA-256 `01D5BDB117B370AE9DAD7F3ABB151583A75519CBAD0E7808EFC9040C8D656888`)
   - `ROOT\AUTONOMOUS_ROTEM_COMPARISON_20260930_2047\01_BASELINES\official_texts\32004R0874.txt` (and `.html`, SHA-256 `62AFB4DDCCAE5E7157590B1386040AA8D160701D7194DBD2F2403AC4B6781449`)

## 3. FORBIDDEN (do not read, list, grep, glob, open, or "peek" at any of these, even for verification or inspiration)

- Anything under `EXP\TRACK_A\`, `EXP\TRACK_B\`, `EXP\01_MDR\`, `EXP\QA\`, `EXP\RUN_LOGS\`, `EXP\TEAM_FEEDBACK\`, `EXP\02_DSA\`, `EXP\03_LEI_13848\`.
- `EXP\EXECUTION_LOG.md`, `EXP\README.md`, `EXP\UPDATED_RESPONSE_REGISTER.md`, `EXP\RESPONSE_*`, `EXP\V8_COMP_01_NEXT_GATE_REPORT.md`, `EXP\G1B_*`, `EXP\CASE_*`, `EXP\AMENDMENT_*`, `EXP\PILOT03_TO_V8_CROSSWALK.csv`.
- Any file whose name contains `TRACK_A_` or `TRACK_B_` or `MDR_A_B` outside your own OUT folder.
- `ROOT\RELATIONAL_LEXIMETRICS_PILOT\` (historical PILOT_03 Model A/B and human adjudications).
- `ROOT\CODEX_*`, `ROOT\AUTONOMOUS_ROTEM_COMPARISON_*` **except the four files named in allow-list item 7**, `ROOT\ENVIO_*`, `ROOT\AUDIT_*`, `ROOT\R4_*`, `ROOT\Before_R2`, `ROOT\Post_R2`, `ROOT\validation`, `ROOT\WORK_2_1`, `ROOT\RELATORIOS_*`.
- `EXP\CROSS_MODEL_REPLICATION\CLAUDE\CLAUDE_TRACK_B\` and `EXP\CROSS_MODEL_REPLICATION\CLAUDE\PROMPTS_AND_LOGS\` (except this prompt file, which you have already read).
- The eight-operation protocol text: `EXP\RESEARCH_PROTOCOL_v0_1.md` and `ROOT\RGAM\V8_ACTIVE\05_CONCEPTUAL_ARTICLE\` (these describe the additional protocol and belong to the other track).
- Do **not** run a directory listing or glob of `EXP\` or `ROOT\` or of `COMPARATIVE_PILOTS\`. Open only the exact paths above. If you accidentally see a forbidden file name, write it in the "contamination events" section of your log; do not open it.
- Do not modify any file outside OUT. Do not run any git command that changes state; no commit, push, reset, branch change.

## 4. Scope controls

- Exactly the 20 statements in the register. P04 Article 22(7) is excluded context. No new provisions, laws or inferred actors absent from the text.
- Do not edit the register or sources.
- A normative assignment without an identifiable counterparty is a **statement/assignment, not automatically a relationship**. Reporting alone is information, not automatically accountability. Do not infer discretion from a job title. Do not infer implementation, practice or effectiveness from formal text.
- You may consult wider provisions of the same two instruments only to resolve a cross-reference quoted in a statement or a wording ambiguity; record each consultation in the log.

## 5. Deliverables (write to OUT; use UTF-8; CSV with header, quoted fields where needed)

All filenames prefixed `CLAUDE_TRACK_A_`.

1. `CLAUDE_TRACK_A_CODING.csv` — one row per statement (20 rows): `statement_id, case_id, provision_anchor, actor_coded, actor_expression (expressed|not_expressed|grammatical_subject), governance_object, function, mechanism, instrument, modality, direct_text_elements, inferred_elements, coding_status, claim_level, authority_note, discretion_note, accountability_note, relationship_decision (ACCEPTED|REJECTED|DEFERRED|ASSIGNMENT_ONLY), relationship_ids, decision_reason, uncertainty_ids`. Use V8 `coding_status` and `claim_level` vocabularies.
2. `CLAUDE_TRACK_A_RELATIONSHIPS.csv` — every candidate relationship you considered, including rejected and deferred: `relationship_id, case_id, actor_a, actor_b, relationship_type (typed, not generic), direction, modality, condition, supporting_statement_ids, cross_provisions_used, coding_status, claim_level, authority, discretion, accountability, decision (ACCEPTED|REJECTED|DEFERRED), decision_reason, human_review_needed (TRUE|FALSE)`.
3. `CLAUDE_TRACK_A_CONFIGURATIONS.md` — candidate configurations (stated combination of relationships/elements/attributes around a function, stage or problem), their members (relationship IDs), the theoretical pattern, what is not established, overlap, and `claim_level` stated. Candidate groupings are not architectural conclusions.
4. `CLAUDE_TRACK_A_ARCHITECTURAL_INFERENCES.md` — for each case, the **highest level actually supported**, any architecture-level claim (problem and scale; qualified coupling; configurational consequence; significance factors; alternatives; boundary limitations) **or an explicit statement that no architecture-level claim is warranted**, any claim you considered and declined and why, the stopping-rule decision for each case, and the full traceability chain for every claim (claim → configuration → relationships/elements → statements → provision → source/hash). No regime claim unless a separate regime-boundary decision is made and justified; default is to stop below regime.
5. `CLAUDE_TRACK_A_UNCERTAINTY_REGISTER.csv` — `uncertainty_id, case_id, statement_or_relationship_ids, type (grammar|scope|segmentation|cross_level|unsupported_relation|modality|boundary|other), description, treatment, status (deferred|human_review_needed|resolved_by_text|accepted_ambiguity)`.
6. `CLAUDE_TRACK_A_QA_REPORT.md` — self-QA against `COMPARISON_EVALUATION_CRITERIA.md` (traceability, inferential defensibility/errors, unsupported-relationship attribution, cross-level errors, structural clarification, uncertainty/stopping compliance, effort). Include count checks (20 statements coded; every relationship has ≥1 supporting statement; every claim traceable). **Do not claim superiority of anything.** Do not compare with any other track or system.
7. `CLAUDE_TRACK_A_EXECUTION_LOG.md` — chronological log: start/end time (use the system clock), model identification **as you know it** (model name/ID; state "unknown" if you do not know), every file you opened (exact paths), every wider-text consultation, SHA-256 verification result for the register and primary sources, every inferential decision and stopping-rule decision, effort estimate (approximate time and number of decisions), any protocol deviation, **a "contamination events" section** (any forbidden or non-listed file or name you saw; write "none" if none), and an explicit statement that you did not use the eight-operation protocol.

Do not compute the freeze manifest; the orchestrator will freeze your outputs by SHA-256. Do not write a cross-track or cross-model comparison.

## 6. Final message

Return a short message (under 200 words): the files written, any blocked or deviated step, and confirmation that you stayed within the allow-list. Do not summarise your analytical conclusions in the final message.
