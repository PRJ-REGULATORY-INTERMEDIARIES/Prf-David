# ETAPA 3 — RECONSTRUÇÃO METODOLÓGICA, CODEBOOK E STRINGS

Trabalhe exclusivamente em `Prf-David/dataset-eurlex/`.

Confirme que o corpus está bloqueado.

## Objetivo

Reconstruir um protocolo operacional autocontido para identificação e codificação de atos/disposições regulatórias.

## Fonte metodológica

É permitido consultar `Prf-David/Arquitetura de trabalho/` como biblioteca metodológica.

Buscar:

- codebooks;
- definições;
- regras de inclusão/exclusão;
- frameworks;
- notas conceituais;
- strings;
- documentação teórica relacionada à regulação e ao referencial adotado.

Não utilizar:

- codificações empíricas do ato;
- tabelas de resultados;
- respostas anteriores de LLM;
- classificações anteriores.

## Criar diretório

Criar `methodology/` se ainda não existir.

## Produtos

Criar:

- `methodology/codebook.md`
- `methodology/strings.yaml`
- `methodology/coding_schema.json`
- `methodology/methodology_manifest.yaml`

## Codebook

Deve cobrir, quando sustentado pelas fontes:

- unidade de análise;
- conceito operacional;
- inclusão;
- exclusão;
- categorias;
- subcategorias;
- atributos;
- regras decisórias;
- casos limítrofes;
- múltiplos atos na mesma disposição;
- obrigações compostas;
- competências;
- instrumentos;
- atores;
- destinatários;
- evidência mínima;
- localização textual.

Não inventar categorias sem suporte.

## Strings

Organizar padrões indicativos por função regulatória.

Strings servem para screening, não para decisão substantiva final.

## Schema

Incluir, no mínimo, campos equivalentes a:

- `candidate_id`
- `source_location`
- `article`
- `paragraph`
- `excerpt`
- `is_regulatory_act`
- `regulatory_act_type`
- `actor`
- `target`
- `instrument`
- `action`
- `object`
- `evidence`
- `confidence`
- `notes`

Adaptar apenas se o codebook justificar.

## Teste

Testar o codebook apenas com exemplos abstratos criados para teste.

Não ajustar categorias usando respostas empíricas do ato.

## Lock

Registrar hashes e fontes em `methodology_manifest.yaml`.

Definir:

`methodology_locked: true`

Atualizar:

`project.status: methodology_locked`

Criar `logs/phase_03_methodology.md`.

PARE.
