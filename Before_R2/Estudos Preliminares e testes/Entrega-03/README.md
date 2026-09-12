# Entrega-03 — Camada de codificação assistida por IA (v4)

Esta pasta **não substitui** `../Entrega-02/`. `Entrega-02/` continua sendo
a entrega corrente do exercício de codificação humana (Stages A/B/C, v3) —
os arquivos `candidate_adjudications_v3.csv` e `rit_relationships_v3.csv`
lá dentro são a fonte de verdade e não são tocados por nada nesta pasta.

`Entrega-03/` é um experimento aditivo: incorpora um LLM como codificador
interpretativo formalmente parte do protocolo (autorizado explicitamente
por David), estruturalmente obrigado a seguir o mesmo teste relacional de
cinco condições já validado em `RIT_CODEBOOK_v3.md` — nunca como
substituto dele.

## Regra estrutural mais importante desta pasta
**Nada em `data/*.jsonl` é copiado ou fundido automaticamente nos CSVs
humanos de `Entrega-02/`.** A única forma de uma linha gerada por IA virar
dado humano é Igor revisar o registro em `data/human_review_queue_v1.csv`
e, se aceitar, escrever ele mesmo a linha em
`Entrega-02/data/candidate_adjudications_v3.csv` ou `rit_relationships_v3.csv`,
com seu próprio `coder`/`coding_date`, mais as colunas `ai_assisted`/
`ai_run_ref` (ver `AI_CODING_PROTOCOL.md`).

## Ordem de leitura
1. `AI_CODING_PROTOCOL.md` — papel da IA, limites, guardrails.
2. `MODEL_SELECTION_PROTOCOL.md` — como o modelo é escolhido (escrito antes
   de qualquer execução).
3. `MODEL_SELECTION_RESULTS.md` — preenchido só depois do Tier 1 rodar.
4. `CHANGELOG_v4.md` — o que esta rodada adiciona.

## Conteúdo
- `reference/` — cópias somente-leitura do que `Entrega-02/` já validou
  (codebook, dicionário de dados, os CSVs humanos, o HTML bruto já
  coletado — sem nova coleta de rede).
- `schemas/` — JSON Schemas (Structured Outputs) por estágio.
- `prompts/` — templates de prompt de sistema/usuário por estágio, mais o
  bloco de guardrails compartilhado.
- `scripts/` — pipeline reprodutível (montagem de contexto, adaptador de
  modelo, execução por estágio, checagem de autoconsistência, laço de
  pedido de contexto adicional, orquestrador do experimento de seleção de
  modelo).
- `data/` — saída das execuções de IA (vazio até a primeira execução real).

## Status atual
**Nenhuma chamada real à API foi feita ainda.** Esta pasta contém o design
completo (protocolos, schemas, prompts, scripts) pronto para uso, mas a
execução do Tier 0 requer confirmação explícita do usuário de que o
`model` id e o preço atual da OpenAI foram checados no próprio painel —
ver `MODEL_SELECTION_PROTOCOL.md`, seção de pré-requisitos.
