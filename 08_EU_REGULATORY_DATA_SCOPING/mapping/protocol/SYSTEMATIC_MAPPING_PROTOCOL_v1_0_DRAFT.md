# PROTOCOLO DE MAPEAMENTO SISTEMÁTICO — v1.0 DRAFT

**Data:** 2026-10-10 | **Estado:** rascunho em uso. Descreve o que foi feito na rodada 1 e o que vale para as seguintes. Aberto a revisão pelo pesquisador responsável.
**Lê-se junto com:** `INDEPENDENT_MAPPING_REORIENTATION_v1_0.md` (pergunta, escopo, unidade de análise).

## 1. Que tipo de estudo é este

É um **mapeamento de recursos e infraestruturas de dados**. O objeto são datasets, corpora, registros, repositórios e serviços. Não é uma revisão sistemática de publicações.

A diferença tem consequências:

| | Revisão de publicações | Este mapeamento |
|---|---|---|
| Unidade | Estudo publicado | Recurso de dados |
| Onde se procura | Índices bibliográficos | Catálogos de dados, repositórios, sítios institucionais; índices bibliográficos só para achar artigos que apresentam datasets |
| Identidade | DOI do artigo | Não há identificador universal; a identidade é estabelecida caso a caso |
| Duplicata | Mesmo registro em duas bases | Mesma coleção em vários endereços, formatos e cópias |
| Estabilidade | O artigo não muda | O recurso muda, muda de endereço e some |
| Universo | Em princípio enumerável | Não enumerável: muito do que existe não está em catálogo algum |

O protocolo toma emprestados princípios de três tradições, sem tratar nenhuma como selo de validade:

- das **scoping reviews** (JBI; PRISMA-ScR): pergunta ampla definida de antemão, critérios escritos, busca em etapas, registro do fluxo de seleção, extração padronizada;
- do **systematic mapping**: classificar e contar o que existe, em vez de sintetizar achados;
- dos **princípios FAIR**: descrever cada recurso por identificador, acesso, formato, licença e proveniência.

O que não se segue: não há dois avaliadores independentes na triagem; não há avaliação de qualidade dos recursos; não há registro prévio em plataforma pública. Qualquer relato deste estudo deve dizer isso.

## 2. Fontes de busca

**Rodada 1, executada**

| Código | Serviço | Para quê | Acesso |
|---|---|---|---|
| DEU | API de busca do data.europa.eu | Recursos institucionais catalogados | Público, sem chave |
| ZEN | API de registros do Zenodo | Dados de pesquisa | Público |
| DVN | API de busca do Harvard Dataverse | Dados de replicação em ciências sociais | Público |
| DCT | API REST do DataCite | Datasets com DOI | Público |
| OAX | API de obras do OpenAlex | Artigos que apresentam datasets | Público |
| HF | API de datasets do Hugging Face Hub | Corpora e benchmarks de PLN | Público |
| GH | API de busca de repositórios do GitHub | Dados hospedados com código | Público, com limite de taxa |

Além disso: leitura direta das páginas registradas nos 41 seeds e de 17 endereços de acesso indicados por elas.

**Previstas para as próximas rodadas** (não executadas): consulta SPARQL ao catálogo do data.europa.eu com filtro por publicador; EU Vocabularies; portais de dados de agências da UE; outros Dataverses (DANS, GESIS, UK Data Service); CLARIN e ELRC para recursos linguísticos; Scopus e Web of Science, se houver acesso; listas de datasets em revisões de PLN jurídico e de estudos empíricos de direito da UE.

## 3. Estratégia de busca

1. **Consultas por família de recursos.** Cada consulta é uma linha de um arquivo de registro (`SEARCH_QUERIES_G2_ROUND1.csv`): identificador, família, conjunto visado, serviço, texto exato, idioma, justificativa.
2. **Uma requisição por consulta**, ao endpoint documentado do serviço, com 25 resultados pedidos na ordenação padrão do serviço.
3. **Resposta preservada** byte a byte, com SHA-256, URL completa e hora UTC (`mapping/evidence/searches/`).
4. **Ocorrências extraídas** das respostas guardadas, sem rede, para `search_hits.csv`.
5. **Triagem** dos títulos e, quando o serviço as fornece, das descrições.
6. **Encadeamento**: links e menções nas páginas e registros lidos geram novos candidatos, com origem `BACKWARD_FORWARD_DISCOVERY` e a página de origem como evidência.
7. **Consultas sem resultado útil são registradas** como tais (`hits_linked_to_resources = 0`).

**Reprodutibilidade.** A URL de cada consulta é função determinística do texto. Repetir a consulta em outra data pode devolver outros resultados: o que se reproduz é a transformação das respostas guardadas em tabelas, coberta por teste. Uma consulta já executada não é repetida pelo mesmo comando; para repeti-la, cria-se nova linha com novo identificador.

**Idiomas.** Inglês em 52 das 54 consultas; uma em francês e uma em alemão, como sondagem. O catálogo data.europa.eu traduz metadados, o que atenua mas não elimina o viés.

**Janela.** Todas as buscas e capturas da rodada 1 foram feitas em 2026-10-10. Não há recorte por data de publicação dos recursos.

## 4. Elegibilidade

Critérios na seção 6 do documento de reorientação. Na prática da triagem:

| Situação | Tratamento |
|---|---|
| Relação com direito ou governança da UE e coleção identificável | Registra-se como recurso |
| Entrada de catálogo de recurso já registrado | Ponto de acesso desse recurso |
| Cópia ou reformatação | Não se registra; decisão de grupo no log |
| Artigo cujo título anuncia um dataset | Registra-se o dataset como `DISCOVERED`, com o artigo como descrição |
| Artigo sem dataset anunciado | Não se registra |
| Caso de fronteira | Registra-se com `UNCERTAIN` |
| Sem relação com a UE | Não se registra |

A triagem desta rodada foi feita pelo agente, por título e descrição. É provisória.

## 5. Individuação e deduplicação

1. **Chaves candidatas**: URL de acesso, URL de descrição, DOI, identificador de catálogo, par nome–mantenedor.
2. **Chave igual gera candidato a duplicata, nunca fusão automática.** A decisão é registrada com evidência.
3. **Mesmo mantenedor e mesmo conteúdo, outro caminho**: ponto de acesso, não recurso.
4. **Partição por ano, idioma ou formato**: um recurso com várias distribuições.
5. **Mantenedor diferente e origem declarada**: recurso derivado, com `derived_from`.
6. **Conjunto encontrado mas não lido**: `GROUP_PENDING_SPLIT`, fora da contagem.
7. **Controle automático**: o validador recusa dois recursos com a mesma URL sem justificativa registrada, e dois recursos com o mesmo nome e mantenedor.

## 6. Verificação

| Estado | Significado |
|---|---|
| `DISCOVERED` | Sabe-se que existe por um resultado de busca ou por menção numa página lida. Nada mais foi conferido |
| `PARTIALLY_VERIFIED` | Parte da identidade consta de fonte primária ou de metadados de repositório preservados; falta o nome oficial, o mantenedor ou o ponto de acesso, ou o acesso não foi alcançado |
| `VERIFIED` | Nome e localização constam de página primária ou metadado de catálogo preservados com hash. **Não** significa que o conteúdo foi aberto, medido ou testado |
| `INACCESSIBLE` | Todas as tentativas falharam. Diz respeito ao acesso, não ao recurso |
| `INDETERMINATE` | Há evidência, mas ela não permite dizer o que o recurso é |
| `OUT_OF_SCOPE` | Fora do escopo por decisão registrada. Não usado na rodada 1 |

**Base de cada campo.** Cada valor preenchido tem a origem declarada em `field_basis`:

| Marca | Significado |
|---|---|
| `PRIMARY_PAGE` | Lido pelo agente em página primária capturada |
| `API_METADATA` | Metadado devolvido por API de repositório ou catálogo, preservado |
| `SEED_UNVERIFIED` | Copiado do inventário de seeds, sem conferência |
| `AGENT_INFERENCE` | Inferência do agente, sem declaração capturada que a sustente |

Campo sem informação recebe `NOT_ASSESSED`. Significa "não coletado", nunca "não existe".

**Hierarquia de fontes.** Página do mantenedor; depois registro de catálogo oficial; depois registro de repositório; depois artigo. Quando duas fontes oficiais divergem, registram-se as duas (ver `DEC-0003`).

**Leitura por modelo de linguagem.** As páginas foram lidas pelo agente a partir das capturas. A captura é a evidência; a leitura é interpretação e pode errar. Buscas na web por ferramenta de busca do agente não são reproduzíveis e seus resumos não entram na base; foram usadas só para procurar trabalhos anteriores (nota de publicação) e estão identificadas lá.

## 7. Resultados inacessíveis

| Observado | Registro | Não se faz |
|---|---|---|
| HTTP 401 ou página de login | Ponto de acesso `AUTH_REQUIRED`; recurso continua no inventário | Criar conta ou autenticar sem decisão do pesquisador |
| HTTP 403 a cliente automatizado | `BLOCKED_TO_TOOL` | Disfarçar o cliente ou insistir |
| Erro de rede ou de certificado | `NETWORK_ERROR`, com o erro literal | Desativar a verificação de certificado |
| Página que só funciona com JavaScript | `JS_ONLY_SHELL`; busca-se outra fonte primária | Tratar a casca como conteúdo |
| Nenhuma via funcionou | Recurso `INACCESSIBLE`, elegibilidade inalterada | Converter em exclusão |

Toda tentativa fica no registro de evidências, inclusive as que falharam.

## 8. Extração de metadados

Campos e vocabulários: `mapping/data/DATA_DICTIONARY.md` e `mapping/schemas/mapping_vocabularies.json`.

Regras:

1. Preenche-se o que a fonte diz, na forma em que diz. Licenças são registradas pelo código ou frase da fonte, sem interpretação jurídica.
2. Não se completa campo por suposição.
3. Todo recurso tem `uncertainties` preenchido: o que não foi conferido é dito.
4. Os julgamentos entram por um arquivo de curadoria por rodada (`mapping/curation/round1.py`). As tabelas são geradas a partir dele e das evidências. Não se editam as tabelas.

## 9. Disciplina de acesso

1. Só endpoints públicos e documentados, e páginas públicas.
2. Uma requisição por consulta ou por página; no máximo duas tentativas; pausa de 2 a 5 segundos entre requisições.
3. Cliente identificado como pesquisa acadêmica no cabeçalho `User-Agent`.
4. Sem autenticação, sem contorno de bloqueio, sem rastreamento de links.
5. Sem download de corpora. A rodada 1 baixou páginas e respostas de API; nenhum dataset.
6. As capturas ficam no repositório de trabalho como evidência. Antes de qualquer publicação da base, decidir se as cópias de páginas de terceiros podem ser redistribuídas ou se vão só os hashes.

**Volume da rodada 1:** 54 requisições de busca e 57 tentativas de captura em 35 hosts.

## 10. Limitações de cobertura

1. **Não exaustiva.** Não há base para estimar quanto do universo foi alcançado.
2. **Profundidade de 25 resultados.** Algumas consultas reportaram mais de um milhão de resultados; só os primeiros foram vistos.
3. **Busca textual livre no data.europa.eu** devolve sobretudo registros nacionais e locais. Nove das 24 consultas ali não trouxeram nenhum registro que tenha sido ligado a um recurso.
4. **Recursos fora de catálogos** só aparecem por seed ou encadeamento. Registros de reguladores setoriais e de agências estão provavelmente sub-representados; isso é uma suspeita, não uma medida.
5. **Datasets que só existem como material suplementar de artigos** quase não são alcançados.
6. **Teste de recuperação:** as consultas reencontraram 12 dos 41 seeds. Isso mede as consultas contra uma lista que não é amostra do universo; serve de alerta, não de estimativa.

## 11. Rastreabilidade e versionamento

| Elemento | Onde |
|---|---|
| Consultas | `mapping/protocol/SEARCH_QUERIES_G2_ROUND<n>.csv` |
| Respostas de busca e seu registro | `mapping/evidence/searches/` |
| Capturas de páginas e seu registro | `mapping/evidence/captures/` |
| Julgamentos da rodada | `mapping/curation/round<n>.py` |
| Tabelas geradas | `mapping/data/*.csv` |
| Verificações | `mapping/scripts/validate_mapping.py`; `tests/test_mapping_base.py` |

Regras de atualização:

1. **Identificadores não se reutilizam.** Recurso fundido ou retirado mantém o identificador, com estado e decisão registrados.
2. **Evidência só cresce.** Nova captura da mesma URL é nova linha; a anterior permanece.
3. **Mudança de classificação** entra como nova decisão no log, com data e autor, sem apagar a anterior.
4. **Confirmação por pesquisador** muda `classification_basis` para `RESEARCHER_CONFIRMED` e `researcher_confirmed` para `YES`, por linha.
5. **Cada rodada** é fechada com manifesto de hashes dos arquivos de `mapping/`.
6. **Git.** Nada foi commitado nesta rodada, por instrução. O histórico por rodada depende, até lá, dos manifestos.

## 12. Qualidade

Verificações automáticas, sem rede:

| Verificação | O que acusa |
|---|---|
| Identificadores | Repetidos ou fora do padrão |
| Vocabulários | Valor fora da lista |
| Integridade referencial | Relação, ponto de acesso, descoberta ou decisão que aponta para o que não existe |
| URLs | Sintaxe inválida |
| Duplicação | Mesmo nome e mantenedor; URL compartilhada sem justificativa; relação ou ponto de acesso repetido |
| Evidência | `VERIFIED` sem captura bem-sucedida; relação sem evidência; ponto testado sem registro |
| Verificado × inferido | Relação `SUPPORTED` baseada em inferência; campo preenchido sem base declarada; linha do agente apresentada como confirmada |
| Origem | `SYSTEMATIC_SEARCH` sem ocorrência em busca registrada; busca citada que não foi executada |
| Preservação | Inventário de seeds alterado; seed ausente ou fora de ordem; nome ou URL registrados alterados |
| Arquivos | Evidência ausente ou com hash diferente |
| Determinismo | Tabelas em disco diferentes do que o construtor produz |

Os testes sintéticos mostram que as ferramentas fazem o que dizem. Não dizem nada sobre a cobertura do mapeamento.

**Validação humana.** Não é condição para descobrir. Antes de apresentar como definitivas as classificações que envolvem julgamento (categoria, conjunto, individuação, relações candidatas), propõe-se uma validação amostral independente: amostra estratificada por categoria e origem, segunda pessoa classificando a partir das mesmas capturas, sem ver a classificação do agente. Os instrumentos do Piloto A (pacotes cegos, trancamento, comparação) servem para isso com pouca adaptação.
