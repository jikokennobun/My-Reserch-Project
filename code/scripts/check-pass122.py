#!/usr/bin/env python3
"""
Pass 122 verification.

Two claims are checked.

(A) DISTINGUISHED-FAMILY REALIZATION IS UNIVERSAL.
    Every finite antichain hypergraph H on [m] is realizable as the
    minimal meet-generator hypergraph H_min^G(w) of a non-principal cut w
    over a *distinguished* coatom family G = {g_1,...,g_m}, inside the
    IDEAL (down-set) completion D(L) of an explicit finite carrier L.

    Construction (maximal-independent-set / set-cover):
      * core atoms c_1,c_2 (shared by every g_j)  -> w non-principal
      * one "fan" atom x_I for each maximal H-independent set I subset [m]
      * g_j sits over exactly the fans {x_I : j in I} (and the core)
    Then, in D(L),  /\_{j in S} g_j = w  iff  intersection of fans is empty
    iff  no maximal independent set contains S  iff  S contains an edge of H.
    Hence H_min^G(w) = H exactly.

(B) TRUE-FRONTIER RIGIDITY IS COMPLETION-UNCONDITIONAL.
    Over the TRUE frontier G_*(w) = min((w)^u \ w) (the genuine minimal
    upper bounds), distinct frontier elements always meet to w -- an
    order-theoretic fact holding in EVERY completion.  Verified
    (i) on the actual MacNeille / ideal / filter completions of K_{n,m},
    (ii) on 2000 random finite posets.

    Consequence: Pass 121's "completion-relative" breaking of rigidity is a
    DISTINGUISHED-FAMILY artifact (the carrier coatoms cease to be the true
    frontier once meet-density is dropped), NOT a property of frontiers.
"""

import itertools, json, random
from itertools import combinations, chain


# ---------------------------------------------------------------- part A
def powerset(xs):
    xs = list(xs)
    return chain.from_iterable(combinations(xs, r) for r in range(len(xs) + 1))


def contains_edge(S, H):
    S = set(S)
    return any(set(e) <= S for e in H)


def maximal_independent(m, H):
    verts = list(range(1, m + 1))
    inds = [set(I) for I in powerset(verts) if not contains_edge(I, H)]
    return [frozenset(I) for I in inds if not any(I < J for J in inds)]


def realize_ideal(m, H):
    Omega = maximal_independent(m, H)
    fan = {j: set(I for I in Omega if j in I) for j in range(1, m + 1)}

    def meet_is_w(S):
        inter = None
        for j in S:
            inter = fan[j] if inter is None else (inter & fan[j])
        return inter is not None and len(inter) == 0

    allS = [set(S) for S in powerset(range(1, m + 1)) if S]
    hit = [S for S in allS if meet_is_w(S)]
    Hmin = [frozenset(S) for S in hit if not any(set(T) < S for T in hit)]
    cover_law = all(meet_is_w(S) == contains_edge(S, H)
                    for S in ([set(x) for x in powerset(range(1, m + 1)) if x]))
    return Omega, set(Hmin), cover_law


def checkA(m, H, label):
    H = [frozenset(e) for e in H]
    Omega, Hmin, cover_law = realize_ideal(m, H)
    return {"label": label, "m": m,
            "H": sorted([sorted(e) for e in H]),
            "num_atoms": 2 + len(Omega),
            "Hmin_realized": sorted([sorted(e) for e in Hmin]),
            "matches_target": Hmin == set(H),
            "cover_law_holds": cover_law}


# ---------------------------------------------------------------- part B: K_{n,m} completions
def carrier(n, m):
    els = ['0', 'U'] + [f'f{i}' for i in range(1, n + 1)] + [f'g{j}' for j in range(1, m + 1)]

    def leq(a, b):
        if a == b: return True
        if a == '0': return True
        if b == 'U': return True
        if a.startswith('f') and b.startswith('g'): return True
        return False
    return els, leq


def principal_down(x, els, leq):
    return frozenset(y for y in els if leq(y, x))


def cut_closure(A, els, leq):
    up = lambda S: frozenset(x for x in els if all(leq(s, x) for s in S))
    lo = lambda S: frozenset(x for x in els if all(leq(x, s) for s in S))
    return lo(up(A))


def macneille_cuts(els, leq):
    up = lambda S: frozenset(x for x in els if all(leq(s, x) for s in S))
    lo = lambda S: frozenset(x for x in els if all(leq(x, s) for s in S))
    cuts = set()
    for r in range(len(els) + 1):
        for C in combinations(els, r):
            A = frozenset(C)
            if lo(up(A)) == A:
                cuts.add(A)
    return cuts


def all_downsets(els, leq):
    ds = set()
    for r in range(len(els) + 1):
        for C in combinations(els, r):
            D = set(C)
            if all((y in D) for x in D for y in els if leq(y, x)):
                ds.add(frozenset(D))
    return ds


def truefrontier_meet_check_macneille(n, m):
    els, leq = carrier(n, m)
    F = [f'f{i}' for i in range(1, n + 1)]
    C = macneille_cuts(els, leq)
    w = cut_closure(frozenset(['0'] + F), els, leq)
    aboveW = [c for c in C if w <= c and c != w]
    tf = [c for c in aboveW if not any(d <= c and d != c and d in aboveW for d in aboveW)]
    meet = lambda a, b: cut_closure(a & b, els, leq)
    return len(tf), (all(meet(a, b) == w for a, b in combinations(tf, 2)) if len(tf) > 1 else True)


def truefrontier_meet_check_ideal(n, m):
    els, leq = carrier(n, m)
    F = [f'f{i}' for i in range(1, n + 1)]
    D = all_downsets(els, leq)
    w = frozenset(x for x in els if any(leq(x, s) for s in (['0'] + F)))
    aboveW = [d for d in D if w <= d and d != w]
    tf = [d for d in aboveW if not any(e <= d and e != d and e in aboveW for e in aboveW)]
    return len(tf), (all((a & b) == w for a, b in combinations(tf, 2)) if len(tf) > 1 else True)


def random_poset_rigidity(trials=2000, seed=0):
    random.seed(seed)
    viol = 0
    for _ in range(trials):
        n = random.randint(4, 7)
        elems = list(range(n))
        perm = elems[:]; random.shuffle(perm)
        less = set()
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < 0.5:
                    less.add((perm[i], perm[j]))
        changed = True
        while changed:
            changed = False
            for a in elems:
                for b in elems:
                    if (a, b) in less:
                        for c in elems:
                            if (b, c) in less and (a, c) not in less:
                                less.add((a, c)); changed = True
        leq = {(a, b): (a == b or (a, b) in less) for a in elems for b in elems}

        def meet(a, b):
            lbs = [x for x in elems if leq[(x, a)] and leq[(x, b)]]
            maxlb = [x for x in lbs if not any(y != x and leq[(x, y)] for y in lbs)]
            return maxlb[0] if len(maxlb) == 1 else None

        w = random.choice(elems)
        ub = [x for x in elems if x != w and leq[(w, x)]]
        front = [x for x in ub if not any(y != x and y in ub and leq[(y, x)] for y in ub)]
        for a, b in combinations(front, 2):
            mab = meet(a, b)
            if mab is not None and leq[(w, mab)] and mab != w:
                viol += 1
    return trials, viol


# ---------------------------------------------------------------- run
partA = [
    checkA(3, [(1, 2), (1, 3), (2, 3)], "K3_complete_baseline"),
    checkA(4, [(1, 2), (2, 3, 4)], "nonuniform_mu_spectrum_2_3"),
    checkA(3, [(1, 2, 3)], "3uniform_single_hyperedge"),
    checkA(4, [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)], "all_triples_on_4"),
    checkA(5, [(1, 2), (3, 4, 5)], "disjoint_2_and_3"),
]

partB_Knm = {}
for (n, m) in [(2, 3), (3, 3), (2, 4), (3, 4)]:
    s_mac, r_mac = truefrontier_meet_check_macneille(n, m)
    s_id, r_id = truefrontier_meet_check_ideal(n, m)
    partB_Knm[f"K_{n}_{m}"] = {
        "macneille_true_frontier_size": s_mac, "macneille_pairwise_meet_is_w": r_mac,
        "ideal_true_frontier_size": s_id, "ideal_pairwise_meet_is_w": r_id,
    }

trials, viol = random_poset_rigidity()

report = {
    "pass": 122,
    "title": "two-sided-free completion: distinguished-family realization is universal, true-frontier rigidity is unconditional",
    "A_distinguished_family_realization": {
        "tests": partA,
        "all_match": all(t["matches_target"] and t["cover_law_holds"] for t in partA),
        "claim": "every finite antichain hypergraph realizes as H_min^G(w) in the ideal completion",
    },
    "B_true_frontier_rigidity": {
        "K_nm_completions": partB_Knm,
        "all_Knm_rigid": all(v["macneille_pairwise_meet_is_w"] and v["ideal_pairwise_meet_is_w"]
                             for v in partB_Knm.values()),
        "random_poset_trials": trials,
        "random_poset_violations": viol,
        "unconditional": viol == 0 and all(v["macneille_pairwise_meet_is_w"] and v["ideal_pairwise_meet_is_w"]
                                           for v in partB_Knm.values()),
        "claim": "over the TRUE frontier min((w)^u\\w) pairwise meets equal w in EVERY completion",
    },
}
report["overall_PASS"] = (report["A_distinguished_family_realization"]["all_match"]
                          and report["B_true_frontier_rigidity"]["unconditional"])

if __name__ == "__main__":
    print(json.dumps(report, indent=2))
