# ESTRATÉGIA DE BUSCA — versão 1.0 proposta

## Princípio

Não existe uma única busca bibliográfica capaz de localizar integralmente datasets governamentais, APIs e corpora jurídico-regulatórios. Usar **busca multicanal** e documentação reproduzível de cada canal (interface, API, artigo, inventário institucional, citações, especialistas). A classificação de coleção canônica será manualmente auditada.

## Fontes principais e instrumentos

**Bloco A — catálogo e infraestrutura jurídica**: data.europa.eu (website + API oficial), EUR-Lex, CELLAR e ELI, European Parliament Open Data, OEIL, Council, EU Commission registers.

**Bloco B — aplicação e intermediários**: NANDO, DSA trusted flaggers, DSA Transparency Database, Comitology, delegated acts, GDPR/EDPB public registers, environmental reporting and notified bodies. Estes são exemplos de buscas-alvo e não inclusões presumidas.

**Bloco C — literatura e depósitos acadêmicos**: OpenAlex, Crossref, Scopus/WoS se disponíveis, Zenodo, OpenAIRE, repositórios institucionais, GitHub usado apenas para encontrar documentação pública de corpora existentes.

**Bloco D — descoberta secundária**: listas de referências das publicações/descrições incluídas, buscas prospectivas de citações quando disponíveis, consultas a especialistas e portais nacionais conectados à UE.

## Expressões base (traduzir por interface e registrar mudança)

- `("European Union" OR "EU law" OR "EUR-Lex") AND ("dataset" OR "corpus" OR "database" OR "API") AND (legislation OR regulation OR directive)`
- `(EU OR European) AND (regulatory OR legislative OR legal) AND ("open data" OR "linked data" OR "knowledge graph")`
- `("notified bodies" OR "trusted flaggers" OR "conformity assessment") AND (register OR dataset OR database)`
- `("transposition" OR "implementing acts" OR "delegated acts") AND (database OR dataset OR API)`
- `("CELEX" OR "ELI") AND (corpus OR dataset OR metadata OR API)`

**Atenção:** data.europa.eu search API aceita `q`, mas o comportamento semântico exato de booleanos deve ser testado. Para maximizar reprodutibilidade, consultas `q` simples também estão listadas em `inputs/search_queries.csv`.

## Limites

- Cobertura temporal dos datasets: sem limite a priori.
- Janela de buscas: registrar abertura, encerramento e data de última atualização nos logs.
- Idiomas: inglês na busca principal; francês/alemão e outros sob busca direcionada, todos registrados.
- Critério de parada: executar todas as plataformas pré-definidas; documentar buscas suplementares, falhas, barreiras de acesso. Saturação conceitual não é justificativa para omitir canais obrigatórios.

## Logging obrigatório

Em `data/search_runs.csv`: ID, data (ISO 8601), plataforma, ID e literal da query, URL, método, resultados recuperados, arquivo de exportação, operador e notas. Uma linha por execução, não por tipo de consulta.

Em `data/discovery_records.csv`: uma linha por hit, vinculada ao `search_run_id`, preservando duplicatas até a etapa de deduplicação.

Em `data/dedup.csv`: identificar duplicações de registros, não de recursos; documentar ID canônico e revisor.

Armazenar payload bruto de API em `data/raw/api/` e calcular SHA-256 quando fizer parte da coleta efetiva. `scripts/eu_data_api.py` faz armazenamento bruto sem triagem ou ingestão automática.

## Teste de recuperação com seeds

Selecionar 12–15 seeds de diferentes famílias e comparar sua presença nas buscas: *recall de seeds* = número recuperado / número de seeds testados. A métrica é um controle de sensibilidade do procedimento, **não** uma estimativa da sensibilidade no universo desconhecido. Insucesso exige revisão documentada das strings e nova execução dos canais afetados.

## Documentação de falhas

Manter registros de zero resultados, timeouts, autorização, bloqueio de acesso, resultados paginados e condições de licença. Nunca imputar 0 resultados sem execução registrada.
