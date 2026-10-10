"""R06 — ROTEM_FIELD_DICTIONARY.csv: every variable defined in the revised codebook tables (¶72, ¶74, ¶79, ¶82, ¶85),
with presence in the unrevised codebook / Chart Key (keyword check) and in the implemented workbook (column match)."""
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, write_csv  # noqa: E402

D = RUN_ROOT / "01_BASELINES/derived_text"
rev = (D / "CODEBOOK_REVISED.md").read_text(encoding="utf-8")
unrev = (D / "CODEBOOK_UNREVISED_BASELINE.md").read_text(encoding="utf-8")
unrev_cb = unrev.split("[¶145]")[0]  # codebook text only (¶1-¶144); embedded commentary excluded (I-006)
chart = (D / "CHART_KEY_UNREVISED_BASELINE.md").read_text(encoding="utf-8")

TABLES = {"72": ("Excluded_acts", "ACT_SCREENING", "Group 1"), "74": ("ACT_SUMMARY", "ACT", "Group 1"),
          "79": ("INTERMEDIARY_MAP", "INTERMEDIARY_X_ACT", "Group 2"), "82": ("INTERMEDIARY_MAP", "INTERMEDIARY_X_ACT", "Group 3"),
          "85": ("INTERMEDIARY_MAP", "INTERMEDIARY_X_ACT", "Group 4")}


def table_rows(par):
    m = re.search(rf"\[¶{par} TABLE\]\n(.*?)(?:\n\n|\Z)", rev, re.S)
    lines = [l for l in m.group(1).splitlines() if l.startswith("|")][2:]
    for l in lines:
        cells = [c.strip() for c in l.strip("|").split(" | ")]
        if len(cells) >= 3:
            yield cells[0], cells[1], cells[2]


wb_cols = {}
for f, sheet in [("BASELINE_ROTEM_WB_CODING_DIGITAL_INTERMEDIARIES.csv", "CDI"), ("BASELINE_ROTEM_WB_LIST_OF_ACTORS.csv", "LoA"),
                 ("BASELINE_ROTEM_WB_LIST_OF_INTERMEDIARIES.csv", "LoI")]:
    with open(RUN_ROOT / "01_BASELINES" / f, encoding="utf-8") as fh:
        hdr = next(csv.reader(fh))[2:]
    for h in hdr:
        wb_cols.setdefault(h.lower().replace(" ", "_").replace("?", ""), []).append(f"{sheet}:{h}")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


ALIASES = {  # explicit, documented equivalences between revised variable names and workbook headers
    "recognition_pathways": ["CDI:Recongnition_pathways (vetting/designation/none)", "LoA:Recognition_pathway", "LoI:Recognition_pathway"],
    "intermediary_type": ["CDI:Intermediary_type (for_profit/industry_association/episdemic)", "LoA:Actor_type (partial analogue)"],
    "intermediary_name": ["CDI:Who are the intermediaries? (free text, act-level)", "LoA:Intermediary_legal_label", "LoI:Intermediary_legal_label"],
    "relevantprovisions": ["CDI:Relevant provision(s) (2/41 substantive rows populated)", "LoA:Relevant_articles_addressing_intermediaries (35/35)", "LoI:Relevant_articles_addressing_intermediaries"],
    "function_description": ["CDI:What do the intermediaries do? (free text, act-level)"],
    "regulation_of_description": ["CDI:How are intermediaries being regulated? (free text, act-level)"],
    "domain": ["CDI:Sector"],
    "act_title": ["CDI:Legislation Name", "LoA:Name_of_legislation"],
    "obligation_intensity": ["CDI:Obligation_intensity", "LoA:Obligation_intensity"],
}

rows = []
for par, (comp, unit, grp) in TABLES.items():
    for var, definition, values in table_rows(par):
        key = norm(var)
        wb = []
        for k, v in wb_cols.items():
            if norm(k) == key:
                wb += v
        for ak, av in ALIASES.items():
            if norm(ak) == key:
                wb += av
        token = var.split("/")[0].replace("Function_", "").replace("_", " ").lower().strip()
        in_unrev = "YES" if token and token in unrev_cb.lower() else "NO"
        in_chart = "YES" if token and token in chart.lower() else "NO"
        multi = "YES" if "multiple values permitted" in values.lower() or "multiple values" in values.lower() else "NO"
        rows.append(dict(FIELD=var, COMPONENT=comp, UNIT_LEVEL=unit, VARIABLE_GROUP=grp, REVISED_CODEBOOK_REF=f"¶{par} TABLE",
                         DEFINITION_VERBATIM=definition, PERMITTED_VALUES_VERBATIM=values, MULTIVALUED=multi,
                         TERM_IN_UNREVISED_CODEBOOK_TEXT=in_unrev, TERM_IN_CHART_KEY=in_chart,
                         WORKBOOK_COLUMNS="; ".join(dict.fromkeys(wb)) or "NONE",
                         LAYER3_STATUS="PRESENT" if wb else "ABSENT", ATTRIBUTION="EXISTING (Rotem codebook, revised)"))
write_csv(RUN_ROOT / "06_CODEBOOK/ROTEM_FIELD_DICTIONARY.csv", list(rows[0].keys()), rows)
from collections import Counter  # noqa: E402
print(len(rows), Counter((r["UNIT_LEVEL"], r["LAYER3_STATUS"]) for r in rows))
for r in rows:
    if r["UNIT_LEVEL"] == "INTERMEDIARY_X_ACT":
        print(r["FIELD"], "|", r["MULTIVALUED"], "|", r["LAYER3_STATUS"], "|", r["WORKBOOK_COLUMNS"][:90])
