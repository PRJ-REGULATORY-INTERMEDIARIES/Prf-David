# COMPLETE RESEARCH ACTIVITY REPORT — DAVID LEVI-FAUR COLLABORATION

**Auditoria do histórico recuperável até 1 de outubro de 2026**

## 1. Resumo executivo

O workspace reúne uma trajetória de pesquisa sobre intermediação regulatória e leximetria relacional: propostas e protótipos EUR-Lex em `Before_R2/`, pilotos de arquitetura relacional, validação estrutural em direito digital e reconstrução conceitual ARQGOV. O Git acessível começa como importação ampla em 12 set 2026, portanto cobre somente parte tardia da evolução. Havia 1.499 arquivos acessíveis antes da auditoria, muitos fora do índice Git em meio a remoções staged e reorganização local.

PILOT_03 registrou 19 adjudicações humanas, 14 com impactos retrospectivos, e gate `ONTOLOGY_STABLE_WITH_REVISIONS`: revisão necessária, não validação completa nem autorização de produção. R4 produziu 1.404 registros estruturais para GDPR, DSA e AI Act e identificou fragilidades em spans, relações e representação de ação. A recomendação documentada é não fazer reparo corpus-wide; RIT/mecanismos e comparação substantiva não começaram. ARQGOV produziu reconstrução conceitual e materiais para revisão, sem endosso autoral demonstrado; closeout fica em `EXTERNAL_REVIEW_PENDING`. Horas totais não são recuperáveis.

## 2. Escopo e método

Raiz: `G:\Meu Drive\PRJ-David\Prf-David`. Um único repositório, branch `main`, HEAD `a12999c14614f99b1ca0a51950b74c2a4beb58a7`, um commit à frente de `origin/main`; worktree e submódulos adicionais não encontrados. A árvore já mostrava muitas remoções staged e diretórios não rastreados; foi preservada. Inventário completo de caminhos consta em `01_FILE_INVENTORY.csv`; todos os commits alcançáveis têm metadados e paths em `02_COMPLETE_CHANGE_REGISTER.csv`. Foram lidos prioritariamente relatórios de fase, decisões e manifests. DOCX/XLSX/PDF/ZIP não foram extraídos em lote e nem todo arquivo foi semanticamente lido, limitação registrada no manifest.

## 3. História e trabalho desenvolvido

O commit inicial visível importa um acervo já substancial: candidatura, notas conceituais, estudos, entregas v1 e PoCs, codebooks, scripts, corpus e protocolos. As versões v3/v4 ampliam screening, esquemas, prompts em estágios, automação e validação. Cleanroom, manifests e arquivos por caso mantêm fonte, saída de modelo e revisão humana separáveis. Esse commit não estabelece a data de início real.

PILOT_01 e PILOT_02 desenvolvem protocolo e comparação; PILOT_03 testa a arquitetura da relação. Duas codificações de modelo foram comparadas e 19 divergências/questões foram adjudicadas por humano. O gate final confirma a primitiva dirigida ancorada em provisão com revisões: decomposição por ação jurídica, pareamento ação-destinatário, separação entre efeitos e arestas de ator, tratamento de modalidade e decomposição de provisões compostas. A validação estendida independente ainda está pendente; o resultado não estabelece intercoder reliability humano nem autoriza migração de produção. [Evidence: `PILOT_03_FINAL_REPORT.md`; `HUMAN_DECISION_LOG.csv`; manifest.]

R4 transferiu a unidade `LEGAL PROVISION × ACTOR × LEGAL ACTION` para GDPR, DSA e AI Act, com textos oficiais congelados e cópias de processamento rastreáveis. Produziu 1.404 registros (485/424/495). A etapa é estrutural: não atribui regulador, intermediário, alvo, RIT ou mecanismo. A QA inicial preparou amostra de 90, mas deixou revisão humana pendente; checks de ponteiro/excerpt são mecânicos. Etapas posteriores preservam calibração e saídas históricas, derivam regras de diagnóstico e revisam amostras direcionadas.

A revisão avançada apontou erros de span, cópia entre frases nos campos counterpart/recipient e colapso de predicados coordenados. Auditoria posterior descobriu que interface Action mostrava rótulo normalizado sem `LEGAL_VERB` e `MODALITY`, então julgamentos de modalidade foram submetidos a sensibilidade, sem sobrescrever o resultado congelado. Como a seleção é purposiva, proporções não estimam prevalência. Igualdade de counterpart e recipient foi interpretada como colapso operacional de dois papéis, não redundância conceitual. A compressão não gerou templates incondicionalmente validados e houve discordâncias e controles defeituosos; recomenda-se não reparar o corpus agora. Ainda faltam RIT/mecanismos, consulta independente a Rotem e comparação substantiva verde-digital. [Evidence: `R4_2_METHOD_NOTE.md`, `R4_2B_QA_REPORT.md`, `R4_2E_B1_METHOD_REPORT.md`, `R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md`.]

R2.1 escolheu o Regulamento Taxonomia 2020/852 para replicação instrument-first, separando-o de Pilot A e mantendo cinco casos R3 fora do escopo. RD-001 documenta D1–D8, firewall e a pendência de localizar fontes antes da análise substantiva. O feedback original de David não foi localizado conforme o próprio log. [Evidence: `WORK_2_1/PILOT_R2_1/RESEARCHER_DECISION_LOG.md`; `FIREWALL_REGISTER.csv`.]

ARQGOV registra leitura e reconstrução de oito dimensões e 83 entradas conceituais, relações e lacunas operacionais, modelo interativo em inglês e nota técnica. É interpretação proposta para revisão, não endosso. A trilha Rotem mantém separada codificação e teoria; o workbook recente contém cinco casos e 16 eventos e a revisão Codex não é decisão humana. O closeout relata envio em 1 out, mas arquivo email local é rascunho pré-despacho sem cópia independente da mensagem enviada. [Evidence: `RESEARCH_CLOSEOUT_2026-10-01.md`; notices e manifests.]

## 4. Agentes, pessoas e validação

Prompts, `ai_runs`, execution logs e notas descrevem uso de automação/modelos. R4 distingue Luna solicitada de variante não exposta, review Terra, autocheck reclassificado e continuidade em Claude, onde modelo solicitado e runtime relatado são mantidos separados. Os documentos não bastam para reconstituir sessões completas ou atribuir commits individualmente a um agente. O autor Git `cairesmachado-svg` é metadado de commit, não identidade do operador de ferramenta. Relatório de atividade separa ações diretamente documentadas, inferências e não atribuídas.

Gates humanos documentados: 19 adjudicações PILOT_03; aceitação humana do corpus R4; amostra inicial R4 sem adjudicação humana; fases posteriores com revisão específica; decisões R2.1. Checks automáticos não são validação científica. ARQGOV depende de feedback externo. Não se elevou `ONTOLOGY_STABLE_WITH_REVISIONS` a validação completa.

## 5. Produtos, entregas e cronologia

O registro de deliverables inclui 1.421 documentos, dados, scripts, interfaces e pacotes. Entre eles estão propostas e relatórios, codebooks, bases e registros de decisão, prompts/schemas, relatórios R4, pacote `ENVIO_R4_TO_DAVID`, pacote Rotem e snapshots em `Enviados/`. Preparação de pacote não prova transmissão. Para ARQGOV, envio é relatado pelo usuário, sem verificação independente. Para R4, pacote preparado e manifestados, sem evidência local independente de envio.

Git alcançável abrange 12 set–1 out; clone registrado em 29 set limita a recuperação de períodos anteriores. Marcos documentais incluem R2.1 em 19 set; R4 em 26–27 set; pacotes Rotem em 29–30 set; closeout ARQGOV em 1 out. SHAs, pais e paths estão nos CSVs de mudanças e na linha do tempo. mtime é apenas timestamp de sistema de arquivos.

## 6. Esforço, pendências e limitações

Há volume e complexidade substanciais, sem cálculo de horas defensável. Tempos automatizados não equivalem a esforço humano; datas e contagens de commits não viraram horas. O benchmark de 80 horas permanece não verificado.

Pendências: feedback externo; validação estendida das regras PILOT_03; recuperação do feedback original de David; gate de fontes R2.1; adjudicação de regras e eventual reparo R4; codificação RIT/mecanismos, consulta independente a Rotem e comparação verde-digital. Há lacunas de sessões agentivas, email transmitido, extração interna de binários e duração por tarefa. Presença de arquivo não prova autoria, submissão ou validação.

## 7. Síntese

O projeto construiu corpus rastreáveis, cleanroom, pipelines de extração, pilotos de codificação, trilhas de decisão humana e uma validação estrutural digital que identificou limites reais da representação. Sua contribuição atual é metodológica e arquitetural, com gates explícitos que evitam converter saída automática em inferência científica sem revisão. O estado local documentado é consolidação e espera por revisão, não produção final validada.
