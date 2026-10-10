"""R01 — Freeze BASELINE_* files before any comparison.

(1) Rotem workbook sheets exported verbatim to CSV (cell values as stored; no normalisation).
(2) Historical relational codings copied byte-for-byte and hash-verified.
"""
import shutil
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, PROJECT_ROOT, sha256, write_csv, now_iso, rel_to_project  # noqa: E402

B = RUN_ROOT / "01_BASELINES"
WB = PROJECT_ROOT / "RELATIONAL_LEXIMETRICS_PILOT/PILOT_01/00_SOURCES/dataset_of_EU_regulatory_intermediation.xlsx"
PIL = PROJECT_ROOT / "RELATIONAL_LEXIMETRICS_PILOT"
R3 = PROJECT_ROOT / "R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM"
ENV = PROJECT_ROOT / "ENVIO_R4_TO_DAVID"

log = []
wb = openpyxl.load_workbook(WB, read_only=True, data_only=True)
for sheet, out in [("Coding Digital Intermediaries", "BASELINE_ROTEM_WB_CODING_DIGITAL_INTERMEDIARIES.csv"),
                   ("List of actors", "BASELINE_ROTEM_WB_LIST_OF_ACTORS.csv"),
                   ("List of intermediaries", "BASELINE_ROTEM_WB_LIST_OF_INTERMEDIARIES.csv")]:
    ws = wb[sheet]
    rows = list(ws.iter_rows(values_only=True))
    hdr = ["WB_SHEET", "WB_ROW"] + [("" if h is None else str(h)) for h in rows[0]]
    data = []
    for i, r in enumerate(rows[1:], start=2):
        if not any(v not in (None, "") for v in r):
            continue
        data.append([sheet, i] + ["" if v is None else str(v) for v in r])
    write_csv(B / out, hdr, data)
    log.append((out, f"verbatim export of sheet '{sheet}' from {rel_to_project(WB)} (SHA256 {sha256(WB)}); {len(data)} non-empty rows; empty rows skipped; WB_ROW = Excel row number"))

COPIES = [
    (PIL / "PILOT_03/07_HUMAN_ADJUDICATION/HUMAN_DECISION_LOG.csv", "BASELINE_REL_PILOT03_HUMAN_DECISION_LOG.csv"),
    (PIL / "PILOT_03/07_HUMAN_ADJUDICATION/HUMAN_ADJUDICATION_RESPONSES_FILLED.csv", "BASELINE_REL_PILOT03_HUMAN_RESPONSES_FILLED.csv"),
    (PIL / "PILOT_03/07_HUMAN_ADJUDICATION/HUMAN_ADJUDICATION_RESPONSES.csv", "BASELINE_REL_PILOT03_PRE_ADJUDICATION_TEMPLATE.csv"),
    (PIL / "PILOT_03/07_HUMAN_ADJUDICATION/BACKWARD_IMPACT_REGISTER.csv", "BASELINE_REL_PILOT03_BACKWARD_IMPACT_REGISTER.csv"),
    (PIL / "PILOT_03/04_MODEL_A/RELATIONSHIPS_MODEL_A.csv", "BASELINE_REL_PILOT03_PASS_A.csv"),
    (PIL / "PILOT_03/05_MODEL_B/RELATIONSHIPS_MODEL_B.csv", "BASELINE_REL_PILOT03_PASS_B.csv"),
    (PIL / "PILOT_03/03_SOURCE_PROVISIONS/PROVISION_REGISTER.csv", "BASELINE_REL_PILOT03_PROVISION_REGISTER.csv"),
    (PIL / "PILOT_03/03_SOURCE_PROVISIONS/LEGAL_EXCERPTS.csv", "BASELINE_REL_PILOT03_LEGAL_EXCERPTS.csv"),
    (PIL / "PILOT_03/01_PROTOCOL/CODING_RULES_V0_3_ADJUDICATED.md", "BASELINE_REL_PILOT03_CODING_RULES_V0_3_ADJUDICATED.md"),
    (PIL / "PILOT_01/02_CROSSWALK/ROTEM_TO_RELATIONAL_CROSSWALK.csv", "BASELINE_REL_PILOT01_ROTEM_CROSSWALK.csv"),
    (R3 / "06_relations/RELATIONS_ADJUDICATED.csv", "BASELINE_REL_R3_RELATIONS_ADJUDICATED.csv"),
    (R3 / "05_law_intermediary/LAW_INTERMEDIARY_REGISTER.csv", "BASELINE_REL_R3_LAW_INTERMEDIARY_REGISTER.csv"),
    (R3 / "07_mechanisms/MECHANISM_EVENTS_RESEARCHER_ADJUDICATED.csv", "BASELINE_REL_R3_MECHANISM_EVENTS.csv"),
    (ENV / "05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv", "BASELINE_R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv"),
]
for src, out in COPIES:
    dst = B / out
    shutil.copyfile(src, dst)
    ok = sha256(src) == sha256(dst)
    log.append((out, f"byte copy of {rel_to_project(src)}; SHA256 {sha256(dst)}; hash_equal_to_source={ok}"))
    assert ok, out

# DSA subset of the R4 structural extraction (rows only, verbatim) for the articles used as case material
import csv  # noqa: E402
src = ENV / "03_SOURCE_DATA_AND_CORPUS/R4_STRUCTURAL_EXTRACTION.csv"
with open(src, newline="", encoding="utf-8-sig") as f:
    rd = csv.DictReader(f)
    hdr = rd.fieldnames
    keep = [r for r in rd if r["CELEX"] == "32022R2065" and r["SOURCE_TYPE"] == "OPERATIVE_ARTICLE" and r["ARTICLE_NUMBER"] in {"21", "22", "37", "42"}]
write_csv(B / "BASELINE_R4_EXTRACTION_DSA_ART21_22_37_42.csv", hdr, keep)
log.append(("BASELINE_R4_EXTRACTION_DSA_ART21_22_37_42.csv", f"row filter (CELEX=32022R2065, operative articles 21/22/37/42) of {rel_to_project(src)} (SHA256 {sha256(src)}); {len(keep)} rows; values verbatim"))

write_csv(B / "BASELINE_FREEZE_LOG.csv", ["BASELINE_FILE", "PROVENANCE"], log)
for l in log:
    print(l[0], "|", l[1][:160])
