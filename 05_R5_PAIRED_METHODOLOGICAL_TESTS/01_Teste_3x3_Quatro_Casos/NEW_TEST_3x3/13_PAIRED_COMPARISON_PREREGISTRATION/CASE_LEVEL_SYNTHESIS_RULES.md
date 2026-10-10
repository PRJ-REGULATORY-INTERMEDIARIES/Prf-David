# Regras de síntese por caso

Após todas as adjudicações exigidas, cada caso recebe vetor categórico, sem escore:

`[SUBSTANCE, TRACEABILITY, SENSITIVITY, CALIBRATION, REGRESSION, COST]`

Os campos devem expressar o padrão observado/adjudicado e apontar os registros justificadores. `COST` é secundário: registrar, quando disponível de forma comparável, número de registros analíticos, etapas distintas, artefatos, itens HQ, dependências explícitas não resolvidas e carga de fluxo documentada. Tempo de execução não é decisivo se sessões, interrupções, hardware ou contexto diferirem. Volume bruto não é custo nem qualidade. Resultado de custo: `LOW_ADDITIONAL_COST`, `MODERATE_ADDITIONAL_COST`, `HIGH_ADDITIONAL_COST` ou `COST_NOT_RELIABLY_COMPARABLE`.

Uma e somente uma categoria de síntese é atribuída:

| Código | Categoria | Regra |
|---|---|---|
| C-A | `RGAM_INCREMENTAL_SUBSTANTIVE_GAIN` | Há ganho substantivo RGAM conforme regra cumulativa, sem regressão material que requeira C-D. |
| C-B | `RGAM_METHOD_GAIN_WITHOUT_SUBSTANTIVE_GAIN` | Substância equivalente, mas ganho material de rastreabilidade, sensibilidade ou calibração. |
| C-C | `SUBSTANTIVE_EQUIVALENCE` | Conclusão defensável equivalente, sem contribuição incremental material. |
| C-D | `MIXED_GAIN_AND_REGRESSION` | Coexistem ganho(s) e regressão(ões) materiais. |
| C-E | `RGAM_REGRESSION` | Há regressão material e nenhum ganho material que imponha C-D. |
| C-F | `COMPARISON_INDETERMINATE` | Adjudicação, evidência ou comparabilidade impede conclusão defensável. |

Relatórios distinguem `OBSERVED`, `ADJUDICATED`, `INFERRED` e `NOT_ESTABLISHED`. Não usam fórmula global “RGAM é melhor que V8”.
