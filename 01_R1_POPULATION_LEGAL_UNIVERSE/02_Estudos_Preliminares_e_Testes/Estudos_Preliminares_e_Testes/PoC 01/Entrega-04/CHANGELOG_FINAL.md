# Final changelog — Entrega-04

## Preserved

- `Entrega-02/` and `Entrega-03/` remain historical/protocol deliveries.
- The seven human-validated v3 R-I-T relationships and 19 inherited actor
  records are retained as a regression baseline, not relabelled as new AI
  findings.
- The four-act A1 counts remain exactly 1,079; Taxonomy adds 13 in the
  five-act PoC, for 1,092 screening rows.

## Adjusted to the master prompt

- The CELEX manifest is now `CELEX_MANIFEST_v4.csv` / `.json` and separates
  base CELEX, version CELEX, ELI, legal-status/version placeholders,
  retrieval metadata, source URL and SHA-256.
- A1 records paragraph, provision type, semantic role and orthogonal entity
  form. A2 uses the canonical lowercase field names and links every output
  to `ai_run_ref`.
- The relationship table now carries explicit rule-source, regulator,
  oversight, enforcement and nested-intermediation fields, with unknowns
  marked rather than inferred. Mechanism detail is also materialised in
  `relationship_mechanisms_v4.csv`.
- The delivery adds `semantic_candidates_v4.csv`, `ai_runs_v4.csv`,
  `human_review_v4.csv`, `validation_sample_v4.csv` and
  `challenge_sample_v4.csv`, plus the candidate-discovery status table.
- The report is expanded with the conceptual framework, pipeline, model
  selection, human-in-the-loop controls, construct-validity boundaries,
  population-scaling plan and six analytical figures.

## Execution status

- EUR-Lex collection, A1 screening, deterministic sample selection,
  relationship regression copy, schema smoke test and DOCX rendering were
  executed.
- The live OpenAI adapter was implemented. The first generation request was
  blocked by `credit_balance_exhausted`; no substantive AI result, benchmark,
  second-coder statistic or winner was fabricated.
- The 201 dry-run calls remain explicitly `DRY_RUN_ONLY` and are excluded from
  findings, candidate promotion and model scoring.

## Open decisions for David

- Adjudicate Climate Benchmarks CAND-07 as conditional until the complete
  legal architecture is documented.
- Decide whether the next stress test should be CBAM; it is not added to this
  PoC corpus.
- Define the target population before any SPARQL/Cellar scale-up. Retrieval
  infrastructure solves retrieval, not population definition.
