"""R03 — Re-verify the R2 corpus (5 CELEX + excluded 32000D0293) against R3 manifests and fresh official texts.

Re-executed checks (read-only on sources):
  C1 R3 PDF SHA-256 == SOURCE_MANIFEST.yaml sha256
  C2 R3 corpus files SHA-256 (as-is and LF-normalised) == CORPUS_MANIFEST.yaml generated_file_sha256
  C3 article-number set in R3 article_index.csv == article headings in the fresh Cellar text (2026-09-30)
  C4 official title (R3 manifest) vs fresh Cellar text contains the act number
  C5 thematic sanity check (climate/greenhouse/emission term counts) — illustrates why 32000D0293 is a false positive
"""
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, PROJECT_ROOT, sha256, write_csv, now_iso  # noqa: E402

R3 = PROJECT_ROOT / "R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM"
OFF = RUN_ROOT / "01_BASELINES/official_texts"
ACTS = ["32003L0087", "32015D1814", "32018R0842", "32021R1119", "32023R0955"]
ACT_NO = {"32003L0087": "2003/87/EC", "32015D1814": "2015/1814", "32018R0842": "2018/842", "32021R1119": "2021/1119",
          "32023R0955": "2023/955", "32000D0293": "293/2000/EC"}


def yaml_val(text, key):
    m = re.search(rf"^\s*{re.escape(key)}:\s*\"?([^\"\n]*)\"?", text, re.M)
    return m.group(1).strip() if m else ""


def official_articles(celex):
    t = (OFF / f"{celex}.txt").read_text(encoding="utf-8")
    return t, [m.group(1) for m in re.finditer(r"(?m)^\s*Article (\d+[a-z]?)\s*$", t)]


rows = []
for c in ACTS + ["32000D0293"]:
    rec = dict(CELEX=c, CHECKED_AT=now_iso())
    t, arts = official_articles(c)
    rec["OFFICIAL_TEXT_SHA256"] = sha256(OFF / f"{c}.html")
    rec["OFFICIAL_ARTICLE_COUNT"] = len(arts)
    rec["C4_ACT_NUMBER_IN_OFFICIAL_TEXT"] = "PASS" if ACT_NO[c] in t else "FAIL"
    low = t.lower()
    rec["C5_TERM_COUNTS"] = f"climate={low.count('climate')}; greenhouse={low.count('greenhouse')}; emission={low.count('emission')}; environment={low.count('environment')}; violence={low.count('violence')}"
    if c in ACTS:
        man = (R3 / "01_sources" / c / "SOURCE_MANIFEST.yaml").read_text(encoding="utf-8")
        pdf = R3 / "01_sources" / c / "source_original_en.pdf"
        rec["R3_TITLE"] = yaml_val(man, "official_title")
        rec["R3_RETRIEVED_AT"] = yaml_val(man, "retrieved_at")
        rec["R3_DOCUMENT_STATUS"] = yaml_val(man, "document_status")
        rec["C1_PDF_HASH_MATCH"] = "PASS" if sha256(pdf) == yaml_val(man, "sha256").upper() else "FAIL"
        cm = (R3 / "02_corpus" / c / "CORPUS_MANIFEST.yaml").read_text(encoding="utf-8")
        res = []
        for fn in ["act_full.md", "recitals.md", "operative.md", "act_numbered.md", "article_index.csv"]:
            exp = yaml_val(cm, fn).upper()
            p = R3 / "02_corpus" / c / fn
            a, b = sha256(p), sha256(p, lf_normalize=True)
            res.append(f"{fn}:{'AS_IS' if a == exp else ('LF_NORMALIZED' if b == exp else 'MISMATCH')}")
        rec["C2_CORPUS_HASHES"] = "; ".join(res)
        rec["C2_STATUS"] = "FAIL" if "MISMATCH" in rec["C2_CORPUS_HASHES"] else "PASS"
        with open(R3 / "02_corpus" / c / "article_index.csv", newline="", encoding="utf-8") as f:
            r3arts = [r["value"] for r in csv.DictReader(f) if r["structural_level"] == "article"]
        rec["R3_ARTICLE_COUNT"] = len(r3arts)
        rec["C3_ARTICLE_SET_MATCH"] = "PASS" if sorted(set(r3arts)) == sorted(set(arts)) else f"FAIL (R3-only={sorted(set(r3arts)-set(arts))}; official-only={sorted(set(arts)-set(r3arts))})"
        rec["ROLE"] = "R2_CORPUS_MEMBER"
        rec["HISTORICAL_STATUS_CLAIM"] = "TEXTS_VERIFIED (learning log 13 Sep, line 279); R3 CORPUS_VALIDATED_WITH_DOCUMENTED_LIMITATIONS (R3_CORPUS_VALIDATION_REGISTER.csv)"
    else:
        rec["ROLE"] = "EXCLUDED_HISTORICAL_FALSE_POSITIVE"
        rec["HISTORICAL_STATUS_CLAIM"] = "In R1 S2 sample (R1 report ¶89); flagged as Daphne programme (¶90); excluded before R2 lock (learning log line 269/633); 'must NOT be reintroduced' (R3 operational prompt)"
        rec["C1_PDF_HASH_MATCH"] = rec["C2_STATUS"] = rec["C3_ARTICLE_SET_MATCH"] = "N/A (no R3 text; not in corpus)"
    rows.append(rec)

hdr = ["CELEX", "ROLE", "R3_TITLE", "R3_RETRIEVED_AT", "R3_DOCUMENT_STATUS", "OFFICIAL_TEXT_SHA256", "C1_PDF_HASH_MATCH", "C2_STATUS",
       "C2_CORPUS_HASHES", "R3_ARTICLE_COUNT", "OFFICIAL_ARTICLE_COUNT", "C3_ARTICLE_SET_MATCH", "C4_ACT_NUMBER_IN_OFFICIAL_TEXT",
       "C5_TERM_COUNTS", "HISTORICAL_STATUS_CLAIM", "CHECKED_AT"]
write_csv(RUN_ROOT / "03_R2/R2_CORPUS_RECONCILIATION.csv", hdr, rows)
for r in rows:
    print(r["CELEX"], r.get("C1_PDF_HASH_MATCH"), r.get("C2_STATUS"), r.get("C3_ARTICLE_SET_MATCH"), r["C4_ACT_NUMBER_IN_OFFICIAL_TEXT"], "|", r["C5_TERM_COUNTS"])
    print("   ", r.get("C2_CORPUS_HASHES", ""))
