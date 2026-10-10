# Codebook operacional — Intermediação regulatória R–I–T

**Projeto:** `dataset-eurlex`  
**Versão:** `1.1.0`  
**Estado:** bloqueado após revisão metodológica externa  
**Relação de versão:** supersede `1.0.0` para as etapas futuras, preservando integralmente a versão anterior para auditoria  
**Escopo:** universo de candidatos, benchmark de referência e três condições experimentais

## 1. Escopo, proveniência e independência

Esta versão foi produzida a partir da revisão metodológica externa e de regras abstratas. Nenhum resultado empírico, resposta de agente, codificação, seleção de candidato ou conteúdo substantivo do ato do corpus foi consultado para ajustar o codebook, as strings ou os schemas.

O texto do corpus continua sendo a autoridade evidencial. A metodologia não importa legislação externa, doutrina, jurisprudência, conhecimento institucional ou expectativa sobre como um regime normalmente funciona.

O fluxo obrigatório é:

```text
EVIDÊNCIA JURÍDICA → INTERPRETAÇÃO INSTITUCIONAL → CÓDIGO
```

Strings servem apenas para screening lexical de saliência. Um `lexical hit` não é evidência suficiente de intermediação e não é requisito para um candidato estrutural.

## 2. Unidade de análise e universo de candidatos

A unidade de análise é uma relação regulatória candidata ancorada na menor disposição jurídica suficiente. A mesma disposição pode gerar mais de uma unidade quando contém relações materialmente distintas; não se criam duplicatas apenas porque a mesma frase usa vários verbos para uma única função.

O universo da Etapa 4 será construído por dois canais independentes e complementares:

1. **`lexical screening`**: busca de famílias morfológicas genéricas para maximizar a saliência de possíveis passagens regulatórias;
2. **`structural reading`**: leitura sistemática por artigo, parágrafo, ponto, subparágrafo e recital, procurando relações regulatórias mesmo quando não houver ocorrência de string.

O universo é a união deduplicada dos dois canais, preservando a proveniência:

- `lexical`: encontrado apenas pelo screening lexical;
- `structural`: encontrado apenas pela leitura estrutural;
- `both`: encontrado pelos dois canais.

Um candidato estrutural não depende de `lexical hit`. A deduplicação exige identidade de localização e de relação material; não se descarta silenciosamente uma ocorrência que tenha originado a mesma unidade pelos dois canais.

O identificador `candidate_id` será atribuído ao universo de candidatos da Etapa 4. Este codebook não cria IDs a partir de trabalhos anteriores.

## 3. R–I–T e distinção entre ator e objeto

O constructo focal é **intermediação regulatória como relação**, e não atributo permanente de uma organização:

```text
R — I — T
```

- `R`: regulador, autoridade ou papel institucional que exerce a função regulatória focal;
- `I`: terceiro ator ou papel institucional distinto que desempenha função regulatória mediadora;
- `T`: ator, classe de atores ou papel institucional sujeito à relação regulatória focal.

### Regra obrigatória para `T`

`T` só pode ser um ator, uma classe de atores ou um papel institucional que seja sujeito à relação regulatória. **Atividade, informação, produto, processo, conduta e estado de conformidade nunca são valores de `T`; todos devem ser codificados em `object`.**

Exemplos abstratos:

- uma entidade obrigada a reportar pode ser `T`, e o relatório é `object`;
- uma classe de operadores sujeita a verificação pode ser `T`, e os dados ou a atividade verificada são `object`;
- uma obrigação de manter um processo não torna o processo `T`; o ator responsável pelo processo é `T` e o processo é `object`;
- “estar em conformidade” é um estado de conformidade em `object`, não um ator em `T`.

R, I e T são papéis relacionais. O mesmo ator pode ocupar papéis distintos em relações distintas, mas isso não autoriza converter um objeto textual em ator.

## 4. Campos relacionais

Separar os campos abaixo, sem preencher lacunas por plausibilidade:

- `action`: ação normativa ou institucional atribuída;
- `object`: atividade, informação, produto, processo, conduta, estado de conformidade ou outro objeto da ação;
- `mediating_function`: função exercida pelo intermediário, quando houver;
- `instrument`: artefato utilizado ou produzido;
- `procedure`: sequência formal de atos, condições ou etapas;
- `primary_mechanism` e `secondary_mechanisms`: famílias funcionais de mecanismo;
- `relational_result`: resultado da adjudicação de referência;
- `decision`: saída neutra comum a G0/G1/G2.

O ato formal que criou ou publicou uma norma não é automaticamente `R`. O papel deve ser sustentado pela relação focal. Da mesma forma, uma entidade mencionada na mesma disposição não é automaticamente `I`.

## 5. Atores e papéis auxiliares

Registrar, quando o texto sustentar:

- `rule_source`: fonte formal da regra;
- `standard_setter`: ator que fixa padrão ou critério;
- `direct_regulator`: ator que dirige a relação regulatória focal;
- `oversight_authority`: ator que supervisiona ou acompanha;
- `enforcement_authority`: ator com função sancionatória ou de execução;
- `intermediary`: terceiro que medeia a relação;
- `target`: destinatário ou alvo regulado, sempre um ator ou papel institucional.

Uma relação direta `T → R` pode ser relevante mesmo sem `I`. Ela não deve ser convertida em relação intermediada apenas porque envolve formulário, relatório, informação ou processo.

## 6. Regras de inclusão e exclusão

### Incluir como candidato

Incluir uma unidade quando o texto:

1. estabelece, atribui, exige, autoriza, supervisiona, verifica, certifica, audita, acredita, avalia, monitora, reporta ou coordena uma relação regulatória;
2. permite identificar pelo menos parte dos atores, da ação, do objeto ou da função;
3. oferece localização e evidência literal suficientes para análise;
4. permite teste prudente da relação, inclusive quando o resultado for negativo, condicional ou insuficiente.

### Excluir da codificação substantiva

Registrar como `not_candidate` quando houver apenas:

- ocorrência lexical sem função normativa relevante;
- menção histórica, bibliográfica ou contextual sem relação analisável;
- ator citado como exemplo ou referência, sem ação regulatória focal;
- serviço ou aconselhamento sem função mediadora entre R e T;
- relação sem mecanismo regulatório identificável;
- atribuição que só poderia ser estabelecida por fonte externa.

## 7. Sequência de codificação de referência

1. Extrair atores e papéis textualmente apoiados, sem atribuir automaticamente R, I ou T.
2. Reconstruir relações básicas antes do teste R–I–T.
3. Propor R, I e T somente depois de reconstruir a arquitetura.
4. Separar `object` de `T`, verificando especialmente atividades, informações, produtos, processos, condutas e estados de conformidade.
5. Aplicar as cinco condições, registrar evidência por condição e atribuir resultado.
6. Codificar mecanismo, instrumento, procedimento, confiança e limites de observação.

## 8. Teste relacional de cinco condições — apenas referência

Cada condição recebe `YES`, `NO` ou `UNCLEAR` e referências aos itens de evidência que a sustentam. Essas condições pertencem ao schema de referência R1/R2/RA e ao benchmark; não aparecem no schema de saída experimental.

### Condição A — regulador

Há um `R` identificável na relação focal?

### Condição B — alvo

Há um `T` identificável, sendo T necessariamente ator, classe de atores ou papel institucional sujeito à relação?

### Condição C — terceiro distinto

Há um terceiro ator analiticamente distinto de R e T?

### Condição D — função mediadora

O terceiro executa função regulatória que medeia a relação entre R e T?

### Condição E — evidência

Há evidência jurídica explícita ou reconstrução institucional claramente documentada a partir do texto fornecido?

## 9. Resultado relacional e status de screening

`screening_status` registra a situação do candidato no universo: `candidate`, `direct_relationship`, `not_candidate` ou `insufficient_evidence`.

`relational_result` registra a adjudicação da relação: `positive`, `negative`, `conditional` ou `insufficient_evidence`. A separação evita duplicar o mesmo conceito com `candidate_status` e `final_relational_result`.

- `positive`: A, B, C, D e E são `YES`;
- `negative`: uma condição estrutural necessária é `NO`, especialmente C ou D, ou a relação é direta sem intermediário;
- `conditional`: há relação plausível, mas uma condição material está `UNCLEAR`;
- `insufficient_evidence`: o texto não permite adjudicação responsável.

Nunca transformar `UNCLEAR`, `EXTERNAL` ou `NOT_OBSERVABLE` em `positive` para completar a tríade.

## 10. Evidência e observabilidade

O schema de referência usa `evidence_items` como registro central de evidência. Cada item contém localização, citação literal, papel da evidência, classe de observabilidade e referências aos campos que apoia. Não há campos paralelos `evidence`, `excerpt` e `verbatim_evidence`.

As classes por item são:

- `DIRECT`: papel, função ou relação explicitamente no texto fornecido;
- `INFERRED`: reconstrução razoável a partir do texto, explicada na nota interpretativa;
- `EXTERNAL`: exigiria outro documento ou conhecimento não fornecido;
- `NOT_OBSERVABLE`: não pode ser inferido responsavelmente do texto.

Não há uma classe de observabilidade global concorrente com a classificação dos itens.

## 11. Mecanismos

Usar a família que o texto sustentar, sem classificar por palavra-chave isolada:

| Código | Uso metodológico |
|---|---|
| `reporting` | produção ou entrega regulatória de informação ou relatório |
| `verification` | conferência, validação ou confirmação de informação ou condição |
| `certification` | certificação formal de condição, produto, processo ou resultado |
| `auditing` | exame sistemático, auditoria ou asseguração formal |
| `monitoring_supervision` | acompanhamento, monitoramento ou supervisão contínua |
| `ranking_rating` | classificação, pontuação ou avaliação comparativa |
| `standard_setting` | definição de padrão, critério, referência ou requisito |
| `enforcement_support` | apoio à execução, sanção, correção ou cumprimento |
| `coordination` | coordenação formal entre atores ou unidades |
| `information_transmission` | transmissão, comunicação ou intercâmbio de informação |
| `delegated_implementation` | implementação delegada ou execução atribuída a outro ator |
| `accreditation` | reconhecimento formal de competência ou habilitação |
| `other_mechanism` | mecanismo sustentado que não cabe nas famílias anteriores |
| `none_or_direct` | relação direta sem mecanismo mediador identificável |

`mediating_function` descreve o que o ator faz; `mechanism` descreve a família funcional. `instrument` e `procedure` permanecem distintos.

## 12. Dimensões secundárias opcionais

`responsibilization` e `empowerment` são dimensões secundárias opcionais. Não fazem parte do núcleo obrigatório R–I–T e podem ser omitidas quando não forem pertinentes ou observáveis.

- `responsibilization`: atribuição de responsabilidade de agir, reportar, medir ou demonstrar conformidade;
- `empowerment`: habilitação de atores para participar, produzir informação, contestar ou exercer capacidade regulatória.

Quando presentes, cada dimensão recebe `YES`, `NO`, `UNCLEAR` ou `NOT_OBSERVABLE`, com evidência associada. Ausência do campo não equivale a `NO`.

## 13. Confiança, abstenção e casos-limite

`confidence` é uma avaliação da segurança da codificação, não uma probabilidade estatística:

- `high`: evidência direta e relação sem ambiguidade material;
- `medium`: reconstrução plausível com interpretação localizada;
- `low`: elemento relevante depende de inferência ou tem ambiguidade significativa;
- `not_assessed`: ainda não avaliada.

Quando faltar evidência, não inventar ator, alvo, mecanismo ou autoridade. Dizer qual elemento não é observável e registrar contexto adicional apenas quando um documento externo específico seria necessário.

Separar relações compostas quando R, I, T, função ou evidência mudarem materialmente. Recitals podem fornecer contexto interpretativo, mas não constituem automaticamente obrigação operativa. Cross-references não importam texto de outro ato; se a decisão depender dele, registrar o limite observacional.

Não inferir efetividade, legitimidade, captura, autonomia real, accountability real, competência institucional ou resultados de policentricidade.

## 14. Interfaces e isolamento experimental

O `reference_coding_schema.json` é destinado a R1/R2/RA e ao benchmark. Ele contém o teste A–E, classes de observabilidade e dimensões secundárias opcionais para permitir adjudicação e auditoria.

O `experimental_output_schema.json` é comum a G0/G1/G2 e contém apenas a estrutura mínima comparável: localização, evidência, R, I, T, ação, objeto, função, mecanismo, decisão, confiança e notas, além da origem do candidato. Ele não contém as condições A–E, descrições do codebook, taxonomias explicativas de observabilidade, `responsibilization`, `empowerment` ou instruções de scaffolding.

Os testes abstratos desta versão verificam regras lógicas gerais e não são dados do ato, não são benchmark e não foram ajustados com conteúdo empírico.
