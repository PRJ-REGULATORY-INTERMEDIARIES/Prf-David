# GDPR Pilot 01 — executive research report

**Date:** 3 October 2026 · **Status:** `MACHINE_PROVISIONAL` — exploratory, single evaluator (an AI agent directed by Igor Caires Machado), no independent coding, **not validation**. The theoretical baseline is `paper/MANUSCRIPT_v0_6_1.md` (Igor's preliminary contribution from David Levi-Faur's V6; not approved by David, Rotem or the team). Nothing below states that the GDPR "has" a given architecture, that any entity operates, or that RGAM is confirmed.

## 1. Corpus and version
Regulation (EU) 2016/679, OJ L 119, 4.5.2016, authentic text (EUR-Lex rendering) **with the 2018 corrigendum (OJ L 127, 23.5.2018) applied** (18 of 18 substitutions; the corrigendum changes Arts 37, 41–43, 57, 64–65, 69–70 and recital 71, several of them consequential for the accreditation and Board provisions). Entry into force 24 May 2016 (computed), application 25 May 2018. **This is a historical baseline, not asserted to be the currently applicable GDPR**; a possible 2021 corrigendum (CELEX R(03)) could not be retrieved and later amendments were not verified (HQ-014).

## 2. Actual coverage
- **Screening:** all 99 articles; **389 of 389 paragraph units** screened (382 point units inventoried automatically but screened inside their paragraph).
- **Detailed extraction:** article order, Chapters I–XI, **328 units extracted** (321 "Yes", 8 "Uncertain" with records, 1 on Hold), **60 units** with no governance observation. Complete at paragraph level, **partial at point level**; recitals not reviewed; external sources not retrieved.
- **Records:** 238 qualified relations, 157 normative assignments, 47 positions/devices, 22 external-reference rows (about 16 distinct sources), 15 extraction uncertainties, 16 human-adjudication items.

## 3. Supported legal observations (provisional)
1. **Only one body is directly established by the Regulation**: the Board (Art. 68(1), "is hereby established", N1; corroborated by Art. 94(2)).
2. **The supervisory authorities are not constituted by the GDPR**: Arts 51(1) and 54(1)(a) oblige Member States to provide for them by law (N2); the Regulation specifies their independence, competence, tasks and powers at type level. National instances, multiplicity and powers beyond the Regulation depend on national law outside W.
3. **Registers are legally required, not "established"**: Board duties to collate/maintain registers (Arts 40(11), 42(8), 70(1)(o),(y)) are N2.
4. **Commission rule-making is conferred as competences** (delegated acts: Arts 12(8), 43(8), 92; implementing acts: Art. 93(2)), controlled by Parliament/Council (92) and by a committee whose rules lie in Regulation (EU) No 182/2011 (not retrieved).
5. **A large part of the text assigns duties without a legally identifiable counterpart or forum** (35 regulated-side assignments, e.g. Arts 24(1), 25, 32(1), 35(1)).
6. **Accountability:** no unit satisfies all elements; one relation is classifiable as ACCOUNTABILITY only by derivation across provisions (controller/processor → SA: Arts 5(2), 24(1), 58, 83); eight relations are ANSWERABILITY candidates; reporting lines to institutions (Arts 59, 71, 97, 38(3)) are INFO.
7. **Optionality:** private enhancement (codes, certification) is optional (Arts 40(2), 42(3)).

## 4. Candidate subconfigurations
Fifteen analyst-defined candidates (SC-01…SC-15) from relation patterns, not chapters; 371 of 395 records placed, 24 unassigned (`SUBCONFIGURATIONS.md`). They include rights against controllers, SA oversight, controller–processor delegation, the DPO, codes of conduct, certification, cooperation and consistency, Commission rule-making, transfers, remedies, Member State specification, reporting lines, Board constitution, national SA constitution, and one made only of assignments (SC-15). Many cross chapters; some overlap heavily (e.g. SC-02/SC-07: 7 shared members).

## 5. Architectural inferences (I1–I4; `ARCHITECTURAL_INFERENCE_REGISTER.csv`)
| AI | Candidate whole | Outcome |
|---|---|---|
| AI-01 | Redress (SC-10; **seeded-draw trace**) | Integrated, simple case A=S; overlapping with SC-02/07; content of remedies indeterminate (national law) |
| AI-02 | Cooperation and consistency (SC-07; **largest-support trace**) | Integrated, simple case, at type level; claims depending on the national constitution of SAs or Treaty review indeterminate |
| AI-03 | SC-02 + SC-07 (supervision with cross-border consistency) | Overlapping / partially integrated: integrated only for cross-border processing |
| AI-04 | SC-05 + SC-06 (codes + certification as one assurance architecture) | **Integration not supported**; overlapping at shared interfaces; distinguishable |
| AI-05 | Commission rule-making (SC-08) | **Indeterminate** (Reg. 182/2011 is decisive); delegated-act control integrated as a sub-case |
| AI-06 | Transfers (SC-09) | Integrated, simple case, as a legally ordered fallback among routes; operation and third-country elements indeterminate |
| AI-07 | Multilevel supervisory architecture (SC-14+13+07+02) | Integrated at type level; instances, multiplicity and national powers indeterminate (mediated constitution) |
| AI-08 | **Whole GDPR as one architecture (W=A)** | **Not supported**; a supervisory cluster plus distinguishable architectures; whole-instrument integration indeterminate |
| AI-09 | Controller-centred compliance with layered enhancement (V6 pattern) | Overlapping / partially integrated: "enhanced self-regulation" present as a **conditional** layer for adherents, not a property of the whole |

The worked traces are in `WORKED_LEGAL_TRACE.md`. They were chosen by the pre-fixed rule (DR §17), not for expected support.

## 6. Source and interpretation limits
Single evaluator; S predicates and I3 statements written by the agent that extracted the data; paragraph-level granularity; recitals not read; external instruments (national law, Reg. 182/2011, Reg. 765/2008, EN-ISO/IEC 17065, the EDPS instrument) not retrieved; discretion not coded; no implementation or operation evidence; historical text baseline. The comparison with Stratmann et al. and ISO 42010 is **not made** (no diagram or description produced; full texts unread).

## 7. Did I2 and I3 work adequately?
- **I2 (qualified coupling)** worked where the text contains explicit conditional or procedural cross-references (AI-01, 02, 03, 06, 07): coupling could be cited provision by provision, and "shared actors", vocabulary or citation were kept apart from coupling. It was **weak between S**: for AI-04 the decisive question (is shared downstream use a coupling?) is a threshold choice, and for AI-08 there is no rule for how much between-S coupling is "enough" for a whole. No scale of connection kinds was needed or used.
- **I3 (configurational consequence)** worked as a *filter against over-claiming*: the anti-circularity sequence **rejected** two integration claims (AI-04, AI-08) because the property re-described the union. Where accepted, the consequences were stated in V6 vocabulary (conditional sequence, alternative routes, stratification) and tied to relations between relations. **Limits:** the I3 statements were authored by the same agent that built the candidates, so confirmation risk is not excluded; the discriminating power for integration claims is untested.
- **Verdict:** adequate as documentation and as a protective filter; **not shown** to be reliable or independent.

## 8. What RGAM added over V6 on this evidence (`V6_RGAM_INCREMENTAL_COMPARISON.md`)
Substantive for this instrument: N1–N4 (what the GDPR itself constitutes), separation of assignments from relations (visible gap in the relational pivot), external-dependency register (changes outcomes to "indeterminate"), stricter accountability criteria. Largely redundant with a careful V6 application: identification of positions, functions, relations; "W is not A". **Unproven:** reliability of the criteria; the contrast design (not tested); devices beyond registers; status axes; multi-view output. Complexity: devices for procedures and type/instance for conduct-defined roles.

## 9. Decisions requiring Igor's adjudication (`HUMAN_ADJUDICATION_QUEUE.md`)
Priority items: **HQ-003** mediated constitution of the national authorities; **HQ-005/006** derived accountability and the requirement of explicit questioning capacity; **HQ-007** relation-type inventory; **HQ-001** devices vs procedures; **HQ-008/009** independent S discovery and blind recoding of AI outcomes; **HQ-010** retrieval of Reg. 182/2011 and the EDPS instrument; **HQ-014** version issues. Theory problems (TP-01…TP-20) are recorded and **no manuscript revision was made**.

## 10. Next executable research step
A **blind, two-coder recoding** of a stratified sample (units from every chapter, including units screened "No"), coding once with V6 constructs alone and once with RGAM records, by human coders who have not seen these records; independent definition of subconfigurations; agreement reported by variable and by interpretive level; disagreements adjudicated by a legal specialist. In parallel, resolve HQ-004, HQ-005 and HQ-006 and retrieve the two decisive external instruments (HQ-010) before any claim on Commission rule-making or the Board's membership.
