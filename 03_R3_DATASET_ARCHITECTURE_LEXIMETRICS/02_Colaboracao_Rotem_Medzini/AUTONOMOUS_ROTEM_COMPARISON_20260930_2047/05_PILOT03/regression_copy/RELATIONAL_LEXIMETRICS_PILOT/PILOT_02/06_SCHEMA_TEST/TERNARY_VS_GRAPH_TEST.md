# Ternary versus compositional graph test

## Model A — ternary record

`R -> I -> T` is stored directly. It is readable for a high-level architecture, but it duplicates the regulator and target whenever one intermediary has several functions, and it can assert a composite relation that no single provision expresses.

## Model B — binary/compositional graph

Store only provision-supported elementary edges: `R -> I`, `I -> T`, `I -> R`, `R -> T`, or another directed pair. Derive an R–I–T configuration only when edges share a case, actor identity, object/procedure and evidence-compatible provision set.

## Pilot result

The graph representation preserved evidence more cleanly in P01, P04 and P05. It handled applicant-to-validation-agent submission separately from validation-agent-to-Registry notification, and it avoided treating Article 18's audit/supervision condition as a settled R–I–T relation. Ternary records remain useful as a derived analytical view, but they should not be the primitive storage unit.

Finding: **MODEL B is preferred as the normalized core, with a derived ternary configuration view.**
