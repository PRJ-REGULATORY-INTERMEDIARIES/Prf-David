# Crosswalk benchmark de referência → outputs experimentais

**Versão:** Etapa 4 / metodologia `v1.1.0`  
**Estado:** informativo; não executa comparação  
**Corpus:** `02_corpus/act.md`  
**Benchmark:** permanece inacessível a G0/G1/G2 até o reference lock da Etapa 5

## Finalidade

Este documento define como o benchmark adjudicado será comparado posteriormente aos outputs experimentais. Ele não altera R1, R2 ou RA, não usa o `experimental_output_schema.json` para construir o benchmark e não executa G0/G1/G2.

## Correspondência de campos

| Benchmark de referência | Output experimental futuro | Regra de comparação |
|---|---|---|
| `candidate_id` | `relation_id` | Comparar por localização e identidade relacional; o ID experimental não precisa ser igual. |
| `candidate_origin` | `candidate_origin` | Comparação descritiva de cobertura lexical/estrutural. |
| `source_location` | `location` | Normalizar artigo, parágrafo, ponto, subparágrafo e recital sem alterar o corpus. |
| `evidence_items[].quote` | `evidence` | Verificar sobreposição localizada e fidelidade ao texto canônico. |
| `R`, `I`, `T` | `R`, `I`, `T` | Comparar rótulos de atores/papéis; `T` só pode ser ator, classe de atores ou papel institucional. |
| `action` | `action` | Comparar presença e correspondência da ação. |
| `object` | `object` | Comparar separadamente de `T`; atividade, informação, produto, processo, conduta e estado de conformidade permanecem objeto. |
| `mediating_function` | `mediating_function` | Comparar por equivalência funcional, sem exigir a mesma formulação lexical. |
| `primary_mechanism` | `mechanism` | Comparar a família primária; mecanismos secundários não têm coluna equivalente experimental. |
| `relational_result` | `decision` | Aplicar uma tabela de mapeamento pré-especificada na análise, preservando `insufficient_evidence` como incerteza e não como positividade. |
| `confidence` | `confidence` | Comparação descritiva, sem interpretação probabilística. |
| `notes` e `interpretive_note` | `notes` | Usar para auditoria qualitativa e explicação de divergências. |

## Mapeamento da decisão

O mapeamento deverá ser aplicado somente na Etapa 7, depois do human gate e do reference lock:

- referência `positive` ↔ decisão experimental `intermediated`;
- relação direta com `I = null` e resultado `negative` ↔ decisão experimental `direct`;
- referência `conditional` ↔ decisão experimental `uncertain`;
- referência `insufficient_evidence` ↔ decisão experimental `not_supported` ou `uncertain`, conforme a semântica efetivamente registrada pelo output e a regra de análise pré-especificada;
- referência `not_candidate` no screening não deve ser convertida automaticamente em falso negativo: primeiro verificar se o output identificou uma relação material distinta na mesma localização.

As regras acima são uma ponte analítica, não uma recodificação do benchmark. Qualquer caso ambíguo deve conservar a localização, a evidência e a justificativa para classificação qualitativa.

## Campos que não terão equivalente experimental

Os seguintes elementos pertencem à referência e não devem ser inferidos artificialmente dos outputs experimentais:

- condições A–E e suas evidências por condição;
- classes de observabilidade por item;
- papéis auxiliares detalhados (`rule_source`, `standard_setter`, `oversight_authority`, `enforcement_authority`);
- `screening_status` e `additional_context_required` como campos de saída experimental;
- `secondary_dimensions.responsibilization` e `secondary_dimensions.empowerment`;
- distinção interna entre `evidence_role` e `supports`.

Esses campos podem orientar a interpretação da referência, mas não devem ser tratados como respostas ausentes ou erradas dos agentes experimentais.

## Controle de acesso e temporalidade

Até a conclusão do `HUMAN_GATE_REFERENCE_ADJUDICATION` e da Etapa 5:

1. R1, R2, RA e `human_review.csv` permanecem em `03_human/`;
2. nenhum benchmark deve ser incluído nos prompts ou enviado a G0/G1/G2;
3. nenhuma métrica deve ser calculada;
4. divergências humanas devem ser registradas antes de qualquer congelamento da referência.
