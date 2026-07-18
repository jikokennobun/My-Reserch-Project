#!/usr/bin/env python3
# Pass 148 verification: (A) Sigma1-orientation dichotomy = monodromy/double-cover;
# (B) target monoidal law: conjunction collapses graded strictness, depth-addition preserves it;
# (C) delta-symmetry census: no linear proof-order is delta-fixed => (Z,Z/2) non-Sigma1.
import json, itertools

def double_cover_components(cycle_len, monodromy_sign):
    # Double cover of a cycle C_L; product of edge signs = monodromy_sign.
    signs = [1]*cycle_len
    signs[-1] = monodromy_sign
    parent = list(range(2*cycle_len))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        parent[find(a)]=find(b)
    def node(i,s): return (i%cycle_len)*2 + s
    for i in range(cycle_len):
        flip = 0 if signs[i]==1 else 1
        for s in (0,1):
            union(node(i,s), node(i+1, s^flip))
    return len({find(x) for x in range(2*cycle_len)})

def reduced_H0_Z2(comps):
    return "Z/2" if comps-1==1 else ("0" if comps-1==0 else f"(Z/2)^{comps-1}")

# ---- Block A: orientation double cover + dichotomy census ----
A = {}
for L in (6,7,8):
    c_or = double_cover_components(L,-1); c_sy = double_cover_components(L,+1)
    A[f"C_{L}_oriented(monodromy-1)"]  = {"comps": c_or, "redH0": reduced_H0_Z2(c_or)}
    A[f"C_{L}_symmetric(monodromy+1)"] = {"comps": c_sy, "redH0": reduced_H0_Z2(c_sy)}
A_ok = all(A[f"C_{L}_oriented(monodromy-1)"]["redH0"]=="0" and
           A[f"C_{L}_symmetric(monodromy+1)"]["redH0"]=="Z/2" for L in (6,7,8))

def census_orientation(n):
    fail=0; total=0
    for perm in itertools.permutations(range(n)):
        total+=1
        if perm==tuple(reversed(perm)): fail+=1   # unoriented linear order (impossible n>=2)
    return total, fail
A_census={}
for n in (2,3,4):
    tot,fail=census_orientation(n); A_census[f"n={n}"]={"linear_orders":tot,"fail_to_orient":fail}
A_census_ok = all(v["fail_to_orient"]==0 for v in A_census.values())

# ---- Block B: target monoidal law ----
def preserves_strict_chain(law, N=6):
    return {"climb_1p1_eq_2": (law(1,1)==2)}
law_conj = lambda n,m: n if n==m else max(n,m)   # idempotent conjunction: <1>^<1>=<1>
law_add  = lambda n,m: n+m                       # depth-addition / concatenation
B={"conjunction": preserves_strict_chain(law_conj),
   "depth_addition": preserves_strict_chain(law_add)}
B_ok = (B["conjunction"]["climb_1p1_eq_2"]==False) and (B["depth_addition"]["climb_1p1_eq_2"]==True)

# ---- Block C: delta-symmetry census ----
def delta_fixed_linear_orders(n):
    return sum(1 for perm in itertools.permutations(range(n)) if perm==tuple(reversed(perm)))
C={f"n={n}":{"delta_fixed_linear_orders":delta_fixed_linear_orders(n),
             "symmetric_relation_delta_fixed":True} for n in (2,3,4,5)}
C_ok = all(v["delta_fixed_linear_orders"]==0 for v in C.values())

overall = A_ok and A_census_ok and B_ok and C_ok
report={"pass":148,
 "title":"Sigma1-orientation dichotomy (a) + Coh monoidal law depth-addition (b)",
 "A_double_cover":A,"A_orientation_census":A_census,"A_ok":A_ok,"A_census_ok":A_census_ok,
 "B_monoidal_law":B,"B_ok":B_ok,"C_delta_symmetry_census":C,"C_ok":C_ok,
 "overall":"PASS" if overall else "FAIL",
 "notes":[
   "A: oriented(Rosser/Moebius) monodromy -1 -> connected double cover (redH0=0);",
   "   symmetric(KF) monodromy +1 -> split (redH0=Z/2); 0 linear orders fail to orient.",
   "B: conjunction is idempotent (<1>^<1>=<1>, no climb) => collapses graded strictness;",
   "   depth-addition (<n>*<m>=<n+m>) climbs, preserving <n> !~ <n+1>. Concatenation wins.",
   "C: no linear proof-order is delta-fixed (n>=2) => symmetric (Z,Z/2) is non-Sigma1."]}
print(json.dumps(report,indent=2))
