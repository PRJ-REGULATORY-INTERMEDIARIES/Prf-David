# Production Methodology — Working Draft v1.3

**Project:** `dataset-eurlex`  
**Version:** production v1.3  
**Status:** working methodological architecture for the final human-review package; no historical coding or frozen corpus is changed  
**Predecessor:** production v1.2 (preserved in its original artifacts and changelog)

## Change in analytical architecture

The v1.1/v1.2 regulatory-relation record remains necessary and is retained. It is the primary **coding and evidentiary** unit: it records the legally anchored episode, the R/I/T reconstruction, the third-actor test, operative evidence, contextual support, and the researcher decision.

For substantive mapping of regulatory intermediation, however, the principal analytical unit is now the **actor-in-role within an act or regulatory context**. The four levels are:

1. **Act / regulatory regime** — the documentary and higher-level comparative architecture.
2. **Actor-in-role** — actor × act × role, and actor × act × context × role only when aggregation would erase a meaningful difference.
3. **Intermediary function / mechanism** — recorded only where the actor occupies I, including target-facing, regulator-facing, or bidirectional orientation.
4. **Regulatory relation / episode** — the retained coding and evidentiary layer supporting the role classification.

> Regulatory relationships are the primary coding and evidentiary units used to identify relational roles. For substantive mapping of regulatory intermediation, the principal analytical unit is the actor-in-role within a regulatory act or regulatory context. Act/regime-level units capture the broader architecture of intermediation.

Nota explicativa em português: **as relações regulatórias continuam sendo as unidades primárias de codificação e evidência para identificar papéis relacionais. Para o mapeamento substantivo da intermediação regulatória, a unidade analítica principal passa a ser o ator-em-papel dentro de um ato ou contexto regulatório. O ato/regime capta a arquitetura comparativa mais ampla da intermediação.**

## Consequences and safeguards

- R, I and T are contextual roles, not permanent attributes of organisations. An actor may be R in one episode, I in another, and T in a third.
- One actor-role record normally aggregates repeated supporting relations in the same case and role. Separate contexts are used only when the role is substantively different and the reason is documented.
- An I record requires at least one supporting relation unless explicitly marked `UNCERTAIN` or `RESEARCHER_DECISION_REQUIRED`.
- The legislative proposer, formal adopter, rule-maker, regulator, implementing regulator, supervisory authority, intermediary, and target are not collapsed. In particular, a proposer is not automatically R for every relation within an act.
- The rule that R cannot be its own I in the same materially overlapping episode remains in force.
- Operative provisions remain necessary for positive relations. Recitals may support interpretation but cannot independently generate a positive relationship.
- The v1.2 general boundary rules remain general: comitology may be an I when it institutionally contributes to a binding rule governing T; integrated expert/advisory input may be regulator-facing I; institutionalization density is evidentiary information; external influence is not automatically I. These are not actor- or article-specific automatic classifications.

## Scope of this change

This version transforms the current 25-record relationship matrix and the one unresolved R2 item into a final human-review package. It is not authorization for an open-ended new relation search. New candidate relations, if ever identified during final review, must remain `RESEARCHER_DECISION_REQUIRED` until the researcher decides.

## Provenance and human decisions

The damaged `R2_HUMAN_VALIDATION_relations.csv` is preserved as a historical artifact. Its reconstructed derivative is not represented as an untouched human-validation file. Every v1.3 derived record retains the human decision source, recorded rationale where available, the reconstruction status, and the source relation/uncertainty identifier. Missing rationale is `NOT_RECORDED`.

## Outputs

The versioned package is `cases/final_human_review_v2/`. Its canonical CSVs preserve the relationship-evidence layer, actor-role map, mechanism map, act summary, unresolved issues, normalization log, and provenance. The workbook is a review surface only.
