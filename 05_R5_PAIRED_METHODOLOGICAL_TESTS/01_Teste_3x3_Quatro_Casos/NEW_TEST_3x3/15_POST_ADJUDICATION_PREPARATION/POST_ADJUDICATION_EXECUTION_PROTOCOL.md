# Protocolo de execução pós-adjudicação — Rodada 2

**Estado atual:** preparação técnica apenas. Nenhuma etapa substantiva abaixo foi executada.

## Ordem obrigatória

1. Receber o arquivo de adjudicação humana congelado, mantendo A/B cegos.
2. Verificar a completude estrutural com `HUMAN_ADJUDICATION_VALIDATOR.py`.
3. Gerar o SHA-256 do arquivo adjudicado validado.
4. Registrar e congelar a adjudicação em `ADJUDICATION_FREEZE_TEMPLATE.md`.
5. Somente após o freeze, abrir a chave de identidade A/B conforme `IDENTITY_REVEAL_PROTOCOL.md`.
6. Aplicar as decisões aos registros comparativos, criando o linkage pós-reveal.
7. Recalcular D1–D8 somente onde a adjudicação o exigir e preservar os demais registros congelados.
8. Produzir o vetor de caso `[SUBSTANCE, TRACEABILITY, SENSITIVITY, CALIBRATION, REGRESSION, COST]`.
9. Classificar cada caso em C-A–C-F conforme o preregistro congelado.
10. Executar a replicação climática SCF × CBAM.
11. Executar a análise de transferência AI Act × Directive 86/361/EEC.
12. Produzir a classificação familiar F1–F7.
13. Produzir a síntese final, com linguagem calibrada e sem ranking global.

## Controles de isolamento

- Nenhuma identidade A/B pode ser acessada antes dos itens 1–4 estarem concluídos e registrados.
- Nenhuma decisão humana pode ser modificada após o item 5.
- As etapas 6–13 são futuras e não foram antecipadas nesta preparação.

## Contrato do arquivo de adjudicação futuro

O CSV de entrega deve conter exatamente uma linha por cartão e as colunas: `card_id`, `human_decision`, `human_confidence`, `human_justification`, `reviewer`, `adjudication_date`.

- Decisões permitidas: `SUPPORTED_READING`, `COMPETING_READING`, `UNRESOLVED_UNCERTAINTY`.
- Confiança: número de 1 a 5, inclusive.
- O validador realiza apenas QA estrutural; não interpreta justificativas, evidência ou mérito metodológico.
