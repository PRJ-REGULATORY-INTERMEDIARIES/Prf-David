# R3_R4_PROVENANCE_MAP (R04)

Abbreviations: `<R3>` = `R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM/`; `<ENV>` = `ENVIO_R4_TO_DAVID/`.

## 1. R3_CLEANROOM (20–21 Sep 2026): executed vs roadmap

Statuses below are quoted from `<R3>/12_audits/R3_PHASE_*_AUDIT.md`, re-read in this run. Counts were recomputed from the frozen `BASELINE_REL_R3_*` copies.

| Phase | Status line (verbatim) | Output verified in this run | Executed? |
|---|---|---|---|
| 0 Environment | `R3_PHASE_0_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION` | — | EXECUTED |
| 1 Fresh sources | `R3_PHASE_1_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION` | 5 PDFs; hashes = manifest (R03, C1 PASS) | EXECUTED |
| 2 / 2B Corpus | `R3_PHASE_2_COMPLETE …`, `R3_PHASE_2B_COMPLETE …` | 25 corpus files = manifest; article sets = official text (R03) | EXECUTED |
| 3 Instrument profiles | `R3_PHASE_3_COMPLETE …` | not recomputed | EXECUTED (documentary) |
| 4 Actor register | `R3_PHASE_4_COMPLETE …` | not recomputed (89 actors reported) | EXECUTED (documentary) |
| 5 Candidate relations | `R3_PHASE_5_COMPLETE …` | 56 relation rows present | EXECUTED |
| 6 / 6B Intermediation adjudication | `R3_PHASE_6_COMPLETE …`, `R3_PHASE_6B_COMPLETE …` | final_classification: **SUPPORTED_INTERMEDIATION 9, DIRECT_R_T 24, LEGAL_RELATION_NON_RIT 23** (recomputed) | EXECUTED. 6B rewrote 5 relation files in place; pre-6B versions survive only as hashes |
| 7 LAW × INTERMEDIARY | `R3_PHASE_7_COMPLETE …` | **7 units** (recomputed): ETS independent verifiers; ESR Central Administrator; ESR EEA; Climate Law EEA; SCF public/private implementing entities; SCF implementing authorities; SCF audit bodies | EXECUTED |
| 8 / 8B / 8C Mechanisms | `R3_PHASE_8_COMPLETE …`, `…8B…`, `…8C…` | **10 events**, researcher_final_mechanism: VERIFICATION 4, EVALUATION_ASSESSMENT 3, IMPLEMENTATION 3; all `CONFIRMED` (recomputed) | EXECUTED |
| 9 Mechanism configurations | `R3_PHASE_9_COMPLETE …` | not recomputed | EXECUTED (reduced form). `MECHANISM_CHAINS.csv` and `META_INTERMEDIATION_MAP.csv` from the original prompt were **not** produced |
| 10 / 10B Dataset proposal | `R3_PHASE_10_COMPLETE …`, `R3_PHASE_10B_COMPLETE — DAVID_DATASET_PROPOSAL_READY_FOR_RESEARCHER_REVIEW` | final package xlsx present (FE3DE0A1…) | EXECUTED |
| 11 Capacity derivation (Knowing/Assuring/Steering) | roadmap only (`R3_RESEARCHER_DECISION_…DIRECTION.md`, "Phase 11 — Capacity derivation … must be derived, not imposed") | none | **ROADMAP_NOT_EXECUTED** |
| 12 Cross-case architecture | roadmap only ("Phase 12 — Cross-case architecture") | none | **ROADMAP_NOT_EXECUTED** |

**Correcting the master prompt's premise.** The prompt suggested that the `LAW × INTERMEDIARY` consolidation and mechanism coding might have been roadmap only. Both were **executed** in R3 (Phases 7 and 8–8C). The items that remained roadmap are capacity derivation, cross-case architecture and the historical comparison.

**Conceptual note relevant to the comparison.** Three of the seven R3 LAW × INTERMEDIARY units are public bodies: the EEA (twice) and the SCF implementing authorities. Rotem's revised codebook ¶31 says "Public authorities exercising public regulatory powers are coded as regulators rather than intermediaries". The R3 relational framework and Rotem's restrictive rule therefore draw the intermediary boundary differently for public bodies. This is a **framework difference**, not an error on either side. Rotem's own implemented workbook does code some public bodies as intermediaries (e.g. "Court of auditors & the Commission internal auditor", rows 74 and 96 of `Coding Digital Intermediaries`), so this is also a Layer 2 ↔ Layer 3 gap in her materials (see `06_CODEBOOK/ROTEM_CONCEPTUAL_OPERATIONAL_ALIGNMENT_MATRIX.csv`).

## 2. R4 (22–29 Sep 2026): digital cross-domain validation

| Stage | What it is (verified) | Provenance class |
|---|---|---|
| R4.1 corpus | GDPR 32016R0679, DSA 32022R2065, AI Act 32024R1689 (`<ENV>/03_SOURCE_DATA_AND_CORPUS/R4_DIGITAL_CORPUS_REGISTER.csv`). **0 rows** for any R2 CELEX (recomputed) | EXECUTED |
| R4.2 structural extraction | 1,404 rows (485/424/495, recomputed). **Values are produced by a PowerShell script based on regular expressions** (`R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2_structural_extraction.ps1`): counterpart = first match of `(to\|with\|from) + determiner/actor word`; `Recipient=$counterpart`; `ActionObject` and `InformationObject` both = `Get-FirstClause $remainder 180`. Recomputed consequences: COUNTERPART = RECIPIENT in **1,404/1,404** rows (409 both empty); ACTION_OBJECT = INFORMATION_OBJECT in **1,404/1,404**. The `EXTRACTION_MODEL` field reads "Codex GPT-5 runtime; GPT-5.6 Luna High requested; exact runtime variant not exposed" for all rows | EXECUTED. **Provenance clarification:** a deterministic script that a model-assisted session wrote and ran, not a per-provision model reading |
| R4.2B QA sample | 90 rows (30 per act); 3 human calibration seeds | EXECUTED |
| R4.2C / 2C-R model reviews | 87 non-seed rows reviewed twice: a Luna self-review (relabelled after a researcher correction) and Terra V2. Both record `MODEL_VARIANT_NOT_EXPOSED` | EXECUTED |
| R4.2D human diagnostic | 12 cases, all `REVIEWED` by Igor Caires Machado; `HUMAN_PATTERN_CONFIRMED` = YES 12/12 | EXECUTED. Genuine human decisions |
| R4.2E-A / B0 / B1 | Triage, compression and advanced validation of repair families | EXECUTED (documentary audit only in this run) |
| Firewall flags | `RIT_CODING = NOT_STARTED`, `MECHANISM_CODING = NOT_STARTED`, `ROTEM_CODING_CONSULTED = NO` | as declared by R4 |

## 3. Implication for the Rotem comparison
- **R4 never applied R–I–T or Rotem's codebook to the digital acts** (its own firewall flags). R4 is evidence about the *reliability of automated provision-level structural extraction*. It is **not** evidence about the adequacy of Rotem's codebook.
- **The R4.2D human-confirmed failure modes are relevant to *our* proposal, not to hers.** These include: a preposition does not imply a recipient; proposition boundaries; modality loss; and that a model-detected pattern is not the root cause. They are risks that any provision-level child layer must control (see R10).
- **Igor's relational coding history (R3, PILOT_03) uses a broader intermediary concept** than Rotem's restrictive rule (public bodies; insurance — see R05/R09). This difference must be reported as a framework difference.
