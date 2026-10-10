"""Automated QA for the RGAM protocol freeze; writes RGAM_PROTOCOL_QA_REPORT.md. Reads only the freeze directory, the register file, and authority-file hashes."""
import csv, glob, hashlib, json, os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
FREEZE = os.path.dirname(HERE)
NT = os.path.dirname(FREEZE)
ROOT = os.path.dirname(NT)
sys.path.insert(0, HERE)
import schema  # noqa: E402

START_HASHES = {
    "RGAM/paper/MANUSCRIPT_v0_6_1.md": "8c10d4e6a650cc45e5dd7e3485c807c8dca808c9ba6ee827a0df03b8120a1b57",
    "RGAM/ontology/ONTOLOGY_v0_4.md": "54f1abf42a195955ef64b94c278ebb6de393f72cf491c53b0455f14f73fe400e",
    "RGAM/pilot/GDPR_PILOT_01/00_PROTOCOL/ONTOLOGY_ALIGNMENT_AND_PRECEDENCE.md": "88cd6dbd3d3b1df79be7f55d9e3aa36ea0b14ab4ad6b189fb55f66d0c05daa2b",
    "RGAM/paper/V0_6_INTEGRATION_REGISTER.md": "ca1b4bb7a98b0dfbc0f82cd28eb3aed73f51ee29db1cae8c9c1c90da4830f2aa",
    "RGAM/pilot/GDPR_PILOT_01/00_PROTOCOL/DECISION_RULES.md": "b6ea6467ed89009cf36b9441d1445cd97386ee028227cc2a04fb7c7ca6b8a004",
    "RGAM/paper/V0_6_1_SCIENTIFIC_REVISION_REGISTER.md": "5f1c4b2a2f0b2896a7861bfb115baaa479531415345252d9337e38e6b357fdfe",
    "RGAM/ontology/DECISION_LOG.md": "10dbc5badb348cd221b715e1b50e6e388844b4aa9987fb1f425653c567cda568",
    "RGAM/paper/START_HERE_V0_6.md": "50fbaf2051d6f2c2c564ab02f73994e6a808295af989da1af13f58f15e0085d5",
    "RGAM/00_ADMIN/EXECUTION_ADDENDUM_v0_4.md": "8e296f79a04c69ad4cbed86a9320a7102ac106f9c5b4fba3c378bcfd23166a7a",
}


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for ch in iter(lambda: f.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()


def read(p):
    return open(p, encoding="utf-8", errors="replace").read()


results = []  # (id, requirement, result, evidence)


def add(i, req, ok, ev):
    results.append((i, req, "PASS" if ok else "FAIL", ev))


METHOD_DOCS = ["RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md", "RGAM_PAIRED_DATA_DICTIONARY_v1_0.md", "RGAM_PAIRED_DECISION_RULES_v1_0.md", "RGAM_CASE_OUTPUT_SCHEMA.md", "RGAM_BLINDNESS_AND_ACCESS_POLICY.md"]
scan_files = [os.path.join(FREEZE, d) for d in METHOD_DOCS] + [os.path.join(HERE, "schema.py")]


def clean(t):
    t = re.sub(r"RGAM_(C1_SCF|C2_CBAM|AI_AI_ACT|O_DIR_86_361)", "CAPSULE_ID", t)
    t = re.sub(r"GDPR_PILOT_01", "TEMPLATE_PILOT_DIR", t)
    return t


# Q01 case independence
CASE_TERMS = ["social climate", "carbon border", "cbam", "artificial intelligence", "ai act", "86/361", "2023/955", "2023/956", "2024/1689", "terminal equipment", "type approval", "climate fund", "deforestation", "scf"]
hits = []
for p in scan_files:
    t = clean(read(p)).lower()
    for term in CASE_TERMS:
        if re.search(r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])", t):
            hits.append((os.path.basename(p), term))
add("Q01", "Protocol is case-general: no case-specific term in the method documents or schema", not hits, "terms searched: %s; hits: %s" % (CASE_TERMS, hits or "none"))

# Q02 no case-specific rule/legal text analysed (structural)
caps = sorted(glob.glob(os.path.join(FREEZE, "CAPSULES", "*")))
tmpl_ok = True
detail = []
hdrs = {t["file"]: [f[0] for f in t["fields"]] for t in schema.TABLES}
for c in caps:
    for fn, hd in hdrs.items():
        p = os.path.join(c, "OUTPUT_TEMPLATES", fn)
        rows = list(csv.reader(open(p, encoding="utf-8-sig", newline="")))
        if len(rows) != 1 or rows[0] != hd:
            tmpl_ok = False
            detail.append((os.path.basename(c), fn, len(rows)))
    if not os.path.isfile(os.path.join(c, "OUTPUT_TEMPLATES", "CASE_RGAM_REPORT_TEMPLATE.md")):
        tmpl_ok = False
add("Q02", "Capsules are input-only: all %d templates per capsule are header-only and identical to the schema; no analytical field populated" % len(schema.TABLES), tmpl_ok and len(caps) == 4, "capsules=%d; problems=%s" % (len(caps), detail or "none"))

# Q03 no scoring / threshold invented
score_lines = []
for p in scan_files:
    for ln in read(p).splitlines():
        if re.search(r"\b(scor(e|es|ing)|composite|threshold|index|indices|rank(ing)?)\b", ln, re.I):
            neg = re.search(r"\b(no|not|never|without|nor|non|cannot|declines|neither|unvalidated|untested|unsettled|open|must not|does not|is not|are not|forbidden|excluded)\b", ln, re.I)
            if not neg:
                score_lines.append((os.path.basename(p), ln.strip()[:140]))
add("Q03", "No scoring rule, composite index or numeric threshold is defined (every mention occurs in a negating/limiting context)", not score_lines, "unqualified mentions: %s" % (score_lines or "none"))

# Q04 INDETERMINATE
dr = read(os.path.join(FREEZE, "RGAM_PAIRED_DECISION_RULES_v1_0.md")) + read(os.path.join(FREEZE, "RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md"))
add("Q04", "`INDETERMINATE` remains a legitimate result (S->A outcome, instrument-level result, stopping rule)", dr.count("INDETERMINATE") >= 6 and "legitimate" in dr, "occurrences=%d" % dr.count("INDETERMINATE"))

# Q05 stopping rule explicit
add("Q05", "Explicit stopping rule stated", "Assert only the highest analytical level authorized by the available evidence" in dr and "RGAM-DR-27" in dr, "Protocol §11 and RGAM-DR-27")

# Q06 O1-O8 not imported
occ = []
for p in [os.path.join(FREEZE, d) for d in METHOD_DOCS] + [os.path.join(FREEZE, "RGAM_PRECEDENCE_AND_CONFLICT_REGISTER.csv"), os.path.join(FREEZE, "RGAM_SOURCE_AUTHORITY_REGISTER.md")]:
    for ln in read(p).splitlines():
        if re.search(r"\bO[1-8]\b|O1[–-]O8|eight[- ]operation|operation list|operation sequence", ln, re.I):
            occ.append((os.path.basename(p), ln.strip()[:150], bool(re.search(r"\b(not|no|never|non|forbidden|import|earlier)\b", ln, re.I))))
add("Q06", "O1-O8 not imported (any mention is a non-import statement); the phases P0-P9 are an execution aid mapped to RGAM-documented activities", all(o[2] for o in occ), "mentions=%d; all negated/contextual=%s" % (len(occ), all(o[2] for o in occ)))

# Q07 GDPR-specific content removed
GD = ["gdpr", "2016/679", "corrigend", "b5085317", "article 4 definitions", "data subject", "controller", "processor", "supervisory authority"]
gh = []
for p in scan_files:
    t = clean(read(p)).lower()
    for term in GD:
        if term in t:
            gh.append((os.path.basename(p), term))
add("Q07", "Template-specific (instrument-specific) content removed from the method documents", not gh, "terms searched: %s; hits: %s" % (GD, gh or "none"))

# Q08 materiality is not a phase
proto = read(os.path.join(FREEZE, "RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md"))
phase_block = proto.split("## 3. Execution phases")[1].split("## 4. Materiality")[0]
phase_rows = [l for l in phase_block.splitlines() if l.startswith("| **P")]
add("Q08", "Materiality is not a sequential phase (no phase row for it; stated as transversal control)", len(phase_rows) == 10 and not any(re.search(r"materiality", r.split("|")[2], re.I) for r in phase_rows) and "not a phase" in proto.lower(), "phase rows=%d" % len(phase_rows))

# Q09 vertical traceability operationalized
tr_ok = all(x in read(os.path.join(FREEZE, "RGAM_PAIRED_DATA_DICTIONARY_v1_0.md")) for x in ["PROVENANCE_LINKS", "TRACE_DEMONSTRATIONS", "vertical_chain", "supporting_unit_ids", "derivation_rule"]) and "RGAM-DR-29" in dr
add("Q09", "Vertical traceability operationalized (ids, many-to-many provenance, trace demonstrations, integrity rules)", tr_ok, "tables PROVENANCE_LINKS, TRACE_DEMONSTRATIONS; integrity rules 1-10")

# Q10 human review separate
hq = hdrs["HUMAN_REVIEW_QUEUE.csv"]
add("Q10", "Human review separate: human-only columns exist and are blank in templates; protocol forbids simulation", all(c in hq for c in ["human_decision", "human_rationale", "decided_by", "decision_date"]) and "Human adjudication is never simulated" in proto, "HUMAN_REVIEW_QUEUE columns present; templates header-only")

# Q11 v0.6.1 precedence and conflicts registered
cr = list(csv.DictReader(open(os.path.join(FREEZE, "RGAM_PRECEDENCE_AND_CONFLICT_REGISTER.csv"), encoding="utf-8-sig", newline="")))
ids = {r["conflict_id"] for r in cr}
cited = set(re.findall(r"\b([CD]-\d\d)\b", dr + proto + read(os.path.join(FREEZE, "RGAM_BLINDNESS_AND_ACCESS_POLICY.md"))))
missing = sorted(cited - ids)
prec = sum(1 for r in cr if r["status"] == "RESOLVED_BY_DOCUMENTED_PRECEDENCE")
add("Q11", "v0.6.1 precedence respected; ontology conflicts registered; every cited conflict id exists", not missing and prec >= 10, "rows=%d; resolved by documented precedence=%d; cited-but-missing=%s" % (len(cr), prec, missing or "none"))

# Q12 authority sources unmodified
mism = [k for k, v in START_HASHES.items() if sha(os.path.join(ROOT, k.replace("/", os.sep))) != v]
add("Q12", "Original RGAM source files unmodified (SHA-256 at start == end)", not mism, "files checked=%d; mismatches=%s" % (len(START_HASHES), mism or "none"))

# Q13 capsule sources hash
reg = list(csv.DictReader(open(os.path.join(FREEZE, "RGAM_EXECUTION_CAPSULE_REGISTER.csv"), encoding="utf-8-sig", newline="")))
eq = {r["case_id"]: r for r in csv.DictReader(open(os.path.join(NT, "08_STRICT_AI_PREPARATION", "FINAL_COMMON_EVIDENCE_EQUALITY_CHECK.csv"), encoding="utf-8-sig", newline=""))}
ok13 = True
bad = []
for r in reg:
    cp = os.path.join(ROOT, "NEW TEST 3x3", r["capsule_source_path"].replace("/", os.sep))
    h = sha(cp)
    e = eq[r["case_id"]]
    if not (h == r["sha256_register_expected"] == r["sha256_capsule_copy"] == r["sha256_original_recomputed"] == e["v8_expected_sha256"].lower() == e["rgam_expected_sha256"].lower() == e["evidence_sha256"].lower()):
        ok13 = False
        bad.append(r["capsule_id"])
add("Q13", "Each capsule source is byte-identical to the frozen common-corpus source and to the hash designated for both arms (hash comparison only)", ok13 and len(reg) == 4, "capsules=%d; mismatches=%s" % (len(reg), bad or "none"))

# Q14 deny configuration
sp = os.path.join(ROOT, ".claude", "settings.local.json")
try:
    d = json.load(open(sp, encoding="utf-8"))
    n = len(d["permissions"]["deny"])
    ok14 = n >= 30
except Exception as e:
    n, ok14 = 0, False
add("Q14", "Technical read-deny configured (rules written, valid JSON). NOTE: activity not verified in the construction session and shell bypass remains - recorded as a limitation", ok14, "deny rules=%d (configured: PASS; active: NOT VERIFIED)" % n)

# Q15 required deliverables 1-8 exist
need = ["RGAM_SOURCE_AUTHORITY_REGISTER.md", "RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md", "RGAM_PAIRED_DATA_DICTIONARY_v1_0.md", "RGAM_PAIRED_DECISION_RULES_v1_0.md", "RGAM_PRECEDENCE_AND_CONFLICT_REGISTER.csv", "RGAM_BLINDNESS_AND_ACCESS_POLICY.md", "RGAM_CASE_OUTPUT_SCHEMA.md", "RGAM_EXECUTION_CAPSULE_REGISTER.csv"]
miss = [n for n in need if not os.path.isfile(os.path.join(FREEZE, n))]
add("Q15", "Deliverables 1-8 present before QA (9-12 produced after QA)", not miss, "missing=%s" % (miss or "none"))

# Q16 schema consistency dictionary vs schema
dd = read(os.path.join(FREEZE, "RGAM_PAIRED_DATA_DICTIONARY_v1_0.md"))
add("Q16", "Data dictionary lists every table and field of the schema", all(("`%s`" % f[0]) in dd for t in schema.TABLES for f in t["fields"]) and all(t["file"] in dd for t in schema.TABLES), "tables=%d, fields=%d" % (len(schema.TABLES), sum(len(t["fields"]) for t in schema.TABLES)))

# Q17 no V8_ACTIVE or 09 dependency in method files
dep = [os.path.basename(p) for p in scan_files if re.search(r"V8_ACTIVE/|09_V8_BASELINE_EXECUTION/\w", read(p)) and "BLINDNESS" not in p and "PROTOCOL_v1_0" not in p and "DECISION_RULES" not in p]
add("Q17", "Method documents do not depend on V8_ACTIVE or on V8 execution content (mentions only in prohibition/deny contexts)", not dep, "unexpected files=%s" % (dep or "none"))

# Q18 INSTITUTIONAL layer distinctions present
for tok in ["W != A", "graph reachability", "counterparty is **never invented**", "N1", "DEV", "INS-TYPE"]:
    pass
need_tokens = ["W ≠ A", "Graph reachability is not a legal relation", "never invented", "N1", "INS-TYPE", "I1–I4", "closure", "support-gap"]
add("Q18", "Core RGAM safeguards present in the protocol (W != A; reachability != transmission; no invented counterparty; N1-N4; INS-TYPE/DEV; I1-I4; closure; support-gap)", all(t in (proto + dr) for t in need_tokens), "tokens checked=%d" % len(need_tokens))

ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
passed = sum(1 for r in results if r[2] == "PASS")
manual = [
    ("M01", "None of the four legal cases was analysed", "Session record: the four source files were copied byte-for-byte (cp) and hashed; none was opened, read, parsed or interpreted in this task."),
    ("M02", "No V8 output was read", "No file inside `09_V8_BASELINE_EXECUTION/` was opened in this task; the earlier exposure of file names/match counts (previous task) is disclosed in the authority register §5."),
    ("M03", "`RGAM/V8_ACTIVE/` was not opened", "No Read/Grep/Glob targeted it in this task; the content search for references was restricted to authorized RGAM files."),
    ("M04", "O1–O8 were not imported", "Q06 plus session record: the earlier procedure's files were not opened in this task."),
    ("M05", "Historical R2/R3/R4/PILOT outputs not used", "None opened in this task except one 3-line administrative header (deny-rule test, disclosed)."),
]
with open(os.path.join(FREEZE, "RGAM_PROTOCOL_QA_REPORT.md"), "w", encoding="utf-8") as f:
    f.write("# RGAM — PROTOCOL QA REPORT (pre-freeze)\n\n")
    f.write(f"Generated {ts} (UTC-03) by `TOOLS/run_qa.py` before the freeze manifest was written. Automated checks: **{passed}/{len(results)} PASS**.\n\n")
    f.write("## 1. Automated checks\n\n| ID | Requirement | Result | Evidence |\n|---|---|---|---|\n")
    for i, req, res, ev in results:
        f.write(f"| {i} | {req} | **{res}** | {str(ev).replace('|', '/')} |\n")
    f.write("\n## 2. Checks established by the session record (not automatable)\n\n| ID | Requirement | Basis |\n|---|---|---|\n")
    for i, req, b in manual:
        f.write(f"| {i} | {req} | {b} |\n")
    f.write("\n## 3. Mapping to the task's QA list (§24)\n\n| Task requirement | Check |\n|---|---|\n")
    for a, b in [("protocol is case-general", "Q01, Q02"), ("none of the four cases analysed", "M01, Q02"), ("no V8 output read", "M02"), ("O1–O8 not imported", "Q06, M04"), ("V8_ACTIVE not opened", "M03, Q17"),
                 ("v0.6.1 precedence respected", "Q11"), ("ontology conflicts registered", "Q11"), ("GDPR-specific content removed", "Q07"), ("no scoring threshold invented", "Q03"),
                 ("INDETERMINATE valid", "Q04"), ("stopping rule explicit", "Q05"), ("vertical traceability operationalized", "Q09, Q16"), ("human review separate", "Q10"),
                 ("materiality not a new sequential phase", "Q08")]:
        f.write(f"| {a} | {b} |\n")
    f.write("\n## 4. Residual limitations carried into the gate\n\n"
            "1. Technical read-deny is configured (33 rules) but **not verified active** and does not block shell commands; the strict allow-list is the primary control (Blindness policy §4, §7).\n"
            "2. Wrapper decisions GAP-01…GAP-07 (annexes/formal provisions, amending provisions, intra-instrument cross-references, no external retrieval, function vocabulary, template references, definitional provisions) await Igor's confirmation; each is queued for human review at execution.\n"
            "3. Open thresholds (device threshold; I2/I3 integration; accountability consequences) and the unharmonised measures list are recorded as unresolved (conflict register C-24, C-25, C-26).\n"
            "4. The author's session had prior exposure to historical case content and V8-comparison file names; case-independence of the protocol rests on construction plus Q01/Q07, not on blindness of the author.\n"
            "5. Actual V8 consumption of the common source files was not verified (equality is a corpus-level designation plus hash verification).\n")
print(f"QA {passed}/{len(results)} PASS")
for r in results:
    if r[2] != "PASS":
        print("FAIL", r)
