# Pacote de preparação da Etapa 4

A tentativa anterior foi arquivada integralmente em [`stage4_attempt_01/`](stage4_attempt_01/). Ela está supersedida e não deve ser usada como benchmark.

A nova execução está preparada em [`stage4_attempt_02/`](stage4_attempt_02/), mas ainda não foi executada:

- `candidate_reconstruction.json` contém contexto hierárquico e referências internas ao mesmo ato;
- `R1_coding_input.json` e `R2_coding_input.json` contêm apenas candidate ID, origem, localização e texto/contexto;
- os manifestos registram isolamento de contexto e proibições de acesso;
- `validate_reference_logic.py` contém os testes lógicos para A–E e `relational_result`;
- o template humano permanece vazio e não recomenda aprovar RA automaticamente.

Estado atual: `methodology_locked` / `not_started`. Não iniciar human gate, RA ou Etapa 5.
