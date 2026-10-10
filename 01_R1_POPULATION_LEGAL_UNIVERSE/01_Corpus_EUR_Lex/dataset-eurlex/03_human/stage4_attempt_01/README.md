# Pacote de benchmark da Etapa 4

O pacote foi construído exclusivamente com `02_corpus/act.md` e `methodology/v1.1.0/`, usando `reference_coding_schema.json` para R1, R2 e RA. O `experimental_output_schema.json` não foi usado na construção.

Arquivos principais:

- `candidate_universe.csv`: universo deduplicado com `candidate_origin`;
- `lexical_screening.csv`: ocorrências e contextos das strings;
- `structural_reading.csv`: cobertura estrutural e base de inclusão;
- `reference_R1.json`, `reference_R2.json`: codificações independentes;
- `reference_auto_adjudication.json`: adjudicação automática RA;
- `reference_comparison.csv`: acordos, divergências e fundamento de RA;
- `HUMAN_REVIEW_REQUIRED.md`, `human_review.csv`: pacote mínimo do gate humano;
- `reference_experimental_crosswalk.md`: ponte para comparação posterior.

O benchmark não está bloqueado como referência final. A revisão humana é obrigatória antes da Etapa 5.
