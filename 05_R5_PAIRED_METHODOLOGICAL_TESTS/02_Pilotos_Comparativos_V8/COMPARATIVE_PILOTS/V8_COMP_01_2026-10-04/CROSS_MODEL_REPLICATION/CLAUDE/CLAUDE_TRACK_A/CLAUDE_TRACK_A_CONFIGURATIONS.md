# Claude Track A - Candidate governance configurations (V8 only)

Evidence base: the 20 frozen statements (register SHA-256 `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F`); relationships in `CLAUDE_TRACK_A_RELATIONSHIPS.csv`. Sources: P03 = FE-001 / 31991L0263 (SHA-256 `01D5BDB117B370AE9DAD7F3ABB151583A75519CBAD0E7808EFC9040C8D656888`); P04 = FE-003 / 32004R0874 (SHA-256 `62AFB4DDCCAE5E7157590B1386040AA8D160701D7194DBD2F2403AC4B6781449`).

## Rules applied

- A configuration is a stated combination of relationships, elements and attributes organised around a function, stage or problem (V8 codebook; V8 section 6.5). Membership may overlap.
- A single information relation does not make a system. Receiving, assessment or follow-up must be evidenced before a "reporting system" is claimed (inference rule 3).
- Shared actors, repeated wording and adjacency are not grounds for a configuration (inference rule 4 applies the same caution one level up).
- Candidate groupings below are not architectural conclusions. Every accepted configuration is stated at `claim_level = configuration` and is formal-text only; nothing is inferred about implementation, practice or effectiveness.
- Only ACCEPTED relationships are members. Deferred or rejected relationships are listed as "missing or excluded", so that each configuration shows what it lacks.

## Summary

| ID | Case | Short name | Decision | claim_level | Members (accepted) |
|---|---|---|---|---|---|
| C-P03-01 | P03 | Designation and notification of conformity bodies and laboratories | ACCEPTED (candidate, thin) | configuration | R-P03-01, R-P03-02, R-P03-03 |
| C-P03-02 | P03 | Notified-body verification of the manufacturer's quality system | ACCEPTED (candidate, partial) | configuration | R-P03-04, R-P03-05, R-P03-06 |
| C-P03-03 | P03 | Designation-to-verification link for the verifier | ACCEPTED (candidate, thin; cross_provision_inference) | configuration | R-P03-02, R-P03-04 |
| C-P04-01 | P04 | Registry-selected validation of prior-right claims | ACCEPTED (candidate, partial) | configuration | R-P04-06, R-P04-07, R-P04-08, R-P04-10, R-P04-11 |
| C-P04-02 | P04 | Appointment and reporting around the independent audit | ACCEPTED (candidate, narrow) | configuration | R-P04-02, R-P04-03, R-P04-01 |
| C-P04-03 | P04 | Escrow arrangement with Commission consent | ACCEPTED (candidate, partial) | configuration | R-P04-13, R-P04-15, R-P04-17 |
| C-P04-04 | P04 | Registry-curated ADR provider channel | DEFERRED (held at relation level) | relation | R-P04-21, R-P04-20 (isolated) |
| C-P04-05 | P04 | Commission-facing touchpoints toward the Registry | DEFERRED / not accepted | none | (R-P04-01, R-P04-03, R-P04-15 considered) |

## P03 configurations

### C-P03-01 Designation and notification of conformity bodies and laboratories

- **Organising problem / function:** which entities carry out certification, product checks, surveillance and tests for the Article 9 procedures, and how the Commission is told about them.
- **Members:** R-P03-01 (Member States to Commission, information on designated entities; CS-P03-001, CS-P03-002); R-P03-02 (Member States designate bodies; CS-P03-001); R-P03-03 (Member States designate laboratories; CS-P03-002).
- **Elements and attributes:** actors Member States, Commission, designated bodies and laboratories (categories); functions information provision and authorization/designation; mechanisms Information and Authorization; instrument notification; authority: designation is the source of the entities' task capacity (derivation), Commission holds no stated power; discretion not coded; accountability: information component only.
- **Theoretical pattern:** designation of performers paired with notification of their identity to a central recipient (a designation-and-registration pairing). The designation relations are thin (U-01).
- **Not established:** that the Commission assesses, accepts, publishes or follows up the notifications (receiving without assessment or follow-up in the frozen statements, so no notification or reporting system is claimed); any criteria for designation; any oversight or withdrawal of designation (R-P03-08 and R-P03-09 rejected); that notification is a condition of the entities' capacity.
- **Overlap:** R-P03-02 is also a member of C-P03-03.
- **Alternative reading:** two separate configurations (one for bodies, one for laboratories) are possible (U-03); nothing downstream depends on the choice.
- **claim_level:** configuration (candidate). coding_status: direct_text for members; the pairing is an analyst grouping.

### C-P03-02 Notified-body verification of the manufacturer's quality system

- **Organising problem / function:** verification that the manufacturer's quality system satisfies the stated requirements, and that it is maintained and applied.
- **Members:** R-P03-04 (assessment of the quality system; CS-P03-003); R-P03-05 (periodic audit; CS-P03-005); R-P03-06 (audit report to the manufacturer; CS-P03-006).
- **Elements and attributes:** actors notified body (verifier) and manufacturer (verified party); function verification/assurance with monitoring; mechanisms Verification and Information; instruments quality-system assessment, audit, audit report; authority: capacity to assess and audit, legal consequence not stated; discretion: indicator only for the timing of audits ('reasonable intervals'); accountability: none constituted (information goes to the audited party).
- **Theoretical pattern:** a partial third-party assurance configuration (assessment, periodic audit, report). The V8 third-party assurance example also includes recognition of the verifier, reporting to a public authority and retained supervisory powers; the first appears only across configurations (C-P03-03), the other two are absent from the frozen statements.
- **Not established:** the legal effect of the assessment decision (R-P03-11 deferred); who notifies the decision (R-P03-07 deferred, actor unexpressed); any supervision of the notified body; accountability of the notified body to any forum (R-P03-10 rejected); that the manufacturer is obliged to use this route (Article 9 offers alternative routes, U-10); gatekeeping, indispensability or market-access consequence.
- **Overlap:** R-P03-04 is also a member of C-P03-03. R-P03-05 and R-P03-06 share the same dyad with R-P03-04; they were kept separate relations (different instruments) and grouped here because they share the verification function.
- **Alternative reading:** assessment (initial stage) and audit plus report (surveillance stage) could be two configurations; a single grouping is used because the same actors and function recur and the statements are connected by the same instrument family. No claim depends on the choice.
- **claim_level:** configuration (candidate).

### C-P03-03 Designation-to-verification link for the verifier

- **Organising problem / function:** who may act as verifier of a manufacturer's quality system, and what that verifier does.
- **Members:** R-P03-02 (designation of bodies) and R-P03-04 (assessment by 'notified body').
- **Qualified coupling:** the term 'notified body' in Annex III is tied to the bodies of Article 10(1) by Annex III point 6 ('Each notified body referred to in Article 10(1)'), read as a cross-reference. The coupling is therefore textual (identity of the actor class), not mere shared vocabulary; it is nevertheless a cross_provision_inference.
- **Theoretical pattern:** governance of the verifier (designation) preceding verification of the target, which is a two-link instance of the V8 'governance of verifier plus verification of target' pattern. Only two links of the chain are evidenced.
- **Not established:** control over the verifier after designation (supervision, annulment, withdrawal: not in the frozen statements); the position of the Commission in this chain; whether the designated body must be used; the effect of verification.
- **Overlap:** R-P03-02 with C-P03-01; R-P03-04 with C-P03-02.
- **Alternative reading:** C-P03-03 is a sub-link of C-P03-01 plus C-P03-02 and adds a coupling claim only; it could be dropped without losing any member relation.
- **claim_level:** configuration (candidate, thin).

## P04 configurations

### C-P04-01 Registry-selected validation of prior-right claims

- **Organising problem / function:** verification of applicants' prior-right claims during phased registration.
- **Members:** R-P04-06 (Registry selects validation agents; CS-P04-003); R-P04-07 (Registry requires objective, transparent, non-discriminatory conduct; CS-P04-004); R-P04-08 (applicant submits evidence to an agent; CS-P04-005); R-P04-10 (agent examines the claim; CS-P04-006); R-P04-11 (agent notifies the Registry of the outcome; CS-P04-007, CS-P04-008).
- **Elements and attributes:** actors Registry, validation agents, applicants; functions authorization/designation, implementation (conduct requirement), information provision, verification/assurance; mechanisms Authorization, Command, Information, Verification; instruments selection, evidence submission, validation examination, notification; authority: Registry selects and requires, agents examine, legal effect of findings not stated; discretion: constrained selection (stated criteria), examination standard not stated; accountability: information components only, agent not answerable to the Registry on this text (R-P04-12 rejected).
- **Theoretical pattern:** a partial third-party assurance configuration: selection of a verifier by an actor, evidence from the verified party, examination, and reporting back to the selecting actor, with a conduct requirement on the verifier. Position labels such as regulator or principal are not assigned to the Registry (V8: positions are relational).
- **Not established:** what the Registry does after the agent's notification and the legal effect of the finding on the applicant (U-18); supervisory, review or withdrawal powers over the agents beyond the conduct requirement; the applicant's remedies; how an agent becomes 'relevant' (R-P04-09 deferred, U-17, U-19); that agents are indispensable or exclusive; any implementation or practice.
- **Overlap:** none by relationship with the other accepted configurations. The Registry is a party in C-P04-01, C-P04-02 and C-P04-03 and the parallel wording of CS-P04-003 and CS-P04-014 recurs; neither is used as a ground for grouping (U-29).
- **Alternative reading:** two configurations (agent selection and control; applicant-agent-Registry validation sequence) could be stated; they are grouped here because R-P04-10 and R-P04-11 depend on the agents created by R-P04-06 through the common term 'validation agent', which is a textual identity within Article 13 and Article 14.
- **claim_level:** configuration (candidate).

### C-P04-02 Appointment and reporting around the independent audit

- **Organising problem / function:** an independent audit at the end of the phased registration, its appointment and its reporting.
- **Members:** R-P04-02 (Registry appoints the auditor; CS-P04-002); R-P04-03 (Registry consults the Commission first; CS-P04-002); R-P04-01 (auditor reports findings to the Commission; CS-P04-001).
- **Elements and attributes:** actors Registry, auditor, Commission; functions authorization/designation, verification/assurance, information provision; mechanisms Authorization, Participation, Verification, Information; instruments appointment, independent audit; authority: appointing power with the Registry, no stated power of the Commission over findings; discretion: Registry's choice conditioned on consultation; accountability: information to the Commission only.
- **Theoretical pattern:** appointment, consultation and report around an audit. The claim is narrow: that these three relations are organised around the audit.
- **Not established:** that the audit verifies the Registry or that the Registry is accountable to the Commission through it (the audited party is not stated in the frozen statements: R-P04-05 deferred, U-13); that the auditor's independence from the Registry is secured or compromised (R-P04-04 deferred, U-14); any Commission assessment or consequence of the report; whether the audit occurs in practice.
- **Overlap:** none by relationship. The Commission is also a party in C-P04-03 (see C-P04-05).
- **Alternative reading:** the grouping could be two configurations (appointment; reporting); it is kept as one because both concern the same audit.
- **claim_level:** configuration (candidate, narrow). The accountability or verification reading of the audit is deferred.

### C-P04-03 Escrow arrangement with Commission consent

- **Organising problem / function:** keeping a copy of the .eu database with an escrow agent under an agreement that requires prior Commission consent.
- **Members:** R-P04-13 (Registry-escrow agent agreement; CS-P04-009); R-P04-15 (Commission consent to the agreement; CS-P04-010, CS-P04-009); R-P04-17 (daily deposit; CS-P04-011).
- **Elements and attributes:** actors Registry, escrow agent (category), Commission; functions implementation (safeguard arrangement), authorization/approval, information provision; mechanisms Contract, Authorization, Information; instruments escrow agreement, prior consent, daily deposit; authority: Commission holds an approval position, Registry duties to conclude and deposit; discretion: not coded for the Commission; accountability: none constituted.
- **Theoretical pattern:** a contractual safeguard arrangement subject to ex ante approval by a third actor, with a recurring information transfer to the escrow agent. The purpose of the safeguard is not coded because it is not stated in the frozen statements.
- **Not established:** what the Commission as beneficiary may claim (R-P04-14 deferred, U-22); whether consent is a validity condition or can be withheld (U-23); terms of release or use of the data; the purpose or effectiveness of the escrow.
- **Overlap:** none by relationship. R-P04-15 was also considered for C-P04-05.
- **Alternative reading:** the approval relation could stand alone (authorization) and the contract plus deposit form the configuration; the three are grouped because R-P04-15 and R-P04-17 both refer back to the agreement of R-P04-13.
- **claim_level:** configuration (candidate).

### C-P04-04 Registry-curated ADR provider channel (DEFERRED)

- **Candidate stated combination:** Registry selects ADR providers (R-P04-21); complainants choose a provider from the Registry's list (R-P04-18, deferred); the provider informs the Registry of a filed request (R-P04-20).
- **Why not accepted:** the link between the Registry's selection and the complainants' choice rests on the deferred relation R-P04-18 (submitter not expressed, U-25); the dispute-resolution function itself (examination, decision) is not evidenced in the frozen statements (Article 22(7) excluded; U-30); the provider-to-Registry notification has no stated receiving or follow-up. What exists is two accepted relations that share the term 'ADR provider' and the cross-reference of CS-P04-012 to the list (U-26).
- **Treatment:** held at relation level (R-P04-21, R-P04-20); recorded as a candidate to be revisited if the actor of CS-P04-012 is decided by a human reviewer.
- **claim_level:** relation (no configuration claim). Status: deferred.

### C-P04-05 Commission-facing touchpoints toward the Registry (DEFERRED, not accepted)

- **Candidate grouping:** consultation by the Registry (R-P04-03), consent to the escrow agreement (R-P04-15) and audit reports (R-P04-01) as a pattern of Commission positions toward the Registry (ex ante approval and ex post reporting).
- **Why not accepted:** the three relations have different functions and instruments and are joined only by the Commission being a party (shared actor). The ex post element depends on the audit being an audit of the Registry, which is not in the frozen statements (R-P04-05 deferred). Calling it oversight of the Registry would treat information and a consent as a control structure without evidence of assessment, consequence or reviewability (U-29).
- **Treatment:** not recorded as a configuration; members stay in C-P04-02 and C-P04-03.
- **claim_level:** none.

## Cross-case note

No configuration spans P03 and P04. The two cases are provisions of two different instruments and the frozen set provides no link between them (container and ecological fallacies are avoided by not grouping them).
