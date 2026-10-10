# G1-PREP — RELATÓRIO TÉCNICO

**Data:** 2026-10-09 (local) | **Elaboração:** agente de programação (Claude Code), sob coordenação humana | **Destinatário:** proponente e equipe científica

## Conclusão

**Os instrumentos do Piloto A estão prontos; o piloto não está pronto para começar.** O que falta é exclusivamente humano: designar os avaliadores e o adjudicador, aprovar a amostra, aprovar os critérios de aceitação e autorizar o início.

Os dois defeitos técnicos do G0 foram corrigidos e estão cobertos por testes: 51 de 51 passam. Nenhuma decisão humana foi preenchida ou simulada, nenhum registro foi classificado, nenhuma fonte foi consultada, nada foi commitado.

Há uma decisão que merece atenção antes das outras: a amostra sorteada é reprodutível e livre de julgamento prévio, mas deixou incompletos dois pares interface/acervo e não tem nenhum registro descontinuado (seção 3).

---

## 1. Arquivos criados e modificados

### Modificado (1)

| Arquivo | SHA-256 antes | SHA-256 depois | Alteração |
|---|---|---|---|
| `scripts/cli.py` | `1eba44ef…2ac6e` | `756f59fa…2a91` | 81 linhas inseridas, 21 removidas (seção 2) |

A versão anterior está no histórico git (commit `4a05e8f`). `outputs/STATUS_REPORT.md` foi reescrito pelo próprio comando `report`, como em toda execução.

### Criados

| Grupo | Arquivos |
|---|---|
| Consolidação G0 | `gates/G0/` — cinco documentos, `MANIFEST.sha256`, `SOURCES.sha256` |
| Consolidação G0.1 | `gates/G0_1/` — cinco documentos, o registro de decisões v1.1, `MANIFEST.sha256`, `SOURCES.sha256` |
| Documentos deste gate | `gates/U1_U6_RESEARCH_UNIVERSE_DECISION_BRIEF.md`, `gates/G1_PREP_READINESS.md`, `gates/G1_PREP_TECHNICAL_REPORT.md` |
| Evidência de execução | `gates/G1_PREP_evidence/` — `tests_before_fix.txt`, `tests_after_fix.txt`, `tests_final.txt`, `cli_run_after_fix.txt`, `pilot_a_selection_run.txt`, `FILES.sha256` |
| Código | `scripts/agreement.py`, `scripts/select_pilot_a.py`, `scripts/pilot_a_forms.py` |
| Vocabulários | `schemas/vocabularies.json` |
| Testes | `tests/test_validation_vocabularies.py`, `tests/test_agreement_pairs.py`, `tests/test_pilot_a_instruments.py` |
| Seleção (coordenador) | `pilot_a/selection/` — amostra candidata, reserva, registro da execução, justificativa |
| Pacotes dos avaliadores | `pilot_a/reviewer_A/` e `pilot_a/reviewer_B/` — formulário, instruções, taxonomia, critérios de elegibilidade |
| Coordenador | `pilot_a/coordinator/` — chave de identificadores, manifesto dos pacotes, arquivo de rótulos (vazio) |

### Não alterados

Os outros 33 arquivos originais do repositório (protocolo, codebook, inventário, dados, demais scripts e testes, manuscrito) mantêm o SHA-256 do início do G0. `.gitignore` não foi tocado. Os documentos G0 e G0.1 em `outputs/` e `protocol/` não foram tocados.

### Consolidação: verificação de correspondência

Onze arquivos copiados; para cada um, o hash do original e o da cópia foram calculados e comparados.

| Gate | Arquivos | Original = cópia | `sha256sum -c MANIFEST.sha256` | Originais inalterados após a cópia |
|---|---|---|---|---|
| G0 | 5 | 5 de 5 | OK | Sim |
| G0.1 | 6 | 6 de 6 | OK | Sim |

Os cinco hashes de `gates/G0/` coincidem com os registrados em `G0_1_STRATEGIC_ALIGNMENT.md`, seção 14. `MANIFEST.sha256` lista as cópias; `SOURCES.sha256` lista os originais com o caminho de origem.

## 2. Correções implementadas e testes

### Método

Os testes foram escritos **antes** das correções e executados contra o código original, para registrar os defeitos; depois o código foi corrigido e os mesmos testes foram executados de novo.

| Execução | Código | Testes | Aprovados | Falhas | Erros | Registro |
|---|---|---|---|---|---|---|
| Antes | `cli.py` original | 34 | 8 | 16 | 10 | `tests_before_fix.txt` |
| Depois | `cli.py` corrigido + `agreement.py` | 34 | 34 | 0 | 0 | `tests_after_fix.txt` |
| Final | Tudo, incluindo instrumentos | 51 | 51 | 0 | 0 | `tests_final.txt` |

Na execução "antes": as 16 falhas são asserções que demonstram os defeitos no código original; os 10 erros são testes do módulo `agreement`, que ainda não existia. Os 8 aprovados são os 4 testes originais e 4 comportamentos que já estavam corretos.

Todos os dados usados em testes são **sintéticos**, gravados em diretório temporário, com identificadores `SYN_…` e aviso no cabeçalho de cada arquivo. Nenhum teste escreve em `data/` nem em `pilot_a/`.

### Defeito 1 — validação de vocabulários

| O que mudou | Teste |
|---|---|
| Vocabulários numa fonte única, `schemas/vocabularies.json`, lida pelo verificador | — |
| Validados: `origin`; `reason_code` na triagem e no consenso; `stage` no consenso; `criterion` na auditoria; `validation_status` | 5 testes, um por valor inválido |
| Datas em ISO 8601 em cinco tabelas | 3 testes |
| URLs com esquema http ou https em seis tabelas | 1 teste |
| `source_record_ids` de um dataset: cada registro precisa existir e ter inclusão por consenso na etapa `full_source` | 2 testes |
| Registro com `origin` inválido deixa de ser contado como busca sistemática | 1 teste |
| URL repetida entre ocorrências gera aviso com os identificadores | 1 teste |
| `check` passou a ser somente leitura: tabela ausente é erro e não é criada | 2 testes |
| Nenhum erro sobre os dados reais nem sobre um conjunto sintético válido | 2 testes |

Cada valor inválido, inserido isoladamente, produz **exatamente um** erro, que nomeia tabela, coluna, chave e valor.

Efeito sobre os dados reais: `check` continua sem erros e passou a emitir um aviso novo e correto — a URL `https://data.europa.eu/en/ELDS` aparece em `SEED_EU03` e `SEED_EU07`.

### Defeito 2 — concordância entre avaliadores

| O que mudou | Teste |
|---|---|
| Novo módulo `scripts/agreement.py`. A unidade de cálculo é o par nomeado de avaliadores; o resultado é uma lista, um elemento por par, com o campo `pooled_result` sempre nulo | T1 |
| `cli.kappa_or_na` recusa-se a operar com mais de um par (antes devolvia n = 2, kappa = 1 para dois pares distintos) | 2 testes |
| Incerteza explícita: itens com resposta incerta são contados; a concordância é dada de duas formas, **com a incerteza como categoria própria** e **só entre respostas categóricas**, cada uma com o seu número de itens | T1 e 1 teste |
| Tabela cruzada completa por par; a soma das células é igual ao número de itens | T5 |
| Kappa ausente, com o motivo, quando só há uma categoria | T2 |
| Valor conferido à mão: 20 e 15 na diagonal, 5 e 10 fora, n = 50 → 0,70 observada, 0,50 esperada, kappa 0,40 | T3 |
| Simetria ao trocar os avaliadores | T4 |
| Itens com um avaliador, com mais de dois, ou com resposta em branco são listados à parte, nunca descartados em silêncio | T6 e 1 teste |
| Variáveis de múltiplos valores: conjuntos idênticos e Jaccard médio, por par | 1 teste |
| O relatório de estado lista cada par em linha própria | 1 teste |
| Variável e rótulo de incerteza são parâmetros (serve a `decision`, `primary_class` etc.) | 1 teste |

Estatísticas por par e por variável: concordância observada (duas formas), kappa de Cohen com intervalo aproximado e o método declarado, coeficiente de Brennan–Prediger, concordância específica por categoria, lista de itens divergentes. Nenhuma função devolve aprovado ou reprovado.

**Nenhuma estatística foi calculada sobre dados reais**, porque não existe codificação. O relatório de estado sobre os dados atuais diz, para cada etapa, "nenhum par de avaliadores com decisões registradas".

### O que das especificações do G0.1 não foi implementado

| Item | Motivo |
|---|---|
| Conferência de `reviewer` contra lista de pessoas | Ninguém foi designado |
| Estatística ordinal ponderada | Sem uso no Piloto A; necessária em G4 |
| Vocabulário de `status` de dataset | O codebook não o define; criá-lo seria decisão de protocolo |
| Detecção de alteração do arquivo de seeds após a importação | Fora dos dois defeitos pedidos |

Dois vocabulários foram incluídos como **provisórios**, porque nenhum documento do protocolo os define: `rit_validation_status` e os quatro vocabulários auxiliares do formulário do piloto (funções, tipo de incerteza, resultado do acesso). Estão marcados como tal no arquivo e pedem decisão da equipe.

## 3. Amostra candidata para o Piloto A

**EU01, EU02, EU03, EU07, EU08, EU13, EU15, EU17, EU19, EU23, EU24, EU25, EU27, EU28, EU30, EU32, EU33, EU37, EU39, EU41.**

Reserva (21): EU04, EU05, EU06, EU09, EU10, EU11, EU12, EU14, EU16, EU18, EU20, EU21, EU22, EU26, EU29, EU31, EU34, EU35, EU36, EU38, EU40.

| Elemento | Valor |
|---|---|
| Código | `scripts/select_pilot_a.py` |
| Semente | `1160865795`, derivada do SHA-256 do arquivo de seeds; não escolhida |
| Execuções | Uma. Aceita na 9ª tentativa |
| Colunas lidas | Identificador, família, nome, tipo de recurso, URL |
| Colunas nunca lidas | `rgam_potential`, `initial_priority`, `limitations` e outras três; um teste embaralha as três primeiras e confirma que a amostra não muda |
| Parâmetros | Fixados antes da execução; não ajustados depois |

| Exigência | Restrição | Resultado |
|---|---|---|
| 11 famílias | Ao menos 1 registro por família | 11 de 11 |
| Possíveis duplicados | Grupos de URL idêntica entram completos | EU03 + EU07 |
| Possíveis relacionados | Ao menos 3 grupos de mesmo host com 2 ou mais | 4 grupos |
| Classificação ambígua | Ao menos 3 registros com tipo de recurso composto ("A/B") | EU01, EU02, EU23 |
| Diversidade de tipos | Ao menos 18 tipos distintos | 20 |
| Equilíbrio | No máximo 4 por família | Máximo 4 |
| Reserva útil | Os 21 restantes cobrem ao menos 9 famílias | 10 |

**As restrições não se mostraram incompatíveis.** Se fossem, o código pararia com erro e relataria as falhas sem relaxar nada; isso está coberto por teste.

**Limites que a equipe precisa conhecer.** "Relacionado" e "ambíguo" são julgamentos; para não usar colunas de julgamento, foram trocados por substitutos computáveis (mesmo host; tipo com dois rótulos). O custo:

- dois pares apontados no G0.1 ficaram incompletos: EU08 sem EU09, EU33 sem EU34;
- o único registro que o inventário marca como descontinuado (EU11) ficou na reserva;
- EU39 entrou sem EU35 nem EU36;
- "Intermediação RIT" é a família mais representada (4), embora a nova finalidade trate registros setoriais como enriquecimento.

Doze dos vinte registros coincidem com a lista intencional do G0.1.

Quatro opções, descritas em `pilot_a/selection/PILOT_A_SELECTION_RATIONALE.md`: (A) aprovar como está; (B) a equipe declara grupos obrigatórios por escrito e o algoritmo é reexecutado com a mesma semente; (C) adotar a lista intencional do G0.1; (D) outra semente, registrada antes. Não improvisei nenhuma delas.

## 4. Instrumentos preparados

| Instrumento | Local | Conteúdo |
|---|---|---|
| Formulário A | `pilot_a/reviewer_A/CODING_FORM_A.csv` | 20 itens `A-01` a `A-20` |
| Formulário B | `pilot_a/reviewer_B/CODING_FORM_B.csv` | Os mesmos 20 recursos, `B-01` a `B-20`, em outra ordem |
| Instruções | `INSTRUCTIONS.md` em cada pasta | Regras de independência; como preencher cada coluna; tratamento da incerteza |
| Regras de classificação | `SOURCE_TAXONOMY_v0_2_DRAFT.md` em cada pasta | Cópia byte a byte da taxonomia |
| Critérios de elegibilidade | `ELIGIBILITY_CRITERIA_PROTOCOL_S6.md` em cada pasta | Transcrição literal da seção 6 do protocolo |
| Chave | `pilot_a/coordinator/ITEM_KEY.csv` | Liga `A-nn` e `B-nn` ao registro de origem |
| Manifesto | `pilot_a/coordinator/PACKET_MANIFEST.json` | Hashes, sementes de ordenação, colunas retidas |
| Ferramentas | `scripts/pilot_a_forms.py` | `build`, `validate`, `lock`, `compare` |

**Campos de cada formulário.** Pré-preenchidos: identificador neutro, rótulo, URL, função do avaliador. A preencher: identificação e data de verificação; resultado do acesso e URL efetivamente usada; nível e categoria operacional, com a regra aplicada; função primária e funções secundárias; candidato a fonte legislativa; elegibilidade, código de motivo e justificativa; relações de duplicação ou sobreposição, com justificativa; URLs e notas de evidência; tipo de incerteza, evidência faltante, observações; minutos.

**Estado dos formulários** (verificado): todos os campos de decisão estão vazios nos 40 itens; o validador reporta 20 itens em branco em cada um; o comando `lock` recusa formulários em branco; `compare` recusa formulários não trancados.

## 5. Condições de independência dos avaliadores

| Condição | Como está garantida | Estado |
|---|---|---|
| Ocultação das classificações preliminares | Os formulários não contêm família, tipo de recurso, `rgam_potential`, prioridade, ressalvas nem o identificador do inventário. Um teste confere a ausência das colunas, dos textos de ressalva e dos identificadores | Verificado |
| Identificadores neutros | `A-nn` e `B-nn`, sem relação com a ordem do inventário | Verificado |
| Ordens independentes | Permutações diferentes por avaliador, com sementes registradas | Verificado |
| Equivalência dos conjuntos | Mesmos 20 recursos, mesmas colunas, mesmas instruções | Verificado |
| Informação factual preservada | Nome e URL de origem | Verificado |
| Decisões do outro avaliador ocultas | Arquivos separados; trancamento por hash antes da comparação; `compare` recusa arquivo alterado depois | Implementado e testado |
| Funções não designadas | Reviewer A, Reviewer B e Adjudicator constam como `NOT ASSIGNED` no manifesto | Verificado |

**Ressalvas** (detalhe em `G1_PREP_READINESS.md`, Parte III):

1. Os rótulos são os nomes do inventário, e vários trazem um descritor que antecipa classificação. Há um arquivo de substituição de rótulos, vazio, à espera de decisão humana.
2. As pastas dos avaliadores, a chave e os arquivos de seleção estão no mesmo repositório. A independência só vale se cada avaliador receber apenas a sua pasta, fora do repositório.
3. O texto da taxonomia menciona "RGAM/V8" em três linhas.
4. Não há captura comum de evidência; os avaliadores veriam páginas vivas.
5. Os relatórios G0, G0.1 e os deste gate contêm julgamentos sobre registros e não devem chegar aos avaliadores.

## 6. Decisões pendentes

**Bloqueiam o início do piloto**

1. Designação de Reviewer A, Reviewer B e Adjudicator; declaração de exposição prévia de cada um.
2. Amostra: opção A, B, C ou D.
3. Rótulos exibidos aos avaliadores: manter os nomes do inventário ou substituir.
4. Critérios de aceitação AC1–AC31; valor do alerta numérico; tamanho da rodada de confirmação.
5. Meio de captura e arquivamento de evidência.
6. Autorização expressa para iniciar.

**Não bloqueiam o piloto, mas precisam de decisão**

7. Adoção da reorientação pela equipe científica (segue pendente).
8. Parâmetros U1–U6 do universo jurídico, a discutir com David Levi-Faur. A nota está em `gates/U1_U6_RESEARCH_UNIVERSE_DECISION_BRIEF.md`, em inglês.
9. Realinhamento da numeração U1–U6: a lista desta fase difere da usada em `SOURCE_SELECTION_FRAMEWORK_v0_1.md`. A nota traz a tabela de equivalência; o quadro não foi editado.
10. Vocabulários provisórios: confirmar, alterar ou retirar.
11. Commit dos documentos de gate, do código e dos testes; publicação no remoto.
12. Destino do vocabulário de funções F1–F8, criado nesta fase.

## 7. Estado de integridade do repositório

| Verificação | Resultado |
|---|---|
| Testes automatizados | 51 de 51 aprovados; Python 3.14.4 |
| `python scripts/cli.py check` | Código 0; nenhum erro; 3 avisos (2 esperados desde o G0 e o novo aviso de URL repetida) |
| `python scripts/cli.py import-seeds` | 0 registros importados; idempotente |
| `python scripts/cli.py report` | Código 0 |
| Tabelas de dados | Inalteradas: 41 seeds em `discovery_records.csv`; demais só com cabeçalho |
| 34 arquivos originais | 33 com o hash do início do G0; 1 alterado de propósito (`scripts/cli.py`) |
| Manifestos de `gates/G0` e `gates/G0_1` | Conferidos sem falha |
| Originais dos documentos de gate | Inalterados após a cópia |
| `.gitignore` | Inalterado; `gates/`, `pilot_a/` e `schemas/` não são ignorados |
| Diretórios `__pycache__` | Nenhum |

**Estado git** (pasta `08_EU_REGULATORY_DATA_SCOPING`):

- Modificado: `scripts/cli.py`.
- Não rastreados: `gates/`, `pilot_a/`, `schemas/`, três scripts novos, três arquivos de teste novos, quatro documentos em `protocol/`, o registro de decisões em `inputs/`.
- Ignorados pelo `.gitignore`: tudo em `outputs/`.
- HEAD: `4a05e8f`. A branch `main` está 1 commit à frente de `origin/main`.
- **Nenhum commit e nenhum push foram feitos.**

Hashes de todos os arquivos criados ou modificados neste gate: `gates/G1_PREP_evidence/FILES.sha256`.

## 8. Recomendação sobre a prontidão

| Dimensão | Avaliação |
|---|---|
| Software | **Pronto.** Os dois defeitos estão corrigidos e cobertos por testes; as ferramentas do piloto validam, trancam e comparam, e recusam operar sobre formulários em branco ou alterados |
| Instrumentos | **Prontos, com ressalvas declaradas.** Formulários equivalentes, cegos e vazios. Rótulos e distribuição dos pacotes pedem decisão |
| Amostra | **Candidata, não aprovada.** Reprodutível, com limites conhecidos; quatro opções na mesa |
| Critérios de aceitação | **Redigidos, não aprovados.** Precisam de data anterior à entrega dos pacotes |
| Pessoas | **Não pronto.** Ninguém designado |
| Evidência | **Não pronto.** Sem procedimento de captura |

**Recomendação.** Não iniciar a codificação. Submeter à equipe, nesta ordem: designação das pessoas; opção de amostra; rótulos; critérios e valor de alerta; procedimento de captura. Cumprido isso, regenerar os pacotes, entregá-los fora do repositório e registrar a autorização. Em paralelo, levar a nota U1–U6 à discussão com David Levi-Faur, porque ela bloqueia G4 e G5 e é o item de prazo mais incerto.

Sobre a amostra, a opção B parece a mais defensável: mantém o sorteio e a semente, e torna explícito, por escrito e antes da execução, o julgamento humano que o algoritmo não podia fazer sozinho. É uma recomendação; a escolha é da equipe.

---

## Registro de conformidade com os limites do gate

| Limite | Estado |
|---|---|
| Codificação humana simulada | Nenhuma. Preenchimentos existem apenas em testes, em diretório temporário, rotulados como sintéticos |
| Triagem sistemática | Nenhuma |
| Seleção definitiva da fonte | Nenhuma |
| Congelamento do protocolo | Nenhum; protocolo e codebook inalterados |
| Publicação, commit, push | Nenhum |
| Alteração de `.gitignore` | Nenhuma |
| Estatísticas fictícias | Nenhuma estatística sobre dados reais; não há dados de codificação |
| Decisões atribuídas a David Levi-Faur | Nenhuma |
| Avanço para G2 | Não |

**Gate:** execução encerrada após a preparação.
