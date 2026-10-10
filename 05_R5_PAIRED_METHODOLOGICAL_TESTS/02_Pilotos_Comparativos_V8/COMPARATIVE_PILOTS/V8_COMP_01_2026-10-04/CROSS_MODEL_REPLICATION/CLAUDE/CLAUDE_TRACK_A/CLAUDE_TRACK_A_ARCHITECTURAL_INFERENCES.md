# Claude Track A - Architectural inferences and stopping-rule decisions (V8 only)

Controlling hashes: register `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F` (verified); P03 source FE-001 (`31991L0263.html`) `01D5BDB117B370AE9DAD7F3ABB151583A75519CBAD0E7808EFC9040C8D656888` (verified); P04 source FE-003 (`32004R0874.html`) `62AFB4DDCCAE5E7157590B1386040AA8D160701D7194DBD2F2403AC4B6781449` (verified).

## 1. Summary of decisions

| Case | Highest level actually supported | Architecture-level claim | Regime-level claim | Stopping-rule decision |
|---|---|---|---|---|
| P03 | Configuration (candidate configurations C-P03-01, C-P03-02, C-P03-03) | None warranted | None; no regime-boundary decision made | STOP at configuration (SR-P03) |
| P04 | Configuration (candidate configurations C-P04-01, C-P04-02, C-P04-03); relation level for the ADR channel | None warranted | None; no regime-boundary decision made | STOP at configuration (SR-P04); ADR channel stops at relation (SR-P04-ADR) |

No claim crosses the architecture boundary. This is the result of applying V8 inference rules 4 to 6, not a default: Section 3 shows what an architecture-level claim would need and which of those requirements the frozen statements do not meet.

## 2. Claims made (all at or below configuration level)

Each claim is a formal-text claim. None asserts implementation, practice or effectiveness.

| Claim ID | Claim (what is asserted) | Level | Status |
|---|---|---|---|
| CL-P03-01 | Within the sampled provisions, Member States are shown designating bodies and laboratories for the Article 9 procedures and informing the Commission of them, with the designation content and any Commission follow-up unspecified. | configuration (candidate, thin) | direct_text members |
| CL-P03-02 | Within Annex III as sampled, a notified body assesses the manufacturer's quality system, audits at reasonable intervals, and provides an audit report to the manufacturer. The report goes to the audited party only. | configuration (candidate, partial) | direct_text and cross_provision_inference members |
| CL-P03-03 | The notified body that assesses and audits is the class of body that Member States designate and notify under Article 10(1) (identity fixed by Annex III point 6). | configuration (candidate, thin) | cross_provision_inference |
| CL-P04-01 | Within Articles 13 and 14 as sampled, the Registry selects validation agents and requires conduct of them; applicants submit evidence to an agent; the agent examines the claim and notifies the Registry of the outcome. | configuration (candidate, partial) | direct_text members |
| CL-P04-02 | Within Article 12(5) as sampled, the Registry appoints the auditor after consulting the Commission and the audit reports its findings to the Commission. No claim is made about what is audited or about accountability. | configuration (candidate, narrow) | direct_text members |
| CL-P04-03 | Within Article 15(1), the Registry concludes an escrow agreement that requires prior Commission consent and deposits a daily copy of the .eu database with the escrow agent. | configuration (candidate, partial) | direct_text and cross_provision_inference members |
| CL-P04-04 | The Registry may select ADR providers and the ADR provider informs the Registry of a filed request. These are two relations; no configuration is claimed. | relation | direct_text members |

### Traceability chains

Format: claim -> configuration -> relationships (accepted members) -> statements -> provision anchor -> source / hash.

- **CL-P03-01** -> C-P03-01 -> R-P03-01, R-P03-02, R-P03-03 -> CS-P03-001, CS-P03-002 -> P03_PR01 Article 10(1); P03_PR02 Article 10(2) -> FE-001, 31991L0263, OJ L 128 of 23.05.1991, SHA-256 `01D5BDB1...6888` (full value above).
- **CL-P03-02** -> C-P03-02 -> R-P03-04, R-P03-05, R-P03-06 -> CS-P03-003, CS-P03-005, CS-P03-006 -> P03_PR03 Annex III point 3.3; P03_PR04 Annex III point 4.3 -> FE-001, SHA-256 `01D5BDB1...6888`. Cross-provisions used for R-P03-04: Annex III points 3.1 and 3.2.
- **CL-P03-03** -> C-P03-03 -> R-P03-02, R-P03-04 -> CS-P03-001, CS-P03-003 -> P03_PR01 Article 10(1); P03_PR03 Annex III point 3.3 -> FE-001, SHA-256 `01D5BDB1...6888`. Cross-provision used for the coupling: Annex III point 6.
- **CL-P04-01** -> C-P04-01 -> R-P04-06, R-P04-07, R-P04-08, R-P04-10, R-P04-11 -> CS-P04-003, CS-P04-004, CS-P04-005, CS-P04-006, CS-P04-007, CS-P04-008 -> P04_PR02 Article 13; P04_PR03 Article 14; P04_PR04 Article 14 -> FE-003, 32004R0874, OJ L 162 of 30.04.2004, SHA-256 `62AFB4DD...1449` (full value above).
- **CL-P04-02** -> C-P04-02 -> R-P04-02, R-P04-03, R-P04-01 -> CS-P04-002, CS-P04-001 -> P04_PR01 Article 12(5) -> FE-003, SHA-256 `62AFB4DD...1449`.
- **CL-P04-03** -> C-P04-03 -> R-P04-13, R-P04-15, R-P04-17 -> CS-P04-009, CS-P04-010, CS-P04-011 -> P04_PR05 Article 15(1) -> FE-003, SHA-256 `62AFB4DD...1449`.
- **CL-P04-04** -> (no configuration) -> R-P04-21, R-P04-20 -> CS-P04-014, CS-P04-013 -> P04_PR06 Article 23(1); P04_PR06 Article 22(6) -> FE-003, SHA-256 `62AFB4DD...1449`.

## 3. Architecture-level sufficiency check (V8 inference rule 4)

V8 rule 4 requires, for a claim from configurations to architecture: problem and scale, qualified coupling, configurational consequence, alternatives, boundary limitations; and V8 section 6.6 names the significance factors (authority, centrality, exclusivity, sequence, consequence, substitutability). The same check applies to both cases.

| Requirement | P03 (frozen statements) | P04 (frozen statements) |
|---|---|---|
| Problem and scale | Problem can be stated for the sampled sub-pathway (who verifies a manufacturer's quality system). The scale (the Directive or the Annex III route) is not fixed by the six statements. | Problem can be stated for sub-pathways (validation of prior rights; independent audit; escrow). No single problem unites them in the frozen set, and the scale (Regulation, phased registration, Registry operation) is not fixed. |
| Qualified coupling | One textual coupling: C-P03-03 (designation to verification via Annex III point 6). It links two relations only. | Couplings are within configurations (the term 'validation agent'; 'that agreement'). Across configurations the only link is a shared actor (Registry; Commission), which is insufficient. |
| Configurational consequence | Not evidenced: the legal effect of the assessment decision, the market-access consequence of verification and any supervision of the verifier are not in the frozen statements (U-05, U-11). | Not evidenced: what follows from the agent's notification, the audit report or the consent is not in the frozen statements (U-18, U-23). |
| Significance factors | Authority: consequence uncoded. Centrality, exclusivity, sequence, substitutability: not assessable; Article 9 shows alternative routes (U-10). Frequency of notified-body relations (3 of 6 accepted) is not evidence of significance. | Authority: consequence uncoded. Sequence: the applicant-agent-Registry order is stated within C-P04-01 but its necessity for registration is not in the frozen statements. Substitutability and exclusivity: not assessable. Frequency of Registry relations (10 of 13 accepted) is not evidence of significance. |
| Alternatives | Groupings C-P03-01 to C-P03-03 can be split or merged without changing any member (see configurations file); no architecture-level alternative can be weighed without consequence evidence. | As P03; in addition a Registry-centred grouping and a Commission-facing grouping were considered and not accepted (C-P04-05, U-29). |
| Boundary limitations | Six statements from three provision anchors of one Directive (Article 10(1), 10(2), Annex III 3.3 and 4.3); formal text only; container fallacy applies to any whole-Directive claim. | Fourteen statements from six anchors of one Regulation; Article 22(7) excluded; formal text only; container fallacy applies to any whole-Regulation claim. |

Conclusion for both cases: the frozen statements support relation-level and candidate configuration-level claims; they do not supply configurational consequence or significance evidence, so no architecture-level claim is warranted.

## 4. Claims considered and declined

| ID | Case | Claim considered | Reason declined | What would be needed |
|---|---|---|---|---|
| DC-P03-01 | P03 | The Directive's conformity-assessment arrangement is an intermediated or third-party-assurance architecture. | One verification configuration and one designation configuration, with consequence and necessity unevidenced; Annex III is one of alternative routes (Article 9); this is the legal atomistic fallacy if inferred from the presence of the notified body (V8 section 6.8) and the stopping-rule example of section 6.10. | Evidence that verification by designated bodies is a necessary or consequential step across the relevant pathways (for instance the legal effect of the decisions and the other routes). |
| DC-P03-02 | P03 | An accreditation/assurance chain (Member States to notified body to manufacturer). | Only designation and verification links are evidenced; no control over the verifier (supervision, annulment) is in the frozen statements; V8 describes this chain by governance of the verifier plus verification of the target. | Evidence of control or supervisory relations over the notified body. |
| DC-P03-03 | P03 | Delegated governance (transfer of capacity from Member States to notified bodies under control). | Designation confers task capacity, but retained control (oversight, review, revocation) is not evidenced; V8 requires a legally constituted transfer under some control. | Control relations (R-P03-09 was rejected for lack of text). |
| DC-P03-04 | P03 | The Commission supervises or controls designated entities (hierarchical or meta-regulatory reading). | Commission is only a recipient of information (R-P03-08 rejected). | Powers of the Commission over notifications or designations. |
| DC-P03-05 | P03 | Notified-body accountability to the manufacturer or to Member States. | Information to the audited party only (R-P03-10 rejected). | Forum assessment power or consequences for the notified body. |
| DC-P04-01 | P04 | The phased-registration validation is an intermediated architecture with validation agents as gatekeepers. | Agents' consequence and indispensability are not in the frozen statements (what the Registry does with the notification is outside the set); sequence is stated but necessity is not (V8 sections 6.6 and 6.12). | Legal effect of the agent's finding on registration; evidence that no alternative path exists. |
| DC-P04-02 | P04 | A Registry-centred delegated or hierarchical architecture. | The Registry's presence as a party in 10 of the 13 accepted relations is frequency and shared-actor adjacency (V8 frequency fallacy; inference rule 4). Registry's relations differ in function (appointment, selection, control, contract, notification). | Evidence of configurational structure showing where authority and sanction concentrate. |
| DC-P04-03 | P04 | Commission oversight or meta-regulation of the Registry (consent, consultation, audit reports to the Commission). | Information and a consent are not shown to confer assessment, consequence or reviewability; the audited party is not in the frozen statements (R-P04-05 deferred); grouping rests on a shared actor (C-P04-05). | Audit object; Commission powers on receipt of the report; effect of consent. |
| DC-P04-04 | P04 | The audit gives accountability of the Registry to the Commission. | Reporting alone is information; forum assessment and consequence not stated; audit object and independence unevidenced (R-P04-04, R-P04-05 deferred). | Same as DC-P04-03. |
| DC-P04-05 | P04 | Validation agent accountable to the Registry (accountability relation). | R-P04-12 rejected: no duty to justify, no assessment power, no consequence stated. | Text establishing those components. |
| DC-P04-06 | P04 | ADR channel as a configuration (Registry list, complainant choice, provider notification). | Complainant-side relation deferred (actor unexpressed); dispute-resolution function not evidenced by the frozen set (Article 22(7) excluded); C-P04-04 deferred. | A decision on the actor of CS-P04-012 and statements on the provider's examination and decision functions. |
| DC-X-01 | P03 and P04 | Any cross-case claim (shared pattern of designation or selection, or a common regime). | Two different instruments; the register provides no link; a shared label for selection or notification is common terminology (inference rule 4) and not a regime boundary decision. | A registered regime-boundary decision and evidence linking the instruments. |
| DC-X-02 | P03 and P04 | A governance regime for either case (e.g. a regime for conformity assessment of telecommunications terminal equipment or for the .eu domain). | Regimes may extend beyond a single instrument and their boundaries are inferential questions (V8 section 6.2); no separate regime-boundary decision is made and none could be justified from 20 statements of two instruments. | Explicit regime-boundary decision with evidence of laws, organisations and standards forming the system. |
| DC-X-03 | P03 and P04 | A governance logic (hierarchical, professional, market, etc.) for either case. | Logic is inferred from coordination and authority patterns after lower-level coding; authority consequences are not evidenced. | Authority and coordination pattern evidence across configurations. |

## 5. Stopping-rule decisions

- **SR-P03:** analysis stops at candidate configuration level. The highest-level claims are CL-P03-01 to CL-P03-03. The architecture-level claim is deferred: configurational consequence and significance factors are unevidenced (U-05, U-10, U-11).
- **SR-P04:** analysis stops at candidate configuration level for C-P04-01, C-P04-02 and C-P04-03. The architecture-level claim is deferred: consequences (U-18, U-23) and significance factors are unevidenced, and the groupings across configurations rest on shared actors only (U-29).
- **SR-P04-ADR:** the ADR channel stops at relation level (R-P04-20, R-P04-21); the configuration is deferred (U-25, U-30).
- **SR-P03-004 and SR-P04-012:** the statements whose actor is not expressed (CS-P03-004, CS-P04-012) stop at statement level (`human_review_needed`).
- **Regime decision:** no regime-boundary decision was made for either case (default: stop below regime).

## 6. Properties borne by the claims

The bearer of each property stated in the claims is the relationship or configuration named, not an actor or the Directive/Regulation as a whole. For instance 'derivation by designation' is an attribute of R-P03-02 and R-P03-03, not of the bodies in general; 'information component only' is an attribute of R-P04-01, R-P04-11, R-P04-17 and R-P04-20 individually. No actor-level property (for instance 'the Registry has broad authority') is asserted.

## 7. Formal-text limit

All claims concern formal legal text (V8 section 6.14: formal architecture). Nothing in this file asserts that any arrangement is implemented, operates as designed, or is effective (functional and implementation fallacies).
