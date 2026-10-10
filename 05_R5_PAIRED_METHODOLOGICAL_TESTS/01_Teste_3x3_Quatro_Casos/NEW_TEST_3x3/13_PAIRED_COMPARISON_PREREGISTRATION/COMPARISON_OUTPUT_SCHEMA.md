# Esquema de saídas futuras

Todos os arquivos abaixo estão pré-criados, somente com cabeçalhos ou estrutura narrativa, em `FUTURE_COMPARISON_OUTPUT_TEMPLATES/`. Permanecem em branco na fase de preregistro. Cada caso recebe cópia isolada do conjunto; a síntese familiar só é criada após quatro perfis congelados.

| Arquivo | Escopo | Finalidade |
|---|---|---|
| `PAIR_MATCH_REGISTER.csv` | caso | Proposições C0–C4, âncoras, correspondência M1–M7 e justificativa. |
| `MATERIAL_DIFFERENCE_REGISTER.csv` | caso | Materialidade, D1–D8, efeitos e registros vinculados. |
| `HUMAN_REVIEW_QUEUE.csv` | caso | Questão cega, evidência, proposições e gatilhos H1–H11; decisão vazia. |
| `HUMAN_ADJUDICATION_REGISTER.csv` | caso | Decisão humana, fundamento, incerteza e efeito metodológico posterior. |
| `CASE_COMPARATIVE_PROFILE.csv` | caso | Vetor categórico, categoria C-A–C-F e base de decisão. |
| `CASE_COMPARISON_REPORT.md` | caso | Relato estruturado, sem ranking. |
| `CASE_COMPARISON_QA.md` | caso | Controle de integridade do caso. |
| `FOUR_CASE_COMPARATIVE_REGISTER.csv` | família | Quatro categorias/perfis e vínculo a relatórios. |
| `CLIMATE_REPLICATION_ANALYSIS.md` | família | Regra e resultado de replicação SCF–CBAM. |
| `TRANSFER_ANALYSIS.md` | família | Regra e resultado AI/Directive. |
| `ANALYTICAL_COST_REGISTER.csv` | família | Descritores de custo e comparabilidade. |
| `FAMILY_COMPARATIVE_SYNTHESIS.md` | família | Categoria F1–F7 e linguagem calibrada. |

### Campos de controle

Todo registro comparativo deve conter `case_id`, `comparison_run_id`, `protocol_manifest_sha256`, `executor_model`, `executor_deviation_note`, `created_at`, `status` e referências estáveis aos artefatos V8/RGAM. Campos de decisão humana ficam em branco até adjudicação real. Nenhum template possui conclusão, contagem analítica ou rótulo de resultado pré-preenchido.

### CSV — cabeçalhos vinculantes

Os cabeçalhos nos arquivos template são a definição operacional mínima. Campos adicionais só podem ser adicionados sem alterar categorias/regras congeladas e devem ser descritos em log de desvio; não podem preencher resultados retrospectivamente.
