---
title: "Coding Regulatory Intermediaries in EU Green-Transition Legislation (v2)"
author: "Igor Caires Machado — Postdoctoral Researcher, ENAP · ORCID 0009-0008-9547-5223"
date: "5 September 2026"
lang: en
---

## Purpose

This is a revised version of the response to the call for a research
assistant/partner to help code intermediaries in EU legislation on the green
transition ("Governance by and of Intermediaries"). The previous version
built a reproducible mechanism-*screening* pipeline; this version corrects
its central limitation by making the substantive unit of analysis the
**R-I-T relationship** (Regulator–Intermediary–Target) rather than the
paragraph. Full technical detail is kept in annexes so this note stays
short and focused.

## Theoretical construct

The proposal treats regulatory intermediation as an architecture of
**actors + mechanisms + strategies** mediating between rule-makers and
rule-takers, structured around four primary mechanisms — reporting
(state-led), certification (NGO-led), ranking/rating (business-led), and
auditing (profession-led) — and a set of intermediary attributes (formal
role, voluntarism, level, sphere, motivation, mode of operation, centrality,
degree of separation). This note treats these as **theoretical constructs
from the proposal**, distinct from the **operationalisations proposed for
this dataset** (defined in the annexes) and from **future analytical
possibilities** not yet operationalised (e.g. an autonomy or accountability
index).

## From legal text to R-I-T observations

The pipeline now follows: legal text → regulatory architecture → R-I-T
relationship → theoretical construct → observable variables → structured
data. A key design principle: **actor roles are relational, not intrinsic**.
The same actor can be the intermediary in one relationship and the target of
a different relationship — found concretely in the EU ETS sample, where the
verifier is intermediary between the competent authority and the operator,
and simultaneously the target of its own accreditation relationship with the
national accreditation body.

## Stage A — screening (candidate detection)

Unchanged in substance from the previous round: four EU acts (CSRD,
Ecolabel, Climate Benchmarks, ETS Verification), collected by CELEX,
screened paragraph-by-paragraph with anchor/weak/exclusion lexical rules per
mechanism. Its role is now explicit: **Stage A only detects candidates**; a
lexical hit is a `screening_confidence` of `high` or `low`, never a
confirmation that an intermediary exists. Detail: `SCREENING_CODEBOOK.md`,
`CODEBOOK.md`.

## Stage B — substantive coding

For each candidate provision, I applied a **relational test** — does this
actor perform an analytically distinct function mediating between a
regulator and a target? — and coded the result as a structured relationship,
never a label. From the same four acts, without adding new source material,
this produced **nine R-I-T relationships**:

- **Two chains showing meta-regulation** (an intermediary itself governed by
  another intermediary): CSRD (group auditor supervising a subsidiary-level
  assurance provider) and Ecolabel (a competent body relying on a
  separately accredited testing/verification body) — in addition to the
  ETS case already found in the previous round.
- **One case of role multiplicity**: the ETS verifier, intermediary in one
  relationship and target in the linked accreditation relationship.
- **Two deliberate negative cases**: a CSRD provision that is a direct
  reporting duty with no mediating actor (dyadic R–T, not R-I-T), and an EU
  Ecolabel advisory board that fails the relational test (it advises the
  regulator; it does not mediate an existing R–T relationship). Negative
  cases are evidence the test discriminates, not gaps in coverage.
- **One conditional case** (Climate Benchmarks) — see below.

Nine relationships, not thousands of hits, is a deliberate choice: the
priority at this stage is demonstrating that the theory has been correctly
turned into data, not corpus coverage. Full table: `RIT_CODEBOOK.md`,
`data/rit_coded_sample_v2.csv`, `DATA_DICTIONARY.md`.

## Construct-validity question — Climate Benchmarks

> Does the benchmark administrator perform regulatory intermediation in the
> theoretical sense used here, or is it primarily an index provider directly
> regulated by the benchmark regime? The administrator selects, weights and
> excludes assets against a predefined decarbonisation standard —
> rating-like — but the regulator is not named in the specific provision
> read, and the target is dual and indirect (the scored companies, and
> separately the asset managers who use the label). I keep the case, coded
> `construct_validity = conditional`, and would value discussing directly
> with David whether it should anchor the ranking/rating mechanism, or
> whether a more direct case (e.g. credit rating agencies) should replace
> it.

## Validation

Stage A screening was checked against a manually read **pilot reference
sample** (not a "gold standard" — the term overstated what a small,
non-random sample can support): precision 100%, recall 94.3%, F1 97.1% over
35 judged paragraphs. Stage B's nine relationships have **not** yet been
checked by a second coder — inter-coder reliability, not precision/recall,
is the right instrument for relationship-level coding, and is the next
validation step, not something claimed as done. Detail:
`VALIDATION_PROTOCOL.md`.

## Limitations

- Nine relationships from four acts demonstrate the architecture; they are
  not a corpus-scale dataset.
- Several theoretically important attributes (autonomy and accountability
  indicator batteries, motivation, centrality) are defined
  (`DATA_DICTIONARY.md`) but not yet coded — populating them without a
  second coder to check the harder judgment calls would manufacture false
  precision.
- The population of "EU green-transition legislation" has not been defined;
  this must happen before any move to query EUR-Lex/Cellar at scale
  (`METHODOLOGY_v2.md`).

## Next steps

1. Define the population and sampling frame in writing before any SPARQL
   query — SPARQL solves retrieval, not population definition.
2. Independent second-coder pass on the same four articles; measure
   inter-coder agreement; adjudicate and revise `RIT_CODEBOOK.md`.
3. Resolve the Climate Benchmarks construct-validity question directly with
   David.
4. Populate the autonomy and accountability indicator batteries once a
   second coder is in place.

## Conclusion

The pilot demonstrates a reproducible workflow in which lexical screening is
used only to locate candidate provisions. Substantive coding then
reconstructs R-I-T relationships, identifies the regulatory mechanism,
records institutional attributes and preserves verbatim legal evidence. The
resulting architecture is designed to support future measurement of
intermediary autonomy, accountability and governance structure without
prematurely converting theoretical constructs into unvalidated indices.

---

**Annexes** (separate files): `RIT_CODEBOOK.md`,
`data/rit_coded_sample_v2.csv`, `DATA_DICTIONARY.md`, `VARIABLE_MAP.md`,
`VALIDATION_PROTOCOL.md`, `METHODOLOGY_v2.md`, `SCREENING_CODEBOOK.md`,
`CODEBOOK.md`, `CHANGELOG.md`.
