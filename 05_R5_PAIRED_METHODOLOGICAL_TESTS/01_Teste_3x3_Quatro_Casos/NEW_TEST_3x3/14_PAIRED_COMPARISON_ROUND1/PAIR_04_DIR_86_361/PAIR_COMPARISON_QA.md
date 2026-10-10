# Pair comparison QA — Council Directive 86/361/EEC — initial stage of mutual recognition of type approval for telecommunications terminal equipment

Run `CMP-R1-DIR-20261007` · created 2026-10-07T10:09:25-03:00

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Unique comparison_proposition_id | **PASS** | 52 units |
| 2 | All V8 source IDs resolve in frozen V8 case registers; all RGAM source IDs resolve in frozen RGAM case tables | **PASS** | 0 unresolved |
| 3 | Exactly one initial M1-M7 category per unit | **PASS** | invalid: [] |
| 4 | M3 has V8 refs only; M4 has RGAM refs only unless annotated; M1/M2/M5/M6 reference both arms | **PASS** | inconsistent: [] |
| 5 | Many-to-many mappings allowed and used (no forced 1:1) | **PASS** | cardinality distribution: {'1:n': 13, 'n:m': 27, 'n:1': 3, '0:n': 7, 'n:0': 2} |
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
| 16 | Human decision/confidence/justification/reviewer/date fields blank on all cards | **PASS** | 7 cards |
| 17 | Identity key held in separate file; queue/cards expose no method labels | **PASS** | PAIR_IDENTITY_KEY.csv |
| 18 | No case-level winner, C-A–C-F category or F1–F7 assigned | **PASS** | Summary and registers contain no synthesis labels |
| 19 | Preregistered rules unchanged (C0–C4, M1–M7, D1–D8, H1–H11, materiality rule) | **PASS** | Codes imported verbatim; interpretive choices logged below, none amends a frozen rule |
| 20 | Frozen V8/RGAM/preregistration artefacts not modified by this run | **PASS** | All writes confined to 14_PAIRED_COMPARISON_ROUND1/PAIR_04_DIR_86_361 |

## Interpretive choices logged (no frozen rule modified)

- SPECIAL RULE (Directive 86/361): the RGAM instrument-level result is INDETERMINATE with highest supported level S. RGAM ARCH-01 and ARCH-02 are ARCHITECTURE_CANDIDATE records, not SUPPORTED_ARCHITECTURAL_CLAIM; no unit treats a raw RGAM 'A' row as an accepted architectural conclusion. V8's A01 is a higher-order inference that V8 labels high-confidence; it is likewise treated as an inference to be compared, not as an adjudicated claim.
- Materiality operationalisation as in Pairs 1–3 (informational/administrative relations attached to no configuration/architecture/property proposition are non-material; relations with legal effect, party identity, modality, configuration membership or architecture boundary may be material).
- The agreement between the arms at C1–C2 is high for this instrument; the principal differences are at C3–C4 (existence/stopping level of the architecture and its external-dependency sensitivity). Agreement is recorded as M1 and not queued.
- Absence-based assertions (H7) are queued even where both arms align (MATCHING_RULES), clustered in HQ-DIR-07.
- RGAM internal HQ items (19) are not queued wholesale; HQ-016/017 are cross-referenced where they touch the V8–RGAM architecture difference.
- The RGAM CASE_GATE records a recovery run (2026-10-07) with corrections logged by the recovery executor; the frozen RGAM case manifest verified identical to its detached hash, and that frozen package is the comparison object.
- RGAM states the legal status at the declared interval (adoption 1986-07-24 to repeal 1992 per neutral metadata); V8 states no reference date. Recorded (DIR.C4.08), not resolved.

## Schema additions (permitted as additional fields; no category or rule changed)

- `PAIR_HUMAN_REVIEW_QUEUE.csv`: added `comparison_level`, `external_evidence_dependency`, `possible_decisions`; `v8_record_refs`/`rgam_record_refs` hold `WITHHELD_SEE_PAIR_IDENTITY_KEY` to preserve reviewer blinding (identity held in `PAIR_IDENTITY_KEY.csv`).
- `PAIR_COMPARATIVE_UNIT_REGISTER.csv`, `PAIR_EVALUATION_DIMENSIONS.csv` (long form) and `PAIR_IDENTITY_KEY.csv` have no pre-frozen template; headers defined in this run.

## Unresolvable or limited units

- No unresolvable comparison unit. DIR.C4.06 (strategy/logic/regime layer) is M7 by the method crosswalk (METHOD_SPECIFIC).
