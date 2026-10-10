# Methodology v2 — addendum

Adds to, does not replace, `METODOLOGIA.md` (sections 1–11 stand). This
addendum covers what changed in the R-I-T relational restructuring: the
population-definition section promised in METODOLOGIA.md section 10, and
the discipline decision behind this round's scope.

## Population and sampling frame (formalising METODOLOGIA.md §10.1)
Before any move to SPARQL/Cellar at scale, the population must be defined in
writing, in this order:

1. **Population definition** — what counts as "EU legislation on the green
   transition"? (Not yet answered here — this is the open question, not a
   default.)
2. **Inclusion/exclusion criteria** — binding vs. soft law; basic acts vs.
   delegated/implementing acts; consolidated vs. original versions; time
   window.
3. **Sampling frame** — the concrete list of CELEX identifiers the criteria
   produce.
4. **SPARQL query** — built only after 1–3 are fixed in writing.
5. Screening (Stage A) → coding (Stage B).

SPARQL solves *retrieval*, not *population definition* — querying before
step 1 produces a technically sophisticated search over a conceptually
undefined universe. This section exists to be filled in during the next
round, not to be skipped.

## Why this round did not add new acts
The four acts already collected (CSRD, Ecolabel, Climate Benchmarks, ETS
Verification) are sufficient to test whether the R-I-T architecture works —
adding more acts before the architecture itself was corrected would have
scaled the earlier mistake (paragraph×mechanism as the substantive unit)
rather than fixed it. Nine well-justified relationships, decomposed from
chains already present in the four acts already read closely, is preferred
over a larger, shallower set: what is being tested at this stage is whether
theory has been correctly turned into data, not corpus coverage.

## The relational-architecture principle (see RIT_CODEBOOK.md for the full coding manual)
Actor roles are relational, not intrinsic. The dataset must allow the same
actor to be `I_actor` in one relationship and `T_actor` (or `R_actor`) in
another — demonstrated concretely in `data/rit_coded_sample_v2.csv`
(ETS-R1/ETS-R2: the verifier is intermediary between the competent authority
and the operator, and simultaneously the target of its own accreditation
relationship).

## Terminology changes in this round
- `status`/`verificar_humano` → `screening_confidence` (`high`/`low`) —
  already done in METODOLOGIA.md §11.
- "gold standard" → "pilot reference sample" (`VALIDATION_PROTOCOL.md`).
- `CODEBOOK.md` reframed (not replaced) as the Stage A pattern reference,
  pointed to by `SCREENING_CODEBOOK.md`.
- New Stage B artefacts: `RIT_CODEBOOK.md` (coding manual),
  `data/rit_coded_sample_v2.csv` (9 coded relationships, superseding the
  4-row `rit_coded_sample.csv` from the previous round — that file is kept
  for the record, not deleted).
