# Mechanical structure dumper (exploratory): prints a depth-indented outline of the controlling source.
import sys, re
from bs4 import BeautifulSoup, NavigableString, Tag
S = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C2_CBAM/LEGAL_SOURCE/32023R0956_official_en.xhtml"
html = open(S, encoding="utf-8").read()
soup = BeautifulSoup(html, "lxml")
def txt(n):
    for im in n.find_all("img"):
        im.replace_with(" [IMAGE:%s] " % im.get("alt", ""))
    return re.sub(r"\s+", " ", n.get_text(" ")).strip()
def show(n, d=0):
    for c in n.children:
        if isinstance(c, Tag):
            if c.name == "p":
                print("  "*d + "P[%s] %s" % (",".join(c.get("class", [])), txt(c)[:150]))
            elif c.name == "table":
                rows = c.find_all("tr", recursive=False) or [r for tb in c.find_all("tbody", recursive=False) for r in tb.find_all("tr", recursive=False)]
                print("  "*d + "TABLE rows=%d" % len(rows))
                for r in rows:
                    tds = r.find_all("td", recursive=False)
                    print("  "*(d+1) + "ROW cells=%d" % len(tds))
                    for td in tds:
                        show(td, d+2)
            elif c.name in ("div", "figure", "span"):
                print("  "*d + "DIV[%s|%s]" % (c.get("id", ""), ",".join(c.get("class", []))))
                show(c, d+1)
if __name__ == "__main__":
    which = sys.argv[1]
    el = soup.find(id=which)
    show(el)
