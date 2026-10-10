# Pre-adjudication descriptive summary — NEW TEST 3x3 Round 1 (four cases)

Comparator: claude-sonnet-5-5 (UI: Claude Sonnet 5.5 High; reasoning effort not exposed to executor; user-confirmed High) · Protocol manifest `0eeab8866b404523012ae39a1ff3e01ea15466ae4ff54a4c49a1a1bcfd2a514a` · Created 2026-10-07T10:11:37-03:00

> Descriptive only. This summary does not conclude that either method is superior, that RGAM has substantive gain or regression, and assigns no C-A–C-F category and no F1–F7 category. Counts of units, records, relations, configurations, files or words are not evidence of quality. Climate replication and transfer analysis are not performed.

## 1. Comparative units by case, level and initial match category

| Case | C0 | C1 | C2 | C3 | C4 | Total | M1 | M2 | M3 | M4 | M5 | M6 | M7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SCF | 11 | 16 | 8 | 14 | 8 | 57 | 26 | 19 | 1 | 6 | 1 | 3 | 1 |
| CBAM | 15 | 22 | 8 | 15 | 10 | 70 | 27 | 30 | 1 | 8 | 1 | 2 | 1 |
| AI | 13 | 29 | 14 | 18 | 11 | 85 | 30 | 24 | 1 | 26 | 1 | 0 | 3 |
| DIR | 11 | 16 | 3 | 12 | 10 | 52 | 30 | 9 | 1 | 10 | 0 | 1 | 1 |
| **All** | 50 | 83 | 33 | 59 | 39 | **264** | 113 | 82 | 4 | 50 | 3 | 6 | 6 |

## 2. Materiality (frozen rule; initial categories preserved)

| Case | Units with a difference (M2–M7) | COMPARATIVELY_MATERIAL | Non-material | Material by level (C0/C1/C2/C3/C4) |
|---|---|---|---|---|
| SCF | 31 | 22 | 9 | 1/4/6/8/3 |
| CBAM | 43 | 29 | 14 | 0/9/8/8/4 |
| AI | 55 | 36 | 19 | 0/15/11/5/5 |
| DIR | 22 | 9 | 13 | 0/2/1/2/4 |
| **All** | 151 | **96** | 55 | 1/30/26/23/16 |

## 3. D1–D8 descriptive distributions (material units only; pre-adjudication, provisional; no composite, no ranking)

| Dimension | Status distribution (all four cases) |
|---|---|
| D1 | EXTERNAL_DEPENDENCY=20; INDETERMINATE=26; PARTIALLY_SUPPORTED=18; SUPPORTED=32 |
| D2 | MATERIAL=36; MINOR=60 |
| D3 | EQUIVALENT=51; NOT_APPLICABLE=45 |
| D4 | EQUIVALENT=21; NOT_APPLICABLE=37; RGAM_CLEARER=38 |
| D5 | DIFFERENT_NONORDERABLE=20; EQUIVALENT=2; NOT_APPLICABLE=33; RGAM_GAIN=41 |
| D6 | INDETERMINATE=93; WELL_CALIBRATED_BOTH=3 |
| D7 (V8) | NO_EVIDENCE_OF_OVERINFERENCE=58; POSSIBLE_OVERINFERENCE=38 |
| D7 (RGAM) | NO_EVIDENCE_OF_OVERINFERENCE=90; POSSIBLE_OVERINFERENCE=6 |
| D8 (V8) | NO_MATERIAL_OMISSION=41; POSSIBLE_MATERIAL_OMISSION=55 |
| D8 (RGAM) | NO_MATERIAL_OMISSION=81; POSSIBLE_MATERIAL_OMISSION=15 |

Reading guide: `POSSIBLE_*` flags are risks conditional on the linked open human-review card; they are not findings. The per-method counts of such flags are not a method comparison: each follows where an arm records, or does not record, a proposition the other states, and RGAM-only propositions (M4) are numerous in the larger instruments because RGAM works at statement level. Per-case notes in each `PAIR_COMPARISON_QA.md` give the same caution.

## 4. Human-review queue

- Unique review cards: **56** (SCF 12; CBAM 16; AI Act 21; Directive 7)
- Trigger distribution across cards (a card may carry several triggers): H1=15, H2=7, H3=2, H4=14, H5=12, H6=11, H7=14, H8=18, H9=13, H10=22, H11=7
- Cards by comparative level of the principal proposition: C0=1, C1=16, C2=11, C3=22, C4=6
- Cards by priority label (reviewer-facing convenience; not a method ranking): HIGH=13, LOW=11, MEDIUM=32
- Cards whose question depends on legal evidence outside the instrument's own text: **19** (HQ-SCF-04, HQ-SCF-06, HQ-SCF-07, HQ-SCF-08, HQ-SCF-10, HQ-CBAM-06, HQ-CBAM-08, HQ-CBAM-11, HQ-CBAM-12, HQ-CBAM-13, HQ-CBAM-14, HQ-CBAM-15, HQ-AI-05, HQ-AI-07, HQ-AI-10, HQ-AI-17, HQ-AI-18, HQ-DIR-01, HQ-DIR-05)
- Blind assignment of proposition A: V8 in 31 cards, RGAM in 25 cards (deterministic hash rule, recorded in the identity key)
- Affected levels (levels with ≥1 material difference or card): C0, C1, C2, C3, C4

## 5. Raw cost descriptors already documented by each arm (descriptive; no additional-cost label assigned)

| Case | V8 analytical records | V8 artefacts | RGAM analytical records | RGAM artefacts | RGAM internal HQ items | RGAM unresolved external references | RGAM instrument-level result |
|---|---|---|---|---|---|---|---|
| SCF | 40 (claims=15; relations=9; configurations=3; architecture=1; uncertainties=12) | 10 | 482 | 27 | 19 | 13 | OVERLAPPING_OR_PARTIALLY_INTEGRATED / highest A |
| CBAM | 43 (claims=16; relations=10; configurations=5; architecture=1; uncertainties=11) | 10 | 488 | 27 | 16 | 17 | OVERLAPPING_OR_PARTIALLY_INTEGRATED / highest A |
| AI | 38 (claims=14; relations=11; configurations=3; architecture=1; uncertainties=9) | 10 | 1163 | 27 | 35 | 39 | OVERLAPPING_OR_PARTIALLY_INTEGRATED / highest A |
| DIR | 47 (claims=21; relations=12; configurations=1; architecture=1; uncertainties=12) | 10 | 232 | 27 | 19 | 4 | INDETERMINATE / highest S |

Workflow stages documented: V8 — Level I–III ladder with stopping-rule record; RGAM — frozen multi-table protocol (W declaration, unit inventory/screening, statements, assignments, positions/devices, qualified relations, subconfigurations, I1–I4 candidate assessment, property register, closure register, HQ queue). These are descriptors only; whether any additional analytical cost is low, moderate or high relative to observed contribution is **not assessed** at Round 1 (Q7 is deferred until adjudication).

## 6. Status

`PAIRED_MATCHING_FROZEN / HUMAN_ADJUDICATION_REQUIRED / CASE_SYNTHESIS_NOT_STARTED`
