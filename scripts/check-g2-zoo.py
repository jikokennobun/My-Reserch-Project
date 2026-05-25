#!/usr/bin/env python3
"""
G2-ZOO Checker — scripts/check-g2-zoo.py

Checks a finite preAPS model (JSON) against the following properties:
  - G2:        boxtimes(T) <= bot  =>  T <= bot
  - FG2:       boxtimes^2(T) <= boxtimes(T)         [= nFG2(1)]
  - nFG2(k):   boxtimes^{k+1}(T) <= boxtimes^k(T)  for k >= 1
  - FP-synt:   exists p in L with  p = boxtimes(p)  (as APS-equivalence)
  - collapse:  T <= bot
  - MacNeille completion properties (with CORRECT L^op-closure extension)

Usage:
  python check-g2-zoo.py MODEL.json [--nfg2-depth 8] [--verbose]

  python check-g2-zoo.py models/examples/M-101.json
  python check-g2-zoo.py models/examples/*.json --verbose

Output: JSON report to stdout; also appends a row to outputs/g2-zoo-registry.csv
        if --register is passed.

Mathematical definitions (all from definitions.md in this repository):

  Preorder:  (L, <=) reflexive and transitive.
  T, bot:    distinguished elements of L.
  boxtimes:  L -> L, antitone (x <= y => boxtimes(y) <= boxtimes(x)).

  G2:        boxtimes(T) <= bot  =>  T <= bot
  nFG2(k):   boxtimes^{k+1}(T) <= boxtimes^k(T)   (k >= 1; nFG2(1) = FG2)
  FP-synt:   {p in L : p ~ boxtimes(p)}  nonempty
              where  p ~ q  iff  p <= q  and  q <= p.

  MacNeille cut:  C = (C^u)^l  (lower-closed set, doubly closed in the Galois sense)
  Principal cut:  i(a) = ({a}^u)^l
  Correct antitone extension (L^op-closure):
    boxtimes_hat(C) = (boxtimes[C]^{l_L})^{u_L}
  Completion FP:  C = boxtimes_hat(C) (as sets)
  Reflected:      C = i(p) for some p with p ~ boxtimes(p)
  Principal-unreflected: C = i(a) but NOT a ~ boxtimes(a)

References:
  - Beklemishev-Shamkanov (2016): Jeroslow FP without formalized G2.
  - Ciabattoni-Galatos-Terui: completion stability for substructural logics.
  - notes/completion-and-fixed-points.md, models/macneille-reflection-search.md
"""

import json
import sys
import argparse
from itertools import product as iter_product


# ─── Preorder utilities ───────────────────────────────────────────────────────

def leq(order_dict, x, y):
    return order_dict.get((x, y), False)

def equiv(order_dict, x, y):
    return leq(order_dict, x, y) and leq(order_dict, y, x)

def apply_n(bt, x, n):
    """Apply boxtimes map n times."""
    for _ in range(n):
        x = bt[x]
    return x

def transitive_closure(carrier, pairs):
    """Return transitive-reflexive closure of a set of pairs."""
    order = {(x, y) for (x, y) in pairs}
    for x in carrier:
        order.add((x, x))
    changed = True
    while changed:
        changed = False
        for (a, b) in list(order):
            for (c, d) in list(order):
                if b == c and (a, d) not in order:
                    order.add((a, d))
                    changed = True
    return order


# ─── MacNeille completion ─────────────────────────────────────────────────────

def uppers(carrier, order_dict, S):
    return [c for c in carrier if all(leq(order_dict, x, c) for x in S)]

def lowers(carrier, order_dict, S):
    return [c for c in carrier if all(leq(order_dict, c, x) for x in S)]

def mac_close_L(carrier, order_dict, S):
    """L-MacNeille closure: (S^u)^l."""
    return frozenset(lowers(carrier, order_dict, uppers(carrier, order_dict, S)))

def lop_close(carrier, order_dict, S):
    """L^op-MacNeille closure: (S^{l_L})^{u_L}.
    This is the CORRECT closure for extending an antitone map."""
    lb = lowers(carrier, order_dict, S)
    return frozenset([c for c in carrier if all(leq(order_dict, l, c) for l in lb)])

def get_all_cuts(carrier, order_dict):
    """Return all MacNeille-closed lower cuts."""
    cuts = set()
    for mask in range(1 << len(carrier)):
        S = frozenset(carrier[i] for i in range(len(carrier)) if mask & (1 << i))
        C = mac_close_L(carrier, order_dict, S)
        if S == C:
            cuts.add(C)
    return sorted(cuts, key=lambda c: (len(c), sorted(c)))

def get_principal_cuts(carrier, order_dict):
    """Return {a: i(a) for a in carrier}."""
    return {a: mac_close_L(carrier, order_dict, frozenset([a])) for a in carrier}

def boxtimes_hat(carrier, order_dict, bt, cut):
    """Correct antitone extension: L^op-closure of boxtimes-image."""
    img = frozenset(bt[x] for x in cut)
    return lop_close(carrier, order_dict, img)

def get_completion_fps(carrier, order_dict, bt, cuts):
    """Find all MacNeille cuts C with boxtimes_hat(C) = C."""
    fps = []
    for cut in cuts:
        ext = boxtimes_hat(carrier, order_dict, bt, cut)
        if ext == cut:
            fps.append(cut)
    return fps

def principal_element(principal_cuts, cut):
    """Return a if cut = i(a), else None."""
    for a, pc in principal_cuts.items():
        if pc == cut:
            return a
    return None


# ─── Property checkers ────────────────────────────────────────────────────────

def check_antitone(carrier, order_dict, bt):
    for x in carrier:
        for y in carrier:
            if leq(order_dict, x, y) and not leq(order_dict, bt[y], bt[x]):
                return False, (x, y)
    return True, None

def check_G2(order_dict, bt, T, bot):
    ante = leq(order_dict, bt[T], bot)
    if not ante:
        return True, 'vacuous'
    return leq(order_dict, T, bot), 'antecedent-true'

def check_nFG2(order_dict, bt, T, k):
    """boxtimes^{k+1}(T) <= boxtimes^k(T)"""
    lhs = apply_n(bt, T, k + 1)
    rhs = apply_n(bt, T, k)
    return leq(order_dict, lhs, rhs)

def check_FP_synt(carrier, order_dict, bt):
    return [p for p in carrier if equiv(order_dict, p, bt[p])]

def check_collapse(order_dict, T, bot):
    return leq(order_dict, T, bot)


# ─── Main checker ─────────────────────────────────────────────────────────────

def check_model(path, nfg2_depth=8, verbose=False):
    with open(path, encoding='utf-8') as fh:
        model = json.load(fh)

    carrier = model['carrier']
    T   = model['top']
    bot = model['bottom']
    bt  = model['refutability']   # boxtimes map: {element: element}

    assert T   in carrier, f"top '{T}' not in carrier"
    assert bot in carrier, f"bottom '{bot}' not in carrier"
    for x in carrier:
        assert x in bt,         f"refutability missing key '{x}'"
        assert bt[x] in carrier, f"refutability('{x}') = '{bt[x]}' not in carrier"

    raw_order = [(pair[0], pair[1]) for pair in model['order']]
    order_set = transitive_closure(carrier, raw_order)
    order_dict = {(x, y): True for (x, y) in order_set}

    # Antitone check
    ant_ok, ant_wit = check_antitone(carrier, order_dict, bt)
    assert ant_ok, f"refutability not antitone: witness {ant_wit}"

    # G2
    g2, g2_mode = check_G2(order_dict, bt, T, bot)

    # n-FG2 hierarchy
    nfg2 = [check_nFG2(order_dict, bt, T, k) for k in range(1, nfg2_depth + 1)]

    # FP-synt
    fps = check_FP_synt(carrier, order_dict, bt)

    # Collapse
    collapsed = check_collapse(order_dict, T, bot)

    # ⊠-orbit of T
    orbit = [T]
    for _ in range(nfg2_depth + 2):
        orbit.append(bt[orbit[-1]])

    # MacNeille completion
    cuts = get_all_cuts(carrier, order_dict)
    principal_cuts = get_principal_cuts(carrier, order_dict)
    cfps = get_completion_fps(carrier, order_dict, bt, cuts)

    # Classify completion FPs
    cfp_details = []
    for c in cfps:
        pe = principal_element(principal_cuts, c)
        if pe is not None:
            reflected = equiv(order_dict, pe, bt[pe])
            cfp_details.append({
                'cut': sorted(c),
                'principal': True,
                'principal_element': pe,
                'reflected': reflected,
            })
        else:
            cfp_details.append({
                'cut': sorted(c),
                'principal': False,
                'principal_element': None,
                'reflected': False,
            })

    # Overall CFP classification
    if not cfps:
        cfp_class = 'no-completion-fixed-point'
    elif all(d['principal'] and d['reflected'] for d in cfp_details):
        cfp_class = 'principal-reflected'
    elif all(d['principal'] for d in cfp_details):
        # Mix of reflected and unreflected, but all principal
        has_reflected = any(d['reflected'] for d in cfp_details)
        cfp_class = 'principal-reflected-mixed' if has_reflected else 'principal-unreflected'
    elif not any(d['principal'] for d in cfp_details):
        cfp_class = 'nonprincipal-without-syntactic' if not fps else 'nonprincipal-with-syntactic'
    else:
        cfp_class = 'mixed-principal-nonprincipal'

    report = {
        'model': model.get('name', path),
        'carrier_size': len(carrier),
        'top': T,
        'bottom': bot,
        'collapse': collapsed,
        'G2': g2,
        'G2_mode': g2_mode,
        'FG2': nfg2[0],
        'nFG2': {str(k + 1): nfg2[k] for k in range(nfg2_depth)},
        'FP_synt': len(fps) > 0,
        'FP_elements': fps,
        'boxtimes_orbit_T': orbit[:nfg2_depth + 2],
        'MacNeille_cut_count': len(cuts),
        'completion_FP_classification': cfp_class,
        'completion_FPs': cfp_details,
        'warnings': [],
    }

    if collapsed:
        report['warnings'].append('Model is collapsed (T <= bot): all properties hold trivially.')
    if not fps and any(d['reflected'] for d in cfp_details):
        report['warnings'].append('Reflected completion FP found but FP_synt=False: internal inconsistency.')

    return report


def format_report(report, verbose=False):
    lines = []
    lines.append(f"Model: {report['model']}  (|L|={report['carrier_size']})")
    lines.append(f"  collapse: {report['collapse']}")
    lines.append(f"  G2:       {report['G2']}  ({report['G2_mode']})")
    lines.append(f"  FG2:      {report['FG2']}")
    nfg2_str = '  '.join(
        f"nFG2({k})={'T' if v else 'F'}"
        for k, v in sorted(report['nFG2'].items(), key=lambda x: int(x[0]))[:8]
    )
    lines.append(f"  {nfg2_str}")
    lines.append(f"  FP-synt:  {report['FP_synt']}  {report['FP_elements']}")
    orbit = report['boxtimes_orbit_T']
    lines.append(f"  ⊠-orbit(T): {' → '.join(str(x) for x in orbit[:7])} → …")
    lines.append(f"  MacNeille cuts: {report['MacNeille_cut_count']}")
    lines.append(f"  Completion FP class: {report['completion_FP_classification']}")
    if verbose:
        for d in report['completion_FPs']:
            cut_str = '{' + ', '.join(str(x) for x in d['cut']) + '}'
            if d['principal']:
                refl = '✓ REFLECTED' if d['reflected'] else 'principal-unreflected'
                lines.append(f"    {cut_str} = i({d['principal_element']}) [{refl}]")
            else:
                lines.append(f"    {cut_str} [non-principal]")
    for w in report['warnings']:
        lines.append(f"  WARNING: {w}")
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='G2-ZOO property checker')
    parser.add_argument('models', nargs='+', help='JSON model file(s)')
    parser.add_argument('--nfg2-depth', type=int, default=8)
    parser.add_argument('--verbose', '-v', action='store_true')
    parser.add_argument('--json', action='store_true', help='Output JSON report')
    args = parser.parse_args()

    reports = []
    for path in args.models:
        try:
            r = check_model(path, nfg2_depth=args.nfg2_depth, verbose=args.verbose)
            reports.append(r)
            if not args.json:
                print(format_report(r, verbose=args.verbose))
                print()
        except Exception as e:
            print(f"ERROR in {path}: {e}", file=sys.stderr)

    if args.json:
        print(json.dumps(reports if len(reports) > 1 else reports[0], indent=2, ensure_ascii=False))
