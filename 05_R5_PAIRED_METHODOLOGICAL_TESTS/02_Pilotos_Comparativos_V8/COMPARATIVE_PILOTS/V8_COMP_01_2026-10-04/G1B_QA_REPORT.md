# G1B — relatório QA

## Verificações concluídas

- **P03 / 31991L0263:** HTML local contém identificação EUR-Lex, título, data 29/04/1991 e OJ L 128 de 23/05/1991. O manifesto de textos oficiais registra origem CELLAR, HTTP 200 em 30/09/2026 e hash HTML `01D5…6888`. Os quatro identificadores PILOT_03 são localizáveis no texto.
- **P04 / 32004R0874:** HTML local contém identificação EUR-Lex, título, data 28/04/2004 e OJ L 162 de 30/04/2004. O manifesto registra origem CELLAR, HTTP 200 em 30/09/2026 e hash HTML `62AF…1449`. Os seis blocos PILOT_03 são localizáveis; Art. 22(7) foi acrescentado somente como contexto de auditoria para a classificação composta histórica.
- **Integridade histórica:** `LEGAL_EXCERPTS.csv`, modelos A/B e adjudicações da cópia canônica e da cópia de regressão têm hash idêntico. `PROVISION_REGISTER.csv` diverge entre as cópias (`EDBBB…59F0` versus `E4F6…16CF`); a cópia canônica é referenciada como registro histórico, mas o HTML oficial prevalece em qualquer divergência.

## Crosswalk

Há 10/10 blocos de provisão mapeados para categorias V8 no `PILOT03_TO_V8_CROSSWALK.csv`. O mapeamento é completo no nível de evidência/declaração e deliberadamente incompleto no nível de relação/configuração: P03_PR02, P03_PR03, P04_PR01, P04_PR05 e P04_PR06 conservam ambiguidade ou exigem decomposição. Isto é conformidade com a stopping rule, não falha a ocultar.

## Não conformidades / riscos

1. Os atos são históricos originais; vigência, consolidação e alterações posteriores não foram verificadas e estão fora do claim permitido.
2. O antigo PILOT_03 usou modelos e adjudicação focal; não é V8, não é confiabilidade humana completa e não é Track A/B.
3. O `PROVISION_REGISTER` possui cópia divergente; não pode servir sozinho de freeze primário.
4. V8 não autoriza que nomeação/designação, objeto de obrigação ou efeito jurídico seja automaticamente tratado como relação entre atores.

## Gate e recomendação

**G1B:** `CONDITIONAL_PASS`. As duas fontes primárias históricas e sua proveniência local são verificáveis; o manifest fixa a mesma base para ambas as trilhas.  
**Recomendação para Track A:** `AUTHORIZE_ONLY_AFTER_SCOPE_ACCEPTANCE`. Antes de começar, registrar aceite explícito do par de casos, recalcular os hashes do manifest e criar o registro comum de declarações fonte-a-fonte. Não iniciar Track B antes de salvar e hashear Track A.

Nenhuma extração jurídica substantiva, inferência V8, Track A, Track B, commit, push ou alteração de fonte congelada ocorreu neste gate.
