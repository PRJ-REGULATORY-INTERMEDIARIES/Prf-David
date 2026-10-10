# CASE_QA_REPORT — RGAM_C2_CBAM

Machine QA of the case execution (mechanical checks plus statements of fact about access). It does not validate the legal or analytical correctness of any record; all records remain machine-generated and provisional.

## A. Case-freeze checks requested by the brief

| # | Check | Result | Basis |
|---:|---|---|---|
| 1 | Source hash matches capsule | PASS | SHA-256 of LEGAL_SOURCE/32023R0956_official_en.xhtml recomputed at the end of the run = `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e`; expected in CASE_METADATA.json = `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e` |
| 2 | Only allow-listed files read | PASS | files read are listed exactly in ACCESS_AND_CONTAMINATION_LOG.md and RUN_METADATA.csv (32 paths, all inside the allow-list) |
| 3 | No V8 output read | PASS | no V8 path was opened, listed or requested |
| 4 | No historical extraction read | PASS | no historical relationship extraction, pilot or R2/R3/R4 path was opened |
| 5 | No other RGAM case result read | PASS | no other capsule or case output directory was opened |
| 6 | All records have stable ids | PASS | ids generated mechanically with the dictionary formats (ST-nnnn, NA-nnnn, PD-nnn, QR-nnnn, EXT-nnn, SC-nn, ARCH-nn, PROP-nnn, CL-nn, UNC-nnn, HQ-nnn, LNK-nnnnn, TR-nn, DEV-nn, RUN-nn); ids unique: True |
| 7 | Every higher-order claim is vertically traceable (A->S->R/NA/PD->ST->unit->span) | PASS | mechanical resolution of 166 relation/assignment records (statement ids exist, unit ids exist, evidence span is a verbatim substring of a cited unit), 11 subconfigurations (members resolve), 7 architecture candidates (member S, I2 relations and I1 units resolve) and 19 properties (supporting records resolve); problems found: 0 |
| 8 | Unsupported claims rejected or deferred | PASS | see section B |
| 9 | INDETERMINATE remained available and was used | PASS | 4 of 7 architecture candidates are INDETERMINATE; 4 properties are `undetermined`; 3 closure statements UNDETERMINED |
| 10 | HQ items not adjudicated | PASS | all `human_decision`, `human_rationale`, `decided_by`, `decision_date` blank in 16 HQ items |
| 11 | Frozen method not altered | PASS | the six frozen method documents were only read; their SHA-256 values at the end of the run are listed in EXECUTION_PROVENANCE.md; every point where the method was silent or applied at the nearest fit is logged in PROTOCOL_DEVIATION_LOG with `gap_ref` where an addendum item applies; no rule was changed, no vocabulary created |
| 12 | Data-dictionary integrity rules 1-10 | see section C | |

## B. Claims rejected or deferred (unsupported at the asserted level)

- Recitals: 82 recitals screened; no record created from any recital (RGAM-DR-07); external instruments named only in recitals produced no EXT.
- No counterparty invented: CBAM declaration, surrender of certificates, the carbon-price claim, record-keeping duties and several Annex IV permissions are kept as NA; the recipient of surrender and of the declaration is not named in W (UNC-log).
- Purposive clauses naming verifiers, the Commission or the competent authority as those whom records are to enable (A7(5), A10(6)) were not coded as relations.
- 'Regulation (EC) No 515/97 shall apply mutatis mutandis' (A25(5)): no relation derived; recorded as EXT with constitutive dependency.
- 'Recognised in all Member States' (A17(1)) is passive and creates no relation.
- The Commission's preliminary calculations and the information it provides to competent authorities (A19(4), A35(4)) are coded as non-binding inputs (indicative; without prejudice), not as authority.
- The delegated-act power of A27(6) was not tied to the investigation of A27(5): the circumvention candidate (ARCH-06) is INDETERMINATE on I3.
- The further reports of A30(5)-(8) and 'relevant stakeholders' were not grouped or given positions (shared parties/theme only).
- Accountability: no relation is ANSWERABILITY or ACCOUNTABILITY; reasons-plus-appeal-information relations are INFO with sufficiency indeterminate (no forum identified); absence-dependent claims about accountability forums, necessary stage and substitutability are UNDETERMINED.
- No relation was inferred from reachability or from co-occurrence of actors; no graph or centrality measure was computed; no score, composite or threshold exists in any table.
- Epistemic statuses: nothing above `legal_constitution_evidenced`; 24 relations/assignments down-coded to `documented` for constitutive external dependencies; positions and devices are `documented`; `material_establishment_evidenced` appears nowhere and exercise is not collected.

## C. Data-dictionary integrity rules (section 4)

| Rule | Statement | Result | Detail |
|---:|---|---|---|
| 1 | Every unit_id exists in SOURCE_UNIT_INVENTORY; units_screened = units_total | PASS | all unit-id columns checked; UNIT_SCREENING rows = SOURCE_UNIT_INVENTORY rows = 558 = INSTRUMENT_LEVEL_SUMMARY.units_total/units_screened |
| 2 | Every NA, PD, QR, EXT cites >=1 ST; every ST cites >=1 unit; recital_only=Y has no derived record | PASS | NA/QR cite ST in `statement_ids`; PD and EXT are cited through `INSTITUTIONAL_STATEMENTS.derived_record_ids` (their tables have no statement column); no ST is recital-only |
| 3 | Every *_ids and *_pd_id field resolves; accountable_via resolves to accountability QR | PASS | all id-typed fields resolve; `accountable_via_qr_ids` is empty because no QR is of type `accountability` (none to point to) |
| 4 | Every QR has origin and counterpart, modality != prohibition, no material_establishment_evidenced | PASS | |
| 5 | Every NA/QR/SC/ARCH/PROP has >=1 provenance row; derived records state a rule and cite >=2 units or an explicit cross-reference | PASS | derived records cite >=2 units in all cases |
| 6 | Every INTEGRATED/OVERLAPPING ARCH has an HQ item; INTEGRATED only if I1-I4 all SATISFIED | PASS | ARCH-01 and ARCH-05 INTEGRATED (HQ-INTEGRATION); ARCH-07 OVERLAPPING (HQ-OVERLAP) |
| 7 | PROP with closure_dependency=Y has a closure_ref; closure UNDETERMINED forces status undetermined | PASS | |
| 8 | Every EXT not_checked and outside_corpus_not_expanded | PASS | 33 EXT |
| 9 | HUMAN_REVIEW_QUEUE human columns blank | PASS | |
| 10 | TRACE_DEMONSTRATIONS.vertical_chain resolves step by step | PASS | ARCH/S -> relation/assignment ids -> ST ids -> unit ids -> span prefixes |

Additional mechanical checks: all 19 CSV headers equal the frozen templates (PASS); every evidence span is <= 400 characters and a verbatim substring of a cited unit (PASS); no QR has `prohibition` modality (PASS); every NA with `prohibition` has `constraint_only = Y` (PASS); screening issues: 0; unresolved record keys at build: 0.

## D. Limitations

- Mechanical QA cannot establish that a relation type, direction or status is the best reading; the human-review queue lists the consequential choices.
- The source-file parse produced one unit for each goods table of Annexes I and II; table geometry is not faithfully represented for the iron and steel tables (declared).
- The technical read-deny described in the blindness policy was not verified active; the allow-list in the brief was the control used.
- A text-completeness check compared every source paragraph with the parsed units (only annex numbers and titles, kept in the locator text, are not unit text).

Result of vertical-traceability problems found: none
