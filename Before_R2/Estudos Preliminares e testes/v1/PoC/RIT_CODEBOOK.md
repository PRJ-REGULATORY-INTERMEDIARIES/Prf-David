# R-I-T Codebook (Stage B — substantive coding manual)

This is the coding manual for Stage B. It is distinct from
`SCREENING_CODEBOOK.md` (Stage A, lexical detection of candidates). Stage A
answers "does this provision contain a signal?"; this document answers "does
a regulatory intermediation relationship actually exist here, and what is
its structure?"

## Core principle
**Do not code labels; code regulatory relationships.** Sequence:
legal provision → regulatory relationship → R-I-T roles → mechanism →
institutional attributes → observable governance indicators. Never invert
this to fit the text into a category decided in advance.

## The R-I-T model
- **R = Rule-maker/Regulator** — establishes the standard, holds legal
  authority, supervises, or sanctions.
- **I = Regulatory Intermediary** — the rule-broker performing an
  analytically distinct mediating function.
- **T = Rule-taker/Target** — legally subject to the obligation, must
  demonstrate compliance, bears consequences of non-compliance.

**Actor roles are relational, not intrinsic.** The same actor can be I in
one relationship and T (or R) in another. Example already found in the ETS
sample: the *verifier* is I between the competent authority and the
operator, and simultaneously T in its own accreditation relationship with
the national accreditation body.

## Unit of analysis
The substantive unit is the **regulatory intermediation relationship**
(one row = one `relationship_id`), not the paragraph. One provision can
produce zero, one, or several relationships; a chain produces more than one
linked relationship (`chain_id`).

## The relational test (apply to every I candidate)
Before setting `intermediary_validated = 1`, answer explicitly, in writing:
> Does this actor perform an analytically distinct regulatory function that
> mediates the relationship between R and T?

- If **yes**, with textual support: `intermediary_validated = 1`.
- If **no** (the actor only advises the regulator, or only receives a
  direct obligation with no mediating function): `intermediary_validated =
  0`, with a written justification. A negative case is not a failure of the
  exercise — it is evidence the test is doing its job. Two negative cases
  are deliberately included in this pilot (see `data/rit_coded_sample_v2.csv`,
  rows CSRD-R3 and ECO-R3).

## Reporting is not automatically intermediation
A reporting duty running directly from an undertaking to a competent
authority is a **dyadic R–T relationship**, not R-I-T, unless a third actor
performs a distinct mediating function on that report (e.g., an auditor).
Code `reporting_present = 1` and `intermediary_validated = 0` in that case
(see CSRD-R3).

## Chains and meta-regulation
When an intermediary is itself subject to accreditation, certification, or
supervision by another intermediary, this is not noise — the proposal's own
concept of enhanced self-regulation/meta-regulation predicts exactly this
structure. Code it as two linked relationships sharing a `chain_id`:
- `intermediation_level = L1` — the intermediary mediates the primary
  regulator-target relationship.
- `intermediation_level = L2` — a second intermediary governs, certifies, or
  accredits the L1 intermediary.

Mark this as an **operational proposal for this dataset**, not a
classification already fixed in Levi-Faur's proposal.

## Ranking/rating: apply construct-validity scrutiny before coding
- **Ranking** = subjects are ordered against each other.
- **Rating** = subjects are evaluated against a predetermined standard.

Before coding a case as ranking/rating, identify explicitly: who is
evaluated; who performs the evaluation; against what criterion; whether the
result produces ordering/classification/regulatory judgment; and whether an
intermediation function (mediating R and T) is actually demonstrable. If any
of these cannot be shown from the text, code `construct_validity =
conditional`, not `confirmed` — never force a case into the mechanism
because it is lexically convenient (see CB-R1).

## Uncertainty and missingness codes
Never use blank or 0 for unknown information.
- `1` = present / observed
- `0` = absent (explicitly established as absent, not merely unmentioned)
- `NA` = not applicable to this relationship
- `UNK` = unknown, insufficient information in the provision read so far
- `NOE` = not observable from the legal text alone
- `EXT` = would require external evidence beyond the legal text

## Observability classes
Tag inference confidence honestly:
- **A — directly observable** from the legal text (e.g., formal legal role,
  mandatory/voluntary, accreditation requirement).
- **B — institutionally inferred** (e.g., R/I/T role assignment,
  public/private/hybrid character, regulatory level).
- **C — requires external evidence**, cannot safely be inferred from the
  provision alone (e.g., actual capture, real institutional centrality,
  actual effectiveness). Do not code class-C variables from the legal text
  in this pilot; leave `EXT`.

## Failures are risks addressed by design, not observed events
A conflict-of-interest rule does not mean `capture = 1`; it means the
institutional design addresses the *risk* of capture. Code
`failure_risk_addressed` (capture / incompetence / under-commitment /
over-commitment / unclear) with the note: *this variable captures the type
of failure apparently addressed by the institutional design, not empirical
evidence that the failure occurred.*

## What this pilot round does and does not cover
Coded now (`data/rit_coded_sample_v2.csv`): relationship identity (R/I/T),
chain structure, primary/secondary mechanism, formal legal role,
mandatory/voluntary character, regulatory level, sphere, governance mode,
organizational separation, construct validity, verbatim evidence — Block
A–C and a slice of Block D in `DATA_DICTIONARY.md`.

Not yet coded (defined in `DATA_DICTIONARY.md` for the next round, not
fabricated here): the full autonomy indicator battery (§25-style:
independence, appointment, removal protection, financial independence),
the full accountability indicator battery (supervision, sanctions,
transparency, appeal), and polycentric/monocentric structural indicators.
Populating these for only 9 relationships without a second coder to check
them risks manufacturing precision the pilot cannot support; they are
scoped as the next coding round, not skipped silently.
