# 05 — Which controls earned their place

**Governing principle.** Additional complexity must earn its place by changing, constraining or qualifying a substantive inference. A control that only produces records is not justified by the records it produces.

**Objective.** Methodological simplification. The recommendation is explicitly *not* to develop the procedure further.

**Evidential basis and its limits.** The frozen Round-1 registers for four cases; the two frozen protocol documents; the prospective crosswalk; and six blinded decisions, purposively selected and archived in `NEW TEST 3x3/16_HUMAN_VALIDATION_IMPORT_2026-10-08/` without recorded justifications. The other 50 cards were not human-adjudicated. Every classification below is a judgment about *this* pilot and is reversible on evidence.

---

## Summary

| # | Control | Classification |
|---|---|---|
| 1 | Provenance (source hash, unit addressing, coverage declaration) | **RETAIN** |
| 2 | Actor / counterparty precision | **RETAIN** |
| 3 | Direction and modality | **RETAIN IN SIMPLIFIED FORM** |
| 4 | Configuration-boundary rules | **RETAIN IN SIMPLIFIED FORM** |
| 5 | Coupling tests (I1–I4) | **RETAIN IN SIMPLIFIED FORM** |
| 6 | External-dependency marking | **RETAIN** |
| 7 | Legal status / reference date | **RETAIN** |
| 8 | Uncertainty recording | **RETAIN IN SIMPLIFIED FORM** |
| 9 | Stopping rule as an explicit output field | **RETAIN** |
| 10 | Sensitivity analysis (rival groupings, defeaters) | **RETAIN IN SIMPLIFIED FORM** |
| 11 | Architecture-candidate status | **RETAIN** |
| 12 | Extensive multi-phase procedural machinery (19 frozen tables, 27 artefacts per case, W/E/P/R/S/A strata, internal queue) | **REMOVE / NOT JUSTIFIED BY THIS PILOT** |

Seven of the twelve shrink or go. The surviving core is six fields and one test.

---

## 1. Provenance — RETAIN

**What it is.** One identical, hash-verified official source file per case for both arms; addressable units; a declared coverage statement (the W declaration) before any inference.

**Why.** Without it the comparison would have been uninterpretable, and the pilot found a real failure that provenance control caught: the pre-existing local CBAM file failed its historical hash check, and the pre-existing AI Act file hashed differently from its recorded expected value. Both were replaced with freshly retrieved official sources before any analysis. Had the arms run on divergent texts, every difference would have been confounded.

**Relation to the framework.** §6.9 vertical traceability requires that a high-level classification remain recoverable to the provisions supporting it. Provenance is the floor of that requirement.

**Cost.** Low. A manifest and a hash.

---

## 2. Actor / counterparty precision — RETAIN

**What it is.** Every relation names identifiable parties; no generic, implied or fabricated counterparty; where a provision assigns a duty without a counterparty, it is kept as a normative assignment rather than forced into a dyad.

**Why it earned its place.** HQ-CBAM-04 is the pilot's one validated instance of a control changing a *relational fact*. Art. 20(1) says a Member State sells CBAM certificates; the baseline proposition recorded the certificate arrangement with "the seller is not identified." In an instrument whose point is conditioning market access, who sells is constitutive, not incidental. The reported decision supported the precise reconstruction.

**Note on symmetry.** This control is shared, not added: the crosswalk records "normative assignment without a counterparty" as `EQUIVALENT` across both procedures — both forbid fabricating a counterparty. What differed was execution, not rule.

**Cost.** Low. It is a discipline, not a stratum.

---

## 3. Direction and modality — RETAIN IN SIMPLIFIED FORM

**What it is.** Textual direction and governance direction recorded separately; modality from a controlled vocabulary (obligation, permission, entitlement, competence, declaratory, definition).

**Why simplified.** Direction and modality are cheap and they prevent a real error — reading a reporting duty as an oversight power. But the pilot gives no instance where the *separation of textual from governance direction* changed a material conclusion: trigger H3 (direction or modality with governance effect) appears on only 2 of 56 cards, the rarest trigger in the family.

**Recommendation.** Keep one modality field with a controlled vocabulary. Drop the dual direction fields; record direction once, as stated in the text, and note inversions in the uncertainty field when they arise.

---

## 4. Configuration-boundary rules — RETAIN IN SIMPLIFIED FORM

**What it is.** A declared membership rule, coupling basis, boundary and relational basis for each configuration.

**Why not a straight retain.** This is the control the counterexample bears on. HQ-AI-12 is the one validated card at the configuration level, and the more finely partitioned reconstruction was **not** preferred: 19 subconfigurations produced no better membership judgment than 3 configurations, and the controlled arm then regrouped designation with certification at the architecture layer — the grouping the reported decision rejected. Across the family, 26 of 96 material differences are at C2 and the pilot provides no evidence that the finer layer resolved any of them.

**What to keep.** The *requirement to state a membership rule*. That is from David §6.5 and it is cheap. A configuration should say why these relations and not others.

**What to drop.** The requirement that every candidate grouping be instantiated as a separate persistent object before aggregation. Configurations should be stated at the granularity the governance question needs, with the membership rule exposed, and revised rather than multiplied.

---

## 5. Coupling tests (I1–I4) — RETAIN IN SIMPLIFIED FORM

**What it is.** For each candidate whole, four conditions stated and evidenced in an anti-circularity sequence: I1 problem and scale; I2 legally evidenced coupling identified independently of the expected global property; I3 configurational consequence (which property attaches to the whole, with its bearer); I4 boundary and defeaters.

**Why it earned its place.** This is the single most load-bearing control in the pilot. It produced the family's recurring result — 9 of 21 candidates `INDETERMINATE`, and I3 `NOT_SATISFIED` for the AI Act as a whole — and it is implicated in all four architectural cards among the six validated, all four reported as supporting the restrained reading.

**Why simplified.** I1 and I2 are the work. I1 forces the question "an architecture *of what*, at what scale" and thereby blocks the container default directly. I2's requirement that coupling be identified *independently of the expected global property* is the anti-circularity provision and is where the indeterminate outcomes came from. I3 is partly a restatement of I2 plus David's property-bearer requirement (§6.6), and I4 overlaps control 10 below. Of 21 candidate assessments, I1 was `SATISFIED` in all 21 — a condition that never discriminates is documentation, not a test.

**Recommendation.** Keep I1 as a *declaration*, not a test: state the governing problem and scale of any candidate whole. Keep I2 and I3 as the test, merged into one question with two parts: *what legally evidenced coupling joins these configurations, and what property follows for the whole rather than for each part?* Fold I4 into the sensitivity record (control 10). Keep the authorized outcome set including `INDETERMINATE`, and keep the prohibition on forced architecture.

---

## 6. External-dependency marking — RETAIN

**What it is.** Every reference to a source outside the declared corpus is recorded, with its role, whether the dependency is constitutive, and its effect on claims. A claim whose legal constitution depends on an unverified external source is `undetermined` or restricted to the declared corpus.

**Why it earned its place.** On three grounds, the strongest case of the twelve.

1. **It changed a top-level conclusion.** Directive 86/361/EEC: the controlled arm declined the architectural level because a NET's constitution rests on a CEPT Memorandum of Understanding and "approved testing laboratory" status is fixed by the CEPT accreditation system. HQ-DIR-01 reported as supporting that restraint.
2. **It produced a substantive finding about the law, not just about the method.** CBAM governs through accredited verifiers whose status arises under Commission Implementing Regulation (EU) 2018/2067, and through national accreditation bodies constituted by Regulation (EC) No 765/2008 Art. 4(1). The AI Act, by contrast, constitutes the designation and supervision of notified bodies inside itself (Arts. 28–38). That contrast is a direct answer to David's question about how intermediaries are themselves governed, and it is visible only because external dependencies were marked.
3. **It is quantitatively unavoidable at this scale.** 148 external references across four instruments, 73 constitutive, 39 of them in the AI Act alone. 19 of the 56 review cards turn on external evidence. An EU-law reconstruction that does not mark these is describing an architecture the instrument does not constitute.

**Cost.** Moderate but proportionate: one table.

---

## 7. Legal status and reference date — RETAIN

**What it is.** A declared version: which text, as published or as consolidated, at what date, with what legal status.

**Why.** Directive 86/361/EEC was repealed in 1992 and the four instruments were coded as original acts as published, not consolidated law. Without a reference-date field an architectural claim is a claim about no particular law, and the claim cannot be re-tested later. This control is nearly free and prevents an error that is invisible once made.

---

## 8. Uncertainty recording — RETAIN IN SIMPLIFIED FORM

**What it is.** A typed uncertainty log (source ambiguity, external dependency, direction, and others) with links to the affected records.

**Why not a straight retain.** The pilot cannot show that the log improved calibration, because calibration was not assessable: D6 was `INDETERMINATE` in 93 of 96 material units and `WELL_CALIBRATED_BOTH` in 3. Both arms kept uncertainty registers — the baseline recorded 12, 11, 9 and 12 entries covering source, actor, action, counterparty, modality, condition, cross-provision, architectural-inference and stopping-rule uncertainty. This control is therefore shared, and its elaborated form is unvalidated.

**What to keep.** A short typed uncertainty field attached to the claim it qualifies, with a small closed vocabulary, and a hard rule that the uncertainty travels with the claim into any output.

**What to drop.** Uncertainty as a separate stratum requiring its own identifiers and cross-reference discipline. 67 source-ambiguity entries across four cases, with no demonstrated effect on a conclusion, is not a return on that structure.

---

## 9. Stopping rule as an explicit output field — RETAIN

**What it is.** `highest_level_reached` is a recorded value. Stopping below the top is an authorized result; `INDETERMINATE` is legitimate at every level; the instrument-level result may be "no architecture warranted."

**Why it earned its place.** This is the control that most directly addresses the vulnerability the pilot identified. Both procedures descend from a framework that already contains the stopping rule as a principle (§6.10) — and the baseline's own stopping records show it took the principle seriously, refusing regime claims, frequency reasoning, implementation and effectiveness claims in every case. The difference is that in one procedure "stop here" had a place to be written, and in that procedure, once, it was written: Directive 86/361/EEC, `highest_level_reached = S`. The reported decision supported it.

**The generalisable point.** For a machine executor, a principle that has no output slot has no effect. The stopping rule needs to be a field, not an instruction.

**Cost.** One field.

---

## 10. Sensitivity analysis (rival groupings and defeaters) — RETAIN IN SIMPLIFIED FORM

**What it is.** For each higher-order claim: what was searched, which rival grouping could explain the same pattern, what unresolved external dependency bears on it; plus the rule that absence-dependent properties (necessity, exclusivity, substitutability, "no alternative path") require a declared coverage statement, since "not found" is a statement about the search and not about the law.

**Why it earned its place.** D5 recorded a boundary or sensitivity gain in 41 of 96 material units and a non-orderable difference in 20, with no instance of the baseline being clearer — the largest single distributional difference in the comparison. Trigger H7 (absence-dependent claim) appears on 14 of 56 cards. And the rule has direct bearing on David's agenda: indispensability and substitutability (§6.12) are absence-dependent properties, so any claim that an intermediary is indispensable needs a coverage statement or it is a claim about the search.

**Why simplified.** The one-sidedness of the D5 distribution is weak evidence: a procedure with a mandatory rival-grouping field will be recorded as stating rival groupings. What is validated is narrower — in HQ-DIR-01 and HQ-SCF-02 the rival grouping was material to the decision.

**Recommendation.** Keep two things and drop the rest: (a) a rival-grouping line on every architectural claim; (b) the coverage statement requirement for any absence-dependent property. Drop the separate closure register as a stratum.

---

## 11. Architecture-candidate status — RETAIN

**What it is.** Every grouping starts as a configuration and becomes an architecture only by passing the coupling test. "Candidate" and "accepted" are distinct recorded states.

**Why it earned its place.** It is the structural fix for the container default. It is also what made the comparison possible at all: the Round-1 QA report records that candidate rows and higher-order inferences were "compared as inferences; none is treated as accepted before adjudication." Without the distinction, a grouping becomes an architecture by being written down, which is precisely the failure mode of a fluent generative executor.

**Cost.** One status value. The cheapest high-value control in the set.

---

## 12. Extensive multi-phase procedural machinery — REMOVE / NOT JUSTIFIED BY THIS PILOT

**What it is.** 19 frozen tables per case, 27 artefacts per case, six analytical strata with their own identifier schemes (W, E, P, R, S, A), a separate internal human-review queue, closure and property registers as standalone tables, and the gate/manifest/QA apparatus around each phase.

**Why it is not justified.**

- **Volume did not convert into contested substance.** 2,365 analytical records across the four cases produced 96 material differences and 56 review cards. On the AI Act: 1,163 records, 21 cards. The frozen materiality rule says volume is never a gain; applied to the procedure that generated it, the honest reading is that most of the structure was not load-bearing.
- **A large share of what it captured is non-material by the comparison's own rule.** `information_reporting` is the largest relation class in three of four cases — 48 of 101 in CBAM, 136 of 281 in the AI Act — and purely informational or administrative relations were treated as non-material under the frozen operationalization.
- **The overhead is worst where the instrument is smallest.** 232 records for a 12-article Directive on which the two arms agreed in 30 of 52 units and differed on one inference.
- **It did not buy traceability.** D3 recorded `EQUIVALENT` or `NOT_APPLICABLE` in all 96 material units: neither arm was clearer on recoverability in a single unit. The baseline's claim registers were already traceable. The strata did not improve on that.
- **It generated its own workload.** 89 internal review items across the four cases, before the paired comparison added 56 more.
- **It cost analytical coverage.** The crosswalk records `NO_DEFENSIBLE_EQUIVALENT` for David's **object** category and `METHOD_SPECIFIC` for his strategies and governance logics. The elaborate procedure dropped parts of the framework it was meant to serve.

**What to do instead.** Fold the surviving controls into the existing coding protocol as fields on the records that already exist, not as additional strata. The practical target: the six fields and one test below.

---

## The simplified residue

What should be added to the existing protocol — nothing more:

1. **Source and version** — hashed official text, declared coverage, legal status and reference date. *(controls 1, 7)*
2. **Named parties and modality** on every relation; assignments without a counterparty stay assignments. *(controls 2, 3)*
3. **Membership rule** stated for every configuration, at the granularity the question needs. *(control 4)*
4. **One coupling question** for any candidate whole: what legally evidenced coupling joins these configurations, and what property follows for the whole rather than for each part — answered independently of the property expected. Authorized answers include indeterminate. *(control 5)*
5. **External constitutive dependency** flagged where an actor, device or specification central to a configuration is constituted outside the corpus. *(control 6)*
6. **Candidate status and stopping level** recorded as values, with "no architecture warranted" available. *(controls 9, 11)*
7. **One rival grouping** per architectural claim, plus a coverage statement for any absence-dependent property. *(control 10)*
8. **Uncertainty** as a short typed field travelling with the claim. *(control 8)*

What should go: the 19-table schema, the six-stratum identifier system, the separate closure and property registers, the dual direction fields, the internal queue as a distinct artefact class, and the per-phase gate apparatus.

---

## Two honest limits on everything above

**The attribution problem.** Both arms and the comparator ran on `claude-sonnet-5-5`; reasoning effort was not exposed to the executor. The pilot therefore cannot separate "effect of the controls" from "effect of a longer and more structured prompt on the same model." A procedure that asks for rival groupings records rival groupings. Nothing here measures how much of the difference is the control and how much is the prompt. An arm-blind single-prompt comparison is the obvious next test and it is cheap.

**The evidence problem.** Six of the 56 cards were assessed; the other 50 were not human-adjudicated. The six were purposively chosen, four of them at one level, decided by the study’s own designer, and archived without justifications — so each is auditable as a decision and not as reasoning. Four of the eleven classifications above rest partly on those six. They should be read as the best available reading of a thin evidence base, not as findings.
