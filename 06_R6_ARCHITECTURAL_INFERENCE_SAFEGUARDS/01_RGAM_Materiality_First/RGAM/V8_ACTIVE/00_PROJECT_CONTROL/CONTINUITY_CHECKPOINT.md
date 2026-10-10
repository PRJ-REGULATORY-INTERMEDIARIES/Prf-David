# Continuity checkpoint — 3 October 2026

**Completed:** V8 baseline; codebook, data dictionary, relational and regime models; methodology; verified GDPR source materialization; complete machine-first unit screening; curated direct observations; worked cooperation/consistency trace; preliminary configurations/profile; technical report; conceptual working draft; consultation materials; standalone interface.

**Processed data:** `01_SOURCES/working_text.json`, correction log and unit inventory; coverage register for all parsed operative paragraph and point units; machine candidate statements; source-linked curated observations.

**Not complete:** human legal review of machine candidates; independent recoding; exhaustive expert interpretation of all candidates; verification of external instruments, national law, later GDPR amendments, and implementation/operation evidence.

**Current scientific decisions:** architecture is an inferential output; direct coding is separate from higher-order claims; incomplete evidence is recorded; the source baseline is historical; the pilot makes no reliability claim.

**Next reproducible operation:** run `python RGAM/V8_ACTIVE/04_EMPIRICAL_PILOT/GDPR_V8/scripts/materialize_verified_source.py`, then `v8_first_pass.py`; compare resulting row counts and hashes against `SOURCE_MANIFEST.md`, before independently reviewing candidate statements with the codebook.
