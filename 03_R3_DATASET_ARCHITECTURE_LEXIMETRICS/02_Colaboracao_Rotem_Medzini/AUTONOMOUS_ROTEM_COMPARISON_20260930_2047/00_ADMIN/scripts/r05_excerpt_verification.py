"""R05 — Verify the 33 PILOT_03 legal excerpts against the official texts fetched in R01 (fresh check).

Excerpts were hard-coded in the PILOT_02/03 build scripts and contain '...' elisions. Each fragment (split on '...')
of >= 12 characters is searched in the normalised official text. If not found verbatim, the best fuzzy window
similarity (difflib) is reported. Result classes:
  VERBATIM_ALL_FRAGMENTS / VERBATIM_SOME_FRAGMENTS / CLOSE_PARAPHRASE (best ratio >= 0.80) / NOT_LOCATED.
"""
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, read_csv, write_csv  # noqa: E402

OFF = RUN_ROOT / "01_BASELINES/official_texts"


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    s = re.sub(r"\s+", " ", s.lower())
    return s.strip(" .;,")


def best_ratio(frag, text):
    n = len(frag)
    if n == 0:
        return 0.0
    # anchor on the rarest 3-word window to find candidate positions
    words = frag.split()
    best = 0.0
    anchors = set()
    for i in range(0, max(1, len(words) - 2)):
        w = " ".join(words[i:i + 3])
        for m in re.finditer(re.escape(w), text):
            anchors.add(m.start())
        if len(anchors) > 200:
            break
    for a in list(anchors)[:200]:
        for off in (0, n // 2):
            s = max(0, a - off)
            r = difflib.SequenceMatcher(None, frag, text[s:s + n + 40]).ratio()
            best = max(best, r)
    return round(best, 3)


cache = {}
rows = []
for r in read_csv(RUN_ROOT / "01_BASELINES/BASELINE_REL_PILOT03_PROVISION_REGISTER.csv"):
    c = r["celex"]
    if c not in cache:
        cache[c] = norm((OFF / f"{c}.txt").read_text(encoding="utf-8"))
    text = cache[c]
    frags = [norm(f) for f in re.split(r"\.\.\.|…", r["excerpt"]) if len(norm(f)) >= 12]
    found = [f for f in frags if f in text]
    ratios = [1.0 if f in text else best_ratio(f, text) for f in frags]
    if frags and len(found) == len(frags):
        cls = "VERBATIM_ALL_FRAGMENTS"
    elif found:
        cls = "VERBATIM_SOME_FRAGMENTS"
    elif ratios and min(ratios) >= 0.80:
        cls = "CLOSE_PARAPHRASE"
    else:
        cls = "NOT_LOCATED_VERBATIM"
    rows.append(dict(PROVISION_ID=r["provision_id"], CASE_ID=r["case_id"], CELEX=c, LOCATION=r["location"],
                     EXCERPT=r["excerpt"], HISTORICAL_STATUS=r["status"], N_FRAGMENTS=len(frags), N_VERBATIM=len(found),
                     FRAGMENT_BEST_RATIOS="; ".join(str(x) for x in ratios), FRESH_VERIFICATION=cls,
                     OFFICIAL_TEXT=f"01_BASELINES/official_texts/{c}.txt"))
write_csv(RUN_ROOT / "05_PILOT03/PILOT03_EXCERPT_VERIFICATION.csv", list(rows[0].keys()), rows)
from collections import Counter  # noqa: E402
print(Counter(x["FRESH_VERIFICATION"] for x in rows))
for x in rows:
    print(x["PROVISION_ID"], x["LOCATION"], x["FRESH_VERIFICATION"], x["FRAGMENT_BEST_RATIOS"])
