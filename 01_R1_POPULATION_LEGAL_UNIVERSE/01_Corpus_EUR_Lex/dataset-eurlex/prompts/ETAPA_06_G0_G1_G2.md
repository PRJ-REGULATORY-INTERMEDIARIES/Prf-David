# ETAPA 6 — PREPARAÇÃO E EXECUÇÃO DE G0, G1 E G2

Trabalhe exclusivamente em `Prf-David/dataset-eurlex/`.

## Pré-condições

Confirmar:

- corpus bloqueado;
- metodologia bloqueada;
- referência bloqueada;
- benchmark inacessível às condições experimentais.

## Desenho

- 1 documento;
- 3 condições;
- 1 execução independente por condição;
- 3 runs no total.

Usar:

- mesmo modelo;
- mesmo nível de reasoning;
- mesmo `02_corpus/act.md`;
- mesmo formato de saída;
- contextos independentes;
- ausência de memória compartilhada.

A diferença substantiva entre condições deve ser apenas o nível de orientação.

## G0 — geral

Recebe:

- tarefa mínima;
- corpus;
- schema mínimo para saída.

Não recebe:

- codebook completo;
- strings;
- contextualização temática especializada.

## G1 — metodológico

Recebe:

- tarefa;
- corpus;
- codebook;
- inclusão/exclusão;
- schema.

Não recebe contextualização substantiva adicional específica de clima.

## G2 — metodológico + substantivo

Recebe tudo de G1 mais uma camada de orientação substantiva pertinente ao domínio climático/regulatório.

Essa camada não pode revelar o benchmark.

## Prompts

Preencher:

- `04_prompts/G0.md`
- `04_prompts/G1.md`
- `04_prompts/G2.md`

Criar:

`04_prompts/prompt_manifest.yaml`

Registrar hashes e diferenças entre condições.

## Auditoria de contaminação

Verificar automaticamente que os prompts não contêm:

- decisões do benchmark;
- R1/R2/RA;
- julgamentos humanos;
- resultados de outra condição.

## Modelo

Usar o modelo e reasoning definidos em `config/experiment.yaml`.

Se qualquer campo essencial estiver `null`, não escolher silenciosamente. Informar o bloqueio ao pesquisador.

## Execução

Executar G0, G1 e G2 em contextos independentes.

Salvar para cada condição:

- `05_runs/<G>/raw_response.*`
- `05_runs/<G>/coding.json`
- metadados da execução.

Registrar:

- modelo;
- reasoning;
- timestamp;
- hash do corpus;
- hash do prompt;
- status;
- tokens, se disponíveis;
- falhas/retries.

Não repetir uma execução por qualidade aparente.

Retry somente por falha técnica objetiva.

## Parsing

Correções estritamente sintáticas são permitidas.

Guardar sempre a resposta bruta original.

## Status

Atualizar:

`experiment.status: runs_complete`

Criar `logs/phase_06_runs.md`.

PARE.
