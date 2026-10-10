# Theory problems encountered — GDPR Pilot 01

**Status:** recorded **without** revising the manuscript or the frozen ontology (directive Part XI). Each entry says what kind of problem it suggests: **L** legal interpretation; **R** missing coding rule; **O** ontological ambiguity; **I** inferential limitation; **E** unresolved external dependency; **S** possible substantive revision of RGAM.

| ID | Problem | Where it arose | Kind | Suggests |
|---|---|---|---|---|
| TP-01 | **Functionally defined positions.** Controller, processor, joint controllers, supervisory authority concerned, lead supervisory authority and recipient are roles defined by conduct or facts, not offices established by norm. "Position = legally specified place" does not fit | Art. 4(7),(8),(16),(22),(9); Art. 56(1) | O | Distinguish *constituted positions* from *conduct-defined roles* in the ontology; role-based positions may need no type/instance structure |
| TP-02 | **Mediated constitution.** The supervisory authorities are constituted by Member State law under a Union obligation (Arts 51(1), 54(1)(a)). N1–N4 assume that one instrument constitutes the entity. The GDPR's "formal architecture" contains the obligation, the competence and the type-level tasks and powers, not the authorities | Chapter VI; AI-07 | O, S | Add a norm type or a rule for constitution mediated by another legal order; state which legal order constitutes what (V6's "legally constituted" is silent on this) |
| TP-03 | **Designation versus establishment.** DPO, representative, joint representative, accredited bodies: the Regulation specifies the office; a private or national act produces the instance | Arts 27, 37, 41, 43, 51(3), 68(4) | R | Separate "designation" norm type or extend N2 explicitly |
| TP-04 | **Procedures as devices.** Whether cooperation, consistency, urgency, mutual-assistance and joint-operation procedures are institutional devices | Arts 60–66 | O, R | Resolve the DEV threshold or recognise "procedure" as a kind (HQ-001) |
| TP-05 | **Relation-type inventory.** V6's ten types lack peer cooperation, consultation, escalation, standstill, liability allocation and jurisdiction rules; 44.5% of QR typed as information/reporting | Chapters V–VIII | R, S | Secondary subtypes or an additional type proposed to David (HQ-007) |
| TP-06 | **Relation-pivot limit.** The pivot leaves assignments without counterparty (self-regulatory duties) outside S and A; 35 NA form a candidate S with no relation. Properties such as self-regulatory autonomy and discretion cannot be reconstructed from relations alone | Arts 5(2), 24, 25, 32, 35 | I, S | Allow assignments to bear S-level properties; or state that relational reconstruction covers only the relation-bearing part of an instrument |
| TP-07 | **Accountability thresholds.** Questioning capacity is rarely stated explicitly in the text; only a cross-provision derived relation reaches full AC; judicial review's content is national law | Arts 41, 43, 64–65, 78, 92 | R, E | Decide whether institutionally implied questioning counts (HQ-006) |
| TP-08 | **Derived versus direct accountability.** AC emerges only across provisions (5(2), 24(1), 58, 83); DR-10 does not say how many provisions may be combined | Arts 5, 24, 58, 83 | R | A derivation rule for cross-provision relations (HQ-005) |
| TP-09 | **Self-modifying scope.** Member State law may derogate from the Regulation's own chapters on supervision and consistency (Arts 85(2), 90; also 23, 89) | Chapter IX | I, E | I4 should include a "scope conditional on derogation" test; boundary notes on every AI record (HQ-015) |
| TP-10 | **Temporal indexing.** Provision-level dates (24 May 2016; 25 May 2018; 25 May 2020) are not coded; legal status is baseline-uniform; the effective date of the Board's N1 establishment is not unit-stated | Arts 68, 92, 99 | R | Unit-level temporal reference (UNC-013; HQ-004) |
| TP-11 | **Analyst-defined S discovery.** Predicates written by the same agent after extraction; false positives; potential encoding of expectations | `reconstruct.py`; SC-10 | I | Independent re-discovery; comparison with a documented clustering method (HQ-008) |
| TP-12 | **Coupling criteria.** "Shared downstream use" (24(3), 28(5), 32(3), 83(2)(j)) was not accepted as coupling between codes and certification; this is a threshold choice that decides AI-04 | AI-04 | I | Adjudication of I2 thresholds (HQ-009) |
| TP-13 | **Optionality.** Voluntary layers (codes "may", certification "voluntary") complicate conditions such as V6's "institutionalized enhancement" | AI-09 | I | Conditional-architecture notion or a rule on optional layers (HQ-013) |
| TP-14 | **External dependencies are decisive.** National law constituting SAs; Reg. 182/2011; Reg. 765/2008; EDPS instrument; courts' procedure. Absence-dependent claims hold only within W | Several | E | Targeted retrieval, case by case (HQ-010); no automatic corpus expansion |
| TP-15 | **Unnamed legislators.** "Union or Member State law" as source of competence is neither a position nor a relation party; 20 NA with unstated subject | Arts 1(3), 6(3), 23, 49(5), 85, 89 | O | Treat as norm-source/competence without a position (HQ-012) |
| TP-16 | **Granularity.** Paragraph-level extraction of lists of tasks and powers loses point-level distinctions | Arts 4, 57, 58, 70, 83 | R | Point-level coding for governance-bearing lists |
| TP-17 | **Recital use.** No recital review; interpretive questions unresolved | e.g. Art. 62(7) | L | Recital pass per unit with explicit rules |
| TP-18 | **Direction convention.** Origin = obligor / subject of the statement; governance direction in `type_note`; rights stated from the right-holder's side invert the V6 reading | DR 1.1–1.2 | R | A two-field direction (statement direction and governance direction) |
| TP-19 | **Same observation, several provisions.** Complaint-handling duty appears under 57(1)(f), 77(2) and 60(7) (UNC-005). The many-to-many rule was applied only partly | Chapter VIII | R | Canonical relation IDs with linked support; deduplication pass |
| TP-20 | **Single evaluator.** No inter-coder reliability; repetition by the same model is not reliability | all | I | Independent human coding (directive Part VIII) |

## Candidate substantive revisions of RGAM suggested by the pilot (not made)

1. A norm-type or constitution rule for **mediated constitution** (TP-02) and **designation** (TP-03).
2. Distinguish **constituted positions** from **conduct-defined roles** (TP-01).
3. Allow **assignments without counterpart** to carry S-level properties (TP-06).
4. A **scope-conditionality test** inside I4 (TP-09).
5. A rule for **derived accountability** (TP-08).
These are proposals for human decision; the manuscript and the frozen ontology were not changed.
