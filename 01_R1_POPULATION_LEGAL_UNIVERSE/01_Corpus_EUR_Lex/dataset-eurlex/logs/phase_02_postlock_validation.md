# Validação pós-lock da Etapa 2

**Data:** 2026-09-07  
**Escopo:** auditoria de equivalência pós-lock  
**Estado mantido:** `project.status: corpus_locked`

## Papéis canônicos

- `02_corpus/act.md` é o **canonical analytical corpus** e deverá ser utilizado como entrada textual comum nas codificações substantivas e nas condições G0, G1 e G2.
- `02_corpus/act_numbered.md` é somente uma representação derivada para localização, auditoria e rastreabilidade da evidência. Não é uma entrada experimental alternativa.

## Verificação de equivalência

Foi removido de cada linha de `act_numbered.md` apenas o prefixo artificial no formato `NNNNN | `. A comparação restante foi feita linha a linha, sem normalização permissiva de conteúdo.

- Linhas comparadas: 423
- Resultado: `PASS`
- Nenhuma palavra, pontuação ou estrutura normativa substantiva diferiu.
- O teste foi mais estrito que a comparação por whitespace: o conteúdo de cada linha foi idêntico após a remoção da numeração.

## Hashes congelados

- `act.md`: `B24A02EA241CA631B606660BB48BB5A2222B29F849C4E4552FB99F871B2E8FD4`
- `act_numbered.md`: `0EB336AEA6C8FF19AF3B6536F3E9029A2E9AF68CA763E962429A8A3DACBB49ED`

Os hashes antes e depois da auditoria foram iguais. Nenhum dos dois arquivos congelados foi alterado.

## Encerramento

A Etapa 2 permanece aprovada e bloqueada. A Etapa 3 não foi iniciada automaticamente.
