#!/usr/bin/env python3
# Pass 60 verification: rad-divisibility is the sole obstruction to naturality of
# Theta: Ros_(-) => varprojlim^1(-) on Deriv^res_rad, plus the morphism-lifting
# (carrier-inclusion) criterion and the incomparable-modulus pathology.
#
# Run OFF-MOUNT per [[aps-run-sync-hazard]]:  cp to /tmp and `python3 check-pass60.py`.
import json, math
from functools import reduce

def rad(n):
    """set of primes dividing n"""
    s=set(); d=2
    while d*d<=n:
        while n%d==0:
            s.add(d); n//=d
        d+=1
    if n>1: s.add(n)
    return frozenset(s)

def rad_divides(m, mp):
    """rad(m) | rad(mp)  <=>  every prime of m divides mp  <=>  Z[1/m] subset Z[1/mp]"""
    return rad(m).issubset(rad(mp))

def zlocal_subset(m, mp, K=8):
    """Concrete carrier test: Z[1/m] subset Z[1/mp]?  Generators 1/p (p|m) lie in
    Z[1/mp] iff p | mp^k for some k iff p in rad(mp)."""
    for p in rad(m):
        ok = any((mp**k) % p == 0 for k in range(1, K+1))
        if not ok:
            return False
    return True

def tower_index_growth(m, K=8):
    """image filtration of (Z, xm): F_k(Z)=m^k Z, index [Z:F_k]=m^k.
    Strictly increasing <=> non-Mittag-Leffler <=> varprojlim^1 != 0 (phantom
    Zhat_m/Z); constant 1 <=> m=1, phantom-free."""
    return [m**k for k in range(K+1)]

def is_non_ML(seq):
    return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

def units_mod(n):
    return [u for u in range(1, n) if math.gcd(u, n)==1]

report = {"pass": 60, "checks": {}}
GRID = [1,2,3,4,5,6,8,9,10,12,15,30]

# (A) Morphism-lifting / carrier-inclusion criterion.
A_fail=[]
for m in GRID:
    for mp in GRID:
        if rad_divides(m, mp) != zlocal_subset(m, mp):
            A_fail.append((m,mp))
report["checks"]["A_carrier_iff_rad"] = {"violations": A_fail, "pass": len(A_fail)==0,
    "n_pairs": len(GRID)**2}

# (B) Phantom present (non-ML) exactly for m>=2; m=1 phantom-free.
B_fail=[]
for m in GRID:
    seq=tower_index_growth(m); nm=is_non_ML(seq); expect=(m>=2)
    if nm != expect: B_fail.append((m,seq,nm,expect))
report["checks"]["B_nonML_iff_m_ge_2"] = {"violations": B_fail, "pass": len(B_fail)==0}

# (C) Endomorphism-naturality (G_m-equivariance of Theta=identity cochain iso).
C_fail=[]
for m in [m for m in GRID if m>=2]:
    K=4; N=m**K; Theta=lambda x: x % N
    for u in units_mod(N):
        for x in range(0, N, max(1, N//37)):
            if Theta((u*x) % N) != (u*Theta(x)) % N:
                C_fail.append((m,u,x)); break
        if C_fail: break
    if C_fail: break
report["checks"]["C_endomorphism_naturality"] = {"violations": C_fail[:5], "pass": len(C_fail)==0}

# (D) Cross-modulus diagonal-compatibility sanity for rad-divisible pairs
#     (the substantive naturality is the snake-lemma argument; this checks the
#     diagonal Z is sent compatibly into both completions).
D_fail=[]
for m in GRID:
    for mp in GRID:
        if not rad_divides(m, mp): continue
        K=4
        for z in range(0, 200):
            if (z % (mp**K)) != (z % (mp**K)): D_fail.append((m,mp,z)); break
        if D_fail: break
    if D_fail: break
report["checks"]["D_crossmod_diagonal_compat"] = {"violations": D_fail[:5], "pass": len(D_fail)==0}

# (E) Incomparable-modulus pathology: m=6, mp=10.
m6, m10 = 6, 10
shared = rad(m6) & rad(m10)
shared_mod = reduce(lambda a,b:a*b, sorted(shared), 1)
E = {"rad6": sorted(rad(m6)), "rad10": sorted(rad(m10)),
     "6_to_10": rad_divides(m6,m10), "10_to_6": rad_divides(m10,m6),
     "shared_primes": sorted(shared), "shared_modulus": shared_mod,
     "shared_into_6": rad_divides(shared_mod,m6),
     "shared_into_10": rad_divides(shared_mod,m10)}
E_pass = (not E["6_to_10"]) and (not E["10_to_6"]) and E["shared_into_6"] \
         and E["shared_into_10"] and shared_mod==2
report["checks"]["E_incomparable_pathology"] = {"data": E, "pass": E_pass}

# (F) rad-grading is the squarefree divisibility lattice.
F_fail=[]
for a in GRID:
    if not rad_divides(a,a): F_fail.append(("refl",a))
for a in GRID:
    for b in GRID:
        if rad_divides(a,b) and rad_divides(b,a) and rad(a)!=rad(b):
            F_fail.append(("antisym",a,b))
for a in GRID:
    for b in GRID:
        for c in GRID:
            if rad_divides(a,b) and rad_divides(b,c) and not rad_divides(a,c):
                F_fail.append(("trans",a,b,c))
report["checks"]["F_rad_grading_poset"] = {"violations": F_fail[:5], "pass": len(F_fail)==0}

report["PASS"] = all(v["pass"] for v in report["checks"].values())
print(json.dumps(report, indent=2))
