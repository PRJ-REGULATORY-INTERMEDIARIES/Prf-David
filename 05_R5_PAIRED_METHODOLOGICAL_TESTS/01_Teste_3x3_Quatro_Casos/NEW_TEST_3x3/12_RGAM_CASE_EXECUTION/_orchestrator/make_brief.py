import sys, os, hashlib
cid = sys.argv[1]
R = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3"
F = R + "/11_RGAM_PROTOCOL_FREEZE"
C = F + "/CAPSULES/" + cid
O = R + "/12_RGAM_CASE_EXECUTION/" + cid
brief = f"""# EXECUTOR BRIEF — RGAM case `{cid}` (identical for all four cases except the capsule id)

You are a fresh, isolated RGAM case executor. You have no prior context. Execute the frozen native RGAM protocol on ONE legal instrument. You are not authorized to analyse anything else.

## 1. STRICT ALLOW-LIST (authoritative; technical deny rules may be inactive and shell commands can bypass them)
READ only these paths:
1. {F}/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md
2. {F}/RGAM_PAIRED_DECISION_RULES_v1_0.md
3. {F}/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md
4. {F}/RGAM_CASE_OUTPUT_SCHEMA.md
5. {F}/RGAM_BLINDNESS_AND_ACCESS_POLICY.md
6. {F}/RGAM_EXECUTION_GAP_DECISIONS_v1_0.md   (execution addendum: GAP-01..07; read it carefully, it is operative)
7. everything under {C}/  (CASE_METADATA.json, CAPSULE_README.md, LEGAL_SOURCE/, OUTPUT_TEMPLATES/)
8. everything under {O}/  (your own output directory, including this brief)
WRITE only under {O}/ . You may create {O}/_work/ for scratch (parsed units, progress notes).
Address files by these exact paths. Do NOT list or browse any other directory (not even parent directories of the repository), do NOT search the repository (no repo-wide grep/glob/find), do NOT read any memory files, CLAUDE.md files or settings files, do NOT browse the web or fetch anything external. If information is not in the allow-listed sources, it is UNAVAILABLE: say so; do not look elsewhere.
FORBIDDEN (never read, never request): any V8 output or the V8 baseline directory; any R2/R3/R4 output; V8-COMP-01 or any earlier comparison material; historical relationship registers or pilot outputs; case-selection or ranking material; any other RGAM case directory or its results; the RGAM theory/ontology/manuscript source files (the frozen protocol is self-contained: use only the frozen documents above).
Shell use (bash/python/PowerShell) is permitted ONLY to operate on allow-listed paths (hashing, parsing the capsule source file with scripts, writing files under your output directory). Never use a shell to read or list anything else.

## 2. Task
Execute RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md phases P0–P9 on the capsule's controlling legal source, following the decision rules, data dictionary and execution addendum EXACTLY. Native chain: W → E → P → R → S → A → profile, with M as the transversal control. Do not use any other operation list, do not use V8 or any other vocabulary, do not optimise for any comparison, do not compare with any other method or case.
- P0: verify the SHA-256 of LEGAL_SOURCE/* against CASE_METADATA.json. If it does not match: STOP, gate RGAM_CASE_BLOCKED.
- Copy the blank templates from OUTPUT_TEMPLATES/ into {O}/ and populate the frozen schema (RGAM_CASE_OUTPUT_SCHEMA.md): exactly the 19 CSV tables with the frozen headers plus CASE_RGAM_REPORT.md. Do not invent another schema. Empty tables are acceptable; do not fabricate records.
- Scripts may be used ONLY for mechanical work (parsing the source file into units, hashing, id generation, schema/ID integrity checks). Every analytical record (statement, NA, PD, QR, EXT, SC, ARCH, PROP, closure, queue item) must come from your own reading of the unit text, not from keyword or pattern rules.
- The whole instrument must be covered: every unit inventoried and screened (RGAM-DR-06). The instrument may be large: work in batches in source order, write results to disk incrementally, keep a progress note in {O}/_work/ so you can resume, and continue until coverage is complete. Do not mark the case frozen with partial coverage; if resources genuinely prevent completion, finish what can be completed honestly and declare RGAM_CASE_BLOCKED with the precise reason.
- Apply the discipline of the protocol: exact provenance (units + verbatim spans); never invent a counterparty; no relation from co-occurrence; no legal transmission from reachability; legal status vs epistemic status; property bearers; scale before architectural inference; I1–I4 exactly as frozen with rival groupings; INDETERMINATE and NO_ARCHITECTURE_WARRANTED are legitimate; obey the stopping rule; do not force an architecture; no scores.
- Human review: create HUMAN_REVIEW_QUEUE items (claim, evidence, inference, uncertainty, exact human question, machine recommendation) where the protocol requires; leave every human_* column blank. Never adjudicate.
- Record every execution-addendum use (GAP-01..07) in PROTOCOL_DEVIATION_LOG with gap_ref; use the tokens NON_OPERATIVE_SOURCE_GAP / FUNCTION_VOCABULARY_UNRESOLVED only as the addendum prescribes.
- Executor settings: use your highest available reasoning effort. In RUN_METADATA record your model identifier exactly as you can observe it and the reasoning/effort setting as displayed or, if you cannot observe it, NOT_EXPOSED; temperature, top-p, seed, token limits: NOT_EXPOSED unless you can actually see them. Record every path you read in files_read.

## 3. Case freeze deliverables (in {O}/)
- CASE_QA_REPORT.md — verify and report: source hash matches capsule; only allow-listed files read; no V8 output read; no historical extraction read; no other RGAM case result read; all records have stable ids; every higher-order claim is vertically traceable (A→S→R/NA/PD→ST→unit→span); unsupported claims were rejected or deferred; INDETERMINATE remained available; HQ items not adjudicated; frozen method not altered; data-dictionary integrity rules 1–10 (state result per rule).
- ACCESS_AND_CONTAMINATION_LOG.md — every file read (exact paths) and every shell command category used; any attempted or accidental read outside the allow-list (exact path and what, if anything, was seen); an explicit contamination status: CLEAN or CONTAMINATED (with detail).
- EXECUTION_PROVENANCE.md — model/effort/parameters as recorded, start/end times, method version, manifest hash of the protocol as stated in the capsule if available, scripts used (only mechanical).
- CASE_FREEZE_MANIFEST.csv (relative_path, bytes, sha256 for every file in {O}/ except the manifest and its sidecar, excluding the _work/ scratch folder) and CASE_FREEZE_MANIFEST_SHA256.txt (sha256 of the manifest).
- CASE_GATE.md — exactly one of: RGAM_CASE_FROZEN or RGAM_CASE_BLOCKED, with a short factual basis. A case-specific analytical difficulty is not a reason to block; method/source failure (hash mismatch, corrupted protocol, impossibility to complete coverage) is.

## 4. RETURN RULE (critical)
Your final message to the orchestrator must contain ONLY these seven items and nothing else — no architecture conclusions, no relationship lists, no counts of records, no findings, no descriptions of what the law does:
1. case id; 2. completion gate; 3. output path; 4. source hash verification result (MATCH/MISMATCH); 5. freeze-manifest SHA-256; 6. contamination status (CLEAN/CONTAMINATED); 7. whether human-review items exist (YES/NO).
"""
os.makedirs(O, exist_ok=True)
p = O.replace("/", os.sep) + os.sep + "EXECUTOR_BRIEF.md"
open(p, "w", encoding="utf-8").write(brief)
print(p, hashlib.sha256(brief.encode("utf-8")).hexdigest())
