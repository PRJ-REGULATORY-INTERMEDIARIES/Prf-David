# QUADRO DE SELEÇÃO DA FONTE LEGISLATIVA — v0.1

**Data:** 2026-10-09 | **Gate:** G0.1 | **Estado:** PROPOSED — não aprovado, não congelado. Nenhuma fonte foi avaliada, pontuada ou escolhida.

**Critério central.** A escolha da fonte legislativa decorre de evidência documentada sobre sua adequação ao universo jurídico de interesse, e não de sua aparente compatibilidade com o quadro teórico que será aplicado depois.

**Situação de EUR-Lex/CELLAR.** Candidato prioritário **a testar** (decisão D05 do registro v1.1). Entra no quadro em igualdade de condições, passa pelos mesmos requisitos e pelos mesmos atos de referência que qualquer outro candidato, e a seção 7 fixa de antemão o que o desqualificaria.

## 1. O que é avaliado

**Unidade de avaliação:** a *configuração candidata* — um recurso com `legislative_candidate = sim` mais uma distribuição específica dele (definições em `SOURCE_TAXONOMY_v0_2_DRAFT.md`, seções 6 e 10). Duas distribuições do mesmo recurso são duas configurações.

**Conjunto de candidatos:** todas as configurações que saírem do inventário adjudicado (G3) com o indicador de candidato. O conjunto não é escolhido por conveniência nem por expectativa de desempenho. Registros administrativos e fontes auxiliares não concorrem (decisão D09); são avaliados em matriz própria, como enriquecimento (seção 5.4).

**Resultado admitido:** uma configuração, ou uma arquitetura híbrida com várias, desde que o parecer identifique o sistema de registro, a precedência em caso de conflito e a origem de cada campo (registro v1.1, seção 5).

## 2. Parâmetros que precisam existir antes da avaliação

Vários critérios perguntam "cobertura suficiente **de quê**?". A resposta vem da definição do universo jurídico, que é decisão separada e ainda não tomada (registro v1.1, seções 8 e 11). O quadro é, por isso, **paramétrico**: a equipe fornece um *envelope provisório* do universo, e a avaliação é feita contra ele.

| Parâmetro | Conteúdo | Quem define | Estado |
|---|---|---|---|
| U1 | Tipos de atos de interesse | Coordenação científica | PENDING VALIDATION |
| U2 | Período (data inicial e final) | Coordenação científica | PENDING VALIDATION |
| U3 | Idiomas necessários | Coordenação científica | PENDING VALIDATION |
| U4 | Estados jurídicos necessários (em vigor, revogados, versões históricas) | Coordenação científica | PENDING VALIDATION |
| U5 | Domínios materiais, se houver recorte | Coordenação científica | PENDING VALIDATION |
| U6 | Finalidade de reuso (análise interna; redistribuição de textos; depósito público de derivados) | Equipe | PENDING VALIDATION |

O envelope é declaradamente provisório e mais largo que o universo final. Se o universo for depois definido fora do envelope, a avaliação de cobertura é refeita; o restante permanece.

**Sem U1–U6 registrados, a Etapa 1 não começa.** Avaliar cobertura sem dizer contra o quê permitiria ajustar a definição ao candidato preferido.

## 3. Estrutura da decisão

| Etapa | O que faz | Regra | Gate |
|---|---|---|---|
| 0 | Parâmetros U1–U6 e este quadro são congelados | Antes de olhar qualquer candidato | G4, entrada |
| 1 | Requisitos eliminatórios (Dimensão A) | Atende / não atende / pendente; pendente não passa | G4 e G5 |
| 2 | Critérios comparativos (Dimensão A), por documentação | Descritores com evidência; sem soma | G4 |
| 3 | Teste empírico com atos de referência (Dimensão A) | Observações registradas; sem soma | G5 |
| 4 | Dimensão A trancada (hash e data) | Só então a Dimensão B é aberta | G5 |
| 5 | Affordances analíticas (Dimensão B) | Matriz separada | G5 |
| 6 | Deliberação humana e parecer | Regra da seção 6 | G5, saída |

Não há pontuação agregada, não há pesos, não há ranking. O produto é uma matriz de evidências por critério e um parecer que explicita os trade-offs.

## 4. DIMENSÃO A — adequação como fonte legislativa

### 4.1 Requisitos eliminatórios

Reformulam os requisitos M1–M6 do registro v1.1 em forma testável. Veredito por requisito: `ATENDE`, `NÃO ATENDE` ou `PENDENTE`. **`PENDENTE` nunca equivale a aprovado**: a configuração só segue adiante quando todos os requisitos avaliáveis no gate estão em `ATENDE`.

| ID | Requisito | Pergunta testável | Evidência mínima | Avaliável em |
|---|---|---|---|---|
| EA1 | Proveniência verificável (M1) | A origem de cada texto é identificável até a publicação oficial? | Documentação do mantenedor que descreva a cadeia de origem; para derivados, declaração da fonte e da data de extração | G4 |
| EA2 | Identificação persistente do ato (M2) | Cada ato tem identificador estável, documentado, que permita recuperá-lo de novo? | Documentação do esquema de identificação; resolução do identificador para os atos de referência | G4 (documento), G5 (teste) |
| EA3 | Acesso lícito e repetível (M3) | Os termos permitem o reuso definido em U6, e o acesso pode ser repetido por terceiro seguindo instruções escritas? | Texto dos termos de uso ou licença, com data; execução repetida por segundo operador | G4 (termos), G5 (repetição) |
| EA4 | Cobertura do envelope (M4) | A fonte declara cobrir os tipos de atos U1 no período U2, com as lacunas explicitadas? | Declaração de cobertura da fonte; no teste, presença dos atos de referência de cada estrato | G4 (declarada), G5 (observada) |
| EA5 | Temporalidade jurídica distinguível (M5) | Texto original, alterações, revogações e versões consolidadas são distinguíveis e datados? | Documentação do modelo de versões; no teste, obtenção separada de original e consolidado para atos alterados | G4 (documento), G5 (teste) |
| EA6 | Integridade do texto e da estrutura (M6) | O texto obtido é completo e preserva artigos, anexos e referências? | Só por teste: comparação com o texto de referência, segundo o protocolo do benchmark | G5 |

**Limiares e exceções.** Onde um requisito admite grau (por exemplo, "cobertura suficiente" em EA4 ou "completo" em EA6), o limiar é um **parâmetro a fixar pela equipe antes da Etapa 1** e registrado junto com U1–U6. Este documento não o fixa: escolher um número agora, sem conhecer o universo, seria arbitrário. Exceções admitidas (por exemplo, falha de cobertura sanável por configuração híbrida) também são escritas antes.

**Reprovação não exclui do inventário.** Uma configuração que não atende a um eliminatório continua no mapa de recursos, com o motivo registrado. Deixa apenas de concorrer a fonte operacional.

### 4.2 Critérios comparativos

Aplicados às configurações que passaram, ou ainda podem passar, pelos eliminatórios. Cada critério tem um indicador documental (G4) e, quando cabe, um indicador empírico (G5). O registro é um **descritor com evidência**, na escala já usada pelo codebook: `2` explícito e verificado, `1` parcial ou indireto, `0` ausente após inspeção suficiente, `UNVERIFIED`, `NA`. A escala serve para leitura da matriz, **não para soma**.

| ID | Critério | Nível | Indicador documental (G4) | Indicador empírico (G5) |
|---|---|---|---|---|
| A1 | Cobertura material | Recurso | Domínios e setores declarados; exclusões declaradas | Atos de referência de cada domínio encontrados / procurados |
| A2 | Cobertura temporal | Recurso | Data do ato mais antigo e mais recente declarados; periodicidade de atualização | Atos de referência de cada período encontrados / procurados |
| A3 | Tipos de atos | Recurso | Tipos declarados, comparados com U1 | Atos de referência de cada tipo encontrados / procurados |
| A4 | Proveniência | Recurso | Cadeia de origem documentada; para derivados, data e método de extração | Metadados de proveniência presentes em cada item obtido |
| A5 | Autenticidade | Recurso | Estatuto jurídico declarado do texto servido (autêntico, oficial sem valor autêntico, cópia informativa) e mecanismo de verificação oferecido | Mecanismo de verificação funciona nos atos de referência |
| A6 | Completude | Recurso e distribuição | Lacunas conhecidas declaradas pelo mantenedor | Partes do ato presentes / esperadas (artigos, considerandos, anexos, tabelas) |
| A7 | Versionamento | Recurso | Modelo de versões documentado: original, consolidações, retificações, vínculos de alteração | Versões obtidas / versões que a referência indica existirem; original e consolidado obtidos como objetos distintos |
| A8 | Identificadores persistentes | Recurso | Esquemas suportados; nível de granularidade (ato, versão, subdivisão) | Identificadores dos atos de referência resolvidos / tentados; estabilidade entre duas execuções |
| A9 | Formatos | Distribuição | Formatos oferecidos; existência de marcação estrutural documentada | Estrutura do ato recuperável por máquina sem heurística textual (sim / parcial / não), por ato |
| A10 | Estabilidade de acesso | Distribuição | Política de versões do serviço, de descontinuação e de limites; histórico de mudanças declarado | Falhas, limites e diferenças observados entre execuções em datas distintas |
| A11 | Condições de reutilização | Recurso e distribuição | Licença ou aviso legal aplicável; restrições; exigência de conta ou contrato | — (documental) |
| A12 | Reprodutibilidade | Distribuição | O acesso pode ser descrito como procedimento determinístico (consulta, parâmetros, versão) | Dois operadores, mesmo procedimento: arquivos com o mesmo hash, ou diferença explicada |

**Regras de registro**

- Cada célula da matriz tem: descritor, referência da evidência, data, captura arquivada com hash e avaliador identificado.
- `0` só após a inspeção mínima definida para o critério (onde se procurou e o que não se achou). Desconhecido é `UNVERIFIED`.
- Indicadores empíricos são registrados como **contagens observadas** (por exemplo, "11 de 14 atos"), não convertidos em nota.
- Um critério em que todas as configurações recebem o mesmo descritor é mantido na matriz e relatado como não discriminante.

### 4.3 O que a Dimensão A deliberadamente não mede

Facilidade de extrair atores, competências ou relações; riqueza de metadados sobre instituições; qualquer propriedade definida em termos do quadro teórico do projeto. Tudo isso está na Dimensão B.

## 5. DIMENSÃO B — affordances analíticas para a operacionalização RGAM/V8

### 5.1 O que esta dimensão pode e não pode medir

Atores, competências, obrigações, mecanismos de delegação e relações regulatórias estão **no texto do ato**. O texto de um mesmo ato é, em princípio, o mesmo em qualquer fonte íntegra. Logo, a diferença entre fontes nesta dimensão não está no conteúdo normativo, e sim no que a fonte **acrescenta ou preserva** em torno dele:

1. granularidade estrutural endereçável (é possível citar e recuperar um artigo, número ou alínea de forma estável?);
2. metadados estruturados sobre o ato (autor, base jurídica, destinatários, relações com outros atos);
3. ligações explícitas a entidades ou vocabulários externos.

A Dimensão B mede essas três coisas. **Não mede** quantos intermediários um ato menciona, nem quão "rico" ele é para a análise: isso é propriedade do ato e pertence à seleção de casos, não à seleção da fonte.

### 5.2 Critérios

Âncoras escritas como propriedades observáveis do dado, de modo que um avaliador sem familiaridade com o quadro teórico chegue ao mesmo registro.

| ID | Affordance | Pergunta observável | Evidência |
|---|---|---|---|
| B1 | Atores | Há campo estruturado que identifique instituições ou órgãos ligados ao ato (autor, destinatário, órgão mencionado)? Com identificador controlado? | Esquema de metadados; amostra de registros dos atos de referência |
| B2 | Competências | O texto é endereçável no nível do dispositivo, permitindo ancorar uma competência num artigo específico e recuperá-lo de novo? | Documentação da marcação; teste de recuperação por subdivisão |
| B3 | Obrigações | Idem a B2, para dispositivos que impõem obrigações; a fonte distingue estruturalmente parte dispositiva, considerandos e anexos? | Idem |
| B4 | Mecanismos de delegação | Há metadado estruturado que ligue o ato de base aos atos delegados e de execução, e vice-versa? | Esquema de relações; teste nos atos de referência que os tenham |
| B5 | Relações regulatórias | Há relações entre atos como dado estruturado (altera, revoga, baseia-se em, executa)? As relações entre **entidades** estão representadas, ou só entre documentos? | Esquema de relações; amostra |
| B6 | Intermediários | A fonte permite ligar um dispositivo a um registro externo de entidades (por identificador do ato ou do artigo)? | Existência de chave de ligação; não se avalia aqui o registro externo |

Registro na mesma escala descritiva da seção 4.2, com as mesmas regras de evidência. Sem soma.

### 5.3 Regras de separação entre as dimensões

1. **Ordem.** A Dimensão B só é aberta depois que a matriz da Dimensão A estiver completa e trancada (hash e data registrados).
2. **Sem eliminatórios em B.** Nenhum critério B reprova uma configuração.
3. **Sem resgate.** Nenhum resultado B reabilita uma configuração reprovada em A.
4. **Uso restrito.** B entra na decisão apenas (a) como desempate entre configurações não dominadas em A, com o trade-off escrito, e (b) para desenhar a combinação com fontes de enriquecimento.
5. **Decisão sem B.** O parecer apresenta obrigatoriamente qual seria a escolha considerando apenas a Dimensão A. Se a escolha final for diferente, a diferença é justificada por escrito.
6. **Avaliadores.** Sempre que a equipe permitir, B é avaliada por pessoa diferente da que avaliou A, ou ao menos sem acesso ao parecer preliminar.
7. **Linguagem.** Os formulários de A não mencionam RGAM, V8, RIT ou intermediários.

### 5.4 Fontes de enriquecimento

Recursos `REG` e `AUX` são descritos em matriz própria, com três perguntas: a que atos ou dispositivos podem ser ligados; por qual chave; com que cobertura declarada. Não recebem veredito de adequação como fonte legislativa e não aparecem na matriz da Dimensão A.

## 6. Regra de decisão

Aplicada por pessoas, em reunião registrada, depois das Etapas 1 a 5.

1. **Eliminatórios.** Saem as configurações com algum `NÃO ATENDE`. Configurações com `PENDENTE` não podem ser escolhidas; ou a pendência é resolvida, ou a configuração fica fora.
2. **Dominância.** Entre as restantes, identifica-se o conjunto não dominado: uma configuração é dominada se outra for igual ou melhor em todos os critérios A e estritamente melhor em pelo menos um. `UNVERIFIED` não conta como melhor nem como pior; impede a afirmação de dominância naquele critério.
3. **Trade-offs.** Se o conjunto não dominado tiver mais de um elemento, a escolha é deliberada. O parecer nomeia os critérios em conflito, a opção feita e a razão. Não se introduzem pesos depois de conhecidos os resultados.
4. **Híbridos.** Uma combinação é admissível se cada componente passar nos eliminatórios para a parte que fornece, e se o parecer fixar a precedência em caso de conflito.
5. **Sensibilidade.** O parecer mostra se a escolha muda (a) sem a Dimensão B; (b) tratando cada `UNVERIFIED` como o pior caso; (c) com e sem os atos de referência já conhecidos do projeto; (d) se um parâmetro U1–U6 for alterado dentro de uma faixa plausível.
6. **Resultado nulo é resultado.** Se nenhuma configuração passar, ou se as configurações forem indistinguíveis, o parecer diz isso.

## 7. Salvaguardas contra viés de confirmação

| Risco | Controle | Como se verifica |
|---|---|---|
| Critérios ajustados ao candidato preferido | Quadro, parâmetros e limiares congelados antes de qualquer avaliação | Data do congelamento anterior à primeira linha de evidência |
| Alternativas avaliadas com menos cuidado | Mesmo formulário, mesmos atos, mesmo esforço mínimo de inspeção por configuração | Registro de tempo e de itens inspecionados por configuração |
| Só há um candidato real | O relatório declara quantas configurações independentes existiam, e não apresenta como comparação o que foi verificação de uma fonte única | Contagem de mantenedores distintos entre os candidatos |
| Falhas do candidato prioritário relevadas | Condições de desqualificação escritas de antemão (abaixo) | Parecer responde a cada uma |
| Dimensão B contamina A | Regras da seção 5.3 | Hash da matriz A anterior à primeira linha de B |
| Avaliadores ancorados | Avaliadores não recebem o registro de decisões v1.1 (seção 5), nem as colunas de julgamento do inventário, nem os relatórios G0 e G0.1 | Declaração de exposição prévia |

**Condições que desqualificariam o candidato prioritário**, fixadas antes do teste. Valem igualmente para qualquer outro candidato:

1. algum requisito eliminatório em `NÃO ATENDE` após teste;
2. impossibilidade de obter separadamente texto original e versão consolidada de atos alterados;
3. dois operadores, seguindo o mesmo procedimento escrito, obterem conteúdos diferentes sem explicação documentada;
4. termos de uso incompatíveis com a finalidade U6;
5. cobertura observada inferior ao limiar fixado em algum estrato do envelope.

## 8. Padrão de evidência

Um julgamento só entra na matriz com:

| Campo | Conteúdo |
|---|---|
| `config_id` | Recurso e distribuição |
| `criterion` | EA1–EA6, A1–A12, B1–B6 |
| `descriptor` | Veredito ou descritor |
| `evidence_type` | documental / teste |
| `evidence_ref` | URL e trecho, ou identificador da execução do teste |
| `accessed_at`, `snapshot_sha256` | Data e captura arquivada |
| `inspection_scope` | Onde se procurou (obrigatório para `0` e `NÃO ATENDE`) |
| `reviewer` | Pessoa identificada |
| `notes` | Limitações |

Texto gerado por modelo de linguagem não é evidência. Um agente pode localizar documentação e preparar capturas; o descritor é atribuído por pessoa que leu a fonte.

## 9. Correspondência com o codebook atual e com FAIR

Para registro histórico; o codebook não foi alterado.

| Critério do CODEBOOK | Destino neste quadro | Princípio FAIR mais próximo |
|---|---|---|
| `LEGAL_ID` | EA2, A8 | F1 |
| `TEMPORALITY` | EA5, A7 | — |
| `MACHINE_ACCESS` | A9, A10, A12 | A1 |
| `PROVENANCE` | EA1, A4 | R1.2 |
| `REUSE_RIGHTS` | EA3, A11 | R1.1 |
| `ACTORS` | B1 | — |
| `FUNCTIONS` | B2, B3 | — |
| `RELATIONS` | B4, B5, B6 | — |
| `LEGAL_BASIS` | B2 (ancoragem no dispositivo), B5 (relação com ato de base) | — |
| — (novo) | A1, A2, A3 cobertura; A5 autenticidade; A6 completude | — |
| Tipologia D0–D3 | Não usada na seleção da fonte; permanece, se a equipe quiser, como descrição do inventário | — |

A correspondência com FAIR é aproximada e precisa ser conferida contra o texto de Wilkinson et al. (2016) antes de publicada: PENDING VALIDATION.

## 10. Produto: estrutura do parecer de seleção

*Source Selection Decision Memo* (nome usado no registro v1.1), a ser redigido em G5:

1. Parâmetros U1–U6 e limiares, com a data em que foram fixados.
2. Conjunto de candidatos e como foi obtido; número de mantenedores independentes.
3. Tabela de eliminatórios, por configuração.
4. Matriz da Dimensão A, com evidência por célula.
5. Resultados do teste empírico, por ato e por configuração.
6. Conjunto não dominado e trade-offs.
7. Escolha considerando apenas a Dimensão A.
8. Matriz da Dimensão B e seu efeito, se houver.
9. Análises de sensibilidade.
10. Decisão: fonte principal, suplementos, exclusões, precedência.
11. Limitações e condições de revisão da decisão.
12. Assinaturas e data.

## 11. Estatuto das afirmações

| Afirmação | Classe |
|---|---|
| Os requisitos EA1–EA6 derivam de M1–M6 do registro v1.1 | VERIFIED |
| Os critérios A1–A12 cobrem os doze aspectos pedidos no G0.1 para a Dimensão A | VERIFIED (por construção) |
| Os critérios B1–B6 cobrem os seis aspectos pedidos para a Dimensão B | VERIFIED (por construção) |
| Os critérios são aplicáveis e discriminam entre candidatos reais | PENDING VALIDATION (Piloto B e G4) |
| Parâmetros U1–U6, limiares e exceções | PENDING VALIDATION (equipe) |
| Existe mais de um candidato independente a comparar | PENDING VALIDATION (G2–G3) |
| Adoção do quadro e da regra de decisão | PROPOSED |
| Qualquer veredito sobre qualquer fonte | Inexistente — nenhuma fonte foi avaliada |
