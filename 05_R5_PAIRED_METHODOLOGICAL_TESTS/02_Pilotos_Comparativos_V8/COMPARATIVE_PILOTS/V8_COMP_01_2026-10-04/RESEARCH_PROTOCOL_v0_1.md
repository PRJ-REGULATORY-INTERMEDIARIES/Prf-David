# Protocolo de pesquisa v0.1

**Projeto:** V8-COMP-01 — Comparative Architectural Inference Pilot  
**Data de registro:** 2026-10-04  
**Estado:** `DESIGN_REGISTERED`; execução empírica depende de G1.

## 1. Pergunta e escopo

Mantendo constantes a fonte jurídica primária, a delimitação declarada e a camada de codificação V8, a aplicação explícita de oito operações produz inferências arquiteturais mais defensáveis, claras ou informativas que V8 aplicado sozinho? O resultado negativo é substantivamente informativo: o protocolo adicional pode apenas tornar explícito o que V8 cuidadoso já exige, ou piorar a análise com escolha interpretativa e falsa precisão.

V8 é a única referência conceitual. Os seguintes rótulos são obrigatórios: `V8_DEFINED` para conceito atribuído diretamente a V8; `OPERATIONAL_SPECIFICATION` para campo, regra ou procedimento do projeto; `METHOD_HYPOTHESIS` para a proposição adicional a ser testada. A especificação das oito operações é uma hipótese metodológica complementar, não uma contribuição atribuída a David.

Não se conclui sobre eficácia observada, implementação, comportamento dos atores ou regime inteiro a partir da mera existência de texto legal. A unidade é uma configuração de intermediação/conformidade sustentada por provisões, não a lei inteira por default.

## 2. Hipóteses concorrentes

- **H1 — benefício incremental:** a sequência adicional melhora rastreabilidade, revela condicionantes/posições e evita relações, saltos de nível ou propriedades do todo sem apoio textual.
- **H0 — ausência de ganho material:** V8 aplicado com cuidado já entrega o mesmo resultado, e o custo adicional não se justifica.
- **H- — efeito adverso:** o protocolo adiciona jargão, viés de recorte, redundância ou falsa precisão, produzindo resultado pior.

## 3. Casos e delimitação prospectiva

MDR (EU 2017/745) vem primeiro porque permite estressar intermediação, gatekeeping, avaliação de conformidade, designação e supervisão. DSA (EU 2022/2065) explora autoridade distribuída e arranjos de plataformas; Lei 13.848/2019 explora autonomia e accountability de reguladores. A seleção é provisória de Igor, não escolha de David ou da equipe. GDPR é antecedente metodológico, não quarto resultado validado. AI Act e CNJ são reservas.

O escopo inicial candidato do MDR é arts. 35–45 e 52, mais referências cruzadas que sejam necessárias e documentadas. A inclusão exige conexão juridicamente verificável com a configuração; a exclusão deve ser registrada, inclusive quando uma regra apenas nomeia ator ou atribui obrigação sem contraparte identificável.

## 4. Evidência comum e trilhas A/B

Antes de qualquer inferência, verificar texto oficial, língua, identificador, versão/consolidação, vigência, data de acesso e provisões. Criar declarações institucionais rastreáveis a uma provisão, preservando sujeito, ação, modalidade, objeto, condição, consequência e cross-reference. Uma atribuição normativa sem contraparte é uma declaração, não uma edge automaticamente.

Após QA, gerar `MDR_SHARED_EVIDENCE.csv`, calcular SHA-256 e congelar a cópia. Ambas as trilhas usam esse exato hash.

- **Track A (V8 only):** aplicar apenas a escada inferencial, significância arquitetural, rastreabilidade e stopping rule de V8. Salvar e hashear antes de abrir Track B.
- **Track B (V8 + 8 operações):** aplicar as oito operações abaixo à mesma evidência. Não modificar Track A após conhecer B.

## 5. Oito operações — `METHOD_HYPOTHESIS`

1. **Delimitação:** objeto, jurisdição, versão, tempo, problema e fronteira.
2. **Decomposição:** separar declarações institucionais e manter modalidade, condição e contexto.
3. **Reconstrução relacional:** reconhecer somente vínculo ator–ator qualificado por texto ou cross-reference declarada.
4. **Reconstrução configuracional:** agrupar atores, relações, funções, mecanismos e instrumentos de modo explicitamente justificado.
5. **Posição e sequência:** distinguir porta de entrada, ordem, opção, obrigatoriedade, substituibilidade e autoridade condicional.
6. **Parte–todo:** distinguir atributo de ator, relação, posição, configuração, lei e regime.
7. **Inferência arquitetural:** declarar evidência, warrant, contraevidência e stopping rule.
8. **Sensibilidade:** testar recortes e leituras alternativas plausíveis e registrar efeitos.

## 6. Rubrica de comparação

Cada claim é comparado provision-by-provision: evidência comum; conclusão A; conclusão B; diferença; suporte jurídico; ganho alegado de clareza/defensabilidade; erro evitado ou introduzido; sensibilidade ao recorte; custo adicional; revisão humana. Os únicos rótulos permitidos são `B_IMPROVES`, `B_CLARIFIES_ONLY`, `B_EQUIVALENT`, `B_WORSE` e `UNRESOLVED`. Não há índice sintético não validado.

Critérios: (a) rastreabilidade vertical claim → configuração → relação → declaração → provisão; (b) validade inferencial; (c) clareza; (d) descoberta distintiva sustentada; (e) robustez; (f) reprodutibilidade/revisão; e (g) custo analítico. A ausência de melhora conta como resultado.

## 7. Gates e critérios de passagem

| Gate | Critério | Estado nesta execução |
|---|---|---|
| G0 | repositório, fontes-base, pré-registro e proteções inventariados | `COMPLETE` |
| G1 | texto oficial verificável e versionado, com snapshot/local checksum | `BLOCKED_SOURCE_PENDING` |
| G2 | 8–12 statements candidatos, fonte a fonte, QA e freeze da evidência comum | `BLOCKED_BY_G1` |
| G3 | Track A V8-only concluído e congelado antes de B | `BLOCKED_BY_G2` |
| G4 | Track B e matriz A/B na mesma evidência | `BLOCKED_BY_G2/G3` |
| G5 | validação humana/independente e análise de sensibilidade | `NOT_STARTED` |
| G6 | decisão de transferência para DSA/Lei 13.848 e relatório de limites | `NOT_STARTED` |

## 8. Salvaguardas e limites

Não editar V8, ontologia, PILOT_03, adjudicações, código de Rotem, corpus GDPR, preprints ou backups. Não escalar produção. Não tratar uma relação unilateral, conectividade gráfica, coocorrência, nomenclatura ou pertença ao mesmo estatuto como arquitetura. Não confundir relação jurídica formal com operação empírica. Não apresentar feedback de equipe sem fonte; novos comentários e emendas são append-only.
