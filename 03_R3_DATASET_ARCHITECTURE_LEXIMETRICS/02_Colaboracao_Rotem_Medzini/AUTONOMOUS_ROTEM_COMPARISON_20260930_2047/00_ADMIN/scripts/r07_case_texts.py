"""R07 — Build frozen, verbatim provision packs for the selected cases from the official texts (Cellar, 2026-09-30).

PROVISION_ID format: {CELEX}:A{article}({paragraph}) or {CELEX}:ANNEX_{label}({point}).
Every provision text is an exact substring of 01_BASELINES/official_texts/{CELEX}.txt (asserted).
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, sha256, write_csv  # noqa: E402
from textutil import article, load  # noqa: E402

OUTDIR = RUN_ROOT / "07_CASE_SELECTION/case_texts"
OUTDIR.mkdir(parents=True, exist_ok=True)


def paragraphs(block):
    """Split an article block into numbered paragraphs '1. ...', '2. ...' (returns dict num->text)."""
    # v2 (fix I-021): accept a paragraph marker only if it continues the 1, 2, 3 … sequence, so that
    # in-text numbers such as "Article 23. That submission" are not mistaken for paragraph starts.
    parts, idx, expect = {}, [], 1
    for m in re.finditer(r"(?:(?<=\n)|(?<=\s))(\d{1,2})\.\s(?=[A-Z‘'(])", block):
        if int(m.group(1)) == expect:
            idx.append((m.start(), m.group(1)))
            expect += 1
    for i, (pos, num) in enumerate(idx):
        end = idx[i + 1][0] if i + 1 < len(idx) else len(block)
        parts[num] = block[pos:end].strip()
    return parts


def between(text, start, end=None):
    i = text.index(start)
    j = text.index(end, i + len(start)) if end else len(text)
    return text[i:j].strip()


CASES = {
    "CASE_01": ("32004R0874", [
        ("A12(5)", lambda: paragraphs(article("32004R0874", 12))["5"]),
        ("A13", lambda: article("32004R0874", 13)),
        ("A14", lambda: article("32004R0874", 14).split("CHAPTER V")[0].strip()),
        ("A15(1)", lambda: paragraphs(article("32004R0874", 15))["1"]),
        ("A22(5)", lambda: paragraphs(article("32004R0874", 22))["5"]),
        ("A22(6)", lambda: paragraphs(article("32004R0874", 22))["6"]),
        ("A22(7)", lambda: paragraphs(article("32004R0874", 22))["7"]),
        ("A23(1)", lambda: paragraphs(article("32004R0874", 23))["1"]),
    ]),
    "CASE_02": ("31989L0336", [
        ("A10(2)", lambda: between(article("31989L0336", 10), "2. In the case of apparatus", "3. Where the standards")),
        ("A10(4)", lambda: paragraphs(article("31989L0336", 10))["4"]),
        ("A10(6)", lambda: paragraphs(article("31989L0336", 10))["6"]),
        ("ANNEX_II", lambda: between(load("31989L0336"), "ANNEX II \n Criteria for the assessment", "ANNEX III")),
    ]),
    "CASE_03": ("31991L0263", [
        ("A10(1)", lambda: between(load("31991L0263"), "Article 10 1. Member States shall notify", "2. Member States shall inform the Commission of test laboratories")),
        ("A10(2)", lambda: between(load("31991L0263"), "2. Member States shall inform the Commission of test laboratories", "3. The Commission shall publish the list of notified bodies")),
        ("A10(4)", lambda: between(load("31991L0263"), "4. A Member State has designated a notified body", "5. In order to facilitate")),
        ("ANNEX_III(3.1)", lambda: between(load("31991L0263"), "3.1.The manufacturer shall lodge", "3.2.The quality system")),
        ("ANNEX_III(3.3)", lambda: between(load("31991L0263"), "3.3.The notified body shall assess", "3.4.The manufacturer shall undertake")),
        ("ANNEX_III(3.4)", lambda: between(load("31991L0263"), "3.4.The manufacturer shall undertake", "4.Surveillance under the responsibility")),
        ("ANNEX_III(4)", lambda: between(load("31991L0263"), "4.Surveillance under the responsibility", "5.The manufacturer shall, for a period")),
        ("ANNEX_V(6)", lambda: between(load("31991L0263"), "6.The notified body must take out liability insurance", "7.The staff of the notified body")),
    ]),
    "CASE_04": ("31986L0361", [
        ("A2(8)", lambda: between(article("31986L0361", 2), "8. 'approved testing laboratory'", "9. 'certificate of conformity'")),
        ("A7(2)", lambda: paragraphs(article("31986L0361", 7))["2"]),
        ("A7(3)", lambda: paragraphs(article("31986L0361", 7))["3"]),
        ("A8(1)", lambda: between(article("31986L0361", 8), "1. A Member State may", "2. Where the decision")),
        ("A8(3)", lambda: between(article("31986L0361", 8), "3. If the reasons given", "4. If the reasons invoked")),
    ]),
    "CASE_05": ("32022R2065", [(f"A37({n})", (lambda n=n: paragraphs(article("32022R2065", 37))[str(n)])) for n in range(1, 8)] + [
        ("A42(4)", lambda: paragraphs(article("32022R2065", 42))["4"]),
    ]),
    "CASE_06": ("32022R2065", [(f"A22({n})", (lambda n=n: paragraphs(article("32022R2065", 22))[str(n)])) for n in range(1, 9)]),
}

reg = []
for case, (celex, provs) in CASES.items():
    full = load(celex)
    lines = [f"# {case} — verbatim provision pack ({celex})", "",
             f"Source: `01_BASELINES/official_texts/{celex}.txt` (SHA-256 {sha256(RUN_ROOT / '01_BASELINES/official_texts' / (celex + '.txt'))}); "
             f"retrieved from http://publications.europa.eu/resource/celex/{celex} on 2026-09-30. Texts below are exact substrings of the source (whitespace as rendered). "
             "EVIDENCE_STATUS = VERIFIED_OFFICIAL_URL.", ""]
    for loc, fn in provs:
        txt = fn()
        assert txt and txt in full, (case, loc)
        pid = f"{celex}:{loc}"
        lines += [f"## {pid}", "", txt, ""]
        reg.append(dict(CASE_ID=case, PROVISION_ID=pid, CELEX=celex, LOCATION=loc, CHARS=len(txt), EXACT_SUBSTRING_OF_OFFICIAL_TEXT="YES",
                        SOURCE_ID=f"OFF-{celex}", EVIDENCE_STATUS="VERIFIED_OFFICIAL_URL"))
    (OUTDIR / f"{case}_PROVISIONS.md").write_text("\n".join(lines), encoding="utf-8")
write_csv(RUN_ROOT / "07_CASE_SELECTION/PROVISION_PACK_REGISTER.csv", list(reg[0].keys()), reg)
for r in reg:
    print(r["PROVISION_ID"], r["CHARS"])
