# R4 — R3 Baseline Manifest

**Round:** R4 cross-domain validation  
**Baseline status:** FROZEN FOR INITIAL R4 SETUP  
**Baseline date:** 2026-09-25  
**R3 freeze date reported by the R3 technical note:** 2026-09-21  
**Repository:** `C:\PROJETOS\GITHUB\git-PRJ-REGULATORY-INTERMEDIARIES--Prf-David`  
**Repository commit inspected:** `27ba3e4` — `feat: initial import of the R-I-T EUR-Lex dataset project`  

## Authority decision

The authoritative R3 package is the five-case Regulatory Intermediation Architecture dataset frozen on 2026-09-21, represented by the workbook and technical note listed below, read together with the explicit researcher decision `R3-D08-IMPLEMENTATION`. The workbook is the available human-facing package and contains the R3 overview, linked analytical sheets, codebook, evidence, decision provenance, research-question map, hypotheses and data dictionary.

The workbook itself states that normalized linked R3 tables remain the analytical source of truth. Separate normalized table files, phase manifests and validation scripts were not located in the inspected Downloads location, the target Git repository, or the legacy project mirror. This is recorded as an unresolved provenance limitation; no substitute R1/R2 artifact is promoted to R3 authority.

The duplicate workbook `REGULATORY_INTERMEDIATION_ARCHITECTURE_CASE_STUDY_DATASET - Copia.xlsx` is byte-identical to the selected authoritative workbook (same SHA-256). It is not copied as a second authority.

## Authoritative R3 artifacts

| Artifact | Original path | Function | Version / state | Authority | Role in R4 | SHA-256 |
|---|---|---|---|---|---|---|
| `REGULATORY_INTERMEDIATION_ARCHITECTURE_CASE_STUDY_DATASET.xlsx` | `C:\Users\Adm\Downloads\REGULATORY_INTERMEDIATION_ARCHITECTURE_CASE_STUDY_DATASET.xlsx` | Human-facing R3 dataset package; contains linked analytical sheets, codebook and data dictionary | R3 freeze, 2026-09-21 | **Authoritative analytical package available** | Frozen reference for R4 schema, units, variables and inherited decisions | `FE3DE0A18BD39391D9E9DAE8C48CB31EEBCA1735C6B14CBAA7880193968BAEFA` |
| `R3_TECHNICAL_NOTE_REGULATORY_INTERMEDIATION_ARCHITECTURE.docx` | `C:\Users\Adm\Downloads\R3_TECHNICAL_NOTE_REGULATORY_INTERMEDIATION_ARCHITECTURE.docx` | Final R3 methodological note, phase ledger, frozen counts, limitations and provenance description | R3 freeze, 2026-09-21 | **Authoritative methodological account** | Governs interpretation of the package and its limits | `3D85E79F80DD420262713C7A851FE6CCA7B27DCA249E3ABD2BB243F5CA2B43B7` |
| `R3_RESEARCHER_DECISION_IMPLEMENTATION_AND_DATASET_DIRECTION.md` | `C:\Users\Adm\Downloads\R3_RESEARCHER_DECISION_IMPLEMENTATION_AND_DATASET_DIRECTION.md` | Explicit human decision `R3-D08-IMPLEMENTATION` and dataset-direction decisions | `ADOPTED_PROVISIONALLY_FOR_R3` | **Authoritative human decision record** | Freezes the inherited provisional `IMPLEMENTATION` mechanism and linked architecture | `A96E422453F305E21C3EDA7CA0C98EC8B8CADA301411E64BA5CF8289B1E423D6` |

## Governing R3 methodological artifacts

| Artifact | Original path | Function | Status | Role in R4 | SHA-256 |
|---|---|---|---|---|---|
| `R3_CLEANROOM_OPERATIONAL_PROMPT.md` | `C:\Users\Adm\Downloads\R3_CLEANROOM_OPERATIONAL_PROMPT.md` | R3 clean-room design, phases, units, mechanism ontology and stop rules | Historical R3 protocol; not a digital coding input | Defines the inherited architecture and provenance expectations | `337384361B199DF6B0D362D6D2200F6C4A4E15939EE109D7BE227602BEDE96CA` |
| `R3_LEARNING_REGISTER_AND_CLEANROOM_PLAN.md` | `C:\Users\Adm\Downloads\R3_LEARNING_REGISTER_AND_CLEANROOM_PLAN.md` | Consolidated methodological learning and clean-room rationale | Methodological input; not ground truth | Documents the rationale behind frozen definitions | `4F952F3A93CA0B23E4EECC75FB03CE8AFA900674A79AF47B520E9AAD26103543` |
| `R3_CONCEPTUAL_JOURNEY_AND_RIA_LEARNING_REGISTER.md` | `C:\Users\Adm\Downloads\R3_CONCEPTUAL_JOURNEY_AND_RIA_LEARNING_REGISTER.md` | Conceptual development from actors to RIA architecture | Conceptual/provenance record | Context for inherited distinctions; no new R4 categories | `ED5BC35372D67F8D69810FC4009A8B8CAA8891E6397CA11C4210931027B3C936` |

## R4 governing inputs copied into the workspace

| Artifact | Original path | Function | Status | SHA-256 |
|---|---|---|---|---|
| `PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx` | `C:\Users\Adm\Downloads\PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1 (1).docx` | Mandatory human–AI governance protocol for R1–R3 reconstruction and R4 | Governing R4 protocol | `89CE912545063B41EA37532D32E93F800D6AEAE8BA0A4FE7BC0EA860B289163B` |
| `R4_INITIAL_SETUP_PROMPT_VERBATIM.txt` | Codex attachment `c833fc9a-ee97-40b9-82d4-a09cc9731102\Pasted text.txt` | User-supplied R4 initial setup request | Current task instruction | `4C152338D6C24EC44F14707931B8BC05338A3A54DE6D0CC7FCF0168E5C4762D0` |

## R4 working references

The following copies are available for R4 use. They are separate from `R3_ORIGINAL` and are byte-identical to the selected R3 artifacts at setup time.

| Working reference | Source artifact | SHA-256 |
|---|---|---|
| `01_baseline/R4_WORKING_REFERENCE/R3_DATASET_WORKING_REFERENCE.xlsx` | `01_baseline/R3_ORIGINAL/final_package/REGULATORY_INTERMEDIATION_ARCHITECTURE_CASE_STUDY_DATASET.xlsx` | `FE3DE0A18BD39391D9E9DAE8C48CB31EEBCA1735C6B14CBAA7880193968BAEFA` |
| `01_baseline/R4_WORKING_REFERENCE/R3_TECHNICAL_NOTE_WORKING_REFERENCE.docx` | `01_baseline/R3_ORIGINAL/final_package/R3_TECHNICAL_NOTE_REGULATORY_INTERMEDIATION_ARCHITECTURE.docx` | `3D85E79F80DD420262713C7A851FE6CCA7B27DCA249E3ABD2BB243F5CA2B43B7` |

## Non-authoritative but preserved provenance

| Artifact | Original path | Function | Status | SHA-256 |
|---|---|---|---|---|
| `EMAIL_TO_DAVID_R3_DATASET_PROPOSAL.docx` | `C:\Users\Adm\Downloads\EMAIL_TO_DAVID_R3_DATASET_PROPOSAL.docx` | Transmittal describing the R3 package and asking for review | Communication/provenance only; not a codebook or source of truth | `C36E27DEE009440737ADC8CE49BF574E93F6256F98F48288969C96F538A1398D` |
| `REGULATORY_INTERMEDIATION_ARCHITECTURE_CASE_STUDY_DATASET - Copia.xlsx` | `C:\Users\Adm\Downloads\REGULATORY_INTERMEDIATION_ARCHITECTURE_CASE_STUDY_DATASET - Copia.xlsx` | Duplicate of the R3 workbook | Not independently authoritative; byte-identical to selected workbook | `FE3DE0A18BD39391D9E9DAE8C48CB31EEBCA1735C6B14CBAA7880193968BAEFA` |

## Frozen inherited architecture

- Five R3 climate-law instruments; R4 does not reopen their coding.
- Linked analytical levels: `LAW`, `LAW × ACTOR`, `LAW × INTERMEDIARY`, `R–I–T RELATION`, `MECHANISM EVENT`, `MECHANISM CONFIGURATION`, legal evidence and decision provenance.
- Intermediation gate: identifiable R–T relationship, institutionally distinct third actor, and demonstrable mediating function.
- Roles are relational, not permanent actor attributes.
- Mechanism events preserve input, mediated object, transformation, output, recipient and regulatory connection.
- Nine operational mechanisms remain frozen: `TRANSMISSION`, `AGGREGATION`, `REPRESENTATION`, `TRANSLATION`, `INTERPRETATION`, `EVALUATION_ASSESSMENT`, `CLASSIFICATION_RANKING`, `MONITORING`, `VERIFICATION`.
- `IMPLEMENTATION` remains a tenth, researcher-added, provisional and unassigned-family mechanism under `R3-D08-IMPLEMENTATION`.
- Negative relations and the substantive-zero case remain part of the architecture.
- R4 must not silently add, remove, merge or redefine variables, roles, mechanisms, confidence rules or units.

## Frozen R3 totals reported by the technical note and workbook

| Item | Frozen value |
|---|---:|
| Laws | 5 |
| LAW × ACTOR records | 89 |
| Adjudicated relations | 56 |
| `DIRECT_R_T` | 24 |
| `LEGAL_RELATION_NON_RIT` | 23 |
| `SUPPORTED_INTERMEDIATION` | 9 |
| LAW × INTERMEDIARY units | 7 |
| Mechanism events | 10 |
| Configurations | 9 |
| Confirmed mechanism edges | 1 |
| Substantive-zero laws | 1 (`32015D1814`) |

## Repository and provenance state

The target Git repository was inspected at commit `27ba3e4`. Its working tree contained 12 staged additions under `WORK_2_1/PILOT_R2_1/`, including a 2020 Taxonomy Regulation pilot inventory. Those files are R2.1 material, were not treated as R3 authority, and were not modified. The R3 artifacts above were external to that commit and have been copied into `R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_ORIGINAL/` as frozen references.

## Baseline conclusion

R3 is frozen for the initial R4 transportability test. The available authority is sufficient to freeze the inherited ontology and decision architecture, but not to claim that all granular R3 phase files, normalized tables, scripts or historical model runs have been recovered. Those missing provenance items remain visible and must not be reconstructed by invention.

## Historical R3 Reconciliation Update

**Update date:** 2026-09-26

### Original limitation

The initial baseline did not independently locate all normalized R3 tables and granular provenance/decision logs.

### Subsequent evidence

The historical archive `PRJ-DAVID-R3.zip` was later provided and integrated through controlled read-only historical reconciliation under `R4.1B`.

### Materials recovered

The recovered archive preserves the original clean-room structure and includes, where applicable:

- actor register and actor aliases;
- provision mappings;
- LAW × INTERMEDIARY register and relation links;
- relation candidates, adjudicated relations, negative boundary cases and uncertain relations;
- mechanism events, researcher-adjudicated mechanism events, mechanism traces and uncertainty logs;
- researcher decision logs and configuration tables;
- dataset architecture, research-question materials, audits and the David-facing package.

The machine-readable inventory records 127 files, and the reconciliation register records the recovered normalized analytical layers and their totals.

### Resolution

`RESOLVED` for the historical archive supplied as `PRJ-DAVID-R3.zip`: normalized tables and granular decision/provenance materials were recovered and independently reconciled without modifying the historical empirical record. The original limitation remains preserved above as an accurate record of the initial R4 baseline state.
