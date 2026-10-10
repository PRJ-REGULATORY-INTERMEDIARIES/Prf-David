# MECHANICAL parser: splits the controlling XHTML into addressable units (no analysis).
import re, json, hashlib, sys, warnings, copy
from bs4 import BeautifulSoup, Tag, XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
CASE = "RGAM_C2_CBAM"
S = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C2_CBAM/LEGAL_SOURCE/32023R0956_official_en.xhtml"
W = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C2_CBAM/_work/"
soup = BeautifulSoup(open(S, encoding="utf-8").read(), "lxml")
warn = []


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def note_text(a):
    href = a.get("href", "")
    if not href.startswith("#"):
        return None
    n = soup.find(id=href[1:])
    if n is None:
        return None
    if n.name != "p":
        n = n.find_parent("p")
    t = norm(n.get_text(""))
    t = re.sub(r"^\(\s*\d+\s*\)\s*", "", t)
    return t


def txt(el):
    el = copy.copy(el)
    for im in el.find_all("img"):
        im.replace_with("[FORMULA_IMAGE alt=%s]" % im.get("alt", ""))
    for a in el.find_all("a"):
        sp = a.find("span", class_="oj-note-tag")
        if sp is not None and a.get("id", "").startswith("ntc"):
            nt = note_text(a)
            a.replace_with("[FN%s: %s]" % (sp.get_text("").strip(), nt))
    return norm(el.get_text(""))


units = []


def sha(t):
    return hashlib.sha256(norm(t).encode("utf-8")).hexdigest()


def add(uid, cls, art, para, point, parent, locator, text, anchor):
    units.append(dict(unit_id=CASE + "." + uid, structure_class=cls, article_or_annex_no=art, paragraph=para, point=point,
                      parent_unit_id=(CASE + "." + parent) if parent else "", locator_text=locator, text=text,
                      text_sha256=sha(text), source_anchor=anchor))


def label_of(cell_text):
    t = cell_text.strip()
    m = re.fullmatch(r"\(([0-9ivxlcdm]+|[a-z]{1,2})\)", t)
    if m:
        return m.group(1)
    m = re.fullmatch(r"([0-9]+)\.", t)
    if m:
        return m.group(1)
    if t in ("\u2014", "\u2013", "-"):
        return "-"
    return None


def kids(el):
    return [c for c in el.children if isinstance(c, Tag)]


def rows_of(t):
    return t.find_all("tr", recursive=False) or [r for tb in t.find_all("tbody", recursive=False) for r in tb.find_all("tr", recursive=False)]


def is_pointtable(t):
    if "oj-table" in (t.get("class") or []):
        return False
    rows = rows_of(t)
    if len(rows) != 1:
        return False
    tds = rows[0].find_all("td", recursive=False)
    return len(tds) == 2 and label_of(txt(tds[0])) is not None


def process(container, base, cls, art, para, locator, anchor, state):
    for c in kids(container):
        nm = c.name
        if nm == "p":
            if "oj-ti-art" in (c.get("class") or []) or "oj-sti-art" in (c.get("class") or []):
                continue
            t = txt(c)
            if not t:
                continue
            if not state["text_done"]:
                state["text"] = t
                state["text_done"] = True
            else:
                state["sub"] += 1
                add("%s.sub%d" % (base, state["sub"]), cls, art, para, "", base, locator + " (unnumbered subparagraph %d)" % state["sub"], t, anchor)
        elif nm == "table":
            if is_pointtable(c):
                row = rows_of(c)[0]
                tds = row.find_all("td", recursive=False)
                lab = label_of(txt(tds[0]))
                if lab == "-":
                    state["dash"] += 1
                    lab = "-%d" % state["dash"]
                pid = "%s.pt%s" % (base, lab)
                pstate = dict(text_done=False, sub=1, dash=0, text="")
                idx = len(units)
                units.append(None)
                process(tds[1], pid, cls, art, para, locator, anchor, pstate)
                units[idx] = dict(unit_id=CASE + "." + pid, structure_class=cls, article_or_annex_no=art, paragraph=para, point=lab,
                                  parent_unit_id=CASE + "." + base,
                                  locator_text=locator + (" point (%s)" % lab if not lab.startswith("-") else " dash point %s" % lab),
                                  text=pstate["text"], text_sha256=sha(pstate["text"]), source_anchor=anchor)
            else:
                warn.append("unclassified/data table in %s: %s" % (base, txt(c)[:80]))
        elif nm == "div":
            process(c, base, cls, art, para, locator, anchor, state)
        elif nm == "figure":
            t = txt(c)
            if t:
                state["sub"] += 1
                add("%s.sub%d" % (base, state["sub"]), cls, art, para, "", base, locator + " (figure)", t, anchor)
        else:
            warn.append("unhandled tag %s in %s" % (nm, base))


def emit_container(base, cls, art, para, parent, locator, anchor, container):
    state = dict(text_done=False, sub=1, dash=0, text="")
    idx = len(units)
    units.append(None)
    process(container, base, cls, art, para, locator, anchor, state)
    text = state["text"]
    units[idx] = dict(unit_id=CASE + "." + base, structure_class=cls, article_or_annex_no=art, paragraph=para, point="",
                      parent_unit_id=(CASE + "." + parent) if parent else "", locator_text=locator, text=text,
                      text_sha256=sha(text), source_anchor=anchor)


# ---------- FRONT MATTER ----------
ti = soup.find(id="tit_1")
add("TITLE", "FORMAL_OTHER", "title", "", "", "", "Title and type of act", txt(ti), "tit_1")
pbl = soup.find(id="pbl_1")
first = [c for c in kids(pbl) if c.name == "p"][0]
add("PREAMBLE_ADDRESS", "FORMAL_OTHER", "preamble", "", "", "", "Enacting authority formula", txt(first), "pbl_1")
for i in range(1, 7):
    d = soup.find(id="cit_%d" % i)
    add("CIT%d" % i, "FORMAL_OTHER", "citation", "", "", "", "Citation %d (Having regard)" % i, txt(d), "cit_%d" % i)
for i in range(1, 83):
    d = soup.find(id="rct_%d" % i)
    t = txt(d)
    t = re.sub(r"^\(%d\)\s*" % i, "", t)
    add("REC%d" % i, "RECITAL", "recital %d" % i, "", "", "", "Recital (%d)" % i, t, "rct_%d" % i)
for p in kids(pbl):
    if p.name == "p" and p.get_text().strip().startswith("Whereas"):
        add("WHEREAS", "FORMAL_OTHER", "preamble", "", "", "", "Recitals introductory formula", txt(p), "pbl_1")
    if p.name == "p" and "HAVE ADOPTED" in p.get_text():
        add("ENACT", "FORMAL_OTHER", "preamble", "", "", "", "Adoption formula", txt(p), "pbl_1/last-p")
# ---------- OPERATIVE PART ----------
enc = soup.find(id="enc_1")
for cpt in [c for c in kids(enc) if c.name == "div"]:
    cid = cpt.get("id")
    num = txt(cpt.find("p", class_="oj-ti-section-1"))
    title = txt(cpt.find("p", class_="oj-ti-section-2"))
    roman = num.replace("CHAPTER", "").strip()
    add("CH%s" % roman, "HEADING_ONLY", num, "", "", "", "%s - %s" % (num, title), "%s %s" % (num, title), cid)
    for art in cpt.find_all("div", class_="eli-subdivision", recursive=False):
        aid = art.get("id")
        if not (aid or "").startswith("art_"):
            warn.append("non-article subdivision %s in %s" % (aid, cid))
            continue
        n = int(aid.split("_")[1])
        atitle = txt(art.find("div", class_="eli-title"))
        loc = "Article %d (%s)" % (n, atitle)
        numbered = [d for d in art.find_all("div", recursive=False) if re.fullmatch(r"\d{3}\.\d{3}", d.get("id", ""))]
        if numbered:
            for c in kids(art):
                if c.name == "p" and ("oj-ti-art" in (c.get("class") or [])):
                    continue
                if c.name == "div" and ("eli-title" in (c.get("class") or []) or re.fullmatch(r"\d{3}\.\d{3}", c.get("id", ""))):
                    continue
                warn.append("art %d: content outside numbered paragraphs: %s %s" % (n, c.name, txt(c)[:80]))
            for d in numbered:
                k = int(d.get("id").split(".")[1])
                emit_container("A%d.P%d" % (n, k), "OPERATIVE_ARTICLE", str(n), str(k), "", "%s paragraph %d" % (loc, k), d.get("id"), d)
        else:
            emit_container("A%d.P0" % n, "OPERATIVE_ARTICLE", str(n), "0", "", loc + " (single paragraph / unnumbered)", aid, art)
# ---------- FINAL ----------
fin = soup.find(id="fnp_1").find("div", class_="oj-final")
ps = [c for c in kids(fin) if c.name == "p"]
add("FINAL.P1", "FORMAL_OTHER", "final", "1", "", "", "Final formula", txt(ps[0]), "fnp_1")
add("FINAL.P2", "FORMAL_OTHER", "final", "2", "", "", "Place and date", txt(ps[1]), "fnp_1")
for i, sg in enumerate([c for c in kids(fin) if c.name == "div"], 1):
    add("FINAL.SIG%d" % i, "FORMAL_OTHER", "final", "", "", "", "Signatory block %d" % i, txt(sg), "fnp_1/sig%d" % i)
# ---------- ANNEXES ----------
ANX_IDS = ["anx_I", "anx_II", "anx_III", "anx_IV", "anx_V", "anx_VI"]
roman2int = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6}
for aid in ANX_IDS:
    ac = soup.find(id=aid)
    if ac is None:
        for d in soup.find_all("div", class_="eli-container"):
            t = d.find("p", class_="oj-doc-ti")
            if t and norm(t.get_text("")) == "ANNEX " + aid.split("_")[1]:
                ac = d
    ptitles = ac.find_all("p", class_="oj-doc-ti", recursive=False)
    rn = norm(ptitles[0].get_text("")).replace("ANNEX", "").strip()
    n = roman2int[rn]
    atitle = norm(ptitles[1].get_text(""))
    loc = "Annex %s (%s)" % (rn, atitle)
    base = "ANX%d" % n
    section = None
    catn = 0
    pcount = {}
    pending_cat = None
    for c in kids(ac):
        cl = c.get("class") or []
        if c.name == "p" and "oj-doc-ti" in cl:
            continue
        if c.name == "div" and "oj-enumeration-spacing" in cl:
            t = txt(c)
            m = re.match(r"^(\d+)\.\s+", t)
            lab = m.group(1) if m else "?"
            add("%s.pt%s" % (base, lab), "ANNEX", rn, "", lab, "", "%s point %s" % (loc, lab), t, aid)
            section = None
        elif c.name == "p" and "oj-ti-grseq-1" in cl:
            t = txt(c)
            m = re.match(r"^(\d+(?:\.\d+)*)\.?\s+(.*)$", t)
            if m:
                lab = m.group(1)
                section = lab
                pcount[section] = 0
                parent = ""
                if "." in lab:
                    parent = "%s.pt%s" % (base, lab.rsplit(".", 1)[0])
                    if not any(u["unit_id"] == CASE + "." + parent for u in units):
                        parent = "%s.pt%s" % (base, lab.split(".")[0])
                kindcls = "ANNEX" if t.rstrip().endswith(":") else "HEADING_ONLY"
                add("%s.pt%s" % (base, lab), kindcls, rn, "", lab, parent, "%s section %s" % (loc, lab), t, aid)
            else:
                pending_cat = t
                section = None
        elif c.name == "p" and "oj-note" in cl:
            continue  # footnote body: already inlined at its marker
        elif c.name == "p" and c.find_next_sibling() is not None and c.find_next_sibling().name == "table" and "oj-table" in (c.find_next_sibling().get("class") or []):
            pending_cat = txt(c)  # category heading printed as ordinary paragraph immediately before a data table
            section = None
        elif c.name == "p":
            t = txt(c)
            if not t:
                continue
            if section is None:
                pcount[None] = pcount.get(None, 0) + 1
                add("%s.P%d" % (base, pcount[None]), "ANNEX", rn, str(pcount[None]), "", "", "%s paragraph %d" % (loc, pcount[None]), t, aid)
            else:
                pcount[section] += 1
                add("%s.pt%s.P%d" % (base, section, pcount[section]), "ANNEX", rn, "", section, "%s.pt%s" % (base, section),
                    "%s section %s paragraph %d" % (loc, section, pcount[section]), t, aid)
        elif c.name == "table":
            if "oj-table" in cl:
                catn += 1
                lines = []
                for r in c.find_all("tr"):
                    cells = [txt(td) for td in r.find_all("td", recursive=False)]
                    lines.append(" | ".join(cells))
                head = pending_cat or ""
                t = (head + " :: " if head else "") + " ;; ".join(lines)
                add("%s.TBL%d" % (base, catn), "ANNEX", rn, "", "", "", "%s table %d%s" % (loc, catn, (" - " + head) if head else ""), t, aid)
                pending_cat = None
            elif is_pointtable(c):
                row = rows_of(c)[0]
                tds = row.find_all("td", recursive=False)
                lab = label_of(txt(tds[0]))
                par = "%s.pt%s" % (base, section) if section else base
                if lab == "-":
                    pcount[("dash", par)] = pcount.get(("dash", par), 0) + 1
                    lab = "-%d" % pcount[("dash", par)]
                pid = "%s.pt%s" % (par, lab)
                pstate = dict(text_done=False, sub=1, dash=0, text="")
                idx = len(units)
                units.append(None)
                process(tds[1], pid, "ANNEX", rn, "", loc, aid, pstate)
                units[idx] = dict(unit_id=CASE + "." + pid, structure_class="ANNEX", article_or_annex_no=rn, paragraph="", point=lab,
                                  parent_unit_id=(CASE + "." + par) if section else "",
                                  locator_text="%s section %s point (%s)" % (loc, section or "-", lab),
                                  text=pstate["text"], text_sha256=sha(pstate["text"]), source_anchor=aid)
            else:
                catn += 1
                lines = []
                for r in c.find_all("tr"):
                    cells = [txt(td) for td in r.find_all("td", recursive=False)]
                    lines.append(" | ".join(cells))
                par = "%s.pt%s" % (base, section) if section else base
                add("%s.TBL%d" % (par, catn), "ANNEX", rn, "", section or "", (par if section else ""), "%s section %s legend/definition table" % (loc, section or "-"), " ;; ".join(lines), aid)
        elif c.name == "hr":
            warn.append("annex %s hr skipped" % rn)
        else:
            warn.append("annex %s: unhandled %s %s" % (rn, c.name, txt(c)[:100]))
units = [u for u in units if u is not None]
# source order: the "Whereas:" formula precedes the recitals
_w = [u for u in units if u["unit_id"].endswith(".WHEREAS")][0]
units.remove(_w)
_i = [i for i, u in enumerate(units) if u["unit_id"].endswith(".REC1")][0]
units.insert(_i, _w)
ids = [u["unit_id"] for u in units]
dups = set(i for i in ids if ids.count(i) > 1)
json.dump(units, open(W + "units.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
with open(W + "units.txt", "w", encoding="utf-8") as f:
    for u in units:
        f.write("### %s [%s]\n%s\n\n" % (u["unit_id"].replace(CASE + ".", ""), u["structure_class"], u["text"]))
print("units:", len(units), "dups:", dups)
from collections import Counter
print(Counter(u["structure_class"] for u in units))
for w in warn:
    print("WARN", w)
