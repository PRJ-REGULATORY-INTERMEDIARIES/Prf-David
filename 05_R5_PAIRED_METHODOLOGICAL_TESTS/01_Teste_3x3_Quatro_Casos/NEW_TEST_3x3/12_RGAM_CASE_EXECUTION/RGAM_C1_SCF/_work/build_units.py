# MECHANICAL ONLY: parse the capsule source into addressable units (no analysis).
import warnings, re, json, hashlib, base64, os
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup
CASE = "RGAM_C1_SCF"
SRC = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/LEGAL_SOURCE/32023R0955_official_en.html"
soup = BeautifulSoup(open(SRC, encoding='utf-8').read(), 'lxml')


def norm(t):
    return re.sub(r'\s+', ' ', t.replace('\xa0', ' ')).strip()


def txt(el):
    return norm(el.get_text(' '))


units = []


def strip_case(x):
    return x[len(CASE) + 1:] if x.startswith(CASE + '.') else x


def add(uid, cls, art, para, pt, parent, loc, text, anchor):
    units.append(dict(unit_id=f"{CASE}.{strip_case(uid)}", structure_class=cls,
                      article_or_annex_no=art, paragraph=para, point=pt,
                      parent_unit_id=(f"{CASE}.{strip_case(parent)}" if parent else ""),
                      locator_text=loc, text=text, source_anchor=anchor))


MARK = re.compile(r'^\(?([0-9]{1,3}|[a-z]{1,4}|[ivxlc]{1,6})[\.\)]?\)?$|^[—–-]$')


def is_marker(s):
    return bool(MARK.match(s))


def label_of(m):
    mm = re.match(r'^\(?([0-9a-z]+)[\.\)]?\)?$', m.strip())
    return mm.group(1) if mm else None


def rows_of(table):
    tb = table.find('tbody', recursive=False) or table
    return tb.find_all('tr', recursive=False)


def cell_parts(node):
    seq = []

    def rec(n_):
        for c in n_.children:
            n = getattr(c, 'name', None)
            if n is None:
                continue
            if n == 'p':
                seq.append(('p', c))
            elif n == 'table':
                seq.append(('t', c))
            elif n == 'span' and not c.find(['p', 'table']):
                if txt(c):
                    seq.append(('p', c))
            elif n in ('span', 'div', 'figure'):
                rec(c)
    rec(node)
    return seq


def lead_text(seq):
    out = []
    for k, e in seq:
        if k == 't':
            break
        out.append(txt(e))
    return norm(' '.join(out))


CLS = ["OPERATIVE_ARTICLE"]


def handle_table(table, parent_id, art, para, loc, anchor, top=False, counter=None):
    rows = rows_of(table)
    if len(rows) == 1:
        tds = rows[0].find_all('td', recursive=False)
        mi = None
        if len(tds) == 2 and is_marker(txt(tds[0])):
            mi = 0
        elif len(tds) == 3 and txt(tds[0]) == '' and is_marker(txt(tds[1])):
            mi = 1
        elif len(tds) == 3 and is_marker(txt(tds[0])):
            mi = 0
        if mi is not None:
            marker = txt(tds[mi])
            content = tds[-1]
            lab = label_of(marker)
            if counter is not None and top:
                counter[0] += 1
                uid = f"{parent_id}.pt{counter[0]}"
            else:
                if lab is None:
                    lab = f"u{len(units)}"
                uid = f"{parent_id}.pt{lab}"
            seq = cell_parts(content)
            ptxt = lead_text(seq)
            if not ptxt and not any(k == 't' for k, _ in seq):
                ptxt = f"[marker only; no text in source cell] {marker}"
            add(uid, CLS[0], art, para, marker, parent_id, f"{loc} item {marker}", ptxt, anchor)
            after = False
            cont = 0
            cur = uid
            for k, e in seq:
                if k == 't':
                    after = True
                    handle_table(e, cur, art, para, f"{loc} item {marker}", anchor, False, None)
                elif after and txt(e):
                    cont += 1
                    cur = f"{uid}.cont{cont}"
                    add(cur, CLS[0], art, para, marker + " (continuation)", uid,
                        f"{loc} item {marker} continuation", txt(e), anchor)
            return
    for ri, r in enumerate(rows, 1):
        tds = r.find_all('td', recursive=False)
        t = ' | '.join(txt(td) for td in tds if txt(td))
        if not t:
            continue
        if counter is not None and top:
            counter[0] += 1
            uid = f"{parent_id}.pt{counter[0]}"
        else:
            uid = f"{parent_id}.row{ri}"
        add(uid, CLS[0], art, para, f"table row {ri}", parent_id, f"{loc} table row {ri}", t, anchor)


def emit_paragraph(container, aid, art, paraname, anchor):
    seq = cell_parts(container)
    add(aid, "OPERATIVE_ARTICLE", art, paraname, "", "", f"Article {art}, paragraph {paraname}", lead_text(seq), anchor)
    after = False
    cont = 0
    cur = aid
    for k, e in seq:
        if k == 't':
            after = True
            handle_table(e, cur, art, paraname, f"Article {art}, paragraph {paraname}", anchor)
        elif after and txt(e):
            cont += 1
            cur = f"{aid}.cont{cont}"
            add(cur, "OPERATIVE_ARTICLE", art, paraname, "(continuation)", aid,
                f"Article {art}, paragraph {paraname} continuation (subparagraph following enumerated points)", txt(e), anchor)


# ---- preamble
hdr_t = soup.body.find('table')
add("HDR", "FORMAL_OTHER", "", "", "", "", "Official Journal page header", norm(' '.join(txt(p) for p in hdr_t.find_all('p'))), "header table")
tit = soup.find(id='tit_1')
add("TITLE", "FORMAL_OTHER", "", "", "", "", "Title and date of the act", norm(' '.join(txt(p) for p in tit.find_all('p'))), "tit_1")
pbl = soup.find(id='pbl_1')
add("PBL", "FORMAL_OTHER", "", "", "", "", "Preamble: institution formula", txt(pbl.find('p', recursive=False)), "pbl_1")
for i in range(1, 7):
    d = soup.find(id=f'cit_{i}')
    add(f"CIT{i}", "FORMAL_OTHER", "", "", "", "", f"Citation {i}", txt(d), f"cit_{i}")
add("WHR", "FORMAL_OTHER", "", "", "", "", "Preamble: 'Whereas:' formula", [txt(p) for p in pbl.find_all('p', recursive=False) if txt(p).startswith('Whereas')][0], "pbl_1 whereas")
for i in range(1, 48):
    d = soup.find(id=f'rct_{i}')
    tds = d.find_all('td')
    t = norm(' '.join(txt(td) for td in tds[1:])) if tds else txt(d)
    add(f"REC{i}", "RECITAL", str(i), "", "", "", f"Recital ({i})", t, f"rct_{i}")
add("ENC", "FORMAL_OTHER", "", "", "", "", "Enacting formula", txt(pbl.find_all('p', recursive=False)[-1]), "pbl_1/last p")

# ---- chapters & articles
body = soup.find(id='enc_1')
NUM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
for cpt in body.find_all('div', recursive=False):
    cid = cpt['id'].replace('cpt_', '')
    nm = NUM[cid]
    ps = cpt.find_all('p', recursive=False)
    ttl = cpt.find(id=f"{cpt['id']}.tit_1")
    add(f"CH{nm}", "HEADING_ONLY", f"CHAPTER {cid}", "", "", "", f"Chapter {cid} heading", norm(txt(ps[0]) + ' ' + txt(ttl)), cpt['id'])
    for art in cpt.find_all('div', id=re.compile(r'^art_\d+$'), recursive=False):
        n = int(art['id'].split('_')[1])
        title = txt(art.find(id=art['id'] + '.tit_1'))
        add(f"A{n}.HD", "HEADING_ONLY", str(n), "", "", "", f"Article {n} heading", f"Article {n} {title}", art['id'])
        pdivs = [d for d in art.find_all('div', recursive=False) if d.get('id') and re.match(r'^\d{3}\.\d{3}$', d['id'])]
        if pdivs:
            for d in pdivs:
                k = int(d['id'].split('.')[1])
                emit_paragraph(d, f"A{n}.P{k}", str(n), str(k), d['id'])
        else:
            direct = [c for c in art.find_all(['p', 'table', 'div'], recursive=False)
                      if c.get('id', '') != art['id'] + '.tit_1' and not (c.name == 'p' and 'oj-ti-art' in (c.get('class') or []))]
            if n == 28:
                lead = [c for c in direct if c.name == 'p']
                add("A28.P0", "OPERATIVE_ARTICLE", "28", "0", "", "", "Article 28 (single paragraph; lead-in of inserted article)", txt(lead[0]), "art_28")
                ins = [c for c in direct if c.name == 'div'][0].find(id='026A')
                ps2 = ins.find_all('p', recursive=False)
                add("A28.INS26a.HD", "HEADING_ONLY", "28", "", "", "A28.P0", "Inserted Article 26a of Regulation (EU) 2021/1060: heading", norm(' '.join(txt(p) for p in ps2)), "026A")
                for d in ins.find_all('div', recursive=False):
                    k = int(d['id'].split('.')[1])
                    add(f"A28.INS26a.P{k}", "OPERATIVE_ARTICLE", "28", f"inserted 26a({k})", "", "A28.P0",
                        f"Article 28, inserted Article 26a of Regulation (EU) 2021/1060, paragraph {k}", txt(d), d['id'])
            else:
                ps_ = [c for c in direct if c.name == 'p']
                tabs = [c for c in direct if c.name == 'table']
                if tabs:
                    add(f"A{n}.P0", "OPERATIVE_ARTICLE", str(n), "0", "", "", f"Article {n}, single unnumbered lead-in paragraph", txt(ps_[0]), art['id'])
                    for t in tabs:
                        handle_table(t, f"A{n}.P0", str(n), "0", f"Article {n}", art['id'])
                elif len(ps_) == 1:
                    add(f"A{n}.P0", "OPERATIVE_ARTICLE", str(n), "0", "", "", f"Article {n} (single unnumbered paragraph)", txt(ps_[0]), art['id'])
                else:
                    for i, p in enumerate(ps_, 1):
                        add(f"A{n}.P{i}", "OPERATIVE_ARTICLE", str(n), str(i), "", "", f"Article {n}, unnumbered paragraph {i} (ordinal)", txt(p), art['id'])

# ---- final formulas
fnp = soup.find(id='fnp_1')
fin = fnp.find('div')
fps = fin.find_all('p')
add("FIN.BIND", "FORMAL_OTHER", "", "", "", "", "Final formula: binding and directly applicable", txt(fps[0]), "fnp_1/p1")
add("FIN.DONE", "FORMAL_OTHER", "", "", "", "", "Final formula: place and date", txt(fps[1]), "fnp_1/p2")
sigdivs = fin.find_all('div', recursive=False)
add("FIN.SIG1", "FORMAL_OTHER", "", "", "", "", "Signature block: European Parliament", norm(' '.join(txt(p) for p in sigdivs[0].find_all('p'))), "fnp_1/sig1")
add("FIN.SIG2", "FORMAL_OTHER", "", "", "", "", "Signature block: Council", norm(' '.join(txt(p) for p in sigdivs[1].find_all('p'))), "fnp_1/sig2")
for el in soup.find_all('p', class_='oj-note'):
    t = txt(el)
    m = re.match(r'^\( (\d+) \)', t)
    if not m:
        continue
    num = int(m.group(1))
    if el.find_parent(id='anx_IV') is None:
        add(f"FN{num}", "FORMAL_OTHER", "", "", "", "", f"Footnote ({num})", t, f"note {num}")
    else:
        add(f"ANX4.FN{num}", "FORMAL_OTHER", "IV", "", "", "ANX4.HD", f"Annex IV footnote ({num})", t, "anx_IV note")

# ---- annexes
imgs = []
for a in soup.find_all('div', id=re.compile(r'^anx_')):
    r = a['id'].split('_')[1]
    n = NUM[r]
    ps = a.find_all('p', recursive=False)
    add(f"ANX{n}.HD", "HEADING_ONLY", r, "", "", "", f"Annex {r} heading", norm(' '.join(txt(p) for p in ps[:2])), a['id'])
    counter = [0]
    CLS[0] = "ANNEX"
    skipped = 0
    for c in a.children:
        nme = getattr(c, 'name', None)
        if nme is None:
            continue
        if nme == 'p':
            if skipped < 2:
                skipped += 1
                continue
            t = txt(c)
            if 'oj-note' in (c.get('class') or []):
                continue
            if not t:
                if c.find('img') or c.find('figure'):
                    counter[0] += 1
                    imgs.append((f"ANX{n}.pt{counter[0]}", c))
                    add(f"ANX{n}.pt{counter[0]}", "ANNEX", r, "", str(counter[0]), f"ANX{n}.HD",
                        f"Annex {r} item {counter[0]} (image-only paragraph)",
                        "[IMAGE-ONLY PARAGRAPH: embedded image (formula/graphic); no text content in source file]", a['id'])
                continue
            counter[0] += 1
            add(f"ANX{n}.pt{counter[0]}", "ANNEX", r, "", str(counter[0]), f"ANX{n}.HD", f"Annex {r} item {counter[0]}", t, a['id'])
        elif nme == 'table':
            handle_table(c, f"ANX{n}", r, "", f"Annex {r}", a['id'], True, counter)
        elif nme in ('div', 'figure'):
            if c.find('img'):
                counter[0] += 1
                imgs.append((f"ANX{n}.pt{counter[0]}", c))
                add(f"ANX{n}.pt{counter[0]}", "ANNEX", r, "", str(counter[0]), f"ANX{n}.HD",
                    f"Annex {r} item {counter[0]} (image container)",
                    "[IMAGE-ONLY ELEMENT: embedded image (formula/graphic); no text content in source file]", a['id'])
            elif txt(c):
                counter[0] += 1
                add(f"ANX{n}.pt{counter[0]}", "ANNEX", r, "", str(counter[0]), f"ANX{n}.HD", f"Annex {r} item {counter[0]} (container)", txt(c), a['id'])
CLS[0] = "OPERATIVE_ARTICLE"

ids_ = {u['unit_id'] for u in units}
for u in units:
    pu = u['parent_unit_id']
    if pu and pu not in ids_ and re.fullmatch(CASE + r'\.ANX\d', pu):
        u['parent_unit_id'] = pu + '.HD'
seen = set()
for u in units:
    u['text_sha256'] = hashlib.sha256(u['text'].encode('utf-8')).hexdigest()
    assert u['unit_id'] not in seen, u['unit_id']
    seen.add(u['unit_id'])
json.dump(units, open('units.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(units))
from collections import Counter
print(Counter(u['structure_class'] for u in units))
os.makedirs('img', exist_ok=True)
for uid, c in imgs:
    for j, im in enumerate(c.find_all('img')):
        m = re.match(r'data:image/(\w+);base64,(.*)', im['src'], re.S)
        if m:
            open(f'img/{uid}_{j}.{m.group(1)}', 'wb').write(base64.b64decode(m.group(2)))
print('image units', len(imgs))
