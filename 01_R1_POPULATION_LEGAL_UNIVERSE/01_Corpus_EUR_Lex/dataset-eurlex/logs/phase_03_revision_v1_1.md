# Registro de revisão versionada da Etapa 3 — metodologia v1.1.0

**Data:** 2026-09-07  
**Projeto:** `dataset-eurlex`  
**Etapa:** 3 — metodologia  
**Decisão:** revisão concluída e v1.1.0 bloqueada  
**Estado do projeto:** `methodology_locked`  
**Estado do experimento:** `not_started`

## 1. Base e escopo da revisão

Esta revisão foi executada após revisão metodológica externa. A versão `1.1.0` **supersede** a versão `1.0.0` para a preparação das etapas futuras, sem substituir, editar ou re-hashar os artefatos v1.0.0 congelados.

Nenhum resultado empírico, resposta de agente, benchmark, seleção de candidato, codificação ou conteúdo substantivo do ato foi acessado para ajustar codebook, strings ou schemas. Os exemplos utilizados nos testes são abstratos e não pertencem ao corpus.

A Etapa 4 não foi executada. Nenhum benchmark, prompt experimental, run, comparação ou resultado foi produzido nesta revisão.

## 2. Preservação integral da versão 1.0.0

Os quatro artefatos v1.0.0 permanecem na raiz de `methodology/` e foram verificados por SHA-256 antes do fechamento:

| Artefato v1.0.0 | SHA-256 verificado |
|---|---|
| `methodology/codebook.md` | `5527F9ECC7575A831F3D90CA14CAA8DFE4DFC1A65641C1B9C1236338625E2B1C` |
| `methodology/strings.yaml` | `4130425FCFA06E6F9705B76EC477EA1B9EEA29BBD21647981C689D4E09ACD318` |
| `methodology/coding_schema.json` | `C35EA63563239DDB0EE11331D4C84E3BA49BD21B753F8AEBB62526A61949A326` |
| `methodology/methodology_manifest.yaml` | `DEDF8B916ADCE86C7FA61F9BF17914A6A6F23E4C503B4FD2BDD2D60FCA35132C` |

Esses arquivos não foram alterados.

## 3. Artefatos bloqueados da v1.1.0

Os novos artefatos estão isolados em `methodology/v1.1.0/`:

| Artefato v1.1.0 | SHA-256 |
|---|---|
| `methodology/v1.1.0/codebook.md` | `C160E153907A786C04070CB09F6E9BAA11DE709A4432A5F89EBE375A8A7EB472` |
| `methodology/v1.1.0/strings.yaml` | `242C288DB010320619A0CDB58C38CB73C6BE8AA499497CCFAE7BFBFC33F34305` |
| `methodology/v1.1.0/reference_coding_schema.json` | `ABBC4325A5E749CF31836FB24314C27ED22061D6E6539FB435FCE8236D5AD2EC` |
| `methodology/v1.1.0/experimental_output_schema.json` | `AAA0C351836120CADEF86D051EF8D950675577AFBABEFD5AC5D3931F33AE875C` |
| `methodology/v1.1.0/methodology_manifest.yaml` | `4BB92019F932A836707D81D087503B60913B3770CDC3881B05FC0662D036FB00` |

O manifesto v1.1.0 registra os hashes dos quatro produtos metodológicos, a relação de supersessão, os hashes v1.0.0, a dependência do corpus congelado, as fontes metodológicas genéricas e a ausência de tuning empírico.

## 4. Alterações metodológicas incorporadas

- `T` foi restringido a ator, classe de atores ou papel institucional sujeito à relação regulatória; atividade, informação, produto, processo, conduta e estado de conformidade são `object`.
- O schema foi separado em `reference_coding_schema.json` para R1/R2/RA e benchmark, e `experimental_output_schema.json` mínimo comum a G0/G1/G2.
- A saída experimental não contém condições A–E, descrições do codebook, taxonomia de observabilidade, `responsibilization`, `empowerment` ou instruções de scaffolding.
- A redundância entre `candidate_status`/`final_relational_result`, `evidence`/`excerpt`/`verbatim_evidence` e observabilidade global/por evidência foi removida ou consolidada.
- `responsibilization` e `empowerment` são dimensões secundárias opcionais fora do núcleo obrigatório R–I–T.
- A taxonomia de mecanismos foi harmonizada entre codebook, strings e schemas com 14 valores: `reporting`, `verification`, `certification`, `auditing`, `monitoring_supervision`, `ranking_rating`, `standard_setting`, `enforcement_support`, `coordination`, `information_transmission`, `delegated_implementation`, `accreditation`, `other_mechanism` e `none_or_direct`.
- As regex passaram a contemplar variantes morfológicas e plurais genericamente; a duplicação `certification body|certification body` foi eliminada.
- O candidate universe foi formalizado como união de dois canais independentes e complementares: `lexical screening` e `structural reading`; candidato estrutural não exige lexical hit.
- `candidate_origin` foi incorporado com os valores `lexical`, `structural` e `both`.

## 5. Validações executadas

1. Os dois arquivos JSON foram parseados e validados como schemas Draft 2020-12.
2. `strings.yaml` e `methodology_manifest.yaml` foram parseados como YAML válido.
3. Instâncias abstratas de referência e experimental foram validadas pelos respectivos schemas.
4. Foram aprovadas 14 asserções abstratas de invariantes, incluindo: enumeração de mecanismos, `candidate_origin`, separação dos schemas, ausência dos campos proibidos no schema experimental, opcionalidade das dimensões secundárias, independência dos canais e estado do projeto.
5. Os hashes dos quatro artefatos v1.0.0 foram comparados com o registro congelado e permaneceram iguais.
6. Foi verificada a ausência da regex duplicada de certification body.
7. O manifesto foi verificado quanto a `methodology_locked: true`, `project_status: methodology_locked`, `experiment_status: not_started`, `stage_4_executed: false`, `act_content_used_for_tuning: false` e `empirical_results_used: false`.

## 6. Dependências congeladas e parada

O corpus canônico permanece `02_corpus/act.md`, SHA-256 `B24A02EA241CA631B606660BB48BB5A2222B29F849C4E4552FB99F871B2E8FD4`. A representação numerada permanece derivada, SHA-256 `0EB336AEA6C8FF19AF3B6536F3E9029A2E9AF68CA763E962429A8A3DACBB49ED`.

O projeto permanece em `methodology_locked`. A metodologia v1.1.0 está bloqueada para revisão externa posterior. **A execução foi encerrada aqui; a Etapa 4 não deve ser iniciada automaticamente.**
