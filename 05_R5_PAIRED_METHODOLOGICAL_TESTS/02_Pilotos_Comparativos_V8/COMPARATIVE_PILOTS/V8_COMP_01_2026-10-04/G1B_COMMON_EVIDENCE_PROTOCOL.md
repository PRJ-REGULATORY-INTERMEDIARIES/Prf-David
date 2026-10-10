# G1B — protocolo de evidência comum

**Data:** 2026-10-04  
**Estado:** `G1B_CONDITIONAL_PASS / TRACKS_NOT_STARTED`

## Finalidade

Congelar a referência à evidência jurídica primária histórica comum aos futuros Tracks A e B. A congelação é por caminho, versão, identificador e SHA-256 dos arquivos locais já preservados; não copia, altera ou substitui o texto jurídico, PILOT_03 ou V8.

Os dois casos são atos originais do *Official Journal*, não textos consolidados vigentes. Este fato delimita qualquer resultado futuro à arquitetura jurídica histórica daquele ato/texto e não à sua vigência ou implementação atual.

## Fontes controladoras e unidade

| Caso | Fonte controladora | Unidade primária congelada | Blocos incluídos |
|---|---|---|---|
| P03 / 31991L0263 | HTML em `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/01_BASELINES/official_texts/31991L0263.html`, identificado pelo CELLAR | provisão/segmento juridicamente endereçável | Art. 10(1), 10(2), Anexo III 3.3, Anexo III 4.3 |
| P04 / 32004R0874 | HTML em `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/01_BASELINES/official_texts/32004R0874.html`, identificado pelo CELLAR | provisão/segmento juridicamente endereçável | Art. 12(5), 13, 14, 15(1), 22(5)-(7), 23(1) |

O texto `.txt` paralelo é uma representação de leitura/ancoragem; o HTML é a fonte controladora. `PROVISION_REGISTER.csv` e `LEGAL_EXCERPTS.csv` do PILOT_03 são evidência histórica de seleção, não substitutos do texto oficial. Model A/B e adjudicações são camadas históricas distintas e não são observações primárias.

## Critérios de inclusão

Incluir somente segmentos que: (a) constam do recorte histórico P03/P04; (b) estão localizáveis no HTML oficial congelado; (c) preservam sujeito, ação, objeto, modalidade e condição relevantes; e (d) podem ser citados por identificador de provisão. Incluir Art. 22(7) apenas como contexto necessário para auditar a classificação histórica composta de P04_PR06; não é uma nova observação nem uma nova relação neste gate.

Excluir: inferências de implementação; estados atuais do direito; recitais não selecionados; disposições externas não recuperadas; agregados históricos `RIT`; e qualquer edge que dependa apenas de nomeação, atribuição unilateral ou classificação de modelo. Art. 9 de 31991L0263 é apenas cross-reference contextual nesta fase, não evidência do microcaso.

## Regras de leitura prospectiva

1. Registrar primeiro declaração institucional e âncoras textuais.
2. Tratar uma atribuição sem contraparte identificável como `NORMATIVE_ASSIGNMENT`, não edge.
3. Criar relação qualificada apenas com partes, ação juridicamente relevante, direção, modalidade/condição e âncora de fonte.
4. Decompor provisão composta em declarações; não transformar o agregado histórico em uma relação única.
5. Manter `DEFERRED` quando o texto não identifica o destinatário, a direção ou a parte relevante.
6. O hash de `FROZEN_EVIDENCE_MANIFEST.csv`, depois de validado, será o identificador de input dos dois Tracks. Nenhum Track pode acrescentar ou retirar fonte sem emenda.

## Sequência A/B e parada

Track A aplicará V8 sem a sequência obrigatória das oito operações e será salvo/hasheado antes de Track B. Track B partirá do mesmo manifest e aplicará a especificação adicional. O antigo Model A/B do PILOT_03 não é nenhum desses Tracks.

G1B não autoriza Track A automaticamente: requer aceitação do escopo e da seleção de dois casos, reconfirmação de integridade no momento de execução e criação de um registro de declarações com fonte idêntico para ambos. Não houve extração, codificação V8, Track A ou Track B nesta execução.
