# Log de execução

## 2026-10-04 — abertura controlada

1. Confirmado workspace canônico: `G:\Meu Drive\PRJ-David\Prf-David`.
2. Git inicial: `main...origin/main [ahead 2]`, com numerosos itens não rastreados já existentes, inclusive `.gitignore`, relatórios, pacotes e `V8_COMP_01_2026-10-04/`. Nenhum commit, push, reset, rebase, mudança de branch ou limpeza foi executado.
3. Localizado o pacote pré-registrado existente na raiz e lido como especificação. Para evitar conflito, criada a nova área `COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04/`.
4. Proteções registradas (SHA-256): pré-registro `01_RESEARCH_PROTOCOL.md` `EF8370B96A0E266E5B8CBB0E7B243CCA1D6A9B8D460B969F4B97660259069CC2`; pré-registro de decisões `647403A6BADDE559E1F2337D96CDE94CDDA37A308CA7E06DE82372A2E70BDBC3`; V8 DOCX `AC48C456B9AC0C0C162D0F882ABC645CAAA03FF1D94812C13DCBFD8DF1AD5074`; V8 codebook `5DAC252E7313C951722439FB592BD295ECDCC03B4E091F0794B1533BF899FDAE`; regras de inferência `4A5DFE2DDCE2F2A30C4D1A30BC9800C886D273CD78AB8B859262DDB509F87110`; GDPR README `02AE4EBEEA54D261081B423DC4B65AC9975B9C400EA9A8DD98F0091659FB624E`; baseline PILOT_03 `DFE4B85A6ABBE7565198BC7B871CB6871520D79AC3D7BEC3F199F79E50EB4381`.
5. Não localizado: `how the chat read Igor september 4.docx`, cópia verificável do e-mail de David de 04/10/2026, nem cópia verificada do e-mail grupal de Igor.
6. Consulta oficial MDR: EUR-Lex retornou CELEX 32017R0745, título do regulamento, OJ L 117 de 05/05/2017, estado em vigor/alterado e versão consolidada indicada como 19/07/2026. A interface bloqueou recuperação do texto com verificação JavaScript. Não se extraiu conteúdo legal, não se gerou `MDR_SHARED_EVIDENCE.csv` e nenhum A/B foi feito.
7. Gates: G0 `COMPLETE`; G1 `BLOCKED_SOURCE_PENDING`; G2 `BLOCKED_BY_G1`; G3 `BLOCKED_BY_G2`; G4 `BLOCKED_BY_G2/G3`.

## Decisão técnica

O bloqueio é preservado como resultado metodologicamente correto. A liberação exige texto oficial conferível, versionado e hasheado; memória, paráfrase ou fonte secundária não satisfazem G1.

## 2026-10-04 — G1B common evidence freeze and V8 crosswalk

1. Localizados textos oficiais históricos de P03/31991L0263 e P04/32004R0874 em `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/01_BASELINES/official_texts/`, com manifest CELLAR que registra HTTP 200 e hashes.
2. Conferidos os 4 blocos P03 e 6 blocos P04 do PILOT_03 contra os textos oficiais; Art. 22(7) de P04 foi registrado como contexto de auditoria, não como nova observação.
3. Criados protocolo G1B, crosswalk, escopo, manifest congelado, rubrica e QA. Nenhum texto-fonte, output histórico, baseline ou arquivo de PILOT foi modificado.
4. Detectada divergência entre cópia canônica e cópia de regressão de `PROVISION_REGISTER.csv`; ela foi documentada. `LEGAL_EXCERPTS`, Model A/B e adjudicações são idênticos entre as cópias verificadas.
5. Gate G1B: `CONDITIONAL_PASS`; Track A e Track B permanecem não iniciados. O próximo passo depende de aceite de escopo, reconfirmação de hash e criação do registro comum de declarações.

## 2026-10-04 — G1B closeout and common statement freeze

1. Relido `FROZEN_EVIDENCE_MANIFEST.csv` e recalculadas hashes de todos os 14 artefatos locais acessíveis (incluindo os três componentes de FE-011): todos correspondem aos valores registrados. Criados `SOURCE_INTEGRITY_RECHECK.csv` e `FE011_COMPONENT_MANIFEST.csv`; o manifesto congelado original não foi alterado.
2. Comparadas a cópia canônica e a cópia de regressão de `PROVISION_REGISTER.csv`. Os dez âncoras P03/P04 são idênticos; a divergência global decorre exclusivamente de `capture_date` em 15 casos cegos não selecionados. A resolução e as fontes controladoras foram documentadas sem reconciliar nem sobrescrever cópias históricas.
3. Criado `COMMON_STATEMENT_REGISTER.csv`: 20 enunciados neutros (P03=6; P04=14), todos ancorados em HTML oficial FE-001/FE-003. Art. 22(7) de P04 foi mantido fora do conjunto como contexto de auditoria.
4. Criados dicionário, manifesto de freeze e QA do registro comum. As classificações e adjudicações históricas não foram usadas como resultados prospectivos.
5. G1B foi encerrado como `PASS`; G1C está `READY_FOR_TRACK_A_ONLY`. Preparado prompt de G2 para a próxima iteração. Track A, Track B, recodificação GDPR, extração adicional, commit, push e mudança de branch não foram executados.

## 2026-10-04 — G2 / Track A only

1. Rechecadas antes da execução as hashes do registro comum e dos dois HTMLs oficiais: correspondem ao freeze G1C.
2. Aplicado V8 relacional-leximétrico somente ao conjunto de 20 enunciados: 16 relações qualificadas, 2 atribuições normativas mantidas no nível de enunciado, 2 decisões adiadas por ausência de ator identificável e 13 incertezas registradas.
3. Reconstruídas duas configurações delimitadas em P03 e quatro em P04. P03 para no nível de configuração; P04 suporta apenas uma arquitetura formal delimitada ao microcaso, com Registry como ponto de conexão de capacidades diferenciadas.
4. Criados e congelados os outputs em `TRACK_A/`, com hashes de entradas, baseline V8, prompt e outputs no manifesto. Nenhum output histórico PILOT_03 foi usado como classificação prospectiva.
5. Track B, protocolo adicional de oito operações, comparação A/B, nova extração legal, commit, push, reset e mudança de branch não foram executados.

## 2026-10-04 — Réplica Claude (cross-model) e G3C closeout (entradas registradas retroativamente no G3C; append-only)

**Nota documental:** na abertura do G3C este log terminava em "G2 / Track A only"; não havia entrada G3 (Codex Track B) nem entrada da réplica Claude. A execução G3 do Codex **não é reconstruída aqui**: seu estado congelado consta de `TRACK_B/TRACK_B_FREEZE_MANIFEST.csv` (carimbo 13:42:38) e `TRACK_B/TRACK_B_EXECUTION_LOG.md`.

1. **Réplica Claude (Sonnet 5.5, `claude-sonnet-5-5`)** em `CROSS_MODEL_REPLICATION/CLAUDE/`: Track A (V8 apenas, subagente novo, 13:54–14:08, congelado 14:09:29) e Track B (V8 + oito operações, segundo subagente novo, 14:10–14:30, congelado 14:30:36). Relatório: `CLAUDE_REPLICATION_COMPLETION_REPORT.md`; divulgação de contexto e contaminação: `PROMPTS_AND_LOGS/00_…DISCLOSURE.md` (eventos C1–C6; erros de processo A-1…A-3). Sem comparação com o Codex.
2. **G3C closeout** (`G4_COMPARISON_PREPARATION/`): recalculadas as hashes dos quatro cells (Codex A 6/6, Codex B 11/11, Claude A 7/7, Claude B 11/11), do registro comum e dos HTML oficiais; IDs idênticos (20). Pacote externo G3C e spec G4 **não localizados**; arquivo auxiliar `TRACK_B_FREEZE_MANIFEST_SHA256.txt` do Codex **ausente** (não regenerado). Regra uniforme de escopo de evidência (E1/E1x/E2/E3), matriz G4, regras de matching e instrumento de revisão humana (Tier 1, 8 cartões anonimizados) preparados.
3. **Status:** `G3C_CONDITIONAL_PASS / G4_PENDING_DOCUMENTARY_RESOLUTION`. Comparação substantiva G4 **não iniciada**. Nenhum artefato congelado foi alterado; nenhum commit, push, reset ou mudança de branch.

## 2026-10-04 — G3C decisions C1–C6 e G4 Step 0 (auditoria de fronteira de evidência; append-only)

1. Registradas as decisões C1–C6 de Igor (`G4_COMPARISON_PREPARATION/G3C_DECISIONS_C1_C6.md`; entrada em `G4_AUTHORIZATION_DECISION.md`). C1 não executável: o pacote `G3C_AUDIT_AND_G4_PREPARATION_2026-10-04.zip` (SHA-256 esperado `686E322F…FA99`) **não foi encontrado** em Downloads nem no workspace; nenhum documento foi importado ou lido; reconciliação feita apenas contra os critérios originais registrados (`EXTERNAL_AUDIT_RECONCILIATION.md`).
2. C5: busca única somente leitura em `C:\Users\Adm\.codex`: modelo `gpt-5.6-terra`, esforço de raciocínio alto, extensão Codex VS Code (CLI 0.159.2), uma sessão cobrindo Track A e Track B (metadados apenas; conteúdo e credenciais não lidos).
3. Dicionário único de escopo de evidência (SC-A…SC-D) e **G4 Step 0** executado sobre os quatro cells: 112 unidades classificadas (Codex A 24, Codex B 29, Claude A 28, Claude B 31) + 2 unidades-núcleo derivadas; 5 desvios materiais de escopo (Claude A: R-P03-04, CL-P03-02, CL-P03-03; Claude B: R-P04-05, CL-P04-02); 2 casos limítrofes SC-B; 13 unidades com marcador periférico; 5 questões de proveniência não resolvidas; fila de 28 itens de revisão humana. Nenhum matching entre cells; nenhum juízo de superioridade; nenhum juízo sobre melhoria de B sobre A.
4. **Status:** `G4_STEP0_CONDITIONAL`; Step 1 não iniciado e não autorizado. Os quatro cells permanecem congelados, com hashes originais inalterados; sem commit, push, reset ou mudança de branch.

## 2026-10-04 — G4 Step 1: extração e normalização de afirmações (append-only)

1. Registradas as decisões C1–C6 de Igor em `G4_AUTHORIZATION_DECISION.md` (entrada "G4 Step 1 authorisation"). C1: nova tentativa de localizar a especificação externa (19:20 -03:00) falhou; vigora `DOCUMENTED_SUPPLEMENTARY_AUDIT_WAIVER`; nenhum arquivo externo foi importado ou revisado. A descrição E0–E3 retransmitida via ChatGPT foi registrada como não autenticada, comparada semanticamente com o dicionário local e **não mapeada**.
2. Verificadas as 112 unidades do Step 0 contra o registro local (IDs, âncoras, caso) e preservadas as conclusões: 5 desvios materiais (Claude A: R-P03-04, CL-P03-02, CL-P03-03; Claude B: R-P04-05, CL-P04-02), 2 casos limítrofes (Claude B CL-P04-04, CL-P04-07) e 13 observações periféricas. Nada foi removido, reparado ou reclassificado.
3. Criado o registro normalizado neutro (`G4_STEP1_NORMALIZED_CLAIMS.csv`: 112 unidades originais — Codex A 24, Codex B 29, Claude A 28, Claude B 31 — + 2 unidades `STEP0_DERIVED`), com formulações originais literais, registro de elegibilidade com propagação de dependências, fila de revisão humana (28 itens preservados; 7 P1 enriquecidos), dicionário de dados, log de decisões de normalização (N-01…N-22) e relatório de QA (25 PASS, 0 FAIL, 1 informativo). Nenhum matching entre cells, nenhum rótulo de melhoria/regressão/concordância, nenhum juízo de superioridade.
4. Elegíveis para comparação primária: 105 (+4 provisórias pendentes de confirmação humana); restritas à sensibilidade: 5. Revisão humana P1 pendente; nenhuma decisão humana criada ou simulada.
5. **Status:** `G4_STEP1_FROZEN / STEP2_NOT_STARTED`. Cells experimentais, registro comum e arquivos do Step 0 inalterados (exceto o append em `G4_AUTHORIZATION_DECISION.md`); sem commit, push, reset ou mudança de branch.

## 2026-10-04 — G4 Step 2A: correspondência candidata entre afirmações (append-only)

1. Pré-condições verificadas após o checkpoint de recuperação: manifesto do Step 1 `0DEC88FF…DD0B` conferido de novo; quatro cells (35 saídas), registro comum, HTML oficiais e arquivos do Step 0 inalterados; relatório de recuperação, regras de matching, fila de revisão e critérios originais presentes. O checkpoint de recuperação foi registrado como evento de proveniência posterior, sem alterar o freeze do Step 1.
2. Executado o G4 Step 2A **somente** de correspondência, agrupamento e rastreabilidade documental: 26 grupos de correspondência candidata (16 de relação, 6 de configuração, 2 posicionais, 2 de nível arquitetural); 101 das 112 unidades originais agrupadas, 11 sem correspondente (Codex A 0, Codex B 2, Claude A 4, Claude B 5); casos muitos-para-um CG-001 e CG-011 e um-para-muitos Claude A CL-P04-04; 3 grupos com conflito de escopo (CG-018, CG-019, CG-022); 5 dependências materiais, 4 unidades provisórias, 2 núcleos derivados e 13 observações periféricas preservados; marcas de escopo propagadas aos grupos arquiteturais.
3. Pacote de revisão humana com 13 cartões anonimizados (identidade em chave separada); os 7 itens P1 seguem pendentes de adjudicação humana; nenhum revisor humano foi simulado. QA: 32 PASS, 0 FAIL.
4. **Status:** `G4_STEP2A_FROZEN / STEP2B_NOT_STARTED`. Sem pontuação de concordância, sem rótulo de melhoria/regressão, sem juízo de superioridade, sem atribuição das cinco categorias do protocolo. Sem commit, push, reset ou mudança de branch.
