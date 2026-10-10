# Pair comparison QA — Regulation (EU) 2023/956 — Carbon Border Adjustment Mechanism (CBAM)

Run `CMP-R1-CBAM-20261007` · created 2026-10-07T09:55:00-03:00

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Unique comparison_proposition_id | **PASS** | 70 units |
| 2 | All V8 source IDs resolve in frozen V8 case registers; all RGAM source IDs resolve in frozen RGAM case tables | **PASS** | 0 unresolved |
| 3 | Exactly one initial M1-M7 category per unit | **PASS** | invalid: [] |
| 4 | M3 has V8 refs only; M4 has RGAM refs only unless annotated; M1/M2/M5/M6 reference both arms | **PASS** | inconsistent: [] |
| 5 | Many-to-many mappings allowed and used (no forced 1:1) | **PASS** | cardinality distribution: {'n:m': 42, '1:n': 17, '0:n': 6, '1:1': 1, 'n:1': 2, 'n:0': 2} |
| 6 | Material differences cite a frozen materiality criterion | **PASS** | missing: [] |
| 7 | M1 units carry no difference (not materially different) | **PASS** | [] |
| 8 | M6 units are non-material (representational only) | **PASS** | [] |
| 9 | D1-D8 applied to every material unit with permitted statuses; D7/D8 recorded separately per method | **PASS** | [] |
| 10 | Every unit's human-review reference resolves to a queue item | **PASS** | [] |
| 11 | Every queue item references existing comparison units | **PASS** | [] |
| 12 | Every unit with an H-trigger is linked to a queue item | **PASS** | [] |
| 13 | Every M5 unit is in the human queue | **PASS** | [] |
| 14 | Review cards use no persuasive/conclusive method-comparative language | **PASS** | [] |
| 15 | Reviewer-facing card text contains no method labels or native record IDs | **PASS** | [] |
| 16 | Human decision/confidence/justification/reviewer/date fields blank on all cards | **PASS** | 16 cards |
| 17 | Identity key held in separate file; queue/cards expose no method labels | **PASS** | PAIR_IDENTITY_KEY.csv |
| 18 | No case-level winner, C-A–C-F category or F1–F7 assigned | **PASS** | Summary and registers contain no synthesis labels |
| 19 | Preregistered rules unchanged (C0–C4, M1–M7, D1–D8, H1–H11, materiality rule) | **PASS** | Codes imported verbatim; interpretive choices logged below, none amends a frozen rule |
| 20 | Frozen V8/RGAM/preregistration artefacts not modified by this run | **PASS** | All writes confined to 14_PAIRED_COMPARISON_ROUND1/PAIR_02_CBAM |

## Interpretive choices logged (no frozen rule modified)

- Same operationalisation of materiality as Pair 1: informational/organisational support relations attached to no configuration/architecture/property proposition in either arm are recorded as differences but NON_MATERIAL; relations with legal effect, party identity, modality, configuration membership or architecture boundary are potentially material.
- C0 statement-level coverage differences confined to provisions already compared at C1–C3 are carried by one aggregated non-material unit (CBAM.C0.15); materiality is assessed at C1–C4 to avoid double counting.
- Absence-based assertions (H7) are queued even where both arms align (MATCHING_RULES); clustered in HQ-CBAM-16, plus cards where the arms treat the absence differently.
- RGAM internal HQ items are not queued wholesale; RGAM HQ-003/005/007/008/009/010/012/013/014/015 appear only as cross-references where they touch a V8–RGAM difference. The RGAM reference date (2026-01-01, chosen by the RGAM executor from Art. 36(2)) is an RGAM scoping choice; V8 states no reference date. The difference is recorded (CBAM.C4.04), not resolved.
- V8 case manifest for CBAM does not list the legal-source row; the source hash is recorded in SOURCE_AND_METHOD_PROVENANCE.md (EVIDENCE_IDENTICAL_CONFIRMED_WITH_CBAM_MANIFEST_DOCUMENTATION_ASYMMETRY).
- V8 CBAM record identifiers (e.g. CFG1, A1) differ in format from the other V8 cases; native IDs are preserved as recorded.

## Schema additions (permitted as additional fields; no category or rule changed)

- `PAIR_HUMAN_REVIEW_QUEUE.csv`: added `comparison_level`, `external_evidence_dependency`, `possible_decisions`; `v8_record_refs`/`rgam_record_refs` hold `WITHHELD_SEE_PAIR_IDENTITY_KEY` to preserve reviewer blinding (identity held in `PAIR_IDENTITY_KEY.csv`).
- `PAIR_COMPARATIVE_UNIT_REGISTER.csv`, `PAIR_EVALUATION_DIMENSIONS.csv` (long form) and `PAIR_IDENTITY_KEY.csv` have no pre-frozen template; headers defined in this run.

## Unresolvable or limited units

- No unresolvable comparison unit. CBAM.C4.07 (strategy/logic/regime layer) is M7 by the method crosswalk (METHOD_SPECIFIC).
