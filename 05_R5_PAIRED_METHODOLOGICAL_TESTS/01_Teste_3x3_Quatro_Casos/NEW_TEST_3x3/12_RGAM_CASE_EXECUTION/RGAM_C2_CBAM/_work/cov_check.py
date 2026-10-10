import json, re, warnings
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
S = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C2_CBAM/LEGAL_SOURCE/32023R0956_official_en.xhtml"
soup = BeautifulSoup(open(S, encoding="utf-8").read(), "lxml")
units = json.load(open("units.json", encoding="utf-8"))
def norm(s): return re.sub(r"\s+", " ", s).strip()
big = " || ".join(norm(u["text"]) for u in units)
def strip_fn(t): return re.sub(r"\[FN\d+: .*?\]", "", t)
bigs = norm(strip_fn(big))
miss = 0
for p in soup.find_all("p"):
    cl = p.get("class") or []
    if any(c in cl for c in ("oj-hd-date","oj-hd-lg","oj-hd-ti","oj-hd-oj","oj-note","oj-ti-art","oj-sti-art")): continue
    t = norm(p.get_text(""))
    t = re.sub(r"\(\s*\d+\s*\)(?=[ ,.;)]|$)", lambda m: m.group(0), t)
    if not t: continue
    # remove footnote marker numerals like "(1)" attached to anchors
    for a in p.find_all("a"):
        sp = a.find("span", class_="oj-note-tag")
        if sp is not None: t = t.replace(norm(a.get_text("")), "")
    t = norm(t)
    if not t: continue
    if t not in bigs and t not in big:
        # tolerate label-only paragraphs
        if re.fullmatch(r"\(?[0-9a-zivx]+[.)]?|[\u2014]", t): continue
        miss += 1
        print("MISSING:", t[:120])
print("missing count", miss)
print("n units", len(units))
arts = sorted({int(u["article_or_annex_no"]) for u in units if u["structure_class"]=="OPERATIVE_ARTICLE"})
print("articles", len(arts), arts[0], arts[-1])
