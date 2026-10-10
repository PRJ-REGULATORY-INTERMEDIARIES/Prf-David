# Pair comparison QA — Regulation (EU) 2024/1689 — Artificial Intelligence Act

Run `CMP-R1-AI-20261007` · created 2026-10-07T10:04:15-03:00

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Unique comparison_proposition_id | **PASS** | 85 units |
| 2 | All V8 source IDs resolve in frozen V8 case registers; all RGAM source IDs resolve in frozen RGAM case tables | **PASS** | 0 unresolved |
| 3 | Exactly one initial M1-M7 category per unit | **PASS** | invalid: [] |
| 4 | M3 has V8 refs only; M4 has RGAM refs only unless annotated; M1/M2/M5/M6 reference both arms | **PASS** | inconsistent: [] |
| 5 | Many-to-many mappings allowed and used (no forced 1:1) | **PASS** | cardinality distribution: {'1:n': 23, '0:n': 18, 'n:m': 39, 'n:1': 2, '1:1': 1, 'n:0': 2} |
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
| 16 | Human decision/confidence/justification/reviewer/date fields blank on all cards | **PASS** | 21 cards |
| 17 | Identity key held in separate file; queue/cards expose no method labels | **PASS** | PAIR_IDENTITY_KEY.csv |
| 18 | No case-level winner, C-A–C-F category or F1–F7 assigned | **PASS** | Summary and registers contain no synthesis labels |
| 19 | Preregistered rules unchanged (C0–C4, M1–M7, D1–D8, H1–H11, materiality rule) | **PASS** | Codes imported verbatim; interpretive choices logged below, none amends a frozen rule |
| 20 | Frozen V8/RGAM/preregistration artefacts not modified by this run | **PASS** | All writes confined to 14_PAIRED_COMPARISON_ROUND1/PAIR_03_AI_ACT |

## Interpretive choices logged (no frozen rule modified)

- Same operationalisation of materiality as Pairs 1–2: informational/administrative relations or arrangements that attach to no configuration/architecture/property proposition in either arm are recorded as differences but NON_MATERIAL; relations/arrangements with legal effect, party identity, modality, configuration membership, architecture boundary or stopping level are potentially material. Arrangement-level RGAM-only units are treated as material where they carry substantive governance functions (rule-making control, authority-gated routes, authorisation of intrusive uses, individual remedies, sanctions, conformity routes, compliance routes for general-purpose models); administrative registration, communication and resource arrangements are non-material.
- The V8 AI Act package is a deliberately compact three-configuration reconstruction (11 relations); the RGAM package is a statement-level reconstruction (281 relations, 19 subconfigurations). The difference in coverage is not itself a difference; only the propositions listed below are compared, and a V8 non-statement is recorded as M4/M2 only where a legally grounded proposition exists in the common corpus and bears on a comparison unit.
- C0 statement-level coverage differences confined to provisions compared at C1–C3 are carried by one aggregated non-material unit (AI.C0.13).
- Absence-based assertions (H7) are queued even where both arms align (MATCHING_RULES), clustered in HQ-AI-21, plus cards where the arms treat the absence differently.
- RGAM internal HQ items (35) are not queued wholesale; only those touching a V8–RGAM difference are cross-referenced (HQ-001, 003, 006, 007, 014, 017, 019–024).
- RGAM 'INTEGRATED (provisional)' outcomes are ARCHITECTURE_CANDIDATE outcomes under I1–I4 with unvalidated I2/I3 thresholds; none is treated as a SUPPORTED_ARCHITECTURAL_CLAIM here. The same distinction applies to V8 higher-order inferences, which V8 itself labels 'higher-order'.
- The RGAM reference point (2 August 2026, Art. 113) is an RGAM scoping choice; V8 states no reference date.
- MSA-as-notified-body is carried by RGAM assignment NA-0126 and property PROP-011 (not by a qualified relation).
- Reading guide for D8 (V8): the 26 'POSSIBLE_MATERIAL_OMISSION' flags for V8 coincide with the 26 M4/M3-type units in which a legally grounded proposition exists in the common corpus and only RGAM states it. They are risks to be adjudicated, not findings; V8's package is a bounded three-configuration baseline governed by its own stopping rule, and no flag implies that V8 omitted something its protocol required. Conversely the D7/D8 flags for RGAM mark where its stopping, derivation or candidate outcomes may exceed or fall short of the corpus (e.g. AI.C3.04, C3.07, C1.25).

## Schema additions (permitted as additional fields; no category or rule changed)

- `PAIR_HUMAN_REVIEW_QUEUE.csv`: added `comparison_level`, `external_evidence_dependency`, `possible_decisions`; `v8_record_refs`/`rgam_record_refs` hold `WITHHELD_SEE_PAIR_IDENTITY_KEY` to preserve reviewer blinding (identity held in `PAIR_IDENTITY_KEY.csv`).
- `PAIR_COMPARATIVE_UNIT_REGISTER.csv`, `PAIR_EVALUATION_DIMENSIONS.csv` (long form) and `PAIR_IDENTITY_KEY.csv` have no pre-frozen template; headers defined in this run.

## Unresolvable or limited units

- No unresolvable comparison unit. AI.C4.07 (strategy/logic/regime layer) and AI.C4.11 (norm-type taxonomy) are M7: no common proposition can be built under the method crosswalk (METHOD_SPECIFIC).
