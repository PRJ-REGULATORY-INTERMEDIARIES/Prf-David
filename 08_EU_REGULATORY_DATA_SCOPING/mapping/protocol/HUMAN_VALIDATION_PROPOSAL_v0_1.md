# PROPOSTA DE VALIDAÇÃO HUMANA PROPORCIONAL — v0.1

**Data:** 2026-10-10 | **Estado:** PROPOSTA. Nada foi executado, atribuído ou simulado. Não bloqueia a descoberta.

## 1. Para que serve

Todas as classificações da base foram propostas por um agente de IA. Os testes de software mostram que as ferramentas funcionam; **não mostram que as classificações estão certas nem que duas pessoas concordariam**. Esta proposta define o mínimo de validação humana necessário para poder apresentar contagens por categoria, nível, conjunto, individuação e relação como algo além de triagem provisória.

Ela não é condição para continuar descobrindo recursos.

## 2. O que se valida (e o que não)

| Objeto | Pergunta ao avaliador | Por que é o ponto frágil |
|---|---|---|
| Categoria e nível (I/II) | Qual categoria descreve este recurso, a partir das capturas? | Fronteiras `REPOSITORY`/`DATASET`/`ADMINISTRATIVE_REGISTER` e `INFRASTRUCTURE`/`CATALOGUE` dependem de leitura de páginas curtas |
| Individuação | É um recurso independente, parte de outro, distribuição ou agrupamento? | A regra de família de catálogo (DEC-0019) é uma convenção do agente; a unidade varia com o mantenedor |
| Conjunto A, B ou AB | A qual conjunto pertence? | A fronteira é definida por conteúdo declarado, em casos de leitura curta |
| Elegibilidade | Entra no escopo? | Há 38 registros `UNCERTAIN` |
| Relação | A relação declarada se sustenta na evidência citada? | As relações candidatas repousam em nome, título ou citação, não em declaração explícita da fonte |

Não se valida: a existência dos recursos (verificada por captura), os valores copiados de fontes (verificáveis nas capturas), nem a utilidade para qualquer aplicação.

## 3. Amostra proposta

`mapping/scripts/validation_sample.py` sorteia, com semente `20261010`, uma amostra reprodutível. Resultado desta construção em `mapping/reports/evidence/VALIDATION_SAMPLE_PROPOSED.csv`:

| Estrato | Critério | Unidades | Tipo |
|---|---|---|---|
| S1 ambíguo | Categoria `INDETERMINATE` ou individuação diferente de `INDIVIDUATED` | 23 recursos | Censo |
| S2 escopo | Elegibilidade `UNCERTAIN` (fora do S1) | 32 recursos | Censo |
| S3 fronteira A/B | Conjunto `AB` (censo) e sorteio de 12 em A e 12 em B entre os individuados | 30 recursos | Censo e sorteio |
| S4 individuados | 4 por célula (nível × rodada de origem) | 16 recursos | Sorteio estratificado |
| S5 relações | Relações candidatas de confiança média (censo) e 8 sustentadas sorteadas | 23 relações | Censo e sorteio |
| **Total** | | **101 recursos e 23 relações** | |

A amostra tem 124 unidades, para uma base de 252 recursos e 48 relações. O desenho prioriza as classes ambíguas, onde o desacordo é mais provável e mais informativo, e é pequeno nas classes que o agente classificou com menos dificuldade. Por isso **não permite estimar uma taxa de acerto global**; permite estimar o desacordo nas classes ambíguas e testar se a regra de individuação é aplicável por outra pessoa.

## 4. Procedimento

1. **Uma pessoa independente** classifica a amostra a partir das mesmas capturas, sem ver a classificação do agente nem o nível derivado. Se houver recursos, uma segunda pessoa classifica o estrato S1 e S3 (censos), o que permite medir concordância entre humanos além da concordância humano–agente.
2. **Instrumentos.** Reutilizam-se os do Piloto A, que já têm pacote por avaliador, campos pré-preenchidos conferidos por hash, trancamento e comparação: `pilot_a_forms.py`, `agreement.py`, `capture_evidence.py`. A taxonomia a entregar é a da emenda A01, que não foi testada com avaliadores.
3. **Instruções ao avaliador:** a classificação é pelo conteúdo e pelo mantenedor, nunca pela utilidade; incerteza é resposta válida; a evidência é a captura, não a página viva.
4. **Divergência.** Tratada por adjudicação nomeada. Resultado final registrado no log de decisões com `decided_by = RESEARCHER`.
5. **Registro.** Linhas confirmadas mudam `classification_basis` para `RESEARCHER_CONFIRMED` e `researcher_confirmed` para `YES`, uma a uma.

## 5. O que reportar

| Medida | Observação |
|---|---|
| Concordância bruta por campo (categoria, nível, conjunto, individuação, elegibilidade) | Com intervalo de confiança; em estratos pequenos, o intervalo é largo e deve ser mostrado |
| Kappa de Cohen por campo | Só onde houver variabilidade suficiente; kappa é instável com poucas categorias dominantes |
| Matriz de confusão agente × humano | Para as categorias com 10 ou mais unidades |
| Divergências qualitativas | Agrupadas por regra: o que a regra deixou ambíguo |
| Taxa de `INDETERMINATE` | Por avaliador |

Não se usará concordância entre execuções do mesmo modelo como substituto de avaliador humano.

## 6. Critérios de decisão (propostos antes de ver resultados)

1. Se a concordância bruta em **individuação** no S1 e no S3 for inferior a 70%, a regra de família de catálogo é revista antes de qualquer contagem ser publicada.
2. Se mais de 25% das linhas do S2 mudarem de elegibilidade, a regra de escopo (D1) precisa ser reescrita, e o conjunto de `UNCERTAIN` reavaliado por inteiro.
3. Se houver desacordo sistemático entre `ADMINISTRATIVE_REGISTER` e `DATASET`, a distinção é colapsada no nível I.
4. As contagens por categoria só são publicadas com a nota de concordância observada. Os limiares são propostas; valem se o pesquisador responsável os adotar antes da execução.

## 7. Proporcionalidade

- Estimativa: cerca de 124 unidades, com leitura de uma a três capturas por unidade.
- Não exige nova captura de evidências.
- Pode ser feita em paralelo à rodada 3 de descoberta; as linhas novas entram na amostra da validação seguinte.
- Se o pesquisador decidir não validar, a base deve ser descrita como triagem provisória em qualquer uso externo.
