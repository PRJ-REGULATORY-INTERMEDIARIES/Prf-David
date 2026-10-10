# BASELINE RUN — G0

**Data da execução:** 2026-10-09 (local, UTC−03:00) / 2026-10-10T01:55Z
**Executor:** agente de programação (Claude Code), sob coordenação humana. Nenhuma decisão científica foi tomada nesta execução.
**Diretório:** `G:\Meu Drive\PRJ-David\Prf-David\08_EU_REGULATORY_DATA_SCOPING`
**Raiz git efetiva:** `G:/Meu Drive/PRJ-David/Prf-David` (este diretório é subpasta do repositório `Prf-David`, não um repositório próprio)
**Commit de referência (HEAD):** `4a05e8fcd6c8ede443bd17eceaec7d3129b99d29` — 34 arquivos desta pasta rastreados; `git status` limpo para a pasta antes e depois da execução.
**Ambiente:** Python 3.14.4, Windows-11-10.0.26300-SP0. Somente biblioteca padrão para os scripts do projeto (`openpyxl` foi usado apenas para leitura da planilha original, em modo somente leitura).

## 1. Comandos executados e saídas literais

Ordem solicitada no G0. `stdout` e `stderr` capturados separadamente; código de saída e carimbo UTC anexados.

### 1_check

```text
$ python scripts/cli.py check
Data tables initialized. Existing files were not overwritten.
[WARNING] No documented systematic search hits: only seed set or empty inventory.
[WARNING] No canonical dataset inclusion decisions: scientific results not available.
No structural errors.
exit=0
2026-10-10T01:55:20Z
[stderr]
```

### 2_import

```text
$ python scripts/cli.py import-seeds
Data tables initialized. Existing files were not overwritten.
Imported 0 seed hits; dataset inclusion still requires full screening and dataset-level deduplication.
exit=0
2026-10-10T01:55:20Z
[stderr]
```

### 2b_import_again

```text
$ python scripts/cli.py import-seeds
Data tables initialized. Existing files were not overwritten.
Imported 0 seed hits; dataset inclusion still requires full screening and dataset-level deduplication.
exit=0
2026-10-10T01:55:21Z
[stderr]
```

### 3_report

```text
$ python scripts/cli.py report
Data tables initialized. Existing files were not overwritten.
Wrote outputs\STATUS_REPORT.md
# RELATÓRIO INTERMEDIÁRIO — NÃO É RESULTADO FINAL

Gerado em: 2026-10-09T22:55:21-03:00

## Status verificável
- Ocorrências do levantamento exploratório (seeds): **41**; não contam como inclusão.
- Registros documentados de buscas não-semente: **0**.
- Registros sistemáticos com decisão de deduplicação: **0 / 0**.
- Deduplicação integral: **NÃO**.
- Consensus título/descrição completa: **NÃO**.
- Consensus documentação integral completa: **NÃO**.
- Datasets canônicos extraídos: **0**, não equivalentes a portais/serviços.
exit=0
2026-10-10T01:55:22Z
[stderr]
```

### 4_tests

```text
$ python -m unittest discover -s tests -v
exit=0
2026-10-10T01:55:22Z
[stderr]
test_canonical_dataset_ids_are_unique (test_pipeline.ProjectTests.test_canonical_dataset_ids_are_unique) ... ok
test_cohen_kappa (test_pipeline.ProjectTests.test_cohen_kappa) ... ok
test_data_headers (test_pipeline.ProjectTests.test_data_headers) ... ok
test_seed_inventory_count (test_pipeline.ProjectTests.test_seed_inventory_count) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.019s

OK
```

Observação: `2b_import_again` é uma repetição deliberada de `import-seeds` para testar idempotência; não fazia parte da lista mínima.
O `unittest` escreve seu relatório em `stderr` por padrão; isso não indica erro.

## 2. Resultados observados

| Item | Resultado | Evidência |
|---|---|---|
| `cli.py check` | exit 0; 0 ERROR; 2 WARNING | saída acima |
| `cli.py import-seeds` | exit 0; **0 registros importados** (os 41 seeds já estavam em `data/discovery_records.csv`) | saída acima |
| Idempotência da importação | **confirmada**: SHA-256 de `data/discovery_records.csv` idêntico antes, depois da 1ª e depois da 2ª execução (`26367add…d770fe`); 42 linhas (1 cabeçalho + 41) | hashes abaixo |
| `cli.py report` | exit 0; reescreveu `outputs/STATUS_REPORT.md` | única diferença de conteúdo em relação à versão anterior: linha `Gerado em:` |
| `unittest` | **4 testes, 4 OK**, 0 falhas, 0 erros | saída acima |
| Arquivos fora de `outputs/` | **nenhum alterado** | comparação SHA-256 de 34 arquivos antes/depois: idêntica |

Avisos emitidos (esperados no estado atual, não são defeitos):

- `[WARNING] No documented systematic search hits: only seed set or empty inventory.`
- `[WARNING] No canonical dataset inclusion decisions: scientific results not available.`

Erros: nenhum.

Efeitos colaterais: a execução dos testes criou `scripts/__pycache__/` e `tests/__pycache__/` (ignorados pelo `.gitignore` local); foram removidos ao final. `outputs/STATUS_REPORT.md` foi sobrescrito pelo próprio comando `report` (arquivo gerado; a versão anterior diferia apenas no carimbo de data).

## 3. Verificações de consistência adicionais (somente leitura)

| Verificação | Resultado |
|---|---|
| `inputs/seed_inventory_v0_1.csv` | 41 linhas, 41 `source_seed_id` únicos (EU01–EU41), todas com `source_url` |
| Planilha original × CSV de seeds | aba `Inventario` com 41 linhas de dados; **0 células divergentes** em 11 colunas × 41 linhas |
| `data/discovery_records.csv` × seeds | 41 registros `SEED_EUxx`; título e URL idênticos aos seeds |
| URLs repetidas nos seeds | **1 caso**: `https://data.europa.eu/en/ELDS` em **EU03** (EUR-Lex bulk data dump) e **EU07** (European Legal Data Space — diretório) |
| Tabelas `search_runs`, `dedup`, `screening`, `consensus`, `datasets`, `resources`, `audit`, `rit_pilot` | apenas cabeçalho (0 registros) |
| Distribuição `layer` (41) | Corpus normativo 4; Infraestrutura 3; Processo legislativo 6; Delegação/implementação 3; Atores/participação 1; Transposição/Estados 3; Fiscalização 3; Jurisprudência 2; Intermediação RIT 7; Aplicação setorial 2; Corpus acadêmico 7 |
| Distribuição `initial_priority` | P1 19; P2 19; P3 3 |
| `resource_type` | 34 valores distintos para 41 registros (texto livre, sem vocabulário controlado) |

## 4. Sondagens de comportamento do código (cópia isolada)

Executadas em **cópia temporária** de `scripts/`, `inputs/`, `data/` e `tests/` fora do repositório, com linhas artificiais inseridas apenas na cópia. Nenhum dado do projeto foi tocado. Servem para fundamentar `outputs/EXECUTION_PLAN.md`.

| Sondagem | Observado |
|---|---|
| P1 — `kappa_or_na` com pares de avaliadores diferentes (A/B num registro, C/D em outro) e um par `include`/`uncertain` | retornou `n=2, agreement=1.0, kappa=1.0`: pares de avaliadores distintos são agrupados num único kappa; o par com `uncertain` some do cálculo sem contagem |
| P2 — todas as decisões `include` | `kappa=None` (tratado corretamente como indefinido) |
| P3 — seed novo acrescentado ao CSV | importado 1 vez; 2ª execução importou 0; arquivo manteve 1 BOM |
| P4 — URL de um seed alterada **depois** da importação | não detectado: `discovery_records` conserva o valor antigo e nenhum aviso é emitido |
| P5 — valores fora do vocabulário (`origin` inventado, URL inválida, data `31/12/2026`, `reason_code` inexistente, `stage` de consenso inválido, `criterion` inexistente com nota 2, `source_record_ids` inexistente, `validation_status` com grafia divergente, URL duplicada) | `check` **não emitiu nenhum ERROR**; o registro com `origin` inventado foi contado como "systematic hit" |

## 5. Hashes SHA-256 de referência (estado antes da execução = estado depois)

```text
53fa78f46bce08fa3d47605b2b231df4c8f1860decd0840e044c665ca490ffde *./.gitignore
ff0ec5fd16d546cdca4946a89273521528b16ff5bb1d6e2e6393a39b13f73563 *./.vscode/extensions.json
6e13fc64e9190afbe184520d3011f974c02f24d2ae2977199869df55ea978b7f *./.vscode/settings.json
cd66db76cd46e4e1b1b0dfe129a7c1398147783eff1fde5ab5123055b8363775 *./.vscode/tasks.json
9c03271879f49f7072f327445e760e73236766c0038b8b5cef981106488654f0 *./PROMPT_MESTRE_VSCODE.md
fb6b653ae7dbf1e299fc0b452e7508d7761783de80e20d48ad7a685d933f1d18 *./README.md
c1008547ccf5abd37c6050f9226b7e7366ead1e4ddf7865da43ef86d5c9a4cee *./SOURCES_VERIFIED_2026-10-09.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 *./data/ai_runs/.gitkeep
b3c4126e2331808aed95684274163137d10331fdcbb131d12b3f026f9f339daa *./data/audit.csv
30fca8d61c8a6fd5fa64f1784a1c2afe918b3dfbe59d5e90080ffe95d06ca360 *./data/consensus.csv
595ce72cb131a17d9d3766708ea33c95146aea7c6087e2be24544aa0f8f66320 *./data/datasets.csv
57bc155363becd13a01e9670753d7c5cd57e93dfa1b582dc4d796bc5f5edd690 *./data/dedup.csv
26367add878a26ccf5e7c507ddc5f25db1631e13ea7116e7f26d439df8d770fe *./data/discovery_records.csv
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 *./data/raw/.gitkeep
ddabfdb1dd964331ad38c5327a779c5ba5d8b799a0902e96fedfedf04b5d6dd1 *./data/resources.csv
710cced27f42ddf1047a44f8c40f0b7db68285e4fe46886bdd1bf87bf995fa70 *./data/rit_pilot.csv
34bb9c83035768e09c0b0ae25d2fc3e523b64ef97e2c611bc65282626dcfcac0 *./data/screening.csv
c0b4e3590e53da1a88cfca963a55527d30c8de3cb8ef24d9bdb69da5325cea8f *./data/search_runs.csv
60723845ed9b3cefcebfb7ce2ca4358626ae7322d1fd98734e3b7cd06e15c13f *./inputs/ORIGINAL_Exploratory_Inventory_2026-10-09.xlsx
16fad86026fe1890805233875d2cb8ef44f18f759b4eff236a89ee3563f45530 *./inputs/search_queries.csv
45316803ea07f677e0e25b0c559ae2cbee43790da06fb86240953cc9bf670bdd *./inputs/seed_inventory_v0_1.csv
c300b3c56718b90549a938ffc45ba5b57737830069b9a967e7b6c78d47785b14 *./manuscript/FIGURE_TABLE_REGISTER.md
94064ca16ae2b8277e12aba15d3a4bd15b948f51c4161a4d72a58570711e3efd *./manuscript/MANUSCRIPT_SKELETON.md
2ba60745524f844603bbd989c8af61de6751685c4942acf0f023ff37b6ed66ec *./protocol/ANALYSIS_AND_VALIDITY.md
49bd026e884327967980b16e242cfce18d4c0d844273971a4be741fa5666c2b1 *./protocol/CODEBOOK_AND_AUDIT.md
aeff9b5f82c54d2377f096d6fa21cfd76f56e3ab6a7a7cb8148941f9eba04b89 *./protocol/DECISIONS_TO_FREEZE.md
aa65770baba4c37916d599f98d2ebe72f8b5a1bc381f7d8e0ad0560c84a51ed5 *./protocol/LLM_RESEARCH_INTEGRITY.md
fe3476f54055cb382e0524bf837f23d56f0cf98e74de00b8a126d6de8c449c81 *./protocol/PREREGISTRATION_TEMPLATE.md
31bb40adfa5e7f4d902f314a252ff05b742cdb1e0d8f23e592ed6fc91c828da6 *./protocol/PROTOCOL_v1_0_DRAFT.md
0e6f12b26ae141fb16e9bb4b51134ea157f1730632aa42fe3dda4fafd5016383 *./protocol/SEARCH_STRATEGY.md
1eba44ef7e20a62bc4fe606eca83875cc3c5fbdecf81e20e0396c90cc9a2ac6e *./scripts/cli.py
e44f1f8d750b7839037a260a14774134f70e07bf837456beb2ab2ace212d9f1f *./scripts/eu_data_api.py
498732001cc0cac3dbdbc79113d56f3bafaf86cb5ccf500a347be9122a826f95 *./tests/test_pipeline.py
```
