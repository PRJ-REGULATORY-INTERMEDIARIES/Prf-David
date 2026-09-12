# Registro da Etapa 4 — benchmark de referência

**Data:** 2026-09-07  
**Projeto:** `dataset-eurlex`  
**Etapa:** 4 — construção automática do benchmark e revisão humana mínima  
**Estado ao final:** `awaiting_reference_adjudication`

## 1. Pré-condições e escopo

As pré-condições estavam satisfeitas: `project.status` era `methodology_locked`, o corpus estava bloqueado e `experiment.status` era `not_started`.

A execução utilizou exclusivamente:

- `02_corpus/act.md` como corpus textual canônico;
- `methodology/v1.1.0/codebook.md` e `methodology/v1.1.0/strings.yaml` como regras metodológicas;
- `methodology/v1.1.0/reference_coding_schema.json` para validar R1, R2 e RA.

O `methodology/v1.1.0/experimental_output_schema.json` não foi utilizado na construção, codificação ou validação de R1/R2/RA.

Hashes de entrada:

- corpus canônico `02_corpus/act.md`: `B24A02EA241CA631B606660BB48BB5A2222B29F849C4E4552FB99F871B2E8FD4`;
- schema de referência v1.1.0: `ABBC4325A5E749CF31836FB24314C27ED22061D6E6539FB435FCE8236D5AD2EC`;
- codebook v1.1.0: `C160E153907A786C04070CB09F6E9BAA11DE709A4432A5F89EBE375A8A7EB472`;
- strings v1.1.0: `242C288DB010320619A0CDB58C38CB73C6BE8AA499497CCFAE7BFBFC33F34305`.

## 2. Universo candidato

Foram executados os dois canais independentes e complementares:

1. `lexical screening`, aplicando todas as strings genéricas da metodologia e registrando ocorrência, localização, contexto, string e categoria;
2. `structural reading`, percorrendo unidades por recital, artigo, parágrafo e ponto e preservando candidatos sem lexical hit.

O universo deduplicado contém **106 candidatos**:

| Origem | Quantidade |
|---|---:|
| `both` | 60 |
| `structural` | 42 |
| `lexical` | 4 |
| **total** | **106** |

Foram registradas **130 ocorrências lexicais**. A origem foi calculada após a união dos canais, sem descartar a proveniência.

## 3. Codificações e adjudicação automática

Foram geradas duas passagens independentes sobre o mesmo universo, sem que R1 recebesse R2 ou que R2 recebesse R1:

- `03_human/reference_R1.json`;
- `03_human/reference_R2.json`.

Os registros são objetos individuais conformes ao `reference_coding_schema.json`. O schema mantém `T` como ator/classe de atores/papel institucional; atividades, informação, produtos, processos, condutas e estados de conformidade foram tratados como `object`.

Resultados R1 × R2:

- acordos: **72**;
- divergências: **34**;
- divergências de inclusão/exclusão, categoria ou atributos: registradas em `reference_comparison.csv`.

A adjudicação automática RA foi produzida com as decisões R1/R2 anonimizadas como A/B e o texto localizado do corpus. Relações diretas sem intermediário foram preservadas como negativas/diretas quando sustentadas; ausência de papel, alvo ou suporte textual foi mantida como `insufficient_evidence`. Nenhum caso foi convertido em positivo para completar a tríade.

Arquivo: `03_human/reference_auto_adjudication.json`.

Distribuição de RA:

- `negative`: 16;
- `insufficient_evidence`: 90;
- `positive`: 0;
- `conditional`: 0.

## 4. Pacote mínimo de revisão humana

O pacote está pronto em:

- `03_human/HUMAN_REVIEW_REQUIRED.md`;
- `03_human/human_review.csv`.

Contém **51 itens**:

- 34 divergências R1/R2;
- 46 casos de baixa confiança de RA, com deduplicação entre critérios;
- 8 itens de auditoria, correspondentes a aproximadamente 10% dos acordos, respeitando o mínimo de 3.

Cada item contém ID, localização, excerto, origem, decisões R1/R2/RA, confiança, fundamento, recomendação e campos para `PESQUISADOR: APPROVE / CHANGE`, correção e nota.

O gate humano não foi executado. A referência não está bloqueada.

## 5. Crosswalk e parada

`03_human/reference_experimental_crosswalk.md` foi criado para documentar a comparação futura sem executar métricas ou acessar outputs experimentais.

Não foram executadas a Etapa 5, a human adjudication, G0, G1, G2, comparação ou relatório. Os prompts experimentais e `05_runs/` permanecem intocados.

O estado foi atualizado para:

- `project.status: awaiting_reference_adjudication`;
- `experiment.status: awaiting_reference_adjudication`;
- `reference.locked: false`;
- `human_reference.completed: false`.

**PARE.** A próxima ação válida depende da revisão humana do pacote mínimo.
