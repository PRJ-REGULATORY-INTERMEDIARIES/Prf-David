# G1-READY — DOSSIÊ DE AUTORIZAÇÃO DO PILOTO A

**Data:** 2026-10-10 | **Elaboração:** agente de programação (Claude Code), sob coordenação humana | **Destinatário:** coordenação científica
**Uso restrito à coordenação e ao coordenador do piloto.** Não entregar aos avaliadores.

## Parecer

**READY para solicitar a autorização. NOT READY para iniciar a codificação.**

As pendências técnicas apontadas no G1-PREP foram resolvidas ou reduzidas a decisões. O que resta depende só de pessoas: aprovar a amostra, os rótulos e os critérios; designar quem avalia; autorizar a captura de evidências e, depois dela, o início.

A autorização tem, por isso, **duas etapas**. A primeira aprova as decisões e libera a captura de evidências. A segunda, depois de capturadas as evidências e entregues os pacotes, libera a codificação. Nenhuma foi concedida, presumida ou simulada neste documento.

O formulário para registrar as decisões está em `gates/G1_READY_AUTHORIZATION_FORM.md`, com todos os campos em branco.

**Classificação:** VERIFIED (observado em arquivo ou comando) · PROPOSED (recomendação; decisão humana) · PENDING VALIDATION (depende de fato, teste ou aprovação ainda inexistentes).

---

## 1. Situação técnica verificada

Nada do G1-PREP foi aceito sem reprodução.

| # | Verificação | Resultado | Classe |
|---|---|---|---|
| 1.1 | Reprodução dos testes do G1-PREP, com o código sem alteração | 51 de 51, como reportado | VERIFIED |
| 1.2 | Hashes do G1-PREP (`gates/G1_PREP_evidence/FILES.sha256`) no início desta fase | 46 de 46 conferem | VERIFIED |
| 1.3 | Reexecução do sorteio do G1-PREP | Mesma semente, mesma tentativa (9ª), mesma amostra | VERIFIED |
| 1.4 | Manifestos de `gates/G0` e `gates/G0_1` | Sem falha | VERIFIED |
| 1.5 | Testes ao fim desta fase | **87 de 87** (Python 3.14.4), sem avisos de recurso | VERIFIED |
| 1.6 | `cli.py check` sobre os dados reais | Código 0; nenhum erro; 3 avisos, os mesmos do G1-PREP | VERIFIED |
| 1.7 | Tabelas de dados, protocolo, codebook, inventário, `.gitignore` | Inalterados: 33 arquivos originais com o hash do início do G0 (o 34º, `cli.py`, foi alterado no G1-PREP e não nesta fase) | VERIFIED |
| 1.8 | Documentos históricos em `gates/G0`, `gates/G0_1` e os relatórios do G1-PREP | Inalterados | VERIFIED |

**Testes, por arquivo**

| Arquivo | Testes | Origem |
|---|---|---|
| `test_pipeline.py` | 4 | Original |
| `test_validation_vocabularies.py` | 17 | G1-PREP |
| `test_agreement_pairs.py` | 13 | G1-PREP |
| `test_pilot_a_instruments.py` | 17 | G1-PREP; dois testes ajustados nesta fase |
| `test_evidence_capture.py` | 12 | G1-READY |
| `test_pilot_a_required_groups.py` | 10 | G1-READY |
| `test_pilot_a_packets_v2.py` | 14 | G1-READY |

**Mudanças de código desta fase.** Para os dois scripts alterados, os testes foram escritos e executados antes: os 10 de grupos obrigatórios e 11 dos 14 de pacotes falhavam contra o código do G1-PREP (os outros 3 testam o arquivo de rótulos). Registros em `gates/G1_READY_evidence/tests_before_*.txt`.

| Script | Mudança |
|---|---|
| `scripts/select_pilot_a.py` | Grupos obrigatórios explícitos; avaliação de viabilidade antes do sorteio; pasta de saída e rótulo como parâmetros. Sem grupos, reproduz a amostra do G1-PREP |
| `scripts/pilot_a_forms.py` | Arquivo de rótulos neutros; manifesto do avaliador; validação automática dos campos pré-preenchidos; comando `package` |
| `scripts/capture_evidence.py` (novo) | Captura fiel de uma URL por vez, registro de arquivo manual, verificação de hashes |
| `scripts/pilot_a_scenarios.py` (novo) | Cenários de grupos obrigatórios: viabilidade e sorteio |
| `scripts/review_seed_urls.py` (novo) | Revisão estática do papel de cada URL do inventário |

Os dois testes do G1-PREP ajustados: um passou a incluir o manifesto do avaliador na lista de arquivos esperados da pasta; o outro passou a usar `precheck=False` para continuar exercitando o caminho de sorteio, já que a mesma entrada agora é dada como inviável antes de qualquer sorteio.

## 2. Inconsistências de identidade e URLs

Detalhe: `gates/G1_READY_SOURCE_IDENTITY_REVIEW.md` e `gates/G1_READY_SEED_URL_REVIEW.csv`. **O inventário de 41 seeds não foi modificado.**

| # | Conclusão | Classe |
|---|---|---|
| 2.1 | EU03 (EUR-Lex data dump) e EU07 (European Legal Data Space) são **recursos distintos descritos na mesma página**. A página oficial, capturada em 2026-10-10 e preservada com hash, apresenta o ELDS e, na seção 4, o data dump, com link próprio. | VERIFIED |
| 2.2 | Para EU03, a URL do inventário é a página de descrição. O endereço de acesso indicado pela fonte é `https://datadump.publications.europa.eu/`, que exige conta: a página o declara e o servidor respondeu 401 em duas tentativas. | VERIFIED |
| 2.3 | O conteúdo do dump não foi acessado. | PENDING VALIDATION |
| 2.4 | URL igual não é duplicata. O aviso do verificador está correto como **candidato**, e a decisão é humana. | VERIFIED |
| 2.5 | Em 25 dos 41 registros, a URL tem forma de página sobre o recurso (ajuda, explicação institucional, notícia) ou de raiz de sítio. Análise estática, sem abrir as páginas. | VERIFIED quanto à forma; PENDING VALIDATION quanto ao conteúdo |
| 2.6 | Quatro URLs têm parâmetros de consulta que a regra de deduplicação precisará tratar. | VERIFIED |
| 2.7 | Só há correção candidata com evidência para EU03 (URL de acesso). | VERIFIED |

A revisão separa cinco conceitos que o campo `source_url` do inventário mistura: identidade do recurso, URL de acesso, página de descrição, distribuição e relação institucional.

**Decisão pedida:** o que o avaliador recebe para EU03 — a URL do inventário (mantém o teste da regra de duplicata; é o que os pacotes propostos fazem) ou o endereço de acesso (leva a uma página de login).

## 3. Amostra revisada candidata

Detalhe: `pilot_a/selection_v2_PROPOSED/SAMPLE_REVISION_RATIONALE.md`. **Estado: PROPOSED. Nenhuma amostra foi escolhida em nome da equipe.**

**Candidata designada (cenário S3a):** EU01, EU03, EU04, EU07, EU08, EU09, EU11, EU12, EU15, EU17, EU19, EU20, EU21, EU23, EU29, EU33, EU34, EU35, EU39, EU41.

**Reserva (21):** EU02, EU05, EU06, EU10, EU13, EU14, EU16, EU18, EU22, EU24, EU25, EU26, EU27, EU28, EU30, EU31, EU32, EU36, EU37, EU38, EU40.

| Elemento | Valor | Classe |
|---|---|---|
| Semente | `1160865795`, a mesma do G1-PREP | VERIFIED |
| Restrições C1–C8 | As mesmas, com os mesmos valores | VERIFIED |
| Grupos obrigatórios | EU08+EU09; EU33+EU34; EU11; EU35+EU39; mais o grupo de URL idêntica EU03+EU07 | PROPOSED |
| Viabilidade | Avaliada antes do sorteio para oito cenários; todos viáveis | VERIFIED |
| Regra de designação | Escrita antes do sorteio: menor conjunto de grupos que cobre tudo o que o G1-READY pediu para avaliar, com o par acadêmico que exercita `derived_from` | VERIFIED (registro anterior ao sorteio) |

**O que cada item pedido trouxe**

| Item avaliado | Incluído em S3a | Efeito |
|---|---|---|
| EU08 e EU09 | Sim | Par interface/acervo completo |
| EU33 e EU34 | Sim | Par completo; a família "Aplicação setorial" sai da reserva, e a restrição de reserva fica no limite |
| EU11 | Sim | Um registro descontinuado na amostra |
| Par de corpora acadêmicos | EU35 + EU39 | Testa derivação entre derivados; a relação não foi verificada |
| Deduplicação e ambiguidade | EU03 + EU07; três registros de tipo composto | Mantidos |

**O que a candidata perde** (VERIFIED): EU02 (CELLAR) saiu, e com ele o confronto mais direto entre distribuição e recurso próprio no ecossistema EUR-Lex; "Fiscalização" e "Intermediação RIT" ficam com um registro cada; não há folga nas restrições de diversidade de tipos e de reserva.

**Opções:** aprovar S3a; declarar também o grupo EU01+EU02 e sortear de novo com a mesma semente (não executado); aprovar outro cenário já sorteado; manter a amostra do G1-PREP; ou a lista intencional do G0.1. Escolher o cenário depois de ver as amostras é uma forma de seleção intencional: aceitável num piloto de regras, desde que o motivo seja registrado.

## 4. Protocolo de evidências

Detalhe: `gates/G1_READY_EVIDENCE_CAPTURE_PROTOCOL.md`. Estado: PROPOSED; execução sobre os itens do piloto **não iniciada**.

| Exigência | Como é atendida |
|---|---|
| URL original e final | Registradas, com a cadeia de redirecionamentos |
| Data e hora UTC | Da captura e de cada tentativa |
| Identificação do recurso | Identificador do inventário no registro; identificador neutro no pacote do avaliador |
| Tipo e formato | Dos cabeçalhos da resposta |
| Arquivo bruto | Byte a byte; opção de guardar só o hash quando os termos proibirem cópia |
| SHA-256 | Sobre os bytes recebidos; comando de verificação |
| Versão ou data de atualização | O que o servidor informa é automático; o que a página declara é campo humano |
| Condições de acesso e reutilização | Campos humanos, em branco até alguém ler os termos |
| Falhas e tentativas | Todas registradas; falha nunca vale como ausência do recurso |
| Relação evidência–item | Índice por item em cada pacote |

Princípios: fonte oficial primeiro; nenhuma extração, resumo ou destaque; uma URL por requisição; nunca sobrescrever; o coordenador captura e os dois avaliadores recebem os mesmos arquivos.

**Validação** (VERIFIED): 12 testes contra servidor local; e um teste de rede com **duas** requisições, às URLs oficiais indicadas na tarefa, com o plano declarado antes. Uma página foi capturada e conferida; a outra produziu falha registrada (401). O teste revelou uma lacuna — o desafio de autenticação não era guardado —, corrigida com teste. Nenhuma outra URL foi acessada.

**Volume previsto para o piloto:** 40 a 60 requisições para 20 itens. Precisa de autorização.

## 5. Proteção da independência dos avaliadores

### 5.1 O que foi implementado e testado

| Proteção | Como | Classe |
|---|---|---|
| Pacote por avaliador | Comando `package`: um arquivo compactado com o formulário, as instruções, a taxonomia, os critérios de elegibilidade, o manifesto do avaliador e a evidência dos seus itens | VERIFIED (teste) |
| Sem chave, sem material do outro avaliador | O empacotamento falha se o arquivo contiver a chave, material do coordenador ou da seleção, ou algum identificador do inventário | VERIFIED (teste) |
| Evidência sob identificadores neutros | Os mesmos arquivos, arquivados como `A-nn` num pacote e `B-nn` no outro | VERIFIED (teste) |
| Campos pré-preenchidos conferidos automaticamente | Cada pacote leva um manifesto com o hash dos quatro campos pré-preenchidos de cada item. O validador acusa rótulo, URL ou função alterados, item removido e item acrescentado, e nomeia o item | VERIFIED (5 testes) |
| Trancamento | `lock` recusa formulário com campo pré-preenchido alterado; `compare` recusa arquivo modificado depois | VERIFIED (teste) |
| Funções não designadas | Reviewer A, Reviewer B e Adjudicator constam como não designados | VERIFIED |

**Resposta à pergunta da tarefa:** sim, os campos pré-preenchidos podem ser validados automaticamente contra o manifesto do pacote, e isso está implementado. O critério AC3 do G1-PREP, que era manual, passa a ser automático.

### 5.2 Rótulos revistos

`pilot_a/labels/LABELS_PROPOSED.csv`: 41 rótulos, um por registro, com o texto removido e a razão de cada mudança. Estado: PROPOSED.

| Tipo de mudança | Qtd. |
|---|---|
| Sem alteração, ou só de pontuação | 15 |
| Descritor do inventário removido | 18 |
| Descritor trocado por termo neutro necessário para identificar o recurso | 3 |
| Reordenado ou reescrito, sem descritor a remover | 4 |
| Nome ajustado à forma usada pela fonte (EU03) | 1 |

Exemplos: "CELLAR — repositório e grafo de metadados" → "CELLAR"; "European Legal Data Space — diretório" → "European Legal Data Space (ELDS)"; "Council votes on legislative acts — dataset antigo" → "Council votes on legislative acts".

**Limite:** só três rótulos foram conferidos contra a fonte (EU03, EU07 e EU23, na página ELDS capturada). Os demais vêm do próprio inventário, sem o descritor: PENDING VALIDATION. A conferência dos nomes oficiais pode ser feita durante a captura de evidências.

### 5.3 Distribuição proposta

1. O coordenador gera os dois pacotes **depois** das aprovações e da captura.
2. Cada pacote é entregue por canal individual: pasta compartilhada só com aquela pessoa, **fora do repositório**. O repositório contém a chave, os arquivos de seleção, os relatórios e os dois formulários.
3. Durante a codificação, os avaliadores não têm acesso ao repositório nem à pasta um do outro.
4. O avaliador devolve só o formulário preenchido, pelo mesmo canal.
5. O coordenador valida a forma, sem comentar conteúdo; tranca os dois formulários; só então compara.
6. O hash de cada pacote entregue fica registrado.

**Pacotes propostos já montados** (não compactados, não entregues): `pilot_a/packets_v2_PROPOSED/`, sobre a amostra S3a e com os rótulos propostos. Todos os campos de decisão vazios nos 40 itens; validador reporta 20 itens em branco em cada formulário e campos pré-preenchidos conferidos. Se a amostra ou os rótulos aprovados forem outros, os pacotes são regenerados.

### 5.4 O que não foi resolvido

| # | Pendência | Motivo |
|---|---|---|
| 1 | O texto da taxonomia entregue aos avaliadores menciona "RGAM/V8" em três linhas | Editar o instrumento seria alterar um documento de protocolo; fica para decisão |
| 2 | O validador não confere o identificador do avaliador contra uma lista de pessoas | Ninguém foi designado, e esta fase não atribui identidades |
| 3 | Quem tem acesso ao repositório vê tudo | Controle de acesso é organizacional, não de código |

## 6. Critérios de aceitação ainda pendentes

Os 31 critérios (AC1–AC31) estão em `gates/G1_PREP_READINESS.md`, redigidos antes de qualquer codificação e **não aprovados**. O que muda com esta fase:

| Critério | Situação |
|---|---|
| AC3 — campos pré-preenchidos intactos | Passa de conferência manual a automática |
| AC10 — evidência citada corresponde à capturada | Passa a ter procedimento (protocolo de evidências) e índice por item |
| AC24 — grupo de URL idêntica | Há agora evidência de que EU03 e EU07 são recursos distintos; o critério continua sendo a decisão dos avaliadores, que não recebem essa informação |
| AC26 — rodada de confirmação | Tamanho proposto na seção 7 |
| Regra 2 da seção 7 — alerta numérico | Valor proposto na seção 7 |
| Demais | Sem mudança; aguardam aprovação |

Os critérios precisam de aprovação **com data anterior à entrega dos pacotes**.

## 7. Propostas para a rodada de confirmação e o alerta estatístico

Ambas PROPOSED. A decisão é da coordenação científica.

### 7.1 Tamanho da rodada de confirmação: 10 registros

| Opção | A favor | Contra |
|---|---|---|
| 8 | Deixa 13 na reserva | Poucos itens para exercitar regras revistas em classes diferentes |
| **10** | Metade da amostra principal; deixa 11 na reserva, o bastante para **uma segunda** rodada do mesmo tamanho se a primeira falhar | — |
| 12 | Mais itens | Deixa 9: uma segunda rodada teria de ser menor |

Como escolher os 10: sorteio com semente registrada entre os 21 da reserva, com uma restrição declarada depois da primeira rodada — incluir ao menos um registro que exercite cada regra revista. Como essa restrição depende do resultado da primeira rodada, ela é escrita na ata de calibração antes do sorteio.

### 7.2 Alerta numérico: 7 ou menos concordâncias em 10 itens, em `operational_level`

O alerta incide sobre a concordância observada em `operational_level` na rodada de confirmação, contando a incerteza como categoria própria. Função, conforme o G1-PREP: abaixo do valor, a taxonomia volta à revisão mesmo com os demais critérios cumpridos; acima dele, nada é dispensado.

A tabela dá a probabilidade de o alerta disparar, para diferentes níveis de concordância verdadeira, supondo itens independentes com a mesma probabilidade de concordância. É uma simplificação: serve para comparar limiares, não para descrever o piloto.

| Alerta dispara se concordarem em… | Conc. verdadeira 0,95 | 0,90 | 0,80 | 0,70 | 0,60 |
|---|---|---|---|---|---|
| 6 ou menos de 10 | 0,1% | 1,3% | 12,1% | 35,0% | 61,8% |
| **7 ou menos de 10** | 1,2% | 7,0% | 32,2% | 61,7% | 83,3% |
| 8 ou menos de 10 | 8,6% | 26,4% | 62,4% | 85,1% | 95,4% |

**Por que 7 ou menos.** O alerta tem consequência forte: manda refazer a revisão da taxonomia mesmo que toda a adjudicação tenha concluído bem. Um alarme falso custa caro, e com "8 ou menos" ele dispararia uma vez em quatro mesmo com concordância verdadeira de 0,90. Com "7 ou menos", o alarme falso fica em 7% nesse caso e o alerta ainda dispara na maioria das vezes quando a concordância verdadeira é 0,70 ou pior.

**O que o alerta não faz.** Ele detecta mal problemas moderados: com concordância verdadeira de 0,80, dispara só uma vez em três. Isso é aceitável porque não é a única barreira — os critérios AC20 a AC26 examinam cada divergência, uma a uma. Com dez itens, nenhum limiar separa bem 0,80 de 0,90; por isso o número é alerta, e não critério de aprovação.

**Alerta secundário opcional:** se, em qualquer variável, um avaliador marcar incerteza em 4 ou mais dos 10 itens, a regra correspondente é revista, qualquer que seja a concordância.

Tabela completa, incluindo rodadas de 8 e 12: `gates/G1_READY_evidence/alert_threshold_table.txt`.

## 8. Decisões que dependem exclusivamente de aprovação humana

Nenhuma foi tomada, presumida ou simulada.

**Etapa 1 — antes da captura de evidências**

1. Adoção da reorientação do estudo pela equipe científica, ou autorização expressa para conduzir o Piloto A enquanto ela é discutida.
2. Amostra: S3a, S3a com o grupo EU01+EU02, outro cenário, a do G1-PREP, ou a lista do G0.1; com o motivo.
3. Grupos obrigatórios: confirmar, alterar ou retirar cada um.
4. URL entregue para EU03: a do inventário ou a de acesso.
5. Rótulos: aprovar a lista proposta, alterá-la ou manter os nomes do inventário.
6. Menções a "RGAM/V8" no texto da taxonomia entregue aos avaliadores: manter ou produzir versão sem elas.
7. Critérios de aceitação AC1–AC31.
8. Tamanho da rodada de confirmação e valor do alerta numérico; alerta secundário.
9. Vocabulários provisórios (funções F1–F8, tipo de incerteza, resultado do acesso).
10. Designação de Reviewer A, Reviewer B, Adjudicator e do coordenador; declaração de exposição prévia de cada um; se quem construiu o inventário pode avaliar.
11. Protocolo de evidências; autorização para as requisições de captura; quem captura.
12. Capturas versionadas no repositório ou só os registros com hash; uso de serviço de arquivamento.
13. Criação ou não de conta para recursos que exigem login.
14. Canal de entrega dos pacotes.

**Etapa 2 — depois da captura e da entrega**

15. Autorização para iniciar a codificação.

**Fora do piloto, ainda pendentes**

16. Parâmetros U1–U6 do universo jurídico, a discutir com David Levi-Faur. Nenhuma posição lhe é atribuída.
17. Commit e publicação dos documentos, do código e dos testes.

## 9. Condições objetivas para iniciar o Piloto A

A codificação só começa com todas cumpridas. Cada uma tem verificação objetiva.

| # | Condição | Verificação | Estado em 2026-10-10 |
|---|---|---|---|
| S1 | Formulário de autorização, etapa 1, preenchido, datado e assinado | Arquivo | Não cumprida |
| S2 | Amostra aprovada gravada, com seu `REQUIRED_GROUPS.json` e o registro do sorteio | Arquivos e hashes | Candidata disponível |
| S3 | Rótulos aprovados gravados | Arquivo e hash | Proposta disponível |
| S4 | Critérios, tamanho da confirmação e alerta aprovados, com data anterior à entrega | Datas no formulário | Não cumprida |
| S5 | Funções designadas; declarações de exposição arquivadas | Arquivos | Não cumprida |
| S6 | Evidências capturadas para os 20 itens; `capture_evidence.py verify` sem problemas; campos humanos preenchidos | Comando | Não iniciada |
| S7 | Pacotes regenerados depois de S2, S3 e S6; `validate` reporta 20 itens em branco e campos pré-preenchidos conferidos, em ambos | Comando | Pacotes propostos montados; regenerar |
| S8 | Pacotes compactados com `package`; hashes registrados; entrega individual, fora do repositório, registrada | `DIST_MANIFEST.json` e registro de entrega | Não cumprida |
| S9 | Testes automatizados aprovados na versão do código usada | `python -m unittest discover -s tests` | Cumprida hoje: 87 de 87 |
| S10 | Formulário de autorização, etapa 2, preenchido, datado e assinado | Arquivo | Não cumprida |

## 10. Riscos metodológicos residuais

| # | Risco | Por que permanece | Classe |
|---|---|---|---|
| R1 | A amostra é, em parte, escolha intencional | Os grupos obrigatórios são julgamento humano, e a escolha do cenário acontece depois de vistas as amostras. Declarado, não eliminado | VERIFIED |
| R2 | Relações supostas nos grupos obrigatórios podem não existir | Nenhuma foi verificada nas fontes; um par sem relação testa pouco | PENDING VALIDATION |
| R3 | A candidata não tem folga em duas restrições | Qualquer troca manual de registro tende a violar diversidade de tipos ou cobertura da reserva | VERIFIED |
| R4 | Evidência incompleta para páginas dinâmicas ou com login | A captura simples não as alcança; o procedimento manual depende de disciplina | PROPOSED (controle no protocolo) |
| R5 | Escolher quais páginas capturar já orienta o avaliador | Só a URL do inventário é capturada sem julgamento; as demais são escolhas do coordenador, registradas | PROPOSED |
| R6 | Rótulos neutros podem dificultar a identificação | Um nome curto demais pode ser ambíguo; a URL acompanha o rótulo | PROPOSED |
| R7 | Nomes oficiais não conferidos em 38 dos 41 rótulos | Sem acesso às fontes nesta fase | PENDING VALIDATION |
| R8 | O coordenador conhece tudo | Ele captura, empacota e compara; não pode avaliar nem comentar conteúdo com os avaliadores | PROPOSED |
| R9 | Equipe pequena | Se quem construiu o inventário tiver de avaliar, a independência é parcial e deve ser declarada | PENDING VALIDATION |
| R10 | Um agente de IA conduziu a preparação e viu as colunas de julgamento | Seleção por sorteio e pacotes cegos reduzem o efeito; os relatórios não chegam aos avaliadores | VERIFIED |
| R11 | Dez itens na confirmação não distinguem concordância boa de moderada | Limite do tamanho; por isso o número é alerta e a decisão é da adjudicação | VERIFIED |
| R12 | Fontes mudam durante o piloto | Datas e hashes registram o que foi visto; não impedem a mudança | PROPOSED |
| R13 | A finalidade do estudo ainda não foi adotada pela equipe | O piloto calibra uma taxonomia desenhada para essa finalidade; se ela mudar, parte do trabalho precisa ser revista | PENDING VALIDATION |
| R14 | Instrumentos originais | Taxonomia, vocabulário de funções e critérios são novos e não validados fora do projeto | VERIFIED |

---

## Problemas não resolvidos nesta fase

1. Conteúdo do EUR-Lex data dump não acessado (exige conta).
2. Tipo de desafio de autenticação do 401 não registrado na requisição feita (a ferramenta foi corrigida depois; a requisição não foi repetida).
3. As outras 39 URLs do inventário não foram abertas; o papel atribuído a cada uma é inferência pela forma do endereço.
4. Nomes oficiais conferidos só em três rótulos.
5. Menções a "RGAM/V8" na taxonomia entregue aos avaliadores.
6. Conferência de identificadores de avaliadores contra lista de pessoas.
7. O manifesto de hashes do G1-PREP acusa, como esperado, três arquivos alterados nesta fase (`select_pilot_a.py`, `pilot_a_forms.py`, `test_pilot_a_instruments.py`). As versões do G1-PREP não estão no git, porque nada foi commitado; o manifesto novo está em `gates/G1_READY_evidence/FILES.sha256`.

## Registro de conformidade

| Limite | Estado |
|---|---|
| Classificação, triagem ou adjudicação | Nenhuma |
| Codificação do Piloto A | Não executada; formulários vazios |
| Decisões ou aprovações simuladas | Nenhuma; formulário de autorização em branco |
| Identidades atribuídas a avaliadores | Nenhuma |
| Decisões atribuídas a David Levi-Faur | Nenhuma |
| Protocolo e documentos históricos | Inalterados |
| 41 seeds originais | Inalterados |
| Outros projetos do PRJ-David | Não tocados |
| Rede | Duas requisições, às URLs indicadas na tarefa, com plano declarado antes |
| Commit ou push | Nenhum |

**Gate:** execução encerrada em G1-READY.
