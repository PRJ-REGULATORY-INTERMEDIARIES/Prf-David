# Pair comparison QA — Regulation (EU) 2023/955 — Social Climate Fund

Run `CMP-R1-SCF-20261007` · created 2026-10-07T09:46:40-03:00

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Unique comparison_proposition_id | **PASS** | 57 units |
| 2 | All V8 source IDs resolve in frozen V8 case registers; all RGAM source IDs resolve in frozen RGAM case tables | **PASS** | 0 unresolved |
| 3 | Exactly one initial M1-M7 category per unit | **PASS** | invalid: [] |
| 4 | M3 has V8 refs only; M4 has RGAM refs only unless annotated; M1/M2/M5/M6 reference both arms | **PASS** | inconsistent: [] |
| 5 | Many-to-many mappings allowed and used (no forced 1:1) | **PASS** | cardinality distribution: {'1:n': 6, 'n:m': 41, '0:n': 4, 'n:1': 4, 'n:0': 2} |
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
| 16 | Human decision/confidence/justification/reviewer/date fields blank on all cards | **PASS** | 12 cards |
| 17 | Identity key held in separate file; queue/cards expose no method labels | **PASS** | PAIR_IDENTITY_KEY.csv |
| 18 | No case-level winner, C-A–C-F category or F1–F7 assigned | **PASS** | Summary and registers contain no synthesis labels |
| 19 | Preregistered rules unchanged (C0–C4, M1–M7, D1–D8, H1–H11, materiality rule) | **PASS** | Codes imported verbatim; interpretive choices logged below, none amends a frozen rule |
| 20 | Frozen V8/RGAM/preregistration artefacts not modified by this run | **PASS** | All writes confined to 14_PAIRED_COMPARISON_ROUND1/PAIR_01_SCF |

## Interpretive choices logged (no frozen rule modified)

- Materiality operationalisation (no frozen rule changed): relations that are purely informational/promotional support duties and that attach to no configuration, property or architecture proposition in either arm are recorded as differences but NON_MATERIAL (H1 speaks of a *material* relation). Relations with legal effect on funding, authority, accountability or configuration membership are treated as potentially material.
- C0 statement-level coverage differences confined to provisions already compared at C1–C3 are carried by one aggregated non-material unit (SCF.C0.07); materiality is assessed at the relational/configurational level to avoid double counting the same difference.
- Absence-based assertions (H7) are queued even where both arms align, in line with MATCHING_RULES; they are clustered in a single low-priority card (HQ-SCF-09) plus the two cards where the arms treat the absence differently.
- RGAM internal HQ items are NOT queued wholesale (89 across the family). RGAM HQ-001/002/003/007/012–018 appear only as cross-references where they touch a V8–RGAM difference; the 'I2/I3 thresholds unvalidated' caveat (UNC-039) is treated as an RGAM-internal calibration statement.
- Case-level V8 directory controls; the V8 family-root registers duplicate the last case and were not used.
- For the V8 narrative-only statements (transfers, technical guidance) the ref token V8_NATIVE_ANALYSIS is used because no typed V8 record exists.

## Schema additions (permitted as additional fields; no category or rule changed)

- `PAIR_HUMAN_REVIEW_QUEUE.csv`: added `comparison_level`, `external_evidence_dependency`, `possible_decisions`; `v8_record_refs`/`rgam_record_refs` hold `WITHHELD_SEE_PAIR_IDENTITY_KEY` to preserve reviewer blinding (identity held in `PAIR_IDENTITY_KEY.csv`).
- `PAIR_COMPARATIVE_UNIT_REGISTER.csv`, `PAIR_EVALUATION_DIMENSIONS.csv` (long form) and `PAIR_IDENTITY_KEY.csv` have no pre-frozen template; headers defined in this run.

## Unresolvable or limited units

- No unresolvable comparison unit. SCF.C4.06 (regime/strategy/logic layer) is M7 by the method crosswalk (METHOD_SPECIFIC), not a failure.
