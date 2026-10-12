# NOTA SOBRE POTENCIAL DE PUBLICAÇÃO

**Data:** 2026-10-10 | **Estado:** avaliação preliminar, feita pelo agente de programação. Não é parecer de originalidade.

## Posição

Há três produtos possíveis, com maturidades diferentes. O produto de dados é o mais próximo de existir. O artigo de mapeamento depende de três coisas que ainda não foram feitas: revisão dos trabalhos anteriores, ampliação da busca no conjunto B e validação humana das classificações. A aplicação ao RGAM/V8 fica para depois e não deve condicionar as outras duas.

**Nenhuma contribuição inédita pode ser afirmada hoje.** A busca por trabalhos semelhantes feita nesta rodada foi curta e já encontrou antecedentes que precisam ser lidos.

## 1. O que foi feito para procurar trabalhos anteriores

Três buscas na web, pela ferramenta de busca do agente, em 2026-10-10:

1. *overview of datasets for empirical research on European Union law and legislation survey of data sources*
2. *systematic mapping review datasets regulatory governance European Union data infrastructure inventory*
3. *legal NLP datasets survey EUR-Lex corpora review multilingual EU legislation resources*

Limites: os resultados são resumidos por modelo de linguagem, não são reproduzíveis e **nenhuma das fontes abaixo foi aberta nem lida**. Os títulos e descrições vêm dos resultados de busca. Isto é uma lista de leitura, não uma revisão.

## 2. Antecedentes a examinar

| Trabalho, como apareceu na busca | Por que importa | O que verificar |
|---|---|---|
| Projeto LYNX (Horizon 2020), relatório D2.7, "Catalogue of relevant legal and regulatory datasets" (2020) | É o antecedente mais próximo pelo título: um catálogo de datasets jurídicos e regulatórios na Europa, com atenção a ELI/ECLI, formatos e acesso | Escopo, método, se ainda está disponível, e em que este mapeamento difere |
| Capítulo "Varieties of Data in EU Legal Scholarship" (Cambridge University Press) | Levanta quais dados a pesquisa jurídica sobre a UE efetivamente usa, a partir de 248 artigos | Mapeia usos em publicações, não recursos; pode ser complementar |
| König, Luetgert e Dannwolf (2006), sobre CELEX e PreLex, em *European Union Politics* | Avaliação comparada de duas bases oficiais do processo legislativo | Precedente metodológico para comparar fontes oficiais |
| Revisões de PLN jurídico: "Natural Language Processing for the Legal Domain: A Survey of Tasks, Datasets, Models, and Challenges" (arXiv 2410.21306); "Computational Law: Datasets, Benchmarks, and Ontologies" (arXiv 2503.04305); revisão sobre sumarização jurídica (arXiv 2501.17830) | Já inventariam corpora e benchmarks derivados do EUR-Lex | A parte "corpora acadêmicos" do conjunto A provavelmente não é novidade |
| Artigos de dados em ciência política da UE: DEU I–III; EUPROPS; artigos de dados sobre o TJUE | Cada um descreve o estado dos dados no seu subcampo | Seções de revisão desses artigos |
| O próprio European Legal Data Space | A iniciativa oficial já se apresenta como ponto de acesso a coleções de legislação e jurisprudência | Em que um inventário acadêmico acrescenta a um diretório oficial |
| Guias de bibliotecas e centros de documentação europeia | Listam as bases institucionais | Não são sistemáticos, mas cobrem o núcleo |

Ainda por procurar: catálogos de dados de direito e política comparados; inventários de dados de governança regulatória; artigos de dados sobre agências e autoridades reguladoras; revisões de "empirical legal studies" sobre a UE.

## 3. Produto 1 — base de dados reutilizável

**O que existe.** 105 registros de recursos, 86 pontos de acesso, 32 relações, 112 evidências com hash, dicionário, vocabulários, construtor determinístico, validador e testes.

**O que pode ter valor próprio**

- Separação entre recurso, ponto de acesso e relação. Catálogos costumam listar entradas; aqui uma entrada de catálogo é um ponto de acesso, e a ligação entre recursos é dado explícito, com evidência e confiança.
- Estado de acesso observado, com data: o que respondeu, o que exige autenticação, o que só funciona com JavaScript, o que falhou.
- Origem de cada valor, campo a campo.
- Registro das buscas que não deram resultado.

**O que falta para depositar**

| Requisito | Estado |
|---|---|
| Classificações confirmadas por pessoa | Nenhuma |
| Licenças lidas na fonte | 37 de 105 com indicação; nenhuma lida nos termos |
| Cobertura do conjunto B | Fraca |
| Decisão sobre redistribuir capturas de páginas de terceiros | Pendente; alternativa é publicar só hashes e URLs |
| Licença da própria base | Não definida |
| Identificador persistente e versão | Não atribuídos |
| Plano de atualização | Descrito no protocolo; não testado numa segunda rodada |

**Avaliação.** Depositar a base como dataset versionado, com documentação, é viável em poucas rodadas, e não precisa esperar o artigo. Um depósito cedo, declaradamente parcial e provisório, é defensável se disser com clareza o que é. Depositar a rodada 1 como está não é recomendável: seria publicar classificações de máquina sem conferência.

## 4. Produto 2 — artigo de mapeamento sistemático

**Contribuições descritivas possíveis**, todas condicionais:

1. Um retrato do ecossistema que junta os dois lados que a literatura trata em separado: recursos institucionais e recursos derivados acadêmicos. Depende de confirmar que os antecedentes não fazem isso.
2. A estrutura de dependência: quantos recursos derivam de quais, e de quantos mantenedores independentes o conjunto depende. A rodada 1 sugere concentração no Serviço das Publicações; é uma observação a testar com mais dados.
3. Uma descrição das condições reais de acesso, distinta das declaradas.
4. A assimetria entre dados legislativos e dados de governança regulatória. Hoje não é sustentável: a diferença observada entre A e B é explicável pela forma da busca.

**Contribuições metodológicas possíveis**

1. O problema da individuação de recursos de dados: URL não é recurso. O caso EU03/EU07 e a divergência entre descrições oficiais do mesmo recurso são exemplos concretos.
2. Um protocolo de mapeamento de recursos de dados, com a distinção em relação a revisões de publicações.
3. Uso documentado de um agente de IA na descoberta e triagem, com as salvaguardas e os limites. Interessa só se a validação humana for feita e relatada, com as taxas de acerto e erro do agente.

**Limitações para publicar**

| Limitação | Consequência | O que resolve |
|---|---|---|
| Sem revisão de antecedentes | Não se pode alegar novidade | Ler os trabalhos da seção 2 e buscar em índices bibliográficos |
| Busca não exaustiva, sem estimativa de cobertura | Contagens não generalizam | Mais vias de busca; teste de recuperação contra lista externa independente (por exemplo, o catálogo LYNX) |
| Classificação por um agente | Categorias e relações sem confiabilidade conhecida | Validação amostral independente |
| Verificação rasa | Não se pode falar de capacidades dos recursos | Exame de conteúdo numa amostra |
| Conjunto B subcoberto | A comparação A–B não se sustenta | Busca dirigida a órgãos e agências |
| Um único dia de observação | Estado de acesso é instantâneo | Segunda rodada em outra data |

**Avaliação.** O artigo é plausível, mas não está perto. O risco principal é descobrir que o catálogo LYNX ou outro trabalho já cobre o essencial; nesse caso a contribuição teria de ser a atualização, a estrutura relacional e o lado da governança regulatória. Convém ler os antecedentes antes de investir em mais rodadas de busca.

## 5. Produto 3 — aplicações ao projeto RGAM/V8

A base pode servir, mais tarde, a duas perguntas do projeto colaborativo: quais configurações de fonte legislativa comparar, e quais registros administrativos podem ser ligados a atos como enriquecimento. O `SOURCE_SELECTION_FRAMEWORK_v0_1.md` continua sendo o instrumento para isso e continua dependendo de U1–U6.

Duas observações desta rodada interessam a essa aplicação, sem antecipá-la:

- os recursos oficiais de textos legislativos parecem depender de um único mantenedor, o que afeta o que se pode chamar de comparação entre fontes;
- vários corpora acadêmicos derivam uns dos outros e do EUR-Lex, de modo que não contam como fontes independentes.

Nada disso foi apresentado a David Levi-Faur nem decidido com ele. Nenhuma fonte foi avaliada pelo quadro de seleção, e nenhuma foi escolhida.

## 6. Validação adicional necessária

| Validação | Para qual produto | Quando |
|---|---|---|
| Leitura dos antecedentes | Artigo | Antes de mais rodadas |
| Confirmação humana das linhas | Base e artigo | Antes de qualquer depósito |
| Validação amostral independente de categoria, conjunto, individuação e relações | Artigo | Antes de publicar contagens |
| Teste de recuperação contra lista externa | Artigo | Depois de ampliar a busca |
| Exame de conteúdo em amostra | Artigo, se falar de capacidades | Depois de estabilizar o inventário |
| Segunda observação de acesso em outra data | Artigo e base | Próxima rodada |

## 7. Recomendação

1. Ler os antecedentes da seção 2, começando pelo catálogo LYNX.
2. Em paralelo, a rodada 2 de descoberta voltada ao conjunto B.
3. Decidir cedo se o primeiro produto público é a base ou o artigo; a base pode sair antes.
4. Não descrever o inventário como "abrangente", "primeiro" ou "exaustivo" em nenhum texto até que 1 e a validação estejam feitos.
