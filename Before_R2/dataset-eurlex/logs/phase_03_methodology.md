# Log — Etapa 3: reconstrução metodológica, codebook e strings

**Data de execução:** 2026-09-07  
**Estado anterior:** `corpus_locked`  
**Estado posterior:** `methodology_locked`

## Dependências e fontes

- Corpus canônico confirmado: `02_corpus/act.md`
- Hash do corpus confirmado: `B24A02EA241CA631B606660BB48BB5A2222B29F849C4E4552FB99F871B2E8FD4`
- A metodologia foi reconstruída a partir de material metodológico histórico autorizado em `Arquitetura de trabalho/Prompts/G1`, `G2` e `Geral`.
- O desenho histórico que descrevia três atos não foi usado como autoridade de desenho; o caso único e o `config` atual permaneceram soberanos.
- Nenhuma codificação, tabela, resposta de LLM, classificação ou decisão empírica anterior foi importada.

## Produtos criados

- `methodology/codebook.md`
- `methodology/strings.yaml`
- `methodology/coding_schema.json`
- `methodology/methodology_manifest.yaml`

## Conteúdo metodológico

- O codebook trata intermediação como constructo relacional R–I–T.
- Papéis são definidos por relação, não como identidades permanentes.
- O teste de cinco condições exige regulador, alvo, terceiro distinto, função mediadora e evidência suficiente.
- Reporting direto, aconselhamento, participação e menção lexical não são convertidos automaticamente em intermediação.
- Ator, mecanismo, instrumento e procedimento permanecem distintos.
- Observabilidade usa `DIRECT`, `INFERRED`, `EXTERNAL` e `NOT_OBSERVABLE`.
- A abstenção é válida e não pode ser convertida em evidência positiva.
- Strings servem somente para screening de saliência e não para decisão substantiva.

## Hashes dos produtos

- `codebook.md`: `5527F9ECC7575A831F3D90CA14CAA8DFE4DFC1A65641C1B9C1236338625E2B1C`
- `strings.yaml`: `4130425FCFA06E6F9705B76EC477EA1B9EEA29BBD21647981C689D4E09ACD318`
- `coding_schema.json`: `C35EA63563239DDB0EE11331D4C84E3BA49BD21B753F8AEBB62526A61949A326`

## Testes abstratos e validação

- JSON Schema parseado com sucesso.
- Todos os campos mínimos da Etapa 3 estão presentes.
- 20 strings possuem `string_id`, `pattern`, `semantic_role`, `mechanism_family`, `confidence`, `exclusion_pattern` e `notes`.
- Exemplos abstratos TEST-01 a TEST-04 foram usados apenas para testar as regras decisórias.
- Os testes de decisão para caso positivo, relação direta sem intermediário e evidência insuficiente passaram.
- Nenhum exemplo contém CELEX, excerto ou observação do ato selecionado.
- O hash do corpus permaneceu inalterado.

## Lock

`methodology_manifest.yaml` registra `methodology_locked: true`. A Etapa 4 poderá usar os produtos bloqueados para construir o benchmark, mas não poderá alterá-los silenciosamente.
