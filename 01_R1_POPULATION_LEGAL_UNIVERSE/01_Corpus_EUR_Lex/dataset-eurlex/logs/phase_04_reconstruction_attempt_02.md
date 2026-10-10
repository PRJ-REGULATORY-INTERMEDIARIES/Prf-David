# Preparação da nova Etapa 4 — `stage4_attempt_02`

**Data:** 2026-09-07  
**Estado:** preparado, não executado  
**Projeto:** `methodology_locked`  
**Experimento:** `not_started`

## Preservação da tentativa anterior

Os outputs da tentativa reprovada foram movidos, sem deleção, para `03_human/stage4_attempt_01/`. A pasta contém os CSVs, R1, R2, RA, comparação, pacote humano, crosswalk, gerador e cópia do log original.

## Nova reconstrução

A nova preparação utilizou somente:

- `02_corpus/act.md`, SHA-256 `B24A02EA241CA631B606660BB48BB5A2222B29F849C4E4552FB99F871B2E8FD4`;
- `methodology/v1.1.0/`, sem alteração;
- `reference_coding_schema.json` como schema previsto para futura validação de R1/R2/RA.

O parser passou a preservar artigo, título do artigo, recital, parágrafo, ponto, linhas, caput/parent paragraph e referências internas a outros artigos. Cada candidata contém `focal_excerpt`, `parent_context` e `same_act_context_refs`, além de `reconstruction_group_id`.

Resultado da reconstrução:

- total: **88**;
- `lexical`: **25**;
- `structural`: **19**;
- `both`: **44**.

Essa reconstrução não preenche R, I, T, ação, objeto, mecanismo, evidência, condições A–E ou resultado. A leitura substantiva será tarefa dos dois contextos independentes.

## Pacotes isolados

Foram preparados:

- `03_human/stage4_attempt_02/R1_coding_input.json`;
- `03_human/stage4_attempt_02/R2_coding_input.json`.

Cada pacote contém exatamente seis campos: `candidate_id`, `candidate_origin`, `source_location`, `focal_excerpt`, `parent_context` e `same_act_context_refs`. R1 e R2 não têm acesso ao output um do outro. RA não foi criado nem iniciado; ocorrerá apenas em terceiro contexto após os dois outputs.

`candidate_transition_audit.csv` documenta a passagem dos 106 candidatos da tentativa 1 para as 88 unidades da tentativa 2: 74 `retained`, 8 `merged`, 24 `excluded_as_fragment/contextual_duplicate` e 6 `newly_reconstructed`. A auditoria usa somente IDs, localizações, excertos e contexto; nenhum campo R/I/T, mecanismo, evidência ou condição anterior foi reutilizado.

## Validação lógica preparada

`validate_reference_logic.py` implementa a regra:

- A–E todas `YES` → `positive`;
- qualquer `NO` estrutural em A–D → `negative`;
- E=`NO` sem NO estrutural → `insufficient_evidence`;
- qualquer `UNCLEAR` restante → `conditional`.

Também rejeita `positive` sem R/I/T, `direct_relationship` com I preenchido e C/D=`YES` sem I. Os testes abstratos passaram.

O futuro pacote humano selecionará automaticamente qualquer caso com `I != null`, C=`YES` ou D=`YES`, além de divergências, baixa confiança e amostra de acordos. O formulário não conterá recomendação automática de aprovação de RA.

As divergências R1/R2 serão comparadas por `substantive_signature`, que inclui `screening_status`, R, I, T, condições A–E, `relational_result`, `primary_mechanism`, ação, objeto e função. Notas, redação, ordem e metadados não gerarão divergência substantiva. Baixa confiança em R1, R2 ou RA sempre acionará revisão humana futura.

## Parada

Não foram executados R1, R2, RA, human gate, Etapa 5, G0 ou G1/G2. O próximo passo requer nova autorização explícita para executar os dois contextos independentes.
