<!-- DERIVED TEXT — not an original. SOURCE_ID=SRC-PROTO-IA; source=G:/Meu Drive/PRJ-David/Prf-David/R4_CROSS_DOMAIN_VALIDATION/00_protocol/PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx; SHA256=89CE912545063B41EA37532D32E93F800D6AEAE8BA0A4FE7BC0EA860B289163B; SOURCE_STATUS=HISTORICAL; transformation=python-docx paragraph+table extraction in document order, paragraph numbering [¶n] added by this run; extracted_at=2026-09-30T20:51:56-03:00 -->

[¶1] PROTOCOLO DE USO DE INTELIGÊNCIA ARTIFICIAL

[¶2] Reconstrução metodológica R1–R3 e padrão de governança para o R4

[¶3] Regulatory Intermediation Research Project
Igor Caires Machado | Projeto PRJ - David Levi-Faur

[¶4] Versão 1.0 — 25 de setembro de 2026

[¶5 TABLE]
| Status do documento
Este protocolo é uma reconstrução metodológica do uso de IA até o encerramento do R3 e, ao mesmo tempo, estabelece regras prospectivas para o R4. A arquitetura histórica principal está documentada da seguinte forma: GPT-5.6 Luna High para etapas simples e repetitivas, visando custo-benefício; GPT-5.6 Terra High para casos complexos, leitura jurídica substantiva e identificação/classificação de mecanismos. Lacunas residuais dizem respeito principalmente ao logging granular de prompts e execuções, não à divisão geral de trabalho entre os modelos. |
|---|

## [¶6] Resumo executivo

[¶7] Este documento formaliza como a inteligência artificial foi incorporada ao projeto de pesquisa sobre intermediação regulatória nas rodadas R1–R3 e define um padrão auditável para o R4. A IA foi usada como instrumento de descoberta, extração, classificação assistida, comparação, revisão e automação do pipeline; as decisões científicas substantivas permaneceram — e devem permanecer — sob responsabilidade humana.

[¶8] A distinção crucial é entre tarefas de baixa inferência (por exemplo, localizar dispositivos, extrair referências, normalizar campos e produzir candidatos) e tarefas de alta inferência (por exemplo, decidir se um ator é efetivamente intermediário, definir a relação R–I–T, distinguir mecanismos sobrepostos e interpretar funções implícitas). Quanto maior a inferência teórica, maior deve ser a intervenção humana.

[¶9] O R4 deverá começar apenas depois de congelado este protocolo e de adotado um registro sistemático de modelo, prompt, versão do codebook, evidência jurídica, confiança e decisão humana. Isso permitirá que a comparação Green × Digital seja, ao mesmo tempo, um teste do framework de intermediação e um experimento sobre a divisão epistemicamente adequada de trabalho entre pesquisador e IA.

## [¶10] 1. Objetivo e princípios

[¶11] O protocolo tem cinco objetivos: documentar o uso histórico de IA; explicitar a divisão de funções entre pesquisador e sistemas de IA; padronizar a extração e a codificação de mecanismos; aumentar a rastreabilidade das decisões; e preparar um desenho comparável para o R4.

[¶12] IA como instrumento de pesquisa, não como autoridade científica autônoma.

[¶13] Evidência jurídica primária precede classificação teórica.

[¶14] Proveniência deve acompanhar toda classificação substantiva.

[¶15] A IA pode propor; a decisão final sobre casos ambíguos é humana.

[¶16] Mudanças de modelo ou de prompt são mudanças metodológicas e devem ser registradas.

[¶17] Discordância entre humano, modelos ou codificadores é informação analítica, não ruído a ser apagado.

[¶18] Automação é desejável apenas quando não reduz validade conceitual e transparência.

[¶19 TABLE]
| Regra de ouro / Nenhuma classificação de “intermediário” ou de “mecanismo de intermediação” deve ser aceita apenas porque foi produzida com alta confiança por um modelo. A classificação precisa estar ancorada em função relacional, evidência jurídica e regra de codificação explícita. |
|---|

## [¶20] 2. Reconstrução do uso de IA nas rodadas R1–R3

[¶21] A reconstrução abaixo combina registros do projeto, artefatos produzidos e decisões metodológicas documentadas nas conversas de trabalho. O objetivo não é reescrever o passado como se houvesse logging completo desde o início, mas identificar de forma verificável onde a IA entrou no processo e quais lacunas de rastreabilidade devem ser corrigidas a partir do R4.

[¶22 TABLE]
| Etapa | Função da IA | Função humana | Limitação documental |
|---|---|---|---|
| R1 — população e corpus | Busca assistida, formulação/refino de queries e strings, triagem de candidatos, apoio à verificação de atos e produção do relatório metodológico. | Delimitação do universo, escolha do corpus, validação de fontes oficiais, aceitação/rejeição de candidatos e redação científica final. | GPT-5.6 Luna High foi o modelo padrão para tarefas simples, repetitivas e de triagem. Quando a tarefa exigia interpretação mais complexa, a análise era escalada para GPT-5.6 Terra High. |
| R2 — calibração conceitual | Extração estrutural, identificação de atores e relações, geração de candidatos a intermediários, apoio à classificação e revisão tabular. Houve auditoria com Claude em ambiente Excel. | Decisões sobre casos limítrofes, critérios de intermediação, aceitação de papéis institucionais, múltiplos papéis e regras de calibração. | GPT-5.6 Luna High foi usado nas operações simples e estruturadas; GPT-5.6 Terra High, nos casos complexos, leitura jurídica e decisões substantivas. Houve também auditoria complementar com Claude em ambiente Excel. |
| R3 — clean-room / consolidação | Apoio à consolidação LAW × INTERMEDIARY, codificação de mechanism events, rastreamento de evidência, reconciliação de registros, auditoria/adjudicação assistida e geração de pacotes. O trabalho operacional foi executado em ambiente de desenvolvimento (VS Code/Codex) com arquivos internos de pipeline. | Congelamento do corpus, definição das unidades analíticas, validação de mecanismos, adjudicação de ambiguidades e decisão sobre o que compõe o dataset entregue. | A consolidação operacional e tarefas simples seguiram com GPT-5.6 Luna High; a leitura substantiva, identificação/classificação de mecanismos e adjudicação de casos complexos foram conduzidas com GPT-5.6 Terra High. O workbook final permanece deliberadamente limpo, exigindo consulta aos artefatos internos para proveniência detalhada. |
| Pré-R4 — desenho comparativo | Discussão metodológica sobre transportabilidade do codebook, comparação Green × Digital e desenho de teste humano–IA. | Definição do protocolo, critérios do experimento e fronteira entre automação e análise qualitativa. | A partir daqui, o logging de modelo, nível de reasoning, prompt, input, output e decisão humana passa a ser requisito formal, preservando a arquitetura de escalonamento Luna High → Terra High. |

## [¶23] 3. Registro de modelos, interfaces e ambientes

[¶24] O projeto utilizou mais de uma interface e mais de um modelo de IA. É importante distinguir “modelo” de “ambiente”: VS Code/Codex e Excel são ambientes de trabalho; GPT-5.6 Luna High, GPT-5.6 Terra High e Claude são modelos/famílias usados em funções distintas. Nas etapas simples e repetitivas, o padrão histórico foi GPT-5.6 Luna High, escolhido pela melhor relação custo-benefício. Nos casos complexos, especialmente leitura jurídica substantiva e identificação/classificação de mecanismos de intermediação, o padrão foi GPT-5.6 Terra High. Claude foi utilizado adicionalmente em auditorias específicas no Excel.

[¶25 TABLE]
| Modelo/ambiente | Status | Uso | Limitação | Regra futura |
|---|---|---|---|---|
| ChatGPT / OpenAI | Confirmado como ambiente principal de análise e diálogo metodológico ao longo do projeto. | Execuções com dois níveis principais: GPT-5.6 Luna High para tarefas simples/repetitivas; GPT-5.6 Terra High para tarefas complexas, leitura jurídica e mecanismos. | Nem todas as execuções iniciais preservaram log granular de prompt, timestamp e contexto. | Registrar em cada execução: modelo, reasoning effort, prompt, etapa, input, output e decisão humana. |
| Claude em Excel | Confirmado no processo de auditoria do workbook durante a calibração. | Revisão/auditoria de codificação tabular e identificação de inconsistências ou casos para decisão. | Versão exata e configuração não consolidadas no log histórico. | Manter como segundo codificador/validador apenas quando o desenho exigir independência; registrar versão e prompt. |
| Codex / VS Code | Confirmado como ambiente operacional do pipeline nas fases avançadas. | Execução de scripts, manipulação de arquivos, reconciliação, geração de outputs e apoio agentic ao workflow. | O ambiente não equivale a um modelo; versão do modelo subjacente precisa ser registrada separadamente. | Logar modelo, commit, prompt de tarefa, arquivos de entrada e saída. |
| GPT-5.6 Luna — High | Confirmado como modelo histórico para etapas simples e repetitivas, com foco em custo-benefício. | Triagem, estruturação, extrações diretas, normalização, reconciliação e outras tarefas de baixa ou média complexidade interpretativa. | Não deve ser usado como único modelo quando a tarefa envolve leitura jurídica complexa ou inferência substantiva sobre mecanismos. | Manter como modelo padrão de primeira linha para tarefas simples no R4. |
| GPT-5.6 Terra — High | Confirmado como modelo histórico para casos complexos e análise substantiva. | Leitura jurídica aprofundada, identificação e classificação de mecanismos de intermediação, casos ambíguos, adjudicação conceitual e análises de maior carga inferencial. | Custo superior ao Luna; deve ser acionado quando a complexidade interpretativa justificar o escalonamento. | Usar como modelo de escalonamento para tarefas complexas e, obrigatoriamente, para mecanismos e leitura jurídica substantiva no R4. |

## [¶26] 4. Divisão de trabalho humano–IA

[¶27 TABLE]
| Operação | Papel da IA | Papel humano | Regra |
|---|---|---|---|
| Descoberta de documentos | Alta | Baixa a média | IA expande termos, sugere rotas e organiza candidatos; pesquisador define escopo e valida fonte oficial. |
| Extração de dispositivos/evidências | Alta | Baixa | IA pode extrair artigos, parágrafos, atores e verbos normativos; humano verifica amostra, exceções e trechos críticos. |
| Normalização e deduplicação | Alta | Baixa | Automatizável, desde que regras sejam determinísticas e haja log. |
| Identificação de candidato a intermediário | Média/alta | Média | IA propõe candidatos com justificativa e evidência; humano decide quando há ambiguidade institucional ou relacional. |
| Definição R–I–T | Média | Alta em casos complexos | IA estrutura hipóteses; humano decide papéis sobrepostos, cadeias aninhadas e relações implícitas. |
| Identificação de mecanismo | Média | Alta | IA localiza verbos/funções e propõe mechanism event; humano valida a correspondência ao codebook. |
| Adjudicação de caso limítrofe | Baixa como decisão final | Muito alta | IA pode apresentar argumentos e alternativas; decisão final é humana e deve ser registrada. |
| Comparação entre domínios | Média | Alta | IA calcula padrões e produz síntese; pesquisador interpreta significado teórico e evita causalidade indevida. |
| Redação metodológica | Média/alta | Alta | IA pode estruturar e redigir; pesquisador assume autoria, valida exatidão e decide claims. |
| Código/automação | Alta | Média | IA pode produzir scripts; humano define especificação, valida saídas e preserva reprodutibilidade. |

## [¶28] 5. Protocolo específico para busca e codificação de mecanismos

[¶29] Os mecanismos são a zona de maior risco epistemológico do projeto: o texto legal raramente apresenta uma etiqueta pronta (“este é um mecanismo de intermediação”). Em geral, o mecanismo precisa ser inferido a partir de competências, obrigações, fluxos de informação, avaliações, verificações, monitoramento, certificação, auditoria ou outras funções. Por isso, a IA deve operar em duas camadas separadas: extração e interpretação.

### [¶30] 5.1 Camada A — extração de evidência

[¶31] Segmentar o texto por artigo, parágrafo, inciso/alínea, anexo ou recital quando relevante.

[¶32] Extrair atores expressamente nomeados e verbos que descrevem suas competências, deveres, poderes ou produtos.

[¶33] Registrar o objeto da ação (o que é monitorado, verificado, certificado, transmitido, avaliado etc.).

[¶34] Registrar destinatário/origem do fluxo quando textual ou juridicamente identificável.

[¶35] Preservar a referência jurídica exata e um trecho curto de evidência.

[¶36] Não atribuir ainda mecanismo definitivo quando a função depender de contexto relacional externo ao dispositivo.

### [¶37] 5.2 Camada B — interpretação relacional

[¶38] Perguntar quem exerce a função regulatória (R), quem é afetado ou regulado (T) e se existe um terceiro ator com função mediadora (I).

[¶39] Testar se I apenas participa do sistema ou se efetivamente transforma, transmite, verifica, avalia, monitora, certifica, coordena ou operacionaliza a relação regulatória.

[¶40] Identificar o mechanism event utilizando o codebook congelado.

[¶41] Registrar alternativas plausíveis quando dois mecanismos forem semanticamente próximos.

[¶42] Classificar a confiança e indicar se há necessidade de revisão humana.

[¶43] Submeter obrigatoriamente à adjudicação humana casos com função implícita, múltiplos papéis, cadeia aninhada, efeito não vinculante ou sobreposição de mecanismos.

[¶44 TABLE]
| Separação obrigatória / O sistema deve guardar três campos distintos: (1) TEXT/EVIDENCE — o que a norma diz; (2) AI PROPOSAL — como a IA propõe codificar; (3) HUMAN DECISION — a classificação científica adotada. Nunca sobrescrever a evidência com a interpretação. |
|---|

[¶45 TABLE]
| Campo mínimo | Função |
|---|---|
| case_id / CELEX | Identificação inequívoca do ato. |
| article / paragraph / annex / recital | Localização jurídica da evidência. |
| evidence_text | Trecho mínimo suficiente para sustentar a decisão. |
| actor_raw | Ator tal como aparece no texto. |
| actor_canonical | Entidade consolidada após normalização. |
| candidate_role | R, I, T ou combinação possível. |
| candidate_mechanism | Mecanismo proposto pela IA sob o codebook vigente. |
| mechanism_rationale | Explicação curta ligando função jurídica à categoria. |
| AI_model | Modelo exato e configuração/effort. |
| prompt_version | ID/versionamento do prompt utilizado. |
| AI_confidence | HIGH / MEDIUM / LOW; nunca substitui validação. |
| human_status | UNREVIEWED / ACCEPTED / MODIFIED / REJECTED / NEEDS_ADJUDICATION. |
| human_decision | Classificação final adotada. |
| decision_note | Razão da alteração ou confirmação quando relevante. |
| provenance_id | Ligação para arquivo/registro de origem e execução. |

## [¶46] 6. Gatilhos de revisão humana obrigatória

[¶47] Ator cumpre simultaneamente mais de um papel (por exemplo, regulador e alvo; alvo e intermediário).

[¶48] A relação R–I–T não aparece em um único dispositivo e depende de reconstrução entre artigos.

[¶49] A influência é indireta, consultiva, reputacional, voluntária ou não vinculante.

[¶50] O mecanismo poderia ser classificado de modo plausível em duas ou mais categorias.

[¶51] O intermediário é coletivo, em rede ou composto por uma cadeia de delegação.

[¶52] O ator é mencionado institucionalmente, mas a função mediadora não é expressa.

[¶53] A IA propõe uma nova categoria não prevista no codebook.

[¶54] A confiança do modelo é LOW, ou MEDIUM quando a decisão altera substantivamente a arquitetura do caso.

[¶55] Há divergência entre modelos/codificadores independentes.

[¶56] O trecho legal utilizado como evidência é insuficiente para sustentar a classificação sem contexto adicional.

## [¶57] 7. Pipeline de controle de qualidade

[¶58] INGESTÃO: adquirir a fonte oficial e registrar versão/identificador.

[¶59] EXTRAÇÃO: IA ou script produz candidatos com evidência rastreável.

[¶60] CLASSIFICAÇÃO ASSISTIDA: modelo aplica o codebook congelado e produz rationale + confiança.

[¶61] VALIDAÇÃO ESTRUTURAL: checar esquema, campos obrigatórios, duplicatas e integridade referencial.

[¶62] REVISÃO HUMANA: revisar todos os casos gatilho e uma amostra dos casos HIGH.

[¶63] ADJUDICAÇÃO: decidir divergências e registrar justificativa.

[¶64] LOCK: congelar a versão validada com hash/commit quando disponível.

[¶65] EXPORTAÇÃO: produzir dataset limpo para compartilhamento, mantendo separadamente o log interno de IA e proveniência.

[¶66] AUDITORIA: possibilitar reconstrução da decisão a partir do registro interno, mesmo que o produto externo seja simplificado.

## [¶67] 8. Práticas que devem ser evitadas

[¶68] Permitir que a IA altere silenciosamente o codebook para acomodar um caso difícil.

[¶69] Aceitar uma classificação sem referência jurídica verificável.

[¶70] Misturar extração factual e julgamento teórico no mesmo campo.

[¶71] Trocar de modelo durante uma rodada comparativa sem registrar a mudança.

[¶72] Usar a codificação de outro pesquisador como contexto antes de completar uma codificação que deveria ser independente.

[¶73] Apagar divergências depois da adjudicação; elas devem permanecer no log histórico.

[¶74] Descrever um output de IA como “ground truth”.

[¶75] Inferir retrospectivamente o nome ou a versão de um modelo quando o histórico não o prova.

[¶76] Usar confiança declarada pelo modelo como medida empírica de acurácia.

## [¶77] 9. Padrão obrigatório de logging a partir do R4

[¶78 TABLE]
| Campo | Conteúdo |
|---|---|
| run_id | ID único da execução. |
| timestamp | Data/hora da execução. |
| research_round | R4.x / fase. |
| model_provider | OpenAI, Anthropic etc. |
| model_name | Nome exato do modelo. |
| reasoning_effort / mode | Configuração utilizada, quando aplicável. |
| prompt_id + version | Versão imutável do prompt. |
| codebook_version | Versão do esquema/regras. |
| input_manifest | Arquivos/atos utilizados. |
| output_manifest | Outputs produzidos. |
| temperature / relevant settings | Registrar quando exposto pela interface. |
| human_reviewer | Responsável pela revisão. |
| review_status | Estado de validação. |
| commit/hash | Referência ao estado do repositório/arquivo quando disponível. |
| notes | Exceções, falhas, mudanças de modelo ou instruções emergenciais. |

[¶79 TABLE]
| Padrão recomendado para o R4
Adotar arquitetura de dois níveis: GPT-5.6 Luna High como modelo padrão para tarefas simples, repetitivas, estruturadas e de melhor relação custo-benefício; GPT-5.6 Terra High para casos complexos, leitura jurídica substantiva, identificação/classificação de mecanismos e adjudicação. O critério de escalonamento deve ser explícito e registrado. O mesmo codebook deve permanecer congelado durante a primeira codificação dos três casos digitais. Comparações com Claude ou outros modelos, quando realizadas, devem constituir braços experimentais separados. |
|---|

## [¶80] 10. Uso de IA como objeto do próprio experimento

[¶81] No R4, a IA não será apenas uma ferramenta; seu desempenho poderá ser analisado empiricamente. A estrutura proposta permite medir onde a IA é estável, onde depende de interpretação humana e onde diferentes modelos/codificadores divergem.

[¶82] Executar primeiro uma codificação independente, sem acesso à codificação de Rotem.

[¶83] Congelar a saída antes de qualquer reconciliação.

[¶84] Comparar decisões por unidade de análise, ator, R/I/T, mecanismo e evidência.

[¶85] Classificar a origem da divergência: extração, conceito, granularidade, interpretação jurídica, mecanismo ou erro.

[¶86] Calcular medidas de concordância apenas quando as categorias e unidades forem comparáveis.

[¶87] Tratar divergências qualitativamente relevantes como dados de pesquisa sobre os limites da automação.

## [¶88] 11. Responsabilidade científica e autoria

[¶89] A IA não assume autoria, responsabilidade metodológica ou julgamento científico. O pesquisador humano é responsável por definir a pergunta de pesquisa, escolher o corpus, aprovar o codebook, validar evidências, adjudicar ambiguidades, decidir claims e interpretar resultados. O uso de IA deve ser descrito de forma suficiente para que outro pesquisador compreenda onde houve automação e onde houve julgamento humano.

[¶90] Quando a IA for usada para redigir relatórios, a redação deve ser considerada assistência editorial/metodológica; todos os enunciados científicos permanecem sujeitos à verificação humana. Quando a IA for usada para gerar código, o código precisa ser testado contra outputs esperados e preservado no repositório para reprodução.

## [¶91] 12. Limitações da reconstrução histórica

[¶92] Este protocolo reconhece três limitações da fase R1–R3. Primeiro, embora a arquitetura principal de uso de modelos esteja agora documentada — GPT-5.6 Luna High para tarefas simples e GPT-5.6 Terra High para tarefas complexas, leitura jurídica e mecanismos — nem todas as execuções históricas preservaram um log granular de prompt, timestamp e contexto. Segundo, parte da auditoria ocorreu em interfaces externas (como Excel com Claude), sem consolidação automática de todos os prompts em um log central. Terceiro, os datasets finais destinados à comunicação científica foram intencionalmente simplificados e não carregam todas as colunas internas de coder/modelo/proveniência.

[¶93] Essas limitações não invalidam o trabalho já realizado, mas impedem que algumas etapas históricas sejam descritas com granularidade experimental retrospectiva. A resposta metodologicamente correta é preservar essa incerteza e adotar logging prospectivo completo a partir do R4.

## [¶94] 13. Matriz prática de decisão humano–IA

[¶95 TABLE]
| Situação | Procedimento | Regra de fechamento |
|---|---|---|
| Trecho explícito + função clara + categoria inequívoca | IA codifica; humano revisa por amostra. | Pode entrar em lote após QA. |
| Trecho explícito + duas categorias plausíveis | IA apresenta alternativas; humano decide. | Não fechar automaticamente. |
| Relação distribuída em vários artigos | IA reconstrói candidata; humano valida cadeia. | Exigir nota de rationale. |
| Intermediação implícita ou não vinculante | IA auxilia; humano decide. | Adjudicação obrigatória. |
| Novo fenômeno fora do codebook | IA registra como GAP; humano não cria categoria durante o teste. | Enviar ao stress-test log. |
| Divergência Igor × Rotem / modelo × modelo | Preservar ambas as codificações e adjudicar depois. | Não usar maioria automática como verdade. |

## [¶96] 14. Controle de versão do protocolo

[¶97] v1.1 — reconstrução R1–R3 + regras pré-R4.

[¶98] Qualquer alteração conceitual deve gerar nova versão (v1.1, v1.2 etc.).

[¶99] Mudança de modelo principal ou de prompt durante uma rodada requer registro explícito e justificativa.

[¶100] O protocolo utilizado para um dataset publicado deve ser preservado de forma imutável junto ao release correspondente.

[¶101] Exceções metodológicas devem ser registradas no momento em que ocorrem, não reconstruídas apenas ao final.

## [¶102] 15. Checklist de gate antes do R4

[¶103] ☐ R3 final e codebook identificados e congelados.

[¶104] ☐ Protocolo de IA v1.1 aprovado como baseline.

[¶105] ☐ Modelo principal definido e registrado.

[¶106] ☐ Prompt R4 versionado e congelado antes da codificação.

[¶107] ☐ Textos oficiais dos três atos digitais adquiridos e versionados.

[¶108] ☐ Estrutura de log criada antes da primeira execução.

[¶109] ☐ Codificação de Rotem mantida fora do contexto até o lock da codificação independente.

[¶110] ☐ Critérios de adjudicação e gatilhos humanos definidos.

[¶111] ☐ Plano de comparação Green × Digital separado da fase de extração/codificação.

[¶112] ☐ Outputs e commits preparados para reprodução.

## [¶113] Apêndice A — Glossário operacional

[¶114 TABLE]
| Termo | Definição operacional |
|---|---|
| Extraction | Recuperação/estruturação de elementos presentes na fonte sem pretensão de interpretação teórica final. |
| Classification | Aplicação de uma categoria previamente definida a uma unidade extraída. |
| Adjudication | Decisão humana formal em caso de ambiguidade ou divergência entre codificações. |
| Mechanism event | Ocorrência juridicamente sustentada de uma função pela qual um intermediário medeia a relação regulatória. |
| R–I–T | Estrutura relacional Regulador–Intermediário–Alvo. |
| Provenance | Trilha que conecta output, input, modelo, prompt, regra e decisão humana. |
| Codebook freeze | Bloqueio temporário das categorias/regras para testar transportabilidade sem adaptação oportunista. |
| Stress-test log | Registro de situações em que o codebook produz ambiguidade, redundância ou falta de cobertura. |
| AI-suitable | Tarefa com forte estrutura textual/determinística e baixa necessidade de julgamento teórico. |
| Qualitative-critical | Tarefa cujo resultado depende materialmente de interpretação institucional, jurídica ou teórica. |

## [¶115] Apêndice B — Template mínimo de registro de execução

[¶116] Cada execução substantiva do R4 deve produzir um registro equivalente ao seguinte:

[¶117 TABLE]
| Campo | Exemplo de preenchimento |
|---|---|
| run_id | R4_DSA_MEC_001 |
| date_time | 2026-09-25T...-03:00 |
| model | GPT-5.6 Luna High ou GPT-5.6 Terra High (conforme complexidade; registrar critério de escalonamento) |
| reasoning | High |
| prompt_version | R4_PROMPT_v1.1 |
| codebook | R3_FROZEN_<hash> |
| input | 32022R2065 official text |
| task | mechanism candidate extraction |
| human_reviewer | Igor Caires Machado |
| status | LOCKED / REVIEWED / NEEDS_ADJUDICATION |
| output | R4_MECHANISM_EVENTS_v... |
| notes | Exceções relevantes e divergências. |

[¶118 TABLE]
| Conclusão metodológica / O princípio orientador do projeto deve ser “AI for traceable assistance, human for scientific accountability”. O ganho científico do R4 não virá de maximizar automação, mas de identificar com precisão quais operações podem ser automatizadas sem perda de validade e quais exigem interpretação qualitativa. Esse limite é, ele próprio, um resultado de pesquisa. |
|---|
