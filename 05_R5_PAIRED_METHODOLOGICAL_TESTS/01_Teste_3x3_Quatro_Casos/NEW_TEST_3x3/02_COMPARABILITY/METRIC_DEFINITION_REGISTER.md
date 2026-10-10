# NEW TEST 3x3 — METRIC DEFINITION REGISTER

Controls which definition of *regulator, intermediary, target, regulatory intermediation, relation* (and *actor*) each historical metric rests on. Nothing here is invented: every definition is taken from a project codebook or method record, cited by path (relative to the repository root `Prf-David/`). SHA-256 of cited files are in `01_CASE_UNIVERSE/CASE_SOURCE_PROVENANCE.csv`.

## 1. Controlling definitions recovered

| # | Source (version/status) | Path | Regulator (R) | Intermediary (I) | Target (T) | Regulatory intermediation | Relation / unit |
|---|---|---|---|---|---|---|---|
| D-R3 | R3 clean-room gate (frozen 2026-09-21; authoritative per `R4_R3_BASELINE_MANIFEST.md`) | `R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM/12_audits/R3_PHASE_6_INTERMEDIATION_AUDIT.md`; manifest `R4_CROSS_DOMAIN_VALIDATION/R4_R3_BASELINE_MANIFEST.md` | role in an identifiable R–T relation; roles are relational | "institutionally distinct third actor" (C2), no support from presence, advice, consultation or non-binding expertise alone | the T of the identifiable R–T relation (C1) | relation with **C1 identifiable R–T relation = YES, C2 distinct institutionalized third party = YES, C3 demonstrable mediating function = YES** → `SUPPORTED_INTERMEDIATION` | one adjudicated relation per candidate (R,I,T, regulatory object); census of candidate relations (56); classes SUPPORTED_INTERMEDIATION / DIRECT_R_T / LEGAL_RELATION_NON_RIT / UNCERTAIN / NOT_SUPPORTED |
| D-R2 | `dataset-eurlex` production codebook v1.0 (locked) + `PRODUCTION_CHANGELOG` v1.1/v1.2 | `Before_R2/dataset-eurlex/methodology/codebook.md`; `.../docs/methodology/PRODUCTION_CHANGELOG.md` | "regulador ou autoridade regulatória na relação focal" (condition A: identifiable authority/rule/function; formal author of the act is not enough) | "terceiro ator analiticamente distinto que desempenha função regulatória mediadora" (conditions C and D); advising, consultation, participation or receiving the same duty are insufficient alone | "destinatário, rule-taker ou alvo" directly subject to the focal requirement (condition B) | `positive` = five conditions A–E all YES (regulator, target, distinct third, mediating function, evidence); UNCLEAR is never rounded up | one provision-anchored candidate relation; arrays of R/I/T actors per record; direct T→R reporting without a third actor is *not* intermediation |
| D-POC | PoC `RIT_CODEBOOK_v4` (and v3) | `Before_R2/Estudos Preliminares e testes/PoC 01/Entrega-04/RIT_CODEBOOK_v4.md` | identifiable regulator/rule-maker | third actor analytically distinct from both, performing a mediating regulatory function "rather than merely advising or receiving the same duty" | identifiable target/rule-taker | five-condition relational test; positive only if five YES; only positives enter `rit_relationships_v4.csv` | one row per relation level (`L1`/`L2` chains decomposed); R, I, T pairwise distinct |
| D-P03 | PILOT_03 `CODING_RULES_V0_3_ADJUDICATED` (v0.3; gate `ONTOLOGY_STABLE_WITH_REVISIONS`, production not authorized) | `RELATIONAL_LEXIMETRICS_PILOT/PILOT_03/01_PROTOCOL/CODING_RULES_V0_3_ADJUDICATED.md`; `.../06_ONTOLOGY_TESTS/RIT_DERIVATION_RULES_V0_1.md` | actor_a with role regulator in a primitive edge | "relational position, never a permanent actor attribute"; insurance, co-occurrence or conditional safeguards alone do not establish it | recipient/target of an edge | derived R–I–T = shared candidate I, explicit R→I and I→T edges, compatible object/modality, no contradiction, governance work | **primitive actor→action→recipient edge** per legally distinct directional action |
| D-ROT | Rotem revised codebook (REV) | `RELATIONAL_LEXIMETRICS_PILOT/PILOT_01/00_SOURCES/Codebook_Regulatory_Intermediation_Revised (1).docx` (as summarized in `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/06_CODEBOOK/CODEBOOK_VERSION_DIFF.md`) | regulator context (multi-valued institutional context) | actor the act "substantively assigns, recognizes, or relies upon … to perform at least one identified regulatory function through an identifiable governance mechanism" (REV ¶27), incl. necessary reliance; mere mention, positional middle, expertise, ordinary commercial service excluded | target-category context | digital-governance intermediary as defined in REV | unit = **intermediary × act** (intermediary category per act); older rows act-packed |
| D-RGAM | GDPR_PILOT_01 `DECISION_RULES` v1.0–1.2 (RGAM v0.6.1/V6) | `RGAM/pilot/GDPR_PILOT_01/00_PROTOCOL/DECISION_RULES.md` | not coded | not coded as a role; positions/devices (e.g., certification body) recorded | counterpart | **no R–I–T gate**; qualified relation = both parties identifiable in the same provision, any relation type | normative assignment / qualified relation / position-device per paragraph unit |
| D-R4 | R4.2 structural method note | `R4_CROSS_DOMAIN_VALIDATION/R4_2_METHOD_NOTE.md` | "does not identify regulators, intermediaries, targets or regulatory intermediation mechanisms; no R, I or T fields were created" | not coded | not coded | not coded | LEGAL PROVISION × ACTOR × LEGAL ACTION structural record |

## 2. Comparison and common operational denominator

1. **R3, R2 and PoC share a single construct**: a *regulatory intermediation relation* is a relation in which an identifiable regulator–target relation is mediated by an analytically distinct third actor performing a regulatory function, with textual evidence; advice, consultation and receiving the same duty do not suffice. R3 states it as three conditions (C1–C3, evidence kept separately), R2/PoC as five conditions (A–E). The wording is aligned (A+B ≈ C1, C ≈ C2, D ≈ C3, E = evidence).
2. **PILOT_03** applies a *relational-position* rule on primitive edges; its "derived R–I–T candidates" follow the same logic but are produced on selected provisions by two model passes before adjudication.
3. **Rotem REV** uses a different construct (the digital intermediary legally constituted, recognized or relied upon, incl. necessary reliance and process-based arrangements) and a different unit (intermediary × act).
4. **RGAM/GDPR_PILOT_01** and **R4** do not contain the R–I–T test at all.

**Decision D1 (documented): a common operational denominator exists** — the relational R–I–T test (§2.1) — so the §7 stop rule (“no defensible common definition → stop”) is **not** triggered. It is the denominator for G1. The denominator is *shared in wording*; whether it is *applied identically* is a separate question and is tested by the bridge check (see `COMPARABILITY_AUDIT_REPORT.md`).

**Decision D2:** metrics from D-ROT, D-RGAM and D-R4 are not on the denominator and cannot be harmonized without new interpretation (classified C4/C5).

**Decision D3:** where R3 and R2 differ in gate application on the same instrument, no reconciliation is attempted (it would need new legal interpretation); strata are kept separate (G4).

## 3. Operational metric definitions used here

For each of the five registered metrics, the *native definition* in each family and the *deterministic recount* (if any) are listed. "Native" means as published in the family's own records; "recount" means computed by `LOGS/scripts/compute_metrics.py` from existing structured fields without interpretation.

| Metric | R3 (stratum S1) | R2 (stratum S2) | PoC v4 | PILOT_03 | R4 | GDPR_PILOT_01 | Rotem lists |
|---|---|---|---|---|---|---|---|
| **Actors** | native: LAW × ACTOR register records of the whole instrument (specific entities + actor classes; recital-only actors flagged) | native: distinct actors with an R/I/T role in retained relation records | recount: distinct actor ids in positive rows | recount: distinct normalized names across selected provisions' edges | native: provisional actor candidates (any textual actor) | recount: distinct strings in origin ∪ counterpart | not recorded |
| **Regulators** (not ranked) | recount: distinct `R_actor_id` over adjudicated relations | native: R-role actors | recount | not recounted (role fields incomplete) | not produced | not produced | not recorded |
| **Intermediaries** | native: LAW × INTERMEDIARY units (distinct I in supported relations) | native: distinct I-role actors | recount: distinct `I_actor_id` | recount: distinct `actor_b` with derived status | not produced | not produced | rows of listed intermediaries (Rotem definition) |
| **Targets** | recount: distinct `T_actor_id` over all adjudicated relations (alt.: supported only) | native: distinct T-role actors | recount | not recounted | not produced | not produced | not recorded |
| **Relations** (total identified) | native: all 56 adjudicated candidate relations (census) | native: all retained relation records incl. uncertain/not supported (curated) | native: positive rows only | native: primitive edges on selected provisions | not produced (structural records are not relations) | native: qualified relations (all types) | not recorded |
| **Intermediation relations** | native: `SUPPORTED_INTERMEDIATION` | native: researcher-approved/modified `intermediated` records | native: positive rows | native flag: `derived_rit_candidate==YES` (candidate, pre-adjudication) | not produced | not produced | not recorded |

## 4. Registered counting rules for the ranking (only for stratum S1 = R3)

- `intermediation_relations` = number of `SUPPORTED_INTERMEDIATION` relations of the instrument.
- `actors` = LAW × ACTOR records of the instrument (R3 actor register).
- `intermediaries` = LAW × INTERMEDIARY units of the instrument.
- `targets` = distinct non-null `T_actor_id` over all adjudicated relations of the instrument (recount; alternative restricted to supported relations stored in `HARMONIZATION_REGISTER.csv`).
- `relations` = all adjudicated relations of the instrument.

## 5. Uncertainties recorded

1. R3 actor records mix specific entities and actor classes; it is the registered `actors` definition anyway (native, identical across the five laws).
2. The harmonized R2 actor/triple recounts rely on stripping role annotations from free-text actor fields (rule in the harmonization register); they are approximate at label level and are used only in the bridge/sensitivity analysis.
3. The Rotem codebook was read through the project's own comparison record (`CODEBOOK_VERSION_DIFF.md`), not re-extracted from the .docx.
4. The R3 workbook states that normalized tables are authoritative; the normalized tables used here are the staging copies in `R3_HISTORY_STAGING`. Their frozen totals were reconciled in `ENVIO_R4_TO_DAVID/12_ARCHIVE_SUPPORT/R4_R3_RECONCILIATION.csv` (all rows `PASS`: 5 laws, 89 actor records, 56 relations = 24 DIRECT_R_T + 23 LEGAL_RELATION_NON_RIT + 9 SUPPORTED_INTERMEDIATION, 7 LAW × INTERMEDIARY units), and the recount in this experiment reproduces those totals. The Phase 6 audit table (23 direct + 1 uncertain) was superseded by Phase 6B, which resolved the single uncertain relation (OLAF) to `DIRECT_R_T`; the frozen state (24 direct, 0 uncertain) is used.
