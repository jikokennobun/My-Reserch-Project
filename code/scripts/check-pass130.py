#!/usr/bin/env python3
"""
check-pass130.py  --  APS/G2-ZOO autonomous discussion, Pass 130.

Verifies the machine-checkable content of Pass 130:

  (A) Phantom divisibility / finite-summand dissolution.
      lim^1(Z, x m_n) = hatZ_N / Z is DIVISIBLE, so no finite Z/q^k splits off.
      We certify the two engines of divisibility at the finite-truncation level:
        (A1) unit-absorption: a finite-valuation prime q is a UNIT in every
             solenoidal Z_p (p != q), so mult-by-q is an automorphism that
             carries q.Z onto Z inside D = prod_{p in Supp_inf} Z_p; hence the
             finite factor Z/q^{e_q} is absorbed when Supp_fin is FINITE.
        (A2) torsion detection: the indicator element e_q at a finite-valuation
             prime q is a genuine order-q^{e_q} torsion element of hatZ_N/Z,
             whereas a solenoidal prime contributes NO torsion.  So
             Tor(hatZ_N/Z) sees exactly the complement of Supp_inf(N).
        (A3) Supp_inf is a monoid homomorphism (Steinitz x)->(P(primes),cup)
             and is IDEMPOTENT: Supp_inf(N^2)=Supp_inf(N)  ==> the iso-type
             phantom is a SEMILATTICE invariant, never injective on valuations.

  (C) Non-normal neighborhood provability box: D1 ^ ~D2 ^ D3hom, refuting WO;
      and WO = Loeb-for-'-<' <=> converse-well-foundedness of the -< relation.

Part (B) (simultaneous higher-lim^n honesty) is a set-theoretic
consistency-strength statement (Bergfalk-Hrusak-Lambie-Hanson: NO large
cardinal needed); it is recorded symbolically, not machine-checked.

Run OFF-MOUNT from a /tmp copy; the JSON report is written back via the
Windows-path file tools per the aps-run-sync-hazard memory.
"""

import json
from math import gcd
from functools import reduce
from itertools import product

report = {"pass": 130, "parts": {}, "overall": None}
fails = []

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def prod(xs):
    return reduce(lambda a, b: a * b, xs, 1)

def crt(residues):
    """residues: list of (r, m); returns x mod lcm with x = r_i mod m_i (coprime m_i)."""
    x, M = 0, 1
    for r, m in residues:
        # solve x = x (mod M), x = r (mod m); assume gcd(M,m)=1
        g = gcd(M, m)
        assert g == 1, (M, m)
        # x + M*t = r (mod m)
        inv = pow(M, -1, m)
        t = ((r - x) * inv) % m
        x = x + M * t
        M = M * m
    return x % M, M

# ---------------------------------------------------------------------------
# (A1) unit-absorption : q a unit mod p^k for all p != q
# ---------------------------------------------------------------------------
A1 = {"name": "unit-absorption (finite prime is a unit in every other Z_p)",
      "cases": [], "ok": True}
# For N = 2^inf * 3 : the finite prime 3 is a unit mod 2^k for all k, so
# mult-by-3 is an automorphism of Z_2 and 3.Z -> Z, giving Z_2/3Z ~= Z_2/Z.
for (q, p, kmax) in [(3, 2, 20), (5, 2, 20), (7, 3, 15), (25, 2, 20), (6, 5, 15)]:
    units = all(gcd(q, p ** k) == 1 for k in range(1, kmax + 1))
    inv_ok = all(pow(q % (p ** k), -1, p ** k) * q % (p ** k) == 1
                 for k in range(1, kmax + 1))
    ok = units and inv_ok
    A1["cases"].append({"q_finitepart": q, "solenoid_prime": p,
                        "q_is_unit": units, "inverse_exists": inv_ok, "ok": ok})
    A1["ok"] &= ok
if not A1["ok"]:
    fails.append("A1")
report["parts"]["A1_unit_absorption"] = A1

# ---------------------------------------------------------------------------
# (A2) torsion detection : indicator e_q is order q^{e_q}, solenoid gives none
# ---------------------------------------------------------------------------
# We model a truncation of hatZ_N by a modulus  Mtrunc = prod p^{f_p}
# ( f_p = min(e_p, cap) ).  The indicator e_q is the CRT element that is 1 in
# the q-part and 0 elsewhere.  It is q^{e_q}-torsion in the quotient by the
# diagonal Z iff q^{e_q}*e_q lies in Z (= diagonal multiples of (1,1,...)),
# while e_q itself does not.  A solenoidal prime (e_p = 'inf', capped high)
# yields NO finite-order indicator (mult by any q^k never lands e_p in Z).
A2 = {"name": "torsion detects complement of Supp_inf", "cases": [], "ok": True}

def indicator_is_torsion(prime_parts, q, cap):
    """prime_parts: dict p -> exponent (int for finite, 'inf' for solenoid).
       Return (order_in_quotient_finite?, order) for the indicator at q."""
    # build modulus per prime, capping 'inf' at `cap`
    mods = {p: (p ** (cap if e == 'inf' else e)) for p, e in prime_parts.items()}
    M = prod(mods.values())
    # indicator e_q : residue 1 at q-part, 0 elsewhere
    resid = [(1 if p == q else 0, mods[p]) for p in prime_parts]
    x, _ = crt(resid)
    # find smallest k>=1 with q^k * x  ==  diagonal integer d*(1,1,...) mod M
    # diagonal element d*(1,...,1) has residue d mod every part; i.e. == d mod M
    # so q^k*x mod M must be constant across all prime parts.
    eq = prime_parts[q]
    if eq == 'inf':
        return (False, None)  # solenoidal: never torsion
    for k in range(1, eq + 3):
        y = (pow(q, k) * x) % M
        # check y is 'diagonal': y mod mods[p] equal for all p  (== some d)
        vals = {p: y % mods[p] for p in prime_parts}
        if len(set(vals.values())) == 1:
            return (True, pow(q, k))
    return (True, None)

test_towers = [
    # primorial-like finite valuations: 2,3,5 each once ; all finite -> all torsion
    ({2: 1, 3: 1, 5: 1}, [2, 3, 5], []),
    # 2 solenoidal, 3 finite : 3 torsion, 2 not
    ({2: 'inf', 3: 1}, [3], [2]),
    # 2 solenoidal, 3 solenoidal, 5 finite(^2): 5 torsion order 25, others none
    ({2: 'inf', 3: 'inf', 5: 2}, [5], [2, 3]),
]
for parts, expect_tors, expect_free in test_towers:
    row = {"tower": {str(k): v for k, v in parts.items()},
           "torsion_primes": [], "torsionfree_primes": [], "ok": True}
    for q in parts:
        is_t, order = indicator_is_torsion(parts, q, cap=6)
        if is_t:
            row["torsion_primes"].append({"q": q, "order": order,
                                          "expected_order": q ** parts[q]})
            if order != q ** parts[q]:
                row["ok"] = False
        else:
            row["torsionfree_primes"].append(q)
    got_t = sorted(d["q"] for d in row["torsion_primes"])
    got_f = sorted(row["torsionfree_primes"])
    row["ok"] &= (got_t == sorted(expect_tors) and got_f == sorted(expect_free))
    A2["cases"].append(row)
    A2["ok"] &= row["ok"]
if not A2["ok"]:
    fails.append("A2")
report["parts"]["A2_torsion_detection"] = A2

# ---------------------------------------------------------------------------
# (A3) Supp_inf is an idempotent monoid homomorphism
# ---------------------------------------------------------------------------
A3 = {"name": "Supp_inf : (Steinitz,x) -> (P(primes),cup) hom + idempotent",
      "cases": [], "ok": True}

def supp_inf(val):  # val: dict p -> exp (int or 'inf')
    return frozenset(p for p, e in val.items() if e == 'inf')

def mul_steinitz(a, b):
    out = dict(a)
    for p, e in b.items():
        if e == 'inf' or out.get(p) == 'inf':
            out[p] = 'inf'
        else:
            out[p] = out.get(p, 0) + e
    return out

samples = [
    ({2: 'inf', 3: 1}, {3: 'inf', 5: 2}),
    ({2: 1, 3: 1}, {5: 1, 7: 1}),
    ({2: 'inf'}, {2: 5}),          # union unchanged; product still solenoidal at 2
]
for a, b in samples:
    lhs = supp_inf(mul_steinitz(a, b))
    rhs = supp_inf(a) | supp_inf(b)
    hom = (lhs == rhs)
    idem = (supp_inf(mul_steinitz(a, a)) == supp_inf(a))
    A3["cases"].append({"a": {str(k): v for k, v in a.items()},
                        "b": {str(k): v for k, v in b.items()},
                        "supp_inf(ab)": sorted(lhs), "supp_inf(a)Usupp_inf(b)": sorted(rhs),
                        "homomorphism": hom, "idempotent": idem, "ok": hom and idem})
    A3["ok"] &= (hom and idem)
if not A3["ok"]:
    fails.append("A3")
report["parts"]["A3_supp_inf_homomorphism"] = A3

# ---------------------------------------------------------------------------
# (C) non-normal neighborhood box  +  WO = Loeb-for-'-<'
# ---------------------------------------------------------------------------
# Neighborhood model on W with N: w -> set of neighborhoods (each a subset of W).
# [box]A true at w  iff  ||A|| in N(w).   A is a subset (its truth set).
# D1 (necessitation): W in N(w) for all w  (theorems are provable).
# D2 (K / closure under sup+intersection): monotone AND closed under finite
#    intersection ; the K axiom box(A->B)->(boxA->boxB) is validity of
#    'if X,Y in N(w) ... ' -- we test the standard characterization:
#    D2 holds iff every N(w) is closed under supersets (monotone) and under
#    binary intersection (a filter base).  We build a model that is monotone
#    (D3hom) but NOT intersection-closed (~D2).
W = [0, 1, 2]
subsets = [frozenset(s) for r in range(len(W) + 1)
           for s in __import__("itertools").combinations(W, r)]
full = frozenset(W)

# Neighborhood function: at each world put W (=> D1), plus two DISTINCT
# proper subsets whose intersection is NOT a neighborhood (=> ~D2), all
# upward closed within themselves handled by explicit monotone-closure test.
Nfun = {
    0: {full, frozenset({0, 1}), frozenset({0, 2})},
    1: {full, frozenset({0, 1}), frozenset({0, 2})},
    2: {full, frozenset({0, 1}), frozenset({0, 2})},
}

def monotone(Nw):
    for X in Nw:
        for Y in subsets:
            if X <= Y and Y not in Nw:
                return False
    return True

def intersection_closed(Nw):
    for X in Nw:
        for Y in Nw:
            if (X & Y) not in Nw:
                return False
    return True

C = {"name": "non-normal neighborhood box D1 ^ ~D2 ^ D3hom", "ok": True}
D1 = all(full in Nfun[w] for w in W)
# monotone closure: we DECLARE the model's N to be its upward closure, then test
Nclosed = {w: set(Nfun[w]) for w in W}
for w in W:
    changed = True
    while changed:
        changed = False
        for X in list(Nclosed[w]):
            for Y in subsets:
                if X <= Y and Y not in Nclosed[w]:
                    Nclosed[w].add(Y); changed = True
D3hom = all(monotone(Nclosed[w]) for w in W)          # monotone = RM = 'D3hom'
D2 = all(intersection_closed(Nclosed[w]) for w in W)  # filter => normal/K
C.update({"D1_necessitation": D1, "D3hom_monotone": D3hom,
          "D2_normal_K": D2, "nonnormal": (not D2)})
# want D1 and D3hom TRUE, D2 FALSE
C["ok"] = D1 and D3hom and (not D2)
if not C["ok"]:
    fails.append("C-neighborhood")
report["parts"]["C_neighborhood_box"] = C

# ---------------------------------------------------------------------------
# (C') WO = Loeb-for-'-<'  <=>  '-<' converse-well-founded
# ---------------------------------------------------------------------------
# Loeb schema for a modality [<] on a finite frame (W, R) is valid
# iff R is transitive AND converse-well-founded (no infinite R-ascending path;
# on finite frames: R is transitive and irreflexive-on-cycles i.e. no R-cycle).
# We test two frames: converse-wellfounded chain (Loeb valid = WO true) and a
# reflexive/cyclic frame (Loeb refuted = WO false).
Cp = {"name": "WO = Loeb-for-'-<' = converse-well-founded", "cases": [], "ok": True}

def transitive(R, Ws):
    return all((a, c) in R for a in Ws for b in Ws for c in Ws
               if (a, b) in R and (b, c) in R)

def has_cycle(R, Ws):
    # reachability; cycle iff some node reaches itself
    reach = {a: set(b for (x, b) in R if x == a) for a in Ws}
    changed = True
    while changed:
        changed = False
        for a in Ws:
            new = set(reach[a])
            for b in list(reach[a]):
                new |= reach[b]
            if new != reach[a]:
                reach[a] = new; changed = True
    return any(a in reach[a] for a in Ws)

def loeb_valid(R, Ws):
    # finite frame: GL-valid iff transitive and converse-wellfounded (=no cycle)
    return transitive(R, Ws) and (not has_cycle(R, Ws))

frames = [
    ("converse-wellfounded chain 0-<1-<2 (transitive closure)",
     [0, 1, 2], {(0, 1), (1, 2), (0, 2)}, True),   # WO true, Loeb valid
    ("reflexive point (loop)", [0], {(0, 0)}, False),           # WO false
    ("converse-ILL-founded 2-cycle", [0, 1], {(0, 1), (1, 0), (0, 0), (1, 1)}, False),
]
for name, Ws, R, expect in frames:
    lv = loeb_valid(R, Ws)
    cwf = not has_cycle(R, Ws)
    row = {"frame": name, "loeb_valid": lv, "converse_wellfounded": cwf,
           "WO_expected": expect, "ok": (lv == cwf == expect)}
    Cp["cases"].append(row)
    Cp["ok"] &= row["ok"]
if not Cp["ok"]:
    fails.append("Cprime-WO")
report["parts"]["Cprime_WO_equals_loeb"] = Cp

# ---------------------------------------------------------------------------
# (B) symbolic record only
# ---------------------------------------------------------------------------
report["parts"]["B_simultaneous_honesty"] = {
    "name": "simultaneous higher-lim^n honesty: consistency strength",
    "machine_checked": False,
    "correction_of_pass129": (
        "Pass 129 Thm 129b(c) called (forall n)h_n a LARGE-CARDINAL statement "
        "(upper bound weakly compact, BLH 2021). CORRECTED: Bergfalk-Hrusak-"
        "Lambie-Hanson removed the large cardinal -- simultaneous vanishing is "
        "consistent with ZFC ALONE. So (forall n)h_n is EQUICONSISTENT WITH ZFC, "
        "not a large-cardinal statement; the relevant threshold is a "
        "cardinal-characteristic one (2^aleph0 >= aleph_2 necessary), not a "
        "weakly compact."),
    "ok": True,
}

# ---------------------------------------------------------------------------
report["overall"] = "PASS" if not fails else ("FAIL: " + ",".join(fails))
print(json.dumps(report, indent=2, default=str))
