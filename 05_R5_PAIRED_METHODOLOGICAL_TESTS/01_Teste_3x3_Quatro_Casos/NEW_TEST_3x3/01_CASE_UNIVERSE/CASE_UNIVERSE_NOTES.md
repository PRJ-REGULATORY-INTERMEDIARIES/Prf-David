# NEW TEST 3x3 — CASE UNIVERSE NOTES

**Files:** `CASE_UNIVERSE_MASTER.csv` (174 case-version rows) · `CASE_SOURCE_PROVENANCE.csv` (1,044 metric-provenance rows, with SHA-256 of every source file)
**Unit of the master:** one row per (legal instrument × source version). Versions of one instrument are linked by `canonical_case_id` and are **never merged**; `is_canonical_version` follows rule G5.

## 1. How the universe was found

A full scan of the repository (518 CSV files catalogued by header and row count; XLSX, JSON and Markdown inspected where relevant) located every place where legal instruments are linked to actors, regulators, intermediaries, targets or relations. Eleven source families were found (table in §3). Previous experiments were opened read-only; nothing was copied into them or modified.

## 2. Counts

| Item | Number |
|---|---:|
| Case-version rows in the master | 174 |
| Distinct **studied** legal instruments (extracted/coded in a PRJ-David pilot or dataset) | **29** |
| Distinct canonical case ids incl. Rotem-only rows | 130 |
| Prohibited V8-stage items listed but not opened (non-circularity) | 2 |

Disposition of the 174 rows: `ELIGIBLE` 5 · `CONDITIONALLY_ELIGIBLE` 2 · `NON_COMPARABLE` 20 · `INSUFFICIENT_SOURCE` 3 · `DUPLICATE_VERSION` 41 · `OTHER_DOCUMENTED_EXCLUSION` 103 (101 Rotem-only rows + 2 prohibited items). Disposition of the 29 studied instruments (by canonical version): **5 eligible**, **2 conditionally eligible**, **19 non-comparable**, **3 insufficient source** (Taxonomy Regulation 2020/852, MDR 2017/745, Lei 13.848/2019). No discovered row has been dropped.

## 3. Source families and treatment

| Family | Instruments | Scope | Why this disposition |
|---|---|---|---|
| **R3 clean-room** (frozen 2026-09-21) | ETS Dir. 2003/87, MSR Dec. 2015/1814, ESR 2018/842, Climate Law 2021/1119, Social Climate Fund 2023/955 | FULL_INSTRUMENT | eligible: whole-instrument actor register, census of 56 relations adjudicated under one R–I–T gate |
| **R2 `dataset-eurlex`** (final_human_review_v2 + earlier versions) | Climate Law, CBAM 2023/956, EUDR 2023/1115 | FULL_INSTRUMENT | CBAM/EUDR conditionally eligible (stratum S2); Climate Law R2 is a version of the R3 case |
| **PoC v1–v4** | CSRD 2022/2464, Ecolabel 66/2010, Benchmarks 2019/2089, ETS verification 2018/2067, Taxonomy 2020/852 | LIMITED_PROVISIONS (Taxonomy: UNKNOWN) | non-comparable; Taxonomy has no records |
| **PILOT_01–03** | 76/889, 86/361, 87/95, 89/336, 91/263, 92/44, 2004/48, 874/2004, 2006/115, 1781/2006 | LIMITED_PROVISIONS | non-comparable (2–6 purposively selected provisions; model-pass edges; pre-adjudication) |
| **R4 digital** | GDPR 2016/679, DSA 2022/2065, AI Act 2024/1689 | FULL_INSTRUMENT (structural) | non-comparable: R/I/T never coded |
| **GDPR_PILOT_01** (RGAM/V6) | GDPR | SUBSTANTIAL_DEFINED_SUBSET (articles only) | version of the GDPR case under a different ontology; architectural outputs not opened |
| **Rotem lists** | P2B 2019/1150, CDSM 2019/790, DSA (22 rows) | UNKNOWN | non-comparable: different construct (intermediary labels) |
| **Rotem comparison packs / Codex package** | 874/2004, 89/336, 91/263, 86/361, DSA Arts 21/22/37/42 | LIMITED_PROVISIONS | versions (diagnostic provision packs), no case-level metric |
| **V8_COMP_01 provisional** | MDR 2017/745, Lei 13.848/2019 (Brazil) | UNKNOWN | insufficient source: never extracted |
| **Rotem-only rows** | 101 act rows of Rotem's `Coding Digital Intermediaries` sheet that no PRJ-David pilot studied | UNKNOWN | documented exclusion: free-text act-level coding, no countable relations; no new legislation is added at this stage |
| **Prohibited V8 outputs** | V8_COMP_01 Track A/B; RGAM `GDPR_V8` | — | listed only (non-circularity) |

## 4. Version relationships (not merged)

| Instrument | Versions in the repository | Canonical (G5) | Notes |
|---|---|---|---|
| European Climate Law 32021R1119 | R3 frozen (1 intermediation relation); R2 final v2 (3); R2 proposals v1.0 / v1.1 / R2 reading (1 / 0 / 1); R2 export sent to David (3); R2 Stage-4 candidate adjudication (0 positive of 90) | **R3 frozen** | the only instrument covered by two full-instrument pipelines → used as the comparability bridge |
| CBAM 32023R0956, EUDR 32023R1115 | R2 v1.0 → v1.1 → R2 reading → final v2 → export sent to David | R2 final v2 | intermediation counts change across versions (CBAM 5/7/3/5; EUDR 3/2/3/4); export carries 20 of the 25 final relation records (uncertain/not-supported not carried) |
| PoC acts | PoC v1 (4 sample rows) → v2 → v3 → v4 | v4 | v4 adds the Taxonomy screening (13 hits) |
| PILOT acts | PILOT_01 → PILOT_02 → PILOT_03 (five acts in all three; five more only in PILOT_03) | PILOT_03 v0.3 | PILOT_03 counts are model-pass rows, 19 human decisions kept separately |
| GDPR | R4 structural extraction (frozen original text) ; GDPR_PILOT_01 (corrected/consolidated baseline, RGAM ontology) | R4 (full instrument) | two different ontologies and text baselines |
| DSA | R4 structural extraction ; Rotem list (22 rows) ; Rotem comparison pack (16 R4 rows for Arts 21/22/37/42) | R4 | |

## 5. Data-quality and provenance flags found during discovery

- `Before_R2/dataset-eurlex/cases/R2_HUMAN_VALIDATION_relations.csv` is corrupted (documented in `PRODUCTION_CHANGELOG.md`); the R2 final package reconstructs it. It was not repaired or modified here.
- `Before_R2/Estudos Preliminares e testes/v1/PoC/data/rit_coded_sample.csv` is a ragged CSV (pandas cannot parse it); rows were counted with the `csv` module.
- The R3 workbook states its normalized tables are authoritative; they exist in `R3_HISTORY_STAGING` and reconcile to the frozen totals (`R4_R3_RECONCILIATION.csv`: all PASS).
- The R2 sent workbook (`Enviados/Email 01/…xlsx`) stores formulas without cached values for its summary; its values were recomputed from the detail sheets.
- R4: 181 of 1,404 structural records have no stored source excerpt; counterpart/recipient fields are identical in all records (R4 summary).
- Rotem-only rows include communications, resolutions, a Hebrew-titled row and untitled rows; they are kept as listed.

## 6. What was deliberately not opened

`TRACK_A/`, `TRACK_B/`, `CROSS_MODEL_REPLICATION/`, `G4_COMPARISON_PREPARATION/` (V8_COMP_01), `RGAM/V8_ACTIVE/04_EMPIRICAL_PILOT/GDPR_V8/`, GDPR_PILOT_01 reconstruction/assessment folders, `FOUNDATIONAL_PAPER_REVIEW/`. Pointer-only files from V8_COMP_01 are listed in `00_PROTOCOL/NON_CIRCULARITY_RULES.md`.

## 7. Ambiguities and uncertainties

1. Whether Rotem's external dataset belongs to the "studied universe" is a judgement: it is a project dataset, but only 10 of its acts (plus P2B/CDSM/DSA lists) entered a PRJ-David pilot; the rest are kept as documented exclusions rather than dropped.
2. GDPR_PILOT_01 scope is classified `SUBSTANTIAL_DEFINED_SUBSET` (all 99 articles, no recitals) rather than full instrument.
3. PoC `32019R2089` (benchmarks) has no stored positive relation (conditional candidate), so its relation metrics are not recorded rather than recorded as zero.
4. The year/jurisdiction fields for Rotem-only rows are as written by Rotem and were not verified.
