# HUMAN_GATE_REFERENCE_ADJUDICATION

Este é o pacote mínimo para revisão humana da Etapa 4. Ele não é a referência final nem um `gold standard humano`.

- Universo candidato: 106 unidades.
- Ocorrências lexicais registradas: 130.
- Acordos R1/R2: 72.
- Divergências R1/R2: 34.
- Casos de baixa confiança de RA: 46.
- Amostra de auditoria de acordos: 8.
- Itens enviados ao pesquisador: 51.

## Instrução

Revisar somente as linhas de `human_review.csv`, confrontando o excerto com o corpus canônico `02_corpus/act.md`. Para cada linha, preencher `PESQUISADOR: APPROVE / CHANGE`; quando necessário, registrar a correção e a nota.

A revisão humana não deve consultar outputs G0/G1/G2. A referência permanece desbloqueada até a conclusão do gate.

## Escopo

A construção utilizou somente `02_corpus/act.md`, `methodology/v1.1.0/reference_coding_schema.json`, `strings.yaml` e as regras do codebook vigente. O `experimental_output_schema.json` não foi utilizado na construção de R1, R2 ou RA.
