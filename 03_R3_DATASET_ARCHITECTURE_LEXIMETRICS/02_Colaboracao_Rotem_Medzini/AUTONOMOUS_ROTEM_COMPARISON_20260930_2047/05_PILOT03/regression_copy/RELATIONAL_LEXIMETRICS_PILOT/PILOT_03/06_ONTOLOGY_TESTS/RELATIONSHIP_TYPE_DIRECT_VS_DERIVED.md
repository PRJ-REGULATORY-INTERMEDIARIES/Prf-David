# Direct versus derived relationship type

`relationship_type_direct` is anchored to one provision-supported directed edge. It may be `EDGE_A_TO_B`, `COMPOSITE_CANDIDATE` where the provision itself contains multiple legal moves, or `UNRESOLVED_DIRECT_EDGE` when the direct edge cannot be responsibly normalized.

`relationship_type_derived` is a separate result: `RIT_DERIVED` only when the preregistered R1–R9 rules can be satisfied; otherwise `BINARY_ONLY`. The derived field never overwrites the primitive edge.
