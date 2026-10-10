# Plano de execução isolada — `stage4_attempt_02`

1. Abrir um contexto/agente limpo para R1 com `R1_coding_input.json`, `02_corpus/act.md`, `methodology/v1.1.0/codebook.md` e `reference_coding_schema.json`. `strings.yaml` não é uma entrada autorizada.
2. Preservar o output bruto de R1 como `R1_output.json` antes de qualquer validação ou normalização.
3. Encerrar o contexto R1. Não compartilhar seu output com R2.
4. Abrir outro contexto/agente limpo para R2 com `R2_coding_input.json`, `02_corpus/act.md`, `methodology/v1.1.0/codebook.md` e `reference_coding_schema.json`. `strings.yaml` não é uma entrada autorizada.
5. Preservar o output bruto de R2 como `R2_output.json` antes de qualquer validação ou normalização.
6. Somente depois abrir um terceiro contexto RA, recebendo R1 e R2 anonimizados como A/B, o corpus canônico, o codebook e o schema de referência. `strings.yaml` continua proibido.
7. Validar logicamente cada registro antes de preparar o pacote humano.

Nenhum desses passos foi executado nesta preparação. Não iniciar o human gate nem a Etapa 5.
