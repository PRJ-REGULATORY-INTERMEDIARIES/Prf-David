# Auditoria de recuperação Git — PRJ-David

**Data:** 03/10/2026  
**Repositório:** `G:/Meu Drive/PRJ-David/Prf-David`  
**Escopo:** investigação local não destrutiva; nenhum arquivo físico foi apagado ou sobrescrito.

## Referências de segurança

- HEAD problemático preservado pela tag `checkpoint/pre-recovery-2026-10-03-ae1af32`, apontando para `ae1af320b1f952a0e2fdd0d2142caf5d3886db46`.
- Estado imediatamente anterior preservado pela branch `safety/pre-recovery-parent-a12999c`, apontando para `a12999c14614f99b1ca0a51950b74c2a4beb58a7`.
- Remote atual: `origin/main`.

## Reconciliação do commit `ae1af32`

Comparação: `a12999c..ae1af32`, usando `git diff --diff-filter=D` e comparação SHA-1 de blob Git entre a versão histórica e o arquivo físico vigente.

| Classe | Quantidade |
|---|---:|
| Caminhos removidos no commit | 1.141 |
| Removidos ainda presentes e idênticos | 76 |
| Removidos ainda presentes, mas modificados | 1.065 |
| Removidos ausentes no disco | 0 |

Os 1.141 caminhos são identificáveis precisamente por:

```text
git diff --name-only --diff-filter=D -z a12999c14614f99b1ca0a51950b74c2a4beb58a7 ae1af320b1f952a0e2fdd0d2142caf5d3886db46
```

Não foram restaurados automaticamente porque 1.065 conteúdos físicos divergem da versão histórica. A preservação correta exige versionar o conteúdo físico vigente em uma recuperação explicitamente marcada, sem apresentá-lo como restauração byte a byte.

## Distribuição dos caminhos removidos

| Área | Idênticos | Modificados | Total |
|---|---:|---:|---:|
| `Before_R2` | 44 | 538 | 582 |
| `R4_CROSS_DOMAIN_VALIDATION` | 19 | 317 | 336 |
| `ENVIO_R4_TO_DAVID` | 3 | 185 | 188 |
| `Enviados` | 8 | 4 | 12 |
| `WORK_2_1` | 0 | 11 | 11 |
| `Arquitetura de trabalho` | 0 | 5 | 5 |
| `Post_R2` | 1 | 2 | 3 |
| Outros arquivos de raiz/arquivo | 1 | 3 | 4 |

## Arquivos físicos fora do histórico pai

Há 1.528 caminhos não rastreados; 387 não pertenciam ao histórico do pai `a12999c`:

- 20 documentos de projeto, auditoria e validação, incluindo `ASTRA_EXECUTION_RECOVERY_REPORT.md`, `AUDIT_RESEARCH_HISTORY/`, `RELATORIOS_DE_ESTADO_DO_PROJETO/` e `validation/`.
- 361 arquivos de acervo científico, incluindo R2/R3/R4, PILOT, Rotem, ARQGOV, fontes e reprodutibilidade.
- 2 itens administrativos ainda não elegíveis por padrão: `AUDIT_RESEARCH_HISTORY.zip` e `Prf-David.code-workspace`.
- 4 arquivos em `validation/` são documentação científica criada nesta execução anterior e devem ser revisados no commit documental.

Os subdiretórios `__pycache__/` e logs de execução foram mantidos fisicamente e não devem ser incluídos automaticamente sem classificação adicional.

## Estado da etapa

- Índice não alterado.
- Nenhum commit novo criado.
- Nenhum push realizado.
- Nenhum arquivo físico removido, substituído ou sobrescrito.

## Estratégia proposta para aprovação

1. Criar uma branch local de recuperação a partir de `origin/main`, sem reescrever o remoto.
2. Reintroduzir em um commit de recuperação o conjunto dos caminhos históricos presentes no disco, preservando o conteúdo físico atual e registrando as divergências.
3. Separar em commits documentais os relatórios de 03/10/2026 e a auditoria Git.
4. Separar, quando possível, acervo científico e reprodutibilidade de arquivos administrativos, caches, pacotes compactados e workspaces.
5. Executar `git diff --check`, revisar a lista staged e comparar manifests/hash antes de qualquer push.
6. Fazer push somente se a branch resultante estiver linearmente baseada em `origin/main`, sem force-push e sem conflito remoto.

