# 16 — Next-phase research plan

**Guiding constraint.** Avoid continued methodological proliferation. The pilot's clearest lesson about the work itself is that the procedural apparatus outgrew the question it was built to answer. The plan below has one phase of consolidation and one phase of substantive research, and deliberately no further methodological phase.

---

## Phase 1 — now complete

**What it did.** Stress-tested the operationalization of architectural inference. Four EU instruments (Reg. 2023/955, Reg. 2023/956, Reg. 2024/1689, Dir. 86/361/EEC), each reconstructed twice from one identical hash-verified official source: once applying David's framework relatively directly, once with additional explicit controls over the inferential transitions. Preregistered comparison, frozen before either set of outputs was opened. 264 comparative units, 96 material differences, 56 blinded disagreement cards, six validated under blinded A/B conditions.

**What it established.** Two vulnerable operations rather than one: relational extraction (30 of 96 material differences at the relational level, including one validated case where a Regulation's own words name a seller and the reconstruction left the seller blank) and upward inference (65 of 96 at configuration, architecture and epistemic levels, with the container default recurring in four cases out of four).

**What it did not establish.** Which procedure is more accurate — fifty of the 56 cards were not human-adjudicated. Whether the controls or the longer prompt produced the difference — both arms ran on the same model. The six assessed decisions are purposive, were made by the study's own designer, and are archived without justifications (stage 16, 2026-10-08).

**Status:** closed. It should not be extended.

---

## Phase 2 — integrate only the useful safeguards

**Objective.** Fold the surviving controls into the existing coding protocol as fields on records that already exist, retire everything else, and close the three cheap evidential gaps Phase 1 left open.

### 2a. Integration (the main task)

Add eight fields, nothing more:

1. source hash, declared coverage, legal status and reference date;
2. named parties and modality on every relation, with duties lacking a counterparty kept as assignments;
3. a stated membership rule per configuration, at the granularity the governance question needs;
4. one coupling question per candidate whole — what legally evidenced coupling joins these configurations, and what property follows for the whole rather than for each part — answered independently of the property expected, with "indeterminate" authorised;
5. an external constitutive dependency flag;
6. candidate status and stopping level as recorded values, with "no architecture warranted" available;
7. one rival grouping per architectural claim, plus a coverage statement for any absence-dependent property;
8. uncertainty as a short typed field travelling with the claim.

Retire: the nineteen-table schema, the six-stratum identifier system, the separate closure and property registers, duplicated direction fields, the internal review queue as a distinct artefact class, and the per-phase gate apparatus.

Restore: David's **object** category and his **strategies and governance logics** layer, both of which the elaborate procedure dropped (recorded in the frozen crosswalk as `NO_DEFENSIBLE_EQUIVALENT` and `METHOD_SPECIFIC`).

**Deliverable.** One revised coding protocol, with a short rationale per retained field citing the manuscript section it operationalizes. Not a new instrument — an amended one.

### 2b. Three cheap validations that should not wait for Phase 3

| Task | Why it matters | Cost |
|---|---|---|
| ~~Archive the six blinded decisions~~ — **done 2026-10-08**, stage 16 | The claim resting on human judgment can now be inspected against the frozen cards and key. Justifications were never captured and were not reconstructed, so the reasoning stays unavailable (DEV-16-02) | complete |
| **Obtain independent adjudication** of a subset of the 56 — ideally the thirteen HIGH-priority cards — by someone who did not design the arms | A single adjudicator who designed the study is the weakest link in the present evidence. This is the single highest-value cheap test available | days |
| **Run an arm-blind prompt control**: same model, same task, two levels of prompt structure, no methodological framing | Separates "effect of the controls" from "effect of a longer, more structured prompt" — currently confounded, and the result could materially change which of the eight fields survive | a day |

A fourth, optional: re-run one case on a different model family to see whether the container default is model-specific or general. Useful, not blocking.

**Gate on Phase 3.** Phase 3 should not start before 2a is delivered and the arm-blind control has run. If the control shows that prompt structure accounts for most of the difference, the eight fields are still worth keeping — a well-structured prompt is cheaper than a procedure — but the note's framing would need revision before anything is published.

---

## Phase 3 — use the simplified protocol on the substantive questions

**Objective.** Investigate David's intermediation questions comparatively across laws and regulatory sub-regimes. This is where the method stops being the object of study.

### Design

**Dependent variables.** Per instrument, a profile across David's six dimensions of intermediation centrality (§6.12) — prevalence, functional breadth, authority, dependency/indispensability, structural position, regulatory embeddedness — reported as a profile and never summed. Plus two variables the pilot shows are codeable and that bear directly on the second-order question:

- the **composition of the second-order chain** over intermediaries (which of accreditation, authorization, reporting, investigation, restriction, suspension, withdrawal are present);
- the **location** of that chain: constituted inside the instrument, or referred out to another instrument.

The second is the pilot's own contribution to the agenda. Across the four cases it varies sharply — internal for the AI Act (ten relations, Arts. 28–38), largely external for CBAM (Reg. 765/2008; Implementing Reg. 2018/2067), almost wholly external for Dir. 86/361 (the CEPT accreditation system), not applicable for the Social Climate Fund. Four instruments cannot establish a pattern; they establish that the variable is measurable.

**Candidate covariates.** Task type routed outward (verification of technical facts versus rule-making versus enforcement); whether third-party assessment is mandatory or conditional; whether the regulated actor may choose its assessor; whether an accreditation infrastructure already existed in the field; instrument type (market-access conditioning versus fiscal transfer).

**Sampling.** A defensible frame is required, and the four-case set is not one — it was chosen to stress-test an inferential procedure, with two climate instruments, one unique-eligible AI case and one instrument repealed in 1992. Phase 3 needs a sampling frame built for variation in intermediation, specified before coding.

**Corpus extension.** For two of the four pilot cases the answer to "who governs the intermediaries" lives outside the instrument. Phase 3 must therefore code the referred-out instruments — Regulation (EC) No 765/2008, Commission Implementing Regulation (EU) 2018/2067, the CEPT material — which Phase 1 deliberately excluded. Expect this to be a substantial share of the work, and note that it is also a test of the external-dependency flag: if the referred-out instruments supply equivalent supervision, the internal/external distinction is about drafting technique; if they do not, it is about governance.

### Claims discipline, carried forward unchanged

Formal legal architecture only. No claim about effectiveness, expertise, capture, implementation, behaviour, practical accountability or operational centrality. Absence-dependent properties — indispensability, substitutability, exclusivity — only with a declared coverage statement. Profiles, never composite scores. The boundary is set out in `07_WHAT_WE_CAN_AND_CANNOT_CLAIM.md` and should be attached to any Phase 3 output.

### What would count as a result

A comparative statement of the form: *laws that route function X outward differ systematically in whether they constitute or import the governance of the actors they route it to, and that difference co-varies with Y.* That is a finding about regulatory governance rather than about coding, which is the point of the whole exercise.

---

## What not to do

- **No Phase 4 of methodological development.** If a Phase 3 case exposes a genuine inferential gap, fix the field and record it; do not open a new methodological programme.
- **No new composite index**, including for intermediation centrality. David's §6.12 asks for the dimensions to be kept separate; the pilot's frozen rules forbid composites; and a single score would discard exactly the profile information that makes the comparison interesting.
- **No reopening of the pilot's paired matching, materiality rules or comparison criteria.** They are frozen and the record is auditable. If Phase 2b's independent adjudication contradicts the six decisions, record that as new evidence rather than re-running Round 1.
- **No further elaboration of the four pilot cases.** They have produced what they can.
