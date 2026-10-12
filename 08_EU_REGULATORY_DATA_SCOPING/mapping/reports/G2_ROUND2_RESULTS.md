# G2 — RESULTADOS DA RODADA 2

**Data das observações:** 2026-10-10 | **Responsabilidade científica:** Igor Caires Machado | **Execução:** agente de programação (Claude Code)
**Base:** `mapping/data/` (construída por `build_mapping_base.py`; instantâneo da rodada 1 em `mapping/snapshots/round1/`).

## Leitura rápida

A rodada 2 tinha como alvo a **confiabilidade da evidência** e a **cobertura do conjunto B**. O resultado, em uma linha por ponto:

1. **Identidade.** Os 63 candidatos pendentes da rodada 1 (30 `DISCOVERED`, 33 novos `PARTIALLY_VERIFIED`) foram verificados diretamente em registros de repositório: 59 mudaram de estado; 4 continuam `DISCOVERED` porque não têm API de registro e a página não foi lida.
2. **Dados.** Pela primeira vez houve inspeção de dados: 106 leituras dos **primeiros 4 KiB** de 92 recursos. Em 61 recursos os bytes lidos eram dados; em 14 o endereço declarado falhou; em 13 devolveu uma página HTML. Nenhum acervo foi baixado.
3. **Conjunto B.** De 35 candidatos (rodada 1) para 168 (+133 novos), obtidos por enumeração completa de 43 catálogos institucionais do data.europa.eu (50 consultas) e por 48 páginas de varredura institucional.
4. **Antecedentes.** O LYNX D2.7 foi lido integralmente e o D2.8 em parte. Das 56 linhas da tabela de portais do LYNX, 3 têm correspondência no inventário no nível da UE e 45 são portais nacionais fora do escopo atual.
5. **Capacidades.** 35 recursos têm nomes de campo observados nos primeiros bytes. Há seis com coluna chamada CELEX; **nenhum com coluna ELI ou ECLI observada**.

**Três avisos.** (a) Toda classificação segue **provisória**; nenhuma linha foi confirmada por pesquisador. (b) A diferença entre rodadas é de esforço e método, não crescimento do campo. (c) "Dados disponíveis" significa que os primeiros bytes de um endereço foram lidos; não diz nada sobre cobertura, completude ou qualidade.

## 1. Preservação e reprodução

| Verificação | Resultado |
|---|---|
| Testes da rodada 1 reproduzidos antes de alterar | 113 de 113 |
| Hashes dos 161 arquivos anteriores fora de `mapping/` | Todos conferem |
| Seeds EU01–EU41 | `inputs/seed_inventory_v0_1.csv` com o SHA-256 do G0 |
| Manifesto do G1-READY | 78 de 78 |
| Reconstrução das tabelas da rodada 1 antes de começar | Idêntica |
| Testes ao fim da rodada | **152 de 152** (113 anteriores, 39 novos) |
| Validador | 0 erros, 4 avisos (seção 4) |

**Alterações em arquivos da rodada 1** (registro completo em `mapping/CHANGES_ROUND2.md`): as oito tabelas CSV são reconstruídas a partir das duas curadorias e preservadas em `mapping/snapshots/round1/`; os dois registros JSONL (capturas e buscas) só receberam linhas novas; os scripts `mapping_search.py`, `build_mapping_base.py` e `validate_mapping.py` e o vocabulário JSON foram **estendidos de forma retrocompatível**, e os 113 testes anteriores passam sem alteração, exceto um teste que foi generalizado (lista de registros de consultas de todas as rodadas). Os documentos de protocolo e relatório da rodada 1 não foram alterados.

## 2. Dados e infraestrutura (emenda A01)

`protocol/AMENDMENT_A01_DATA_VS_INFRASTRUCTURE_v1_0.md`. Os níveis são derivados da categoria; nenhuma linha foi removida ou reclassificada.

| Contagem provisória (252 linhas) | Rodada 1 (105) | Rodada 2 (252) |
|---|---|---|
| **Nível I — dados**, individuados | 77 | **203** |
| **Nível II — infraestrutura**, individuados | 11 | **26** |
| Distribuições de nível I (nunca individuadas) | 2 | 2 |
| Categoria indeterminada | 4 | 4 |
| Candidatos fora da contagem (`CANDIDATE_SEPARATE`, `CANDIDATE_NOT_INDEPENDENT`, `GROUP_PENDING_SPLIT`) | 17 | 23 |
| **Total de linhas** | 105 | 252 |

Os números da rodada 1 foram recalculados com a regra da emenda sobre o instantâneo (as 88 linhas "individuadas" da rodada 1 incluíam portais, catálogos e normas, que agora são nível II). Eles não substituem os números publicados no relatório inicial.

**Nível I por categoria (individuados, rodada 2):** `ADMINISTRATIVE_REGISTER` 93, `DATASET` 82, `CORPUS` 13, `REPOSITORY` 8, `BENCHMARK` 7. **Nível II:** `INFRASTRUCTURE` 11, `CATALOGUE` 6, `STANDARD_OR_VOCABULARY` 5, `ACCESS_PORTAL` 3, `API` 1. Na rodada 1, sob a mesma regra: nível I = `DATASET` 39, `CORPUS` 12, `ADMINISTRATIVE_REGISTER` 11, `REPOSITORY` 8, `BENCHMARK` 7; nível II = `ACCESS_PORTAL` 3, `STANDARD_OR_VOCABULARY` 3, `CATALOGUE` 2, `INFRASTRUCTURE` 2, `API` 1.

**Inconsistências documentadas** (emenda A01, seção 3): oito. As duas pedidas:

- **`SOFTWARE_OR_PIPELINE`**: a regra de inclusão exclui software sem dados próprios, mas a categoria existe e tem dois registros (`MR-0081`, `MR-0097`). Tratamento proposto: nível II, nunca individuado; o validador avisa se for individuado.
- **`DATA_DISTRIBUTION`**: definida como não recurso, mas `MR-0003` e `MR-0043` são linhas com `CANDIDATE_SEPARATE`. Tratamento proposto: nível "distribuição", nunca `INDIVIDUATED` (o validador impede); o caso `MR-0003` fica em aberto.

## 3. Verificações de identidade

Nível `identity_level` (definição na emenda; derivado, não digitado):

| Nível | Linhas |
|---|---|
| `IDENTITY_VERIFIED` | 229 |
| `IDENTITY_PARTIAL` | 21 |
| `NOT_VERIFIED` | 2 (EU10 e EU32, ambos falhas de acesso) |

**Rodada 1 versus rodada 2 nos 63 candidatos pendentes:**

| Mudança de estado histórico | Linhas |
|---|---|
| `PARTIALLY_VERIFIED` → `VERIFIED` | 33 |
| `DISCOVERED` → `VERIFIED` | 13 |
| `DISCOVERED` → `PARTIALLY_VERIFIED` | 13 |
| Sem mudança (`DISCOVERED`) | 4 (`MR-0101` a `MR-0104`) |

Registro por linha em `verification_history.csv`, com o motivo. Dos 13 que passaram a `PARTIALLY_VERIFIED`, nove são artigos de dados (registros Crossref, DataCite ou OpenAlex lidos) cujo depósito não foi localizado: o artigo confirma que o dataset existe, não onde está. Os outros quatro: o pôster do MultiLegalPile (o registro do Zenodo não é o corpus), o repositório GitHub que usa o dataset do CEPS (o dado não está nele), as listas da Swedac (agrupadas em um recurso) e a página dos Coordenadores de Serviços Digitais.

**Correção de classificação da rodada 1.** Quatro linhas `VERIFIED` na rodada 1 (`MR-0005`, `MR-0018`, `MR-0023`, `MR-0034`) têm o mantenedor inferido ou não apurado e portanto `IDENTITY_PARTIAL`. O estado histórico foi mantido; o nível derivado as sinaliza e o validador emite aviso.

**Caso EU03 / EU07, reexaminado.** A página ELDS foi capturada de novo e tem o mesmo SHA-256 da captura do G1-READY. As duas linhas continuam como recursos distintos (`MR-0003` e `MR-0007`) sem relação `same_resource_as`. O endereço de acesso do dump respondeu 401 pela terceira vez; nenhuma autenticação foi tentada, nem inspeção de bytes (o validador e um teste impedem o endereço). Uma terceira descrição oficial do dump (entrada de catálogo, emitida em 2025-05-08) diz setores CELEX 2, 3 e 4, enquanto a página ELDS e a página de reuso dizem setor 3. A divergência não se resolve sem acesso.

## 4. Verificações de disponibilidade real de dados

**Método.** Uma requisição HTTP com faixa de bytes (`Range`), no máximo 4 KiB, por recurso, ao endereço de dados indicado pelo registro do repositório ou do catálogo. Os bytes lidos são guardados com hash. Não segue links nem baixa o restante. Uma segunda passagem tentou, uma vez, um segundo endereço nos recursos cujo primeiro endereço não devolveu dados, e uma nova tentativa nos dois casos de erro 5xx.

| Medida | Valor |
|---|---|
| Leituras registradas | 106, em 34 hospedeiros, 92 recursos |
| Bytes lidos no total | 333.344 (cerca de 326 KiB) |
| Faixa de bytes honrada pelo servidor (HTTP 206) | 59 de 106 |

**Resultado por recurso** (nível `data_availability_level`):

| Nível | Recursos | Observação |
|---|---|---|
| `DATA_AVAILABILITY_VERIFIED` | **61** | Por leitura: tabelar 21, arquivo ZIP ou OOXML 18, JSON 8, XML 6, comprimido 4, Parquet 4 |
| `LANDING_PAGE_ONLY` | 13 | O endereço devolveu HTML, em vários casos um endereço que a fonte declara como arquivo (CSV, XML) |
| `ACCESS_FAILED` | 14 | Nenhuma leitura bem-sucedida. Por leitura, 19 falhas: 404 (11), rede ou certificado (5), 5xx (3, das quais uma foi repetida e leu) |
| `LISTING_ONLY` | 3 | Listagem de repositório GitHub, sem arquivo de dados identificado |
| `DOCUMENT_ONLY` | 1 | O registro do Zenodo do MultiLegalPile é um pôster |
| `NOT_TESTED` | 160 | Sem endereço de dados no registro, endereço só HTML de acesso, ou exige autenticação |

**Declarado versus observado.** Entre os 49 recursos novos do conjunto B/A com endereço de dados declarado pelo catálogo e inspecionado: 27 devolveram dados (55%), 13 falharam (27%), 9 devolveram HTML (18%). É uma observação de um dia, em um subconjunto escolhido por ter endereço de dados; não é taxa de obsolescência de catálogos.

**Falhas de acesso do ambiente** (não do recurso): três hospedeiros ECHA e um da ERA e outro do ELRC falharam por erro de rede ou de certificado nesta máquina; a verificação de certificado não foi desativada.

## 5. Capacidades confirmadas

`capability_level = CAPABILITY_VERIFIED` em **35 recursos** (116 observações em `capabilities.csv`). Cada observação diz que, nos primeiros bytes lidos, há coluna ou chave com nome compatível com o padrão.

| Capacidade | Recursos | Exemplos |
|---|---|---|
| `SCHEMA_FIELDS_OBSERVED` (nomes de campo lidos) | 35 | — |
| `FIELD_DATE` | 21 | |
| `FIELD_ENTITY_ID` | 20 | |
| `FIELD_ENTITY_NAME` | 14 | |
| `FIELD_COUNTRY_OR_MEMBER_STATE` | 7 | `MR-0068` (NPdata), `MR-0071`, `MR-0076` |
| `FIELD_DECISION_OR_SANCTION` | 7 | `MR-0063` (CLED), `MR-0099`, `MR-0195` (lista de sanções financeiras) |
| `FIELD_LEGAL_BASIS` | 6 | `MR-0066`, `MR-0099` |
| **`FIELD_CELEX`** | **6** | `MR-0061`, `MR-0070`, `MR-0072`, `MR-0076`, `MR-0083` (EUR-Lex-Sum), `MR-0091` |
| `FIELD_ELI` | **0** | |
| `FIELD_ECLI` | **0** | |

**O que não se segue.** A ausência de ELI e ECLI entre as capacidades observadas não diz que os recursos não os contêm: foram lidos 4 KiB de 92 recursos, os conjuntos ELI em RDF não foram inspecionados no formato, e muitos formatos binários (Parquet, arquivos comprimidos) não expõem campos nos primeiros bytes. A presença de coluna com nome CELEX não diz que está preenchida nem que cobre o universo.

## 6. Mudanças nos estados e novos recursos do conjunto B

**Busca institucional estruturada (tarefa 4).**

| Passo | Resultado |
|---|---|
| Lista oficial de órgãos (SW-001, SW-002) | Páginas paginadas; só as primeiras entradas legíveis. Usadas como referência, não como lista completa |
| Catálogos do data.europa.eu | 212 catálogos enumerados (3 consultas) e sondagem de facetas; 124 com país `EUROPE` |
| Enumeração completa de catálogos de instituições e agências | **50 consultas** a 43 catálogos (41 de agências, direções-gerais e outros órgãos da UE, mais Publicações e Parlamento): 1.658 entradas lidas |
| Entradas individuadas como recurso | 133 candidatos novos do conjunto B ou AB (131 B, 2 AB), por regra de triagem escrita (DEC-0020) |
| Varredura de páginas institucionais | 48 páginas: 34 capturadas, 14 falharam; 17 recursos novos (origem `OTHER`) |
| Consultas temáticas livres em todos os catálogos | 23 consultas, nenhum recurso de nível UE adicional além dos conjuntos do JRC (DEC-0021) |

**Composição do conjunto B+AB (168 linhas, rodada 1 incluída):** Comissão Europeia 64, outros órgãos e agências da UE 54, supervisão financeira (ESMA, EBA, EIOPA, SRB) 24, acadêmicos e nacionais 21, Serviço das Publicações 3, Parlamento, Conselho e Tribunal 1, não apurado 1.

**Exemplos de registros novos:** registros ESMA (empresas de investimento, agências de notação, repositórios de transações, administradores de índices, internalizadores sistemáticos, aplicação do IFRS), registros do EIOPA (seguradoras, fundos de pensão), listas da ECHA (candidatas, autorização, restrições, C&L, avaliação de dossiês), ERADIS e ERATV (ferrovias), THETIS e SafeSeaNet (marítimo), registros da DG SANTE (alegações de saúde, aditivos para alimentos e rações, RASFF, novel food, pesticidas), Registro Fiscal e aduaneiro (AEO, SEED, REX), sanções financeiras, lista de segurança aérea, registro de reuniões da Comissão e opiniões do Regulatory Scrutiny Board.

**Estado dos novos do conjunto B/A:**

| Estado | Linhas |
|---|---|
| `VERIFIED` (registro do mantenedor preservado) | 124 |
| `PARTIALLY_VERIFIED` | 7 |
| `DISCOVERED` | 16 |

Dos 16 `DISCOVERED`, 11 são do conjunto B (título de página ou resultado do OpenAlex apenas).

**Conjunto B, nível I, individuado (143 linhas):** dados verificados 35, falha de acesso 10, página HTML 10, **não testado 88**. A maior parte do conjunto B continua sem teste de dados.

**Resultados negativos registrados.** Consultas sem nenhuma ligação a recursos: 14 de 54 na rodada 1 e 100 de 142 na rodada 2 (74 de 88 nas consultas que não são enumeração; 22 de 50 nas enumerações de catálogos, onde a maioria das entradas não é individuada por regra: relatórios, estatísticas, séries). Na varredura, 14 requisições falharam (404, 403, certificado). Nenhuma falha foi tratada como ausência do recurso.

## 7. Relações entre recursos com evidência

48 relações (32 da rodada 1, 16 da rodada 2): 20 `SUPPORTED`, 28 `CANDIDATE`.

| Tipo | Total | Novas |
|---|---|---|
| `part_of` | 10 | 8 (6 módulos do ERADIS com evidência de título; NANDO e ICSMS ao SMCS por redirecionamento) |
| `derived_from` | 12 | 4 (EUR-Lex-Resources e Super-EURLEX do EUR-Lex, `SUPPORTED`; cjeu-opendata do Cellar e EUR-Lex-Sum do EUR-Lex, `CANDIDATE`) |
| `overlaps_with` | 11 | 2 |
| `successor_of` | 1 | 1 (DEU IV, `LOW`) |
| `catalogues` | 2 | 1 (`LOW`) |

Cadeia de derivação em benchmarks: EUR-Lex → MultiEURLEX → {LexGLUE, pacote MTEB} permanece candidata de confiança média, apoiada em metadados de cartão e citação.

## 8. Licenças e condições de acesso

| Medida | Rodada 1 | Rodada 2 |
|---|---|---|
| Linhas com licença ou condição de reuso registrada | 37 de 105 | **158 de 252** |
| Formatos declarados | 29 | 155 |
| Cobertura temporal declarada | 17 | 28 |
| Condições de acesso registradas | 5 | 5 |

**Natureza do dado de licença.** São códigos e frases **copiados de registros de catálogo e de repositório** (`COM_REUSE` em 89 linhas, `CC BY 4.0` em cerca de 40, `CC0` em 12, e outros). **Nenhum texto de termos de uso foi lido na fonte**; nenhuma interpretação jurídica foi feita.

**Condições de acesso observadas** (pontos de acesso, 440): 132 acessíveis, 12 erro HTTP, 9 só casca de JavaScript, 7 erro de rede, 3 bloqueados ao cliente (403), 1 com autenticação (data dump), 276 sem teste. Condições registradas em campo próprio: registro para o serviço web do EUR-Lex; EU Login para o dump; arquivos restritos no Dataverse de `MR-0077`; sem autenticação para a API do TED (declaração da documentação); atraso de 10 dias do TRIS.

## 9. Resultados da comparação com o LYNX

`reports/PRIOR_ART_AND_LYNX_COMPARISON.md`; dados em `data/lynx_reference.csv`.

| Situação das 56 linhas da Tabela 6 do D2.8 | Linhas |
|---|---|
| Presente como recurso (EUR-Lex) | 1 |
| Presente como ponto de acesso de recurso | 2 |
| Relacionada (conjuntos ELI hospedados pelo Serviço das Publicações) | 5 |
| Ausente, escopo em aberto (portais nacionais) | 45 |
| Fora da regra geográfica (Reino Unido) | 3 |

O LYNX é referência externa, não padrão-ouro. Não há afirmação de originalidade.

## 10. Comparação entre as rodadas 1 e 2

Quadro **descritivo do esforço**. **Nenhuma diferença deve ser lida como crescimento ou diminuição real do campo.**

| Medida | Rodada 1 | Rodada 2 (acumulado) | O que mudou no método |
|---|---|---|---|
| Consultas registradas | 54 | 196 | Enumeração por catálogo e por publicador, além de texto livre |
| Ocorrências brutas | 1.251 | 5.333 | Mais consultas e profundidade em páginas de 100 |
| Capturas e falhas de captura | 57 | 193 | Registros de repositório e varredura institucional |
| Inspeções de dados | 0 | 106 | Primeira inspeção operacional |
| Linhas em `resources.csv` | 105 | 252 | Conjunto B por enumeração institucional |
| Linhas do conjunto B ou AB | 35 | 168 | Idem |
| Origem `SYSTEMATIC_SEARCH` | 58 | 187 | |
| Origem `OTHER` (varredura) | 0 | 17 | Nova via |
| Relações | 32 | 48 | |
| Seeds reencontrados por consulta | 12 | não recontado | Os seeds reencontrados pelas consultas da rodada 2 não foram curados |

O aumento de linhas decorre de **mudanças de método**: a rodada 2 enumerou catálogos de instituições da UE por inteiro, onde a rodada 1 fez buscas em texto livre. Não se pode inferir daí o tamanho do campo, a proporção entre os conjuntos A e B, nem a "disponibilidade" de dados regulatórios.

## 11. Limitações e decisões ainda necessárias

**Limitações desta rodada**

1. **Classificação por agente único.** Nenhuma confirmação humana. A amostra proposta (124 unidades) está em `protocol/HUMAN_VALIDATION_PROPOSAL_v0_1.md`.
2. **Inspeção mínima.** Primeiros 4 KiB de um arquivo por recurso. Mostra que bytes foram obtidos e o aspecto das primeiras linhas; não mostra conteúdo, completude, cobertura nem qualidade.
3. **Individuação segue a granularidade do catálogo do mantenedor.** As contagens por mantenedor não são comparáveis (DEC-0019).
4. **Triagem por título.** As 1.658 entradas das enumerações e as 1.251 + 4.082 ocorrências de busca foram triadas por título e descrição, por um leitor.
5. **Páginas dinâmicas.** Nove pontos de acesso devolvem só a casca; EUDAMED, EPREL, Safety Gate, Sanctions Map e Regulated Professions entraram só pelo título.
6. **Falhas de ambiente e de cliente.** ECHA, ERA, ELRC (certificado ou rede) e Conselho (403) não puderam ser lidos.
7. **Um único dia.** Link rot e disponibilidade são instantâneos.
8. **Requisições exploratórias não registradas.** Cerca de 20 chamadas de teste de API feitas antes dos registros formais (conectividade, formato de resposta) não foram preservadas; as enumerações usadas foram refeitas como consultas registradas.
9. **Fonte oficial da lista de órgãos** não utilizável; a lista de trabalho vem do catálogo data.europa.eu.
10. **Transcrição de tabela do LYNX por texto extraído de PDF.**

**Decisões do pesquisador, em aberto**

| # | Decisão |
|---|---|
| D1 | Regra para os 38 registros de elegibilidade `UNCERTAIN` (14 no conjunto A, 23 no B, 1 em AB) |
| D2 | Compilações temáticas de uma só política entram ou não |
| D3 | Adoção das categorias `STANDARD_OR_VOCABULARY` e `SOFTWARE_OR_PIPELINE` e da emenda A01 |
| D4 | Conta EU Login para o data dump |
| D5 | Portais e catálogos como recursos (nível II) ou relatados à parte |
| D6 | Desenho e execução da validação humana |
| **D7** | **Portais nacionais de publicação de legislação e jurisprudência (45 linhas do LYNX)** |
| D8 | Redistribuição das capturas de páginas de terceiros ou publicação só de hashes. A pasta `evidence/` tem 233 MB de cópias (respostas de API de até 6 MB cada); não foi publicada, e convém decidir antes de qualquer commit |
| D9 | Se a rodada 3 deve abrir os 160 recursos `NOT_TESTED` por captura de páginas e novas inspeções |

## 12. Onde está cada coisa

| Item | Caminho |
|---|---|
| Recursos (252) | `mapping/data/resources.csv` |
| Pontos de acesso (440) | `mapping/data/access_endpoints.csv` |
| Relações (48) | `mapping/data/resource_relations.csv` |
| Descobertas e buscas | `mapping/data/discovery_log.csv` |
| Evidências (496) | `mapping/data/evidence_registry.csv` |
| Histórico de estados (59) | `mapping/data/verification_history.csv` |
| Inspeções (106) | `mapping/data/data_inspections.csv` |
| Capacidades (116) | `mapping/data/capabilities.csv` |
| Varredura institucional (48) | `mapping/data/institutional_sweep.csv` |
| Referência LYNX (56) | `mapping/data/lynx_reference.csv` |
| Decisões (28) | `mapping/data/decisions_log.csv` |
| Instantâneo da rodada 1 | `mapping/snapshots/round1/` |
| Consultas da rodada 2 | `mapping/protocol/SEARCH_QUERIES_G2_ROUND2.csv` |
| Registro da varredura | `mapping/protocol/INSTITUTIONAL_SWEEP_G2_ROUND2.csv` |
| Julgamentos da rodada | `mapping/curation/round2.py` |
