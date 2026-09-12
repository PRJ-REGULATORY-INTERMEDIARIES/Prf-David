# Variable map v4

| Conceptual layer | Operational fields | Source of truth | v4 state |
|---|---|---|---|
| Legal source | base/version CELEX, ELI, URL, version, hash, retrieval date | `CELEX_MANIFEST_v4.csv` | complete for five acts |
| Stage A1 signal | screening id, article, mechanism, semantic role, confidence, evidence | `screening_hits_v4.csv` | complete: 1,092 hits |
| Stage A2 proposal | `ai_candidate`, actor, function, mechanism, evidence, context request, run ref | A2 schema/log | dry-run schema test only |
| Architecture | actors and explicit relations | B1 schema/log | dry-run schema test only |
| R-I-T adjudication | five conditions, R/I/T, verdict, mechanisms | B2 schema/log; human candidate CSV | seven inherited positives; 20 new units pending |
| Institutional attributes | eight fixed attributes plus deferred proposals | C schema/log; relationship CSV | seven inherited v3 rows; no AI promotion |
| Actor lookup | actor id, label, type, public/private/hybrid, jurisdiction | `actors_v4.csv` | 19 inherited actors |
| Human audit | deterministic sample, status, adjudication, note | `audit_sample_v4.csv` | 20 selected; review pending |

The map deliberately keeps actor, mechanism, instrument, procedure and
institution as separate ontological dimensions. A lexical mention is not
treated as proof of a role or relationship.
