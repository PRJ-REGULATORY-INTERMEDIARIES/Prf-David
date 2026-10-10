# NEW TEST 3x3 — COMPARABILITY AUDIT REPORT

**Date:** 2026-10-05 · **Rules applied:** G1–G7 of `00_PROTOCOL/TEST_3X3_PRE_REGISTRATION.md` (fixed before ranking)
**Tables:** `CASE_METRIC_COMPARABILITY.csv` (1,032 case-version × metric rows), `HARMONIZATION_REGISTER.csv` (48 rows), `01_CASE_UNIVERSE/CASE_SOURCE_PROVENANCE.csv`

## 1. The question

> Are the historical counts sufficiently comparable to support the registered ranking?

## 2. Answer

**Only inside one comparability stratum.** The five R3 clean-room laws are mutually comparable on all five registered metrics (stratum **S1**). Nothing else in the universe can be ranked against them: the R2 laws come from a different codebook version whose application demonstrably diverges on the shared instrument; the PoC, PILOT and Rotem material covers selected provisions or a different construct; the R4 and GDPR extractions never produced intermediation, intermediary or target counts.

### FINAL GATE: `COMPARABILITY_CONDITIONAL_PASS`

Meaning (as registered in G7): a comparability stratum with ≥3 rank-eligible case-versions exists (S1: 5 laws), ranking is permitted **only within S1**, and whether the three-domain selection is feasible must be tested at the diversity step (see `04_RANKING_AND_SELECTION/THREE_CASE_SELECTION_DECISION.md`). The gate is **not** `PASS` because cross-pipeline comparison fails; it is **not** `FAIL` because a common denominator exists (`METRIC_DEFINITION_REGISTER.md`, decision D1) and S1 is internally comparable.

## 3. Classification outcome

172 case-versions were classified (2 prohibited V8-stage items were listed in the universe but not opened or classified). Counts of case-version × metric rows by class:

| Class | Rows | Where |
|---|---:|---|
| C1_DIRECTLY_COMPARABLE | 20 | R3: actors, intermediaries, relations, intermediation relations (5 laws × 4) |
| C2_HARMONIZABLE_FROM_EXISTING_DATA | 10 | R3: regulators and targets (deterministic recount, one rule for all laws) |
| C3_PARTIALLY_COMPARABLE | 18 | R2 final version (3 laws × 6 metrics): same construct, diverging application, curated relation set |
| C4_NOT_COMPARABLE | 165 | R2 superseded versions; PoC; PILOT_01–03; R4 actors; GDPR_PILOT_01; Rotem lists |
| C5_PROVENANCE_INSUFFICIENT | 819 | metric never produced or never recorded (R4 R/I/T, Taxonomy, MDR, Lei 13.848, Rotem-only rows, provision packs, PILOT regulators/targets, ...) |

Every C3–C5 row carries an explanation in the CSV (`explanation` column). Canonical rank-eligibility: only the five R3 case-versions are rank-eligible (`rank_eligible_for_metric = YES` on all five ranking metrics).

## 4. Principal methodological discrepancies

1. **Scope (G2).** R3 and R2 read whole instruments. PILOT_01–03 coded 2–6 purposively selected provisions per act (chosen because Rotem had coded intermediaries there); PoC coded a small sample of lexical hits and stored only positives; the Rotem comparison packs are provision diagnostics. R4 processed whole instruments but only structurally. GDPR_PILOT_01 covers all 99 articles but not recitals and uses a different text baseline. A partially extracted law cannot compete with a fully extracted one, and the selected provisions are not independent of intermediation content.
2. **Metric production (G3).** R4 states that regulator/intermediary/target and mechanism coding are "not started"; GDPR_PILOT_01 has no R–I–T gate; the Rotem lists record intermediary labels, not relations. For these, three of the five registered metrics do not exist.
3. **Unit of analysis.** R3: census of candidate relations, one relation per (R, I, T, regulatory object). R2: curated provision-anchored records with actor arrays; includes direct, uncertain and not-supported records. PILOT_03: primitive actor→action→recipient edges. PoC: positive relation rows (levels L1/L2). R4: provision × actor × action records. GDPR_PILOT_01: qualified relations of all RGAM types. Rotem: intermediary × act.
4. **Actor definition.** R3: whole-instrument actor register (89 records, specific entities and classes). R2: actors holding an R/I/T role in retained relations. R4: provisional textual actor candidates (195/139/179, merge ambiguity flagged). The R3 count of actors (e.g., 34 for the Social Climate Fund) and the R2 count (e.g., 16 for CBAM) do not measure the same thing.
5. **Application of the intermediary rule — documented divergence.** See §5.
6. **Provenance.** R2 final package was rebuilt from an in-session read of a corrupted working file (`06_PROVENANCE.csv`; 20 base rows reconstructed, 5 promoted; evidence quotes `NOT_RECOVERED`; one issue unresolved). PILOT_03 rows are pre-adjudication model passes (19 targeted human decisions are not merged back into the pass files). GDPR_PILOT_01 is a single AI evaluator with 16 adjudication items pending. R4 has 181 of 1,404 records without a stored source excerpt.
7. **Within-pipeline version instability (R2).** Intermediation counts for the same law changed across R2 versions: Climate Law 1 / 0 / 1 / 3; CBAM 5 / 7 / 3 / 5; EUDR 3 / 2 / 3 / 4 (v1.0 proposal / v1.1 reading / R2 reading / final), so even the R2 value depends on which version is taken.

## 5. Bridge check (G4) — European Climate Law (32021R1119), counted by three pipelines

| Version | Intermediation relations | Which relations |
|---|---:|---|
| R3 frozen (clean-room gate, 2026-09-21) | **1** | EEA assisting the Commission's assessment of Member States (REL-32021-010) |
| R2 final_human_review_v2 (codebook v1.2) | **3** | Commission–{EEA, Scientific Advisory Board}–Member States; Commission–Advisory Board (2040 target)–Member States; Commission–Energy Union Committee–Member States |
| R2 Stage-4 attempt 02 (pre-human-gate RA adjudication) | **0** positive of 90 candidates | RA result: 89 negative, 1 insufficient evidence |

R3 recorded two of the R2 intermediaries as **negative boundary cases** for the same law: the European Scientific Advisory Board (BND-004, failed C1: advice with no identifiable separate target) and the Energy Union Committee (BND-006, failed C1: inter-institutional process support). The R2 changelog explains why R2 counts them: v1.2 decisions 1–2 (2026-09-08) reversed the earlier exclusion of comitology committees and of advisory input that shapes a forthcoming binding norm ("intermediação em sentido mais amplo"). R3 was run afterwards as a clean room that did not consult prior rounds.

**Result of the bridge check: material divergence on the primary metric (1 vs 3, with documented rule difference). G4 therefore forbids pooling R2 and R3 counts in one ranking; R2 case-versions are C3 and form their own stratum S2.**

A proxy harmonization (drop R2 relations whose I is a committee or an advisory body) was considered and **rejected** (`HARMONIZATION_REGISTER.csv`, `H-R2-PROXY`): R3's rejection of those two Climate Law relations rested on the absence of an identifiable target, whereas the R2 records for the analogous CBAM and EUDR committee/expert relations identify targets; deciding whether R3 would reject them needs re-adjudication of the provisions (new legal interpretation, forbidden by the harmonization rule), and the proxy could be checked on one shared instrument only.

## 6. Harmonization performed

All computations use existing structured fields only (`LOGS/scripts/compute_metrics.py`); originals are preserved in `CASE_UNIVERSE_MASTER.csv`; harmonized values are stored separately.

| Register ids | What | Used? |
|---|---|---|
| R3 targets, regulators (rule: distinct `T_actor_id` / `R_actor_id` over adjudicated relations) | converts relation fields into per-law counts under one rule for all five laws | **Yes** — registered ranking counts for S1 (class C2) |
| R3 alt. targets (supported relations only), alt. actors (in any relation / in supported relations), triples | sensitivity definitions | No (stored) |
| R2 triple unit (R × I × T expansion of intermediated records): CL 3, CBAM 7, EUDR 9 vs native 3 / 5 / 4 | aligns the unit with R3 | No — sensitivity only; it changes values but cannot reconcile the gate (bridge fails) |
| R2 actors in intermediated/any relations | counterparts of the R3 alternates | No |
| PILOT_03 Model B recount | pass-to-pass check | No (class remains C4) |
| Bridge row (Climate Law: 1 vs 3 vs 0) | comparability audit | **Yes** — used only to decide G4 |
| `NOT_HARMONIZABLE` rows (R2 relations census, R2 gate application, H-R2-PROXY, R4/GDPR/others) | documented impossibility | — |

No relation was added, no new V8 analysis was performed, no legal text was re-read for coding.

## 7. Consequences for the ranking

- Rank-eligible set = {32003L0087, 32015D1814, 32018R0842, 32021R1119, 32023R0955} (R3, stratum S1; all FULL_INSTRUMENT).
- `CONDITIONALLY_ELIGIBLE` (not rank-eligible, retained in `GLOBAL_CASE_RANKING.csv` as NOT_RANKED): CBAM 32023R0956 and EUDR 32023R1115 (R2, stratum S2).
- Everything else is non-comparable or has no source (see `CASE_UNIVERSE_MASTER.csv`).
- Tie-breakers: within S1 no C3/C4/C5 metric is needed (G6).

## 8. Limits of this audit

1. The bridge rests on one shared instrument; it demonstrates the divergence, it does not estimate its size elsewhere.
2. R2's text-field parsing for the triple and actor recounts is label-level (role annotations stripped); used for sensitivity only.
3. R3 was read through its normalized staging tables, reconciled against the frozen workbook (`R4_R3_RECONCILIATION.csv`: all PASS).
4. The Rotem .docx codebook was read through the project's comparison record, not re-extracted.
5. Legal status/vigência of the instruments was not re-verified (not part of this stage).
