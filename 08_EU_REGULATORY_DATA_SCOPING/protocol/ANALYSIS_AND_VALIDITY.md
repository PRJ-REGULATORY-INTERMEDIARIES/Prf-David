# PLANO DE ANÁLISE, VALIDADE E SENSIBILIDADE

## Descrições científicas mínimas

- Dados: número de buscas, ocorrências, duplicatas, triagens, registros incluídos, datasets canônicos e distribuições. Denominadores distintos nunca se misturam.
- Distribuições descritivas: por domínio, mantenedor, nível jurídico, cobertura temporal, tipo de acesso/licença, formato e nível D0–D3.
- Matriz: `dataset_id` × cada critério de auditoria, com faixa `0/1/2/UNVERIFIED/NA`; apresentar medidas de cobertura por dimensão com N explícito.
- Pareamentos: contagem de datasets com campo CELEX, ELI, URL de norma, referência de artigo, ator codificado e vínculo interinstitucional.
- Relações normativas: qualitativas e ancoradas em fonte; evitar transformar associações de coocorrência em relações causais ou competências jurídicas.

## Verificações de robustez

1. Sintetizar resultados com e sem `archived/discontinued`.
2. Descrever separado `open`, `restricted`, `metadata_only`, `unknown`.
3. Contar interfaces e datasets separadamente; relatório obrigatório de consolidação de portais sobrepostos.
4. Distinguir cobertura no catálogo de cobertura confirmada por busca e teste.
5. Reavaliar resultados excluindo recursos cuja informação de licença é `UNVERIFIED`.
6. Comparar notas técnicas antes de adjudicação; apresentar divergências com conteúdo.
7. Documentar dependência em dados europeus versus nacionais e diferenças linguísticas.

## Métricas de concordância

Acordo observado binário = (decisões idênticas include/exclude) / (pares elegíveis de decisões categóricas). Cohen's kappa pode ser calculado se dois avaliadores forem os mesmos em todas as unidades comparadas e se prevalências permitirem interpretação; relatar N, marginais e categorias `uncertain` em separado. Se houver vários revisores/falhas, não misturar pares nem calcular um único kappa arbitrário.

## Ameaças à validade

Cobertura desconhecida impede afirmações de que a pesquisa encontrou **todos** os datasets existentes. Ausência de atributo em metadado não prova sua ausência na arquitetura jurídica. Registro de entidade intermediária não comprova relação RIT. Acesso técnico não demonstra licenciamento de reutilização.

## Mérito científico pretendido

A contribuição do artigo não é a contagem de links; é uma tipologia auditável das infraestruturas e uma demonstração verificável das diferenças entre capacidade de fornecer texto jurídico, metadados, atores e relações jurídicas para análise comparativa da governança regulatória.
