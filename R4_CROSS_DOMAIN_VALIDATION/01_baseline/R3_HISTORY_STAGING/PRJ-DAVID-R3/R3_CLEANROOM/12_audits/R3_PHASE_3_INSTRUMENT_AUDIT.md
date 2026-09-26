# R3 Phase 3 — Whole-Instrument Reconstruction Audit

## Status and scope

**[EXPLICIT_TEXT — Phase 3 authorization]** Phase 2B was approved and Phase 3 was executed only for the five validated R3 corpora: `32003L0087`, `32015D1814`, `32018R0842`, `32021R1119` and `32023R0955`.

**[EXPLICIT_TEXT — clean-room control]** No previous corpus, dataset, coding, case summary, actor map, relation map, mechanism assignment, review output or prior analytical note was consulted.

**[EXPLICIT_TEXT — Phase 3 prohibition log]** No intermediary list, `LAW × INTERMEDIARY` row, R/I/T relation, direct R-T relation, mechanism code, Articulation code, Treatment of Information code, Regulatory Reliability code, mechanism chain, accountability assessment or meta-intermediation analysis was created.

## Corpora used and completeness of reading

**[EXPLICIT_TEXT — corpus manifests and validation register]** The source of analysis was the validated structural corpus under `02_corpus`, not the raw source PDFs and not any earlier material. For each case, `act_numbered.md`, `act_full.md`, `recitals.md`, `operative.md`, `article_index.csv` and `CORPUS_MANIFEST.yaml` were used for reading and structural control.

| CELEX | Instrument type | Recitals | Articles | Annexes | Reading status |
|---|---:|---:|---:|---:|---|
| 32003L0087 | Directive | 30 | 33 | I-V (5) | COMPLETE — full validated corpus and all annexes examined |
| 32015D1814 | Decision | 12 | 5 | none | COMPLETE — full validated corpus examined |
| 32018R0842 | Regulation | 46 | 17 | I-IV (4) | COMPLETE — full validated corpus and all annexes examined |
| 32021R1119 | Regulation | 40 | 14 | none | COMPLETE — full validated corpus examined, including amendment provisions |
| 32023R0955 | Regulation | 47 | 29 | I-V (5) | COMPLETE — full validated corpus, chapters and all annexes examined |

**[EXPLICIT_TEXT — corpus register]** The counts above are the validated structural counts recorded in `02_corpus/R3_CORPUS_REGISTER.csv`; they are not estimates derived from keyword hits.

## Analytical uncertainties

**[EXPLICIT_TEXT / ANALYTICAL_UNCERTAINTY]** All five original acts refer to other Union instruments that supply part of their operating context. Phase 3 retained those references as scope or dependency statements and did not import the content of the external instruments.

**[EXPLICIT_TEXT / ANALYTICAL_UNCERTAINTY — 32003L0087 Articles 24-30]** Directive 2003/87/EC contains an architecture designed for expansion, linkage and later development. The profile therefore describes the original legal structure without treating later consolidated provisions as part of the primary coding source.

**[EXPLICIT_TEXT / ANALYTICAL_UNCERTAINTY — 32015D1814 Article 2]** The Decision modifies an existing Directive and assumes the wider EU ETS auction architecture. The memo reconstructs the Decision as a reserve instrument and does not reconstruct the full amended Directive.

**[EXPLICIT_TEXT / ANALYTICAL_UNCERTAINTY — 32018R0842 Articles 2, 5-7 and 16]** The annual target system depends on inventory, LULUCF, EU ETS and Energy Union reporting instruments. The memo records the legal interfaces but keeps the instrument boundary.

**[EXPLICIT_TEXT / ANALYTICAL_UNCERTAINTY — 32021R1119 Article 4(3)-(6)]** The 2040 climate target is not fixed by the original act; the act mandates a later legislative proposal and an indicative budget process.

**[EXPLICIT_TEXT / ANALYTICAL_UNCERTAINTY — 32023R0955 Articles 1, 10-11 and 29]** Fund resources and implementation timing are partly linked to external Directive provisions. The memo records the dependency without reconstructing that external financing regime.

## Cross-provision reconstruction

**[CROSS_PROVISION_RECONSTRUCTION]** Cross-provision reconstruction was used where the regulatory system could not be represented faithfully by article-by-article listing. The principal instances were:

- **32003L0087 — Articles 4-20 and Annexes I-V:** permit, information, verification, allowance and registry rules were reconstructed as one compliance-market sequence.
- **32015D1814 — Article 1(4)-(8), Article 2 and Article 3:** circulation publication, reserve formulas, auction-calendar adjustment and review were reconstructed as one stabilization cycle.
- **32018R0842 — Articles 4-12:** annual allocations, flexibilities, corrective action, compliance checks and registry accounting were reconstructed as one national trajectory system.
- **32021R1119 — Articles 3-11 and Articles 12-13:** goals, science, adaptation, assessment, participation and Energy Union integration were reconstructed as one framework-and-review system.
- **32023R0955 — Articles 4-21 and 22-27:** Plan design, finance, appraisal, payment, controls, monitoring and evaluation were reconstructed as one Fund lifecycle.

## Analytical inference

**[ANALYTICAL_INFERENCE]** One declared orientation was assigned per instrument from the instrument's declared objective and whole-instrument structure, not from mechanism frequency:

- `32003L0087`: compliance-oriented market-organization regime.
- `32015D1814`: market-stabilization instrument within the EU ETS market framework.
- `32018R0842`: binding national target-setting and compliance framework.
- `32021R1119`: framework-setting and review-oriented climate governance structure.
- `32023R0955`: conditional social-financing and implementation-governance instrument.

**[ANALYTICAL_INFERENCE]** These labels are instrument-level orientations only. They are not mechanism codes, relation codes or claims about comparative complexity, intermediary dependence, monitoring intensity, centralization or maturity.

## Difficult distinctions recorded

### Regulatory object versus target

**[CROSS_PROVISION_RECONSTRUCTION]** The principal distinctions were:

- `32003L0087`: emissions and allowance infrastructure are the regulatory object; installation operators and allowance holders are broad governed classes.
- `32015D1814`: allowance supply timing and reserve operation are the regulatory object; Member State auction arrangements and market participants are broad governed classes.
- `32018R0842`: national emissions and annual allocations are the regulatory object; Member States are the directly obligated class.
- `32021R1119`: climate objectives, emissions/removals and policy consistency are the regulatory object; Union institutions and Member States are the broad governed classes.
- `32023R0955`: social effects of carbon pricing and Fund resource use are the regulatory object; vulnerable households, micro-enterprises and transport users are the broad beneficiary/governed classes.

### Authority versus governed actor

**[CROSS_PROVISION_RECONSTRUCTION]** The profiles distinguish institutional responsibility from broad governance exposure. For example, Commission assessment or publication functions were recorded as authority components, while Member States, operators, market participants or beneficiaries were recorded as governed classes where the provisions impose duties, conditions or affected status.

**[EXPLICIT_TEXT — R-I-T firewall]** No institution was assigned a fixed R, I or T identity. Any later relation-level classification requires a separate authorized phase.

### Orientation ambiguities

**[ANALYTICAL_UNCERTAINTY]** `32003L0087` could be described as both a market-organization and compliance instrument; the selected label preserves both dimensions. `32015D1814` depends on the underlying EU ETS and could be treated as an amendment-only instrument; its standalone reserve objective supports the selected stabilization label. `32021R1119` contains binding targets but its dominant architecture is framework and review, so it was not labeled only as a compliance regime. `32023R0955` contains social policy, climate investment and financial control; the selected label reflects the conditional financing lifecycle.

## Quality gate

| Question | Result | Audit basis |
|---|---|---|
| Q1 — Can an unfamiliar researcher understand the objective? | PASS | Each memo states the declared objective with provisions. |
| Q2 — Object distinguished from target? | PASS | Object/target distinctions are recorded above and in each memo. |
| Q3 — Targets broad only? | PASS | No individual R-T relations or candidate intermediaries were created. |
| Q4 — Authorities without relational R/I/T coding? | PASS | Authorities are instrument-level institutions only. |
| Q5 — Obligations grouped functionally? | PASS | Each memo uses functional clusters, with provision ranges. |
| Q6 — Structural logic explicit? | PASS | Each memo contains a functional sequence grounded in provisions. |
| Q7 — Orientation justified by law? | PASS | Each orientation is tagged `ANALYTICAL_INFERENCE` and justified from structure. |
| Q8 — Intermediary/mechanism coding avoided? | PASS | Prohibited outputs were not created. |

## Researcher decisions required before Phase 4

**[EXPLICIT_TEXT / RESEARCHER_DECISION_REQUIRED]** Before Phase 4, the researcher must authorize whether the instrument-level profiles are accepted as the baseline for actor-level reconstruction.

**[RESEARCHER_DECISION_REQUIRED]** The researcher should decide whether Phase 4 will use only the original-act wording preserved here or may add separately authorized reference-only consolidated/amending materials for contextual navigation. No such materials were used in Phase 3.

**[RESEARCHER_DECISION_REQUIRED]** The researcher should confirm the treatment of broad institutional classes that recur across instruments, including Commission, Member States, registries, reporting systems, audit bodies, public/private implementing entities and beneficiaries, before any relation-level R/I/T coding.

**[EXPLICIT_TEXT — stop rule]** No Phase 4 work was initiated. The five memos and `INSTRUMENT_PROFILE.csv` are the complete Phase 3 outputs.

R3_PHASE_3_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
