# EMENDA A01 — DADOS E INFRAESTRUTURA (NÍVEIS I E II) E NÍVEIS DE EVIDÊNCIA

**Data:** 2026-10-10 | **Gate:** G2, rodada 2 | **Estado:** PROPOSTA do agente; vale como convenção de trabalho até revisão do pesquisador responsável.
**Altera:** `INDEPENDENT_MAPPING_REORIENTATION_v1_0.md` (seções 5 e 6) e `SYSTEMATIC_MAPPING_PROTOCOL_v1_0_DRAFT.md` (seção 6). Não reescreve esses documentos nem os resultados da rodada 1.

## 1. Por que

A rodada 1 contou "recursos" misturando coisas de natureza diferente: acervos de dados (um dataset de infrações), portais que dão acesso a vários acervos (EUR-Lex), padrões (ELI, ECLI) e software. O relatório já alertava que "os 41 seeds não são 41 datasets independentes". A pergunta de pesquisa fala de *datasets e infraestruturas de dados*; os dois precisam ser contados em separado para que uma lacuna em um não seja lida como lacuna no outro.

## 2. Os dois níveis

| Nível | O que é | Categorias da rodada 1 que o compõem |
|---|---|---|
| **I — dados** | Acervos de dados: datasets, corpora, benchmarks, registros administrativos e repositórios de documentos jurídicos. O que se consulta ou analisa | `DATASET`, `CORPUS`, `BENCHMARK`, `ADMINISTRATIVE_REGISTER`, `REPOSITORY` |
| **II — infraestrutura de suporte** | O que descobre, identifica, descreve ou dá acesso a dados, sem ser o acervo | `CATALOGUE`, `ACCESS_PORTAL`, `SEARCH_INTERFACE`, `API`, `INFRASTRUCTURE`, `STANDARD_OR_VOCABULARY`, `SOFTWARE_OR_PIPELINE`, `DESCRIPTIVE_PAGE` |
| (distribuição) | Caminho ou pacote de acesso a todo ou parte de um recurso de nível I | `DATA_DISTRIBUTION` |
| (não atribuído) | A evidência não permite decidir | `INDETERMINATE` |

Os níveis são **derivados** da categoria, que continua sendo a classificação do agente (provisória). A coluna `resource_level` de `resources.csv` é calculada pelo construtor; não é digitada.

**Regra de contagem.** Cada nível é contado entre os recursos com `individuation_status = INDIVIDUATED`. Candidatos (`CANDIDATE_SEPARATE`, `CANDIDATE_NOT_INDEPENDENT`), agrupamentos (`GROUP_PENDING_SPLIT`) e distribuições são relatados à parte e nunca somados ao nível I nem ao II.

**Relação com a unidade de análise.** A unidade continua sendo o recurso (L1 da taxonomia v0.2). O ponto de acesso (L2) continua em `access_endpoints.csv`. Nada muda nas relações já registradas; o nível de cada ponta de uma relação passa a ser legível, de modo que `derived_from` entre dois recursos de nível I, ou `uses` de um recurso de nível I sobre um de nível II, possam ser contados separadamente.

## 3. Inconsistências identificadas entre as regras de inclusão e as categorias

| # | Inconsistência | Onde | Tratamento proposto |
|---|---|---|---|
| 1 | O critério de inclusão 6.2 diz "não se registra software sem dados próprios", mas existe a categoria `SOFTWARE_OR_PIPELINE`, usada em registros da rodada 1 (`MR-0081`, `MR-0097`) | Reorientação §6; vocabulário | Software fica no nível II e só é registrado como ponteiro, nunca `INDIVIDUATED`. O validador emite aviso se for individuado. O critério 6.2 passa a ler: "não se individua software sem dados próprios; registra-se como infraestrutura de apoio quando é a via documentada de acesso a um recurso" |
| 2 | `DATA_DISTRIBUTION` é definida como "pacote ou caminho de acesso a outro recurso, não conta como recurso", mas `MR-0003` (EUR-Lex data dump) e `MR-0043` (ELI do EUR-Lex) são linhas de `resources.csv` com `individuation_status = CANDIDATE_SEPARATE`, que sugere "possivelmente recurso próprio" | Vocabulário; individuação | A categoria é mantida; o nível é "distribuição". Ela nunca pode ser `INDIVIDUATED` (o validador impede). `CANDIDATE_SEPARATE` passa a significar apenas que a hipótese de recurso próprio está em aberto. O caso `MR-0003` fica explicitamente em aberto porque a descrição oficial e o conteúdo divergem e o acesso exige conta |
| 3 | O critério 6.3 diz "não se registra cópia, reenvio ou reformatação", mas há linhas de reformatação (por exemplo `MR-0094`, `MR-0090`, `MR-0039`) registradas como `CANDIDATE_NOT_INDEPENDENT` | Reorientação §6 | Mantidas como candidatas fora da contagem. A regra passa a ser "não se *individua*"; o registro serve de evidência de dependência (`derived_from`) |
| 4 | As categorias `ACCESS_PORTAL` e `CATALOGUE` estão no vocabulário como recursos, e ficaram dentro das 88 linhas "individuadas" da rodada 1, somadas a datasets | Contagens do relatório inicial | Passam ao nível II. A contagem de nível I da rodada 1 pode ser reproduzida filtrando a categoria; os números do relatório 1 não são reescritos |
| 5 | `API` é categoria de recurso, mas a regra R2 da taxonomia trata API como distribuição de um recurso já registrado | Taxonomia v0.2 §4 | `API` fica no nível II. Só é recurso quando não foi possível ligá-la a um recurso de nível I (caso de `MR-0008`) |
| 6 | `SEARCH_INTERFACE` e `DESCRIPTIVE_PAGE` estão no vocabulário e nenhuma linha as usa | Vocabulário | Mantidas por completude; interfaces e páginas descritivas vão para `access_endpoints.csv` |
| 7 | Há entradas de catálogo cujo título declara "módulo de X" (ERADIS), tratadas aqui como `CANDIDATE_NOT_INDEPENDENT`, e outras da mesma natureza sem o nome do sistema no título (listas do ACER), tratadas como individuadas | Individuação na rodada 2 | Regra escrita em `DEC-0019`: título que declara módulo de sistema nomeado conta com o pai; o resto segue a granularidade do catálogo do mantenedor, que varia entre mantenedores. As contagens por mantenedor não são comparáveis |
| 8 | A rodada 1 chamou de `VERIFIED` linhas cujo mantenedor foi inferido ou não apurado (`MR-0005`, `MR-0018`, `MR-0023`, `MR-0034`) | Rodada 1 | O estado histórico fica como está (não se reclassifica retroativamente). O nível de identidade derivado as marca como `IDENTITY_PARTIAL`; o validador emite aviso |

Nenhuma linha foi apagada ou recategorizada por esta emenda.

## 4. Três níveis de evidência

Os estados históricos de verificação respondem "quanta evidência de identidade existe". Eles não distinguem o que se **declara** do que se **observou**. A rodada 2 acrescenta três colunas calculadas, sem substituir `verification_status`.

| Coluna | Valores | Quando |
|---|---|---|
| `identity_level` | `IDENTITY_VERIFIED`, `IDENTITY_PARTIAL`, `NOT_VERIFIED` | `IDENTITY_VERIFIED`: nome, mantenedor e URL de descrição preenchidos; nome e mantenedor com base em página primária ou registro de repositório ou catálogo preservado (não em seed nem em inferência); ao menos uma evidência bem-sucedida. `IDENTITY_PARTIAL`: há evidência bem-sucedida, mas falta alguma condição. `NOT_VERIFIED`: nenhuma evidência bem-sucedida |
| `data_availability_level` | `DATA_AVAILABILITY_VERIFIED`, `DOCUMENT_ONLY`, `LANDING_PAGE_ONLY`, `LISTING_ONLY`, `ACCESS_FAILED`, `NOT_TESTED` | Resultado de uma **inspeção de primeiros bytes** (no máximo 4 KiB, por faixa HTTP) de um endereço de dados do recurso. `DATA_AVAILABILITY_VERIFIED`: os bytes lidos são dados (tabular, JSON, XML, arquivo comprimido ou Parquet). `LANDING_PAGE_ONLY`: o endereço devolveu uma página HTML. `DOCUMENT_ONLY`: PDF. `LISTING_ONLY`: listagem de repositório. A existência de dados **declarada** por uma lista de arquivos num registro não basta |
| `capability_level` | `CAPABILITY_VERIFIED`, `NOT_ASSESSED` | Há ao menos uma capacidade na tabela `capabilities.csv`, observada nos bytes lidos: nomes de campos ou chaves (`SCHEMA_FIELDS_OBSERVED`) e correspondências de nome de campo com padrões jurídicos (`FIELD_CELEX`, `FIELD_ELI`, `FIELD_ECLI`, `FIELD_LEGAL_BASIS`, `FIELD_DECISION_OR_SANCTION`, `FIELD_COUNTRY_OR_MEMBER_STATE`, `FIELD_DATE`, `FIELD_ENTITY_NAME`, `FIELD_ENTITY_ID`) |

**O que "capacidade verificada" não diz.** Que existe uma coluna ou chave com aquele nome nos primeiros bytes. Não diz que a coluna está preenchida, que cobre o universo, nem que o identificador é o jurídico. Uma capacidade ausente na amostra não é ausência no recurso, e a amostra são os primeiros 4 KiB.

**Declarado versus observado.** O campo `field_basis` ganhou o valor `OPERATIONAL_INSPECTION` para campos preenchidos a partir de uma leitura de primeiros bytes. `API_METADATA` e `PRIMARY_PAGE` continuam sendo declaração da fonte.

## 5. Correspondência com os estados históricos

| Estado histórico (rodada 1) | Significado | Relação com o nível de identidade | Relação com os outros dois |
|---|---|---|---|
| `VERIFIED` | Nome e localização constam de página primária ou registro de catálogo preservado | Em geral `IDENTITY_VERIFIED`. Exceção: quando o mantenedor foi inferido ou não apurado (`IDENTITY_PARTIAL`) | Nenhuma. `VERIFIED` nunca implicou disponibilidade de dados |
| `PARTIALLY_VERIFIED` | Parte da identidade consta de fonte preservada | `IDENTITY_PARTIAL` ou `IDENTITY_VERIFIED`, conforme as condições da seção 4 | Idem |
| `DISCOVERED` | Conhecido por resultado de busca ou menção | `IDENTITY_PARTIAL` se um registro de busca foi preservado; `NOT_VERIFIED` se nem isso | Idem |
| `INACCESSIBLE` | Todas as tentativas falharam | `NOT_VERIFIED` (nenhuma leitura bem-sucedida) | `ACCESS_FAILED` quando houve inspeção; falha nunca vira exclusão |
| `INDETERMINATE` | A evidência não permite propor categoria | Qualquer | Qualquer |

Os dois sistemas convivem. Uma mudança de `verification_status` é registrada em `verification_history.csv`, com a rodada, o estado anterior, o novo e o motivo; os níveis são recalculados a cada construção.

## 6. O que a emenda não decide

Se o nível II deve ser objeto de análise própria ou apenas de apoio; a regra para os registros `UNCERTAIN`; a adoção definitiva das categorias `STANDARD_OR_VOCABULARY` e `SOFTWARE_OR_PIPELINE`. São decisões do pesquisador responsável.
