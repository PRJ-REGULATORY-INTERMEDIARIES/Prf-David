"""Generates (1) RGAM_PAIRED_DATA_DICTIONARY_v1_0.md from schema.py and (2) the four input-only execution capsules.

No legal text is opened or interpreted: source files are copied byte-for-byte and verified by SHA-256 only.
"""
import csv, hashlib, json, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FREEZE = os.path.dirname(HERE)
NT = os.path.dirname(FREEZE)
sys.path.insert(0, HERE)
import schema  # noqa: E402

# ------------------------------------------------------------------ data dictionary
lines = []
lines.append("# RGAM — PAIRED DATA DICTIONARY v1.0 (frozen before case execution)\n")
lines.append("Companion to `RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md` and `RGAM_PAIRED_DECISION_RULES_v1_0.md`. Generated from `TOOLS/schema.py` so that this dictionary, the output schema and the blank templates are identical in structure. **Case-general:** no field or vocabulary derives from any experimental legal text. Source tags: MS = manuscript v0.6.1 (controlling), ON = ontology v0.4 rev3 (subordinate), TPL = template rules v1.2 (procedural only).\n")
lines.append("## 1. Conventions\n")
lines.append("- All outputs are CSV (UTF-8 with BOM), one file per table, header row exactly as listed below; list-valued cells use `;` as separator; empty cells are blank, never `NA` unless an enumeration lists it.")
lines.append("- All machine-generated records are provisional (`machine_provisional`). Human-only columns exist only in HUMAN_REVIEW_QUEUE and must stay blank.")
lines.append("- Unit ids: `<case_id>.A{n}.P{k}` (paragraph), `…pt{x}` (point), `.P0` (single-paragraph article), `<case_id>.ANX{n}.pt{x}` (annex point), `<case_id>.REC{n}` (recital). Record ids: `ST-nnnn`, `NA-nnnn`, `PD-nnn`, `QR-nnnn`, `EXT-nnn`, `SC-nn`, `ARCH-nn`, `PROP-nnn`, `CL-nn`, `UNC-nnn`, `HQ-nnn`, `LNK-nnnnn`, `TR-nn`, `DEV-nn`, `RUN-nn`.")
lines.append("- Evidence spans are verbatim minimal spans (≤ 400 characters) from the unit; no paraphrase in an `evidence_span` column.")
lines.append("- Counts recorded in any table are evidence descriptors only; no table defines a score, index, threshold or ranking.\n")
lines.append("## 2. Controlled vocabularies\n")
lines.append("| Vocabulary | Values and source |\n|---|---|")
for k, v in schema.ENUMS.items():
    lines.append(f"| `{k}` | {v} |")
lines.append("")
lines.append("Additional fixed vocabularies are given inline in the field tables (e.g., `ACCOUNTABILITY` classes, `ARCH.outcome`). Instrument-level result tokens: `NO_ARCHITECTURE_WARRANTED`, `ONE_ARCHITECTURE`, `SEVERAL_DISTINGUISHABLE`, `OVERLAPPING_OR_PARTIALLY_INTEGRATED`, `INDETERMINATE`. Claim-status ceilings from legal text: `documented`, `legal_constitution_evidenced`; `material_establishment_evidenced` and `exercise_evidenced` are not collected (`not_assessed`).\n")
lines.append("## 3. Tables\n")
lines.append("| # | File | Stratum | Purpose |\n|---:|---|---|---|")
for i, t in enumerate(schema.TABLES, 1):
    lines.append(f"| {i} | `{t['file']}` | {t['stratum']} | {t['purpose']} |")
lines.append("")
for i, t in enumerate(schema.TABLES, 1):
    lines.append(f"### 3.{i} `{t['file']}` — {t['name']} (stratum {t['stratum']})\n")
    lines.append(t["purpose"] + "\n")
    lines.append("| Field | Definition | Allowed values / format |\n|---|---|---|")
    for f, d, a in t["fields"]:
        lines.append(f"| `{f}` | {d} | {a} |")
    lines.append("")
lines.append("## 4. Referential-integrity rules (checked by the executor at P9 and by any later validator)\n")
lines += [
    "1. Every `unit_id` in any table exists in SOURCE_UNIT_INVENTORY; `units_screened` = `units_total` in INSTRUMENT_LEVEL_SUMMARY.",
    "2. Every NA, PD, QR, EXT cites ≥1 `ST` id, and every `ST` cites ≥1 unit; a statement with `recital_only = Y` has no derived NA/PD/QR.",
    "3. Every `*_ids` and `*_pd_id` field resolves to an existing record; `accountable_via_qr_ids` resolve to QR records of type `accountability`.",
    "4. Every QR has non-empty `origin_pd_id` and `counterpart_pd_id`, modality ≠ prohibition, and no `material_establishment_evidenced` status.",
    "5. Every NA/QR/SC/ARCH/PROP record has ≥1 row in PROVENANCE_LINKS; every derived record states `derivation_rule` and cites ≥2 units or an explicit cross-reference.",
    "6. Every `ARCH` with `outcome` INTEGRATED or OVERLAPPING_OR_PARTIALLY_INTEGRATED has an HQ item; no `ARCH` outcome is INTEGRATED unless `i1`–`i4` statuses are all SATISFIED.",
    "7. Every `PROP` with `closure_dependency = Y` has a `closure_ref` resolving to CLOSURE_REGISTER; a closure result `UNDETERMINED` forces `PROP.status = undetermined`.",
    "8. Every EXT has `source_verification_status = not_checked` and, unless a boundary decision is recorded, `boundary_status = outside_corpus_not_expanded`.",
    "9. HUMAN_REVIEW_QUEUE columns `human_decision`, `human_rationale`, `decided_by`, `decision_date` are blank.",
    "10. `TRACE_DEMONSTRATIONS.vertical_chain` resolves, step by step, to existing ids down to a unit and an evidence span.",
]
with open(os.path.join(FREEZE, "RGAM_PAIRED_DATA_DICTIONARY_v1_0.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

# ------------------------------------------------------------------ capsules
REG = os.path.join(NT, "08_STRICT_AI_PREPARATION", "FINAL_COMMON_EXECUTION_CORPUS_REGISTER.csv")
rows = list(csv.DictReader(open(REG, encoding="utf-8-sig", newline="")))
BY_CASE = {r["case_id"]: r for r in rows}
CAPS = [
    ("RGAM_C1_SCF", "CASE-32023R0955"),
    ("RGAM_C2_CBAM", "CASE-32023R0956"),
    ("RGAM_AI_AI_ACT", "CASE-32024R1689"),
    ("RGAM_O_DIR_86_361", "CASE-31986L0361"),
]


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for ch in iter(lambda: fh.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()


PROTO_FILES = ["RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md", "RGAM_PAIRED_DATA_DICTIONARY_v1_0.md", "RGAM_PAIRED_DECISION_RULES_v1_0.md", "RGAM_CASE_OUTPUT_SCHEMA.md", "RGAM_BLINDNESS_AND_ACCESS_POLICY.md"]
reg_rows = []
for cap_id, case in CAPS:
    r = BY_CASE[case]
    cdir = os.path.join(FREEZE, "CAPSULES", cap_id)
    os.makedirs(os.path.join(cdir, "LEGAL_SOURCE"), exist_ok=True)
    os.makedirs(os.path.join(cdir, "OUTPUT_TEMPLATES"), exist_ok=True)
    src = os.path.join(NT, r["local_source_path"].replace("/", os.sep))
    assert os.path.isfile(src), src
    dst = os.path.join(cdir, "LEGAL_SOURCE", os.path.basename(src))
    shutil.copyfile(src, dst)
    h_src, h_dst = sha(src), sha(dst)
    expected = r["source_sha256"].lower()
    assert h_src == expected == h_dst, (cap_id, h_src, expected, h_dst)
    meta = dict(
        capsule_id=cap_id, instrument_title=r["instrument"], celex=r["celex"], language=r["language"],
        version_and_scope=r["source_date_and_scope"], official_source_url=r["official_source_url"],
        corpus_scope=r["corpus_scope"], article_count_metadata=int(r["article_count"]), annex_count_metadata=int(r["annex_count"]),
        controlling_source_file="LEGAL_SOURCE/" + os.path.basename(src), source_sha256=expected,
        corpus_register_status=r["completeness_status"],
    )
    if case == "CASE-31986L0361":
        meta["temporal_note"] = "Historical original act; later repealed (1992); no successor act is substituted."
    json.dump(meta, open(os.path.join(cdir, "CASE_METADATA.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    for t in schema.TABLES:
        with open(os.path.join(cdir, "OUTPUT_TEMPLATES", t["file"]), "w", encoding="utf-8-sig", newline="") as fh:
            csv.writer(fh).writerow([f[0] for f in t["fields"]])
    with open(os.path.join(cdir, "OUTPUT_TEMPLATES", "CASE_RGAM_REPORT_TEMPLATE.md"), "w", encoding="utf-8") as fh:
        fh.write("# CASE_RGAM_REPORT — " + cap_id + " (blank template; machine-generated and provisional)\n\n"
                 "## 1. W declaration and coverage\n\n## 2. Record counts by table (evidence descriptors only)\n\n## 3. Subconfigurations and warrants\n\n"
                 "## 4. Candidate architectures: I1–I4, rival groupings, outcomes\n\n## 5. Property register summary (scale, bearer, aggregation)\n\n"
                 "## 6. Status profile\n\n## 7. Closure and external-reference limitations\n\n## 8. Open human-review items\n\n## 9. Deviations and gaps\n\n"
                 "## 10. Statement of provisional status (no comparison with any other method or case)\n")
    with open(os.path.join(cdir, "CAPSULE_README.md"), "w", encoding="utf-8") as fh:
        fh.write(f"""# Execution capsule {cap_id} — INPUT ONLY (no analytical field populated)

**Status:** frozen input. Do not execute until separately authorized.

## Allowed reads (strict allow-list)
1. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md`
2. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DECISION_RULES_v1_0.md`
3. `11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`
4. `11_RGAM_PROTOCOL_FREEZE/RGAM_CASE_OUTPUT_SCHEMA.md`
5. `11_RGAM_PROTOCOL_FREEZE/RGAM_BLINDNESS_AND_ACCESS_POLICY.md`
6. This capsule directory only: `CASE_METADATA.json`, `LEGAL_SOURCE/{os.path.basename(src)}`, `OUTPUT_TEMPLATES/`.

## Allowed writes
`12_RGAM_EXECUTION/{cap_id}/` only (copy the blank templates there and fill the machine columns).

## Source verification
Expected SHA-256 of the controlling legal source: `{expected}` (identical to the hash designated for the V8 arm in `08_STRICT_AI_PREPARATION/FINAL_COMMON_EVIDENCE_EQUALITY_CHECK.csv`). Verify before analysis; stop on mismatch (RGAM-DR-03).

## Not provided and not to be read
Any V8 output, count or conclusion; any R2/R3/R4 or historical relationship extraction; case-selection rankings; results of any other RGAM case; `09_V8_BASELINE_EXECUTION/`; `RGAM/V8_ACTIVE/`; any other directory of the repository.
""")
    reg_rows.append(dict(
        capsule_id=cap_id, case_id=case, instrument=r["instrument"], celex=r["celex"],
        original_source_path="NEW TEST 3x3/" + r["local_source_path"], capsule_source_path=f"11_RGAM_PROTOCOL_FREEZE/CAPSULES/{cap_id}/LEGAL_SOURCE/{os.path.basename(src)}",
        sha256_register_expected=expected, sha256_original_recomputed=h_src, sha256_capsule_copy=h_dst, hash_equal_all_three="YES",
        v8_rgam_equality_status="EQUAL_AT_COMMON_CORPUS_LEVEL (designation in FINAL_COMMON_EVIDENCE_EQUALITY_CHECK.csv; actual V8 consumption not verified because 09_V8_BASELINE_EXECUTION was not opened)",
        corpus_scope=r["corpus_scope"], article_count_metadata=r["article_count"], annex_count_metadata=r["annex_count"], completeness_status=r["completeness_status"],
        protocol_files_referenced=" | ".join(PROTO_FILES), output_templates_dir=f"11_RGAM_PROTOCOL_FREEZE/CAPSULES/{cap_id}/OUTPUT_TEMPLATES",
        output_templates_count=len(schema.TABLES) + 1, analytical_fields_populated="NO", planned_output_dir=f"12_RGAM_EXECUTION/{cap_id}/",
        execution_order=len(reg_rows) + 1, capsule_status="INPUT_READY_NOT_EXECUTED"))

cols = list(reg_rows[0].keys())
with open(os.path.join(FREEZE, "RGAM_EXECUTION_CAPSULE_REGISTER.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in reg_rows:
        w.writerow(r)
print("dictionary + 4 capsules written; tables:", len(schema.TABLES))
