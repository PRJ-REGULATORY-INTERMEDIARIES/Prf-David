#!/usr/bin/env python3
"""Pilot A instruments: blinded coding packets, form validation, locking, comparison.

Commands
    build     write two equivalent, independent, blinded coding forms (Reviewer A / B)
    validate  check a form against the vocabularies, the completeness rules and, for the
              pre-filled columns, against the reviewer manifest of its packet
    package   zip one reviewer's folder, with that reviewer's evidence, for delivery
    lock      record the SHA-256 of both filled forms before anyone compares them
    compare   per-variable agreement for the locked pair of forms (diagnostic only)

No command fills in, infers or simulates a human decision. `compare` refuses to
run on blank or unlocked forms. Standard library only.
"""
import argparse
import csv
import hashlib
import json
import io
import random
import re
import zipfile
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

import agreement

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / 'pilot_a'
VOCAB_FILE = ROOT / 'schemas' / 'vocabularies.json'
TAXONOMY = ROOT / 'protocol' / 'SOURCE_TAXONOMY_v0_2_DRAFT.md'
PROTOCOL = ROOT / 'protocol' / 'PROTOCOL_v1_0_DRAFT.md'

# Columns of the seed inventory / selection files that must never reach a reviewer.
FORBIDDEN = ('layer', 'resource_type', 'rgam_potential', 'initial_priority', 'limitations',
             'possible_legal_id', 'observation_unit', 'announced_access', 'objective_properties',
             'source_seed_id')
PREFILLED = ('item_id', 'source_label', 'source_url', 'reviewer_role')
DECISION_FIELDS = (
    'reviewer_id', 'verification_date', 'access_outcome', 'url_actually_used',
    'operational_level', 'operational_category', 'rule_applied',
    'primary_function', 'secondary_functions', 'legislative_candidate',
    'eligibility', 'eligibility_reason_code', 'eligibility_justification',
    'relations', 'relations_justification',
    'evidence_urls', 'evidence_notes',
    'uncertainty_type', 'missing_evidence', 'observations', 'minutes')
FORM_COLUMNS = PREFILLED + DECISION_FIELDS
# Variables compared one value at a time, with the label that means "uncertain" in each.
SINGLE = {'operational_level': 'UNCERTAIN', 'operational_category': 'UNCERTAIN',
          'primary_function': 'UNCERTAIN', 'legislative_candidate': 'indeterminado',
          'eligibility': 'uncertain'}
ISO_DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')


def vocab():
    return json.loads(VOCAB_FILE.read_text(encoding='utf-8'))['pilot_a']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_csv(path):
    with Path(path).open('r', encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def split(value, sep=';'):
    return [p.strip() for p in (value or '').split(sep) if p.strip()]


def item_digest(row):
    """SHA-256 of the four pre-filled columns of one item, as delivered to the reviewer."""
    return hashlib.sha256('\x1f'.join(row[c] for c in PREFILLED).encode('utf-8')).hexdigest()


# ----------------------------------------------------------------- build ----

def protocol_section_6():
    """Verbatim text of section 6 (eligibility) of the protocol, for the reviewers."""
    text = PROTOCOL.read_text(encoding='utf-8')
    start = text.index('## 6. Elegibilidade a priori')
    end = text.index('## 7.', start)
    return text[start:end].rstrip() + '\n'


def instructions(letter):
    return f"""# PILOTO A — INSTRUÇÕES AO AVALIADOR ({letter})

**Estado:** instrumento preparado; codificação NÃO autorizada até designação dos avaliadores, aprovação da amostra e autorização expressa.

## O que você recebe

| Arquivo | Conteúdo |
|---|---|
| `CODING_FORM_{letter}.csv` | 20 itens, um por linha. As quatro primeiras colunas vêm preenchidas; as demais são suas |
| `SOURCE_TAXONOMY_v0_2_DRAFT.md` | Regras de classificação (níveis, classes, regras R0–R11, relações) |
| `ELIGIBILITY_CRITERIA_PROTOCOL_S6.md` | Critérios de inclusão e exclusão, transcritos da seção 6 do protocolo |
| `INSTRUCTIONS.md` | Este arquivo |

## Regras de independência

1. Trabalhe sozinho. Não converse sobre os itens com ninguém até entregar o formulário.
2. Não consulte o inventário de origem, relatórios do projeto nem o formulário de outro avaliador.
3. Não use modelo de linguagem para decidir. Tradução automática de páginas é permitida; anote em `observations`.
4. Os identificadores (`{letter}-01` …) são neutros e a ordem é aleatória. Não significam nada.
5. Entregue o arquivo ao coordenador sem alterar as quatro primeiras colunas nem o nome das colunas.

## Como preencher

Para cada item: abra `source_url`; se a página não for o recurso, navegue até ele e registre o endereço em `url_actually_used`. Aplique as regras R0–R11 **na ordem**. Registre a evidência que sustentou cada decisão.

| Coluna | Preenchimento |
|---|---|
| `reviewer_id` | Seu identificador, igual em todas as linhas |
| `verification_date` | Data em que você verificou a fonte, `AAAA-MM-DD` |
| `access_outcome` | `acessivel` / `parcial` / `inacessivel` |
| `url_actually_used` | Endereço do recurso, se diferente de `source_url` |
| `operational_level` | `K` contêiner / `L1` recurso / `L2` distribuição / `DUPLICATE` / `UNCERTAIN` |
| `operational_category` | `FPL` `REP` `DSE` `API` `COD` `REG` `AUX` `FDE` `IND` ou `UNCERTAIN`. Para nível `K`, `L2` ou `DUPLICATE`, deixe em branco se a taxonomia não atribuir classe |
| `rule_applied` | A regra que decidiu: `R0` … `R11` |
| `primary_function` | O que o recurso principalmente faz: `F1_TEXTOS_DE_ATOS`, `F2_METADADOS_DE_ATOS`, `F3_ACESSO_PROGRAMATICO`, `F4_CATALOGO_OU_DIRETORIO`, `F5_REGISTRO_DE_ENTIDADES_OU_CASOS`, `F6_CLASSIFICACAO_OU_IDENTIFICACAO`, `F7_CORPUS_PARA_PESQUISA`, `F8_OUTRA`, `UNCERTAIN` |
| `secondary_functions` | Zero ou mais códigos de função, separados por `;` |
| `legislative_candidate` | `sim` / `nao` / `indeterminado` (taxonomia, seção 6) |
| `eligibility` | `include` / `exclude` / `uncertain` |
| `eligibility_reason_code` | Obrigatório se `exclude`: `NOT_EU_RELATED`, `UNSTRUCTURED`, `NOT_LEGAL_REGULATORY`, `NOT_IDENTIFIABLE`, `INSUFFICIENT_DOCUMENTATION`, `OTHER` |
| `eligibility_justification` | Critérios I1–I5 / E1–E5 que fundamentam a decisão |
| `relations` | Duplicação, distribuição ou sobreposição com **outro item deste pacote**: `tipo:ITEM`, separados por `;`. Ex.: `distribution_of:{letter}-07; overlaps_with:{letter}-12`. Tipos: `duplicate_of`, `distribution_of`, `hosted_by`, `derived_from`, `part_of`, `overlaps_with`, `successor_of`, `uses`. Relação com algo fora do pacote: use `tipo:EXTERNAL` e descreva na justificativa |
| `relations_justification` | Evidência de cada relação declarada |
| `evidence_urls` | Endereços das páginas que sustentam suas decisões, separados por `;`. Pelo menos um por item |
| `evidence_notes` | O que em cada página sustenta a decisão |
| `uncertainty_type` | `nenhuma` / `regra_ausente` / `regra_ambigua` / `evidencia_insuficiente` |
| `missing_evidence` | Obrigatório quando houver incerteza: o que faltou |
| `observations` | Livre |
| `minutes` | Tempo gasto no item, em minutos |

## Incerteza

`UNCERTAIN`, `uncertain`, `indeterminado` e `IND` são respostas legítimas. Ninguém espera que você force uma escolha. Sempre que usar uma delas, preencha `uncertainty_type` e `missing_evidence`. A incerteza é um dos resultados que o piloto procura.

## O que o piloto mede

O piloto testa as **regras**, não você e não os recursos. Suas decisões não entram em nenhuma contagem da pesquisa.
"""


def build(base=PILOT, sample_file=None, seed=None, labels_file=None):
    base = Path(base)
    sample_file = Path(sample_file) if sample_file else base / 'selection' / 'PILOT_A_CANDIDATE_SAMPLE.csv'
    rows = read_csv(sample_file)
    log_file = sample_file.parent / 'PILOT_A_SELECTION_LOG.json'
    if seed is None:
        seed = json.loads(log_file.read_text(encoding='utf-8'))['seed']
    overrides = {}
    over_file = base / 'coordinator' / 'LABEL_OVERRIDES.csv'
    ids = sorted(r['source_seed_id'] for r in rows)
    if labels_file:
        # A complete label file: every item of the sample must have a neutral label.
        overrides = {r['source_seed_id']: r['neutral_label'].strip() for r in read_csv(labels_file) if r.get('neutral_label', '').strip()}
        missing = [i for i in ids if i not in overrides]
        if missing:
            raise SystemExit(f'label file has no neutral label for: {missing}')
    elif over_file.exists():
        overrides = {r['source_seed_id']: r['neutral_label'].strip() for r in read_csv(over_file) if r.get('neutral_label', '').strip()}
    by_id = {r['source_seed_id']: r for r in rows}
    key = {i: {} for i in ids}
    written = {}
    section6 = protocol_section_6()
    for offset, letter in ((1, 'A'), (2, 'B')):
        rng = random.Random(seed + offset)
        order = [i for _, i in sorted((rng.random(), i) for i in ids)]
        folder = base / f'reviewer_{letter}'
        folder.mkdir(parents=True, exist_ok=True)
        form = folder / f'CODING_FORM_{letter}.csv'
        digests = {}
        with form.open('w', encoding='utf-8-sig', newline='') as handle:
            w = csv.writer(handle, lineterminator='\n')
            w.writerow(FORM_COLUMNS)
            for n, sid in enumerate(order, 1):
                item = f'{letter}-{n:02d}'
                key[sid][letter] = item
                label = overrides.get(sid, by_id[sid]['name'])
                prefilled = [item, label, by_id[sid]['source_url'], f'REVIEWER_{letter}']
                digests[item] = item_digest(dict(zip(PREFILLED, prefilled)))
                w.writerow(prefilled + [''] * len(DECISION_FIELDS))
        (folder / 'INSTRUCTIONS.md').write_text(instructions(letter), encoding='utf-8', newline='\n')
        (folder / 'SOURCE_TAXONOMY_v0_2_DRAFT.md').write_bytes(TAXONOMY.read_bytes())
        (folder / 'ELIGIBILITY_CRITERIA_PROTOCOL_S6.md').write_text(
            '<!-- Transcrição literal da seção 6 de protocol/PROTOCOL_v1_0_DRAFT.md. Não é emenda. -->\n\n' + section6,
            encoding='utf-8', newline='\n')
        leaked = [c for c in FORBIDDEN if c in FORM_COLUMNS]
        text = form.read_text(encoding='utf-8-sig')
        leaked += [sid for sid in ids if re.search(rf'\b{sid}\b', text)]
        if leaked:
            raise SystemExit(f'blinding check failed for reviewer {letter}: {leaked}')
        # Reviewer-side manifest: lets `validate` confirm the pre-filled columns were not changed.
        # It names no inventory identifier and nothing about the other reviewer's packet.
        reviewer_manifest = {
            'packet': f'REVIEWER_{letter}', 'items': len(digests), 'prefilled_columns': list(PREFILLED),
            'prefilled_item_sha256': digests,
            'reference_files_sha256': {n: sha(folder / n) for n in ('INSTRUCTIONS.md', 'SOURCE_TAXONOMY_v0_2_DRAFT.md', 'ELIGIBILITY_CRITERIA_PROTOCOL_S6.md')},
            'note': 'Do not edit. Used only to check that item_id, source_label, source_url and reviewer_role are intact.',
        }
        (folder / f'PACKET_MANIFEST_REVIEWER_{letter}.json').write_text(json.dumps(reviewer_manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
        written[letter] = {p.name: sha(p) for p in sorted(folder.iterdir()) if p.is_file()}
    coord = base / 'coordinator'
    coord.mkdir(parents=True, exist_ok=True)
    with (coord / 'ITEM_KEY.csv').open('w', encoding='utf-8-sig', newline='') as handle:
        w = csv.writer(handle, lineterminator='\n')
        w.writerow(['source_seed_id', 'item_id_A', 'item_id_B', 'label_shown'])
        for sid in ids:
            w.writerow([sid, key[sid]['A'], key[sid]['B'], overrides.get(sid, by_id[sid]['name'])])
    if not labels_file and not over_file.exists():
        with over_file.open('w', encoding='utf-8-sig', newline='') as handle:
            csv.writer(handle, lineterminator='\n').writerow(['source_seed_id', 'neutral_label'])
    manifest = {
        'built_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'script': 'scripts/pilot_a_forms.py', 'script_sha256': sha(__file__),
        'sample_file': str(sample_file.relative_to(base.parent)) if base.parent in sample_file.parents else str(sample_file),
        'sample_sha256': sha(sample_file),
        'order_seed_A': seed + 1, 'order_seed_B': seed + 2,
        'columns_withheld_from_reviewers': list(FORBIDDEN),
        'label_overrides_applied': sorted(i for i in overrides if i in ids),
        'labels_file': str(labels_file) if labels_file else None,
        'labels_file_sha256': sha(labels_file) if labels_file else None,
        'taxonomy_sha256': sha(TAXONOMY), 'protocol_sha256': sha(PROTOCOL),
        'reviewer_A_files': written['A'], 'reviewer_B_files': written['B'],
        'roles': {'REVIEWER_A': 'NOT ASSIGNED', 'REVIEWER_B': 'NOT ASSIGNED', 'ADJUDICATOR': 'NOT ASSIGNED'},
        'status': 'PREPARED - coding not authorised; no decision field is filled',
    }
    (coord / 'PACKET_MANIFEST.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    return manifest


# -------------------------------------------------------------- validate ----

def is_http(value):
    parts = urlsplit(value)
    return parts.scheme in ('http', 'https') and bool(parts.netloc) and not any(c.isspace() for c in value)


def validate(form_path):
    """Return (errors, stats). Errors are (item_id, column, message)."""
    v = vocab()
    rows = read_csv(form_path)
    errors = []
    if not rows or tuple(rows[0].keys()) != FORM_COLUMNS:
        return [('-', '-', 'unexpected columns; the form header must not be changed')], {}
    items = {r['item_id'] for r in rows}
    # Pre-filled columns against the reviewer manifest delivered with the packet, when present.
    manifest_file = Path(form_path).parent / f'PACKET_MANIFEST_REVIEWER_{Path(form_path).stem[-1]}.json'
    prefilled_checked = manifest_file.exists()
    if prefilled_checked:
        expected = json.loads(manifest_file.read_text(encoding='utf-8'))['prefilled_item_sha256']
        for r in rows:
            if r['item_id'] not in expected:
                errors.append((r['item_id'], 'prefilled', 'item is not part of this packet'))
            elif item_digest(r) != expected[r['item_id']]:
                errors.append((r['item_id'], 'prefilled', 'a pre-filled column (item_id, source_label, source_url, reviewer_role) was changed'))
        for missing in sorted(set(expected) - items):
            errors.append((missing, 'prefilled', 'item of the packet is missing from the form'))
    blank = [r['item_id'] for r in rows if not any(r[c].strip() for c in DECISION_FIELDS)]
    uncertain_items = []
    for r in rows:
        if r['item_id'] in blank:
            continue
        def err(col, msg):
            errors.append((r['item_id'], col, msg))
        def in_vocab(col, name, required=True):
            value = r[col].strip()
            if not value:
                if required:
                    err(col, 'required')
            elif value not in v[name]:
                err(col, f'not in vocabulary: {value!r}')
        if not r['reviewer_id'].strip():
            err('reviewer_id', 'required')
        if not ISO_DATE.match(r['verification_date'].strip()):
            err('verification_date', 'required, format YYYY-MM-DD')
        else:
            try:
                date.fromisoformat(r['verification_date'].strip())
            except ValueError:
                err('verification_date', 'not a valid date')
        in_vocab('access_outcome', 'access_outcome')
        in_vocab('operational_level', 'level')
        in_vocab('operational_category', 'class', required=r['operational_level'].strip() == 'L1')
        in_vocab('rule_applied', 'rule')
        in_vocab('primary_function', 'function')
        for f in split(r['secondary_functions']):
            if f not in v['function'] or f == 'UNCERTAIN':
                err('secondary_functions', f'not a function code: {f!r}')
        in_vocab('legislative_candidate', 'legislative_candidate')
        in_vocab('eligibility', 'eligibility')
        if r['eligibility'].strip() == 'exclude' and not r['eligibility_reason_code'].strip():
            err('eligibility_reason_code', 'required when eligibility is exclude')
        if r['eligibility'].strip() and not r['eligibility_justification'].strip():
            err('eligibility_justification', 'required')
        for rel in split(r['relations']):
            kind, _, target = rel.partition(':')
            kind, target = kind.strip(), target.strip()
            if kind not in v['relation_type']:
                err('relations', f'unknown relation type: {kind!r}')
            if target != 'EXTERNAL' and target not in items:
                err('relations', f'target is not an item of this packet: {target!r}')
            if target == r['item_id']:
                err('relations', 'an item cannot be related to itself')
        if split(r['relations']) and not r['relations_justification'].strip():
            err('relations_justification', 'required when a relation is declared')
        urls = split(r['evidence_urls'])
        if r['access_outcome'].strip() != 'inacessivel' and not urls:
            err('evidence_urls', 'at least one evidence URL is required')
        for u in urls + split(r['url_actually_used']):
            if not is_http(u):
                err('evidence_urls', f'not an http(s) URL: {u!r}')
        if urls and not r['evidence_notes'].strip():
            err('evidence_notes', 'required: say what in the evidence supports the decision')
        in_vocab('uncertainty_type', 'uncertainty_type')
        is_uncertain = (any(r[c].strip() == label for c, label in SINGLE.items())
                        or r['operational_category'].strip() == 'IND')
        if is_uncertain:
            uncertain_items.append(r['item_id'])
            if r['uncertainty_type'].strip() in ('', 'nenhuma'):
                err('uncertainty_type', 'an uncertain answer needs its type')
            if not r['missing_evidence'].strip():
                err('missing_evidence', 'an uncertain answer needs the missing evidence or rule')
        if r['minutes'].strip() and not r['minutes'].strip().replace('.', '', 1).isdigit():
            err('minutes', 'number expected')
    reviewers = sorted({r['reviewer_id'].strip() for r in rows if r['reviewer_id'].strip()})
    if len(reviewers) > 1:
        errors.append(('-', 'reviewer_id', f'more than one reviewer id in one form: {reviewers}'))
    stats = {'items': len(rows), 'blank_items': blank, 'coded_items': len(rows) - len(blank),
             'items_with_uncertain_answer': uncertain_items, 'reviewer_ids': reviewers,
             'prefilled_checked_against_manifest': prefilled_checked}
    return errors, stats


# --------------------------------------------------------------- package ----

INDEX_COLUMNS = ('item_id', 'outcome', 'method', 'original_url', 'final_url', 'captured_at_utc',
                 'content_type', 'bytes', 'sha256', 'last_modified', 'file')


def package(base=PILOT, letter='A', evidence_dir=None, out=None):
    """Zip one reviewer's folder for delivery, with the evidence of that reviewer's items.

    Evidence is stored by inventory record; here it is re-filed under the reviewer's
    neutral item ids, so the package contains no inventory identifier, no key and
    nothing from the other reviewer or the coordinator.
    """
    base = Path(base)
    folder = base / f'reviewer_{letter}'
    out = Path(out) if out else base / 'dist'
    out.mkdir(parents=True, exist_ok=True)
    key = {r['source_seed_id']: r[f'item_id_{letter}'] for r in read_csv(base / 'coordinator' / 'ITEM_KEY.csv')}
    zpath = out / f'PILOT_A_PACKET_REVIEWER_{letter}.zip'
    index, files = [], 0
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for path in sorted(folder.iterdir()):
            if path.is_file():
                z.write(path, path.name)
        if evidence_dir:
            ev = Path(evidence_dir)
            log = ev / 'CAPTURE_LOG.jsonl'
            for line in (log.read_text(encoding='utf-8').splitlines() if log.exists() else []):
                if not line.strip():
                    continue
                rec = json.loads(line)
                if rec.get('record_id') not in key:
                    continue
                item, name = key[rec['record_id']], ''
                if rec.get('raw_file'):
                    src = ev / rec['raw_file']
                    name = f'evidence/{item}/{src.name}'
                    if name not in z.namelist():
                        z.write(src, name)
                        files += 1
                index.append({**{c: rec.get(c, '') for c in INDEX_COLUMNS}, 'item_id': item, 'file': name})
            if index:
                buf = io.StringIO()
                w = csv.DictWriter(buf, fieldnames=INDEX_COLUMNS, lineterminator='\n')
                w.writeheader()
                w.writerows(sorted(index, key=lambda r: (r['item_id'], r['captured_at_utc'] or '')))
                z.writestr('evidence/EVIDENCE_INDEX.csv', '\ufeff' + buf.getvalue())
        names = z.namelist()
    listing = '\n'.join(names) + '\n' + '\n'.join(str(v) for r in index for k, v in r.items() if k not in ('original_url', 'final_url'))
    leaked = sorted(set(re.findall(r'\bEU\d\d\b', listing)) & set(key))
    banned = [n for n in names if re.search(r'ITEM_KEY|LOCK|coordinator|selection|CAPTURE_LOG', n)]
    if leaked or banned:
        zpath.unlink()
        raise SystemExit(f'package check failed for reviewer {letter}: {leaked + banned}')
    info = {'reviewer': letter, 'zip': str(zpath), 'sha256': sha(zpath), 'files': len(names),
            'evidence_files': files, 'evidence_rows': len(index),
            'packaged_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds')}
    record_file = base / 'coordinator' / 'DIST_MANIFEST.json'
    record = json.loads(record_file.read_text(encoding='utf-8')) if record_file.exists() else {}
    record[letter] = {**info, 'zip': zpath.name}
    record_file.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8', newline='\n')
    return info


# ---------------------------------------------------------- lock, compare ----

def lock(base=PILOT):
    base = Path(base)
    forms = {L: base / f'reviewer_{L}' / f'CODING_FORM_{L}.csv' for L in 'AB'}
    problems = {}
    for L, path in forms.items():
        errors, stats = validate(path)
        if errors or stats.get('blank_items'):
            problems[L] = {'errors': len(errors), 'blank_items': len(stats.get('blank_items', []))}
    if problems:
        raise SystemExit(f'cannot lock: forms are incomplete or invalid: {problems}')
    record = {'locked_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
              'forms': {L: {'file': str(p.relative_to(base)), 'sha256': sha(p)} for L, p in forms.items()}}
    (base / 'coordinator' / 'LOCK.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8', newline='\n')
    return record


def compare(base=PILOT):
    """Per-variable agreement for the single locked pair. Diagnostic indicators only."""
    base = Path(base)
    lock_file = base / 'coordinator' / 'LOCK.json'
    if not lock_file.exists():
        raise SystemExit('forms are not locked; run `lock` first (independence safeguard)')
    record = json.loads(lock_file.read_text(encoding='utf-8'))
    key = read_csv(base / 'coordinator' / 'ITEM_KEY.csv')
    to_seed = {L: {r[f'item_id_{L}']: r['source_seed_id'] for r in key} for L in 'AB'}
    rows = []
    for L in 'AB':
        path = base / record['forms'][L]['file']
        if sha(path) != record['forms'][L]['sha256']:
            raise SystemExit(f'form {L} changed after locking; comparison refused')
        for r in read_csv(path):
            r = dict(r)
            r['record_id'] = to_seed[L][r['item_id']]
            rels = []
            for rel in split(r['relations']):
                kind, _, target = rel.partition(':')
                rels.append(f'{kind.strip()}:{to_seed[L].get(target.strip(), target.strip())}')
            r['relations'] = ';'.join(sorted(rels))
            r['reviewer'] = r['reviewer_id'].strip()
            rows.append(r)
    reviewers = sorted({r['reviewer'] for r in rows})
    if len(reviewers) != 2:
        raise SystemExit(f'exactly two distinct reviewer ids are required, found {reviewers}')
    v = vocab()
    cats = {'operational_level': v['level'], 'operational_category': v['class'], 'primary_function': v['function'],
            'legislative_candidate': v['legislative_candidate'], 'eligibility': v['eligibility']}
    out = {'reviewers': reviewers, 'lock': record, 'single_valued': {}, 'multi_valued': {},
           'note': 'Diagnostic indicators for one named pair. Not an acceptance verdict; adjudication decides.'}
    for var, unc in SINGLE.items():
        categories = [c for c in cats[var] if c != unc]
        out['single_valued'][var] = agreement.pairwise_agreement(rows, variable=var, uncertain_values=(unc,), categories=categories)
    for var in ('secondary_functions', 'relations'):
        out['multi_valued'][var] = agreement.pairwise_set_agreement(rows, variable=var)
    return out


def render(result):
    a, b = result['reviewers']
    lines = ['# PILOTO A — COMPARAÇÃO DESCRITIVA', '',
             f'Par de avaliadores: **{a} × {b}**. Formulários trancados em {result["lock"]["locked_at_utc"]}.', '',
             'Indicadores diagnósticos de um único par nomeado. Não constituem veredito de aprovação.', '']
    fmt = lambda x: 'n/d' if x is None else f'{x:.3f}'
    for var, res in result['single_valued'].items():
        lines += [f'## {var}', '']
        for p in res['pairs']:
            labels = sorted(p['table'])
            lines += [f'- Itens comparados: {p["n_items"]}; com resposta incerta: {p["n_items_with_uncertain"]} (ambos incertos: {p["n_items_both_uncertain"]})',
                      f'- Concordância observada, incerteza como categoria própria: {fmt(p["observed_agreement_all"])}',
                      f'- Concordância observada, só respostas categóricas (n={p["n_items_both_categorical"]}): {fmt(p["observed_agreement_categorical"])}',
                      f'- Kappa de Cohen, só categóricas: {fmt(p["kappa_categorical"])} — {p["kappa_categorical_note"]}',
                      f'- Brennan–Prediger, só categóricas: {fmt(p["brennan_prediger_categorical"])}',
                      f'- Itens divergentes: {", ".join(p["disagreements"]) or "nenhum"}', '',
                      f'| {a} \\ {b} | ' + ' | '.join(labels) + ' |', '|---|' + '---|' * len(labels)]
            lines += [f'| {x} | ' + ' | '.join(str(p['table'][x][y]) for y in labels) + ' |' for x in labels]
            lines.append('')
        for label, k in (('um só avaliador', 'items_with_one_reviewer'), ('resposta em branco', 'items_with_blank_answer')):
            if res[k]:
                lines += [f'- Itens com {label}: {", ".join(res[k])}', '']
    for var, res in result['multi_valued'].items():
        lines += [f'## {var} (conjuntos)', '']
        for p in res['pairs']:
            lines += [f'- Itens: {p["n_items"]}; conjuntos idênticos: {p["n_items_identical_sets"]}; Jaccard médio: {fmt(p["mean_jaccard"])}',
                      f'- Itens divergentes: {", ".join(p["disagreements"]) or "nenhum"}', '']
    return '\n'.join(lines) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='command', required=True)
    pb = sub.add_parser('build')
    pb.add_argument('--base', default=str(PILOT), help='pilot folder that receives reviewer_A, reviewer_B and coordinator')
    pb.add_argument('--sample', help='candidate sample CSV (default: <base>/selection/PILOT_A_CANDIDATE_SAMPLE.csv)')
    pb.add_argument('--labels', help='CSV with source_seed_id and neutral_label for every item of the sample')
    pp = sub.add_parser('package')
    pp.add_argument('--base', default=str(PILOT))
    pp.add_argument('--reviewer', choices=['A', 'B'], required=True)
    pp.add_argument('--evidence', help='evidence folder holding CAPTURE_LOG.jsonl')
    pv = sub.add_parser('validate')
    pv.add_argument('form')
    pv.add_argument('--require-complete', action='store_true')
    sub.add_parser('lock')
    sub.add_parser('compare')
    args = ap.parse_args()
    if args.command == 'build':
        m = build(base=args.base, sample_file=args.sample, labels_file=args.labels)
        print(json.dumps({k: m[k] for k in ('order_seed_A', 'order_seed_B', 'roles', 'status')}, indent=2))
    elif args.command == 'validate':
        errors, stats = validate(args.form)
        for item, col, msg in errors:
            print(f'[ERROR] {item} {col}: {msg}')
        print(json.dumps(stats, indent=2, ensure_ascii=False))
        incomplete = args.require_complete and stats.get('blank_items')
        if incomplete:
            print(f'[ERROR] {len(stats["blank_items"])} item(s) not coded')
        return 2 if errors or incomplete else 0
    elif args.command == 'package':
        print(json.dumps(package(args.base, args.reviewer, evidence_dir=args.evidence), indent=2))
    elif args.command == 'lock':
        print(json.dumps(lock(), indent=2))
    elif args.command == 'compare':
        text = render(compare())
        out = PILOT / 'coordinator' / 'COMPARISON.md'
        out.write_text(text, encoding='utf-8', newline='\n')
        print(f'written {out.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
