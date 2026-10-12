# REGISTRO DE ALTERAÇÕES — RODADA 2 (G2)

**Data:** 2026-10-10 | Comparado com `mapping/snapshots/round1/MANIFEST_ROUND1.sha256` (132 arquivos, estado ao fim da rodada 1).

## 1. Fora de `mapping/`

| Arquivo | Alteração |
|---|---|
| `tests/test_mapping_base.py` | **Modificado**: um teste (`test_every_executed_search_is_in_the_discovery_log`) passou a ler os registros de consultas de todas as rodadas em vez de só o da rodada 1. Nenhum outro teste foi alterado |
| `tests/test_mapping_round2.py` | **Novo**: 39 testes |

Nenhum dos 161 arquivos que existiam antes da rodada 1 fora de `mapping/` foi alterado (conferido pelo manifesto `mapping/reports/evidence/PRE_G2_BASELINE.sha256`). O inventário de seeds mantém o SHA-256 do G0. `09_BLOG/`, `.gitignore`, o manuscrito e os gates anteriores não foram tocados. Não houve commit nem push.

## 2. Arquivos da rodada 1 modificados (16)

| Arquivo | Natureza | Preserva a rodada 1? |
|---|---|---|
| `data/resources.csv`, `access_endpoints.csv`, `resource_relations.csv`, `discovery_log.csv`, `evidence_registry.csv`, `decisions_log.csv`, `seed_audit.csv`, `search_hits.csv` | **Reconstruídos** pelo construtor a partir das duas curadorias. Ganham linhas; `resources.csv` ganha cinco colunas derivadas; linhas da rodada 1 mantêm identificadores e nomes registrados; estados mudam conforme `verification_history.csv` | Sim: cópia exata em `snapshots/round1/` e testes que comparam |
| `evidence/captures/CAPTURE_LOG.jsonl`, `evidence/searches/SEARCH_LOG.jsonl` | **Só acréscimo** de linhas | Sim: os identificadores de evidência da rodada 1 e seus hashes são conferidos por teste |
| `schemas/mapping_vocabularies.json` | Valores acrescentados; os da rodada 1 permanecem | Sim |
| `scripts/mapping_search.py` | Estendido (paginação, parâmetro de catálogo, cinco serviços) | Sim: os URLs da rodada 1 são idênticos (teste) |
| `scripts/build_mapping_base.py` | Reescrito para fundir curadorias, derivar níveis e gerar cinco tabelas | Sim: reproduz as tabelas da rodada 1 a partir de `round1.py` |
| `scripts/validate_mapping.py` | Verificações acrescentadas | Sim |
| `data/DATA_DICTIONARY.md` | Atualizado; a versão da rodada 1 está em `snapshots/round1/` | Sim |
| `README.md` | Seção de navegação da rodada 2 acrescentada | Sim (índice) |

**Não modificados:** `protocol/INDEPENDENT_MAPPING_REORIENTATION_v1_0.md`, `protocol/SYSTEMATIC_MAPPING_PROTOCOL_v1_0_DRAFT.md`, `protocol/SEARCH_QUERIES_G2_ROUND1.csv`, `reports/G2_INITIAL_MAPPING_REPORT.md`, `reports/G2_NEXT_ROUND_PLAN.md`, `reports/PUBLICATION_POTENTIAL_NOTE.md`, `curation/round1.py`, todos os arquivos preservados de capturas e respostas de busca da rodada 1.

## 3. Arquivos novos (354, mais os acréscimos acima)

| Pasta | Arquivos | Conteúdo |
|---|---|---|
| `curation/` | 1 | `round2.py` |
| `protocol/` | 4 | Emenda A01; proposta de validação humana; registro de consultas da rodada 2; registro da varredura institucional |
| `reports/` | 4 | Resultados da rodada 2; comparação com o LYNX; arquivos de evidência de teste e estatísticas |
| `scripts/` | 4 | `verify_resources.py`, `institutional_sweep.py`, `validation_sample.py`, `round_stats.py` |
| `data/` | 5 | `verification_history.csv`, `data_inspections.csv`, `capabilities.csv`, `institutional_sweep.csv`, `lynx_reference.csv` |
| `snapshots/round1/` | 10 | Tabelas e dicionário da rodada 1, e o manifesto da rodada 1 |
| `evidence/searches/` | 142 | Uma resposta de API por consulta registrada (SR-G2-055 a SR-G2-196) |
| `evidence/captures/` | 96 | Registros de repositório, páginas da varredura, relatórios do LYNX |
| `evidence/inspections/` | 88 | Primeiros bytes de 92 recursos (arquivo por inspeção com leitura bem-sucedida) |

## 4. Defeitos encontrados e corrigidos durante a rodada

| # | Defeito | Efeito | Correção |
|---|---|---|---|
| 1 | O classificador de URLs do Zenodo usava `lastindex` e montava o endereço de registro com o DOI inteiro | 11 requisições de registro devolveram 404 | Corrigido; refeitas. As falhas permanecem no registro de capturas |
| 2 | DOIs de periódicos eram consultados só no DataCite | 7 requisições devolveram 404 | Segunda tentativa automática no Crossref |
| 3 | Endereços propostos pelo agente na varredura institucional que não existem | 9 requisições com 404 | Registradas como falha de acesso; não são evidência sobre os órgãos |
| 4 | A rodada 1 chamou `VERIFIED` quatro linhas com mantenedor inferido ou não apurado | Estado histórico mais forte que a evidência | Mantido; o nível de identidade derivado e o validador sinalizam |
| 5 | A primeira versão do estado de acesso rotulava erros HTTP 404 como erro de rede | Rótulo errado nos pontos de acesso | Valor `HTTP_ERROR` acrescentado ao vocabulário |
| 6 | Entrada duplicada na descrição de um corpus (`Europarl`) | Erro do validador | A URL de descrição foi removida do registro novo |

## 5. Conferências no fim da rodada

| Conferência | Resultado |
|---|---|
| `python -m pytest` | 152 de 152 |
| `python mapping/scripts/validate_mapping.py` | 0 erros, 4 avisos |
| Reconstrução determinística | Teste confere que as tabelas em disco são a saída do construtor |
| Hashes dos arquivos de evidência (capturas, respostas, inspeções) | Conferem |
| Manifesto do G1-READY | 78 de 78 |
| `mapping/MANIFEST.sha256` | Regenerado ao fim da rodada |
