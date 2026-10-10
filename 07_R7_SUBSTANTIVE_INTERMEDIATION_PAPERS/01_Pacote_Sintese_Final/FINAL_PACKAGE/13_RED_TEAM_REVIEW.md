# 13 — Red team review

**Role adopted.** A skeptical senior reviewer with no stake in the project, asked whether the note's argument survives.

**Verdict.** The argument survives, but the **headline claim is overstated as written** and three absence claims are phrased as claims about the law when they are claims about the reconstruction. Ten corrections are required. All are applied in `14_FINAL_NOTE_FOR_DAVID.md`; the three that also affect the standalone executive summary and one-page brief are applied there too.

---

## Attack 1 — "Extraction worked. The hard part is the transitions."

**This is the note's headline and it does not hold as stated.** The evidence offered is that one material difference arose at the evidence level C0. But the frozen registers also record **30 material differences at C1, the relational level** — the second-largest count of any level. C1 units are propositions about *parties, direction, action, modality, conditions and effect*. Getting those right is reading, not inferring.

And the note's own best-evidenced example proves the point against itself. HQ-CBAM-04 is a **C1** card. Article 20(1) says in terms that "A Member State shall sell CBAM certificates…" and the direct reconstruction recorded the certificate arrangement with the seller *unidentified*. That is not an inferential overreach at a level transition. That is a failure to record what the provision states. The note presents it as a bonus finding "different in kind"; a hostile reader will present it as a refutation of the headline.

The honest structure of the result is **two** vulnerabilities, not one:

1. **relational precision** — parties, direction and modality, at C1 (30 material differences, one validated instance);
2. **upward inference** — coupling, boundary, whole-level property, stopping, at C2–C4 (65 material differences, four validated instances).

This is also a better argument, because the two surviving control families in `05_METHOD_CONTROLS_REVIEW.md` map onto exactly those two vulnerabilities. The note was underselling its own structure.

**Correction R1 (required).** Replace the headline claim. Statement-level agreement is near-total (1 of 96 at C0); relational extraction is not safe (30 of 96 at C1); upward inference is where the bulk sits (65 of 96 at C2–C4). HQ-CBAM-04 must be presented as evidence for vulnerability (1), not as a separate curiosity.

---

## Attack 2 — "Two independent reconstructions"

The executive summary says "two independent reconstructions." They were **isolated** — separate execution contexts, access and contamination logs, a blindness and access policy — but they were not independent. Both ran on `claude-sonnet-5-5`, under instructions derived from the same manuscript, in the same project, authored by the same researcher. Correlated errors are not merely possible; they are expected. Any agreement figure between them therefore overstates reliability, and the 113 substantively equivalent units cannot be read as convergent validation.

**Correction R2 (required).** "Independent" → "separately conducted and isolated". Add, once, that agreement between two runs of the same model is not evidence of correctness.

---

## Attack 3 — The counts are attached to the wrong objects

The note's central table and Figure 1 label the counts as belonging to *transitions* (text → statements, statements → relationships, and so on). The frozen registers record them by **comparative level of the principal proposition** (C0–C4). Mapping a level onto the transition that produces it is an interpretive step the note does not disclose. It is a reasonable mapping, but a reviewer is entitled to see it flagged.

**Correction R3 (required).** State the mapping explicitly in the note and in Figure 1.

---

## Attack 4 — Absence claims dressed as findings about the law

Three claims assert that something is not in an instrument, on the basis that it is not in the reconstruction. The pilot's own decision rule (DR-22) says that "not found" is a statement about the search, and that absence-dependent properties require a declared coverage statement. The note breaks its own rule three times:

- "the only relation governing the verifier *inside* the Regulation is Article 18(2)";
- "no supervision, suspension or withdrawal relation over the verifier is recorded inside the instrument";
- "the Social Climate Fund has no third-party intermediary at all."

Each may well be right. None is licensed as phrased, and the CBAM claim is load-bearing for the note's most interesting substantive suggestion.

**Correction R4 (required).** Rephrase all three as claims about the frozen reconstruction within the declared corpus, and say so once explicitly.

---

## Attack 5 — Does this accidentally present Igor as creating a new theory?

**No, and the framing is robust.** Every control is attributed to a numbered section of the manuscript; the prospective crosswalk records thirteen of twenty-two elements as equivalent in conceptual function to requirements already in the paper; the note states its own additions as three narrow ones and reports **two subtractions** from David's framework (the object category, and strategies and logics). The three figures contain no proprietary apparatus. No label for a model appears anywhere.

One residual risk: §8's list of eight safeguards reads like a specification and could be mistaken for a proposed instrument. **Correction R5 (minor).** Frame it as what to fold into the existing protocol, not as a thing.

---

## Attack 6 — Does it exaggerate the six decisions?

**No.** Every mention carries the purposive, non-representative, six-of-fifty-six, four-at-one-level qualifications. No rate, percentage, accuracy or win appears. The note states in §1 and §4 that the other fifty cards were not human-adjudicated and are not treated as adjudicated evidence. Since the 2026-10-08 provenance import it also states that the six decisions are archived but carry no recorded justification, so each is auditable as a decision and not as reasoning.

But one thing is missing: the note never says that the person who made the six blinded decisions is the same person who designed both arms, built the comparison and is now writing the note. Blinding to arm identity does not remove that. A reviewer will see it immediately.

**Correction R6 (required).** Disclose the single-adjudicator conflict in one sentence, and note that independent adjudication is what would make the six decisions count.

---

## Attack 7 — Does it confuse more detail with better analysis?

**No — it argues the opposite, and with evidence.** The counterexample is in §1, has its own section, and recurs in §12. §7 adds the sharper point that the nineteen-subconfiguration layer *deferred* the membership judgment and then resolved it in the rejected direction (verifiable in `ARCHITECTURE_CANDIDATES` ARCH-02). Three dimensions that cut against the controls are reported: traceability equivalent in every unit, calibration unassessable in 93 of 96, and volume unmatched by contribution.

One asymmetry remains. The note uses the record ratio (~2,400 records against 96 material differences) as evidence of excess, while the frozen rule says volume is never evidence of quality. The rule cuts both ways: volume is not evidence of waste either.

**Correction R7 (required).** State the symmetry explicitly. The ratio is a documented cost not matched by a demonstrated contribution — not a measured inefficiency.

---

## Attack 8 — Does it suppress the AI-12 counterexample?

**No.** It appears in the executive summary ("and I want to put it early rather than late"), has its own section, and is restated in the conclusion. If anything the note gives it more analytical weight than the four decisions that went the other way, which is the right imbalance given that four of six went one way.

---

## Attack 9 — Candidate versus established architecture

**Handled.** The note consistently says "declined", "indeterminate", "candidate", "the controlled arm's recorded assessment". The AI Act whole-instrument result is reported as the arm's assessment rather than as a fact about the Regulation. No candidate is upgraded.

---

## Attack 10 — Does it infer implementation effects from legal text?

**No.** §10 is strict; §9 repeatedly marks the formal/operational boundary; Figure 3 carries an explicit limit line; the capture discussion states that the text cannot distinguish competition from competitive laxity.

One gap: §6 and §9 cite external instruments (Reg. 765/2008, Implementing Reg. 2018/2067, the CEPT material) in a way that could suggest their contents are known. They were never retrieved.

**Correction R8 (required).** Say once, in §9, that the external instruments were not retrieved and that the claim is about what the instrument refers out to.

---

## Attack 11 — Does it overstate what four cases demonstrate?

Mostly no. §9's Q4 discussion is appropriately negative; the "structural variable" suggestion is marked as measurable rather than established; the complementarity reading is marked "suggestive and nothing more."

One overreach survives. §5 says the container problem is "the default behaviour of an AI-assisted run." Four cases, one model, one task framing. It is a well-replicated observation *within this pilot* and a hypothesis outside it.

**Correction R9 (required).** Scope it to the pilot.

---

## Attack 12 — Is any complexity retained only because it was expensive to build?

Tested against each `RETAIN`:

- *Provenance* — justified independently: it caught two failed source hashes.
- *Actor precision* — justified by HQ-CBAM-04, and it is a shared rule, not an addition.
- *External dependency* — justified three ways, including a substantive finding. The strongest case in the set.
- *Reference date* — nearly free; prevents an invisible error.
- *Stopping level* — one field; one clean demonstrated instance.
- *Candidate status* — one status value; it is the structural fix for the dominant failure.

And *uncertainty recording* is classified `RETAIN IN SIMPLIFIED FORM` while the review admits calibration was never assessable. That is retention without validation. It is defensible — both arms kept uncertainty registers, so this is a shared requirement rather than added complexity — but the note should not imply it was vindicated.

**Correction R10 (required).** State that the uncertainty field is retained as a shared requirement, not as a validated control.

The heavy machinery is removed, including artefacts that took the most effort to build. No sunk-cost retention found.

---

## Attack 13 — Residual weaknesses the note discloses but cannot fix

Noted for completeness; no correction possible within this package.

1. **Fifty of the 56 were never human-adjudicated.** The note says so three times. It remains the binding limit.
2. **Attribution.** Controls versus prompt structure are not separated. Disclosed, with the fix proposed for Phase 2.
3. **No recorded reasons.** Resolved in part on 2026-10-08: the six decisions are archived, so the claim resting on them can be inspected against the frozen cards and key. But no justification or confidence was captured and none was reconstructed, so the reasoning is permanently unavailable. Disclosed in §4.
4. **Comparator interpretive latitude.** Round-1 QA check 29 records that the materiality operationalization, the clustering of absence claims and the blinding were the comparator's choices, logged rather than pre-specified. Worth a clause in §4. **Correction R11 (minor).**
5. **Case selection.** Four instruments chosen for a methodological test — two climate, one unique-eligible AI case, one repealed 1992 Directive. Not a sample. Stated in §9.

---

## Corrections applied in `14_FINAL_NOTE_FOR_DAVID.md`

| # | Correction | Where |
|---|---|---|
| R1 | Headline restated as two vulnerabilities — relational precision and upward inference; HQ-CBAM-04 moved into the evidence for the first | §1, §3, §5, §6, §12 |
| R2 | "Independent" → "separately conducted and isolated"; agreement between two runs of one model is not evidence of correctness | §4, §5 |
| R3 | Level-to-transition mapping disclosed | §5, Figure 1 note |
| R4 | Three absence claims rephrased as claims about the reconstruction within the declared corpus | §9 |
| R5 | §8 framed as what to fold in, not as an instrument | §8 |
| R6 | Single-adjudicator conflict disclosed | §4 |
| R7 | Volume symmetry stated; ratio is a cost not matched by a demonstrated contribution | §7 |
| R8 | External instruments were not retrieved | §9 |
| R9 | "Default behaviour" scoped to the pilot | §5 |
| R10 | Uncertainty field retained as a shared requirement, not a validated control | §8 |
| R11 | Comparator interpretive latitude noted | §4 |

**Also applied to the standalone short versions** (both are sendable and must not contradict the note): R1 and R2 in `10_EXECUTIVE_SUMMARY_FOR_DAVID.md` and `11_ONE_PAGE_BRIEF.md`; R3 in both diagrams; R4 in the one-page brief's intermediation paragraph.
