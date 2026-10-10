# PROMPT PARA COLAR NO VS CODE — ABERTURA CONTROLADA DE V8-COMP-01

Atue como assistente de pesquisa e desenvolvimento metodológico do projeto PRJ-David. Execute **nesta sessão do VS Code**, com trabalho local verificável, a abertura de uma nova etapa de investigação chamada `V8-COMP-01 — Comparative Architectural Inference Pilot` (registro de desenho: 2026-10-04). Trabalhe com rigor científico, transparência de evidências, sem agentes paralelos e sem modificar arquivos congelados.

## Contexto e decisões já tomadas

1. A referência conceitual única é a versão de 3 de outubro de 2026 do manuscrito de David Levi-Faur, *Law and the Architectures of Governance: Towards a Relational Leximetrics Approach* (V8). Não derive uma ontologia alternativa de versões antigas.
2. No email de 4 de outubro de 2026, David orientou tratar o exercício do GDPR como **piloto metodológico**, compartilhar o material com a equipe e testar em **duas ou três leis suficientemente diferentes** se o protocolo arquitetural explícito fornece inferências **melhores, mais claras ou mais defensáveis** do que V8 aplicado sozinho. Ele incentivou a revisão de V8, o estudo de regulatory intermediaries e a integração entre teoria, método e banco de dados. Ele **não escolheu as três leis aqui propostas** nem aprovou artigo teórico separado.
3. Igor já comunicou ao grupo sua disposição para colaborar e pediu sugestões de novas legislações, casos e rumos teóricos; a mensagem enviada e respostas posteriores devem ser verificadas documentalmente antes de transcrição. Não fabrique respostas de David, Rotem, Ivana, Nir, Michael ou outros.
4. Igor aceitou registrar **provisoriamente** três casos de máxima variação teórica: (a) MDR, EU 2017/745 (intermediation/gatekeeping); (b) DSA, EU 2022/2065 (autoridade distribuída, plataformas e arranjos mistos); (c) Lei brasileira 13.848/2019 (regulação das próprias agências, autonomia e accountability). Ordem inicial: MDR → DSA → Lei 13.848. GDPR é antecedente metodológico, **não dataset validado**; AI Act e CNJ são casos-reserva.
5. Tenho um pacote de registro composto por `01_RESEARCH_PROTOCOL.md`, `02_RESPONSE_AND_DECISION_REGISTER.md`, `03_VSCODE_EXECUTION_PROMPT.md` e `04_RESPONSE_LOG_TEMPLATE.csv`. Se estiver disponível no workspace, leia esses arquivos como especificação pré-registrada. Se não estiver, implemente o desenho integralmente a partir deste prompt; não alegue ter lido anexos inexistentes.

## A. Primeiro, reconhecimento seguro e integridade do repositório

- Localize o workspace/repositório canônico `PRJ-David/Prf-David` (historicamente referido por Igor como `G:\Meu Drive\PRJ-David\Prf-David`, mas confirme o caminho real em vez de presumir acesso a essa unidade).
- Inspecione a árvore de diretórios, documentação-mestre, estado de Git (`git status` se aplicável), versões existentes de V8, manuscritos anteriores, trabalho de Rotem, pilotos de GDPR e `PILOT_03`. Registre caminho, status e hashes dos arquivos protegidos que encontrar. Não realize commits, push, rebases, alterações de branch, limpeza destrutiva nem instalações desnecessárias.
- Preserve integralmente, em modo somente leitura, V8 original, ontologia congelada, PILOT_03, adjudicações, código de Rotem, base de GDPR, preprints e backups existentes. Nenhum teste aqui autoriza escala produtiva ou mudança retrospectiva de evidência.
- Crie um diretório **novo, não conflitante** para esta etapa, preferencialmente `COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04/` sob a raiz canônica. Se a estrutura existente tiver convenção mais apropriada, respeite-a e documente a escolha. Não sobrescreva arquivos homônimos; crie revisão versionada quando necessário.

## B. Registro institucional: instalar o protocolo e o acompanhamento das respostas

Na nova pasta, crie ou importe, com conteúdo substancial, no mínimo:

- `README.md` — objetivo, status, desenho A/B, mapa dos artefatos, links para versões-fonte, contato do projeto e instruções de retomada.
- `RESEARCH_PROTOCOL_v0_1.md` — desenho completo: questão de valor incremental do protocolo; H0/H1 e possibilidade de resultado negativo; variação de casos; critérios de delimitação; procedimento de oito operações; evidência compartilhada; trilhas A e B; rubrica de comparação; gates G0–G6; limites das conclusões.
- `RESPONSE_AND_DECISION_REGISTER.md` — transcreva **apenas o que tiver fonte**. Inicie com a direção documentada no email de David (04/10/2026), notas anexas de ChatGPT com a ressalva de que David não adotou todas as recomendações, relato de email grupal de Igor sem fingir ter prova do texto final, e aceitação da proposta de abrir este experimento. Reserve entradas `AWAITING_EVIDENCE` para respostas futuras de Rotem, Ivana, Nir, Michael, David e demais colegas.
- `RESPONSE_LOG.csv` — cabeçalho/seed estruturado com ID, data, ator, canal, direção, fonte, modo `verbatim/paraphrase/reported`, proposta, racional teórico, status decisório, decisor, impacto e follow-up. Atualizações **append-only**. Receber sugestão não significa aprová-la.
- `CASE_SELECTION_AND_AMENDMENTS.md` — tabela provisória MDR/DSA/Lei 13.848; por que diferem; vieses de seleção; casos-reserva; protocolo explícito para incorporar sugestões futuras sem reescrever retrospectivamente o plano inicial.
- `SOURCE_MANIFEST.csv` — nome, tipo de fonte, origem/caminho ou URL oficial, versão e estado jurídico, data de acesso, checksum local, estado `VERIFIED | PENDING | UNAVAILABLE`.
- `EXECUTION_LOG.md` — linha do tempo com ações realmente executadas, arquivos criados, hashes de snapshots, erros, decisões técnicas e gates atingidos.
- Subpastas `01_MDR/`, `02_DSA/`, `03_LEI_13848/`, `TEAM_FEEDBACK/`, `QA/` e `RUN_LOGS/`. Deixe DSA/Lei 13.848 em `NOT_STARTED`; não invente resultados.

Fontes documentais locais a procurar, caso estejam no workspace: V8 de 03/10/2026 (`draft v8   Law_and_Governance_Architectures_Revised.docx` ou equivalente), anexo de David (`how the chat read Igor september 4.docx` ou equivalente), registros existentes do GDPR, e eventual cópia efetivamente enviada do email grupal. Arquivos vistos apenas numa conversa de ChatGPT **não estão automaticamente presentes no computador**. Identifique `SOURCE_PENDING` quando ausentes.

## C. Dar início ao MDR: primeiro micro-piloto, sem extração maciça

1. Use o MDR, Regulation (EU) 2017/745, como primeiro caso. Ponto oficial inicial: `https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng`. Verifique texto vigente/consolidado, emendas, data da versão, idioma e identificadores legais. Comece pelos arts. **35–45 e 52 como escopo CANDIDATO**, sem assumir que bastam; registre cross-references necessárias. Se a versão legal oficial não puder ser consultada ou conferida, crie apenas o plano e marque `SOURCE_PENDING`: é proibido preencher linhas jurídicas de memória ou sinteticamente.
2. Crie `01_MDR/MDR_SOURCE_CONTROL.md` e `01_MDR/MDR_BOUNDARY.md` com unidade de análise (configuração de intermediação/conformidade), critérios de inclusão/exclusão, hipóteses e racional teórico. Não confunda nomeação de atores com evidência de vínculos jurídicos entre eles.
3. Se, e somente se, os dispositivos estiverem confirmados, selecione uma amostra inicial pequena de aproximadamente **8–12 statements candidatos**, fonte a fonte. Use V8 para gerar `MDR_SHARED_EVIDENCE.csv` com IDs, texto/fonte/provisão, atores, funções, mecanismos, instrumentos, status de vínculo (assignment/qualified relation), condição, direção, authority/discretion/accountability quando explícitos, justificativa e lacunas. Conserve IDs fonte e relações many-to-many quando aplicável. Explique método da seleção; 8–12 não é meta que justifique inventar conteúdo.
4. Faça QA do conjunto de evidências, congele uma cópia com SHA-256 e registre a data. Ambas as trilhas **têm de usar o mesmo snapshot**.
5. Produza **primeiro** `MDR_TRACK_A_V8_ONLY.md`: inferências conforme V8, com regras de agregação, arquitetura e *stopping rule* que V8 já fornece. Salve hash e não reescreva após ver Track B. Depois produza `MDR_TRACK_B_V8_PLUS_8OPS.md`: aplique explicitamente delimitação, decomposição, reconstrução relacional, reconstrução configuracional, posição/sequência, atribuição parte–todo, inferência arquitetural e análise de sensibilidade. As oito operações são hipótese metodológica complementar, não conceitos que se possa atribuir indevidamente a David.
6. Produza `MDR_A_B_COMPARISON.md` com uma matriz claim-by-claim: evidência comum, conclusão A, conclusão B, diferença, suporte jurídico, suposto ganho de clareza/defensibilidade, erro evitado ou introduzido, sensibilidade ao recorte e custo adicional. Rótulos possíveis: `B_IMPROVES`, `B_CLARIFIES_ONLY`, `B_EQUIVALENT`, `B_WORSE`, `UNRESOLVED`. Não force inovação nem índice sintético não validado.
7. Em `QA/MDR_VALIDATION.md`, audite: texto e versionamento; directionality; falsa edge a partir de obrigação unilateral; conditionality; artigos constitutivos dispersos; propriedade do ator versus configuração; deslizamento lei→regime; claims sobre implementação indevida; rastreabilidade vertical; independência entre A e B. Human review é pendente até alguém efetivamente revisar.

## D. Critérios obrigatórios e respostas do grupo

- Documente qualquer novo comentário do grupo como entrada com fonte e status `OPEN`; se recomendar outra legislação, registre seu valor para variação teórica e eventual efeito na seleção, mas preserve a escolha de 04/10 como histórico. Mudanças relevantes exigem `PROTOCOL_AMENDMENT_NNN.md` com data, justificativa, decisor e etapa afetada.
- A comparação **principal é intra-caso A versus B**, nunca MDR versus DSA como se fossem objetos homólogos apenas porque ambos são regulamentos europeus. A comparação transversal serve para explorar transferibilidade e limites.
- V8 contém conceitos de relevância arquitetural, intermediação, regras de inferência e rastreabilidade vertical: não os apresente como invenções do novo protocolo. O ganho deve ser demonstrado, não afirmado.
- Separe `V8_DEFINED`, `OPERATIONAL_SPECIFICATION` e `METHOD_HYPOTHESIS` em todos os novos campos relevantes.
- Mantenha estado geral `DESIGN_REGISTERED`, passando a `MDR_SOURCE_VERIFIED`, `MDR_SHARED_EVIDENCE_FROZEN` e `MDR_A_B_EXPLORATORY_COMPLETE` **somente após completar realmente cada gate**. Se faltar fonte, `BLOCKED_SOURCE_PENDING` é um resultado correto.

## E. Relatório final obrigatório ao terminar esta execução

Exiba no terminal/resposta um **closeout auditável** em português, contendo (i) caminho real da nova pasta; (ii) lista de arquivos criados e quais já estavam disponíveis; (iii) fontes presentes/ausentes e a versão oficial jurídica verificada; (iv) decisões documentadas versus propostas e feedback ainda pendente; (v) gates G0–G4 realmente cumpridos ou bloqueados; (vi) resultados A/B apenas se houve duas inferências de fato; (vii) divergências, incertezas e riscos; (viii) estado Git antes/depois e hashes de proteção quando disponíveis; (ix) próximos dois passos objetivos. **Não diga que o piloto foi concluído se apenas preparou seus arquivos.**

Comece agora por reconhecimento do workspace e execução de G0. Em seguida tente G1–G4, sequencialmente e sem extrapolar os dados disponíveis. Não peça confirmação para criar apenas os novos arquivos metodológicos; em caso de risco de sobrescrita, preserve os originais e documente o bloqueio.
