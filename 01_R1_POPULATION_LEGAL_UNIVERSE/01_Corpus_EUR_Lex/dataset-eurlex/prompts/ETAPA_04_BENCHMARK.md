# ETAPA 4 — CONSTRUÇÃO AUTOMÁTICA DO BENCHMARK E REVISÃO HUMANA MÍNIMA

Trabalhe exclusivamente em `Prf-David/dataset-eurlex/`.

Leia:

- `02_corpus/act.md`
- `methodology/codebook.md`
- `methodology/strings.yaml`
- `methodology/coding_schema.json`

## Objetivo

Construir um **benchmark de referência adjudicado pelo pesquisador**, minimizando a carga humana.

Não utilizar a expressão `gold standard humano`.

## 1. Screening lexical

Aplicar todas as strings ao corpus e registrar:

- ocorrência;
- localização;
- contexto;
- string;
- categoria indicativa.

## 2. Cobertura estrutural

Executar leitura sistemática por artigo/parágrafo para identificar candidatos sem correspondência lexical.

## 3. Universo candidato

Criar:

`03_human/candidate_universe.csv`

Cada candidato deve possuir ID estável.

## 4. Codificações independentes

Produzir duas codificações independentes:

- R1
- R2

Ambas recebem o mesmo corpus, codebook e schema.

R1 não acessa R2.

R2 não acessa R1.

Nenhuma acessa resultados G0/G1/G2.

Salvar:

- `03_human/reference_R1.json`
- `03_human/reference_R2.json`

## 5. Consolidação

Classificar cada candidato como:

- acordo positivo;
- acordo negativo;
- divergência de inclusão/exclusão;
- divergência de categoria;
- divergência de atributos;
- evidência insuficiente;
- baixa confiança.

## 6. Adjudicação automática RA

Para divergências, executar uma terceira análise independente.

Apresentar R1 e R2 anonimamente como A e B.

RA decide com base apenas no texto e codebook.

Salvar:

`03_human/reference_auto_adjudication.json`

## 7. Pacote humano mínimo

Criar:

- `03_human/HUMAN_REVIEW_REQUIRED.md`
- `03_human/human_review.csv`

Incluir somente:

1. divergências não resolvidas com alta confiança;
2. casos de baixa confiança de RA;
3. casos conceitualmente importantes;
4. casos que alterem significativamente contagem/tipologia;
5. auditoria aleatória de aproximadamente 10% dos acordos, com mínimo de 3 casos quando possível.

Cada item deve mostrar:

- ID;
- localização;
- excerto;
- decisão R1;
- decisão R2;
- decisão RA;
- fundamento;
- decisão recomendada;
- `PESQUISADOR: APPROVE / CHANGE`;
- campo para correção.

## 8. Minimização

Se R1, R2 e RA convergirem com alta confiança, não enviar o caso ao pesquisador, exceto na amostra de auditoria.

## 9. Status

Atualizar:

- `project.status: awaiting_reference_adjudication`
- `experiment.status: awaiting_reference_adjudication`

## 10. Saída ao pesquisador

Informar apenas:

- número de candidatos;
- concordância R1/R2;
- número de itens para revisão;
- localização dos dois arquivos de revisão.

PARE obrigatoriamente.

Não executar G0, G1 ou G2.
