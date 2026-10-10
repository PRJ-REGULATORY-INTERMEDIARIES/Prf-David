# EMENDAS PROPOSTAS AO PROTOCOLO — G0

**Data:** 2026-10-09 | **Origem:** avaliação G0 (agente de programação, sob coordenação humana) | **Estado:** PROPOSTAS — nenhuma foi aplicada.

Este arquivo **não altera** o protocolo. `PROTOCOL_v1_0_DRAFT.md`, `SEARCH_STRATEGY.md`, `CODEBOOK_AND_AUDIT.md`, `ANALYSIS_AND_VALIDITY.md`, `DECISIONS_TO_FREEZE.md` e os demais arquivos permanecem byte a byte como estavam (hashes em `outputs/BASELINE_RUN.md`). Cada emenda precisa de decisão humana registrada: **aceita / aceita com modificação / rejeitada**, com data e responsável.

**Gravidade**

- **CRÍTICA** — sem resolução, a revisão não é executável ou não é defensável em revisão por pares.
- **ALTA** — compromete reprodutibilidade ou validade de um componente; resolver antes do congelamento.
- **MÉDIA** — reduz transparência ou gera retrabalho; resolver antes da busca sistemática.
- **BAIXA** — redação, consistência ou conveniência.

## Quadro-resumo

| ID | Tema | Gravidade | Documento afetado |
|---|---|---|---|
| A01 | Ordem dos gates: congelar antes ou depois da calibração | CRÍTICA | PROTOCOL §9, DECISIONS, PREREGISTRATION, PROMPT_MESTRE |
| A02 | Tipologia operacional de unidades e regra de dataset canônico | CRÍTICA | PROTOCOL §5–6, CODEBOOK |
| A03 | Consultas não executáveis e plataformas sem consulta | CRÍTICA | SEARCH_STRATEGY, `inputs/search_queries.csv` |
| A04 | Regra de volume: quanto de cada busca será triado | CRÍTICA | PROTOCOL §8–9, SEARCH_STRATEGY |
| A05 | Equipe de avaliação e independência real | CRÍTICA | PROTOCOL §9 e §12, DECISIONS |
| A06 | Evidência congelada (snapshot) para triagem e auditoria | ALTA | PROTOCOL §9–11, CODEBOOK |
| A07 | Cegamento em relação às colunas de julgamento do inventário exploratório | ALTA | PROTOCOL §9, piloto |
| A08 | Circularidade entre a tipologia D0–D3 e a operacionalização RGAM | ALTA | PROTOCOL §3, §11, §14; CODEBOOK |
| A09 | Nível de aplicação dos critérios de auditoria (dataset × distribuição) | ALTA | CODEBOOK, esquema `audit.csv` |
| A10 | Divergência de critérios: 8 no protocolo, 9 no codebook | ALTA | PROTOCOL §11, CODEBOOK |
| A11 | Estatísticas de concordância e critério de passagem do piloto | ALTA | PROTOCOL §12, ANALYSIS, DECISIONS (G1) |
| A12 | Regras de deduplicação em dois níveis | ALTA | PROTOCOL §9 (S2, S5), CODEBOOK |
| A13 | Data de fechamento da busca e janela de execução | ALTA | PROTOCOL §7, SEARCH_STRATEGY |
| A14 | Etapas de triagem adaptadas a recursos sem título/resumo | MÉDIA | PROTOCOL §9, CODEBOOK |
| A15 | Reformulação das RQs 1, 3 e 5 | MÉDIA | PROTOCOL §2 |
| A16 | Justificativa da adaptação do PCC | MÉDIA | PROTOCOL §4 |
| A17 | Amostragem de portais nacionais e consulta a especialistas | MÉDIA | PROTOCOL §8, SEARCH_STRATEGY |
| A18 | Mapeamento explícito dos critérios aos princípios FAIR | MÉDIA | PROTOCOL §3 e §11, CODEBOOK |
| A19 | Lacunas PRISMA-ScR / PRISMA-S / JBI | MÉDIA | PROTOCOL §3, §8, §18 |
| A20 | Campos previstos no protocolo e ausentes no esquema | MÉDIA | PROTOCOL §8 e §10, esquema `data/` |
| A21 | Dados pessoais e termos de uso por fonte | MÉDIA | PROTOCOL §15 |
| A22 | Teste de recuperação de seeds × amostra de calibração | MÉDIA | SEARCH_STRATEGY |
| A23 | Seleção dos casos do subestudo exploratório RIT | MÉDIA | PROTOCOL §14 |
| A24 | Versionamento das evidências do G0 e dos payloads brutos | MÉDIA | `.gitignore`, README, DECISIONS |
| A25 | Idioma do protocolo registrado | BAIXA | PROTOCOL, PREREGISTRATION |
| A26 | Rótulo "verificadas" nas referências | BAIXA | PROTOCOL §18, SOURCES_VERIFIED |
| A27 | URL repetida e URLs de página explicativa nos seeds | BAIXA | `inputs/seed_inventory_v0_1.csv` (não alterar; anotar) |

---

## A01 — Ordem dos gates: congelar antes ou depois da calibração — CRÍTICA

**Problema.** Há definições incompatíveis do mesmo marco:

- PROTOCOL §9: "S0. Congelar protocolo antes de buscas sistemáticas" e, no fim da seção, "Calibração: 15–20 registros diversificados **antes** da triagem formal, com revisão das definições".
- DECISIONS_TO_FREEZE: G0 = "Protocolo v1.0 datado; repositório commitado; plano de registro público acordado"; G1 = piloto, com critério "Codebook estável".
- PREREGISTRATION_TEMPLATE: "campos a preencher **antes de G0**".
- PROMPT_MESTRE: G0 = nota de revisão + autorização para coleta.

Se o protocolo é congelado em G0 e o codebook só se estabiliza em G1, toda correção nascida do piloto vira emenda pós-registro e, pelo próprio §9, "demanda adendo datado e nova calibração". O piloto existe justamente para mudar definições.

**Proposta.** Separar dois marcos: **G0 = aprovação do desenho e autorização do piloto** (protocolo ainda DRAFT); **G1 = piloto concluído, definições revistas, protocolo congelado e registrado**. A busca sistemática (G2) só começa depois de G1. Ajustar o template de pré-registro para "antes de G2".

**Justificativa.** A orientação JBI prevê piloto das ferramentas de seleção e extração antes da aplicação; o PRISMA-ScR pede que o relato descreva se os formulários foram calibrados antes do uso (item 10).

**Impacto.** Sem custo de execução. Evita emendas pós-registro previsíveis e elimina a ambiguidade sobre o que "aprovar G0" autoriza.

## A02 — Tipologia operacional de unidades e regra de dataset canônico — CRÍTICA

**Problema.** O §5 define quatro níveis de identidade, mas não há regra de decisão para classificar um recurso concreto, e os critérios de inclusão não dizem o que fazer com classes que **já estão no inventário exploratório**:

- padrões de identificação e ontologias (EU05 ELI, EU23 ECLI);
- vocabulários controlados (EU06 EuroVoc);
- catálogos e diretórios de coleções (EU07 European Legal Data Space; e o próprio data.europa.eu);
- portais que abrigam várias coleções (EU01 EUR-Lex, EU24 Competition Case Search);
- benchmarks e corpora derivados de outra coleção (EU39 LexGLUE; EU36 EURLEX57K em relação a EU35);
- software e bases cívicas derivadas (EU41 ParlTrack);
- pares interface/coleção (EU08 × EU09; EU33 × EU34; EU01 × EU02 × EU03 × EU04).

I2 fala em "coleção ou serviço estruturado", o que tanto admite quanto exclui um vocabulário SKOS, conforme o leitor. O campo `resource_type` do inventário é texto livre: 34 valores distintos em 41 registros. O §5 diz que o agrupamento "exige metadados e justificativa", sem dizer quais.

**Proposta.**

1. Vocabulário controlado de **tipo de unidade**, com definição e exemplo negativo para cada classe. Sugestão inicial a ser calibrada: `dataset`, `registro_administrativo`, `corpus_academico`, `servico_de_acesso` (API, endpoint, dump), `portal_multicolecao`, `catalogo_diretorio`, `padrao_vocabulario`, `derivado_benchmark`, `software`.
2. Declarar, para cada classe, se pode ser **dataset canônico**, apenas **resource/distribution**, ou **contexto** (registrado e relatado, mas fora do denominador de datasets).
3. Regra de identidade canônica com critérios conjuntos e verificáveis — mesmo mantenedor, mesma unidade de observação, mesmo escopo material e temporal declarado — e regra explícita para versões e derivados.
4. Árvore de decisão de uma página no codebook.

**Justificativa.** O denominador de todas as análises do §13 é "datasets canônicos". Sem regra, dois avaliadores produzem denominadores diferentes e a contagem central do artigo não é reprodutível.

**Impacto.** É o principal objeto do piloto de calibração (ver `outputs/PILOT_CALIBRATION_PLAN.md`). Altera o codebook e o esquema de `datasets.csv` e `resources.csv` (novo campo de tipo).

## A03 — Consultas não executáveis e plataformas sem consulta — CRÍTICA

**Problema.** Em `inputs/search_queries.csv`:

- Q07, Q08, Q11, Q12 e Q13 trazem **descrições**, não expressões executáveis ("legal acts metadata CELEX ELI", modo "Official manual + API").
- Q09 e Q10 atribuem uma única linha a várias plataformas ("OpenAlex / Scopus / WoS"; "Zenodo / OpenAIRE"), cada uma com sintaxe, campos e truncagem diferentes.
- As cinco expressões-base do SEARCH_STRATEGY não têm correspondência um-a-um com as 14 linhas do CSV.
- Fontes citadas no PROTOCOL §8 e no SEARCH_STRATEGY sem nenhuma linha: OEIL, Council, N-Lex, Crossref, GitHub, DSA Transparency Database, registros EDPB/GDPR, reporte ambiental.
- Apenas Q14 tem variante não inglesa, embora o §7 prometa buscas complementares em francês e alemão.
- Nenhuma linha traz campos pesquisados, filtros, limite de data ou regra de paginação.

**Proposta.** Uma linha por **plataforma × expressão × idioma**, com sintaxe nativa, campos, filtros e regra de paginação; coluna que liga cada linha à expressão-base de origem e registra a tradução feita; consultas explícitas para cada fonte dos Blocos A–D, ou declaração de que a fonte será tratada por **inspeção manual estruturada** com roteiro próprio. Incluir a estratégia completa de pelo menos uma base no apêndice.

**Justificativa.** O PRISMA-ScR (item 8) exige a estratégia eletrônica completa de ao menos uma base, de modo que possa ser repetida. No estado atual, um terceiro não consegue repetir Q07–Q13.

**Impacto.** Trabalho de desenho antes de G2. Sem isso, o teste de recuperação de seeds (A22) falha por construção para as famílias de fiscalização e de intermediários.

## A04 — Regra de volume: quanto de cada busca será triado — CRÍTICA

**Problema.** O §9 exige triagem dupla **integral** de todos os registros únicos. Consultas amplas como Q01 ("EU legislation") num catálogo agregador podem devolver um volume muito alto de registros — **UNVERIFIED: nenhuma consulta foi executada**. O protocolo não diz se serão triados todos os resultados, os N primeiros por relevância ou uma amostra, nem o que fazer com datasets nacionais agregados pelo catálogo. O exemplo do README usa `--limit 25` sem justificar.

**Proposta.** Definir antes do congelamento, por plataforma:

1. execução exploratória única e registrada apenas para medir volume (contagem total, sem ingestão), a ser autorizada pela equipe;
2. regra pré-registrada — triagem integral até um teto T; acima dele, filtros declarados (publicador, catálogo de origem, tema) ou ordenação por relevância com corte fixo;
3. relato do total recuperado e do total triado como números distintos.

**Justificativa.** Uma regra de corte decidida depois de ver os resultados é fonte clássica de viés de seleção e inviabiliza a repetição.

**Impacto.** Determina a viabilidade do cronograma de triagem dupla. Depende de decisão da equipe sobre a medição de volume (não é coleta, mas é contato com a API).

## A05 — Equipe de avaliação e independência real — CRÍTICA

**Problema.** O desenho exige dois avaliadores independentes em duas etapas, um adjudicador que não tenha produzido a decisão contestada e dupla codificação de ≥20% da auditoria. DECISIONS diz "sem imputar tarefas a pessoas específicas" e o template de pré-registro tem "Equipe e afiliações: [PREENCHER / VALIDAR]". Não há registro de quem são os avaliadores, de sua formação, nem das horas disponíveis.

**Proposta.** Nomear antes do piloto: avaliador 1, avaliador 2, adjudicador, responsável pela busca. Registrar formação relevante e eventual envolvimento prévio com o inventário exploratório (quem o construiu não é cego a ele — ver A07). Se só houver um avaliador humano disponível, **rebaixar o desenho de forma declarada** (triagem simples com verificação de amostra por segundo avaliador), em vez de manter no papel uma triagem dupla que não ocorrerá.

**Justificativa.** A concordância entre avaliadores é resultado a ser relatado; não pode ser simulada (PROMPT_MESTRE, regra 6 e item 3 da segunda sessão; LLM_RESEARCH_INTEGRITY).

**Impacto.** Bloqueia o início do piloto. Decisão exclusivamente humana.

## A06 — Evidência congelada (snapshot) para triagem e auditoria — ALTA

**Problema.** A unidade triada é uma página web, documentação de API ou repositório, que muda sem aviso. O protocolo pede "evidência verificável e data", mas não exige cópia. Dois avaliadores em dias diferentes podem ver conteúdos diferentes; um revisor do artigo, meses depois, pode não ver nenhum.

**Proposta.** Para cada registro que chega à triagem de fonte completa e para cada nota de auditoria: URL, data e hora de acesso, e cópia arquivada (serviço de arquivamento público ou captura local com SHA-256), respeitando termos de uso e sem redistribuir conteúdo restrito. Os dois avaliadores trabalham sobre a **mesma** captura.

**Justificativa.** Garante que a discordância medida é de julgamento, não de conteúdo, e torna a auditoria verificável a posteriori.

**Impacto.** Acrescenta campos (`snapshot_ref`, `snapshot_sha256`, `accessed_at`) a `screening.csv` e `audit.csv`, e um passo operacional por registro.

## A07 — Cegamento em relação às colunas de julgamento do inventário exploratório — ALTA

**Problema.** `inputs/seed_inventory_v0_1.csv` contém três colunas que já são julgamentos: `rgam_potential` (Baixo a Muito alto), `initial_priority` (P1–P3) e `limitations`, que em vários casos antecipa a decisão de classificação ("Identificador/ontologia, não corpus independente"; "Diretório de fontes; não constitui dataset único"; "não contar como fonte autônoma de atos"). A coluna `layer` inclui o rótulo "Intermediação RIT". O comando `import-seeds` copia `limitations` para o campo `notes` de `discovery_records.csv`.

**Proposta.** No piloto e na triagem formal, os avaliadores recebem apenas identificador, nome e URL. As colunas de julgamento ficam ocultas até o fim da codificação independente. Registrar no manuscrito que o inventário exploratório foi construído por pesquisa documental não sistemática e que suas classificações não foram usadas como decisão.

**Justificativa.** Ancoragem: uma etiqueta prévia desloca a decisão do avaliador e infla a concordância.

**Impacto.** Exige um pacote de triagem cego gerado a partir dos dados (ver plano do piloto). O campo `notes` de `discovery_records.csv` não deve ser exibido aos avaliadores.

## A08 — Circularidade entre a tipologia D0–D3 e a operacionalização RGAM — ALTA

**Problema.** O título promete avaliar a "capacidade de representar arquiteturas de governança regulatória". O instrumento que mede essa capacidade (D0–D3 e os critérios `ACTORS`, `FUNCTIONS`, `RELATIONS`, `LEGAL_BASIS`) deriva do mesmo quadro teórico que a equipe desenvolve, e o subestudo do §14 aplica esse quadro aos datasets escolhidos pela própria revisão. Um revisor perguntará se o instrumento mede uma propriedade dos datasets ou a proximidade deles com o quadro dos autores.

**Proposta.**

1. Declarar no §3 que a auditoria é um instrumento **original e não validado**, e que a tipologia D0–D3 depende de um quadro teórico específico (relações regulador–intermediário–destinatário).
2. Ancorar cada nível D em propriedades observáveis do dado (campo estruturado de entidade; campo estruturado de papel; identificador de ato ou artigo), de modo que um avaliador sem familiaridade com o quadro chegue à mesma classificação.
3. Manter o subestudo RIT fisicamente separado no relato, como já previsto.
4. Prever, se possível, um avaliador externo ao projeto na dupla codificação da auditoria.

**Justificativa.** Validade de construto e risco de viés de confirmação.

**Impacto.** Redação dos §3, §11 e §14 e âncoras do codebook. Não altera a operacionalização RGAM, o V8, nem os demais subprojetos.

## A09 — Nível de aplicação dos critérios de auditoria — ALTA

**Problema.** `audit.csv` é indexado apenas por `dataset_id`. `MACHINE_ACCESS` e `REUSE_RIGHTS` são propriedades de **distribuições**: o mesmo dataset canônico pode ter uma API documentada e um dump restrito a login, com licenças diferentes.

**Proposta.** Declarar para cada critério o nível de aplicação. Para critérios de distribuição, pontuar por `resource_id` e definir a regra de agregação para o dataset (por exemplo, melhor distribuição disponível, relatando também a dispersão).

**Justificativa.** Sem a regra, a nota depende de qual interface o avaliador abriu primeiro.

**Impacto.** Coluna `resource_id` opcional em `audit.csv`; ajuste da validação no CLI.

## A10 — Divergência de critérios: 8 no protocolo, 9 no codebook — ALTA

**Problema.** PROTOCOL §11 lista oito dimensões (identificadores jurídicos; estruturação de atores; competência/função; relações dirigidas; temporalidade; documentação e reprodutibilidade; acesso automático; condições de reutilização). O CODEBOOK traz nove códigos: acrescenta `LEGAL_BASIS` e usa `PROVENANCE` onde o protocolo diz "documentação e reprodutibilidade". `LEGAL_ID` e `LEGAL_BASIS` têm âncoras parcialmente sobrepostas. O CLI não valida o nome do critério (BASELINE_RUN, sondagem P5).

**Proposta.** Uma única lista normativa, no codebook, citada pelo protocolo. Delimitar `LEGAL_ID` (o dado carrega identificador do ato?) de `LEGAL_BASIS` (o dado liga cada registro ao dispositivo que o fundamenta?). Rever a escala de `REUSE_RIGHTS`, que hoje mistura clareza da condição com grau de permissão. Definir "inspeção suficiente" para atribuir nota 0 (roteiro mínimo de onde procurar).

**Impacto.** Codebook e validação; nenhuma coleta afetada.

## A11 — Estatísticas de concordância e critério de passagem do piloto — ALTA

**Problema.**

1. Com 15–20 registros, o kappa de Cohen tem intervalo de confiança muito largo e é instável sob prevalência desbalanceada.
2. O critério de G1 é "Codebook estável e lista de exclusões inequívocas", sem definição operacional.
3. Para a auditoria, a escala 0/1/2 é ordinal, mas não há estatística ordinal prevista, nem tratamento para o caso de um avaliador atribuir `UNVERIFIED` e o outro uma nota.
4. A decisão `uncertain` é excluída do cálculo; se for frequente, o kappa relatado descreve só os casos fáceis.

**Proposta.** No piloto: relatar concordância bruta, matriz de confusão completa incluindo `uncertain`, e lista qualitativa de divergências por regra do codebook; não usar o kappa do piloto como critério numérico de passagem. O critério de passagem é definido pela equipe antes de abrir as respostas (por exemplo: toda divergência atribuída a uma regra, e cada regra revista ou confirmada). Na triagem formal: kappa com intervalo de confiança e uma medida robusta a prevalência, mais a proporção de `uncertain`. Na auditoria: kappa ponderado ou alfa de Krippendorff ordinal, com `UNVERIFIED` tratado como categoria própria.

**Impacto.** ANALYSIS_AND_VALIDITY e a função `kappa_or_na` do CLI (ver EXECUTION_PLAN).

## A12 — Regras de deduplicação em dois níveis — ALTA

**Problema.** S2 fala em "URL canônica/identificador e inspeção manual" sem definir canonicalização (esquema, barra final, parâmetros de idioma como `?locale=en`, fragmentos), sem dizer quem deduplica nem se há verificação. O segundo nível (datasets sobrepostos) depende de A02. `dedup.csv` não tem coluna de método nem de data.

**Proposta.** Regra de canonicalização escrita e implementada de forma determinística; deduplicação de ocorrências feita por um avaliador e verificada por outro em amostra; nível de coleção decidido na construção das entidades canônicas, com justificativa obrigatória em campo próprio.

**Impacto.** Codebook, esquema de `dedup.csv`, função auxiliar no CLI.

## A13 — Data de fechamento da busca e janela de execução — ALTA

**Problema.** §7: "fechamento documental explicitamente datado no registro de buscas (definir antes do início)". Não está definido. Recursos web mudam diariamente; buscas feitas ao longo de semanas descrevem universos diferentes.

**Proposta.** Fixar no protocolo congelado a janela de execução (data de abertura e de encerramento) e a regra para atualização da busca antes da submissão.

**Impacto.** Uma linha no protocolo; condiciona o cronograma.

## A14 — Etapas de triagem adaptadas a recursos sem título/resumo — MÉDIA

**Problema.** As etapas `title_abstract` e `full_source` vêm de revisões bibliográficas. Um registro de catálogo tem título e descrição; uma página institucional não tem resumo; um repositório tem README.

**Proposta.** Definir, por tipo de fonte, o que constitui o material da etapa 1 (título e descrição do catálogo, ou título e primeiro bloco descritivo da página) e da etapa 2 (documentação técnica, ficha de metadados, artigo de dados), e um limite de profundidade de navegação na etapa 2.

**Impacto.** Codebook; reduz divergência por esforço desigual de inspeção.

## A15 — Reformulação das RQs 1, 3 e 5 — MÉDIA

**Problema.** RQ1 ("quais… são identificáveis publicamente") e RQ5 ("em quantos…") pedem um universo e uma contagem que o próprio ANALYSIS_AND_VALIDITY declara inalcançáveis. RQ3 não é pergunta de mapeamento, e sim da auditoria original.

**Proposta.** Condicionar RQ1 e RQ5 ao método ("identificados pela estratégia de busca definida"; "entre os datasets incluídos"). Marcar RQ3 e RQ5 como perguntas da auditoria técnica, distinguindo-as das perguntas de escopo (RQ1, RQ2, RQ4).

**Impacto.** Redação; alinha perguntas, método e limites de inferência.

## A16 — Justificativa da adaptação do PCC — MÉDIA

**Problema.** No PCC do JBI, "Population" refere-se a participantes. Aqui é "recursos de informação estruturada", e se sobrepõe ao "Concept" ("representações reutilizáveis de…"). O "Context" inclui "conexões documentadas com execução nacional" sem critério de até onde vai.

**Proposta.** Um parágrafo que declare a adaptação e sua razão; separar População (o objeto mapeado: recursos de dados) de Conceito (a propriedade de interesse: o que representam e com que capacidade); delimitar o Contexto nacional remetendo a E3 e a A17.

**Impacto.** Redação.

## A17 — Amostragem de portais nacionais e consulta a especialistas — MÉDIA

**Problema.** O §8 prevê "amostragem de portais nacionais e consulta direcionada a especialistas" sem quadro amostral, sem número de Estados-membros, sem critério de escolha dos especialistas e sem forma de registro das respostas.

**Proposta.** Ou definir o procedimento (Estados-membros escolhidos por critério declarado; roteiro de consulta; registro das sugestões como `expert_suggestion` com data e fonte), ou retirar o componente nacional do escopo desta revisão e declará-lo como limitação.

**Impacto.** Escopo e esforço; decisão da equipe.

## A18 — Mapeamento explícito dos critérios aos princípios FAIR — MÉDIA

**Problema.** O §3 diz que FAIR "inspira" os critérios, sem mapa. Lacunas aparentes em relação a Wilkinson et al. (2016): identificador persistente do **próprio dataset** (F1), riqueza de metadados (F2), indexação em recurso pesquisável (F4), uso de vocabulários formais (I1/I2). `PROVENANCE` e `REUSE_RIGHTS` correspondem de perto a R1.2 e R1.1; `MACHINE_ACCESS`, a A1.

**Proposta.** Tabela critério × subprincípio FAIR, declarando o que é coberto, o que é deliberadamente omitido e por quê. Decidir se entra um critério para identificador persistente do dataset.

**Impacto.** Codebook e seção de métodos; responde antecipadamente à pergunta "por que não usar um instrumento FAIR existente?".

## A19 — Lacunas PRISMA-ScR / PRISMA-S / JBI — MÉDIA

**Problema e proposta, por item.**

- **Registro (PRISMA-ScR item 5):** plataforma e momento não decididos. Decidir (ver A01).
- **Estratégia completa (item 8):** ver A03.
- **Piloto do formulário de extração (item 10):** o piloto previsto cobre triagem; estender à extração e à auditoria em subconjunto.
- **Avaliação crítica (item 12):** declarar que não se faz avaliação crítica das fontes de evidência e que a auditoria técnica é resultado, não apreciação de qualidade.
- **Fluxograma:** adotar o modelo com coluna para "outros métodos" (registros institucionais, encadeamento de citações, especialistas), já que a maior parte das fontes não é base bibliográfica.
- **Relato da busca:** considerar a extensão PRISMA-S.
- **Revisão por pares da estratégia de busca:** considerar a diretriz PRESS ou revisão por bibliotecário.
- **JBI, três etapas:** declarar que a etapa 1 é substituída pela calibração de termos em fontes-semente, e por quê.

As referências a PRISMA-S e PRESS precisam ser localizadas e verificadas pela equipe antes de citadas; **não foram verificadas nesta sessão**.

**Impacto.** Redação do protocolo e do esqueleto do manuscrito.

## A20 — Campos previstos no protocolo e ausentes no esquema — MÉDIA

**Problema.** Comparação do texto com `SCHEMA` em `scripts/cli.py`:

- O §8 exige, por consulta, filtros, paginação, hash do arquivo bruto e restrições. `search_runs.csv` não tem colunas para filtros, paginação, hash nem total informado pela plataforma.
- O §10 exige, por dataset, condição de acesso, data de verificação, evidência, tipo de recurso, disponibilidade de documentação, chaves oficiais e decisão de elegibilidade. Ausentes em `datasets.csv`.
- O §10 exige, por distribuição, "existência confirmada ou anunciada". Ausente em `resources.csv`.
- A tipologia D0–D3 **não tem coluna em nenhuma tabela**.
- Não há tabela para o teste de recuperação de seeds nem para o registro de emendas.

**Proposta.** Rever o esquema após o piloto e antes do congelamento, com migração versionada (ver EXECUTION_PLAN). Publicar um dicionário de dados.

**Impacto.** Código e dados; nenhuma tabela afetada tem registros, exceto `discovery_records.csv`.

## A21 — Dados pessoais e termos de uso por fonte — MÉDIA

**Problema.** O §15 trata o tema em termos gerais. Há no inventário recursos que, pela descrição, contêm ou podem conter dados de pessoas naturais (EU17 Transparency Register — "Organização / representante"; EU41 ParlTrack — "Dossiê / MEP / votação"; EU25 decisões EDPB).

**Proposta.** Regra operacional: a revisão registra **metadados sobre o recurso**, nunca registros individuais; qualquer teste de acesso (critério `MACHINE_ACCESS` = 2) baixa a menor amostra necessária, não a armazena no repositório e registra os termos de uso consultados. Verificar com a instituição se é necessário parecer ético ou de proteção de dados.

**Impacto.** Procedimento de auditoria; possível trâmite institucional.

## A22 — Teste de recuperação de seeds × amostra de calibração — MÉDIA

**Problema.** O SEARCH_STRATEGY prevê teste com 12–15 seeds sem dizer como são escolhidos nem se podem coincidir com os 15–20 da calibração. Seeds usados para ajustar as expressões não servem depois para testá-las.

**Proposta.** Dividir os 41 antes de qualquer busca: um subconjunto de desenvolvimento (pode informar termos) e um de teste (só para medir recuperação), ambos estratificados; ou testar a recuperação dos 41 e relatar por família. Definir o que conta como "recuperado" (mesma URL? mesmo dataset canônico?).

**Impacto.** SEARCH_STRATEGY; depende de A02 para a definição de equivalência.

## A23 — Seleção dos casos do subestudo exploratório RIT — MÉDIA

**Problema.** O §14 lista cinco casos candidatos (os mesmos da aba "Casos candidatos" da planilha original) e manda "congelar amostragem antes de extrair relações", mas não dá critério de escolha entre candidatos nem regra para o caso de um deles não ser elegível na revisão.

**Proposta.** Critérios de seleção escritos (diversidade de domínio e de função; elegibilidade confirmada na revisão; existência de dispositivo normativo identificável), lista de substitutos ordenada, e congelamento datado **depois** da triagem e **antes** de qualquer extração.

**Impacto.** §14. Não altera a operacionalização RGAM, o V8, nem outros subprojetos.

## A24 — Versionamento das evidências do G0 e dos payloads brutos — MÉDIA

**Problema.** O `.gitignore` desta pasta ignora `outputs/*`, `data/raw/*` e `data/ai_runs/*`. Consequências:

1. `BASELINE_RUN.md`, `PILOT_CALIBRATION_PLAN.md`, `EXECUTION_PLAN.md` e `G0_REVIEW_NOTE.md` **não entram no histórico git**, embora o PROMPT_MESTRE peça "resultados auditáveis por arquivo/commit" e DECISIONS exija "repositório commitado" para G0.
2. Os payloads brutos de API e os registros de uso de IA, que o protocolo manda preservar, só existem na cópia local sincronizada.

**Proposta.** Versionar os documentos de gate (mover para pasta rastreada, por exemplo `reports/`, ou abrir exceção no `.gitignore`) e manter fora do git apenas arquivos regeneráveis. Para `data/raw/`, versionar ao menos os manifestos com SHA-256 e prever depósito dos brutos em repositório de dados quando a licença permitir.

**Impacto.** Rastreabilidade do G0. Mudança de `.gitignore` e commits dependem de autorização (não realizados nesta sessão).

## A25 — Idioma do protocolo registrado — BAIXA

**Problema.** Protocolo em português, manuscrito-alvo em inglês, códigos do codebook em inglês, rótulos do inventário em português.

**Proposta.** Versão em inglês do protocolo para registro público, com a versão em português preservada; declarar qual é a normativa.

## A26 — Rótulo "verificadas" nas referências — BAIXA

**Problema.** PROTOCOL §18 intitula-se "Referências fundacionais (verificadas)" e o arquivo `SOURCES_VERIFIED_2026-10-09.md` leva "verified" no nome, mas o próprio arquivo declara que recuperação em rede, limites e licenças não foram verificados de dentro do scaffold. Nesta sessão G0 nenhuma URL foi acessada.

**Proposta.** Registrar, por referência, quem verificou, quando e o quê (existência da página; conteúdo citado). Até lá, tratar como "consultadas".

## A27 — URL repetida e URLs de página explicativa nos seeds — BAIXA

**Problema.** EU03 (EUR-Lex bulk data dump) e EU07 (European Legal Data Space — diretório) têm a mesma `source_url`. Em vários seeds, a URL registrada tem caminho de página de política, ajuda ou perguntas frequentes, não de recurso de dados (por exemplo EU13, EU14, EU15, EU16, EU21, EU23, EU27, EU30). Se as páginas estão ativas e o que contêm é **UNVERIFIED**.

**Proposta.** **Não corrigir o arquivo de seeds** (é artefato de proveniência). Tratar a localização da URL do recurso como tarefa da triagem de fonte completa e registrar o resultado em `resources.csv`. O par EU03/EU07 serve de teste de mesa para a regra de deduplicação por URL (A12): uma regra puramente baseada em URL fundiria dois recursos que o inventário descreve como distintos. EU03 está na amostra de calibração proposta; EU07 é suplente.

---

## Registro de decisão (a preencher pela equipe)

| ID | Decisão (aceita / modificada / rejeitada) | Data | Responsável | Observação |
|---|---|---|---|---|
| A01 | | | | |
| A02 | | | | |
| A03 | | | | |
| A04 | | | | |
| A05 | | | | |
| A06 | | | | |
| A07 | | | | |
| A08 | | | | |
| A09 | | | | |
| A10 | | | | |
| A11 | | | | |
| A12 | | | | |
| A13 | | | | |
| A14 | | | | |
| A15 | | | | |
| A16 | | | | |
| A17 | | | | |
| A18 | | | | |
| A19 | | | | |
| A20 | | | | |
| A21 | | | | |
| A22 | | | | |
| A23 | | | | |
| A24 | | | | |
| A25 | | | | |
| A26 | | | | |
| A27 | | | | |
