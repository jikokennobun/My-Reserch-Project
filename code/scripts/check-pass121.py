#!/usr/bin/env python3
"""
Pass 121 verification: is frontier meet-rigidity (Thm 120a) a MacNeille
artifact or a completion-universal law?

Carrier: K_{2,3}^{0,U} = {0, f1,f2, g1,g2,g3, U},
  0 < everything < U,  f_i < g_j for all i,j.

We compute three completions and, in each, locate the completion element
w = f1 v f2, its upper frontier G, and the meet-generator hypergraph
H_min(w) = { minimal G' subseteq G : /\ G' = w }, plus mu(w) = min |G'|.

  (A) MacNeille  (cuts)                 -> also = canonical extension (finite)
  (B) Ideal / downset completion D(L)   (meets = intersection)
  (C) Filter / upset completion F(L)    (order-dual; meets = union of upsets)

Claim under test (Thm 120a / Cor 120b): distinct g's meet to w and mu(w)=2.
"""
import itertools, json

bot, U = '0', 'U'
F = ['f1', 'f2']
G = ['g1', 'g2', 'g3']
elems = [bot] + F + G + [U]

# ---- order ----
def build_leq():
    leq = set((x, x) for x in elems)
    for x in elems:
        leq.add((bot, x)); leq.add((x, U))
    for f in F:
        for g in G:
            leq.add((f, g))
    changed = True
    while changed:
        changed = False
        for (a, b) in list(leq):
            for (c, d) in list(leq):
                if b == c and (a, d) not in leq:
                    leq.add((a, d)); changed = True
    return leq
LEQ = build_leq()
def le(a, b): return (a, b) in LEQ

def subsets(lst):
    for r in range(len(lst) + 1):
        for c in itertools.combinations(lst, r):
            yield frozenset(c)

def upper(S):  # upper bounds in L
    return frozenset(x for x in elems if all(le(s, x) for s in S))
def lower(S):
    return frozenset(x for x in elems if all(le(x, s) for s in S))

# ---------- (A) MacNeille ----------
def macneille():
    cuts = set()
    for S in subsets(elems):
        cuts.add(lower(upper(S)))          # C = l(u(S)) is a cut
    cuts = sorted(cuts, key=lambda c: (len(c), sorted(c)))
    # completion order = inclusion; meet = intersection (a cut), join = cut(union)
    principal = {x: lower(upper(frozenset([x]))) for x in elems}  # = down-set of x
    return cuts, principal

# ---------- (B) ideal / downset completion ----------
def is_downset(S):
    return all((y in S) for x in S for y in elems if le(y, x))
def ideal_completion():
    D = [S for S in subsets(elems) if is_downset(S)]
    principal = {x: frozenset(y for y in elems if le(y, x)) for x in elems}
    return D, principal   # order = inclusion; meet=intersection, join=union

# ---------- (C) filter / upset completion ----------
def is_upset(S):
    return all((y in S) for x in S for y in elems if le(x, y))
def filter_completion():
    Ups = [S for S in subsets(elems) if is_upset(S)]
    principal = {x: frozenset(y for y in elems if le(x, y)) for x in elems}
    # order: a <= b  iff  up(a) SUPSET-EQ up(b)  (reverse inclusion)
    # meet(a,b) = up(a) UNION up(b) ; join(a,b) = up(a) INTERSECT up(b)
    return Ups, principal

def report_completion(name, kind, principal):
    """Locate w = f1 v f2, its upper frontier G, H_min(w), mu(w)."""
    p = principal
    if kind in ('macneille', 'ideal'):
        # element repr = down-closed cut/downset; order = inclusion
        wjoin = p['f1'] | p['f2']
        if kind == 'macneille':
            wjoin = lower(upper(wjoin))     # close to a cut
        w = wjoin
        def ge_w(x): return p[x] >= w and p[x] != w   # strictly above w
        def eq_meet(Gp):
            m = elems and None
            sets = [p[x] for x in Gp]
            inter = sets[0]
            for s in sets[1:]:
                inter = inter & s
            return inter == w
        w_is_principal = any(p[x] == w for x in elems)
    else:  # filter completion, reverse inclusion
        # w = f1 v f2 = join = up(f1) INTERSECT up(f2)
        w = p['f1'] & p['f2']
        def ge_w(x):  # x > w  iff up(x) STRICT-SUBSET w
            return p[x] < w
        def eq_meet(Gp):
            sets = [p[x] for x in Gp]
            union = set()
            for s in sets:
                union |= s
            return frozenset(union) == w
        w_is_principal = any(p[x] == w for x in elems)

    frontier = [x for x in G if ge_w(x)]
    # minimal-among-frontier already: all g's are atoms above w here
    # meet-generator hypergraph over the upper frontier G
    gens = []
    for Gp in subsets(frontier):
        if len(Gp) >= 1 and eq_meet(Gp):
            gens.append(tuple(sorted(Gp)))
    minimal = [g for g in gens if not any(set(h) < set(g) for h in gens)]
    mu = min((len(g) for g in minimal), default=None)
    return {
        'completion': name,
        'w_is_principal': w_is_principal,
        'upper_frontier_G': sorted(frontier),
        'H_min(w)': sorted(minimal),
        'mu(w)': mu,
        'meet_rigid (all pairs -> w)': all(
            eq_meet((a, b)) for a, b in itertools.combinations(frontier, 2)
        ) if len(frontier) >= 2 else None,
    }

out = {}

# (A) MacNeille
cuts, mac_p = macneille()
nonprincipal_cuts = [c for c in cuts if c not in set(mac_p.values())]
out['macneille'] = report_completion('MacNeille', 'macneille', mac_p)
out['macneille']['n_elements'] = len(cuts)
out['macneille']['n_nonprincipal'] = len(nonprincipal_cuts)

# (B) ideal
D, id_p = ideal_completion()
out['ideal'] = report_completion('Ideal/downset D(L)', 'ideal', id_p)
out['ideal']['n_elements'] = len(D)
out['ideal']['n_nonprincipal'] = len(D) - len(set(id_p.values()))

# (C) filter
Ups, fi_p = filter_completion()
out['filter'] = report_completion('Filter/upset F(L)', 'filter', fi_p)
out['filter']['n_elements'] = len(Ups)
out['filter']['n_nonprincipal'] = len(Ups) - len(set(fi_p.values()))

# canonical extension = MacNeille for finite poset (all filters/ideals principal)
def all_finite_filters_principal():
    # a filter = down-directed up-set; check every up-set that is down-directed
    for S in subsets(elems):
        if not is_upset(S) or len(S) == 0:
            continue
        downdirected = all(
            any(le(z, a) and le(z, b) for z in S) for a in S for b in S
        )
        if downdirected:
            # must be principal: has a minimum
            has_min = any(all(le(m, x) for x in S) for m in S)
            if not has_min:
                return False
    return True
out['canonical_ext_eq_macneille'] = all_finite_filters_principal()

# ---- assertions ----
checks = {}
checks['macneille_rigid_mu2'] = (out['macneille']['mu(w)'] == 2
                                 and out['macneille']['meet_rigid (all pairs -> w)'] is True
                                 and out['macneille']['n_nonprincipal'] == 1)
checks['ideal_meet_rigid_mu2'] = (out['ideal']['mu(w)'] == 2
                                  and out['ideal']['meet_rigid (all pairs -> w)'] is True)
checks['filter_breaks_rigidity_mu3'] = (out['filter']['mu(w)'] == 3
                                        and out['filter']['meet_rigid (all pairs -> w)'] is False
                                        and out['filter']['H_min(w)'] == [('g1', 'g2', 'g3')])
checks['canonical_eq_macneille'] = out['canonical_ext_eq_macneille'] is True
out['checks'] = checks
out['OVERALL'] = 'PASS' if all(checks.values()) else 'FAIL'

print(json.dumps(out, indent=2, default=lambda o: sorted(o) if isinstance(o, frozenset) else str(o)))
