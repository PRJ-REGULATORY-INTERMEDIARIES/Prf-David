# CODEX WORKFLOW — dataset-eurlex

## Finalidade

Este documento define o fluxo operacional do projeto `dataset-eurlex` para que o Codex possa executar as fases por comandos curtos do pesquisador, preservando rastreabilidade, integridade experimental e pontos mínimos de validação humana.

## Comandos aceitos

O agente deve reconhecer, no mínimo, os seguintes comandos do pesquisador:

- `execute etapa 1`
- `execute etapa 2`
- `execute etapa 3`
- `execute etapa 4`
- `execute etapa 5`
- `execute etapa 6`
- `execute etapa 7`
- `execute etapa 8`
- `próxima etapa`
- `status`

O agente não deve exigir que o pesquisador cole novamente o prompt completo da etapa. O prompt oficial deve ser carregado do diretório `prompts/`.

## Mapa das etapas

| Etapa | Prompt oficial | Status esperado ao final |
|---|---|---|
| 1 | `prompts/ETAPA_01_FONTE.md` | `source_acquired` |
| 2 | `prompts/ETAPA_02_CORPUS.md` | `corpus_locked` |
| 3 | `prompts/ETAPA_03_METODOLOGIA.md` | `methodology_locked` |
| 4 | `prompts/ETAPA_04_BENCHMARK.md` | `awaiting_reference_adjudication` |
| 5 | `prompts/ETAPA_05_REFERENCE_LOCK.md` | `reference_locked` |
| 6 | `prompts/ETAPA_06_G0_G1_G2.md` | `runs_complete` |
| 7 | `prompts/ETAPA_07_COMPARACAO.md` | `analyzed` |
| 8 | `prompts/ETAPA_08_RELATORIO.md` | `completed` |

## Máquina de estados

Fluxo normal:

```text
setup
  ↓
source_acquired
  ↓
corpus_locked
  ↓
methodology_locked
  ↓
awaiting_reference_adjudication
  ↓
reference_locked
  ↓
runs_complete
  ↓
analyzed
  ↓
completed
```

O agente deve ler `config/project.yaml` e `config/experiment.yaml` antes de decidir qual etapa é legalmente executável.

## Comando `execute etapa N`

Ao receber `execute etapa N`:

1. ler `README.md`;
2. ler `AGENTS.md`;
3. ler `docs/CODEX_WORKFLOW.md`;
4. ler `config/project.yaml`;
5. ler `config/experiment.yaml`;
6. abrir o prompt oficial correspondente à etapa;
7. verificar pré-condições;
8. executar integralmente a etapa;
9. validar os arquivos produzidos;
10. atualizar status e logs apenas se a etapa tiver sido concluída com sucesso;
11. parar ao final da etapa, salvo instrução explícita em contrário.

Se a etapa solicitada não puder ser executada porque uma pré-condição não foi atendida, não improvisar. Informar objetivamente o bloqueio.

## Comando `próxima etapa`

Ao receber `próxima etapa`:

1. identificar o status atual;
2. determinar a próxima etapa legal;
3. carregar automaticamente o prompt oficial correspondente;
4. executar a etapa.

Exceção obrigatória:

Se o status for `awaiting_reference_adjudication`, verificar se `03_human/human_review.csv` foi efetivamente revisado pelo pesquisador. Se a revisão não estiver concluída, não executar a Etapa 5. Informar apenas quais itens ainda exigem decisão.

## Comando `status`

Ao receber `status`, não executar análise substantiva. Informar:

- status do projeto;
- status do experimento;
- última etapa concluída;
- próxima etapa disponível;
- bloqueios;
- arquivos críticos presentes/ausentes;
- se há validação humana pendente.

## Validação humana mínima

Existe apenas um gate substantivo obrigatório:

`HUMAN_GATE_REFERENCE_ADJUDICATION`

Ele ocorre entre as Etapas 4 e 5.

O pesquisador não precisa recodificar integralmente o ato. Ele deve revisar apenas o pacote produzido em:

- `03_human/HUMAN_REVIEW_REQUIRED.md`
- `03_human/human_review.csv`

O agente deve minimizar esse pacote conforme as regras da Etapa 4.

## Regras de integridade

1. Um único ato normativo compõe o exercício.
2. O corpus bloqueado em `02_corpus/act.md` deve ser idêntico para G0, G1 e G2.
3. G0, G1 e G2 devem ser execuções independentes.
4. Nenhum agente experimental pode acessar o benchmark.
5. Resultados antigos de outros diretórios nunca podem ser usados como ground truth.
6. O agente deve guardar respostas brutas antes de qualquer parsing ou correção estrutural.
7. Não repetir uma execução experimental porque o resultado parece ruim.
8. Retries são permitidos apenas por falha técnica objetiva e devem ser registrados.
9. Arquivos congelados não podem ser alterados silenciosamente.
10. Qualquer alteração pós-lock exige registro explícito em log.

## Estrutura adicional esperada

Além da estrutura inicial, as etapas podem criar:

```text
dataset-eurlex/
├── methodology/
│   ├── codebook.md
│   ├── strings.yaml
│   ├── coding_schema.json
│   └── methodology_manifest.yaml
├── prompts/
│   ├── ETAPA_01_FONTE.md
│   ├── ETAPA_02_CORPUS.md
│   ├── ETAPA_03_METODOLOGIA.md
│   ├── ETAPA_04_BENCHMARK.md
│   ├── ETAPA_05_REFERENCE_LOCK.md
│   ├── ETAPA_06_G0_G1_G2.md
│   ├── ETAPA_07_COMPARACAO.md
│   └── ETAPA_08_RELATORIO.md
└── docs/
    ├── CODEX_WORKFLOW.md
    └── RESEARCH_DESIGN.md
```

## Regra final

O Codex deve operar como executor do protocolo, não como pesquisador livre para alterar o desenho. Mudanças de método, categorias, condições experimentais ou número de atos exigem instrução explícita do pesquisador.
