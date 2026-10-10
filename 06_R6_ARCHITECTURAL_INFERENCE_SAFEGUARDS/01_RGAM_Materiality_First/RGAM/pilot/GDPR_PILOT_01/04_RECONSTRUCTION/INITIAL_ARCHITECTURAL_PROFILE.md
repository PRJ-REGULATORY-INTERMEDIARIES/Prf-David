# Initial architectural profile of the GDPR baseline text — GDPR Pilot 01

**Status:** `MACHINE_PROVISIONAL`, exploratory, single evaluator. A *profile*, not a classification: properties are stated per bearer and scale (S or A), with their evidential status. No score, no label for the instrument as a whole. Counts are composition (V6 §6.6: "counts identify composition; configurations identify organization").
**Baseline:** Regulation (EU) 2016/679, OJ L 119, 4.5.2016, with the 2018 corrigendum; **not** asserted to be the currently applicable GDPR.
**What the profile covers:** 389 paragraph units screened; 321 yielded at least one record; 238 qualified relations, 157 normative assignments, 47 positions/devices, 22 external-reference rows (about 16 distinct sources).

## 1. Composition (descriptors only)

- **Relation types (238 QR):** information/reporting 106; authority/control 41; representation/participation 23; beneficiary/protective 19; delegation/authorization 15; oversight/supervision 11; review/adjudication 11; contractual/exchange 7; verification/assurance 5. (The dominance of "information/reporting" is partly an artefact of the type inventory — UNC-006.)
- **Modality:** QR — obligation 163, competence 27, entitlement 24, permission 17, declaratory 4, prohibition 3. NA — obligation 88, competence 27, permission 23, declaratory 7, other 12.
- **Relations by sector of origin → counterpart:** public→public 101; public→regulated side 30; regulated side→public 17; regulated side→regulated side 21; regulated side→data subject 45; public→data subject 17; other 7. The large public→public block is mainly Chapter VII; it says nothing about significance.
- **Derivation:** 231 of 238 QR are direct; 7 are derived (including the BCR content requirements and the Art.33(5) documentation duty).
- **Origin of relations by position type (QR origin, function-grouped):** supervisory authorities 92 (information 21; enforcement/sanction 18; cooperation 17); controllers 53 (information 29; remediation 9); the Board 27; Member States 18; certification/monitoring bodies 8; the Commission 6 as QR origin (its main role is as holder of competences recorded as NA); data-protection officer 5.

## 2. Establishment and constitution profile (D03/N1–N4)

| Finding | Evidence (provisions) | Note |
|---|---|---|
| **One body established by explicit N1 wording** | Art. 68(1): the Board "is hereby established as a body of the Union and shall have legal personality"; corroborated by Art. 94(2) ("the European Data Protection Board established by this Regulation") | Found by pattern search over the working text; no other "hereby established" body. Effective date (24 May 2016 vs 25 May 2018) not stated unit by unit (HQ-004) |
| **Competence conferred directly (N1-like, a power, not an entity)** | Art. 92(1)–(2): power to adopt delegated acts "conferred on the Commission" from 24 May 2016 | |
| **N2: obligation to provide for / designate / ensure** | Arts 51(1), 54(1)(a) (supervisory authorities: "provide for", "provide by law for the establishment"); 37(1), 27(1), 51(3), 68(4) (designation of DPO, representative, representing authority); 43(1) (accreditation); 58(5) (power to litigate "by law"); 53(1) (appointment procedures) | The supervisory authorities are **constituted by Member State law**; the GDPR contains the obligation and the competence at type level |
| **N2: register duties (not "established")** | Arts 40(11), 42(8), 70(1)(o), 70(1)(y): the Board "shall collate … in a register" / "maintain a public register" | Registers are legally required, not N1-established |
| **N2-promotional** | Arts 40(1), 42(1): "shall encourage" codes of conduct and certification mechanisms | The mechanisms are not constituted by these units |
| **N3-like competences/permissions** | Commission acts (28(7), 40(9), 43(8) with Art.92, 43(9), 45(3), 47(3), 61(9), 67); SA adoption of standard clauses (28(8)); Member State options (36(5), 80(2), 83(7), 58(6)) | Competence ≠ instrument; instruments exist only if adopted |
| **N4-type temporal effect** | Art. 99(1) (entry into force 24 May 2016, computed from publication on 4 May 2016), 99(2) (application 25 May 2018); provision-level dates elsewhere | Not coded unit by unit (UNC-013) |
| **Devices** | 13 PD records of kind `device`; ten flagged DEV-threshold (procedures such as Arts 60–62, 63, 66; schemes such as codes, certification, BCR, SCC) | Whether procedures are devices is open (HQ-001) |
| **Material establishment and observed exercise** | **Not assessed** (layer X; DR §4(5)) | Every device carries `establishment_evidence = not_assessed` |

## 3. Dimensions of V6 §5.2.1, per bearer (status of each statement)

| V6 dimension | Bearer / scale | Statement supported by the pilot evidence | Status |
|---|---|---|---|
| Centralization | S/A per case type | First-instance competence is national (Arts 55–56); resolution of disputes among authorities is concentrated in the Board (Art. 65); secondary rule-making by the Commission (SC-08) | Determinate at type level for stated case types (AI-02/03) |
| Directness and intermediation | S per function | Monitoring: direct SA supervision (Art. 58) coexists with *optional* private monitoring and certification bodies (Arts 41, 43) and an internal DPO; enforcement and fines: direct (SA), judicial review | Candidate; intermediation of monitoring is conditional (AI-09) |
| Public–private allocation | A/S per function | Rule-making: public (Commission, SAs, Member States) with private standard-setting by associations (Art. 40(2)) and groups (Art. 47); monitoring/verification: public with private layers; enforcement: public with private sanction by monitoring bodies (Art. 41(4)) | Candidate descriptor |
| Self-regulatory autonomy | S | Controllers design risk-based "appropriate measures" (Arts 24, 25, 32, 35); 35 assignments without counterpart (SC-15); enhancement by third parties is optional | Candidate (AI-09); autonomy not quantified |
| Vertical distribution | A | Member State level (authorities, courts, specification competences) and Union level (Board, Commission, EP/Council) with coupling clauses (Arts 51(2),(3), 52(4), 58(6), 68(3)) | Determinate at type level (AI-07) |
| Decision-centre plurality | A | Not computable: national authorities have `legal_multiplicity` "one or more" per Member State and are constituted outside W (PT-7) | **Undetermined** |
| Relational depth | S per chain | Certification chain as stated in W: Commission (Art. 43(8),(9)) → Board/SA (criteria, requirements, Arts 42(5), 43(3)) → accreditor (SA or national accreditation body, Art. 43(1)) → certification body → controller/processor (Art. 42(5),(7)); cross-border enforcement chain: controller/processor ← lead SA ← concerned SAs ← Board (Arts 56, 60, 65) | Candidate; depth stated as a legal chain, not a metric |
| Functional allocation | A | Counts by position and function are in `profile_stats.json` (composition only): e.g. SAs hold information, enforcement and cooperation functions; the Board mostly information/opinion and dispute resolution; controllers mostly information duties toward data subjects | Composition only |
| Discretion distribution | A (profile by function × position × relation) | **Not built.** Discretion was not coded as an attribute in the pilot | **Not done** (no score would be produced in any case: D09-W05) |
| Accountability structure | A | See §5: no unit satisfies all elements; one cross-provision derived ACCOUNTABILITY relation | Candidate |

## 4. Status profile (D03)

- **Legal constitution evidenced (baseline):** all operative provisions of the authentic text for the stated version; this is a claim about the *text*, not about the entities it mentions.
- **Entities legally constituted within W:** the Board (N1) and powers conferred by the text; **not** the national authorities, the DPO, the representative, the registers or the certification/accreditation bodies as instances.
- **Material establishment:** not assessed. **Observed exercise:** not assessed.

## 5. Accountability screening (DR-10, v0.6.1 four classes with separate sufficiency)

| Relation (actor → forum) | Provisions | Elements present | Elements missing / external | Class (sufficiency) |
|---|---|---|---|---|
| Controller/processor → SA | 5(2), 24(1), 58(1)(a),(b),(e), 58(2), 83 | duty to demonstrate; forum SA; questioning (order information, access, audits); assessment (warnings, reprimands, orders); consequences (limitations, fines) | single provision stating all; the relation is **derived across provisions** | **ACCOUNTABILITY, derived** (sufficient at W level; HQ-005) |
| Competent SA → Board | 64(7),(8) → 65(1)(c) | duty to take utmost account and to give grounds; assessment/judgment; binding consequence | questioning capacity not stated | ANSWERABILITY (+assessment, +consequence) — not AC under D10 (HQ-006) |
| Monitoring body → SA | 41(2),(4),(5) | duty to inform with reasons; assessment; revocation | questioning not stated | ANSWERABILITY candidate |
| Certification body → SA | 43(2),(5),(7); 58(2)(h) | duty to give reasons; assessment; withdrawal/revocation | questioning not stated | ANSWERABILITY candidate |
| Requested SA → requesting SA | 61(5),(8); 66(2) | reasons for refusal; consequence (provisional measure; urgent Board decision) | questioning not stated | ANSWERABILITY candidate |
| SA concerned → SAs, Board, Commission | 66(1) | reasons communicated; consequence via 66(2)–(4) | questioning not stated | ANSWERABILITY candidate |
| SA → courts | 78(1)–(4) | forum identified; judicial assessment; remedy | duty of explanation beyond 78(4); remedy content is national law | **Indeterminate** (external) |
| SA → complainant | 57(1)(f), 77(2), 60(7) | duty to inform on progress/outcome; judicial route | questioning, assessment | INFO / ANSWERABILITY candidate |
| Commission → EP/Council | 92(4),(5); 97(1) | notification/report; objection and revocation (92) | duty to justify; questioning | INFO + review/oversight relation (not accountability under DR-10) |
| SA → national parliament/government | 59 | annual report | forum capacities (national law) | INFO |
| Board → EP, Council, Commission | 71(1) | annual report | duty to justify; questioning | INFO |
| DPO → highest management | 38(3) | direct reporting | duty to justify; capacities | INFO |

No relation was classified ACCOUNTABILITY on a single provision. The **exercise** of accountability is not inferred for any of them.

## 6. Limits of this profile

Single evaluator and machine-provisional; point-level partial; S predicates analyst-defined; generic national-law dependencies incomplete; discretion not coded; no implementation or operation evidence; recitals not reviewed. The profile is a description of what the pilot's extraction supports, not a validated characterization of the GDPR.
