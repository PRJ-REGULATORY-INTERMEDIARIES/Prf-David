# dataset-eurlex

## Objetivo e desenho

`dataset-eurlex` é um piloto metodológico exploratório de caso único para observar como níveis progressivos de orientação alteram a identificação e a codificação de atos/disposições regulatórias por um LLM.

O desenho é fixo: um ato normativo do EUR-Lex, um corpus textual normalizado e bloqueado, três condições experimentais e uma execução independente por condição.

```text
SETUP
  ↓
ETAPA 1 — fonte
  ↓
ETAPA 2 — corpus
  ↓
ETAPA 3 — metodologia
  ↓
ETAPA 4 — benchmark assistido
  ↓
HUMAN GATE ÚNICO
  ↓
ETAPA 5 — reference lock
  ↓
ETAPA 6 — G0 / G1 / G2
  ↓
ETAPA 7 — comparação
  ↓
ETAPA 8 — relatório
```

Há apenas um ato e três execuções no total: G0 (condição geral), G1 (orientação metodológica) e G2 (orientação metodológica mais substantiva sobre regulação climática). A comparação é descritiva; o piloto não sustenta generalização estatística.

## Operação por comandos curtos

O fluxo é controlado pelo pesquisador com comandos como:

- `execute etapa 1` até `execute etapa 8`;
- `próxima etapa`;
- `status`.

Os prompts operacionais oficiais ficam em `prompts/`. O diretório `04_prompts/` é reservado exclusivamente aos prompts experimentais G0/G1/G2, preenchidos somente na Etapa 6.

## Estrutura

```text
01_source/       Fonte oficial e proveniência do ato
02_corpus/       Corpus único normalizado e bloqueado
03_human/        Benchmark de referência e gate de adjudicação
04_prompts/      Prompts experimentais G0, G1 e G2
05_runs/         Respostas brutas das execuções
06_comparison/   Comparações e métricas descritivas
07_report/       Relatório final
methodology/     Produtos metodológicos criados na Etapa 3
prompts/         Instruções operacionais das oito etapas
docs/            Workflow e desenho de pesquisa
config/          Parâmetros e estados do experimento
logs/            Registros de execução e decisões técnicas
```

## Isolamento e integridade

Este núcleo é independente de resultados empíricos anteriores. Material histórico fora de `dataset-eurlex/` pode servir apenas como fonte metodológica, nunca como ground truth. O mesmo `02_corpus/act.md` será usado nas três condições; o benchmark permanecerá inacessível aos agentes experimentais; respostas brutas serão preservadas; e retries só serão permitidos por falha técnica objetiva.

## Estado atual

- `project.status`: `methodology_locked`
- `experiment.status`: `not_started`
- um único ato normativo foi selecionado e preservado em `01_source/`;
- `02_corpus/act.md` é a versão textual canônica e está bloqueada;
- `methodology/v1.1.0/` contém a metodologia vigente bloqueada;
- `03_human/stage4_attempt_01/` preserva integralmente a tentativa de benchmark supersedida;
- `03_human/stage4_attempt_02/` contém a nova reconstrução e os inputs R1/R2 ainda não executados;
- a referência ainda não está bloqueada e nenhuma execução experimental foi produzida;
- nenhum prompt experimental foi definido.

O próximo passo válido depende de autorização explícita para executar R1 e R2 em contextos independentes. Não iniciar o human gate nem a Etapa 5 nesta preparação.

`PARE` até nova autorização de execução.
