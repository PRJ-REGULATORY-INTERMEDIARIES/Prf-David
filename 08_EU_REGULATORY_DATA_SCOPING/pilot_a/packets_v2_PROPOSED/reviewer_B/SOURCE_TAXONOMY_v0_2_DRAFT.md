# TAXONOMIA OPERACIONAL DE FONTES — v0.2 DRAFT

**Data:** 2026-10-09 | **Gate:** G0.1 | **Estado:** PROPOSED — instrumento a calibrar no Piloto A; não aprovado, não congelado.
**Antecedente:** a v0.1 é a lista de nove tipos sugerida na emenda A02 de `PROPOSED_AMENDMENTS.md`. Esta versão a substitui como proposta, sem alterar aquele arquivo.

**Aviso de uso.** Este documento é o instrumento de trabalho dos avaliadores. Por isso **não classifica nenhum dos 41 registros do inventário exploratório** e não usa nenhum deles como exemplo. Os exemplos são genéricos.

## 1. Princípios

1. **Classifica-se pelo conteúdo e pelo mantenedor, não pelo modo de acesso.** O mesmo acervo servido por página web, API e arquivo em lote é um recurso com três distribuições.
2. **Classe e relação são coisas diferentes.** "Distribuição de um mesmo recurso" e "recurso duplicado ou sobreposto" não são tipos de recurso; são relações entre registros. Tratá-las como classes produziria dupla contagem.
3. **A unidade que se conta no inventário não é a unidade que se codifica.** O inventário conta recursos. O que a operacionalização RGAM/V8 codificará no futuro é uma unidade jurídica (ato, versão, dispositivo). As duas vivem em tabelas separadas e nenhuma contagem as mistura.
4. **Toda classificação tem evidência.** Sem evidência suficiente, a resposta correta é `INDETERMINADO`, nunca a classe mais provável.
5. **A classe não diz nada sobre qualidade nem sobre utilidade para a pesquisa.** A adequação é avaliada depois, em `SOURCE_SELECTION_FRAMEWORK_v0_1.md`.

## 2. Níveis de identidade

| Nível | Nome | O que é | Conta-se? |
|---|---|---|---|
| L0 | Ocorrência | Uma linha de descoberta: um resultado de busca, um seed, uma sugestão. Pode repetir outra. | Sim, como número de ocorrências; nunca como recurso |
| K | Contêiner | Portal, sítio ou catálogo que hospeda ou lista vários recursos e não tem acervo próprio distinto deles. | Não entra em denominador; é relatado à parte |
| L1 | **Recurso** | Acervo lógico ou serviço com mantenedor, escopo declarado e unidade de observação próprios. **Unidade de contagem do inventário.** | Sim |
| L2 | Distribuição | Um caminho de acesso a um recurso: interface, formato, protocolo, pacote. | Sim, separadamente de L1 |
| L3 | Unidade jurídica | Ato, versão de ato ou dispositivo contido num recurso. | Fora do inventário (seção 8) |

Corresponde aos quatro níveis do PROTOCOL §5, com dois acréscimos: o contêiner (K) e o desdobramento explícito de L3.

## 3. Classes de recurso (L1)

Sete classes mutuamente exclusivas para a **classe primária**, mais duas residuais. As sete correspondem às sete primeiras categorias pedidas no G0.1; as duas últimas categorias pedidas são tratadas como relações (seção 5).

| Código | Classe | Definição operacional | Teste decisivo | Não é |
|---|---|---|---|---|
| `FPL` | Fonte primária de legislação | Recurso cujo conteúdo são os próprios atos jurídicos, mantido pelo órgão que tem a atribuição de publicá-los oficialmente, ou por conta dele. | Há ato normativo ou declaração institucional que atribua ao mantenedor a publicação oficial desses atos, **e** o recurso não declara ter sido construído a partir de outro. | Uma cópia fiel feita por terceiro; um índice sem os textos |
| `REP` | Repositório jurídico | Acervo consultável de documentos jurídicos de uma ou várias origens, que reúne, organiza ou republica textos sem ser o local de publicação oficial deles. | O conteúdo são documentos jurídicos em texto, **e** o teste de `FPL` falha, **e** não há transformação analítica (seleção amostral, anotação, rotulagem). | Um corpus anotado; um catálogo de links |
| `DSE` | Dataset jurídico estruturado | Coleção de registros com esquema declarado cuja unidade de observação é o ato jurídico, um evento do seu ciclo de vida ou um atributo dele, publicada como dado e não como documento. | Existe esquema ou dicionário de campos, **e** a unidade de observação é jurídico-normativa (ato, procedimento, votação, medida de transposição). | Um conjunto de textos sem campos; um registro de entidades reguladas |
| `API` | Infraestrutura de API e dados vinculados | Serviço ou grafo com **modelo de dados e identificadores próprios**, que expõe entidades e relações não disponíveis como tal em outra distribuição do mesmo mantenedor. | Há documentação de modelo ou ontologia próprios **e** evidência de conteúdo relacional que só existe ali. Se o serviço apenas dá outro acesso ao mesmo acervo, **não é recurso**: é distribuição (L2). | Qualquer endpoint; a API de um dataset já registrado |
| `COD` | Corpus legislativo derivado | Coleção construída por terceiro a partir de outro recurso, por seleção, limpeza, alinhamento, anotação ou rotulagem. | A documentação declara a origem, **ou** a origem é demonstrável por identificadores herdados. Exige preencher `derived_from`. | A fonte de onde deriva; uma distribuição oficial em outro formato |
| `REG` | Registro administrativo ou setorial | Cadastro ou registro produzido na aplicação do direito, cuja unidade de observação é uma entidade, decisão, caso, notificação ou evento, e não o ato normativo. | A unidade de observação não é um ato jurídico de alcance geral. | Um dataset sobre o processo legislativo (`DSE`) |
| `AUX` | Fonte auxiliar de enriquecimento | Vocabulário controlado, tesauro, padrão de identificação, ontologia ou tabela de autoridades, usado para classificar, identificar ou ligar registros de outros recursos. | Não contém atos nem registros de entidades reguladas; contém conceitos, códigos ou regras de identificação. | Um dataset que usa o vocabulário |
| `FDE` | Fora de escopo | Não tem relação material com legislação ou regulação da UE, ou não é coleção estruturada (PROTOCOL E1, E5). | Critérios de exclusão do protocolo. | — |
| `IND` | Indeterminado | A evidência disponível não permite decidir. | Exige dizer qual evidência falta. | Uma classe de descanso: é um estado provisório |

Dois tipos não pedidos no G0.1 foram acrescentados porque existem recursos assim no inventário e precisam de destino: o **contêiner** (nível K, seção 2) e o **software** sem dados próprios, que vai para `FDE` com `reason_code` específico, registrando-se à parte os dados que ele eventualmente distribua.

## 4. Regras de classificação

Aplicar na ordem. A primeira regra que se aplica decide. Cada resposta exige a evidência indicada.

| Passo | Pergunta | Se sim | Evidência exigida |
|---|---|---|---|
| R0 | O registro aponta para algo já registrado, com o mesmo conteúdo e o mesmo caminho de acesso? | Relação `duplicate_of`; não cria recurso | URL canônica idêntica **ou** mesmo identificador persistente |
| R1 | É um portal, sítio ou catálogo que reúne vários acervos com unidades de observação ou escopos distintos? | Nível K; cada acervo interno é avaliado em separado a partir de R2 | Lista dos acervos internos, com a página que os distingue |
| R2 | É outro caminho de acesso a um recurso já registrado, do mesmo mantenedor, com o mesmo escopo declarado e a mesma unidade de observação? | Nível L2, relação `distribution_of`; se cobrir só parte do acervo, marcar `partial` e descrever | Documentação que ligue o caminho ao acervo |
| R3 | Tem relação material com o direito da UE e é coleção estruturada? | Se **não**: `FDE` com motivo | Critérios I1, I2, E1, E5 do protocolo |
| R4 | Contém conceitos, códigos ou regras de identificação, e não atos nem entidades? | `AUX` | Descrição do conteúdo |
| R5 | A unidade de observação é entidade, decisão individual, caso, notificação ou evento de aplicação? | `REG` | Descrição da unidade de observação |
| R6 | Declara ter sido construído a partir de outro recurso, por terceiro? | `COD`, com `derived_from` | Declaração de origem |
| R7 | O conteúdo são textos de atos jurídicos, e o mantenedor tem atribuição de publicação oficial? | `FPL` | Base normativa ou declaração institucional da atribuição |
| R8 | O conteúdo são textos de documentos jurídicos, sem a atribuição de R7? | `REP` | Descrição do acervo |
| R9 | O conteúdo são registros com esquema sobre atos, procedimentos ou eventos normativos? | `DSE` | Esquema ou dicionário de campos |
| R10 | É serviço com modelo de dados e identificadores próprios e conteúdo relacional exclusivo? | `API` | Documentação do modelo; evidência do conteúdo exclusivo |
| R11 | Nenhuma das anteriores pôde ser respondida com evidência. | `IND`, com a evidência faltante | — |

**Notas às regras**

- **R1 antes de tudo o mais.** Um portal não recebe classe. Recebem classe os acervos que ele hospeda. O critério para separar acervos internos é objetivo: unidade de observação diferente, **ou** escopo declarado diferente com documentação ou identificador próprio.
- **R2 é o padrão para APIs.** Um serviço programático só chega a R10 se falhar em R2. A carga da prova é de quem quer registrá-lo como recurso.
- **R7 exige evidência positiva da atribuição.** "É o sítio oficial" não basta; registrar o ato ou a declaração que estabelece a atribuição. Sem isso, a classe é `REP`, com nota.
- **Autenticidade não se decide aqui.** Se a versão eletrônica tem valor jurídico autêntico é pergunta da avaliação de adequação (critério A5 do quadro de seleção), não da classificação.

## 5. Relações entre registros

Registradas em tabela própria, uma linha por relação, com evidência. São elas que resolvem as duas últimas categorias pedidas no G0.1.

| Relação | Significado | Efeito na contagem |
|---|---|---|
| `duplicate_of` | Mesmo recurso, mesmo caminho de acesso; ocorrência repetida. | A ocorrência não gera recurso nem distribuição |
| `distribution_of` | Caminho de acesso a um recurso. Atributo `partial` quando cobre só parte. | Conta como distribuição (L2) |
| `hosted_by` | Recurso hospedado ou listado num contêiner. | Nenhum |
| `derived_from` | Construído a partir de outro recurso por transformação. | Ambos contam como recursos; o derivado nunca conta como fonte independente de atos |
| `part_of` | Subconjunto próprio de outro recurso, mantido como unidade separada pelo mesmo mantenedor. | Conta como recurso só se tiver documentação e identidade próprias; caso contrário, é distribuição parcial |
| `overlaps_with` | Recursos distintos, de mantenedores ou finalidades diferentes, com conteúdo em parte coincidente. | Ambos contam; a sobreposição é relatada |
| `successor_of` | Substitui um recurso descontinuado. | Ambos contam, com estado distinto |
| `uses` | Emprega um recurso `AUX` (vocabulário, identificador). | Nenhum |

**Duplicado × sobreposto.** Duplicado é identidade: some na contagem. Sobreposto é interseção de conteúdo entre recursos que continuam distintos: permanece na contagem e gera uma linha de relação. A regra de decisão entre `distribution_of` e `overlaps_with` é o mantenedor: mesmo mantenedor e mesmo acervo declarado, distribuição; mantenedores diferentes, sobreposição ou derivação.

**Deduplicação por URL não basta.** Duas ocorrências com a mesma URL podem descrever recursos distintos hospedados na mesma página, e duas URLs diferentes podem levar ao mesmo recurso. A URL canônica gera **candidatos** a duplicata; a decisão é humana e registrada.

## 6. Recursos com mais de uma função

1. **Uma classe primária, decidida pelas regras da seção 4.** A ordem das regras é a regra de precedência.
2. **Papéis secundários** em campo multivalorado `secondary_roles`, com o mesmo vocabulário de classes. Cada papel secundário exige a sua própria evidência.
3. **Portais multifuncionais são decompostos** (R1), não classificados. A multifuncionalidade aparente de um portal quase sempre é a soma de acervos distintos.
4. **Nenhuma contagem usa papéis secundários.** As tabelas por classe usam a classe primária; os papéis secundários aparecem em tabela descritiva à parte.
5. **O papel na pesquisa não é propriedade do recurso.** Se um recurso servirá como fonte de textos, como enriquecimento ou como comparação é decisão registrada no parecer de seleção, não na taxonomia.

### Subclasse derivada: fonte legislativa candidata

Atendendo ao registro de decisões v1.1 (seção 4.2), define-se um indicador **derivado**, não uma classe:

`legislative_candidate = sim` se, e somente se, (a) a classe primária é `FPL`, `REP`, `COD` ou `DSE`; (b) o recurso contém o **texto** de atos jurídicos da UE, e não apenas metadados; (c) cada texto é recuperável por um identificador de ato.

Recursos `REG` e `AUX` nunca são candidatos (decisão D09 do registro). Um recurso `API` é candidato apenas por meio do recurso a que dá acesso. O indicador só diz quem **entra** na avaliação comparativa; não antecipa o resultado.

## 7. Identificadores canônicos

| Objeto | Identificador | Regra |
|---|---|---|
| Ocorrência (L0) | `record_id` existente (por exemplo `SEED_EUxx`) | Mantido; nunca reutilizado |
| Contêiner (K) | `K` + três dígitos | Atribuído na adjudicação |
| Recurso (L1) | `R` + quatro dígitos | **Opaco e sequencial**; atribuído só depois da adjudicação; nunca codifica classe, mantenedor ou julgamento |
| Distribuição (L2) | identificador do recurso + `-D` + dois dígitos | Uma por caminho de acesso |
| Relação | `REL` + cinco dígitos | Uma linha por par ordenado e tipo |
| Identificadores externos | campos `pid_type` e `pid_value` | DOI, URI, identificador de catálogo; registrados como informados pela fonte |

Identificadores opacos são deliberados: um identificador que contém a classe ou o nome do recurso fica errado quando a classificação é revista e induz o leitor a tomar o rótulo por fato.

Um identificador nunca é reatribuído. Recurso fundido ou desfeito após revisão mantém o identificador antigo com estado `merged_into` ou `withdrawn`.

## 8. A unidade jurídica (L3) e sua separação do inventário

**O inventário não conta atos.** Quantos atos um recurso contém é atributo descritivo do recurso (cobertura), nunca linha do inventário.

A unidade jurídica tem estrutura própria, que o teste empírico (G5) e a futura codificação precisam distinguir:

| Componente | O que distingue | Campo | Regra |
|---|---|---|---|
| Ato | A norma como obra intelectual | `act_celex`, `act_eli`, `act_oj_ref` | Cadeias de caracteres, como informadas pela fonte; equivalência entre elas só após inspeção (CODEBOOK, regra 4) |
| Versão temporal | Texto original, versão consolidada em certa data, retificação | `version_type`, `version_date` | Original e consolidado nunca são tratados como o mesmo texto |
| Expressão linguística | Idioma | `language` | Código de idioma informado pela fonte |
| Manifestação | Formato do arquivo | `format`, `sha256` | Hash do arquivo obtido |
| Subdivisão | Artigo, número, alínea, anexo | `subdivision` | Como endereçável na fonte; registrar se o endereçamento é estruturado ou apenas textual |

O que esta taxonomia fixa são os **nomes dos campos e a regra de não equivalência**. Ela não decide:

- qual é o universo de atos elegíveis (*Legal Universe Definition*);
- quais atos serão amostrados (*Sampling and Case Selection Protocol*);
- qual nível de subdivisão será a unidade de codificação da operacionalização RGAM/V8, nem suas categorias (*Codebook* do RGAM/V8).

Essas três decisões pertencem a documentos próprios, conforme a seção 8 do registro de decisões v1.1, e não são tocadas aqui.

## 9. Campos mínimos por classificação

| Campo | Conteúdo |
|---|---|
| `record_id` | Ocorrência avaliada |
| `level` | K, L1 ou L2 (ou `duplicate`) |
| `primary_class` | Código da seção 3 |
| `rule_applied` | Passo R0–R11 que decidiu |
| `secondary_roles` | Lista, possivelmente vazia |
| `relations` | Tipo e alvo de cada relação declarada |
| `legislative_candidate` | sim / não / indeterminado |
| `maintainer` | Como declarado na fonte |
| `observation_unit` | Como declarada na fonte |
| `evidence_ref`, `accessed_at`, `snapshot_sha256` | Evidência arquivada (emenda A06) |
| `missing_evidence` | Obrigatório se `IND` |
| `reviewer`, `date` | Pessoa identificada |

## 10. Unidades de contagem e de avaliação

| Finalidade | Unidade | Tabela |
|---|---|---|
| Fluxo de descoberta | Ocorrência (L0) | `discovery_records` |
| Tamanho e composição do inventário | Recurso (L1), por classe primária | recursos |
| Diversidade de acesso | Distribuição (L2) | distribuições |
| Avaliação de adequação (Dimensão A) | **Configuração candidata** = um recurso + uma distribuição específica | quadro de seleção |
| Teste empírico | Unidade jurídica (L3) obtida por uma configuração | execuções do benchmark |
| Codificação RGAM/V8 | Definida pelo codebook do RGAM/V8 | fora deste estudo |

A avaliação de adequação recai sobre a configuração, e não sobre o recurso, porque propriedades como formato, estabilidade de acesso e reprodutibilidade variam entre distribuições do mesmo recurso.

## 11. Questões abertas para o Piloto A

1. A fronteira `FPL` × `REP` é decidível com a evidência normalmente disponível numa página institucional?
2. A fronteira `DSE` × `REG` (dado sobre o processo normativo × dado sobre a aplicação) é estável entre avaliadores?
3. R1 produz decomposições iguais do mesmo portal por avaliadores diferentes?
4. R2 e R10 separam de modo consistente a API-distribuição da API-recurso?
5. Vocabulário distribuído como arquivo de dados é `AUX` ou `DSE`? (A regra atual responde `AUX`, por R4 vir antes de R9.)
6. `part_of` é necessário, ou `distribution_of` com `partial` basta?
7. Qual a frequência de `IND`, e que evidência costuma faltar?

## 12. Estatuto das afirmações deste documento

| Afirmação | Classe |
|---|---|
| A taxonomia cobre as nove categorias pedidas no G0.1 (sete como classes, duas como relações) | VERIFIED (por construção) |
| As regras são aplicáveis de modo consistente por avaliadores independentes | PENDING VALIDATION (Piloto A) |
| As classes são mutuamente exclusivas e exaustivas para os recursos reais | PENDING VALIDATION (Piloto A) |
| A adoção da taxonomia | PROPOSED (decisão da equipe) |
