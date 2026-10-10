# CASE_RGAM_REPORT — RGAM_O_DIR_86_361 (machine-generated and provisional)

Instrument: Council Directive 86/361/EEC of 24 July 1986 on the initial stage of the mutual recognition of type approval for telecommunications terminal equipment (CELEX 31986L0361). Protocol: RGAM paired execution protocol v1.0 with the execution-gap addendum (GAP-01..07). Chain: W → E → P → R → S → A → profile, with M as the transversal claim-anchoring control.

Execution note: this report describes the frozen output of a **recovery run**. The 19 analytical tables were first produced by an earlier executor that was interrupted by an API rate limit before any validation; the recovery executor independently re-verified them from the frozen source and method, made the corrections listed in `CASE_QA_REPORT.md`, and completed the missing deliverables. No comparison with any other method or case is made anywhere in this report.

## 1. W declaration and coverage

- W is the complete frozen official source file `LEGAL_SOURCE/31986L0361_official_en.html` (original act as published, OJ L 217, 05/08/1986, p. 21; no consolidation). SHA-256 `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57`, re-verified in the recovery run: **MATCH** with `CASE_METADATA.json`.
- Domain, from the title and the object clause of Article 1 only: the initial stage of mutual recognition of type approval for telecommunications terminal equipment, namely mutual recognition of the results of tests of conformity with common conformity specifications for mass-produced terminal equipment.
- Temporal reference: adoption 24 July 1986 (signature block); Article 11(1) gives Member States a period of not more than one year after adoption (derived deadline 24 July 1987); W states no entry-into-force date; neutral metadata: historical original act, later repealed (1992), no successor act substituted. Legal status `in_force` is asserted for this interval only (queued, HQ-015).
- Structure: 12 articles (metadata 12), 0 annexes (metadata 0), 14 recitals (not stated in the metadata), 93 units in total (67 operative-article units, 14 recitals, 11 formal units, 1 title block). Structure check: MATCH.
- Coverage: every unit is inventoried and screened in source order (93 = 93). 61 units screened Yes (at least one derived statement), 32 No (14 recitals, definitions not relied on, formal and footnote units). A "No" is a legitimate result; headings and recitals create no record (RGAM-DR-06, DR-07). An independent mechanical check confirmed that the inventory plus the article-heading and numbering labels exhaust the source body text.
- Declared exclusions: page chrome of the EUR-Lex file, the `*****` separator, "Article N" heading lines (kept as locators), Official Journal page layout. No tables or annexes exist.
- `W != A`: W is the documentary universe, not an architecture.

## 2. Record counts by table (evidence descriptors only)

| Table | Rows |
|---|---:|
| W_DECLARATION | 1 |
| SOURCE_UNIT_INVENTORY | 93 |
| UNIT_SCREENING | 93 |
| INSTITUTIONAL_STATEMENTS | 86 |
| NORMATIVE_ASSIGNMENTS | 20 |
| POSITIONS_AND_DEVICES | 12 (11 positions, 1 device row classified BORDERLINE_INS-TYPE) |
| QUALIFIED_RELATIONS | 39 |
| EXTERNAL_REFERENCES | 10 |
| SUBCONFIGURATIONS | 6 |
| ARCHITECTURE_CANDIDATES | 2 |
| PROPERTY_REGISTER | 15 |
| CLOSURE_REGISTER | 6 |
| PROVENANCE_LINKS | 746 |
| UNCERTAINTY_LOG | 36 |
| HUMAN_REVIEW_QUEUE | 19 |
| TRACE_DEMONSTRATIONS | 2 |
| INSTRUMENT_LEVEL_SUMMARY | 1 |
| PROTOCOL_DEVIATION_LOG | 15 |
| RUN_METADATA | 1 |

Counts describe the evidence base; they carry no significance, score or ranking.

## 3. Subconfigurations and warrants

Every S is constructed from stated relations (not from chapters, vocabulary or theme), starts as `S`, and records pattern rule, governance question, constituents, organizing mechanism, warrant, boundary, overlap, competing grouping and uncertainty.

| S | Scope | Pattern rule (summary) | Organizing legal coupling |
|---|---|---|---|
| SC-01 | Specification chain: programming, mandate and drafting of common conformity specifications | programming–mandate–drafting chain | Commission programming duty conditioned on consultation of the Committee and based on the essential requirements (A4(1)); Council competence over the essential-requirements list (A3, A2(17)); Commission request to the CEPT (A4(2)); CEPT consultation duty |
| SC-02 | Recognition of certificates of conformity for type approval | issuer–certificate–recognizer | recognition and no-re-testing rule (A6(2)) conditioned by explicit cross-reference on the certificate issued by the approved laboratory (A7(3), A2(16)); mandatory use of specifications (A6(3)); implementation duty (A1) |
| SC-03 | Qualification, notification and publication of authorities and laboratories | qualification–notification chain | laboratory verification/approval (definition-derived, A2(8), GAP-07) → notification and reports (A7(1)-(2)) → publication of the authorities list and Committee consultations (A5(2)(b), A7(5)); transmission to the Committee not used (transmitter unspecified) |
| SC-04 | Waiver from the use of specifications in purchasing | conditional-dependency chain | explicit triggers and conditions in A7(4)(b), A7(4) subparagraphs 2 and 3 |
| SC-05 | Suspension of recognition, revocation and the associated Community procedure | safeguard-procedure pattern | chain of triggered duties in A8(1)-(5) with explicit conditions; the electrical-safety branch (A8(2)) is external and is not S content |
| SC-06 | Committee organic frame | forum-constitution pattern | designation, chair, secretariat, rules of procedure, request-based consideration (A5); weaker warrant than SC-02 to SC-05 because membership is not stated in W |

Overlaps are recorded (for example SC-01/SC-04/SC-05/SC-06 through the shared Committee and CEPT relations; SC-02/SC-03/SC-05). The intersection of two S is not treated as a third S. Relations not grouped into any S (the Article 9 proposals to the Council, the Article 11 notification relations, and the corresponding assignments) remain at relation level.

## 4. Candidate architectures: I1–I4, rival groupings, outcomes

Both candidates followed the anti-circularity sequence (question → independent coupling → consequence → rivals and boundary).

**ARCH-01** (SC-01, SC-02, SC-03, SC-05). I1 SATISFIED: governing problem = making test-based conformity results and the specifications on which they rest usable across Member States for type approval, including the Member State option to suspend recognition; scale Community/Member States; interval adoption to repeal. I2 SATISFIED: couplings read from explicit cross-references (A6(1)-(2) with A4(2); A6(2) "without prejudice" to A8; A7(3)/A2(8) issuers; A8(3) laboratory "notified in accordance with Article 7"; A8(4) withdrawal and further brief); kinds: qualified procedural dependency and conditional dependency. I3 SATISFIED: the recognition effect of a certificate (SC-02) is conditional on a published reference to a specification that the Commission and the CEPT are mandated to produce (SC-01) and is subject to suspension by a Member State (SC-05); bearer ARCH-01, rule read from the stated conditions, not from reachability. A feedback consequence from suspension ground (b) to withdrawal of the specification is **not** asserted because the identity of the "list published" in A8(4) with the references of A6 is not stated (UNC-012, HQ-008). I4 INDETERMINATE: constitutive external dependencies (the CEPT Memorandum of Understanding on NETs, the CEPT accreditation system, Article 9 of Directive 73/23/EEC, the non-prejudice clause for Directive 83/189/EEC) are unresolved and no retrieval is authorized. Rival groupings: recognition regime with specifications as an external input; SC-05 as a stand-alone safeguard; shared Commission/Committee participation only (rejected for the couplings that rest on cross-references). **Outcome: INDETERMINATE.**

**ARCH-02** (SC-01 to SC-06). I1 SATISFIED (the Directive as one regime for the initial stage). I2 INDETERMINATE: satisfied for some pairs (SC-04–SC-01 through A7(4)(b); SC-06 as a mandatory consultation interface) but not shown between SC-04 and SC-05 other than shared participants, and ambiguous for A6(3) subparagraph 2 (HQ-005). I3 INDETERMINATE: no whole-level property beyond ARCH-01's is established; shared participation would only re-describe the inventory. I4 INDETERMINATE for the same external dependencies. Rivals: ARCH-01 with SC-04 and SC-06 peripheral; several independent architectures coupled only by shared actors. **Outcome: INDETERMINATE**; a DISTINGUISHABLE outcome is not asserted because coverage is not sufficient while constitutive external references are unresolved (RGAM-DR-25).

Instrument-level result: **INDETERMINATE**; highest level reached **S**. The reading of RGAM-DR-25 that makes every candidate touched by a constitutive external reference INDETERMINATE is logged (DEV-11, UNC-034) and queued (HQ-016). No INTEGRATED or OVERLAPPING outcome was asserted, so no HQ-INTEGRATION/HQ-OVERLAP item is required. No architecture is forced; no score or threshold is used.

## 5. Property register summary (scale, bearer, aggregation)

Fifteen properties, each with exactly one bearer and a stated scale; values are qualitative and per S before any summary; no scalar score, composite or graph index is computed; `property_family` is left blank because the F1–F5 mapping is not in the allow-listed sources (DEV-10, UNC-036, HQ-014).

- Subconfiguration-scale (asserted): functional allocation for SC-01, SC-02 and SC-05 (no property is stated for SC-03 or SC-06); discretion distribution for SC-04 and SC-05; vertical distribution for SC-04 and SC-05; decision-centre plurality for SC-05 (Member State count undetermined, stated multiplicity only); accountability structure for SC-04 (INFO relations only, within the declared corpus; CL-05).
- Undetermined: public-private allocation (SC-01: the character of the CEPT is not stated in W); accountability structure for SC-05 (derived accountability relation with sufficiency indeterminate; HQ-004); necessary stage for the ground (b) Committee opinion (CL-03); substitutability of the Commission request to the CEPT (CL-04); centralization at ARCH-01 scale (no aggregation rule; premature aggregation avoided).
- Not attributable: depth from the rule-making position at ARCH-01 (no legal rule links successive relations as path steps; reachability is not transmission, RGAM-DR-21).

Fallacy checks (atomistic, ecological, premature aggregation) are recorded for every property.

## 6. Status profile

Descriptive tally (no label, no score): 12 positions/devices `documented` (material establishment `not_assessed`); 39 relations: 35 `legal_constitution_evidenced`, 4 `documented`; 20 assignments: 16 `legal_constitution_evidenced`, 4 `documented`; 0 `material_establishment_evidenced` and 0 `exercise_evidenced` (not collected from legal text); 10 external references `not_checked`. The ceiling rule applied (legal_constitution_evidenced where the legal subject is an addressee Member State or a Community institution or organ to which the Directive assigns the task, and no constitutive external reference touches the claim; otherwise documented) is a gap of the frozen documents, logged (DEV-12, UNC-035) and queued (HQ-015). Prohibitions are recorded as constraints (one NA, `constraint_only = Y`), never as relations.

## 7. Closure and external-reference limitations

- CL-01 and CL-02 (COVERAGE): complete search of W, internal cross-references followed, references outside W identified by reading; result ASSERTED_WITHIN_DECLARED_CORPUS. "Not found" is a statement about the search of W only.
- CL-03 (necessity of the Committee stage in the ground (b) route) and CL-04 (substitutability of the request to the CEPT) are UNDETERMINED because of unresolved external dependencies; the corresponding properties are `undetermined`. CL-05 (no answerability/accountability relation in SC-04) and CL-06 (no qualified coupling between SC-04 and SC-05 other than shared participants) are asserted within the declared corpus only; absence of an edge does not establish separation.
- Ten EXT records, all `not_checked` and `outside_corpus_not_expanded`; four carry a constitutive dependency (EXT-005 CEPT Memorandum of Understanding on NETs; EXT-006 CEPT accreditation system; EXT-009 Article 9 of Directive 73/23/EEC; EXT-010 non-prejudice clause for Directive 83/189/EEC). Relations contained in external sources do not enter any subconfiguration or architecture. No external retrieval was performed (GAP-04).

## 8. Open human-review items

Nineteen HQ items, all open, none adjudicated; every `human_*` column is blank: HQ-NORMTYPE (HQ-001 Committee establishment wording; HQ-002 compound wording of A7(3)); HQ-DEV (HQ-003 accreditation system); HQ-ACCOUNT (HQ-004 Article 8 procedure); HQ-XREF (HQ-005 A6(3) subparagraph 2; HQ-006 counterparty of recognition; HQ-007 A8(5) procedures; HQ-008 identity of published lists); HQ-DIRECTION (HQ-009 transmitters of lists and information; HQ-010 passive and trigger-stated relations); HQ-GAP (HQ-011 GAP-07 definition-derived relations; HQ-012 GAP-01 formal units; HQ-013 GAP-05 function vocabulary; HQ-014 family mapping; HQ-016 reading of RGAM-DR-25); HQ-EXTDEP (HQ-017); HQ-OTHER (HQ-015 status ceiling and temporal reference; HQ-018 non-addressee obligations of the CEPT; HQ-019 residual relation-type fit).

## 9. Deviations and gaps

Fifteen entries in PROTOCOL_DEVIATION_LOG: identifier extensions for source structures (DEV-01, GAP-01); handling of headings, separator and merged source paragraphs (DEV-02); GAP-01 formal units (DEV-03); adoption-procedure citations not coded as EXT (DEV-04); GAP-03 internal cross-references (DEV-05); GAP-04 no retrieval (DEV-06); GAP-05 function vocabulary, token `FUNCTION_VOCABULARY_UNRESOLVED` for assistance by experts and for financial settlement (DEV-07); GAP-06 `NON_OPERATIVE_SOURCE_GAP` (DEV-08); GAP-07 definition-derived relations (DEV-09); family mapping unavailable (DEV-10); reading of RGAM-DR-25 (DEV-11); status ceiling for a directive (DEV-12); span from one cited unit (DEV-13); trace selection procedure details (DEV-14); the recovery run and its corrections (DEV-15). GAP-02 (provisions amending other acts) did not arise: W contains no such provision.

## 10. Statement of provisional status

All records are machine-generated and provisional; repetition by the same model is not inter-coder reliability. No human adjudication was performed or simulated. The result stops at the highest level the evidence authorizes (S) with the instrument-level result INDETERMINATE; D (strategies, logics) and X (implementation, operation, outcomes) are not coded. This report contains no comparison with any other method or case, no ranking, no score and no index.
