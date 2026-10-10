# CLAUDE Track B - O4 Configurational reconstruction

Track: V8 plus eight operations (METHOD_HYPOTHESIS, applied as specified). Evidence: the 20 frozen statements (register SHA-256 417A35A3...F77F). All relationship and uncertainty IDs refer to CLAUDE_TRACK_B_RELATIONSHIPS.csv and CLAUDE_TRACK_B_UNCERTAINTY_REGISTER.csv. Configuration claims here are `claim_level = configuration` at most, with `coding_status = cross_provision_inference` (a configuration is an analyst's grouping, never directly stated by the text).

## 1. Membership criteria applied (stated before grouping)

A group was formed only where accepted relations were joined by at least one qualified coupling, namely:

1. a stated precedence or trigger condition in the text that connects one relation's action to another's (for example "before the deadline", "if ... finds", "after consulting", "before it is concluded", "as soon as");
2. a stated cross-reference or anaphora ("that agreement", "the escrow agent", "the list referred to in ... Article 23"); or
3. a shared object that one statement defines as the output of another (for example "an audit report" for the audit in the same sentence).

The following were not accepted as couplings: a shared actor (the Registry or the Commission appears in several groups), a shared article or annex, a shared context (phased registration), a shared term used as a category name, or graph connectivity. Deferred and rejected relations are not members.

## 2. Candidate configurations

### C-P03-A - Notified-body assessment and surveillance of the manufacturer's quality system (Annex III anchor)

| Item | Content |
|---|---|
| Members (relations) | R-P03-02 (notified body -> manufacturer, verification/assurance), R-P03-03 (notified body -> manufacturer, audit report) |
| Statements | CS-P03-005 and CS-P03-006 (support); CS-P03-003 (assessment function and object only; no expressed counterparty) |
| Excluded but adjacent | CS-P03-004 / R-P03-04 (notifier not expressed, DEFERRED); R-P03-05 (designation, DEFERRED) |
| Elements | Actors: notified body, manufacturer (category in the object clause and recipient). Functions: verification/assurance, monitoring (uncertain_boundary), information provision. Mechanisms: verification, reporting. Instruments: assessment of the quality system; periodic audit; audit report |
| Justification of grouping | Same two parties, one object (the manufacturer's quality system). Coupling type 3: the object of R-P03-03 ("an audit report") is the output of the audit in R-P03-02, in the same sentence (CS-P03-005 / CS-P03-006). The assessment statement CS-P03-003 shares the actor and object family but, lacking a counterparty, is not counted as a coupling |
| Theoretical pattern | A partial instance of V8's "third-party assurance configuration" (assessment of a regulated organisation by a verifier, with reporting back to it). A pattern label is offered only as a description of what is present |
| Overlap | None with another configuration. R-P03-01 is a separate relation (see X-P03-1, X-P03-2) |
| What is not established | Designation or recognition of the notified body (DEFERRED); legal consequence of the assessment or audit (binding effect, approval status, market access); whether the assessment precedes surveillance (not stated in the statements); the notified body's public/private status (U-11); public supervision of the notified body; any information duty of the manufacturer (outside the 20 statements); the Annex IV equivalent (U-07); implementation or effectiveness |
| claim_level / coding_status | configuration / cross_provision_inference (spans anchors P03_PR03 and P03_PR04) |

### C-P04-A - Prior-rights validation procedure in phased registration (Registry, validation agent, applicant)

| Item | Content |
|---|---|
| Members (relations) | Core: R-P04-08 (applicant -> agent, evidence), R-P04-10 (agent -> applicant, examination), R-P04-11 (agent -> Registry, notification of outcome). Registry-facing attachment: R-P04-06 (Registry -> agents, selection), R-P04-07 (Registry -> agent, requirement of conduct) |
| Statements | CS-P04-003 to CS-P04-008 |
| Excluded but adjacent | R-P04-09 (indication of the agent, DEFERRED); R-P04-22 (delegation of decision authority, DEFERRED) |
| Elements | Actors: Registry, validation agents, applicants. Functions: designation of verifiers (equivalent), implementation (conduct requirement), information provision, verification/assurance. Mechanisms: authorization, command, information, verification, notification. Instruments: selection, requirement, documentary-evidence submission, examination, notification |
| Justification of grouping | Core: coupling type 1. Submission is a stated condition of examination (CS-P04-006: evidence "submitted before the deadline"), and the notification conditions refer to receipt and to the agent's finding (CS-P04-007, CS-P04-008). Attachment: coupling is weaker, namely the category term "validation agent" and the phrase "indicated by the Registry" in CS-P04-005. The attachment is recorded as weaker and tested in S-11 |
| Theoretical pattern | A procedural verification stage in which an examining actor distinct from the Registry assesses applicants' claims and reports outcomes to the Registry; the Registry selects and sets conduct requirements for that actor (V8: verification relation with a designation/control relation attached). Not labelled as delegation, gatekeeping or intermediation |
| Overlap | Shares the actor "Registry" with C-P04-B, C-P04-C, C-P04-D; shares the context "phased registration" with C-P04-B. No shared statements or relations |
| What is not established | The legal effect of the agent's finding or notification on any registration outcome (U-20); whether the examination is a necessary stage (gateway); transfer of decision authority (R-P04-22); the agent's public/private status (U-32); allocation among several agents (U-18); that the audit covers the validation (R-P04-25 rejected); implementation or effectiveness |
| claim_level / coding_status | configuration / cross_provision_inference (spans anchors P04_PR02, PR03, PR04) |

### C-P04-B - Independent audit of the phased registration with Commission consultation and reporting (Article 12(5))

| Item | Content |
|---|---|
| Members (relations) | R-P04-02 (Registry -> auditor, appointment), R-P04-03 (Registry -> Commission, consultation), R-P04-05 (auditor -> Registry, audit; cross_provision_inference), R-P04-01 (auditor -> Commission, findings; human review) |
| Statements | CS-P04-001, CS-P04-002 |
| Excluded but adjacent | R-P04-04 (cost-bearing, REJECTED); R-P04-21 (accountability, REJECTED); R-P04-25 (audit of validation agents, REJECTED) |
| Elements | Actors: Registry, auditor, Commission. Functions: designation of a verifier (equivalent), verification/assurance, information provision. Mechanisms: authorization (appointment), participation (consultation), verification, reporting. Instrument: independent audit |
| Justification of grouping | One paragraph, one instrument. Couplings: type 1 (consultation precedes appointment; "at the end of the phased registration"; report of "its findings"); identity of the audit's performer with the appointed auditor is a provisional reading (U-12) |
| Theoretical pattern | V8's audit arrangement (auditee, auditor, reporting, relation to an institution outside the auditee), here with appointment by the audited entity. Present: appointment, performance, report to a named institution. Absent: standards of assessment in the statements, information access, follow-up, any consequence |
| Overlap | Context overlap with C-P04-A (phased registration) only |
| What is not established | Independence in fact or safeguards defining it (U-16); Commission assessment, response or consequence; accountability of the Registry (R-P04-21 rejected); what the audit covers beyond the Registry's administration (U-13, U-33); implementation |
| claim_level / coding_status | configuration (thin) / cross_provision_inference; human review flagged for R-P04-01 and R-P04-05 |

### C-P04-C - Escrow arrangement with Commission consent precondition and beneficiary designation (Article 15(1))

| Item | Content |
|---|---|
| Members (relations) | R-P04-12 (Registry <-> escrow agent, contract), R-P04-13 (beneficiary designation, thin), R-P04-14 (Commission -> Registry, consent), R-P04-15 (Registry -> escrow agent, daily deposit) |
| Statements | CS-P04-009, CS-P04-010, CS-P04-011 |
| Excluded but adjacent | R-P04-23 (escrow agent -> Commission, REJECTED) |
| Elements | Actors: Registry, escrow agent (category), Commission. Function: uncertain (data safeguarding; purpose not stated). Mechanisms: contract, authorization (consent), information (deposit). Instrument: escrow agreement |
| Justification of grouping | Instrument-defined group. Couplings: type 2 ("that agreement" in CS-P04-010 refers to the agreement of CS-P04-009; "the escrow agent" in CS-P04-011 refers to the agent of that agreement) and type 1 ("before it is concluded"). The group is organised around the instrument, since the problem the instrument addresses is not stated in the 20 statements |
| Theoretical pattern | A tripartite instrument: a contract between the Registry and a third party, conditioned ex ante on the Commission's consent, naming the Commission as beneficiary, with a continuing deposit. V8's "risk-transfer" instrument family is a possible label but would assume the purpose, so it is not adopted |
| Overlap | None except the actors Registry and Commission |
| What is not established | Purpose and release conditions of the escrow; the Commission's rights as beneficiary (U-23); whether the Commission may withhold consent and whether validity depends on it (U-24); order agreement -> deposit as a rule (U-25); implementation |
| claim_level / coding_status | configuration (thin, instrument-defined) / cross_provision_inference |

### C-P04-D - Complaint routing and ADR provider selection (Articles 22(5), 22(6), 23(1))

| Item | Content |
|---|---|
| Members (relations) | R-P04-19 (Registry -> ADR providers, selection, "may"), R-P04-16 (complainant -> provider, choice from the list), R-P04-18 (provider -> Registry, information) |
| Statements | CS-P04-012 (choice clause only), CS-P04-013, CS-P04-014 |
| Excluded but adjacent | R-P04-17 (submission of complaints and responses, DEFERRED); R-P04-24 (supervision of providers, REJECTED) |
| Elements | Actors: Registry, ADR providers, complainant. Functions: designation of dispute-resolution providers (equivalent); dispute resolution (intake and routing only); information provision. Mechanisms: authorization (designation), participation (choice), notification. Instruments: ADR complaint procedure; list of providers |
| Justification of grouping | Couplings: type 2 (CS-P04-012 refers to "the list referred to in the first paragraph of Article 23", resolved as the providers the Registry selects in CS-P04-014; U-27) and type 1 ("as soon as a request for ADR is properly filed ... and the appropriate fee is paid", CS-P04-013) |
| Theoretical pattern | The access and routing stage of a complaint procedure in which the Registry designates the providers, the complainant chooses among them, and the chosen provider informs the Registry. The 20 statements contain no adjudicative statement, so no adjudication architecture is described |
| Overlap | None except the actor Registry |
| What is not established | Who the parties to the ADR are (not stated in the 20 statements), so no claim about the Registry's position relative to providers is made; adjudication, decisions, remedies, review; the effect of the information on the Registry (frozen excerpt of CS-P04-013 ends with the information duty; U-28); implementation |
| claim_level / coding_status | configuration (thin) / cross_provision_inference |

## 3. Groupings considered and declined

| ID | Candidate | Reason declined |
|---|---|---|
| X-P03-1 | Member State notification as a "notification system" (R-P03-01 alone) | One report relation; no receiving structure, assessment or follow-up stated (V8 inference rule 3). Stays at relation level |
| X-P03-2 | Designation -> notification -> assessment chain (R-P03-05, R-P03-01, R-P03-02) | The only coupling (designation) is DEFERRED; identity of "notified body" with notified "bodies" is by naming plus wider text and is not a qualified coupling (U-03, U-04). Tested in S-04 |
| X-P04-1 | Registry-centred designation configuration (R-P04-02, -06, -19, -07) | Shared actor and repeated function across different problems and stages; no qualified coupling between the three; different modalities (shall, shall, may); recurrence is a product of the frozen selection (U-31). Tested in S-10 |
| X-P04-2 | Integrated phased-registration assurance configuration (C-P04-A plus C-P04-B) | Link is contextual membership only; R-P04-25 rejected (U-33). Tested in S-09 |
| X-P04-3 | Commission-facing supervisory configuration across C-P04-B and C-P04-C | Commission positions are four different thin things (report recipient, consulted, consenting, named beneficiary); R-P04-20 rejected; label "supervision" not supported |
| X-P04-4 | ADR adjudication architecture | No adjudicative statement among the 20; C-P04-D covers routing only |

## 4. Overlap and coverage

| Statement | Configuration | Note |
|---|---|---|
| CS-P03-001, CS-P03-002 | none (relation R-P03-01 only) | single information relation |
| CS-P03-003 | C-P03-A (function/object only) | no expressed counterparty |
| CS-P03-004 | none | DEFERRED, actor not expressed |
| CS-P03-005, CS-P03-006 | C-P03-A | |
| CS-P04-001, CS-P04-002 | C-P04-B | |
| CS-P04-003 to CS-P04-008 | C-P04-A | |
| CS-P04-009 to CS-P04-011 | C-P04-C | |
| CS-P04-012 | C-P04-D (choice clause only) | submission relation DEFERRED |
| CS-P04-013, CS-P04-014 | C-P04-D | |

No statement or relation belongs to two configurations. Overlap exists only through shared actors (Registry in A, B, C, D; Commission in B, C) and shared context (phased registration in A, B); none of these was treated as architecture.

## 5. Summary of what O4 produced

Five thin configurations (one for P03, four for P04) and six declined groupings. No configuration is claimed to carry a property that its members do not individually or jointly have as stated; the only whole-level descriptions are the procedural patterns listed above. Whether these are "configurations" in V8's full sense, or merely clusters of typed relations, is a judgment the analyst makes explicit here and which a human reviewer may reasonably decide differently (see S-06 and S-11).
