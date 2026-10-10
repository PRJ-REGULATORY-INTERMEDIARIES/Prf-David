# PILOTO A — INSTRUÇÕES AO AVALIADOR (B)

**Estado:** instrumento preparado; codificação NÃO autorizada até designação dos avaliadores, aprovação da amostra e autorização expressa.

## O que você recebe

| Arquivo | Conteúdo |
|---|---|
| `CODING_FORM_B.csv` | 20 itens, um por linha. As quatro primeiras colunas vêm preenchidas; as demais são suas |
| `SOURCE_TAXONOMY_v0_2_DRAFT.md` | Regras de classificação (níveis, classes, regras R0–R11, relações) |
| `ELIGIBILITY_CRITERIA_PROTOCOL_S6.md` | Critérios de inclusão e exclusão, transcritos da seção 6 do protocolo |
| `INSTRUCTIONS.md` | Este arquivo |

## Regras de independência

1. Trabalhe sozinho. Não converse sobre os itens com ninguém até entregar o formulário.
2. Não consulte o inventário de origem, relatórios do projeto nem o formulário de outro avaliador.
3. Não use modelo de linguagem para decidir. Tradução automática de páginas é permitida; anote em `observations`.
4. Os identificadores (`B-01` …) são neutros e a ordem é aleatória. Não significam nada.
5. Entregue o arquivo ao coordenador sem alterar as quatro primeiras colunas nem o nome das colunas.

## Como preencher

Para cada item: abra `source_url`; se a página não for o recurso, navegue até ele e registre o endereço em `url_actually_used`. Aplique as regras R0–R11 **na ordem**. Registre a evidência que sustentou cada decisão.

| Coluna | Preenchimento |
|---|---|
| `reviewer_id` | Seu identificador, igual em todas as linhas |
| `verification_date` | Data em que você verificou a fonte, `AAAA-MM-DD` |
| `access_outcome` | `acessivel` / `parcial` / `inacessivel` |
| `url_actually_used` | Endereço do recurso, se diferente de `source_url` |
| `operational_level` | `K` contêiner / `L1` recurso / `L2` distribuição / `DUPLICATE` / `UNCERTAIN` |
| `operational_category` | `FPL` `REP` `DSE` `API` `COD` `REG` `AUX` `FDE` `IND` ou `UNCERTAIN`. Para nível `K`, `L2` ou `DUPLICATE`, deixe em branco se a taxonomia não atribuir classe |
| `rule_applied` | A regra que decidiu: `R0` … `R11` |
| `primary_function` | O que o recurso principalmente faz: `F1_TEXTOS_DE_ATOS`, `F2_METADADOS_DE_ATOS`, `F3_ACESSO_PROGRAMATICO`, `F4_CATALOGO_OU_DIRETORIO`, `F5_REGISTRO_DE_ENTIDADES_OU_CASOS`, `F6_CLASSIFICACAO_OU_IDENTIFICACAO`, `F7_CORPUS_PARA_PESQUISA`, `F8_OUTRA`, `UNCERTAIN` |
| `secondary_functions` | Zero ou mais códigos de função, separados por `;` |
| `legislative_candidate` | `sim` / `nao` / `indeterminado` (taxonomia, seção 6) |
| `eligibility` | `include` / `exclude` / `uncertain` |
| `eligibility_reason_code` | Obrigatório se `exclude`: `NOT_EU_RELATED`, `UNSTRUCTURED`, `NOT_LEGAL_REGULATORY`, `NOT_IDENTIFIABLE`, `INSUFFICIENT_DOCUMENTATION`, `OTHER` |
| `eligibility_justification` | Critérios I1–I5 / E1–E5 que fundamentam a decisão |
| `relations` | Duplicação, distribuição ou sobreposição com **outro item deste pacote**: `tipo:ITEM`, separados por `;`. Ex.: `distribution_of:B-07; overlaps_with:B-12`. Tipos: `duplicate_of`, `distribution_of`, `hosted_by`, `derived_from`, `part_of`, `overlaps_with`, `successor_of`, `uses`. Relação com algo fora do pacote: use `tipo:EXTERNAL` e descreva na justificativa |
| `relations_justification` | Evidência de cada relação declarada |
| `evidence_urls` | Endereços das páginas que sustentam suas decisões, separados por `;`. Pelo menos um por item |
| `evidence_notes` | O que em cada página sustenta a decisão |
| `uncertainty_type` | `nenhuma` / `regra_ausente` / `regra_ambigua` / `evidencia_insuficiente` |
| `missing_evidence` | Obrigatório quando houver incerteza: o que faltou |
| `observations` | Livre |
| `minutes` | Tempo gasto no item, em minutos |

## Incerteza

`UNCERTAIN`, `uncertain`, `indeterminado` e `IND` são respostas legítimas. Ninguém espera que você force uma escolha. Sempre que usar uma delas, preencha `uncertainty_type` e `missing_evidence`. A incerteza é um dos resultados que o piloto procura.

## O que o piloto mede

O piloto testa as **regras**, não você e não os recursos. Suas decisões não entram em nenhuma contagem da pesquisa.
