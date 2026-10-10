"""Helpers to cut article / annex blocks from the Cellar plain-text renderings (01_BASELINES/official_texts/*.txt)."""
import re
from pathlib import Path
OFF = Path(__file__).resolve().parents[2] / "01_BASELINES/official_texts"

def load(celex):
    return (OFF / f"{celex}.txt").read_text(encoding="utf-8")

def article(celex, n):
    t = load(celex)
    heads = [(m.start(), m.group(1)) for m in re.finditer(r"(?m)^\s*Article (\d+[a-z]?)\s*$", t)]
    for i, (pos, num) in enumerate(heads):
        if num == str(n):
            end = heads[i + 1][0] if i + 1 < len(heads) else len(t)
            m = re.search(r"(?m)^\s*ANNEX", t[pos:end])
            if m:
                end = pos + m.start()
            return t[pos:end].strip()
    return None

def annex(celex, label):
    t = load(celex)
    heads = [(m.start(), m.group(1).strip()) for m in re.finditer(r"(?m)^\s*(ANNEX [IVXL]+)\s*$", t)]
    for i, (pos, lab) in enumerate(heads):
        if lab == label:
            end = heads[i + 1][0] if i + 1 < len(heads) else len(t)
            return t[pos:end].strip()
    return None
