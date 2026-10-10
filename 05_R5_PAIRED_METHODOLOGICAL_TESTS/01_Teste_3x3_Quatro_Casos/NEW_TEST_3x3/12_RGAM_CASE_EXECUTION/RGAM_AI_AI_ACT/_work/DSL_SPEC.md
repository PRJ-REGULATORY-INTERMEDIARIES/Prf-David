# DSL / workflow notes (executor scratch; resume here after any interruption)
Files: _work/units.json (parsed units, mechanical), _work/dump/dNN.txt (unit text batches, source order),
_work/rec/rNN.txt (executor-authored records, one line per record: `TYPE | key=value | ...`),
_work/assemble.py (mechanical: resolves labels, extracts verbatim spans between executor anchors `sp=start~~end`, writes build/*.csv, runs integrity checks -> build/CHECK.txt),
_work/ls_map.json (per-unit-prefix legal-status defaults).
Record types: ST, NA, QR, PD, EXT, UNC, HQ, SC, ARCH, PROP, CL, TR, DEV, RUN, SCR (screening of units with no statement).
Codes: fn rm/im/it/ip/mo/va/en/ad/re/rp/ag/cc/un ; mod ob/op/pr/pe/co/en/de/dc ; rt ac/da/os/acc/ir/va/ra/rp/ce/bp ; ST kind ab/rb/pd/dd/df/sc/pr/ex/ff/ot
NA/QR attach to the most recent ST line unless st= given. Units are short ids (prefix RGAM_AI_AI_ACT. omitted); X..Y = inclusive source-order range.
Progress file: PROGRESS.md
