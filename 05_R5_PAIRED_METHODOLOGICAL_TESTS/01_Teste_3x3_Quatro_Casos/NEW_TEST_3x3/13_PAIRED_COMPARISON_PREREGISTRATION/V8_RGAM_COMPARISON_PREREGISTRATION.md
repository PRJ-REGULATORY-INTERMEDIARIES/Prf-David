# Prerregistro de comparação pareada V8 × RGAM

**Projeto:** PRJ-David / Law and Governance Architectures  
**Coordenador:** Igor Caires Machado  
**Data:** 2026-10-06  
**Estado:** congelado prospectivamente; comparação não iniciada

## Objeto e cegamento

Este documento fixa como será feita a comparação, não compara V8 e RGAM. A unidade experimental é cada par de aplicações ao mesmo instrumento, corpus jurídico comum congelado e caso: Social Climate Fund (Regulamento (UE) 2023/955), CBAM (Regulamento (UE) 2023/956), AI Act (Regulamento (UE) 2024/1689) e Diretiva 86/361/CEE.

V8 é a linha de base conceitual/metodológica. RGAM é a extensão operacional candidata. Nenhuma regra abaixo presume vantagem de RGAM. São admissíveis ganho substantivo, ganho de rastreabilidade, ganho de sensibilidade/robustez, explicitação apenas procedimental, equivalência, ganho misto com regressão, regressão e indeterminação.

Durante a elaboração deste preregistro não foram abertos conteúdos substantivos de `09_V8_BASELINE_EXECUTION/` nem de `12_RGAM_CASE_EXECUTION/`. A comparação futura deve ser executada em contexto novo, que só poderá abrir ambos os braços depois deste congelamento. Desvio do modelo recomendado (Claude Sonnet 5.5 High) deve ser registrado antes da comparação. Síntese pós-adjudicação deve, preferencialmente, usar outro contexto novo.

## Perguntas registradas

**Q1.** Dado o mesmo instrumento jurídico completo e o mesmo corpus probatório, RGAM fornece valor incremental analiticamente defensável além de uma aplicação competente de V8 na reconstrução da arquitetura de governança?

**Q2.** RGAM recupera informação relacional, configuracional ou arquitetural juridicamente apoiada que V8 não recupera?  
**Q3.** RGAM torna a cadeia evidência → relação → configuração → arquitetura mais reconstruível/auditável?  
**Q4.** RGAM reduz inferência arquitetural sem apoio ou excessiva — ou introduz sobre-inferência?  
**Q5.** RGAM identifica condições de fronteira, agrupamentos rivais, dependências de corpus ou sensibilidades que alteram materialmente a confiança?  
**Q6.** RGAM representa indeterminação genuína de modo mais explícito ou defensável?  
**Q7.** Qual carga analítica adicional RGAM exige em relação à contribuição incremental observada?  
**Q8.** Diferenças V8–RGAM se replicam nos dois casos climáticos?  
**Q9.** Diferenças semelhantes aparecem nos casos de transferência (AI Act e Diretiva 86/361/CEE)?

## Princípios vinculantes

1. A comparação primária é estritamente **intra-caso**: SCF V8↔SCF RGAM; CBAM V8↔CBAM RGAM; AI Act V8↔AI Act RGAM; Diretiva 86/361 V8↔Diretiva 86/361 RGAM. Nenhuma comparação cruzada entre instrumentos prova desempenho metodológico.
2. Volume de arquivos, registros, relações, configurações, tabelas, palavras, tokens, atores ou complexidade computacional não é indicador de qualidade. Pode ser descritor de custo somente.
3. Não se força correspondência um-para-um entre registros. O denominador comum é a proposição juridicamente sustentada, nos níveis C0–C4.
4. Diferença material deve ser avaliada quanto a evidência, contribuição, rastreabilidade, explicitação, fronteira/sensibilidade, calibração, sobre-inferência e omissão; não há escore composto ou ranking numérico.
5. Divergência juridicamente consequencial requer adjudicação humana antes de qualquer implicação metodológica. O comparador formula a pergunta; não simula a decisão humana.
6. Ausência de vantagem e equivalência substantiva são resultados científicos válidos.

## Fonte metodológica e precedência

A ponte V8–RGAM usa exclusivamente documentos metodológicos: os quatro protocolos V8 em `RGAM/V8_ACTIVE/03_METHODOLOGY/`, o preprint fundacional V8 e os cinco documentos RGAM congelados em `11_RGAM_PROTOCOL_FREEZE/`. A ponte é auxiliar de tradução e não declara identidade teórica. Conflitos de interpretação comparativa são registrados como `NO_DEFENSIBLE_EQUIVALENT`, `M7_NOT_COMPARABLE` ou encaminhados para adjudicação, conforme aplicável.

## Fluxo futuro obrigatório

Para cada caso: (1) comparar C0; (2) C1; (3) C2; (4) C3; (5) C4, fronteiras e parada; (6) formar a fila humana; **parar**; (7) incorporar adjudicações; (8) produzir vetor e uma categoria C-A–C-F. Somente depois dos quatro perfis congelados poderá haver análise climática e, em seguida, transferência e síntese familiar.

Os templates, regras operacionais, esquema de saída e QA vinculantes estão nos documentos irmãos deste diretório. Qualquer esclarecimento posterior às saídas pareadas deve ser uma emenda datada, que declare expressamente se os resultados pareados já tinham sido vistos; não altera retrospectivamente as regras congeladas.

## Regra de congelamento

Depois de vistos os resultados pareados, não podem ser alterados: categorias M1–M7, regra de materialidade, D1–D8, gatilhos H1–H11, categorias C-A–C-F, critérios de replicação/transferência ou categorias F1–F7. O manifesto e sua soma SHA-256 identificam este pacote.

**Gate final:** `V8_RGAM_COMPARISON_PROTOCOL_FROZEN / PAIRED_RESULTS_NOT_OPENED / COMPARISON_NOT_STARTED`
