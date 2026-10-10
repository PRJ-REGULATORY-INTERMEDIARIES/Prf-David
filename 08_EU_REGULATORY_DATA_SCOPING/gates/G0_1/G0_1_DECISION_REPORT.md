# RELATÓRIO DE DECISÃO G0.1

**Projeto:** EU Regulatory Data Scoping (`08_EU_REGULATORY_DATA_SCOPING`)
**Data:** 2026-10-09 | **Elaboração:** agente de programação (Claude Code), sob coordenação humana | **Destinatário:** equipe científica do PRJ-David

## Conclusão

**A reorientação é viável e melhora o estudo, mas cria duas dependências que o desenho original não tinha, e é delas que depende o calendário.**

1. A avaliação de cobertura exige saber de antemão que tipos de atos e que período interessam. Essa definição ainda está pendente de discussão com David e a equipe. Proponho um envelope provisório, fixado antes de qualquer avaliação.
2. O inventário exploratório sugere que os candidatos a fonte legislativa podem ser, na prática, uma única fonte oficial com várias distribuições e corpora derivados dela. Se a busca não encontrar alternativa independente, o estudo será uma verificação dessa fonte e uma comparação de suas vias de acesso, e não uma comparação entre fontes. Isso muda o que se pode afirmar e publicar.

Nada foi decidido em nome da equipe. Nenhuma fonte foi avaliada, pontuada ou escolhida. O G1 pode começar quando as condições da seção 9 forem cumpridas; a de maior peso é a nomeação das pessoas.

**Classificação:** VERIFIED (observado em arquivo ou comando) · PROPOSED (recomendação; decisão humana) · PENDING VALIDATION (depende de fato, teste ou aprovação ainda inexistentes).

**Documentos desta fase**

| Arquivo | Conteúdo |
|---|---|
| `protocol/G0_1_STRATEGIC_ALIGNMENT.md` | Revisão das 27 emendas; problemas novos; especificações de salvaguarda; roteiro |
| `protocol/SOURCE_TAXONOMY_v0_2_DRAFT.md` | Taxonomia operacional |
| `protocol/SOURCE_SELECTION_FRAMEWORK_v0_1.md` | Quadro de seleção em duas dimensões |
| `outputs/G0_1_REVISED_PILOT_DESIGN.md` | Pilotos A e B |
| `outputs/G0_1_DECISION_REPORT.md` | Este relatório |

---

## 1. Síntese da reorientação científica

| # | Conclusão | Classe |
|---|---|---|
| 1.1 | O registro de decisões v1.1 está no repositório (`inputs/`) e foi lido na íntegra. Estabelece como finalidade prioritária justificar a seleção da infraestrutura legislativa do dataset RGAM/V8; a publicação autônoma passa a ser possibilidade condicionada aos resultados. | VERIFIED |
| 1.2 | O registro declara ser diretriz do proponente, não aprovação de David, de Rotem ou dos demais colaboradores. | VERIFIED |
| 1.3 | A adoção da reorientação pela equipe. | PENDING VALIDATION |
| 1.4 | O registro manda separar quatro decisões: escolha da fonte, definição do universo jurídico, seleção de casos e codificação. Este estudo trata só da primeira; os documentos do G0.1 foram escritos para não antecipar as outras. | VERIFIED (registro, seção 8) |
| 1.5 | O mapeamento passa de fim a meio. Daí decorre que a exaustividade exigida varia por classe de recurso: integral para candidatos a fonte legislativa, delimitada para registros setoriais e fontes auxiliares. | PROPOSED |
| 1.6 | O estudo deixa de ser apenas uma revisão de escopo. A parte de mapeamento segue JBI e PRISMA-ScR; a parte de seleção é avaliação comparativa com teste empírico e precisa de relato próprio. | PROPOSED |
| 1.7 | O subestudo exploratório RIT do protocolo (§14) sai deste estudo. O que permanece é a Dimensão B do quadro de seleção, que mede o que a fonte oferece, não relações regulatórias. | PROPOSED |
| 1.8 | O diagnóstico G0 foi preservado: os cinco documentos têm os mesmos hashes registrados antes desta fase. | VERIFIED |

## 2. Avaliação crítica das 27 emendas

Tabela completa, com razão e destino de cada uma: `G0_1_STRATEGIC_ALIGNMENT.md`, seção 4. Todas as situações são PROPOSED.

| Situação | Qtd. | Emendas |
|---|---|---|
| Mantida | 8 | A11, A12, A14, A18, A24, A25, A26, A27 |
| Ampliada | 6 | A02, A05, A06, A07, A13, A20 |
| Reformulada | 8 | A01, A03, A04, A08, A09, A16, A19, A22 |
| Substituída | 3 | A10, A15, A23 |
| Rebaixada | 2 | A17, A21 |

**As cinco críticas do G0 continuam críticas.** O que muda em cada uma:

| Emenda | No G0 | Agora |
|---|---|---|
| A01 gates | Inverter piloto e congelamento | Quatro congelamentos, cada um antes do dado que governa |
| A02 unidade canônica | Lista de tipos | Taxonomia com níveis, classes, relações e separação da unidade jurídica |
| A03 busca | Tornar as consultas executáveis | Um método por classe; enumeração institucional para candidatos oficiais |
| A04 volume | Teto de triagem | Cobertura proporcional à função da classe na decisão |
| A05 avaliadores | Nomear dois avaliadores e um adjudicador | Mais funções: operadores do benchmark, quem seleciona os atos, quem avalia a Dimensão B |

**Problemas novos**, que o G0 não podia ver:

| ID | Problema | Gravidade | Classe |
|---|---|---|---|
| N01 | Cobertura "suficiente" depende de universo jurídico ainda indefinido | CRÍTICA | VERIFIED (dependência) |
| N02 | Os candidatos podem reduzir-se a uma fonte e seus derivados | CRÍTICA | VERIFIED (inventário); alternativas PENDING VALIDATION |
| N03 | Viés de confirmação a favor do candidato prioritário | ALTA | PROPOSED |
| N04 | Três roteiros de gates e nomes de artefatos divergentes | MÉDIA | VERIFIED |
| N05 | Parte do estudo já não é revisão de escopo | ALTA | PROPOSED |
| N06 | Nível de exaustividade do mapeamento | ALTA | PROPOSED |
| N07 | Registro de decisões em `inputs/` e fora do git | BAIXA | VERIFIED |

## 3. Nova taxonomia operacional

Detalhe: `SOURCE_TAXONOMY_v0_2_DRAFT.md`. Tudo PROPOSED; aplicabilidade PENDING VALIDATION no Piloto A.

**Ideia central.** Das nove categorias pedidas, sete são classes de recurso e duas são **relações** entre registros. "Distribuição de um mesmo recurso" e "duplicado ou sobreposto" não são tipos de coisa; são vínculos. Tratá-los como classes reproduziria a dupla contagem que se quer evitar.

| Níveis | |
|---|---|
| L0 Ocorrência | Linha de descoberta; conta-se como ocorrência |
| K Contêiner | Portal ou catálogo; não entra em denominador |
| L1 Recurso | **Unidade de contagem do inventário** |
| L2 Distribuição | Caminho de acesso a um recurso |
| L3 Unidade jurídica | Ato, versão, dispositivo; **fora do inventário** |

| Classe | Código | Teste decisivo, em resumo |
|---|---|---|
| Fonte primária de legislação | `FPL` | Textos dos atos, mantenedor com atribuição de publicação oficial comprovada, não derivado |
| Repositório jurídico | `REP` | Textos de documentos jurídicos, sem aquela atribuição, sem transformação analítica |
| Dataset jurídico estruturado | `DSE` | Registros com esquema sobre atos, procedimentos ou eventos normativos |
| Infraestrutura de API e dados vinculados | `API` | Modelo de dados próprio e conteúdo relacional exclusivo; caso contrário é distribuição |
| Corpus legislativo derivado | `COD` | Construído por terceiro a partir de outro recurso; origem obrigatória |
| Registro administrativo ou setorial | `REG` | Unidade de observação é entidade, caso ou evento de aplicação |
| Fonte auxiliar de enriquecimento | `AUX` | Vocabulários, identificadores, ontologias |
| Residuais | `FDE`, `IND` | Fora de escopo; indeterminado, com a evidência que falta |

Relações: `duplicate_of`, `distribution_of`, `hosted_by`, `derived_from`, `part_of`, `overlaps_with`, `successor_of`, `uses`.

**Regras que respondem aos pontos pedidos**

| Ponto | Regra |
|---|---|
| Classificação objetiva | Onze perguntas em ordem fixa (R0–R11); a primeira que se aplica decide; cada resposta exige evidência nomeada |
| Mais de uma função | Uma classe primária pela ordem das regras; papéis secundários em campo à parte, nunca usados em contagem; portais são decompostos, não classificados |
| Identificadores canônicos | Opacos e sequenciais, atribuídos só após adjudicação, nunca reutilizados; identificadores externos guardados como informados |
| Duplicado × sobreposto | Duplicado é identidade e some da contagem; sobreposto é interseção entre recursos que continuam distintos |
| Candidato a fonte legislativa | Indicador derivado, não classe: contém texto de atos recuperável por identificador; registros setoriais e auxiliares nunca o recebem |
| Unidade de contagem × unidade jurídica | O inventário não tem linhas de ato. A unidade jurídica tem campos próprios (ato, versão, idioma, formato, subdivisão). Universo, amostra e unidade de codificação ficam para os documentos previstos no registro |

O documento da taxonomia não classifica nenhum dos 41 registros, porque é o instrumento que os avaliadores usarão.

## 4. Quadro comparativo dos critérios de seleção

Detalhe: `SOURCE_SELECTION_FRAMEWORK_v0_1.md`. Tudo PROPOSED. **Nenhuma pontuação foi atribuída e nenhuma fonte foi selecionada.** EUR-Lex/CELLAR é candidato prioritário a testar, sujeito às mesmas regras.

**Unidade avaliada:** configuração candidata = um recurso mais uma distribuição específica.

| | Dimensão A — adequação como fonte legislativa | Dimensão B — affordances para a operacionalização RGAM/V8 |
|---|---|---|
| Pergunta | A fonte entrega o direito de forma completa, autêntica, versionada, identificável, reutilizável e repetível? | O que a fonte acrescenta ao texto que facilite extração rastreável? |
| Eliminatórios | Seis (EA1–EA6), derivados de M1–M6 do registro | Nenhum |
| Comparativos | Doze (A1–A12): cobertura material, temporal e de tipos; proveniência; autenticidade; completude; versionamento; identificadores; formatos; estabilidade; reutilização; reprodutibilidade | Seis (B1–B6): atores; competências; obrigações; delegação; relações; ligação a intermediários |
| Evidência | Documental em G4; empírica em G5, com os mesmos atos em todas as configurações | Esquemas de metadados e teste de endereçamento por dispositivo |
| Registro | Veredito ou descritor com evidência arquivada, data, escopo da inspeção e avaliador | Idem |
| Papel na decisão | Determina | Desempate entre opções não dominadas em A; desenho dos suplementos. Nunca reprova, nunca resgata |
| Quando | Primeiro; trancada com hash | Só depois de A trancada |

**Regra de decisão:** eliminatórios; conjunto não dominado na Dimensão A; trade-offs deliberados e escritos; sem pesos, soma ou ranking; análises de sensibilidade, entre elas a escolha feita **sem** a Dimensão B. Resultado nulo é resultado.

**Um ponto de método que sustenta a separação.** Atores, competências e relações estão no texto do ato, e o texto íntegro de um ato é o mesmo em qualquer fonte. A Dimensão B, portanto, não pode medir "riqueza regulatória": mede estrutura endereçável, metadados e ligações que a fonte oferece. O interesse analítico de um ato pertence à seleção de casos, não à seleção da fonte.

**Condições que desqualificariam o candidato prioritário**, escritas antes do teste e válidas para todos: eliminatório não atendido; impossibilidade de obter original e consolidado como objetos distintos; dois operadores obterem conteúdos diferentes sem explicação; termos de uso incompatíveis com a finalidade; cobertura observada abaixo do limiar em algum estrato.

**O que falta para o quadro funcionar** (PENDING VALIDATION): parâmetros U1–U6 do envelope (tipos de atos, período, idiomas, estados jurídicos, domínios, finalidade de reuso), limiares e exceções. O quadro não os fixa; fixá-los sem conhecer o universo seria arbitrário.

## 5. Estratégia revisada dos pilotos

Detalhe: `G0_1_REVISED_PILOT_DESIGN.md`.

**A amostra de 18 do G0 não é reaproveitável como está** (VERIFIED): calibrava elegibilidade, não classificação; omitia Jurisprudência; sobrerrepresentava P1 (11 de 18); deixava incompletos os pares que testam deduplicação; não tinha nenhum teste com atos.

| | Piloto A — taxonomia de recursos | Piloto B — benchmark de fontes legislativas |
|---|---|---|
| Testa | Regras de nível, classe, relação, candidato e elegibilidade | O protocolo de benchmark: executável por segunda pessoa? medidas bem definidas e aplicáveis a todas as configurações? |
| Amostra | 20 registros do inventário, com reserva de 21 para confirmação | Pequeno conjunto comum de atos; **critérios definidos, seleção não feita** |
| Quem | Dois avaliadores independentes, coordenador que não avalia, adjudicador | Dois operadores independentes com o mesmo procedimento escrito |
| Compara | Tabelas cruzadas por variável, incluindo incerteza | Hash dos arquivos obtidos; observações binárias; contagens |
| Não faz | Não decide elegibilidade definitiva | Não decide qual fonte é melhor |

**Piloto A, composição proposta** (VERIFIED por contagem; adoção PROPOSED): EU01, EU02, EU03, EU06, EU07, EU08, EU09, EU11, EU15, EU17, EU19, EU22, EU24, EU28, EU29, EU33, EU34, EU35, EU39, EU40.

| | Proposto | G0 | Universo |
|---|---|---|---|
| Famílias | 11 de 11 | 10 de 11 | 11 |
| P1 / P2 / P3 | 8 / 10 / 2 | 11 / 5 / 2 | 19 / 19 / 3 |

Treze registros mantidos, cinco retirados (EU05, EU18, EU21, EU25, EU26), sete acrescentados (EU06, EU07, EU09, EU19, EU22, EU24, EU33). Jurisprudência entra com EU22. A lista continua sendo escolha de um agente que viu as colunas de julgamento; por isso o desenho oferece a alternativa de sorteio com restrições e semente registrada.

**Piloto B, critérios de seleção dos atos.** Variação em tipo de ato, período, histórico de alterações, complexidade estrutural, vínculos entre atos, domínio e idioma. São critérios de esforço sobre a fonte, não de interesse analítico. Três subconjuntos relatados em separado: âncoras (atos de que o projeto já tem cópia local), estresse (antigos, muito alterados, revogados) e, opcionalmente, sorteados. A lista é trancada antes de qualquer consulta e não é o universo nem a amostra de casos.

**Regras comuns**

- Agente de IA nunca conta como avaliador, operador ou adjudicador; duas execuções de um agente não são duas avaliações.
- Respostas incertas são legítimas, exigem o motivo e formam categoria própria.
- Indicadores por par nomeado e por variável. **Pares diferentes nunca são combinados.**
- Critérios de passagem (PA1–PA8, PB1–PB9) combinam integridade do procedimento, causa atribuída a cada divergência, decisão sobre cada regra e rodada de confirmação. Um valor numérico funciona só como alerta que obriga a rever; atingi-lo não dispensa as demais condições.
- Os critérios são aprovados pela coordenação científica, com data anterior à entrega do primeiro pacote.

## 6. Alterações metodológicas indispensáveis

Especificações com verificação: `G0_1_STRATEGIC_ALIGNMENT.md`, Parte II. Todas PROPOSED; nenhuma implementada.

| # | Alteração | Especificação |
|---|---|---|
| 6.1 | Quatro congelamentos escalonados (taxonomia; busca; quadro de seleção e parâmetros; atos de referência), cada um com etiqueta, manifesto de hashes e aprovação | S-A01 |
| 6.2 | Taxonomia com níveis, classes, relações e separação da unidade jurídica | S-A02 |
| 6.3 | Busca por classe: enumeração institucional para candidatos oficiais; busca dirigida e consulta a especialistas para alternativas; busca bibliográfica para derivados | S-A03 |
| 6.4 | Cobertura proporcional por classe; regra de volume escrita depois da medição e antes da execução | S-A04 |
| 6.5 | Matriz de funções com nomes, declaração de exposição prévia, limites do uso de IA | S-A05 |
| 6.6 | Pacotes cegos gerados por programa; lista de documentos reservados; formulários da Dimensão A sem vocabulário do quadro teórico | S-A07 |
| 6.7 | Separação A/B com ordem, tranca e escolha "sem B" no parecer | S-A08 |
| 6.8 | Envelope provisório do universo antes da avaliação | Quadro, seção 2 |
| 6.9 | Declaração do número de mantenedores independentes entre os candidatos, e nome do estudo coerente com o que foi comparado | Quadro, seção 7 |
| 6.10 | Validação de vocabulários no verificador, com fonte única e verificação somente leitura | SPEC-V, seis testes de aceitação |
| 6.11 | Concordância por par nomeado, com incerteza contada | SPEC-K, seis testes de aceitação |
| 6.12 | Documentos de gate em pasta rastreada, copiados byte a byte, com manifesto | S-VER |

**Defeitos técnicos.** Os dois permanecem no código (VERIFIED: `scripts/cli.py` com o mesmo hash). Não afetam o Piloto A, que é manual, mas precisam estar corrigidos e testados antes de qualquer dado de triagem ser lido pelo programa.

**Versionamento.** Seis documentos de gate em `outputs/` estão fora do git por força do `.gitignore`; quatro em `protocol/` e o registro em `inputs/` estão apenas não rastreados (VERIFIED). A opção recomendada é uma pasta `gates/` rastreada com cópias conferidas por hash, sem tocar no `.gitignore`. Os hashes de referência dos relatórios do G0 estão registrados no documento de alinhamento, seção 14.

## 7. Riscos residuais

Riscos que as salvaguardas reduzem mas não eliminam.

| # | Risco | Por que permanece | Classe |
|---|---|---|---|
| 7.1 | Comparação com um candidato só | Depende do que existe no mundo, não do desenho. O desenho garante apenas que isso seja declarado | PENDING VALIDATION |
| 7.2 | Envelope do universo ajustado depois | Se o universo final sair do envelope, a cobertura é reavaliada; a tentação de ajustar ao resultado existe | PROPOSED (controle: data e análise de sensibilidade) |
| 7.3 | Equipe pequena | Com poucas pessoas, quem construiu o inventário pode ter de avaliar; a independência fica parcial e precisa ser declarada | PENDING VALIDATION |
| 7.4 | Preferência prévia pelo candidato prioritário | Pré-especificação limita, mas a deliberação sobre trade-offs é humana | PROPOSED |
| 7.5 | Fontes mudam durante o estudo | Entre G4 e G5 um serviço pode mudar de versão ou de termos; os resultados valem para as datas registradas | PROPOSED |
| 7.6 | Ausência de texto de referência independente | Se a única via para o texto oficial for a fonte em teste, mede-se consistência, não integridade | PENDING VALIDATION |
| 7.7 | Instrumentos originais | Taxonomia e quadro de seleção são novos e não validados fora deste projeto | VERIFIED (fato); mitigação PROPOSED |
| 7.8 | Âncoras já conhecidas | Atos com que o projeto já trabalhou podem favorecer a fonte de onde vieram | PROPOSED (controle: relato separado) |
| 7.9 | Termos de uso | Podem restringir o depósito de textos obtidos e limitar o pacote de replicação a manifestos e código | PENDING VALIDATION |
| 7.10 | Pasta sincronizada | Edição concorrente de tabelas em unidade de nuvem; não resolvido | VERIFIED |
| 7.11 | Estes documentos como âncora | Os relatórios G0 e G0.1 contêm julgamentos sobre registros; se chegarem aos avaliadores, o cegamento cai | PROPOSED (controle: lista de documentos reservados) |

## 8. Decisões pendentes de aprovação humana

Nenhuma foi tomada, presumida ou simulada.

**Sobre a reorientação**

1. A equipe (David e colaboradores) adota a finalidade registrada pelo proponente?
2. As cinco perguntas de pesquisa do registro são aceitas? A RQ3 é reescrita para não trazer a Dimensão B para dentro de um requisito mínimo?
3. O subestudo exploratório RIT sai deste estudo?
4. Qual numeração de gates é a normativa, e com que nomes de artefatos?

**Sobre o desenho**

5. Decisão registrada para cada uma das 27 emendas, na situação proposta ou em outra, e para N01–N07.
6. A taxonomia v0.2 vai ao Piloto A como está?
7. O quadro de seleção e sua regra de decisão são aceitos como base de trabalho?
8. As condições de desqualificação do candidato prioritário são aceitas?
9. O componente nacional sai do escopo?

**Sobre o universo — a decidir com David e a equipe**

10. Parâmetros U1–U6: tipos de atos, período, idiomas, estados jurídicos, domínios, finalidade de reuso.
11. Limiares e exceções dos requisitos eliminatórios.

**Sobre os pilotos**

12. Lista intencional do Piloto A ou sorteio com restrições.
13. Critérios de passagem; valores de alerta; tamanho da rodada de confirmação.
14. Número de atos de referência; uso de âncoras e de sorteados; quem seleciona; o que conta como texto de referência.
15. Piloto B tardio ou antecipado; autorização para consultar fontes externas.

**Sobre pessoas**

16. Coordenador, avaliadores, operadores, adjudicador, avaliador da Dimensão B.
17. Quem construiu o inventário pode avaliar? Haverá avaliador externo ao projeto?

**Sobre o repositório**

18. Solução de versionamento dos documentos de gate; local do registro de decisões.
19. Autorização para commit dos documentos do G0 e do G0.1 e para publicação no remoto.
20. Autorização para implementar SPEC-V e SPEC-K.

## 9. Condições para iniciar G1

Todas PROPOSED.

| # | Condição | Estado hoje |
|---|---|---|
| C1 | Reorientação adotada pela equipe, ou autorização expressa para prosseguir com o Piloto A enquanto ela é discutida | Pendente |
| C2 | Revisão científica dos cinco documentos do G0.1 | Pendente |
| C3 | Taxonomia aprovada para ir a piloto | Proposta entregue |
| C4 | Funções nomeadas; declarações de exposição arquivadas | Pendente |
| C5 | Amostra do Piloto A decidida | Duas opções entregues |
| C6 | Critérios de passagem aprovados e datados | Proposta entregue |
| C7 | Documentos de gate versionados | Especificação entregue; não executado |
| C8 | Meio de captura de evidência definido | Pendente |
| C9 | Gerador de pacote cego e formulário prontos | Não iniciado |

**O que G1 não precisa esperar:** os parâmetros do universo, a estratégia de busca executável, as correções de código e a seleção dos atos de referência. Esses itens bloqueiam G2, G4 e G5, não o Piloto A. Como a definição do universo é o item de maior risco de atraso, convém abrir essa discussão em paralelo ao G1.

## 10. Potencial de contribuição científica e publicabilidade

Avaliação PROPOSED. **Nenhuma busca de literatura foi feita nesta fase**; toda afirmação sobre originalidade é PENDING VALIDATION até que alguém verifique o que já existe.

**O produto garantido** é interno: um parecer de seleção de fonte, reproduzível, que alimenta a seção de fontes de dados do projeto principal. Tem valor mesmo se confirmar a hipótese inicial, porque substitui uma escolha por conveniência por uma escolha documentada.

**Contribuições que poderiam sustentar publicação autônoma**

| Contribuição | Depende de | Avaliação |
|---|---|---|
| Evidência empírica de perdas e inconsistências entre a fonte oficial, suas distribuições e os corpora derivados usados em pesquisa (versões, completude, estrutura, metadados) | O benchmark encontrar diferenças documentáveis | A mais promissora, se for verdade que corpora derivados costumam ser usados sem verificação do que perderam em relação à fonte (premissa PENDING VALIDATION). Se as diferenças forem pequenas, o resultado ainda é informativo, mas menos publicável |
| Método reutilizável para justificar a escolha de fonte em pesquisa jurídica empírica: taxonomia, eliminatórios, duas dimensões separadas, regra de decisão sem pesos | Os instrumentos sobreviverem aos pilotos; alguém fora do projeto conseguir aplicá-los | Plausível como artigo de método; mais forte com aplicação por um segundo grupo ou a um segundo ordenamento |
| Inventário classificado de recursos de dados sobre legislação da UE, com relações de distribuição e derivação | Busca e triagem executadas como descritas | Útil como dado depositado; sozinho, dificilmente sustenta um artigo, sobretudo com cobertura deliberadamente desigual entre classes |
| Demonstração de como separar adequação da fonte de conveniência para o quadro teórico | Execução fiel da separação A/B | Reforça as demais; não é contribuição isolada |

**O que enfraquece a publicabilidade**

1. **Candidato único** (N02). Um artigo intitulado como comparação de fontes que compara uma fonte consigo mesma não passa por revisão. O enquadramento honesto, nesse caso, é "auditoria de uma infraestrutura oficial e de seus derivados".
2. **Mapeamento de cobertura desigual.** Uma revisão de escopo declarada como tal precisa de busca abrangente; a reorientação reduz isso de propósito. O artigo não deve se apresentar como revisão de escopo geral do campo.
3. **Instrumentos originais não validados.** Limitação a declarar.
4. **Possível trabalho anterior.** Não verificado.

**Recomendação.** Manter a decisão D10 do registro: a publicação autônoma decide-se em G6, com os resultados à vista. Até lá, três cuidados baratos preservam a opção: registrar publicamente o desenho antes de G4; manter os registros de execução completos desde o Piloto A; verificar a literatura existente antes de G2.

---

## Registro de integridade desta fase

| Item | Estado |
|---|---|
| Buscas sistemáticas, coleta, triagem formal, consulta a fonte externa | Nenhuma |
| Protocolo original, codebook, scripts, dados, inventário | Inalterados; 34 arquivos com o hash do início do G0 |
| Cinco documentos do G0 | Inalterados; hashes conferidos |
| Operacionalização RGAM/V8 e demais subprojetos | Não tocados |
| Decisões humanas, resultados, fontes ou evidências | Nenhum inventado |
| Commit ou publicação remota | Nenhum |
| Arquivos criados | Os cinco listados no início |
| Gate | Execução encerrada no G0.1; aguarda revisão científica |
