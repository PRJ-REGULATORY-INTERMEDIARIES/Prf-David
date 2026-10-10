# Error taxonomy

This taxonomy is operational and prospective. It is a coding aid for later error analysis; no real result is classified here.

| Category | Operational criterion |
|---|---|
| `omission` | A reference-supported unit or required element is absent from the experimental output. |
| `over-inclusion` | The output includes a unit as positive although no corresponding reference-positive unit is supported. |
| `boundary_error` | The output identifies the relevant provision or relation but uses an materially too broad, narrow, or mis-segmented span. |
| `category_error` | The unit is present but its substantive category or relational status is assigned incorrectly. |
| `regulator_error` | `R` is missing, replaced, or assigned to the wrong actor/role. |
| `intermediary_error` | `I` is missing, invented, or assigned to the wrong actor/role. |
| `target_error` | `T` is missing, replaced, or assigned to the wrong actor/role. |
| `target/object_confusion` | An activity, information, product, process, conduct, or compliance state is coded as `T`, or an actor is coded as `object`. |
| `mechanism_error` | The mechanism family does not fit the supported regulatory function. |
| `instrument/procedure_error` | An instrument or procedure is misidentified or conflated; applies mainly in reference review because the common experimental output does not expose these fields. |
| `evidence_error` | Evidence is absent, not located, inaccurately quoted, or does not support the asserted field. |
| `hallucination` | The output introduces an actor, fact, relation, or authority not supported by the supplied corpus. |
| `unsupported_inference` | The output makes an interpretation that may be plausible but is not sufficiently grounded in the supplied text. |
| `over-coding` | The output assigns extra actors, relations, attributes, mechanisms, or certainty beyond what the text supports. |
| `under-coding` | The output records less structure, evidence, or distinction than the text supports. |

## Coding rules

1. Assign the narrowest primary category that explains the error; add secondary categories when one error has distinct consequences.
2. Separate omission from under-coding: omission means an absent unit, while under-coding means a present but incomplete unit.
3. Separate over-inclusion from hallucination: over-inclusion concerns an unsupported positive unit; hallucination identifies unsupported invented content within an output.
4. Use `target/object_confusion` whenever the error violates the rule that only actors or institutional roles can be `T`.
5. Do not infer error solely from disagreement. A disagreement is a candidate for review; the taxonomy label requires evidence from the locked corpus and the reference decision.
6. Record the evidence location and the affected field in the later error table.

