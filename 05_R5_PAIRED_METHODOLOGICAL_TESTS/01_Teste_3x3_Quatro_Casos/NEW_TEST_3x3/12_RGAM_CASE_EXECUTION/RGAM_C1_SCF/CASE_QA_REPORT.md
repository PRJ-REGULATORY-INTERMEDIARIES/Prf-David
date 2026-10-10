# CASE_QA_REPORT — RGAM_C1_SCF

QA performed by the executor on its own outputs (mechanical checks by scripts in `_work/`; judgments by the executor). It is a self-audit, not independent validation.

## 1. Required verifications

| # | Verification | Result |
|---|---|---|
| 1 | Source hash matches the capsule | PASS. SHA-256 of `LEGAL_SOURCE/32023R0955_official_en.html` = `cf8c60fc233311436dfdd3ee236d0c8399eda55fea174610e91b5594f84a0408` = `source_sha256` in `CASE_METADATA.json`; structure parse: 29 articles and 5 annexes (metadata 29 and 5), 47 recitals. |
| 2 | Only allow-listed files read | PASS. See `ACCESS_AND_CONTAMINATION_LOG.md` (no attempted read outside the allow-list; harness-supplied directory and commit-subject names seen, no content). |
| 3 | No V8 output read | PASS. |
| 4 | No historical extraction read | PASS. |
| 5 | No other RGAM case result read | PASS. |
| 6 | All records have stable ids | PASS. Id formats and uniqueness checked for ST, NA, PD, QR, EXT, SC, ARCH, PROP, CL, LNK, UNC, HQ, TR, DEV, RUN (checker). |
| 7 | Every higher-order claim is vertically traceable (A to S to R/NA/PD to ST to unit to span) | PASS. TR-01 (seeded draw, SC-05) and TR-02 (largest support, ARCH-01) resolve step by step; in addition a script traced every member of every subconfiguration, every I2 relation of every candidate and every supporting record of every property down to statement, unit and verbatim span (0 failures). |
| 8 | Unsupported claims were rejected or deferred | PASS (see section 3). |
| 9 | INDETERMINATE remained available | PASS. Used for ARCH-03 (I3 and I4 indeterminate), four properties (`undetermined`), four closure records (`UNDETERMINED`); `NO_ARCHITECTURE_WARRANTED` was available at instrument level and not selected. |
| 10 | Human-review items not adjudicated | PASS. 19 HQ items; `human_decision`, `human_rationale`, `decided_by`, `decision_date` blank in every row. |
| 11 | Frozen method not altered | PASS. No frozen document, vocabulary or schema was edited; no new vocabulary beyond the two registered execution tokens (`NON_OPERATIVE_SOURCE_GAP`, `FUNCTION_VOCABULARY_UNRESOLVED`); the allocation of dimensions to families F1-F5 (absent from the allowed sources) and the status-ceiling operationalisation are logged as deviations (DEV-08, DEV-12). All seven execution-addendum gaps (GAP-01..07) are logged with `gap_ref`. |

## 2. Data-dictionary integrity rules 1-10 (section 4), result per rule

1. **Rule 1 — PASS.** All 706 units are inventoried and screened exactly once (`units_total` = `units_screened` = 706); every unit id in every table (statements, assignments, positions, relations, external references, subconfigurations, candidates, provenance links, uncertainties, inventory parents) exists in `SOURCE_UNIT_INVENTORY`.
2. **Rule 2 — PASS.** 188 statements each cite at least one unit; `recital_only` = N for all (no statement rests on a recital alone); every NA (63), PD (28), QR (60) and EXT (46) is cited by at least one statement (statement ids for NA and QR; `derived_record_ids` of statements for all four), and the two directions agree.
3. **Rule 3 — PASS.** Every id-valued field resolves to an existing record; `accountable_via_qr_ids` point only to the two accountability relations (QR-0037, QR-0058).
4. **Rule 4 — PASS.** All 60 QR have `origin_pd_id` and `counterpart_pd_id`, none has modality `prohibition` (the four prohibitions are NA with `constraint_only` = Y), none carries `material_establishment_evidenced`.
5. **Rule 5 — PASS.** 3 036 provenance links; every NA, QR, SC, ARCH and PROP has at least one link and every cited supporting unit of NA, QR, PD, EXT and ST is mirrored; all 26 derived records (11 NA, 15 QR) state a derivation rule and cite at least two units or an explicit cross-reference.
6. **Rule 6 — PASS.** ARCH-01 (INTEGRATED, I1-I4 SATISFIED) is queued as HQ-001 and ARCH-02 (OVERLAPPING_OR_PARTIALLY_INTEGRATED) as HQ-002; ARCH-03 is INDETERMINATE (no queue item required; its accountability question is queued as HQ-003).
7. **Rule 7 — PASS.** Every PROP with `closure_dependency` = Y resolves to a closure record; the four PROP whose closure result is UNDETERMINED (decision-centre plurality of SC-01, necessary stage, substitutability, accountability toward the Parliament) have status `undetermined`.
8. **Rule 8 — PASS.** All 46 EXT are `not_checked` and `outside_corpus_not_expanded`; no boundary decision was recorded.
9. **Rule 9 — PASS.** Human-only columns of the queue are blank.
10. **Rule 10 — PASS.** Both trace chains resolve to existing ids, units and the verbatim evidence span.

Additional checks (all PASS): headers identical to the blank templates; UTF-8 with BOM; controlled vocabularies of the data dictionary respected in every table (checker `vocab_check.py`, 0 issues); every evidence span of ST, NA, PD and QR is a verbatim substring of a cited unit and at most 400 characters; every EXT supporting unit lies within the units of the statements it cites; parties and subjects of every subconfiguration member are among its member positions; every borderline device, compound or ambiguous norm type, accountability-sufficiency `indeterminate` and constitutive external dependency has a queue item; no score, index, threshold or ranking appears in any table.

## 3. Examples of claims rejected, deferred or limited (stopping rule)

- **No counterparty invented:** requests up to the maximum allocation (A14.P2), revised Plan (A16.P1), obligor of the information entitlement of recipients (A23.P2), reporting requirements imposed on recipients (A24.P3), programme amendments and notifications under the inserted Article 26a (A28) are NA without counterparty; A25.P2 yields a statement only (obligor unstated); all are queued (HQ-DIRECTION).
- **No relation from diffuse audiences:** the public, media and "multiple audiences" (A23) are not admitted as parties.
- **No relation toward a discharge authority:** A21.P3 refers to a procedure outside W; recorded as an NA of the device Fund with a constitutive external dependency; accountability toward a discharge authority is undetermined.
- **Device not an actor:** the funding relation is attributed to the Commission by a stated derivation from A12.P0, with the Fund as instrument (flagged and queued).
- **Absence-dependent properties:** necessary stage, substitutability and plurality of decision centres in SC-01 are undetermined; depth from the rule-making position and self-regulatory autonomy are not attributable.
- **No subconfiguration from a single relation or thematic proximity:** the delivery and pass-on relation (A9), the entrustment of managing authorities (A11(3)), the joint-communication relation (A23(3)), and the A25 transmission and invitation relations remain ungrouped relations.
- **No architecture asserted for the Parliament dialogue:** ARCH-03 is INDETERMINATE (accountability elements missing; constitutive external dependency).
- **Recital-only content creates no record:** e.g. the information and monitoring system (data-mining and risk-scoring tool) and the Plan submission date of recital 17.
- **Annex content limited:** Annex I formulae and Annex II values yield statements only (no relation); the 27 named Member States of Annex II are not recorded as separate INSTANCE positions.
- **External sources:** none retrieved; 13 of 46 EXT carry a constitutive dependency and limit the dependent claims to the declared corpus.

## 4. Known limitations (self-assessed)

- Single-pass machine execution; repetition by the same model is not reliability; all records are provisional.
- The invocation context displayed a reasoning-effort setting of 10 although the brief asked for the highest available effort; the setting could not be changed (recorded in `EXECUTION_PROVENANCE.md`).
- Annex I formula images were viewed only in part (three of six image-only units) and are not transcribed; no record rests on them.
- Borderline classification choices (nearest relation types, residual function tags, internal control system and performance reporting system as borderline devices, the accountability readings, the status-ceiling operationalisation, the family allocation) are flagged and queued rather than resolved.
- The I2/I3 thresholds are unvalidated by design; the INTEGRATED and OVERLAPPING outcomes are scoped to the declared corpus.
