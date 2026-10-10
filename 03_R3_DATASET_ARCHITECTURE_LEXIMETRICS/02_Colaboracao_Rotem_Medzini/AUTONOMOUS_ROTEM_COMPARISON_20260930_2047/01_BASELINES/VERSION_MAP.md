# VERSION_MAP (R01)

Versions were identified by SHA-256, size, file date and internal document metadata. File names alone were not used to decide identity. Hashes are in `SOURCE_REGISTER.csv` and `BASELINE_HASHES.csv`.

## 1. Rotem / codebook family (three schema layers)

| Layer | Source ID | File | SHA-256 (prefix) | Internal metadata | Status in this run |
|---|---|---|---|---|---|
| LAYER_1_CONCEPTUAL | SRC-ROTEM-EMAIL | `Enviados/30_09_26/email e chat`, lines 1–20 | 546E4BBC06BF | plain text, file date 2026-09-30 07:45 | Canonical Rotem text. Possible truncation (I-005) |
| LAYER_2_DOCUMENTED (a) | SRC-CB-UNREV | `Downloads/Codebook - Regulatory Intermediation (1).docx` | 35982A3916BC | last_modified_by David Levi Faur, 2026-09-04, rev. 174 | `UNREVISED_BASELINE`. Codebook text is ¶1–¶144 only. ¶145–¶339 are embedded review commentary whose author is not established (I-006) |
| LAYER_2_DOCUMENTED (a) | SRC-CHARTKEY | `Downloads/Chart Key - Regulatory Intermediation (2).docx` | 87FA617FA467 | last_modified_by Rotem Medzini, 2026-08-31, rev. 84 | `UNREVISED_BASELINE` |
| LAYER_2_DOCUMENTED (b) | SRC-CB-REV = SRC-CB-REV-DL | `PILOT_01/00_SOURCES/Codebook_Regulatory_Intermediation_Revised (1).docx` (identical copy in Downloads) | 7FE634455AED | last_modified_by David Levi Faur, 2026-09-28, rev. 32 | Revised codebook. Who made each revision is not established (I-007) |
| LAYER_3_IMPLEMENTED | SRC-WB = SRC-WB-DL | `PILOT_01/00_SOURCES/dataset_of_EU_regulatory_intermediation.xlsx` (identical copy in Downloads) | 529F818E21B5 | creator and last_modified_by Rotem Medzini, 2026-04-10 → 2026-09-02; 6 sheets | Implemented schema. The workbook (last saved 2 Sep) is **older** than the revised codebook (28 Sep) |

**Chronology from metadata:**
1. Chart Key, 31 Aug.
2. Workbook last saved, 2 Sep.
3. Unrevised codebook, 4 Sep.
4. Revised codebook, 28 Sep.
5. Rotem's e-mail, received before the 30 Sep 07:45 file date.

The revised schema (INTERMEDIARY_MAP, `regulator_context`, `target_context`, `orientation`, `mechanism_family`, `Function_registry_administration`, disaggregated obligations) therefore post-dates the implemented workbook. A gap between Layer 2(b) and Layer 3 is expected by construction and is not, by itself, a defect (delta §6: `DOCUMENTATION_IMPLEMENTATION_GAP`).

## 2. Relational (Igor) family

| Artefact | Version / location | Notes |
|---|---|---|
| Earlier R–I–T codebooks | `Before_R2/dataset-eurlex/methodology/codebook.md`, `v1.1.x` | Igor's provision-anchored codebook. Not Rotem's |
| R1 report | `Downloads/EU_green_…_progress_report_REVISED.docx` (A4472478…), plus earlier `…report.docx` (B96A413D…) and `…REVISED (1).docx` (A2EF08F0…) | Three distinct hashes = three versions. REVISED (rev. 2, last_modified_by Igor Caires, 2026-09-13 12:17) is taken as the latest |
| R2 | `Downloads/R2_METHOD_REPORT_TAXONOMY_CALIBRATION_v1_2.docx`, `R2_calibration_…_v1_2_audited.xlsx`, `R2_DAVID_VALIDATION_PACKAGE_v1_3.zip` | Taxonomy Regulation (32020R0852) calibration |
| R2.1 | `WORK_2_1/PILOT_R2_1/` | Stopped at `PHASE_0B_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION` |
| R3_CLEANROOM | `R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM/` | Staging copy of `C:/PROJETOS/ICM-PMO/.../R3_CLEANROOM` (not re-read here; its equivalence was reported by the planning exploration and is recorded as `UNVERIFIED_IN_THIS_RUN`) |
| R4 | `R4_CROSS_DOMAIN_VALIDATION/` (working) and `ENVIO_R4_TO_DAVID/` (delivery) | `R4_STRUCTURAL_EXTRACTION.csv` has the same hash in both (45F1C05C…) |
| PILOT_01/02/03 | `RELATIONAL_LEXIMETRICS_PILOT/` | Untracked in git. PILOT_03 pre- and post-adjudication manifests both present |

## 3. Duplicate / variant pairs resolved by hash

| Pair | Result |
|---|---|
| SRC-CB-REV vs SRC-CB-REV-DL | identical (7FE63445…) |
| SRC-WB vs SRC-WB-DL | identical (529F818E…) |
| SRC-R4-EXTR vs SRC-R4-EXTR-WORK | identical (45F1C05C…) |
| SRC-R4-SYSAUD-01 vs -02 (`…AUDIT.csv` vs `…AUDIT_UPDATED.csv`) | identical (C1EC0373…) despite different names |
| SRC-R4-LUNAREV-01 vs -02 (delivery vs `r4_2c_working_copies/`) | **different** (5104298A… vs 0370B299…). The delivery copy is used; the difference is not investigated further (not needed for the comparison) |
| SRC-P03-ADJ-04 (project) vs SRC-P03-FILLED-DL (Downloads) | identical (78A99F4F…); this matches the input hash recorded in `PILOT_03_MANIFEST_FINAL.json` |
