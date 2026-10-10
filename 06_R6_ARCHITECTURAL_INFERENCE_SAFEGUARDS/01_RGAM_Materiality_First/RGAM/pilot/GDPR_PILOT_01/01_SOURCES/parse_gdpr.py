"""Parse EUR-Lex XHTML of Regulation (EU) 2016/679 into article / paragraph units.
Deterministic, no interpretation. Usage: python parse_gdpr.py
Outputs (in ../01_SOURCES/parsed/): original_units.json, consolidated_units.json, textdiff.json
"""
import json, re, hashlib, os, sys, html
from bs4 import BeautifulSoup

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw")
OUT = os.path.join(BASE, "parsed")
os.makedirs(OUT, exist_ok=True)


def norm(t):
    t = html.unescape(t).replace("\xa0", " ")
    return re.sub(r"\s+", " ", t).strip()


def parse(path, consolidated=False):
    soup = BeautifulSoup(open(path, encoding="utf-8", errors="ignore").read(), "lxml")
    units = []
    recitals = []
    # recitals
    for d in soup.select("div.eli-subdivision[id^=rct_]"):
        rid = d.get("id")
        recitals.append({"id": rid, "text": norm(d.get_text(" "))})
    chapter = None
    section = None
    arts = []
    # walk in document order through chapter / section / article divs
    for d in soup.find_all("div", class_="eli-subdivision"):
        did = d.get("id", "")
        if did.startswith("cpt_") and "." not in did:
            t = d.find("p", class_="oj-ti-section-1")
            tt = d.find("div", class_="eli-title")
            chapter = norm((t.get_text(" ") if t else "") + " " + (tt.get_text(" ") if tt else ""))
            section = None
        elif did.startswith("cpt_") and ".sct_" in did:
            t = d.find("p", class_="oj-ti-section-2")
            tt = d.find("div", class_="eli-title")
            section = norm((t.get_text(" ") if t else "") + " " + (tt.get_text(" ") if tt else ""))
        elif re.fullmatch(r"art_\d+", did):
            n = int(did[4:])
            title_div = d.find("div", class_="eli-title")
            title = norm(title_div.get_text(" ")) if title_div else ""
            # chapter assignment from enclosing cpt
            enc = d.find_parent("div", id=re.compile(r"^cpt_[IVX]+$"))
            ch = enc.get("id") if enc else None
            sec_enc = d.find_parent("div", id=re.compile(r"^cpt_[IVX]+\.sct_\d+$"))
            sc = sec_enc.get("id") if sec_enc else None
            # paragraphs: child divs with numeric ids like 042.001, or single-paragraph articles
            paras = []
            for pd in d.find_all("div", recursive=False):
                pid = pd.get("id", "")
                if re.fullmatch(r"\d{3}\.\d{3}", pid):
                    paras.append((pid, pd))
            if not paras:
                # article without numbered paragraphs: use direct <p class=oj-normal> and tables
                paras = [(f"{n:03d}.000", d)]
            for pid, pd in paras:
                # main text: first p.oj-normal, then points
                parts = []
                for el in pd.find_all(["p", "table"], recursive=True):
                    if el.name == "p" and ("oj-ti-art" in (el.get("class") or []) or "oj-sti-art" in (el.get("class") or [])):
                        continue
                    if el.name == "table":
                        for tr in el.find_all("tr"):
                            cells = [norm(c.get_text(" ")) for c in tr.find_all("td")]
                            parts.append(" ".join(cells))
                    elif el.name == "p" and el.find_parent("table") is None:
                        parts.append(norm(el.get_text(" ")))
                text = " ".join(x for x in parts if x)
                m = re.match(r"^(\d+)\.\s+(.*)$", text)
                label = m.group(1) if m else "0"
                units.append({
                    "article": n, "article_title": title, "chapter_id": ch, "section_id": sc,
                    "unit_id": f"GDPR.A{n}.P{label}", "div_id": pid, "para_label": label, "text": text,
                })
    return units, recitals


def main():
    o_units, o_rec = parse(os.path.join(RAW, "gdpr_eurlex_html.html"))
    c_units, c_rec = parse(os.path.join(RAW, "corr_02016R0679-20160504.html"), consolidated=True)
    json.dump({"units": o_units, "recitals": o_rec}, open(os.path.join(OUT, "original_units.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump({"units": c_units, "recitals": c_rec}, open(os.path.join(OUT, "consolidated_units.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("original: articles", len({u['article'] for u in o_units}), "units", len(o_units), "recitals", len(o_rec))
    print("consolidated: articles", len({u['article'] for u in c_units}), "units", len(c_units), "recitals", len(c_rec))
    # diff
    od = {u["unit_id"]: u["text"] for u in o_units}
    cd = {u["unit_id"]: u["text"] for u in c_units}
    diffs = []
    for k in sorted(set(od) | set(cd), key=lambda x: (int(x.split(".A")[1].split(".")[0]), x)):
        if od.get(k) != cd.get(k):
            diffs.append({"unit_id": k, "original": od.get(k), "consolidated": cd.get(k)})
    json.dump(diffs, open(os.path.join(OUT, "textdiff.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("units differing between original and consolidated:", len(diffs))
    for d in diffs:
        print(" -", d["unit_id"])
    rd = {r["id"]: r["text"] for r in o_rec}
    rc = {r["id"]: r["text"] for r in c_rec}
    print("recitals differing:", [k for k in rd if rd.get(k) != rc.get(k)])


if __name__ == "__main__":
    main()
