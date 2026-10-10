# Log — Etapa 2: normalização e congelamento do corpus

**Data de execução:** 2026-09-07  
**Estado anterior:** `source_acquired`  
**Estado posterior:** `corpus_locked`

## Entrada

- Fonte exclusiva: `01_source/act_official.xhtml`
- CELEX: `32021R1119`
- Hash da fonte: `8BBE15AF032AF1A3950CF1E42BEAD62E0C816AFBF56DCED883ECECB604DA6075`

## Produtos

- `02_corpus/act.md`
- `02_corpus/act_numbered.md`
- `02_corpus/corpus_manifest.yaml`

## Normalização

Foi aplicada normalização estrutural, sem tradução, resumo, paráfrase, seleção de relevância ou codificação. Foram preservados o título, o preâmbulo, 40 recitals, os 14 artigos, parágrafos, alíneas, disposições inseridas/amendments e a ordem da fonte. O ato selecionado não contém anexos próprios.

`act.md` contém somente o texto normativo normalizado e marcação estrutural. Não foram inseridas categorias analíticas, strings, relações regulatórias ou conhecimento metodológico.

## Integridade e lock

- Tamanho de `act.md`: 64.928 bytes
- Palavras aproximadas: 9.803
- Hash SHA-256 de `act.md`: `B24A02EA241CA631B606660BB48BB5A2222B29F849C4E4552FB99F871B2E8FD4`
- Hash SHA-256 de `act_numbered.md`: `0EB336AEA6C8FF19AF3B6536F3E9029A2E9AF68CA763E962429A8A3DACBB49ED`
- `corpus_manifest.yaml: locked: true`

## Validação

- artigos 1–14 presentes e em ordem;
- recitals 1–40 presentes e em ordem;
- título, preâmbulo e cláusula de adoção presentes;
- XHTML de origem parseado com sucesso;
- nenhum artefato de Etapa 3, benchmark, run ou comparação criado;
- nenhuma condição G0/G1/G2 executada.

A Etapa 3 não foi iniciada.
