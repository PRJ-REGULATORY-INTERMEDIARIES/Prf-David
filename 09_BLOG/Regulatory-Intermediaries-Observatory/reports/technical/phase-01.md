# Relatório de execução — Fase 01

Data: 09/10/2026. Projeto proposto; documentação científica **DRAFT — NOT VALIDATED**.

## A. Resumo executivo

Foi implementado um repositório independente em `09_BLOG/Regulatory-Intermediaries-Observatory`, contendo infraestrutura Python/SQLite, documentação metodológica preliminar das trilhas A e B, validação, exportações controladas e website/blog Quarto. O documento DOCX indicado e o bootstrap anexado foram lidos como especificações. O hash do DOCX está em `references/specification-sha256.txt`.

O banco de trabalho `data/working/rio.sqlite` está vazio. O banco separado `data/working/synthetic.sqlite` contém exclusivamente a fixture identificada como sintética; sua exportação está em `data/processed/synthetic-demo`. `data/public` contém somente `.gitkeep`.

Resultados efetivos: 26 testes aprovados; renderização Quarto de seis páginas concluída; seis respostas HTTP 200 no preview verificado; nenhum link/recurso local ausente na checagem gerada. A inspeção visual em navegador e uma auditoria formal de acessibilidade não foram realizadas. Houve uma falha transitória no primeiro preview e avisos de limpeza de diretórios na unidade sincronizada, registrados abaixo.

Não houve coleta de dados reais, busca bibliográfica, publicação, configuração de hosting, remote, commit ou push. Não foram importados ou modificados RGAM/V8 ou outros projetos. O status inicial do repositório pai já continha arquivos não rastreados em 08_EU_REGULATORY_DATA_SCOPING; eles foram preservados. Na inspeção final apareceu também `G0_1_STRATEGIC_ALIGNMENT.md` naquela pasta, não criado por esta execução. Nenhuma alteração em arquivo rastreado do repositório pai foi indicada por `git diff --stat`.

## B. Estrutura real do repositório

Árvore dos arquivos-fonte e relatórios efetivamente existentes, obtida de `git ls-files --others --exclude-standard` no repositório novo (ainda sem commit). Os arquivos gerados/ignorados são discriminados em seguida.

```text
Regulatory-Intermediaries-Observatory/
├── codebook/
│   ├── codebook-v0.1.md
│   └── fields.md
├── data/
│   ├── processed/
│   │   └── .gitkeep
│   ├── public/
│   │   └── .gitkeep
│   ├── raw/
│   │   └── .gitkeep
│   ├── synthetic/
│   │   ├── README.md
│   │   └── minimal.json
│   └── working/
│       └── .gitkeep
├── database/
│   ├── migrations/
│   │   └── README.md
│   └── schema.sql
├── docs/
│   ├── architecture/
│   │   └── data-model.md
│   ├── concept/
│   │   └── concept-note.md
│   ├── decisions/
│   │   └── 0001-local-foundation.md
│   └── governance/
│       └── release.md
├── protocol/
│   ├── case_selection/
│   │   └── pilot.md
│   ├── coding/
│   │   └── workflow.md
│   ├── scoping_review/
│   │   ├── metadata-template.csv
│   │   ├── protocol-v0.1.md
│   │   ├── screening.csv
│   │   └── search-log.csv
│   └── validation/
│       └── procedure.md
├── references/
│   ├── README.md
│   └── specification-sha256.txt
├── reports/
│   ├── methodological/
│   │   └── pending-decisions.md
│   ├── technical/
│   │   ├── environment.json
│   │   └── phase-01.md
│   └── validation/
│       ├── local-checks.json
│       ├── test-results.md
│       └── website-checks.json
├── scripts/
│   ├── database/
│   │   └── initialize.py
│   ├── import_export/
│   │   └── export.py
│   ├── utilities/
│   │   └── load_synthetic.py
│   ├── validation/
│   │   └── validate.py
│   └── README.md
├── src/
│   └── rio/
│       ├── __init__.py
│       ├── __main__.py
│       └── storage.py
├── tests/
│   └── test_pipeline.py
├── website/
│   ├── posts/
│   │   ├── infrastructure-preview/
│   │   │   └── index.qmd
│   │   └── README.md
│   ├── .gitignore
│   ├── _quarto.yml
│   ├── blog.qmd
│   ├── dataset.qmd
│   ├── index.qmd
│   ├── research.qmd
│   ├── styles.css
│   └── team.qmd
├── .gitignore
├── CHANGELOG.md
├── PROJECT_STATUS.md
├── README.md
└── pyproject.toml
```

Artefatos locais adicionais, deliberadamente ignorados pelo Git:

- `.git/`: repositório independente, sem remote e sem commits.
- `.venv/`: ambiente Python local com a instalação editável e pytest.
- `data/working/rio.sqlite`: banco de trabalho inicial vazio.
- `data/working/synthetic.sqlite`: banco técnico sintético.
- `data/processed/synthetic-demo/`: snapshot.json, manifest.json e um CSV para cada uma das 14 tabelas.
- `website/_site/`: seis documentos HTML e recursos estáticos da renderização Quarto.
- `website/.quarto/`, `.pytest_cache/`, caches Python e metadados da instalação editável: artefatos transitórios.

## C. Principais arquivos e decisões

| Artefato | Função |
|---|---|
| README.md | Procedimento reproduzível Windows/PowerShell, comandos reais, fluxo de dados e alternativa de preview |
| PROJECT_STATUS.md / CHANGELOG.md | Estado técnico e versão inicial |
| database/schema.sql | Esquema 0.1.0, IDs estáveis, integridade, papéis contextuais, vínculos e histórico |
| src/rio/storage.py / __main__.py | Inicialização sem sobrescrita, fixture, validação, fingerprint e exportação local |
| data/synthetic/minimal.json | Fixture inteiramente sintética, sem alegação factual |
| tests/test_pipeline.py | 26 casos parametrizados de integridade, reprodutibilidade e proteção de exportação |
| protocol/scoping_review/ | Protocolo e templates vazios de busca, triagem e extração |
| protocol/case_selection/, coding/, validation/ | Critérios preliminares para seleção, codificação, revisão e adjudicação |
| codebook/codebook-v0.1.md / fields.md | Definições preliminares e dicionário extraído do esquema executável |
| docs/architecture/data-model.md | Separação analítica das trilhas e limites técnicos |
| docs/governance/release.md | Condições de validação/elegibilidade e autorização vinculada ao snapshot |
| docs/decisions/0001-local-foundation.md | Justificativas auditáveis de localização, isolamento e arquitetura |
| website/ | Cinco páginas principais e uma entrada técnica que exercita a listagem do blog |
| reports/validation/ | Registro dos testes e checagens de integração/website |
| reports/technical/environment.json | Versões efetivamente usadas |

A tabela `records` centraliza identidade, status, versões e elegibilidade. As entidades tipadas mantêm a normalização. Relações referenciam papéis do mesmo episódio; atores podem mudar de papel e um episódio pode ter vários intermediários. Evidências suportam múltiplas afirmações e vice-versa. Decisões de codificação são acrescentadas, não sobrescritas.

A exportação pública opera de forma conservadora sobre um banco curado completo: todos os registros devem estar validados, explicitamente elegíveis e não sintéticos. Exige evidência/revisão e autorização humana para o hash exato do conteúdo, inclusive decisões internas. A exportação omite decisões pessoais de codificação, mas os demais campos exigem revisão de privacidade/direitos. Esse mecanismo local é uma barreira de procedimento, não autenticação de responsáveis ou garantia de verdade científica. Não há autorização preenchida no projeto.

`.env.example` foi omitido porque não há configuração por variáveis de ambiente ou segredos. Nenhuma licença foi atribuída. Não há dependências Python de runtime além da biblioteca padrão; pytest é a dependência direta de desenvolvimento.

## D. Testes e verificações executados

| Comando / checagem | Resultado observado |
|---|---|
| python -m venv .venv | Ambiente criado |
| .\.venv\Scripts\python.exe -m pip install -e '.[dev]' | Instalação concluída; pytest 9.0.3 |
| .\.venv\Scripts\python.exe -m pytest -q | **26 passed in 0.89s**, saída 0 |
| python -m rio init (no ambiente virtual) | Banco vazio criado sem sobrescrita |
| python -m rio init --db data/working/synthetic.sqlite | Banco de teste criado |
| python -m rio load-synthetic --db data/working/synthetic.sqlite | Fixture carregada |
| python -m rio validate, nos dois bancos | valid=true, errors=[] |
| python scripts/validation/validate.py --db data/working/synthetic.sqlite | Wrapper operacional; valid=true |
| python -m rio export --db data/working/synthetic.sqlite --out data/processed/synthetic-demo | Snapshot interno e CSVs gerados, saída 0 |
| quarto render website | Renderização final de 6 documentos; saída 0, sem avisos |
| quarto preview website --host 127.0.0.1 --port 4321 --no-browser --no-watch-inputs | Preview serviu as 6 páginas com HTTP 200; encerrado após a verificação |
| Links locais, recursos e entrada do blog | Sem destinos ausentes na inspeção dos HTMLs |
| git init / git remote -v | Repositório local criado; nenhum remote |
| git check-ignore | Ambiente, bancos, snapshot interno e build excluídos |

Os testes cobrem inicialização, tabelas, unicidade, chaves estrangeiras, valores permitidos, integridade referencial, múltiplos intermediários, contexto de papéis, múltiplas evidências, decisões preservadas, fixture transacional, exportação determinística, separação de diretórios, bloqueio de candidatos/sintéticos e invalidação de autorização após mudança. O teste positivo de exportação simula os indicadores de liberação somente em diretório temporário do pytest, mantendo os textos rotulados como sintéticos; nada foi destinado ao data/public real.

Intercorrências: a leitura inicial do DOCX esbarrou na codificação de stdout do Windows e foi repetida com UTF-8. A primeira renderização ocorreu antes de team.qmd estar concluído e apontou o link; a renderização final corrigida não teve avisos. O primeiro teste HTTP do preview retornou 500; a repetição com --no-watch-inputs passou nas seis páginas. O Quarto ainda registrou um aviso de remoção de diretório na unidade sincronizada. A causa subjacente não foi estabelecida. O README contém alternativa por servidor estático após renderização. Não há dependência ausente ou teste pytest pendente.

Não foi realizada inspeção visual em navegador. A responsividade e o foco visível estão definidos em CSS, mas não foram submetidos a uma auditoria visual/acessível independente.

## E. Decisões metodológicas pendentes

Aprovar escopo geográfico/temporal/linguístico, definição operacional de dataset, fontes elegíveis e estratégia de busca. Fixar as regras somente após revisão, sem converter o protocolo preliminar em protocolo registrado.

Revisar fronteiras de episódios, identificação de atores, sobreposição R/I/T, funções, limiar de inferência, suficiência das evidências, temporalidade, confiança e ausência de dados. Definir seleção e revisão independente do piloto, registro de divergências e adjudicação. O piloto sugerido de doze episódios em três domínios não foi selecionado nem aprovado e não implica representatividade.

Confirmar governança, autoria, afiliações, responsabilidades, direitos e linha editorial. Nenhum desses itens foi decidido pela implementação.

## F. Decisões técnicas pendentes

Ferramentas necessárias estão instaladas. Confirmar extensões de VS Code e local definitivo de desenvolvimento; considerar um checkout fora da sincronização para reduzir interferência de arquivos. Git ignore não restringe compartilhamento pelo Drive. Definir armazenamento/acesso antes de qualquer dado sensível.

A instalação usa o checkout completo em modo editável; uma distribuição wheel independente não foi implementada. Planejar migrações e regras de transição mais estritas após o piloto. A ingestão de dados reais ainda deve ser projetada e autorizada. Escolha de licenças, remote privado, hosting, domínio, DOI e publicação permanecem decisões futuras, sem configuração nesta fase.

## G. Proposta para a Fase 02 — não executada

1. Revisar coletivamente o protocolo de escopo: pergunta, unidade, limites, fontes, strings, filtros, triagem e mudanças versionadas.
2. Refinar o formulário de extração e mapear campos detalhados para o catálogo, registrando dados ausentes e verificações de acesso/licença.
3. Após aprovação do protocolo, identificar fontes candidatas por categoria, sem presumir utilidade RIT ou acesso permitido; manter logs reproduzíveis e motivos de exclusão.
4. Definir uma seleção contrastiva de casos para testar fronteiras, papéis, evidências e adjudicação; avaliar a proposta de doze episódios e sua viabilidade documental.
5. Planejar o primeiro texto do blog sobre o desenho metodológico e a pergunta “Where Are Regulatory Intermediaries in Existing Governance Datasets?”, sem antecipar lacunas ou achados. Submeter fatos, autoria e conteúdo à revisão antes de qualquer divulgação.

Nenhuma atividade empírica ou publicação da Fase 02 foi iniciada.
