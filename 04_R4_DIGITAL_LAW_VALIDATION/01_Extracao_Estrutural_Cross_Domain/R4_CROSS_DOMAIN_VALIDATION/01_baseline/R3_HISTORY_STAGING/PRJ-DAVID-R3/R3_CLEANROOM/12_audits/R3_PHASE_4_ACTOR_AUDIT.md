# R3 Phase 4 — Actor Register and Actor–Provision Mapping Audit

## A. Inputs used

**[EXPLICIT_TEXT — authorized inputs]** Phase 4 used only:

1. the validated R3 corpora for `32003L0087`, `32015D1814`, `32018R0842`, `32021R1119` and `32023R0955`, specifically their `act_numbered.md`, `act_full.md`, `recitals.md`, `operative.md`, `article_index.csv` and `CORPUS_MANIFEST.yaml` files;
2. `03_instrument_profiles/INSTRUMENT_PROFILE.csv`;
3. `03_instrument_profiles/INSTRUMENT_MEMO_32003L0087.md`;
4. `03_instrument_profiles/INSTRUMENT_MEMO_32015D1814.md`;
5. `03_instrument_profiles/INSTRUMENT_MEMO_32018R0842.md`;
6. `03_instrument_profiles/INSTRUMENT_MEMO_32021R1119.md`;
7. `03_instrument_profiles/INSTRUMENT_MEMO_32023R0955.md`.

**[EXPLICIT_TEXT]** Phase 1 source PDFs were not used as an analytical substitute for the validated corpus, and no prior-round material was used.

## B. Clean-room compliance

**[EXPLICIT_TEXT — clean-room declaration]** No prior actor map, coding, dataset, relation map, intermediary list, mechanism coding, adjudication file, spreadsheet, summary, memo or other empirical output was consulted, compared, reused or imported.

**[EXPLICIT_TEXT — stage separation]** The conceptual RIA learning register was not used to add Knowing, Assuring, Steering, architecture, mechanism or capacity fields to Phase 4. Phase 4 records institutional actors, legal actions and textual counterparties only.

## C. Actor counts

**[EXPLICIT_TEXT — ACTOR_REGISTER.csv]** The actor register contains 89 law-specific actor records. The counts below are descriptive inventory counts, not centrality or role measures.

| CELEX | Actor records | Specific entities | Actor classes | Public | Private | Hybrid | EU level | Member-State level | E1 | E2 | E3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 32003L0087 | 15 | 4 | 11 | 7 | 0 | 4 | 5 | 4 | 15 | 0 | 0 |
| 32015D1814 | 8 | 4 | 4 | 6 | 0 | 1 | 5 | 2 | 7 | 1 | 0 |
| 32018R0842 | 11 | 6 | 5 | 8 | 0 | 2 | 6 | 2 | 11 | 0 | 0 |
| 32021R1119 | 21 | 9 | 12 | 13 | 0 | 0 | 10 | 2 | 20 | 1 | 0 |
| 32023R0955 | 34 | 8 | 26 | 15 | 2 | 5 | 10 | 5 | 34 | 0 | 0 |

**[EXPLICIT_TEXT]** The remaining records in the public/private field are coded `COLLECTIVE` or `UNSPECIFIED` where the original act does not establish a public/private status. The controlled vocabulary was not expanded to force a classification.

**[EXPLICIT_TEXT]** The highest actor count occurs in `32023R0955` because the Fund Regulation expressly differentiates beneficiaries, implementing authorities, audit bodies, data subjects and consulted constituencies.

## D. Actor–provision mapping

**[EXPLICIT_TEXT — ACTOR_PROVISION_MAP.csv]** The map contains 173 `LAW × ACTOR × PROVISION × LEGAL ACTION` rows:

| CELEX | Actor rows | Actor records | Average mapped rows per actor | Highest mapped counts |
|---|---:|---:|---:|---|
| 32003L0087 | 44 | 15 | 2.93 | Member States 13; European Commission 7; Operators 5 |
| 32015D1814 | 13 | 8 | 1.62 | European Commission 4; Member States 3 |
| 32018R0842 | 24 | 11 | 2.18 | European Commission 7; Member States 6; Central Administrator 3 |
| 32021R1119 | 34 | 21 | 1.62 | European Commission 9; Member States 4; European Scientific Advisory Board on Climate Change 3 |
| 32023R0955 | 58 | 34 | 1.71 | European Commission 13; Member States 13 |

**[EXPLICIT_TEXT]** The highest-count values above are counts of mapped legal-action rows only. They are not measures of institutional centrality, influence, regulatory importance or intermediation.

**[EXPLICIT_TEXT]** Every actor record has at least one mapped provision. Every map row contains a legal action, a source anchor and one of `E1_EXPLICIT` or `E2_CROSS_PROVISION_RECONSTRUCTED`.

## E. Alias resolution

**[EXPLICIT_TEXT — ACTOR_ALIAS_LOG.csv]** The alias log contains 38 normalization records. Short forms such as `Commission`, `EEA`, `Advisory Board`, singular/plural variants and legally supplied directional descriptors were mapped to law-specific canonical names.

**[EXPLICIT_TEXT]** No cross-law actor records were collapsed: the same institution retains a separate `LAW × ACTOR` record in each instrument.

**[EXPLICIT_TEXT]** Eleven law-specific records are flagged with `identity_uncertain = YES`: persons, third-country parties and schemes, relevant stakeholders, persons holding allowances, EU ETS installations, international scientific bodies, public or private implementing entities, other stakeholders, final recipients, beneficial owners and recipients of support from the Fund.

**[EXPLICIT_TEXT]** The uncertainty flags reflect open-ended legal classes or dependence on an underlying instrument; they do not block the institutional inventory.

## F. Difficult classifications

### Actor versus regulatory object

**[CROSS_PROVISION_RECONSTRUCTED]** Emissions, allowances, plans, reports, data, targets, financial allocations, indicators and technologies were excluded as non-actors unless the text separately named an action-capable institution or class associated with them.

**[CROSS_PROVISION_RECONSTRUCTED]** `EU ETS installations`, `vulnerable households`, `vulnerable micro-enterprises` and `vulnerable transport users` were retained because the instruments legally situate them as installation, beneficiary or affected classes with status, entitlements or information/compliance consequences.

### Actor class versus specific entity

**[EXPLICIT_TEXT]** `Member States`, `competent authorities`, `operators`, `verification bodies`, `audit bodies`, `stakeholders` and beneficiary classes were kept as actor classes when the act did not identify an individual institution or legally required subclass.

**[EXPLICIT_TEXT]** `Member States listed in Annex II` in `32018R0842` was kept as a separate law-specific class because the Annex creates a differentiated notification and cancellation entitlement.

### Public/private/hybrid status

**[ANALYTICAL_UNCERTAINTY]** Operators, verifiers, trustees, public/private entities, contractors, final recipients and similar classes can vary by national or transactional context. They were coded `HYBRID`, `UNSPECIFIED` or `UNRESOLVED`-equivalent descriptive status where the act did not establish one fixed status; no external institutional knowledge was imported.

### Member States versus competent authorities

**[EXPLICIT_TEXT]** Member States and competent authorities were kept distinct whenever the act assigned a duty to the State as a whole and a separate permit, registry or administrative task to a designated authority. This distinction is explicit in `32003L0087` Articles 4, 6, 14, 18 and 19 and recurs in the later instruments.

### Recital-only actor

**[EXPLICIT_TEXT]** `Market intermediaries acting on an agency basis` in `32018R0842` is retained as one legally relevant actor-class record because the phrase appears in recital 20. It is flagged `recital_only_actor = YES`, `analytical_uncertainty = YES` and `review_required = YES`; no operative duty is assigned to it in this phase.

## G. Evidence quality

**[EXPLICIT_TEXT]** E2 actors:

- `32015D1814` — EU ETS installations;
- `32021R1119` — international scientific bodies.

These records required limited reconstruction across provisions or across the instrument's reference structure and are flagged for review.

**[EXPLICIT_TEXT]** E3 actors: none. No actor was included solely on broad contextual inference without a traceable legal anchor.

**[EXPLICIT_TEXT]** Recital-only actors: `32018R0842` — market intermediaries acting on an agency basis.

**[EXPLICIT_TEXT]** The five corpora contain no unmapped actor record and no map row lacking a legal action, evidence level or source anchor.

## H. Possible upstream issues

**[EXPLICIT_TEXT]** No upstream correction to Phase 3 was made or is required by the Phase 4 inventory.

**[CROSS_PROVISION_RECONSTRUCTED]** Phase 4 identifies additional legally relevant institutional classes not individually named in the high-level Phase 3 memos, including verifiers, committees, registries, national advisory bodies, audit bodies, final recipients, contractors, stakeholders and beneficiaries. This is an expected granularity expansion from whole-instrument reconstruction to actor inventory, not an inconsistency.

**[UPSTREAM_REVIEW_NOTE]** `32018R0842` contains the recital-only actor class concerning agency-based allocation transfers. Phase 3 mentioned the transfer architecture at instrument level; Phase 4 now records the exact actor-class expression and its recital-only status without modifying the Phase 3 memo.

## I. Prohibited-stage check

**[EXPLICIT_TEXT]** No prohibited coding was performed:

- R: **NO**
- I: **NO**
- T: **NO**
- intermediary adjudication: **NO**
- regulatory relation reconstruction: **NO**
- mechanism coding: **NO**
- 3–4–2 family coding: **NO**
- Knowing, Assuring or Steering coding: **NO**
- accountability, centrality, discretion or architecture coding: **NO**

All actor records have `role_not_adjudicated = YES`.

## J. Researcher decisions required before Phase 5

**[RESEARCHER_DECISION_REQUIRED]** Authorize whether Phase 5 may reconstruct regulatory relations from the Phase 4 actor–provision map using the law-specific actor IDs.

**[RESEARCHER_DECISION_REQUIRED]** Confirm whether recital-only and E2 actor classes may be carried into relation review as provisional candidates, subject to explicit evidence review, or should remain excluded from relation construction unless an operative provision independently supports them.

**[RESEARCHER_DECISION_REQUIRED]** Confirm whether open-ended actor classes such as stakeholders, public/private implementing entities and final recipients should remain aggregated at class level in Phase 5 or be split only when a later provision supplies a legally distinct subclass.

No other decision is required to close Phase 4.

## Quality gate

| Gate | Result | Basis |
|---|---|---|
| Q1 — Coverage | PASS | 89 actor records and 173 mapped actions across all five laws. |
| Q2 — Evidence | PASS | Every actor and action has traceable provision evidence; E3 count is zero. |
| Q3 — Consolidation | PASS | 38 alias records; canonical names and law-specific IDs are stable. |
| Q4 — Granularity | PASS | Specific entities and actor classes are distinguished. |
| Q5 — Actor/object separation | PASS | Non-actor regulatory objects were excluded. |
| Q6 — Task fidelity | PASS | Legal verbs are recorded without converting them into mechanisms. |
| Q7 — Role neutrality | PASS | Every actor has `role_not_adjudicated = YES`. |
| Q8 — No intermediation coding | PASS | No actor was adjudicated as an intermediary. |
| Q9 — No relation reconstruction | PASS | No R–T or R–I–T relation rows were created. |
| Q10 — No mechanism coding | PASS | No nine-mechanism assignment was made. |
| Q11 — Provenance | PASS | Map rows contain article/paragraph or recital/annex location and source anchors. |
| Q12 — Clean-room integrity | PASS | Only authorized R3 corpora and Phase 3 outputs were used. |

**[EXPLICIT_TEXT — stop rule]** Phase 5 was not started. No relation, intermediary or mechanism outputs were created.

R3_PHASE_4_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
