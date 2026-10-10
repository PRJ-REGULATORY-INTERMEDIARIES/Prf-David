# G1-PREP — CRITÉRIOS DE PRONTIDÃO E DE ACEITAÇÃO DO PILOTO A

**Data:** 2026-10-09 | **Estado:** PROPOSTA, redigida antes de qualquer codificação. Vale depois de aprovada e datada pela coordenação científica.
**Uso restrito ao coordenador e à coordenação científica.** Não entregar aos avaliadores.

Este documento fixa, antes da execução, o que precisa estar pronto para o Piloto A começar (Parte I) e o que será exigido para considerá-lo aceito (Parte II). Detalha e operacionaliza os critérios PA1–PA8 de `gates/G0_1/G0_1_REVISED_PILOT_DESIGN.md`.

**Princípio.** O piloto testa as regras da taxonomia, não os avaliadores nem os recursos. Indicadores estatísticos são instrumentos de diagnóstico: mostram onde olhar. Quem decide se uma regra está adequada é a adjudicação científica, por escrito.

---

## PARTE I — Condições para iniciar a codificação

A codificação dos 20 registros só começa com **todas** as condições abaixo cumpridas.

| # | Condição | Como se verifica | Estado em 2026-10-09 |
|---|---|---|---|
| I1 | Reviewer A, Reviewer B e Adjudicator designados pela equipe, com nome e data | Registro de designação assinado | **Não cumprida** — funções não designadas |
| I2 | Declaração de exposição prévia de cada pessoa: construiu ou leu o inventário; leu relatórios G0, G0.1 ou G1-PREP; já extraiu dados de fonte candidata | Declarações arquivadas | Não cumprida |
| I3 | Amostra aprovada: opção A, B, C ou D de `pilot_a/selection/PILOT_A_SELECTION_RATIONALE.md`, com lista final, data e responsável | Registro de aprovação | Não cumprida — candidata entregue |
| I4 | Rótulos exibidos aos avaliadores revistos (ver limitação L1) | `LABEL_OVERRIDES.csv` preenchido ou decisão escrita de manter os nomes | Não cumprida |
| I5 | Estes critérios aprovados, com os valores de alerta da seção 7 fixados e data anterior à entrega dos pacotes | Registro de aprovação | Não cumprida |
| I6 | Tamanho da rodada de confirmação fixado | Idem | Não cumprida |
| I7 | Meio de captura e arquivamento de evidência definido; capturas dos 20 registros feitas e com hash | Lista de capturas | Não cumprida — procedimento não definido |
| I8 | Pacotes regenerados depois de I3 e I4, e manifesto conferido | `PACKET_MANIFEST.json` com data posterior às aprovações | Pacotes gerados sobre a amostra candidata; regenerar se algo mudar |
| I9 | Pacotes entregues **fora do repositório**: cada avaliador recebe só a sua pasta | Registro de entrega | Não cumprida (ver L4) |
| I10 | Autorização humana explícita para iniciar | Registro datado | **Não concedida** |
| I11 | Testes automatizados aprovados na versão do código usada | `python -m unittest discover -s tests` | Cumprida: 51 de 51 |

---

## PARTE II — Critérios de aceitação do Piloto A

### 1. Completude dos formulários

| ID | Critério | Verificação |
|---|---|---|
| AC1 | Os dois formulários têm os 20 itens codificados; nenhum em branco | `python scripts/pilot_a_forms.py validate <formulário> --require-complete` termina sem erro |
| AC2 | Todos os valores pertencem aos vocabulários; campos obrigatórios preenchidos | Mesmo comando: zero linhas `[ERROR]` |
| AC3 | As quatro colunas pré-preenchidas e o cabeçalho não foram alterados | Conferência do coordenador contra o pacote entregue (manual: o validador confere o cabeçalho, não o conteúdo pré-preenchido) |
| AC4 | Um único `reviewer_id` por formulário, diferente entre os dois | Validador e comando `compare` |

Formulário incompleto não é comparado. O coordenador devolve ao avaliador a lista de erros de forma, **sem comentar o conteúdo** de nenhuma decisão.

### 2. Evidência mínima

| ID | Critério | Verificação |
|---|---|---|
| AC5 | Cada item tem ao menos um endereço de evidência e uma nota dizendo o que nele sustenta a decisão. Exceção: item declarado inacessível | Validador |
| AC6 | Cada item tem data de verificação | Validador |
| AC7 | Toda classificação `FPL` cita a base normativa ou a declaração institucional da atribuição de publicação oficial (regra R7) | Leitura pelo adjudicador |
| AC8 | Toda relação declarada tem justificativa | Validador (presença) e adjudicador (suficiência) |
| AC9 | Toda resposta incerta (`UNCERTAIN`, `uncertain`, `indeterminado`, `IND`) traz o tipo de incerteza e o que faltou | Validador |
| AC10 | As evidências citadas correspondem às capturas arquivadas, ou a diferença é explicada | Conferência do coordenador |

Uma decisão sem evidência verificável é tratada, na adjudicação, como resposta incerta por evidência insuficiente, qualquer que seja o valor marcado.

### 3. Independência e integridade do procedimento

| ID | Critério | Verificação |
|---|---|---|
| AC11 | Os dois formulários foram trancados antes de qualquer comparação | `pilot_a/coordinator/LOCK.json`, gerado por `python scripts/pilot_a_forms.py lock`, com hashes e data |
| AC12 | A comparação foi feita sobre os arquivos trancados | O comando `compare` recusa arquivo alterado depois do trancamento |
| AC13 | Nenhuma quebra de independência relatada ou detectada | Declaração dos avaliadores e do coordenador |
| AC14 | Critérios e valores de alerta aprovados com data anterior à entrega dos pacotes | Condição I5 |

Quebra de independência anula os itens afetados. Eles são refeitos com registros da reserva.

### 4. Tratamento de divergências

| ID | Critério | Verificação |
|---|---|---|
| AC15 | Toda divergência, em qualquer variável, tem na ata: a regra envolvida e a causa | Ata sem linhas em branco |
| AC16 | Toda resposta incerta tem o mesmo tratamento, mesmo quando os dois avaliadores concordam em estar incertos | Ata |
| AC17 | O adjudicador decide por escrito, com justificativa, o que não foi resolvido na reunião | Ata |
| AC18 | Nenhuma divergência é resolvida por média, por maioria ou por escolha do valor mais frequente | Ata |
| AC19 | Divergência causada por leitura diferente da mesma evidência é distinguida de divergência causada por regra | Código de causa |

Códigos de causa: `regra_ausente` · `regra_ambigua` · `leitura_da_evidencia` · `evidencia_insuficiente` · `erro_de_preenchimento`.

### 5. Validade das definições

Esta é a parte que decide o piloto.

| ID | Critério | Verificação |
|---|---|---|
| AC20 | Para cada regra R0–R11 envolvida em divergência ou incerteza, a equipe registrou: **confirmada** como está, ou **revista**, com a nova redação | Lista de regras |
| AC21 | Idem para cada classe, cada tipo de relação e cada código de função | Lista |
| AC22 | Não há item para o qual os dois avaliadores declararam que nenhuma classe serve | Formulários (`operational_category = IND` com `uncertainty_type = regra_ausente` em ambos) |
| AC23 | As fronteiras apontadas como questões abertas na taxonomia (seção 11) têm resposta registrada: `FPL` × `REP`; `DSE` × `REG`; R2 × R10; decomposição de portais; vocabulário distribuído como dado; necessidade de `part_of` | Ata |
| AC24 | O grupo de URL idêntica tem nível e relação acordados, ou adjudicados com justificativa | Ata |
| AC25 | O vocabulário de funções (F1–F8), novo e provisório, foi avaliado: mantido, alterado ou retirado | Ata |
| AC26 | **Rodada de confirmação:** com as regras revistas, o mesmo par codifica registros da reserva, em número fixado antes; não surge **tipo novo** de lacuna de regra | Comparação dos códigos de causa entre as rodadas |

Se AC26 falhar, repete-se com outros registros da reserva. Esgotada a reserva sem estabilidade, o resultado do piloto é que a taxonomia não é aplicável como está, e isso é relatado como tal.

### 6. Rastreabilidade das decisões

| ID | Critério | Verificação |
|---|---|---|
| AC27 | Existe, para cada rodada: lista aprovada; manifesto dos pacotes; registro de entrega; dois formulários; registro de trancamento; comparação; ata | Inventário de arquivos |
| AC28 | Cada mudança de regra cita os itens que a motivaram | Proposta de emenda |
| AC29 | A chave de identificadores permite reconstituir, para cada item, o registro de origem e as duas respostas | `ITEM_KEY.csv` |
| AC30 | Os documentos da rodada são copiados para pasta de gate com manifesto de hashes | `sha256sum -c` |
| AC31 | As decisões do piloto não aparecem em `data/screening.csv`, `data/consensus.csv` nem em qualquer contagem do inventário | `python scripts/cli.py check` e inspeção |

### 7. Indicadores estatísticos: uso diagnóstico

Produzidos por `python scripts/pilot_a_forms.py compare`, para o **único par nomeado** de avaliadores, **por variável**. Se em algum momento houver mais de um par, cada par tem a sua tabela; não existe valor combinado.

| Indicador | Variáveis | Para que serve |
|---|---|---|
| Tabela cruzada completa, com a incerteza como categoria | nível, categoria, função primária, candidato a fonte legislativa, elegibilidade | Ver **onde** as respostas se separam |
| Concordância observada com incerteza como categoria | Idem | Visão geral |
| Concordância observada só entre respostas categóricas, com o número de itens | Idem | Separar discordância de dúvida |
| Kappa de Cohen entre respostas categóricas, com intervalo aproximado | Idem | Descritivo. Com 20 itens e várias categorias, o intervalo é largo demais para sustentar conclusão |
| Brennan–Prediger | Idem | Leitura menos sensível a categorias raras |
| Concordância específica por categoria | Idem | Identificar a classe problemática |
| Conjuntos idênticos e Jaccard médio | funções secundárias, relações | Variáveis de múltiplos valores |
| Proporção de respostas incertas, por variável e por avaliador | Todas | Regra que gera dúvida precisa de revisão mesmo com alta concordância |
| Minutos por item | — | Dimensionar G3 |

**Regras de uso**

1. Nenhum indicador aprova o piloto. A aceitação exige AC1–AC31.
2. **Alerta numérico.** A coordenação científica fixa, antes da entrega dos pacotes, um valor de concordância observada em `operational_level` na rodada de confirmação. Abaixo dele, a taxonomia volta à revisão **mesmo que os demais critérios estejam cumpridos**. Acima dele, nada é dispensado. Este documento não fixa o valor.
3. Concordância alta não valida uma definição: dois avaliadores podem concordar aplicando mal a mesma regra. A adjudicação lê os itens concordantes dos grupos críticos (AC23, AC24).
4. Concordância baixa não invalida uma definição: pode vir de evidência insuficiente. O código de causa decide.
5. Nenhuma estatística do piloto é relatada como resultado da pesquisa.

### 8. Resultado do piloto

Decidido pelo adjudicador e pela coordenação científica, por escrito.

| Resultado | Condição |
|---|---|
| **Aceito** | AC1–AC31 cumpridos; rodada de confirmação sem tipo novo de lacuna |
| **Aceito com revisão** | Regras revistas e confirmadas em nova rodada; a versão revista da taxonomia é a que segue para congelamento |
| **Não aceito** | Independência quebrada sem possibilidade de refazer; ou reserva esgotada sem estabilidade; ou alerta numérico acionado sem causa identificada |

---

## PARTE III — Limitações conhecidas dos instrumentos

Declaradas agora para que a decisão de iniciar as leve em conta.

| # | Limitação | Consequência | Opção |
|---|---|---|---|
| L1 | Os rótulos exibidos são os nomes do inventário. Vários trazem um descritor que antecipa classificação ("repositório e grafo de metadados", "diretório", "bases legais nacionais", "busca de jurisprudência") | Ancoragem residual | Preencher `pilot_a/coordinator/LABEL_OVERRIDES.csv` com rótulos neutros e regenerar; decisão humana, porque encurtar o nome pode impedir a identificação do recurso |
| L2 | O texto da taxonomia entregue aos avaliadores menciona "RGAM/V8" três vezes, ao explicar a separação entre inventário e unidade jurídica | Revela a finalidade a jusante; não contém julgamento sobre itens | Aceitar, ou produzir versão do instrumento sem essas menções |
| L3 | O vocabulário de funções F1–F8 foi criado nesta fase para atender ao campo "função primária e secundárias". Não consta da taxonomia v0.2 | É um instrumento a mais em teste | Avaliado em AC25 |
| L4 | As pastas dos avaliadores, a chave e os arquivos de seleção estão no mesmo repositório | Quem tem acesso ao repositório vê tudo | Entregar pacotes fora do repositório (I9) |
| L5 | A captura e o arquivamento de evidência não foram implementados | AC10 depende de procedimento ainda inexistente | Definir em I7 |
| L6 | O validador não confere `reviewer_id` contra uma lista de pessoas, porque ninguém foi designado | Um identificador de agente não seria rejeitado automaticamente | Acrescentar a conferência depois da designação |
| L7 | A amostra candidata tem pares interface/acervo incompletos e nenhum registro descontinuado | Algumas regras (R2, R10, estado descontinuado) ficam pouco exercitadas | Opção B da justificativa da amostra |
| L8 | Estatística ordinal ponderada não foi implementada | Sem efeito no Piloto A, cujas variáveis são nominais | Implementar antes da auditoria (G4) |
| L9 | Os avaliadores acessam páginas vivas; sem captura comum, podem ver conteúdos diferentes | Divergência de conteúdo confundida com divergência de julgamento | I7 |

## Registro de aprovação (a preencher)

| Item | Decisão | Data | Responsável |
|---|---|---|---|
| Critérios AC1–AC31 | | | |
| Valor de alerta (seção 7, regra 2) | | | |
| Tamanho da rodada de confirmação | | | |
| Amostra (opção A, B, C ou D) | | | |
| Rótulos (L1) | | | |
| Reviewer A | | | |
| Reviewer B | | | |
| Adjudicator | | | |
| Autorização para iniciar | | | |
