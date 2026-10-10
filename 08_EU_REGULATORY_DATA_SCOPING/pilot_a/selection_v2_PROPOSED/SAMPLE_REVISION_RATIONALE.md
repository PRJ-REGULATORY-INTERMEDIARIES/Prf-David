# PILOTO A — AMOSTRA REVISADA (OPÇÃO B): JUSTIFICATIVA

**Data:** 2026-10-10 | **Estado:** **PROPOSED**. Nenhuma amostra foi escolhida em nome da equipe. Nenhum registro foi classificado ou triado.
**Uso restrito ao coordenador.**

A amostra candidata do G1-PREP (`pilot_a/selection/`) permanece intacta. Tudo o que é novo está em `pilot_a/selection_v2_PROPOSED/`.

## 1. O que mudou no procedimento

| Elemento | G1-PREP | G1-READY |
|---|---|---|
| Semente | `1160865795` | **A mesma** |
| Algoritmo de sorteio | Primeiro sorteio que satisfaz C1–C8 | O mesmo |
| Restrições C1–C8 e seus valores | — | **Inalterados** |
| Registros forçados | Grupos de URL idêntica | Grupos de URL idêntica **mais grupos obrigatórios declarados por escrito** |
| Viabilidade | Verificada só pelo próprio sorteio | Avaliada **antes** do sorteio: limites necessários por restrição, mais busca em sequência aleatória separada |
| Saída | `pilot_a/selection/` | Uma pasta por cenário, cada uma com `REQUIRED_GROUPS.json`, amostra, reserva e registro |

Os grupos obrigatórios são o julgamento humano que o algoritmo do G1-PREP não podia fazer sem ler colunas de julgamento. Aqui ele entra de forma explícita, com o motivo de cada grupo gravado no registro da execução. O algoritmo continua sem ler `rgam_potential`, `initial_priority` e `limitations`.

Sem grupos obrigatórios, o código reproduz exatamente a amostra do G1-PREP; há teste para isso.

## 2. Grupos avaliados

Cada grupo é uma **hipótese de relação** tirada dos nomes e hosts do inventário. Nenhuma relação foi verificada nas fontes.

| Grupo | Registros | Motivo | Regra que exercita |
|---|---|---|---|
| EP | EU08 + EU09 | Interface e acervo da mesma instituição, em hosts diferentes; o substituto por host não os emparelhou | R2 × R10; `distribution_of` × `overlaps_with` |
| TED | EU33 + EU34 | Serviço de dados e API de busca do mesmo publicador, em hosts diferentes | R2 × R10; `distribution_of` |
| DISC | EU11 | Único registro cujo nome no inventário o marca como dataset antigo | Critério I5; `successor_of`; evidência de recurso descontinuado |
| ACAD_DERIV | EU35 + EU39 | Corpus de pesquisa e tarefa de benchmark sobre legislação da UE; possível cadeia de derivação entre dois recursos de terceiros | R6; `derived_from` entre derivados |
| ACAD_ACQUIS | EU37 + EU38 | Dois corpora paralelos no mesmo host e com o mesmo radical no nome | `overlaps_with` × `part_of`; regra do mesmo mantenedor |
| ACAD_EURLEX | EU35 + EU36 | Dois corpora com o radical EURLEX no nome | `overlaps_with` × `successor_of` |

O grupo de URL idêntica (EU03 + EU07) continua forçado em todos os cenários.

## 3. Viabilidade, avaliada antes de qualquer sorteio

Comando: `python scripts/pilot_a_scenarios.py feasibility`. Saída literal em `gates/G1_READY_evidence/pilot_a_feasibility_run.txt`; detalhe em `FEASIBILITY_BEFORE_SELECTION.json`.

**Método.** Para cada cenário: (a) limites necessários de C1–C8 dados os registros forçados — se um falha, o cenário é comprovadamente inviável e nada é sorteado; (b) 2.000 tentativas numa sequência aleatória **separada** da de seleção, que mostram se existe amostra viável e com que frequência. A amostra encontrada nessa busca não é devolvida, para não virar alternativa.

| Cenário | Grupos | Forçados | Estado | Taxa de aceitação | Restrições no limite |
|---|---|---|---|---|---|
| S0 | nenhum (G1-PREP) | 2 | VIÁVEL | 17,7% | — |
| S1 | EP, TED | 6 | VIÁVEL | 4,8% | C8 |
| S2 | EP, TED, DISC | 7 | VIÁVEL | 4,6% | C8 |
| **S3a** | EP, TED, DISC, ACAD_DERIV | 9 | VIÁVEL | 4,6% | C8 |
| S3b | EP, TED, DISC, ACAD_ACQUIS | 9 | VIÁVEL | 3,5% | C6, C8 |
| S3c | EP, TED, DISC, ACAD_EURLEX | 9 | VIÁVEL | 2,8% | C6, C8 |
| S4 | EP, TED, DISC, ACAD_DERIV, ACAD_ACQUIS | 11 | VIÁVEL | 1,5% | C6, C8 |
| S5 | EP, TED, DISC, ACAD_DERIV, ACAD_EURLEX | 10 | VIÁVEL | 2,5% | C6, C8 |

**Nenhum cenário é inviável.** Dois efeitos estruturais, que valem para qualquer semente:

1. **C8 fica no limite assim que o par TED entra.** "Aplicação setorial" só tem EU33 e EU34; forçados os dois, a família sai da reserva. Com "Atores/participação" (um único registro, sempre selecionado), a reserva cobre no máximo 9 famílias, exatamente o mínimo exigido. Consequência: "Jurisprudência", que tem dois registros, passa a ter exatamente um na amostra.
2. **C6 fica no limite nos cenários com EU36, EU37 ou EU38.** Esses registros repetem um tipo de recurso já presente entre os forçados; todo registro restante precisa trazer tipo novo.

Um limite atingido não é violação: a restrição continua satisfeita, mas sem folga.

## 4. Regra de designação, fixada antes do sorteio

> A candidata revisada é o cenário com o menor conjunto de grupos obrigatórios que cobre todos os itens listados para avaliação no G1-READY (EU08+EU09, EU33+EU34, EU11, um par relacionado de corpora acadêmicos), sendo o par acadêmico aquele que exercita `derived_from` (regra R6), a relação mais relevante para a finalidade do estudo.

Pela regra, o cenário designado é **S3a**. A regra está gravada em `scripts/pilot_a_scenarios.py` e em `FEASIBILITY_BEFORE_SELECTION.json`, cujo registro de execução (03:23:00Z) antecede o do sorteio (03:23:15Z). Os demais cenários foram sorteados para comparação e continuam disponíveis.

## 5. Amostras sorteadas (uma execução por cenário, mesma semente)

Comando: `python scripts/pilot_a_scenarios.py select`. Saída literal em `gates/G1_READY_evidence/pilot_a_scenarios_run.txt`.

| Cenário | Tentativa aceita | Amostra |
|---|---|---|
| S0 | 9 | EU01 EU02 EU03 EU07 EU08 EU13 EU15 EU17 EU19 EU23 EU24 EU25 EU27 EU28 EU30 EU32 EU33 EU37 EU39 EU41 |
| S1 | 5 | EU01 EU03 EU07 EU08 EU09 EU12 EU14 EU16 EU17 EU19 EU23 EU24 EU25 EU26 EU27 EU30 EU32 EU33 EU34 EU40 |
| S2 | 3 | EU01 EU02 EU03 EU07 EU08 EU09 EU11 EU16 EU17 EU18 EU19 EU21 EU23 EU26 EU27 EU30 EU32 EU33 EU34 EU37 |
| **S3a** | 75 | **EU01 EU03 EU04 EU07 EU08 EU09 EU11 EU12 EU15 EU17 EU19 EU20 EU21 EU23 EU29 EU33 EU34 EU35 EU39 EU41** |
| S3b | 224 | EU01 EU02 EU03 EU07 EU08 EU09 EU11 EU15 EU16 EU17 EU18 EU21 EU23 EU26 EU27 EU28 EU33 EU34 EU37 EU38 |
| S3c | 224 | EU01 EU02 EU03 EU07 EU08 EU09 EU11 EU15 EU16 EU17 EU18 EU21 EU23 EU26 EU27 EU28 EU33 EU34 EU35 EU36 |
| S4 | 43 | EU02 EU03 EU07 EU08 EU09 EU11 EU12 EU16 EU17 EU18 EU19 EU21 EU23 EU27 EU33 EU34 EU35 EU37 EU38 EU39 |
| S5 | 30 | EU03 EU05 EU07 EU08 EU09 EU11 EU12 EU16 EU17 EU19 EU21 EU23 EU24 EU29 EU31 EU33 EU34 EU35 EU36 EU39 |

| Cenário | Tipos distintos | Tipo composto | Grupos de host com 2+ | Famílias na reserva | Máx. por família | Em comum com S0 |
|---|---|---|---|---|---|---|
| S0 | 20 | EU01, EU02, EU23 | 4 | 10 | 4 | 20 |
| S1 | 19 | EU01, EU12, EU23 | 4 | 9 | 4 | 13 |
| S2 | 19 | EU01, EU02, EU23 | 4 | 9 | 4 | 13 |
| **S3a** | 18 | EU01, EU12, EU23 | 3 | 9 | 4 | 11 |
| S3b | 18 | EU01, EU02, EU23 | 5 | 9 | 3 | 12 |
| S3c | 18 | EU01, EU02, EU23 | 4 | 9 | 3 | 11 |
| S4 | 18 | EU02, EU12, EU23 | 4 | 9 | 4 | 11 |
| S5 | 18 | EU05, EU12, EU23 | 3 | 9 | 4 | 9 |

## 6. A candidata designada (S3a) em detalhe

**EU01, EU03, EU04, EU07, EU08, EU09, EU11, EU12, EU15, EU17, EU19, EU20, EU21, EU23, EU29, EU33, EU34, EU35, EU39, EU41.**

Reserva (21): EU02, EU05, EU06, EU10, EU13, EU14, EU16, EU18, EU22, EU24, EU25, EU26, EU27, EU28, EU30, EU31, EU32, EU36, EU37, EU38, EU40.

| Família | Na amostra | Registros |
|---|---|---|
| Corpus normativo | 3 | EU01, EU03, EU04 |
| Infraestrutura | 1 | EU07 |
| Processo legislativo | 4 | EU08, EU09, EU11, EU12 |
| Delegação/implementação | 1 | EU15 |
| Atores/participação | 1 | EU17 |
| Transposição/Estados | 2 | EU19, EU20 |
| Fiscalização | 1 | EU21 |
| Jurisprudência | 1 | EU23 |
| Intermediação RIT | 1 | EU29 |
| Aplicação setorial | 2 | EU33, EU34 |
| Corpus acadêmico | 3 | EU35, EU39, EU41 |

### Efeitos em relação à amostra do G1-PREP

| Mudança | Efeito |
|---|---|
| Entraram | EU04, EU09, EU11, EU12, EU20, EU21, EU29, EU34, EU35 |
| Saíram | EU02, EU13, EU24, EU25, EU27, EU28, EU30, EU32, EU37 |
| Pares interface/acervo completos | De 0 para 2 (EU08+EU09, EU33+EU34) |
| Registro descontinuado | De 0 para 1 (EU11) |
| Par de corpora acadêmicos | EU35 + EU39 |
| "Intermediação RIT" | De 4 para 1, mais coerente com o papel de enriquecimento dado aos registros setoriais |
| "Processo legislativo" | De 2 para 4, no teto |
| Tipos distintos | De 20 para 18, no mínimo exigido |
| Famílias na reserva | De 10 para 9, no mínimo exigido |
| Em comum com a lista intencional do G0.1 | De 12 para 14 |

### O que a candidata perde

1. **EU02 (CELLAR) saiu.** A amostra mantém três registros do ecossistema EUR-Lex (EU01, EU03, EU04), mas sem o grafo de metadados o confronto mais direto entre R2 e R10 nesse ecossistema fica de fora. Para a finalidade do estudo, é a perda mais relevante. EU02 aparece em S2, S3b, S3c e S4.
2. **"Fiscalização" e "Intermediação RIT" ficam com um registro cada.** A fronteira entre dataset normativo e registro setorial é exercitada por menos casos.
3. **Sem folga em C6 e C8.** Qualquer substituição manual de um registro tende a violar uma das duas.
4. **O par EU35 + EU39 repousa numa relação não verificada.** Se a derivação não existir, o par testa pouco.

## 7. Opções para a decisão da equipe

| Opção | O que é | Observação |
|---|---|---|
| B-1 | Aprovar S3a | Cobre tudo o que o G1-READY pediu para avaliar; perde EU02 |
| B-2 | Declarar também o grupo EU01 + EU02 e sortear de novo com a mesma semente | Recupera o confronto R2 × R10 no ecossistema EUR-Lex. Exige nova avaliação de viabilidade; a declaração do grupo deve ser escrita **antes** de ver o resultado |
| B-3 | Aprovar outro cenário já sorteado (S2, S3b, S3c, S4, S5) | Cada um com seus efeitos, na tabela da seção 5 |
| A | Manter a amostra do G1-PREP (S0) | Pares incompletos; nenhum descontinuado |
| C | Lista intencional do G0.1 | Seleção por agente com acesso a colunas de julgamento |

**Cuidado de método.** Depois de vistas as amostras, escolher o cenário pelo resultado é uma forma de seleção intencional. Não invalida o piloto, cujo objetivo é testar regras e não estimar proporções, mas deve ser declarado: quem aprova registra o cenário escolhido e o motivo. A opção B-2 foi descrita, mas não executada, justamente para não acrescentar mais um sorteio visto de antemão.

## 8. Reprodução

```
python scripts/pilot_a_scenarios.py feasibility
python scripts/pilot_a_scenarios.py select
```

Um cenário isolado, a partir do seu arquivo de grupos:

```
python scripts/select_pilot_a.py --required-groups pilot_a/selection_v2_PROPOSED/S3a_deriv/REQUIRED_GROUPS.json --no-write
```

## 9. Estatuto das afirmações

| Afirmação | Classe |
|---|---|
| Viabilidade dos oito cenários; amostras sorteadas; contagens das tabelas | VERIFIED (execução registrada) |
| Efeitos estruturais sobre C6 e C8 | VERIFIED (limites calculados) |
| Relações supostas em cada grupo obrigatório | PENDING VALIDATION |
| Designação de S3a como candidata; qualquer aprovação | PROPOSED — decisão da equipe |
