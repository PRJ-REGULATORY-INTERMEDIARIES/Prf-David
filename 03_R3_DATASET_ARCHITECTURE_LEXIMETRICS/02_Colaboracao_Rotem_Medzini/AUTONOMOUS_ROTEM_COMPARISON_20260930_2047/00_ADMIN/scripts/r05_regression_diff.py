"""R05 — Compare re-generated pilot outputs (derived copy) with the original files, file by file.

A difference is classified as VOLATILE_ONLY when every differing line contains a run-date/timestamp/hash/mtime token
(volatile metadata); otherwise SUBSTANTIVE_DIFF. CSV/MD content diffs are listed line by line.
"""
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, PROJECT_ROOT, sha256, write_csv  # noqa: E402

ORIG = PROJECT_ROOT / "RELATIONAL_LEXIMETRICS_PILOT"
COPY = RUN_ROOT / "05_PILOT03/regression_copy/RELATIONAL_LEXIMETRICS_PILOT"
VOL = re.compile(r"(20\d\d-\d\d-\d\d|generated_at|built_on|capture_date|incorporated_at|sha256|SHA-256|[0-9a-fA-F]{64}|Modification time|\d{2}:\d{2}:\d{2})")

rows, details = [], []
for o in sorted(p for p in ORIG.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
    rel = o.relative_to(ORIG).as_posix()
    c = COPY / rel
    if not c.exists():
        rows.append([rel, "MISSING_IN_COPY", "", "", ""])
        continue
    ho, hc = sha256(o), sha256(c)
    if ho == hc:
        rows.append([rel, "IDENTICAL", ho, hc, ""])
        continue
    cls, nd = "BINARY_DIFF", ""
    if o.suffix.lower() in {".csv", ".md", ".json", ".txt", ".py"}:
        a = o.read_text(encoding="utf-8-sig", errors="replace").splitlines()
        b = c.read_text(encoding="utf-8-sig", errors="replace").splitlines()
        diff = [d for d in difflib.unified_diff(a, b, lineterm="", n=0) if d[:1] in "+-" and not d.startswith(("+++", "---"))]
        subst = [d for d in diff if not VOL.search(d)]
        if a == b:
            cls = "IDENTICAL_TEXT_DIFFERENT_BYTES"
        else:
            cls = "VOLATILE_ONLY" if not subst else "SUBSTANTIVE_DIFF"
        nd = f"{len(diff)} changed lines; {len(subst)} non-volatile"
        for d in diff[:40]:
            details.append([rel, "NONVOLATILE" if d in subst else "VOLATILE", d[:400]])
    rows.append([rel, cls, ho, hc, nd])
for c in sorted(p for p in COPY.rglob("*") if p.is_file()):
    rel = c.relative_to(COPY).as_posix()
    if not (ORIG / rel).exists():
        rows.append([rel, "NEW_IN_COPY", "", sha256(c), ""])

write_csv(RUN_ROOT / "05_PILOT03/PILOT03_REGRESSION_FILE_COMPARISON.csv", ["RELATIVE_PATH", "RESULT", "SHA256_ORIGINAL", "SHA256_REGENERATED", "DIFF_SUMMARY"], rows)
write_csv(RUN_ROOT / "05_PILOT03/PILOT03_REGRESSION_DIFF_LINES.csv", ["RELATIVE_PATH", "LINE_CLASS", "DIFF_LINE"], details)
from collections import Counter  # noqa: E402
print(Counter(r[1] for r in rows))
for r in rows:
    if r[1] not in ("IDENTICAL",):
        print(r[1], "|", r[0], "|", r[4])
