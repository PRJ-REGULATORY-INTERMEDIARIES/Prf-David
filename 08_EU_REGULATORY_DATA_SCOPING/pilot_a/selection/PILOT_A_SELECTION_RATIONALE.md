# PILOTO A — AMOSTRA CANDIDATA: JUSTIFICATIVA

**Data:** 2026-10-09 | **Estado:** CANDIDATA — depende de aprovação humana. Nenhum registro foi classificado ou triado.
**Uso restrito ao coordenador.** Este arquivo e os demais desta pasta contêm colunas do inventário que os avaliadores não devem ver.

## 1. Resultado

Execução única de `scripts/select_pilot_a.py`, aceita na 9ª tentativa.

| ID | Nome (inventário) | Família (`layer`) | `resource_type` | Propriedades objetivas |
|---|---|---|---|---|
| EU01 | EUR-Lex — legislação e documentos jurídicos | Corpus normativo | Portal/corpus | host eur-lex.europa.eu; tipo composto |
| EU02 | CELLAR — repositório e grafo de metadados | Corpus normativo | Grafo/API | host op.europa.eu; tipo composto |
| EU03 | EUR-Lex bulk data dump | Corpus normativo | Arquivo em lote | URL idêntica à de EU07; host data.europa.eu |
| EU07 | European Legal Data Space — diretório | Infraestrutura | Catálogo de coleções | URL idêntica à de EU03; host data.europa.eu |
| EU08 | European Parliament Open Data API — procedures | Processo legislativo | API estruturada | — |
| EU13 | Register of Commission Documents | Processo legislativo | Base documental | host commission.europa.eu |
| EU15 | Comitology Register — comitês e atos de execução | Delegação/implementação | Base processual | host commission.europa.eu |
| EU17 | EU Transparency Register | Atores/participação | Cadastro de atores | host data.europa.eu |
| EU19 | N-Lex — bases legais nacionais | Transposição/Estados | Portal federado | — |
| EU23 | ECLI / European e-Justice — busca de jurisprudência | Jurisprudência | Padrão/federação | host eur-lex.europa.eu; tipo composto |
| EU24 | Competition Case Search — antitrust, mergers, State aid, DMA | Fiscalização | Base multissetorial | — |
| EU25 | EDPB — register of final one-stop-shop GDPR decisions | Fiscalização | Registro de decisões | — |
| EU27 | DSA Transparency Database — statements of reasons | Intermediação RIT | Dataset de eventos | host digital-strategy.ec.europa.eu |
| EU28 | DGA — Register of Data Intermediation Services | Intermediação RIT | Cadastro temático | host digital-strategy.ec.europa.eu |
| EU30 | EEA Eionet — Reporting Obligations Database (ROD) | Intermediação RIT | Base de obrigações | — |
| EU32 | ECHA CHEM — REACH / CLP | Intermediação RIT | Cadastro regulatório | — |
| EU33 | TED Open Data Service (contratações) | Aplicação setorial | Grafo de dados | — |
| EU37 | JRC-Acquis | Corpus acadêmico | Corpus paralelo | host joint-research-centre.ec.europa.eu |
| EU39 | LexGLUE — subtarefa EUR-LEX | Corpus acadêmico | Benchmark jurídico | — |
| EU41 | ParlTrack | Corpus acadêmico | Base cívica derivada | — |

**Reserva para confirmação (21):** EU04, EU05, EU06, EU09, EU10, EU11, EU12, EU14, EU16, EU18, EU20, EU21, EU22, EU26, EU29, EU31, EU34, EU35, EU36, EU38, EU40.

## 2. Reprodução

```
python scripts/select_pilot_a.py
```

| Elemento | Valor |
|---|---|
| Semente | `1160865795` |
| Origem da semente | Oito primeiros dígitos hexadecimais do SHA-256 de `inputs/seed_inventory_v0_1.csv` (`45316803…`), lidos como inteiro. Derivada do dado, não escolhida |
| Entrada | `inputs/seed_inventory_v0_1.csv`, SHA-256 `45316803ea07f677…` |
| Colunas lidas | `source_seed_id`, `layer`, `name`, `resource_type`, `source_url` |
| Colunas nunca lidas | `rgam_potential`, `initial_priority`, `limitations`, `possible_legal_id`, `observation_unit`, `announced_access` |
| Registro completo | `PILOT_A_SELECTION_LOG.json` |

Um teste automatizado embaralha `rgam_potential`, `initial_priority` e `limitations` no inventário e confirma que a amostra não muda.

## 3. Algoritmo

1. Ordenar os 41 registros por identificador.
2. **Forçados:** todo registro que compartilha `source_url` idêntica com outro.
3. Em cada tentativa: partir dos forçados; para cada família ainda sem representante, sortear um de seus registros; sortear os restantes até completar 20.
4. Aceitar a **primeira** tentativa que satisfaz todas as restrições.
5. Se nenhuma satisfizer dentro do limite, parar com erro e relatar quantas vezes cada restrição falhou. Nada é relaxado automaticamente.

Cada sorteio é `lista[int(rng.random() × tamanho)]` sobre a lista ordenada, com `random.Random(semente)`. A regra evita funções de amostragem cuja implementação possa variar entre versões do Python.

## 4. Restrições e como cada exigência foi operacionalizada

Os valores foram fixados antes da execução e não foram ajustados depois.

| Exigência do G1-PREP | Restrição | Operacionalização objetiva | Na amostra |
|---|---|---|---|
| Tamanho | C1 | 20 registros | 20 |
| Cobertura das 11 famílias | C2 | Pelo menos 1 registro por valor de `layer` | 11 de 11 |
| Casos potencialmente duplicados | C3 | Todo grupo com `source_url` idêntica entra completo | EU03 + EU07 |
| Casos potencialmente relacionados | C4 | Pelo menos 3 grupos de mesmo nome de host com 2 ou mais selecionados (excluídas plataformas genéricas de hospedagem: github.com, zenodo.org, huggingface.co) | 4 grupos |
| Classificação ambígua | C5 | Pelo menos 3 registros cujo `resource_type` traz dois rótulos ("A/B") | EU01, EU02, EU23 |
| Diversidade de tipos | C6 | Pelo menos 18 valores distintos de `resource_type` | 20 |
| Equilíbrio entre famílias | C7 | No máximo 4 registros por família | máximo 4 |
| Preservação da reserva | C8 | Os 21 não selecionados cobrem pelo menos 9 famílias | 10 |

Falhas nas oito tentativas rejeitadas: C5 sete vezes, C8 quatro, C4 duas, C6 duas. **Não houve conflito entre restrições**: uma amostra viável foi encontrada na 9ª tentativa.

## 5. Limites das operacionalizações

As exigências "relacionados" e "ambíguos" são, por natureza, julgamentos. Para não usar colunas de julgamento, foram substituídas por substitutos computáveis. Isso tem custo:

1. **Relação medida por nome de host é um substituto fraco.** Captura registros no mesmo sítio institucional, que podem ou não ter relação de distribuição ou hospedagem. Não captura pares em hosts diferentes da mesma instituição.
2. **Dois pares apontados no G0.1 ficaram incompletos:** EU08 entrou sem EU09; EU33 entrou sem EU34. Os hosts diferem (`data.europarl` × `oeil.europarl`; `data.ted` × `docs.ted`), e o algoritmo não tinha como reconhecê-los sem recorrer a julgamento.
3. **Ambiguidade medida por rótulo composto é estreita.** Só cinco registros têm `resource_type` com dois rótulos. Outros casos ambíguos existem, mas identificá-los exigiria a coluna `limitations`, que foi excluída de propósito.
4. **Nenhum registro descontinuado na amostra.** O único que o inventário marca assim (EU11) ficou na reserva; a marcação está no nome e em `limitations`, que o algoritmo não interpreta.
5. **Corpus derivado sem sua origem aparente.** EU39 entrou; EU35 e EU36 ficaram na reserva.
6. **"Intermediação RIT" no teto de 4.** A nova finalidade trata registros setoriais como enriquecimento; mesmo assim, é a família mais representada na amostra (4, contra 3 de "Corpus normativo" e 3 de "Corpus acadêmico").
7. **A família é um rótulo do inventário.** Garantir cobertura de `layer` usa uma classificação preliminar como estrato. Ela não chega aos avaliadores, mas molda a amostra.

## 6. Comparação com a lista intencional do G0.1

| | Algoritmo (esta proposta) | Lista intencional (G0.1) |
|---|---|---|
| Em comum | 12 registros: EU01, EU02, EU03, EU07, EU08, EU15, EU17, EU19, EU24, EU28, EU33, EU39 | |
| Só nesta | EU13, EU23, EU25, EU27, EU30, EU32, EU37, EU41 | |
| Só na outra | | EU06, EU09, EU11, EU22, EU29, EU34, EU35, EU40 |
| Como foi feita | Sorteio com restrições, sem colunas de julgamento | Escolha de um agente que leu as colunas de julgamento |
| Pares interface/acervo completos | 1 (URL idêntica) | 4 |

## 7. Alternativas para a decisão da equipe

Nenhuma foi executada além da primeira.

| Opção | O que é | A favor | Contra |
|---|---|---|---|
| A | Aprovar a amostra do algoritmo como está | Reprodutível; livre de julgamento prévio | Pares incompletos (itens 2, 4 e 5 da seção 5) |
| B | A equipe declara por escrito grupos obrigatórios (por exemplo EU08+EU09, EU33+EU34) e o algoritmo é reexecutado **com a mesma semente** | Mantém a reprodutibilidade e torna explícito o julgamento humano acrescentado | Exige uma decisão documentada antes da execução; o código precisa de um parâmetro novo |
| C | Adotar a lista intencional do G0.1 | Pares completos | Seleção por agente com acesso a colunas de julgamento |
| D | Outra semente, registrada antes | — | Só se justifica com razão declarada de antemão; trocar de semente depois de ver o resultado invalida o procedimento |

Em qualquer opção, a lista aprovada, a data e o responsável são registrados antes da entrega dos pacotes. Se a amostra mudar, os formulários são regenerados com `python scripts/pilot_a_forms.py build`.
