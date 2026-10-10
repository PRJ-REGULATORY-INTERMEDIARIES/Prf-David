# Experimental protocol correction — v1.1.1

This is a prospective, experimental-only correction to the locked `methodology/v1.1.0` interface.

It removes `candidate_origin` from `experimental_output_schema.json`. That field describes whether a reference candidate came from lexical screening, structural reading, or both. Passing it to G0/G1/G2 would leak reference-construction information and violate condition symmetry.

The correction does not modify the v1.1.0 codebook, reference schema, candidate universe, benchmark construction, or any empirical output. It is justified before G0/G1/G2 and must never be justified by their future results.

`relation_id` remains a run-local experimental identifier. Reference `candidate_id` values and `candidate_origin` values are not experimental inputs.

