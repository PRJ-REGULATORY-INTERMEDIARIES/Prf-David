"""R01 — Source register, baseline hashes and derived text extraction (read-only on sources)."""
import datetime as dt
import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, PROJECT_ROOT, sha256, write_csv, rel_to_project, now_iso  # noqa: E402

DL = Path("C:/Users/Adm/Downloads")
P = PROJECT_ROOT
R3 = P / "R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM"
PIL = P / "RELATIONAL_LEXIMETRICS_PILOT"
ENV = P / "ENVIO_R4_TO_DAVID"
R4 = P / "R4_CROSS_DOMAIN_VALIDATION"

# (SOURCE_ID, path or glob, category, role, schema_layer, source_status)
SOURCES = [
    # --- Rotem / conceptual sources
    ("SRC-ROTEM-EMAIL", P / "Enviados/30_09_26/email e chat", "CORRESPONDENCE", "Rotem reply (lines 1-20) + AI analysis + AI-drafted reply from Igor (lines 22-440)", "LAYER_1_CONCEPTUAL", "PRIMARY_ROTEM_TEXT_LINES_1_20"),
    ("SRC-CB-UNREV", DL / "Codebook - Regulatory Intermediation (1).docx", "CODEBOOK", "Codebook, unrevised version (with embedded review commentary)", "LAYER_2_DOCUMENTED", "UNREVISED_BASELINE"),
    ("SRC-CHARTKEY", DL / "Chart Key - Regulatory Intermediation (2).docx", "CODEBOOK", "Chart Key companion to the codebook", "LAYER_2_DOCUMENTED", "UNREVISED_BASELINE"),
    ("SRC-CB-REV", PIL / "PILOT_01/00_SOURCES/Codebook_Regulatory_Intermediation_Revised (1).docx", "CODEBOOK", "Codebook, file labelled 'Revised' (project copy)", "LAYER_2_DOCUMENTED", "REVISED_BY_FILENAME_AND_CONTENT"),
    ("SRC-CB-REV-DL", DL / "Codebook_Regulatory_Intermediation_Revised (1).docx", "CODEBOOK", "Same file as SRC-CB-REV (Downloads origin)", "LAYER_2_DOCUMENTED", "DUPLICATE_CHECK"),
    ("SRC-WB", PIL / "PILOT_01/00_SOURCES/dataset_of_EU_regulatory_intermediation.xlsx", "WORKBOOK", "Rotem workbook (implemented coding)", "LAYER_3_IMPLEMENTED", "IMPLEMENTED_SCHEMA"),
    ("SRC-WB-DL", DL / "dataset_of_EU_regulatory_intermediation.xlsx", "WORKBOOK", "Same workbook (Downloads origin)", "LAYER_3_IMPLEMENTED", "DUPLICATE_CHECK"),
    ("SRC-DAVID-MS", PIL / "PILOT_01/00_SOURCES/v1 Law_and_Governance_Architectures_Revised.docx", "MANUSCRIPT", "David Levi-Faur manuscript (context only)", "CONTEXT", "CONTEXT_ONLY"),
    ("SRC-KOSTI", PIL / "PILOT_01/00_SOURCES/seidl-kosti-paper-4-with-appendix.pdf", "ARTICLE", "Seidl & Kosti, Mapping Europe's Digital Acquis (context only)", "CONTEXT", "CONTEXT_ONLY"),
    ("SRC-P01-INV", PIL / "PILOT_01/00_SOURCES/SOURCE_INVENTORY.md", "INVENTORY", "PILOT_01 source inventory with hashes", "HISTORY", "HISTORICAL"),
    ("SRC-MEETING-DEC", DL / "regulatory-intermediation-meeting-decisions.txt", "CORRESPONDENCE", "Meeting decisions template (12 Sep)", "HISTORY", "HISTORICAL"),
    # --- History R1/R2/R2.1
    ("SRC-R1-REPORT", DL / "EU_green_regulatory_intermediation_method_progress_report_REVISED.docx", "REPORT", "R1 method progress report (REVISED)", "HISTORY_R1", "HISTORICAL"),
    ("SRC-R1-REPORT-ORIG", DL / "EU_green_regulatory_intermediation_method_progress_report.docx", "REPORT", "R1 report (earlier version)", "HISTORY_R1", "HISTORICAL_VERSION"),
    ("SRC-R1-REPORT-REV1", DL / "EU_green_regulatory_intermediation_method_progress_report_REVISED (1).docx", "REPORT", "R1 report (REVISED (1) variant)", "HISTORY_R1", "HISTORICAL_VERSION"),
    ("SRC-LEARNLOG", DL / "PROJECT_LEARNING_LOG_PRJ_DAVID_LEVI_FAUR.md", "LOG", "Project learning log (R2 corpus lock, TEXTS_VERIFIED)", "HISTORY_R2", "HISTORICAL"),
    ("SRC-MASTERCTX", DL / "PROJECT_MASTER_CONTEXT_DAVID_LEVI_FAUR.md", "LOG", "Project master context", "HISTORY", "HISTORICAL"),
    ("SRC-R2-REPORT", DL / "R2_METHOD_REPORT_TAXONOMY_CALIBRATION_v1_2.docx", "REPORT", "R2 Taxonomy calibration method report", "HISTORY_R2", "HISTORICAL"),
    ("SRC-R2-XLSX-AUD", DL / "R2_calibration_regulatory_intermediation_v1_2_audited.xlsx", "DATASET", "R2 calibration workbook (audited)", "HISTORY_R2", "HISTORICAL"),
    ("SRC-R2-PKG", DL / "R2_DAVID_VALIDATION_PACKAGE_v1_3.zip", "PACKAGE", "R2 David validation package v1.3", "HISTORY_R2", "HISTORICAL"),
    ("SRC-R21-DECLOG", P / "WORK_2_1/PILOT_R2_1/RESEARCHER_DECISION_LOG.md", "LOG", "R2.1 researcher decision log", "HISTORY_R2_1", "HISTORICAL"),
    ("SRC-R21-P0", P / "WORK_2_1/PILOT_R2_1/PHASE_0_AUDIT_REPORT.md", "REPORT", "R2.1 Phase 0 audit", "HISTORY_R2_1", "HISTORICAL"),
    ("SRC-PROTO-IA", R4 / "00_protocol/PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx", "PROTOCOL", "Protocol defining R1/R2/R3", "HISTORY", "HISTORICAL"),
    ("SRC-R2-NOTES", P / "Post_R2/R2_notes/Resumos IA", "NOTES", "AI meeting summaries (Post R2)", "HISTORY_R2", "HISTORICAL"),
    # --- R3
    ("SRC-R3-RELADJ", R3 / "06_relations/RELATIONS_ADJUDICATED.csv", "DATASET", "R3 adjudicated relations (post-6B)", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-TESTMAT", R3 / "06_relations/INTERMEDIATION_TEST_MATRIX.csv", "DATASET", "R3 intermediation test matrix", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-LIREG", R3 / "05_law_intermediary/LAW_INTERMEDIARY_REGISTER.csv", "DATASET", "R3 LAW x INTERMEDIARY register", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-MECH", R3 / "07_mechanisms/MECHANISM_EVENTS_RESEARCHER_ADJUDICATED.csv", "DATASET", "R3 mechanism events (researcher adjudicated)", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-ACTORS", R3 / "04_actor_register/ACTOR_REGISTER.csv", "DATASET", "R3 actor register", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-DECDOC", R3 / "00_governance/R3_RESEARCHER_DECISION_IMPLEMENTATION_AND_DATASET_DIRECTION.md", "GOVERNANCE", "R3 researcher decisions and roadmap", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-CORPVAL", R3 / "02_corpus/R3_CORPUS_VALIDATION_REGISTER.csv", "DATASET", "R3 corpus validation register", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-AUDITS", str(R3 / "12_audits/*.md"), "AUDIT", "R3 phase audits", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-PDF", str(R3 / "01_sources/*/*.pdf"), "LEGAL_TEXT", "R3 official-journal PDFs of the five R2 acts", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-MANIF", str(R3 / "01_sources/*/SOURCE_MANIFEST.yaml"), "MANIFEST", "R3 per-act source manifests", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-ACTFULL", str(R3 / "02_corpus/*/act_numbered.md"), "LEGAL_TEXT", "R3 numbered corpus per act", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-COMMAUDIT", R4 / "01_baseline/R3_ORIGINAL/communications/COMMUNICATION_ARCHIVE_AUDIT.md", "AUDIT", "R3 communications archive audit", "HISTORY_R3", "HISTORICAL"),
    ("SRC-R3-FINALXLSX", str(R4 / "01_baseline/R3_ORIGINAL/final_package/*.xlsx"), "DATASET", "R3 final package dataset", "HISTORY_R3", "HISTORICAL"),
    # --- R4
    ("SRC-R4-EXTR", ENV / "03_SOURCE_DATA_AND_CORPUS/R4_STRUCTURAL_EXTRACTION.csv", "DATASET", "R4 structural extraction (1,404 rows)", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-EXTR-WORK", R4 / "03_extraction/R4_STRUCTURAL_EXTRACTION.csv", "DATASET", "R4 structural extraction (working copy)", "HISTORY_R4", "DUPLICATE_CHECK"),
    ("SRC-R4-CORPREG", ENV / "03_SOURCE_DATA_AND_CORPUS/R4_DIGITAL_CORPUS_REGISTER.csv", "DATASET", "R4 digital corpus register", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-2D", str(ENV / "05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/*"), "ADJUDICATION", "R4.2D human diagnostic files", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-PATTERN", ENV / "05_QA_AND_HUMAN_ADJUDICATION/R4_2C_R_PATTERN_CONFIRMATION.csv", "DATASET", "R4.2C-R pattern confirmation", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-SYSAUD", str(ENV / "05_QA_AND_HUMAN_ADJUDICATION/R4_2B_SYSTEMATIC_ERROR_AUDIT*.csv"), "DATASET", "R4.2B systematic error audit", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-LUNAREV", str(ENV / "05_QA_AND_HUMAN_ADJUDICATION/**/R4_2C_TERRA_CALIBRATED_REVIEW.csv"), "DATASET", "Luna self-review (87 rows)", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-TERRAREV", str(ENV / "05_QA_AND_HUMAN_ADJUDICATION/**/R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv"), "DATASET", "Terra V2 review (87 rows)", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-BUILDEXTR", R4 / "09_logs/build_r4_2_structural_extraction.ps1", "SCRIPT", "R4.2 extraction build script (regex)", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-BUILD2CR", ENV / "11_REPRODUCIBILITY/build_r4_2cr_true_terra_review.ps1", "SCRIPT", "R4.2C-R pattern definition script", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-WORKNOTE", str(P / "**/R4_COMPLETE_WORK_NOTE.md"), "REPORT", "R4 complete work note", "HISTORY_R4", "HISTORICAL"),
    ("SRC-R4-DSA-TXT", str(R4 / "02_sources/D2_DSA/normalized/*"), "LEGAL_TEXT", "DSA normalized text (R4 corpus)", "LEGAL_SOURCE", "HISTORICAL"),
    ("SRC-R4-DSA-ORIG", str(R4 / "02_sources/D2_DSA/original/*"), "LEGAL_TEXT", "DSA original download (R4 corpus)", "LEGAL_SOURCE", "HISTORICAL"),
    ("SRC-R4-DSA-META", str(R4 / "02_sources/D2_DSA/metadata/*"), "MANIFEST", "DSA source metadata (R4 corpus)", "LEGAL_SOURCE", "HISTORICAL"),
    # --- Pilots
    ("SRC-P01-XWALK", PIL / "PILOT_01/02_CROSSWALK/ROTEM_TO_RELATIONAL_CROSSWALK.csv", "DATASET", "PILOT_01 crosswalk (MODEL_PILOT)", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P01-XWALK-MD", PIL / "PILOT_01/02_CROSSWALK/ROTEM_TO_RELATIONAL_CROSSWALK.md", "REPORT", "PILOT_01 crosswalk summary", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P01-REPORT", PIL / "PILOT_01/05_RESULTS/PILOT_01_REPORT.md", "REPORT", "PILOT_01 report", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P01-MODEL", PIL / "PILOT_01/01_DESIGN/RELATIONAL_MODEL_V0_1.md", "DESIGN", "Relational model v0.1", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-MANIF-PRE", PIL / "PILOT_03/99_REPRODUCIBILITY/PILOT_03_MANIFEST.json", "MANIFEST", "PILOT_03 pre-adjudication manifest", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-MANIF-FINAL", PIL / "PILOT_03/99_REPRODUCIBILITY/PILOT_03_MANIFEST_FINAL.json", "MANIFEST", "PILOT_03 final manifest", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-ADJ", str(PIL / "PILOT_03/07_HUMAN_ADJUDICATION/*"), "ADJUDICATION", "PILOT_03 human adjudication files", "HISTORY_PILOT", "HUMAN_DECISIONS_PRESERVED"),
    ("SRC-P03-RESULTS", str(PIL / "PILOT_03/08_RESULTS/*"), "REPORT", "PILOT_03 results", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-PROV", str(PIL / "PILOT_03/03_SOURCE_PROVISIONS/*"), "DATASET", "PILOT_03 provision register and excerpts", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-CMP", str(PIL / "PILOT_03/04_COMPARISON/*"), "DATASET", "PILOT_03 coder comparison", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-A", str(PIL / "PILOT_03/04_MODEL_A/*"), "DATASET", "PILOT_03 pass A", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-B", str(PIL / "PILOT_03/05_MODEL_B/*"), "DATASET", "PILOT_03 pass B", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-RULES", str(PIL / "PILOT_03/01_PROTOCOL/*"), "PROTOCOL", "PILOT_03 protocol and coding rules", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-SCRIPTS", str(PIL / "PILOT_03/99_REPRODUCIBILITY/*.py"), "SCRIPT", "PILOT_03 build/incorporate scripts", "HISTORY_PILOT", "HISTORICAL"),
    ("SRC-P03-FILLED-DL", DL / "HUMAN_ADJUDICATION_RESPONSES_FILLED.csv", "ADJUDICATION", "Filled human adjudication responses (Downloads, input of incorporate script)", "HISTORY_PILOT", "HUMAN_DECISIONS_PRESERVED"),
    ("SRC-PROMPT-MESTRE", DL / "PROMPT_MESTRE_REEXECUCAO_AUTONOMA_ROTEM_OPUS.md", "INSTRUCTION", "Master prompt copy", "ADMIN", "INSTRUCTION"),
]


def docx_meta(path):
    try:
        import docx
        cp = docx.Document(path).core_properties
        return f"author={cp.author}; last_modified_by={cp.last_modified_by}; created={cp.created}; modified={cp.modified}; revision={cp.revision}"
    except Exception as e:  # noqa: BLE001
        return f"docx_meta_error={e}"


def xlsx_meta(path):
    try:
        import openpyxl
        wb = openpyxl.load_workbook(path, read_only=True)
        p = wb.properties
        return f"creator={p.creator}; last_modified_by={p.lastModifiedBy}; created={p.created}; modified={p.modified}; sheets={'|'.join(wb.sheetnames)}"
    except Exception as e:  # noqa: BLE001
        return f"xlsx_meta_error={e}"


def expand(spec):
    s = str(spec)
    if any(ch in s for ch in "*?"):
        return sorted(Path(x) for x in glob.glob(s, recursive=True) if Path(x).is_file())
    return [Path(s)]


rows, hashes = [], []
for sid, spec, cat, role, layer, status in SOURCES:
    files = expand(spec)
    if not files:
        rows.append(dict(SOURCE_ID=sid, PATH=str(spec), LOCATION="MISSING", CATEGORY=cat, ROLE=role, SCHEMA_LAYER=layer,
                         SOURCE_STATUS=status, EXISTS="NO", READ_STATE="MISSING"))
        continue
    for i, f in enumerate(files, 1):
        fid = sid if len(files) == 1 else f"{sid}-{i:02d}"
        exists = f.exists()
        rec = dict(SOURCE_ID=fid, PATH=rel_to_project(f), LOCATION=("PROJECT" if str(f.resolve()).startswith(str(PROJECT_ROOT)) else "OUTSIDE_PROJECT"),
                   CATEGORY=cat, ROLE=role, SCHEMA_LAYER=layer, SOURCE_STATUS=status, EXISTS="YES" if exists else "NO")
        if exists:
            st = f.stat()
            rec.update(SIZE_BYTES=st.st_size, MTIME=dt.datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
                       SHA256=sha256(f), SHA256_LF_NORMALIZED=sha256(f, lf_normalize=True) if f.suffix.lower() in {".md", ".csv", ".txt", ".json", ".yaml", ".py", ".ps1", ""} else "",
                       READ_STATE="HASHED")
            if f.suffix.lower() == ".docx":
                rec["INTERNAL_METADATA"] = docx_meta(f)
            elif f.suffix.lower() == ".xlsx":
                rec["INTERNAL_METADATA"] = xlsx_meta(f)
            hashes.append(dict(SOURCE_ID=fid, PATH=rec["PATH"], SHA256=rec["SHA256"], SIZE_BYTES=st.st_size, HASHED_AT=now_iso()))
        else:
            rec["READ_STATE"] = "MISSING"
        rows.append(rec)

hdr = ["SOURCE_ID", "PATH", "LOCATION", "CATEGORY", "ROLE", "SCHEMA_LAYER", "SOURCE_STATUS", "EXISTS", "SIZE_BYTES", "MTIME", "SHA256", "SHA256_LF_NORMALIZED", "INTERNAL_METADATA", "READ_STATE"]
write_csv(RUN_ROOT / "01_BASELINES/SOURCE_REGISTER.csv", hdr, rows)
write_csv(RUN_ROOT / "01_BASELINES/BASELINE_HASHES.csv", ["SOURCE_ID", "PATH", "SHA256", "SIZE_BYTES", "HASHED_AT"], hashes)
print(len(rows), "register rows;", sum(1 for r in rows if r["EXISTS"] == "NO"), "missing")
for r in rows:
    if r["EXISTS"] == "NO":
        print("MISSING:", r["SOURCE_ID"], r["PATH"])
