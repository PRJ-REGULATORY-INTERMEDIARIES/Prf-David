# PROTOCOLO CIENTÍFICO v1.0 — RASCUNHO PRÉ-EXECUÇÃO

**Title:** Mapping European Union Legislative and Regulatory Datasets: A Scoping Review of Data Infrastructures and Their Capacity to Represent Regulatory Governance Architectures

**Versão:** 1.0-DRAFT | **Data:** 2026-10-09 | **Condição:** não registrado; sem autorização para reivindicar busca sistemática concluída.

## 1. Justificativa e contribuição

O universo de dados da UE sobre produção, conteúdo e implementação do direito é disperso entre portais jurídicos, registros administrativos, dados de fiscalização, APIs, ontologias e corpora acadêmicos. A investigação da governança regulatória requer identificar não apenas quais textos existem, mas se são possíveis inferências rastreáveis sobre competências, funções, obrigações e relações entre reguladores (R), intermediários (I) e destinatários (T). Nosso desenho mapeia recursos de informação e examina sua aptidão técnico-jurídica, evitando confundir metadados e acesso tecnológico com observação substantiva das relações regulatórias.

## 2. Perguntas de pesquisa

RQ1. Quais datasets, registros estruturados, APIs, corpora e infraestruturas de dados sobre legislação e governança regulatória da UE são identificáveis publicamente?

RQ2. Qual a distribuição por mantenedor, domínio, nível territorial, unidade de observação, cobertura temporal, formato, licença e meio de acesso?

RQ3. Que dimensões da arquitetura regulatória (atores, funções/competências, relações dirigidas, fundamento normativo, temporalidade) podem ser observadas **diretamente**, **indiretamente por integração** ou **não observadas**?

RQ4. Quais lacunas de acesso, rastreabilidade, cobertura, preservação e interoperabilidade impedem reuso comparativo?

RQ5. Em quantos e quais tipos de recursos há elementos para ligação auditável a atos jurídicos mediante CELEX, ELI ou identificadores oficiais equivalentes?

## 3. Natureza do estudo

Método principal: revisão de escopo de recursos e descrições de datasets, com evidências oriundas de fontes governamentais, repositórios, artigos de dados e documentação técnica. Conduta adaptada às orientações JBI; relato pelo PRISMA-ScR. Incorpora auditoria técnica **original**, com protocolo detalhado e escala ordinal desagregada; princípios FAIR inspiram critérios sem substituir a nossa avaliação de capacidade inferencial.

Componente secundário: prova de conceito RIT/RGAM, limitada a 3–5 casos contrastantes, pré-definidos antes de análise. Deve ser reportada como **exploratória**, nunca como validação independente do V8.

## 4. PCC adaptado à pesquisa

- **Population / universo:** recursos de informação estruturada (datasets, coleções versionadas, registros estruturados e serviços de acesso) relacionados ao direito e à governança da UE.
- **Concept:** representações reutilizáveis de atos, processos, instituições, competências, obrigações, relações e atividades regulatórias.
- **Context:** ordem jurídica e práticas de governança da União Europeia, incluindo conexões documentadas com execução nacional.

## 5. Unidade de inclusão e estrutura hierárquica

Quatro níveis de identidade deverão ser preservados:

1. **Search hit / discovery record:** ocorrência identificada por uma consulta em uma fonte específica; pode repetir outra ocorrência.
2. **Dataset canônico:** coleção lógica com escopo, mantenedor e unidade de observação, identificável independentemente de diferentes interfaces.
3. **Resource / distribution:** portal, API, arquivo, endpoint, dump ou interface que distribui um dataset canônico.
4. **Legal act / organizational entity:** objeto substantivo dentro de um dataset, **não** é automaticamente uma nova base.

Exemplo: EUR-Lex, CELLAR e seus endpoints podem constituir interfaces e coleções relacionadas; não serão somados indiscriminadamente como datasets independentes. A decisão de agrupamento exige metadados e justificativa.

## 6. Elegibilidade a priori

### Inclusão

I1. Evidência de relação material com legislação/regulação da UE (direito primário ou derivado, sua elaboração, transposição, implementação, aplicação, fiscalização ou órgãos/intermediários juridicamente vinculados).

I2. Existência de coleção ou serviço **estruturado**, com registros passíveis de consulta ou exportação, ou documentação suficiente para auditá-lo.

I3. Metadados mínimos verificáveis por página institucional, artigo, ficha técnica, repositório ou documentação de API.

I4. Disponível em qualquer idioma, desde que possa ser documentado e eventualmente traduzido com revisão.

I5. Estado: ativo, arquivado ou descontinuado **com documentação suficiente**; conservar status para análise histórica.

### Exclusão

E1. Página puramente opinativa, notícia ou documento isolado sem estrutura de coleção de dados.

E2. Duplicata de interface ou distribuição já ligada à mesma coleção, como **dataset separado**; preservar como `resource`.

E3. Base nacional sem relação demonstrável com aplicação/transposição de legislação europeia.

E4. Descrição sem prova minimamente identificável de existência da coleção (página morta sem metadados recuperáveis ou referência independente).

E5. Material não relacionável ao objeto de legislação e governança regulatória.

**Acesso restrito não implica exclusão automática:** registrar restrição; elegibilidade depende da documentação, não da possibilidade de download irrestrito.

## 7. Horizonte e idiomas

Busca desde a origem das coleções até o **fechamento documental explicitamente datado no registro de buscas** (definir antes do início). Sem restrição temporal de criação/publicação. Estratégia inicial em inglês, com buscas complementares em francês e alemão e expansão dirigida a outros idiomas quando necessário. Limitação linguística operacional será relatada; não declarar buscas em 24 idiomas se não realizadas.

## 8. Fontes e estratégia de busca

Canais principais: data.europa.eu (portal e API), EUR-Lex/CELLAR, European Parliament Open Data, OEIL, registros da Comissão e agências da UE, N-Lex, OpenAIRE, Zenodo, Crossref/OpenAlex e bases bibliográficas disponíveis institucionalmente. Acrescentar busca reversa/prospectiva de citações, amostragem de portais nacionais e consulta direcionada a especialistas.

Executar estratégia JBI em três movimentos: identificação e calibração dos termos em fontes-semente; pesquisa extensiva reproduzível por plataformas; rastreamento de citações e busca manual de literatura cinzenta. **A lista inicial de 41 itens é um seed set, não conta como amostra final nem demonstra cobertura exaustiva.**

Para cada consulta: plataforma, data/hora, expressão literal, URL/endpoint, paginação, filtros, quantidade recuperada, método de exportação, pessoa responsável, hash do arquivo bruto (se aplicável) e restrições.

As strings modelo, seus limites e uma tabela operacional ficam em `SEARCH_STRATEGY.md` e `inputs/search_queries.csv`. Se uma API não admitir operadores booleanos, registrar a tradução da string sem simular equivalência perfeita.

## 9. Processo de seleção

S0. Congelar protocolo antes de buscas sistemáticas; versionar todas as alterações.

S1. Capturar registros de descoberta com proveniência e guardar originais imutáveis.

S2. Deduplicar **ocorrências de busca** por URL canônica/identificador e inspeção manual. Registro de duplicatas é mantido; identificação de datasets sobrepostos ocorre depois, em nível de coleção lógica.

S3. Triagem de título/descrição por **dois avaliadores independentes**; decisão include/exclude/uncertain com justificativa.

S4. Triagem da fonte completa (documentação, artigo ou landing page) pelos mesmos princípios. Em divergência, discussão documentada e eventual terceiro adjudicador.

S5. Construção de entidades canônicas dos datasets e recursos. Reportar separadamente número de search hits, registros únicos elegíveis, datasets canônicos e distribuições.

Calibração: 15–20 registros diversificados **antes** da triagem formal, com revisão das definições. Alteração substantiva do protocolo demanda adendo datado e nova calibração.

## 10. Extração / charting

Campos obrigatórios por dataset: ID, nome, mantenedor, domínio, cobertura espacial/temporal, unidade de observação, condição de acesso, licença/status conhecido, data de verificação, evidência, tipo de recurso, disponibilidade de documentação, chaves oficiais de referência, ligação a entidades e relações jurídicas, restrições e decisão de elegibilidade.

Por distribuição: URL, tipo, formato, modo de acesso, existência confirmada ou anunciada e relação com o dataset canônico.

**Normas de codificação:** `UNVERIFIED` ≠ `NO`; `NOT_APPLICABLE` ≠ `MISSING`; ausência de licença informada ≠ licença aberta.

## 11. Auditoria e avaliação da aptidão para arquitetura regulatória

Cada dataset recebe observações por critério 0/1/2 ou `UNVERIFIED`/`NA`, com evidência verificável e data: identificadores jurídicos; estruturação de atores; competência/função; relações dirigidas; temporalidade; documentação e reprodutibilidade; acesso automático; condições de reutilização.

As categorias e âncoras das notas estão detalhadas em `CODEBOOK_AND_AUDIT.md`. Não gerar ranking único sem pré-registro de pesos, análise de sensibilidade e tratamento de dados ausentes. Relatar matrizes por critério, tipologias e lacunas.

## 12. Confiabilidade e adjudicação

Triagem dupla integral e independente. Estimar acordo bruto e kappa para decisões binárias include/exclude **somente quando comparáveis**, por etapa, antes de adjudicação; incertezas devem ser reportadas separadamente. Inspecionar distribuição das categorias. Auditoria técnica: dupla codificação de ≥20% da amostra final, estratificada por família de recurso, com mínimo de 10 unidades se houver ao menos 10 elegíveis; se <10, codificar todas. Registrar frequência de divergências, seus motivos e decisões de consenso. Indicadores não substituem validade.

## 13. Análise de resultados

Descritiva: frequências e porcentagens com denominadores informados; tabelas por domínio, família de fonte, nível normativo, tipo de acesso, licença e chaves CELEX/ELI. Mapas de cobertura (dataset × capacidade de inferência RIT) usando critérios explícitos. Análise qualitativa de documentação e lacunas. Não usar testes inferenciais de significância quando universo incompleto e seleção não probabilística. Descrever a sensibilidade da síntese a fontes de acesso restrito e recursos com documentação limitada.

## 14. Subestudo exploratório RIT/RGAM

Selecionar 3–5 pares *norma + registro* com diversidade de área e função do intermediário: DSA/trusted flaggers; NANDO/notified bodies; conformidade ambiental/relatórios; GDPR/cooperação; DGA/data intermediaries (elegibilidade de cada um dependerá da revisão). Congelar amostragem antes de extrair relações. Registrar CELEX/ELI, artigo, evidência, R, I, T, função, natureza da inferência e validação humana. A existência de um intermediário de dados não implica automaticamente intermediação regulatória RIT.

## 15. Ética, direitos e uso de IA

Trabalhar prioritariamente com metadados públicos e documentos institucionais, sem redistribuir dados pessoais ou conteúdo sujeito a restrições/licenças incompatíveis. Respeitar limites e condições de APIs. Se LLM for usado para triagem assistida ou extração, preservar prompts, versão do modelo, insumos permitidos, saídas brutas, decisões humanas e taxa de erro em amostra verificada. **LLM não adjudica automaticamente inclusão ou interpretação jurídica.**

## 16. Limitações esperadas

Viés de indexação e idioma; heterogeneidade entre portais, serviços e datasets; dependência de documentação não padronizada; mudanças de URL e versões; falta de prova negativa de relação regulatória; limitações de captura de fontes nacionais; inadequação de métricas FAIR genéricas para inferência jurídico-institucional.

## 17. Produtos e requisitos de transparência

P1. Artigo de scoping review com análise de lacunas; P2. Inventário canônico de datasets com dicionário de dados, proveniência e decisões de triagem; P3. Scripts e documentação para reprodução; P4. Apêndice exploratório RIT com trilhas de evidência se houver dados suficientes. Pré-registro, codebook versionado, fluxograma PRISMA-ScR e depósito com DOI são condições almejadas para publicação.

## 18. Referências fundacionais (verificadas)

- Tricco, A.C. et al. (2018). PRISMA-ScR. *Annals of Internal Medicine* 169:467–473. DOI: https://doi.org/10.7326/M18-0850
- JBI. *Manual for Evidence Synthesis* (capítulo de scoping reviews), https://jbi.global/scoping-review-network/resources
- Wilkinson, M.D. et al. (2016). FAIR Guiding Principles. *Scientific Data* 3:160018. https://doi.org/10.1038/sdata.2016.18
- Publications Office / EUR-Lex, ELI implementation: https://eur-lex.europa.eu/content/eli-register/implementing_eli.html
- EU Open Data Search API description: https://data.europa.eu/api/hub/search/

**Não editar este protocolo silenciosamente após registro. Toda alteração requer adendo e motivo.**
