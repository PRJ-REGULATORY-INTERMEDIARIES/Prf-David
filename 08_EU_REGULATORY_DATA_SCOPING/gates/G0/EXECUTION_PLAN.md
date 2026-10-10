# PLANO DE EXECUÇÃO E VIABILIDADE TÉCNICA — G0

**Data:** 2026-10-09 | **Base:** inspeção estática de `scripts/cli.py` (197 linhas), `scripts/eu_data_api.py` (44 linhas) e `tests/test_pipeline.py` (32 linhas), mais a execução registrada em `outputs/BASELINE_RUN.md`.
**Limite desta avaliação:** nenhuma requisição de rede foi feita. Tudo o que depende do comportamento de serviços externos está marcado **UNVERIFIED**. Nenhum coletor foi implementado e nenhum script foi alterado.

## 1. Síntese

O scaffold é um **registro com verificação de integridade referencial**: guarda tabelas CSV com esquema fixo, importa os seeds de forma idempotente, recusa-se a apresentar contagens PRISMA incompletas e avisa quando o trabalho sistemático não existe. Essa parte funciona e foi verificada.

Ele **não é ainda uma cadeia de coleta e triagem**. Faltam: registro automático das buscas, paginação, deduplicação, geração de pacotes cegos, captura de evidência, validação de vocabulário e verificação de hashes. A estatística de concordância tem um defeito que precisa ser corrigido antes de qualquer uso. Nada disso impede o piloto de calibração, que é manual; tudo isso precisa existir antes da busca sistemática.

## 2. Capacidade por requisito

| # | Requisito | Estado | O que existe (verificado) | O que falta |
|---|---|---|---|---|
| 1 | Consultar e registrar fontes | **Parcial** | `eu_data_api.py` faz uma requisição a um endpoint do data.europa.eu e grava resposta e manifesto | Uma plataforma só; uma página só (`page=0` fixo); não escreve em `search_runs.csv`; sem nova tentativa nem pausa entre chamadas; endpoint e parâmetros UNVERIFIED |
| 2 | Preservar dados brutos e metadados | **Parcial** | Resposta gravada byte a byte; manifesto com URL, status, data UTC, SHA-256 e tamanho | `data/raw/` é ignorado pelo git; nenhum comando reconfere os hashes; sem captura de páginas web (emenda A06) |
| 3 | Registrar buscas e parâmetros | **Parcial** | Tabela `search_runs.csv` com 11 colunas; `check` exige `search_run_id` válido em registro `systematic_search` | Preenchimento manual; faltam filtros, paginação, total informado pela plataforma, hash do bruto (emenda A20); `inputs/search_queries.csv` não é lido por nenhum script |
| 4 | Controlar duplicatas | **Ausente como função** | Tabela `dedup.csv`; `check` valida referências e o vocabulário `unique`/`duplicate`; importação de seeds idempotente por `source_seed_id` | Nenhuma canonicalização de URL (`urlsplit` é importado e não usado); nenhuma detecção de candidatos; URL repetida não é sinalizada (EU03/EU07) |
| 5 | Produzir tabelas auditáveis | **Parcial** | Nove tabelas com cabeçalho validado; `report` gera `STATUS_REPORT.md` e se recusa a dar contagens PRISMA incompletas | Sem exportação das tabelas e figuras previstas em `manuscript/FIGURE_TABLE_REGISTER.md`; `report` sobrescreve o anterior e carrega carimbo de hora (saída não determinística) |
| 6 | Verificar integridade e rastreabilidade | **Parcial** | Integridade referencial entre tabelas; IDs duplicados; exclusão sem motivo; nota sem evidência ou data; `NA` sem justificativa; código de saída 2 em erro | Vocabulários não validados (sondagem P5: nove valores inválidos, zero erros); alteração de seed após importação não detectada (P4); `source_record_ids` não conferido; sem manifesto de hashes do repositório |
| 7 | Apoiar estatística e relatório PRISMA-ScR | **Insuficiente** | `kappa_or_na` calcula concordância e kappa binário; trata corretamente o caso de categoria única | Agrupa pares de avaliadores diferentes num só kappa (P1); descarta sem contar os pares com `uncertain`; sem intervalo de confiança; nada para a escala ordinal da auditoria; nenhum gerador de fluxograma ou de matriz dataset × critério |

## 3. Limitações técnicas observadas

Cada item indica onde foi observado. "Sondagem Pn" refere-se à seção 4 de `BASELINE_RUN.md`.

### 3.1 Integridade e validação (`cli.py`, função `issues`)

- **L1 — Vocabulários controlados não são verificados.** `origin`, `reason_code`, `stage` em `consensus.csv`, `criterion` em `audit.csv`, `validation_status` em `rit_pilot.csv`, formato de data e formato de URL passam sem erro. Sondagem P5.
- **L2 — `origin` desconhecido conta como busca sistemática.** A separação usa `origin != 'seed'`; qualquer erro de digitação infla o número de registros "sistemáticos". Linhas 127 e 160. Sondagem P5.
- **L3 — Seeds não têm verificação de integridade.** A importação compara apenas `source_seed_id`. Se o CSV de seeds for editado depois, `discovery_records.csv` diverge em silêncio. Linha 55. Sondagem P4.
- **L4 — `datasets.source_record_ids` não é conferido** contra `discovery_records` nem contra decisão de consenso. É o elo que impede um dataset de entrar sem triagem, e hoje é texto livre.
- **L5 — `check` cria arquivos.** O comando de verificação chama `init()` e, se uma tabela faltar, cria uma vazia em vez de acusar a ausência. Linha 189.
- **L6 — Sem aviso de URL repetida.** Linha 79 só verifica `record_id`.

### 3.2 Concordância (`cli.py`, função `kappa_or_na`)

- **L7 — Pares de avaliadores heterogêneos são agrupados.** A função ordena os nomes dentro de cada registro e trata o primeiro como "avaliador A", seja quem for. O comentário da linha 149 trata só o caso de mais de dois avaliadores. Contraria `ANALYSIS_AND_VALIDITY.md` ("não misturar pares"). Sondagem P1.
- **L8 — `uncertain` desaparece.** Um registro com `include` e `uncertain` fica com uma decisão e é descartado sem contagem; o relatório diz que esses pares "devem ser apresentados separadamente", mas o código não os conta. Linhas 142–146.
- **L9 — Sem intervalo de confiança, sem marginais, sem medida ordinal.**

### 3.3 Coleta (`eu_data_api.py`)

- **L10 — Sem paginação.** `page=0` fixo, `limit` até 1000. Uma consulta com mais resultados que o limite é truncada, e o manifesto não registra o total informado pela plataforma. Linha 25.
- **L11 — Não registra a execução.** O script imprime "Next step: manually populate data/search_runs.csv". O elo entre o arquivo bruto e o registro de busca é manual.
- **L12 — Colisão de nomes.** O nome do arquivo usa segundo UTC, `query_id` e hash da URL; duas execuções idênticas no mesmo segundo se sobrescrevem. Improvável em uso manual, relevante se houver laço.
- **L13 — Sem controle de ritmo nem nova tentativa.** `time` é importado e não usado.
- **L14 — Endpoint não testado.** A URL base, o parâmetro `filters=dataset` e o comportamento de `q` com operadores booleanos são UNVERIFIED (o próprio `SEARCH_STRATEGY.md` avisa disso).
- **L15 — Não lê `inputs/search_queries.csv`.** A consulta é digitada na linha de comando; o `query_id` pode não corresponder ao texto registrado.

### 3.4 Testes

- **L16 — Quatro testes; nenhum cobre `issues()`, `seed_import()`, `report()` ou o script de API.** A idempotência da importação foi confirmada nesta sessão por hash, mas não há teste que a proteja.
- **L17 — Os testes leem os dados reais** (`data/`, `inputs/`), não um diretório temporário (`tempfile` é importado e não usado). Um teste que escrevesse alteraria dados de pesquisa.
- **L18 — O teste do inventário fixa o número 41.** Correto hoje; passa a ser obstáculo se a equipe decidir versionar o inventário.

### 3.5 Repositório e ambiente

- **L19 — Evidências não versionadas.** `outputs/*`, `data/raw/*` e `data/ai_runs/*` estão no `.gitignore` local (emenda A24).
- **L20 — Pasta de trabalho em unidade sincronizada** (`G:\Meu Drive`). Durante esta sessão, um conjunto de arquivos virtuais da própria unidade não pôde ser lido pelo git em outra pasta do repositório. Escrita concorrente em CSV e conflitos de sincronização são riscos reais para tabelas editadas por duas pessoas.
- **L21 — CSV como armazenamento compartilhado.** `screening.csv` único é incompatível com avaliação cega: cada avaliador veria as linhas do outro.
- **L22 — Sem declaração de ambiente.** Não há `pyproject.toml` nem arquivo de versão; o README pede Python ≥ 3.10 e a execução foi em 3.14.4. Não há licença, `CITATION.cff`, dicionário de dados nem lista de verificação PRISMA-ScR no repositório.
- **L23 — Estilo do código.** Indentação de um espaço e várias instruções por linha dificultam revisão por terceiros; importações não usadas (`json`, `urlsplit`, `urlunsplit`, `time`, `tempfile`). Não afeta resultados.

## 4. Melhorias prioritárias

Nenhuma foi implementada. A ordem segue a dependência em relação aos gates.

### Prioridade 0 — antes do piloto de calibração

| ID | Melhoria | Resolve | Esforço |
|---|---|---|---|
| M01 | Decidir onde ficam os documentos de gate para que sejam versionados | L19, emenda A24 | decisão + minutos |
| M02 | Gerador de **pacote cego** por avaliador a partir de `discovery_records.csv` (ID, nome, referência de captura; ordem aleatória com semente registrada) | emenda A07 | pequeno |
| M03 | Modelo de formulário do piloto e pasta `data/pilot/` separada das tabelas formais | plano do piloto | pequeno |
| M04 | Procedimento de captura de evidência com SHA-256 (pode ser manual no piloto) | emenda A06 | pequeno |

### Prioridade 1 — antes do congelamento do protocolo

| ID | Melhoria | Resolve | Esforço |
|---|---|---|---|
| M05 | Validação de vocabulários, datas ISO 8601 e URLs em `issues()`; `origin` desconhecido vira ERROR | L1, L2 | pequeno |
| M06 | Corrigir `kappa_or_na`: calcular por par nomeado de avaliadores; contar e relatar `uncertain`; marginais e intervalo de confiança | L7, L8, L9, emenda A11 | médio |
| M07 | Revisão do esquema conforme emendas aceitas, com versão de esquema e script de migração | emendas A02, A09, A20 | médio |
| M08 | Hash do arquivo de seeds registrado na importação; aviso se divergir | L3 | pequeno |
| M09 | `check` somente leitura; ausência de tabela vira ERROR | L5 | pequeno |
| M10 | Testes em diretório temporário para `issues`, `seed_import`, `report` e para as correções acima | L16, L17 | médio |

### Prioridade 2 — antes da busca sistemática (G2)

| ID | Melhoria | Resolve | Esforço |
|---|---|---|---|
| M11 | Coletor do data.europa.eu lê `search_queries.csv`, pagina até o fim ou até o teto pré-registrado, grava total informado e acrescenta a linha em `search_runs.csv` | L10, L11, L15, emendas A03 e A04 | médio |
| M12 | Comando `verify-raw`: reconfere SHA-256 de todos os brutos contra os manifestos | L19, requisito 6 | pequeno |
| M13 | Canonicalização determinística de URL e lista de **candidatos** a duplicata para decisão humana (nunca fusão automática) | L6, emenda A12 | médio |
| M14 | Arquivos de triagem separados por avaliador, com trancamento por hash antes da fusão | L21 | médio |
| M15 | Um adaptador por plataforma adicional, cada um só depois de lida a documentação e os termos | seção 5 | variável |
| M16 | Declaração de ambiente, licença, `CITATION.cff`, dicionário de dados | L22 | pequeno |

### Prioridade 3 — antes da síntese (G5)

| ID | Melhoria | Resolve |
|---|---|---|
| M17 | Exportadores determinísticos: contagens do fluxograma, matriz dataset × critério, tabelas 1–5 | requisito 7 |
| M18 | Concordância ordinal para a auditoria | emenda A11 |
| M19 | Relatório com data como parâmetro e histórico preservado | requisito 5 |

**Regra para todas as melhorias de código:** nenhuma pode decidir elegibilidade, fundir datasets, atribuir nota de auditoria ou classificar relação. Ferramentas propõem candidatos e conferem consistência; decisões são linhas escritas por pessoas identificadas.

## 5. Plano de coleta por plataforma

Nada nesta tabela foi testado. As colunas "autenticação", "paginação" e "condições" registram **o que precisa ser verificado na documentação oficial na data da execução**, não fatos estabelecidos. As plataformas vêm do PROTOCOL §8 e do `SEARCH_STRATEGY.md`.

| Plataforma | Consultas atuais | Modo previsto | A verificar antes de executar | Risco principal |
|---|---|---|---|---|
| data.europa.eu | Q01–Q06 | API de busca (script existente) | Endpoint e parâmetros; semântica de `q`; limite por página; total informado; termos de uso | Volume muito alto em consultas amplas (emenda A04); catálogo agrega portais nacionais |
| EUR-Lex / CELLAR | Q07 (descritiva) | Inspeção manual estruturada da documentação; eventual consulta SPARQL | Existência e limites do endpoint; necessidade de conta para dumps; condições de reutilização | A fonte é ao mesmo tempo canal de busca e objeto da revisão |
| Parlamento Europeu — Open Data e OEIL | Q08 (descritiva); OEIL sem consulta | Inspeção manual do catálogo de datasets e da documentação da API | Lista de coleções; formatos; sobreposição entre os dois serviços | Dupla contagem (EU08 × EU09) |
| Registros da Comissão (atos delegados, comitologia, grupos de peritos, infrações) | Q11 (descritiva) | Inspeção manual, registro a registro, com roteiro fixo | Se há exportação; URL do registro distinta da página de política | URLs do inventário apontam para páginas explicativas (emenda A27) |
| Conselho | sem consulta | Inspeção manual | Coleções abertas atuais; estado dos datasets antigos | Recursos descontinuados |
| Agências e registros setoriais (NANDO, DSA, EDPB, EEA, ECHA, TED) | Q04 e Q06 apenas via data.europa.eu | Inspeção manual por lista pré-definida de órgãos | Quais órgãos entram na lista e por que critério | Sem lista fechada, a busca não é repetível |
| OpenAlex | Q09 (compartilhada) | API bibliográfica | Sintaxe de busca e filtros; paginação; identificação do cliente | Uma linha para três bases com sintaxes diferentes (emenda A03) |
| Crossref | sem consulta | API bibliográfica | Idem | Idem |
| Scopus / Web of Science | Q09 (compartilhada) | Interface institucional, exportação manual | Se a instituição tem acesso; limites de exportação; termos | Pode não estar disponível; o protocolo diz "se disponíveis" |
| Zenodo / OpenAIRE | Q10 (compartilhada) | API de repositório | Sintaxe; filtro por tipo "dataset"; paginação | Muitos resultados irrelevantes para consulta genérica |
| GitHub | sem consulta | Apenas localização de documentação de corpora já identificados | Regra de uso restrito, como diz o SEARCH_STRATEGY | Virar canal de descoberta não planejado |
| Portais nacionais / N-Lex | Q13, Q14 | Depende da decisão sobre o componente nacional | Quadro amostral (emenda A17) | Escopo aberto |
| Encadeamento de citações | Q12 | Manual, a partir das fontes incluídas | Ferramenta e profundidade | Só pode começar depois da triagem |
| Especialistas | sem procedimento | Consulta dirigida | Quem, como, e como registrar (emenda A17) | Fonte não repetível; relatar como tal |

Para cada plataforma com API, a sequência proposta é sempre a mesma: (1) ler documentação e termos e registrar a data; (2) uma requisição mínima para confirmar formato e total informado, com autorização da equipe; (3) fixar a expressão literal e a regra de paginação em `search_queries.csv`; (4) só então a execução registrada.

## 6. Sequência operacional proposta

| Etapa | Conteúdo | Depende de |
|---|---|---|
| G0 (este gate) | Aprovação do desenho e das decisões pendentes; autorização do piloto | equipe científica |
| G1-a | M01–M04; captura de evidência dos 18; piloto com dois avaliadores; ata de calibração | A05, aprovação da amostra |
| G1-b | Emendas decididas; M05–M10; protocolo e codebook revistos; congelamento e registro | piloto concluído |
| G2-prep | Consultas executáveis por plataforma; medição de volume autorizada; M11–M16 | protocolo congelado |
| G2 | Busca sistemática dentro da janela fixada | G2-prep |

**Nenhuma etapa depois de G0 foi iniciada.**

## 7. O que este plano não cobre

- Estimativa de volume de resultados por consulta: impossível sem executar consultas.
- Estimativa de horas de triagem: depende do volume e dos minutos por registro que o piloto vai medir.
- Compatibilidade de licenças de cada fonte com o depósito do dataset final: exige leitura dos termos, fonte a fonte.
