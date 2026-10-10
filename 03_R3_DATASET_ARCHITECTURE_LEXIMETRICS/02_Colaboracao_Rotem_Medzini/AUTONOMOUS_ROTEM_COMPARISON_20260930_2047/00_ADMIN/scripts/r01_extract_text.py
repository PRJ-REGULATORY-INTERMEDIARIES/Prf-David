"""R01 — Derived text extraction (docx -> md, paragraph/table order preserved). Sources are opened read-only."""
import sys
from pathlib import Path

import docx
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, PROJECT_ROOT, sha256, now_iso  # noqa: E402

DL = Path("C:/Users/Adm/Downloads")
TARGETS = [
    ("SRC-CB-UNREV", DL / "Codebook - Regulatory Intermediation (1).docx", "CODEBOOK_UNREVISED_BASELINE.md", "UNREVISED_BASELINE"),
    ("SRC-CHARTKEY", DL / "Chart Key - Regulatory Intermediation (2).docx", "CHART_KEY_UNREVISED_BASELINE.md", "UNREVISED_BASELINE"),
    ("SRC-CB-REV", PROJECT_ROOT / "RELATIONAL_LEXIMETRICS_PILOT/PILOT_01/00_SOURCES/Codebook_Regulatory_Intermediation_Revised (1).docx", "CODEBOOK_REVISED.md", "REVISED_BY_FILENAME_AND_CONTENT"),
    ("SRC-DAVID-MS", PROJECT_ROOT / "RELATIONAL_LEXIMETRICS_PILOT/PILOT_01/00_SOURCES/v1 Law_and_Governance_Architectures_Revised.docx", "DAVID_MANUSCRIPT_CONTEXT.md", "CONTEXT_ONLY"),
    ("SRC-R1-REPORT", DL / "EU_green_regulatory_intermediation_method_progress_report_REVISED.docx", "R1_METHOD_PROGRESS_REPORT_REVISED.md", "HISTORICAL"),
    ("SRC-R2-REPORT", DL / "R2_METHOD_REPORT_TAXONOMY_CALIBRATION_v1_2.docx", "R2_METHOD_REPORT_TAXONOMY_v1_2.md", "HISTORICAL"),
    ("SRC-PROTO-IA", PROJECT_ROOT / "R4_CROSS_DOMAIN_VALIDATION/00_protocol/PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx", "PROTOCOLO_USO_IA_R1_R3.md", "HISTORICAL"),
]


def iter_blocks(d):
    body = d.element.body
    for child in body.iterchildren():
        tag = child.tag.rsplit('}', 1)[-1]
        if tag == 'p':
            yield Paragraph(child, d)
        elif tag == 'tbl':
            yield Table(child, d)


def cell_text(c):
    return " / ".join(p.text.strip() for p in c.paragraphs if p.text.strip()).replace("|", "\\|")


for sid, src, out, status in TARGETS:
    d = docx.Document(src)
    lines = [
        f"<!-- DERIVED TEXT — not an original. SOURCE_ID={sid}; source={src.as_posix()}; SHA256={sha256(src)}; "
        f"SOURCE_STATUS={status}; transformation=python-docx paragraph+table extraction in document order, "
        f"paragraph numbering [¶n] added by this run; extracted_at={now_iso()} -->", ""]
    pn = 0
    for b in iter_blocks(d):
        if isinstance(b, Paragraph):
            t = b.text.strip()
            if not t:
                continue
            pn += 1
            style = (b.style.name or "") if b.style is not None else ""
            if style.lower().startswith("heading"):
                lvl = ''.join(ch for ch in style if ch.isdigit()) or "2"
                lines.append(f"{'#' * min(int(lvl) + 1, 6)} [¶{pn}] {t}")
            else:
                lines.append(f"[¶{pn}] {t}")
            lines.append("")
        else:
            rows = [[cell_text(c) for c in r.cells] for r in b.rows]
            if not rows:
                continue
            pn += 1
            lines.append(f"[¶{pn} TABLE]")
            w = max(len(r) for r in rows)
            rows = [r + [""] * (w - len(r)) for r in rows]
            lines.append("| " + " | ".join(rows[0]) + " |")
            lines.append("|" + "---|" * w)
            for r in rows[1:]:
                lines.append("| " + " | ".join(r) + " |")
            lines.append("")
    (RUN_ROOT / "01_BASELINES/derived_text" / out).write_text("\n".join(lines), encoding="utf-8")
    print(out, pn, "blocks")
