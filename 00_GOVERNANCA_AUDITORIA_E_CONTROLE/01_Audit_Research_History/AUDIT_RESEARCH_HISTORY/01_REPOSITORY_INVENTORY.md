# Inventário do repositório e cobertura

**Raiz:** `G:\Meu Drive\PRJ-David\Prf-David`. **Data:** 2026-10-01 (America/Sao_Paulo). **HEAD:** `a12999c14614f99b1ca0a51950b74c2a4beb58a7` em `main`.

## Estado Git preservado antes dos relatórios

A saída inicial de `git status --short --branch` indicava `main...origin/main [ahead 1]`. A árvore já apresentava remoções staged e múltiplas áreas como untracked, entre elas `Before_R2/`, `R4_CROSS_DOMAIN_VALIDATION/`, `RELATIONAL_LEXIMETRICS_PILOT/`, `WORK_2_1/`, `ENVIO_R4_TO_DAVID/` e `Enviados/`. Essa organização é preexistente e não foi normalizada.

## Repositórios e estrutura

Foi encontrado um repositório Git principal em `.git`; uma worktree; nenhum submódulo ativo ou repositório aninhado; branches `main`, `origin/main`, `origin/HEAD`; sem tags. O reflog acessível registra clone em 29 set e HEAD em 1 out. Diretórios substantivos incluem `00_ADMIN`, `Arquitetura de trabalho`, `Before_R2`, `Bibliografia`, `Post_R2`, `RELATIONAL_LEXIMETRICS_PILOT`, `R4_CROSS_DOMAIN_VALIDATION`, `WORK_2_1`, `ENVIO_R4_TO_DAVID`, `Enviados`, `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047` e `CODEX_ROTEM_SHARE_PACKAGE_20260930_2153`. `R3_CLEANROOM` aparece como arquivo histórico no R4, não checkout próprio.

## Cobertura

Foram inventariados 1499 arquivos acessíveis antes da criação da auditoria. Extensões mais frequentes: .md=558, .csv=438, .py=122, .json=82, .yaml=55, .html=51, .ps1=36, .docx=33, .txt=26, .pdf=23, .png=15, [no extension]=13, .xlsx=12, .xhtml=12. `01_FILE_INVENTORY.csv` registra caminho, extensão, tamanho, mtime local não verificado e SHA-256 atual. A busca percorreu a raiz, excluindo `.git` e a própria auditoria.

Cobertura exaustiva de caminhos, não leitura semântica integral de todos os arquivos. Foram lidos prioritariamente relatórios de fase, closeout, manifests e decisões; binários DOCX/XLSX/PDF/ZIP não foram extraídos em lote. Sessões locais fora do workspace não foram acessadas. Assim, itens não lidos estão cobertos pelo índice, mas não devem ser tratados como conteúdo validado. Nenhum projeto alheio foi claramente identificado.
