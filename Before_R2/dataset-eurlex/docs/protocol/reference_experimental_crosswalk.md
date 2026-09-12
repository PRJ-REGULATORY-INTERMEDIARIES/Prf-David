# Reference–experimental crosswalk

This crosswalk defines what can be compared after reference lock and completion of G0/G1/G2. It defines no empirical value and performs no matching now. The common experimental interface is v1.1.2; v1.1.1 remains preserved as a historical pre-experiment correction.

| Reference benchmark variable | Experimental counterpart | Classification | Later use / limitation |
|---|---|---|---|
| `candidate_id` | none; `relation_id` is run-local | somente referência | Never expose to a condition; use only for post-hoc matching artifacts when justified |
| `candidate_origin` | none | somente referência | Must remain hidden; lexical/structural/both is a confirmed leakage risk |
| `source_location` | `location` | diretamente produzida pelo experimental output | Normalize article/paragraph/point/subparagraph/recital; CELEX is reference/metadata only |
| `screening_status` | none | somente referência | Construction status is not an experimental response |
| `is_regulatory_act` | `decision` plus coded fields | derivável | Only a cautious post-hoc binary proxy; not identical to reference screening |
| `regulatory_act_type` | none | somente referência | Not represented by the common experimental contract |
| `rule_source` | none | somente referência | Reference actor sub-role is not a common experimental field |
| `standard_setter` | none | somente referência | Do not infer from an experimental `R` |
| `direct_regulator` | `R` | derivável | Compare normalized actor labels, with role/context caveat |
| `oversight_authority` | none | somente referência | Not directly comparable |
| `enforcement_authority` | none | somente referência | Not directly comparable |
| `R` | `R` | diretamente produzida pelo experimental output | v1.1.2 array of zero, one, or multiple actor-label strings; compare as unordered normalized actor labels with role-aware review |
| `I` | `I` | diretamente produzida pelo experimental output | v1.1.2 array of zero, one, or multiple actor-label strings; compare as unordered normalized actor labels |
| `T` | `T` | diretamente produzida pelo experimental output | v1.1.2 array of zero, one, or multiple actor-label strings; activity/object values must not be coerced into actors |
| `action` | `action` | diretamente produzida pelo experimental output | Normalize labels, preserve multi-valued output |
| `object` | `object` | diretamente produzida pelo experimental output | Compare as object, not as `T` |
| `mediating_function` | `mediating_function` | diretamente produzida pelo experimental output | Direct field comparison after normalization |
| `instrument` | none | somente referência | No experimental field in v1.1.2 |
| `procedure` | none | somente referência | No experimental field in v1.1.2 |
| `relational_test.condition_A`–`condition_E` | none | somente referência | A–E belong to reference adjudication and must not be supplied to conditions |
| `relational_result` | `decision` | derivável | For the focal binary comparison, intermediated is positive and every other decision is non-intermediated; the finer mapping is secondary/exploratory only |
| `primary_mechanism` | `mechanism` | diretamente produzida pelo experimental output | Compare primary family only; secondary mechanisms have no counterpart |
| `secondary_mechanisms` | none | somente referência | Not comparable |
| `evidence_items` | `evidence` | derivável | Experimental evidence is an array of strings, not structured evidence items; compare presence/location/text cautiously |
| `confidence` | `confidence` | diretamente produzida pelo experimental output | Same labels, but not necessarily calibrated equivalently |
| `interpretive_note` | `notes` | derivável | Qualitative only; no numeric metric |
| `additional_context_required` | none | somente referência | Not comparable |
| `notes` | `notes` | derivável | Free-text audit context; do not score as substantive agreement |
| `secondary_dimensions.responsibilization` | none | somente referência | Not in common experimental output |
| `secondary_dimensions.empowerment` | none | somente referência | Not in common experimental output |
| `celex` | none in experimental record | somente metadado | Corpus-level metadata; do not use as a candidate-level prediction |

## Metric derivation

For later analysis, the binary focal comparison is **intermediated vs non-intermediated**: `decision == intermediated` is positive, while `direct`, `uncertain`, and `not_supported` are grouped as non-intermediated. A direct experimental decision maps into the broader reference negative class only for this derived comparison; it is not asserted to be substantively identical to every reference negative adjudication.

The multicategory mapping `intermediated→positive`, `direct→negative`, `uncertain→conditional`, and `not_supported→insufficient_evidence` is secondary and exploratory. It must not replace or redefine the focal binary comparison. With transparent post-hoc matching:

- **TP:** matched reference-positive unit and experimental-positive unit;
- **FP:** experimental-positive unit without a matched reference-positive unit;
- **FN:** reference-positive unit without a matched experimental-positive unit;
- **precision:** TP / (TP + FP), or 0 when the denominator is zero;
- **recall:** TP / (TP + FN), or 0 when the denominator is zero;
- **F1:** harmonic mean of precision and recall, or 0 when both are zero.

The same comparison layer may report `relational_result` agreement, R/I/T agreement, and mechanism agreement for matched records. A missing or uncertain match must be reported as such rather than forced.
