# Emenda 001 — política do modelo comparador

**Data:** 2026-10-07  
**Projeto:** PRJ-David / Law and Governance Architectures  
**Experimento:** NEW TEST 3x3  
**Estado:** adição prospectiva e apensa; resultados pareados não abertos

## Preservação do congelamento original

Esta emenda não modifica os 14 artefatos congelados do preregistro de comparação. O manifesto original verificado é `0eeab8866b404523012ae39a1ff3e01ea15466ae4ff54a4c49a1a1bcfd2a514a` e seu gate permanece `V8_RGAM_COMPARISON_PROTOCOL_FROZEN / PAIRED_RESULTS_NOT_OPENED / COMPARISON_NOT_STARTED`.

## Comparador primário

`PRIMARY_COMPARATOR_MODEL = Claude Sonnet 5.5 High`

O comparador primário deve operar em contexto novo que não executou V8 ou RGAM, não participou de recuperação de casos RGAM, não realizou adjudicação humana e não inspecionou previamente saídas substantivas de nenhum braço. Poderá abrir ambos os braços somente depois de: (1) congelamento formal da família RGAM; (2) congelamento desta emenda; e (3) confirmação de integridade do preregistro original.

O motivo é consistência experimental: ambos os braços foram desenhados para a mesma família Claude; a escolha não afirma superioridade de Claude sobre qualquer outro modelo.

## Indisponibilidade e desvio

Não existe substituição automática. Se `Claude Sonnet 5.5 High` estiver indisponível quando a comparação for iniciada, interromper com:

`PRIMARY_COMPARATOR_UNAVAILABLE / PROSPECTIVE_AMENDMENT_REQUIRED`

Não substituir silenciosamente por Codex, outro Claude, Gemini ou outro modelo. Um substituto requer nova emenda datada, concluída antes de abrir qualquer braço naquele contexto.

Se a interface exibir modelo/versão diverso de `Claude Sonnet 5.5 High`, registrar `COMPARATOR_MODEL_DEVIATION` **antes** de abrir saídas substantivas, contendo: modelo exibido; versão se disponível; configuração de esforço/raciocínio; temperatura se exposta; seed se exposta; data; razão; e decisão de prosseguir. Depois da abertura das saídas, uma emenda sobre modelo não poderá ser considerada prospectiva.

## Independência do contexto

Antes da comparação, o contexto proposto deve atestar todos como `NO`:

```text
V8_EXECUTION_PARTICIPATION = NO
RGAM_EXECUTION_PARTICIPATION = NO
HUMAN_ADJUDICATION_PARTICIPATION = NO
PREVIOUS_SUBSTANTIVE_V8_EXPOSURE = NO
PREVIOUS_SUBSTANTIVE_RGAM_EXPOSURE = NO
```

Qualquer resposta `YES` desqualifica o contexto como comparador primário e exige novo contexto.

## Limite desta emenda

A seleção de modelo não autoriza revisar C0–C4, M1–M7, D1–D8, H1–H11, C-A–C-F, regra de materialidade, adjudicação humana, replicação, transferência ou F1–F7.

Uma repetição posterior por Codex ou outro modelo deve ser intitulada `SECONDARY_CROSS_MODEL_COMPARATOR_REPLICATION`; permanece externa ao resultado inferencial primário até que a comparação primária esteja congelada e só poderá avaliar sensibilidade do comparador, robustez de correspondência e dependência de classificações em relação ao modelo avaliador.
