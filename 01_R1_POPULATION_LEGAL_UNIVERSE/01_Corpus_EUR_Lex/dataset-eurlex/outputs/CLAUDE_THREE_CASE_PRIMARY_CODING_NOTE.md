# Three-case primary coding — handoff note

**To:** GPT-5.6 Luna (secondary reviewer), researcher
**From:** Claude, primary coder, production v1.0
**Scope:** case_01 (Regulation (EU) 2021/1119, Climate Law), case_02 (Regulation (EU) 2023/956,
CBAM), case_03 (Regulation (EU) 2023/1115, EUDR)
**Status:** proposals only — not ground truth, not adjudicated

Each case was coded by a separate, memoryless run of the same primary-coder prompt and
codebook, reading only that case's own frozen corpus. Case 01 was treated as fully fresh:
the earlier intensive pilot on this same act was neither consulted nor used to calibrate
this proposal, and this run reaches its own conclusions on Article 8(4) independently of
that pilot's prior adjudication of the same provision — Luna and the researcher should treat
that as a substantive disagreement to examine, not a bug.

## 1. Volume per case

| Case | Total | intermediated | direct | uncertain | not_supported | uncertainty log |
|---|---|---|---|---|---|---|
| case_01 — Climate Law | 7 | 1 | 4 | 2 | 0 | 10 |
| case_02 — CBAM | 22 | 5 | 16 | 1 | 0 | 11 |
| case_03 — EUDR | 10 | 3 | 5 | 2 | 0 | 9 |

No case was coded to hit a target count. CBAM's larger main matrix reflects its longer,
more procedurally dense text (36 articles, 6 annexes), not a different substantive standard —
all three runs used the identical prompt and self-check.

## 2. Intermediated relations proposed

**case_01** (1): Commission (R) — EEA (I) — Member States (T), Article 8(4)/Recital 37. The
EEA has an express duty to assist the Commission's Article 6–7 assessments of Member States.
Coded `mechanism: monitoring_supervision`, confidence medium, flagged
`conceptual_boundary` because "assist the regulator" versus "mediate toward the target" is
exactly the boundary this construct exists to test.

**case_02** (5), all involving a genuinely third-party actor with a documented function:
two verification relations (accredited verifier verifying an authorised CBAM declarant's, and
a third-country installation operator's, embedded-emissions data — Art. 8, 10, Annex VI, both
high confidence); one certification relation (an independent person certifying a declarant's
carbon-price documentation, Art. 9(2), medium confidence); two information-transmission
relations in which customs authorities pass import/declarant data into the Commission's and
competent authorities' supervision of declarants and importers (Art. 14, 19, 25, 33, medium
confidence). The verification pair is the most structurally clean intermediation in the
three-case set: an accreditation-backed third party, a specific verified object (an embedded-
emissions report), and an institutionally integrated output.

**case_03** (3), all more contestable and flagged accordingly: customs authorities executing
release/suspension decisions delegated from competent authorities' compliance findings
(Art. 26–28, high confidence, `mechanism: delegated_implementation`); the Commission's
Article 33 information system automatically flagging high-risk non-compliance to competent
authorities (medium confidence, flagged `possible_overcoding` — the system may be better read
as an instrument the competent authorities use directly rather than a mediating actor);
submitters of "substantiated concerns" under Article 31 acting as a formally institutionalized
reporting channel that triggers competent-authority investigation (medium confidence, also
flagged `possible_overcoding` — this is the closest the corpus comes to treating ordinary
third parties as a regulatory function, and deserves the most scrutiny of the ten).

## 3. Mechanisms observed

Across the three cases: `monitoring_supervision`, `reporting`, `information_transmission`,
`coordination` (case_01); `verification`, `certification`, `accreditation`, `standard_setting`,
`enforcement_support`, `monitoring_supervision`, `reporting`, `information_transmission`,
`coordination`, `other_mechanism` (case_02 — the widest spread, consistent with its more
elaborate compliance architecture); `monitoring_supervision`, `enforcement_support`,
`delegated_implementation`, `information_transmission`, `ranking_rating`, `reporting`
(case_03 — `ranking_rating` reflects the country-benchmarking provisions). `none_or_direct`
was used for direct relations throughout and is not tabulated above as a "mechanism finding."

## 4. Recurring actor types

The European Commission is the dominant R across all three cases, often alongside or
interchangeable with a named "competent authority" (case_02, case_03) — the primary coder
did not treat "competent authority" and "European Commission" as automatically the same
actor even where a provision names both; where a provision genuinely names both R is coded
as an array. Recurring T types are Member States (case_01), authorised declarants/importers
(case_02), and operators/traders (case_03) — no case coded an object (a report, a
certificate, embedded-emissions data, a due-diligence statement) as T. Recurring candidate I
types are scientific/technical bodies with an evidentiary role (case_01: EEA, Advisory Board,
JRC), accreditation-backed verifiers and independent certifiers (case_02), and customs
authorities plus information systems or third-party reporters (case_03).

## 5. Conceptual boundaries that recurred across cases

- **Assisting the regulator vs. mediating toward the target.** The case_01 EEA relation and,
  more sharply, the case_02 customs-authority relations turn on whether transmitting
  information that feeds the regulator's own supervision is itself mediation, or merely
  support internal to R's side of the relation. This is the single most consequential
  boundary in the whole three-case set and is flagged in all three proposals.
- **Automated systems and formally-invited third parties as I.** case_03's Article 33
  information system and Article 31 "substantiated concerns" mechanism both raise whether a
  process or a class of unspecified third parties can occupy I, as opposed to a named
  institutional actor. Flagged `possible_overcoding` in both instances precisely because this
  is a live extension of the construct rather than a settled application of it.
  Luna should treat these two as the primary test of whether the codebook's I definition
  needs a boundary condition for this pattern, not merely as two more cases to accept or
  reject individually.
- **Third-party certification the text treats as voluntary operator input, not a regulatory
  function.** case_03 explicitly declined to code voluntary certification-scheme reliance as
  intermediation (logged in its uncertainty file), consistent with case_02's own certification
  relation being coded only where the text itself assigns the certifying act a function inside
  the compliance mechanism (Art. 9(2)), not merely as an option an operator may use.
- **External-context dependence.** case_01 flagged one relation as depending on content not
  reproduced in this corpus; case_02 flagged two. case_03 flagged none in the main matrix but
  logged external-context limitations in its uncertainty file for provisions referencing the
  benchmarking delegated act.

## 6. Cases deserving priority review

In descending order of how much a reviewer's judgment could change the classification:

1. **case_03-rel-006** (substantiated concerns as reporting intermediary) and
   **case_03-rel-004** (Commission information system as intermediary) — both
   `possible_overcoding`, both novel applications of I to a non-institutional or automated
   actor.
2. **case_02-rel-004 / rel-005** (customs authorities as I between declarants/importers and
   the Commission/competent authorities) — turns on the same assist-vs-mediate boundary as
   case_01's EEA relation, so a consistent ruling across case_01 and case_02 on this boundary
   would materially help comparability.
3. **case_01-rel-003** (EEA/Commission/Member States, Article 8(4)) — flagged above as a
   point of open, undisguised disagreement with the earlier pilot's own adjudication of the
   identical provision; worth Luna's and the researcher's direct attention for that reason
   alone.
4. **case_02-rel-003** (independent person certifying carbon-price documentation) — the
   certifier's institutional status is thin in the text (identified only as "independent"),
   which is why confidence is medium rather than high despite the relation type being clear.

## 7. What this note does not claim

This note reports counts and boundaries observed while proposing, not a validated result.
No relation here has been reviewed by Luna, adjudicated by the researcher, or compared
against the earlier pilot, Terra, or any other model. The absence of intermediated relations
in a passage is not evidence of a coding failure, and their presence is not evidence of
correctness — both await independent secondary review and researcher adjudication.
