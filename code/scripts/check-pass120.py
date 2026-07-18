#!/usr/bin/env python3
"""
Pass 120 verification.

Theme: asymmetric MacNeille frontiers |F| != |G|, the meet-generator hypergraph
H(w), its mu-spectrum, and the FRONTIER MEET-RIGIDITY theorem:

  For a non-principal MacNeille cut w with upper frontier G (min strict upper
  bounds of w), EVERY pair of distinct g,g' in G meets to w in the completion.

Consequences verified here:
  (A) K_{2,3}^{0,U}: |F|=2, |G|=3, mu(w)=2, H_min(w) = complete graph K_3 on G;
      census of antitone synt-FP-free maps fixing w; slack s=|F|-mu=0 forces every
      fixing boxt to inject F onto a DISTINCT pair of frontier g's (no U/repeat image).
  (B) K_{3,3} contrast: slack s=1 (Pass 119 reproduced structurally).
  (C) Rigidity survey: over a family of bounded posets, EVERY non-principal cut's
      minimal meet-generator hypergraph is a COMPLETE graph (0 counterexamples) ->
      negative answer to "does every antichain arise as some H_min(w)".
  (D) Self-healing witness: attempting to force g2 ^ g3 = z > w just inserts z into
      the frontier; rigidity is restored on the enlarged frontier.
"""

from itertools import product, combinations
import json, sys

# ---------- generic finite poset / MacNeille machinery ----------

class Poset:
    def __init__(self, elems, leq_pairs):
        self.E = list(elems)
        S = set(elems)
        self.leq = {(a,b): False for a in self.E for b in self.E}
        for a in self.E:
            self.leq[(a,a)] = True
        for (a,b) in leq_pairs:
            self.leq[(a,b)] = True
        # transitive closure
        changed = True
        while changed:
            changed = False
            for a in self.E:
                for b in self.E:
                    if self.leq[(a,b)]:
                        for c in self.E:
                            if self.leq[(b,c)] and not self.leq[(a,c)]:
                                self.leq[(a,c)] = True
                                changed = True

    def le(self, a, b): return self.leq[(a,b)]

    def lower_bounds(self, S):
        return frozenset(x for x in self.E if all(self.le(x, s) for s in S))

    def upper_bounds(self, S):
        return frozenset(x for x in self.E if all(self.le(s, x) for s in S))

    def cuts(self):
        # every MacNeille cut = lower_bounds(S) for some S subset E; dedupe
        seen = set()
        for r in range(len(self.E)+1):
            for S in combinations(self.E, r):
                seen.add(self.lower_bounds(set(S)))
        # also the whole set (lower_bounds of emptyset = E) and empty handled
        return seen

    def principal(self, x):
        return frozenset(y for y in self.E if self.le(y, x))

    def maxima(self, S):
        S = set(S)
        return [x for x in S if not any(x != y and self.le(x, y) for y in S)]

    def minima(self, S):
        S = set(S)
        return [x for x in S if not any(x != y and self.le(y, x) for y in S)]

    def meet_cut(self, A, B):
        # meet in MacNeille = intersection of down-set cuts
        return frozenset(A & B)

def analyze_cut(P, w):
    """Return (is_principal, F, G) for cut w (frozenset of carrier elems)."""
    principals = {P.principal(x) for x in P.E}
    is_principal = w in principals
    F = sorted(P.maxima(w))                       # lower frontier
    strict_ub = [x for x in P.E if all(P.le(f, x) for f in F) and x not in w]
    G = sorted(P.minima(strict_ub))               # upper frontier
    return is_principal, F, G

def meet_generator_hypergraph(P, w, G):
    """Minimal G' subseteq G with meet(G') == w (meet = lower_bounds)."""
    gens = []
    for r in range(1, len(G)+1):
        for Gp in combinations(G, r):
            if P.lower_bounds(set(Gp)) == w:
                gens.append(frozenset(Gp))
    # minimal ones
    minimal = [g for g in gens if not any(h < g for h in gens)]
    return minimal

# ---------- antitone map census ----------

def antitone_maps(P, fp_free=True):
    E = P.E
    for img in product(E, repeat=len(E)):
        m = dict(zip(E, img))
        ok = True
        for a in E:
            for b in E:
                if P.le(a, b) and not P.le(m[b], m[a]):
                    ok = False; break
            if not ok: break
        if not ok: continue
        if fp_free and any(m[x] == x for x in E):
            continue
        yield m

def boxt_hat(P, m, cut):
    img = set(m[x] for x in cut)
    return P.lower_bounds(img)   # (boxt[C])^l

# ---------- build K_{m,n}^{0,U} ----------

def K_bipartite(m, n):
    fs = [f"f{i}" for i in range(1, m+1)]
    gs = [f"g{j}" for j in range(1, n+1)]
    elems = ["0"] + fs + gs + ["U"]
    pairs = []
    for x in elems:
        pairs.append(("0", x)); pairs.append((x, "U"))
    for f in fs:
        for g in gs:
            pairs.append((f, g))
    return Poset(elems, pairs), fs, gs

report = {"pass": 120, "checks": {}}

# =========== (A) K_{2,3} ===========
P23, fs, gs = K_bipartite(2, 3)
cuts = P23.cuts()
principals = {P23.principal(x) for x in P23.E}
nonprincipal = [c for c in cuts if c not in principals]
assert len(nonprincipal) == 1, f"expected 1 nonprincipal cut, got {len(nonprincipal)}"
w = nonprincipal[0]
isp, F, G = analyze_cut(P23, w)
Hmin = meet_generator_hypergraph(P23, w, G)
mu = min(len(h) for h in Hmin)
# all pairs of G meet to w?
pair_meets = {tuple(sorted(pr)): (P23.lower_bounds(set(pr)) == w) for pr in combinations(G,2)}
report["checks"]["A_K23_basic"] = {
    "carrier": P23.E, "w": sorted(w), "F": F, "G": G,
    "|F|": len(F), "|G|": len(G), "mu": mu,
    "Hmin": [sorted(h) for h in Hmin],
    "all_pairs_meet_to_w": all(pair_meets.values()),
    "complete_graph": sorted([sorted(h) for h in Hmin]) == sorted([sorted(list(pr)) for pr in combinations(G,2)]),
}

# census
total=0; fixing=0; img_repeat=0; img_hasU=0; inter_dist={}
inject_distinct_g=0
for m in antitone_maps(P23, fp_free=True):
    total += 1
    if boxt_hat(P23, m, w) == w:
        fixing += 1
        imgF = [m[f] for f in F]
        boxtF = set(imgF)
        inter = len(boxtF & set(G))
        inter_dist[inter] = inter_dist.get(inter,0)+1
        if len(set(imgF)) < len(imgF): img_repeat += 1
        if "U" in imgF: img_hasU += 1
        if len(set(imgF))==2 and set(imgF) <= set(G): inject_distinct_g += 1
report["checks"]["A_K23_census"] = {
    "antitone_fpfree_total": total, "fixing_w": fixing,
    "fixing_with_repeat_image": img_repeat,
    "fixing_with_U_image": img_hasU,
    "fixing_inject_onto_distinct_g_pair": inject_distinct_g,
    "|boxtF cap G|_distribution": inter_dist,
    "slack_s = |F|-mu": len(F)-mu,
    "forced_injection_onto_frontier_pair": (img_repeat==0 and img_hasU==0 and inject_distinct_g==fixing),
}

# =========== (B) K_{3,3} slack contrast ===========
P33, fs3, gs3 = K_bipartite(3,3)
cuts3 = P33.cuts()
principals3 = {P33.principal(x) for x in P33.E}
np3 = [c for c in cuts3 if c not in principals3]
w3 = np3[0]
isp3, F3, G3 = analyze_cut(P33, w3)
Hmin3 = meet_generator_hypergraph(P33, w3, G3)
mu3 = min(len(h) for h in Hmin3)
report["checks"]["B_K33_contrast"] = {
    "|F|": len(F3), "|G|": len(G3), "mu": mu3,
    "slack_s": len(F3)-mu3,
    "Hmin_is_complete_K3": sorted([sorted(h) for h in Hmin3]) == sorted([sorted(list(pr)) for pr in combinations(G3,2)]),
    "num_nonprincipal_cuts": len(np3),
}

# =========== (C) rigidity survey ===========
survey = []
violations = 0
def survey_poset(name, P):
    global violations
    cuts = P.cuts()
    principals = {P.principal(x) for x in P.E}
    for c in cuts:
        if c in principals: continue
        isp, F, G = analyze_cut(P, c)
        if len(G) < 2:  # cannot be non-principal genuinely; skip degenerate
            # a non-principal cut must have |G|>=2; assert it
            violations += 1
            survey.append({"poset":name,"cut":sorted(c),"BAD_|G|":len(G)})
            continue
        Hmin = meet_generator_hypergraph(P, c, G)
        complete = sorted([sorted(h) for h in Hmin]) == sorted([sorted(list(pr)) for pr in combinations(G,2)])
        mu = min(len(h) for h in Hmin)
        rec = {"poset":name,"|F|":len(F),"|G|":len(G),"mu":mu,"complete_graph":complete}
        survey.append(rec)
        if not complete or mu != 2:
            violations += 1

for (m,n) in [(2,2),(2,3),(3,2),(2,4),(3,3),(3,4),(4,4)]:
    P,_,_ = K_bipartite(m,n)
    survey_poset(f"K_{m}_{n}", P)

report["checks"]["C_rigidity_survey"] = {
    "posets_tested": ["K_2_2","K_2_3","K_3_2","K_2_4","K_3_3","K_3_4","K_4_4"],
    "nonprincipal_cuts_examined": len(survey),
    "rigidity_violations (non-complete or mu!=2)": violations,
    "all_frontier_hypergraphs_complete_graphs": violations==0,
    "detail": survey,
}

# =========== (D) self-healing witness ===========
# Attempt: K_{2,3} but add element z with g2^g3 = z > w, i.e. z below g2,g3, above the f's.
# elems: 0, f1,f2, z, g1,g2,g3, U ; f_i<g_j all; f_i<z; z<g2; z<g3 ; (z NOT < g1)
elemsD = ["0","f1","f2","z","g1","g2","g3","U"]
pairsD = []
for x in elemsD:
    pairsD.append(("0",x)); pairsD.append((x,"U"))
for f in ["f1","f2"]:
    for g in ["g1","g2","g3"]:
        pairsD.append((f,g))
    pairsD.append((f,"z"))
pairsD.append(("z","g2")); pairsD.append(("z","g3"))
PD = Poset(elemsD, pairsD)
cutsD = PD.cuts()
principalsD = {PD.principal(x) for x in PD.E}
npD = [c for c in cutsD if c not in principalsD]
healD = []
for c in npD:
    isp,F,G = analyze_cut(PD, c)
    if len(G)>=1:
        Hmin = meet_generator_hypergraph(PD, c, G) if len(G)>=1 else []
        complete = (len(G)>=2 and sorted([sorted(h) for h in Hmin]) == sorted([sorted(list(pr)) for pr in combinations(G,2)]))
        healD.append({"cut":sorted(c),"F":F,"G":G,"Hmin":[sorted(h) for h in Hmin],"complete":complete})
report["checks"]["D_self_healing"] = {
    "num_nonprincipal_cuts": len(npD),
    "cuts": healD,
    "note": "z enters as a frontier/intermediate element; every non-principal cut still has a complete-graph frontier hypergraph",
    "all_complete": all(h["complete"] for h in healD),
}

# ---------- overall PASS ----------
passA = (report["checks"]["A_K23_basic"]["complete_graph"]
         and report["checks"]["A_K23_basic"]["mu"]==2
         and report["checks"]["A_K23_census"]["forced_injection_onto_frontier_pair"]
         and report["checks"]["A_K23_census"]["fixing_with_U_image"]==0
         and report["checks"]["A_K23_census"]["fixing_with_repeat_image"]==0)
passB = (report["checks"]["B_K33_contrast"]["slack_s"]==1
         and report["checks"]["B_K33_contrast"]["Hmin_is_complete_K3"]
         and report["checks"]["B_K33_contrast"]["mu"]==2)
passC = report["checks"]["C_rigidity_survey"]["all_frontier_hypergraphs_complete_graphs"]
passD = report["checks"]["D_self_healing"]["all_complete"]
report["overall_PASS"] = bool(passA and passB and passC and passD)
report["subresults"] = {"A":bool(passA),"B":bool(passB),"C":bool(passC),"D":bool(passD)}

print(json.dumps(report, indent=2))
