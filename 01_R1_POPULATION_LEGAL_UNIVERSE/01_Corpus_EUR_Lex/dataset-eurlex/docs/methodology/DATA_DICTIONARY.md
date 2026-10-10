# Data dictionary

This dictionary separates reference variables, experimental variables, derived comparison variables, and metadata. It is prospective and contains no empirical values.

| Field | Meaning | Reference | Experimental | Derived / metadata |
|---|---|---:|---:|---:|
| `candidate_id` | Stable ID assigned to a reference-universe candidate | yes | no | reference-only |
| `relation_id` | Run-local ID assigned in an experimental response | no | yes | experimental-only |
| `source_location` | Reference location including CELEX and structural coordinates | yes | no | reference-only |
| `location` | Experimental structural location | no | yes | directly comparable after normalization |
| `R` | Regulator or focal regulatory role | yes | yes | directly produced / comparable |
| `I` | Distinct mediating actor or role | yes | yes | directly produced / comparable |
| `T` | Actor, class of actors, or institutional role subject to the relation | yes | yes | directly produced / comparable |
| `action` | Normative or institutional action | yes | yes | directly produced / comparable |
| `object` | Activity, information, product, process, conduct, or compliance state acted upon | yes | yes | directly produced / comparable |
| `mediating_function` | Function performed by an intermediary | yes | yes | directly produced / comparable |
| `instrument` | Artefact used or produced | yes | no | reference-only |
| `procedure` | Formal sequence, condition, or step | yes | no | reference-only |
| `mechanism` / `primary_mechanism` | Functional mechanism family | yes | yes | directly comparable at primary level |
| `secondary_mechanisms` | Additional reference mechanism families | yes | no | reference-only |
| `relational_test` | Conditions A–E used in reference adjudication | yes | no | reference-only |
| `relational_result` | Reference adjudication: positive, negative, conditional, or insufficient evidence | yes | no | derived from experimental `decision` for comparison only |
| `decision` | Experimental relation decision: intermediated, direct, uncertain, or not supported | no | yes | source for derived relational result |
| `evidence_items` | Structured reference evidence records with location, quote, role, observability, and supports | yes | no | reference-only |
| `evidence` | Experimental evidence strings | no | yes | derivable comparison evidence |
| `confidence` | Qualitative coding confidence | yes | yes | directly comparable labels, not calibrated probabilities |
| `interpretive_note` | Reference interpretation note | yes | no | reference-only |
| `notes` | Free-text run or coding notes | yes | yes | derived qualitative context |
| `candidate_origin` | Reference construction channel: lexical, structural, or both | yes | no | must remain hidden from experiment |
| `screening_status` | Candidate-universe screening state | yes | no | reference-only |
| `is_regulatory_act` | Reference boolean for regulatory-act status | yes | no | reference-only |
| `regulatory_act_type` | Reference type label | yes | no | reference-only |
| `rule_source`, `standard_setter`, `direct_regulator`, `oversight_authority`, `enforcement_authority` | Reference actor-role lists | yes | no | reference-only unless later derivation is explicitly justified |
| `additional_context_required` | Specific external context needed for reference adjudication | yes | no | reference-only |
| `responsibilization`, `empowerment` | Optional reference secondary dimensions | yes | no | reference-only |

## Normalization rules for later comparison

- Match structural locations after normalizing case, whitespace, and null/empty representations.
- Prefer explicit legitimate candidate IDs only in post-hoc comparison artifacts; never send them to G0/G1/G2.
- Normalize actor labels and lists conservatively; preserve uncertainty and multiplicity.
- Treat `candidate_origin` as inaccessible experimental metadata.
- Do not turn free text into a scored field without a separately documented coding rule.

