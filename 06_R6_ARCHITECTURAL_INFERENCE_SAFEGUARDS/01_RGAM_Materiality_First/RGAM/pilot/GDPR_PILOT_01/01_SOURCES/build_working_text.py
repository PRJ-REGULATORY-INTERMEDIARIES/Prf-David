"""Build the Pilot 01 working text of Regulation (EU) 2016/679 from the authentic OJ L 119 XHTML.
Steps: (1) deterministic parse into paragraph units with point sub-units; (2) apply the 2018 corrigendum
(OJ L 127, 23.5.2018, p. 2) to the affected units; (3) emit JSON/CSV inventories and a change log.
No interpretation is performed. Run: python build_working_text.py
"""
import json, re, os, csv, html, hashlib, warnings
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore")

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw")
OUT = os.path.join(BASE, "parsed")
os.makedirs(OUT, exist_ok=True)


def norm(t):
    t = html.unescape(t).replace("\xa0", " ")
    return re.sub(r"\s+", " ", t).strip()


def top_level(el, name_set):
    """descendant elements of given names not nested inside a table (for p) or another table (for table)."""
    out = []
    for x in el.find_all(list(name_set)):
        if x.name == "p" and x.find_parent("table") is not None:
            continue
        if x.name == "table" and x.find_parent("table") is not None:
            continue
        out.append(x)
    return out


def table_points(tb):
    pts = []
    for tr in tb.find_all("tr", recursive=False) or tb.find_all("tr"):
        if tr.find_parent("table") is not tb:
            continue
        tds = tr.find_all("td", recursive=False)
        if len(tds) >= 2:
            lab = norm(tds[0].get_text(" "))
            body = norm(" ".join(x.get_text(" ") for x in tds[1:]))
            pts.append((lab, body))
        elif len(tds) == 1:
            pts.append(("", norm(tds[0].get_text(" "))))
    return pts


def parse_article(d, n):
    paras = [(pd.get("id"), pd) for pd in d.find_all("div", recursive=False) if re.fullmatch(r"\d{3}\.\d{3}", pd.get("id", ""))]
    if not paras:
        paras = [(f"{n:03d}.000", d)]
    res = []
    for pid, pd in paras:
        lead_parts, points = [], []
        for el in top_level(pd, {"p", "table"}):
            if el.name == "p":
                cls = el.get("class") or []
                if "oj-ti-art" in cls or "oj-sti-art" in cls:
                    continue
                lead_parts.append(norm(el.get_text(" ")))
            else:
                points.extend(table_points(el))
        lead = " ".join(lead_parts)
        m = re.match(r"^(\d+)\.\s+(.*)$", lead)
        label = m.group(1) if m else "0"
        res.append({"div_id": pid, "para_label": label, "lead": lead, "points": points})
    return res


def parse_original(path):
    soup = BeautifulSoup(open(path, encoding="utf-8", errors="ignore").read(), "lxml")
    recitals = []
    for d in soup.select("div.eli-subdivision[id^=rct_]"):
        recitals.append({"id": d.get("id"), "number": int(d.get("id").split("_")[1]), "text": norm(d.get_text(" "))})
    chap_titles, sec_titles = {}, {}
    for d in soup.find_all("div", class_="eli-subdivision"):
        did = d.get("id", "")
        if re.fullmatch(r"cpt_[IVX]+", did):
            t = d.find("p", class_="oj-ti-section-1"); tt = d.find("div", class_="eli-title")
            chap_titles[did] = norm((t.get_text(" ") if t else "") + " " + (tt.get_text(" ") if tt else ""))
        elif re.fullmatch(r"cpt_[IVX]+\.sct_\d+", did):
            t = d.find("p", class_="oj-ti-section-2"); tt = d.find("div", class_="eli-title")
            sec_titles[did] = norm((t.get_text(" ") if t else "") + " " + (tt.get_text(" ") if tt else ""))
    arts = []
    for d in soup.find_all("div", class_="eli-subdivision"):
        did = d.get("id", "")
        if re.fullmatch(r"art_\d+", did):
            n = int(did[4:])
            td = d.find("div", class_="eli-title")
            enc = d.find_parent("div", id=re.compile(r"^cpt_[IVX]+$"))
            sec = d.find_parent("div", id=re.compile(r"^cpt_[IVX]+\.sct_\d+$"))
            arts.append({"article": n, "title": norm(td.get_text(" ")) if td else "",
                         "chapter_id": enc.get("id") if enc else None,
                         "chapter": chap_titles.get(enc.get("id")) if enc else None,
                         "section_id": sec.get("id") if sec else None,
                         "section": sec_titles.get(sec.get("id")) if sec else None,
                         "paragraphs": parse_article(d, n)})
    return arts, recitals


# --- 2018 corrigendum (OJ L 127, 23.5.2018, p. 2): (article, paragraph label or None, point label or None, old, new)
CORR = [
    (37, "1", "(c)", "special categories of data pursuant to Article 9 and personal data relating to criminal convictions", "special categories of data pursuant to Article 9 or personal data relating to criminal convictions"),
    (41, "3", None, "draft criteria for accreditation", "draft requirements for accreditation"),
    (41, "5", None, "if the conditions for accreditation are not, or are no longer, met", "if the requirements for accreditation are not, or are no longer, met"),
    (42, "7", None, "provided that the relevant requirements continue to be met", "provided that the relevant criteria continue to be met"),
    (42, "7", None, "where the requirements for the certification are not or are no longer met", "where the criteria for the certification are not or are no longer met"),
    (43, "3", None, "shall take place on the basis of criteria approved", "shall take place on the basis of requirements approved"),
    (43, "6", None, " The Board shall collate all certification mechanisms and data protection seals in a register and shall make them publicly available by any appropriate means.", ""),
    (57, "1", "(p)", "draft and publish the criteria for accreditation", "draft and publish the requirements for accreditation"),
    (64, "1", "(c)", "aims to approve the criteria for accreditation of a body pursuant to Article 41(3) or a certification body pursuant to Article 43(3);", "aims to approve the requirements for accreditation of a body pursuant to Article 41(3), of a certification body pursuant to Article 43(3) or the criteria for certification referred to in Article 42(5);"),
    (64, "6", None, "The competent supervisory authority shall not adopt its draft decision referred to in paragraph 1 within the period", "The competent supervisory authority referred to in paragraph 1 shall not adopt its draft decision referred to in paragraph 1 within the period"),
    (64, "7", None, "The supervisory authority referred to in paragraph 1 shall take utmost account", "The competent supervisory authority referred to in paragraph 1 shall take utmost account"),
    (64, "8", None, "Where the supervisory authority concerned informs the Chair", "Where the competent supervisory authority referred to in paragraph 1 informs the Chair"),
    (65, "1", "(a)", "a draft decision of the lead authority or the lead authority has rejected such an objection as being not relevant or reasoned", "a draft decision of the lead supervisory authority and the lead supervisory authority has not followed the objection or has rejected such an objection as being not relevant or reasoned"),
    (69, "2", None, "requests by the Commission referred to in point (b) of Article 70(1) and in Article 70(2)", "requests by the Commission referred to in Article 70(1) and (2)"),
    (70, "1", "(l)", "guidelines, recommendations and best practices referred to in points (e) and (f);", "guidelines, recommendations and best practices;"),
    (70, "1", "(o)", "carry out the accreditation of certification bodies and its periodic review pursuant to Article 43 and maintain a public register of accredited bodies pursuant to Article 43(6) and of the accredited controllers or processors established in third countries pursuant to Article 42(7);", "approve the criteria of certification pursuant to Article 42(5) and maintain a public register of certification mechanisms and data protection seals and marks pursuant to Article 42(8) and of the certified controllers or processors established in third countries pursuant to Article 42(7);"),
    (70, "1", "(p)", "specify the requirements referred to in Article 43(3) with a view to the accreditation of certification bodies under Article 42;", "approve the requirements referred to in Article 43(3) with a view to the accreditation of certification bodies referred to in Article 43;"),
]
REC71_OLD = "secure personal data in a manner that takes account of the potential risks involved for the interests and rights of the data subject and that prevents, inter alia, discriminatory effects"
REC71_NEW = "secure personal data in a manner that takes account of the potential risks involved for the interests and rights of the data subject, and prevent, inter alia, discriminatory effects"
REC71_OLD2 = "or that result in measures having such an effect"
REC71_NEW2 = "or processing that results in measures having such an effect"


def apply_corr(arts, recitals):
    log = []
    for (n, pl, ptl, old, new) in CORR:
        a = next(x for x in arts if x["article"] == n)
        p = next(x for x in a["paragraphs"] if x["para_label"] == pl)
        done = False
        if ptl:
            for i, (lab, body) in enumerate(p["points"]):
                if lab == ptl and old in body:
                    p["points"][i] = (lab, body.replace(old, new)); done = True
                    break
        else:
            if old in p["lead"]:
                p["lead"] = p["lead"].replace(old, new); done = True
            else:
                for i, (lab, body) in enumerate(p["points"]):
                    if old in body:
                        p["points"][i] = (lab, body.replace(old, new)); done = True
                        break
        log.append({"article": n, "paragraph": pl, "point": ptl, "applied": done, "old": old, "new": new})
    for r in recitals:
        if r["number"] == 71:
            ok1 = REC71_OLD in r["text"]; ok2 = REC71_OLD2 in r["text"]
            r["text"] = r["text"].replace(REC71_OLD, REC71_NEW).replace(REC71_OLD2, REC71_NEW2)
            log.append({"article": "recital 71", "applied": ok1 and ok2, "old": REC71_OLD + " | " + REC71_OLD2, "new": REC71_NEW + " | " + REC71_NEW2})
    return log


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    arts, recitals = parse_original(os.path.join(RAW, "gdpr_eurlex_html.html"))
    orig = json.loads(json.dumps(arts))
    log = apply_corr(arts, recitals)
    json.dump({"articles": arts, "recitals": recitals}, open(os.path.join(OUT, "working_text.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(orig, open(os.path.join(OUT, "original_articles_uncorrected.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(log, open(os.path.join(OUT, "corrigendum_application_log.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rows = []
    for a in arts:
        for p in a["paragraphs"]:
            base = f"GDPR.A{a['article']}.P{p['para_label']}"
            full = p["lead"] + " " + " ".join(f"{l} {b}" for l, b in p["points"])
            rows.append({"unit_id": base, "kind": "paragraph", "article": a["article"], "article_title": a["title"], "paragraph": p["para_label"], "point": "", "chapter": a["chapter_id"], "section": a["section_id"] or "", "chars": len(full), "n_points": len(p["points"]), "text_sha256_16": hashlib.sha256(full.encode()).hexdigest()[:16]})
            for l, b in p["points"]:
                lab = l.strip("()") or "x"
                rows.append({"unit_id": f"{base}.pt{lab}", "kind": "point", "article": a["article"], "article_title": a["title"], "paragraph": p["para_label"], "point": l, "chapter": a["chapter_id"], "section": a["section_id"] or "", "chars": len(b), "n_points": 0, "text_sha256_16": hashlib.sha256(b.encode()).hexdigest()[:16]})
    with open(os.path.join(BASE, "SOURCE_UNIT_INVENTORY.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("articles", len(arts), "paragraph units", sum(1 for r in rows if r["kind"] == "paragraph"), "point units", sum(1 for r in rows if r["kind"] == "point"), "recitals", len(recitals))
    print("corrigendum items applied:", sum(1 for x in log if x["applied"]), "of", len(log))
    for x in log:
        if not x["applied"]:
            print("NOT APPLIED:", x["article"], x.get("paragraph"), x.get("point"))
    print("sha256 original html:", sha(os.path.join(RAW, "gdpr_eurlex_html.html")))


if __name__ == "__main__":
    main()
