# AI coding protocol v4

The AI layer proposes; it does not write directly to authoritative candidate
or relationship tables. The sequence is A1 lexical screening, A2 semantic
candidate detection, B1 architecture reconstruction, B2 five-condition
relational adjudication, human review, C institutional attributes and D
validation/error analysis.

Every call uses the supplied legal-context package, strict JSON Schema and
verbatim evidence requirements. One bounded context request may be made; an
unresolved gap is an abstention and a human-review route. B1 reconstructs all
actors and relations before R/I/T labels. B2 records YES/NO/UNCLEAR plus
actor, evidence and interpretive note for every condition. A false-
intermediary counterfactual is a diagnostic aid only.

Each unit is intended to run three times. Disagreement is preserved and sent
to human review, never averaged. Each run records provider, model id and
snapshot, reasoning setting, prompt/schema versions, timestamp, input/output
hashes, run id, token usage and cost estimate. A2 outputs link `ai_run_ref`
to that run id.

Human adjudication is distinct from independent second-coder validation. No
intercoder reliability statistic is claimed without a second coder. Strategy
variables `responsibilization_present` and `empowerment_present` are
independent codes with `1`, `0`, `UNCLEAR` or `NOE`; no strategy score is
computed. Failures are design risks the institution addresses, not evidence
that capture occurred.
