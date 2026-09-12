# Registro da atualização da arquitetura

**Data:** 2026-09-07  
**Projeto:** `dataset-eurlex`  
**Tipo:** atualização estrutural e documental  
**Estado mantido:** `project.status: setup`; `experiment.status: not_started`

## Arquivos criados

- `prompts/ETAPA_01_FONTE.md`
- `prompts/ETAPA_02_CORPUS.md`
- `prompts/ETAPA_03_METODOLOGIA.md`
- `prompts/ETAPA_04_BENCHMARK.md`
- `prompts/ETAPA_05_REFERENCE_LOCK.md`
- `prompts/ETAPA_06_G0_G1_G2.md`
- `prompts/ETAPA_07_COMPARACAO.md`
- `prompts/ETAPA_08_RELATORIO.md`
- `docs/CODEX_WORKFLOW.md`
- `docs/RESEARCH_DESIGN.md`
- `methodology/README.md`
- `logs/architecture_update.md`

## Arquivos modificados

- `README.md`
- `AGENTS.md`
- `04_prompts/README.md`
- `config/project.yaml`
- `config/experiment.yaml`

## Validações realizadas

- Os oito prompts oficiais foram instalados em `prompts/`.
- `docs/CODEX_WORKFLOW.md` e `docs/RESEARCH_DESIGN.md` foram instalados.
- `README.md` documenta o fluxo SETUP → Etapas 1–8 e os comandos curtos.
- `AGENTS.md` documenta roteamento, pré-condições, máquina de estados, gate humano único e bloqueios.
- `project.status` permanece `setup`.
- `experiment.status` permanece `not_started`.
- `config/project.yaml` mantém CELEX, título e URL como `null`.
- `config/experiment.yaml` mantém modelo, reasoning e API configuráveis como `null` e define `execution.automated: true`.
- O diretório `methodology/` contém somente um README preparatório.
- O ZIP de bootstrap não foi descompactado nem alterado.

## Testes lógicos sem execução

- `execute etapa 1` resolve para `prompts/ETAPA_01_FONTE.md`.
- `execute etapa 4` resolve para `prompts/ETAPA_04_BENCHMARK.md`.
- Com estado `setup`, `próxima etapa` resolve para a Etapa 1.
- Com estado `awaiting_reference_adjudication`, `próxima etapa` bloqueia a Etapa 5 se `03_human/human_review.csv` não estiver revisado.
- `status` é somente leitura e não altera arquivos substantivos.

## Problemas e limites

Nenhum problema encontrado. Nenhum ato foi selecionado, nenhum resultado foi produzido, G0/G1/G2 não foram executados e nenhum resultado empírico anterior foi importado.
