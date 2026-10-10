# G1-READY — REVISÃO DE IDENTIDADE DAS FONTES E DAS URLs

**Data:** 2026-10-10 | **Estado:** correções **candidatas**; nenhuma foi aplicada. O inventário de 41 seeds não foi modificado (SHA-256 `45316803ea07f677…`, igual ao do G0).
**Uso restrito ao coordenador.** Este documento afirma coisas sobre registros que os avaliadores vão classificar.

Tabela completa, com colunas de decisão em branco: `gates/G1_READY_SEED_URL_REVIEW.csv`.

## 1. Cinco coisas que o inventário guarda num único campo

O campo `source_url` do inventário é usado ora para uma coisa, ora para outra. A revisão separa:

| Conceito | O que é | Exemplo verificado |
|---|---|---|
| **Identidade do recurso** | O acervo ou serviço em si, com mantenedor, escopo e unidade de observação | "EUR-Lex data dump": todos os atos em vigor, por idioma, setor CELEX 3 |
| **URL de acesso** | O endereço onde o conteúdo é obtido | `https://datadump.publications.europa.eu/` |
| **Página de descrição** | Página que explica o recurso e aponta para ele | Seção 4 de `https://data.europa.eu/en/ELDS` |
| **Distribuição** | Um caminho de acesso entre vários ao mesmo recurso | Não verificado para este caso |
| **Relação institucional** | Quem mantém o quê | A página ELDS declara ser gerida pelo Serviço das Publicações |

Uma URL identifica uma página, não um recurso. Dois recursos podem ser descritos na mesma página, e um recurso pode ter página de descrição num host e acesso em outro.

## 2. EU03 e EU07: o que foi verificado

**Evidência.** Duas requisições, as únicas feitas nesta fase, limitadas às URLs indicadas na tarefa.

| Requisição | Resultado | Registro |
|---|---|---|
| `GET https://data.europa.eu/en/ELDS` | HTTP 200, `text/html`, 69.561 bytes, `Last-Modified: Thu, 08 Oct 2026 16:48:29 GMT`, capturada em 2026-10-10T03:18:41Z | Arquivo preservado; SHA-256 `f5807d8e8ce108c6e8101319377d3fb31a54f1bdd264278c61428c675492efea` |
| `GET https://datadump.publications.europa.eu/` | **HTTP 401** nas duas tentativas (03:18:46Z e 03:18:51Z) | Falha registrada; nenhum arquivo |

Log e arquivo: `pilot_a/evidence_procedure_test/`.

**O que a página capturada diz** (leitura do arquivo preservado):

- Título: "European Legal Data Space | data.europa.eu".
- Apresenta o European Legal Data Space como um dos espaços comuns europeus de dados, e tem quatro seções: (1) Common standards; (2) Access to collections of legislation and case-law; (3) Data on justice systems and improving access to justice; (4) EUR-Lex data dump.
- Seção 4, literalmente: "It allows downloading in bulk all legal acts in force per language (CELEX sector 3). To access the data dump an EU login account is required. Link to EUR-Lex data dump: https://datadump.publications.europa.eu/".
- A seção 2 aponta para duas entradas de catálogo (`data.europa.eu/data/datasets/elds` e `…/elds-caselaw`) e para a página de reutilização de conteúdo do EUR-Lex, que é a URL registrada no inventário para EU04.
- Rodapé: "This website is managed by: Publications Office of the European Union".

**Conclusões**

| # | Conclusão | Classe |
|---|---|---|
| 2.1 | EU03 e EU07 são **dois recursos distintos** descritos na mesma página. A URL comum não indica duplicata. | VERIFIED (página capturada) |
| 2.2 | Para EU07, a URL do inventário é a página do próprio recurso. | VERIFIED |
| 2.3 | Para EU03, a URL do inventário é uma **página de descrição**. O endereço de acesso declarado pela fonte é `https://datadump.publications.europa.eu/`. | VERIFIED |
| 2.4 | O endereço de acesso de EU03 exige autenticação: a página o declara e o servidor respondeu 401. | VERIFIED |
| 2.5 | O conteúdo do dump (formatos, cobertura efetiva, data de atualização, termos) | PENDING VALIDATION — exige conta; não foi acessado |
| 2.6 | O tipo de desafio de autenticação do 401 não ficou registrado: a ferramenta, naquele momento, não guardava os cabeçalhos da resposta de erro. Foi corrigida e testada depois; a requisição não foi repetida. | VERIFIED (lacuna) |
| 2.7 | Se o dump é uma distribuição parcial de outro recurso do inventário ou um recurso próprio | **Não decidido aqui.** É exatamente o que o Piloto A pede aos avaliadores |

**Correção candidata para EU03:** acrescentar `https://datadump.publications.europa.eu/` como URL de acesso, mantendo `https://data.europa.eu/en/ELDS` como página de descrição. Registrada na tabela; não aplicada.

**Consequência para o verificador.** O aviso "Same URL in records SEED_EU03, SEED_EU07", emitido por `cli.py check`, é correto e deve ser mantido: a URL coincide. O que este caso mostra é que URL igual gera um **candidato** a duplicata, nunca uma decisão — como já dizia a taxonomia (seção 5).

**Consequência para o Piloto A.** Duas opções, a decidir pela equipe:

| Opção | O avaliador recebe para EU03 | Efeito |
|---|---|---|
| Manter a URL do inventário | `https://data.europa.eu/en/ELDS` | O piloto testa se a regra R0 resiste a URLs iguais para recursos distintos. É o teste mais informativo da regra de duplicata |
| Entregar a URL de acesso | `https://datadump.publications.europa.eu/` | O avaliador cai numa página que exige login e pode ficar sem evidência; o teste de R0 desaparece |

Os pacotes propostos mantêm a URL do inventário.

## 3. Outros casos: URL de página agregadora ou explicativa

**Método.** Análise **estática** do formato de cada URL (`scripts/review_seed_urls.py`): sem rede, sem abrir páginas. Dez regras aplicadas em ordem atribuem a cada URL um **papel candidato**. O resultado diz o que o endereço *parece* ser; só a página confirma.

| Papel candidato da URL | Qtd. | Registros |
|---|---|---|
| Página de ajuda, FAQ, "about" ou documentação | 10 | EU04, EU05, EU08, EU09, EU13, EU16, EU23, EU27, EU30, EU34 |
| Página institucional explicativa de política ou serviço | 10 | EU10, EU12, EU14, EU15, EU21, EU26, EU28, EU29, EU37, EU38 |
| Raiz de um sítio inteiro | 4 | EU01, EU24, EU31, EU33 |
| Página de coleção ou registro nomeado | 4 | EU02, EU06, EU18, EU25 |
| Repositório de código | 3 | EU36, EU39, EU41 |
| Entrada de catálogo (descrição de um dataset) | 2 | EU11, EU17 |
| Interface de busca | 2 | EU19, EU20 |
| Notícia ou anúncio | 1 | EU22 |
| Registro em repositório de dados | 1 | EU35 |
| Outra página específica | 4 | EU03, EU07, EU32, EU40 |

**Leitura**

| # | Conclusão | Classe |
|---|---|---|
| 3.1 | Em 25 dos 41 registros, a URL tem a forma de página **sobre** o recurso (ajuda, explicação, notícia) ou de raiz de sítio, e não de endereço do recurso. | VERIFIED quanto à forma da URL; PENDING VALIDATION quanto ao conteúdo |
| 3.2 | Só um caso de URL repetida: EU03 e EU07. | VERIFIED |
| 3.3 | Quatro URLs trazem parâmetros de consulta (`?locale=en`), que a regra de deduplicação precisa tratar: EU04, EU11, EU18, EU23. | VERIFIED |
| 3.4 | As regras de padrão erram em casos de fronteira. Por exemplo, EU13 e EU16 caem em "ajuda" porque o caminho contém `/about/`, e EU37 e EU38 caem em "página institucional" embora possam ser a página do próprio corpus. | VERIFIED (limite do método) |
| 3.5 | Para nenhum registro além de EU03 há URL de acesso candidata com evidência. | VERIFIED |

**O que isso muda.** Para a maioria dos itens, o primeiro passo do avaliador será sair da página registrada e localizar o recurso. O formulário já tem o campo `url_actually_used` para isso. O protocolo de evidências prevê capturar **as duas** páginas: a registrada e a efetivamente usada.

**O que não foi feito.** Não abri as outras 39 páginas. Verificá-las uma a uma é parte da captura de evidências dos itens da amostra aprovada, depois da autorização, e não uma coleta a fazer agora.

## 4. Correções candidatas

Nenhuma aplicada. O inventário é artefato de proveniência e permanece como está; correções aceitas vão para uma tabela de recursos, não para o arquivo de seeds.

| ID | Campo | Valor no inventário | Candidato | Evidência | Estado |
|---|---|---|---|---|---|
| EU03 | URL de acesso | (ausente; só a página de descrição) | `https://datadump.publications.europa.eu/` | Página ELDS capturada, seção 4 | Candidata; decisão humana pendente |
| EU03 | Nome | "EUR-Lex bulk data dump" | "EUR-Lex data dump" | Mesma página: é a forma usada pela fonte | Candidata (rótulo) |
| EU07 | Nome | "European Legal Data Space — diretório" | "European Legal Data Space (ELDS)" | Título e texto da mesma página | Candidata (rótulo) |
| 25 registros | Papel da URL | — | Marcar como "página de descrição, endereço do recurso a localizar" | Forma da URL | Candidata; confirmar na captura |

## 5. Estatuto das afirmações

| Afirmação | Classe |
|---|---|
| Conteúdo da página ELDS em 2026-10-10 | VERIFIED (arquivo preservado, com hash) |
| Resposta 401 do endereço do dump | VERIFIED (duas tentativas registradas) |
| Papel candidato das 41 URLs | VERIFIED como aplicação das regras; PENDING VALIDATION como descrição das páginas |
| Qualquer classificação de EU03 ou EU07 na taxonomia | Inexistente — não é feita aqui |
