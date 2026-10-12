# REORIENTAÇÃO DO ESTUDO — MAPEAMENTO INDEPENDENTE v1.0

**Data:** 2026-10-10 | **Gate:** G2 | **Natureza:** emenda rastreável aos protocolos de G0, G0.1, G1-PREP e G1-READY. Não os substitui nem os reescreve.
**Responsabilidade científica:** Igor Caires Machado.
**Redação:** agente de programação (Claude Code), por instrução da coordenação registrada na tarefa G2. As decisões descritas aqui são as da instrução; onde o agente propôs algo além dela, o texto diz "proposta".

## 1. Por que a orientação mudou

Até G1-READY, o estudo existia para justificar a escolha de uma infraestrutura legislativa para um dataset de arquiteturas de governança regulatória, no projeto conduzido com David Levi-Faur. Essa finalidade produziu instrumentos cuidadosos, mas tornou o mapeamento dependente de decisões que não são dele: os parâmetros U1–U6 do universo jurídico, a designação de dois avaliadores, a aprovação de uma amostra de 20 itens.

O efeito foi que, depois de quatro gates, nenhuma fonte além de duas URLs havia sido aberta. O dossiê G1-READY registra isso: 39 das 41 URLs do inventário não tinham sido consultadas, e 38 dos 41 nomes não tinham sido conferidos.

A coordenação decidiu separar as duas coisas. O levantamento do que existe passa a ser uma pesquisa em si. A escolha de fontes para a operacionalização RGAM/V8 passa a ser uma aplicação possível dos resultados.

Três consequências práticas:

1. A descoberta não espera U1–U6, nem a designação de avaliadores, nem autorização de terceiros.
2. Nenhum recurso entra ou sai do inventário por ser ou não útil ao RGAM/V8.
3. Os controles de validade continuam, mas ajustados ao que um mapeamento precisa: evidência preservada, origem de cada registro, separação entre o que foi verificado e o que foi inferido.

Nenhuma decisão descrita neste documento é atribuída a David Levi-Faur ou à equipe do projeto colaborativo.

## 2. Pergunta e objetivos

**Pergunta.** *What datasets and data infrastructures are available for the systematic study of European Union legislation and regulatory governance, and what are their characteristics, capabilities, relationships, and limitations?*

Quais datasets e infraestruturas de dados estão disponíveis para o estudo sistemático da legislação e da governança regulatória da União Europeia, e quais são suas características, capacidades, relações e limitações?

**Objetivos específicos**

| # | Objetivo | Onde aparece na base |
|---|---|---|
| 1 | Identificar e inventariar recursos | `resources.csv`, `discovery_log.csv` |
| 2 | Classificar tipos de recurso | `resource_category`, `individuation_status` |
| 3 | Descrever mantenedores e coberturas | `maintainer`, `thematic_coverage`, `territorial_scope`, `temporal_coverage` |
| 4 | Documentar acesso, formatos, identificadores, reuso | `access_endpoints.csv`; `formats`, `access_modes`, `identifiers_supported`, `licence_or_reuse` |
| 5 | Reconstruir relações entre recursos | `resource_relations.csv` |
| 6 | Examinar limitações | `access_status`, `access_conditions`, `uncertainties` |
| 7 | Identificar lacunas estruturais | Relatórios; nenhuma lacuna é afirmada sem dizer o grau de confirmação |
| 8 | Disponibilizar inventário rastreável | Toda a pasta `mapping/` |
| 9 | Avaliar aplicação a estudos de arquitetura regulatória | Secundário; adiado |

## 3. Objetivo principal e aplicação ao RGAM/V8

| | Mapeamento (objetivo principal) | Aplicação ao RGAM/V8 (secundária) |
|---|---|---|
| Pergunta | O que existe e como é | O que serve para codificar arquiteturas de governança |
| Critério de inclusão | Relação com legislação ou governança regulatória da UE | Adequação como fonte de textos e de enriquecimento |
| Depende de U1–U6 | Não | Sim |
| Instrumento | Este documento e o protocolo de mapeamento | `SOURCE_SELECTION_FRAMEWORK_v0_1.md`, preservado |
| Estado | Em execução | Adiado; nenhuma fonte foi avaliada nem escolhida |

A base não tem coluna de "potencial RGAM". As colunas `rgam_potential` e `initial_priority` do inventário de seeds ficam onde estão, no arquivo original, e não são copiadas.

## 4. Escopo: conjuntos A e B

**Conjunto A — dados legislativos e jurídicos da UE.** Direito primário e derivado; regulamentos, diretivas e decisões; atos delegados e de execução; procedimentos e documentos preparatórios; alterações, revogações, consolidações; identificadores (CELEX, ELI, ECLI); transposição nacional; jurisprudência sobre a aplicação do direito da UE; corpora acadêmicos e bases derivadas; dados estruturados extraídos de documentos jurídicos.

**Conjunto B — dados de governança regulatória da UE.** Reguladores e autoridades competentes; fiscalização e sanções; autorização, licenciamento, certificação; acreditação e avaliação de conformidade; intermediários regulatórios; delegação e implementação de obrigações; transparência e participação; supervisão e prestação de contas; registros administrativos; bases setoriais.

**Regras**

- Cada recurso recebe `A`, `B` ou `AB`. `AB` é um valor, não duas linhas.
- A atribuição é pelo conteúdo declarado do recurso, não pelo uso que se pretende dar a ele.
- A presença de intermediários regulatórios não é critério de inclusão em B.
- **Geografia.** Prioridade a recursos de abrangência da UE. Um recurso nacional ou internacional entra quando há conexão documentada com legislação, implementação ou governança da UE; o campo `eu_connection_note` diz qual.

A fronteira entre A e B não é nítida em alguns casos (notificações de regras técnicas nacionais, obrigações de reporte anotadas em legislação, placares de transposição). Esses casos recebem `AB` com a razão em `uncertainties`. A estabilidade dessa atribuição entre pessoas diferentes não foi testada.

## 5. Unidade de análise

A unidade contada é o **recurso**: um acervo ou serviço com mantenedor, escopo declarado e conteúdo próprios. Vem do nível L1 da taxonomia v0.2, que continua valendo.

**Uma URL não é um recurso.** Uma página pode descrever dois recursos (caso EU03 e EU07), e um recurso pode ter página de descrição num endereço, acesso em outro e registro de catálogo num terceiro.

| Categoria | Definição operacional | Teste prático |
|---|---|---|
| `DATASET` | Coleção de registros com estrutura declarada, publicada como dado | Há campos, arquivo tabular ou registros exportáveis |
| `CORPUS` | Coleção de textos reunida para análise, com ou sem anotação | O conteúdo principal é texto; a unidade é o documento ou segmento |
| `BENCHMARK` | Dataset ou corpus empacotado com tarefa, rótulos e partições de avaliação | Há tarefa definida e divisão treino/teste |
| `REPOSITORY` | Acervo consultável de documentos, mantido como serviço contínuo | O conteúdo são documentos; atualiza-se por depósito ou publicação |
| `ADMINISTRATIVE_REGISTER` | Cadastro produzido na aplicação do direito: entidades, decisões, casos, notificações | A unidade não é um ato normativo de alcance geral |
| `INFRASTRUCTURE` | Plataforma com modelo de dados próprio que sustenta vários acervos ou fluxos | Há modelo ou ontologia documentados e mais de um acervo |
| `API` | Serviço programático registrado como recurso | Só quando não foi possível, ainda, ligá-lo a um recurso já registrado; caso contrário é ponto de acesso |
| `ACCESS_PORTAL` | Sítio que dá acesso a vários acervos | Vários acervos sob uma entrada |
| `SEARCH_INTERFACE` | Interface de consulta sobre um acervo | Normalmente é ponto de acesso, não recurso |
| `CATALOGUE` | Lista ou diretório de recursos de terceiros ou de vários acervos | Aponta para outros; não tem acervo próprio distinto |
| `DATA_DISTRIBUTION` | Pacote ou caminho de acesso a parte ou ao todo de outro recurso | Mesmo mantenedor e conteúdo de outro recurso |
| `DESCRIPTIVE_PAGE` | Página que só descreve outro recurso | Não se conta; vira ponto de acesso |
| `STANDARD_OR_VOCABULARY` | Norma de identificação, ontologia, tesauro, tabela de autoridades | Contém regras, códigos ou conceitos |
| `SOFTWARE_OR_PIPELINE` | Programa que obtém ou transforma dados de outra fonte | Sem dados próprios |
| `INDETERMINATE` | A evidência não permite propor | Exige dizer o que falta |

As doze primeiras vêm da instrução G2. As duas penúltimas foram acrescentadas como proposta (decisão `DEC-0014`): ELI, ECLI e a ontologia CDM não cabem em nenhuma das doze.

**Três estados separados.** A categoria diz o que o recurso parece ser. `individuation_status` diz se ele conta como recurso independente. `verification_status` diz quanta evidência há. Nesta rodada, toda categoria tem `category_status = CANDIDATE`.

**Pontos de acesso** ficam em tabela própria (`access_endpoints.csv`), com papel, origem da URL, exigência de autenticação e resultado do teste. É o nível L2 da taxonomia.

**Relações** ficam em `resource_relations.csv`, dirigidas, com tipo, confiança, base e evidência: `same_resource_as`, `distribution_of`, `derived_from`, `access_interface_for`, `catalogues`, `part_of`, `links_to`, `overlaps_with`, `successor_of`, `uses`. Uma relação é `SUPPORTED` quando uma fonte primária a declara; do contrário é `CANDIDATE`. Relação inferida de nome ou domínio tem confiança `LOW` e nunca é `SUPPORTED`; o validador impede o contrário.

## 6. Critérios preliminares de inclusão e exclusão

Derivam de I1, I2, E1 e E5 do `PROTOCOL_v1_0_DRAFT.md` (seção 6), com o filtro RGAM retirado.

**Inclui-se** o recurso que:

1. tem relação material com legislação ou governança regulatória da UE, nos termos da seção 4; e
2. é coleção ou serviço com registros consultáveis ou exportáveis, ou norma, vocabulário ou infraestrutura que os sustenta; e
3. é identificável: tem nome, responsável e algum endereço.

**Não se registra como recurso** (mas fica em `search_hits.csv` e, quando há decisão de grupo, em `decisions_log.csv`):

1. publicação sem dataset;
2. página que só descreve outro recurso;
3. cópia, reenvio ou reformatação de recurso já registrado;
4. software sem dados próprios;
5. registro nacional ou local sem conexão documentada com o direito da UE.

**Fica em aberto**, com `eligibility_preliminary = UNCERTAIN`: dados de aplicação setorial distante da regulação (contratações públicas), documentos de agenda política, debates parlamentares, jurisprudência nacional sobre um único instrumento, compilações temáticas de uma única política. A regra é do pesquisador.

**Indisponibilidade não exclui.** Falha de acesso gera `INACCESSIBLE` ou um ponto de acesso com `AUTH_REQUIRED`, `BLOCKED_TO_TOOL` ou `NETWORK_ERROR`. Nenhuma delas equivale a `OUT_OF_SCOPE`.

## 7. Riscos de duplicação e dependência

| Risco | Como aparece | Controle |
|---|---|---|
| Uma página, dois recursos | EU03 e EU07 | URL repetida exige justificativa registrada; o validador acusa as demais |
| Um recurso, muitas entradas de catálogo | Vinte entradas anuais do Jornal Oficial; três visões do EUR-Lex | Entradas viram pontos de acesso (`DEC-0004`, `DEC-0005`) |
| Cópias em repositórios de modelos | Dezenas de reenvios no Hugging Face | Não individuadas (`DEC-0009`) |
| Derivados contados como fontes | Corpora extraídos do EUR-Lex | `derived_from` obrigatório quando a origem é declarada; contagens separam oficiais e derivados |
| Dependência de uma só família institucional | Serviço das Publicações mantém grande parte do núcleo | Relatório informa mantenedores; nenhuma afirmação de independência sem verificar |
| Catálogo que agrega catálogos | data.europa.eu colhe portais nacionais | Catálogo de origem registrado na evidência; recurso atribuído ao mantenedor, não ao portal |
| Agrupamentos não lidos | ELI nacionais; séries Swedac | `GROUP_PENDING_SPLIT`, fora da contagem de individuados |

## 8. Estratégia de descoberta, classificação e atualização

Detalhe em `SYSTEMATIC_MAPPING_PROTOCOL_v1_0_DRAFT.md`.

1. **Descoberta em quatro vias**, cada uma com rótulo de origem: seeds (`SEED`); consultas registradas a serviços de busca (`SYSTEMATIC_SEARCH`); encadeamento a partir de páginas e registros lidos (`BACKWARD_FORWARD_DISCOVERY`); indicações de especialistas (`EXPERT_SUGGESTION`).
2. **Verificação na fonte primária**, com captura preservada e hash.
3. **Classificação provisória** pelo agente, marcada como tal; confirmação por pesquisador registrada em campo próprio.
4. **Atualização por rodadas.** Cada rodada tem seu arquivo de consultas e seu arquivo de curadoria. As tabelas são reconstruídas a partir deles; nada é editado à mão; identificadores nunca são reutilizados.

## 9. Limitações metodológicas

1. **Classificação por um único agente de IA.** Todas as categorias, conjuntos, estados e relações desta rodada foram propostos por um modelo de linguagem lendo as capturas. São provisórios. Rodar outro prompt no mesmo sistema não seria avaliação independente e não foi feito.
2. **A busca não é exaustiva.** Sete serviços, 54 consultas, primeiros 25 resultados de cada. Não há estimativa de cobertura.
3. **Verificação rasa.** "Verificado" significa que nome e localização constam de fonte primária capturada. Não significa que o conteúdo foi aberto, medido ou testado.
4. **Viés de idioma e de plataforma.** Consultas quase só em inglês; repositórios anglófonos; nenhum índice bibliográfico por assinatura.
5. **Páginas dinâmicas e com login** não são lidas por requisição simples. Oito pontos de acesso devolveram só a casca.
6. **O ambiente interfere.** Dois hosts falharam por causa da cadeia de certificados desta máquina, e dois recusaram o cliente automatizado.
7. **Instantâneo.** Tudo foi observado em 10 de outubro de 2026.
8. **Fronteiras em aberto.** A–B e os casos da seção 6.

## 10. Produtos esperados

| Produto | Estado |
|---|---|
| Base de mapeamento com dicionário, vocabulários e evidências | Iniciada (rodada 1) |
| Protocolo de mapeamento | Rascunho v1.0 |
| Relatório inicial | `mapping/reports/G2_INITIAL_MAPPING_REPORT.md` |
| Artigo de mapeamento | Possível; depende do que a nota de potencial de publicação aponta |
| Pacote de replicação | Scripts, consultas e respostas preservadas já permitem refazer as tabelas |
| Aplicação ao RGAM/V8 | Adiada |

## 11. Matriz de continuidade

Estado de cada elemento dos protocolos anteriores. Nenhum arquivo anterior foi alterado.

| Elemento | Origem | Estado | Observação |
|---|---|---|---|
| Inventário de 41 seeds | `inputs/seed_inventory_v0_1.csv` | RETAINED | Conjunto preliminar de descoberta; arquivo intacto (mesmo SHA-256 do G0); identificadores EU01–EU41 preservados em `seed_id` |
| Níveis de identidade L0, L1, L2 | Taxonomia v0.2, §2 | RETAINED | L0 = `search_hits.csv`; L1 = `resources.csv`; L2 = `access_endpoints.csv` |
| Nível K (contêiner) | Taxonomia v0.2, §2 | ADAPTED | Vira categoria (`ACCESS_PORTAL`, `CATALOGUE`) em vez de nível fora da contagem; a contagem de individuados é informada com e sem eles |
| Nível L3 (unidade jurídica) | Taxonomia v0.2, §8 | NOT APPLICABLE | O mapeamento não conta nem codifica atos |
| Princípios "classifica-se pelo conteúdo e pelo mantenedor" e "classe ≠ relação" | Taxonomia v0.2, §1 | RETAINED | |
| "URL igual gera candidato, nunca decisão" | Taxonomia v0.2, §5; G1-READY | RETAINED | Regra de validação e caso de teste |
| Classes FPL, REP, DSE, API, COD, REG, AUX, FDE, IND | Taxonomia v0.2, §3 | DEFERRED | Não aplicadas. Correspondência aproximada abaixo; a calibração delas continua sendo tarefa do Piloto A |
| Regras R0–R11 | Taxonomia v0.2, §4 | DEFERRED | R0–R2 inspiram as decisões de individuação; a sequência completa não foi aplicada |
| Vocabulário de relações | Taxonomia v0.2, §5 | ADAPTED | `duplicate_of` → `same_resource_as`; `hosted_by` → `catalogues` (sentido inverso); acrescentados `access_interface_for` e `links_to` |
| Identificadores opacos | Taxonomia v0.2, §7 | ADAPTED | Série própria `MR-nnnn`. A série `R` + quatro dígitos continua reservada a recursos adjudicados |
| Indicador `legislative_candidate` | Taxonomia v0.2, §6 | DEFERRED | Pertence à aplicação secundária |
| Critérios I1, I2, E1, E5 | Protocolo v1.0, §6 | ADAPTED | Seção 6 deste documento |
| Consultas Q01–Q14 | `inputs/search_queries.csv` | ADAPTED | Desdobradas em 54 consultas registradas; Q09 em OpenAlex apenas; Q13 e Q14 só como sondagem (2 consultas) |
| Registro obrigatório de buscas e de falhas | `SEARCH_STRATEGY.md` | RETAINED | Implementado em `mapping_search.py` |
| Teste de recuperação com seeds | `SEARCH_STRATEGY.md` | ADAPTED | Registrado como `SEED_REFOUND_BY_SEARCH`: 12 dos 41 |
| Política de IA: saída de modelo não é evidência | `LLM_RESEARCH_INTEGRITY.md`; quadro de seleção, §8 | RETAINED | Toda linha traz `AGENT_PROVISIONAL` |
| Protocolo de captura: fidelidade, hash, falha ≠ ausência, sem login | G1-READY | RETAINED | Mesma ferramenta, sem alteração |
| Autorização em duas etapas para capturar | G1-READY, §8 | ADAPTED | A instrução G2 autoriza a descoberta; a disciplina de acesso está no protocolo de mapeamento |
| Separação coordenador/avaliador; pacotes cegos | G1-READY, §5 | DEFERRED | Volta a valer se houver validação amostral independente |
| Piloto A: amostra S3a, rótulos, pacotes, AC1–AC31, alerta 7/10 | G1-PREP, G1-READY | DEFERRED | Preservado sem alteração. Pode ser reaproveitado como validação amostral da classificação |
| Concordância entre avaliadores como condição de início | G1-PREP | NOT APPLICABLE | Não se exige para descobrir; proposta para antes de publicar classificações com julgamento |
| Parâmetros U1–U6 | Quadro de seleção, §2; brief U1–U6 | DEFERRED | Não condicionam o mapeamento |
| Dimensões A e B, eliminatórios, regra de decisão | Quadro de seleção | DEFERRED | Aplicação secundária; nenhuma fonte avaliada |
| EUR-Lex/CELLAR como candidato prioritário a testar | Registro de decisões v1.1 | DEFERRED | Sem efeito sobre o mapeamento |
| Critérios técnicos de auditoria (LEGAL_ID, TEMPORALITY, …) | Codebook | ADAPTED | Tornam-se campos descritivos, sem pontuação |
| Tipologia D0–D3 e subestudo RIT | Codebook; Protocolo §14 | NOT APPLICABLE | |
| Tabelas `data/*.csv` e `scripts/cli.py` | Estrutura original | RETAINED | Intocadas; a base nova está em `mapping/data/` |
| Manuscrito do projeto colaborativo | `manuscript/` | NOT APPLICABLE | Não tocado |

**Correspondência aproximada entre categorias e classes da taxonomia v0.2.** Serve para leitura; não é reclassificação. `REPOSITORY` ≈ FPL ou REP; `DATASET` ≈ DSE ou REG; `ADMINISTRATIVE_REGISTER` ≈ REG; `CORPUS` e `BENCHMARK` ≈ COD; `STANDARD_OR_VOCABULARY` ≈ AUX; `INFRASTRUCTURE` e `API` ≈ API; `ACCESS_PORTAL` e `CATALOGUE` ≈ nível K; `DATA_DISTRIBUTION` ≈ nível L2; `SOFTWARE_OR_PIPELINE` ≈ FDE com motivo próprio; `INDETERMINATE` ≈ IND.

## 12. O que este documento não decide

A regra para os casos de fronteira da seção 6; a adoção definitiva das duas categorias acrescentadas; se haverá validação amostral e por quem; onde a base será depositada e sob qual licença; qualquer coisa sobre o projeto colaborativo.
