# RGAM four-case family — cross-case descriptive summary

**Status:** descriptive only; machine-assembled from the four frozen case directories; every number below is a count taken from, or recomputed from, the frozen case tables. Counts are descriptors of what each case recorded; they are not scores, rates, quality indicators or rankings, and the four cases have different source sizes. "Total" columns are arithmetic sums over the four cases and carry no further meaning. This file reports what each frozen case recorded; it does not interpret what any provision of any instrument "means", does not adjudicate any human-review item, and contains no comparison with any other method.

Case labels used below: C1_SCF = RGAM_C1_SCF (Regulation (EU) 2023/955); C2_CBAM = RGAM_C2_CBAM (Regulation (EU) 2023/956); AI_AI_ACT = RGAM_AI_AI_ACT (Regulation (EU) 2024/1689); O_DIR_86_361 = RGAM_O_DIR_86_361 (Directive 86/361/EEC).

## 1. Cases, frozen status and verified inputs

| Case | Instrument | Case gate (as recorded) | Source hash vs capsule | Contamination status (case access log) | Case manifest (recomputed) |
|---|---|---|---|---|---|
| RGAM_C1_SCF | Regulation (EU) 2023/955 — Social Climate Fund (CELEX 32023R0955) | RGAM_CASE_FROZEN | MATCH | CLEAN | OK (`7fd01ed8e0e95616...`) |
| RGAM_C2_CBAM | Regulation (EU) 2023/956 — CBAM (CELEX 32023R0956) | RGAM_CASE_FROZEN | MATCH | CLEAN | OK (`84647523b5800816...`) |
| RGAM_AI_AI_ACT | Regulation (EU) 2024/1689 — Artificial Intelligence Act (CELEX 32024R1689) | RGAM_CASE_FROZEN | MATCH | CLEAN | OK (`160217c11f2cf5e7...`) |
| RGAM_O_DIR_86_361 | Directive 86/361/EEC — terminal equipment type approval (CELEX 31986L0361) | RGAM_CASE_FROZEN | MATCH | CLEAN | OK (`3dc9add69f04c3a9...`) |

## 2. Counts by RGAM stratum (per case and total)

Stratum mapping, as instructed for this family stage (from `RGAM_CASE_OUTPUT_SCHEMA.md` section 2): **E** = SOURCE_UNIT_INVENTORY + INSTITUTIONAL_STATEMENTS; **P** = NORMATIVE_ASSIGNMENTS + POSITIONS_AND_DEVICES; **R** = QUALIFIED_RELATIONS + EXTERNAL_REFERENCES; **S** = SUBCONFIGURATIONS; **A** = ARCHITECTURE_CANDIDATES. (The schema also maps UNIT_SCREENING to E and TRACE_DEMONSTRATIONS to A; they are given in the per-table counts below, not added to the stratum counts.)

| Stratum / table | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| E - SOURCE_UNIT_INVENTORY | 706 | 558 | 1553 | 93 | 2910 |
| E - INSTITUTIONAL_STATEMENTS | 188 | 174 | 400 | 86 | 848 |
| **E subtotal** | 894 | 732 | 1953 | 179 | 3758 |
| P - NORMATIVE_ASSIGNMENTS | 63 | 65 | 251 | 20 | 399 |
| P - POSITIONS_AND_DEVICES | 28 | 27 | 71 | 12 | 138 |
| **P subtotal** | 91 | 92 | 322 | 32 | 537 |
| R - QUALIFIED_RELATIONS | 60 | 101 | 281 | 39 | 481 |
| R - EXTERNAL_REFERENCES | 46 | 33 | 59 | 10 | 148 |
| **R subtotal** | 106 | 134 | 340 | 49 | 629 |
| S - SUBCONFIGURATIONS | 7 | 11 | 19 | 6 | 43 |
| A - ARCHITECTURE_CANDIDATES | 3 | 7 | 9 | 2 | 21 |


Records per stratum, total over the five strata (E+P+R+S+A) per case: C1_SCF = 1101; C2_CBAM = 976; AI_AI_ACT = 2643; O_DIR_86_361 = 268.

### 2.1 Rows in all 19 frozen tables

| Table | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| W_DECLARATION | 1 | 1 | 1 | 1 | 4 |
| SOURCE_UNIT_INVENTORY | 706 | 558 | 1553 | 93 | 2910 |
| UNIT_SCREENING | 706 | 558 | 1553 | 93 | 2910 |
| INSTITUTIONAL_STATEMENTS | 188 | 174 | 400 | 86 | 848 |
| NORMATIVE_ASSIGNMENTS | 63 | 65 | 251 | 20 | 399 |
| POSITIONS_AND_DEVICES | 28 | 27 | 71 | 12 | 138 |
| QUALIFIED_RELATIONS | 60 | 101 | 281 | 39 | 481 |
| EXTERNAL_REFERENCES | 46 | 33 | 59 | 10 | 148 |
| SUBCONFIGURATIONS | 7 | 11 | 19 | 6 | 43 |
| ARCHITECTURE_CANDIDATES | 3 | 7 | 9 | 2 | 21 |
| PROPERTY_REGISTER | 24 | 19 | 14 | 15 | 72 |
| CLOSURE_REGISTER | 14 | 7 | 7 | 6 | 34 |
| PROVENANCE_LINKS | 3036 | 2855 | 4793 | 746 | 11430 |
| UNCERTAINTY_LOG | 49 | 44 | 52 | 36 | 181 |
| HUMAN_REVIEW_QUEUE | 19 | 16 | 35 | 19 | 89 |
| TRACE_DEMONSTRATIONS | 2 | 2 | 2 | 2 | 8 |
| INSTRUMENT_LEVEL_SUMMARY | 1 | 1 | 1 | 1 | 4 |
| PROTOCOL_DEVIATION_LOG | 12 | 12 | 12 | 15 | 51 |
| RUN_METADATA | 1 | 1 | 1 | 1 | 4 |


Rows are data rows (header excluded). The `record_counts` text written inside each case's own INSTRUMENT_LEVEL_SUMMARY lists a different subset of tables per case (for example C2_CBAM's omits PROVENANCE_LINKS, TRACE_DEMONSTRATIONS and PROTOCOL_DEVIATION_LOG); every number it does list equals the recomputed row count.

### 2.2 Source-unit structure and screening

| Structure class (SOURCE_UNIT_INVENTORY) | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| OPERATIVE_ARTICLE | 208 | 329 | 1068 | 67 | 1672 |
| ANNEX | 358 | 105 | 231 | 0 | 694 |
| RECITAL | 47 | 82 | 180 | 14 | 323 |
| HEADING_ONLY | 40 | 28 | 61 | 1 | 130 |
| FORMAL_OTHER | 53 | 14 | 13 | 11 | 91 |


| governance_relevance (UNIT_SCREENING) | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| Yes | 526 | 433 | 1251 | 61 | 2271 |
| No | 180 | 125 | 302 | 32 | 639 |


In every case units screened = units inventoried (706, 558, 1553, 93).

## 3. Records by type (as coded by each case)

| POSITIONS_AND_DEVICES `kind` / `type_or_instance` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| POSITION / TYPE | 18 | 19 | 56 | 7 | 100 |
| POSITION / INSTANCE | 8 | 6 | 13 | 4 | 31 |
| DEVICE / TYPE | 0 | 2 | 2 | 0 | 4 |
| DEVICE / INSTANCE | 2 | 0 | 0 | 1 | 3 |


| NORMATIVE_ASSIGNMENTS `norm_type` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| N0 | 38 | 43 | 193 | 13 | 287 |
| N1 | 0 | 0 | 0 | 0 | 0 |
| N2 | 5 | 2 | 11 | 0 | 18 |
| N3 | 16 | 18 | 29 | 6 | 69 |
| N4 | 1 | 0 | 13 | 0 | 14 |
| COMPOUND | 2 | 0 | 5 | 1 | 8 |
| AMBIGUOUS | 1 | 2 | 0 | 0 | 3 |


| NORMATIVE_ASSIGNMENTS `modality` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| obligation | 39 | 40 | 175 | 13 | 267 |
| permission | 18 | 6 | 24 | 6 | 54 |
| competence | 0 | 12 | 24 | 0 | 36 |
| prohibition | 4 | 4 | 21 | 1 | 30 |
| declaratory | 0 | 3 | 2 | 0 | 5 |
| obligation_promotional | 1 | 0 | 4 | 0 | 5 |
| entitlement | 1 | 0 | 1 | 0 | 2 |


| QUALIFIED_RELATIONS `relation_type` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| information_reporting | 15 | 48 | 136 | 11 | 210 |
| oversight_supervision | 5 | 8 | 46 | 0 | 59 |
| representation_participation | 6 | 4 | 36 | 13 | 59 |
| delegation_authorization | 7 | 13 | 23 | 5 | 48 |
| authority_control | 6 | 17 | 6 | 1 | 30 |
| review_adjudication | 8 | 0 | 14 | 3 | 25 |
| verification_assurance | 2 | 6 | 9 | 3 | 20 |
| contractual_exchange | 7 | 4 | 4 | 2 | 17 |
| accountability | 2 | 0 | 4 | 1 | 7 |
| beneficiary_protective | 2 | 1 | 3 | 0 | 6 |


| QUALIFIED_RELATIONS `modality` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| obligation | 49 | 81 | 214 | 31 | 375 |
| permission | 4 | 14 | 27 | 4 | 49 |
| competence | 5 | 5 | 21 | 2 | 33 |
| entitlement | 1 | 1 | 10 | 0 | 12 |
| declaratory | 0 | 0 | 6 | 0 | 6 |
| obligation_promotional | 1 | 0 | 3 | 0 | 4 |
| definition | 0 | 0 | 0 | 2 | 2 |


| QUALIFIED_RELATIONS `accountability_class` / `accountability_sufficiency` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| ACCOUNTABILITY / indeterminate | 0 | 0 | 2 | 1 | 3 |
| ACCOUNTABILITY / sufficient | 1 | 0 | 0 | 0 | 1 |
| ANSWERABILITY / indeterminate | 1 | 0 | 13 | 0 | 14 |
| INFO / NA | 12 | 0 | 99 | 11 | 122 |
| INFO / indeterminate | 0 | 6 | 0 | 0 | 6 |
| INFO / sufficient | 0 | 49 | 0 | 0 | 49 |
| NONE / NA | 46 | 46 | 167 | 27 | 286 |


| Derivation (NA + QR) | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| direct | 97 | 146 | 437 | 47 | 727 |
| derived | 26 | 20 | 95 | 12 | 153 |


| Function field use (NA + QR) | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| flagged residual tags (`*`) | 24 | 26 | 103 | 8 | 161 |
| `FUNCTION_VOCABULARY_UNRESOLVED` | 5 | 0 | 27 | 3 | 35 |
| other documented FUNCTION values | 94 | 140 | 402 | 48 | 684 |


| Function field: `FUNCTION_VOCABULARY_UNRESOLVED` by table | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| NORMATIVE_ASSIGNMENTS | 5 | 0 | 27 | 1 | 33 |
| QUALIFIED_RELATIONS | 0 | 0 | 0 | 2 | 2 |


## 4. Architecture candidates: outcomes, I1-I4 statuses, instrument-level result, stopping level

### 4.1 Candidate outcome categories (ARCHITECTURE_CANDIDATES.outcome)

| Outcome | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| INTEGRATED | 1 | 2 | 5 | 0 | 8 |
| DISTINGUISHABLE | 0 | 0 | 0 | 0 | 0 |
| OVERLAPPING_OR_PARTIALLY_INTEGRATED | 1 | 1 | 1 | 0 | 3 |
| INDETERMINATE | 1 | 4 | 3 | 2 | 10 |
| **candidates total** | 3 | 7 | 9 | 2 | 21 |


Per-candidate listing as recorded (member subconfigurations; I1, I2, I3, I4 statuses; outcome):

- **C1_SCF**: ARCH-01 [SC-01,SC-02,SC-03,SC-04,SC-07] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=SATISFIED -> INTEGRATED; ARCH-02 [SC-05] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=SATISFIED -> OVERLAPPING_OR_PARTIALLY_INTEGRATED; ARCH-03 [SC-06] I1=SATISFIED, I2=SATISFIED, I3=INDETERMINATE, I4=INDETERMINATE -> INDETERMINATE.
- **C2_CBAM**: ARCH-01 [SC-01,SC-04,SC-05] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=SATISFIED -> INTEGRATED; ARCH-02 [SC-02,SC-03,SC-05] I1=SATISFIED, I2=SATISFIED, I3=INDETERMINATE, I4=INDETERMINATE -> INDETERMINATE; ARCH-03 [SC-07] I1=SATISFIED, I2=SATISFIED, I3=INDETERMINATE, I4=INDETERMINATE -> INDETERMINATE; ARCH-04 [SC-08] I1=SATISFIED, I2=SATISFIED, I3=INDETERMINATE, I4=INDETERMINATE -> INDETERMINATE; ARCH-05 [SC-09] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=SATISFIED -> INTEGRATED; ARCH-06 [SC-10] I1=SATISFIED, I2=SATISFIED, I3=INDETERMINATE, I4=SATISFIED -> INDETERMINATE; ARCH-07 [SC-01,SC-02,SC-03,SC-04,SC-05,SC-06,SC-07,SC-08,SC-09,SC-10,SC-11] I1=SATISFIED, I2=INDETERMINATE, I3=INDETERMINATE, I4=INDETERMINATE -> OVERLAPPING_OR_PARTIALLY_INTEGRATED.
- **AI_AI_ACT**: ARCH-01 [SC-06,SC-07,SC-16] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=SATISFIED -> INTEGRATED; ARCH-02 [SC-01,SC-02,SC-03,SC-18] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=SATISFIED -> INTEGRATED; ARCH-03 [SC-04,SC-05,SC-12,SC-17] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=SATISFIED -> INTEGRATED; ARCH-04 [SC-09] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=SATISFIED -> INTEGRATED; ARCH-05 [SC-09,SC-10] I1=SATISFIED, I2=INDETERMINATE, I3=NOT_SATISFIED, I4=INDETERMINATE -> INDETERMINATE; ARCH-06 [SC-19] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=SATISFIED -> INTEGRATED; ARCH-07 [SC-08] I1=SATISFIED, I2=SATISFIED, I3=INDETERMINATE, I4=INDETERMINATE -> INDETERMINATE; ARCH-08 [SC-14] I1=SATISFIED, I2=INDETERMINATE, I3=INDETERMINATE, I4=INDETERMINATE -> INDETERMINATE; ARCH-09 [SC-06,SC-07,SC-01,SC-02,SC-03,SC-18,SC-04,SC-05,SC-12,SC-16,SC-11,SC-08,SC-19,SC-13,SC-09,SC-17] I1=SATISFIED, I2=SATISFIED, I3=NOT_SATISFIED, I4=SATISFIED -> OVERLAPPING_OR_PARTIALLY_INTEGRATED.
- **O_DIR_86_361**: ARCH-01 [SC-01,SC-02,SC-03,SC-05] I1=SATISFIED, I2=SATISFIED, I3=SATISFIED, I4=INDETERMINATE -> INDETERMINATE; ARCH-02 [SC-01,SC-02,SC-03,SC-04,SC-05,SC-06] I1=SATISFIED, I2=INDETERMINATE, I3=INDETERMINATE, I4=INDETERMINATE -> INDETERMINATE.

| I1 status | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| SATISFIED | 3 | 7 | 9 | 2 | 21 |
| NOT_SATISFIED | 0 | 0 | 0 | 0 | 0 |
| INDETERMINATE | 0 | 0 | 0 | 0 | 0 |


| I2 status | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| SATISFIED | 3 | 6 | 7 | 1 | 17 |
| NOT_SATISFIED | 0 | 0 | 0 | 0 | 0 |
| INDETERMINATE | 0 | 1 | 2 | 1 | 4 |


| I3 status | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| SATISFIED | 2 | 2 | 5 | 1 | 10 |
| NOT_SATISFIED | 0 | 0 | 2 | 0 | 2 |
| INDETERMINATE | 1 | 5 | 2 | 1 | 9 |


| I4 status | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| SATISFIED | 2 | 3 | 6 | 0 | 11 |
| NOT_SATISFIED | 0 | 0 | 0 | 0 | 0 |
| INDETERMINATE | 1 | 4 | 3 | 2 | 10 |


### 4.2 Instrument-level result and highest level reached (as recorded in INSTRUMENT_LEVEL_SUMMARY)

| Case | instrument_level_result | highest_level_reached (stopping level) |
|---|---|---|
| C1_SCF | OVERLAPPING_OR_PARTIALLY_INTEGRATED | A |
| C2_CBAM | OVERLAPPING_OR_PARTIALLY_INTEGRATED | A |
| AI_AI_ACT | OVERLAPPING_OR_PARTIALLY_INTEGRATED | A |
| O_DIR_86_361 | INDETERMINATE | S |

Result tokens used across the four cases: INDETERMINATE, OVERLAPPING_OR_PARTIALLY_INTEGRATED. Tokens available in the dictionary but not recorded by any case: NO_ARCHITECTURE_WARRANTED, ONE_ARCHITECTURE, SEVERAL_DISTINGUISHABLE. Per the frozen dictionary the instrument-level entry is a profile of candidate outcomes, not a single label or score. Case-recorded stopping rationale: C1_SCF, C2_CBAM and AI_AI_ACT record level A as the highest level reached while recording INDETERMINATE candidates (and, in AI_AI_ACT, NOT_SATISFIED I3 for two candidates); O_DIR_86_361 records level S, with both candidates INDETERMINATE (its DEV-11 and HQ-016 record the reading of RGAM-DR-25 that produced this).

### 4.3 Subconfigurations, couplings, properties and closure

| Subconfigurations (SC) recorded | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| rows | 7 | 11 | 19 | 6 | 43 |


| I2 coupling kind (ARCHITECTURE_CANDIDATES.i2_coupling_kind, as written; some cases record several kinds in one cell) | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| qualified_procedural_dependency | 2 | 5 | 5 | 0 | 12 |
| conditional_dependency | 0 | 1 | 1 | 0 | 2 |
| mandatory_interface | 0 | 0 | 2 | 0 | 2 |
| NONE | 0 | 0 | 1 | 0 | 1 |
| coordination_or_communication | 1 | 0 | 0 | 0 | 1 |
| integration_through_distributed_powers | 0 | 1 | 0 | 0 | 1 |
| qualified_procedural_dependency; conditional_dependency | 0 | 0 | 0 | 1 | 1 |
| shared_participation; mandatory_interface; conditional_dependency | 0 | 0 | 0 | 1 | 1 |


| PROPERTY_REGISTER `status` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| asserted | 18 | 15 | 8 | 9 | 50 |
| undetermined | 4 | 4 | 5 | 5 | 18 |
| not_attributable | 2 | 0 | 1 | 1 | 4 |


| PROPERTY_REGISTER `bearer_type` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| SUBCONFIGURATION | 14 | 12 | 8 | 11 | 45 |
| ARCHITECTURE | 6 | 5 | 5 | 2 | 18 |
| RELATION | 4 | 1 | 0 | 2 | 7 |
| POSITION | 0 | 1 | 1 | 0 | 2 |


| PROPERTY_REGISTER `property_family` (blank = not assigned) | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| (blank) | 3 | 0 | 14 | 15 | 32 |
| F5 | 6 | 6 | 0 | 0 | 12 |
| F1 | 5 | 6 | 0 | 0 | 11 |
| F3 | 4 | 3 | 0 | 0 | 7 |
| F4 | 4 | 2 | 0 | 0 | 6 |
| F2 | 2 | 2 | 0 | 0 | 4 |


| CLOSURE_REGISTER `record_kind` / `result` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| COVERAGE / ASSERTED_WITHIN_DECLARED_CORPUS | 1 | 2 | 2 | 2 | 7 |
| COVERAGE / UNDETERMINED | 1 | 0 | 0 | 0 | 1 |
| ABSENCE_CLAIM / ASSERTED_WITHIN_DECLARED_CORPUS | 9 | 2 | 3 | 2 | 16 |
| ABSENCE_CLAIM / UNDETERMINED | 3 | 3 | 2 | 2 | 10 |


TRACE_DEMONSTRATIONS: each case recorded two rows (one SEEDED_DRAW, one LARGEST_SUPPORT), `chain_complete = Y` in all eight rows. Traced ids: C1_SCF SEEDED_DRAW->SC-05, LARGEST_SUPPORT->ARCH-01; C2_CBAM SEEDED_DRAW->SC-05, LARGEST_SUPPORT->ARCH-07; AI_AI_ACT SEEDED_DRAW->SC-12, LARGEST_SUPPORT->ARCH-09; O_DIR_86_361 SEEDED_DRAW->SC-05, LARGEST_SUPPORT->ARCH-02.

## 5. Status profiles

### 5.1 Recomputed from the tables

| Epistemic status | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| QR - legal_constitution_evidenced | 36 | 83 | 263 | 35 | 417 |
| QR - documented | 24 | 18 | 18 | 4 | 64 |
| QR - material_establishment_evidenced | 0 | 0 | 0 | 0 | 0 |
| QR - exercise_evidenced | 0 | 0 | 0 | 0 | 0 |
| NA - legal_constitution_evidenced | 45 | 52 | 242 | 16 | 355 |
| NA - documented | 18 | 13 | 9 | 4 | 44 |
| NA - material_establishment_evidenced | 0 | 0 | 0 | 0 | 0 |
| NA - exercise_evidenced | 0 | 0 | 0 | 0 | 0 |
| PD - legal_constitution_evidenced | 1 | 0 | 1 | 0 | 2 |
| PD - documented | 27 | 27 | 70 | 12 | 136 |
| PD - material_establishment_evidenced | 0 | 0 | 0 | 0 | 0 |
| PD - exercise_evidenced | 0 | 0 | 0 | 0 | 0 |


| Legal status of norm (QR + NA) | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| in_force | 122 | 166 | 517 | 59 | 864 |
| not_yet_applicable | 0 | 0 | 0 | 0 | 0 |
| suspended | 0 | 0 | 0 | 0 | 0 |
| expired_or_repealed | 0 | 0 | 0 | 0 | 0 |
| conditional_on_further_act | 1 | 0 | 15 | 0 | 16 |


The temporal reference declared in each W_DECLARATION differs by case (C1_SCF: reference date 30 June 2024 with the 2026-2032 Fund interval; C2_CBAM: point reference 2026-01-01; AI_AI_ACT: reference point 2 August 2026; O_DIR_86_361: the interval from adoption on 1986-07-24 to the repeal indicated in the neutral metadata).

### 5.2 As recorded by each case (INSTRUMENT_LEVEL_SUMMARY.status_profile, verbatim)

- **C1_SCF**: 60 relations: 36 legal_constitution_evidenced; 24 documented | 63 assignments: 45 legal_constitution_evidenced; 18 documented | 28 positions/devices: 1 legal_constitution_evidenced; 27 documented | 46 external references: not_checked; 0 material_establishment_evidenced; 0 exercise_evidenced
- **C2_CBAM**: QUALIFIED_RELATIONS: 83 legal_constitution_evidenced; 18 documented; 0 material_establishment_evidenced (never carried by relations); 0 exercise_evidenced. NORMATIVE_ASSIGNMENTS: 52 legal_constitution_evidenced; 13 documented; 0 material_establishment_evidenced; 0 exercise_evidenced. POSITIONS_AND_DEVICES: 0 legal_constitution_evidenced; 27 documented; material establishment not_assessed for all; 0 exercise_evidenced. Legal status of norm at the 2026-01-01 reference: in_force for all coded norms; no not_yet_applicable, suspended, expired_or_repealed or conditional_on_further_act status asserted.
- **AI_AI_ACT**: Relations: 263 legal_constitution_evidenced, 18 documented, 0 material_establishment_evidenced (not permitted for relations), 0 exercise_evidenced; legal status 266 in_force, 15 conditional_on_further_act. Assignments: 242 legal_constitution_evidenced, 9 documented, 0 exercise_evidenced; legal status 251 in_force, 0 not_yet_applicable/conditional. Positions and devices: 70 documented, 1 legal_constitution_evidenced (Board, N1); material_establishment not_assessed for all. Architecture candidates: 5 INTEGRATED (provisional), 1 OVERLAPPING_OR_PARTIALLY_INTEGRATED, 3 INDETERMINATE, 0 DISTINGUISHABLE; instrument-level profile OVERLAPPING_OR_PARTIALLY_INTEGRATED
- **O_DIR_86_361**: Positions/devices: 12 documented (0 material_establishment_evidenced: not assessed). 4 relations documented; 35 relations legal_constitution_evidenced; 4 assignments documented; 16 assignments legal_constitution_evidenced; 0 material_establishment_evidenced (not assessed); 0 exercise_evidenced (not assessed); external references: 10 not_checked.

## 6. External references and unresolved constitutive dependencies

| EXTERNAL_REFERENCES rows | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| rows | 46 | 33 | 59 | 10 | 148 |


| `constitutive_dependency` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| Y | 13 | 17 | 39 | 4 | 73 |
| N | 33 | 16 | 20 | 6 | 75 |


| `source_kind` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| legal_instrument | 41 | 27 | 50 | 5 | 123 |
| other_normative | 3 | 5 | 7 | 2 | 17 |
| administrative_act | 1 | 1 | 1 | 1 | 4 |
| technical_standard | 1 | 0 | 1 | 2 | 4 |


| `reference_role` (first token) | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| constitutes_device | 0 | 0 | 1 | 0 | 1 |
| constitutes_position | 1 | 2 | 2 | 0 | 5 |
| defines_term | 10 | 10 | 6 | 2 | 28 |
| designates_competence | 1 | 0 | 0 | 0 | 1 |
| other | 10 | 3 | 29 | 4 | 46 |
| supplies_rule_or_standard | 24 | 18 | 21 | 4 | 67 |


All EXTERNAL_REFERENCES rows in all four cases carry `source_verification_status = not_checked` and `boundary_status = outside_corpus_not_expanded`. `unresolved_ext_count` recorded in each INSTRUMENT_LEVEL_SUMMARY equals the recomputed number of rows with `constitutive_dependency = Y` (13, 17, 39, 4; total 73).

## 7. Uncertainty log: types and distribution

| `uncertainty_type` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| SOURCE_AMBIGUITY | 13 | 8 | 30 | 16 | 67 |
| EXTERNAL_DEPENDENCY | 9 | 6 | 7 | 5 | 27 |
| DIRECTION | 10 | 6 | 5 | 3 | 24 |
| OTHER | 3 | 13 | 0 | 6 | 22 |
| PROTOCOL_GAP | 3 | 2 | 2 | 4 | 11 |
| ACCOUNTABILITY_SUFFICIENCY | 2 | 1 | 6 | 1 | 10 |
| DRAFTING_CUE | 5 | 5 | 0 | 0 | 10 |
| DEV_THRESHOLD | 2 | 2 | 2 | 1 | 7 |
| COUPLING_THRESHOLD | 1 | 1 | 0 | 0 | 2 |
| CLOSURE | 1 | 0 | 0 | 0 | 1 |


| `status` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| OPEN | 14 | 29 | 28 | 16 | 87 |
| ESCALATED_TO_HQ | 35 | 15 | 24 | 20 | 94 |


Uncertainty types in the frozen dictionary vocabulary that appear in no case: none. Types absent in individual cases can be read from the table above (zero cells).

## 8. Human-review queue: volume, trigger distribution, recurring categories

| HUMAN_REVIEW_QUEUE items | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| rows | 19 | 16 | 35 | 19 | 89 |


| `trigger_code` | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| HQ-NORMTYPE | 1 | 2 | 7 | 2 | 12 |
| HQ-DEV | 2 | 0 | 1 | 1 | 4 |
| HQ-ACCOUNT | 1 | 1 | 5 | 1 | 8 |
| HQ-INTEGRATION | 1 | 2 | 5 | 0 | 8 |
| HQ-OVERLAP | 1 | 1 | 1 | 0 | 3 |
| HQ-XREF | 1 | 1 | 1 | 4 | 7 |
| HQ-DIRECTION | 1 | 1 | 2 | 2 | 6 |
| HQ-GAP | 3 | 1 | 10 | 5 | 19 |
| HQ-EXTDEP | 7 | 6 | 2 | 1 | 16 |
| HQ-OTHER | 1 | 1 | 1 | 3 | 6 |


| `recurring_category_label` (descriptive label assigned by the family assembler to items asking the same type of question; not a merge) | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 | Total |
|---|---:|---:|---:|---:|---:|
| EXTERNAL_DEPENDENCY_CLAIM_SCOPE | 7 | 6 | 2 | 1 | 16 |
| NORM_TYPE_CLASSIFICATION | 1 | 2 | 7 | 2 | 12 |
| EXECUTION_ADDENDUM_USE_CONFIRMATION | 1 | 0 | 6 | 2 | 9 |
| ACCOUNTABILITY_CLASS_QUESTION | 1 | 1 | 5 | 1 | 8 |
| ARCHITECTURE_INTEGRATION_WARRANT_QUESTION | 1 | 2 | 5 | 0 | 8 |
| COUNTERPARTY_OR_DIRECTION_NOT_STATED | 1 | 1 | 3 | 3 | 8 |
| CROSS_REFERENCE_SCOPE_RESOLUTION | 1 | 1 | 0 | 3 | 5 |
| DEVICE_THRESHOLD_CLASSIFICATION | 2 | 0 | 1 | 1 | 4 |
| ARCHITECTURE_OVERLAP_OR_SEPARATION_QUESTION | 1 | 1 | 1 | 0 | 3 |
| FUNCTION_VOCABULARY_FIT | 1 | 0 | 1 | 1 | 3 |
| PROPERTY_FAMILY_MAPPING_ABSENT | 1 | 0 | 1 | 1 | 3 |
| RELATION_TYPE_NEAREST_FIT | 1 | 0 | 0 | 1 | 2 |
| TEMPORAL_REFERENCE_AND_STATUS_CEILING_CHOICE | 0 | 1 | 0 | 1 | 2 |
| ADDRESSEE_SCOPE_OF_INSTRUMENT_QUESTION | 0 | 0 | 0 | 1 | 1 |
| BEARER_ATTRIBUTION_QUESTION | 0 | 0 | 1 | 0 | 1 |
| DEVICE_AS_RELATION_PARTY_QUESTION | 0 | 0 | 1 | 0 | 1 |
| MULTIPLE_PROTOCOL_GAP_CONFIRMATION | 0 | 1 | 0 | 0 | 1 |
| PROTOCOL_RULE_READING_QUESTION | 0 | 0 | 0 | 1 | 1 |
| UNIT_IDENTIFIER_CONVENTION_CONFIRMATION | 0 | 0 | 1 | 0 | 1 |


Open HQ count recorded in each INSTRUMENT_LEVEL_SUMMARY equals the number of queue rows (19, 16, 35, 19). No item has been adjudicated; `human_decision`, `human_rationale`, `decided_by` and `decision_date` are blank in every row of the case queues and of the combined family queue. The combined queue preserves every case-level item separately (see `RGAM_FAMILY_HUMAN_REVIEW_QUEUE.csv`).

## 9. Recurring methodological issues and deviation patterns (as recorded in each PROTOCOL_DEVIATION_LOG)

### 9.1 Execution-addendum gaps GAP-01 to GAP-07 (rows of PROTOCOL_DEVIATION_LOG with `gap_ref`)

| Gap | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 |
|---|:---|:---|:---|:---|
| GAP-01 | DEV-01, DEV-11 | DEV-02, DEV-03 | DEV-01 | DEV-01, DEV-03 |
| GAP-02 | DEV-02 | DEV-04 | DEV-02 | - |
| GAP-03 | DEV-03 | DEV-05 | DEV-03 | DEV-05 |
| GAP-04 | DEV-04 | DEV-06 | DEV-04 | DEV-06 |
| GAP-05 | DEV-05 | DEV-07 | DEV-05 | DEV-07 |
| GAP-06 | DEV-06 | DEV-08 | DEV-06 | DEV-08 |
| GAP-07 | DEV-07 | DEV-09 | DEV-07 | DEV-09 |


Deviation-log rows per case: C1_SCF = 12 (of which with `gap_ref`: 8); C2_CBAM = 12 (of which with `gap_ref`: 8); AI_AI_ACT = 12 (of which with `gap_ref`: 7); O_DIR_86_361 = 15 (of which with `gap_ref`: 7). GAP-02 (provisions amending other acts): used in C1_SCF (Article 28) and AI_AI_ACT (Articles 102 to 110); C2_CBAM logged that it examined GAP-02 and did not use it (DEV-04); O_DIR_86_361 has no GAP-02 row and its QA report states that GAP-02 did not arise. GAP-06 (the "six questions") is recorded as `NON_OPERATIVE_SOURCE_GAP` in all four cases. GAP-05: `FUNCTION_VOCABULARY_UNRESOLVED` appears in the function field of C1_SCF, AI_AI_ACT and O_DIR_86_361 and not in C2_CBAM (its DEV-07 records that it was not needed); counts in section 3.

### 9.2 Other patterns recorded in the deviation logs (case and DEV id)

| Pattern | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 |
|---|---|---|---|---|
| Mapping of the ten dimensions to property families F1-F5 not stated in the allow-listed sources (RGAM-DR-24) | DEV-08 (provisional assignment by listing order; positional examples left blank) | DEV-10 (provisional assignment by listing order) | DEV-10 (left blank for all properties) | DEV-10 (left blank for all properties) |
| Unit-identifier conventions beyond those in the dictionary (RGAM-DR-05) | DEV-10 | DEV-02 (with GAP-01) | DEV-08 | DEV-01 (with GAP-01), DEV-02 |
| Operationalisation of the status ceiling / down-coding of records with constitutive external dependencies (RGAM-DR-18 to DR-20) | DEV-12 | DEV-11 | DEV-04 (kept at documented level); QA section 3 (down-coding rule) | DEV-12 |
| Choice of temporal reference by the executor | stated in W_DECLARATION; not logged as a deviation | DEV-01 (HQ-OTHER) | stated in W_DECLARATION; not logged as a deviation | DEV-12 (with status ceiling); HQ-015 |
| Content not representable in the source file (images, table geometry, footnote apparatus, page chrome) | DEV-11 (Annex I formula images) | DEV-03 (Annex IV formula images; Annex I-II table geometry) | DEV-08 (footnote apparatus declared as exclusion) | W_DECLARATION exclusions (page chrome, separator, heading lines); DEV-02 (headings, separator, merged-point splitting) |
| Reading depth limits recorded | DEV-11 (3 of 6 image-only units viewed) | none logged | DEV-11 (recitals REC34-REC180 screened from opening text and length) | none logged |
| Relation-admission or party questions not covered by the dictionary | DEV-07 (definitions yield positions only where they bear a record) | DEV-12 (NA and PD members in subconfigurations) | DEV-09 (devices used as relation counterparts); DEV-12 (accountability class independent of relation type) | DEV-04 (citations not coded as EXT); DEV-09 (definition-derived relations) |
| Reading of an ambiguous protocol rule | none logged | none logged | none logged | DEV-11 (RGAM-DR-25 applied to every candidate touched by a constitutive external reference); DEV-13 (trace-selection generator and meaning of "part") |
| Recovery after an interrupted executor | none | none | recovery executor started fresh; earlier executor interrupted before producing records (per case log and orchestrator audit) | DEV-14 (recovery run reusing the earlier executor's tables, with listed corrections) |

Property-family field: blank in C1_SCF 3 of 24; C2_CBAM 0 of 19; AI_AI_ACT 14 of 14; O_DIR_86_361 15 of 15 PROPERTY_REGISTER rows.

### 9.3 Cross-reference derivation and function-vocabulary points

Internal cross-references were followed under GAP-03 in all four cases; derived NA+QR records are counted in section 3. Function-vocabulary questions (GAP-05) are queued as HQ-GAP items in all four cases (as separate items in C1_SCF HQ-010, AI_AI_ACT HQ-030 and O_DIR_86_361 HQ-013; inside the bundled item HQ-016 in C2_CBAM). Property-family mapping, accountability-class readings, norm-type readings, device-threshold readings and external-dependency scope recur as queue categories in more than one case (section 8).

### 9.4 Small internal inconsistencies noticed while reading the frozen case files (reported, not corrected)

- O_DIR_86_361: `EXECUTION_PROVENANCE.md` section 5 says the trace-generator choice is "logged DEV-14", while PROTOCOL_DEVIATION_LOG records it as DEV-13 (DEV-14 is the recovery-run entry); `CASE_QA_REPORT.md` section D (C5) and `CASE_GATE.md` cite DEV-14/DEV-15 for the recovery corrections in a way that differs from the log's row numbering (DEV-14 recovery run; DEV-15 evidence-span convention). The frozen files were not changed.
- RUN_METADATA.model_parameters: C1_SCF, C2_CBAM and the O_DIR_86_361 recovery run record `reasoning_effort=10` as displayed in the invocation context; AI_AI_ACT records reasoning effort as NOT_EXPOSED. The orchestrator audit states that the Agent tool exposes no reasoning-effort parameter.
- INSTRUMENT_LEVEL_SUMMARY.record_counts lists different table subsets per case (section 2.1).

## 10. Run and provenance facts as recorded

| Case | Model id (RUN_METADATA) | Parameters as recorded | Start / end (as recorded) | Executor (orchestrator audit) | Earlier interrupted executor (orchestrator audit) |
|---|---|---|---|---|---|
| C1_SCF | claude-sonnet-5-5 (as stated in the invocation context: Sonnet 5.5) | reasoning_effort=10 (value displayed in the invocation context; the brief requested the highest available effort and the displayed setting could not be changed by the executor); temperature NOT_EXPOSED; top-p NOT_EXPOSED; seed NOT... | 2026-10-06T15:19:41-03:00 / 2026-10-06T15:59:29-03:00 | a773412851ad46032 | NONE |
| C2_CBAM | claude-sonnet-5-5 (Sonnet 5.5, as stated in the session context) | reasoning_effort=10 (value displayed in the session context; the brief requested the highest available effort, which was not user-settable here); temperature, top-p, seed, token limits: NOT_EXPOSED | 2026-10-06T19:03:42Z / 2026-10-06T19:43:24Z | aee1506e1d0e70177 | NONE |
| AI_AI_ACT | claude-sonnet-5-5 (Sonnet 5.5, as stated in the session environment) | reasoning effort: NOT_EXPOSED; temperature: NOT_EXPOSED; top-p: NOT_EXPOSED; seed: NOT_EXPOSED; token limits: NOT_EXPOSED | 2026-10-06T19:44:21 (local) / 2026-10-06T20:42:41 (local; end of record production, report writing and freeze steps follow) | ad615b1d8063b1df2 (fresh recovery run) | ad1c4f939eaef025b (interrupted at 12 calls; blank templates only; not reused) |
| O_DIR_86_361 | claude-sonnet-5-5 (Sonnet 5.5, as stated in the session environment) | RECOVERY RUN reusing the partial work of an earlier executor that was interrupted by an API rate limit (earlier run: start 2026-10-06T20:47:08-03:00 as recorded by that executor, last file write 2026-10-06T21:11:05-03:00; this row... | 2026-10-07T07:37:48-03:00 / 2026-10-07T07:45:05-03:00 | a04521a3bcdf0d1d0 (fresh recovery run) | a86c431b77ac102f0 (interrupted; analytical tables produced; later adopted as partial state) |

All four RUN_METADATA rows record `protocol_version = RGAM paired execution protocol v1.0`, the protocol manifest SHA-256 `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932`, `fresh_context_attested = Y`, `forbidden_paths_attempted = NONE` and `machine_generated = Y`.

## 11. Limits of this summary

Single-pass machine execution by one model family for all four cases; case executors checked their own outputs; none of the numbers here measure correctness, completeness of legal interpretation or architectural properties of the legal instruments. Instrument sizes differ widely (93 to 1553 units), so raw counts are not mutually normalised and no normalisation is offered. No human adjudication has taken place; all records are machine-generated and provisional. This file contains no comparison with V8 or any other method, no improvement, agreement or performance measure, and no inference about any other arm of the experiment.
