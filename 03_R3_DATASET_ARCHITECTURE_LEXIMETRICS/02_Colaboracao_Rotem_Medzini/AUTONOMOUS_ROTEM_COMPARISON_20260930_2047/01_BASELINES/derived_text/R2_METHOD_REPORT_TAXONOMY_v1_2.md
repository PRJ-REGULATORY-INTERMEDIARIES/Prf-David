<!-- DERIVED TEXT — not an original. SOURCE_ID=SRC-R2-REPORT; source=C:/Users/Adm/Downloads/R2_METHOD_REPORT_TAXONOMY_CALIBRATION_v1_2.docx; SHA256=FD9421045577E856F217F52E37EDC2A3973047309ED45E724F2484ACD30E28AF; SOURCE_STATUS=HISTORICAL; transformation=python-docx paragraph+table extraction in document order, paragraph numbering [¶n] added by this run; extracted_at=2026-09-30T20:51:56-03:00 -->

[¶1] R2 Methodological Calibration Report

[¶2] Regulatory intermediation coding — EU Taxonomy Regulation (Regulation (EU) 2020/852)

[¶3] Status: ready for human adjudication of conceptual threshold cases

[¶4 TABLE]
| Workbook output | R2_calibration_regulatory_intermediation_v1_2_audited.xlsx |
|---|---|
| Pilot case | CASE_01 — EU Taxonomy Regulation — CELEX 32020R0852 |
| Corpus status | Independent calibration case; outside the five substantive R2 cases |
| Method | Theory-informed qualitative content analysis with directed coding and emergent-code allowance |
| Version | v1.2 |

## [¶5] Executive summary

[¶6] Purpose. This report documents the methodological construction, audit, correction and first relational reconstruction of the calibration workbook used to operationalise regulatory intermediation before application to the five-case R2 corpus.

[¶7] Current result. The pilot now contains 27/27 articles screened, 41 atomic textual coding units and 40 relation candidates. A new RIT-eligibility gate separates genuinely regulator–target relations from scope clauses, institutional design, public transparency, inter-authority coordination and object-only rules. The current reconstruction identifies 28 RIT-eligible relations, 10 non-RIT relations and 2 eligibility-uncertain relations. Five relations presently support intermediation, seven are direct, and eighteen remain deliberately uncertain pending human adjudication.

[¶8] Main methodological gain. The workbook no longer equates “third actor” with “intermediary”. Coding now proceeds through a controlled sequence: exact text → actors → action → function → RIT eligibility → relation → R/I/T roles → intermediation → mechanism/orientation/force. R, I and T are restricted to actors or actor classes; regulatory objects are stored separately.

[¶9 TABLE]
| Indicator | v1.2 status | Interpretation |
|---|---|---|
| Articles screened | 27 / 27 | Complete article-level screening of the pilot act |
| Atomic units | 41 | 22 original descriptive units + 19 text-completion units |
| Relation candidates | 40 | All 21 legacy relations re-adjudicated plus 19 new relation candidates |
| RIT eligible | 28 YES / 10 NO / 2 UNCERTAIN | Eligibility is now evaluated before relation type |
| Intermediation status | 5 YES / 18 UNCERTAIN | Uncertain cases are intentionally preserved |
| Direct relations | 7 | Only among RIT-eligible relations |
| Human-review queue | 18 | Conceptual threshold cases in REVIEW_LOG |
| Open code decisions | 3 | D004, D005 and D019 |

## [¶10] 1. Research-design logic

[¶11] The pilot was intentionally separated from the five-case R2 substantive corpus. Regulation (EU) 2020/852 was used as an independent methodological calibration case because it combines classification criteria, disclosure duties, delegated rulemaking, expert bodies, supervisory authorities, monitoring and advisory structures. This makes it sufficiently complex to stress-test the coding protocol without training the instrument on the cases intended for substantive analysis.

[¶12] The method is best described as theory-informed or directed qualitative content analysis. The coding starts with theoretical categories derived from the regulatory-intermediation framework and the recent Levi-Faur agenda, while preserving an EMERGENT mechanism for phenomena not adequately represented in the initial codebook. The method is therefore neither purely deductive nor purely inductive.

## [¶13] 2. Stages completed

### [¶14] Stage 1 — Case registration and source control

[¶15] The EU Taxonomy Regulation (CELEX 32020R0852) was registered as CASE_01, with the official EUR-Lex ELI preserved as source. The case was explicitly marked as a calibration pilot and excluded from the five-case R2 substantive corpus.

### [¶16] Stage 2 — Article-by-article screening

[¶17] All 27 operative articles were screened. ARTICLE_SCREENING records article role, whether the article is actor-bearing, whether atomic coding was initially performed, and the reason for inclusion, exclusion or deferral. This separates corpus coverage from coding density.

### [¶18] Stage 3 — Atomic descriptive coding

[¶19] The first descriptive pass produced 22 atomic units. Each unit preserved exact text and coded actor(s), action, object, counterpart, modality, output, primary/secondary descriptors, function, evidence level, confidence and analytical memo. R/I/T assignment was deliberately deferred.

### [¶20] Stage 4 — Independent workbook audit

[¶21] The coding instrument was audited inside Excel using a separate model as an auditor rather than as a second primary coder. The audit catalogued 26 findings across theory, codebook/list consistency, descriptive quality, relational readiness and protocol governance. Findings were given researcher-decision and rationale fields rather than being silently auto-corrected.

### [¶22] Stage 5 — Codebook stabilization

[¶23] Audit adjudication produced permanent rules: actor position alone is insufficient for intermediary status; R/I/T are assigned only after descriptive/function coding; action, function and mechanism are distinct layers; orientation is relational; duty force and output force are distinct; reporting/advice/assessment require an explicit relational gate; Primary_Code is controlled while Secondary_Code remains descriptive.

### [¶24] Stage 6 — Detection of a coverage bias

[¶25] A methodological review of the first relational pass showed that the most intermediation-relevant provisions had not yet been atomically extracted: Articles 10–15 contained mandatory Platform consultation clauses and Article 20(2) contained the Platform’s statutory tasks. Proceeding without these provisions risked structurally misclassifying the Platform.

### [¶26] Stage 7 — Text-completion gate

[¶27] Nineteen additional atomic units were added before finalising the relational pass: six mandatory Platform-consultation clauses (Articles 10–15), twelve atomic units covering Article 20(2)(a)–(k), with monitoring and reporting separated within Article 20(2)(e), and Article 24(2) on Commission–Member State exchange through Expert Group meetings. The descriptive corpus therefore increased from 22 to 41 units.

### [¶28] Stage 8 — Introduction of RIT eligibility

[¶29] A new RIT_Eligible variable was inserted before Relation_Type. This prevents a false inference that every non-intermediated legal relation is DIRECT. Scope clauses, institutional creation, public transparency, inter-authority exchanges and relations involving only regulatory objects can now be coded NO without forcing an R–T classification.

### [¶30] Stage 9 — Separation of actors from regulatory objects

[¶31] Regulator, Intermediary and Target are now restricted to actors or actor classes. Technical screening criteria, delegated acts, economic activities, disclosures and compliance requirements are stored in Regulatory_Object. This corrects the previous use of non-actors in Target fields.

### [¶32] Stage 10 — Legal-force refinement

[¶33] Duty_Bearer was introduced to identify which actor actually bears the legal shall/may/must. Duty_Force records whether that actor must act; Output_Force records whether the recipient must follow, must consider, or is not legally bound by the output. This corrects cases where a duty on the Commission to consult was previously treated as a duty on an expert body, and cases where “shall advise” was over-read as “must consider”.

### [¶34] Stage 11 — Relational reconstruction

[¶35] All 21 legacy relation rows were re-adjudicated under the new gates and canonical source IDs. Nineteen relation candidates derived from the text-completion units were then added. The master now contains 40 auditable relation candidates with explicit RIT eligibility, actor roles, regulatory object, intermediation basis, mechanism, orientation, force and episode ID.

### [¶36] Stage 12 — Human adjudication queue

[¶37] Eighteen unresolved conceptual cases were moved into REVIEW_LOG rather than forced into binary classifications. These cases concentrate the questions that matter theoretically: mandatory consultation with non-binding advice, expertise as intermediation, mixed stakeholder populations, and regulator-facing assessment inferred from institutional architecture.

## [¶38] 3. Current coding architecture

[¶39] Core sequence: TEXT → ACTOR(S) → ACTION → FUNCTION → RIT_ELIGIBILITY → RELATION → R/I/T → INTERMEDIATION → MECHANISM → ORIENTATION → FORCE → EPISODE.

[¶40 TABLE]
| Layer | Question answered | Examples |
|---|---|---|
| Text | What is the exact legal evidence? | Article/paragraph + verbatim normative fragment |
| Action | What does the actor legally do? | advise, consult, monitor, report, disclose |
| Function | What regulatory function does that action perform? | ADVICE, MONITORING, REPORTING, ASSESSMENT |
| RIT eligibility | Is this an actor-based regulator–target relation? | YES / NO / UNCERTAIN |
| R/I/T roles | Which actors occupy regulator, intermediary and target roles in this relation? | Commission / Platform / FMP |
| Regulatory object | What is being governed? | technical screening criteria; disclosures; safeguards |
| Mechanism | Through what institutional mechanism is mediation produced? | ADVISORY, MONITORING, REPORTING, ASSESSMENT |
| Orientation | Which side of the relation does the intermediary primarily face? | REGULATOR_FACING / TARGET_FACING |
| Force | Who must act, and how binding is the output? | Duty_Bearer + Duty_Force + Output_Force |
| Episode | Which rows belong to one multi-step intermediation chain? | EP-CASE01-REQUESTS; EP-CASE01-CAPITALFLOWS |

## [¶41] 4. Calibration examples and why they matter

[¶42] Direct disclosure: Articles 5–8. Financial market participants and undertakings bear disclosure duties themselves. Investors and public users receive information, but reception of a disclosure does not make them regulatory intermediaries. These relations are RIT-eligible and DIRECT.

[¶43] Target-facing monitoring: Article 21(1). Member States must ensure that competent authorities monitor financial-market-participant compliance. In the higher-order relation, competent authorities can be coded as target-facing intermediaries even though the same authorities may act as regulators in other relations. This demonstrates that R/I/T roles are relation-specific, not permanent actor attributes.

[¶44] Bottom-up request processing: Articles 20(6) + 20(2)(c). Financial market participants may inform the Platform that an activity should qualify as environmentally sustainable. The Platform must assist the Commission in analysing stakeholder requests. Taken together, these provisions create a comparatively strong T→I→R episode because the intermediary transforms target-side input before it reaches the regulator.

[¶45] Monitoring and reporting: Article 20(2)(e). The Platform must monitor capital-flow trends and regularly report them to the Commission. This is coded as regulator-facing intermediation because monitoring and reporting are explicit, linked functions; reporting is not treated as intermediation merely because a report exists.

[¶46] Mandatory consultation with non-binding advice: Articles 10–15. The Commission must consult the Platform before adopting delegated acts on screening criteria. The process is mandatory, but the substantive advice is not legally binding. These cases are kept UNCERTAIN to test whether mandatory procedural embedding is sufficient for intermediation.

[¶47] Member State Expert Group: Articles 23(4), 24(1), 24(2). The Group has a formal advisory role, but Article 24(2) also shows it serving as a forum through which the Commission informs Member States and facilitates exchange. This is a useful negative/threshold case: being a venue or expert body is not by itself enough to establish intermediation.

## [¶48] 5. Corrections made after the audit

[¶49 TABLE]
| Problem in earlier pass | v1.2 correction | Methodological effect |
|---|---|---|
| Relation_Type used before establishing an R–T relation | Added RIT_Eligible gate | Prevents scope/institutional relations from being mislabeled DIRECT |
| Technical criteria / delegated acts appeared as Target | Added Regulatory_Object; R/I/T restricted to actors | Removes actor/object category error |
| Short Source_Unit_ID (U###) | Replaced with full canonical Unit_ID | Preserves traceability when cases are merged |
| Duty_Force implicitly attributed to intermediary | Added Duty_Bearer | Separates who is legally required to act from who occupies I |
| “shall advise” treated as MUST_CONSIDER | Changed to NON_BINDING or UNCERTAIN unless recipient consideration is explicit | Avoids overstating legal effect |
| Platform classified from incomplete Article 20 extraction | Added full Article 20(2) task architecture and Articles 10–15 consultation clauses | Reduces structural coverage bias |
| Every multi-actor relation treated as candidate RIT | RIT_Eligible=NO allowed | Keeps inter-authority or public-transparency relations visible without forcing RIT |

## [¶50] 6. Current empirical state of the pilot

[¶51] The figures below are calibration outputs, not substantive findings for publication. They remain conditional on human adjudication of the 18 threshold cases.

[¶52 TABLE]
| Dimension | Count | Notes |
|---|---|---|
| RIT_Eligible = YES | 28 | Actor-based regulator–target architecture supported |
| RIT_Eligible = NO | 10 | Scope, institutional, public or inter-authority relations outside RIT |
| RIT_Eligible = UNCERTAIN | 2 | Eligibility itself needs adjudication |
| Relation_Type = DIRECT | 7 | RIT-eligible direct relations |
| Intermediation_Status = YES | 5 | Strongest supported intermediary episodes |
| Intermediation_Status = UNCERTAIN | 18 | Mostly advisory/expertise threshold cases |
| Open human-review items | 18 | Recorded in REVIEW_LOG |
| Open methodological decisions | 3 | D004, D005 and D019 |

## [¶53] 7. Questions intentionally left unresolved

[¶54] • Does mandatory consultation with a non-binding output constitute regulatory intermediation, or is a stronger transformation/implementation role required?

[¶55] • When does institutionalized expertise/advice become intermediation rather than consultation internal to the regulator’s own decision process?

[¶56] • How should mixed stakeholder categories be treated when only some members of the category are regulatory targets?

[¶57] • When is regulator-facing assessment sufficiently connected to targets if the target link is architectural rather than named in the same clause?

[¶58] • Should SCOPE_ACTOR_DELIMITATION and SUBSTANTIVE_COMPLIANCE remain function codes, be promoted to separate descriptive categories, or be removed from the function ontology?

## [¶59] 8. Scientific safeguards now embedded in the workbook

[¶60] • Exact legal text is preserved separately from interpretation.

[¶61] • Descriptive coding precedes R/I/T assignment, reducing anchoring.

[¶62] • Intermediary status is functional and relational, not nominal or positional.

[¶63] • R/I/T roles are relation-specific; the same actor may occupy different roles in different relations.

[¶64] • Evidence level and coder confidence remain distinct dimensions.

[¶65] • Uncertainty is represented explicitly rather than forced into binary categories.

[¶66] • All codebook changes are logged and versioned in CODE_DECISIONS.

[¶67] • Canonical identifiers preserve provenance from relation to source unit.

[¶68] • Audit and substantive coding are separated: the auditor identifies inconsistencies; the researcher adjudicates conceptual choices.

## [¶69] 9. Limitations of the calibration

[¶70] This is a single-act calibration exercise. It establishes internal consistency and stress-tests the coding logic but does not yet demonstrate cross-case reliability. The Taxonomy Regulation is also unusually rich in formal expert/advisory architecture; the codebook must still be tested on acts where intermediation is less explicit, more target-facing, or located across instruments. Articles whose relevance depends primarily on cross-instrument amendments remain outside the completed calibration pass unless needed for a specific RIT episode. No inter-coder reliability statistic should be reported until a stable codebook is applied independently to a common sample.

## [¶71] 10. Recommended next step

[¶72] Do not add another substantive R2 case yet. First, adjudicate the 18 REVIEW_LOG items, with particular attention to D019 (mandatory consultation / advice threshold). Resolve D004 and D005, freeze the resulting codebook as the first transferable version, and then run a small blind replication on a second independent calibration act. Only after that replication should the codebook be applied to the five-case R2 corpus.

## [¶73] Appendix A — Version/provenance record

[¶74 TABLE]
| Version | Main change |
|---|---|
| v0.1 | Base workbook architecture and initial codebook |
| v0.2 | 27-article screening + 22-unit descriptive coding |
| v0.3 | Audit corrections and relation-type reconciliation |
| v1.0 | Action/function/mechanism ontology; orientation; duty/output force; controlled Primary_Code |
| v1.2 | Text-completion gate; RIT eligibility; actor/object separation; Duty_Bearer; canonical IDs; complete re-adjudication of 21 legacy relations; 18-item human review queue |

[¶75] Primary legal source: EUR-Lex, Regulation (EU) 2020/852, ELI: https://eur-lex.europa.eu/eli/reg/2020/852/oj/eng

[¶76] Theoretical anchor used in the project: David Levi-Faur, Rabat conference outline on greenwashing, regulatory intermediation, enhanced self-regulation, polycentric governance and trust regimes; project RIT coding notes and decisions.

## [¶77] Appendix B — Short English methodological abstract

[¶78] Methodological abstract. An independent EU Taxonomy Regulation pilot was used to calibrate a theory-informed qualitative content-analysis protocol for regulatory intermediation before application to the five-case R2 corpus. The workflow separates textual evidence, actions, functions and relational mechanisms; applies an RIT-eligibility gate before classifying relations; restricts regulator, intermediary and target roles to actors or actor classes; records regulatory objects separately; and distinguishes duty force from output force. Following an independent spreadsheet audit, the descriptive corpus was expanded from 22 to 41 atomic units to include the Platform on Sustainable Finance’s statutory tasks and mandatory consultation clauses. Forty relation candidates were reconstructed, while 18 advice/expertise threshold cases were deliberately retained for human adjudication. The calibration therefore prioritizes traceability and explicit uncertainty over premature binary classification.
