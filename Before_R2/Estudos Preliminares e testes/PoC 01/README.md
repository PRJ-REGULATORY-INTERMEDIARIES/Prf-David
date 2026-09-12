# PoC 01 — Produto final: codificação de intermediários regulatórios

Pacote completo do exercício de codificação de intermediários regulatórios
na legislação da UE sobre transição verde (proposta do Prof. David
Levi-Faur). Contém tudo que existe hoje, validado ou não — ver a divisão
abaixo.

## `Entrega-02/` — codificação humana v3 (validada)

O produto principal, pronto para uso e leitura:

- **`ARTIGO_VALIDACAO.qmd` / `.docx`** — o trabalho em formato de artigo
  acadêmico (Resumo → Introdução → Método → Resultados → Validação →
  Discussão → Conclusão), com figuras e tabelas. Ponto de entrada
  recomendado.
- **`RELATORIO_FINAL_APRESENTACAO.qmd` / `.docx`** — relatório de
  apresentação passo a passo do exercício, mais longo e didático.
- **`RESEARCH_NOTE_v3.md` / `.docx`** — nota curta, em inglês, pronta para
  enviar ao Prof. Levi-Faur.
- **Codebooks e documentação metodológica**: `RIT_CODEBOOK_v3.md`,
  `SCREENING_CODEBOOK_v3.md`, `DATA_DICTIONARY_v3.md`, `VARIABLE_MAP_v3.md`,
  `METHODOLOGY_v3.md`, `SCREENING_VALIDATION_v3.md`,
  `RELATIONSHIP_VALIDATION_PROTOCOL_v3.md`, `CHANGELOG_v3.md`.
- **`scripts/`** — pipeline reprodutível (`collect.py`, `screening_v3.py`).
- **`data/`** — os 3 datasets do pipeline (`screening_hits_v3.csv` — 1.079
  linhas; `candidate_adjudications_v3.csv` — 10 candidatos; e
  `rit_relationships_v3.csv` — 7 relações R-I-T) mais `actors_v3.csv`.
- **`figures/`** — as 4 figuras usadas nos documentos acima.

## `Entrega-03/` — camada de codificação assistida por IA (protocolo pronto, ainda não executado)

Design completo (protocolos, JSON Schemas, prompts, scripts de
orquestração) para incorporar um LLM como codificador interpretativo
assistido, testado de ponta a ponta em modo `dry_run` (sem chamada real à
API, sem custo). **Nenhum resultado real existe ainda** — ver
`Entrega-03/CHANGELOG_v4.md` e `Entrega-03/MODEL_SELECTION_PROTOCOL.md`
para os pré-requisitos antes de rodar de verdade (confirmar `model` id e
preço atual no painel da OpenAI).

## O que fica de fora deste pacote, de propósito

- **`../v1/`** — versões anteriores (v1/v2) do exercício, superadas,
  mantidas só para histórico em `Prf-David/v1/`, não copiadas aqui.
- **`../Inputs/`** — materiais de origem do próprio Prof. David (a
  proposta dele em `.docx` e o flyer do WhatsApp com contato pessoal) —
  não fazem parte do produto que você produziu, então não estão neste
  pacote.

## Nota sobre caminhos relativos
`Entrega-02/` e `Entrega-03/` precisam continuar como pastas irmãs dentro
deste mesmo diretório — os scripts e a documentação de `Entrega-03/`
referenciam `../Entrega-02/...` internamente. Não mova uma sem a outra.
