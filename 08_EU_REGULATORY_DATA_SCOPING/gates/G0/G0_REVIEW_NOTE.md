# NOTA DE REVISÃO G0 — PRONTIDÃO CIENTÍFICA

**Projeto:** Mapping European Union Legislative and Regulatory Datasets: A Scoping Review of Data Infrastructures and Their Capacity to Represent Regulatory Governance Architectures
**Data:** 2026-10-09 | **Elaboração:** agente de programação (Claude Code), sob coordenação humana | **Destinatário:** equipe científica do PRJ-David

## Conclusão

**O repositório está íntegro e o desenho é sólido, mas o protocolo não está pronto para ser congelado.** Recomenda-se uma aprovação **condicional** do G0: autorizar o piloto de calibração com 18 registros, e não autorizar o congelamento do protocolo nem a busca sistemática até que cinco questões críticas tenham decisão registrada.

As cinco questões: ordem dos gates (A01), regra de dataset canônico (A02), consultas não executáveis (A03), regra de volume da triagem (A04) e nomeação dos avaliadores (A05). As três últimas não impedem o piloto; a A05 impede.

**Classificação das conclusões**

- **VERIFIED** — observado diretamente nesta sessão, em arquivo ou em saída de comando.
- **UNVERIFIED** — depende de fato externo não testado (rede, conteúdo de páginas, comportamento de APIs, disponibilidade de pessoas).
- **PROPOSED** — recomendação ou julgamento metodológico; depende de decisão humana.

Documentos associados: `outputs/BASELINE_RUN.md`, `protocol/PROPOSED_AMENDMENTS.md`, `outputs/PILOT_CALIBRATION_PLAN.md`, `outputs/EXECUTION_PLAN.md`.

---

## 1. Estado atual do repositório

| # | Conclusão | Classe |
|---|---|---|
| 1.1 | A pasta é subdiretório do repositório git `Prf-David`, não repositório próprio. 34 arquivos rastreados no commit `4a05e8f`; árvore limpa para a pasta. | VERIFIED |
| 1.2 | O commit `4a05e8f` é local; a branch `main` está um commit à frente de `origin/main`. Nada foi publicado. | VERIFIED |
| 1.3 | Todos os arquivos citados no G0 existem e foram lidos na íntegra: `README.md`, `PROMPT_MESTRE_VSCODE.md`, sete documentos de `protocol/`, os dois CSV de `inputs/`, `SOURCES_VERIFIED_2026-10-09.md`, dois scripts, um arquivo de testes, nove tabelas de `data/`, dois arquivos de `manuscript/`. | VERIFIED |
| 1.4 | O inventário de seeds tem 41 registros, 41 identificadores únicos, e coincide célula a célula com a aba `Inventario` da planilha original (0 divergências em 451 células). | VERIFIED |
| 1.5 | `data/discovery_records.csv` contém os 41 seeds com origem `seed`. As outras oito tabelas têm só cabeçalho. Não existe nenhuma busca, triagem, dataset canônico, nota de auditoria ou caso RIT registrado. | VERIFIED |
| 1.6 | O `.gitignore` local exclui `outputs/*`, `data/raw/*` e `data/ai_runs/*`. Quatro dos cinco documentos deste G0 **não estão no histórico git**. | VERIFIED |
| 1.7 | Ausentes: declaração de ambiente, licença, `CITATION.cff`, dicionário de dados, lista de verificação PRISMA-ScR, registro de emendas. | VERIFIED |
| 1.8 | As páginas e serviços apontados pelas 41 URLs e pelas 10 referências de `SOURCES_VERIFIED` estão ativos e contêm o que se descreve. | UNVERIFIED |
| 1.9 | Arquivos originais preservados: SHA-256 dos 34 arquivos idêntico antes e depois da sessão. Criados: cinco documentos. Reescrito pelo próprio comando `report`: `outputs/STATUS_REPORT.md` (muda apenas a data). | VERIFIED |

## 2. Resultados efetivamente observados nos testes

| # | Conclusão | Classe |
|---|---|---|
| 2.1 | `python scripts/cli.py check`: código de saída 0, nenhum erro estrutural, dois avisos esperados (sem buscas sistemáticas; sem datasets canônicos). | VERIFIED |
| 2.2 | `python scripts/cli.py import-seeds`: importou 0 registros, porque os 41 já estavam presentes. | VERIFIED |
| 2.3 | A importação é idempotente: hash de `discovery_records.csv` idêntico antes e depois de duas execuções; em cópia isolada, um seed novo foi importado uma vez e não se duplicou. | VERIFIED |
| 2.4 | `python scripts/cli.py report`: código 0; relatório coerente com o estado das tabelas; recusa-se a gerar contagens PRISMA. | VERIFIED |
| 2.5 | `python -m unittest discover -s tests -v`: 4 testes, 4 aprovados. | VERIFIED |
| 2.6 | Os quatro testes cobrem contagem de seeds, cabeçalhos, um caso de kappa e unicidade de IDs. Não cobrem validação, importação, relatório nem o script de API. | VERIFIED |
| 2.7 | A verificação de integridade não detecta valores fora do vocabulário controlado: nove valores inválidos inseridos em cópia isolada produziram zero erros. | VERIFIED |
| 2.8 | A função de kappa agrupa pares de avaliadores diferentes e descarta sem contagem os pares com `uncertain`. | VERIFIED |
| 2.9 | `scripts/eu_data_api.py` funciona contra o serviço real. | UNVERIFIED (não executado; nenhuma requisição de rede nesta sessão) |

## 3. Avaliação crítica do protocolo

### Pontos fortes

| # | Conclusão | Classe |
|---|---|---|
| 3.1 | O protocolo distingue quatro níveis de identidade (ocorrência, dataset canônico, distribuição, objeto substantivo) e proíbe somá-los. É a salvaguarda mais importante contra a inflação de contagens. | VERIFIED (texto) |
| 3.2 | O estatuto dos 41 seeds é declarado de forma consistente em README, protocolo, estratégia de busca, prompt mestre e código: não são amostra, não são inclusão. | VERIFIED |
| 3.3 | A distinção `UNVERIFIED` ≠ `NO` e `NA` ≠ ausente está no protocolo, no codebook e parcialmente no código. | VERIFIED |
| 3.4 | O subestudo RIT é declarado exploratório e separado, e o codebook exige norma, artigo, papéis e trilha de evidência para o nível D3. | VERIFIED (texto) |
| 3.5 | A política de uso de IA proíbe decisão automática de inclusão e exige registro. | VERIFIED (texto) |
| 3.6 | O desenho — revisão de escopo mais auditoria técnica original, sem inferência estatística sobre universo desconhecido — é adequado à pergunta e publicável se executado como descrito. | PROPOSED |

### Avaliação por dimensão solicitada

| Dimensão | Avaliação | Classe | Emenda |
|---|---|---|---|
| Clareza das perguntas | RQ2 e RQ4 são claras. RQ1 e RQ5 pedem universo e contagem que o plano de análise declara inalcançáveis. RQ3 é pergunta da auditoria, não do mapeamento. | PROPOSED | A15 |
| Adequação do PCC | Utilizável, mas a adaptação de "Population" para recursos de dados não é justificada e se sobrepõe ao "Concept". Limite do contexto nacional indefinido. | PROPOSED | A16, A17 |
| Inclusão e exclusão | Coerentes entre si. Não cobrem padrões, vocabulários, catálogos, derivados e software, classes presentes no próprio inventário. | VERIFIED (lacuna no texto) | A02 |
| Estratégias de busca | Não reprodutíveis no estado atual: 5 de 14 consultas são descrições; 2 linhas servem a várias bases; várias fontes do protocolo não têm consulta; sem regra de volume; data de fechamento em branco. | VERIFIED | A03, A04, A13 |
| Unidade de análise | Bem concebida em quatro níveis; sem regra operacional de identidade canônica. | VERIFIED (lacuna) | A02 |
| Dataset × portal × API × registro × corpus | A distinção é afirmada, mas não há vocabulário controlado: o inventário usa 34 rótulos diferentes para 41 registros. | VERIFIED | A02 |
| Deduplicação | Dois níveis previstos; sem regra de canonicalização, sem responsável, sem verificação, sem ferramenta. | VERIFIED | A12 |
| Avaliação independente e adjudicação | Bem desenhada no papel. Avaliadores não nomeados; tabela única de triagem impede cegamento; evidência não é congelada. Viabilidade depende de pessoas. | VERIFIED (lacunas); viabilidade UNVERIFIED | A05, A06, A07 |
| Auditoria e interoperabilidade | Escala com âncoras claras. Protocolo lista 8 critérios e o codebook 9; critérios de distribuição pontuados por dataset; "inspeção suficiente" indefinida. | VERIFIED | A09, A10 |
| Risco de viés | Ancoragem nas colunas de julgamento do inventário; circularidade entre o instrumento D0–D3 e o quadro teórico da equipe; regra de corte de volume não pré-registrada. | PROPOSED | A07, A08, A04 |
| JBI | Segue a estrutura geral. A etapa 1 da busca em três etapas é substituída por seeds sem declaração. A ordem piloto–congelamento está invertida. | PROPOSED | A01, A19 |
| PRISMA-ScR | Itens 5 (registro), 8 (estratégia completa), 10 (piloto do formulário de extração) e 12 (avaliação crítica) precisam de definição. | PROPOSED | A19 |
| FAIR | Declarado como inspiração, sem mapa critério × princípio. Sem critério para identificador persistente do próprio dataset. | VERIFIED (ausência do mapa) | A18 |

## 4. Problemas metodológicos e técnicos

### Capazes de comprometer a publicação

| # | Problema | Classe | Emenda |
|---|---|---|---|
| 4.1 | **O denominador central não é reprodutível.** Sem regra de dataset canônico, dois avaliadores contam datasets diferentes. | PROPOSED (consequência); VERIFIED (ausência da regra) | A02 |
| 4.2 | **A busca não pode ser repetida por terceiros.** | VERIFIED | A03 |
| 4.3 | **Risco de inviabilidade da triagem dupla integral** se consultas amplas devolverem volume alto; corte decidido depois dos resultados introduz viés. | UNVERIFIED (volume); PROPOSED (regra) | A04 |
| 4.4 | **Concordância entre avaliadores sem avaliadores definidos.** Se a triagem dupla não ocorrer como descrita, o relato não pode afirmá-la. | VERIFIED (ausência de nomeação) | A05 |
| 4.5 | **Congelar antes de calibrar** gera emendas pós-registro previsíveis, que enfraquecem o valor do pré-registro. | PROPOSED | A01 |
| 4.6 | **Validade de construto da "capacidade de representar arquiteturas regulatórias".** Instrumento original, não validado, derivado do quadro dos autores. | PROPOSED | A08 |

### Que comprometem reprodutibilidade ou transparência

| # | Problema | Classe | Emenda / melhoria |
|---|---|---|---|
| 4.7 | Evidência de triagem e auditoria não é arquivada; páginas mudam. | VERIFIED (ausência do requisito) | A06 |
| 4.8 | Estatística de concordância inadequada para o piloto e com defeito de implementação. | VERIFIED | A11, M06 |
| 4.9 | Esquema de dados não comporta campos que o protocolo exige; a tipologia D0–D3 não tem coluna. | VERIFIED | A20, M07 |
| 4.10 | Verificação de integridade não valida vocabulários. | VERIFIED | M05 |
| 4.11 | Documentos de gate e dados brutos fora do controle de versão. | VERIFIED | A24, M01 |
| 4.12 | Coletor sem paginação e sem registro automático da busca. | VERIFIED | M11 |
| 4.13 | Trabalho em pasta sincronizada com edição concorrente de CSV. | VERIFIED (configuração); risco PROPOSED | — |
| 4.14 | Dados pessoais em recursos do inventário tratados apenas em termos gerais. | PROPOSED | A21 |

Lista completa, com localização no código: `outputs/EXECUTION_PLAN.md`, seção 3 (23 limitações).

## 5. Amostra proposta para calibração

Dezoito registros, três por estrato, todos com identificador existente no inventário. Seleção intencional por diversidade, não aleatória. **Classe: PROPOSED** — depende de aprovação. Nenhum registro foi triado.

| Estrato | Registros |
|---|---|
| A — repositórios legislativos oficiais | EU01, EU03, EU18 |
| B — APIs e dados vinculados | EU02, EU08, EU34 |
| C — corpora acadêmicos | EU35, EU39, EU40 |
| D — implementação e fiscalização | EU15, EU21, EU25 |
| E — registros de organizações intermediárias | EU26, EU28, EU29 |
| F — restrito, descontinuado ou ambíguo | EU05, EU11, EU17 (EU03 também é caso de acesso restrito) |

Suplentes, em ordem: EU22, EU31, EU07, EU19, EU41, EU38.

| # | Conclusão | Classe |
|---|---|---|
| 5.1 | Os 18 identificadores e os 6 suplentes existem em `inputs/seed_inventory_v0_1.csv`. | VERIFIED |
| 5.2 | A amostra cobre 10 das 11 famílias de origem; falta Jurisprudência. Prioridades P1/P2/P3: 11/5/2, contra 19/19/3 no universo. | VERIFIED |
| 5.3 | As dificuldades de classificação listadas no plano são hipóteses lidas do inventário; o que cada recurso de fato oferece não foi conferido. | UNVERIFIED |
| 5.4 | A seleção foi feita por agente de IA com acesso às colunas de julgamento do inventário; os avaliadores não devem vê-las. | VERIFIED (fato); PROPOSED (cegamento) |

Justificativa por registro, regras em teste e procedimento para os dois avaliadores: `outputs/PILOT_CALIBRATION_PLAN.md`.

## 6. Emendas recomendadas

Vinte e sete emendas em `protocol/PROPOSED_AMENDMENTS.md`: 5 críticas, 8 altas, 11 médias, 3 baixas. **Todas PROPOSED; nenhuma aplicada; nenhum documento do protocolo foi alterado.**

| Gravidade | Emendas |
|---|---|
| CRÍTICA | A01 ordem dos gates · A02 tipologia de unidades e dataset canônico · A03 consultas executáveis · A04 regra de volume · A05 equipe de avaliação |
| ALTA | A06 evidência arquivada · A07 cegamento · A08 circularidade do instrumento · A09 nível dos critérios · A10 lista única de critérios · A11 concordância · A12 deduplicação · A13 data de fechamento |
| MÉDIA | A14 etapas de triagem · A15 RQs · A16 PCC · A17 componente nacional e especialistas · A18 mapa FAIR · A19 PRISMA-ScR/JBI · A20 esquema · A21 dados pessoais · A22 teste de recuperação · A23 casos RIT · A24 versionamento |
| BAIXA | A25 idioma · A26 rótulo "verificadas" · A27 URLs dos seeds |

## 7. Condições para aprovação do G0

Todas PROPOSED. Distinguem-se dois níveis, conforme a emenda A01.

### Para autorizar o piloto de calibração

| # | Condição | Estado hoje |
|---|---|---|
| C1 | Decisão sobre a ordem dos gates (A01) | pendente |
| C2 | Avaliador 1, avaliador 2 e adjudicador nomeados (A05) | pendente |
| C3 | Lista de 18 registros aprovada ou alterada | proposta entregue |
| C4 | Critério de passagem do piloto escrito antes da abertura das respostas (A11) | pendente |
| C5 | Regra de cegamento e de captura de evidência aceita (A06, A07) | proposta entregue |
| C6 | Local versionado para os documentos de gate (A24) | pendente |

### Para congelar o protocolo e iniciar a busca (não satisfeitas)

| # | Condição | Estado hoje |
|---|---|---|
| C7 | Piloto concluído e codebook revisto | não iniciado |
| C8 | Regra de dataset canônico e tipologia de unidades no codebook (A02) | pendente |
| C9 | Consultas executáveis por plataforma, com regra de volume e janela de datas (A03, A04, A13) | pendente |
| C10 | Lista única de critérios de auditoria, com nível de aplicação (A09, A10) | pendente |
| C11 | Decisão registrada para cada uma das 27 emendas | pendente |
| C12 | Correções de prioridade 1 no código (M05–M10) | não iniciado |
| C13 | Plataforma e momento do registro público definidos; template de pré-registro preenchido | pendente |

## 8. Plano operacional para o G1

PROPOSED. Não iniciado; depende de autorização.

| Passo | Atividade | Responsável sugerido | Produto |
|---|---|---|---|
| 1 | Decidir C1–C6 | coordenação científica | ata com decisões datadas |
| 2 | Preparar pacote cego, formulário e pasta do piloto (M02–M04) | responsável pela infraestrutura | arquivos do piloto |
| 3 | Capturar evidência dos 18 registros, um a um, com data e hash | coordenador da busca, que não avalia | capturas arquivadas |
| 4 | Avaliação independente | avaliador 1 e avaliador 2 | dois arquivos trancados |
| 5 | Comparação descritiva e reunião de calibração | avaliadores e adjudicador | ata de divergências |
| 6 | Revisão do codebook e do protocolo; decisão das emendas | equipe | protocolo revisto |
| 7 | Correções de código de prioridade 1 e novos testes | responsável pela infraestrutura | versão testada |
| 8 | Congelamento e registro | equipe | protocolo v1.0 com identificador |

Detalhes: `outputs/PILOT_CALIBRATION_PLAN.md` (seções 5–8) e `outputs/EXECUTION_PLAN.md` (seções 4 e 6).

## 9. Decisões que dependem da equipe científica

Nenhuma destas foi tomada, presumida ou simulada.

**Desenho**

1. G0 autoriza o piloto e o congelamento fica para G1, ou mantém-se a ordem atual? (A01)
2. Padrões, vocabulários, catálogos, benchmarks derivados e software são unidades elegíveis, distribuições ou contexto? (A02)
3. O componente nacional permanece no escopo? Com que quadro amostral? (A17)
4. As RQs 1, 3 e 5 são reformuladas? (A15)
5. Entra um critério de identificador persistente do dataset? (A18)

**Pessoas**

6. Quem são os dois avaliadores e o adjudicador? Quem construiu o inventário exploratório pode avaliar? (A05, A07)
7. Se não houver dois avaliadores para toda a triagem, o desenho é rebaixado de forma declarada? (A05)
8. Haverá avaliador externo ao projeto na auditoria? (A08)
9. A estratégia de busca terá revisão por bibliotecário ou par? (A19)

**Execução**

10. A lista de 18 registros é aprovada? Inclui-se Jurisprudência?
11. Qual o critério de passagem do piloto? (A11)
12. Autoriza-se uma requisição mínima por plataforma apenas para medir volume? (A04)
13. Qual a janela de datas da busca? (A13)
14. Scopus e Web of Science estão disponíveis institucionalmente? (A03)
15. É necessário parecer ético ou de proteção de dados? (A21)

**Registro e publicação**

16. Onde e quando o protocolo é registrado? Em que idioma? (A01, A25)
17. Os documentos de gate passam a ser versionados? Os commits desta pasta podem ser publicados no remoto? (A24)
18. Equipe, afiliações, financiamento e conflitos de interesse para o pré-registro.

**Subestudo exploratório RIT**

19. Critérios de seleção e momento de congelamento dos 3–5 casos. (A23)

---

## Registro de integridade desta sessão

- Nenhuma busca sistemática, coleta em lote ou requisição de rede.
- Nenhum dataset, fonte, resultado, decisão de avaliador ou concordância inventados.
- Nenhum dos 41 seeds foi tratado como dataset elegível.
- A operacionalização RGAM, o V8 e os demais subprojetos do PRJ-David não foram tocados.
- Protocolo não congelado; nenhum documento de protocolo alterado; emendas apenas propostas.
- Nenhum commit e nenhuma publicação remota nesta etapa.
- **Gate:** a execução se encerra aqui. G1 e G2 não foram iniciados.
