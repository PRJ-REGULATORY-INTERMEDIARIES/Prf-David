# 12 — Claims audit

**Scope.** Every substantive claim in `09_FROM_CODING_TO_ARCHITECTURE_NOTE_FOR_DAVID.md`, in document order, against the frozen record.

**Statuses.** `SAFE` — supported by frozen evidence as stated. `SAFE WITH QUALIFICATION` — supported only if the stated qualification travels with it. `PRELIMINARY` — defensible reading of a thin base; must be marked as provisional. `DO NOT REPORT` — not supportable; must not appear.

---

## §1 Executive summary

| # | Claim | Evidence | Status | Required qualification |
|---|---|---|---|---|
| 1 | 264 comparative units; 1 material disagreement at the evidence level; 65 of 96 at C2–C4 | `PRE_ADJUDICATION_DESCRIPTIVE_SUMMARY.md` §2; material by level C0=1, C1=30, C2=26, C3=23, C4=16 | **SAFE** | State it as a distribution of *differences between two reconstructions*, not as a measure of extraction accuracy. Neither arm was checked against a gold standard. |
| 2 | "The difficulty is in the transitions between your levels" | #1 plus trigger distribution (H5 on 12 cards, H6 on 11, H11 on 14) | **SAFE WITH QUALIFICATION** | Must carry the refinement: the *upward* transitions. The C1 count (30) is the second largest, so "upper levels only" would overstate it. |
| 3 | A language model "will complete an architectural claim whether or not the evidence warrants one" | Four of four cases produced an architecture-boundary card; the direct application asserted one architecture per instrument in all four | **PRELIMINARY** | This is an inference from four cases with one executor model. It is a hypothesis about machine-assisted coding, not an established property. The note frames it as the pilot's reading; keep that framing. |
| 4 | "Five supported the more restrained reconstruction. One supported the more compact one." | `16_HUMAN_VALIDATION_IMPORT_2026-10-08/HUMAN_VALIDATION_REGISTER_6.csv` and `POST_REVEAL_LINKAGE_6.csv`, resolved against the frozen `MASTER_IDENTITY_KEY.csv`: B/B/A/B/B/A → five controlled, one baseline (HQ-AI-12) | **SAFE WITH QUALIFICATION** | Must always be stated as: targeted blinded assessment of six purposively selected cards of fifty-six, identity revealed afterwards, four of the six at one comparative level, decided by the study’s own designer, archived without justifications, and the other fifty not human-adjudicated. Because the six were selected for methodological centrality the pattern is illustrative rather than representative. No rate, no proportion, no "83%", no accuracy, no win, no superiority. |
| 5 | "The controls that restrain upward inference appear to earn their place; those that subdivide do not" | Five endorsements at C1/C3 vs one non-endorsement at C2; plus D5 distribution | **PRELIMINARY** | "Appear to" is load-bearing and must stay. Six decisions cannot establish this. |
| 6 | "I would strip it to roughly six fields and one test" | `05_METHOD_CONTROLS_REVIEW.md` | **SAFE** | A recommendation, not a finding. The note presents it as such. |
| 7 | "None of the fifty-six has been formally adjudicated; both arms ran on the same model" | `MASTER_HUMAN_REVIEW_QUEUE.csv` all `OPEN_AWAITING_HUMAN_ADJUDICATION`; QA check 28; comparator attestation `claude-sonnet-5-5` | **SAFE** | None. This must not be removed under any shortening. |

---

## §2–3 Why the exercise became necessary; the inferential problem

| # | Claim | Evidence | Status | Required qualification |
|---|---|---|---|---|
| 8 | The framework already contains inference rules, the six fallacies, traceability and the stopping rule | Manuscript §6.7, §6.8, §6.9, §6.10 | **SAFE** | None. This is the note's central framing claim and it is textually supported. |
| 9 | The added controls are mostly equivalent in conceptual function to requirements already in the paper | `V8_RGAM_METHOD_CROSSWALK.md`, frozen prospectively; `EQUIVALENT` on 13 of 22 rows including architectural inference and the stopping rule | **SAFE** | Note that the crosswalk is a *prospective* translation aid, by its own terms "not evidence of equivalence of results." It supports a claim about conceptual function, not about outcomes. |
| 10 | The controls' genuine additions are: a field where stop/indeterminate are legal answers; earned candidate status; a mandatory rival-grouping record | Crosswalk `EQUIVALENT` rows; execution protocol §9, §11; decision rule DR-25 | **SAFE** | None. |
| 11 | The elaborate procedure *dropped* the object category and the strategies/logics layer | Crosswalk: `NO_DEFENSIBLE_EQUIVALENT` for object; `METHOD_SPECIFIC` for strategies and logics | **SAFE** | Must be reported. It is a cost on the controlled side and omitting it would make the note one-sided. |
| 12 | Nine decisions are not lexical extraction | Manuscript §6.5–§6.10; the eleven trigger categories; the frozen uncertainty typology | **SAFE** | Presented as an analysis of what the task requires, not as a finding. |
| 13 | "Fluency carries no signal of warrant"; "the prompt's unit becomes the answer's unit"; "completion pressure runs upward" | Interpretive, grounded in #3 | **PRELIMINARY** | Keep as the note's reading of what it observed. Not measured. |

---

## §4 How the pilot was conducted

| # | Claim | Evidence | Status | Required qualification |
|---|---|---|---|---|
| 14 | One identical hash-verified official source per case, complete with annexes | `SOURCE_COMPLETENESS_AUDIT.md`; `AI_ACT_SOURCE_RECOVERY_REPORT.md`; Amendment 02 equality requirement; Round-1 QA checks 15–18 | **SAFE** | One documented asymmetry: the CBAM baseline case manifest has no legal-source row; the identical hash is in its provenance record. Disclosed in the QA report; worth a footnote if the note is challenged on this. |
| 15 | Two pre-existing local source files failed their recorded hashes and were replaced before analysis | `SOURCE_COMPLETENESS_AUDIT.md` integrity findings; `AI_ACT_SOURCE_RECOVERY_REPORT.md` | **SAFE** | None. |
| 16 | Instruments coded as original acts as published, not consolidated; Directive 86/361 repealed 1992 | `SOURCE_COMPLETENESS_AUDIT.md` version boundary | **SAFE** | None. |
| 17 | The comparison was preregistered and frozen before either set of outputs was opened | `COMPARISON_PREREGISTRATION_GATE.md`; Round-1 QA checks 9–10, 29 (codes imported verbatim) | **SAFE WITH QUALIFICATION** | QA check 29 also records that the *operationalization* of materiality, the clustering of absence claims and the blinding were interpretive choices made by the comparator and logged. The rules were frozen; their application was not pre-specified in full. |
| 18 | 264 units, 113 equivalent, 151 differences, 96 material, 56 cards | `PRE_ADJUDICATION_DESCRIPTIVE_SUMMARY.md`; QA checks 20–23 | **SAFE** | None. |
| 19 | Blind assignment by deterministic hash; identity held in a separate key; cards carry no attribution | `MASTER_IDENTITY_KEY.csv` rule field; QA checks 24–26 | **SAFE** | None. |
| 20 | "The remaining fifty cards were not human-adjudicated and are not treated as adjudicated evidence in this note" | `MASTER_HUMAN_REVIEW_QUEUE.csv`: 50 rows still `OPEN_AWAITING_HUMAN_ADJUDICATION`; QA check 28; stage-16 register covers exactly 6 | **SAFE** | None. This sentence must survive any shortening. It replaces the pre-import wording ("nothing yet"), which became inaccurate on 2026-10-08. |
| 21 | A blinded machine-simulated pass over the 56 took place | Produced during exploratory workflow outside the frozen workspace; **formally excluded** from the evidentiary basis (`HUMAN_VALIDATION_PROVENANCE.md` §5); the frozen protocol states the executor does not simulate adjudication | **DO NOT REPORT** | Correctly omitted from the note, and nothing in the package rests on it. The 50 unassessed cards are described as not human-adjudicated, never as adjudicated by any means. |

---

## §5–7 What the comparison revealed; where controls helped and became excessive

| # | Claim | Evidence | Status | Required qualification |
|---|---|---|---|---|
| 22 | The whole-act architecture question recurred in all four cases | HQ-SCF-02, HQ-CBAM-10, HQ-AI-14 (whole vs several); HQ-DIR-01 (whether any) | **SAFE** | None. The strongest replicated observation in the pilot. |
| 23 | Neither arm was clearer on vertical traceability in any of the 96 material units | D3: `EQUIVALENT` 51, `NOT_APPLICABLE` 45; no `V8_CLEARER`, no `RGAM_CLEARER` | **SAFE** | None. Reporting this is required for balance — it cuts against the controls. |
| 24 | Calibration could not be assessed: D6 indeterminate in 93 of 96 | D6 distribution | **SAFE** | Must accompany any statement about uncertainty control. The note must not claim the controls improved calibration. |
| 25 | The baseline arm was not a straw man; its own stopping records refuse regime, frequency, implementation and effectiveness claims | The four `V8_STOPPING_RULE_RECORD.md`; CBAM record on Art. 1 and the EU ETS | **SAFE** | None. Required for fairness and present in the note. |
| 26 | SCF: direct = one architecture; controlled = integrated + overlapping + indeterminate | HQ-SCF-02 card; `ARCHITECTURE_CANDIDATES` ARCH-01/02/03 | **SAFE** | Decision attribution now archived — see #4. |
| 27 | AI Act: coupling-consequence condition not satisfied for the Regulation as a whole | ARCH-09, I3 `NOT_SATISFIED`; `INSTRUMENT_LEVEL_SUMMARY` | **SAFE** | State as the controlled arm's recorded assessment, not as an established fact about the Regulation. |
| 28 | Directive 86/361: NETs rest on a CEPT Memorandum of Understanding; "approved testing laboratory" status is fixed by the CEPT accreditation system; Art. 2(8) defines it by reference to that system | EXT-005, EXT-006, both `constitutive_dependency = Y`; QR-0001/0002 on Art. 2(8) | **SAFE WITH QUALIFICATION** | **Neither external source was retrieved** (`source_verification_status = not_checked`). The claim is about what the Directive's own text refers out to, not about what those instruments contain. |
| 29 | CBAM Art. 20(1) names the Member State as seller; the direct reconstruction left the seller unidentified | HQ-CBAM-04 card, verbatim provisions and both propositions; identity key | **SAFE** | None. This is the best-evidenced single claim in the note: the text is quoted, both propositions are frozen, and the arm attribution is in the key. |
| 30 | HQ-AI-12: the blinded decision supported the three-arrangement reconstruction | Card HQ-AI-12 (level C2, triggers H4/H6); identity key (A = controlled, B = baseline); decision archived as **B** | **SAFE WITH QUALIFICATION** | Must be reported, not minimised, and must be identified as the one card at the configuration level. See #4 for the status of the decision itself. |
| 31 | The controlled arm later regrouped designation with certification at the architecture layer | `ARCHITECTURE_CANDIDATES` ARCH-02 = [SC-01, SC-02, SC-03, SC-18], outcome `INTEGRATED`; `SUBCONFIGURATIONS` labels | **SAFE** | This is the analytically important part of the counterexample and is independently verifiable in the frozen tables. |
| 32 | "Greater granularity is not greater analytical quality" | One validated card plus #31 | **PRELIMINARY** | One instance. The note states it as a lesson drawn from that instance, which is the most it can bear. |
| 33 | ~2,400 analytical records against 96 material differences; 1,163 on the AI Act | Family summary §5 (482 + 488 + 1,163 + 232 = 2,365) | **SAFE WITH QUALIFICATION** | The frozen rule forbids treating volume as quality **in either direction**. The note must therefore not present the ratio as proof of waste; it presents it as a cost not matched by a demonstrated contribution. That distinction must be preserved. |
| 34 | Information-reporting is the largest relation class in three of four cases, and such relations were treated as non-material | 136/281 AI Act, 48/101 CBAM, 15/60 SCF, 11/39 DIR; materiality operationalization in Round-1 QA | **SAFE WITH QUALIFICATION** | The non-materiality of informational relations is the comparator's operationalization, logged as such, not a frozen rule. A reviewer may disagree. |
| 35 | 89 internal review items before the comparison added 56 | Family summary §5 (19 + 16 + 35 + 19) | **SAFE** | None. |

---

## §8 What should remain

| # | Claim | Evidence | Status | Required qualification |
|---|---|---|---|---|
| 36 | The eight surviving safeguards | `05_METHOD_CONTROLS_REVIEW.md` | **SAFE** | A proposal. Four of the eleven classifications rest partly on the six reported decisions; the review document says so. |
| 37 | "For a machine executor, a principle with no output slot has no effect" | The Directive 86/361 contrast: `highest_level_reached = S` in one arm, high-confidence architecture in the other, from identical provisions | **PRELIMINARY** | A generalisation from one clean instance. Keep as a formulated lesson. |
| 38 | The provenance control caught a real failure | #15 | **SAFE** | None. |

---

## §9 Intermediation

| # | Claim | Evidence | Status | Required qualification |
|---|---|---|---|---|
| 39 | AI Act notified body: issues/extends/restricts/suspends/withdraws certificates (Art. 44); audits QMS; may require access to data sets and premises (Annex VII) | QR-0094, QR-0095, QR-0280, QR-0279, QR-0281 with unit anchors | **SAFE** | Formal legal authority only. No claim about exercise. |
| 40 | A provider may choose any notified body (Art. 43(1)) | QR-0093 | **SAFE** | The note's gloss — equally consistent with competition and with competitive laxity — is correct and must stay. |
| 41 | Ten distinct second-order relations over notified bodies, entirely within Arts. 28–38 | QR-0053 through QR-0085 with unit anchors | **SAFE** | "Ten distinct relations" is a count of the frozen reconstruction, not a claim that it is exhaustive. |
| 42 | CBAM: the only relation governing the verifier inside the Regulation is Art. 18(2) accreditation on request | QR-0044; no supervision/withdrawal relation over the verifier in `QUALIFIED_RELATIONS.csv` | **SAFE WITH QUALIFICATION** | This is an **absence-dependent claim about the frozen reconstruction**, not about the Regulation. It must be phrased as "no such relation is recorded in the reconstruction," with the coverage limit stated. By the pilot's own rule, "not found" is a statement about the search. |
| 43 | Verifier status arises under Implementing Reg. (EU) 2018/2067; national accreditation body constituted by Reg. (EC) 765/2008 Art. 4(1) | EXT-018, EXT-014, both constitutive | **SAFE WITH QUALIFICATION** | Neither retrieved. The claim is about what CBAM refers out to. |
| 44 | Whether a law constitutes or imports the governance of its own intermediaries is a structural variable | Four instruments: internal (AI Act), mostly imported (CBAM), almost wholly imported (86/361), not applicable (SCF) | **PRELIMINARY** | Four instruments, three policy fields, three decades, selected for a methodological test and not for variation in intermediation. The note presents it as measurable and as a question for David, not as a finding. That framing is required. |
| 45 | Intermediation is embedded in hierarchy in the AI Act: no consequential public power transferred; the intermediary's authority is revocable by the conferring authority | QR-0070, QR-0071, QR-0076, QR-0080, QR-0231; Arts. 74, 79–83 | **SAFE WITH QUALIFICATION** | Formal structure only. Formal revocability is compatible with designations that are never revoked. |
| 46 | SCF has no third-party intermediary | 28 positions/devices, all Union institutions, Member States, entrusted public authorities, control bodies, recipients, consulted stakeholders | **SAFE WITH QUALIFICATION** | An absence claim about the reconstruction, within the declared corpus. Phrase accordingly. |
| 47 | Three instruments "consistent with complementarity rather than substitution" | §9 of the note | **PRELIMINARY** | Explicitly marked "suggestive and nothing more" in the note. Required. |
| 48 | Indispensability and substitutability are absence-dependent and need a coverage statement | Manuscript §6.12; decision rule DR-22 | **SAFE** | None. |
| 49 | Degree measures will track informational traffic unless weighted by relation type | #34 relation-class distributions; manuscript §6.12 caution on network measures | **SAFE** | None. |

---

## §10–12 Boundary, next phase, conclusion

| # | Claim | Evidence | Status | Required qualification |
|---|---|---|---|---|
| 50 | The "cannot establish" list — effectiveness, expertise, capture, implementation, behaviour, practical accountability, performance, operational centrality, regime boundaries | Manuscript §6.8 (functional and implementation fallacies), §6.13–§6.14 | **SAFE** | None. |
| 51 | 73 constitutive external references across the four cases, none retrieved | RGAM cross-case summary §6 (13 + 17 + 39 + 4); all rows `not_checked` / `outside_corpus_not_expanded` | **SAFE** | None. |
| 52 | "Nothing here establishes that the controls as such caused the difference" | Comparator attestation; no arm-blind control run | **SAFE** | None. Must survive shortening. |
| 53 | Phase 2 should obtain independent adjudication and run an arm-blind prompt control; archiving the six is "now done, though without the justifications" | Stage 16 register, linkage and deviation log; attribution limit | **SAFE** | A recommendation plus a statement of fact about the archive. The "without the justifications" clause is required: DEV-16-02 records that none was captured. |
| 54 | "The apparatus outgrew the question it was built to answer" | #23, #24, #33, #34, #35, #11 | **SAFE WITH QUALIFICATION** | A self-assessment. Defensible on the listed evidence, but it is a judgment, and it should not be read as a measured inefficiency. |

---

## Claims checked for and confirmed absent from the note

| Prohibited claim | Status |
|---|---|
| any percentage, rate, accuracy, win rate, validation score from the six decisions | **absent** |
| "superior", "outperformed", "better method", any methodological winner | **absent** |
| the six decisions described as representative, statistical or full adjudication | **absent** — and the illustrative-not-representative qualifier now follows the 5/1 statement immediately in §4 |
| machine adjudication presented as human adjudication, or as evidence of anything | **absent** — formally excluded in `HUMAN_VALIDATION_PROVENANCE.md` §5 |
| any composite or weighted score | **absent** |
| output volume presented as quality | **absent** |
| the additional controls described as a model, theory, framework or competing project | **absent** |
| any claim about implementation, effectiveness, capture or expertise from legal text | **absent** |
| architecture candidates described as established architectures | **absent** — the note uses "candidate", "declined", "indeterminate" throughout |
| claims attributed to David that he has not made | **absent** — every framework attribution is to a numbered manuscript section |
| suppression of the HQ-AI-12 counterexample | **absent** — flagged in §1, given its own section in §7, and restated in §12 |
