# ETAPA 2 — NORMALIZAÇÃO E CONGELAMENTO DO CORPUS

Trabalhe exclusivamente em `Prf-David/dataset-eurlex/`.

Leia os documentos de governança e confirme que o status atual é `source_acquired`.

## Objetivo

Transformar o ato oficial em um corpus textual limpo, rastreável e único para todas as condições experimentais.

## Fonte

Use apenas a versão oficial em `01_source/`.

Não acrescente doutrina, resumos, jurisprudência, comentários ou contexto externo.

## Produção

Criar:

- `02_corpus/act.md`
- `02_corpus/act_numbered.md`
- `02_corpus/corpus_manifest.yaml`

Preservar, quando existentes:

- título;
- preâmbulo;
- considerandos;
- capítulos;
- seções;
- artigos;
- parágrafos;
- alíneas;
- anexos relevantes.

## Normalização permitida

Pode remover navegação, scripts, CSS e artefatos técnicos.

Não pode:

- resumir;
- parafrasear;
- traduzir silenciosamente;
- excluir dispositivos;
- reordenar conteúdo;
- alterar redação jurídica.

## Identificadores

Preservar identificadores estruturais estáveis quando possível.

## Manifesto

Registrar no `corpus_manifest.yaml`:

- CELEX;
- fonte;
- arquivos gerados;
- tamanho;
- palavras aproximadas;
- artigos;
- hash SHA-256 de `act.md`;
- transformações;
- data de normalização;
- `locked: true`.

## Validação automática

Verificar:

- artigos ausentes;
- anexos omitidos;
- duplicação;
- truncamento;
- ordem.

Corrigir apenas problemas inequívocos.

## Regra central

Após o lock, `02_corpus/act.md` é a única versão textual autorizada para G0, G1 e G2.

## Status

Atualizar:

`project.status: corpus_locked`

Criar `logs/phase_02_corpus.md`.

PARE.
