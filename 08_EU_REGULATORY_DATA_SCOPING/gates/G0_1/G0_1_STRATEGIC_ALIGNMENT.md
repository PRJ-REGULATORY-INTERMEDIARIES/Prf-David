# G0.1 — ALINHAMENTO ESTRATÉGICO

**Data:** 2026-10-09 | **Gate:** G0.1 | **Estado:** PROPOSED — documento de revisão; não altera o protocolo, não o congela, não aplica emendas.
**Elaboração:** agente de programação (Claude Code), sob coordenação humana.

Este documento reúne três partes do G0.1 que não têm arquivo próprio: a revisão das 27 emendas (Parte I), as especificações de salvaguarda (Parte II) e o roteiro revisado (Parte III).

**Classificação das conclusões:** VERIFIED (observado em arquivo ou saída de comando) · PROPOSED (recomendação; depende de decisão humana) · PENDING VALIDATION (depende de fato, teste ou aprovação ainda inexistentes).

---

## PARTE I — REVISÃO E ALINHAMENTO

### 1. Base documental

| Documento | Situação | Classe |
|---|---|---|
| `outputs/BASELINE_RUN.md`, `outputs/G0_REVIEW_NOTE.md`, `outputs/PILOT_CALIBRATION_PLAN.md`, `outputs/EXECUTION_PLAN.md`, `protocol/PROPOSED_AMENDMENTS.md` | Lidos na íntegra; inalterados nesta fase (hashes na seção 14) | VERIFIED |
| `protocol/PROTOCOL_v1_0_DRAFT.md`, `protocol/CODEBOOK_AND_AUDIT.md`, `README.md`, `inputs/seed_inventory_v0_1.csv` e demais arquivos originais | Lidos na íntegra; os 34 arquivos originais mantêm o SHA-256 do início do G0 | VERIFIED |
| `inputs/REGISTRO_DECISOES_EU_REGULATORY_DATA_SCOPING_v1_1_2026-10-09.docx` | **Disponível e lido na íntegra.** Arquivo novo, não rastreado pelo git. SHA-256 `1197d299…f99c812a` | VERIFIED |

**Estatuto do registro de decisões.** O próprio documento se declara "registro interno, sujeito à revisão científica", com "diretrizes registradas pelo proponente" que "dependem de análise G0/G0.1 e, quando cabível, concordância de David e da equipe", e afirma que "não equivale à aprovação formal de David, Rotem ou demais colaboradores". Portanto: a reorientação é uma decisão **do proponente**, VERIFIED como registro; sua adoção pela equipe é PENDING VALIDATION. Este documento a toma como premissa de trabalho, não como fato aprovado.

### 2. O que a reorientação muda

| | Protocolo v1.0 DRAFT | Depois da decisão D01 |
|---|---|---|
| Finalidade principal | Mapear recursos de dados sobre legislação e governança da UE | Justificar a escolha da fonte legislativa do dataset RGAM/V8 |
| Papel do mapeamento | Fim em si | Meio: identifica e caracteriza as alternativas |
| Produto principal | Artigo de revisão de escopo | Parecer de seleção de fonte, documentado e reproduzível |
| Publicação autônoma | Objetivo | Possibilidade, condicionada aos resultados (D10) |
| Objeto da avaliação | Todos os datasets incluídos, por nove critérios | Duas camadas: (A) inventário de recursos; (B) configurações candidatas a fonte legislativa |
| Registros setoriais | Avaliados como os demais | Enriquecimento; não concorrem como fonte (D09) |
| Subestudo RIT | Prova de conceito com 3–5 casos | Sai deste estudo como subestudo; o que resta é a Dimensão B do quadro de seleção |

**O que não muda** (VERIFIED no registro): os 41 recursos continuam sendo apenas seeds (D04); os quatro níveis de identidade do protocolo são conservados (seção 4.2 do registro); julgamento humano independente e adjudicação documentada (D08); `UNVERIFIED` nunca vale como aprovado.

**As quatro decisões que o registro manda manter separadas** (seção 8): escolha da fonte; definição do universo jurídico; seleção de casos; codificação RGAM/V8. Este estudo responde só à primeira. Todos os documentos do G0.1 foram escritos para não antecipar as outras três.

### 3. Problemas novos, criados pela reorientação

O G0 não podia tê-los visto. São acrescentados às 27 emendas, com numeração própria.

| ID | Problema | Gravidade | Classe | Tratamento |
|---|---|---|---|---|
| N01 | **A avaliação de cobertura depende de um universo jurídico ainda não definido.** O requisito M4 do registro pede "cobertura suficiente dos tipos de atos e períodos definidos pelo desenho teórico"; a delimitação de normas e do recorte temporal está "pendente de discussão científica com David e equipe". Sem ela, "suficiente" não tem referente, e o critério pode ser ajustado ao candidato. | CRÍTICA | VERIFIED (dependência no texto) | Envelope provisório U1–U6, fixado antes da avaliação (quadro de seleção, seção 2) |
| N02 | **O conjunto de candidatos pode ser, na prática, uma fonte só.** No inventário exploratório, os quatro registros da família "Corpus normativo" aparecem como portal, grafo, arquivo em lote e coleção XML, e seus nomes e URLs remetem todos a EUR-Lex e ao Serviço das Publicações; e os nomes e ressalvas de vários corpora acadêmicos indicam derivação desse mesmo acervo. Se a busca não encontrar alternativa de mantenedor independente, não haverá *comparação de fontes*, e sim *verificação de uma fonte e comparação de suas distribuições e derivados*. | CRÍTICA | VERIFIED (descrições do inventário); existência de alternativas PENDING VALIDATION | A busca de G2 procura ativamente alternativas independentes; o relatório declara o número de mantenedores independentes; o estudo é nomeado conforme o que de fato comparou |
| N03 | **Viés de confirmação a favor do candidato prioritário.** A hipótese D05 é declarada; o risco é que critérios, esforço de inspeção e leitura dos resultados a favoreçam. | ALTA | PROPOSED | Condições de desqualificação escritas antes; mesmo formulário e mesmos atos para todos (quadro de seleção, seção 7) |
| N04 | **Dois roteiros de gates e nomes de artefatos divergentes.** O registro (seção 6) define G4 como "auditoria e benchmark" e G5 como "decisão de fonte"; o prompt do G0.1 define G4 como avaliação comparativa e G5 como teste empírico e seleção; `DECISIONS_TO_FREEZE.md` tem um terceiro conjunto (G4 AUDIT, G5 SYNTHESIS, G6 PUBLICATION). O registro prevê `BENCHMARK_PLAN.md` e `STRATEGIC_ALIGNMENT_DECISION.md`; os arquivos pedidos têm outros nomes. O registro cita uma planilha `EU_Legislation_Datasets_Scoping_Inventory_v0_1_2026-10-09.xlsx`; a que existe em `inputs/` chama-se `ORIGINAL_Exploratory_Inventory_2026-10-09.xlsx`. | MÉDIA | VERIFIED | Parte III propõe uma sequência única e a tabela de equivalência; nomes a confirmar pela equipe |
| N05 | **A natureza metodológica do estudo mudou.** Uma avaliação comparativa de infraestruturas com teste empírico não é uma revisão de escopo. PRISMA-ScR e JBI cobrem a camada A; a camada B precisa de outro enquadramento de relato. | ALTA | PROPOSED | Relato em duas partes; ver seção 5 e Parte III |
| N06 | **Quanto mapeamento é necessário?** Se o inventário serve à seleção, a exaustividade exigida não é a mesma para todas as classes de recurso. | ALTA | PROPOSED | Cobertura proporcional por classe (especificação S-A04) |
| N07 | **O registro de decisões está em `inputs/` e fora do git.** É documento de governança, não insumo de dados. | BAIXA | VERIFIED | Decidir local e versionar junto com os documentos de gate (especificação S-VER) |

### 4. Avaliação das 27 emendas

Situação: **MANTIDA** (vale como escrita) · **REFORMULADA** (o problema persiste, a solução muda) · **AMPLIADA** (vale e ganha alcance) · **SUBSTITUÍDA** (outro texto ocupa o lugar) · **REBAIXADA** (perde prioridade). O arquivo `PROPOSED_AMENDMENTS.md` não foi alterado; esta tabela é a sua leitura à luz da nova finalidade. Todas as situações são PROPOSED.

| ID | Tema | Grav. G0 | Situação | Razão e destino |
|---|---|---|---|---|
| A01 | Ordem dos gates | CRÍTICA | REFORMULADA | A inversão piloto–congelamento continua válida, mas um único congelamento não basta: há quatro objetos a congelar em momentos distintos. Especificação S-A01 |
| A02 | Unidade canônica | CRÍTICA | AMPLIADA | Vira o centro do estudo. A lista de tipos do G0 é substituída por `SOURCE_TAXONOMY_v0_2_DRAFT.md`, que acrescenta relações, o indicador de candidato e a separação da unidade jurídica |
| A03 | Consultas executáveis | CRÍTICA | REFORMULADA | Persiste. A estratégia passa a ser organizada por classe de recurso, com método diferente para cada uma. S-A03 |
| A04 | Regra de volume | CRÍTICA | REFORMULADA | Passa de "teto de triagem" para "cobertura proporcional por classe": exaustiva para candidatos a fonte legislativa, delimitada para o resto. S-A04 |
| A05 | Equipe de avaliação | CRÍTICA | AMPLIADA | Persiste e ganha funções: operadores do benchmark, avaliador da Dimensão B, quem seleciona os atos de referência. S-A05 |
| A06 | Evidência arquivada | ALTA | AMPLIADA | Estende-se ao benchmark: todo arquivo obtido tem hash, data e parâmetros (registro v1.1, seção 4.4) |
| A07 | Cegamento | ALTA | AMPLIADA | Novas âncoras: a hierarquia de candidatos da seção 5 do registro e os relatórios G0 e G0.1. S-A07 |
| A08 | Circularidade com RGAM/V8 | ALTA | REFORMULADA | Era risco de um instrumento; passa a ser risco da decisão principal. Resolvida pela separação das Dimensões A e B. S-A08 |
| A09 | Nível dos critérios | ALTA | REFORMULADA | Resolvida no quadro de seleção: a unidade avaliada é a configuração (recurso + distribuição), e cada critério declara seu nível |
| A10 | 8 × 9 critérios | ALTA | SUBSTITUÍDA | A lista normativa passa a ser a do quadro de seleção (EA1–EA6, A1–A12, B1–B6). A divergência entre protocolo e codebook fica registrada como histórica |
| A11 | Concordância | ALTA | MANTIDA | Detalhada em `G0_1_REVISED_PILOT_DESIGN.md` e na especificação SPEC-K |
| A12 | Deduplicação | ALTA | MANTIDA | Incorporada à taxonomia (relações; URL gera candidatos, não decisões) |
| A13 | Data de fechamento | ALTA | AMPLIADA | Além da janela de busca, o benchmark precisa de datas de execução e, quando a fonte informar, versão do serviço |
| A14 | Etapas de triagem | MÉDIA | MANTIDA | Sem mudança |
| A15 | RQs 1, 3 e 5 | MÉDIA | SUBSTITUÍDA | O registro v1.1 propõe cinco novas perguntas. Observações sobre elas na seção 5 |
| A16 | PCC | MÉDIA | REFORMULADA | O PCC continua aplicável à camada A. A camada B não é revisão de escopo e não usa PCC (N05) |
| A17 | Componente nacional e especialistas | MÉDIA | REBAIXADA | Fontes nacionais não são candidatas a fonte de legislação da UE. O componente nacional deixa de ser necessário para a decisão principal; mantê-lo no mapa é opcional. Consulta a especialistas ganha um uso preciso: perguntar por alternativas ao candidato prioritário (N02) |
| A18 | Mapa FAIR | MÉDIA | MANTIDA | Tabela de correspondência no quadro de seleção, seção 9; conferência PENDING VALIDATION |
| A19 | PRISMA-ScR / JBI | MÉDIA | REFORMULADA | Aplica-se à camada A. Para a camada B não há lista de verificação consagrada equivalente; o relato precisa ser transparente por construção (N05) |
| A20 | Esquema de dados | MÉDIA | AMPLIADA | Além das lacunas do G0, faltam tabelas para recursos, distribuições, relações, configurações, matriz de evidências, atos de referência e execuções do benchmark |
| A21 | Dados pessoais | MÉDIA | REBAIXADA | Textos legislativos não levantam a questão. Permanece para registros setoriais usados como enriquecimento |
| A22 | Teste de recuperação | MÉDIA | REFORMULADA | O teste que importa agora é: a busca recupera os candidatos a fonte legislativa já conhecidos e encontra outros? Divisão desenvolvimento/teste continua necessária |
| A23 | Casos do subestudo RIT | MÉDIA | SUBSTITUÍDA | O subestudo deixa este estudo. A seleção de casos é decisão própria (registro, seção 8). No seu lugar: critérios de seleção dos **atos de referência** do benchmark, que não são casos RIT |
| A24 | Versionamento | MÉDIA | MANTIDA | Especificação S-VER |
| A25 | Idioma | BAIXA | MANTIDA | — |
| A26 | Rótulo "verificadas" | BAIXA | MANTIDA | — |
| A27 | URLs dos seeds | BAIXA | MANTIDA | O par EU03/EU07 entra completo no Piloto A revisto |

**Balanço** (VERIFIED por contagem da tabela): 8 mantidas, 6 ampliadas, 8 reformuladas, 3 substituídas, 2 rebaixadas. Nenhuma emenda ficou sem objeto. Das cinco críticas do G0, todas continuam críticas; somam-se a elas N01 e N02.

### 5. Observações sobre as perguntas de pesquisa do registro v1.1

Redação proposta no registro, seção 3. As observações são PROPOSED.

| RQ do registro | Observação |
|---|---|
| RQ1 — Quais fontes de atos jurídicos da UE disponibilizam coleções, metadados e serviços computacionalmente acessíveis e documentados? | Responde à crítica da A15 se for condicionada ao método ("identificadas pela estratégia definida"). Usar os termos da taxonomia: "fontes" aqui são recursos com o indicador de candidato |
| RQ2 — Como diferem em cobertura, proveniência, versionamento, identificadores, estrutura, interoperabilidade e direitos? | Respondida pela matriz da Dimensão A. Pressupõe mais de uma fonte: ver N02 |
| RQ3 — Quais satisfazem os requisitos mínimos para constituir um universo jurídico adequado à codificação de arquiteturas regulatórias? | Duas ressalvas. "Adequado" depende do universo ainda indefinido (N01). E a expressão "adequado à codificação de arquiteturas regulatórias" traz a Dimensão B para dentro de um requisito mínimo, o que o critério central do G0.1 proíbe. Sugestão: "requisitos mínimos de adequação como fonte legislativa" |
| RQ4 — Em testes com atos pré-selecionados, quais perdas, inconsistências, restrições e custos são observáveis? | Respondida pelo benchmark de G5. É a pergunta com maior potencial de contribuição original |
| RQ5 — Que configuração de fonte principal e recursos complementares oferece melhor fundamentação? | Respondida pelo parecer. "Melhor" precisa remeter à regra de decisão escrita antes (quadro de seleção, seção 6) |

---

## PARTE II — SALVAGUARDAS: ESPECIFICAÇÕES VERIFICÁVEIS

Nenhuma alteração de código, de `.gitignore` ou de protocolo foi feita. Cada especificação traz a solução proposta e o modo de verificar que foi cumprida.

### 6. S-A01 — Sequência dos gates e congelamentos

**Solução.** Quatro congelamentos, cada um anterior ao primeiro dado que ele governa.

| Congelamento | Objeto | Momento | Governa |
|---|---|---|---|
| F1 | Taxonomia e critérios de elegibilidade, revistos após o Piloto A | Saída de G1 | Classificação em G3 |
| F2 | Estratégia de busca executável, regras de cobertura, janela de datas | Entrada de G2 | Buscas |
| F3 | Quadro de seleção, parâmetros U1–U6, limiares, exceções, condições de desqualificação | Entrada de G4 | Avaliação comparativa |
| F4 | Lista de atos de referência, textos de referência, procedimentos de benchmark | Entrada de G5 | Teste empírico |

Cada congelamento é: uma etiqueta git anotada, um manifesto de SHA-256 dos arquivos congelados e um registro de aprovação com nomes e data. Mudança posterior é emenda datada em arquivo próprio.

**Verificação.**

- V1: para cada tabela de dados, a data mais antiga registrada é posterior à data do congelamento que a governa.
- V2: os hashes dos arquivos congelados coincidem com o manifesto.
- V3: toda emenda posterior tem arquivo, data, motivo e aprovação.

### 7. S-A02 — Unidade canônica

**Solução.** `SOURCE_TAXONOMY_v0_2_DRAFT.md`: cinco níveis, sete classes primárias mais duas residuais, oito relações tipadas, identificadores opacos, e separação entre a unidade contada (recurso) e a unidade jurídica.

**Verificação.**

- V1: todo recurso tem nível, classe do vocabulário, regra aplicada, evidência e avaliador.
- V2: toda relação aponta para identificadores existentes; não há `distribution_of` cujo alvo não seja um recurso.
- V3: os denominadores do relatório são recalculáveis a partir da tabela de recursos, filtrando por nível L1; nenhum usa ocorrências, contêineres ou distribuições.
- V4: nenhuma linha do inventário representa um ato jurídico.
- V5: após o Piloto A, cada regra R0–R11 tem decisão registrada (confirmada ou revista).

### 8. S-A03 — Estratégias de busca executáveis

**Solução.** A busca é organizada por classe de recurso, porque cada classe se descobre de modo diferente.

| Classe-alvo | Método | Por quê |
|---|---|---|
| Candidatos a fonte legislativa de mantenedor oficial | **Enumeração estruturada**: lista fechada de instituições e órgãos de publicação, com roteiro fixo de inspeção de cada sítio e catálogo | São poucos e institucionais; busca por palavra-chave não os enumera de forma confiável |
| Candidatos de terceiros (repositórios não oficiais, agregadores, serviços comerciais) | Busca dirigida, com expressões registradas, mais consulta a especialistas com pergunta única e registrada: "que alternativas ao candidato prioritário você usa ou conhece?" | Responde a N02 |
| Corpora derivados | Busca sistemática em bases bibliográficas e repositórios de dados, com sintaxe por plataforma | É literatura; cabe o método clássico |
| Registros setoriais e fontes auxiliares | Busca delimitada (S-A04) | Enriquecimento; não precisam de exaustividade |

Tabela de consultas com uma linha por plataforma × expressão × idioma e os campos: identificador; classe-alvo; plataforma; expressão literal na sintaxe nativa; campos pesquisados; filtros; regra de paginação; expressão-base de origem; idioma; data de validação da sintaxe.

**Verificação.**

- V1: nenhuma linha contém descrição em lugar de expressão; cada plataforma tem linha própria.
- V2: **teste de repetição** — uma segunda pessoa executa uma consulta de cada método usando apenas a tabela e obtém o total registrado, ou a diferença é explicada pela data.
- V3: toda fonte citada no protocolo tem consulta, roteiro de inspeção, ou exclusão justificada.
- V4: a lista fechada de instituições da enumeração está escrita e datada antes da execução.

### 9. S-A04 — Cobertura e volume de triagem

**Solução.** Cobertura proporcional à função da classe na decisão.

| Classe | Meta de cobertura | Regra de volume |
|---|---|---|
| Candidatos a fonte legislativa | Exaustiva dentro da lista de instituições e das plataformas definidas | Triagem integral, sem teto |
| Corpora derivados | Sistemática | Triagem integral até um teto fixado; acima dele, filtros declarados |
| Registros setoriais e auxiliares | Ilustrativa e declarada como tal | Lista de órgãos fechada de antemão; não se promete exaustividade |
| Catálogos agregadores | Usados como canal, não como alvo | Antes da regra: uma execução de medição, autorizada, que registra só o total |

Para cada plataforma, a regra é escrita depois da medição de volume e antes da execução. O relatório apresenta, por classe, total recuperado e total triado como números distintos, e declara o nível de cobertura pretendido para cada classe.

**Verificação.**

- V1: a data da regra é anterior à da execução correspondente.
- V2: cada execução registra total informado pela plataforma, total exportado e total triado.
- V3: não há registro triado fora da regra, nem registro dentro da regra sem triagem.
- V4: o texto do relatório não usa "exaustivo" para classes cuja meta não era essa.

### 10. S-A05 — Independência e responsabilidades humanas

**Solução.** Matriz de funções, preenchida com nomes antes do Piloto A.

| Atividade | Responsável | Pode ser assistida por IA? | Decisão final |
|---|---|---|---|
| Captura de evidência, preparação de pacotes | Coordenador | Sim | Coordenador |
| Classificação e elegibilidade | Dois avaliadores | Não na decisão | Cada avaliador |
| Adjudicação | Adjudicador | Não | Adjudicador |
| Redação de procedimento de benchmark | Autor do procedimento | Sim, com revisão humana | Autor |
| Execução do benchmark | Dois operadores | Scripts sim; a execução e o registro são do operador | Cada operador |
| Atribuição de descritores na matriz | Avaliador que leu a evidência | Não | Avaliador |
| Seleção dos atos de referência | Pessoa sem conhecimento do desempenho das fontes | Não | Coordenação científica |
| Parâmetros U1–U6, limiares, critérios de passagem | Coordenação científica | Não | Coordenação científica |
| Parecer de seleção | Equipe | Redação sim; conteúdo não | Equipe, com assinaturas |

Cada pessoa declara por escrito a exposição prévia: construiu ou leu o inventário; leu relatórios G0 ou G0.1; já extraiu dados de alguma fonte candidata. Se só houver um avaliador disponível, o desenho é rebaixado de forma declarada, e o relato diz o que foi feito.

**Verificação.**

- V1: arquivo de funções com nomes e data anterior ao primeiro pacote.
- V2: todo valor de `reviewer`, `operator` e `adjudicator` nas tabelas consta da lista de pessoas; identificadores de agentes são rejeitados pela verificação de integridade.
- V3: declarações de exposição arquivadas.
- V4: nenhuma decisão tem o mesmo nome como avaliador e como adjudicador.

### 11. S-A07 — Viés de ancoragem

**Solução.**

1. **Pacotes cegos** gerados por programa: `record_id`, nome, referência da captura. Excluídos: `layer`, `resource_type`, `rgam_potential`, `initial_priority`, `limitations`, e o campo `notes` de `discovery_records.csv`.
2. **Documentos reservados** (não entregues a avaliadores e operadores): `G0_REVIEW_NOTE.md`, `PILOT_CALIBRATION_PLAN.md`, `G0_1_REVISED_PILOT_DESIGN.md`, `G0_1_DECISION_REPORT.md`, este documento, e a seção 5 do registro de decisões v1.1 (hierarquia das fontes candidatas).
3. **Ordem aleatória** por pessoa, com semente registrada.
4. **Formulários da Dimensão A** sem menção a RGAM, V8, RIT ou intermediários.
5. **Declaração de exposição** (S-A05); quem construiu o inventário não avalia, se a equipe tiver alternativa.
6. **Novas ocorrências** vindas da busca entram nos pacotes misturadas aos seeds, sem marca de origem.

**Verificação.**

- V1: teste automático do gerador de pacotes falha se alguma coluna excluída aparecer na saída.
- V2: lista de documentos reservados com registro de quem os recebeu.
- V3: semente e ordem de cada pacote arquivadas.
- V4: busca textual nos formulários da Dimensão A por "RGAM", "V8", "RIT", "intermedi" retorna zero.

### 12. S-A08 — Circularidade com a operacionalização RGAM/V8

**Solução.** Sete regras, detalhadas no quadro de seleção (seções 5.3 e 6).

1. Duas dimensões, com matrizes separadas.
2. Requisitos eliminatórios só na Dimensão A.
3. A Dimensão A é concluída e trancada antes de a Dimensão B ser aberta.
4. A Dimensão B não reprova nem resgata.
5. A Dimensão B mede o que a **fonte** acrescenta ao texto (estrutura endereçável, metadados, ligações), não o conteúdo normativo dos atos.
6. O parecer mostra a escolha feita só com a Dimensão A.
7. Os atos de referência são escolhidos por critérios de esforço sobre a fonte, não por interesse analítico, e não são a amostra de casos.

**Verificação.**

- V1: hash e data da matriz A anteriores à primeira linha da matriz B.
- V2: nenhuma linha de eliminatório com critério B.
- V3: o parecer contém a seção "escolha considerando apenas a Dimensão A".
- V4: cada âncora dos critérios B descreve propriedade do dado e não usa categoria do codebook RGAM/V8; conferência por leitor externo ao projeto, se houver.
- V5: registro da seleção dos atos com os critérios aplicados a cada um.

### 13. Defeitos técnicos identificados no G0

Código não alterado. `scripts/cli.py` mantém o SHA-256 `1eba44ef…2ac6e`.

#### SPEC-V — Validação de vocabulários

**Defeito** (VERIFIED, `BASELINE_RUN.md`, sondagem P5): nove valores inválidos em sete tabelas produziram zero erros; um `origin` inventado foi contado como busca sistemática.

**Especificação.**

1. Vocabulários controlados num único arquivo legível por máquina, lido pelo verificador e citado pelo codebook. Fonte única; o código não repete listas.
2. Colunas validadas, no mínimo: `origin`; `stage` e `decision` em triagem e consenso; `reason_code`; `criterion` e `score` na auditoria; `validation_status`; e, quando existirem, nível, classe, tipo de relação e descritor do quadro de seleção.
3. Datas em ISO 8601; URLs com esquema `http` ou `https`; identificadores de pessoa pertencentes à lista de funções.
4. `origin` fora do vocabulário é ERROR e o registro não entra em nenhuma contagem.
5. `source_record_ids` de um recurso: cada identificador existe e tem decisão de consenso `include` na última etapa.
6. O comando de verificação é somente leitura: tabela ausente é ERROR, não é criada.
7. URL repetida entre ocorrências gera WARNING com os identificadores envolvidos.

**Testes de aceitação.**

- T1: sobre os dados atuais, zero erros (o comportamento de hoje se mantém).
- T2: cada um dos nove valores inválidos da sondagem P5, inserido isoladamente em cópia temporária, produz exatamente um ERROR que nomeia tabela, coluna e valor.
- T3: com uma tabela removida, a verificação termina com ERROR e nenhum arquivo é criado.
- T4: com `origin` inválido, as contagens do relatório não mudam.
- T5: a verificação não altera o SHA-256 de nenhum arquivo de dados.
- T6: os testes rodam em diretório temporário e nunca escrevem em `data/`.

#### SPEC-K — Concordância entre avaliadores

**Defeito** (VERIFIED, sondagem P1): a função agrupa pares de avaliadores diferentes num único resultado e descarta, sem contar, registros em que um avaliador marcou `uncertain`.

**Especificação.**

1. A unidade de cálculo é o **par nomeado e não ordenado** de avaliadores, por etapa e por variável. A saída é uma lista de resultados, um por par. Não existe resultado agregado.
2. Para cada par: número de itens avaliados por ambos; tabela cruzada completa, incluindo `uncertain` como categoria; concordância bruta sobre todos os itens; concordância bruta restrita aos itens em que ambos deram resposta categórica; concordância específica por categoria.
3. Kappa de Cohen apenas quando ambos os avaliadores usaram ao menos duas categorias; caso contrário, valor ausente com o motivo. Intervalo de confiança com o método declarado na saída.
4. Itens com um só avaliador, ou com mais de dois, são listados à parte, com contagem; nunca descartados em silêncio.
5. Variáveis ordinais (descritores 0/1/2): estatística ponderada, com `UNVERIFIED` e `NA` tratados como categorias próprias fora da ponderação e relatados em tabela.
6. Nenhuma função devolve "aprovado" ou "reprovado". O critério de passagem é dos documentos de piloto, não do código.

**Testes de aceitação.**

- T1: caso da sondagem P1 (A e B no item 1; C e D no item 2; A `include` e B `uncertain` no item 3) → dois resultados: par (A, B) com 2 itens, sendo 1 com `uncertain`; par (C, D) com 1 item. Nenhum resultado com n = 2 e kappa = 1.
- T2: todas as decisões iguais → kappa ausente, com motivo; concordância bruta 1.
- T3: valor conhecido — tabela 2 × 2 com 20 e 15 na diagonal e 5 e 10 fora dela (n = 50): concordância observada 0,70; esperada 0,50; kappa 0,40.
- T4: trocar a ordem dos avaliadores não altera concordância nem kappa.
- T5: a soma das células da tabela cruzada é igual ao número de itens avaliados por ambos.
- T6: item com três avaliadores aparece na lista à parte e em nenhum par.

### 14. S-VER — Versionamento dos documentos de gate

**Situação** (VERIFIED): o `.gitignore` da pasta ignora `outputs/*`. Seis documentos de gate não estão no histórico: quatro do G0 e dois do G0.1 em `outputs/`. Quatro arquivos em `protocol/` e o registro em `inputs/` estão não rastreados por serem novos, não por serem ignorados.

**Hashes de referência dos relatórios do G0**, tomados nesta fase, antes de qualquer cópia:

| Arquivo | SHA-256 |
|---|---|
| `outputs/BASELINE_RUN.md` | `225ff098fffb22f2ffdd8aed37d885a7df0502f6649abaee0fe9deafce2a661f` |
| `outputs/EXECUTION_PLAN.md` | `12e4b4a1c6bdcff93a2c921932d135a5a732766f46d20d15d0e055ef86496f4d` |
| `outputs/G0_REVIEW_NOTE.md` | `282ea52231e7aa61c0e1da5336fdfdc6457130da6e85ba5e9e17726b2fb8e7bd` |
| `outputs/PILOT_CALIBRATION_PLAN.md` | `3a4044825d7646a435b463b5a7fc07e3103747481bf2387e5cfe7e56b64d7595` |
| `protocol/PROPOSED_AMENDMENTS.md` | `52463ccefee0d855239fa044d350270fa25668cff8678c07393f695461284774` |

**Opções.**

| Opção | Como | A favor | Contra |
|---|---|---|---|
| 1 — Pasta rastreada de gates (**recomendada**) | Criar `gates/G0/` e `gates/G0_1/`; copiar para lá os documentos, byte a byte; gravar `MANIFEST.sha256` em cada pasta; `outputs/` continua ignorada e passa a conter só arquivos regeneráveis | Não toca no `.gitignore`; separa registro histórico de saída de programa; o manifesto prova a integridade | Duas cópias até que `outputs/` seja limpa |
| 2 — Exceção no `.gitignore` | Acrescentar negações para os documentos de gate | Sem cópia | Mistura registro histórico com arquivos regeneráveis; cada novo documento exige nova linha |
| 3 — Adição forçada | `git add -f` | Imediato | Frágil; depende de lembrar; não documenta a regra |

**Procedimento da opção 1**, a executar só com autorização:

1. Conferir que os hashes atuais coincidem com a tabela acima.
2. Copiar sem editar; calcular os hashes das cópias; conferir igualdade.
3. Gravar o manifesto.
4. Um commit por gate, com mensagem que cite o gate e o manifesto; etiqueta anotada por gate.
5. A partir daí, novos documentos de gate nascem em `gates/`.

`outputs/STATUS_REPORT.md` é regenerável e fica de fora. O registro de decisões sai de `inputs/` para uma pasta de governança, por cópia com hash conferido (N07).

**Verificação.**

- V1: `sha256sum -c MANIFEST.sha256` sem falhas em cada pasta de gate.
- V2: os hashes de `gates/G0/` coincidem com a tabela desta seção.
- V3: o histórico de um documento de gate tem um único commit; correções são feitas por documento novo, nunca por edição.

---

## PARTE III — ROTEIRO REVISADO

Proposta sujeita à aprovação da equipe. Nenhum gate posterior ao G0.1 foi iniciado.

### 15. Sequência

| Gate | Conteúdo | Depende de | Condições de aprovação | Entregas |
|---|---|---|---|---|
| **G0** — Diagnóstico inicial | Concluído | — | — | Cinco documentos do G0 (inalterados) |
| **G0.1** — Alinhamento estratégico | Este gate | G0; registro v1.1 | Revisão científica dos cinco documentos do G0.1; decisão sobre a reorientação pela equipe; decisão registrada para cada emenda e para N01–N07 | Alinhamento; taxonomia v0.2; quadro de seleção v0.1; desenho dos pilotos; relatório de decisão |
| **G1** — Calibração de classificação e elegibilidade | Piloto A, com rodada de confirmação; aprovação do desenho do Piloto B; correções de código SPEC-V e SPEC-K | G0.1 aprovado; funções nomeadas; critérios de passagem datados; documentos de gate versionados | PA1–PA8 satisfeitos; taxonomia e elegibilidade revistas; testes de aceitação de SPEC-V e SPEC-K aprovados | Taxonomia v1.0; ata de calibração; **congelamento F1**; código corrigido e testado |
| **G2** — Descoberta e mapeamento sistemático | Buscas por classe, dentro da janela de datas | F1; estratégia executável; medição de volume autorizada; regras de cobertura escritas | **Congelamento F2** antes da primeira busca; todas as plataformas executadas ou a falha registrada; teste de repetição aprovado | Registro de buscas; ocorrências com proveniência; brutos com hash |
| **G3** — Triagem, deduplicação e adjudicação | Classificação dupla; relações; indicador de candidato | G2 | Nenhum registro com conflito aberto; denominadores recalculáveis; número de mantenedores independentes entre os candidatos declarado | Inventário adjudicado; conjunto de configurações candidatas; concordância por par |
| **G4** — Avaliação comparativa das fontes | Eliminatórios e critérios da Dimensão A por documentação | G3; parâmetros U1–U6, limiares e exceções decididos | **Congelamento F3** antes de qualquer avaliação; cada célula com evidência arquivada; dupla avaliação conforme decidido | Matriz documental da Dimensão A; lista de pendências que só o teste resolve |
| **G5** — Teste empírico e seleção fundamentada | Piloto B (se tardio); benchmark com os atos de referência; Dimensão B; deliberação | G4; atos e textos de referência selecionados | **Congelamento F4** antes da primeira consulta; matriz A trancada antes de B; regra de decisão aplicada; análises de sensibilidade feitas | Resultados do benchmark; matriz B; **parecer de seleção** assinado |
| **G6** — Documentação, integração e manuscrito | Pacote de replicação; seção de fontes de dados para o projeto; avaliação da publicação autônoma | G5 | Dados, código e manifestos depositáveis; termos de cada fonte respeitados; decisão sobre o manuscrito tomada com os resultados à vista | Pacote de replicação; texto de métodos; decisão de publicação |

### 16. Fora deste roteiro

Por força da seção 8 do registro v1.1, ficam para documentos próprios, não iniciados e não afetados aqui: definição do universo jurídico; protocolo de amostragem e seleção de casos; codebook e validação da operacionalização RGAM/V8. O envelope U1–U6 é insumo provisório deste estudo e não substitui a definição do universo.

### 17. Equivalência entre os três roteiros existentes

| Este roteiro | Registro v1.1, seção 6 | `DECISIONS_TO_FREEZE.md` |
|---|---|---|
| G0 | G0 | — (lá, G0 era o congelamento do protocolo) |
| G0.1 | G0.1 | — |
| G1 | G1 calibração | G1 PILOT |
| G2 | G2/G3 descoberta e triagem | G2 SEARCH |
| G3 | G2/G3 descoberta e triagem | G3 SCREEN |
| G4 | G4 auditoria e benchmark (parte documental) | G4 AUDIT |
| G5 | G4 (parte de teste) e G5 decisão de fonte | — |
| G6 | G6 integração e publicação | G5 SYNTHESIS e G6 PUBLICATION |

`DECISIONS_TO_FREEZE.md` não foi alterado. A equipe decide qual numeração é a normativa e registra a equivalência (N04).

### 18. Caminho crítico

1. **Decisões humanas do G0.1.** Sem elas nada começa.
2. **Parâmetros U1–U6.** Dependem da discussão sobre o universo com David e a equipe. São o item de maior risco de atraso: bloqueiam F3, G4 e a escolha dos atos de referência.
3. **Existência de alternativas independentes** (N02). Só se sabe ao fim de G3 e muda a natureza do produto.

---

## Registro de integridade desta fase

- Nenhuma busca, coleta, triagem ou consulta a fonte externa.
- Protocolo, codebook, scripts, dados e os cinco documentos do G0: inalterados.
- Nenhuma alteração na operacionalização RGAM/V8 nem em outros subprojetos.
- Nenhuma decisão humana, resultado de avaliação, fonte ou evidência inventados.
- Nenhum commit, nenhuma publicação remota.
- Gate: a execução se encerra no G0.1 e aguarda revisão científica.
