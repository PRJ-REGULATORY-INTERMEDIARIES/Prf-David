# V8-COMP-01 — relatório de próximo gate

**Estado após AMENDMENT_002:** `PRIORITY_REALIGNED / NO_SUBSTANTIVE_EXTRACTION`.

## Resultado da auditoria

Foram inventariados 24 instrumentos com evidência local de análise, perfil analítico, proposição de codificação ou extração estrutural. O inventário exclui fontes apenas baixadas sem evidência de trabalho analítico e marca explicitamente os casos em que há corpus mas não observação validada.

A instrução de David desloca a prioridade para casos analisados; não comprova interpretação de “3 and 3”/“2 and 2”. MDR está `ON_HOLD_SOURCE_PENDING`; nenhum arquivo dele foi alterado. A amostra recomendada é 31991L0263 + 32004R0874, sujeita à confirmação da composição e aos gates abaixo.

## Gates

| Gate | Exigência | Estado |
|---|---|---|
| P0 | emenda, resposta e inventário append-only | `COMPLETE` |
| P1 | confirmar com Igor a composição numérica, se necessário; registrar decisão | `OPEN` |
| P2 | para cada caso, obter/conferir e congelar a mesma evidência primária legal, versão, estado e SHA-256 | `NOT_STARTED` |
| P3 | crosswalk explícito: antiga codificação relacional → campos V8, sem transportar conclusões | `NOT_STARTED` |
| P4A | Track A V8-only, hash antes de B | `NOT_STARTED` |
| P4B | Track B com oito operações, no mesmo hash | `NOT_STARTED` |
| P5 | matriz A/B e auditoria de rastreabilidade/sensibilidade | `NOT_STARTED` |
| P6 | revisão humana independente e decisão de expansão | `NOT_STARTED` |

## Riscos que bloqueiam reutilização automática

- Os três arquivos fonte R4 atuais têm SHA-256 diferente do SHA anotado nos seus JSONs de metadados; isso requer reconciliação antes de qualquer uso de GDPR, DSA ou AI Act como fonte congelada.
- O GDPR anterior é exploratório, V6/RGAM e não uma aplicação V8 independente.
- A adjudicação do PILOT_03 é focal e não equivale a confiabilidade intercodificador humana.
- Os dois casos recomendados usam trechos históricos e intencionais; vigência e texto integral precisam de novo controle antes de claims novos.

## Parada

Esta execução encerra antes de extração substantiva, recodificação GDPR, processamento em escala ou abertura de Track A/B. Nenhum baseline pré-existente foi escrito, movido ou apagado; nenhum commit ou push foi executado.
