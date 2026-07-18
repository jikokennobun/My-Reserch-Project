#!/usr/bin/env python3
"""
Pass 115 verification: top/join order-repair of the Pass-113 four-element
MacNeille G2+APS witness.

Base witness (Pass 113/114), carrier {0,a,b,c}:
    order   0<a<b, 0<c, b || c        (0 least, NO greatest element)
    T=a, bot=0
    box:  0->0, a->0, b->b, c->0
    boxt: 0->b, a->b, b->0, c->0

The Pass-114 same-carrier/same-order residual no-go had first obstruction the
non-principal fiber {x : 0 (x) x <= 0} = {0,a,b,c} (whole carrier, no top).

Order repair (Pass 115): adjoin U = b v c as a NEW greatest element.
Resulting order 0<a<b<U, 0<c<U is the pentagon N5 (the non-modular lattice).

We test:
  (A) N5 carries a well-defined APS extension (A1-A4, G2, FG2, no syntactic FP)
      for the forced boxt-extension and every admissible box-extension.
  (B) The MacNeille completion-separation profile: does N5 still have a
      non-principal completion-fixed cut with no syntactic fixed point?
  (C) Residuated-tensor existence: does adjoining the top make the Pass-114
      fiber principal, and does a commutative residuated tensor now exist?
      (Residuated on a finite/complete lattice  <=>  x(x)(-) preserves all
       joins, hence is determined by its values on join-irreducibles.)
"""

import itertools, json, os

# ---------------------------------------------------------------------------
# N5 carrier and order
# ---------------------------------------------------------------------------
C = ['0', 'a', 'b', 'c', 'U']
# leq[x][y] == True iff x <= y
_lt_pairs = {('0','a'),('0','b'),('0','c'),('0','U'),
             ('a','b'),('a','U'),('b','U'),('c','U')}
leq = {x: {y: (x == y or (x, y) in _lt_pairs) for y in C} for x in C}

def LE(x, y):
    return leq[x][y]

def meet(x, y):
    lb = [z for z in C if LE(z, x) and LE(z, y)]
    # greatest lower bound
    for z in lb:
        if all(LE(w, z) for w in lb):
            return z
    return None  # not a lattice (shouldn't happen for N5)

def join(x, y):
    ub = [z for z in C if LE(x, z) and LE(y, z)]
    for z in ub:
        if all(LE(z, w) for w in ub):
            return z
    return None

# sanity: N5 is a lattice
assert all(meet(x, y) is not None and join(x, y) is not None
           for x in C for y in C), "N5 not a lattice?"

TOP, BOT, T = 'U', '0', 'a'

# join-irreducibles (x != bottom, x not a join of strictly-smaller elements)
def is_join_irreducible(x):
    if x == BOT:
        return False
    smaller = [z for z in C if LE(z, x) and z != x]
    for combo_len in range(2, len(smaller) + 1):
        for combo in itertools.combinations(smaller, combo_len):
            j = combo[0]
            for e in combo[1:]:
                j = join(j, e)
            if j == x:
                return False
    return True

JI = [x for x in C if is_join_irreducible(x)]  # expect ['a','b','c']; U=bvc not JI

# ---------------------------------------------------------------------------
# operators
# ---------------------------------------------------------------------------
box_base  = {'0':'0','a':'0','b':'b','c':'0'}
boxt_base = {'0':'b','a':'b','b':'0','c':'0'}

# boxt on U forced by antitonicity: boxt U <= boxt x for all x<U  => <= meet = 0
boxt = dict(boxt_base); boxt['U'] = '0'

def antitone(f):
    return all((not LE(x, y)) or LE(f[y], f[x]) for x in C for y in C)

def monotone(f):
    return all((not LE(x, y)) or LE(f[x], f[y]) for x in C for y in C)

def A2(box, boxt):  # T <= boxt bot
    return LE(T, boxt[BOT])

def A3(box, boxt):  # x<=box y & x<=boxt y => x<=boxt T
    for x in C:
        for y in C:
            if LE(x, box[y]) and LE(x, boxt[y]) and not LE(x, boxt[T]):
                return False
    return True

def A4(box, boxt):  # boxt x <= box boxt x
    return all(LE(boxt[x], box[boxt[x]]) for x in C)

def G2(box, boxt):  # boxt T <= bot => T <= bot
    return (not LE(boxt[T], BOT)) or LE(T, BOT)

def FG2(box, boxt):  # boxt^2 T <= boxt T
    return LE(boxt[boxt[T]], boxt[T])

def synt_fp(boxt):
    return [x for x in C if boxt[x] == x]

# admissible box-extensions: box|_{0,a,b,c}=box_base, box U free & monotone,
# antitone boxt fixed
def box_extensions():
    for u in C:
        box = dict(box_base); box['U'] = u
        if monotone(box):
            yield box

# ---------------------------------------------------------------------------
# (A) APS profile on N5
# ---------------------------------------------------------------------------
resultA = {'boxt_antitone': antitone(boxt),
           'synt_fixed_points': synt_fp(boxt),
           'box_extensions': []}
for box in box_extensions():
    resultA['box_extensions'].append({
        'boxU': box['U'],
        'box_monotone': monotone(box),
        'A2': A2(box, boxt), 'A3': A3(box, boxt), 'A4': A4(box, boxt),
        'G2': G2(box, boxt), 'FG2': FG2(box, boxt),
    })

# ---------------------------------------------------------------------------
# (B) MacNeille completion-separation
# For a finite lattice, MacNeille completion = the lattice itself; every cut is
# principal (= down-set of its join). We compute the closed lower cuts and the
# antitone lower-extension boxt_hat, then look for NON-principal fixed cuts.
# ---------------------------------------------------------------------------
def upper(X):
    return frozenset(z for z in C if all(LE(x, z) for x in X))
def lower(X):
    return frozenset(z for z in C if all(LE(z, x) for x in X))
def closure(X):  # (X^u)^l
    return lower(upper(X))

# enumerate MacNeille-closed lower cuts C = (C^u)^l
cuts = set()
for r in range(len(C) + 1):
    for sub in itertools.combinations(C, r):
        S = frozenset(sub)
        if closure(S) == S:
            cuts.add(S)

def is_principal(cut):
    # principal iff cut = down-set of some single element (its max)
    for x in C:
        if cut == frozenset(z for z in C if LE(z, x)):
            return True
    return False

# correct antitone lower extension:  boxt_hat(Cut) = ((boxt[Cut])^{l})^{u}
def boxt_hat(cut):
    img = frozenset(boxt[x] for x in cut)
    return upper(lower(img))   # L^op-MacNeille closure of the image

fixed_cuts = []
for cut in cuts:
    if boxt_hat(cut) == cut:
        fixed_cuts.append({'cut': sorted(cut), 'principal': is_principal(cut)})

resultB = {
    'num_closed_cuts': len(cuts),
    'all_cuts_principal': all(is_principal(c) for c in cuts),
    'completion_fixed_cuts': fixed_cuts,
    'nonprincipal_fixed_cut_exists': any(not fc['principal'] for fc in fixed_cuts),
    'syntactic_fixed_points': synt_fp(boxt),
}

# ---------------------------------------------------------------------------
# (C) Commutative residuated-tensor census on N5.
# On a complete lattice, (x)(-) has a right residual  <=>  it preserves all
# joins  <=>  it is determined by its values on join-irreducibles and sends
# bottom to bottom.  We enumerate commutative tensors so specified, check the
# two-sided unit, monotonicity, associativity, and (defining residual by
# x\z = V{y : x(x)y <= z}) verify the residuation law a(x)b<=c <=> b<=a\c.
# ---------------------------------------------------------------------------
def join_of(elts):
    if not elts:
        return BOT
    j = elts[0]
    for e in elts[1:]:
        j = join(j, e)
    return j

def build_tensor(vals):
    """vals: dict on unordered JI-pairs (as sorted tuple) -> element.
       Extend join-preservingly to all of C x C.
       Every element x is the join of the JIs below it (plus possibly bottom)."""
    def ji_below(x):
        return [g for g in JI if LE(g, x)]
    T_ = {}
    for x in C:
        for y in C:
            gs_x = ji_below(x); gs_y = ji_below(y)
            terms = []
            for gx in gs_x:
                for gy in gs_y:
                    key = tuple(sorted((gx, gy)))
                    terms.append(vals[key])
            T_[(x, y)] = join_of(terms)   # bottom if either side has no JI
    return T_

def has_unit(T_):
    for e in C:
        if all(T_[(e, x)] == x and T_[(x, e)] == x for x in C):
            return e
    return None

def is_assoc(T_):
    return all(T_[(T_[(x, y)], z)] == T_[(x, T_[(y, z)])]
               for x in C for y in C for z in C)

def is_monotone_tensor(T_):
    for x in C:
        for y in C:
            for z in C:
                if LE(y, z):
                    if not LE(T_[(x, y)], T_[(x, z)]):
                        return False
                    if not LE(T_[(y, x)], T_[(z, x)]):
                        return False
    return True

def residual(T_, x, z):  # x\z = V{y : x(x)y <= z}
    return join_of([y for y in C if LE(T_[(x, y)], z)])

def residuates(T_):
    for x in C:
        for z in C:
            xz = residual(T_, x, z)
            for y in C:
                if LE(T_[(x, y)], z) != LE(y, xz):
                    return False
    return True

ji_pairs = [tuple(sorted(p)) for p in itertools.combinations_with_replacement(JI, 2)]
census = {'commutative_residuated_total': 0, 'by_unit': {}, 'examples': {}}
for choice in itertools.product(C, repeat=len(ji_pairs)):
    vals = dict(zip(ji_pairs, choice))
    T_ = build_tensor(vals)
    e = has_unit(T_)
    if e is None:
        continue
    if not is_monotone_tensor(T_):
        continue
    if not is_assoc(T_):
        continue
    if not residuates(T_):
        continue
    census['commutative_residuated_total'] += 1
    census['by_unit'][e] = census['by_unit'].get(e, 0) + 1
    if e not in census['examples']:
        census['examples'][e] = {f"{x}*{y}": T_[(x, y)]
                                 for x in C for y in C}

# Pass-114 fiber, now on N5, for the meet tensor with unit U (integral):
# {x : 0 (x) x <= 0}. With meet, = {0}. Report principality of the analogue.
meet_tensor = {(x, y): meet(x, y) for x in C for y in C}
fiber_meet = [x for x in C if LE(meet_tensor[(BOT, x)], BOT)]
census['meet_tensor_is_residuated'] = residuates(meet_tensor)  # N5 non-distributive -> expect False
census['meet_tensor_unit'] = has_unit(meet_tensor)
census['pass114_fiber_under_meet'] = {
    'fiber': fiber_meet,
    'principal': (frozenset(fiber_meet) in
                  {frozenset(z for z in C if LE(z, x)) for x in C})
}

out = {'pass': 115, 'carrier': C, 'order': 'N5 (0<a<b<U, 0<c<U)',
       'join_irreducibles': JI,
       'A_aps_profile': resultA,
       'B_macneille_separation': resultB,
       'C_residuated_census': census}

os.makedirs('artifacts/reports', exist_ok=True)
path = 'artifacts/reports/pass115-top-repair-n5-check.json'
with open(path, 'w') as fh:
    json.dump(out, fh, indent=2)

print(json.dumps(out, indent=2))
print("\nWrote", path)
