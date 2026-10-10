"""R04 — Independent recomputation (Python re-implementation) of the R4.2B/2C/2D defect statistics from the frozen inputs.

Compares recomputed values with the recorded outputs. Nothing is written outside RUN_ROOT.
"""
import collections
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, PROJECT_ROOT, write_csv  # noqa: E402

ENV = PROJECT_ROOT / "ENVIO_R4_TO_DAVID"
QA = ENV / "05_QA_AND_HUMAN_ADJUDICATION"


def rd(p):
    with open(p, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def codes(s):
    return [c.strip() for c in re.split(r"[;|]", s or "") if c.strip()]


out = []
luna = {r["QA_ID"]: r for r in rd(QA / "R4_2C_TERRA_CALIBRATED_REVIEW.csv")}
terra = {r["QA_ID"]: r for r in rd(QA / "R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv")}
out.append(("ROWS_LUNA_SELF_REVIEW", len(luna), "87 (script asserts 87)"))
out.append(("ROWS_TERRA_V2", len(terra), "87"))
for name, src in [("LUNA", luna), ("TERRA", terra)]:
    c = collections.Counter(x for r in src.values() for x in codes(r["ERROR_TYPE_TERRA"]))
    for k, v in sorted(c.items()):
        out.append((f"{name}_ERRORCODE_{k}", v, ""))
    models = collections.Counter((r.get("RUNTIME_OBSERVED_MODEL") or r.get("ACTUAL_MODEL") or "") for r in src.values())
    out.append((f"{name}_MODEL_FIELD_VALUES", "; ".join(f"{k or '(blank)'}={v}" for k, v in models.items()), ""))

recorded = {r["PATTERN"]: r for r in rd(QA / "R4_2C_R_PATTERN_CONFIRMATION.csv")}
for pname, rx in [("COUNTERPART_RECIPIENT_OVERATTRIBUTION", r"COUNTERPART_EXTRACTION_ERROR|RECIPIENT_EXTRACTION_ERROR"),
                  ("ACTOR_ACTION_FRAGMENTATION", r"ACTOR_EXTRACTION_ERROR|ACTION_EXTRACTION_ERROR")]:
    li = {k for k, r in luna.items() if re.search(rx, r["ERROR_TYPE_TERRA"] or "")}
    ti = {k for k, r in terra.items() if re.search(rx, r["ERROR_TYPE_TERRA"] or "")}
    over, union = li & ti, li | ti
    rate = round(100 * len(over) / len(union), 1) if union else 0
    rec = recorded[pname]
    out.append((f"{pname}_LUNA_N", len(li), f"recorded {rec['LUNA_SELFREVIEW_FLAGGED_N']}"))
    out.append((f"{pname}_TERRA_N", len(ti), f"recorded {rec['TERRA_INDEPENDENT_FLAGGED_N']}"))
    out.append((f"{pname}_OVERLAP_N", len(over), f"recorded {rec['OVERLAP_N']}"))
    out.append((f"{pname}_AGREEMENT_PCT", rate, f"recorded {rec['AGREEMENT_RATE_WITHIN_FLAGGED_UNIVERSE_PERCENT']} (decimal comma in source)"))
    out.append((f"{pname}_HUMAN_CONFIRMED_AT_2C", rec["HUMAN_CONFIRMED"], "recorded"))

# R4.2D human diagnostic
d = rd(RUN_ROOT / "01_BASELINES/BASELINE_R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv")
out.append(("R4_2D_CASES", len(d), ""))
out.append(("R4_2D_REVIEW_STATUS", "; ".join(f"{k}={v}" for k, v in collections.Counter(r["HUMAN_REVIEW_STATUS"] for r in d).items()), ""))
out.append(("R4_2D_REVIEWER", "; ".join(f"{k}={v}" for k, v in collections.Counter(r["HUMAN_REVIEWER"] for r in d).items()), ""))
out.append(("R4_2D_PATTERN_CONFIRMED", "; ".join(f"{k}={v}" for k, v in collections.Counter(r["HUMAN_PATTERN_CONFIRMED"] for r in d).items()), ""))
for f in ["ACTOR", "ACTION", "OBJECT", "COUNTERPART", "RECIPIENT"]:
    out.append((f"R4_2D_{f}_CORRECT_NO", sum(1 for r in d if r[f"HUMAN_{f}_CORRECT"] == "NO"), ""))
out.append(("R4_2D_BY_SELECTED_PATTERN", "; ".join(f"{k}={v}" for k, v in collections.Counter(r["PATTERN"] for r in d).items()), ""))
cls = collections.Counter(x for r in d for x in codes(r["HUMAN_DIAGNOSTIC_DEFECT_CLASS"]))
for k, v in sorted(cls.items()):
    out.append((f"R4_2D_HUMAN_CLASS_{k}", v, ""))
same = sum(1 for r in d if r["PATTERN"] in codes(r["HUMAN_DIAGNOSTIC_DEFECT_CLASS"]))
out.append(("R4_2D_SELECTED_PATTERN_EQUALS_A_HUMAN_CLASS", same, "of 12"))

# R4 structural extraction field identities (1,404 rows)
x = rd(ENV / "03_SOURCE_DATA_AND_CORPUS/R4_STRUCTURAL_EXTRACTION.csv")
out.append(("R4_EXTRACTION_ROWS", len(x), ""))
out.append(("R4_COUNTERPART_EQUALS_RECIPIENT", sum(1 for r in x if r["COUNTERPART_TEXT"] == r["RECIPIENT_TEXT"]), "rows where the two fields are string-identical (incl. both empty)"))
out.append(("R4_COUNTERPART_RECIPIENT_BOTH_EMPTY", sum(1 for r in x if not r["COUNTERPART_TEXT"] and not r["RECIPIENT_TEXT"]), ""))
out.append(("R4_ACTIONOBJECT_EQUALS_INFOOBJECT", sum(1 for r in x if r["ACTION_OBJECT"] == r["INFORMATION_OR_MATERIAL_OBJECT"]), ""))
out.append(("R4_EXTRACTION_MODEL_VALUES", "; ".join(f"{k}={v}" for k, v in collections.Counter(r["EXTRACTION_MODEL"] for r in x).items()), ""))
out.append(("R4_BY_CELEX", "; ".join(f"{k}={v}" for k, v in collections.Counter(r["CELEX"] for r in x).items()), ""))
r2 = {"32003L0087", "32015D1814", "32018R0842", "32021R1119", "32023R0955"}
out.append(("R4_ROWS_WITH_R2_CELEX", sum(1 for r in x if r["CELEX"] in r2), "expected 0 (R4 = digital acts)"))

# Script-level evidence that recipient := counterpart (regex assignment)
ps = (PROJECT_ROOT / "R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2_structural_extraction.ps1").read_text(encoding="utf-8", errors="replace")
out.append(("R4_SCRIPT_RECIPIENT_ASSIGNED_FROM_COUNTERPART", "YES" if "Recipient=$counterpart" in ps else "NO", "string 'Recipient=$counterpart' in build_r4_2_structural_extraction.ps1"))
out.append(("R4_SCRIPT_INFOOBJECT_ASSIGNED_SAME_AS_ACTIONOBJECT", "YES" if "ActionObject=(Get-FirstClause $remainder 180)" in ps and "InformationObject=(Get-FirstClause $remainder 180)" in ps else "NO", "both fields filled by Get-FirstClause $remainder 180"))
out.append(("R4_SCRIPT_COUNTERPART_REGEX", "YES" if "(to|with|from)" in ps else "NO", "counterpart = first match of (to|with|from) + determiner/actor word"))

write_csv(RUN_ROOT / "04_R3_R4/R4_RECOMPUTATION_RESULTS.csv", ["METRIC", "RECOMPUTED_VALUE", "NOTE"], out)
for o in out:
    print(*o, sep=" | ")
