# ETAPA 1 — SELEÇÃO, AQUISIÇÃO E REGISTRO DO ÚNICO ATO

Você está trabalhando exclusivamente em `Prf-David/dataset-eurlex/`.

Antes de qualquer ação, leia integralmente:

- `README.md`
- `AGENTS.md`
- `docs/CODEX_WORKFLOW.md`
- `docs/RESEARCH_DESIGN.md`
- `config/project.yaml`
- `config/experiment.yaml`

## Objetivo

Selecionar, adquirir e registrar **um único ato normativo do EUR-Lex** adequado ao exercício experimental.

## Critérios de seleção

Priorize um ato relacionado a clima, governança climática, mitigação, adaptação, emissões, energia e clima ou instrumentos regulatórios climáticos.

O ato deve, preferencialmente:

1. ter CELEX estável;
2. estar disponível integralmente no EUR-Lex;
3. conter conteúdo normativo substantivo;
4. conter diversidade suficiente de obrigações, competências, instrumentos, procedimentos ou mecanismos de implementação;
5. ter extensão administrável;
6. ser adequado ao codebook de atos regulatórios;
7. não ser mera retificação ou documento sem densidade regulatória.

## Autonomia

Selecione apenas UM ato. Não encaminhe várias opções ao pesquisador, salvo impossibilidade objetiva de escolha.

## Material histórico

É permitido consultar `Prf-David/Arquitetura de trabalho/` apenas para compreensão teórica/metodológica.

É proibido utilizar:

- codificações anteriores;
- classificações anteriores;
- tabelas empíricas;
- resultados de LLM;
- ground truth anterior.

## Aquisição

Salvar em `01_source/` a versão oficial mais adequada e seus metadados.

Criar `01_source/provenance.yaml` com:

```yaml
source:
  provider: EUR-Lex
  celex:
  title:
  document_type:
  date:
  language:
  official_url:
  accessed_at:

selection:
  purpose: pilot
  thematic_focus: climate regulation
  rationale:
  inclusion_criteria:
  exclusions_considered:

integrity:
  previous_empirical_results_used: false
```

Criar `01_source/selection_note.md` com justificativa metodológica concisa.

## Atualização de status

Atualizar `config/project.yaml` para:

`status: source_acquired`

Preencher CELEX, título e URL.

Não iniciar a Etapa 2.

## Log

Criar `logs/phase_01_source.md`.

## Validação final

Confirmar:

- apenas um ato selecionado;
- proveniência registrada;
- nenhum resultado anterior usado;
- nenhuma condição G0/G1/G2 executada.

PARE.
