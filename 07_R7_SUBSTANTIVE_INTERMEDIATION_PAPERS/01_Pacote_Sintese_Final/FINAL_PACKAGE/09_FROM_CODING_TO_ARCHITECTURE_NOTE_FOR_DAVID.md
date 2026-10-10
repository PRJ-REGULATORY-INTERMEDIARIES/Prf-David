# From Coding to Architecture
## Operationalizing Relational Leximetrics with AI

*Preliminary note for discussion — Igor, October 2026*

---

## 1. Executive summary

I set out to do something that sounded straightforward: apply the inferential sequence in your paper — legal text → institutional statements → relationships → configurations → architecture → governance propositions — to four EU legal instruments, with AI assistance doing the coding. The exercise became far more elaborate than I expected, and I think the reason is worth reporting, because it is not a reason about software.

The extraction worked. Across four instruments and 264 paired comparative units, the two reconstructions I ran produced **one** material disagreement at the level of what the legal text says. Sixty-five of the ninety-six material disagreements were at the level of configurations, architecture, and the epistemic questions around them. The difficulty is not in reading law. It is in the transitions between your levels — and specifically in the *upward* transitions, where a language model will complete an architectural claim whether or not the evidence warrants one.

I then tested a set of explicit procedural controls over those transitions, by running each instrument twice: once applying your framework relatively directly, once with the same framework plus controls that force the inferential step to be declared. Six central disagreements were examined by me under blinded A/B conditions before I knew which reconstruction was which. Five supported the more restrained reconstruction. One — and I want to put it early rather than late — supported the more compact one, and it is the most instructive of the six.

My conclusions are: the controls that *restrain upward inference* appear to earn their place; the controls that *subdivide the representation* do not; and the procedural apparatus I built around both is far heavier than the pilot justifies. I would now strip it to roughly six fields and one test, fold those into the existing coding protocol, and use the result on the substantive questions you raised about intermediation — where, as it happens, one of the surviving controls turns out to produce a finding about the law rather than only about the method.

Two honest limits frame everything below. None of the fifty-six recorded disagreements has been formally adjudicated; six were validated, purposively chosen. And both reconstructions ran on the same model, so the pilot cannot separate the effect of the controls from the effect of a longer, more structured prompt.

---

## 2. Why this exercise became necessary

Your paper specifies the inference ladder with unusual care. §6.7 gives explicit cross-level inference rules. §6.8 names six recurrent errors. §6.9 requires vertical traceability. §6.10 states the stopping rule: assert only the highest-level claim the evidence presently warrants. On paper, a coder has everything needed.

The problem appeared as soon as the coder was a model. A principle that tells a human coder to hesitate does not make a model hesitate. Three vulnerabilities turned out to matter.

**Fluency carries no signal of warrant.** The output of an architectural inference is prose, and a model writes equally well-formed architectural prose from thin evidence and from thick. A human coder who is unsure writes awkwardly, hedges, or stops. A model does not.

**The prompt's unit becomes the answer's unit.** Ask for "the governance architecture of this Regulation" and you will receive one architecture per Regulation. This is precisely your **container fallacy** — assuming that provisions in the same act form a single coherent architecture — arriving not as a researcher's carelessness but as an artefact of how the task is framed. In four cases out of four it was the dominant disagreement.

**Completion pressure runs upward.** Your levels are hierarchical, so a model treats the top as the goal. "Indeterminate," and "stop at the configuration level," are not natural completions of a task whose stated object is an architecture. They have to exist as available outputs or they do not occur.

So the elaboration was not an attempt to improve your framework. It was an attempt to find out which of its requirements survive contact with a machine executor, and what has to change in the *recording* for them to survive. That reframing matters to me, because for a while I was carrying two internal labels for the two reconstructions as though they were two intellectual projects. They are not. They are one framework and two levels of procedural explicitness in applying it.

I can be concrete about that. Before running the comparison I built an element-by-element bridge between the two procedures. It records most of the added machinery as *equivalent in conceptual function* to requirements already in your paper: coverage declaration, institutional statements, assignments without a counterparty, qualified relations, candidate configurations, whole-level properties, the architectural inference itself, boundary and sensitivity control, evidential status, the stopping rule, human review, and profiles without composite scores. The genuine additions are narrow: a field in which "stop" and "indeterminate" are legal answers; a candidate status that must be earned; and a mandatory rival-grouping record. There are also two genuine *subtractions*, which I should not hide: the elaborate procedure has no equivalent for your **object** category, and it excluded your strategies and governance logics from basic coding.

---

## 3. The inferential problem

Nine decisions had to be made, in every case, before any architectural statement could be written. None is recoverable from the text by reading. Each is a point where an AI-assisted coder supplies a default unless something stops it.

*Configuration membership* — which relations belong to the same arrangement. *Relation coupling* — whether a link between two arrangements makes them one or leaves them two. *Architecture boundaries* — where one architecture ends, i.e. the container question. *External legal dependencies* — what to do when the actors who carry a configuration are constituted elsewhere. *Legal reference date* — which text, as published or consolidated, at what date. *Attribution of local properties to larger structures* — your ecological fallacy, and the property-bearer requirement. *Uncertainty* — which is a property of the output, not of the evidence. *Stopping* — which needs somewhere to be written. And *candidate versus accepted architecture* — because without that distinction a grouping becomes an architecture by being written down.

The proposition I was testing was that the hard part lies in these transitions rather than in extraction. I think the pilot supports it, with one qualification that I did not anticipate and that changes the recommendation:

> The vulnerable operation is the *upward* transition — configuration to architecture, architecture to governance proposition — where a machine executor completes what the evidence does not warrant. Finer *downward* decomposition at the configuration level is a different operation, and the pilot gives one direct instance in which it made things worse.

---

## 4. How the four-case pilot was conducted

Four instruments: Regulation (EU) 2023/955 (Social Climate Fund), Regulation (EU) 2023/956 (CBAM), Regulation (EU) 2024/1689 (AI Act), and Council Directive 86/361/EEC on the initial stage of mutual recognition of type approval for telecommunications terminal equipment. Two climate instruments, one strict-AI case, one historical transfer case.

Each instrument was reconstructed twice from **one identical official source file**, hash-verified, complete with annexes, retrieved fresh from the Publications Office. That control caught a real problem before it could do damage: two pre-existing local source files failed their recorded hashes, and had the arms run on divergent texts every difference would have been confounded. The instruments were coded as *original acts as published*, not consolidated law — which matters, since Directive 86/361 was repealed in 1992.

One reconstruction applied your framework relatively directly. The other applied the same framework with the additional controls. The comparison itself was preregistered and frozen before either set of outputs was opened: five comparative levels (evidence, relational, configurational, architectural, epistemic), seven mutually exclusive initial match categories, eight evaluation dimensions with no weights and no composite score, eleven mandatory human-review triggers, and an explicit materiality rule whose key clause I want to quote because it governed everything: *longer or more numerous output never converts a difference into a gain.*

The comparison produced 264 comparative units, of which 113 were substantively equivalent; 151 differences, of which 96 were comparatively material; and **56 blinded review cards**. Each card states the common legal evidence, two propositions with no attribution, the exact disagreement, and the precise question — never "which method is better." The arm↔proposition mapping was held in a separate identity key, with blind assignment by a deterministic hash rule.

I then examined six of the fifty-six under blinded conditions, chosen for centrality, with the identity revealed only afterwards. Five supported the propositions produced under the additional controls; one supported the more compact baseline reconstruction.

Three things about this design I should state plainly rather than let you discover. First, the correct description of what happened to the 56 is: **nothing yet**. All fifty-six remain formally open; there is no adjudication register. What I have is targeted blinded validation of six purposively chosen cards — not representative, not statistical, and not a basis for any rate. Second, four of those six are at the architectural level, so the set is weighted towards the question I was most interested in. Third, both arms and the comparator ran on the same model with reasoning effort not exposed to the executor, so "effect of the controls" and "effect of a longer, more structured prompt" are not separated by this design.

---

## 5. What the comparison revealed

The central result is a distribution, and it replicated in all four cases.

| Transition | Material differences |
|---|---|
| text → institutional statements | **1** of 96 |
| statements → relationships | 30 |
| relationships → configurations | 26 |
| configurations → architecture | 23 |
| architecture → proposition (stopping, uncertainty) | 16 |

One material disagreement about what four EU instruments say. Sixty-five about what may be built from what they say. On the Directive — twelve articles — the two reconstructions agreed on 30 of 52 units, and four of the nine material differences were purely epistemic.

The recurring disagreement was the same in every case: whether the instrument constitutes **one** architecture. Three cases produced a whole-act-versus-several-architectures question; the fourth produced a whether-any-architecture question. Your container fallacy, four times out of four, as the default behaviour of an AI-assisted run.

Two further observations cut against a simple reading. On **vertical traceability**, neither reconstruction was clearer in a single one of the 96 material units — your §6.9 requirement was already satisfied by the direct application, and the controls did not improve recoverability. And on **uncertainty calibration**, the dimension was indeterminate in 93 of 96 units: the comparison could not assess calibration before adjudication, so I cannot claim the controls improved it.

I should also say that the baseline arm was not a straw man. Its own stopping records refuse regime claims, refuse frequency reasoning, and refuse implementation and effectiveness claims in every case. On CBAM it noted that Article 1 says the mechanism complements the EU ETS and still declined a regime claim, because the corpus could not support mapping the boundary. That is your framework being applied conscientiously. The difference between the arms is not attention.

---

## 6. Where additional controls helped

Four of the six blinded decisions turned on the configuration→architecture transition, and in each the control at issue was a form of restraint.

**Social Climate Fund.** Direct application: one bounded architecture over the whole Fund design. Controlled: one integrated architecture (plan, payment, control, transfers), plus monitoring and evaluation as an *overlapping* candidate joined through a shared indicator interface, plus the Parliamentary social climate dialogue as an *indeterminate* candidate for which no architecture is asserted. The blinded decision supported the latter.

**CBAM.** Direct application: one architecture over the whole design, medium-high confidence. Controlled: an integrated core, with verification and delegation overlapping but indeterminate in coupling, and the transitional regime, circumvention and reporting arrangements not coupled to it. Supported.

**AI Act.** Direct application: one bounded architecture, "differentiated, hybrid and multilevel," high confidence. Controlled: several partially integrated candidates and — for the Regulation as a whole — the coupling-consequence condition **not satisfied**, so no property attributable to the Regulation as such. Supported.

**Directive 86/361/EEC.** This is the sharpest case. Both reconstructions describe the mechanism identically: the Commission requests CEPT to draw up specifications as NETs; approved laboratories test and certify; a certificate removes further testing; competent authorities recognise it for type approval; recognition can be suspended, with a laboratory opinion, Committee referral, delisting and revocation. Direct application: a bounded formal architecture, high confidence. Controlled: **stop below architecture** — because a NET's legal constitution rests on a Memorandum of Understanding between CEPT signatories, and what counts as an "approved testing laboratory" is fixed by the CEPT accreditation system. Neither is in the Directive. Article 2(8) defines an approved laboratory by reference to conformity with that external system. The reconstruction's reasoning was that an architecture whose central performers and central specifications are constituted elsewhere is not an architecture this Directive constitutes. Supported.

There is a fifth, different in kind and worth noting because it is not about restraint. **CBAM, at the relational level.** Article 20(1) reads: "A Member State shall sell CBAM certificates on a common central platform to authorised CBAM declarants established in that Member State." The direct application recorded the certificate arrangement with the seller *unidentified*. The controlled reconstruction named the Member State as seller and repurchaser and the Commission as platform operator, registrar and canceller. In an instrument whose point is conditioning market access, who sells is constitutive. The blinded decision supported the precise version. This is the one validated instance of a control changing a relational fact rather than restraining an inference — and the rule involved (never fabricate or omit a counterparty) is one both procedures already share.

So the pattern among the five: the controls were endorsed where they **blocked the container default**, where they **refused a whole-level property on failed coupling**, where they **refused an architectural claim resting on external constitution**, and where they **made the text's own actor explicit**.

---

## 7. Where additional controls became excessive

Now the sixth card, which is the one I find most useful.

**AI Act, configuration level.** The question was where three groups of relations belong: designation of notified bodies, operator duties toward authorities, and incident reporting. The controlled reconstruction gave seven separate overlapping arrangements, with designation grouped with certification. The direct application gave three arrangements, with designation grouped with market surveillance. **The blinded decision supported the three-arrangement version.**

I want to resist the easy reading of this, which would be "more detail is worse." Something more specific happened. The controlled arm produced nineteen subconfigurations where the direct application produced three configurations — and it did not thereby answer the membership question. It *deferred* it to the architecture layer, where it then grouped the operator chain, designation, certification and standardisation into one integrated candidate. Which is to say: designation with certification, the grouping the decision rejected. The finer intermediate layer multiplied objects without improving the judgment it was supposed to inform.

That generalises to a real criticism of what I built. Across the four cases the controlled procedure produced roughly 2,400 analytical records — 1,163 on the AI Act alone — against 96 material differences and 56 cards. A large share of what it captured is non-material by the comparison's own rule: information-reporting is the largest relation class in three of four cases (136 of 281 relations in the AI Act, 48 of 101 in CBAM), and purely informational or administrative relations were treated as non-material. The overhead is worst where the instrument is smallest: 232 records for a twelve-article Directive on which the two arms agreed in 30 of 52 units and differed on exactly one inference. It generated 89 internal review items of its own before the comparison added 56 more. And it did not buy traceability, which was equivalent in every unit.

The honest summary is that the apparatus was built to make the inferential transitions explicit and ended up making the *inventory* explicit. Those are different goals, and only the first was worth the cost.

---

## 8. What safeguards should remain

My proposal is to keep roughly this much and no more, as fields on records that already exist rather than as additional analytical strata:

1. **Source and version** — hashed official text, declared coverage, legal status and reference date.
2. **Named parties and modality** on every relation; a duty without an identifiable counterparty stays an assignment rather than being forced into a dyad.
3. **Membership rule** stated for each configuration — stated once, at the granularity the governance question needs, and revised rather than multiplied.
4. **One coupling question** for any candidate whole: *what legally evidenced coupling joins these configurations, and what property follows for the whole rather than for each part?* — answered independently of the property expected, with "indeterminate" as an authorised answer.
5. **External constitutive dependency** flagged wherever an actor, device or specification central to a configuration is constituted outside the corpus.
6. **Candidate status and stopping level** recorded as values, with "no architecture warranted" available as a result.
7. **One rival grouping** per architectural claim, plus a coverage statement for any absence-dependent property — since necessity, exclusivity and substitutability are claims about what was searched.
8. **Uncertainty** as a short typed field that travels with the claim into any output.

What should go: the nineteen-table schema, the six-stratum identifier system, the separate closure and property registers, the duplicated direction fields, the internal queue as a distinct artefact class, and the per-phase gate apparatus. Also worth restoring: your object category, and your strategies and logics layer, both of which the elaborate procedure dropped.

The underlying principle is one the pilot taught me rather than one I started with: **for a machine executor, a principle with no output slot has no effect.** Your stopping rule is in the paper; both arms descend from it; only one arm had a field in which "stop here" could be written, and in that arm, once, it was written.

---

## 9. Returning to regulatory intermediation

Everything above is instrumental. The reason to get the inferential discipline right is to use it on your substantive questions, and I think the pilot shows the coding can now carry more of that weight than I expected — with one genuine surprise.

**What makes an intermediary structurally important.** The coding establishes, with provenance, the facts your §6.12 asks for: whether an intermediary's decision is a legal *condition* for an effect (CBAM Article 8(1); Directive 86/361 Article 6(2)); what legally consequential capacities it holds (an AI Act notified body issues, extends, restricts, suspends or withdraws certificates under Article 44, audits quality management systems, and may require access to training data and to development premises under Annex VII); the breadth of functions routed outward; and formal limits on its leverage (Article 43(1): a provider may choose any notified body). What the coding can only *suggest* is indispensability and substitutability, because these are absence-dependent — a claim that no alternative path exists is a claim that none was found, and needs a declared coverage statement. And structural centrality must be weighted by relation type, or degree measures will simply track informational traffic.

**Who governs the intermediaries.** Your question, and the surprise is here. The full candidate chain — accreditation, authorization, reporting, investigation, restriction, suspension, withdrawal — is recoverable at relation level. For the AI Act it is dense and entirely internal: ten distinct second-order relations across Articles 28–38, from the accreditation certificate under Article 29(2) through withdrawal of a designation under Article 36(3) to the Commission's own investigation power under Article 37. But for CBAM, the only relation governing the verifier *inside* the Regulation is Article 18(2) — the national accreditation body may accredit on request. The criteria and the supervision sit outside: "accredited verifier" status for CBAM purposes arises under Commission Implementing Regulation (EU) 2018/2067, and "national accreditation body" is constituted by Regulation (EC) No 765/2008 Article 4(1). For Directive 86/361 the chain is almost wholly external, as described above.

This is why the external-dependency control turns out to earn its place *substantively* and not just procedurally. Without it, a CBAM verifier and an AI Act notified body look like similar intermediaries under similar oversight. With it, they do not: one instrument constitutes the governance of its intermediaries, the other imports it. Whether that is a general structural variable, I cannot say from four instruments — and none of the external instruments was retrieved, since retrieval was deliberately excluded. But it is measurable, which is the claim I want to make.

**When intermediation complements rather than substitutes for hierarchy.** At the level of formal relations, the AI Act supports the embedded reading cleanly. Verification, certification and audit are routed through the notified body; authorization, designation and its withdrawal, the power to require suspension of certificates the body has issued, market surveillance, Union safeguard review and penalties remain public. No consequential public power is transferred, and the intermediary's own authority is revocable by the authority that conferred it. CBAM shows the same shape over the target, with the caveat that the hierarchy *over the intermediary* is not visible within the Regulation. Directive 86/361 has a clear internal hierarchy over *recognition* — suspension, laboratory opinion, Committee referral, delisting, revocation — but its intermediary side rests on external constitution, which is exactly why the controlled reconstruction declined an architectural claim there. And the Social Climate Fund has no third-party intermediary at all: its actors are Union institutions, Member States, entrusted implementing and audit authorities, control bodies, recipients and consulted stakeholders. A useful reminder that a complex architecture need not be an intermediated one.

So: three instruments, all consistent with complementarity rather than substitution. That is suggestive and nothing more — three instruments, two climate-adjacent, one repealed in 1992, selected for a methodological test rather than for variation in intermediation.

**What explains variation.** The coding can now produce the dependent variable — a comparable per-instrument profile across your six dimensions, with the location of second-order governance recorded. It cannot answer the question. That needs a comparative design with a defensible sampling frame, which is the point of the next phase rather than of this one.

---

## 10. What the current coding can and cannot answer

**Can support:** formal authority and its object; legal duties and their modality; discretion the text grants; formal gateways within the coded corpus; institutional dependence, including the legal source of an actor's status; formal supervision chains; formal answerability channels; structural relationships and configurations where coupling is evidenced; the architecture's boundary *including the negative result*; and comparative structural difference between instruments.

**Cannot establish:** effectiveness; whether third-party verification improves quality; capture — the AI Act's free choice of notified body is equally consistent with competition and with competitive laxity, and the text cannot distinguish them; implementation quality; behavioural consequences; whether an answerability channel produces answers; costs, delays, market concentration or enforcement rates; operational centrality as against formal; regime boundaries; anything resting on an unverified external instrument — 73 constitutive external references across the four cases, none retrieved; and anything resting on absence without a coverage statement.

Three claims specific to this exercise that I do not want overstated. The comparison establishes where the two procedures diverge, not which is more accurate — none of the 56 cards has been adjudicated. The six validated cards support "here is a pattern worth testing," not a rate, a proportion or a superiority claim, and the card that went the other way is part of the evidence rather than an exception to it. And because both arms ran on the same model, nothing here establishes that the controls as such caused the difference.

---

## 11. Proposed next phase

**Phase 1 is complete.** The operationalization of architectural inference has been stress-tested on four instruments, and the stress-test found the vulnerable transitions.

**Phase 2** is integration and shrinkage. Fold the eight surviving safeguards into the existing coding protocol as fields, retire the apparatus, and restore your object and strategy/logic layers. Two cheap pieces of validation belong here and not later: archive the six blinded decisions with their justifications, so that the one claim in this note resting on them becomes auditable; and run an arm-blind control in which the same model receives the same task at two levels of prompt structure, to find out how much of the observed difference is the controls and how much is the prompt. Both are a day's work and both could change what Phase 3 should carry.

**Phase 3** is substantive: use the simplified protocol on your intermediation questions comparatively, across instruments and sub-regimes, with the second-order governance chain and the internal-versus-external location of that chain as recorded variables. That is where I think the method stops being interesting in itself and starts producing findings about regulatory governance. It also means retrieving and coding the external instruments this pilot deliberately left outside — Regulation 765/2008, Implementing Regulation 2018/2067, the CEPT material — because for two of the four cases the answer to "who governs the intermediaries" lives there.

What I would avoid is a Phase 4 of further methodological development. The pilot's clearest lesson about my own work is that the apparatus outgrew the question it was built to answer.

---

## 12. Conclusion

I tried to operationalize the inferential sequence in your framework with AI assistance, found where that kind of coding becomes vulnerable to unsupported inference, tested some safeguards against it, and now think the procedure can be simplified and turned towards your substantive questions.

The finding I would stand behind is narrow and, I think, useful. Extraction is not the hard part — one material disagreement at the evidence level across four instruments. The hard part is the upward transitions, and the characteristic failure is the one your paper already names: treating an act as an architecture because it is an act. A machine executor commits that error by default, because the instrument is the unit of the prompt and the top of the ladder is the goal of the task. The safeguards that help are the ones that make restraint an available output — a stopping level, a candidate status, an external-dependency flag, a coupling question whose honest answer may be "indeterminate."

The safeguards that do not help are the ones that subdivide. I built a great deal of the second kind, and one blinded decision out of six was enough to show it: greater granularity is not greater analytical quality, and a finer intermediate layer can defer a judgment rather than improve it.

Two things remain genuinely open. Nothing here is adjudicated, so these are observations under a thin evidence base rather than results. And since both reconstructions ran on the same model, I cannot yet tell you how much of the difference is the discipline and how much is simply a longer prompt. I would like to close that second gap before we build anything on this.

What I would most value from you is a view on whether the eight surviving safeguards are the right eight, and whether the internal-versus-external location of second-order governance over intermediaries looks to you like a variable worth building a comparative design around.
