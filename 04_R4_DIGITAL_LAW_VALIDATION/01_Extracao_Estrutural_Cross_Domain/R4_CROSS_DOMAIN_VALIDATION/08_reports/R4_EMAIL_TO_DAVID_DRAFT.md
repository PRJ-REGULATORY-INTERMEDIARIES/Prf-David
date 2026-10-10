# Draft email to Professor David Levi-Faur

**Subject:** R4 digital structural validation — portability and parsimony results

---

Dear David,

We have completed the structural validation round on the digital corpus. It speaks directly to your
first two questions, and it produced some findings about the coding architecture itself that I think
are more useful than the headline counts.

We ran the exercise on the three instruments Rotem suggested — GDPR, the Digital Services Act and
the AI Act — producing 1,404 structural records on the unit *legal provision × actor × legal
action* (485 GDPR, 424 DSA, 495 AI Act). We then put 143 cases through advanced legal review.

**The architecture is portable at the structural level, with adaptation.** The green unit of
analysis applies to digital law without redefinition, and the three instruments decomposed into it
fairly evenly. Actor travels well. The relational variables travel conceptually but their extraction
rules do not: digital regulation is dense with prepositional phrases that look relational and are
not, and that is where most of the corrections fall.

**On variable burden, the answer is not uniform.** Two object fields are textually identical in
every record in the corpus and are never populated independently — one variable coded twice. A
quality-flag pair turned out to be redundant in one direction only, so one of them can be dropped
and the other cannot. But the Action variable runs the other way: it is a structured construct
across three columns, and assessing it from any one of them is a mistake.

**The counterpart/recipient result is the most informative.** In the original extraction the two
fields are textually identical across all 1,404 records, which on its face suggests one is
redundant. Advanced review says otherwise: it found 27 recipient-only and 14 counterpart-only
propositions, and not a single case where the same entity genuinely occupies both positions. The
initial extraction operationally collapsed two relational positions that are distinct in at least
some legal propositions. The implication is not to drop a variable — it is that the two fields
currently cost two columns and deliver one.

**The exercise also showed where AI-assisted structural extraction needs more careful
representation.** Our own review interface exposed only the normalised action label and not the
adjacent column holding the source predicate with its modality. Reviewers consequently recorded
modality as missing when it was present. We re-audited all 143 Action judgments against the full
representation: the Action correction count moves from 87 to 63, but only one of 143 overall defect
decisions is affected, because in nearly every case the record was defective on other grounds
anyway. Both figures are in the memo; neither replaces the other. Two related defects survive the
audit and are real: entitlement constructions genuinely lose their "shall", and coordinated
obligations genuinely get buried inside the object of the first.

Two caveats I want to be explicit about. The proportions above describe a review set purposively
selected to concentrate suspected defects; they are not corpus error rates and we have not computed
any. And the twelve NO_REPAIR controls were diagnostic probes rather than a blinded test — the
implementation did not guarantee blinding — so they tell us about compression coverage, not about a
false-negative rate. Seven of the twelve contained defects, which is why we are recommending that
the compression design be reassessed before any corpus-wide repair rather than applying the
templates now.

To be clear about what this is not: this is the structural validation round, not the substantive
green × digital comparison. Regulator/intermediary/target coding and mechanism coding have not
started, and we have deliberately not consulted Rotem's coding so that the later comparison stays a
genuine independent test. The governance-difference question needs that theoretical layer, and we
did not want to answer it from structural extraction alone.

The memo sets out the method and the limitations in full, with a compact summary table alongside it.

Best regards,

---

## Attachments

- `R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md`
- `R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv`
