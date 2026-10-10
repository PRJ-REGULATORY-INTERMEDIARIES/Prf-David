# Protocolo de demonstração empírica — V6

**Data:** 2026-10-03  
**Status:** desenho proposto, `NOT_EXECUTED`. Nenhuma inferência sobre um corpus legal real foi aqui codificada ou validada.

## 1. Finalidade

Testar com um **microcaso legislativo real** a questão mais importante do artigo: como passar de disposições jurídicas a uma afirmação sobre arquitetura de governança sem presumir relações institucionais ausentes do texto. A demonstração serve também como prova de clareza das categorias, não como validação estatística ou generalização setorial.

## 2. Seleção de corpus

**Possível candidato de trabalho:** disposições do GDPR relativas a certificação, organismos de certificação, acreditação e poderes de autoridades de supervisão (investigar, por exemplo, arts. 42–43 e disposições conexas, conferindo a versão consolidada oficial e as remissões). Isto é uma sugestão de corpus, **não a afirmação de que tais dispositivos já foram codificados**.

Critérios de escolha: número pequeno de dispositivos; identificação jurídica não ambígua de atores/ações; ao menos uma relação direta e uma mediada; regras de autoridade e consequência suficientemente concretas; possibilidade de avaliar uma inferência contestável; texto oficial estável e com indicação de artigo/parágrafo/alínea.

## 3. Percurso obrigatório de evidência

```text
Fonte normativa oficial, versão e referência exata
       ↓
Unidade de observação (dispositivo ou cláusula)
       ↓
Enunciado institucional atômico (ator, ação, objeto, condições, modalidade)
       ↓
Relação juridicamente demonstrada (direção, destinatário/foro e função)
       ↓
Atributos da relação (autoridade, discricionariedade, accountability, se previstos)
       ↓
Configuração entre múltiplos enunciados ou relações
       ↓
Alegação arquitetural limitada pelo conjunto de premissas demonstradas
```

A sequência acima é um **esquema de protocolo** inspirado na escada do §6; não substitui a descrição integral das etapas de David nem estabelece novo codebook aprovado.

## 4. Tabela mínima de rastreabilidade

| Campo | O que registrar |
|---|---|
| `source_id` | Legislação oficial, versão/data, URL ou identificador e referência precisa. |
| `legal_span` | Trecho reproduzido de forma limitada ou posição textual reconstituível. |
| `statement_id` | Enunciado atômico e modalidade (dever, poder, proibição, condição etc.). |
| `actor/action/object` | Atores explicitamente constituídos ou reconhecidos; ação e objeto. |
| `recipient/forum` | Destinatário ou foro **somente** se a evidência o fundamenta; senão `NOT_ESTABLISHED`. |
| `relation_id` | Origem, destino, direção, base legal e regra de extração. |
| `function/mechanism/instrument` | Codificar separadamente, anotando eventual ambiguidade. |
| `authority/discretion/accountability` | Indicadores jurídicos e alcance do atributo; nunca dedução pelo nome da instituição. |
| `configuration_claim` | Conjunto de relações e dependências que sustenta uma configuração. |
| `architecture_claim` | Alegação arquitetural proposta e enunciados que a justificam. |
| `alternative/stop_level` | Interpretação alternativa e **mais alto nível inferencial justificado**. |
| `adjudication_status` | `PRELIMINARY`, `HUMAN_REVIEW_REQUIRED` ou valor aprovado em protocolo posterior. |

## 5. Testes críticos obrigatórios

**T1 — Acreditação e autoridade.** Se um dispositivo alude a um "auditor acreditado", quais premissas autorizam atribuir a acreditação a uma autoridade concreta ou uma cadeia de supervisão? Sem premissa jurídica específica, não adicionar ligação pública como fato. Esse teste responde ao problema do exemplo estilizado da V6 (§6.15).

**T2 — Relação versus efeito jurídico.** Uma obrigação de verificar não basta, por si só, para atribuir à entidade verificadora todo e qualquer poder contra o sujeito regulado. Separar obrigação de submissão, destinatário legal da informação e autoridade competente para consequência.

**T3 — Relevância arquitetural.** Distinguir frequência de centralidade, condicionalidade, exclusividade, dependência sequencial e consequência jurídica. Identificar também dispositivos únicos que estruturam uma etapa obrigatória.

**T4 — Accountability.** Reporting a um órgão constitui somente relação informacional ou há foro, avaliação/resposta e consequências jurídicas suficientes para classificar accountability? Anotar decisão e fundamento.

**T5 — Limite formal.** Nenhuma evidência de desempenho efetivo, rotinas administrativas ou conformidade factual poderá ser atribuída a dispositivo legal isoladamente; distinguir formal / implementação / operacional (§6.14).

## 6. Produtos esperados

1. Quadro de cinco a dez enunciados institucionais cuidadosamente selecionados (ajustar conforme o corpus efetivo).
2. Lista de relações demonstradas, com dispositivos-fontes e anotações de dúvida.
3. Um diagrama dirigido simples, onde cada aresta seja rastreável.
4. Uma alegação configuracional e, somente se permitida, uma alegação arquitetural de escopo definido.
5. Dois contraexemplos: uma inferência rejeitada por falta de premissa e uma hipótese rival compatível com a mesma evidência.
6. Nota metodológica curta mostrando o ganho da leitura relacional face à mera contagem de disposições.

## 7. Critério de conclusão

O protocolo somente poderá ser considerado demonstrado quando um segundo leitor conseguir reconstruir **cada relação e cada transição inferencial a partir dos trechos jurídicos indicados**. Resultado inconclusivo é cientificamente válido se devidamente justificado pelo stopping rule. A demonstração não autoriza classificação automática de um ato inteiro ou inferências sobre governança em prática.

**Próxima decisão necessária:** confirmação do corpus e recorte com David/Rotem, seguida de leitura e adjudicação humana dos enunciados selecionados.
