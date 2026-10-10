#!/usr/bin/env python3
"""Inter-reviewer agreement, computed per named pair of reviewers and per variable.

Design rules (SPEC-K, gates/G0_1/G0_1_STRATEGIC_ALIGNMENT.md):

* The unit of computation is the unordered, named pair of reviewers. Results for
  different pairs are never pooled; there is no aggregate figure.
* "Uncertain" answers are never dropped. Every figure states how they were
  treated: either as a category of their own ("all") or excluded ("categorical").
* Items coded by one reviewer, by more than two, or with a blank answer are
  listed, never silently discarded.
* Nothing here returns a pass/fail verdict. These are diagnostic indicators;
  acceptance of a pilot is decided by people against the written criteria.

Standard library only.
"""
from collections import Counter, defaultdict
from math import sqrt

KAPPA_CI_METHOD = ('approximate large-sample interval: kappa +/- 1.96 * '
                   'sqrt(po * (1 - po) / (n * (1 - pe)^2)); unreliable for small n')


def _answers(rows, variable, item_key, reviewer_key):
    by_item, repeated = defaultdict(dict), []
    for r in rows:
        item, reviewer = r[item_key], r[reviewer_key]
        if reviewer in by_item[item]:
            repeated.append((item, reviewer))
            continue
        by_item[item][reviewer] = (r.get(variable) or '').strip()
    return by_item, repeated


def _split_items(by_item):
    """Group two-reviewer items by pair; list everything that cannot be paired."""
    paired, one, many, blank = defaultdict(list), [], [], []
    for item, answers in by_item.items():
        if len(answers) == 1:
            one.append(item)
        elif len(answers) > 2:
            many.append(item)
        elif any(v == '' for v in answers.values()):
            blank.append(item)
        else:
            a, b = sorted(answers)
            paired[(a, b)].append((item, answers[a], answers[b]))
    return paired, sorted(one), sorted(many), sorted(blank)


def _kappa(pairs, labels):
    """Cohen's kappa over (x, y) pairs. Returns (po, pe, kappa, note, ci)."""
    n = len(pairs)
    if n == 0:
        return None, None, None, 'no items', None
    po = sum(x == y for x, y in pairs) / n
    left, right = Counter(x for x, _ in pairs), Counter(y for _, y in pairs)
    pe = sum(left[c] / n * right[c] / n for c in labels)
    if pe >= 1:
        return po, pe, None, 'undefined: both reviewers used a single category', None
    kappa = (po - pe) / (1 - pe)
    se = sqrt(po * (1 - po) / (n * (1 - pe) ** 2))
    return po, pe, kappa, '', (kappa - 1.96 * se, kappa + 1.96 * se)


def pairwise_agreement(rows, variable='decision', item_key='record_id', reviewer_key='reviewer',
                       uncertain_values=('uncertain',), categories=None):
    """Agreement on one single-valued variable, one result per reviewer pair.

    `categories`, if given, is the list of substantive categories of the variable
    (uncertain excluded); it enables the Brennan-Prediger coefficient, which does
    not depend on the observed prevalence of each category.
    """
    by_item, repeated = _answers(rows, variable, item_key, reviewer_key)
    paired, one, many, blank = _split_items(by_item)
    unc = set(uncertain_values)
    results = []
    for pair in sorted(paired):
        triples = paired[pair]
        answers = [(x, y) for _, x, y in triples]
        labels = sorted({v for xy in answers for v in xy})
        table = {x: {y: 0 for y in labels} for x in labels}
        for x, y in answers:
            table[x][y] += 1
        categorical = [(x, y) for x, y in answers if x not in unc and y not in unc]
        cat_labels = sorted({v for xy in categorical for v in xy})
        po_all, _, k_all, note_all, _ = _kappa(answers, labels)
        po_c, pe_c, k_c, note_c, ci_c = _kappa(categorical, cat_labels)
        specific = {}
        for c in labels:
            denom = sum(table[c].values()) + sum(table[x][c] for x in labels)
            specific[c] = (2 * table[c][c] / denom) if denom else None
        bp = None
        if categories and po_c is not None and len(categories) > 1:
            k = len(categories)
            bp = (po_c - 1 / k) / (1 - 1 / k)
        results.append({
            'pair': pair,
            'reviewer_rows': pair[0], 'reviewer_columns': pair[1],
            'n_items': len(answers),
            'n_items_with_uncertain': sum(1 for x, y in answers if x in unc or y in unc),
            'n_items_both_uncertain': sum(1 for x, y in answers if x in unc and y in unc),
            'n_items_both_categorical': len(categorical),
            'table': table,
            'observed_agreement_all': po_all,
            'kappa_all': k_all, 'kappa_all_note': note_all or 'uncertain treated as a category of its own',
            'observed_agreement_categorical': po_c,
            'expected_agreement_categorical': pe_c,
            'kappa_categorical': k_c,
            'kappa_categorical_note': note_c or 'items with an uncertain answer excluded',
            'kappa_categorical_ci95': ci_c,
            'kappa_ci_method': KAPPA_CI_METHOD,
            'brennan_prediger_categorical': bp,
            'specific_agreement': specific,
            'disagreements': sorted(item for item, x, y in triples if x != y),
        })
    return {
        'variable': variable,
        'uncertain_values': sorted(unc),
        'pairs': results,
        'items_with_one_reviewer': one,
        'items_with_more_than_two_reviewers': many,
        'items_with_blank_answer': blank,
        'repeated_submissions': repeated,
        'pooled_result': None,  # by design: pairs are never combined
    }


def _as_set(value, separator):
    return frozenset(part.strip() for part in (value or '').split(separator) if part.strip())


def pairwise_set_agreement(rows, variable, item_key='record_id', reviewer_key='reviewer', separator=';'):
    """Agreement on a multi-valued variable (e.g. secondary functions, relations).

    Reports, per pair, how many items received identical sets and the mean Jaccard
    index. Two empty sets count as identical (Jaccard 1): both reviewers said "none".
    """
    by_item, repeated = defaultdict(dict), []
    for r in rows:
        item, reviewer = r[item_key], r[reviewer_key]
        if reviewer in by_item[item]:
            repeated.append((item, reviewer))
            continue
        by_item[item][reviewer] = _as_set(r.get(variable), separator)
    paired, one, many = defaultdict(list), [], []
    for item, answers in by_item.items():
        if len(answers) == 1:
            one.append(item)
        elif len(answers) > 2:
            many.append(item)
        else:
            a, b = sorted(answers)
            paired[(a, b)].append((item, answers[a], answers[b]))
    results = []
    for pair in sorted(paired):
        scores = []
        for _, x, y in paired[pair]:
            scores.append(1.0 if not (x | y) else len(x & y) / len(x | y))
        results.append({
            'pair': pair,
            'n_items': len(scores),
            'n_items_identical_sets': sum(1 for _, x, y in paired[pair] if x == y),
            'mean_jaccard': sum(scores) / len(scores),
            'disagreements': sorted(item for item, x, y in paired[pair] if x != y),
        })
    return {'variable': variable, 'pairs': results, 'items_with_one_reviewer': sorted(one),
            'items_with_more_than_two_reviewers': sorted(many), 'repeated_submissions': repeated,
            'pooled_result': None}
