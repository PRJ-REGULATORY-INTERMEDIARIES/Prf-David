# RESEARCH DESIGN — dataset-eurlex

## 1. Natureza do exercício

Piloto metodológico exploratório de caso único.

O objetivo é observar como diferentes níveis de instrução fornecidos ao mesmo modelo alteram sua capacidade de identificar e codificar atos/disposições regulatórias em um único ato normativo do EUR-Lex.

O exercício não pretende fornecer inferência estatística nem generalização para todo o universo regulatório europeu.

## 2. Unidade documental

- Número de atos normativos: 1
- Fonte: EUR-Lex
- Foco temático preferencial: regulação climática
- Corpus experimental: uma única versão textual normalizada e bloqueada

## 3. Condições experimentais

### G0 — condição geral

Recebe a tarefa, o corpus e apenas a estrutura mínima de resposta.

Não recebe o codebook completo, strings ou contextualização substantiva especializada.

### G1 — orientação metodológica

Recebe a tarefa, o corpus, o codebook, critérios de inclusão/exclusão e schema.

### G2 — orientação metodológica + substantiva

Recebe tudo de G1 e uma camada adicional de orientação substantiva pertinente ao domínio climático/regulatório.

Nenhuma condição recebe o benchmark de referência.

## 4. Número de execuções

- 1 execução por condição
- 3 execuções no total

As execuções devem ser independentes.

## 5. Benchmark de referência

O benchmark não será denominado `gold standard humano`.

Será tratado como:

**benchmark de referência adjudicado pelo pesquisador**

Sua construção inclui:

1. screening lexical;
2. cobertura estrutural;
3. universo de candidatos;
4. codificação independente R1;
5. codificação independente R2;
6. comparação R1 × R2;
7. adjudicação automática RA dos casos divergentes;
8. revisão humana mínima de divergências relevantes e pequena amostra de auditoria;
9. congelamento da referência.

## 6. Papel humano

O pesquisador entra substantivamente em apenas um gate:

`HUMAN_GATE_REFERENCE_ADJUDICATION`

Sua função é aprovar ou corrigir o subconjunto de decisões apresentado pelo sistema.

Não há obrigação de recodificação humana integral do documento.

## 7. Comparações principais

- G0 × benchmark
- G1 × benchmark
- G2 × benchmark
- comparação incremental G0 → G1 → G2

## 8. Métricas possíveis

Quando aplicáveis:

- true positives;
- false positives;
- false negatives;
- precision;
- recall;
- F1;
- concordância de categoria;
- concordância de atributos;
- taxonomia qualitativa de erros.

Como se trata de um único ato e uma execução por condição, as métricas devem ser interpretadas como descritivas.

## 9. Pergunta analítica

Pergunta principal:

> Como níveis progressivos de orientação metodológica e substantiva alteram a capacidade de um LLM de identificar e codificar atos regulatórios em um ato normativo europeu?

## 10. Limitações assumidas

- caso único;
- apenas uma execução por condição;
- ausência de estimativa de variabilidade inter-run;
- referência parcialmente assistida por IA;
- dependência do modelo e da formulação dos prompts;
- impossibilidade de generalização estatística.

## 11. Escalabilidade futura

Somente após o piloto poderá ser considerada expansão para:

- mais atos;
- mais replicações;
- outros domínios regulatórios;
- outros modelos;
- medidas de estabilidade;
- desenhos de confiabilidade inter-run.
