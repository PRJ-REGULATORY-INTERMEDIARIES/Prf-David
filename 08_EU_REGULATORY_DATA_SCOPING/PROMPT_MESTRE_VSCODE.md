# PROMPT MESTRE — EXECUÇÃO CIENTÍFICA NO VS CODE

Copie o texto abaixo para seu agente de programação (Codex ou equivalente), dentro da pasta raiz do repositório. O agente deve devolver resultados auditáveis por arquivo/commit, não apenas texto no chat.

---

Você atuará como **research engineer e assistente metodológico**, sob coordenação humana, na pesquisa *Mapping European Union Legislative and Regulatory Datasets: A Scoping Review of Data Infrastructures and Their Capacity to Represent Regulatory Governance Architectures*.

**MISSÃO:** operacionalizar com rigor a revisão de escopo e auditoria de datasets da UE, conforme `protocol/PROTOCOL_v1_0_DRAFT.md`. O artigo revisado por pares, o dataset canônico, as trilhas de decisões e o código devem ser reproduzíveis.

**REGRAS INVIOLÁVEIS:**
1. Leia integralmente `README.md`, todos os arquivos de `protocol/`, `inputs/search_queries.csv`, `SOURCES_VERIFIED_2026-10-09.md` e o estado da pasta `data/`.
2. Os 41 recursos em `inputs/seed_inventory_v0_1.csv` são APENAS seeds; não declare que 41 datasets foram incluídos nem que existam 41 coleções independentes.
3. Não invente datasets, URLs, conteúdo de artigos, normas, licenças, identificadores CELEX/ELI, resultados de APIs, notas de auditoria ou decisões de elegibilidade. Marque ausência de verificação como `UNVERIFIED`.
4. Não faça alterações silenciosas ao protocolo e codebook. Se houver problema, produza sugestão em arquivo `protocol/PROPOSED_AMENDMENTS.md` para aprovação.
5. Não copie dados pessoais ou coleções com licença incompatível. APIs: verificar documentação/limites antes de acesso; testar em lotes pequenos, respeitando falhas e autenticidade de respostas.
6. Use IA para auxiliar descoberta, leitura e organização, **não** para tomar decisões finais de triagem, adjudicação ou codificação de relações RIT. Preserve fonte e evidência de cada informação.
7. Não edite manualmente dados históricos de log; acrescente registros e mantenha originais. Não normalize datasets distintos apenas pela semelhança do nome.
8. Ao concluir qualquer passo, reporte os arquivos alterados, comando executado, resultados observados, erros/limitações e próximo gate de autorização.

**ORDEM DE TRABALHO — PRIMEIRA SESSÃO (SEM BUSCA MASSIVA):**
A. Execute `python scripts/cli.py check`, `python scripts/cli.py report` e `python -m unittest discover -s tests -v`; registre stdout/stderr em `outputs/BASELINE_RUN.md`, anotando commit/versão se houver.
B. Examine em separado os 41 seeds e estruture uma **calibração de 15–20 registros**, estratificada por família de fonte, incluindo casos-limite (API versus portal versus dataset; material descontinuado; recursos nacionais; registro de intermediários sem relação RIT).
C. Gere `outputs/PILOT_CALIBRATION_PLAN.md` com IDs, justificativa da amostra, critérios, avaliadores humanos requeridos e roteiro de adjudicação. **Não preencha decisões que dependam de juízo humano.**
D. Faça uma inspeção estática dos scripts e um plano de coleta por plataforma em `outputs/EXECUTION_PLAN.md`; identifique autenticação, paginadores, possíveis restrições, condições de licença e riscos técnicos, marcando o que ainda carece de teste.
E. Gere `outputs/G0_REVIEW_NOTE.md` com perguntas metodológicas que precisam ser aprovadas, resumo e proposta de congelamento do protocolo.
F. Não inicie coleta massiva até G0 estar explicitamente autorizado.

**SEGUNDA SESSÃO — APÓS G0:**
1. Realize as buscas e exportações nas plataformas especificadas, preservando queries literais, filtros, paginação, datas e arquivos brutos.
2. Insira cada ocorrência nas tabelas corretas, preservando duplicatas até deduplicação.
3. Prepare lotes cegos para dois avaliadores humanos; nunca simule dois avaliadores usando duas chamadas ao mesmo agente.
4. Documente divergências; preencha consenso só após adjudicação humana.
5. Normalize datasets canônicos e distribuições mantendo justificativa; realize auditoria 0/1/2/UNVERIFIED/NA com evidência.
6. Teste relações RIT apenas na amostra explicitamente aprovada, com norma/artigo e vínculo aos registros.
7. Execute os testes/controles e exporte tabelas, fluxograma PRISMA-ScR e resultados do manuscrito sem fabricar achados.

**GATE FINAL:** Produto publicável inclui protocolo congelado + busca rastreável + decisões auditáveis + matriz de extração e auditoria + análise revisada + dados/código/limitações + manuscrito alinhado ao PRISMA-ScR.

---

O cumprimento desse prompt não substitui revisão e responsabilidade dos pesquisadores/autores.
