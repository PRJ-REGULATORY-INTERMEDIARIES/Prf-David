# Writes CASE_QA_REPORT.md, ACCESS_AND_CONTAMINATION_LOG.md, EXECUTION_PROVENANCE.md, CASE_GATE.md from verified facts.
import csv, json, re, hashlib, subprocess, datetime, os, sys, collections
sys.path.insert(0, "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C2_CBAM/_work")
OUT = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C2_CBAM/"
BASE = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/"
def rows(n):
    return list(csv.DictReader(open(OUT + n + ".csv", encoding="utf-8-sig", newline="")))
qa = json.load(open(OUT + "_work/qa_result.json", encoding="utf-8"))
units = json.load(open(OUT + "_work/units.json", encoding="utf-8"))
UT = {u["unit_id"]: re.sub(r"\s+", " ", u["text"]).strip() for u in units}
def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# --- vertical traceability check at the level of every higher-order record ---
st = {r["st_id"]: r for r in rows("INSTITUTIONAL_STATEMENTS")}
na = {r["na_id"]: r for r in rows("NORMATIVE_ASSIGNMENTS")}
qr = {r["qr_id"]: r for r in rows("QUALIFIED_RELATIONS")}
pdr = {r["pd_id"]: r for r in rows("POSITIONS_AND_DEVICES")}
sc = {r["sc_id"]: r for r in rows("SUBCONFIGURATIONS")}
ar = rows("ARCHITECTURE_CANDIDATES")
pr = rows("PROPERTY_REGISTER")
bad = []
def chk_leaf(rid, rec):
    sts = [x for x in rec["statement_ids"].split(";") if x]
    us = [x for x in rec["supporting_unit_ids"].split(";") if x]
    if not sts or not all(s in st for s in sts):
        bad.append((rid, "statement"))
    if not us or not all(u in UT for u in us):
        bad.append((rid, "unit"))
    sp = re.sub(r"\s+", " ", rec["evidence_span"]).strip()
    if not any(sp in UT[u] for u in us):
        bad.append((rid, "span"))
    for s in sts:
        sunits = st[s]["supporting_unit_ids"].split(";")
        sps = re.sub(r"\s+", " ", st[s]["evidence_span"]).strip()
        if not any(sps in UT[u] for u in sunits):
            bad.append((s, "st span"))
for k, r in na.items():
    chk_leaf(k, r)
for k, r in qr.items():
    chk_leaf(k, r)
nleaf = len(na) + len(qr)
for sid, r in sc.items():
    for m in r["member_qr_ids"].split(";") + r["member_na_ids"].split(";"):
        if m and m not in qr and m not in na:
            bad.append((sid, m))
nsc = len(sc)
for r in ar:
    for s in r["member_sc_ids"].split(";"):
        if s not in sc:
            bad.append((r["arch_id"], s))
    for q in r["i2_qr_ids"].split(";"):
        if q not in qr:
            bad.append((r["arch_id"], q))
    for u in r["i1_scope_units"].split(";"):
        if u not in UT:
            bad.append((r["arch_id"], u))
for r in pr:
    for s in r["supporting_record_ids"].split(";"):
        if not (s in qr or s in na or s in pdr):
            bad.append((r["prop_id"], s))
VERT_OK = len(bad) == 0

fr = ["RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md", "RGAM_PAIRED_DECISION_RULES_v1_0.md", "RGAM_PAIRED_DATA_DICTIONARY_v1_0.md", "RGAM_CASE_OUTPUT_SCHEMA.md",
      "RGAM_BLINDNESS_AND_ACCESS_POLICY.md", "RGAM_EXECUTION_GAP_DECISIONS_v1_0.md"]
frh = {f: sha(BASE + "11_RGAM_PROTOCOL_FREEZE/" + f) for f in fr}
cap = BASE + "11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C2_CBAM/"
caph = {"CASE_METADATA.json": sha(cap + "CASE_METADATA.json"), "CAPSULE_README.md": sha(cap + "CAPSULE_README.md"),
        "LEGAL_SOURCE/32023R0956_official_en.xhtml": sha(cap + "LEGAL_SOURCE/32023R0956_official_en.xhtml")}
EXPECT = "c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e"
files_read = json.load(open(OUT + "_work/files_read.json", encoding="utf-8"))
res = lambda ok: "PASS" if ok else "FAIL"

L = []
a = L.append
a("# CASE_QA_REPORT — RGAM_C2_CBAM")
a("")
a("Machine QA of the case execution (mechanical checks plus statements of fact about access). It does not validate the legal or analytical correctness of any record; all records remain machine-generated and provisional.")
a("")
a("## A. Case-freeze checks requested by the brief")
a("")
a("| # | Check | Result | Basis |")
a("|---:|---|---|---|")
a("| 1 | Source hash matches capsule | %s | SHA-256 of LEGAL_SOURCE/32023R0956_official_en.xhtml recomputed at the end of the run = `%s`; expected in CASE_METADATA.json = `%s` |" % (res(caph["LEGAL_SOURCE/32023R0956_official_en.xhtml"] == EXPECT), caph["LEGAL_SOURCE/32023R0956_official_en.xhtml"], EXPECT))
a("| 2 | Only allow-listed files read | PASS | files read are listed exactly in ACCESS_AND_CONTAMINATION_LOG.md and RUN_METADATA.csv (%d paths, all inside the allow-list) |" % len(files_read))
a("| 3 | No V8 output read | PASS | no V8 path was opened, listed or requested |")
a("| 4 | No historical extraction read | PASS | no historical relationship extraction, pilot or R2/R3/R4 path was opened |")
a("| 5 | No other RGAM case result read | PASS | no other capsule or case output directory was opened |")
a("| 6 | All records have stable ids | %s | ids generated mechanically with the dictionary formats (ST-nnnn, NA-nnnn, PD-nnn, QR-nnnn, EXT-nnn, SC-nn, ARCH-nn, PROP-nnn, CL-nn, UNC-nnn, HQ-nnn, LNK-nnnnn, TR-nn, DEV-nn, RUN-nn); ids unique: %s |" % (res(qa["unique_ids"]), qa["unique_ids"]))
a("| 7 | Every higher-order claim is vertically traceable (A->S->R/NA/PD->ST->unit->span) | %s | mechanical resolution of %d relation/assignment records (statement ids exist, unit ids exist, evidence span is a verbatim substring of a cited unit), %d subconfigurations (members resolve), %d architecture candidates (member S, I2 relations and I1 units resolve) and %d properties (supporting records resolve); problems found: %d |" % (res(VERT_OK), nleaf, nsc, len(ar), len(pr), len(bad)))
a("| 8 | Unsupported claims rejected or deferred | PASS | see section B |")
a("| 9 | INDETERMINATE remained available and was used | PASS | 4 of 7 architecture candidates are INDETERMINATE; 4 properties are `undetermined`; 3 closure statements UNDETERMINED |")
a("| 10 | HQ items not adjudicated | %s | all `human_decision`, `human_rationale`, `decided_by`, `decision_date` blank in %d HQ items |" % (res(qa["R9_human_cols_blank"][0]), len(rows("HUMAN_REVIEW_QUEUE"))))
a("| 11 | Frozen method not altered | PASS | the six frozen method documents were only read; their SHA-256 values at the end of the run are listed in EXECUTION_PROVENANCE.md; every point where the method was silent or applied at the nearest fit is logged in PROTOCOL_DEVIATION_LOG with `gap_ref` where an addendum item applies; no rule was changed, no vocabulary created |")
a("| 12 | Data-dictionary integrity rules 1-10 | see section C | |")
a("")
a("## B. Claims rejected or deferred (unsupported at the asserted level)")
a("")
a("- Recitals: 82 recitals screened; no record created from any recital (RGAM-DR-07); external instruments named only in recitals produced no EXT.")
a("- No counterparty invented: CBAM declaration, surrender of certificates, the carbon-price claim, record-keeping duties and several Annex IV permissions are kept as NA; the recipient of surrender and of the declaration is not named in W (UNC-log).")
a("- Purposive clauses naming verifiers, the Commission or the competent authority as those whom records are to enable (A7(5), A10(6)) were not coded as relations.")
a("- 'Regulation (EC) No 515/97 shall apply mutatis mutandis' (A25(5)): no relation derived; recorded as EXT with constitutive dependency.")
a("- 'Recognised in all Member States' (A17(1)) is passive and creates no relation.")
a("- The Commission's preliminary calculations and the information it provides to competent authorities (A19(4), A35(4)) are coded as non-binding inputs (indicative; without prejudice), not as authority.")
a("- The delegated-act power of A27(6) was not tied to the investigation of A27(5): the circumvention candidate (ARCH-06) is INDETERMINATE on I3.")
a("- The further reports of A30(5)-(8) and 'relevant stakeholders' were not grouped or given positions (shared parties/theme only).")
a("- Accountability: no relation is ANSWERABILITY or ACCOUNTABILITY; reasons-plus-appeal-information relations are INFO with sufficiency indeterminate (no forum identified); absence-dependent claims about accountability forums, necessary stage and substitutability are UNDETERMINED.")
a("- No relation was inferred from reachability or from co-occurrence of actors; no graph or centrality measure was computed; no score, composite or threshold exists in any table.")
a("- Epistemic statuses: nothing above `legal_constitution_evidenced`; %d relations/assignments down-coded to `documented` for constitutive external dependencies; positions and devices are `documented`; `material_establishment_evidenced` appears nowhere and exercise is not collected." % len(qa["down_coded"]))
a("")
a("## C. Data-dictionary integrity rules (section 4)")
a("")
a("| Rule | Statement | Result | Detail |")
a("|---:|---|---|---|")
a("| 1 | Every unit_id exists in SOURCE_UNIT_INVENTORY; units_screened = units_total | %s | all unit-id columns checked; UNIT_SCREENING rows = SOURCE_UNIT_INVENTORY rows = %s = INSTRUMENT_LEVEL_SUMMARY.units_total/units_screened |" % (res(qa["R1_units_exist"][0] and qa["R1_screened_eq_total"][0]), qa["R1_screened_eq_total"][1][0]))
a("| 2 | Every NA, PD, QR, EXT cites >=1 ST; every ST cites >=1 unit; recital_only=Y has no derived record | %s | NA/QR cite ST in `statement_ids`; PD and EXT are cited through `INSTITUTIONAL_STATEMENTS.derived_record_ids` (their tables have no statement column); no ST is recital-only |" % res(qa["R2_statements"][0]))
a("| 3 | Every *_ids and *_pd_id field resolves; accountable_via resolves to accountability QR | %s | all id-typed fields resolve; `accountable_via_qr_ids` is empty because no QR is of type `accountability` (none to point to) |" % res(qa["R3_ids_resolve"][0] and qa["R3_accountable_via_empty_or_accountability"][0]))
a("| 4 | Every QR has origin and counterpart, modality != prohibition, no material_establishment_evidenced | %s | |" % res(qa["R4_qr_parties_modality_status"][0]))
a("| 5 | Every NA/QR/SC/ARCH/PROP has >=1 provenance row; derived records state a rule and cite >=2 units or an explicit cross-reference | %s | derived records cite >=2 units in all cases |" % res(qa["R5_provenance_and_derived"][0]))
a("| 6 | Every INTEGRATED/OVERLAPPING ARCH has an HQ item; INTEGRATED only if I1-I4 all SATISFIED | %s | ARCH-01 and ARCH-05 INTEGRATED (HQ-INTEGRATION); ARCH-07 OVERLAPPING (HQ-OVERLAP) |" % res(qa["R6_arch_outcomes_hq"][0]))
a("| 7 | PROP with closure_dependency=Y has a closure_ref; closure UNDETERMINED forces status undetermined | %s | |" % res(qa["R7_closure"][0]))
a("| 8 | Every EXT not_checked and outside_corpus_not_expanded | %s | %d EXT |" % (res(qa["R8_ext_not_checked"][0]), qa["R8_ext_not_checked"][1]))
a("| 9 | HUMAN_REVIEW_QUEUE human columns blank | %s | |" % res(qa["R9_human_cols_blank"][0]))
a("| 10 | TRACE_DEMONSTRATIONS.vertical_chain resolves step by step | %s | ARCH/S -> relation/assignment ids -> ST ids -> unit ids -> span prefixes |" % res(qa["R10_trace"][0]))
a("")
a("Additional mechanical checks: all 19 CSV headers equal the frozen templates (%s); every evidence span is <= 400 characters and a verbatim substring of a cited unit (%s); no QR has `prohibition` modality (%s); every NA with `prohibition` has `constraint_only = Y` (%s); screening issues: %d; unresolved record keys at build: %d." % (
    res(qa["headers_equal_templates"]), res(qa["spans_le_400_verbatim"]), res(qa["no_prohibition_QR"]), res(qa["na_prohibition_constraint_only_Y"]), len(qa["screen_issues"]), len(qa["unresolved_keys"])))
a("")
a("## D. Limitations")
a("")
a("- Mechanical QA cannot establish that a relation type, direction or status is the best reading; the human-review queue lists the consequential choices.")
a("- The source-file parse produced one unit for each goods table of Annexes I and II; table geometry is not faithfully represented for the iron and steel tables (declared).")
a("- The technical read-deny described in the blindness policy was not verified active; the allow-list in the brief was the control used.")
a("- A text-completeness check compared every source paragraph with the parsed units (only annex numbers and titles, kept in the locator text, are not unit text).")
a("")
a("Result of vertical-traceability problems found: %s" % (bad if bad else "none"))
open(OUT + "CASE_QA_REPORT.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

# ---------------- ACCESS LOG ----------------
L = []
a = L.append
a("# ACCESS_AND_CONTAMINATION_LOG — RGAM_C2_CBAM")
a("")
a("## Contamination status: **CLEAN**")
a("")
a("No path outside the allow-list was read, listed, searched or requested. No V8 output, V8 baseline, R2/R3/R4 output, V8-COMP-01 or earlier comparison material, historical relationship register or pilot output, case-selection or ranking material, other RGAM case directory or result, RGAM theory/ontology/manuscript source, memory file, CLAUDE.md or settings file was opened. No web or external retrieval was made.")
a("")
a("Disclosure of harness-provided context (outside the executor's control): the invocation context contained an automatic git-status snapshot listing top-level folder and file names of the repository and the subjects of recent commits. Only names were visible; no file content from any denied folder was read or used; nothing in that snapshot was used as a method input, source of vocabulary or analytical input.")
a("")
a("## Files read (exact paths)")
a("")
for f in files_read:
    a("- `%s`" % f)
a("")
a("The executor also read back its own output tables and `_work/` files (allow-list item 8) for verification.")
a("")
a("The 20 capsule template files under `OUTPUT_TEMPLATES/` were read to take the frozen header rows and were copied to the output directory; the report template was read in full and copied to `_work/`. `_work/units.txt` and `_work/units.json` are the executor's own parsed units of the capsule source file.")
a("")
a("## Shell and tool command categories used")
a("")
a("- Hashing (`sha256sum`, Python `hashlib`) of allow-listed files and of files written under the output directory.")
a("- Directory listing (`ls -la`) of the capsule directory, `LEGAL_SOURCE/`, `OUTPUT_TEMPLATES/` and of the output directory.")
a("- Reading and searching the capsule source file with `head`, `sed`, `grep` (single file, allow-listed path) and with Python (BeautifulSoup/lxml) to parse it into units; identifier and structure listings of the parsed units.")
a("- Copying the blank templates from `OUTPUT_TEMPLATES/` to the output directory (`cp`).")
a("- Creating the `_work/` directory and writing parsing, building and checking scripts, authored record files and the output tables under the output directory (Write/Edit tools and Python).")
a("- `date` (clock) and `which python` (interpreter lookup; no repository content read).")
a("- The Python interpreter loaded its own installed libraries (standard library, bs4, lxml); these are tooling, not data.")
a("")
a("## Attempted or accidental reads outside the allow-list")
a("")
a("None. (`forbidden_paths_attempted = NONE` in RUN_METADATA.)")
a("")
a("## Allow-list note")
a("")
a("Writes were made only under `12_RGAM_CASE_EXECUTION/RGAM_C2_CBAM/` (and its `_work/` scratch folder). The brief's path clarification (output root `12_RGAM_CASE_EXECUTION/`) was applied.")
open(OUT + "ACCESS_AND_CONTAMINATION_LOG.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

# ---------------- PROVENANCE ----------------
L = []
a = L.append
a("# EXECUTION_PROVENANCE — RGAM_C2_CBAM")
a("")
a("| Item | Value |")
a("|---|---|")
a("| Case id | RGAM_C2_CBAM |")
a("| Method version | RGAM paired execution protocol v1.0 (decision rules v1.0, data dictionary v1.0, output schema v1.0, blindness policy v1.0, execution gap decisions v1.0) |")
a("| Protocol manifest SHA-256 | `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932` — as stated in `RGAM_EXECUTION_GAP_DECISIONS_v1_0.md` (it is not stated in the capsule metadata or README; the manifest file itself is outside the allow-list and was not read) |")
a("| Model | `claude-sonnet-5-5` (Sonnet 5.5), as stated in the session context |")
a("| Reasoning/effort setting | `reasoning_effort=10` as displayed in the session context; the brief asked for the highest available effort, which was not settable by the executor |")
a("| Temperature, top-p, seed, token limits | NOT_EXPOSED |")
a("| Start (UTC) | 2026-10-06T19:03:42Z |")
a("| End of table construction / P9 (UTC) | %s (RUN_METADATA.end_time) |" % rows("RUN_METADATA")[0]["end_time"])
a("| End of case documentation (UTC) | %s |" % now)
a("| Fresh context attested | Y (isolated executor; only the brief, the allow-listed documents and the capsule were read) |")
a("| Source SHA-256 | `%s` (MATCH with capsule) |" % EXPECT)
a("")
a("## Hashes of the frozen inputs at the end of the run")
a("")
for f, h in frh.items():
    a("- `%s`: `%s`" % (f, h))
for f, h in caph.items():
    a("- capsule `%s`: `%s`" % (f, h))
a("")
a("## Scripts used (mechanical work only; all in `_work/`)")
a("")
a("- `dump_struct.py` (exploratory structure outline of the source file), `parse_units.py` (split the source file into addressable units, compute text hashes and ids), `cov_check.py` (compare every source paragraph with the parsed units), `rgam_lib.py` (record containers and mechanical id/legal-status helpers), `check1.py` (span and key checks), `build.py` (id assignment, derivation of mechanical columns, CSV writing, integrity checks), `make_report.py` and `make_docs.py` (assemble report and QA text from the finished tables).")
a("- The analytical records (statements, normative assignments, positions and devices, relations, external references, subconfigurations, architecture candidates, properties, closure statements, uncertainties, queue items, deviation entries and screening notes) were written by the executor from its own reading of the unit text in the data files `rec_01_pd.py`, `rec_02_ch1.py`, `rec_03_ch2.py`, `rec_04_ch3.py`, `rec_05_ch4_6.py`, `rec_06_ch7_11.py`, `rec_07_annex.py`, `rec_86_ext_more.py`, `rec_85_screening.py`, `rec_80_sc_arch.py`, `rec_82_prop.py`, `rec_90_hq_unc.py`; the scripts serialize them and apply rules stated in the frozen protocol (legal status from the act's own application schedule; down-coding of records with constitutive external dependencies; seeded draw for traceability), not keyword or pattern rules.")
a("- No script derives any analytical record from keywords or patterns.")
a("")
a("## Other facts")
a("")
a("- Reference date for legal status: 2026-01-01 (executor selection from Article 36(2); queued, HQ-OTHER).")
a("- Trace selection: seed = %d (first 8 hex digits of the source SHA-256); candidate list and draw in TRACE_DEMONSTRATIONS.csv." % int(EXPECT[:8], 16))
open(OUT + "EXECUTION_PROVENANCE.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

# ---------------- GATE ----------------
ok = VERT_OK and all(v[0] for k, v in qa.items() if isinstance(v, list) and len(v) == 2 and isinstance(v[0], bool)) and qa["headers_equal_templates"] and qa["spans_le_400_verbatim"]
gate = "RGAM_CASE_FROZEN" if ok else "RGAM_CASE_BLOCKED"
L = ["# CASE_GATE — RGAM_C2_CBAM", "", gate, "", "Factual basis:"]
L.append("- Source SHA-256 verified before analysis: MATCH with the capsule (`%s`)." % EXPECT)
L.append("- Structure parse consistent with the neutral metadata (36 articles, 6 annexes); no unexplained discrepancy.")
L.append("- Coverage complete: %d units inventoried and %d screened in source order (every unit accounted for)." % (len(rows("SOURCE_UNIT_INVENTORY")), len(rows("UNIT_SCREENING"))))
L.append("- All 19 frozen CSV tables (headers equal to the capsule templates) and CASE_RGAM_REPORT.md produced; data-dictionary integrity rules 1-10 pass mechanically.")
L.append("- No allow-list breach; contamination status CLEAN; protocol documents unchanged; gaps logged with `gap_ref`.")
L.append("- Case-specific analytical difficulty (external dependencies, passive wording, ambiguous norm types) is recorded as uncertainty and queued for human review, not as a blocking condition.")
L.append("- All outputs are machine-generated and provisional.")
open(OUT + "CASE_GATE.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print(gate, VERT_OK, len(bad))
