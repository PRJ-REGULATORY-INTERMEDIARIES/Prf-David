# R3 — REGISTRO DE APRENDIZADO E PLANO DE NOVO PILOTO CLEAN-ROOM

**Projeto:** Regulatory Intermediation — David Levi-Faur  
**Rodada:** R3  
**Status:** Novo início metodológico e empírico  
**Princípio central:** construir tudo de novo, em pasta nova, sem utilizar datasets, codificações, corpora, classificações ou outputs anteriores como base empírica.

---

## 1. Objetivo deste registro

Este documento consolida os aprendizados acumulados a partir:

1. do feedback metodológico de David Levi-Faur;
2. do material enviado por David sobre o exercício de Ivana;
3. das discussões metodológicas sobre unidade de análise, mecanismos e arquitetura do dataset;
4. das decisões tomadas durante as rodadas anteriores.

O documento NÃO é um dataset e NÃO deve ser utilizado como ground truth para codificação.

Ele funciona apenas como **registro de aprendizado metodológico** e como **ponte conceitual para o novo Piloto R3**.

O R3 será construído integralmente do zero.

---

# PARTE I — APRENDIZADOS CONSOLIDADOS

## 2. Aprendizado central: intermediação não é presença de terceiro ator

A presença de três atores não demonstra, por si só, uma relação de intermediação.

Não utilizar:

> R + terceiro ator + T = intermediação.

A identificação de intermediação requer demonstrar uma função mediadora concreta.

A pergunta central passa a ser:

> O que o ator intermediário faz que efetivamente medeia uma relação regulatória entre R e T?

---

## 3. Teste mínimo para identificar regulatory intermediation

Uma relação deve satisfazer cumulativamente três condições:

### 3.1 Relação R–T identificável

Deve existir uma relação regulatória identificável entre um regulador e um target.

Essa relação pode ser:

- explícita no mesmo dispositivo;
- reconstruída entre dispositivos;
- excepcionalmente inferida de contexto, com cautela.

### 3.2 Terceiro ator institucionalizado

O ator I deve ter um papel institucionalmente reconhecido e distinto de R e T naquela relação.

A institucionalização é evidência relevante, mas não é suficiente.

### 3.3 Função mediadora demonstrável

O ator deve realizar alguma transformação relevante para a relação R–T.

Exemplos de operações possíveis:

- transmitir;
- traduzir;
- agregar;
- interpretar;
- avaliar;
- classificar;
- representar;
- monitorar;
- verificar.

---

## 4. Bindingness não é critério suficiente

O output do intermediário não precisa ser juridicamente vinculante.

Separar sempre:

- obrigatoriedade do procedimento;
- força jurídica do output;
- existência de intermediação.

Consulta obrigatória não implica automaticamente intermediação.

Advice não vinculante pode ser intermediação, desde que exista uma função mediadora demonstrável.

---

## 5. Advice e expertise não bastam

Um expert body, advisory board, committee ou consultant não é intermediary apenas porque fornece expertise.

A pergunta deve ser:

> Que transformação o ator produz dentro da relação regulatória?

Exemplo conceitual:

Fraco:

> Platform advises Commission.

Forte:

> Platform recebe conhecimento técnico e científico, avalia e traduz esse material em critérios ou recomendações que entram na regulação de targets identificáveis.

---

## 6. Artigos são unidades de evidência, não necessariamente unidades substantivas de análise

A leitura artigo por artigo continua necessária.

Mas o artigo não deve ser tratado como uma unidade regulatória autossuficiente.

A análise deve começar pelo instrumento completo.

Sequência recomendada:

1. compreender a lei como um todo;
2. identificar objetivo e objeto regulatório;
3. mapear atores;
4. reconstruir relações;
5. identificar intermediários;
6. identificar mecanismos;
7. retornar aos artigos como evidência.

---

## 7. Unidade comparativa sugerida por David: LAW–INTERMEDIARY

O feedback de David ao trabalho de Ivana introduziu um ponto metodológico decisivo:

> cada intermediary deve ter sua própria linha dentro da mesma law.

Portanto, o novo desenho deve incorporar explicitamente:

**LAW × INTERMEDIARY**

como unidade comparativa principal.

Isso não elimina unidades subordinadas.

Arquitetura sugerida:

**LAW → LAW–INTERMEDIARY → RELATION → MECHANISM EVENT → EVIDENCE**

---

## 8. O ator não deve carregar um papel fixo

R, I e T devem ser tratados como papéis relacionais.

Um mesmo ator pode potencialmente ocupar papéis diferentes em relações diferentes.

Contudo, esse role switching deve permanecer sujeito a revisão.

Não assumir automaticamente.

Criar flag:

`ROLE_SWITCH_REVIEW`

---

## 9. Cross-provision reconstruction é necessária

R, I e T não precisam aparecer no mesmo artigo.

Uma relação pode ser reconstruída entre diferentes dispositivos.

Toda reconstrução deve registrar separadamente a evidência de:

- R;
- I;
- T;
- relação R–T;
- função de I;
- mecanismo.

Níveis de evidência:

- `E1_EXPLICIT`
- `E2_CROSS_PROVISION_RECONSTRUCTED`
- `E3_INFERRED_CONTEXTUAL`

---

# PARTE II — MECANISMOS

## 10. Regra fundamental de mecanismo

Não codificar mecanismo a partir do nome do ator.

Não utilizar:

> Auditor = verification.

Em vez disso:

> actor + input + transformação + output + destinatário → mecanismo.

Pergunta operacional:

> Quem recebe o quê, transforma como, produz o quê, para quem, e com qual importância para a relação regulatória?

---

## 11. Nove mecanismos operacionais

### Família didática 1 — ARTICULAÇÃO

#### 11.1 TRANSMISSION

Move informação, sinal, relatório, obrigação ou demanda de um ator para outro.

Pergunta:

> O que está sendo transportado de A para B?

#### 11.2 AGGREGATION

Combina múltiplos inputs em um output consolidado.

Pergunta:

> Muitos inputs estão sendo sintetizados em um resultado organizado?

#### 11.3 REPRESENTATION

Articula interesses, experiências ou preferências de uma constituency.

Pergunta:

> Em nome de quem o intermediário fala?

---

### Família didática 2 — TRATAMENTO DA INFORMAÇÃO

#### 11.4 TRANSLATION

Converte conteúdo de um registro para outro.

Exemplos:

- ciência → critério regulatório;
- princípio abstrato → procedimento;
- regra → orientação prática.

#### 11.5 INTERPRETATION

Estabiliza ou esclarece o significado de uma regra, standard ou conceito.

Pergunta:

> O que essa regra significa?

#### 11.6 EVALUATION / ASSESSMENT

Aplica critérios, conhecimento ou julgamento a evidência, proposta, comportamento ou claim.

Pergunta:

> Que julgamento é produzido e com base em quais critérios?

#### 11.7 CLASSIFICATION / RANKING

Transforma complexidade em categoria, score, rating, status ou ordenação.

Pergunta:

> O intermediário atribui uma categoria ou posição?

---

### Família didática 3 — CONFIABILIDADE REGULATÓRIA

#### 11.8 MONITORING

Observa comportamento, performance ou condição ao longo do tempo.

Pergunta:

> O que está acontecendo com o target?

#### 11.9 VERIFICATION

Confere se uma alegação, condição ou comportamento corresponde a um standard previamente definido.

Pergunta:

> A alegação ou condição de compliance é sustentada pela evidência?

---

## 12. As famílias 3–4–2 são hipótese didática, não teoria validada

A organização:

- 3 mecanismos de articulação;
- 4 mecanismos de tratamento da informação;
- 2 mecanismos de confiabilidade regulatória;

é uma ferramenta de organização e memória.

Não deve ser apresentada como classificação publicada por David.

Ela poderá futuramente ser testada empiricamente.

Possibilidades futuras:

- análise de coocorrência;
- cluster analysis;
- análise fatorial, se houver N adequado;
- network analysis;
- análise de sequências.

---

# PARTE III — TECNOLOGIAS, FUNÇÕES E EFEITOS

## 13. Não confundir mecanismo com tecnologia institucional

Exemplos de tecnologias compostas:

- audit;
- testing;
- certification;
- accreditation;
- environmental impact assessment.

Essas tecnologias podem conter vários mecanismos.

Exemplo:

**certification**
- verification;
- evaluation;
- classification;
- transmission.

---

## 14. Não confundir mecanismo com função

Exemplos de função:

- advice;
- expertise;
- oversight;
- implementation support;
- compliance support.

A função responde:

> para que serve?

O mecanismo responde:

> como a mediação ocorre?

---

## 15. Não confundir mecanismo com efeito sistêmico

Exemplos:

- assurance;
- trust;
- credibility;
- legitimacy;
- compliance.

Esses podem ser resultados de combinações de mecanismos.

---

# PARTE IV — APRENDIZADOS DO EXERCÍCIO DE IVANA

## 16. Utilidade do material

O exercício de Ivana mostra uma tentativa paralela de operacionalizar o mesmo programa de pesquisa.

Ele não deve ser usado como ground truth.

Ele serve como fonte de perguntas e variáveis úteis.

---

## 17. Correção metodológica de David a Ivana

David pediu explicitamente:

1. resumo da law em explanatory note;
2. uma linha por `law–intermediary`;
3. elaboração de research questions teóricas e empíricas que o database deverá responder.

Esse terceiro ponto é especialmente importante:

> o coding scheme deve ser calibrado pelas perguntas científicas que o dataset permitirá responder.

---

## 18. Variáveis úteis identificadas no exercício

Variáveis a considerar no novo R3:

### 18.1 Institutionalization / formality

Possíveis categorias:

- `MANDATORY`
- `OPTIONAL_LEGAL`
- `VOLUNTARY_RECOGNIZED`
- `SELF_INITIATED`

### 18.2 Separation from target

Avaliar independência institucional, organizacional ou funcional do intermediary.

### 18.3 Capacity brought to governance

Possíveis dimensões:

- expertise;
- independence;
- operational capacity;
- legitimacy;
- information access;
- technical capacity.

### 18.4 Legal effect of intermediary output

Possível escala categórica:

- `INFORMATION_ONLY`
- `ADVISORY`
- `SUPPORTING_EVIDENCE`
- `MUST_BE_CONSIDERED`
- `COMPLIANCE_EVIDENCE`
- `ESTABLISHES_STATUS`
- `BINDING_DECISION`

### 18.5 Accountability

Perguntas:

- accountable to whom?
- for what?
- through which procedure?
- with which consequences?

### 18.6 Meta-intermediation

Pergunta:

> Quem supervisiona, verifica ou acredita o intermediary?

Isso permite observar chains como:

`R → I2 → I1 → T`

---

# PARTE V — PERGUNTAS TEÓRICAS EMERGENTES

## 19. Pergunta ampla

> How is regulatory intermediation architected across EU climate regulation?

Essa formulação deve ser tratada como hipótese de trabalho, não como teoria já estabelecida.

---

## 20. Perguntas derivadas

O novo dataset deve ser capaz de explorar perguntas como:

1. Quais funções regulatórias são atribuídas a intermediários?
2. Quais tipos de intermediários estão associados a quais mecanismos?
3. Quais mecanismos aparecem isoladamente e quais formam cadeias recorrentes?
4. Como a institucionalização do intermediary se relaciona ao efeito jurídico de seu output?
5. Quando a intermediação permanece triádica e quando se transforma em chain of intermediation?
6. Quem controla os intermediários?
7. Quais mecanismos regulam os próprios intermediários?
8. Intermediários regulator-facing utilizam mecanismos diferentes de target-facing intermediaries?
9. Qual a relação entre independência do intermediary e mecanismos de monitoring/verification?
10. Diferentes instrumentos apresentam diferentes perfis de articulação, tratamento da informação e confiabilidade regulatória?
11. O objetivo declarado do instrumento corresponde à arquitetura de mecanismos observada?
12. Quais padrões de regulatory intermediation se repetem entre diferentes instrumentos climáticos?

---

# PARTE VI — DECISÃO R3: RECOMEÇAR DO ZERO

## 21. Princípio CLEAN-ROOM

R3 será construído em uma nova pasta.

Não utilizar como base empírica:

- Pilot A;
- R2.1;
- v1.3;
- v1.4;
- datasets enviados a David;
- corpora antigos;
- classificações antigas;
- relações previamente identificadas;
- mechanism assignments anteriores;
- notas de adjudicação;
- outputs de modelos anteriores.

O novo agente pode utilizar:

- este registro de aprendizado metodológico;
- textos teóricos explicitamente autorizados;
- fontes jurídicas oficiais adquiridas novamente;
- instruções e decisões de pesquisa expressamente fornecidas para R3.

---

## 22. Pasta proposta

Criar:

`R3_CLEANROOM/`

Subestrutura recomendada:

```text
R3_CLEANROOM/
├── 00_governance/
├── 01_sources/
├── 02_corpus/
├── 03_instrument_profiles/
├── 04_actor_register/
├── 05_law_intermediary/
├── 06_relations/
├── 07_mechanisms/
├── 08_evidence/
├── 09_research_questions/
├── 10_dataset/
├── 11_audits/
└── 12_reports/
```

---

# PARTE VII — NOVO PILOTO R3 COM CINCO CASOS

## 23. Casos selecionados anteriormente

R3 utilizará os cinco casos substantivos já selecionados anteriormente:

1. `32003L0087`
2. `32015D1814`
3. `32018R0842`
4. `32021R1119`
5. `32023R0955`

O caso `32000D0293` permanece excluído como falso positivo histórico.

R3 deve tratar os cinco casos como novos casos.

Não utilizar codificação anterior.

---

# PARTE VIII — NOVA ARQUITETURA DO DATASET

## 24. Nível 1 — INSTRUMENT

Uma linha por law.

Campos mínimos:

- `instrument_id`
- `celex_id`
- `official_title`
- `instrument_type`
- `date`
- `legal_basis`
- `policy_domain`
- `declared_regulatory_objective`
- `regulatory_object`
- `principal_targets`
- `primary_regulatory_authorities`
- `scope`
- `declared_orientation`

---

## 25. Nível 2 — LAW_INTERMEDIARY

Uma linha por combinação:

`LAW × INTERMEDIARY`

Campos mínimos:

- `law_intermediary_id`
- `instrument_id`
- `intermediary_actor_id`
- `intermediary_name`
- `intermediary_type`
- `institutionalization`
- `separation_from_target`
- `capacity_brought`
- `centrality`
- `output_legal_effect`
- `accountability_to_whom`
- `accountability_mechanism`
- `sanctions_or_consequences`
- `orientation`
- `notes`

---

## 26. Nível 3 — RELATION

Uma linha por relação reconstruída.

Campos:

- `relation_id`
- `law_intermediary_id`
- `R_actor`
- `I_actor`
- `T_actor`
- `regulatory_object`
- `relation_purpose`
- `relation_description`
- `intermediation_status`
- `evidence_level`
- `role_switch_review`
- `researcher_review_flag`

Status:

- `SUPPORTED_INTERMEDIATION`
- `DIRECT_R_T`
- `LEGAL_RELATION_NON_RIT`
- `UNCERTAIN`
- `NOT_SUPPORTED`

---

## 27. Nível 4 — MECHANISM EVENT

Uma relação pode ter vários mecanismos.

Campos:

- `mechanism_event_id`
- `relation_id`
- `mechanism_code`
- `mechanism_family`
- `primary_or_secondary`
- `input`
- `mediated_object`
- `transformation`
- `output`
- `recipient`
- `mechanism_trace`
- `confidence`

Template:

> [I] recebe/observa [X], transforma por [M], produz [Y], e esse output entra na regulação de [T] por [R].

---

## 28. Nível 5 — LEGAL EVIDENCE

Campos:

- `evidence_id`
- `relation_id`
- `mechanism_event_id`
- `article`
- `paragraph`
- `recital`
- `annex`
- `text_excerpt_or_paraphrase`
- `evidence_function`
- `source_location`
- `evidence_level`

---

## 29. Nível 6 — RESEARCH QUESTION MAP

Criar uma tabela que conecte cada variável do dataset a perguntas científicas.

Campos:

- `research_question_id`
- `research_question`
- `theoretical_or_empirical`
- `variables_required`
- `unit_of_analysis`
- `expected_comparison`
- `status`
- `notes`

Esse componente responde diretamente ao pedido de David.

---

# PARTE IX — PRINCÍPIO DE EXECUÇÃO DO R3

## 30. Novo corpus, nova aquisição

Para cada um dos cinco CELEX:

1. adquirir novamente o texto oficial;
2. registrar URL, data, versão e hash;
3. construir novo corpus;
4. não reutilizar corpora antigos;
5. verificar integridade;
6. congelar a fonte antes da codificação.

---

## 31. Ordem de análise

Para cada law:

### Etapa A
Leitura global do instrumento.

### Etapa B
Instrument profile.

### Etapa C
Actor register.

### Etapa D
Law–intermediary register.

### Etapa E
Relations.

### Etapa F
Mechanism events.

### Etapa G
Legal evidence.

### Etapa H
Mechanism chains.

### Etapa I
Research-question relevance.

### Etapa J
Comparação entre os cinco instrumentos.

---

## 32. Regra de independência

Nenhum resultado anterior deve ser utilizado para confirmar, negar ou calibrar uma classificação durante a construção do R3.

Somente depois do fechamento do novo dataset poderá existir uma rodada separada de comparação histórica.

Essa comparação deve ser explicitamente pós-codificação.

---

# PARTE X — CRITÉRIO DE SUCESSO DO R3

O novo R3 deve ser capaz de responder, para cada law:

1. O que a law pretende regular?
2. Quem são os regulators?
3. Quem são os targets?
4. Quais intermediaries aparecem?
5. Qual é a unidade `law–intermediary`?
6. Que relações cada intermediary integra?
7. Qual mecanismo ocorre em cada relação?
8. Que objeto é mediado?
9. Qual transformação ocorre?
10. Qual output é produzido?
11. Para quem?
12. Qual a força jurídica do output?
13. Como o intermediary é institucionalizado?
14. Como o intermediary é responsabilizado?
15. Quem controla o intermediary?
16. Existem meta-intermediaries?
17. Existem chains of intermediation?
18. Quais famílias de mecanismos aparecem?
19. Qual arquitetura de intermediação emerge em cada law?
20. Quais perguntas teóricas o conjunto dos cinco casos permite explorar?

---

# 33. Estado final deste documento

Este arquivo registra aprendizado metodológico.

Ele não deve ser utilizado como dataset ou como fonte de classificações empíricas.

Status:

`R3_LEARNING_REGISTER_COMPLETE`

Próximo passo:

> elaborar o prompt operacional CLEAN-ROOM do R3, com fases, auditorias e paradas obrigatórias, para construir do zero os cinco casos selecionados.
