# MECHANICAL registry/helpers for authoring RGAM records (id assignment, key resolution, span validation, CSV emit).
# Every analytical value passed to these helpers is authored by the executor from reading the unit text.
import json, re, os, csv, hashlib

CASE = 'RGAM_C1_SCF'
W = os.path.dirname(os.path.abspath(__file__))
UNITS = json.load(open(os.path.join(W, 'units.json'), encoding='utf-8'))
UT = {u['unit_id'][len(CASE) + 1:]: u['text'] for u in UNITS}
UORDER = [u['unit_id'][len(CASE) + 1:] for u in UNITS]
UCLASS = {u['unit_id'][len(CASE) + 1:]: u['structure_class'] for u in UNITS}


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def full(u):
    return f"{CASE}.{u}"


WIDTH = dict(ST=4, NA=4, PD=3, QR=4, EXT=3, SC=2, ARCH=2, PROP=3, CL=2, UNC=3, HQ=3, DEV=2, TR=2, RUN=2)
REG = {k: [] for k in WIDTH}
K = {}          # key -> id
KT = {}         # key -> type
CNT = {k: 0 for k in WIDTH}
SCREEN = {}     # unit -> dict


def _new(kind, key):
    if key in K:
        raise ValueError(f"duplicate key {key}")
    CNT[kind] += 1
    i = f"{kind}-{CNT[kind]:0{WIDTH[kind]}d}"
    K[key] = i
    KT[key] = kind
    return i


def check_span(span, units, what):
    if not span:
        return
    for part in span.split(' || '):
        p = norm(part)
        ok = any(p in norm(UT[u]) for u in units)
        if not ok:
            raise ValueError(f"SPAN NOT VERBATIM for {what}: {p[:140]!r} (units {units})")
    if len(span) > 400:
        raise ValueError(f"SPAN > 400 chars for {what} ({len(span)})")


def chk_units(units, what):
    for u in units:
        if u not in UT:
            raise ValueError(f"unknown unit {u} in {what}")


def L(x):
    if x is None:
        return []
    if isinstance(x, str):
        return [x] if x else []
    return list(x)


T_REF = ("Reference date 30 June 2024 (date from which the Regulation applies, A29.P2) and the Fund interval 2026-2032 "
         "with payments to 31 December 2033 (A1.P1, A20.P8); original act as published (OJ L 130, 16.5.2023)")
JUR_EU = "European Union (Union level)"
JUR_MS = "Member States of the European Union (national level)"


def st(key, units, kind, summary, span, recital_only='N'):
    units = L(units)
    chk_units(units, key)
    check_span(span, units, key)
    i = _new('ST', key)
    REG['ST'].append(dict(key=key, st_id=i, supporting_unit_ids=units, statement_kind=kind, statement_summary=summary,
                          evidence_span=span, recital_only=recital_only))
    return i


def pd(key, kind, label, ti, mult, estab, const, epi, units, span, jur=None, inst_src=None, devid='', devfn='',
       devclass='', unc=(), hq=(), ind=(), sts=()):
    units = L(units)
    chk_units(units + L(ind) + L(inst_src), key)
    check_span(span, units, key)
    if jur is None:
        jur = JUR_EU
    i = _new('PD', key)
    REG['PD'].append(dict(key=key, pd_id=i, kind=kind, label=label, type_or_instance=ti,
                          instance_source_unit_ids=L(inst_src), jurisdiction=jur, temporal_reference=T_REF,
                          legal_multiplicity=mult, establishment_norm_type=estab, device_identity_evidence=devid,
                          device_function_evidence=devfn, device_classification=devclass,
                          legal_constitution_status=const, material_establishment_evidence='not_assessed',
                          epistemic_status=epi, units=units, ind=L(ind), evidence_span=span, unc=L(unc), hq=L(hq),
                          sts=L(sts)))
    return i


def na(key, sts, subj, action, obj, fn, mech, instr, mod, cond, cp, cpstat, nt, effect, notc, constraint='N',
       deriv='direct', rule='', deps=None, legal='in_force', epi='documented', span=None, unc=(), hq=(), ind=(),
       units=None):
    sts = L(sts)
    for s in sts:
        assert KT.get(s) == 'ST', f"{key}: unknown statement key {s}"
    u = []
    for s in sts:
        for x in next(r for r in REG['ST'] if r['key'] == s)['supporting_unit_ids']:
            if x not in u:
                u.append(x)
    if units:
        for x in L(units):
            if x not in u:
                u.append(x)
    chk_units(u + L(ind), key)
    if span is None:
        span = next(r for r in REG['ST'] if r['key'] == sts[0])['evidence_span']
    check_span(span, u, key)
    if deriv == 'derived':
        assert rule and (len(u) + len(L(ind)) >= 2), f"derived NA {key} needs rule and >=2 units"
    i = _new('NA', key)
    REG['NA'].append(dict(key=key, na_id=i, sts=sts, units=u, ind=L(ind), subj=subj, action=action, object=obj,
                          function=fn, mechanism=mech, instrument_ref=instr, modality=mod, conditions=cond,
                          counterpart_if_identifiable=cp, counterpart_status=cpstat, norm_type=nt,
                          constitution_effect=effect, not_constituted_note=notc, constraint_only=constraint,
                          derivation=deriv, derivation_rule=rule, deps=L(deps) if deps else [subj],
                          legal_status_of_norm=legal, epistemic_status=epi, evidence_span=span, unc=L(unc),
                          hq=L(hq)))
    return i


def qr(key, sts, origin, cp, rtype, action, obj, fn, mod, mech='', instr='', tnote='', gdir='', cond='', validity='',
       legal='in_force', epi='documented', deriv='direct', rule='', auth='', disc='', acc='NONE', accs='NA',
       accmiss='', accvia=(), deps=None, gap='', ext=(), span=None, unc=(), hq=(), ind=(), add=(), units=None, tdir=''):
    sts = L(sts)
    for s in sts:
        assert KT.get(s) == 'ST', f"{key}: unknown statement key {s}"
    u = []
    for s in sts:
        for x in next(r for r in REG['ST'] if r['key'] == s)['supporting_unit_ids']:
            if x not in u:
                u.append(x)
    if units:
        for x in L(units):
            if x not in u:
                u.append(x)
    chk_units(u + L(ind), key)
    if span is None:
        span = next(r for r in REG['ST'] if r['key'] == sts[0])['evidence_span']
    check_span(span, u, key)
    assert mod != 'prohibition', key
    assert epi != 'material_establishment_evidenced', key
    if deriv == 'derived':
        assert rule and (len(u) + len(L(ind)) >= 2), f"derived QR {key} needs rule and >=2 units"
    i = _new('QR', key)
    REG['QR'].append(dict(key=key, qr_id=i, sts=sts, units=u, ind=L(ind), origin=origin, cp=cp, add=L(add), tdir=tdir,
                          relation_type=rtype, type_note=tnote, governance_direction=gdir, action=action,
                          object=obj, function=fn, mechanism=mech, instrument_ref=instr, modality=mod,
                          conditions=cond, validity_note=validity, legal_status_of_norm=legal,
                          epistemic_status=epi, derivation=deriv, derivation_rule=rule, authority_attribute=auth,
                          discretion_attribute=disc, accountability_class=acc, accountability_sufficiency=accs,
                          accountability_missing_elements=accmiss, accvia=L(accvia),
                          deps=L(deps) if deps else [origin, cp], support_gap_report=gap, ext=L(ext),
                          evidence_span=span, unc=L(unc), hq=L(hq)))
    return i


def ext(key, sts, units, source, skind, role, dependents, depkind, constitutive, effect, extra_units=()):
    sts = L(sts)
    units = L(units)
    chk_units(units + L(extra_units), key)
    i = _new('EXT', key)
    REG['EXT'].append(dict(key=key, ext_id=i, sts=sts, units=units, referenced_legal_source=source, source_kind=skind,
                           reference_role=role, source_verification_status='not_checked',
                           boundary_status='outside_corpus_not_expanded', dependents=L(dependents),
                           dependency_kind=depkind, constitutive_dependency=constitutive, effect_on_claims=effect,
                           ind=L(extra_units)))
    return i


def sc(key, scope, pattern, question, qrs, nas, pds, mech, warrant, spanned, boundary, overlap, nested, competing,
       unc=(), hq=()):
    i = _new('SC', key)
    REG['SC'].append(dict(key=key, sc_id=i, scope_label=scope, pattern_rule=pattern, governance_question=question,
                          qrs=L(qrs), nas=L(nas), pds=L(pds), organizing_mechanism=mech, warrant_basis=warrant,
                          units_spanned=L(spanned), boundary_statement=boundary, overlap=L(overlap),
                          nested_in=nested or '', competing_grouping=competing, unc=L(unc), hq=L(hq)))
    return i


def arch(key, member_scs, i1, i1_units, i1s, i2, i2k, i2_qrs, i2s, i3, i3b, i3s, i4_searched, i4_ext, i4_rival,
         i4_sens, i4s, outcome, basis, profile, unc=(), hq=()):
    i = _new('ARCH', key)
    REG['ARCH'].append(dict(key=key, arch_id=i, member_scs=L(member_scs), i1=i1, i1_units=L(i1_units), i1s=i1s,
                            i2=i2, i2k=i2k, i2_qrs=L(i2_qrs), i2s=i2s, i3=i3, i3b=i3b, i3s=i3s,
                            i4_searched=i4_searched, i4_ext=L(i4_ext), i4_rival=i4_rival, i4_sens=i4_sens, i4s=i4s,
                            anticirc='Y', outcome=outcome, basis=basis, profile=profile, unc=L(unc), hq=L(hq)))
    return i


def prop(key, name, fam, btype, bearer, scale, value, rule, pathsem, agg, support, closure_dep, closure_ref,
         count_basis, fallacy, rival, status, hq=(), units_ind=()):
    i = _new('PROP')if False else _new('PROP', key)
    REG['PROP'].append(dict(key=key, prop_id=i, property_name=name, property_family=fam, bearer_type=btype,
                            bearer=bearer, scale=scale, value_statement=value, inference_rule=rule,
                            path_semantics=pathsem, aggregation_rule=agg, supporting=L(support),
                            closure_dependency=closure_dep, closure_ref=closure_ref, count_basis=count_basis,
                            fallacy_check=fallacy, rival_partition=rival, status=status, hq=L(hq),
                            units_ind=L(units_ind)))
    return i


def cl(key, kind, claim, search, unresolved, result, affected, units=()):
    i = _new('CL', key)
    REG['CL'].append(dict(key=key, closure_id=i, record_kind=kind, claim_or_scope=claim, search_description=search,
                          unresolved_ext=L(unresolved), result=result, affected=L(affected), units=L(units)))
    return i


def unc(key, records, units, utype, desc, treatment, effect, hq=None):
    chk_units(L(units), key)
    i = _new('UNC', key)
    REG['UNC'].append(dict(key=key, unc_id=i, records=L(records), units=L(units), uncertainty_type=utype,
                           description=desc, treatment=treatment, effect_on_claims=effect, hq=hq))
    return i


def hq(key, trigger, records, question, competing, rec, reason):
    i = _new('HQ', key)
    REG['HQ'].append(dict(key=key, hq_id=i, trigger_code=trigger, records=L(records), question=question,
                          competing_readings=competing, machine_recommendation=rec, reason_human_required=reason))
    return i


def dev(key, rule, desc, reason, impact, gap=''):
    i = _new('DEV', key)
    REG['DEV'].append(dict(key=key, dev_id=i, rule_id=rule, description=desc, reason=reason, impact=impact,
                           gap_ref=gap))
    return i


def scr(units, role, note, rel=None):
    for u in L(units):
        if u not in UT:
            raise ValueError(f"scr: unknown unit {u}")
        if u in SCREEN:
            raise ValueError(f"scr: unit screened twice {u}")
        SCREEN[u] = dict(role=role, note=note, rel=rel)


def rng(prefix, a, b, sep='.'):
    """expand helper: units whose id starts with prefix and lies between ids a and b inclusive in source order"""
    ia, ib = UORDER.index(a), UORDER.index(b)
    return UORDER[ia:ib + 1]
