# RGAM — PROTOCOL QA REPORT (pre-freeze)

Generated 2026-10-06 15:09 (UTC-03) by `TOOLS/run_qa.py` before the freeze manifest was written. Automated checks: **18/18 PASS**.

## 1. Automated checks

| ID | Requirement | Result | Evidence |
|---|---|---|---|
| Q01 | Protocol is case-general: no case-specific term in the method documents or schema | **PASS** | terms searched: ['social climate', 'carbon border', 'cbam', 'artificial intelligence', 'ai act', '86/361', '2023/955', '2023/956', '2024/1689', 'terminal equipment', 'type approval', 'climate fund', 'deforestation', 'scf']; hits: none |
| Q02 | Capsules are input-only: all 19 templates per capsule are header-only and identical to the schema; no analytical field populated | **PASS** | capsules=4; problems=none |
| Q03 | No scoring rule, composite index or numeric threshold is defined (every mention occurs in a negating/limiting context) | **PASS** | unqualified mentions: none |
| Q04 | `INDETERMINATE` remains a legitimate result (S->A outcome, instrument-level result, stopping rule) | **PASS** | occurrences=7 |
| Q05 | Explicit stopping rule stated | **PASS** | Protocol §11 and RGAM-DR-27 |
| Q06 | O1-O8 not imported (any mention is a non-import statement); the phases P0-P9 are an execution aid mapped to RGAM-documented activities | **PASS** | mentions=6; all negated/contextual=True |
| Q07 | Template-specific (instrument-specific) content removed from the method documents | **PASS** | terms searched: ['gdpr', '2016/679', 'corrigend', 'b5085317', 'article 4 definitions', 'data subject', 'controller', 'processor', 'supervisory authority']; hits: none |
| Q08 | Materiality is not a sequential phase (no phase row for it; stated as transversal control) | **PASS** | phase rows=10 |
| Q09 | Vertical traceability operationalized (ids, many-to-many provenance, trace demonstrations, integrity rules) | **PASS** | tables PROVENANCE_LINKS, TRACE_DEMONSTRATIONS; integrity rules 1-10 |
| Q10 | Human review separate: human-only columns exist and are blank in templates; protocol forbids simulation | **PASS** | HUMAN_REVIEW_QUEUE columns present; templates header-only |
| Q11 | v0.6.1 precedence respected; ontology conflicts registered; every cited conflict id exists | **PASS** | rows=27; resolved by documented precedence=13; cited-but-missing=none |
| Q12 | Original RGAM source files unmodified (SHA-256 at start == end) | **PASS** | files checked=9; mismatches=none |
| Q13 | Each capsule source is byte-identical to the frozen common-corpus source and to the hash designated for both arms (hash comparison only) | **PASS** | capsules=4; mismatches=none |
| Q14 | Technical read-deny configured (rules written, valid JSON). NOTE: activity not verified in the construction session and shell bypass remains - recorded as a limitation | **PASS** | deny rules=33 (configured: PASS; active: NOT VERIFIED) |
| Q15 | Deliverables 1-8 present before QA (9-12 produced after QA) | **PASS** | missing=none |
| Q16 | Data dictionary lists every table and field of the schema | **PASS** | tables=19, fields=271 |
| Q17 | Method documents do not depend on V8_ACTIVE or on V8 execution content (mentions only in prohibition/deny contexts) | **PASS** | unexpected files=none |
| Q18 | Core RGAM safeguards present in the protocol (W != A; reachability != transmission; no invented counterparty; N1-N4; INS-TYPE/DEV; I1-I4; closure; support-gap) | **PASS** | tokens checked=8 |

## 2. Checks established by the session record (not automatable)

| ID | Requirement | Basis |
|---|---|---|
| M01 | None of the four legal cases was analysed | Session record: the four source files were copied byte-for-byte (cp) and hashed; none was opened, read, parsed or interpreted in this task. |
| M02 | No V8 output was read | No file inside `09_V8_BASELINE_EXECUTION/` was opened in this task; the earlier exposure of file names/match counts (previous task) is disclosed in the authority register §5. |
| M03 | `RGAM/V8_ACTIVE/` was not opened | No Read/Grep/Glob targeted it in this task; the content search for references was restricted to authorized RGAM files. |
| M04 | O1–O8 were not imported | Q06 plus session record: the earlier procedure's files were not opened in this task. |
| M05 | Historical R2/R3/R4/PILOT outputs not used | None opened in this task except one 3-line administrative header (deny-rule test, disclosed). |

## 3. Mapping to the task's QA list (§24)

| Task requirement | Check |
|---|---|
| protocol is case-general | Q01, Q02 |
| none of the four cases analysed | M01, Q02 |
| no V8 output read | M02 |
| O1–O8 not imported | Q06, M04 |
| V8_ACTIVE not opened | M03, Q17 |
| v0.6.1 precedence respected | Q11 |
| ontology conflicts registered | Q11 |
| GDPR-specific content removed | Q07 |
| no scoring threshold invented | Q03 |
| INDETERMINATE valid | Q04 |
| stopping rule explicit | Q05 |
| vertical traceability operationalized | Q09, Q16 |
| human review separate | Q10 |
| materiality not a new sequential phase | Q08 |

## 4. Residual limitations carried into the gate

1. Technical read-deny is configured (33 rules) but **not verified active** and does not block shell commands; the strict allow-list is the primary control (Blindness policy §4, §7).
2. Wrapper decisions GAP-01…GAP-07 (annexes/formal provisions, amending provisions, intra-instrument cross-references, no external retrieval, function vocabulary, template references, definitional provisions) await Igor's confirmation; each is queued for human review at execution.
3. Open thresholds (device threshold; I2/I3 integration; accountability consequences) and the unharmonised measures list are recorded as unresolved (conflict register C-24, C-25, C-26).
4. The author's session had prior exposure to historical case content and V8-comparison file names; case-independence of the protocol rests on construction plus Q01/Q07, not on blindness of the author.
5. Actual V8 consumption of the common source files was not verified (equality is a corpus-level designation plus hash verification).
