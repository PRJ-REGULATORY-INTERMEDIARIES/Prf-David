# Critérios prospectivos de avaliação A/B

**Aplicação:** somente após G1B e sobre o mesmo manifest de evidência. Nenhum resultado é lançado nesta etapa.

| Critério | Pergunta de auditoria | Evidência exigida |
|---|---|---|
| Defensabilidade inferencial | o claim para no nível que a evidência sustenta? | warrant, contraevidência e stopping rule |
| Rastreabilidade jurídica | leitor consegue ir de claim a provisão? | claim → configuração → relação → declaração → fonte/hash |
| Relação sem suporte | atribuição/dever unilateral virou edge? | partes, ação, direção, modalidade e condição |
| Erro entre níveis | propriedade de ator/relação virou configuração/arquitetura/regime? | portador da propriedade e fronteira declarados |
| Clarificação estrutural | B esclarece ordem, porta, condição, posição ou parte–todo? | diferença específica, não rótulo adicional |
| Incerteza e parada | ambiguidades foram preservadas e claims não foram promovidos? | `deferred`/`human_review_needed` e motivos |
| Valor incremental | B muda corretamente ou apenas repete A? | `B_IMPROVES`, `B_CLARIFIES_ONLY`, `B_EQUIVALENT`, `B_WORSE` ou `UNRESOLVED` |
| Esforço adicional | ganho justifica campos, tempo e decisões extras? | tempo, novos campos, ambiguidades/adjudicação |

Track A deve declarar as regras V8, produzir claims e receber hash antes do acesso à produção de B. Track B pode qualificar, reduzir ou contradizer A, mas não altera A. Nenhuma comparação intercaso substitui a comparação A/B intra-caso.
