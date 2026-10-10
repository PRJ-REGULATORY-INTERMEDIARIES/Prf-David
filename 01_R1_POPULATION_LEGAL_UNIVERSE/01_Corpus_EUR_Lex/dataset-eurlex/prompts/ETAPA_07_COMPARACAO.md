# ETAPA 7 — COMPARAÇÃO AUTOMÁTICA E ANÁLISE DOS RESULTADOS

Trabalhe exclusivamente em `Prf-David/dataset-eurlex/`.

## Referência

Usar:

`03_human/reference_benchmark.json`

Comparar:

- G0 × benchmark;
- G1 × benchmark;
- G2 × benchmark.

## Matching

Construir correspondência transparente usando:

- localização;
- artigo;
- parágrafo;
- sobreposição textual;
- conteúdo semântico apenas quando necessário.

Não forçar correspondências duvidosas.

## Métricas

Quando aplicáveis, calcular:

- TP;
- FP;
- FN;
- precision;
- recall;
- F1;
- acurácia de classificação entre positivos;
- concordância de categoria;
- concordância de atributos.

Não produzir inferência estatística indevida.

## Taxonomia de erros

Classificar, quando aplicável:

- omission;
- over-inclusion;
- boundary error;
- category error;
- actor error;
- target error;
- instrument error;
- evidence error;
- hallucination;
- unsupported inference.

Adaptar ao codebook quando necessário.

## Comparação incremental

Analisar:

- o que G1 corrige em G0;
- o que G2 corrige em G1;
- onde orientação adicional não ajuda;
- onde orientação adicional piora;
- possíveis sinais de overcoding.

## Produtos

Criar:

- `06_comparison/comparison.csv`
- `06_comparison/metrics.csv`
- `06_comparison/error_taxonomy.csv`
- `06_comparison/comparison.md`

## Interpretação

Tratar os resultados como:

- piloto;
- demonstração metodológica;
- estudo exploratório de caso único.

## Status

Atualizar:

`experiment.status: analyzed`

Criar `logs/phase_07_analysis.md`.

Não solicitar revisão humana adicional, salvo erro técnico incontornável.

PARE.
