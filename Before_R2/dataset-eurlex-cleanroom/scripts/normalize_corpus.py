#!/usr/bin/env python3
"""
Corpus normalization for dataset-eurlex-cleanroom.

Converts each case's act_official.xhtml (official EUR-Lex / Publications
Office ELI-structured XHTML) into deterministic Markdown:

  act_full.md       - full act: preamble, citations, recitals, enacting
                       articles, final formula/signatures, annexes.
  act_operative.md  - PRIMARY CODING CORPUS: enacting articles + annexes
                       only (no recitals, no citations, no preamble).
  act_recitals.md   - recitals only (contextual; not sufficient alone to
                       support a positive regulatory relationship).
  corpus_manifest.yaml - hashes, article/annex/recital counts, validation.

Rules enforced: no translation, no summarization, no paraphrasing, no
semantic labels; numbering is preserved verbatim (it is embedded in the
source text itself); whitespace is normalized (collapsed) and nothing else;
webpage/navigation artefacts do not exist in this source format (official
Official Journal XHTML, not the eur-lex website rendering) so none are
stripped beyond the bibliographic masthead table, which is retained as a
one-line provenance note in act_full.md only.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml
from bs4 import BeautifulSoup, NavigableString, Tag

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = PROJECT_ROOT / "config" / "case_registry.yaml"

WS_RE = re.compile(r"\s+")

HEADING_NUMBER_CLASSES = {"oj-ti-grseq-1", "oj-ti-section-1", "oj-ti-art"}


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def clean_text(s: str) -> str:
    s = s.replace("\xa0", " ")
    s = WS_RE.sub(" ", s)
    return s.strip()


def children_tags(node) -> list:
    return [c for c in node.find_all(recursive=False) if isinstance(c, Tag)]


def get_classes(tag) -> set:
    """bs4's lxml-xml parser mode treats `class` as a single opaque string
    attribute (unlike its HTML mode, which splits it into a list), so this
    normalizes either representation into a set of class tokens."""
    raw = tag.get("class") if isinstance(tag, Tag) else None
    if not raw:
        return set()
    if isinstance(raw, str):
        return set(raw.split())
    return set(raw)


def render_inline(node) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""
    classes = get_classes(node)
    inner = "".join(render_inline(c) for c in node.children)
    if node.name == "sup" or "oj-super" in classes:
        return f"<sup>{inner}</sup>"
    if node.name == "sub" or "oj-sub" in classes:
        return f"<sub>{inner}</sub>"
    if "oj-bold" in classes or node.name in ("b", "strong"):
        return f"**{inner}**"
    if "oj-italic" in classes or node.name in ("i", "em"):
        return f"*{inner}*"
    return inner


def para_text(tag) -> str:
    return clean_text(render_inline(tag))


def is_data_table(table) -> bool:
    return "oj-table" in get_classes(table)


def render_data_table(table) -> list:
    trs = table.find_all("tr")
    rows = []
    for tr in trs:
        cells = [c for c in tr.find_all(["td", "th"], recursive=False)]
        texts = []
        for cell in cells:
            ps = [p for p in cell.find_all("p", recursive=False)]
            if ps:
                joined = "<br>".join(t for p in ps if (t := para_text(p)))
                texts.append(joined)
            else:
                texts.append(para_text(cell))
        rows.append(texts)
    rows = [r for r in rows if any(c.strip() for c in r)]
    if not rows:
        return []
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]

    def esc(c: str) -> str:
        return c.replace("|", "\\|").replace("\n", " ")

    lines = [
        "| " + " | ".join(esc(c) for c in rows[0]) + " |",
        "|" + "|".join(["---"] * width) + "|",
    ]
    for r in rows[1:]:
        lines.append("| " + " | ".join(esc(c) for c in r) + " |")
    return lines


def render_list_table(table, indent: str) -> list:
    """Two-column [label | content] enumeration table (used for numbered
    paragraphs, lettered/roman sub-points, recital numbers, and inline
    footnotes throughout the source). Not a genuine data table."""
    tr = table.find("tr")
    if tr is None:
        return []
    tds = children_tags(tr)
    if len(tds) < 2:
        text = para_text(table)
        return [f"{indent}{text}"] if text else []
    label = para_text(tds[0])
    body_blocks = render_container(tds[1], indent + "    ")
    if not body_blocks:
        return [f"{indent}{label}"] if label else []
    first = body_blocks[0].lstrip()
    combined = f"{indent}{label} {first}".rstrip() if label else body_blocks[0]
    return [combined] + body_blocks[1:]


def render_container(container, indent: str = "") -> list:
    """Render the direct block-level descendants of `container` (a Tag or
    a list of Tags) as a flat list of markdown block strings. Used for
    article/annex body content, table cells, and generic wrapper divs."""
    if isinstance(container, list):
        children = container
    else:
        children = children_tags(container)

    blocks = []
    for child in children:
        if child.name == "p":
            classes = get_classes(child)
            text = para_text(child)
            if not text:
                continue
            if "oj-quotation" in classes:
                blocks.append(f"{indent}> {text}")
            else:
                blocks.append(f"{indent}{text}")
        elif child.name == "div":
            classes = get_classes(child)
            if "oj-enumeration-spacing" in classes:
                text = clean_text(" ".join(t for p in children_tags(child) if (t := para_text(p))))
                if text:
                    blocks.append(f"{indent}{text}")
            elif "eli-title" in classes:
                p = child.find("p")
                text = para_text(p) if p else para_text(child)
                if text:
                    blocks.append(f"{indent}*{text}*")
            else:
                blocks.extend(render_container(child, indent))
        elif child.name == "table":
            if is_data_table(child):
                blocks.extend(render_data_table(child))
            else:
                blocks.extend(render_list_table(child, indent))
    return blocks


def extract_heading(children: list, idx: int):
    """If children[idx] is a heading-number paragraph (chapter/section/
    article marker), consume it plus an optional following eli-title
    subtitle div, and return (heading_text, next_idx). Else (None, idx)."""
    if idx >= len(children):
        return None, idx
    child = children[idx]
    if child.name == "p" and get_classes(child) & HEADING_NUMBER_CLASSES:
        num_text = para_text(child)
        j = idx + 1
        subtitle = ""
        if (
            j < len(children)
            and children[j].name == "div"
            and "eli-title" in get_classes(children[j])
        ):
            p = children[j].find("p")
            subtitle = para_text(p) if p else para_text(children[j])
            j += 1
        heading_text = f"{num_text} \u2014 {subtitle}" if subtitle else num_text
        return heading_text, j
    return None, idx


def render_articles_level(container, level: int, counters: dict) -> list:
    """Walk a container whose direct children are either chapter wrapper
    divs (id starts with 'cpt_') or article divs (id starts with 'art_'),
    possibly interleaved with stray lead-in paragraphs (e.g. 'HAVE ADOPTED
    THIS REGULATION:')."""
    children = children_tags(container)
    blocks = []
    for child in children:
        cid = child.get("id") or ""
        if child.name == "div" and cid.startswith("cpt_"):
            sub_children = children_tags(child)
            heading, j = extract_heading(sub_children, 0)
            if heading:
                blocks.append(f"{'#' * level} {heading}")
            blocks.extend(render_articles_level(_wrap(sub_children[j:]), level + 1, counters))
        elif child.name == "div" and cid.startswith("art_"):
            counters["articles"] = counters.get("articles", 0) + 1
            art_children = children_tags(child)
            heading, j = extract_heading(art_children, 0)
            if heading:
                blocks.append(f"{'#' * level} {heading}")
            blocks.extend(render_container(art_children[j:]))
        else:
            blocks.extend(render_container([child]))
    return blocks


class _Wrapper:
    """Minimal shim so render_articles_level can re-use children_tags()
    logic uniformly whether given a Tag or a pre-sliced list of Tags."""

    def __init__(self, tags):
        self._tags = tags

    def find_all(self, recursive=False):
        return self._tags


def _wrap(tags):
    return _Wrapper(tags)


def render_recitals(pbl_div, counters: dict) -> list:
    blocks = []
    for child in children_tags(pbl_div):
        cid = child.get("id") or ""
        if cid.startswith("rct_"):
            counters["recitals"] = counters.get("recitals", 0) + 1
            blocks.extend(render_container(child))
    return blocks


def render_preamble_citations(pbl_div) -> list:
    blocks = []
    for child in children_tags(pbl_div):
        cid = child.get("id") or ""
        if child.name == "p":
            text = para_text(child)
            if text:
                blocks.append(text)
        elif cid.startswith("cit_"):
            blocks.extend(render_container(child))
        elif cid.startswith("rct_"):
            continue
        else:
            blocks.extend(render_container(child))
    return blocks


def render_annex(anx_div, counters: dict) -> tuple:
    children = children_tags(anx_div)
    title_lines = []
    i = 0
    while i < len(children) and children[i].name == "p" and "oj-doc-ti" in get_classes(children[i]):
        title_lines.append(para_text(children[i]))
        i += 1
    title = " \u2014 ".join(t for t in title_lines if t)
    counters["annexes"] = counters.get("annexes", 0) + 1
    body = render_articles_level(_wrap(children[i:]), 2, counters)
    header = [f"# {title}"] if title else []
    return header, body


def get_masthead_note(soup) -> str:
    table = soup.find("table")
    if table is None:
        return ""
    date = table.find(class_="oj-hd-date")
    lg = table.find(class_="oj-hd-lg")
    ti = table.find(class_="oj-hd-oj")
    oj = table.find(class_="oj-hd-oj")
    parts = [para_text(x) for x in (date, ti) if x is not None]
    oj_ref = None
    for td in table.find_all("td"):
        t = para_text(td)
        if t.upper().startswith("L "):
            oj_ref = t
    bits = [p for p in parts if p]
    if oj_ref:
        bits.append(oj_ref)
    return " \u2014 ".join(bits)


def convert_case(case: dict) -> dict:
    case_id = case["case_id"]
    source_dir = PROJECT_ROOT / "cases" / case_id / "source"
    corpus_dir = PROJECT_ROOT / "cases" / case_id / "corpus"
    corpus_dir.mkdir(parents=True, exist_ok=True)

    xhtml_path = source_dir / "act_official.xhtml"
    raw = xhtml_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(raw, "lxml-xml")

    main_container = soup.find("div", class_="eli-container", id=None)
    if main_container is None:
        # fallback: first eli-container encountered in document order
        main_container = soup.find("div", class_="eli-container")

    title_div = main_container.find("div", class_="eli-main-title")
    title_text = " ".join(para_text(p) for p in title_div.find_all("p") if para_text(p))

    pbl_div = main_container.find("div", id="pbl_1")
    enc_div = main_container.find("div", id="enc_1")
    fnp_div = main_container.find("div", id="fnp_1")

    counters: dict = {}

    preamble_blocks = render_preamble_citations(pbl_div)
    recital_blocks = render_recitals(pbl_div, counters)
    article_blocks = render_articles_level(enc_div, 2, counters)
    final_blocks = render_container(fnp_div) if fnp_div is not None else []

    annex_headers = []
    annex_full_blocks = []
    annex_operative_blocks = []
    for anx_div in soup.find_all("div", class_="eli-container", id=re.compile(r"^anx_")):
        header, body = render_annex(anx_div, counters)
        annex_full_blocks.append("\n\n".join(header + body))
        annex_operative_blocks.append("\n\n".join(header + body))

    masthead = get_masthead_note(soup)

    # ---- act_full.md ----
    full_parts = [f"# {title_text}"]
    if masthead:
        full_parts.append(f"> {masthead}")
    if preamble_blocks:
        full_parts.append("\n\n".join(preamble_blocks))
    if recital_blocks:
        full_parts.append("\n\n".join(recital_blocks))
    if article_blocks:
        full_parts.append("\n\n".join(article_blocks))
    if final_blocks:
        full_parts.append("\n\n".join(final_blocks))
    full_parts.extend(annex_full_blocks)
    act_full = "\n\n".join(p for p in full_parts if p.strip()) + "\n"

    # ---- act_operative.md (PRIMARY CODING CORPUS: articles + annexes only) ----
    op_parts = [f"# {title_text}"]
    if article_blocks:
        op_parts.append("\n\n".join(article_blocks))
    op_parts.extend(annex_operative_blocks)
    act_operative = "\n\n".join(p for p in op_parts if p.strip()) + "\n"

    # ---- act_recitals.md (contextual only) ----
    rec_parts = [f"# {title_text} \u2014 Recitals"]
    if recital_blocks:
        rec_parts.append("\n\n".join(recital_blocks))
    act_recitals = "\n\n".join(p for p in rec_parts if p.strip()) + "\n"

    files = {
        "act_full.md": act_full,
        "act_operative.md": act_operative,
        "act_recitals.md": act_recitals,
    }
    hashes = {}
    for name, content in files.items():
        out_path = corpus_dir / name
        out_path.write_text(content, encoding="utf-8", newline="\n")
        data = out_path.read_bytes()
        hashes[name] = {"sha256": sha256_of(data), "byte_size": len(data)}

    source_bytes = xhtml_path.read_bytes()

    manifest = {
        "case_id": case_id,
        "celex": case["celex"],
        "source": {
            "file": "../source/act_official.xhtml",
            "sha256": sha256_of(source_bytes),
        },
        "counts": {
            "articles": counters.get("articles", 0),
            "recitals": counters.get("recitals", 0),
            "annexes": counters.get("annexes", 0),
        },
        "derived_files": hashes,
        "normalization_rules": [
            "no_translation",
            "no_summarization",
            "no_paraphrasing",
            "no_semantic_labels",
            "article_paragraph_numbering_preserved_verbatim",
            "whitespace_normalized_only",
        ],
        "act_operative_is_primary_coding_corpus": True,
        "act_recitals_is_contextual_only": True,
    }
    manifest_path = corpus_dir / "corpus_manifest.yaml"
    with open(manifest_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(manifest, f, sort_keys=False, allow_unicode=True)

    return manifest


def main() -> int:
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry = yaml.safe_load(f)

    for case in registry["cases"]:
        print(f"Normalizing {case['case_id']} ({case['celex']}) ...")
        manifest = convert_case(case)
        c = manifest["counts"]
        print(
            f"  articles={c['articles']} recitals={c['recitals']} "
            f"annexes={c['annexes']}"
        )
        for name, h in manifest["derived_files"].items():
            print(f"  {name:20s} bytes={h['byte_size']:7d} sha256={h['sha256']}")
    print("\nCorpus normalization complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
