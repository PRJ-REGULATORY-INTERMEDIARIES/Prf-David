"""Fetch official EN texts from the Publications Office Cellar (content negotiation) and store raw HTML + plain text.

Endpoint: http://publications.europa.eu/resource/celex/{CELEX}  (Accept: text/html; Accept-Language: eng)
The EUR-Lex HTML front-end returned HTTP 202/empty (bot challenge) on 2026-09-30, so Cellar is used.
"""
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, sha256, now_iso, write_csv  # noqa: E402

OUT = RUN_ROOT / "01_BASELINES/official_texts"
CELEX = {
    # PILOT_03 sample acts
    "31976L0889": "PILOT_03 P01", "31989L0336": "PILOT_03 P02", "31991L0263": "PILOT_03 P03",
    "32004R0874": "PILOT_03 P04", "32006R1781": "PILOT_03 P05", "31986L0361": "PILOT_03 C01",
    "31992L0044": "PILOT_03 C02", "32004L0048": "PILOT_03 C03", "32006L0115": "PILOT_03 C04",
    "31987D0095": "PILOT_03 C05",
    # R2 corpus + historical false positive
    "32003L0087": "R2 corpus", "32015D1814": "R2 corpus", "32018R0842": "R2 corpus",
    "32021R1119": "R2 corpus", "32023R0955": "R2 corpus", "32000D0293": "R1 S2 sample; excluded as historical false positive",
    # DSA (cross-check of R4 local copy)
    "32022R2065": "R4 corpus / case material",
}


def fetch(celex):
    """Try text/html first (older acts), then application/xhtml+xml (newer acts)."""
    url = f"http://publications.europa.eu/resource/celex/{celex}"
    last = None
    for accept in ("text/html", "application/xhtml+xml"):
        req = urllib.request.Request(url, headers={"Accept": accept, "Accept-Language": "eng",
                                                   "User-Agent": "research-reproduction (AUTONOMOUS_ROTEM_COMPARISON)"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return url + f"  [Accept: {accept}]", r.geturl(), r.status, r.read()
        except Exception as e:  # noqa: BLE001
            last = e
    raise last


def to_text(raw):
    t = raw.decode("utf-8", errors="replace")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()


def title_of(raw):
    m = re.search(rb'<meta name="DC.title" content="([^"]*)"', raw)
    if m:
        return m.group(1).decode("utf-8", "replace")
    m = re.search(rb'<title>([^<]*)</title>', raw)
    return m.group(1).decode("utf-8", "replace").strip() if m else ""


rows = []
for celex, purpose in CELEX.items():
    try:
        url, final, status, raw = fetch(celex)
        (OUT / f"{celex}.html").write_bytes(raw)
        txt = to_text(raw)
        (OUT / f"{celex}.txt").write_text(txt, encoding="utf-8")
        rows.append(dict(CELEX=celex, PURPOSE=purpose, REQUEST_URL=url, RESOLVED_URL=final, HTTP_STATUS=status,
                         ACCESSED_AT=now_iso(), BYTES=len(raw), SHA256_HTML=sha256(OUT / f"{celex}.html"),
                         SHA256_TXT=sha256(OUT / f"{celex}.txt"), DC_TITLE=title_of(raw), TEXT_CHARS=len(txt),
                         EVIDENCE_STATUS="VERIFIED_OFFICIAL_URL"))
        print(celex, status, len(raw))
    except Exception as e:  # noqa: BLE001
        rows.append(dict(CELEX=celex, PURPOSE=purpose, REQUEST_URL=f"http://publications.europa.eu/resource/celex/{celex}",
                         HTTP_STATUS=f"ERROR {e}", ACCESSED_AT=now_iso(), EVIDENCE_STATUS="MISSING"))
        print(celex, "ERROR", e)
    time.sleep(1.5)

hdr = ["CELEX", "PURPOSE", "REQUEST_URL", "RESOLVED_URL", "HTTP_STATUS", "ACCESSED_AT", "BYTES", "SHA256_HTML", "SHA256_TXT", "DC_TITLE", "TEXT_CHARS", "EVIDENCE_STATUS"]
write_csv(OUT / "OFFICIAL_TEXT_MANIFEST.csv", hdr, rows)
