# V8-COMP-01 — Comparative Architectural Inference Pilot

**Registro de desenho:** 2026-10-04  
**Estado geral:** `DESIGN_REGISTERED / BLOCKED_SOURCE_PENDING`  
**Contato do projeto:** Igor Caires Machado (`cairesmachado@gmail.com`, conforme relato pré-registrado; não verificado nesta execução)

## Objetivo

Testar, dentro de cada caso e sobre o mesmo snapshot de evidência jurídica, se uma especificação explícita de oito operações acrescenta valor inferencial demonstrável ao enquadramento V8 de David Levi-Faur. O teste não substitui V8, não cria uma ontologia alternativa, não valida retrospectivamente o GDPR e não mede implementação.

O primeiro micro-piloto é MDR (Regulamento (UE) 2017/745). DSA e Lei brasileira 13.848/2019 estão apenas registrados, ainda sem início. A comparação relevante é **A versus B no mesmo caso**; uma leitura transversal, se houver, examinará transferibilidade e limites, nunca equivalência bruta entre leis.

## Estado de execução desta sessão

- G0 — registro, integridade e fontes de base: concluído.
- G1 — texto jurídico oficial integral, versionado e congelável: pendente. O EUR-Lex confirmou metadados do MDR e aponta versão consolidada de 19/07/2026, mas a sessão não obteve o texto dos arts. 35–45 e 52 em formato que pudesse ser conferido e preservado.
- G2–G4: bloqueados por dependência de G1. Não há evidência compartilhada, Track A, Track B ou conclusão A/B nesta pasta.

## Mapa de artefatos

| Artefato | Papel | Estado |
|---|---|---|
| `RESEARCH_PROTOCOL_v0_1.md` | desenho, hipóteses, operações, rubrica e gates | registrado |
| `RESPONSE_AND_DECISION_REGISTER.md` / `RESPONSE_LOG.csv` | decisões e respostas, append-only | aberto |
| `CASE_SELECTION_AND_AMENDMENTS.md` | seleção provisória e emendas | registrado |
| `SOURCE_MANIFEST.csv` | procedência e estado das fontes | atualizado nesta execução |
| `EXECUTION_LOG.md` | ações efetivamente feitas | atualizado nesta execução |
| `01_MDR/` | controle de fonte, fronteira e futuros artefatos A/B | G1 pendente |
| `02_DSA/`, `03_LEI_13848/` | marcadores de não início | `NOT_STARTED` |
| `TEAM_FEEDBACK/`, `QA/`, `RUN_LOGS/` | feedback, validação e logs | aberto |

## Fontes e retomada

O baseline conceitual é o DOCX local de V8 de 03/10/2026, listado com checksum no manifesto. As regras operacionais foram consultadas somente como material de apoio V8 em `RGAM/V8_ACTIVE/02_CODING_ONTOLOGY/`; elas não autorizam editar V8 ou a ontologia congelada.

Para retomar: (1) obter e preservar um texto oficial em inglês do MDR que identifique a versão consolidada e os arts. 35–45 e 52; (2) atualizar o manifesto com URL, data e SHA-256; (3) cumprir G1 antes de selecionar 8–12 statements; (4) congelar a evidência antes de escrever Track A e somente depois Track B. Toda resposta de equipe entra como nova linha/entrada, sem alterar o histórico.

## Proteção

Esta pasta é nova e não modifica os artefatos pré-existentes. O pacote de pré-registro em `V8_COMP_01_2026-10-04/`, V8, PILOT_03, material de Rotem, GDPR e adjudicações permanecem somente como referências protegidas; seus hashes encontrados constam de `EXECUTION_LOG.md` e `SOURCE_MANIFEST.csv`.
