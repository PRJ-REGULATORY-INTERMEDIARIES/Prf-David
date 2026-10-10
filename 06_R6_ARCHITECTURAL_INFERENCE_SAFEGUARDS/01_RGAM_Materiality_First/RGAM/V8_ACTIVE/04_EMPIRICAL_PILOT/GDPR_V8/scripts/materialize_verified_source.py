"""Materialize a fresh, reproducible GDPR working text from verified official files.

This runner reuses only the prior project's deterministic parsing utility and raw
official EUR-Lex files. It imports no prior analytical records or classifications.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[5]
UTILITY = ROOT / "RGAM" / "pilot" / "GDPR_PILOT_01" / "01_SOURCES" / "build_working_text.py"
RAW = ROOT / "RGAM" / "pilot" / "GDPR_PILOT_01" / "01_SOURCES" / "raw"
OUT = Path(__file__).resolve().parents[1] / "01_SOURCES"

EXPECTED = {
    "gdpr_eurlex_html.html": "b5085317e90f6cc77bed4867b22de17a9bc0719e663b9f0bab1f59474fe622fd",
    "corr_32016R0679R02.html": "52c9966557c1b4549d3580b02442e1c0defcd9f304ef90d72974d106f524f7e8",
    "corr_02016R0679-20160504.html": "7d8d3263e23108b0d9bcbd5326aad916a9aeeae2ed365145b9335f2a9e3d3144",
}

for name, expected in EXPECTED.items():
    actual = hashlib.sha256((RAW / name).read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f"Integrity failure: {name}: {actual}")

spec = spec_from_file_location("verified_parser", UTILITY)
module = module_from_spec(spec)
spec.loader.exec_module(module)
module.BASE = str(OUT)
module.RAW = str(RAW)
module.OUT = str(OUT)
OUT.mkdir(parents=True, exist_ok=True)
module.main()
