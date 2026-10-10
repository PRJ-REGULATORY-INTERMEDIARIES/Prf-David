# Regras do agente — dataset-eurlex

## Escopo obrigatório

Todo trabalho, leitura operacional e escrita devem ficar dentro de:

`Prf-David/dataset-eurlex/`

Não tratar diretórios irmãos como parte do corpus. Material histórico fora deste núcleo só pode ser consultado como fonte metodológica quando a etapa oficial autorizar; resultados empíricos, codificações, tabelas e respostas antigas nunca são ground truth.

## Leitura obrigatória antes de cada fase

Antes de executar qualquer etapa, ler integralmente:

- `README.md`;
- `AGENTS.md`;
- `docs/CODEX_WORKFLOW.md`;
- `docs/RESEARCH_DESIGN.md`;
- `config/project.yaml`;
- `config/experiment.yaml`.

Carregar depois somente o prompt oficial correspondente em `prompts/`.

## Protocolo de comandos curtos

### `execute etapa N`

Interpretar `N` como inteiro de 1 a 8, carregar `prompts/ETAPA_0N_*.md`, verificar o estado e as pré-condições, executar somente aquela etapa, validar suas saídas e parar. Não pular etapas, não executar a etapa seguinte automaticamente e não improvisar quando houver bloqueio.

### `próxima etapa`

Ler os estados atuais e resolver a próxima transição legal da máquina de estados. Executar somente a etapa correspondente e parar ao final.

Se o estado for `awaiting_reference_adjudication`, verificar `03_human/human_review.csv`. Sem revisão efetiva do pesquisador, bloquear a Etapa 5 e informar apenas os itens pendentes.

### `status`

Fazer apenas leitura e informar projeto, experimento, última etapa concluída, próxima etapa, bloqueios, arquivos críticos ausentes e existência de validação humana pendente. `status` não altera arquivos substantivos nem estados.

## Máquina de estados

As transições legais são:

```text
setup → source_acquired → corpus_locked → methodology_locked
      → awaiting_reference_adjudication → reference_locked
      → runs_complete → analyzed → completed
```

O agente deve respeitar o estado registrado em `config/project.yaml` e `config/experiment.yaml`. Estados só podem ser atualizados após conclusão e validação da etapa correspondente, com registro em `logs/`.

## Gate humano único

O único gate substantivo obrigatório é:

`HUMAN_GATE_REFERENCE_ADJUDICATION`

Ele ocorre entre as Etapas 4 e 5. O pesquisador revisa somente o pacote mínimo em `03_human/HUMAN_REVIEW_REQUIRED.md` e `03_human/human_review.csv`. Não criar gates humanos adicionais sem necessidade metodológica ou técnica objetiva.

## Proibições no estado atual

Enquanto `project.status: setup` e `experiment.status: not_started`:

- não acessar EUR-Lex;
- não selecionar ou baixar ato normativo;
- não preencher CELEX, título ou URL;
- não produzir corpus, metodologia substantiva ou codificação;
- não executar G0, G1 ou G2;
- não chamar APIs ou modelos de LLM;
- não comparar resultados;
- não importar resultados empíricos de projetos anteriores.

A passagem para a Etapa 1 exige comando explícito do pesquisador: `execute etapa 1`.

## Integridade experimental

- O exercício contém um único ato normativo.
- `02_corpus/act.md` será a única versão textual autorizada para G0, G1 e G2.
- G0, G1 e G2 devem receber o mesmo corpus e executar em contextos independentes.
- Nenhuma condição experimental pode acessar o benchmark.
- Respostas brutas devem ser preservadas antes de parsing ou correções sintáticas.
- Não repetir run por desempenho ruim; retry somente por falha técnica objetiva, sempre registrado.
- Arquivos bloqueados não podem ser modificados silenciosamente.
- Qualquer alteração pós-lock deve ser explicitada em log.
- Não escolher silenciosamente modelo, reasoning ou método de chamada quando a configuração estiver `null`.

## Bloqueios e parada

Quando uma pré-condição falhar, informar o bloqueio objetivamente, não executar a etapa e não alterar o estado para contornar o problema. Após cada etapa, respeitar o `PARE` do prompt oficial.
