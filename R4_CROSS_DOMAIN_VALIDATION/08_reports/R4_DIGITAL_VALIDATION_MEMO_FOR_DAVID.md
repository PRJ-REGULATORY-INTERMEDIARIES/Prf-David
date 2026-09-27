# Testing the Portability and Parsimony of a Regulatory Intermediation Dataset
## R4 Digital-Law Structural Validation

**Status:** R4 digital *structural* validation round complete, including a post-hoc sensitivity
audit of the Action variable. Regulator/intermediary/target coding and mechanism coding have not
begun.

---

## 1. Why this round was conducted

You asked three questions of the digital-law exercise:

1. Which variables are genuinely worth coding, relative to what they cost to code?
2. How compatible is the green-regulation dataset architecture with digital regulation?
3. What differences in regulatory governance emerge between the green and digital domains?

This memo reports on the first two, and deliberately does not attempt the third. The third question
requires the theoretical coding layer — regulator, intermediary, target, and mechanism — which has
not been started. What we have completed is the layer beneath it: whether the structural
architecture built on the green corpus can be applied to digital law at all, and whether each of its
variables earns its keep.

That is a narrower claim than "R4 is done". It is also, as it turns out, where the more useful
findings were — several of them about the coding architecture itself rather than about the law.

## 2. The digital corpus

Three instruments, suggested by Rotem, in their frozen original form:

| Instrument | CELEX | Structure |
| --- | --- | --- |
| GDPR, Regulation (EU) 2016/679 | 32016R0679 | 99 articles, 173 recitals |
| Digital Services Act, Regulation (EU) 2022/2065 | 32022R2065 | 93 articles, 156 recitals |
| AI Act, Regulation (EU) 2024/1689 | 32024R1689 | 113 articles, 180 recitals, 13 annexes |

The green baseline against which portability is judged is the completed R3 corpus of five EU
instruments, whose mechanism ontology remains a provisional researcher-adjudicated construct and is
not assumed to transfer.

## 3. The structural dataset

Structural extraction produced **1,404 records**: 485 GDPR, 424 DSA, 495 AI Act. The unit is

> **legal provision × actor × legal action**

Of the 1,404 records, 842 come from operative articles, 546 from recitals and 16 from annexes. Only
the AI Act contributes annex records, which is itself a structural difference worth noting: its
normative content is distributed across annexes in a way the green instruments and the other two
digital instruments are not.

This extraction is treated as immutable. Nothing reported here modified it.

## 4. Validation design

The round was layered, so that expensive human attention is spent only where cheaper methods cannot
decide:

1. **Deterministic structural extraction** over the three frozen texts.
2. **Initial QA**, which flagged counterpart/recipient over-attribution and actor/action
   fragmentation.
3. **Human diagnostic** on 12 purposively selected cases. All 12 contained confirmed defects —
   which reflects how they were selected and is not a corpus error rate. The important result was
   qualitative: the human root cause frequently differed from the pattern the models had detected.
4. **Fifteen human-derived structural rules** frozen from that diagnostic, used as guidance rather
   than as automatic truth.
5. **Deterministic triage** over all 1,404 records. It rediscovered 9 of the 12 known defects and
   missed 3, which remain recorded blind spots.
6. **Repair-family compression**, which grouped the corpus into 211 repair families and reduced the
   advanced-review workload from 524 cases to 131.
7. **Advanced legal review** of 143 cases: 99 family representatives, 32 individual cases, and 12
   **NO_REPAIR diagnostic controls** — records the compression had declared to need no repair.
8. **A post-hoc sensitivity audit** of the Action variable, described in section 5, prompted by a
   representation problem we found after the review was complete.

Batches 1 to 3 were reviewed with GPT-5.6 Terra High under OpenAI Codex. That environment reached
its usage limit mid-round, and batch 4 was completed in Claude Code as a planned continuity
fallback. For that batch the researcher-selected model was Claude Opus 5.5 Extra High; the runtime
reported Claude Opus 5 (`claude-opus-5`), and we could not verify the relationship between the two
labels from inside the session, so both are recorded and neither is asserted to be the other. No
earlier batch was rerun or relabelled; per-row model provenance is preserved, and results are
reported separately by model where that matters.

## 5. A correction we had to make to our own method

Before the substantive findings, one result about the instrument, because it changes how one of the
headline numbers should be read.

The review interface showed reviewers a field called Action. That field carried only the
*normalised* action label — `LEGAL_ACTION`, a controlled-vocabulary value such as "notify or
inform". The dataset separately stores `LEGAL_VERB`, which holds the source predicate with its
modality, and a `MODALITY` category. Corpus-wide, an explicit modal appears in `LEGAL_VERB` in
**1,370 of 1,404 records** but in `LEGAL_ACTION` in **5**.

Reviewers working from that interface therefore saw an Action field that looked stripped of deontic
force, and recorded it as defective. The modality had not been lost; it was in an adjacent column
they were not shown.

We re-audited all 143 Action judgments against the full `LEGAL_ACTION` + `LEGAL_VERB` + `MODALITY`
representation, without reopening any other field:

| | Count |
| --- | --- |
| Action corrections as originally recorded | **87** |
| Action corrections on sensitivity recount | **63** |
| Judgments changed | 26 (25 from defective to correct, 1 the other way) |
| Judgments where the verdict held but part of the stated reason dissolved | 16 |
| Overall defect decisions materially affected | **1 of 143** |

Both figures are reported; the 87 stands as the frozen review result and is not overwritten. The 63
is a *post-hoc action representation sensitivity result*, not a re-review. The important number is
the last row. In 24 of the 25 cases that flipped, the record was defective on other grounds anyway
— a mis-spanned object, a relational field quoting the wrong sentence — so the overall picture of
the corpus is essentially unchanged. Only one record's defect rested on the Action field alone.

The same distinction applies to the defect totals. Frozen: YES 111, PARTIALLY 15, NO 17.
Sensitivity-adjusted, descriptive only: YES 111, PARTIALLY 14, NO 18.

Two things survive the audit intact and are worth separating from the artefact:

- **Entitlement constructions are genuinely damaged.** Where the GDPR says "the data subject shall
  have the right to obtain", the dataset records "have the right to obtain" with modality coded
  UNCLEAR. The "shall" is missing from *both* action fields. This was not a display problem.
- **Coordinated predicates are genuinely collapsed.** Where a provision imposes two obligations,
  the second is frequently absent from the predicate and buried inside the object of the first.

We report this at length rather than quietly correcting the number, because the finding generalises:
a coding interface that shows a coder one of several fields holding a construct will produce
confident, systematic, wrong judgments about that construct. That is a design lesson for the
project, not only a footnote about this round.

## 6. Main findings

Across all 143 reviewed cases: 111 defects confirmed, 15 partial, 17 clean. Proposed field
corrections number 47 for Actor, 87 for Action as recorded (63 on sensitivity recount), 83 for
Object, 88 for Counterpart and 98 for Recipient.

These proportions describe the reviewed set, which was purposively selected to concentrate suspected
defects. They are not corpus prevalence.

The defects cluster into three recurring families:

- **Span-boundary errors.** The action or object span cuts across a grammatical constituent, or one
  field absorbs the head of its neighbour. GDPR Article 42(8), for instance, splits the phrase
  "data protection | seals and marks" across the action and object fields.
- **Cross-sentence relational copying.** Counterpart and Recipient hold an identical prepositional
  phrase lifted from a different sentence of the same provision, often truncated mid-word.
- **Coordinated-predicate collapse.** Where a provision imposes two obligations, the second is
  buried inside the object of the first and ceases to exist as a separate record.

The third is the most consequential for later analysis, because it silently deletes obligations from
the dataset rather than merely misplacing text.

## 7. Variable parsimony

Deterministic inspection of all 1,404 records, recomputed for this memo, gives the following. The
distinctions between the rows matter more than the overlaps themselves.

| Pair | Overlap | Exactness | Status |
| --- | --- | --- | --- |
| Counterpart / Recipient | 1,404 of 1,404 identical | exact textual equality | **retain both, fix the population rule** |
| Action object / Information-or-material object | 1,404 of 1,404 identical | exact textual equality | **strong redundancy candidate** |
| Structural ambiguity / Extraction confidence | derivable one way | deterministic transformation | **drop structural ambiguity** |
| Legal action / Legal verb | never identical | complementary, not redundant | **retain both, never show one alone** |
| Modality / Legal verb | largely recoverable from the verb | partial overlap | **retain, but audit the categories** |

Three comments on that table.

**The second row is the clean redundancy.** The two object fields are textually identical in every
record in the corpus and are never populated independently. Unlike the relational pair, advanced
review produced no case in which the underlying distinction was realised. On present evidence this
is one variable being coded twice.

**The third row is one-way, and we previously overstated it.** `EXTRACTION_CONFIDENCE = LOW`
coincides exactly with `STRUCTURAL_AMBIGUITY = YES`, but `AMBIGUITY = NO` splits into HIGH and
MEDIUM. Confidence therefore carries strictly more information, and ambiguity is derivable from it
rather than the two being interchangeable. Ambiguity can be dropped; confidence cannot.

**The fourth row is the opposite of redundancy.** Action is not one variable but a structured
construct across `LEGAL_ACTION`, `LEGAL_VERB` and `MODALITY`. Its coding burden should be assessed
as a construct, and no analysis should read the normalised label alone — which is exactly the
mistake our own review interface induced.

One caution about the quality flags. `EXTRACTION_CONFIDENCE` did not reliably separate defective
from non-defective records *within this review set*: of 25 reviewed cases the extraction itself
rated HIGH, advanced review still found 18 defective and 5 partial against 2 clean. Because the
review set was deliberately enriched for suspected defects, this is not an estimate of the flag's
predictive performance on the corpus. It does mean the flag cannot be used to decide what to skip.

## 8. Counterpart and Recipient

This is the sharpest illustration of why an observed redundancy is not a conceptual one.

In the original extraction the two fields are textually identical in **1,404 of 1,404** records —
995 where both are populated, 409 where both are empty — with zero counterpart-only and zero
recipient-only cases. On that evidence alone the obvious inference is that one variable is redundant.

Advanced review contradicts that inference. It returned:

- **27 RECIPIENT_ONLY** — an express addressee with no counterpart. GDPR Article 14(2) names the
  data subject as addressee of the controller's duty to provide information; DSA Article 52(2) names
  the Commission as addressee of Member States' notification duty.
- **14 COUNTERPART_ONLY** — a relational party that is not an addressee. Under GDPR Article 17(1)
  the data subject obtains erasure *from* the controller: the controller is the other party to the
  relation, not the recipient of a transmission.
- **95 NEITHER** and **7 UNCERTAIN**.
- **0 BOTH_SAME_ENTITY_JUSTIFIED** and **0 DIFFERENT_ENTITIES**.

The defensible interpretation: *the initial extraction operationally collapsed two legal-relational
positions that are, in at least some legal propositions, structurally distinct.* The identity across
the corpus is an artefact of how the extractor populated the fields — it copied one span into both.

That penultimate row matters too. In 143 reviewed cases the review never once found a proposition
where the same entity genuinely occupies both positions. The two variables are not duplicates; they
are two roles, one of which was being filled by accident.

The implication for coding burden is not "drop one field". It is that the two fields currently cost
two columns and deliver one, and that fixing the extraction would add real information at no
additional cost to the human coder.

## 9. What travels from green to digital

**Structurally portable.** The provision × actor × action unit applies to digital law without
redefinition. All three instruments decomposed into it, and the records are distributed fairly
evenly (485 / 424 / 495) despite substantial differences in length and drafting style. Actor is the
most robust variable: 47 corrections in 143 reviewed cases, the lowest of the five.

**Portable with adaptation.** The relational variables. Counterpart and recipient are meaningful in
digital law — the review demonstrates both roles occurring separately — but the extraction rules
that populate them do not survive the transfer. Digital regulation, and the GDPR in particular, is
dense with prepositional phrases ("from the controller", "to the information referred to in
paragraph 1") that look relational and are not. Six of the fifteen frozen human rules address
precisely this, which suggests the problem was visible in the green work and is amplified here.

**Not yet resolved.** Object remains the weakest variable: 83 corrections in 143 cases, and it is
the field into which everything unassigned tends to fall. The AI Act's annex-borne normative content
has no clear green analogue. And passive constructions with an explicit agent turn out to lack a
coding convention altogether — the frozen rule set covers passives with *no* actor but is silent on
passives where the agent is named, which is now recorded for your adjudication.

## 10. What this round does *not* show

- **It is not a corpus error rate.** The 143 reviewed cases were selected to concentrate suspected
  defects. Nothing here licenses a claim about what proportion of the 1,404 records is defective.
- **The 12 controls are not a blinded test.** They were selected before review as NO_REPAIR
  diagnostic probes, but the implementation did not guarantee reviewer blinding: the file
  identifying them lists all twelve with no batch column, and the protocol requires reading it to
  unblind each batch in turn. They therefore provide diagnostic evidence about compression coverage
  rather than a blinded estimate of false-negative performance. No false-negative rate is computed
  from them. Seven of the twelve contained defects; none was graded serious and none showed actor
  invention.
- **Regulator/intermediary/target coding has not started.**
- **Mechanism coding has not started.** The R3 mechanism ontology remains provisional and
  untransferred.
- **Rotem's independent coding has not been consulted**, deliberately, so that the later comparison
  remains a genuine independent inter-coder and inter-method test.
- **No substantive green × digital governance comparison has been made.** Structural extraction
  cannot support claims about governance differences, and we have not made any.

One further caveat: the two reviewing models applied slightly different thresholds for what counts
as an action or object defect, so batch-level defect proportions should not be pooled naively, and
we have not used the differing case sets to compare the models.

## 11. Where the repair stands

Of 99 family representatives reviewed, **none produced an unconditionally validated repair
template**. Sixty-four are validated *with conditions*, 16 need more representatives, 9 need human
review and 8 were rejected.

Grouping by family, 50 families have all their reviewed representatives conditionally validated,
covering **296 corpus records**. A further 141 records sit in 6 families whose representatives
disagree with each other, and are excluded.

We are therefore recommending against launching the corpus repair now. Two things argue for
reassessing the compression design first: seven of twelve NO_REPAIR controls turned out defective,
and six families returned representatives that disagree — which is precisely the assumption that
one-representative-per-family compression depends on. Applying 64 conditionally validated templates
across the corpus on this evidence would be faster than it would be defensible.

## 12. Implication for the next stage

R/I/T and mechanism coding both read *from* the structural fields. If Counterpart and Recipient are
populated by copying one span into both, every downstream inference about who intermediates between
whom inherits that artefact — and it would be invisible at the theoretical layer, because the data
would look internally consistent. The same applies to coordinated-predicate collapse: an obligation
absorbed into another record's object cannot later be coded as a mechanism, because as far as the
dataset is concerned it does not exist.

Doing structural validation first therefore buys three things. It establishes that the green unit of
analysis genuinely applies to digital law. It identifies which variables carry information and which
pay twice for the same signal. And it fixes the relational fields before they are used to make
claims about intermediation — which is the substantive question the project exists to answer.

---

### Supporting artefacts

- `R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv` — compact aggregate table
- `R4_VARIABLE_REDUNDANCY_AUDIT.csv` — the five variable pairs, with exactness and direction
- `R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv` — all 143 Action judgments re-examined
- `R4_2E_B1_METHOD_REPORT.md` — full validation method and results
- `R4_2E_B1_FINAL_SUMMARY.csv` — all 143 reconciled cases
- `R4_2E_B1_CONTROL_DIAGNOSTIC_CONSOLIDATED.csv` — all 12 diagnostic controls
- `R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv` — issues recorded for adjudication
