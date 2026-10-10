# Reconstrução do trabalho científico e metodológico

## 1. Formação do problema e desenho inicial

O acervo `Before_R2/` reúne candidatura/proposta, notas teóricas sobre intermediação regulatória, desenho de corpus EUR-Lex, protocolos de screening e codificação e sucessivas entregas. Entrega-01/PoC construiu uma primeira representação de instrumentos ambientais/climáticos, dicionário, codebook RIT, screening e amostras. Entregas v3 e v4 ampliaram a arquitetura em estágios, os esquemas JSON, prompts, scripts de coleta/triagem e validação, além de conjuntos derivados e relatórios. A presença de múltiplas cópias com nomes de PoC e entrega indica evolução e preservação; datas de criação humana não podem ser deduzidas de timestamps correntes. [Evidence: `Before_R2/Estudos Preliminares e testes/`; commit inicial `27ba3e4`]

## 2. Passagem para cleanroom e evidência empírica

`Before_R2/dataset-eurlex/` e `dataset-eurlex-cleanroom/` separam corpus, codificação humana, tentativas de revisão, scripts, protocolo e rastreabilidade. Há fontes oficiais, manifests e revisões por caso, incluindo tentativas que ficaram arquivadas. O desenho preserva regras, decisões humanas e resultados de agentes separados, em vez de tratar uma codificação como verdade automática. Este histórico anterior é material de baseline, não um experimento recente reexecutado nesta auditoria. [Evidence: `Before_R2/dataset-eurlex/README_PRODUCTION.md`; `Before_R2/dataset-eurlex-cleanroom/AGENTS.md`; manifests em `cases/`]

## 3. Pilotos relacionais e adjudicação da ontologia

PILOT_01–02 estabelecem procedimentos, casos, comparação e manifests. PILOT_03 comparou duas codificações independentes de modelo e submeteu 19 questões de ontologia a adjudicação humana. A auditoria contou 19 linhas em `HUMAN_DECISION_LOG.csv`; 14 têm `backward_impact_flag=YES`. O relatório final mantém o gate `ONTOLOGY_STABLE_WITH_REVISIONS`: confirma uma primitiva direcional ancorada em disposição, mas requer decomposição por ação juridicamente distinta, correspondência ação-destinatário, separação entre efeitos jurídicos e arestas de ator, status intermediário sensível à modalidade e decomposição de provisões compostas. A nova decomposição ainda precisa de validação estendida independente; gate não autoriza produção nem prova confiabilidade entre humanos. [Evidence: `RELATIONAL_LEXIMETRICS_PILOT/PILOT_03/08_RESULTS/PILOT_03_FINAL_REPORT.md`; `07_HUMAN_ADJUDICATION/HUMAN_DECISION_LOG.csv`; manifest final.]

## 4. R4: transferência estrutural para direito digital

R4 toma como baseline cinco instrumentos verdes de R3, preservados em arquivo histórico, e examina GDPR, DSA e AI Act em textos oficiais congelados. A fase 4.2 limita-se à unidade **LEGAL PROVISION × ACTOR × LEGAL ACTION** e declara expressamente não produzir regulador/intermediário/alvo, RIT ou mecanismos. A extração documentada produziu 1.404 linhas: 485 GDPR, 424 DSA e 495 AI Act, cobrindo artigos, recitais e anexos. Fonte, estrutura e procedência são retidas; normalização é descritiva. [Evidence: `R4_2_METHOD_NOTE.md`; `R4_DIGITAL_CORPUS_REGISTER.csv`; arquivos `02_sources/` e `03_extraction/`.]

A primeira QA preparou amostra estratificada de 90, mas o relatório R4.2B informa que nenhuma linha recebeu revisão humana assinada; testes de ponteiro e excerpt são mecânicos e não demonstram correção semântica. Fases posteriores documentam calibração, revisão diagnóstica e uma sequência de triagem/compressão/revisão avançada, congelando saídas anteriores em vez de sobrescrever a extração. A auditoria de sensibilidade do campo Action descobriu problema de representação: a interface exibia rótulo normalizado `LEGAL_ACTION`, omitindo `LEGAL_VERB` e `MODALITY`; a releitura alterou contagens específicas e manteve a versão congelada. O memo limita explicitamente os achados a amostra purposiva e análise estrutural, sem extrapolar taxa de erro populacional ou comparação substantiva verde-digital. [Evidence: `R4_2B_QA_REPORT.md`; `R4_2E_B1_METHOD_REPORT.md`; `R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md`.]

Resultados R4 relevantes incluem erros de span, cópia relacional entre frases, colapso de predicados coordenados e a distinção real entre counterpart e recipient apesar de igualdade operacional original dos campos. A compressão de famílias não obteve templates incondicionalmente validados conforme o memo; o relatório recomenda não iniciar reparo corpus-wide. Regulator/intermediary/target coding, mechanism coding e comparação governança permanecem não iniciados. [Evidence: memo R4, seções 5–12; `R4_2E_B1_FINAL_SUMMARY.csv`; `R4_2E_B1_HANDOFF_STATE.md`.]

## 5. R2.1 e recuperação de proveniência

`WORK_2_1/PILOT_R2_1/` cria replicação metodológica centrada no instrumento Taxonomy Regulation 2020/852, distinguindo-a dos três casos anteriores e fechando por firewall cinco casos de R3. O log de decisão de 19 set registra escolha humana do instrumento, preservação da questão CBAM/EUDR como fora do escopo, separação de Pilot A e R2.1 e condição de início dependente de localização dos materiais. A auditoria de fase 0B documenta resolução de fontes, mas o portão indicado no log continua pendente de aceitação/acesso antes da análise substantiva. [Evidence: `RESEARCHER_DECISION_LOG.md`; `PHASE_0_AUDIT_REPORT.md`; `PHASE_0B_TAXONOMY_SOURCE_RESOLUTION.md`; `FIREWALL_REGISTER.csv`.]

## 6. ARQGOV: reconstrução teórica e suspensão

O closeout de 1 out 2026 registra duas trilhas: reconstrução da proposta de David (oito dimensões fundacionais, 83 entradas de tabela conceitual, relações e definições operacionais incompletas, arquitetura interativa e nota técnica) e alinhamento metodológico com evidência/pilotos de Rotem. A arquitetura é explicitamente uma interpretação proposta para revisão, sem endosso de autores. O estado é `EXTERNAL_REVIEW_PENDING`, com despacho reportado pelo usuário, não verificado independentemente. O ciclo documental está suspenso até resposta; sem produção, revisão de manuscrito ou reclassificação. [Evidence: `RESEARCH_CLOSEOUT_2026-10-01.md`; `EXTERNAL_REVIEW_REGISTER.md`; `RESUMPTION_PROTOCOL.md`.]

## Limites científicos

Não se inspecionaram sistematicamente todos os dados linha a linha, não se reexecutaram modelos e não se verificaram envios em contas externas. Relatórios de fase são evidência do que foi declarado e produzido; seu conteúdo não substitui replicação, auditoria estatística independente ou parecer científico externo.
