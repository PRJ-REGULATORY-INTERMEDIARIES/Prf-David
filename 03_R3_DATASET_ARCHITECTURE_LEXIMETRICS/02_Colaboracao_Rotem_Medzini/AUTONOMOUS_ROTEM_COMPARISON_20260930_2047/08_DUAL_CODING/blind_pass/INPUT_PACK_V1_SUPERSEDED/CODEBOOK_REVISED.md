<!-- DERIVED TEXT — not an original. SOURCE_ID=SRC-CB-REV; source=G:/Meu Drive/PRJ-David/Prf-David/RELATIONAL_LEXIMETRICS_PILOT/PILOT_01/00_SOURCES/Codebook_Regulatory_Intermediation_Revised (1).docx; SHA256=7FE634455AEDC0A7ADD0134DDB6DD20735194D8414A549A36DF18F805EED128B; SOURCE_STATUS=REVISED_BY_FILENAME_AND_CONTENT; transformation=python-docx paragraph+table extraction in document order, paragraph numbering [¶n] added by this run; extracted_at=2026-09-30T20:51:55-03:00 -->

[¶1] Codebook for Regulatory Intermediation in European Digital Governance

[¶2] Revised structure integrating act screening, regulatory architecture, regulation by intermediaries, and regulation of intermediaries

[¶3] This codebook documents the construction and interpretation of a historical dataset of regulatory intermediation in European digital governance. It defines the scope of the corpus, the units of observation, the rules governing positive and negative coding decisions, and the variables used to analyze regulatory architectures and strategies over time.

## [¶4] 1 Research Purpose and Analytical Framework

[¶5] The study asks two related questions:

[¶6] 1.  How have the architectures and strategies of digital regulation evolved in the European Union over time, particularly through changing arrangements for the regulation of and by regulatory intermediaries?

[¶7] 2.  How do these architectures and strategies structure European digital regulatory regimes?

[¶8] To investigate these questions empirically, the coding constructs a systematic historical and institutional map of regulatory intermediation. It records the legal and substantive characteristics of each included act, the regulatory objects it governs, its regulatory architecture and strategy, each regulatory intermediary identified within it, the object and functions of intermediation, and the arrangements through which the intermediary is constituted and regulated.

[¶9] The framework distinguishes five analytical questions:

[¶10] who participates, what is regulated, how regulation is institutionally organized, what regulatory functions intermediaries perform, and how those intermediaries are themselves governed. These distinctions separate regulatory objects from regulatory strategies and architectures, functions from mechanisms, and regulation by intermediaries from regulation of intermediaries.

## [¶11] 2 Scope and Act Selection

### [¶12] 2.1 Corpus

[¶13] The dataset covers European Union legislative acts and policy documents that substantively concern digital governance from the 1970s to 2026. This includes acts governing information, data, digital content, communications networks and infrastructure, digital services, platforms, digital technologies, and the economic or organizational activities directly associated with them. The generic term "act" covers both binding legal instruments and non-binding policy documents. Type of Regulatory Instrument records their specific legal or policy form.

### [¶14] 2.2 Act inclusion rule

[¶15] An act is included when digital governance forms a substantive part of its regulatory purpose or operation. Inclusion requires more than an incidental reference to electronic communication, information systems, technical standards, or digital technologies. The assessment concerns the act as a whole, read across the provisions relevant to its regulatory purpose and operation. The mapping also includes acts that establish, constitute, or form an integral part of a regulatory framework substantially governing digital activities.

### [¶16] 2.3 Act exclusion rule

[¶17] An act is excluded when its connection to digital governance is incidental, technical only, or secondary to a different regulatory purpose. Repeal is not an exclusion criterion. A repealed act remains eligible where it forms part of the historical development of European digital governance.

[¶18] Excluded acts are recorded in the separate Excluded_acts list, together with their identifying information, the exclusion decision, the reason for exclusion, and screening notes. They do not appear in ACT_SUMMARY and do not generate observations in INTERMEDIARY_MAP.

[¶19] An included act with no qualifying regulatory intermediary is not excluded. It remains in ACT_SUMMARY and generates a No_intermediary observation in INTERMEDIARY_MAP.

## [¶20] 3 Coding Structure and Units of Observation

[¶21] The dataset contains three connected components:

[¶22 TABLE]
| Component | Unit of observation | Purpose |
|---|---|---|
| Excluded_acts | One record per assessed act excluded from the corpus | Documents the scope boundary and the application of the exclusion criteria. |
| ACT_SUMMARY | One record per included EU act or policy document | Records act identity, scope, regulatory object, architecture, configuration, and strategy. |
| INTERMEDIARY_MAP | One record per qualifying intermediary category identified within an included act, or one No_intermediary record where none is identified. | Records the intermediary, its relational position, regulation by the intermediary, and regulation of the intermediary. |

[¶23] An ‘act’ is the unit of observation in ACT_SUMMARY. The intermediary as legally constituted or recognized within a particular act is the unit of observation in INTERMEDIARY_MAP. Meanwhile, a legal provision is a unit of evidence, not a separate unit of observation. Several provisions may jointly establish the identity, function, position, recognition, or obligations of one intermediary.

[¶24] Where an act identifies several intermediary categories, each category receives a separate record. Each row represents a legally defined category of intermediary participants rather than each individual organization or representative. Separate collective rows are used where the act assigns different roles to different categories of intermediaries.

## [¶25] 4 Regulatory Intermediary Inclusion Rule

[¶26] Following the Regulator–Intermediary–Target model, a regulatory intermediary is an actor or organizational arrangement that performs a regulatory function within or between a regulator, a regulatory target, another intermediary, or regulatory beneficiaries, while contributing its own capacity, authority, expertise, or legitimacy to the regulatory arrangement (Abbott, Levi-Faur, and Snidal 2017).

[¶27] An actor is coded as a regulatory intermediary where the focal act substantively assigns, recognizes, or relies upon that actor to perform at least one identified regulatory function through an identifiable governance mechanism or legally structured arrangement. The actor need not exercise public authority and need not act directly upon the ultimate regulatory target.

[¶28] The intermediary role may be explicit or may follow necessarily from an express legal mechanism. For example, an express requirement that an intermediary maintain liability insurance necessarily relies upon an insurance provider, even where that insurance provider is not individually named. A merely historical, technical, or contextual reference to an external actor is insufficient.

[¶29] An actor is not coded as an intermediary solely because it is mentioned, occupies an organizational position between other actors, possesses relevant expertise, supplies an ordinary commercial service, is itself regulated, or is known from external practice to perform a regulatory role.

[¶30] A regulated entity is also coded as an intermediary only where the act assigns it a regulatory function in relation to another actor, such as monitoring, assurance, complaint handling, enforcement, or rights protection. Compliance with duties imposed upon the entity itself does not constitute intermediation.

[¶31] Public authorities exercising public regulatory powers are coded as regulators rather than intermediaries. An intermediary may nevertheless be secondary, meaning that it performs a regulatory function in relation to another intermediary. European and national standardization bodies are not coded as regulatory intermediaries under the operational boundary adopted for this project. Their involvement may be described at act level where relevant.

## [¶32] 5 Evidence and Restrictive Positive Coding Rules

### [¶33] 5.1 Evidentiary basis

[¶34] Coding is based on the official text of the focal act. Operative provisions and binding annexes provide the primary basis for coding. Recitals may support interpretation but do not ordinarily provide sufficient evidence for a positive coding decision by themselves. For policy documents that are not structured as binding legislation, explicit sections assigning roles, functions, expectations, or governance arrangements provide the relevant evidence.

[¶35] A cross-reference may support coding where the focal act expressly incorporates, applies, or extends provisions from another act. A technical, historical, or incidental citation does not independently establish an intermediary or a positive variable value.

[¶36] Evidence may be distributed across several provisions. One provision may identify the actor, another may assign a function, and an annex may specify the applicable obligations. Relevant provision(s) must identify all provisions needed to support the row.

### [¶37] 5.2 Restrictive rule for regulatory_object

[¶38] Code only an object that constitutes an express and substantial subject of the act. Do not code every ancillary procedure, implementation arrangement, institutional safeguard, general purpose, or legal consequence as an additional regulatory object.

### [¶39] 5.3 Restrictive rule for intermediary_object

[¶40] Code only the object upon which the intermediary directly acts through the function assigned to it. Do not code the procedure used, the broader sector in which it operates, the intended beneficiary, or a remote legal consequence unless the intermediary directly governs that object.

### [¶41] 5.4 Rules for functions, strategies, and obligations

[¶42] A function receives Yes only where the function is assigned to the intermediary itself.

[¶43] An obligation receives Yes only where the obligation is imposed upon the intermediary itself. A duty imposed solely on a public authority to approve, supervise, notify, or control the intermediary is not an intermediary obligation.

[¶44] An intermediary strategy is not inferred solely because the same strategy appears at act level. It must be supported by the intermediary’s legally stated role.

[¶45] Intermediary_type is coded from the focal act, not from external knowledge about the actor’s usual organisational form or practice.

[¶46] A regulatory object, function, mechanism, strategy, target, beneficiary, and legal consequence are analytically distinct and must not be treated as interchangeable.

## [¶47] 6 General Coding Conventions

[¶48] Use only the permitted values specified in this codebook. Do not introduce a new category, combine categories into an unapproved value, or substitute a synonymous label during coding.

[¶49] Where a variable permits multiple values, record all applicable approved values separated by a semicolon.

[¶50] Yes means that the focal act provides sufficient evidence for the function or obligation. No means that a qualifying intermediary exists but the focal act does not assign the specified function or obligation to that intermediary. N/A means that no qualifying intermediary exists or the variable does not apply to the observation.

[¶51] A blank cell means that the variable has not yet been assessed. It is not equivalent to No, N/A, or Unclear.

[¶52] Unclear is used only where it is an expressly permitted value and the focal act does not provide sufficient evidence for reliable classification.

[¶53] Free-text descriptions must summarise the focal act without importing characteristics from external practice.

[¶54] Where a coding issue cannot be resolved using the approved definitions and values, stop coding that issue, record it for adjudication, and amend the dataset or codebook only after the decision has been agreed and documented.

## [¶55] 7 Coding Procedure and Quality Assurance

[¶56] 1.  Identify a candidate act and record its official title, form, reference, CELEX identifier, source, and date.

[¶57] 2.  Apply the act inclusion and exclusion rules. Record excluded acts in Excluded_acts and included acts in ACT_SUMMARY.

[¶58] 3.  Code the included act’s substantive scope, regulatory object, regulatory architecture, architecture configuration, and regulatory strategies, with value-specific rationales.

[¶59] 4.  Screen the act for actors or organizational arrangements assigned regulatory functions through identifiable mechanisms. Apply the intermediary inclusion rule to each candidate.

[¶60] 5.  Create one INTERMEDIARY_MAP record for each qualifying intermediary category. Where none is identified, create one No_intermediary record.

[¶61] 6.  Code intermediary identity and relational position, regulation by the intermediary, and regulation of the intermediary. Support each positive decision with the relevant provisions and free-text rationale where required.

[¶62] 7.  Conduct backward checks when a definition, value, or function is added or revised. Identify whether the change requires a completely new intermediary row or only corrections to existing variables.

[¶63] 8.  Resolve uncertain or disputed cases before changing the codebook or dataset. Record the decision, affected variables and records, legal basis, date, and resulting backward corrections in the project decision log.

[¶64] Quality assurance relies on traceability to the focal act, consistent application of controlled values, separation of act-level and intermediary-level judgments, backward checks following schema changes, and adjudication of ambiguous cases before amendments are entered. Version histories for the dataset and codebook should identify material changes to variables, values, definitions, or previously coded records.

## [¶65] 8 Variable Groups

[¶66] The variables are organized into four analytical groups. In the recommended workbook order, each group appears as a contiguous block so that the codebook and dataset share the same conceptual structure.

[¶67 TABLE]
| Group | Variables from and to | Analytical question |
|---|---|---|
| 1 Act Context and Regulatory Design | Excluded_acts variables; ACT_SUMMARY from case_id through regulatory_strategy_rationale | What is the act, what does it govern, and how does it organize regulation? |
| 2 Intermediary Identity and Relational Position | INTERMEDIARY_MAP from intermediary_record_id through target_context | Who is the intermediary and where is it positioned in the regulatory relationship? |
| 3 Regulation by Intermediaries | INTERMEDIARY_MAP from Function_description through Function_enforcement | What does the intermediary regulate and how does it perform regulatory functions? |
| 4 Constitution and Regulation of Intermediaries | INTERMEDIARY_MAP from Regulation_of_description through complaints_redress_obligations | How does the intermediary acquire its role and how is it governed, constrained, and held to requirements? |

## [¶68] 9 Variable Dictionary

### [¶69] 9.1 Group 1 Act Context and Regulatory Design

[¶70] This group records act screening, identity, legal and temporal characteristics, substantive scope, regulatory object, and act-level architecture and strategy. It contains the variables in Excluded_acts and ACT_SUMMARY.

#### [¶71] Excluded_acts

[¶72 TABLE]
| Variable | Definition | Permitted values or format |
|---|---|---|
| Act_title | Official English title of the assessed act. | Free text |
| Type of Regulatory Instrument | Legal or policy form of the assessed act. | Approved act-type vocabulary |
| Legislation Code | Formal identifying number or official reference of the assessed act. | Official reference |
| celex | CELEX identifier assigned to the assessed act, where available. | CELEX identifier; N/A |
| source_url | Link to the official online text of the assessed act. | URL |
| Enactment Year | Year in which the assessed act was formally adopted or issued. | Four-digit year |
| screening_decision | Records that the assessed act was excluded from the analytical corpus. | Excluded |
| exclusion_reason | Controlled or standardized reason explaining why the act falls outside the corpus. | Approved exclusion reason |
| screening_notes | Concise explanation supporting the exclusion decision, including the feature assessed and why the digital connection was insufficient. | Free text |

#### [¶73] ACT_SUMMARY

[¶74 TABLE]
| Variable | Definition | Permitted values or format |
|---|---|---|
| case_id | Unique identifier assigned to each included act. | case_XX |
| act_title | Official English title of the included act. | Free text |
| Type of Regulatory Instrument | Legal or policy form of the included act. | Approved act-type value |
| Legislation Code | Formal identifying number or official reference of the included act. | Official reference |
| celex | Unique CELEX identifier assigned to the included act. | CELEX identifier |
| source_url | Link to the official online text of the included act. | URL |
| Downloaded as PDF | Indicates whether an official PDF copy of the included act identified by case_id has been downloaded. | Yes; No |
| Assessed? | Indicates whether the included act identified by case_id has been reviewed for the purposes of the dataset. | Yes; No |
| Included in the text on governance? | Indicates whether the included act identified by case_id is included in the project’s governance analysis. | Yes; No |
| Included in the text on self-regulation? | Indicates whether the included act identified by case_id is included in the project’s analysis of self-regulation. | Yes; No |
| Enactment Year | Year in which the act was formally adopted or issued. | Four-digit year |
| In force, changed, or repealed? | Current legal status of the act. | In force; Changed; Repealed |
| Information/infrastructure | Principal dimension of digital governance addressed by the act. | Information; Infrastructure; Information and infrastructure; Unspecified |
| Horizontal or vertical | Whether the act applies across sectors or primarily within a specific sector or field. | Horizontal; Vertical |
| Domain | Sector or field of activity principally governed by the act. | Connectivity; Data & Privacy; E-commerce & Consumer Protection; IPR; Media; Telecommunications; Trust & Safety; Unspecified |
| Who regulates? | Concise description of how the act allocates public and private regulatory authority and responsibilities. | Free text |
| How is self-regulation operationalised? | Concise description of whether and how the act relies on regulated organisations or other non-state actors to implement regulatory requirements or objectives. | Free text |
| regulatory_object | Principal object or objects that constitute an express and substantial subject of the act. Apply the restrictive act-level direct-object rule. | technical_artifacts_and_resources; services_and_markets; transactions_and_contracts; information_and_communications; rights_and_entitlements; rules_and_regulatory_processes; organizational_and_financial_governance; protection_and_redress; multiple values permitted |
| regulatory_object_rationale | Explains why each regulatory_object value applies, identifies the specific regulated object represented by the principal value, and places the supporting legal provisions beside the value-specific explanation. | Free text; value-specific explanations with provisions in parentheses |
| regulatory_architecture | How the act organizes regulation of the activity, including how regulatory roles are allocated among public regulation, private ordering, self-regulation, and enhanced oversight. Code all applicable arrangements whether or not a qualifying intermediary is identified. | Direct public regulation; Regulated private ordering; Enforced self-regulation; Enhanced self-regulation; multiple values permitted |
| regulatory_architecture_rationale | Explains separately how each coded architecture is constituted and identifies the supporting provisions beside the corresponding explanation. | Free text |
| architecture_configuration | Relationship between different regulatory architectures coded for the act. Do not use this variable for steps within a single architecture. | Single; Alternative; Sequential; Complementary; Separate; multiple values except with Single |
| architecture_configuration_rationale | Explains separately why the coded architectures are alternative, sequential, complementary, or separate, with the supporting provisions placed beside each relationship. | Free text |
| regulatory_strategy | Major ways through which the act directs, structures, or protects conduct. This variable records the regulatory logic through which the act governs, rather than the object being regulated or the institutional allocation of regulatory roles. Code only strategies significant to the act. | Prescriptive; Process-based; Performance-based; Principles-based; Rights-based; Risk-based; multiple values permitted |
| regulatory_strategy_rationale | Explains separately how each coded strategy operates in the act and identifies the supporting provisions beside each explanation. | Free text |

#### [¶75] Definitions of the Eight regulatory object values

[¶76 TABLE]
| Value | Definition |
|---|---|
| technical_artifacts_and_resources | Products, equipment, software, technical systems, networks, facilities, spectrum, numbers, names, identifiers, or other technical resources, including their design, conformity, allocation, connection, operation, access, or administration. |
| services_and_markets | The provision, availability, quality, continuity, or conditions of services, together with market entry, competition, non-discrimination, and commercial relationships among service providers or market participants. |
| transactions_and_contracts | The formation, negotiation, performance, modification, or termination of contractual and transactional relationships, including consumer contracts, commercial agreements, procurement, payments, withdrawal, and contractual disclosures. |
| information_and_communications | The creation, collection, processing, storage, transmission, publication, disclosure, restriction, or removal of information, data, communications, or content, including personal data, broadcasting content, advertising, and regulatory reporting. |
| rights_and_entitlements | The allocation, exercise, administration, representation, or recognition of legal rights and entitlements, including intellectual-property rights, privacy rights, consumer and user rights, access rights, and remuneration entitlements. |
| rules_and_regulatory_processes | The development, adoption, recognition, notification, interpretation, or application of standards, codes, technical rules, authorisations, administrative procedures, and regulatory decisions. |
| organizational_and_financial_governance | The internal organisation, governance, compliance arrangements, personnel, independence, competence, resources, accounting, financing, tariffs, liability cover, or other institutional and financial arrangements of a regulated entity or intermediary. |
| protection_and_redress | Arrangements for preventing, identifying, or mitigating harm and for responding to alleged violations, including safety, security, risk management, monitoring, complaints, claims, dispute resolution, corrective measures, remedies, and compensation. |

### [¶77] 9.2 Group 2 Intermediary Identity and Relational Position

[¶78] Variables from intermediary_record_id through target_context identify the intermediary category, the legal evidence for its inclusion, whether its involvement is required or permitted, and its position within the regulatory relationship.

[¶79 TABLE]
| Variable | Definition | Permitted values or format |
|---|---|---|
| intermediary_record_id | Unique identifier assigned to each intermediary-level observation. | RI_CXX_0XX; No_intermediary_XX |
| case_id | Identifier linking the intermediary record to the corresponding act in ACT_SUMMARY. | case_XX |
| act_title | Official English title of the act in which the intermediary is identified. | Free text |
| Type of Regulatory Instrument | Legal or policy form of the act. | Value used in ACT_SUMMARY |
| Legislation Code | Formal identifying number or official reference of the act. | Official reference |
| intermediary_present | Indicates whether the act contains a qualifying regulatory intermediary. | Yes; No |
| Intermediary_name | Name or legally grounded description of the actor category or organizational arrangement performing the intermediary function. | Free text; N/A |
| Relevant provision(s) | All provisions needed to establish, recognise, or specify the intermediary, its functions, position, recognition, or obligations. | Free text; N/A |
| Intermediary_type | Organizational type of the intermediary as defined or identifiable from the focal act. Do not infer the type from external practice. | For-profit; Industry association; Epistemic/professional; Unclear; N/A |
| intermediary_involvement | Whether the act requires or permits use of the intermediary in the arrangement described in that row. | Required; Conditional; Optional; Member State option; Not specified; N/A; multiple values permitted where distinct routes apply |
| intermediary_involvement_rationale | Explains why the intermediary’s involvement is required, conditional, optional, left to Member State choice, or not specified, with the supporting provisions beside each explanation. | Free text |
| orientation | Direction of the intermediary’s function within the regulatory arrangement. It identifies toward whom the intermediary acts, rather than the function performed or the object upon which it acts. | target-facing; regulator-facing; bidirectional; intermediary-facing; N/A; multiple values permitted |
| regulator_context | Institutional context of the actor or actors responsible for the regulatory arrangement in which the intermediary operates. | EU_public; national_public; multilevel_public; private_self_regulatory; hybrid_public_private; Unclear; N/A; multiple values permitted |
| target_context | Category or categories of actor constituting the relevant target of the intermediary relationship. | product_economic_operator; service_provider; platform_provider; regulated_professional; public_body; individual; regulatory_intermediary; N/A; multiple values permitted |

### [¶80] 9.3 Group 3 Regulation by Intermediaries

[¶81] Variables from Function_description through Function_enforcement record what the intermediary acts upon, the mechanism and strategy through which it participates in regulation, and the functions assigned to it.

[¶82 TABLE]
| Variable | Definition | Permitted values or format |
|---|---|---|
| Function_description | Concise description of what the intermediary is assigned to do under the focal act. | Free text; N/A |
| intermediary_object | Object or objects upon which the intermediary directly acts through its legally assigned function. Apply the restrictive intermediary-level direct-object rule. | technical_artifacts_and_resources; services_and_markets; transactions_and_contracts; information_and_communications; rights_and_entitlements; rules_and_regulatory_processes; organizational_and_financial_governance; protection_and_redress; multiple values permitted; N/A |
| intermediary_object_rationale | Explains why each intermediary_object value applies, identifies the specific direct object represented by the principal value, and places the supporting provisions beside each value-specific explanation. | Free text; N/A |
| mechanism_family | Broad approved family of regulatory mechanisms through which the intermediary performs its primary function. It is distinct from the intermediary’s specific function and must use an approved family label. | Code creation; Assurance; Monitoring; Registry administration; Internal compliance; Dispute resolution; Complaint handling; Insurance / risk underwriting; Enforcement; N/A; approved multiple values where necessary |
| Function_summary | Short standardised description of the intermediary’s specific operational function. It records the regulatory task assigned to the intermediary, rather than the broader mechanism family, regulatory strategy, object, or orientation. The label must come from the approved project vocabulary. | Approved standardised label; N/A |
| intermediated_strategy | Regulatory strategies within the intermediary’s legally stated role. This is a row-specific variable and must not be inferred solely from the act-level regulatory strategy. Code each intermediary row separately. | Prescriptive; Process-based; Performance-based; Principles-based; Rights-based; Risk-based; Unclear; N/A; multiple values permitted |
| intermediated_strategy_rationale | Explains separately how each coded strategy operates through the intermediary’s assigned role and places the supporting provisions beside the corresponding explanation. | Free text; N/A |
| Function_code_creation | Indicates whether the intermediary develops or designs codes, rules, standards, specifications, or comparable regulatory frameworks. | Yes; No; N/A |
| Function_assurance | Indicates whether the intermediary assesses or verifies conformity with regulatory requirements. | Yes; No; N/A |
| Function_monitoring | Indicates whether the intermediary systematically tracks conduct, compliance, risks, implementation, or outcomes. | Yes; No; N/A |
| Function_registry_administration | Indicates whether the intermediary operates or maintains a legally prescribed or institutionally authoritative registry or directory, substitutes for a public notification or registration mechanism, or controls delegation, registration, entry, updating, suspension, removal, or access where these activities have regulatory consequences. | Yes; No; N/A |
| Function_internal_compliance | Indicates whether the intermediary supports implementation of regulatory requirements or internal controls within a regulated organization. | Yes; No; N/A |
| Function_dispute_resolution | Indicates whether the intermediary resolves or determines disputes outside ordinary judicial proceedings. | Yes; No; N/A |
| Function_complaint_handling | Indicates whether the intermediary receives, represents, assesses, processes, or determines complaints. | Yes; No; N/A |
| Function_auditing | Indicates whether the intermediary conducts a systematic examination identified or structured as an audit. | Yes; No; N/A |
| Function_Insurance / risk underwriting | Indicates whether the intermediary provides insurance or underwrites risks connected to the regulated activity or intermediary arrangement. | Yes; No; N/A |
| Function_enforcement | Indicates whether the intermediary takes action to secure third-party compliance, protect rights, restrict conduct, or remedy violations. | Yes; No; N/A |

### [¶83] 9.4 Group 4 Constitution and Regulation of Intermediaries

[¶84] Variables from Regulation_of_description through complaints_redress_obligations record how the intermediary acquires its recognized role and the substantive requirements imposed upon the intermediary itself.

[¶85 TABLE]
| Variable | Definition | Permitted values or format |
|---|---|---|
| Regulation_of_description | Concise description of how the intermediary is recognized, constituted, governed, supervised, controlled, or subjected to requirements under the focal act. | Free text; N/A |
| Recognition_pathways | Formal pathway through which the intermediary acquires its recognised status or authority under the focal act. | Vetting; Designation; None; N/A |
| Obligation_intensity | Overall intensity of the requirements imposed on the intermediary itself, used as a summary alongside the disaggregated obligation variables. Do not count duties imposed only on a regulator or another actor. | None; Light; Moderate; Strong; Unclear; N/A |
| competence_capacity | Indicates whether the intermediary must possess specified expertise, qualifications, personnel, technical resources, or operational capacity. | Yes; No; N/A |
| independence_impartiality | Indicates whether the intermediary must be independent or act impartially. | Yes; No; N/A |
| conflict_of_interest_safeguards | Indicates whether the intermediary must identify, prevent, disclose, manage, or avoid conflicts of interest. | Yes; No; N/A |
| integrity_reliability | Indicates whether the intermediary or its personnel must satisfy requirements concerning integrity, good repute, honesty, or reliability. | Yes; No; N/A |
| organizational_formalization | Indicates whether the intermediary must maintain a specified organizational structure, governance arrangement, management system, or documented operational framework. | Yes; No; N/A |
| liability_financial_cover | Indicates whether the intermediary must maintain insurance, financial guarantees, reserves, or other cover for potential liability. | Yes; No; N/A |
| representativeness | Indicates whether the intermediary must represent specified interests, constituencies, sectors, or stakeholder groups. | Yes; No; N/A |
| Confidentiality | Indicates whether the intermediary must protect confidential information or observe professional secrecy. | Yes; No; N/A |
| Data_protection | Indicates whether the intermediary must comply with requirements governing the lawful processing or protection of personal data. | Yes; No; N/A |
| data_security | Indicates whether the intermediary must protect information or systems against unauthorized access, loss, alteration, or other security risks. | Yes; No; N/A |
| reporting/notification | Indicates whether the intermediary must report or notify specified information, events, findings, or changes to a regulator or another designated actor. | Yes; No; N/A |
| Procedural compliance | Indicates whether the intermediary must follow prescribed procedures, methods, standards, guides, or operational requirements when performing its role. | Yes; No; N/A |
| Recordkeeping_traceability | Indicates whether the intermediary must create, retain, maintain, or make traceable specified records or documentation. | Yes; No; N/A |
| transparency_disclosure | Indicates whether the intermediary must make specified information publicly available or disclose it to affected parties. | Yes; No; N/A |
| cooperation_access | Indicates whether the intermediary must cooperate with public authorities or provide access to information, documents, premises, personnel, or systems. | Yes; No; N/A |
| responsiveness_service_duties | Indicates whether the intermediary must respond to requests, provide services within specified periods, maintain availability, or satisfy comparable service requirements. | Yes; No; N/A |
| corrective_remedial_duties | Indicates whether the intermediary must correct deficiencies, address non-compliance, withdraw or suspend an output, or take another remedial action. | Yes; No; N/A |
| complaints_redress_obligations | Indicates whether the intermediary must establish or follow procedures for complaints, review, appeal, or redress concerning its activities or decisions. | Yes; No; N/A |

## [¶86] 10 Distinguishing Objects, Strategies, Functions, and Architecture

[¶87 TABLE]
| Variable family | Question answered | Coding boundary |
|---|---|---|
| regulatory_object | What does the act govern? | Substantial object of the act, not every procedure, safeguard, purpose, or consequence. |
| regulatory_strategy | Through what regulatory logic does the act govern? | Major act-level strategy only. |
| regulatory_architecture | How and among whom is regulation institutionally organized? | Allocation among public regulation, private ordering, self-regulation, and enhanced oversight. |
| intermediary_object | What does the intermediary act upon? | Direct object of the assigned intermediary function. |
| Function variables | What regulatory task does the intermediary perform? | Specific activity assigned to the intermediary. |
| mechanism_family | Through what broad operational mechanism is the function performed? | Mechanism must use the approved family label and remain distinct from the function. |
| intermediated_strategy | Through what regulatory logic does the intermediary perform its role? | Row-specific strategy supported by the intermediary mandate. |
| Orientation and contexts | Toward whom and within what institutional relationship does the intermediary act? | Relational position, not function or object. |
| Obligation variables | How is the intermediary itself regulated? | Duties imposed upon the intermediary, not solely upon its regulator. |

[¶88] There is no automatic correspondence between an object and a strategy. The same technical product may be regulated prescriptively, through a performance standard, through a conformity-assessment process, or through a risk-based arrangement. Likewise, a right may be the regulatory object without every associated intermediary necessarily using a Rights-based strategy.

## [¶89] 11 Administrative Dataset Documentation

[¶90 TABLE]
| Item | Documentation |
|---|---|
| Dataset title | Regulatory Intermediation in European Digital Governance |
| Principal investigator | Rotem Medzini, Department of Political Science and Federmann School of Public Policy and Governance, The Hebrew University of Jerusalem |
| Co-investigator | David Levi-Faur, Department of Political Science and Federmann School of Public Policy and Governance, The Hebrew University of Jerusalem |
| Language | English |
| Geographical scope | European Union |
| Period of data collection | 10 April 2026 to ongoing |
| License | CC BY 4.0, subject where applicable to applicable copyright and database-rights law |
| Dataset file | dataset_of_EU_regulatory_intermediation.xlsx |
| Codebook file | codebook_regulatory_intermediation.docx |
| Version and update date | To be completed before release |
| ORCID and funding information | To be completed before release |
| Recommended citation | Medzini, Rotem, and David Levi-Faur. Regulatory Intermediation in European Digital Governance. Version to be added upon release. |

## [¶91] 12 Reference

[¶92] Abbott, Kenneth W., David Levi-Faur, and Duncan Snidal. 2017. “Theorizing Regulatory Intermediaries: The RIT Model.” The ANNALS of the American Academy of Political and Social Science 670(1): 14–35.
