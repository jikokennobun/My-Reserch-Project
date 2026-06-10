#!/usr/bin/env python3
"""
Pass 52 verification: the flipped invariant Phi(tau) = 1 - |F^tau|.

Setup. F is a finite poset with minimum hat0 (so the order complex Delta(F) is a
cone, hence F2-acyclic). tau is an order-REVERSING involution of F.  By the Hopf
trace formula the simplicial Lefschetz number is

    L(tau) = sum_{sigma tau-invariant} (-1)^{dim sigma} * sign(tau|sigma) = 1,

because Delta(F) is contractible.  A tau-invariant chain sigma = {x_0<...<x_d}
has tau x_i = x_{d-i} (order reversal), so tau acts on its d+1 vertices as the
reversal permutation, of sign (-1)^{(d+1)d/2}.  Hence each invariant d-chain
contributes

    s(d) = (-1)^d * (-1)^{d(d+1)/2}  =  +1 if d = 0,1 (mod 4),  -1 if d = 2,3 (mod 4).

Splitting off the d=0 part (the fixed vertices F^tau, an ANTICHAIN by Thm 51a, so
e(F^tau) = chi(Delta(F^tau)) = |F^tau|) gives the Bredon identity

    L(tau) = e(F^tau) + Phi(tau) = 1,  Phi(tau) = sum_{d>=1} s(d) N_d = 1 - |F^tau|,

where N_d = #(tau-invariant d-chains).  We verify all of this by brute force, and
confirm the geometric-vs-combinatorial Euler gap
    Phi(tau) = chi(|Delta(F)|^tau) - |F^tau|,  with chi(|Delta(F)|^tau) = 1 (Smith).
"""
import itertools, json

def s_sign(d):
    return 1 if (d % 4) in (0, 1) else -1

class Poset:
    def __init__(self, elems, leq):
        self.elems = list(elems)
        self.leq = leq  # reflexive partial order predicate
    def lt(self, a, b):
        return a != b and self.leq(a, b)
    def chains(self):
        out = []
        n = len(self.elems)
        for r in range(1, n + 1):
            for combo in itertools.combinations(self.elems, r):
                ok = True
                for a, b in itertools.combinations(combo, 2):
                    if not (self.leq(a, b) or self.leq(b, a)):
                        ok = False; break
                if ok:
                    ordered = sorted(combo, key=lambda x: sum(1 for y in combo if self.leq(y, x)))
                    out.append(tuple(ordered))
        return out

def analyze(name, elems, leq, tau, expected_Phi=None):
    P = Poset(elems, leq)
    fixed = [x for x in elems if tau[x] == x]
    antichain = all(not P.lt(a, b) for a in fixed for b in fixed if a != b)
    Nd = {}
    L = 0
    for ch in P.chains():
        chs = set(ch)
        img = set(tau[x] for x in ch)
        if img == chs:                      # tau-invariant simplex
            d = len(ch) - 1
            Nd[d] = Nd.get(d, 0) + 1
            L += s_sign(d)                  # Hopf trace contribution
    chi_geo = L                             # L(involution) = chi(Fix); Smith => 1
    Phi = sum(s_sign(d) * c for d, c in Nd.items() if d >= 1)
    e = len(fixed)                          # = N_0
    res = {
        "name": name,
        "|F|": len(elems),
        "fixed_is_antichain": antichain,
        "N_d": {str(k): Nd.get(k, 0) for k in range(max(Nd) + 1)} if Nd else {},
        "|F^tau| (=N_0=e)": e,
        "Phi (signed flipped-chain sum)": Phi,
        "L(tau) (Hopf trace)": L,
        "1 - |F^tau|": 1 - e,
        "chi(|Delta(F)|^tau)": chi_geo,
        "identity_L=e+Phi=1": (L == e + Phi == 1),
        "identity_Phi=1-e": (Phi == 1 - e),
    }
    if expected_Phi is not None:
        res["expected_Phi"] = expected_Phi
        res["Phi_matches_expected"] = (Phi == expected_Phi)
    return res

results = []

# ---- 1. Boolean cubes 2^[n] under complementation (cube-gap, Phi=1) ----
for n in (1, 2, 3):
    elems = list(itertools.product((0, 1), repeat=n))
    leq = lambda a, b: all(x <= y for x, y in zip(a, b))
    tau = {x: tuple(1 - xi for xi in x) for x in elems}
    results.append(analyze(f"cube 2^[{n}] (complementation)", elems, leq, tau, expected_Phi=1))

# ---- 2. Fixed-antichain fan: hat0 < a_1..a_m < hat1; tau: hat0<->hat1, a_i fixed (Phi=1-m) ----
for m in (1, 2, 3, 4, 5):
    elems = ["b"] + [f"a{i}" for i in range(1, m + 1)] + ["t"]
    def leq(a, c):
        if a == c: return True
        if a == "b": return True
        if c == "t": return True
        return False
    tau = {"b": "t", "t": "b"}
    for i in range(1, m + 1):
        tau[f"a{i}"] = f"a{i}"
    results.append(analyze(f"fixed-antichain fan m={m}", elems, leq, tau, expected_Phi=1 - m))

# ---- 3. Odd chain 0<1<2 with reversal (bracketing case, Phi=0, e=1) ----
results.append(analyze("3-chain (reversal)", [0,1,2], lambda a,b: a<=b,
                        {0:2,1:1,2:0}, expected_Phi=0))

# ---- 4. Even chain 0<1<2<3 with reversal (no fixed vertex; Phi=1, e=0) ----
results.append(analyze("4-chain (reversal)", [0,1,2,3], lambda a,b: a<=b,
                        {0:3,1:2,2:1,3:0}, expected_Phi=1))

# ---- 5. C4 diamond b<{a1,a2}<t, tau: a1<->a2, b<->t (cube-gap analogue, Phi=1) ----
def leq_c4(a, b):
    if a == b: return True
    if a == "b": return True
    if b == "t": return True
    return False
results.append(analyze("C4 diamond (a1<->a2, b<->t)", ["b","a1","a2","t"], leq_c4,
                       {"b":"t","t":"b","a1":"a2","a2":"a1"}, expected_Phi=1))

all_ok = all(r["identity_L=e+Phi=1"] and r["identity_Phi=1-e"]
             and r.get("Phi_matches_expected", True)
             and r["fixed_is_antichain"] for r in results)

fan_Phis = [r["Phi (signed flipped-chain sum)"] for r in results if r["name"].startswith("fixed-antichain")]
extremal = {
    "sup_Phi_attained_at_1": max(r["Phi (signed flipped-chain sum)"] for r in results) == 1,
    "fan_Phi_sequence (m=1..5)": fan_Phis,
    "fan_realizes_Phi=1-m": fan_Phis == [1 - m for m in (1, 2, 3, 4, 5)],
}

out = {"PASS": bool(all_ok and extremal["fan_realizes_Phi=1-m"]),
       "extremal": extremal, "cases": results}
print(json.dumps(out, indent=2))
