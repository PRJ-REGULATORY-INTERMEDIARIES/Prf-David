# Lexical codebook v4

Stage A1 is a screening layer. A hit means that a provision deserves
inspection; it does not establish an intermediary or a positive R-I-T
relationship.

## Ontology rule

Every pattern is assigned exactly one `semantic_role`:

- `actor`: an organisational or professional role (for example, `benchmark
  administrator`, `competent body`, `statutory auditor`);
- `mechanism`: an activity or mode of mediation (for example, reporting,
  accreditation, ranking, auditing);
- `instrument`: a document, methodology or artefact (for example,
  `verification report`, `benchmark methodology`, `sustainability report`).

The pipeline never compresses these roles into one generic “intermediary”
label.

## Mechanism families

| Family | Anchor examples | Weak examples | Main exclusions |
|---|---|---|---|
| `reporting` | sustainability reporting; management report; non-financial report | shall report; shall disclose; report | reports about the application/review of the act |
| `certification` | competent/accredited body; conformity assessment body; accreditation body | certification; accreditation; accredited | none in this PoC |
| `ranking_rating` | benchmark administrator; benchmark methodology; rating agency | benchmark; rating; ranking; score | generic reports/review clauses |
| `auditing` | statutory auditor; audit firm; verification body; accredited verifier | audit; assurance | Court of Auditors |

Anchor matches receive `high` screening confidence; weak matches receive
`low`. Evidence is the normalized verbatim paragraph, capped at 500
characters. Stage A2 is a separate semantic layer and is not substituted by
this regex pass.

## Reproducibility

The implemented rules are in `scripts/screening_v4.py`. The output is
`data/screening_hits_v4.csv`; the five-act distribution is 559 CSRD, 94
Ecolabel, 61 Climate Benchmarks, 365 ETS Verification and 13 Taxonomy hits.
