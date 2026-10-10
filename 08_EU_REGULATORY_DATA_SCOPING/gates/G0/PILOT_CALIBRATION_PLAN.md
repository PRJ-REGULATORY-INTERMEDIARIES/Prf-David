# PLANO DE CALIBRAÇÃO PILOTO — G0

**Data:** 2026-10-09 | **Estado:** PROPOSTA para aprovação da equipe científica. Nenhum registro foi triado, classificado ou adjudicado.

## 1. Finalidade e limites

O piloto testa **as regras**, não os recursos. Serve para descobrir onde o protocolo e o codebook levam dois avaliadores humanos a decisões diferentes, e para rever essas regras antes do congelamento (ver emenda A01 em `protocol/PROPOSED_AMENDMENTS.md`).

O que este plano **não** faz:

- não atribui elegibilidade a nenhum registro;
- não contém decisão de avaliador, real ou simulada;
- não produz concordância, kappa ou adjudicação;
- não trata os 41 recursos do inventário exploratório como datasets incluídos, nem os 18 selecionados como amostra representativa de qualquer universo.

Universo de calibração: os 41 registros de `inputs/seed_inventory_v0_1.csv` (EU01–EU41), e apenas eles. Todos os identificadores abaixo existem nesse arquivo; nome, família e acesso anunciado são transcritos dele.

## 2. Como a amostra foi construída

Seleção **intencional por diversidade máxima**, não aleatória. Critérios, nesta ordem:

1. três registros em cada um dos seis estratos pedidos no G0 (6 × 3 = 18);
2. dentro de cada estrato, preferência por registros que o próprio inventário sinaliza como caso-limite de alguma regra do protocolo (coluna `limitations`);
3. cobertura do maior número possível de famílias de origem (coluna `layer`);
4. inclusão de pares que testam a regra de dataset canônico (interface × coleção; original × derivado).

**Aviso de viés.** A escolha foi feita por um agente de IA lendo as colunas de julgamento do inventário (`layer`, `limitations`, `initial_priority`). Isso é aceitável para montar um conjunto de teste de regras, mas a equipe deve aprovar ou substituir a lista. Os avaliadores não devem ver essas colunas (seção 6).

## 3. Amostra proposta (18 registros)

Estratos: **A** repositórios legislativos oficiais · **B** APIs e dados vinculados · **C** corpora acadêmicos · **D** bases de implementação e fiscalização · **E** registros de organizações intermediárias · **F** acesso restrito, descontinuado ou classificação ambígua.

| # | ID | Nome (inventário) | Família de origem (`layer`) | Estrato | Por que está na amostra |
|---|---|---|---|---|---|
| 1 | EU01 | EUR-Lex — legislação e documentos jurídicos | Corpus normativo | A | Portal com várias coleções: dataset, portal ou os dois? |
| 2 | EU03 | EUR-Lex bulk data dump | Corpus normativo | A (e F) | Acesso anunciado com EU Login; URL registrada é a mesma de EU07 |
| 3 | EU18 | EUR-Lex — National Transposition Measures (NIM) | Transposição/Estados | A | Coleção dentro do EUR-Lex com vínculo nacional; testa agrupamento com EU01 e o critério E3 |
| 4 | EU02 | CELLAR — repositório e grafo de metadados | Corpus normativo | B | Grafo/API sobre o mesmo acervo de EU01: distribuição ou dataset próprio? |
| 5 | EU08 | European Parliament Open Data API — procedures | Processo legislativo | B | API estruturada; identificador é número de procedimento, não CELEX |
| 6 | EU34 | TED Search API — notices | Aplicação setorial | B | Dados de aplicação do direito, não corpus legislativo; sobreposição declarada com EU33 |
| 7 | EU35 | MultiEURLEX — EU legislation corpus | Corpus acadêmico | C | Corpus de pesquisa depositado; caso presumivelmente simples, serve de âncora |
| 8 | EU39 | LexGLUE — subtarefa EUR-LEX | Corpus acadêmico | C | Benchmark derivado: unidade própria ou derivado de outra coleção? |
| 9 | EU40 | EU Policy Agendas Project — European Council Conclusions | Corpus acadêmico | C | Documentos de agenda política; testa a fronteira de I1/E5 |
| 10 | EU15 | Comitology Register — comitês e atos de execução | Delegação/implementação | D | Base processual; URL registrada é página de política, não o registro |
| 11 | EU21 | Commission — Infringement Decisions Register | Fiscalização | D | Registro de casos; URL registrada é página geral sobre aplicação do direito |
| 12 | EU25 | EDPB — register of final one-stop-shop GDPR decisions | Fiscalização | D | Acesso anunciado como consulta/PDF: satisfaz "estruturado" (I2)? |
| 13 | EU26 | DSA — EU Trusted Flaggers List | Intermediação RIT | E | Lista em XLSX anunciada; cadastro com base legal declarada |
| 14 | EU28 | DGA — Register of Data Intermediation Services | Intermediação RIT | E | Rótulo "intermediação" sem relação regulatória presumida |
| 15 | EU29 | NANDO — Notified Bodies | Intermediação RIT | E | Cadastro consultável; exportação em lote não confirmada |
| 16 | EU05 | European Legislation Identifier (ELI) | Infraestrutura | F | Padrão de identificação: é unidade elegível? |
| 17 | EU11 | Council votes on legislative acts — dataset antigo | Processo legislativo | F | Marcado no inventário como descontinuado; testa I5 e E4 |
| 18 | EU17 | EU Transparency Register | Atores/participação | F | Cadastro de atores sem papel regulatório presumido; testa I1 |

### Cobertura obtida

| Dimensão | Amostra | Universo (41) |
|---|---|---|
| Famílias de origem cobertas | 10 de 11 | 11 |
| Família sem representante | Jurisprudência (EU22, EU23) | — |
| Prioridade exploratória P1 / P2 / P3 | 11 / 5 / 2 | 19 / 19 / 3 |

A amostra sobrerrepresenta P1 (61% contra 46% no universo). Isso decorre de os casos-limite mais nítidos estarem entre os P1 e não tem consequência para o objetivo do piloto, mas impede qualquer leitura das proporções da amostra como estimativa.

### Suplentes, em ordem de uso

Usar apenas se a equipe substituir um registro, ou se uma fonte estiver inacessível no dia da captura (seção 5). A substituição deve ser registrada com motivo.

| Ordem | ID | Nome | Família | O que acrescenta |
|---|---|---|---|---|
| 1 | EU22 | InfoCuria — decisões do TJUE | Jurisprudência | Cobre a família ausente |
| 2 | EU31 | EEA — Reportnet 3 / Dataflows | Intermediação RIT | Acesso parcialmente restrito; plataforma com conjuntos variáveis |
| 3 | EU07 | European Legal Data Space — diretório | Infraestrutura | Catálogo de coleções; par de URL com EU03 |
| 4 | EU19 | N-Lex — bases legais nacionais | Transposição/Estados | Portal federado nacional |
| 5 | EU41 | ParlTrack | Corpus acadêmico | Base cívica derivada, com componente de software |
| 6 | EU38 | DGT-Acquis | Corpus acadêmico | Corpus integral disponível só por contato |

## 4. Regras a testar e dificuldades esperadas

As "dificuldades esperadas" são hipóteses derivadas da leitura do inventário. Nenhuma página foi acessada nesta sessão; o que cada recurso de fato oferece é **UNVERIFIED**.

| Regra em teste | Fonte no protocolo | Registros que a exercitam | Pergunta que o piloto deve responder |
|---|---|---|---|
| Relação material com direito/regulação da UE | I1, E3, E5 | EU40, EU34, EU17, EU18 | Agenda política, contratação pública e cadastro de lobby satisfazem I1? |
| "Coleção ou serviço estruturado" | I2, E1 | EU25, EU21, EU15, EU05 | Registro que só oferece PDF ou busca em página é estruturado? Um padrão é uma coleção? |
| Metadados mínimos verificáveis | I3, E4 | EU11, EU03, EU15, EU21 | Que metadados bastam? O que fazer quando a URL do inventário não leva ao recurso? |
| Estado ativo, arquivado ou descontinuado | I5 | EU11 | "Documentação suficiente" para um recurso descontinuado é o quê? |
| Acesso restrito não exclui | §6, nota final | EU03 | O avaliador consegue decidir elegibilidade sem conseguir entrar? |
| Dataset canônico × distribuição | §5, E2 | EU01 × EU02 × EU03 × EU18; EU34 | Os avaliadores agrupam do mesmo modo? Com que justificativa? |
| Original × derivado | §5 | EU35 × EU39 | Um benchmark derivado conta como dataset canônico? |
| Tipo de unidade | emenda A02 | os 18 | A lista de tipos proposta é exaustiva e mutuamente exclusiva? |
| Rótulo não implica relação | §14, CODEBOOK (D3) | EU26, EU28, EU29, EU17 | Na triagem, os avaliadores mantêm separadas a elegibilidade e a suposta relação RIT? |
| Motivos de exclusão | CODEBOOK | todos os que receberem `exclude` | Os seis códigos bastam? `OTHER` é usado com que frequência? |
| Deduplicação por URL | S2, emenda A12 | EU03 (com EU07, se incluído) | Teste de mesa: a regra de URL fundiria dois recursos distintos? |

Fora do escopo do piloto: auditoria técnica (notas 0/1/2), tipologia D0–D3 e qualquer extração de relações. Se a equipe quiser pilotar também a extração e a auditoria (PRISMA-ScR item 10; emenda A19), recomenda-se um segundo piloto, menor, depois da revisão do codebook.

## 5. Preparação (antes de os avaliadores começarem)

Responsável: quem coordena a busca, que **não** será um dos dois avaliadores, se a equipe permitir.

1. **Aprovação da lista** de 18 e dos suplentes pela coordenação científica, com data.
2. **Nomeação** de avaliador 1, avaliador 2 e adjudicador (emenda A05). Registrar se algum deles participou da construção do inventário exploratório.
3. **Critério de passagem** do piloto definido por escrito antes de abrir qualquer resposta (emenda A11).
4. **Captura de evidência** (emenda A06): para cada registro, localizar a página do recurso a partir da URL do inventário, registrar a URL efetivamente usada, data e hora de acesso, e guardar cópia arquivada com SHA-256. Se a URL do inventário não levar ao recurso, registrar o caminho percorrido. Esta etapa é acesso manual a páginas públicas, registro a registro; não é busca sistemática nem coleta em lote.
5. **Pacote cego** (emenda A07): para cada avaliador, uma lista com `record_id`, nome e a referência da captura, em ordem aleatorizada diferente para cada um. Ficam fora do pacote as colunas `layer`, `resource_type`, `rgam_potential`, `initial_priority`, `limitations`, a coluna `notes` de `data/discovery_records.csv`, e este documento.
6. **Formulário** idêntico para ambos (seção 6), com o protocolo e o codebook na versão DRAFT atual, sem as emendas propostas — o piloto testa o texto que existe.

## 6. Procedimento para os dois avaliadores independentes

**Independência.** Cada avaliador trabalha sozinho, em arquivo próprio, sem acesso ao arquivo do outro e sem discutir os casos até ambos entregarem. As respostas são entregues ao coordenador, que as tranca (hash e data) antes de comparar.

**Uso de IA.** Os avaliadores não usam LLM para decidir. Se usarem ferramenta de tradução ou de leitura, registram em `data/ai_runs/` conforme `LLM_RESEARCH_INTEGRITY.md`.

**Formulário, por registro:**

| Campo | Valores | Observação |
|---|---|---|
| `record_id` | SEED_EUxx | do pacote |
| `reviewer` | identificador do avaliador | |
| I1, I2, I3, I5 | atendido / não atendido / não foi possível determinar | um campo por critério; I4 (idioma) apenas anotar se relevante |
| E1 a E5 | aplica-se / não se aplica / não foi possível determinar | um campo por critério |
| `decision` | `include` / `exclude` / `uncertain` | vocabulário do codebook |
| `reason_code` | código do codebook | obrigatório se `exclude` |
| `unit_type` | lista da emenda A02, mais `nenhuma_serve` | campo experimental do piloto |
| `unit_level` | dataset canônico / distribuição de outro dataset / contexto / não sei | |
| `groups_with` | `record_id` de outro registro da amostra, se julgar que pertencem à mesma coleção | com justificativa |
| `rule_gap` | texto livre | regra ausente, ambígua ou contraditória que dificultou a decisão |
| `minutes` | número | tempo gasto; alimenta a estimativa de esforço do G2 |
| `evidence_ref` | referência da captura consultada | |

As decisões do piloto ficam em arquivos separados das tabelas de execução (sugestão: `data/pilot/screening_<avaliador>.csv`). **Não** devem ser escritas em `data/screening.csv`, que é a tabela da triagem formal e cujo vocabulário de etapas não prevê piloto.

## 7. Comparação e adjudicação (roteiro; a executar por humanos)

1. O coordenador confirma que os dois arquivos estão trancados e só então os cruza.
2. Produz, sem interpretar: matriz 3 × 3 de decisões (`include`/`exclude`/`uncertain`), concordância bruta por campo, lista de registros divergentes por campo, e as anotações de `rule_gap` agrupadas por regra.
3. Reunião de calibração com os dois avaliadores e o adjudicador. Para cada divergência, registrar: regra envolvida; causa (regra ausente, regra ambígua, leitura diferente da evidência, erro); resolução; e se exige mudança no protocolo ou no codebook.
4. O adjudicador decide apenas as divergências que persistirem após a discussão, e registra a decisão com justificativa.
5. As mudanças de regra entram em `protocol/PROPOSED_AMENDMENTS.md` como novas emendas ou como revisão das existentes, com referência aos registros que as motivaram.
6. Se houver mudança substantiva de definição, repetir o piloto com registros **não usados** (suplentes e demais registros do inventário), conforme o §9 do protocolo.

**Sobre estatísticas.** Com 18 registros, o kappa é impreciso demais para servir de critério; relatar concordância bruta e a matriz completa (emenda A11). As decisões do piloto não entram nas contagens da revisão nem no fluxograma PRISMA-ScR.

## 8. Entregáveis do piloto (G1)

- lista aprovada de registros, com eventuais substituições justificadas;
- capturas de evidência com hashes;
- dois arquivos de respostas independentes, trancados antes da comparação;
- ata de calibração com as divergências e suas causas;
- emendas ao protocolo e ao codebook decorrentes do piloto, com decisão registrada;
- estimativa de minutos por registro, por tipo de fonte.

## 9. Decisões que este plano deixa para a equipe

1. Aprovar, alterar ou substituir a lista de 18 e a ordem dos suplentes.
2. Incluir ou não a família Jurisprudência (trocar um registro por EU22).
3. Quem são os avaliadores e o adjudicador, e se quem construiu o inventário pode avaliar.
4. Critério de passagem do piloto.
5. Se a captura de evidência pode ser feita por serviço público de arquivamento.
6. Se haverá um segundo piloto para extração e auditoria.
7. Relação entre esta amostra e o teste de recuperação de seeds (emenda A22).
