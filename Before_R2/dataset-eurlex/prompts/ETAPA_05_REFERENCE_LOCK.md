# ETAPA 5 — INCORPORAÇÃO DA REVISÃO HUMANA E CONGELAMENTO DA REFERÊNCIA

Trabalhe exclusivamente em `Prf-David/dataset-eurlex/`.

## Pré-condição obrigatória

Verificar se `03_human/human_review.csv` foi revisado pelo pesquisador.

Se houver item pendente, PARE e informe apenas os itens faltantes.

## Consolidação

Integrar:

- R1;
- R2;
- RA;
- decisões humanas.

A decisão humana prevalece nos itens revisados.

## Produtos

Criar:

- `03_human/reference_benchmark.json`
- `03_human/reference_benchmark.csv`
- `03_human/reference_summary.md`
- `03_human/reference_manifest.yaml`

## Proveniência

Para cada decisão final registrar, quando aplicável:

- R1;
- R2;
- RA;
- revisão humana;
- decisão final;
- localização;
- evidência;
- categoria;
- atributos.

## Resumo

Incluir:

- candidatos;
- positivos;
- negativos;
- concordância R1/R2;
- adjudicados automaticamente;
- revisados pelo pesquisador.

## Lock

Calcular hashes de:

- benchmark;
- corpus;
- codebook;
- schema.

Definir:

`reference_locked: true`

Atualizar:

- `project.status: reference_locked`
- `experiment.status: ready`

Criar `logs/phase_05_reference_lock.md`.

PARE.
