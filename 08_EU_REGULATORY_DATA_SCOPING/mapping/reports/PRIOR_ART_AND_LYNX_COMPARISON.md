# ANTECEDENTES CIENTÍFICOS E COMPARAÇÃO COM O LYNX

**Data:** 2026-10-10 | **Estado:** comparação feita pelo agente de programação a partir de dois relatórios de projeto lidos. Não é parecer de originalidade e não substitui a leitura dos demais antecedentes.

## 1. O que foi lido, e o que não foi

| Documento | Obtido | Lido |
|---|---|---|
| **D2.7** — *Catalogue of relevant legal and regulatory datasets* (Lynx, H2020-780602; 29/02/2020; DOI 10.5281/zenodo.3692561; CC BY 4.0) | Zenodo, PDF de 343.180 bytes, SHA-256 `e49107df…`, 13 páginas | **Integralmente** (texto extraído do PDF; 8 páginas de texto e 5 de tabela) |
| **D2.8** — *Final Report of Data Management Activities* (Lynx; 31/03/2021; DOI 10.5281/zenodo.4651389; CC BY 4.0) | Zenodo, PDF de 2.240.380 bytes, SHA-256 `491be853…`, 55 páginas | **Parcialmente**: resumo, índice, plano de gestão de dados (resumo de dados), introdução do modelo de dados, vocabulários de domínio (§4.2), conjuntos colhidos (§4.4.2, Tabela 5), início do Anexo A e o Anexo B inteiro (Tabela 6). **Não lido**: seções FAIR, alocação de recursos, segurança, aspectos legais e éticos, detalhes da ontologia, Anexo A integral |

Os arquivos estão em `mapping/evidence/captures/LYNX-D2.7-PDF/` e `LYNX-D2.8-PDF/`, com os registros Zenodo correspondentes. A extração de texto de tabelas de PDF pode misturar células; as linhas de `lynx_reference.csv` foram transcritas da Tabela 6 do D2.8 e conferidas contra o texto, não contra a imagem das páginas.

Além disso, o portal de dados mencionado pelos dois relatórios (`data.lynx-project.eu/dataset`) teve a conexão reiniciada pelo servidor na tentativa de acesso, e o site `lynx-project.eu` respondeu (HTTP 200). Isso é uma falha de acesso nesta data; não diz que o portal deixou de existir.

## 2. O que os documentos descrevem

- **D2.7** é um catálogo em tabela de **portais de publicação de legislação e jurisprudência** de 27 Estados-membros, do Reino Unido e da União Europeia. As colunas são área, endereço, conteúdo (lei, jurisprudência, indicação de ELI e ECLI), tipo de licença (livre ou restrito), formato (PDF, XML, HTML, outro), interface de acesso (API, download em lote, endpoint SPARQL) e idioma.
- **D2.8** é o relatório final da gestão de dados do projeto: plano de gestão de dados, modelo de dados do *Lynx Document*, vocabulários, conjuntos colhidos por piloto (Tabela 5) e a mesma tabela de portais, atualizada em março de 2021 (Tabela 6, Anexo B).
- O objetivo do catálogo era **abastecer um grafo de conhecimento jurídico** (*Legal Knowledge Graph*) para serviços de conformidade; o texto diz que priorizou as jurisdições dos casos de uso do projeto para ingestão.

## 3. Comparação com este mapeamento

| Dimensão | LYNX D2.7 / D2.8 | Este mapeamento (rodada 2) |
|---|---|---|
| **Escopo** | Legislação e jurisprudência, nível da UE e dos Estados-membros (mais Reino Unido) | Dados legislativos e jurídicos da UE (A) e dados de governança regulatória da UE (B); prioridade ao nível da UE, nacionais só com conexão documentada |
| **Período** | Observação de fevereiro de 2020 (D2.7) e março de 2021 (D2.8) | Observação de 10 de outubro de 2026; instantâneo |
| **Unidade de análise** | O **portal ou sítio** de publicação. Uma linha por portal; o mesmo país tem linhas separadas para lei e jurisprudência | O **recurso** (acervo ou serviço), com pontos de acesso, relações e níveis separados |
| **Definição de dataset** | Não há. "Datasets legais" são os portais; o catálogo não distingue acervo, interface e catálogo | Definição operacional por categoria (emenda A01), com níveis I e II |
| **Critérios de seleção** | Declara os critérios *de interesse* (tipo de documento, nível de implementação do ELI, formatos, idioma, acesso). Não declara critérios de inclusão e exclusão | Critérios de inclusão e exclusão escritos antes e aplicados a cada candidato, com decisão registrada |
| **Método de busca** | "Busca exaustiva de recursos na web" a partir de quatro fontes de partida (relatório de 2009 sobre acesso à legislação, fórum dos jornais oficiais, informação sobre jornais oficiais, portal e-Justice). Não há consultas, datas nem registros de busca | Consultas registradas (texto, serviço, data, profundidade, resposta preservada com hash); varredura institucional com registro dos caminhos e das falhas |
| **Recursos derivados** | Fora da tabela. Corpora e vocabulários aparecem em outros entregáveis (D2.5, D2.6, Anexo A) | Tratados: `derived_from`, benchmarks e corpora acadêmicos, com a ressalva de que a derivação declarada não é linhagem verificada |
| **Evidência de acesso** | Células da tabela (livre ou restrito, formato, interface). Não há captura, data por linha nem teste de acesso descritos | Captura com hash, estado de cada ponto de acesso e inspeção dos primeiros bytes; distinção entre declarado e observado |
| **Governança regulatória** | O título diz "legal and regulatory", mas as colunas cobrem lei e jurisprudência; não há registros de reguladores, supervisão, sanções, autorizações | Conjunto B é objeto explícito; 133 candidatos novos nesta rodada |
| **Reprodutibilidade** | Tabela publicada com licença CC BY 4.0 e dados no portal CKAN do projeto. Os relatórios não trazem consultas nem scripts | Consultas, respostas, scripts, construtor determinístico e testes; as capturas de páginas de terceiros ainda não têm decisão de redistribuição |

## 4. Quais recursos do LYNX já estão no inventário

A Tabela 6 do D2.8 tem **56 linhas**: 3 da União Europeia, 50 de 26 Estados-membros e 3 do Reino Unido. A lista está em `mapping/data/lynx_reference.csv`, com a decisão por linha.

| Situação da linha | Linhas | Quais |
|---|---|---|
| Presente como recurso | 1 | EUR-Lex (`MR-0001`) |
| Presente como ponto de acesso de um recurso | 2 | Entrada de catálogo das listas do Jornal Oficial em inglês (`MR-0004`); entrada de catálogo "EU case-law" (`MR-0001`, regra DEC-0004: seus links são vistas do EUR-Lex) |
| Relacionada: o inventário tem o conjunto de metadados ELI publicado pelo Serviço das Publicações, não o portal | 5 | Irish Statute Book, Retsinformation (Dinamarca), Gazzetta Ufficiale (Itália), Legilux (Luxemburgo), Finlex (Finlândia) |
| Ausente, escopo em aberto | 45 | Portais nacionais de legislação e jurisprudência sem ligação documentada, nas fontes lidas, com a aplicação do direito da UE |
| Fora da regra geográfica | 3 | Reino Unido |

**Como ler.**

1. A lista do LYNX é uma **referência externa de recuperação**, não um universo nem um padrão-ouro. Ela mede portais de publicação jurídica; o inventário mede recursos de dados.
2. No nível da UE, as três linhas encontram correspondência. Isso mostra que o núcleo institucional da UE está coberto, não que a cobertura seja ampla.
3. No nível nacional, **nenhum portal está individuado no inventário**. A ausência é de escopo: a regra geográfica da reorientação inclui recursos nacionais apenas com conexão documentada com legislação, implementação ou governança da UE. Os portais do LYNX declaram ELI e ECLI, que são iniciativas da União, mas isso é uma conexão por padrão de identificação e não por transposição ou aplicação. Se a regra for ampliada (decisão D7), 45 linhas viram candidatos imediatos.
4. O N-Lex (`MR-0019`) é um portal federado que dá acesso às bases nacionais e está no inventário. O LYNX não o lista.
5. A taxa "3 de 56" não é uma taxa de recuperação das buscas. Os recursos do LYNX não foram procurados pelas consultas; a comparação é feita contra o conjunto final.
6. A lista é **volátil**: entre o D2.7 e o D2.8 há substituições de portais. Por exemplo, para a Alemanha o D2.7 lista Bundesanzeiger e juris e o D2.8 lista o Bundesgesetzblatt (bgbl.de) e o Tribunal Constitucional; para a Irlanda, o D2.7 traz o Iris Oifigiúil e o D2.8 o Irish Statute Book. O estado de 2026 dos 56 endereços não foi testado.

## 5. O que o LYNX tem que o inventário não tem, e o inverso

**O LYNX tem e nós não:**

- cobertura sistemática dos portais nacionais de publicação oficial, com os indicadores de ELI e ECLI por portal;
- o modelo de dados de documento (*Lynx Document*) e os conjuntos colhidos com contagens por jurisdição (Tabela 5), úteis para estimar tamanho;
- vocabulários de domínio e corpora de terminologia (Anexo A, não lido integralmente).

**O inventário tem e o LYNX não tem:**

- registros administrativos de reguladores e agências (conjunto B);
- corpora, benchmarks e conjuntos de pesquisa derivados (conjunto A acadêmico), com a distinção entre oficial e derivado;
- registro de relações com evidência e confiança;
- estado de acesso observado, com data e hash, e inspeção mínima de dados;
- registro das buscas e dos resultados negativos.

**O que nenhum dos dois tem:** avaliação do conteúdo dos acervos (cobertura efetiva, completude, qualidade) nem teste de capacidade longitudinal.

## 6. Outros antecedentes ainda não lidos

Foram identificados por três buscas na web da rodada 1. **Não foram abertos nem lidos** e não entram na comparação acima.

| Trabalho | Por que importa | Estado |
|---|---|---|
| Capítulo "Varieties of Data in EU Legal Scholarship" (Cambridge University Press) | Levantamento dos dados que a pesquisa jurídica sobre a UE usa, a partir de 248 artigos | Não lido |
| König, Luetgert e Dannwolf (2006), *European Union Politics* | Compara CELEX e PreLex como fontes do processo legislativo | Não lido |
| Revisões de PLN jurídico (arXiv 2410.21306; 2503.04305; 2501.17830) | Inventariam corpora e benchmarks derivados do EUR-Lex; sobrepõem-se à parte acadêmica do conjunto A | Não lidas |
| Artigos de dados da ciência política da UE (DEU, EUPROPS, EfSoLaw, ECJ Dataset) | Descrevem o estado dos dados em subcampos; os datasets estão registrados no inventário | Registro lido pelos metadados; artigos não lidos |
| `Interview-based datasets for quantitative research on the Council of the EU: a survey` (2025; OpenAlex) | Parece levantamento de datasets sobre o Conselho; apareceu numa busca desta rodada | Só o título; não registrado como recurso porque é levantamento |

## 7. O que se pode e o que não se pode afirmar

**Pode-se afirmar:**

1. O LYNX D2.7/D2.8 é um antecedente direto na ideia de catalogar recursos jurídicos europeus com atenção a identificadores, formatos e acesso.
2. Difere deste mapeamento no escopo (lei e jurisprudência *versus* dados legislativos e de governança regulatória), na unidade (portal *versus* recurso), na ausência de registro de busca e de evidência de acesso, e na ausência de recursos derivados e de reguladores.
3. A sobreposição direta no nível da UE é pequena (3 linhas), porque o LYNX é majoritariamente nacional.

**Não se pode afirmar:**

1. Que este mapeamento seja inédito. Há antecedentes não lidos (seção 6) e as buscas por trabalhos semelhantes foram poucas.
2. Que o conjunto B não tenha sido inventariado por outro trabalho.
3. Que a diferença de método implique melhor cobertura: o inventário desta rodada não é exaustivo, e o LYNX cobre 26 Estados-membros que o inventário não cobre.

## 8. Consequências para a continuação

1. **Decisão D7 (nova):** os portais nacionais de publicação de legislação e jurisprudência entram, ou não, como família? Se entrarem, a Tabela 6 do D2.8 é o ponto de partida, e o teste de acesso (primeiros bytes) é barato.
2. **Verificar a Tabela 6 hoje**: uma requisição por portal para marcar os que mudaram de endereço.
3. Ler o capítulo de Cambridge e o levantamento de datasets sobre o Conselho antes de qualquer alegação de contribuição.
4. Registrar a diferença de escopo na descrição de qualquer produto público: o inventário **não** substitui nem atualiza o catálogo do LYNX.
