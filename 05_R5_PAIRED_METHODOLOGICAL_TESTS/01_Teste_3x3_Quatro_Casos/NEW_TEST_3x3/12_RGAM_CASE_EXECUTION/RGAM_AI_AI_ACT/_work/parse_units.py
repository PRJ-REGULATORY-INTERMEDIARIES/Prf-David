# MECHANICAL PARSER ONLY: splits the frozen source into units; no analytical content.
from lxml import etree
import re, json, hashlib
from collections import Counter

CASE = "RGAM_AI_AI_ACT"
P = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_AI_AI_ACT/LEGAL_SOURCE/32024R1689_official_en.xhtml"
parser = etree.XMLParser(load_dtd=False, no_network=True, resolve_entities=False, recover=True)
root = etree.parse(P, parser).getroot()
XH = 'http://www.w3.org/1999/xhtml'
ns = {'h': XH}


def tag(e):
    return etree.QName(e).localname if isinstance(e.tag, str) else None


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('\xa0', ' ')).strip()


def tx(e):
    return norm(''.join(e.itertext()))


units = []
seen = set()


def add(uid, cls, art, para, pt, parent, loc, text, anchor):
    base = uid
    n = 2
    while uid in seen:
        uid = f"{base}~dup{n}"
        n += 1
    seen.add(uid)
    units.append(dict(unit_id=uid, structure_class=cls, article_or_annex_no=art, paragraph=para, point=pt,
                      parent_unit_id=parent, locator_text=loc, text=text,
                      text_sha256=hashlib.sha256(norm(text).encode('utf-8')).hexdigest(), source_anchor=anchor))
    return uid


def lab_clean(l):
    l = norm(l)
    m = re.match(r'^\((\w+)\)$', l)
    if m:
        return m.group(1)
    m = re.match(r'^(\w+)\.$', l)
    if m:
        return m.group(1)
    m = re.match(r'^(\d+(?:\.\d+)+)\.?$', l)
    if m:
        return m.group(1)
    return l


BULLETS = ('\u2013', '-', '\u2014', '\u2022', '')


def build(root_uid, children, cls, art, para, anchor, locbase, parent, skip_empty_root=False):
    """Emit unit root_uid (own text = first p), subsequent p -> .SPn units, tables -> point units (recursive)."""
    bullet = {}
    cur = root_uid
    own_set = False
    sp = 1
    texts = {root_uid: []}
    order = [root_uid]
    spparent = {}
    pts = []  # (parent_unit, pid, label, text|None, childs|None)
    for c in children:
        t = tag(c)
        if t in ('p', 'span'):
            s = tx(c)
            if not s:
                continue
            if not own_set:
                texts[cur].append(s)
                own_set = True
            else:
                sp += 1
                nu = f"{root_uid}.SP{sp}"
                order.append(nu)
                texts[nu] = [s]
                spparent[nu] = root_uid
                cur = nu
        elif t == 'table':
            for tr in c.xpath('./h:tbody/h:tr', namespaces=ns):
                tds = tr.xpath('./h:td', namespaces=ns)
                if len(tds) == 3:
                    lab, cont = tds[1], tds[2]
                elif len(tds) == 2:
                    lab, cont = tds[0], tds[1]
                else:
                    lab, cont = None, tds[-1]
                lt = norm(''.join(lab.itertext())) if lab is not None else ''
                embedded = None
                if lt == '':
                    mm = re.match(r'^(\d+(?:\.\d+)+\.?)\s+', tx(cont))
                    if mm:
                        embedded = mm.group(1)
                        lt = embedded
                if lt in BULLETS:
                    bullet[cur] = bullet.get(cur, 0) + 1
                    lc = f"b{bullet[cur]}"
                else:
                    lc = lab_clean(lt)
                pid = f"{cur}.pt{lc}"
                childs = [x for x in cont if isinstance(x.tag, str)]
                if embedded:
                    # strip the embedded label from the first p
                    for k_, x in enumerate(childs):
                        if tag(x) == 'p':
                            full = tx(x)
                            newp = etree.Element('{%s}p' % XH)
                            newp.text = full[len(embedded):].strip() if full.startswith(embedded) else full
                            childs[k_] = newp
                            break
                if not any(tag(x) in ('p', 'table') for x in childs) or (False):
                    t_ = tx(cont)
                    if embedded and t_.startswith(embedded):
                        t_ = t_[len(embedded):].strip()
                    pts.append((cur, pid, lt, lc, t_, None))
                else:
                    pts.append((cur, pid, lt, lc, None, childs))
        elif t == 'div' and (c.get('class') or '') == 'oj-enumeration-spacing':
            full = tx(c)
            mm = re.match(r'^(\d+)\.\s+', full)
            lc = mm.group(1) if mm else 'u'
            lt = (mm.group(1) + '.') if mm else ''
            pid = f"{cur}.pt{lc}"
            inner = [x for x in c if isinstance(x.tag, str)]
            if any(tag(x) in ('table',) for x in inner):
                childs = []
                first = True
                for x in inner:
                    if tag(x) == 'p' and first:
                        newp = etree.Element('{%s}p' % XH)
                        newp.text = tx(x)[len(mm.group(0)):] if mm else tx(x)
                        childs.append(newp)
                        first = False
                    else:
                        childs.append(x)
                pts.append((cur, pid, lt, lc, None, childs))
            else:
                pts.append((cur, pid, lt, lc, full[len(mm.group(0)):] if mm else full, None))
        elif t == 'div':
            # unexpected nested div: treat as extra paragraph text
            s = tx(c)
            if s:
                sp += 1
                nu = f"{root_uid}.SP{sp}"
                order.append(nu)
                texts[nu] = [s]
                spparent[nu] = root_uid
                cur = nu
    for u in order:
        txt = ' '.join(texts.get(u, []))
        par = parent if u == root_uid else spparent[u]
        loc = locbase if u == root_uid else locbase + " (" + u.split('.')[-1] + ")"
        pt_label = ''
        skip = skip_empty_root and u == root_uid and not txt.strip()
        if not skip:
            add(u, cls, art, para, pt_label, par, loc, txt, anchor)
        u_eff = parent if skip else u
        for (pu, pid, lt, lc, ptxt, childs) in pts:
            if pu != u:
                continue
            ploc = f"{loc}, point {lt}"
            if childs is None:
                add(pid, cls, art, para, lc, u_eff, ploc, ptxt, anchor)
            else:
                build(pid, childs, cls, art, para, anchor, ploc, u_eff)


# ---------- preamble ----------
add(f"{CASE}.TITLE", "FORMAL_OTHER", "title", "", "", "", "Title and type of act",
    tx(root.xpath('//h:div[@id="tit_1"]', namespaces=ns)[0]), "tit_1")
pbl = root.xpath('//h:div[@id="pbl_1"]', namespaces=ns)[0]
pre_p = [c for c in pbl if tag(c) == 'p']
add(f"{CASE}.PRE.P1", "FORMAL_OTHER", "preamble", "", "", "", "Preamble: adopting institutions", tx(pre_p[0]), "pbl_1")
for cit in pbl.xpath('./h:div[starts-with(@id,"cit_")]', namespaces=ns):
    n = int(cit.get('id').split('_')[1])
    add(f"{CASE}.CIT{n}", "FORMAL_OTHER", "citation", "", "", "", f"Preamble citation {n}", tx(cit), cit.get('id'))
# recitals
for r in root.xpath('//h:div[starts-with(@id,"rct_")]', namespaces=ns):
    n = int(re.search(r'rct_(\d+)', r.get('id')).group(1))
    tds = r.xpath('.//h:tr[1]/h:td', namespaces=ns)
    txt = tx(tds[-1]) if tds else tx(r)
    add(f"{CASE}.REC{n}", "RECITAL", f"recital {n}", "", "", "", f"Recital ({n})", txt, r.get('id'))
# enacting formula
for p_ in root.xpath('//h:p', namespaces=ns):
    if tx(p_).startswith('HAVE ADOPTED'):
        add(f"{CASE}.PRE.ENACT", "FORMAL_OTHER", "preamble", "", "", "", "Enacting formula", tx(p_), "enacting-formula")
        break

# ---------- enacting terms ----------
enc = root.xpath('//h:div[@id="enc_1"]', namespaces=ns)[0]


def art(a):
    n = int(a.get('id').split('_')[1])
    ti = [tx(x) for x in a.xpath('./h:div[@class="eli-title"]', namespaces=ns)]
    title = ti[0].rstrip('`') if ti else ''
    aloc = f"Article {n} ({title})"
    kids = [c for c in a if isinstance(c.tag, str) and c.get('class') not in ('oj-ti-art', 'eli-title')]
    pdivs = [c for c in kids if tag(c) == 'div' and re.fullmatch(r'\d{3}\.\d{3}', c.get('id') or '')]
    others = [c for c in kids if c not in pdivs]
    if pdivs and others:
        print("MIXED article", n, [(tag(o), o.get('class')) for o in others][:5])
    if pdivs:
        for d in pdivs:
            k = int(d.get('id').split('.')[1])
            ch = [x for x in d if isinstance(x.tag, str)]
            first = ch[0]
            if tag(first) == 'p':
                full = tx(first)
                m = re.match(r'^%d\.\s*' % k, full)
                if m:
                    newp = etree.Element('{%s}p' % XH)
                    newp.text = full[len(m.group(0)):]
                    ch = [newp] + ch[1:]
                else:
                    print("NO LABEL MATCH", n, k, full[:30])
            build(f"{CASE}.A{n}.P{k}", ch, "OPERATIVE_ARTICLE", str(n), str(k), d.get('id'),
                  f"{aloc}, paragraph {k}", f"{CASE}.A{n}")
    else:
        build(f"{CASE}.A{n}.P0", others, "OPERATIVE_ARTICLE", str(n), "0", a.get('id'),
              aloc + " (single/unnumbered paragraph body)", f"{CASE}.A{n}")


def walk(e):
    for c in e:
        if tag(c) != 'div':
            continue
        i = c.get('id') or ''
        if re.fullmatch(r'cpt_[IVXL]+', i) or re.fullmatch(r'cpt_[IVXL]+\.sct_\d+', i):
            ps = [tx(x) for x in c if tag(x) == 'p']
            tt = [tx(x) for x in c if tag(x) == 'div' and (x.get('id') or '').endswith('.tit_1')]
            head = (ps[0] if ps else '') + ' - ' + (tt[0] if tt else '')
            if '.sct_' in i:
                cm = re.match(r'cpt_([IVXL]+)\.sct_(\d+)', i)
                uid = f"{CASE}.CH{cm.group(1)}.SEC{cm.group(2)}"
            else:
                uid = f"{CASE}.CH{i.split('_')[1]}"
            add(uid, "HEADING_ONLY", ps[0] if ps else '', "", "", "", head, head, i)
            walk(c)
        elif re.fullmatch(r'art_\d+', i):
            art(c)


walk(enc)

# ---------- annexes ----------
ROM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12, 'XIII': 13}
for a in root.xpath('//h:div[starts-with(@id,"anx_")]', namespaces=ns):
    r = a.get('id').split('_')[1]
    n = ROM[r]
    ch = [c for c in a if isinstance(c.tag, str)]
    titles = [tx(c) for c in ch if tag(c) == 'p' and c.get('class') == 'oj-doc-ti']
    aloc = f"{titles[0]} - {titles[1] if len(titles) > 1 else ''}"
    add(f"{CASE}.ANX{n}.HEAD", "HEADING_ONLY", f"Annex {r}", "", "", "", aloc, aloc, a.get('id'))
    rest = [c for c in ch if not (tag(c) == 'p' and c.get('class') == 'oj-doc-ti')]
    groups = []
    curg = [None, []]
    for c in rest:
        if tag(c) == 'p' and c.get('class') == 'oj-ti-grseq-1':
            if curg[0] is not None and not curg[1]:
                curg[0] = curg[0] + ' - ' + tx(c)   # consecutive headings merge (e.g. "Section 1" + its title)
            else:
                groups.append(curg)
                curg = [tx(c), []]
        else:
            curg[1].append(c)
    groups.append(curg)
    for head, items in groups:
        if head is None:
            base = f"{CASE}.ANX{n}"
            if not items:
                continue
            build(base + ".P0", items, "ANNEX", f"Annex {r}", "0", a.get('id'), aloc, f"{CASE}.ANX{n}.HEAD", skip_empty_root=True)
        else:
            m = re.match(r'^(Section|Part)\s+([A-Z0-9]+)', head)
            m2 = re.match(r'^(\d+)\.\s', head)
            lab = m.group(2) if m else (m2.group(1) if m2 else 'X')
            sid = f"{CASE}.ANX{n}.S{lab}"
            add(sid + ".HEAD", "HEADING_ONLY", f"Annex {r}", "", "", f"{CASE}.ANX{n}.HEAD", head, head, a.get('id') + "/section")
            build(sid + ".P0", items, "ANNEX", f"Annex {r}", "0", a.get('id'), aloc + " / " + head, sid + ".HEAD", skip_empty_root=True)

# ---------- final formal ----------
fin = root.xpath('//h:div[@class="oj-final"]', namespaces=ns)[0]
fps = [c for c in fin if tag(c) == 'p']
add(f"{CASE}.FIN.BINDING", "FORMAL_OTHER", "final", "", "", "", "Final formula (binding force and direct applicability)", tx(fps[0]), "fnp_1/p1")
add(f"{CASE}.FIN.DONE", "FORMAL_OTHER", "final", "", "", "", "Date and place of adoption", tx(fps[1]), "fnp_1/p2")
add(f"{CASE}.FIN.SIGN", "FORMAL_OTHER", "final", "", "", "", "Signature block (office titles and named signatories)",
    ' | '.join(tx(d) for d in fin.xpath('./h:div[@class="oj-signatory"]', namespaces=ns)), "fnp_1/signatories")

json.dump(units, open('units.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(units), Counter(u['structure_class'] for u in units))
print(sum(1 for u in units if '~dup' in u['unit_id']), "dups")
print(sum(1 for u in units if not u['text'].strip() and u['structure_class'] != 'HEADING_ONLY'), "empty non-heading")
