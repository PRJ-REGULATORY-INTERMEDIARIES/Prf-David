# Etapa 4 — `stage4_attempt_02`

Esta é uma nova preparação da Etapa 4 após a reprovação metodológica de `stage4_attempt_01`. A tentativa anterior permanece preservada integralmente em `../stage4_attempt_01/`.

## Estado

- reconstrução de candidatos: preparada;
- R1: input preparado, não executado;
- R2: input preparado, não executado;
- RA: não iniciado;
- human gate: não iniciado;
- Etapa 5: não executada;
- estado operacional: `methodology_locked`.

## Reconstrução

`candidate_reconstruction.json` e `candidate_reconstruction.csv` foram construídos somente a partir de `02_corpus/act.md` e das strings vigentes. Cada unidade preserva:

- `focal_excerpt`;
- `parent_context` com artigo, título, parágrafo e ponto quando disponíveis;
- `same_act_context_refs` para cross-references internas;
- `reconstruction_group_id` para relacionar fragmentos da mesma disposição.
- `candidate_transition_audit.csv` documenta a passagem 106→88 sem reutilizar codificação substantiva.

A seleção estrutural é apenas uma cobertura de reconstrução para preparar a leitura substantiva. Ela não preenche R, I, T, ação, objeto, mecanismo, evidência, condições A–E ou resultado.

## Isolamento

`R1_coding_input.json` e `R2_coding_input.json` contêm exatamente o mesmo conjunto de campos não substantivos. Cada contexto recebe somente seu próprio pacote, o corpus canônico e a metodologia vigente. R1 não recebe arquivos R2; R2 não recebe arquivos R1; `strings.yaml` foi usado somente no screening/reconstrução e não é entrada autorizada de R1, R2 ou RA; RA só poderá existir em terceiro contexto após os dois outputs independentes.

Os manifestos `R1_context_manifest.yaml` e `R2_context_manifest.yaml` registram as proibições de acesso.

## Validação e revisão futura

`validate_reference_logic.py` impede combinações incompatíveis entre A–E e `relational_result`, compara R1/R2 por `substantive_signature` e aciona revisão para baixa confiança em qualquer um de R1, R2 ou RA. O futuro pacote humano deverá incluir automaticamente qualquer caso em que R1, R2 ou RA tenha `I != null`, C=`YES` ou D=`YES`, além de divergências, baixa confiança e amostra aleatória de acordos.

`human_review_template.csv` contém apenas campos de revisão e não recomenda aprovar RA. Ele permanece vazio até que R1, R2 e RA sejam executados em seus contextos próprios.
