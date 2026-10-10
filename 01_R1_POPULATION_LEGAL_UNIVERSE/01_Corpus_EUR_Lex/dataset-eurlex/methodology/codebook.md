# Codebook operacional — Regulatory Intermediation R–I–T

**Projeto:** `dataset-eurlex`  
**Versão:** 1.0.0  
**Estado:** bloqueado após validação da Etapa 3  
**Escopo:** um ato normativo, uma codificação de referência e três condições experimentais

## 1. Princípio e unidade de análise

O constructo focal é **intermediação regulatória como relação**, não como atributo permanente de uma organização.

```text
R — I — T
```

- `R`: regulador ou autoridade regulatória na relação focal;
- `I`: terceiro ator analiticamente distinto que desempenha função regulatória mediadora;
- `T`: destinatário, rule-taker ou alvo cuja conduta, informação, produto, processo ou conformidade está sujeito à regulação.

### Unidade primária

A unidade de análise é uma **relação regulatória candidata ancorada em uma disposição jurídica**. A mesma disposição pode gerar mais de uma unidade quando contém relações materialmente distintas. Uma relação não deve ser duplicada apenas porque a mesma frase usa vários verbos para a mesma função.

O identificador `candidate_id` será atribuído ao universo de candidatos da Etapa 4. O codebook não cria IDs a partir de trabalhos anteriores.

### Regra de localização

Cada unidade deve apontar para a menor localização jurídica suficiente, usando quando disponível:

- CELEX;
- artigo;
- parágrafo;
- alínea/ponto;
- subparágrafo;
- recital, quando usado como contexto interpretativo;
- excerto literal.

Recitals podem contextualizar finalidade, atores e conceitos, mas não são tratados automaticamente como obrigações equivalentes ao articulado.

## 2. Limites da evidência

O texto fornecido é a autoridade evidencial da codificação. Não completar lacunas com legislação externa, conhecimento institucional, prática administrativa, doutrina, jurisprudência ou expectativa sobre como um regime normalmente funciona.

O fluxo obrigatório é:

```text
EVIDÊNCIA JURÍDICA → INTERPRETAÇÃO INSTITUCIONAL → CÓDIGO
```

Strings indicam saliência para screening. `lexical_hit` nunca equivale a `intermediary`.

## 3. Atores e papéis relacionais

Um ator só recebe papel dentro de uma relação específica. O mesmo ator pode ser `I` em uma relação, `T` em outra e `R` em outra.

### Papéis auxiliares

Registrar, quando o texto sustentar:

- `rule_source`: fonte formal da regra;
- `standard_setter`: ator que fixa padrão ou critério;
- `direct_regulator`: ator que dirige a relação regulatória focal;
- `oversight_authority`: ator que supervisiona ou acompanha;
- `enforcement_authority`: ator com função sancionatória ou de execução;
- `intermediary`: terceiro que medeia a relação;
- `target`: destinatário ou alvo regulado.

O órgão que adotou o regulamento não é automaticamente o `direct_regulator` da relação analisada.

### Ator

`actor` deve representar uma entidade, órgão, grupo ou papel institucional juridicamente identificável. Não codificar uma palavra institucional sem evidência de função ou participação relevante.

### Destinatário/alvo

`target` é o ator, atividade, informação, produto, processo ou estado de conformidade diretamente submetido à exigência focal. Se o objeto não permitir identificar um alvo responsável, marcar a incerteza em vez de inventar um `T`.

## 4. Critérios de inclusão e exclusão

### Incluir como candidato

Incluir uma unidade quando o texto:

1. estabelece, atribui, exige, autoriza, supervisiona, verifica, certifica, audita, acredita, avalia, monitora ou reporta uma relação regulatória;
2. permite identificar pelo menos parte dos atores, ação/função e objeto;
3. oferece localização e evidência literal suficientes para análise;
4. pode sustentar teste explícito das cinco condições R–I–T, mesmo que o resultado final seja negativo, condicional ou insuficiente.

### Excluir da codificação substantiva

Excluir como relação regulatória candidata, registrando a razão quando necessário:

- ocorrência lexical sem função normativa relevante;
- menção histórica, bibliográfica ou meramente recitativa sem relação analisável;
- ator citado apenas como exemplo, autoridade de referência ou parte de uma definição, sem ação regulatória focal;
- serviço ou aconselhamento sem função mediadora entre `R` e `T`;
- relação puramente econômica, administrativa ou comunicacional sem mecanismo regulatório identificável;
- informação que só poderia ser estabelecida por fonte externa.

Uma relação direta `T → R` de reporte pode ser registrada como relação regulatória sem intermediário. Ela não deve ser convertida em R–I–T apenas porque contém informação, formulário ou relatório.

## 5. Sequência de codificação

### Fase 1 — extração de atores

Listar atores e papéis textualmente apoiados sem atribuir imediatamente `R`, `I` ou `T`.

### Fase 2 — reconstrução da arquitetura

Representar relações básicas antes do teste R–I–T:

```text
Actor A estabelece exigência para Actor B.
Actor B apresenta informação a Actor A.
Actor C verifica informação produzida por Actor B.
Actor D acredita Actor C.
```

Não colapsar relações diferentes em uma cadeia artificial.

### Fase 3 — reconstrução da candidata R–I–T

Propor `R`, `I` e `T` somente depois de reconstruir a arquitetura. Uma disposição pode conter uma relação direta e outra intermediada, ou relações aninhadas.

### Fase 4 — codificação

Aplicar as cinco condições, codificar mecanismo, instrumento, procedimento, evidência, observabilidade, confiança e incerteza.

## 6. Teste relacional de cinco condições

Cada condição recebe somente `YES`, `NO` ou `UNCLEAR`, com evidência própria.

### Condição A — regulador

Há um `R` identificável na relação focal?

`YES` exige autoridade, regra ou função regulatória juridicamente identificável. O mero autor formal do ato não basta.

### Condição B — alvo

Há um `T` identificável?

`YES` exige destinatário ou objeto regulado identificável no texto. Se a relação não permite localizar o alvo, usar `NO` ou `UNCLEAR` conforme a evidência.

### Condição C — terceiro distinto

Há um terceiro ator analiticamente distinto de `R` e `T`?

Um ator não é terceiro apenas porque aparece na mesma disposição. O papel precisa ser distinto na relação focal.

### Condição D — função mediadora

O terceiro executa função regulatória que medeia a relação entre `R` e `T`?

Advising, participar da elaboração da regra, ser consultado, receber a mesma obrigação ou prestar serviço genérico não é suficiente por si só.

### Condição E — evidência

Há evidência jurídica explícita ou reconstrução institucional claramente documentada a partir do texto fornecido?

Uma reconstrução inferida deve explicar cada passo e não pode depender de fonte externa.

## 7. Resultado relacional

- `positive`: A, B, C, D e E são `YES`.
- `negative`: uma condição estrutural necessária é `NO`, especialmente C ou D; pode também registrar relação direta sem intermediário.
- `conditional`: há relação plausível, mas uma condição material está `UNCLEAR` e poderia ser resolvida com explicitação jurídica adicional.
- `insufficient_evidence`: o texto não permite adjudicação responsável, mesmo com interpretação prudente.

Nunca transformar `UNCLEAR`, `EXTERNAL` ou `NOT_OBSERVABLE` em `positive` para completar a tríade.

## 8. Função, mecanismo, instrumento e procedimento

Manter as categorias separadas:

- **ator:** quem exerce papel institucional;
- **função mediadora:** o que o terceiro faz na relação;
- **mecanismo:** família funcional da atividade regulatória;
- **instrumento:** artefato usado ou produzido;
- **procedimento:** sequência formal de atos, condições ou etapas.

Exemplo abstrato: `verifier` é ator; `verification` é função/mecanismo; `verification report` é instrumento; `accreditation procedure` é procedimento.

### Famílias de mecanismo

Usar, quando sustentado:

- `reporting`;
- `certification`;
- `ranking_rating`;
- `auditing`;
- `other_mechanism`;
- `none_or_direct` quando há relação direta sem intermediação.

Verification, assurance, accreditation, assessment, monitoring e supervision podem ser registrados em `mediating_function` e, quando não couberem nas quatro famílias principais, em `other_mechanism`. Não classificar por palavra-chave isolada.

### Estratégias

Quando a disposição sustentar uma dimensão estratégica, registrar separadamente:

- `responsibilization`: atribuição de responsabilidade de agir, reportar, medir ou demonstrar conformidade;
- `empowerment`: habilitação de atores para participar, produzir informação, contestar ou exercer capacidade regulatória.

As dimensões não são mutuamente exclusivas. Ausência de evidência deve resultar em `not_observable`, não em `NO` substantivo.

## 9. Evidência e observabilidade

### Evidência mínima

Cada atribuição substantiva deve conter:

- localização normativa;
- excerto literal suficiente;
- distinção entre texto direto e interpretação;
- nota de incerteza quando necessário.

Não usar uma citação genérica para sustentar simultaneamente todos os papéis se o texto não os sustentar.

### Classes de observabilidade

- `DIRECT`: o papel, função ou relação está explicitamente no texto fornecido;
- `INFERRED`: reconstrução razoável a partir do texto, explicada passo a passo;
- `EXTERNAL`: exigiria outro documento ou conhecimento não fornecido;
- `NOT_OBSERVABLE`: o constructo não pode ser inferido responsavelmente do texto.

`EXTERNAL` e `NOT_OBSERVABLE` não significam ausência substantiva; significam limite da observação.

### Confiança

`confidence` é uma avaliação da segurança da codificação, não uma probabilidade estatística:

- `high`: evidência direta e relação sem ambiguidade material;
- `medium`: reconstrução plausível com alguma interpretação localizada;
- `low`: elemento relevante depende de inferência ou há ambiguidade significativa;
- `not_assessed`: ainda não avaliada.

## 10. Casos-limite

### Relações compostas

Separar funções quando um mesmo parágrafo exige que um ator reporte e outro verifique, ou quando uma obrigação contém múltiplos alvos materialmente distintos. Manter uma unidade única quando as ações são apenas formulações cumulativas da mesma relação.

### Múltiplos atos na mesma disposição

Uma disposição pode conter mais de uma relação. Criar candidatos distintos somente quando `R`, `I`, `T`, função ou evidência mudarem materialmente. Compartilhar a localização, mas não o `candidate_id`.

### Papéis múltiplos

Codificar cada relação separadamente. Um ator que supervisiona um verificador pode ser `R` em uma relação e o verificador pode ser `T`; isso não torna automaticamente a relação inteira uma única tríade.

### Consultas, assessoria e participação

Consulta, aconselhamento ou participação institucional não são intermediação sem função regulatória mediadora documentada entre `R` e `T`.

### Reporte direto

`T` reportar diretamente a `R` é mecanismo de reporting, mas não constitui intermediação se não houver terceiro mediador. Registrar a relação direta e `I: null` quando ela for relevante para o universo de candidatos.

### Cross-references

Preservar a referência cruzada como aparece no ato. Não importar o texto do ato referido. Se a decisão depender desse texto ausente, marcar `EXTERNAL` ou `NOT_OBSERVABLE`.

### Recitals

Usar recitals como contexto interpretativo e evidência de finalidade quando apropriado. Não codificar obrigação operativa baseada exclusivamente em recital se o articulado não apoiar a relação.

## 11. Abstenção

Abstenção é resultado válido. Quando faltar evidência:

- não inventar ator, alvo, mecanismo ou autoridade;
- dizer exatamente qual elemento não é observável;
- registrar `additional_context_required` somente quando um documento externo específico seria necessário;
- preservar a distinção entre `negative`, `conditional` e `insufficient_evidence`.

Não inferir do texto jurídico efetividade, legitimidade, confiança, captura, autonomia real, accountability real, competência institucional ou resultados de policentricidade.

## 12. Exemplos abstratos de validação

Os exemplos abaixo são testes lógicos, não dados do ato e não devem entrar no corpus ou no benchmark.

### TEST-01 — relação positiva

Uma disposição abstrata estabelece que uma autoridade (`R`) exige que um operador (`T`) apresente dados a um verificador acreditado (`I`), e que o verificador valide os dados e os transmita à autoridade. A–E = `YES`; resultado esperado: `positive`; mecanismo: `auditing` ou `other_mechanism`, conforme a função codificada.

### TEST-02 — reporte direto sem intermediário

Uma disposição abstrata exige que o operador (`T`) entregue diretamente um relatório à autoridade (`R`) e não menciona terceiro que desempenhe função mediadora. C = `NO`, D = `NO`; resultado esperado: `negative`; mecanismo: `reporting`; `I = null`.

### TEST-03 — evidência insuficiente

Uma disposição abstrata menciona um conselho que pode aconselhar a autoridade, mas não identifica alvo regulado nem função entre autoridade e alvo. B e D = `UNCLEAR` ou `NO`, conforme o texto; resultado esperado: `insufficient_evidence` ou `negative`, nunca `positive`.

### TEST-04 — multiplicidade de papéis

Uma disposição abstrata faz um órgão supervisionar um verificador em uma relação e, em outra, exige que o mesmo verificador apresente informação ao órgão. Codificar relações separadas; não atribuir um papel intrínseco permanente ao órgão ou ao verificador.

Esses testes verificam regras decisórias e não ajustam categorias a partir do ato selecionado.
