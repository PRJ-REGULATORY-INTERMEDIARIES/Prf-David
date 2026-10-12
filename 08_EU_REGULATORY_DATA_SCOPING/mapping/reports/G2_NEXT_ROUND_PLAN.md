# G2 — PLANO DA RODADA 2

**Data:** 2026-10-10 | Continuação direta do mapeamento. Não é um novo gate: nenhum item abaixo precisa de autorização de terceiros, e só os marcados com (D) pedem decisão do pesquisador.

## Objetivo

Fechar o que a rodada 1 deixou aberto e corrigir o seu principal viés: a subcobertura do conjunto B.

## Bloco 1 — Fechar pendências da rodada 1

| # | Tarefa | Itens | Feito quando |
|---|---|---|---|
| 1.1 | Capturar o registro ou a página de cada recurso `DISCOVERED` | 30 | Cada um tem captura com hash e sai de `DISCOVERED`, ou tem decisão registrada |
| 1.2 | Capturar o registro de repositório dos novos `PARTIALLY_VERIFIED` e ler licença, período e arquivos | 33 | Campos `licence_or_reuse`, `temporal_coverage`, `formats` preenchidos ou mantidos `NOT_ASSESSED` com motivo |
| 1.3 | Localizar o depósito dos 9 datasets conhecidos só pelo artigo | `MR-0078` a `MR-0082`, `MR-0084` a `MR-0087` | Ponto de acesso registrado, ou "não localizado" na coluna de incertezas |
| 1.4 | Desdobrar os dois agrupamentos | `MR-0044`, `MR-0054` | Cada entrada é recurso, ponto de acesso ou descartada, com decisão |
| 1.5 | Registrar as fontes a montante mencionadas | EuroVoc, GDPRhub, OpenEFSA, MAPA, Europarl original, CEPS EurLex | Linha em `resources.csv` com origem `BACKWARD_FORWARD_DISCOVERY` |
| 1.6 | Repetir de outro ambiente os acessos que falharam por causa desta máquina ou do cliente | EU10, EU32, buscador ECLI | Captura, ou segunda falha registrada |
| 1.7 | Capturar manualmente, no navegador, as oito páginas dinâmicas e registrá-las com o comando `register` | 8 pontos `JS_ONLY_SHELL` | Arquivo PDF com hash no registro de evidências |
| 1.8 | Conferir nos seeds os campos ainda `SEED_UNVERIFIED` | 39 valores de identificadores; unidades de observação | Marcados com base primária ou mantidos como estão |

## Bloco 2 — Conjunto B, por órgão

A busca em catálogos alcança mal os registros de reguladores. Muda-se a via.

1. Obter a lista oficial de agências e órgãos descentralizados da UE (uma captura da página institucional).
2. Para cada um, uma captura da página de registros, bases ou dados abertos.
3. Registrar cada registro público encontrado: autorizações, entidades supervisionadas, sanções, decisões, organismos designados.
4. Fazer o mesmo para as redes de autoridades nacionais com registro europeu (proteção de dados, concorrência, serviços digitais, acreditação, vigilância do mercado).

Teto: uma a três requisições por órgão. Origem dos registros: `OTHER`, com a nota "varredura institucional por lista de órgãos", porque não é consulta a serviço de busca.

## Bloco 3 — Consultas registradas novas

Arquivo `SEARCH_QUERIES_G2_ROUND2.csv`, identificadores `SR-G2-055` em diante.

| Família | Serviço | Consultas previstas |
|---|---|---|
| Catálogo por publicador | data.europa.eu (SPARQL ou filtro de catálogo) | Uma por publicador institucional da UE identificado na rodada 1 |
| Governança regulatória, acadêmico | Zenodo, Dataverse, OpenAlex | *notified bodies*; *accreditation*; *regulatory intermediaries*; *national regulatory authorities*; *independent regulatory agencies Europe dataset*; *enforcement decisions dataset*; *sanctions dataset European*; *market surveillance* |
| Processo legislativo | Zenodo, Dataverse, OpenAlex | *trilogues dataset*; *Council voting dataset*; *impact assessments dataset*; *public consultations European Commission dataset* |
| Transposição e conformidade | OpenAlex, Dataverse | *infringement database*; *transposition dataset*; *compliance EU law dataset* |
| Jurisprudência | Zenodo, OpenAlex | *preliminary references dataset*; *CJEU citation network* |
| Outros repositórios | DANS, GESIS, UK Data Service, CLARIN, ELRC | Conjunto mínimo das consultas da rodada 1, depois de conferir se há API pública |
| Idiomas | data.europa.eu | Francês e alemão para as famílias de B |
| Profundidade | Serviços que informaram mais de 100 mil resultados | Segunda página das consultas mais produtivas da rodada 1 |

## Bloco 4 — Antecedentes

1. Capturar e ler o catálogo do projeto LYNX (D2.7) e o capítulo sobre dados na pesquisa jurídica da UE.
2. Extrair as listas de datasets de duas revisões de PLN jurídico e do artigo de König, Luetgert e Dannwolf.
3. Usar a lista do LYNX como teste de recuperação externo: quantos dos seus itens pertinentes estão na base.

## Bloco 5 — Decisões do pesquisador (D)

| # | Decisão | Efeito |
|---|---|---|
| D1 | Regra para os 14 registros `UNCERTAIN` | Fixa o escopo nas bordas |
| D2 | Compilações temáticas de uma só política entram ou não | Afeta cinco ocorrências já vistas e muitas futuras |
| D3 | Adotar ou não as duas categorias acrescentadas | Estabiliza o vocabulário |
| D4 | Criar conta EU Login para examinar o data dump | Único modo de resolver a divergência sobre o seu conteúdo |
| D5 | Portais e catálogos contam como recursos ou são relatados à parte | Muda as contagens |
| D6 | Desenho da validação amostral: tamanho, estratos, quem classifica | Condição para publicar contagens |

Nenhuma delas bloqueia os blocos 1 a 4.

## Disciplina

A mesma do protocolo: uma requisição por página ou consulta; cliente identificado; sem autenticação e sem contorno de bloqueios; sem download de datasets; toda tentativa registrada.

## Medida de progresso

Não há meta de quantidade. Ao fim da rodada 2, relatar:

- quantos `DISCOVERED` e `PARTIALLY_VERIFIED` mudaram de estado;
- quantos recursos de B foram individuados pela varredura institucional;
- quantos registros têm licença lida na fonte;
- o resultado do teste de recuperação externo;
- quantas linhas foram confirmadas por pesquisador.
