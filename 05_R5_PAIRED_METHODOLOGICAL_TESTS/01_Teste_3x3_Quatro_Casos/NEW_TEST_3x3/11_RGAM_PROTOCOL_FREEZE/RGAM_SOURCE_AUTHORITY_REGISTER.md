# RGAM — SOURCE AUTHORITY REGISTER (frozen before case execution)

Paths relative to the repository root `Prf-David/`. SHA-256 computed at the start of construction (2026-10-06 ≈15:01 UTC-03) and re-verified at the end (QA report). Original RGAM source files were **not modified**.

## 1. Authoritative stack

| Level | Role | Path | Version / date | SHA-256 | Used for |
|---|---|---|---|---|---|
| **1** | Controlling methodological source | `RGAM/paper/MANUSCRIPT_v0_6_1.md` | working draft v0.6.1, 3 Oct 2026 (file 12:39) | `8c10d4e6a650cc45e5dd7e3485c807c8dca808c9ba6ee827a0df03b8120a1b57` | §§1–2 (W/A, E→A chain), §4.3–4.7 (N1–N4, materiality, statuses, claims), §5.3, §6 (definition, strata, S→A, I1–I4, accountability, bearers, contrast), §7.1/7.7, §8.2–8.4 |
| **2** | Ontological specification (subordinate to Level 1) | `RGAM/ontology/ONTOLOGY_v0_4.md` | candidate ontology v0.4 rev3, 3 Oct 2026 (file 11:37) | `54f1abf42a195955ef64b94c278ebb6de393f72cf491c53b0455f14f73fe400e` | §3 entity classes, §3.7 external references, §4, §5 boundary rules and stopping rule, §6 bearers, §6.1 dimensions, §10–11 |
| **3a** | Precedence record | `RGAM/pilot/GDPR_PILOT_01/00_PROTOCOL/ONTOLOGY_ALIGNMENT_AND_PRECEDENCE.md` | 3 Oct 2026 | `88cd6dbd3d3b1df79be7f55d9e3aa36ea0b14ab4ad6b189fb55f66d0c05daa2b` | documented precedence v0.6.1 > v0.4; discrepancies #1–#6; label collision |
| **3b** | Integration / version register | `RGAM/paper/V0_6_INTEGRATION_REGISTER.md` | 3 Oct 2026 | `ca1b4bb7a98b0dfbc0f82cd28eb3aed73f51ee29db1cae8c9c1c90da4830f2aa` | preserved safeguards; frozen-ontology divergences |
| **3c** | Version record v0.6→v0.6.1 | `RGAM/paper/V0_6_1_SCIENTIFIC_REVISION_REGISTER.md` | 3 Oct 2026 | `5f1c4b2a2f0b2896a7861bfb115baaa479531415345252d9337e38e6b357fdfe` | I1–I4 provenance; scientific cautions |
| **3d** | Ontology decision log (PT-1…PT-8, D01–D11) | `RGAM/ontology/DECISION_LOG.md` | 3 Oct 2026 | `10dbc5badb348cd221b715e1b50e6e388844b4aa9987fb1f425653c567cda568` | status of PT rules (approved/provisional) — directly necessary for PT-4/PT-8 and D10 |
| **3e** | Version-control note (read only to register a conflict) | `RGAM/paper/START_HERE_V0_6.md` | 3 Oct 2026 | `50fbaf2051d6f2c2c564ab02f73994e6a808295af989da1af13f58f15e0085d5` | conflict C-13 only |
| **3f** | Execution addendum (reconstructed summary; read only for provenance of Phase-1 decisions) | `RGAM/00_ADMIN/EXECUTION_ADDENDUM_v0_4.md` | 3 Oct 2026 | `8e296f79a04c69ad4cbed86a9320a7102ac106f9c5b4fba3c378bcfd23166a7a` | not used as a rule source |
| **4** | Operational template only | `RGAM/pilot/GDPR_PILOT_01/00_PROTOCOL/DECISION_RULES.md` | decision rules v1.2 (3 Oct 2026) | `b6ea6467ed89009cf36b9441d1445cd97386ee028227cc2a04fb7c7ca6b8a004` | procedural structure only; instrument-specific content removed (see decision rules Appendix B) |

## 2. Explicitly non-authoritative / excluded

| Source | Reason |
|---|---|
| `PROMPT_CODEX_RGAM_v0_3_MATERIALITY_FIRST.md` | drafting prompt, not an analytical method (task §3) — **not opened in this task** |
| the eight-operation sequence (O1–O8) of the earlier V8 experiment | not RGAM; not imported (task §1) — **not opened in this task** |
| V8 outputs, V8-COMP-01 results, `09_V8_BASELINE_EXECUTION/` | forbidden (task §0) — not opened |
| `RGAM/V8_ACTIVE/` | forbidden for protocol construction (task §4) — not opened |
| historical R2/R3/R4/PILOT outputs and case-specific architectural findings | forbidden (task §3, §20) — not opened |
| the four legal texts | not opened or interpreted; copied only into capsules by byte-for-byte file copy with hash check |
| `RGAM/handoff/V8_RGAM_ALIGNMENT_2026-10-03/*`, `RGAM/theory/*`, `RGAM/validation/*`, other manuscript versions (v0.4, v0.5, v0.5.1, v0.6) | not part of the authorized stack; not used (the alignment note was read in the previous preflight task only; nothing from it is used here) |

## 3. V8_ACTIVE reference check

A content search (patterns `V8_ACTIVE`, an operation-sequence marker, "eight operations") over the authorized files — manuscript v0.6.1, ontology v0.4, the three precedence/version records, template rules, ontology decision log, execution addendum and start-here note — returned **no matches**. Conclusion: no authorized RGAM document references `V8_ACTIVE`; no rule was found that exists only there; `RGAM_PROTOCOL_DEPENDENCY_UNRESOLVED` was **not** raised (conflict register D-01).

## 4. Files actually read during construction (this task)

`MANUSCRIPT_v0_6_1.md` (lines 1–115 and 185–528, i.e. §§1–2, §§4–8.4; §3 and the reference list were not read in this task); `ONTOLOGY_v0_4.md` (entire); `V0_6_1_SCIENTIFIC_REVISION_REGISTER.md`; `DECISION_LOG.md`; plus, earlier in the same session, `DECISION_RULES.md`, `ONTOLOGY_ALIGNMENT_AND_PRECEDENCE.md`, `V0_6_INTEGRATION_REGISTER.md`, `START_HERE_V0_6.md`, `EXECUTION_ADDENDUM_v0_4.md` and the manuscript's lines 299–415 (preflight task). Also read: `08_STRICT_AI_PREPARATION/FINAL_COMMON_EXECUTION_CORPUS_REGISTER.csv` (neutral metadata for the capsules). Claude Code settings schema (configuration only).

## 5. Exposure and independence disclosures (exact)

1. **Deny-rule test read:** after writing the deny rules, one 3-line read of `R4_CROSS_DOMAIN_VALIDATION/R4_BASELINE_FREEZE_RECORD.md` (an administrative freeze header: title and freeze date) succeeded, showing the rules were not yet active. No analytical content was exposed.
2. **Previous preflight task (same session):** a broad content search returned file names and per-file match counts (no contents) inside `09_V8_BASELINE_EXECUTION/` (names of the gate, QA and summary files and of four per-case folders); three lines of the earlier experiment's agent prompt (labels of three operations) were read; one line of `STRICT_AI_PRE_EXECUTION_GATE.md` reporting a count of supported relations in a restricted pre-analytical baseline was displayed; the V8–RGAM alignment note was read (conceptual).
3. **Earlier stages of the experiment (same session):** the author had read historical R2/R3 relation tables and counts and R4/PILOT material relating to the climate-fund, carbon-border and terminal-equipment cases, and R4 structural counts for the AI instrument, during case-universe construction. **None of it was used** to design the protocol; case-independence is enforced by construction (no case-specific rule) and by the automated checks of the QA report. Future executors must nevertheless be fresh contexts.
4. **No substantive V8 analytical output** (claims, relations, configurations, architectures, uncertainties, summaries, QA findings) was read at any point.
5. **No legal text** of the four cases was opened or interpreted in this task.
