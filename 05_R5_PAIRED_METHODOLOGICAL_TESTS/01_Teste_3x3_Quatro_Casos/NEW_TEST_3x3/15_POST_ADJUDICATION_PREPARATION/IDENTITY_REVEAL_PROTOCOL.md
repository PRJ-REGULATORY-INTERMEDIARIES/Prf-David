# Protocolo estrito de revelação de identidade

## Pré-condições cumulativas

1. Registrar o SHA-256 do arquivo de adjudicação no registro de freeze.
2. Obter gate de completude aprovado pelo validador estrutural.
3. Confirmar que não existem campos obrigatórios em branco.
4. Registrar timestamp de conclusão do freeze em ISO 8601 com fuso horário.

## Revelação controlada

5. Somente após as pré-condições, abrir a chave de identidade A/B.
6. Criar um novo arquivo de linkage a partir de `POST_REVEAL_LINKAGE_TEMPLATE.csv`; preservar o arquivo de adjudicação como somente leitura.
7. Registrar no linkage o timestamp de reveal e a referência ao hash congelado, sem reescrever a decisão humana.

## Irreversibilidade metodológica

Após o reveal, decisões, confiança, justificativas, reviewer e datas da adjudicação humana não podem ser alterados. Qualquer correção administrativa posterior exige novo artefato versionado, justificativa e preservação imutável do original; não pode substituir silenciosamente a adjudicação congelada.
