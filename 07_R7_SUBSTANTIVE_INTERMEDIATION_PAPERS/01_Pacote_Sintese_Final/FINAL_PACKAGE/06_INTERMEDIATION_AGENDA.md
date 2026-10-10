# 06 — Returning to regulatory intermediation

**Purpose.** Connect the coding to David's four priority questions, and say for each what legal-text coding can establish, what it can suggest, and what requires new empirical evidence.

**Framing.** None of the concepts below is new. Intermediation centrality as a six-dimensional property — prevalence, functional breadth, authority, dependency/indispensability, structural position, regulatory embeddedness — is David's (§6.12). "Who governs those who themselves govern" is his phrase, from the conclusion. What follows is an assessment of which of these dimensions the coding can now actually carry, using the four frozen cases as evidence of feasibility.

**Standing constraints.** Structural importance is not frequency (§6.6, §6.12). Intermediation is not privatization: a law may route governing through third parties while retaining every consequential decision in public hands, and the AI Act and CBAM both do so. Formal architecture is not implementation (§6.13–§6.14).

**Evidence base.** Four instruments, frozen relational reconstructions. The pilot was designed to test an inferential procedure, not to measure intermediation. Everything below is a feasibility assessment supported by illustrations from these four cases, not a comparative finding about EU law.

---

## Q1. What makes an intermediary structurally important?

### What current legal-text coding can establish

Formal, instrument-bounded facts about position and power, each traceable to a provision:

- **Whether an intermediary decision is a legal condition.** Whether a certificate, verification or approval is a necessary condition for a legal effect — market access, legal status, a permitted calculation basis. CBAM Art. 8(1): a declarant must ensure embedded emissions are verified by an accredited verifier; Annex IV pt 5(e) with Art. 7(3): certification by an accredited verifier is one of the cumulative criteria for using actual emissions for imported electricity. The verifier's finding determines whether declared emissions count as verified (Annex VI pt 1). Directive 86/361 Art. 6(2): competent authorities recognise a laboratory's certificate for type approval, and no further tests are required where a certificate exists.
- **The legally consequential capacities held by the intermediary.** Whether it decides, or only informs. AI Act: a notified body issues, refuses, extends, restricts, suspends or withdraws a certificate (Arts. 44(2), 44(3)); audits the provider's quality management system periodically (Annex VII §5.1); may require access to training, validation and testing data sets, including through APIs, and to the premises where systems are developed and tested (Annex VII §4.3, §5.2). These are powers over legal status, not informational roles.
- **Functional breadth and allocation.** Which governance functions are routed through third parties and which are retained. In the four cases the relation-level reconstruction distinguishes verification/assurance, monitoring, authorization/designation, enforcement, rule-making/standard-setting, information provision and adjudication, so the division of labour between public bodies and intermediaries is directly readable.
- **Formal gateway position.** Whether the intermediary sits at a necessary stage of a sequence — David's "sequence" and "consequence" criteria (§6.6).
- **Whether the regulated actor can choose.** AI Act Art. 43(1) third subparagraph: a provider may choose any notified body. That is a formal limit on any one body's leverage and a measurable difference from a single-gatekeeper design.

### What it can suggest

- **Indispensability and substitutability**, which David treats as central (§6.12). These are *absence-dependent* properties: a claim that no alternative pathway exists is a claim that none was found. The pilot's own rule is the right one — such properties require a declared coverage statement, and "not found" is a statement about the search. Coding can suggest indispensability strongly where a provision makes the intermediary decision a condition, and weakly otherwise.
- **Structural centrality.** The typed relations support degree and brokerage measures, but §6.12 is right that position does not establish authority: 136 of 281 AI Act relations and 48 of 101 CBAM relations are information-reporting, so degree measures will be dominated by informational traffic unless weighted by the kind of relation.
- **Profiles rather than ranks.** The six dimensions can be reported side by side per instrument. They should not be summed; the pilot's frozen rules forbid composite scores and the manuscript (§6.12) asks that the dimensions be retained separately.

### What requires new empirical evidence

- Whether an intermediary that is formally indispensable is operationally consequential — whether certificates are refused, whether audits find anything, whether gateways bind.
- Whether formal choice among notified bodies produces competitive laxity or not.
- Market structure: how many bodies actually operate, and with what concentration.
- Everything about expertise, capture, cost and behaviour.

### Operationalizable concepts, with the honest status of each

| Concept | Status in legal-text coding |
|---|---|
| authority (over legal status) | **codeable** — directly, from the power conferred |
| discretion granted by law | **codeable** — where the text states a judgment, threshold or proportionality margin |
| functional breadth | **codeable** — from the function field across relations |
| gateway position | **codeable** — where a provision makes the decision a condition |
| accreditation, authorization, supervision, review, sanction, removal | **codeable as relations** — see Q2 |
| indispensability | **codeable only with a declared coverage statement** |
| substitutability | **codeable only with a declared coverage statement** |
| configuration / network position | **codeable but weakly interpretable** — must be weighted by relation type |

---

## Q2. How are intermediaries themselves governed? (the governed governors)

This is David's own question. Treating it as an operational path, the analytical structure is:

```
PUBLIC / AUTHORIZING / ACCREDITING / REVIEW BODY
                    |
                    v
              INTERMEDIARY
                    |
                    v
                 TARGET
```

The candidate governance relations over the intermediary — accreditation, licensing, authorization, supervision, reporting, review, sanction, removal — are exactly the relation types the coding already records. The pilot shows they are recoverable, and it shows something more interesting: **the chain is sometimes constituted inside the instrument and sometimes outside it.**

### What current legal-text coding can establish

**The AI Act: a dense second-order chain inside the instrument.** From the frozen relational record:

| Relation | Provision | Direction |
|---|---|---|
| national accreditation body issues an accreditation certificate attesting the body meets the requirements | Art. 29(2) | accrediting → CAB |
| conformity-assessment body applies to the notifying authority for notification | Art. 29(1)–(2) | CAB → authority |
| notifying authority assesses, designates, notifies and monitors conformity-assessment bodies | Art. 28(1) | authority → CAB |
| Commission may object to a notification within two weeks | Art. 30(4) | Commission → authority |
| notified body must update its documentation on relevant changes; must inform of subcontracting; must inform of cessation | Arts. 29(4), 33(1)/(4), 36(3) | body → authority |
| notifying authority withdraws the designation | Art. 36(3) | authority → body |
| notifying authority investigates and may restrict, suspend or withdraw the designation, the measure depending on seriousness | Arts. 36(4)–(5) | authority → body |
| notifying authority may require the body to suspend or withdraw certificates it has issued | Art. 36(7)(c) | authority → body |
| Commission investigates doubts about competence and may suspend, restrict or withdraw a designation | Art. 37(1), (4) | Commission → body |
| notified bodies must participate in a sectoral coordination group | Art. 38(2) | Commission/authority → bodies |

Ten distinct second-order relations, entirely within the Regulation. This is high regulatory embeddedness in David's sense (§6.12), and it is directly codeable.

**CBAM: a thin chain inside, the substance outside.** In the frozen reconstruction the only governance relation over the verifier located *within* the Regulation is Art. 18(2): the national accreditation body may, on request, accredit a person as a verifier. No supervision, suspension or withdrawal relation over the verifier is recorded inside the instrument. The two external dependencies carry the rest:

- the position "national accreditation body" is constituted by **Regulation (EC) No 765/2008 Art. 4(1)** (EXT-014, constitutive);
- the status "accredited verifier" for the purposes of this Regulation arises from accreditation under **Commission Implementing Regulation (EU) 2018/2067** (EXT-018, constitutive).

**Directive 86/361/EEC: the chain is almost entirely outside.** Which laboratories count as "approved testing laboratories" is fixed by the **CEPT accreditation system** (EXT-006, constitutive); Art. 2(8) defines an approved laboratory by reference to conformity with that external system; and a NET's legal constitution rests on a **Memorandum of Understanding between CEPT signatories** (EXT-005, constitutive). What the Directive itself constitutes is the *recognition* of the certificate (Art. 6(2)) and the *suspension* of that recognition (Art. 8), not the governance of the laboratory.

**The Social Climate Fund: no third-party intermediary at all.** Its 27 positions are Union institutions, Member States, implementing and audit authorities, OLAF, the Court of Auditors, the EPPO, final recipients, and consulted stakeholders. Audit and control run through entrusted public authorities; stakeholder involvement is consultation, not intermediation. It is the family's low-intermediation comparison case — and a useful reminder that a complex governance architecture need not be an intermediated one.

### What it can suggest

A hypothesis worth stating carefully, because it is exactly the kind of claim this pilot was built to discipline:

> Where a law governs through intermediaries, the second-order governance of those intermediaries may be constituted inside or outside the instrument, and this is a structural variable in its own right.

The four cases are consistent with that — AI Act inside, CBAM mostly outside, 86/361 almost entirely outside — but four instruments across three decades and three policy fields cannot establish a pattern, and the external instruments were never retrieved. What the cases do establish is that the variable is **measurable**, and that measuring it requires the external-dependency control. Without it, the CBAM verifier and the AI Act notified body look like similar intermediaries with similar oversight; with it, they do not.

### What requires new empirical evidence

- Whether the external instruments in fact supply equivalent supervision (requires retrieving and coding Regulation 765/2008, Implementing Regulation 2018/2067, and the CEPT instruments — all excluded from this pilot by design).
- Whether second-order powers are exercised: designations withdrawn, certificates suspended, bodies sanctioned.
- Whether dense formal oversight corresponds to effective oversight. It may not. A reconstruction of Arts. 28–38 establishes an answerability channel and nothing about what travels through it.

---

## Q3. When does intermediation complement rather than substitute for hierarchy?

### The structural pattern, and whether the cases support it

The pattern to test:

```
THIRD PARTY / INTERMEDIARY          PUBLIC AUTHORITY
  verification                        authorization
  certification            +          review
  monitoring                          enforcement
  information                         sanction
                                      final decision
```

**Supported in the AI Act, at relation level.** The notified body verifies conformity (Art. 34(1)), issues and may withdraw certificates (Art. 44), and audits quality management systems (Annex VII §5.1). The public side retains: designation of the body and its withdrawal (Arts. 28, 36), the power to require the body to suspend or withdraw certificates it has issued (Art. 36(7)(c)), national market surveillance (Art. 74), Union safeguard review (Arts. 79–83), and penalties and administrative fines. The market surveillance authority informs the relevant notified body of its measures (Art. 79(2)), not the reverse. On the formal record, intermediation here is embedded in hierarchy rather than displacing it: no consequential public power is transferred to the body, and the body's own authority is revocable by the authority that conferred it.

**Supported in CBAM, with a caveat.** Verification is routed through accredited verifiers; authorization of declarants, the registry, certificate sale and cancellation, penalties and the circumvention procedure remain with Member States and the Commission. The caveat is the one from Q2: the verifier's own accreditation and supervision regime sits outside the instrument, so the hierarchy *over the intermediary* is not visible within the Regulation even though the hierarchy *over the target* plainly is.

**Partially supported in Directive 86/361, and this is where the pilot's restraint matters.** The hierarchical element is clear and internal: the Commission may suspend recognition, seek a laboratory opinion, refer to the Committee, delist a specification and revoke (Art. 8(1)–(5)). But the intermediary side rests on external constitution, which is precisely why the controlled arm declined to assert an architecture here. One can say the Directive constitutes a *recognition-and-safeguard* hierarchy over certificates; one cannot say, from the Directive alone, that it constitutes an intermediated architecture.

**Not applicable to the Social Climate Fund.** No third-party intermediary.

### What it can suggest

That "complement or substitute" is answerable as a structural question about **which functions are retained**: whether final decision, authorization, enforcement and sanction stay public while verification, certification, monitoring and information are routed outward. On that reading the three intermediated cases here all look like complementarity rather than substitution. This is suggestive and no more: three instruments, two of them climate-adjacent and one repealed in 1992, selected for a methodological test and not for variation in intermediation.

### What requires new empirical evidence

Everything about operation. Formal retention of enforcement authority is compatible with enforcement that never happens; formal revocability of a designation is compatible with designations that are never revoked. Whether intermediation complements hierarchy *in practice* is a question about implementation and operational architecture (§6.14), and legal-text coding establishes only the formal baseline against which it can be asked.

---

## Q4. What explains variation in intermediation across laws and sub-regimes?

### What current legal-text coding can establish

Coding can establish the **dependent variable** — a comparable, traceable profile per instrument across David's six dimensions, with configurational position and the location of second-order governance recorded. The four cases show that such profiles differ in structurally interesting ways: dense internal second-order governance (AI Act), thin internal and heavy external (CBAM), almost wholly external (86/361), and absent (SCF).

It can also establish the **structural covariates** that are themselves legal facts: whether conformity assessment is conditional or mandatory; whether the regulated actor may choose its assessor; whether the function routed outward is verification or rule-making; whether the instrument constitutes its own accreditation regime or imports one.

### What it can suggest

Candidate explanations visible in these cases but far from established:

- **The nature of the task.** Verification of technical or quantitative facts is routed outward in all three intermediated cases; authorization and sanction never are.
- **The availability of an existing accreditation infrastructure.** CBAM and 86/361 import one; the AI Act builds on the Union's own notification machinery and constitutes its supervision internally. Whether a law constitutes or imports its intermediary infrastructure may depend on what already exists in the field.
- **Instrument type.** The one case with no intermediation is the one that distributes money to Member States rather than conditioning private market access. That is a plausible structural regularity and it is also a sample of one.

### What requires new empirical evidence

A real answer to Q4 needs a comparative design: many instruments, sampled on a defensible frame, coded with the simplified protocol, with sub-regime and task type as covariates. Four cases chosen to stress-test an inferential procedure cannot support it, and should not be presented as a pilot for it.

---

## What this section does and does not claim

**It claims:** that the relations David's framework needs for the intermediation agenda — authority over legal status, conferred discretion, functional allocation, gateway conditions, and the full accreditation/authorization/supervision/review/sanction/removal chain over the intermediary itself — are recoverable from legal text at relation level, with provenance, and that the pilot demonstrates this on four instruments. It also claims that the external-dependency control is **substantively necessary** for the second-order question, not merely procedurally tidy, because in two of four cases the governance of the intermediary is constituted outside the instrument that relies on it.

**It does not claim:** any comparative finding about intermediation in EU law; any measurement of intermediation centrality for these four instruments; that the cases are a sample of anything; or that formal structure licenses any inference about effectiveness, capture, expertise or practice.
