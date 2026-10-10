# G1-READY — PROTOCOLO DE CAPTURA DE EVIDÊNCIAS

**Data:** 2026-10-10 | **Estado:** PROPOSED. Procedimento desenhado, ferramenta implementada e testada; execução sobre os itens do piloto **não iniciada** e dependente de autorização.

## 1. Finalidade

Os dois avaliadores devem julgar **o mesmo conteúdo**. Páginas mudam; sem cópia comum, uma divergência pode ser de conteúdo e passar por divergência de julgamento. O protocolo produz, para cada item, uma cópia fiel e datada do que foi consultado, com hash, e a liga ao item de avaliação.

## 2. Princípios

1. **Fidelidade.** O conteúdo é guardado byte a byte, como o servidor o entregou.
2. **Nada de extração seletiva.** A ferramenta não resume, não destaca trechos, não extrai campos. Qualquer recorte poderia conduzir a classificação.
3. **Fonte oficial primeiro.** Captura-se a página do mantenedor. Fontes secundárias só quando a oficial falhar, e identificadas como tais.
4. **Falha não é ausência.** Uma requisição malsucedida é registrada como falha de acesso. Nunca como prova de que o recurso não existe.
5. **Uma URL por requisição.** Sem seguir links, sem paginar, sem baixar dados do recurso. Captura-se a página que descreve; não o acervo.
6. **Nunca sobrescrever.** Cada captura é um arquivo novo e uma linha nova no registro.
7. **O coordenador captura; os avaliadores não.** Quem avalia recebe a evidência pronta.

## 3. Campos registrados

Um registro por captura, em `CAPTURE_LOG.jsonl`, uma linha JSON por registro.

| Exigência | Campo | Preenchimento |
|---|---|---|
| URL original | `original_url` | Automático |
| URL final | `final_url`, `redirect_chain` | Automático; cadeia completa de redirecionamentos |
| Data e hora UTC | `captured_at_utc`; `started_utc` em cada tentativa | Automático |
| Identificação do recurso | `record_id` | Informado pelo coordenador: identificador do inventário |
| Tipo e formato do conteúdo | `content_type`, `charset`, `content_language`, `bytes` | Automático, dos cabeçalhos |
| Arquivo bruto | `raw_file` | Automático; vazio se a cópia não for permitida |
| Hash | `sha256` | Automático, sobre os bytes recebidos |
| Versão ou data de atualização | `last_modified`, `etag` (do servidor); `human_fields.resource_version_or_update_date` (declarada na página) | Automático o que o servidor informa; **humano** o que a página declara |
| Condições de acesso e reutilização | `human_fields.access_conditions`, `reuse_terms_url`, `reuse_terms_note` | **Humano**, depois de ler os termos; nunca inferido |
| Falhas e tentativas | `attempts[]`: número, hora, resultado, código HTTP, erro, desafio de autenticação; `outcome` = `CAPTURED` ou `FAILED` | Automático |
| Relação com o item de avaliação | `record_id` no registro; `EVIDENCE_INDEX.csv` no pacote de cada avaliador, já com o identificador neutro | Automático no empacotamento |
| Rastreabilidade da ferramenta | `tool`, `tool_sha256`, `user_agent`, `method`, `purpose` | Automático |

Os campos humanos nascem **em branco**. A ferramenta não os preenche e um teste confere isso.

## 4. Procedimento

### 4.1 Antes

1. Amostra aprovada e registrada.
2. Para cada item, o coordenador lista as URLs a capturar: (a) a URL do inventário, sempre; (b) a página do recurso propriamente dito, quando a URL do inventário for página explicativa (ver `G1_READY_SOURCE_IDENTITY_REVIEW.md`, seção 3); (c) a página de termos de uso ou aviso legal do sítio.
3. A lista é gravada antes da execução. Teto de 25 URLs por execução, imposto pelo código.
4. Leitura dos termos de uso de cada sítio. Se proibirem cópia, usar `--no-store`: guarda-se hash e metadados, sem o arquivo.

### 4.2 Captura

```
python scripts/capture_evidence.py capture --url <URL> --record-id <ID> --purpose "Pilot A evidence"
```

- No máximo duas tentativas por URL, com pausa entre elas; pausa de pelo menos 5 segundos entre URLs.
- Identificação do cliente como pesquisa acadêmica, no cabeçalho `User-Agent`.
- Saída: `pilot_a/evidence/<ID>/<data-hora>_<hash>.<ext>` e uma linha no registro.

### 4.3 Páginas que só existem com JavaScript ou atrás de login

A captura por requisição simples devolve, nesses casos, uma casca vazia ou um erro. Procedimento:

1. Registrar a tentativa automática, com o resultado obtido.
2. Capturar manualmente no navegador: "salvar como PDF" da página inteira, **sem** recorte.
3. Registrar o arquivo:

```
python scripts/capture_evidence.py register --file <arquivo> --url <URL> --record-id <ID> --method manual_browser_pdf --captured-at-utc <AAAA-MM-DDTHH:MM:SS+00:00>
```

4. Recursos que exigem conta: **não** criar conta nem autenticar para o piloto sem decisão da equipe. Registrar a exigência; a evidência disponível é a página pública que descreve o recurso.

### 4.4 Depois

1. O coordenador abre cada captura e confere, a olho, que corresponde à página pretendida. Não anota conteúdo.
2. Preenche os campos humanos (versão declarada, condições de acesso, termos).
3. `python scripts/capture_evidence.py verify` recalcula todos os hashes.
4. O empacotamento (`pilot_a_forms.py package`) copia as capturas de cada item para o pacote de cada avaliador, sob o identificador neutro daquele avaliador, com um índice.

### 4.5 Durante a avaliação

- O avaliador julga pela captura. Pode abrir a página viva para navegar; se o que encontrar divergir da captura, anota em `observations`.
- Se precisar de página não capturada, pede ao coordenador, que captura e redistribui **aos dois**. O avaliador não captura por conta própria: a evidência tem de ser a mesma para ambos.
- Cada pedido é registrado. O número de pedidos por item é, em si, informação sobre a suficiência da evidência inicial.

## 5. Validação do procedimento

### 5.1 Testes automatizados

Doze testes em `tests/test_evidence_capture.py`, contra um servidor local em `127.0.0.1` com conteúdo sintético; nenhuma rede externa.

| Comportamento | Teste |
|---|---|
| Corpo gravado byte a byte, com hash, tamanho, tipo e `Last-Modified` | sim |
| URL original, URL final e cadeia de redirecionamento | sim |
| Falha registrada com todas as tentativas, sem arquivo, com o aviso de que não prova ausência | sim |
| Erro de rede registrado | sim |
| Exigência de autenticação registrada com o desafio | sim |
| Captura repetida não sobrescreve | sim |
| `--no-store` guarda só hash e metadados | sim |
| Campos humanos nascem vazios | sim |
| `verify` detecta arquivo adulterado | sim |
| Registro de arquivo capturado manualmente | sim |
| Só aceita `http` e `https` | sim |
| Lista acima do teto é recusada antes de qualquer requisição | sim |

### 5.2 Teste de rede

**Plano, declarado antes da execução:** duas requisições GET, uma para cada URL oficial indicada no G1-READY; no máximo duas tentativas cada; sem seguir links.

| URL | Resultado |
|---|---|
| `https://data.europa.eu/en/ELDS` | Capturada: HTTP 200, `text/html`, 69.561 bytes, SHA-256 `f5807d8e…92efea`, `Last-Modified` de 8 de outubro de 2026 |
| `https://datadump.publications.europa.eu/` | Falha registrada: HTTP 401 nas duas tentativas |

`verify`: 2 registros, 0 problemas. Arquivos em `pilot_a/evidence_procedure_test/`, separados da evidência do piloto.

**O que o teste mostrou**

| # | Achado | Classe |
|---|---|---|
| 1 | O procedimento funciona de ponta a ponta numa página oficial real. | VERIFIED |
| 2 | A página capturada traz o texto completo no HTML recebido; não depende de JavaScript para o conteúdo principal. | VERIFIED para esta página; PENDING VALIDATION para as demais |
| 3 | Recurso atrás de login produz falha registrada, não arquivo. O tratamento da seção 4.3 é necessário. | VERIFIED |
| 4 | Lacuna encontrada e corrigida: a ferramenta não guardava o desafio de autenticação da resposta de erro. Corrigido, com teste. A requisição não foi repetida. | VERIFIED |
| 5 | Nenhuma outra URL foi acessada. | VERIFIED |

## 6. Relação entre evidência e item

```
inventário (EUxx) ──> captura (record_id = EUxx, sha256) ──> pacote do avaliador A (A-nn/arquivo)
                                                          └─> pacote do avaliador B (B-nn/arquivo)
```

- O coordenador guarda as capturas por identificador do inventário.
- Cada avaliador recebe os mesmos arquivos, arquivados sob os **seus** identificadores neutros, com `EVIDENCE_INDEX.csv`: item, resultado, método, URL original, URL final, data, tipo, tamanho, hash, data de modificação, arquivo.
- O índice não contém identificador do inventário. O empacotamento falha se algum aparecer; há teste.
- No formulário, o avaliador cita a evidência por URL em `evidence_urls`. A conferência entre o citado e o capturado é feita pelo coordenador (critério AC10).

## 7. Volume previsto

Para uma amostra de 20 itens: 20 URLs do inventário, mais a página do recurso onde a URL registrada for explicativa (11 dos 20 itens na candidata S3a, pela análise estática, além de EU03), mais uma página de termos por sítio distinto. Ordem de grandeza: **40 a 60 requisições**, em duas ou três execuções. Não é coleta em massa, mas é acesso externo e precisa de autorização.

## 8. Limites

| # | Limite | Tratamento |
|---|---|---|
| 1 | Uma página HTML sem suas folhas de estilo e imagens fica menos legível | Para leitura, o avaliador pode abrir a página viva; o juízo é sobre o texto capturado |
| 2 | Conteúdo carregado por JavaScript não é capturado por requisição simples | Seção 4.3 |
| 3 | Recursos com login | Seção 4.3; decisão da equipe sobre contas |
| 4 | A captura é de uma data; o recurso pode mudar durante o piloto | Datas registradas; divergências anotadas pelo avaliador |
| 5 | Termos de uso de cada sítio não foram lidos | Leitura obrigatória antes da captura (4.1); campos humanos |
| 6 | Capturas ficam fora do git se `data/raw/` for usado; em `pilot_a/evidence/` não são ignoradas | Decidir se as capturas são versionadas, considerando os termos de cada fonte |
| 7 | Escolher quais páginas capturar já é um julgamento | A URL do inventário é sempre capturada; páginas adicionais são registradas com quem as escolheu e por quê |

## 9. Decisões para a equipe

1. Autorizar a captura para a amostra aprovada.
2. Quem captura (o coordenador, que não avalia).
3. Capturas versionadas no repositório, ou só os registros com hash.
4. Uso de serviço público de arquivamento como cópia adicional.
5. Criar ou não conta para recursos que exigem login.
