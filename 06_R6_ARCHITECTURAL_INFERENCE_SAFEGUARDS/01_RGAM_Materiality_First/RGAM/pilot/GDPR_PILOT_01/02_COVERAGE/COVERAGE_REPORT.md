# Coverage report — GDPR Pilot 01

**Status:** descriptive; the screening and extraction are machine-generated and provisional (single evaluator, no independent coding). This report states what was actually covered.

## 1. What was covered

- **Instrument:** Regulation (EU) 2016/679, all 99 articles, in the authentic OJ L 119 text with the 2018 corrigendum applied (18 of 18 corrigendum substitutions applied; log in `01_SOURCES/parsed/corrigendum_application_log.json`).
- **Units:** 389 paragraph units (single-paragraph articles count as one unit; Art. 4 is one unit with 26 definition points). **All 389 were screened** — no unit is pending. A complete **point-level** inventory (382 points) exists in `01_SOURCES/SOURCE_UNIT_INVENTORY.csv`, but **points were screened inside their paragraph, not individually**.
- **Recitals:** 173 recitals extracted into the working text; **not reviewed** as interpretive context beyond classification as non-operative. No record was created from a recital.
- **Detailed extraction:** performed for every unit screened relevant ("Yes"/"Uncertain") in article order (batches 01–10 = Chapters I–XI); one unit (Art. 21(5)) is on Hold. So the detailed extraction is *complete at paragraph level and partial at point level*; it is **not** a validated reconstruction.

## 2. Screening results

| Chapter | Articles | Units | Points (inventoried) | Yes | Uncertain | No | Units with QR | Units with NA | Units with EXT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| I | 1–4 | 11 | 32 | 1 | 2 | 8 | 0 | 3 | 4 |
| II | 5–11 | 20 | 29 | 11 | 2 | 7 | 3 | 10 | 0 |
| III | 12–23 | 45 | 80 | 34 | 1 | 10 | 31 | 3 | 1 |
| IV | 24–43 | 109 | 75 | 92 | 2 | 15 | 45 | 53 | 4 |
| V | 44–50 | 26 | 39 | 19 | 0 | 7 | 7 | 15 | 4 |
| VI | 51–59 | 36 | 58 | 34 | 1 | 1 | 19 | 20 | 2 |
| VII | 60–76 | 76 | 48 | 68 | 0 | 8 | 52 | 18 | 4 |
| VIII | 77–84 | 30 | 19 | 30 | 0 | 0 | 21 | 11 | 0 |
| IX | 85–91 | 16 | 0 | 15 | 0 | 1 | 4 | 11 | 0 |
| X | 92–93 | 8 | 0 | 8 | 0 | 0 | 5 | 7 | 3 |
| XI | 94–99 | 12 | 2 | 9 | 0 | 3 | 2 | 7 | 4 |
| **Total** | **1–99** | **389** | **382** | **321** | **8** | **60** | **189** | **158** | **26** |

Extraction status: Extracted 328; Not applicable 60; Hold 1. Screening status: Reviewed 381; Uncertain 8.

**How to read "Yes".** The criterion is deliberately inclusive (DR §3): a unit is "Yes" if it yields at least one normative assignment, position/device or relation. 321 of 389 units (82%) therefore pass. The discriminating figures are the **189 units that carry a qualified relation** (49%) and the **60 units with no governance observation** (15%), plus the **35 regulated-side assignments with no counterpart** (SC-15), which show that a considerable part of the text assigns duties without a legally identifiable counterparty or forum.

A legitimate "no relational observation" result exists for whole articles: Arts 1–3 (Art. 1(3) and 2(3) yield an assignment with an unstated subject but no relation), 9(1)–(3), 22(2),(4), 27(2),(5), 89(4), 94(1), 95, 96 were screened "No" or yielded no relation.

## 3. Limits

1. **Granularity:** points screened within paragraphs (UNC-004).
2. **Recitals:** not reviewed (UNC-014).
3. **External sources:** 22 reference rows for about 16 distinct sources; **none retrieved**; generic references to national law incompletely registered (UNC-011, UNC-012).
4. **Temporal:** baseline legal status uniform (UNC-013); the 2021 corrigendum (CELEX 32016R0679R(03)) was not retrievable in English; later amendments not verified.
5. **Machine-provisional:** a single model run; no independent coding; no reliability statistic.

No claim in this report asserts that the GDPR has been "reconstructed". It states that every article of the baseline text was inventoried and screened, and that records were extracted from 328 units (the Hold unit, Art. 21(5), has only an external-reference row).
