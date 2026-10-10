**NOTA TÉCNICA — VERSÃO PRELIMINAR**

Identificação de intermediários regulatórios na legislação europeia

Exercício piloto de codificação assistida por LLM · Regulatory Intermediation · Transição verde da União Europeia

|  |  |
| --- | --- |
| **STATUS** | Codificação primária por Claude e revisão independente por Luna concluídas. Universo de revisão: 43 relações. Adjudicação final do pesquisador pendente. |

Esta nota apresenta a formulação preliminar de um exercício destinado a testar a viabilidade de converter atos normativos da União Europeia em dados estruturados sobre relações regulatórias, com foco em regulatory intermediation. A versão atual incorpora duas etapas concluídas: a codificação substantiva primária por Claude e a revisão crítica independente por Luna. Claude propôs 39 relações; Luna revisou integralmente essas propostas, acrescentou quatro relações omitidas e produziu um universo de revisão com 43 linhas. Os resultados permanecem provisórios até a adjudicação do pesquisador.

# 1. Objetivo do exercício

O exercício investiga se é possível reconstruir, de forma sistemática, auditável e posteriormente escalável, relações regulatórias contidas em legislação europeia e convertê-las em observações estruturadas. O foco não recai sobre a simples identificação de organizações citadas no texto normativo, mas sobre a arquitetura relacional Regulator–Intermediary–Target (R–I–T): quem exerce uma função regulatória, por meio de quem, sobre qual target, mediante qual mecanismo e com qual evidência textual.

|  |  |
| --- | --- |
|  | *O propósito não é identificar atores que possam ser classificados genericamente como “intermediários”, mas reconstruir relações regulatórias nas quais um ator desempenha uma função mediadora entre um regulador e um target.* |

O produto imediato é um proof of concept composto por três atos regulatórios associados à transição verde da União Europeia, uma matriz de relações codificadas e uma avaliação inicial da utilidade de LLMs como instrumentos de leitura e codificação substantiva. A ambição, nesta etapa, é metodológica: demonstrar que a passagem de texto jurídico para dados relacionais pode ser executada com regras explícitas, evidência rastreável e adjudicação do pesquisador.

# 2. Problema conceitual: de atores para relações

R, I e T são tratados como papéis relacionais, não como atributos permanentes de atores. A mesma organização pode atuar como regulator em uma relação, intermediary em outra e target em uma terceira. Por isso, a unidade analítica não é uma lista de instituições previamente classificadas, mas uma relação regulatória sustentada por evidência documental.

| **NÃO É SUFICIENTE** | **É NECESSÁRIO** |
| --- | --- |
| Palavra-chave | Relação regulatória reconstruída |
| Menção a um ator | Função regulatória identificável |
| Presença de um terceiro ator | Função mediadora demonstrável |
| Relatório ou informação | Papel do fluxo informacional na relação R–T |
| Advice / assistance | Contribuição integrada à operação regulatória |

**Quatro regras operacionais**

|  |  |
| --- | --- |
|  | *Keyword ≠ regulatory relationship · Actor mention ≠ intermediary · Advice/assistance ≠ automatically intermediation · Object ≠ target* |

Essas distinções reduzem dois riscos centrais: overcoding — classificar como intermediação qualquer participação institucional — e role confusion — confundir o objeto material da obrigação com o target regulado. O teste decisivo é funcional: o ator intermediário precisa desempenhar uma função institucionalmente integrada à operação da relação entre R e T.

# 3. O que o piloto metodológico já ensinou

A fase inicial foi deliberadamente intensiva em calibração. Foram combinadas codificações independentes, diferentes famílias de LLM, comparação estruturada e adjudicação de divergências. Esse desenho não foi concebido como workflow permanente, mas como mecanismo para revelar onde se concentram os problemas de confiabilidade antes da produção rotineira.

**1.** Screening lexical é útil para ampliar recall e localizar candidatos, mas não substitui interpretação substantiva da relação regulatória.

**2.** A unidade jurídica precisa ser contextual: regulator, intermediary e target podem estar distribuídos entre caput, parágrafos, anexos e referências internas.

**3.** A concordância tende a ser maior nos casos negativos; as divergências relevantes concentram-se justamente nas fronteiras teoricamente interessantes da intermediação.

**4.** A fronteira entre informação, advice, assistance e regulatory intermediation mostrou-se um dos pontos conceituais mais sensíveis.

**5.** A arquitetura experimental inicial mostrou-se excessivamente complexa para uso rotineiro, justificando um workflow de produção mais simples sem abandonar os safeguards substantivos.

|  |  |
| --- | --- |
|  | *O piloto cumpriu uma função de calibração. A fase de produção foi simplificada, mas preserva leitura integral, revisão crítica, evidência textual e adjudicação final do pesquisador.* |

# 4. Workflow simplificado de produção

|  |
| --- |
| **ATO OFICIAL EUR-LEX** |
| **↓ Corpus congelado** |
| **CLAUDE · leitura integral + proposta de codificação** |
| **LUNA · revisão crítica + estruturação do dataset** |
| **PESQUISADOR · adjudicação final** |
| **CSV FINAL** |

## 4.1 Claude — codificador substantivo primário

A etapa de codificação substantiva primária foi concluída. Claude realizou a leitura integral dos três corpora congelados e produziu propostas estruturadas de relações regulatórias, registrando regulator (R), intermediary (I), target (T), ação, objeto, função mediadora, mecanismo, evidência, tipo da relação e nível de confiança. O resultado consolidado contém 39 relações propostas: 7 na European Climate Law, 22 no CBAM e 10 no EUDR.

## 4.1.1 Resultado da codificação primária

A classificação primária de Claude distribuiu as 39 relações entre 9 propostas intermediated, 25 direct e 5 uncertain. A distribuição abaixo descreve apenas a primeira codificação e não substitui a revisão independente nem a decisão do pesquisador.

| **Caso** | **Total** | **Intermediated** | **Direct** | **Uncertain** |
| --- | --- | --- | --- | --- |
| Climate Law | 7 | 1 | 4 | 2 |
| CBAM | 22 | 5 | 16 | 1 |
| EUDR | 10 | 3 | 5 | 2 |
| **Total** | **39** | **9** | **25** | **5** |

## 4.1.2 Salvaguarda de independência e proveniência

A avaliação da etapa identificou uma ressalva de proveniência no Case 01. Os subagentes responsáveis pela codificação foram executados sem memória do piloto anterior, o que preserva a autonomia dos outputs primários. Entretanto, o resumo da sessão orquestradora registrou que a relação case\_01-rel-003 estava em “desacordo aberto” com uma adjudicação anterior. Isso indica uso de conhecimento histórico na camada de consolidação, ainda que não demonstre contaminação da codificação dos subagentes.

Como salvaguarda, os JSONs produzidos pelos três subagentes devem ser preservados como outputs primários. Comentários da sessão orquestradora que comparem as novas propostas com o piloto anterior serão tratados apenas como metadados de revisão e não como fundamento da classificação. A revisão por Luna deverá decidir exclusivamente a partir do corpus congelado e do codebook vigente.

## 4.2 Luna — revisor secundário e estruturador

A revisão secundária independente por Luna foi concluída. O revisor releu os três corpora, auditou as 39 propostas de Claude e realizou uma busca dirigida por omissões. O resultado demonstra revisão substantiva, e não mera normalização: 27 propostas foram ACCEPT, 6 REVISE, 5 QUESTION e 1 REJECT; Luna acrescentou ainda 4 ADD\_MISSING\_RELATION. O universo de revisão passou, assim, de 39 para 43 linhas. O piloto anterior não foi tratado como ground truth para decidir as classificações atuais.

## 4.2.1 Resultado da revisão secundária

A distribuição substantiva provisória após a revisão de Luna é de 8 relações intermediated, 27 direct, 7 uncertain e 1 not\_supported. Entre os 39 registros originalmente propostos por Claude, os dois modelos mantiveram o mesmo relation\_type em 32 casos (aproximadamente 82%). Seis relações foram classificadas como intermediated por ambos. Esses números são indicadores descritivos de concordância substantiva; não constituem, por si, estimativa de confiabilidade ou validação do construto.

| **Status de revisão Luna** | **N** |
| --- | --- |
| ACCEPT | 27 |
| REVISE | 6 |
| QUESTION | 5 |
| REJECT | 1 |
| ADD\_MISSING\_RELATION | 4 |
| **Total no universo de revisão** | **43** |

| **Relation type provisório após Luna** | **N** |
| --- | --- |
| Intermediated | 8 |
| Direct | 27 |
| Uncertain | 7 |
| Not supported | 1 |
| **Total** | **43** |

O padrão de concordância é substantivamente informativo porque há um núcleo de casos positivos mantido por duas leituras e, simultaneamente, divergências concentradas em fronteiras teóricas relevantes. A revisão, portanto, reduziu a incerteza em parte do corpus sem eliminá-la artificialmente.

## 4.3 Pesquisador — adjudicação

A autoridade final permanece humana. Nenhuma camada adicional de agentes é prevista antes da adjudicação. O pesquisador deverá concentrar a revisão integral nos 8 casos classificados por Luna como intermediated e nos 7 uncertain; em seguida, revisar rapidamente os 4 ADD\_MISSING\_RELATION, o único REJECT e as REVISE que alteraram R, I, T ou relation\_type. Registros ACCEPT + direct + high confidence podem ser aprovados em bloco após auditoria amostral. A formulação operacional permanece: the LLM proposes; the researcher remains responsible for the final coding.

# 5. Casos selecionados

Os três casos foram selecionados prospectivamente por relevância para a transição verde, diversidade institucional e viabilidade de leitura integral. A seleção não utilizou resultados R–I–T, quantidade de keywords ou conhecimento prévio da existência de intermediários, evitando selecionar o universo pelo próprio fenômeno que se pretende observar.

| **Caso** | **CELEX** | **Regulação** | **Arquitetura regulatória geral** |
| --- | --- | --- | --- |
| 1 | 32021R1119 | European Climate Law | Governança climática, assessment, monitoring e scientific inputs. |
| 2 | 32023R0956 | Carbon Border Adjustment Mechanism (CBAM) | Importação, emissões, certificados, verification, customs e compliance. |
| 3 | 32023R1115 | Deforestation-Free Products Regulation (EUDR) | Due diligence, rastreabilidade, informação, checks e supply-chain governance. |

# 6. Protocolo de codificação

## 6.1 Unidade de análise

A unidade é uma relação regulatória apoiada por evidência textual. Uma relação pode exigir leitura contextual de mais de uma disposição, desde que sua reconstrução permaneça vinculada ao corpus e seja auditável.

## 6.2 Tipos de relação

**•** intermediated — relação R–I–T com função mediadora demonstrável;

**•** direct — relação R–T sem intermediário identificado;

**•** uncertain — arquitetura regulatória plausível, mas um elemento essencial permanece indeterminado;

**•** not supported — não há relação regulatória sustentada pela evidência disponível.

## 6.3 Regra de evidência

A interpretação é source-bounded. São admitidos o texto do ato, seu contexto hierárquico e referências internas reproduzidas no corpus. Informação externa pode ser usada em etapas posteriores de interpretação teórica, mas não é importada silenciosamente para preencher a codificação primária.

## 6.4 Critério de intermediação

|  |  |
| --- | --- |
|  | *Um ator pode ser intermediary sem possuir autoridade coercitiva própria sobre T, desde que desempenhe uma função institucionalmente integrada à operação da relação regulatória R–T. Mera consulta, aconselhamento, expertise ou fornecimento genérico de informação, por si sós, não bastam.* |

# 7. Resultados preliminares dos três casos

Com a revisão secundária concluída, o exercício passa de uma lista primária de 39 relações para um universo de revisão de 43 linhas. Luna acrescentou quatro relações omitidas e alterou a interpretação substantiva de parte dos registros, demonstrando que a segunda leitura funcionou como instância crítica efetiva. As categorias abaixo continuam provisórias: apenas a adjudicação do pesquisador produzirá o dataset empírico final.

|  |
| --- |
| **STATUS DOS RESULTADOS — revisão Luna concluída; 43 relações no universo de revisão. Contagens ainda não adjudicadas pelo pesquisador.** |

| **Caso** | **Claude: relações** | **Claude: intermediated** | **Claude: direct** | **Claude: uncertain** | **Etapa** |
| --- | --- | --- | --- | --- | --- |
| Climate Law | 7 | 1 | 4 | 2 | Revisto por Luna |
| CBAM | 22 | 5 | 16 | 1 | Revisto por Luna |
| EUDR | 10 | 3 | 5 | 2 | Revisto por Luna |
| **Total** | **39** | **9** | **25** | **5** | **+4 relações Luna** |

A revisão de Luna elevou o universo para 43 relações e produziu a distribuição provisória 8 intermediated, 27 direct, 7 uncertain e 1 not\_supported. O dado mais relevante não é a contagem bruta, mas a existência de um núcleo de seis relações classificadas como intermediated por ambos os codificadores, cercado por fronteiras conceituais específicas. A maior densidade de relações no CBAM não deve ser interpretada como medida diretamente comparável de “quantidade de intermediação”, pois os atos diferem em extensão e desenho institucional.

As contagens não serão tratadas como medidas diretamente comparáveis da “quantidade de intermediação”. Os atos diferem em extensão, densidade normativa e desenho institucional. Além disso, a concordância Claude–Luna é um sinal útil de estabilidade local, mas não substitui a adjudicação conceitual nem deve ser apresentada como coeficiente formal de confiabilidade.

## 7.1 Relações representativas

A revisão identificou um núcleo de seis relações classificadas como intermediated por Claude e Luna. Elas constituem os primeiros candidatos a exemplos representativos, mas permanecem sujeitas à decisão do pesquisador:

**•** Climate Law, Article 8(4): Commission → EEA → Member States. Luna entendeu que a EEA possui dever jurídico específico de assistência na preparação das avaliações usadas pela Commission para supervisionar Member States.

**•** CBAM: duas relações envolvendo accredited verifier, incluindo verificação de authorised CBAM declarant e de third-country installation operator. Ambos os modelos as trataram como casos fortes de verification integrada ao compliance.

**•** CBAM, Article 9(2): independent certifier. Claude e Luna mantiveram a classificação intermediated, embora Luna tenha revisado a descrição da ação.

**•** EUDR, Article 26: competent authorities → customs authorities → operators/traders. Ambos mantiveram intermediated; a função envolve implementação de consequências de fronteira ligadas à avaliação de compliance.

**•** EUDR: persons submitting substantiated concerns. Ambos mantiveram intermediated, mas este permanece conceitualmente delicado porque exige decidir se o acionamento institucionalizado do enforcement é suficiente para configurar intermediação.

|  |
| --- |
| **A PREENCHER APÓS ADJUDICAÇÃO — substituir esta síntese por 3–6 relações finais com R, I, T, função mediadora, mecanismo, localização e evidência textual extraídos do dataset adjudicado.** |

## 7.2 Divergências substantivas que exigem adjudicação

A segunda leitura tornou visíveis quatro fronteiras particularmente importantes. Elas não devem ser resolvidas por maioria entre modelos, pois implicam decisões ontológicas sobre o próprio construto de regulatory intermediation.

**•** CBAM — customs information chains: duas propostas que Claude classificou como intermediated foram rebaixadas por Luna para uncertain. A questão é distinguir intermediary de data conduit ou co-regulator paralelo.

**•** EUDR — Commission information system, Article 33: Claude classificou como intermediated; Luna rebaixou para uncertain. O caso expõe o problema de tratar infraestrutura tecnológica como ator intermediário. Mantido o critério atual de que I deve ser ator ou classe de atores, a tendência é excluir o sistema como I.

**•** CBAM — Articles 15 e 35: Luna elevou duas relações originalmente direct para intermediated, interpretando a competent authority como elo de um enforcement handoff sequencial entre Commission e target. A decisão exige distinguir intermediary de divisão vertical de competências entre co-regulators.

**•** EUDR — substantiated concerns: a classificação positiva depende de decidir se um terceiro que formalmente aciona assessment e follow-up de enforcement desempenha função mediadora ou apenas exerce um canal episódico de participação/denúncia.

# 8. Questão substantiva emergente: information and assistance as regulatory intermediation

|  |  |
| --- | --- |
|  | *When does informational, scientific, advisory, verification or implementation assistance become regulatory intermediation?* |

O piloto sugere que uma das fronteiras mais relevantes não é computacional, mas teórica. A legislação regulatória mobiliza inúmeros atores que produzem conhecimento, aconselham, reportam, verificam, certificam, monitoram ou apoiam a implementação. Nem toda participação desse tipo constitui regulatory intermediation. O desafio é identificar quando o fluxo de informação ou assistência deixa de ser apenas input contextual e passa a integrar funcionalmente a relação entre regulator e target.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| background knowledge | scientific advice | institutional information input | mandatory reporting | verification / certification | delegated monitoring | **regulatory intermediation** |

Esse continuum é apenas heurístico. A codificação não presume que exista uma fronteira lexical automática nem que toda função situada “mais à direita” seja necessariamente intermediação. A decisão depende da inserção institucional da função no mecanismo regulatório específico. Esta questão deverá ser retomada após os casos concretos permitirem observar padrões recorrentes.

## 8.1 Fronteiras prioritárias para a adjudicação

A revisão secundária confirmou que as fronteiras mais informativas do exercício não se concentram em termos lexicais, mas na arquitetura institucional. Três famílias devem orientar a adjudicação e eventual refinamento do codebook:

• verifiers e certifiers no CBAM, que formam o conjunto empiricamente mais forte de candidatos a intermediários, com função de verification/certification juridicamente integrada ao compliance;

• customs authorities e competent authorities no CBAM, cuja posição pode oscilar entre intermediary, implementador delegado e co-regulator conforme a estrutura de competências e o encadeamento do enforcement;

• information systems, fluxos informacionais e substantiated concerns no EUDR, onde a ontologia do ator e o limiar entre informação institucionalizada e mediação regulatória precisam ser definidos com especial cuidado.

# 9. Produto entregue: dataset relacional

O CSV continua sendo o principal produto empírico do exercício; a nota técnica funciona como documentação sintética de sua lógica. Após a revisão Luna, o arquivo de trabalho contém 43 linhas e deve preservar, lado a lado, a proposta de Claude, a revisão de Luna e os campos ainda vazios de decisão do pesquisador. Somente a versão pós-adjudicação poderá ser denominada dataset final.

|  |
| --- |
| case · CELEX · location · evidence · R · I · T · action · object · mediating\_function · mechanism · relation\_type · confidence · researcher\_decision |

|  |  |
| --- | --- |
|  | *CSV = produto principal. Nota técnica = explicação necessária para interpretar o CSV.* |

# 10. Limitações e próximo passo

O exercício é deliberadamente exploratório. Trabalha com três casos substantivos, não com uma amostra estatística; utiliza codificação assistida por LLM; e depende de definições operacionais ainda em estabilização. A revisão secundária aumentou a robustez do processo ao contestar classificações e recuperar omissões, mas a concordância entre modelos não equivale a verdade substantiva. A ressalva de proveniência identificada na consolidação do Case 01 continua relevante e reforça a necessidade de preservar outputs primários, revisão secundária e decisão humana como camadas separadas e auditáveis.

O próximo passo imediato é a adjudicação do pesquisador. A revisão pode ser hierarquizada: Tier 1 — revisão integral dos 8 intermediated e 7 uncertain; Tier 2 — revisão rápida dos 4 ADD\_MISSING\_RELATION, do único REJECT e das REVISE que alteraram R/I/T ou relation\_type; Tier 3 — aprovação em bloco dos ACCEPT + direct + high confidence após pequena auditoria amostral. Concluída essa etapa, serão produzidos o REGULATORY\_INTERMEDIARIES\_3\_CASES\_FINAL.csv e a nota técnica final, com contagens adjudicadas, relações representativas e 2–3 achados substantivos.

|  |
| --- |
| **A PREENCHER APÓS ADJUDICAÇÃO DO PESQUISADOR — inserir contagens finais, 3–6 relações representativas com evidência, 2–3 achados substantivos e eventual ajuste do codebook. Esta será a última atualização antes da versão destinada ao professor David Levi-Faur.** |

**Nota de versão.** Versão atualizada após conclusão e avaliação da revisão Luna. Registra o universo de 43 relações, os padrões de concordância e divergência Claude–Luna e a fila conceitual para adjudicação, mantendo explícita a distinção entre revisão secundária e dataset final.