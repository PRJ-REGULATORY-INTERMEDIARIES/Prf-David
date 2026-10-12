# G2 — RELATÓRIO INICIAL DE MAPEAMENTO (RODADA 1)

**Data das observações:** 2026-10-10 | **Responsabilidade científica:** Igor Caires Machado | **Execução:** agente de programação (Claude Code)

## Leitura rápida

A primeira rodada registrou **105 candidatos a recurso**: os 41 do inventário inicial e 64 novos. Dos 105, 88 estão individuados como recursos independentes; os outros 17 são prováveis distribuições, partes de outros recursos ou agrupamentos ainda não lidos.

Três coisas limitam o que se pode concluir daqui:

1. **Toda classificação é provisória.** Categorias, conjuntos, estados e relações foram propostos por um agente de IA a partir das capturas. Nenhuma linha foi confirmada por pesquisador.
2. **"Verificado" quer dizer pouco.** Significa que o nome e a localização constam de fonte primária preservada. Nenhum dataset foi aberto.
3. **A busca não é exaustiva** e não há estimativa de cobertura. As contagens descrevem o que esta rodada alcançou, não o campo.

O caso de teste pedido se confirmou: EU03 (EUR-Lex data dump) e EU07 (European Legal Data Space) são recursos distintos descritos na mesma página, e a base os mantém assim.

Um achado não previsto: as descrições oficiais do data dump divergem sobre o que ele contém (seção 9).

## 1. Pergunta e escopo

*What datasets and data infrastructures are available for the systematic study of European Union legislation and regulatory governance, and what are their characteristics, capabilities, relationships, and limitations?*

Dois conjuntos: **A**, dados legislativos e jurídicos da UE; **B**, dados de governança regulatória da UE. Definições, unidade de análise e critérios em `mapping/protocol/INDEPENDENT_MAPPING_REORIENTATION_v1_0.md`. A utilidade para o RGAM/V8 não foi critério de nada.

## 2. Buscas executadas

**Consultas registradas.** 54 consultas a sete serviços, uma requisição cada, 25 resultados pedidos. Todas responderam. Registro: `mapping/protocol/SEARCH_QUERIES_G2_ROUND1.csv`; respostas preservadas com hash em `mapping/evidence/searches/`.

| Serviço | Consultas | Ocorrências devolvidas | Ocorrências ligadas a recursos | Consultas sem nenhuma ligação |
|---|---|---|---|---|
| data.europa.eu | 24 | 577 | 34 | 9 |
| Zenodo | 8 | 200 | 12 | 1 |
| Harvard Dataverse | 4 | 100 | 11 | 0 |
| DataCite | 3 | 75 | 1 | 2 |
| OpenAlex | 6 | 150 | 12 | 2 |
| Hugging Face Hub | 6 | 130 | 14 | 0 |
| GitHub | 3 | 19 | 7 | 0 |
| **Total** | **54** | **1.251** | **91** | **14** |

Dezenove consultas informaram mais de cem mil resultados existentes; só os 25 primeiros de cada foram vistos.

**Leitura de páginas.** 57 tentativas de captura em 35 hosts: as 40 URLs distintas dos 41 seeds e 17 endereços de acesso indicados por elas. 52 capturas; 5 falhas registradas. A página ELDS capturada no G1-READY foi recapturada e tem o mesmo hash.

**Encadeamento.** Links e menções nas páginas e nos metadados lidos deram 6 candidatos novos e 24 pontos de acesso adicionais.

**Não executado:** índices bibliográficos por assinatura; consultas SPARQL ao catálogo; buscas em idiomas além de uma sondagem em francês e uma em alemão; leitura dos artigos encontrados; qualquer acesso autenticado; qualquer download de dataset.

Três buscas na web, pela ferramenta de busca do agente, foram feitas só para localizar trabalhos anteriores semelhantes. Não são reproduzíveis e não geraram registros na base; estão na nota de potencial de publicação.

## 3. Resultados identificados

| Medida | Valor |
|---|---|
| Ocorrências brutas de busca | 1.251 |
| Ocorrências ligadas a algum recurso | 91 |
| Seeds reencontrados pelas buscas | 12 de 41 |
| Candidatos a recurso registrados | 105 |
| — do inventário inicial (`SEED`) | 41 |
| — por busca registrada (`SYSTEMATIC_SEARCH`) | 58 |
| — por encadeamento (`BACKWARD_FORWARD_DISCOVERY`) | 6 |
| — por indicação de especialista | 0 |

A maior parte das ocorrências não virou registro: publicações sem dataset, registros nacionais e locais sem ligação com a UE, cópias e reformatações, software. As decisões de grupo estão em `decisions_log.csv` (`DEC-0008` a `DEC-0012`).

O reencontro de 12 dos 41 seeds diz que as consultas, sozinhas, não teriam achado a maioria dos recursos institucionais já conhecidos. Vários deles não estão no catálogo data.europa.eu, ou estão e não aparecem entre os 25 primeiros.

## 4. Recursos individualizados

| Estado de individuação | Total | Seeds | Novos |
|---|---|---|---|
| `INDIVIDUATED` | 88 | 34 | 54 |
| `CANDIDATE_SEPARATE` — provavelmente próprio, não decidido | 10 | 5 | 5 |
| `CANDIDATE_NOT_INDEPENDENT` — provável distribuição, interface ou parte | 5 | 2 | 3 |
| `GROUP_PENDING_SPLIT` — agrupamento não lido | 2 | 0 | 2 |

**Os 41 seeds não são 41 datasets independentes.** Dois são normas de identificação (ELI, ECLI); três são portais; dois são catálogos ou diretórios; um é subtarefa de um benchmark (LexGLUE); um é interface de acesso a avisos que outro seed expõe em grafo (TED Search API); um é coleção dentro do EUR-Lex (medidas nacionais de transposição); dois não puderam ser lidos.

**O que deixou de ser contado como recurso:**

- vinte entradas anuais de catálogo do Jornal Oficial: um recurso com muitas distribuições;
- três entradas de catálogo que são visões de busca do EUR-Lex;
- cinco entradas de catálogo de seeds já registrados (comitologia, grupos de peritos, registro de transparência, votações do Conselho, ECLI);
- dezenas de reenvios no Hugging Face.

## 5. Recursos com evidência verificada

| Estado | Total | Seeds | Novos |
|---|---|---|---|
| `VERIFIED` | 31 | 31 | 0 |
| `PARTIALLY_VERIFIED` | 41 | 8 | 33 |
| `DISCOVERED` | 30 | 0 | 30 |
| `INACCESSIBLE` | 2 | 2 | 0 |
| `INDETERMINATE` | 1 | 0 | 1 |

Os 31 verificados são todos seeds, porque só as páginas dos seeds foram abertas. Os novos têm, no máximo, metadados de API de repositório; nenhum teve a página lida.

**Seeds:** antes desta rodada, 3 dos 41 nomes tinham sido conferidos na fonte. Agora 38 têm nome baseado em página primária ou metadado de catálogo; em 1 (EU08) o nome é inferência, porque a página é dinâmica; em 2 (EU10, EU32) o acesso falhou.

**Parcialmente verificados entre os seeds (8):** EU03 (acesso com autenticação), EU08 (página dinâmica; API respondeu), EU12 (a URL registrada é página de política), EU14 e EU24 (aplicações dinâmicas), EU19 (mantenedor não declarado na página), EU21 (registro não aberto), EU31 (casca de navegador não suportado).

## 6. Classificação preliminar por tipo

Categoria proposta, todas com `category_status = CANDIDATE`.

| Categoria | Total | Seeds | Novos |
|---|---|---|---|
| `DATASET` | 41 | 7 | 34 |
| `CORPUS` | 13 | 2 | 11 |
| `ADMINISTRATIVE_REGISTER` | 12 | 8 | 4 |
| `BENCHMARK` | 10 | 3 | 7 |
| `REPOSITORY` | 8 | 7 | 1 |
| `INDETERMINATE` | 4 | 2 | 2 |
| `ACCESS_PORTAL` | 3 | 3 | 0 |
| `CATALOGUE` | 3 | 2 | 1 |
| `STANDARD_OR_VOCABULARY` | 3 | 2 | 1 |
| `API` | 2 | 2 | 0 |
| `DATA_DISTRIBUTION` | 2 | 1 | 1 |
| `INFRASTRUCTURE` | 2 | 2 | 0 |
| `SOFTWARE_OR_PIPELINE` | 2 | 0 | 2 |

A composição reflete onde se procurou. Os novos são quase todos datasets, corpora e benchmarks porque seis dos sete serviços consultados são repositórios de dados de pesquisa. Registros administrativos e repositórios institucionais vieram dos seeds. A tabela não mede a composição do campo.

## 7. Distribuição pelos conjuntos

| Conjunto | Total | Seeds | Novos | Individuados |
|---|---|---|---|---|
| A — legislativo e jurídico | 70 | 25 | 45 | 56 |
| B — governança regulatória | 30 | 14 | 16 | 27 |
| AB | 5 | 2 | 3 | 5 |

| Estado | A | B | AB |
|---|---|---|---|
| `VERIFIED` | 20 | 10 | 1 |
| `PARTIALLY_VERIFIED` | 25 | 12 | 4 |
| `DISCOVERED` | 23 | 7 | 0 |
| `INACCESSIBLE` | 1 | 1 | 0 |
| `INDETERMINATE` | 1 | 0 | 0 |

**Onde cada tipo aparece.** Em A: 25 datasets, 13 corpora, 9 benchmarks, 7 repositórios, 3 normas ou vocabulários, 3 catálogos. Em B: 13 datasets e 12 registros administrativos. Todos os corpora e quase todos os benchmarks estão em A.

A diferença entre A e B é esperada pela forma da busca e não deve ser lida como diferença real de disponibilidade. Dados de governança regulatória tendem a existir como registros em sítios de órgãos, fora de catálogos e de repositórios de pesquisa, e as consultas desta rodada alcançam mal esse tipo de recurso.

## 8. Mantenedores e famílias institucionais

| Família | Recursos |
|---|---|
| Comissão Europeia (direções-gerais, Secretariado-Geral, JRC) | 20 |
| Serviço das Publicações da UE | 13 |
| Outros órgãos e agências da UE (TJUE, EDPB, AEA, ESMA, Eurostat) | 6 |
| Parlamento Europeu | 2 |
| Conselho da UE | 2 |
| Órgãos públicos nacionais (Luxemburgo, Letônia, Suécia) | 4 |
| Acadêmicos, indivíduos e projetos cívicos | 51 |
| Não apurado | 7 |

O Serviço das Publicações mantém o núcleo do conjunto A entre os recursos oficiais: EUR-Lex, Cellar, o data dump, as listas do Jornal Oficial, EU Vocabularies, ELDS, e também os serviços TED. Qualquer comparação entre "fontes legislativas oficiais" precisa perguntar antes quantos mantenedores independentes há. Nesta base, entre os recursos oficiais de textos legislativos, há essencialmente um.

A atribuição de mantenedor tem bases diferentes: em 98 linhas há valor, mas em vários casos ele é o publicador declarado no catálogo, o dono de uma conta em repositório, ou uma inferência (marcada em `field_basis`).

## 9. Relações entre recursos

32 relações: 12 `SUPPORTED`, 20 `CANDIDATE`.

| Tipo | Total |
|---|---|
| `overlaps_with` | 9 |
| `derived_from` | 8 |
| `links_to` | 6 |
| `distribution_of` | 3 |
| `part_of` | 2 |
| `uses` | 2 |
| `access_interface_for` | 1 |
| `catalogues` | 1 |

**EU03 e EU07 (caso de teste).** A página `https://data.europa.eu/en/ELDS` apresenta o European Legal Data Space e, em seção própria, o EUR-Lex data dump, com outro endereço. A base registra dois recursos (`MR-0003`, `MR-0007`), uma relação `links_to` entre eles e nenhuma `same_resource_as`. Para `MR-0003`: página de descrição = a página ELDS; acesso = `https://datadump.publications.europa.eu/`, com `AUTH_REQUIRED`. O servidor respondeu 401 pela terceira vez em duas fases, sem cabeçalho de desafio; nenhuma autenticação foi tentada. O recurso continua `PARTIALLY_VERIFIED` e elegível. Há ainda uma entrada de catálogo para o dump (`eur-lex-data-dump`, emitida em 2025-05-08).

**Divergência entre descrições oficiais do dump.** A página ELDS e a página de reuso do EUR-Lex dizem: atos em vigor, setor CELEX 3. A entrada de catálogo diz: setores 2, 3 e 4 (acordos internacionais, atos jurídicos e legislação complementar). Só o acesso resolve. Registrado em `DEC-0003`, sem preferência.

**Núcleo EUR-Lex.** A página de reuso do EUR-Lex descreve quatro vias de obtenção: serviço web para usuários registrados; data dump; listas do Jornal Oficial em Formex no data.europa.eu; acesso direto ao Cellar por SPARQL e REST. Daí três relações candidatas (`MR-0003` e `MR-0004` como distribuições do EUR-Lex; EUR-Lex como interface do Cellar). O que não foi verificado é se alguma via contém algo que as outras não têm.

**Oficiais e derivados.** Oito relações `derived_from`. Quatro apontam para o EUR-Lex; duas para o MultiEURLEX (LexGLUE e um pacote de avaliação de embeddings); uma para as listas do Jornal Oficial (DGT-Acquis, declarada na página); uma para o InfoCuria (candidata fraca). Três estão sustentadas por declaração da fonte; as demais se apoiam em nome ou em citação.

**Cadeia de derivação em benchmarks.** Os metadados do LexGLUE listam a configuração `eurlex` e citam o artigo do MultiEURLEX. Isso sustenta, como candidata de confiança média, a relação que o G1-READY deixou como não verificada (EU35–EU39). Se confirmada, a cadeia é EUR-Lex → MultiEURLEX → LexGLUE, e as três não são fontes independentes de atos.

**Sobreposições candidatas** entre registros da Comissão (documentos, atos delegados e de execução, comitologia), entre a API do Parlamento e o Observatório Legislativo, e entre os dois serviços TED. Nenhuma foi medida.

## 10. Acesso, cobertura e licenciamento

**Pontos de acesso (86)**

| Resultado do teste | Pontos |
|---|---|
| `ACCESSIBLE` | 46 |
| `NOT_TESTED` | 27 |
| `JS_ONLY_SHELL` | 8 |
| `BLOCKED_TO_TOOL` (403) | 2 |
| `NETWORK_ERROR` | 2 |
| `AUTH_REQUIRED` (401) | 1 |

- **Páginas dinâmicas.** Oito endereços devolvem só a casca sem JavaScript: portal de desenvolvedores do Parlamento, páginas de dataset do data.europa.eu, busca de casos de concorrência, registros de comitologia, de grupos de peritos e de atos delegados, Reportnet 3. Para os catalogados, a API do catálogo supriu os metadados.
- **Bloqueio a cliente automatizado.** Página de votações do Conselho e buscador ECLI do e-Justice: 403.
- **Falha local.** `echa.europa.eu` e `chem.echa.europa.eu` falharam na verificação de certificado nesta máquina. É problema do ambiente; a verificação não foi desativada.
- **Autenticação.** Um caso confirmado (data dump). O serviço web do EUR-Lex exige registro, segundo a página; não foi testado.
- **Redirecionamento.** O endereço do NANDO leva hoje à aplicação Single Market Compliance Space.

`ACCESSIBLE` significa que uma requisição simples devolveu conteúdo. Não significa que os dados foram obtidos.

**Formatos e modos de acesso.** Formato declarado em 29 dos 105; modo de acesso em 55. Entre estes: download em lote em 40, busca na web em 15, API em 5, SPARQL em 3. O predomínio de download reflete os repositórios de pesquisa.

**Licenças.** Há indicação em 37 dos 105 (11 seeds). CC BY 4.0 em 14; o código `COM_REUSE` do catálogo em 9; CC BY-SA 4.0 em 3; Apache-2.0 em 3; e casos únicos (CC0, CC BY 2.0, MIT, uso não comercial, "unknown"). São códigos e frases copiados das fontes, sem leitura dos termos. Para 68 recursos a licença não foi apurada, o que não quer dizer que não exista.

**Cobertura temporal.** Declarada em 17 dos 105. Vai de séries longas (1952–2020; 1958–2021; 1965–2013) a recortes curtos.

**Metadados jurídicos.** A coluna de identificadores tem valor em 43 linhas, mas em 39 ele vem do inventário de seeds, sem conferência. Em 4 há evidência direta: identificadores `eli/dl/proc` na API do Parlamento; identificadores próprios no registro do EDPB; ELI no pacote de metadados do EUR-Lex e nas entradas nacionais. **Não há, nesta rodada, base para afirmar quais recursos suportam CELEX, ELI ou ECLI.**

**Capacidade longitudinal.** Não avaliada. Os indícios disponíveis são poucos e indiretos: versões ou instantâneos em 9 recursos; atualização declarada em 7, dos quais 2 descontinuados (votações do Conselho; déficit de transposição do Eurostat).

## 11. Lacunas observadas e grau de confirmação

Nenhuma é lacuna confirmada do campo. São ausências nesta rodada, com explicações possíveis.

| Observação | Grau | Explicação alternativa |
|---|---|---|
| Nove consultas ao data.europa.eu sobre temas de B (infrações, sinalizadores de confiança, autoridades competentes, acreditação, autorizações, consultas públicas) e sobre CELLAR e atos delegados não deram nenhum registro ligado a recurso | Observado em 25 resultados por consulta | Busca textual livre sobre catálogos de toda a Europa; vários desses recursos existem e foram verificados nos próprios sítios |
| Nenhum dataset acadêmico sobre organismos notificados, acreditação ou intermediários regulatórios | Não procurado diretamente nos repositórios acadêmicos | Faltam as consultas |
| Poucos recursos ligam atos da UE a autoridades ou entidades responsáveis por aplicá-los | Impressão do agente, sem contagem | Campo `observation_unit` não verificado; conteúdo não aberto |
| Dados de fiscalização aparecem como registros de decisões em PDF ou interfaces de busca (EDPB; casos de concorrência) | Dois casos observados | Exportações podem existir e não foram procuradas |
| Recursos de transposição são nacionais e heterogêneos (Luxemburgo, Letônia, países de Visegrado) ou agregados (placar do mercado único) | Oito registros (`MR-0047` a `MR-0050`, `MR-0061`, `MR-0070` a `MR-0072`) | O acervo central (medidas nacionais no EUR-Lex) não foi examinado quanto a exportação |
| Dois recursos de acompanhamento descontinuados | Declarado nos catálogos | Podem ter sucessores não localizados |
| Recursos oficiais de textos legislativos dependem de um mantenedor | Observado nos mantenedores registrados | — |

## 12. Pendências

**Por recurso**

- 30 `DISCOVERED`: abrir a página ou o registro. Entre eles, 9 conhecidos só pelo artigo que os apresenta (falta localizar o depósito) e 5 conhecidos só por menção em página lida.
- 33 novos `PARTIALLY_VERIFIED`: ler o registro do repositório.
- 2 `INACCESSIBLE`: votações do Conselho (EU10) e ECHA (EU32). Tentar de outro ambiente ou por captura manual no navegador.
- 2 agrupamentos a desdobrar: ELI nacionais; séries Swedac.
- `MR-0089` (EURLex-4K): origem não identificada.

**Fontes a montante mencionadas e ainda não registradas:** EuroVoc como recurso próprio; GDPRhub; OpenEFSA; o corpus MAPA; o corpus Europarl original; o depósito do CEPS EurLex.

**Pistas vindas de buscas não registradas** (ferramenta de busca do agente; não estão na base): catálogo de datasets jurídicos e regulatórios do projeto LYNX; DEU-III no B2FIND; coleção EUR-Lex da TU Darmstadt, possível origem de `MR-0089`. Devem entrar por consulta registrada ou como encadeamento documentado.

**Decisões científicas em aberto**

1. Regra para os 14 registros com elegibilidade `UNCERTAIN`.
2. Compilações temáticas de uma só política entram ou não (`DEC-0011`).
3. Adoção das categorias `STANDARD_OR_VOCABULARY` e `SOFTWARE_OR_PIPELINE`.
4. Criar ou não conta para ver o data dump.
5. Portais e catálogos contam como recursos ou são relatados à parte.

## 13. Limitações do primeiro ciclo

1. Classificação por um único agente de IA, sem segunda leitura.
2. Busca não exaustiva; 25 resultados por consulta; inglês.
3. Nenhum conteúdo de dataset examinado: cobertura, unidade de observação, identificadores e qualidade não foram verificados.
4. Metadados de catálogo e de repositório aceitos como declarados, inclusive quando parecem desatualizados.
5. Vários campos dos seeds seguem como vieram do inventário (`SEED_UNVERIFIED`).
6. Composição enviesada pelas plataformas: A e pesquisa acadêmica sobre-representados; registros de reguladores sub-representados.
7. Observações de um único dia.
8. Leitura das páginas por modelo de linguagem, sujeita a erro; a evidência preservada permite conferir.
9. As relações candidatas são hipóteses.
10. Triagem das 1.251 ocorrências por título, por um só leitor.

## 14. Recomendações

Em ordem de retorno esperado.

1. **Fechar os 30 `DISCOVERED` e os 33 parciais novos**: uma captura do registro ou da página para cada, e leitura da licença.
2. **Atacar o conjunto B por onde ele vive.** Partir da lista de agências e órgãos da UE e visitar as páginas de registros e de dados abertos de cada um. É a via com maior chance de mudar a composição do inventário.
3. **Consultar o catálogo data.europa.eu por publicador** (SPARQL ou filtros da API), em vez de texto livre.
4. **Ler os artigos** de dados achados no OpenAlex e seguir as referências, sobretudo em conformidade, infrações, delegação e agências.
5. **Registrar as fontes a montante** já mencionadas.
6. **Resolver o que só depende de ambiente**: Conselho e ECHA de outra máquina; páginas dinâmicas por captura manual, com o procedimento `register` já existente.
7. **Decidir as cinco questões em aberto** da seção 12.
8. **Validação amostral independente** antes de publicar qualquer contagem por categoria ou conjunto: amostra estratificada dos 105, segunda pessoa, mesmas capturas, sem ver a classificação do agente.
9. **Só depois**, aprofundar o que os recursos contêm: identificadores jurídicos, cobertura temporal, capacidade longitudinal.

## Onde está cada coisa

| Item | Caminho |
|---|---|
| Recursos | `mapping/data/resources.csv` |
| Pontos de acesso | `mapping/data/access_endpoints.csv` |
| Relações | `mapping/data/resource_relations.csv` |
| Descobertas e buscas | `mapping/data/discovery_log.csv` |
| Evidências | `mapping/data/evidence_registry.csv`; arquivos em `mapping/evidence/` |
| Decisões | `mapping/data/decisions_log.csv` |
| Auditoria dos 41 seeds | `mapping/data/seed_audit.csv` |
| Ocorrências brutas | `mapping/data/search_hits.csv` |
| Dicionário e vocabulários | `mapping/data/DATA_DICTIONARY.md`; `mapping/schemas/mapping_vocabularies.json` |
| Julgamentos da rodada | `mapping/curation/round1.py` |
