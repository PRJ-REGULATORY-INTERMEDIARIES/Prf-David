"""Write EXTRACTION_UNCERTAINTIES.md and HUMAN_ADJUDICATION_QUEUE.md from _store.json."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
D = json.load(open(os.path.join(HERE, "_store.json"), encoding="utf-8"))
L = ["# Extraction uncertainties — GDPR Pilot 01", "", "**Status:** `MACHINE_PROVISIONAL`. Generated from the extraction store; each item states what it affects. These are limits of the pilot's own extraction, not findings about the GDPR.", "",
     "| ID | Units | Type | Description | Effect |", "|---|---|---|---|---|"]
for u in D["unc"]:
    L.append(f"| {u['id']} | {u['units'].replace('GDPR.', '')[:60]} | {u['type']} | {u['description']} | {u['effect']} |")
L += ["", "## Review flags carried by records", ""]
import collections
fl = collections.Counter()
for k in ("na", "qr", "pd"):
    for r in D[k]:
        if r.get("review_flag"):
            fl[(k.upper(), r["review_flag"])] += 1
for (k, f), n in sorted(fl.items()):
    L.append(f"- {k} `{f}`: {n}")
open(os.path.join(HERE, "EXTRACTION_UNCERTAINTIES.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
Q = ["# Human adjudication queue — GDPR Pilot 01", "", "**Status:** open items for Igor and, where marked, specialist legal review. Machine-generated extraction is provisional; none of these has been silently resolved. The last column states whether adjudication is required before the dependent claim is used; no item prevents the pilot from continuing.", "",
     "| ID | Issue | Why it matters | Options | Adjudication required before the dependent claim is used |", "|---|---|---|---|---|"]
for h in D["hq"]:
    Q.append(f"| {h['id']} | {h['issue']} | {h['why_it_matters']} | {h['options']} | {h['blocking']} |")
Q += ["", "## Standing rule", "", "A subsequent independent review should use separately produced human coding, with agreement reported by variable and by interpretive level. Repetition by the same model is not inter-coder reliability.", ""]
os.makedirs(os.path.join(ROOT, "05_SCIENTIFIC_ASSESSMENT"), exist_ok=True)
open(os.path.join(ROOT, "05_SCIENTIFIC_ASSESSMENT", "HUMAN_ADJUDICATION_QUEUE.md"), "w", encoding="utf-8").write("\n".join(Q) + "\n")
print("docs written", len(D["unc"]), len(D["hq"]))
