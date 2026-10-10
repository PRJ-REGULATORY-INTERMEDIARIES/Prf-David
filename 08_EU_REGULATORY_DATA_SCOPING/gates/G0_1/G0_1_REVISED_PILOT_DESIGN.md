# DESENHO REVISADO DOS PILOTOS — G0.1

**Data:** 2026-10-09 | **Estado:** PROPOSED. Nenhum registro foi classificado, nenhum ato foi selecionado, nenhuma fonte foi consultada, nenhuma resposta de avaliador existe.
**Substitui, como proposta,** `outputs/PILOT_CALIBRATION_PLAN.md`, que permanece intacto como registro do G0.

**Aviso de cegamento.** Este documento contém julgamentos sobre registros do inventário. **Não deve ser entregue aos avaliadores.** Eles recebem a taxonomia, o formulário e o pacote de evidências.

## 1. Exame crítico da amostra de 18 registros do G0

| # | Problema | Evidência | Classe |
|---|---|---|---|
| 1 | Foi desenhada para calibrar **elegibilidade** numa revisão de escopo. A finalidade agora é selecionar a fonte legislativa; o que mais precisa de calibração é a distinção recurso × distribuição × derivado. | Estratos do plano G0 são os seis do prompt G0, não classes da taxonomia | VERIFIED |
| 2 | Não cobre a família Jurisprudência. | 10 de 11 famílias | VERIFIED |
| 3 | Sobrerrepresenta a prioridade exploratória P1. | 11/5/2 na amostra contra 19/19/3 no universo | VERIFIED |
| 4 | Pares que testam deduplicação e sobreposição ficaram incompletos: o registro com a mesma URL de EU03 (EU07) ficou como suplente; EU08 entrou sem EU09; EU34 sem EU33. | Lista do plano G0 | VERIFIED |
| 5 | Três registros de "Intermediação RIT" numa amostra de 18 pesam mais do que a nova finalidade justifica: registros setoriais passam a ser enriquecimento (decisão D09). | Registro de decisões v1.1 | VERIFIED |
| 6 | A seleção foi feita por agente de IA com acesso às colunas de julgamento do inventário. | Declarado no plano G0, seção 2 | VERIFIED |
| 7 | Um único exercício tentava calibrar elegibilidade, tipo de unidade, agrupamento e separação da relação RIT. Misturava instrumentos. | Formulário do plano G0, seção 6 | VERIFIED |
| 8 | Não havia nenhum teste com atos jurídicos. A pergunta "esta fonte entrega o texto, as versões e os vínculos?" não era tocada. | Plano G0, seção 4, "fora do escopo" | VERIFIED |

Conclusão: a amostra do G0 não é reaproveitável como está. O que se segue separa dois exercícios com objetos, instrumentos e critérios de passagem diferentes.

| | Piloto A | Piloto B |
|---|---|---|
| Objeto | Recursos do inventário | Atos jurídicos obtidos de fontes candidatas |
| Instrumento testado | `SOURCE_TAXONOMY_v0_2_DRAFT.md` e critérios de elegibilidade | Protocolo de benchmark do `SOURCE_SELECTION_FRAMEWORK_v0_1.md` |
| Pergunta | Dois avaliadores classificam e agrupam do mesmo modo? | Dois operadores, com o mesmo procedimento escrito, obtêm a mesma coisa, e as medidas funcionam? |
| Natureza da discordância | De julgamento | De execução e de definição da medida |
| Gate | G1 | Desenho aprovado em G1; execução conforme a seção 4.9 |

---

## 2. Disposições comuns aos dois pilotos

### 2.1 Funções

| Função | Responsabilidade | Restrições |
|---|---|---|
| Coordenador do piloto | Prepara pacotes, captura evidências, tranca respostas, produz a comparação descritiva, redige a ata | Não avalia. Pode ter visto o inventário e os relatórios G0 e G0.1 |
| Avaliador 1 e Avaliador 2 (Piloto A) | Classificam, cada um sozinho, todos os registros do pacote | Pessoas. Não leram este documento, nem `G0_REVIEW_NOTE`, `PILOT_CALIBRATION_PLAN`, `G0_1_DECISION_REPORT`, nem a seção 5 do registro v1.1. Declaram por escrito a exposição prévia ao inventário |
| Operador 1 e Operador 2 (Piloto B) | Executam, cada um sozinho, o mesmo procedimento escrito e registram o que obtiveram | Pessoas. Podem usar scripts; a execução e o registro são de responsabilidade do operador |
| Adjudicador | Decide as divergências que persistirem após a reunião | Não produziu a decisão contestada |
| Coordenação científica | Aprova amostras, critérios de passagem e mudanças de regra | Decisões datadas e assinadas |
| Agente de IA | Prepara pacotes, gera listas de candidatos a duplicata, confere consistência formal, redige atas a partir de registros | **Nunca** conta como avaliador, operador independente ou adjudicador. Duas execuções de um agente não são duas avaliações |

Quem ocupa cada função é decisão da equipe: PENDING VALIDATION.

### 2.2 Independência

- Arquivos de resposta separados por pessoa; nenhum acesso ao arquivo do outro.
- Nenhuma conversa sobre os casos até ambos entregarem.
- Ordem dos itens aleatorizada de modo diferente para cada pessoa, com semente registrada.
- Entrega ao coordenador, que registra SHA-256 e data de cada arquivo **antes** de abrir qualquer um.
- Quebra de independência detectada anula os itens afetados, que são refeitos com registros não usados.

### 2.3 Respostas incertas

- `uncertain` (Piloto A) e `não determinado` (Piloto B) são respostas legítimas. Ninguém é obrigado a escolher.
- Toda resposta incerta traz obrigatoriamente o que faltou: regra ausente, regra ambígua, ou evidência insuficiente (e qual).
- Na comparação, incerteza é **categoria própria** nas tabelas. Não é descartada, não é convertida e não é tratada como concordância quando ambos a marcam sem o mesmo motivo.
- A proporção de incertas por variável é indicador do piloto: muita incerteza numa regra indica regra a rever, mesmo com alta concordância nos demais itens.

### 2.4 Indicadores de concordância

- Calculados **por par nomeado** (Avaliador 1 × Avaliador 2; Operador 1 × Operador 2) e **por variável**. Se houver mais de um par, cada par tem a sua tabela. **Pares diferentes nunca são combinados num único kappa nem numa única taxa.**
- Sempre relatados: número de itens; tabela cruzada completa, incluindo a categoria de incerteza; concordância bruta; concordância específica por categoria.
- Kappa de Cohen pode ser relatado para variáveis nominais com o respectivo intervalo de confiança e a ressalva do tamanho da amostra. Com cerca de 20 itens e várias categorias, é descritivo.
- **Nenhum limiar estatístico é, sozinho, condição de aprovação.** Os critérios de passagem são os das seções 3.7 e 4.8.

### 2.5 Adjudicação

1. O coordenador produz a comparação sem interpretar.
2. Reunião com o par e o adjudicador. Para cada divergência e cada incerteza: regra envolvida; causa (regra ausente, regra ambígua, leitura diferente da evidência, evidência insuficiente, erro de execução); resolução.
3. O adjudicador decide só o que restar em aberto, com justificativa escrita.
4. Mudança de regra vira proposta de emenda, com referência aos itens que a motivaram.
5. As decisões do piloto **não** entram nas tabelas de execução, nas contagens do inventário nem no fluxograma.

### 2.6 Critérios de passagem: quando são fixados

Os critérios das seções 3.7 e 4.8 são propostas. A coordenação científica os aprova, altera ou substitui, **por escrito e com data anterior à entrega do primeiro pacote**. O coordenador confere essa anterioridade antes de abrir respostas. Onde um critério usa um valor numérico de alerta, o valor é fixado pela equipe nesse mesmo ato; este documento não o fixa.

---

## 3. PILOTO A — calibração da taxonomia de recursos

### 3.1 Objetivo

Verificar se as regras R0–R11 e as relações da taxonomia levam duas pessoas às mesmas respostas sobre: nível (contêiner, recurso, distribuição, duplicata), classe primária, relações com outros registros, indicador de candidato a fonte legislativa e elegibilidade.

### 3.2 Regra de composição

1. Todas as 11 famílias de origem do inventário, com pelo menos um registro cada.
2. Proporção de prioridades exploratórias próxima da do universo (19/19/3).
3. **Pares e grupos completos**: quando um registro entra por testar deduplicação, distribuição ou derivação, o seu par entra junto.
4. Ao menos um registro que o inventário descreve como descontinuado e um com acesso restrito.
5. Tamanho: 20, limite superior da faixa de 15–20 do protocolo, para acomodar os pares.
6. Reserva de registros não usados para a rodada de confirmação.

### 3.3 Composição proposta (20 registros)

Todos os identificadores existem em `inputs/seed_inventory_v0_1.csv`; nome e família são transcritos dele. A coluna "função" diz por que o registro está no pacote; **não é classificação**.

| ID | Nome (inventário) | Família (`layer`) | Prior. | Função no piloto | Em relação ao G0 |
|---|---|---|---|---|---|
| EU01 | EUR-Lex — legislação e documentos jurídicos | Corpus normativo | P1 | Grupo 1: contêiner × recurso | mantido |
| EU02 | CELLAR — repositório e grafo de metadados | Corpus normativo | P1 | Grupo 1: R2 × R10 | mantido |
| EU03 | EUR-Lex bulk data dump | Corpus normativo | P1 | Grupo 1: distribuição parcial; acesso restrito; par de URL | mantido |
| EU07 | European Legal Data Space — diretório | Infraestrutura | P2 | Par de URL com EU03; contêiner | **novo** |
| EU06 | EuroVoc — tesauro multilíngue | Infraestrutura | P2 | Fronteira auxiliar × dataset | **novo** |
| EU08 | European Parliament Open Data API — procedures | Processo legislativo | P1 | Grupo 2: interface × acervo | mantido |
| EU09 | Legislative Observatory — OEIL | Processo legislativo | P1 | Grupo 2: par de EU08 | **novo** |
| EU11 | Council votes on legislative acts — dataset antigo | Processo legislativo | P3 | Descontinuado | mantido |
| EU15 | Comitology Register — comitês e atos de execução | Delegação/implementação | P1 | Dataset normativo × registro | mantido |
| EU17 | EU Transparency Register | Atores/participação | P2 | Registro sem ato normativo como unidade | mantido |
| EU19 | N-Lex — bases legais nacionais | Transposição/Estados | P2 | Portal federado; limite do escopo nacional | **novo** |
| EU22 | InfoCuria — decisões do TJUE | Jurisprudência | P2 | Família ausente no G0; repositório não legislativo | **novo** |
| EU24 | Competition Case Search — antitrust, mergers, State aid, DMA | Fiscalização | P2 | Contêiner com subcoleções | **novo** |
| EU28 | DGA — Register of Data Intermediation Services | Intermediação RIT | P2 | Registro setorial | mantido |
| EU29 | NANDO — Notified Bodies | Intermediação RIT | P1 | Registro setorial | mantido |
| EU33 | TED Open Data Service (contratações) | Aplicação setorial | P2 | Grupo 3: par de EU34 | **novo** |
| EU34 | TED Search API — notices | Aplicação setorial | P2 | Grupo 3: R2 × R10 | mantido |
| EU35 | MultiEURLEX — EU legislation corpus | Corpus acadêmico | P1 | Grupo 4: corpus derivado | mantido |
| EU39 | LexGLUE — subtarefa EUR-LEX | Corpus acadêmico | P2 | Grupo 4: derivado de derivado | mantido |
| EU40 | EU Policy Agendas Project — European Council Conclusions | Corpus acadêmico | P3 | Fronteira de escopo | mantido |

**Cobertura** (VERIFIED por contagem sobre o arquivo de seeds):

| Dimensão | Piloto A proposto | Amostra G0 | Universo |
|---|---|---|---|
| Famílias cobertas | 11 de 11 | 10 de 11 | 11 |
| P1 / P2 / P3 | 8 / 10 / 2 | 11 / 5 / 2 | 19 / 19 / 3 |
| Mantidos do G0 | 13 | — | — |
| Retirados | EU05, EU18, EU21, EU25, EU26 | — | — |
| Acrescentados | EU06, EU07, EU09, EU19, EU22, EU24, EU33 | — | — |

**Reserva (21 registros não usados):** EU04, EU05, EU10, EU12, EU13, EU14, EU16, EU18, EU20, EU21, EU23, EU25, EU26, EU27, EU30, EU31, EU32, EU36, EU37, EU38, EU41. Cobre 9 famílias; inclui quatro corpora e um registro de "Corpus normativo" que os avaliadores não terão visto, úteis para a rodada de confirmação.

### 3.4 Alternativa: sorteio com restrições

A lista acima continua sendo escolha intencional de um agente de IA que viu as colunas de julgamento (problema 6 da seção 1). Se a equipe preferir eliminar esse viés, o procedimento alternativo é:

1. a coordenação fixa uma semente e a registra antes do sorteio;
2. sorteia-se um registro por família (11);
3. completam-se os pares e grupos dos sorteados (regra 3 da seção 3.2);
4. sorteiam-se os restantes até 20, respeitando a proporção de prioridades;
5. o sorteio é executado por script versionado, e a lista resultante é registrada com a semente.

Não foi executado. A escolha entre a lista intencional e o sorteio é decisão da equipe.

### 3.5 Material entregue aos avaliadores

- `SOURCE_TAXONOMY_v0_2_DRAFT.md` e os critérios de elegibilidade do protocolo (§6), na redação atual.
- Para cada registro: `record_id`, nome, e a captura arquivada da página (emenda A06), a mesma para os dois.
- Formulário.

**Não recebem:** as colunas `layer`, `resource_type`, `rgam_potential`, `initial_priority`, `limitations` do inventário; o campo `notes` de `discovery_records.csv`; a tabela da seção 3.3; qualquer relatório G0 ou G0.1.

### 3.6 Formulário e variáveis comparadas

| Variável | Valores | Como se compara |
|---|---|---|
| `level` | K / L1 / L2 / duplicate / uncertain | Tabela cruzada 5 × 5 |
| `primary_class` | FPL, REP, DSE, API, COD, REG, AUX, FDE, IND, uncertain | Tabela cruzada completa |
| `rule_applied` | R0–R11 | Divergência de regra com mesma classe é registrada |
| `relations` | Conjunto de pares (tipo, alvo) dentro do pacote | Por relação: declarada por ambos, por um, por nenhum |
| `legislative_candidate` | sim / não / indeterminado | Tabela cruzada 3 × 3 |
| `eligibility` | include / exclude / uncertain, com `reason_code` | Tabela cruzada 3 × 3 |
| `secondary_roles` | Lista | Descritivo |
| `rule_gap` | Texto | Agrupado por regra |
| `minutes` | Número | Média e amplitude por tipo de página |

### 3.7 Critérios de passagem propostos

O piloto passa quando **todas** as condições abaixo são satisfeitas. São condições de processo e de conteúdo; nenhuma é só um número.

| ID | Condição | Verificação |
|---|---|---|
| PA1 | Integridade do procedimento: os dois arquivos trancados antes da comparação; nenhuma quebra de independência; critérios de passagem datados antes da entrega do pacote | Hashes e datas no registro do coordenador |
| PA2 | Toda divergência e toda resposta incerta têm causa atribuída na ata | Ata sem linhas em branco |
| PA3 | Para cada regra R0–R11 e cada tipo de relação envolvido em divergência, a equipe decidiu: confirmar o texto, ou revisá-lo com nova redação | Lista de regras com decisão |
| PA4 | Nenhuma classe ficou sem definição aplicável: não há registro para o qual os dois avaliadores declararam que nenhuma classe serve | Formulários |
| PA5 | Os grupos 1 a 4 e o par de URL têm resolução de nível e de relação acordada após a reunião, ou a divergência foi adjudicada com justificativa | Ata |
| PA6 | **Rodada de confirmação**: com as regras revistas, o mesmo par classifica registros da reserva (a equipe fixa quantos, antes) e não surge tipo novo de lacuna de regra | Comparação das categorias de `rule_gap` entre as duas rodadas |
| PA7 | Alerta numérico: se a concordância bruta em `level` na rodada de confirmação ficar abaixo do valor fixado previamente pela equipe, a taxonomia volta à revisão, **mesmo que PA1–PA6 estejam satisfeitas**. O inverso não vale: atingir o valor não dispensa PA1–PA6 | Tabela cruzada da rodada de confirmação |
| PA8 | Adjudicador e coordenação científica assinam a ata | Assinaturas |

Se PA6 falhar, repete-se com outros registros da reserva. Esgotada a reserva sem estabilidade, o resultado é que a taxonomia não é aplicável como está, e isso é relatado.

### 3.8 Produtos

Capturas com hashes; dois arquivos de resposta por rodada, trancados; comparação descritiva; ata; emendas à taxonomia e aos critérios de elegibilidade; estimativa de minutos por registro.

---

## 4. PILOTO B — benchmark de fontes legislativas

### 4.1 Objetivo

Testar **o protocolo de benchmark**, em pequena escala, antes da comparação definitiva de G5. O piloto responde a três perguntas:

1. O procedimento escrito é executável por uma segunda pessoa sem instrução oral?
2. As medidas estão definidas de modo que dois operadores registrem a mesma coisa?
3. As medidas são aplicáveis a todas as configurações candidatas, ou alguma só faz sentido para uma delas?

O Piloto B **não** decide qual fonte é melhor. Seus resultados não entram no parecer de seleção.

### 4.2 Princípio

O mesmo conjunto pequeno de atos jurídicos é buscado em cada configuração candidata, pelo mesmo procedimento. Registra-se o que foi obtido. Compara-se entre configurações e entre operadores.

### 4.3 Critérios para a seleção dos atos de referência

**A seleção não é feita aqui.** Abaixo estão os critérios; a lista de atos é fixada pela coordenação científica, registrada com data e trancada antes de qualquer consulta a qualquer fonte.

Os critérios são de **esforço sobre a fonte**: escolhem-se atos que exercitam as capacidades em teste, não atos interessantes para a análise posterior.

| Dimensão de variação | Categorias a cobrir | Capacidade que exercita |
|---|---|---|
| Tipo de ato | Os tipos do parâmetro U1; ao menos um ato de base e um ato delegado ou de execução ligado a ele | A3 tipos; B4 vínculo de delegação |
| Período | Faixas do parâmetro U2, incluindo a mais antiga e a mais recente | A2 cobertura temporal |
| Histórico de alterações | Nunca alterado; alterado uma vez; alterado muitas vezes, com várias consolidações; revogado; com retificação publicada | A7 versionamento; EA5 |
| Complexidade estrutural | Ato curto sem anexos; ato com anexos extensos; ato com tabelas ou fórmulas | A6 completude; A9 formatos; EA6 |
| Vínculos entre atos | Ato que altera outro; ato com base jurídica em outro ato derivado; ato que revoga | B5; metadados de relação |
| Domínio material | Diversidade dentro do parâmetro U5 | A1 cobertura material |
| Idioma | Os idiomas do parâmetro U3 | Cobertura linguística |

**Regras de seleção**

1. **Tamanho.** Pequeno: o suficiente para preencher as categorias acima sem que um único ato represente sozinho mais de duas dimensões críticas. A equipe fixa o número; como ordem de grandeza, 12 a 16 atos: PROPOSED, a confirmar depois de conhecidos U1–U5.
2. **Três subconjuntos, relatados separadamente:**
   - *âncoras*: atos de que o projeto já tem cópia local verificada, o que permite comparação de integridade com um texto conhecido. O README do repositório registra que as etapas R4 e R5 trabalharam com GDPR, DSA, AI Act, CBAM, SCF e a Diretiva 86/361 (VERIFIED como menção; a adequação dessas cópias como referência é PENDING VALIDATION). Usar âncoras não altera aqueles subprojetos: lê-se, não se escreve;
   - *estresse*: atos escolhidos para preencher as categorias da tabela que as âncoras não cobrem, sobretudo atos antigos, muito alterados e revogados;
   - *sorteados*, se a equipe quiser: atos sorteados de uma enumeração independente do caminho de acesso em teste. Exige um quadro de amostragem; se o único quadro disponível for o da fonte prioritária, declarar a limitação.
3. **Quem seleciona.** Pessoa que não conhece o desempenho das fontes nos atos considerados. Quem já extraiu atos de uma fonte candidata declara isso.
4. **Proibição.** Nenhum ato é incluído ou retirado depois de iniciadas as consultas. Substituição só por impossibilidade objetiva, com registro.
5. **Separação.** Esta lista não é o universo jurídico, não é a amostra de casos da operacionalização RGAM/V8 e não cria precedente para nenhum dos dois.
6. **Texto de referência.** Para cada ato, define-se antes o que conta como texto de referência para a comparação de integridade (por exemplo, a publicação oficial original) e como ele é obtido de forma independente da configuração em teste. Se não houver referência independente, a medida de integridade passa a ser de **consistência entre fontes**, e é relatada com esse nome.

### 4.4 Configurações testadas no piloto

Não escolhidas aqui. Regra de composição mínima, para que o piloto exercite o protocolo em situações diferentes:

- o candidato prioritário, em pelo menos duas distribuições distintas;
- pelo menos um corpus derivado;
- pelo menos uma configuração de mantenedor independente do candidato prioritário, **se o inventário contiver alguma**. Se não contiver, o piloto registra esse fato, que é em si um resultado relevante para G4.

### 4.5 O que se registra por ato e por configuração

Observações, não notas. Uma linha por (operador, configuração, ato, versão solicitada).

| Bloco | Observação | Tipo |
|---|---|---|
| Obtenção | Ato localizado pelo identificador? Texto original obtido? | sim / não / não determinado |
| Identificação | Identificadores devolvidos pela fonte, como informados | texto |
| Texto original | Formato; tamanho; SHA-256 do arquivo; idioma | registro |
| Integridade | Inventário estrutural do texto obtido: número de artigos, de considerandos, de anexos; presença de tabelas; comparação com a referência | contagens e sim / não |
| Metadados | Lista dos campos devolvidos; presença de data de adoção, de publicação, de entrada em vigor, autor, base jurídica, estado de vigência | lista e sim / não por campo |
| Versões históricas | Versões consolidadas listadas pela fonte; datas; cada uma obtida como objeto distinto?; original distinguível do consolidado? | contagem e sim / não |
| Vínculos entre atos | Relações devolvidas como dado estruturado (altera, alterado por, revoga, base jurídica, ato delegado ou de execução ligado); contagem por tipo | contagens |
| Rastreabilidade | URL ou endpoint; parâmetros exatos; data e hora UTC; versão do serviço, se informada; código de resposta | registro |
| Operação | Número de passos manuais; exigência de conta; falhas e novas tentativas; tempo, se medido | registro |
| Incerteza | Qualquer observação que o operador não conseguiu determinar, com o motivo | texto |

Os campos de identificação e de versão seguem a seção 8 da taxonomia. Arquivos obtidos ficam fora do controle de versão quando a licença não permitir redistribuição; os manifestos com hash são sempre versionados.

### 4.6 Funções específicas

- **Autor do procedimento:** escreve o passo a passo por configuração. Pode ser assistido por agente de IA; o texto é revisto por pessoa.
- **Operador 1 e Operador 2:** executam separadamente, em datas registradas. O Operador 2 recebe **apenas** o procedimento escrito.
- **Julgamentos** (por exemplo, "a integridade é adequada") **não são feitos no piloto**. O piloto registra observações. Os julgamentos pertencem a G4 e G5, com o quadro de seleção.

### 4.7 Indicadores

Por par nomeado de operadores e por configuração; nunca agregados entre pares.

| Indicador | Definição |
|---|---|
| Reprodutibilidade de arquivo | Atos em que os dois operadores obtiveram arquivo com o mesmo SHA-256 / atos obtidos por ambos. Diferenças classificadas por causa (conteúdo, metadado embutido, data de geração, erro) |
| Concordância em observações binárias | Por observação: tabela cruzada sim / não / não determinado, com concordância bruta |
| Concordância em contagens | Por contagem: proporção de valores idênticos e maior diferença absoluta |
| Completude do registro | Linhas com todos os campos de rastreabilidade preenchidos / linhas |
| Aplicabilidade da medida | Para cada observação, número de configurações em que ela pôde ser registrada |
| Incerteza | Proporção de "não determinado" por observação e por configuração |

### 4.8 Critérios de passagem propostos

| ID | Condição | Verificação |
|---|---|---|
| PB1 | Lista de atos, textos de referência, configurações e critérios de passagem trancados com data anterior à primeira consulta | Hashes e datas |
| PB2 | O Operador 2 concluiu o procedimento só com o texto escrito; cada pedido de esclarecimento foi registrado e virou correção do procedimento | Registro de esclarecimentos |
| PB3 | Completude do registro de rastreabilidade integral, ou cada lacuna explicada | Indicador de completude |
| PB4 | Toda diferença entre operadores tem causa atribuída. Diferença de conteúdo sem explicação é achado a relatar, não defeito a esconder | Ata |
| PB5 | Cada medida é aplicável a todas as configurações testadas, ou foi redefinida, ou foi declarada específica de um tipo de configuração | Indicador de aplicabilidade |
| PB6 | Para cada ato, a medida de integridade tem referência definida, ou foi renomeada como consistência entre fontes | Lista de atos |
| PB7 | Há estimativa de esforço por ato e por configuração para dimensionar G5 | Registro de operação |
| PB8 | Alerta numérico, com valor fixado antes pela equipe, sobre a reprodutibilidade de arquivo: abaixo dele, o procedimento volta à revisão. Atingi-lo não dispensa PB1–PB7 | Indicador |
| PB9 | Adjudicador e coordenação científica assinam | Assinaturas |

### 4.9 Quando o Piloto B é executado

Duas opções; a escolha é da equipe.

| Opção | Sequência | Vantagem | Custo |
|---|---|---|---|
| B-tardio | Desenho aprovado em G1; execução no início de G5, depois que G2–G3 definiram o conjunto de candidatos | As configurações testadas são as do inventário adjudicado | Problemas do protocolo de benchmark só aparecem tarde |
| B-antecipado | Desenho aprovado em G1; execução logo depois, sobre configurações já conhecidas pelo inventário exploratório | Protocolo amadurece cedo; informa o desenho de G4 | Usa candidatos ainda não triados; exige autorização explícita, porque envolve obter textos de fontes externas; não pode ser lido como avaliação |

Em qualquer das opções, o piloto exige autorização expressa para consultar fontes externas e obter arquivos. **Nada disso foi feito nesta fase.**

### 4.10 Produtos

Lista de atos e referências, trancada; procedimentos por configuração; dois registros de execução; manifestos com hashes; comparação descritiva; ata; protocolo de benchmark revisto; estimativa de esforço.

---

## 5. Decisões que este desenho deixa para a equipe

1. Lista intencional do Piloto A (seção 3.3) ou sorteio com restrições (seção 3.4).
2. Quem são os avaliadores, operadores, coordenador e adjudicador; se quem construiu o inventário pode avaliar.
3. Critérios de passagem PA1–PA8 e PB1–PB9: aprovar, alterar ou substituir; fixar os valores de alerta de PA7 e PB8 e o número de registros da rodada de confirmação.
4. Parâmetros U1–U6 do quadro de seleção, sem os quais os atos de referência não podem ser escolhidos.
5. Número de atos de referência; uso ou não de âncoras e de atos sorteados; quem seleciona.
6. O que conta como texto de referência.
7. B-tardio ou B-antecipado; autorização para consultar fontes.
8. Meio de arquivamento das capturas de evidência.

## 6. Estatuto das afirmações

| Afirmação | Classe |
|---|---|
| Os 20 identificadores do Piloto A e os 21 da reserva existem no inventário; cobertura de 11 famílias; prioridades 8/10/2 | VERIFIED |
| Diferenças em relação à amostra do G0 (13 mantidos, 5 retirados, 7 acrescentados) | VERIFIED |
| A "função no piloto" de cada registro corresponde ao que o recurso realmente é | PENDING VALIDATION (é hipótese lida do inventário; nenhuma página foi acessada) |
| As cópias locais de atos das etapas R4 e R5 servem como texto de referência | PENDING VALIDATION |
| Existe configuração de mantenedor independente do candidato prioritário | PENDING VALIDATION (G2–G3) |
| Composição das amostras, critérios de passagem, opção de calendário do Piloto B | PROPOSED |
| Qualquer resultado de avaliação, concordância ou adjudicação | Inexistente |
