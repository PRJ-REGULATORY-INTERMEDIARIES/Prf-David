# G1-READY — FORMULÁRIO DE AUTORIZAÇÃO DO PILOTO A

**Estado deste arquivo:** EM BRANCO. Nenhum campo foi preenchido por agente de IA. Só a equipe preenche.

**Como usar.** Cada linha de decisão recebe: a decisão, o nome de quem decide e a data. Linha sem os três campos vale como **não decidida**. Depois de preenchido e assinado, registrar o SHA-256 do arquivo e copiá-lo para a pasta de gate. Alterações posteriores são feitas em novo arquivo datado, nunca por edição deste.

Documento de apoio: `gates/G1_READY_AUTHORIZATION_DOSSIER.md`.

---

## ETAPA 1 — Decisões e autorização da captura de evidências

### 1. Enquadramento

| # | Decisão | Opções | Decisão | Responsável | Data |
|---|---|---|---|---|---|
| 1.1 | Reorientação do estudo (finalidade: fundamentar a seleção da fonte legislativa) | Adotada pela equipe / Piloto A autorizado enquanto se discute / Não autorizado | | | |

### 2. Amostra

| # | Decisão | Opções | Decisão | Responsável | Data |
|---|---|---|---|---|---|
| 2.1 | Amostra do Piloto A | S3a / S3a com o grupo EU01+EU02 (novo sorteio, mesma semente) / outro cenário (qual) / G1-PREP / lista do G0.1 / outra | | | |
| 2.2 | Motivo da escolha (obrigatório) | Texto | | | |
| 2.3 | Grupo obrigatório EU08 + EU09 | Confirmar / Retirar | | | |
| 2.4 | Grupo obrigatório EU33 + EU34 | Confirmar / Retirar | | | |
| 2.5 | Grupo obrigatório EU11 | Confirmar / Retirar | | | |
| 2.6 | Grupo obrigatório de corpora acadêmicos | EU35+EU39 / EU37+EU38 / EU35+EU36 / mais de um / nenhum | | | |
| 2.7 | Outros grupos obrigatórios | Lista e motivo, ou "nenhum" | | | |
| 2.8 | Lista final dos 20 registros | Identificadores | | | |
| 2.9 | SHA-256 do arquivo da amostra aprovada | Hash | | | |

### 3. Identidade e rótulos

| # | Decisão | Opções | Decisão | Responsável | Data |
|---|---|---|---|---|---|
| 3.1 | URL entregue ao avaliador para EU03 | A do inventário / A de acesso | | | |
| 3.2 | Correção candidata de EU03 (registrar URL de acesso) | Aceita / Rejeitada / Adiada | | | |
| 3.3 | Rótulos exibidos | Lista proposta / Lista proposta com alterações (quais) / Nomes do inventário | | | |
| 3.4 | Menções a "RGAM/V8" no texto da taxonomia entregue | Manter / Produzir versão sem elas | | | |

### 4. Critérios

| # | Decisão | Opções | Decisão | Responsável | Data |
|---|---|---|---|---|---|
| 4.1 | Critérios de aceitação AC1–AC31 | Aprovados / Aprovados com alterações (quais) / Não aprovados | | | |
| 4.2 | Tamanho da rodada de confirmação | Proposto: 10 | | | |
| 4.3 | Alerta numérico em `operational_level` | Proposto: 7 ou menos concordâncias em 10 | | | |
| 4.4 | Alerta secundário de incerteza | Proposto: 4 ou mais respostas incertas em 10, por avaliador e variável / Não adotar | | | |
| 4.5 | Vocabulário de funções F1–F8 | Manter no piloto / Alterar / Retirar | | | |
| 4.6 | Demais vocabulários provisórios | Confirmar / Alterar | | | |

### 5. Pessoas

Este formulário é o único lugar em que as funções são atribuídas.

| Função | Nome | Declaração de exposição prévia arquivada (sim/não) | Designado por | Data |
|---|---|---|---|---|
| Coordenador do piloto (não avalia) | | | | |
| Reviewer A | | | | |
| Reviewer B | | | | |
| Adjudicator | | | | |

| # | Decisão | Opções | Decisão | Responsável | Data |
|---|---|---|---|---|---|
| 5.1 | Quem construiu ou leu o inventário pode avaliar? | Sim, com declaração / Não | | | |
| 5.2 | Se a independência for parcial, como será declarada no relato | Texto | | | |

### 6. Evidências

| # | Decisão | Opções | Decisão | Responsável | Data |
|---|---|---|---|---|---|
| 6.1 | Protocolo de captura de evidências | Aprovado / Aprovado com alterações / Não aprovado | | | |
| 6.2 | Autorização para as requisições de captura da amostra aprovada | Autorizada / Não autorizada | | | |
| 6.3 | Quem captura | Nome | | | |
| 6.4 | Capturas no repositório | Arquivos e registros / Só registros com hash | | | |
| 6.5 | Cópia em serviço público de arquivamento | Sim / Não | | | |
| 6.6 | Conta para recursos que exigem login | Criar (quem) / Não criar | | | |

### 7. Entrega

| # | Decisão | Opções | Decisão | Responsável | Data |
|---|---|---|---|---|---|
| 7.1 | Canal de entrega dos pacotes | Descrição | | | |
| 7.2 | Prazo de codificação | Data | | | |

### Assinaturas da Etapa 1

| Nome | Função | Assinatura | Data |
|---|---|---|---|
| | | | |
| | | | |

---

## ETAPA 2 — Autorização para iniciar a codificação

Preencher somente depois de concluída a captura e entregues os pacotes.

### 8. Verificação das condições

| # | Condição | Evidência | Cumprida (sim/não) | Conferido por | Data |
|---|---|---|---|---|---|
| S1 | Etapa 1 preenchida, datada e assinada | Este arquivo | | | |
| S2 | Amostra aprovada gravada, com grupos obrigatórios e registro do sorteio | Arquivos e hashes | | | |
| S3 | Rótulos aprovados gravados | Arquivo e hash | | | |
| S4 | Critérios, confirmação e alerta aprovados antes da entrega | Datas das seções 4 e 9 | | | |
| S5 | Funções designadas; declarações arquivadas | Seção 5 | | | |
| S6 | Evidências capturadas; verificação de hashes sem problemas; campos humanos preenchidos | Saída de `capture_evidence.py verify` | | | |
| S7 | Pacotes regenerados; validador reporta 20 itens em branco e campos pré-preenchidos conferidos, em ambos | Saída de `pilot_a_forms.py validate` | | | |
| S8 | Pacotes compactados; hashes registrados; entrega individual fora do repositório | `DIST_MANIFEST.json`; registro de entrega | | | |
| S9 | Testes automatizados aprovados na versão do código usada | Saída de `python -m unittest discover -s tests` | | | |

### 9. Registro da entrega

| Pacote | SHA-256 do arquivo entregue | Entregue a | Canal | Data e hora |
|---|---|---|---|---|
| Reviewer A | | | | |
| Reviewer B | | | | |

### 10. Autorização

| Decisão | Opções | Decisão | Responsável | Data |
|---|---|---|---|---|
| Início da codificação do Piloto A | Autorizado / Não autorizado | | | |

### Assinaturas da Etapa 2

| Nome | Função | Assinatura | Data |
|---|---|---|---|
| | | | |
| | | | |

---

## Registro do arquivo

| Item | Valor |
|---|---|
| SHA-256 deste arquivo depois da Etapa 1 | |
| SHA-256 deste arquivo depois da Etapa 2 | |
| Copiado para a pasta de gate em | |
