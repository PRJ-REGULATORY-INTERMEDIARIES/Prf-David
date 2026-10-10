# AMENDMENT_002 — prioridade para legislação já analisada

**Data:** 2026-10-04  
**Status:** `REGISTERED / NO_LEGAL_EXTRACTION_AUTHORIZED`  
**Decisor metodológico que motivou a emenda:** David Levi-Faur (mensagem documentada por Igor; evidência original local pendente).

## Alteração registrada

A proposta inicial registrada em 04/10 era a sequência MDR (Regulamento (UE) 2017/745) → DSA (Regulamento (UE) 2022/2065) → Lei brasileira 13.848/2019. Em mensagem posterior fornecida por Igor nesta sessão, David escreveu: “great. Start with the laws that you already analyzed 3 and 3. or 2 and 2”.

O texto da mensagem é registrado como instrução de supervisão recebida e documentada por Igor. Não há, nesta execução, arquivo de e-mail original, exportação, cabeçalhos, data/hora, destinatários ou outro comprovante local. A redação acima não permite inferir com segurança se “3 and 3” e “2 and 2” referem-se a número de leis, grupos, etapas, codificadores ou outra organização; a emenda não escolhe essa interpretação.

## Efeito de prioridade

1. Priorizar somente instrumentos para os quais o repositório demonstra análise prévia, fonte local rastreável e, quando alegado, observações/relações realmente existentes.
2. **MDR:** `ON_HOLD_SOURCE_PENDING`. Não foi extraído; continua registrado para possível expansão futura e não foi descartado.
3. DSA e Lei 13.848/2019 permanecem disponíveis como casos futuros. O DSA possui corpus/extratação estrutural prévia, mas não R/I/T ou validação humana; a Lei 13.848 não teve análise prévia verificada nesta auditoria.
4. Nenhum baseline, protocolo, hash, QA ou log anterior é modificado por esta emenda. Esta é uma camada append-only de direcionamento.

## Racional científico

Usar casos já analisados pode permitir um experimento A/B mais rastreável e de menor custo, desde que o baseline seja reconstruído sob V8 e que as duas trilhas usem exatamente o mesmo conjunto de fontes primárias congeladas. A existência de uma codificação prévia não prova compatibilidade com V8, validação humana completa, vigência atual ou reutilização automática. Cada uma dessas condições continua sendo gate independente.

## Limites e pendências

A recomendação de dois casos no `CASE_SELECTION_MEMO.md` é deliberadamente conservadora e não pretende resolver a ambiguidade numérica de David. Qualquer mudança de número, agrupamento ou seleção exige uma emenda posterior com fonte, interpretação explícita e decisor identificado.
