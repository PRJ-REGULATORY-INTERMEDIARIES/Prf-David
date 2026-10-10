<!-- DERIVED TEXT — not an original. SOURCE_ID=SRC-R1-REPORT; source=C:/Users/Adm/Downloads/EU_green_regulatory_intermediation_method_progress_report_REVISED.docx; SHA256=A4472478F951E0D9D87FF2FCD50AE5B27907E9E12D1CCF4771ECD38BCCD9FB78; SOURCE_STATUS=HISTORICAL; transformation=python-docx paragraph+table extraction in document order, paragraph numbering [¶n] added by this run; extracted_at=2026-09-30T20:51:55-03:00 -->

[¶1] From a Broad Legal Inventory
to a Five-Case Calibration Corpus

[¶2] Methodological progress report for the study of regulatory intermediation in EU green regulation

[¶3] Prepared by Igor Caires Machado
For discussion with Prof. David Levi-Faur
13 September 2026

[¶4] Purpose: to explain, in plain language and with an explicit audit trail, how the project moved from an exploratory legal inventory to a bounded EU-level working population and a provisional five-case corpus — including how data were collected, queried, normalized, reconciled and legally validated — before any substantive coding of regulatory intermediation.

## [¶5] Executive overview

[¶6] After our recent discussion, I understood that the immediate problem was not to identify more intermediaries, but to establish a defensible population of laws and to clarify the analytical levels before coding. I therefore paused substantive interpretation and treated population construction as a separate research task.

[¶7] The work proceeded in stages. I first reconstructed the architecture of the digital-governance dataset that you and Rotem shared with me. That exercise was important because the supplied codebook already distinguishes the regulatory instrument from intermediary observations, while the workbook itself contains several sheets that represent different stages and units of analysis. Rather than copying the structure, I tried to understand what was conceptually stable and what remained under development.

[¶8] I then explored the available landscape of climate and environmental policy sources. That broader search produced a large national-level discovery inventory, but it also showed why volume alone is not useful: many records were policy measures rather than clearly identified binding legal acts. I therefore separated the national work from the EU-level work instead of forcing them into a single population. The revised report now documents that collection more explicitly, including the acquisition sequence, reconciliation rules, thematic query families, CELEX retrieval pattern and the operational filters used to move from discovery records to canonical legal acts.

[¶9] For the EU-level component, I built and tested an acquisition route using CELEX/EUR-Lex/CELLAR identifiers, separated legal acts from consolidated expressions, and constructed a canonical set of legal identities. The current result is a working population of 35 EU-level binding basic acts drawn from the validated climate and broad-environment frames. This is a pilot population, not a claim that every possible piece of EU green regulation has already been captured.

[¶10] From that population, a five-case calibration sample was generated using temporal and substantive variation rather than the known presence of intermediaries. Official EUR-Lex texts were recovered for all five selected CELEX records. No actor, intermediary, mechanism, flow, R-I-T relation, prevalence estimate or historical trend has yet been coded. The project is therefore still positioned before the substantive interpretation stage.

[¶11 TABLE]
| In one sentence / The main methodological achievement so far is separation: population selection, legal identity, text retrieval and regulatory-intermediation coding are being treated as different research problems rather than collapsed into one operation. |
|---|

### [¶12] A brief map of the work completed

## [¶13] 1. Why I paused before coding intermediaries

[¶14] The first iterations of the project moved quickly from legal texts to possible Regulator–Intermediary–Target (R-I-T) configurations. That was useful for learning, but it also exposed a methodological risk: if I selected laws because they already looked rich in intermediation, the eventual dataset would be biased toward the phenomenon I wanted to study.

[¶15] The safer sequence is the opposite. First define the population independently of intermediary-related outcomes. Then select cases by ex ante legal, temporal and substantive characteristics. Only after the cases are fixed should we ask which actors appear, what they do, which regulatory mechanisms are present, and whether a relational configuration qualifies as regulatory intermediation.

[¶16] This change of sequence is why the work described here may look more like data infrastructure than substantive regulatory analysis. The infrastructure is serving a narrow purpose: to make later interpretation more credible and reproducible.

## [¶17] 2. Starting from the David–Rotem digital-governance materials

[¶18] The materials you sent with Rotem became the methodological starting point for this stage: the main Excel workbook, the Codebook for Regulatory Intermediation in European Digital Governance, and the Chart Key. I treated them as working research materials, not as a finished template to reproduce mechanically.

[¶19] The codebook describes a two-stage logic. The regulatory instrument is coded first; each intermediary identified within an instrument is then intended to become a separate observation. It also organizes the project around three analytical purposes: historical/institutional mapping, governance analysis, and institutional variation among intermediaries. The Chart Key reinforces this structure and lists functions such as rule-setting, assurance, monitoring, internal compliance, dispute redress, complaint handling, auditing, insurance/risk underwriting and enforcement.

[¶20] This architecture was especially useful because it suggested that the instrument and the intermediary should not be forced into the same unit of observation. At the same time, the workbook showed that the empirical implementation is still evolving: some sheets operate at instrument level, others at actor/intermediary level, and some rows aggregate several actors or arrangements in one cell.

[¶21 TABLE]
| Source note / This section is grounded in the working Codebook and Chart Key supplied by David/Rotem. In particular, the Codebook describes the two-stage coding logic and the three analytical purposes, while the Chart Key summarizes the intermediary functions and additional dimensions such as recognition pathway and obligation intensity. |
|---|

## [¶22] 3. Reconstructing the original workbook before adapting it

[¶23] I first audited the workbook sheet by sheet. The purpose was not to clean it, but to understand the empirical pipeline that already existed.

[¶24 TABLE]
| Workbook component | Observed size | Interpretive role |
|---|---|---|
| Fuller list of EU legislations | 205 non-empty records; 189 distinct references | Broadest legislative inventory in the workbook |
| Overview of EU legislation | 101 references | Selected overview; all correspond to the Fuller list |
| Coding Digital Intermediaries | 111 filled rows; 106 distinct codes | Main coding sheet, mainly instrument-level |
| List of intermediaries | 13 observations | Small intermediary-level pilot |
| List of actors | 35 observations | More developed actor/arrangement-level restructuring |
| List of unused | 12 entries | Excluded/unused material; unstable header structure |

[¶25] I then reconstructed the selection funnel across sheets and reconciled identifiers. The first deterministic pass showed many apparent mismatches, so I added a conservative normalization audit rather than assuming that every unmatched code represented a genuinely different law. The reconciliation ultimately produced 53 exact matches, 10 additional normalized matches, 3 probable matches, 18 apparently external cases and 22 unresolved cases.

[¶26] The important conclusion was negative but useful: the workbook does not allow me to recover a clear substantive rule explaining why every law entered or left the coding set. That means I should not simply use the digital-governance selection process as an undocumented model for the green-regulation project.

## [¶27] 4. Why population construction became a separate workstream

[¶28] Once the selection rule could not be reconstructed confidently from the digital workbook, I treated population construction as an explicit research problem. In plain terms, I needed a list of eligible laws from which cases could be selected without looking first at whether they contain intermediaries.

[¶29] A sampling frame is simply that list. It does not yet tell us which cases are theoretically interesting; it gives us a transparent denominator and makes it possible to explain why a case was eligible before we know its intermediation outcome.

[¶30] I therefore created a separate population-discovery workstream with source registries, raw-source preservation, normalization, deduplication, crosswalks, provenance traces, reproducibility tests and decision gates. These are safeguards, not ends in themselves.

## [¶31] 5. The broad multi-source discovery exercise — and why I did not use it as the final population

[¶32] The exploratory search registered 35 sources, including EEA Policies and Measures, OECD IFCMA, Climate Change Laws of the World, IEA policies, OECD PINE, OECD CAPMF, EUR-Lex/CELLAR, N-Lex and national portals for the EU-27.

[¶33 TABLE]
| Discovery result | Value |
|---|---|
| Raw record-equivalents | 9,383 |
| Normalized records | 9,478 |
| Master instruments | 4,010 |
| Source-trace rows | 7,016 |
| Deterministic matches | 3,006 |
| Unresolved fuzzy candidates | 194 |
| Member States represented | 27 |
| EU-level instruments in this master | 0 |

[¶34] This was informative, but it did not produce a legal population that could be used directly. The master was dominated by national policy measures from the EEA and OECD sources. Binding legal status was not explicitly confirmed, official texts were not yet resolved, and EU-level legislation was absent.

[¶35] Rather than relabel a policy inventory as a population of regulations, I froze this branch as a discovery asset. This was an important methodological decision: the large number of records was not treated as evidence of a valid legal population.

## [¶36] 6. How the population was actually built: acquisition, harmonisation and legal validation

[¶37] The previous sections explain why population construction became a separate methodological problem. This section makes the operational side explicit: where the records came from, what was done to them, which criteria were applied, and how the project moved from broad discovery records to a bounded EU-level legal population. The sequence is important because data collection, legal identification and substantive selection were treated as different tasks rather than collapsed into a single search.

### [¶38] 6.1 Source discovery before legal selection

[¶39] The first collection step was deliberately broad. I registered 35 potential sources rather than assuming that one database could represent the universe of green-transition regulation. The registry included European and international policy databases, EU institutional sources and national portals. Among the principal sources were EEA Policies and Measures, OECD IFCMA, Climate Change Laws of the World, IEA policy sources, OECD PINE, OECD CAPMF, EUR-Lex/CELLAR, N-Lex, and portals covering the 27 EU Member States. At this stage, the goal was discovery: a record found in a policy database was not automatically treated as a law.

### [¶40] 6.2 Raw records were preserved before transformation

[¶41] The acquired source material was preserved in a raw layer before any harmonisation. The workflow then separated source records from normalized records, candidate instruments and canonical legal acts. This was done so that every later transformation could be traced back to the source as received. The broad acquisition produced 9,383 raw record-equivalents. Source-specific normalization yielded 9,478 normalized records. The increase was retained and documented rather than retrospectively forced to match the raw count, because normalization can restructure or expand source records.

### [¶42] 6.3 Normalization was technical, not substantive

[¶43] Normalization aligned fields such as title, date, jurisdiction, source identifier and available instrument descriptors. Original values were retained alongside normalized values. This stage did not identify regulators, intermediaries or targets, and it did not use intermediary-related terminology to determine whether a record belonged in the population.

### [¶44] 6.4 Cross-source reconciliation and deduplication

[¶45] Because the same measure can appear in several databases, source records were reconciled before they were counted as candidate instruments. Stable identifiers and deterministic matches were preferred. Fuzzy similarity was used only to flag possible matches for review, not to merge records silently. The process produced 7,016 source-trace rows, 3,006 deterministic matches and 194 unresolved fuzzy candidates. The resulting discovery master contained 4,010 candidate instruments.

[¶46] The operational funnel up to this point can be read as follows:

[¶47 TABLE]
| Operational layer | Observed result | Interpretation |
|---|---|---|
| Registered sources | 35 sources | Discovery universe; not yet a legal population |
| Raw acquisition | 9,383 record-equivalents | Source material as collected |
| Normalized records | 9,478 | Technically harmonised source records |
| Cross-source trace | 7,016 rows | Provenance linking source records to candidate instruments |
| Deterministic matches | 3,006 | High-confidence reconciliations across sources |
| Unresolved fuzzy candidates | 194 | Review candidates; not auto-merged |
| Discovery master | 4,010 instruments | Predominantly Member-State policy measures; not a final legal population |

### [¶48] 6.5 Why the national discovery master was not used as the final population

[¶49] The 4,010-instrument master was useful as a map of available measures, but it was dominated by national policy-oriented sources, especially EEA and OECD IFCMA. At that point, official legal text had not been resolved, binding status had not been systematically verified, and EU-level legislation was absent from the master. Rather than relabel that discovery inventory as a population of regulations, I froze it as a separate asset and created an EU-level acquisition stream.

### [¶50] 6.6 EU-level legal identification and canonicalization

[¶51] The EU-level stream used CELEX as the principal stable identifier and EUR-Lex/CELLAR as the authoritative legal infrastructure. Three known CELEX acts were used as positive controls for the route, not as criteria for population inclusion: 32021R1119, 32023R0956 and 32023R1115. The EU-level process generated 80 CELEX candidates. Legal identity was then canonicalized by distinguishing basic acts from consolidated expressions. Twenty-nine candidates were consolidated expressions; 28 could be mapped to basic acts already represented in the inventory. Collapsing those duplicate legal identities reduced the 80 records to 52 canonical legal acts.

### [¶52] 6.7 Legal eligibility and substantive frame selection

[¶53] Legal and substantive criteria were applied only after canonicalization. The preferred legal rule, Option A, retained binding basic acts and treated consolidated texts as textual versions rather than independent cases. This produced 50 legally eligible canonical acts. The thematic frames were then compared on the level of canonical legal identity. The working population P4 was defined as the union of the valid climate-core and broad-environment frames under Option A, yielding 35 acts. The 2019 breakpoint was retained for analytical stratification, not as an inclusion rule.

### [¶54] 6.8 What was automated, and what remained a research decision

[¶55] Automation supported retrieval, field normalization, identifier matching, crosswalk creation, deduplication, provenance tracking, frame comparison and validation tests. It did not decide the theoretical population. Decisions about separating Member-State and EU-level material, defining one case as one canonical basic act, retaining binding basic acts as the main denominator, choosing the substantive frame, and constructing a five-case calibration sample remained methodological research decisions. In other words, the computational workflow was used to make the research decisions traceable, not to replace them.

## [¶56] 7. Illustrative queries, search strings and operational filters

[¶57] The R1 workflow combined source discovery queries, thematic search terms, legal-identifier rules and later lexical-screening vocabularies. The examples below are included to make the search logic visible. Where an exact stable string or URI pattern is available, it is reproduced directly. Where the original user-facing search log was not preserved verbatim in the available report package, the text is explicitly presented as a reconstructed illustration of the query logic rather than as a literal transcript.

### [¶58] 7.1 Source-discovery queries

[¶59 TABLE]
| "European Union" AND (climate OR environment OR sustainability OR "green transition") / AND (law OR legislation OR regulation OR policy) AND (dataset OR database) / "EU climate policy database" OR "EU climate laws dataset" / "EU environmental legislation dataset" OR "environmental policy instruments Europe" / "EU energy policy instruments" OR "European energy legislation dataset" / "EUR-Lex" AND (climate OR environment OR energy) / AND (Regulation OR Directive OR Decision) |
|---|

[¶60] These strings examples the discovery logic used to identify candidate repositories and official sources. Their purpose was to find datasets and legal infrastructures, not to select acts because they appeared to contain intermediaries.

### [¶61] 7.2 Thematic string families used to build or test frames

[¶62 TABLE]
| CLIMATE FAMILY: / climate \| greenhouse gas \| emissions \| carbon \| climate neutrality \| decarbonisation \| Paris Agreement / BROAD ENVIRONMENT FAMILY: / environment \| environmental \| pollution \| air \| waste \| biodiversity \| nature \| environmental quality / ENERGY FAMILY (query remained unresolved): / energy \| renewable \| efficiency \| electricity \| gas \| Energy Union |
|---|

[¶63] These are thematic families rather than a claim that every listed term appeared in every source query. The important design rule was that thematic framing was independent of intermediary terminology. The unresolved energy route was recorded as QUERY_UNRESOLVED rather than interpreted as evidence that relevant energy legislation did not exist.

### [¶64] 7.3 Exact legal-text retrieval pattern and identifier logic

[¶65 TABLE]
| Official EUR-Lex HTML retrieval template: / https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:{CELEX} / Examples: / .../?uri=CELEX:32018R0842 / .../?uri=CELEX:32021R1119 / .../?uri=CELEX:32023R0955 / Canonicalization rule: / basic-act CELEX -> legal case identity / consolidated CELEX expression (commonly beginning with 0) -> textual version, not a second case |
|---|

### [¶66] 7.4 Operational filtering logic used after acquisition

[¶67 TABLE]
| OPTION A: / binding basic acts only / P4 WORKING POPULATION: / (climate_core UNION broad_environment) INTERSECT Option_A / TEMPORAL VARIABLE: / pre_2019 versus 2019_plus = analytical stratification, not eligibility / DEDUPLICATION PRINCIPLE: / stable identifier > normalized exact match > multi-attribute probable match > fuzzy candidate for review |
|---|

### [¶68] 7.5 Strings deliberately excluded from population selection

[¶69 TABLE]
| report* \| monitor* \| verif* \| certif* \| audit* \| supervis* / assess* \| accredit* \| designat* \| notif* \| enforc* \| delegat* \| coordinat* / standard* \| compliance \| assurance \| complaint \| dispute \| inspection |
|---|

[¶70] These terms are potentially useful for later lexical screening of regulatory functions and intermediary candidates, but they were deliberately not used to define the legal population. Using them as inclusion criteria would enrich the corpus for the very phenomenon the study later seeks to observe and would create selection bias. A keyword hit is therefore treated as a candidate signal, not as evidence of regulatory intermediation.

## [¶71] 8. Building an EU-level component separately

[¶72] I then created an isolated EU-level acquisition workstream. The national master was left unchanged so that the two problems — national policy discovery and EU legal population construction — would not contaminate each other.

[¶73] The EU-level route was tested through official EUR-Lex/CELLAR identifiers using three known CELEX controls. This produced an initial set of 80 unique CELEX candidates. Forty-nine had CELLAR metadata resolved at that stage. The legal-status field indicated 78 binding acts, one non-binding act and one unknown case.

[¶74] Four thematic frames were carried forward: climate core, climate + energy, broad environment, and a green/legal proxy. The energy query returned no CELEX values despite a technically successful request, so I recorded it as QUERY_UNRESOLVED rather than interpreting zero as a substantive absence of energy legislation.

[¶75 TABLE]
| Why this matters / A technical zero and a substantive zero are different claims. Recording an unresolved query as unresolved prevents a software or parameter problem from becoming a false empirical conclusion. |
|---|

## [¶76] 9. Canonicalizing legal identity: a law is not the same thing as a consolidated expression

[¶77] The next problem was legal identity. EUR-Lex may contain both the basic legal act and later consolidated expressions of the same act. If both are counted as independent cases, the population becomes artificially inflated.

[¶78] I therefore treated the basic act as the case identity and the consolidated expression as a textual version that may be used for substantive reading. This distinction is analogous to treating different editions of the same book as versions of one work rather than as different books.

[¶79] Among the 80 candidates, 29 were identified as consolidated expressions. Twenty-eight were successfully mapped to basic acts that were already present in the inventory, removing 28 duplicate legal identities. The 80 records therefore collapsed to 52 canonical legal acts. Under the working legal-eligibility rule — Option A, binding basic acts only — 50 remained eligible. One legal-status conflict was preserved as a conflict rather than silently corrected.

[¶80 TABLE]
| Canonicalization step | Result |
|---|---|
| Initial EU candidates | 80 |
| Consolidated expressions identified | 29 |
| Expressions mapped to base acts already present | 28 |
| Canonical legal acts after collapse | 52 |
| Eligible under Option A | 50 |

## [¶81] 10. Defining the working population

[¶82] After canonicalization, the thematic frames could be compared on the level of legal acts rather than document expressions. A notable result was that climate_core and green_legal_proxy became exactly the same set: 26 eligible acts, Jaccard overlap 1.000, with no set differences. The supposed green proxy therefore did not provide an independent frame.

[¶83] The broad_environment frame contributed a smaller, partially distinct set. I therefore retained the union of the valid climate and broad-environment frames as the broadest defensible working option for the pilot. This became P4.

[¶84] P4 contains 35 canonical EU-level binding basic acts. Of these, 21 are pre-2019 and 14 are from 2019 onward. The set includes 5 decisions, 14 directives and 16 regulations. Nine acts are broad-environment-only. The unresolved energy frame remains a limitation and is explicitly documented rather than hidden.

[¶85 TABLE]
| Careful terminology / I would describe P4 as a working population of eligible EU-level binding legal acts identified through the validated climate and environmental frames. I would not yet call it “the complete population of EU green regulation,” because the energy query remains unresolved and broad-environment boundary cases have not all been substantively validated. |
|---|

## [¶86] 11. Moving from 35 acts to a five-case calibration corpus

[¶87] The five-case stage was designed as conceptual calibration, not statistical sampling. The purpose is to create a small set that allows us to discuss definitions and boundary cases before scaling to all 35 acts.

[¶88] Three five-case designs were generated. The recommended design, S2, prioritized temporal variation together with substantive-frame variation. The selection rules did not use previous intermediary findings, intermediary-related keywords, or perceived richness of intermediation. Official English-language EUR-Lex texts were successfully recovered for all five selected CELEX records, and the corpus was locked with provenance information.

[¶89] The current S2 output contains CELEX 32000D0293, 32003L0087, 32018R0842, 32021R1119 and 32023R0955. This set is still formally awaiting researcher approval, and it should be understood as a calibration set rather than a representative sample.

[¶90 TABLE]
| Important quality-control finding before substantive coding / During preparation of this report, I independently re-checked the five CELEX identifiers against EUR-Lex. CELEX 32000D0293 is Decision No 293/2000/EC establishing the Daphne programme on preventive measures to fight violence against children, young persons and women. It is therefore not an obvious climate/environmental act. This does not invalidate the 35-act population work, but it does mean that the five-case S2 sample should not be approved until this item is traced back to the sampling output and either justified or corrected. I would treat this as a useful final semantic sanity check rather than a substantive failure. |
|---|

[¶91] The other four CELEX identifiers correspond to well-established climate-related legal instruments: Directive 2003/87/EC (EU emissions trading), Regulation (EU) 2018/842 (binding annual greenhouse-gas reductions for Member States), Regulation (EU) 2021/1119 (European Climate Law), and Regulation (EU) 2023/955 (Social Climate Fund).

## [¶92] 12. What the project deliberately has not done

[¶93] No actor has yet been coded as a regulator, intermediary or target in the 35-act population.

[¶94] No regulatory mechanism or governance flow has yet been systematically extracted from the pilot corpus.

[¶95] No prevalence estimate has been calculated for regulatory intermediation.

[¶96] No historical trend has been inferred from the 35 acts.

[¶97] No AI output has been treated as ground truth for substantive intermediation.

[¶98] The national discovery inventory has not been merged into the EU-level population.

[¶99] The unresolved energy query has not been converted into a substantive zero.

[¶100] These non-actions are part of the method. They preserve the distinction between constructing a defensible empirical base and interpreting regulatory governance within that base.

## [¶101] 13. What I learned from the David–Rotem architecture

[¶102] The digital-governance materials suggest that the final green-regulation database should probably be multilevel rather than organized around one universal row. The legal instrument is the natural unit for population construction and historical comparison. Actors and intermediary arrangements belong to a lower level. Functions, mechanisms, governance positions and evidence may require additional linked tables.

[¶103] The most useful conceptual lesson is that an intermediary should not be treated simply as an actor type. Intermediation is relational. The same organization can occupy different roles in different regulatory configurations. This is why the next stage should begin with actors, actions, functions, mechanisms and governance positions before a final intermediary classification is imposed.

[¶104] The supplied workbook also contains exploratory concepts such as Position_in_governance_chain and Primary_function_mechanism. These are especially relevant to the discussion we had about regulatory flows, but they should be calibrated rather than imported mechanically into the green domain.

## [¶105] 14. Where the project stands now

[¶106] The population problem is sufficiently bounded for a pilot, subject to two explicit caveats: the energy frame still requires later resolution, and the current five-case sample contains at least one CELEX entry that needs semantic re-checking before approval.

[¶107 TABLE]
| Layer | Current status | What remains |
|---|---|---|
| Population discovery | Completed for current pilot purpose | Energy route to be resolved later |
| EU legal identity | Canonicalized | One preserved legal-status conflict |
| Working population | P4 frozen at 35 acts | Researcher approval / boundary review |
| Five-case corpus | Technically acquired and locked | Semantic validation of sample, especially 32000D0293 |
| Conceptual codebook | Not yet applied to green cases | Next substantive stage |
| Intermediation coding | Not started | Should follow calibration with David |

## [¶108] 15. Proposed next scientific step

[¶109] Once the five-case sample is semantically validated, I propose to use it as a calibration corpus rather than immediately coding all 35 acts. The first pass would identify actors, actions, objects, regulatory functions, mechanisms and positions in the governance chain without asking first who the intermediary is.

[¶110] Only after those elements are reconstructed from the legal text would each episode be discussed as a possible instance of regulatory intermediation. This should produce a small set of difficult boundary cases that we can examine together — for example, reporting without independent judgment, scientific advice that must be considered but is not binding, third-party verification, monitoring, certification, consultation and information transmission.

[¶111] The aim of the next discussion would therefore be conceptual calibration: to decide what minimum conditions turn a third actor, process or arrangement into a regulatory intermediary, and how many distinct flow configurations are theoretically useful. Once those decisions are stable, the coding can scale to the 35-act working population.

## [¶112] 16. Short glossary of the data terms used in this report

[¶113 TABLE]
| Term | Plain-language meaning |
|---|---|
| Sampling frame | The list of eligible cases from which a sample can be drawn. |
| Canonical legal act | The basic legal act treated as the identity of one case. |
| Consolidated expression | A later textual version that incorporates amendments; useful for reading, but not a separate law for case counting. |
| Crosswalk | A table showing how records from different sources refer to the same legal act. |
| Source trace / provenance | A record of where each item came from and how it was transformed. |
| Decision gate | A deliberate stop point where a scientific choice must be approved before the pipeline continues. |
| Calibration sample | A small set used to refine concepts and coding rules; it is not meant to estimate population frequencies. |

## [¶114] Appendix A. Audit trail: stages, decisions and principal outputs

[¶115 TABLE]
| Stage | Scientific purpose | Main evidence/output |
|---|---|---|
| Workbook reconstruction | Understand how the David–Rotem material is actually structured | Workbook architecture note; population-funnel note |
| Identifier reconciliation | Separate real differences from formatting/matching problems | Identifier reconciliation note and crosswalks |
| Conceptual audit | Identify mixed units and conceptual overlaps | Conceptual architecture, governance-flow and codebook audit notes |
| Population discovery | Map available national and EU-related sources without claiming final population | Source registry, population report and coverage report |
| EU-level acquisition | Build a separate official-identifier route | EU-level source registry, normalized inventory and terminal report |
| EU-3 population freeze | Audit the 80 EU candidates and test official-text retrieval | Population-freeze audit and text-resolution diagnostic |
| EU-3.5 canonicalization | Collapse consolidated expressions to base-act identities | Canonical act crosswalk and canonical population |
| EU-4 pilot design | Freeze P4 and generate five-case calibration alternatives | Frozen P4 population, sample recommendation and corpus manifest |

## [¶116] Appendix B. Evidence base used for this report

[¶117] Medzini, Rotem & David Levi-Faur. Codebook: Regulatory Intermediation in European Digital Governance Dataset. Working document supplied for methodological comparison.

[¶118] Chart Key: Regulatory Intermediation in Digital Governance. Working document supplied with the dataset.

[¶119] dataset_of_EU_regulatory_intermediation.xlsx. Working research workbook supplied by David/Rotem.

[¶120] Project-generated audit and population files listed in Appendix A and in the EU-3 / EU-3.5 / EU-4 outputs.

[¶121] Official EUR-Lex legal-text and metadata pages used for CELEX validation and text acquisition.

[¶122] Closing note

[¶123] My intention in documenting the process at this level is not to make the project more technical than necessary. It is the opposite: to make the substantive regulatory analysis easier to trust. Each technical step was introduced only when it answered a specific research problem — what counts as a case, where it came from, whether two records are actually the same law, and why a law was eligible before we know whether it contains intermediation. With that foundation in place, the next stage can return to the central theoretical question with much less ambiguity.
