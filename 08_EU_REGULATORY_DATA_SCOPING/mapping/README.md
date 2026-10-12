# mapping/ — Mapeamento sistemático de dados legislativos e regulatórios da UE

Pesquisa independente, sob responsabilidade científica de Igor Caires Machado. Iniciada no gate G2 (2026-10-10) por reorientação do estudo *EU Regulatory Data Scoping*. Tudo o que é de G0 a G1-READY fica fora desta pasta e não foi alterado.

**Estado:** rodada 2 concluída (2026-10-10). 252 candidatos a recurso, todos com classificação provisória feita por agente de IA; nenhuma linha confirmada por pesquisador. O estado da rodada 1 (105 candidatos) está congelado em `snapshots/round1/`.

## Por onde começar

| Quero | Abrir |
|---|---|
| Entender a mudança de rumo | `protocol/INDEPENDENT_MAPPING_REORIENTATION_v1_0.md` |
| Saber como se busca e se verifica | `protocol/SYSTEMATIC_MAPPING_PROTOCOL_v1_0_DRAFT.md` |
| Ver os resultados | `reports/G2_INITIAL_MAPPING_REPORT.md` |
| Ver o que vem a seguir | `reports/G2_NEXT_ROUND_PLAN.md` |
| Avaliar publicação | `reports/PUBLICATION_POTENTIAL_NOTE.md` |
| Usar os dados | `data/resources.csv` e `data/DATA_DICTIONARY.md` |

## Rodada 2

| Quero | Abrir |
|---|---|
| Resultados da rodada 2 | `reports/G2_ROUND2_RESULTS.md` |
| Separação dados e infraestrutura; níveis de evidência | `protocol/AMENDMENT_A01_DATA_VS_INFRASTRUCTURE_v1_0.md` |
| Comparação com o LYNX e antecedentes | `reports/PRIOR_ART_AND_LYNX_COMPARISON.md` |
| Proposta de validação humana | `protocol/HUMAN_VALIDATION_PROPOSAL_v0_1.md` |
| O que mudou em arquivos da rodada 1 | `CHANGES_ROUND2.md` |

## Conteúdo

```
mapping/
  protocol/    reorientação, protocolo, registro de consultas da rodada
  curation/    julgamentos provisórios da rodada, com a base de cada campo
  data/        tabelas geradas (não editar à mão) e dicionário de dados
  schemas/     vocabulários controlados
  scripts/     busca registrada, construtor, validador
  evidence/    respostas de busca e capturas de páginas, com registros e hashes
  reports/     relatório, plano, nota de publicação, saídas de teste
  MANIFEST.sha256
```

## Refazer

```
python mapping/scripts/build_mapping_base.py     # gera as tabelas a partir da curadoria e das evidências
python mapping/scripts/validate_mapping.py       # verificações de consistência
python -m unittest discover -s tests             # 152 testes: 87 anteriores, 26 da rodada 1 e 39 da rodada 2
```

Nada disso usa a rede. Só `mapping_search.py run` e `scripts/capture_evidence.py capture` fazem requisições.

## Nova rodada

1. Criar `protocol/SEARCH_QUERIES_G2_ROUND<n>.csv` e executar `python mapping/scripts/mapping_search.py run --registry <arquivo>`.
2. Capturar páginas com `scripts/capture_evidence.py` (pasta de saída `mapping/evidence/captures`).
3. Acrescentar os julgamentos num arquivo de curadoria; reconstruir; validar.
4. Identificadores `MR-nnnn` nunca são reutilizados; evidência nunca é apagada.

## Avisos

- `VERIFIED` significa que nome e localização constam de fonte primária preservada. Nenhum dataset foi aberto.
- `NOT_ASSESSED` significa não coletado, não inexistente.
- Falha de acesso não é evidência de ausência.
- `evidence/` contém cópias de páginas de terceiros. Antes de publicar a pasta, decidir se elas podem ser redistribuídas.
