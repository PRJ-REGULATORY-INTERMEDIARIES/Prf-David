# CODEBOOK DE DADOS, TRIAGEM E AUDITORIA

## Vocabulário controlado

**Origem de registros:** `seed`, `systematic_search`, `citation_chaining`, `expert_suggestion`, `manual_grey_literature`.
**Decisões individuais:** `include`, `exclude`, `uncertain`.
**Etapas:** `title_abstract`, `full_source`.
**Decisões consensuais:** `include`, `exclude` (exigir justificativa para exclusões na etapa final).
**Dedup:** `unique`, `duplicate`.
**Status técnico:** `UNVERIFIED`, `NA` ou nota `0`, `1`, `2`.

## Motivos de exclusão

- `NOT_EU_RELATED` — relação com legislação/governança UE não demonstrável.
- `UNSTRUCTURED` — notícia ou documento isolado sem estrutura de dados.
- `NOT_LEGAL_REGULATORY` — fora do domínio jurídico-regulatório.
- `NOT_IDENTIFIABLE` — coleção inexistente/inverificável.
- `INSUFFICIENT_DOCUMENTATION` — impossibilidade de determinar elegibilidade mesmo após fonte completa (usar criteriosamente).
- `OTHER` — especificar no campo notas.

**Não excluir por licença desconhecida ou acesso restrito por si só.**

## Critérios técnicos (avaliados separadamente por reviewer e dataset)

Cada score vem acompanhado de URL da evidência, método de verificação e data. `UNVERIFIED` não participa de denominadores de capacidade observada. `NA` somente com motivo documentado.

| Criterion | 0 = não evidenciado / ausente após inspeção | 1 = indireto/parcial | 2 = explícito/estruturado |
|---|---|---|---|
| `LEGAL_ID` | sem identificador jurídico utilizável | identificador recuperável por texto ou integração | CELEX/ELI ou equivalente em campo estruturado |
| `ACTORS` | atores não distinguíveis | atores em texto/metadado não-normalizado | atores em entidade/campo estruturado |
| `FUNCTIONS` | funções/competências não distinguíveis | descrições abertas/documentais | funções/competências estruturadas ou códigos explícitos |
| `RELATIONS` | relações de governança não verificáveis | relações inferíveis com interpretação documental | relações dirigidas codificadas com papeis identificáveis |
| `LEGAL_BASIS` | sem ancoragem jurídica verificável | ligação legal indireta, referência ampla | instrumento/artigo/ID legal recuperável com precisão |
| `TEMPORALITY` | não há tempo relevante identificado | data de atualização ou referência temporal parcial | validade/versionamento/ocorrência com semântica temporal documentada |
| `MACHINE_ACCESS` | apenas material não estruturado | consulta web/exportação manual estruturada | API/download de dados estruturados documentado e testado |
| `PROVENANCE` | fonte e histórico indeterminados | mantenedor ou atualização parcial | origem, documentação e versão verificáveis |
| `REUSE_RIGHTS` | licença ou condição explicitamente impeditiva | condições restritas mas claras para uso definido | licença autorizando claramente o reuso planejado |

**Limites das notas:** zero deve ser atribuído apenas após inspeção suficiente; não usar `0` como sinônimo de desconhecido. Em `MACHINE_ACCESS`, `2` exige teste e registro do resultado, não mera publicidade de uma API.

## Capacidade RIT (tipologia, não pontuação artificial)

- `D0_DOCUMENT`: textos jurídicos ou metadados sem atores e relações extraídos.
- `D1_ENTITIES`: atores ou organizações identificáveis, mas vínculos regulatórios não explicitados.
- `D2_NORMATIVE_LINK`: atores/decisões vinculáveis a atos ou artigos; relação ainda pode exigir extração.
- `D3_ROLE_RELATION`: relação dirigida R–I–T ancorada em evidência, identificada de modo explícito ou após extração auditável.

Um registro D3 exige **norma, artigo, identificação dos papéis e trilha de evidência**; não deve ser inferido apenas do rótulo *intermediary*, *notified body* ou *data intermediation service*.

## Confiabilidade

- Screening: duas decisões independentes por registro e fase; comparar antes de consenso.
- Auditoria: mínimo 20% duplo, estratificado; um valor idêntico sem evidência não representa concordância válida.
- Divergências: registrar motivo, método de adjudicação e revisão de codebook quando mudança conceitual afetar vários casos.
- Não somar notas para construir ranking geral até uma decisão metodológica adicional.

## Regras de vinculação

1. Um `record_id` é uma ocorrência de busca, não um dataset.
2. O dataset canônico exige `dataset_id` único, com `source_record_ids` ligados a evidência de triagem.
3. Cada recurso técnico pertence a um dataset canônico pelo `dataset_id`.
4. `legal_celex`/`legal_eli` são armazenados como *strings*; nenhum join permite afirmar equivalência sem inspeção.
5. `rit_pilot` documenta inferências separadas, com validador humano e artigo da norma.
