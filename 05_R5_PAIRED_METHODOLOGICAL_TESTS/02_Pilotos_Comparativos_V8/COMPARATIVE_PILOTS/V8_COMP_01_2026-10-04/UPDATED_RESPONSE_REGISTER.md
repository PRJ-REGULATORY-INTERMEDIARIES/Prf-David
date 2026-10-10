# Registro atualizado de respostas e decisões

**Regra:** este documento acrescenta entradas ao registro anterior sem o editar. O original em `RESPONSE_AND_DECISION_REGISTER.md` permanece preservado.

## R-005 — instrução posterior de David sobre prioridade

- **Data relatada:** 2026-10-04.
- **Ator:** David Levi-Faur.
- **Canal:** mensagem/e-mail relatado e documentado por Igor nesta sessão.
- **Conteúdo recebido:** “great. Start with the laws that you already analyzed 3 and 3. or 2 and 2”.
- **Modo de registro:** `verbatim_as_supplied`; a cadeia de custódia é a instrução de Igor fornecida nesta sessão, não um export local do e-mail.
- **Evidência original local:** `MISSING_PENDING_INCORPORATION`. Nenhuma mensagem original, exportação, cabeçalho ou metadado de envio foi localizada durante a auditoria.
- **Classificação:** `DOCUMENTED_RESEARCH_SUPERVISION / PRIORITY_DIRECTION`.
- **Interpretação delimitada:** priorizar leis previamente analisadas. O sentido numérico de “3 and 3” ou “2 and 2” é `UNCONFIRMED`; não foi transformado em decisão de tamanho de amostra.
- **Efeito:** MDR muda para `ON_HOLD_SOURCE_PENDING`; o inventário de casos existentes passa a anteceder qualquer extração nova.
- **Estado decisório:** `IMPLEMENTED_AS_PRIORITY_REALIGNMENT`; a composição final da amostra permanece `PROPOSED_PENDING_CONFIRMATION`.

## Correção de status de feedback

David **não** é `AWAITING_EVIDENCE` para esta instrução: a mensagem foi recebida/documentada por Igor. O que permanece pendente é apenas a incorporação de evidência documental original. A slot anterior `P-DAVID-NEW` deve ser lida como reservada para resposta futura, não como negação desta mensagem.

## Preservação de entradas anteriores

R-001 a R-004 continuam válidas conforme seus próprios limites de evidência. A nova instrução não significa que David tenha endossado MDR, DSA, Lei 13.848, uma ontologia nova, um artigo separado, nem qualquer conclusão empírica.

## D-G1B-001 — decisão de execução controlada

- **Data:** 2026-10-04; **decisor operacional:** Igor/Codex sob a instrução G1B fornecida nesta sessão.
- **Decisão:** verificar apenas a proveniência histórica e preparar o freeze/crosswalk para P03 e P04; não iniciar Track A/B, extração substantiva ou recodificação.
- **Fundamento:** a instrução de G1B exige mesmo input primário para as duas trilhas e preservação de baselines históricos.
- **Estado:** `IMPLEMENTED_AT_G1B`; autorização final de Track A permanece condicionada ao aceite de escopo indicado no QA.

## D-G1B-002 — aceite operacional de escopo e freeze comum

- **Data:** 2026-10-04; **decisor operacional:** Igor, conforme a instrução de closeout fornecida nesta sessão.
- **Decisão:** autorizar P03/Directive 91/263/EEC e P04/Regulation (EC) No 874/2004 como dois microcasos de viabilidade; isto não interpreta nem confirma a expressão numérica de David.
- **Efeito:** as condições de escopo de G1B estão satisfeitas para criar o registro neutro e o freeze comum; a autorização é somente para a futura Track A após rechecagem de hash.
- **Limites:** Track B continua vedada até Track A ser concluída, salva e congelada; Art. 22(7) de P04 permanece excluído; a evidência original do e-mail de David continua `MISSING_PENDING_INCORPORATION`.
- **Estado:** `IMPLEMENTED_AT_G1B_CLOSEOUT`.

## D-G2-001 — autorização e congelamento da Track A

- **Data:** 2026-10-04; **autorização:** instrução G2 fornecida nesta sessão.
- **Decisão executada:** aplicar V8 relacional-leximétrico ao input comum congelado para P03 e P04, sem o protocolo adicional de oito operações e sem iniciar Track B.
- **Resultado:** `TRACK_A_FROZEN`; o manifest de freeze contém hashes do input, fontes, baseline V8, prompt e outputs.
- **Limite:** o resultado histórico PILOT_03 permanece apenas proveniência; qualquer futura Track B requer autorização independente e não pode reconstruir esta Track A.

## D-G3C-001 — fechamento condicional do G3C e preparação do G4 (recomendação registrada; decisão de Igor pendente)

- **Data:** 2026-10-04; **registrado por:** Claude Code (Sonnet 5.5) a partir da instrução G3C fornecida nesta sessão; **decisor operacional:** Igor (confirmação ainda não registrada).
- **Resultado preparado:** `G3C_CONDITIONAL_PASS / G4_PENDING_DOCUMENTARY_RESOLUTION`. Os quatro cells foram reverificados localmente (6/6, 11/11, 7/7, 11/11); permanecem abertos P-01 (pacote externo e spec G4 não localizados), P-02 (auxiliar de freeze do Codex Track B ausente), P-04 (regra de escopo de evidência; R-P04-05), P-06 (documentos de método diferentes entre ambientes) e P-07 (modelo Codex não documentado).
- **Limites:** comparação substantiva G4 não autorizada por este registro; nenhum artefato congelado alterado; o arquivo auxiliar ausente não foi regenerado; nenhum resultado de revisão humana existe ou foi simulado.
- **Documentos:** `G4_COMPARISON_PREPARATION/G4_AUTHORIZATION_DECISION.md` (condições C1–C6 com padrões) e `DOCUMENTARY_PENDING_ITEMS_REGISTER.md`.
- **Estado:** `PREPARED_AWAITING_DECISION`.

## D-G3C-002 — decisões C1–C6 e resultado do G4 Step 0 (registro; append-only)

- **Data:** 2026-10-04; **fonte:** instrução de registro das decisões C1–C6 fornecida por Igor nesta sessão; registrado por Claude Code (Sonnet 5.5).
- **Decisões:** C1 `INCORPORATE_AND_RECONCILE` (não executável: pacote não localizado); C2 `ACCEPT_WITH_DOCUMENTED_LIMITATION`; C3 `APPROVED` sujeito a reconciliação semântica; C4 `CONFOUNDED_INPUT`; C5 busca de proveniência do Codex (encontrado `gpt-5.6-terra`, esforço alto, CLI 0.159.2); C6 avaliação preliminar por IA autorizada, revisão humana obrigatória para evidência contestada, afirmações arquiteturais centrais e conclusões finais de validade jurídica.
- **Resultado:** `G4_STEP0_CONDITIONAL`; 112 unidades classificadas; 5 desvios materiais de escopo; 2 limítrofes; 5 questões de proveniência; 28 itens para revisão humana.
- **Limites:** as decisões autorizam preparação e classificação de evidência, não aprovam qualquer conclusão favorável ao Track B; Step 1 **não** autorizado por este registro; nenhum artefato congelado alterado.
- **Estado:** `RECORDED_STEP1_PENDING_DECISION`.

## D-G4-S1-001 — autorização e congelamento do G4 Step 1 (registro; append-only)

- **Data:** 2026-10-04; **fonte:** instrução G4 Step 1 e decisões C1–C6 fornecidas por Igor nesta sessão; registrado por Claude Code (Sonnet 5.5).
- **Decisões:** C1 `DOCUMENTED_SUPPLEMENTARY_AUDIT_WAIVER` (especificação externa não localizada); C2 `ACCEPT_WITH_DOCUMENTED_LIMITATION`; C3 dicionário SC-A…SC-D aprovado (descrição E0–E3 retransmitida via ChatGPT registrada, comparada e não mapeada); C4 `CONFIRMED_AS_CONFOUNDED_INPUT`; C5 proveniência Codex atualizada (`gpt-5.6-terra`, esforço High, extensão Codex VS Code, CLI 0.159.2; demais parâmetros `NOT_DOCUMENTED`); C6 normalização e triagem preliminares por IA autorizadas; P1 pendentes de adjudicação humana.
- **Resultado:** `G4_STEP1_FROZEN / STEP2_NOT_STARTED`; 112 unidades + 2 derivadas; 105 elegíveis (+4 provisórias); 5 apenas sensibilidade; 5 questões de proveniência; fila de 28 itens (7 P1).
- **Limites:** não autoriza matching, pontuação, rótulos de melhoria/regressão, concordância nem o Step 2; nenhum artefato congelado alterado.
- **Estado:** `RECORDED_STEP2_NOT_AUTHORIZED`.

## D-G4-S2A-001 — autorização e congelamento do G4 Step 2A (registro; append-only)

- **Data:** 2026-10-04; **fonte:** autorização do Step 2A fornecida por Igor após o checkpoint `RECOVERY_VERIFIED / G4_STEP1_FROZEN / STEP2_AWAITING_AUTHORIZATION`; registrado por Claude Code (Sonnet 5.5).
- **Autorizado:** correspondência, agrupamento e rastreabilidade documental de afirmações entre os quatro cells. **Não autorizado:** pontuação comparativa, avaliação de superioridade, escores de concordância, rótulos de melhoria/regressão ou das cinco categorias do protocolo, adjudicação final de validade jurídica, Step 2B.
- **Resultado:** `G4_STEP2A_FROZEN / STEP2B_NOT_STARTED`; 26 grupos candidatos; 101 unidades originais agrupadas e 11 sem correspondente; 13 grupos com revisão humana requerida (9 YES, 4 SPOT_CHECK); P1 pendentes.
- **Limites:** CONFOUNDED_INPUT preservado; nenhum artefato congelado alterado; recuperação registrada como evento de proveniência posterior.
- **Estado:** `RECORDED_STEP2B_NOT_AUTHORIZED`.
