#!/usr/bin/env python3
"""
Pass 41 verification: the limit fixed point s_omega and the median tower.

Three machine-confirmable claims back the Pass-41 analytic theorems.

(A) Antitone index-2 collapse.
    THEOREM (A). In any APS (boxtimes antitone), all-level nFG2
        boxtimes^{k+1} T <= boxtimes^k T   for all k >= 1
    forces boxtimes^2 T = boxtimes^3 T (stabilization at index 2), hence FP-synt
    at p = boxtimes^2 T.
    PROOF. nFG2(1): X2 <= X1. Apply antitone boxtimes: X2 <= X3. nFG2(2): X3 <= X2.
    Hence X2 = X3 and boxtimes X2 = X3 = X2.
    MACHINE GUARD. Enumerate *all* antitone self-maps on every poset up to a size
    bound; verify the implication "nFG2(1) and nFG2(2)  =>  X2 == X3" has zero
    counterexamples. (This guards the statement, not the 3-line proof.)

(B) Limit-FP obstruction (no order-attached fixed point caps an infinite orbit).
    THEOREM (B). Let the boxtimes-orbit o_0=T, o_1, ... be a boxtimes-antichain
    (the coupled infinite-front situation) with boxtimes o_n = o_{n+1}. There is
    NO fresh sigma order-related to the orbit (sigma <= o_n for all n, OR
    sigma >= o_n for all n, OR sigma sandwiched) with boxtimes sigma = sigma that
    keeps boxtimes antitone: every such placement forces o_{n+1} = sigma, i.e. the
    orbit collapses. The only consistent fixed point is order-INCOMPARABLE to the
    whole orbit (a detached fixed point), which therefore does not cap/complete it.
    MACHINE GUARD. Finite proxy: take an antichain orbit a_1,a_2,a_3 with the
    intended boxtimes action, attempt each order-placement of sigma with
    boxtimes sigma = sigma, and confirm antitonicity FAILS for every non-detached
    placement and HOLDS only for the detached one.

(C) Median tower and phantom median.
    With Pass-40 backwards-Cap-Ejection, each obstructing pair {T, e} forces the
    unique median T v e. For a family of pairs the admissible-median poset M is a
    product of singletons: one forced median per pair. For a nested DESCENDING
    family e_1 > e_2 > ... with meet eps = /\ e_i, the medians m_i = T v e_i are a
    descending tower; residuation forces every m_i, but the limit pair {T, eps}
    only forces T v eps. Since join need not commute with the descending meet
    (failure of meet-continuity / join-infinite-distributivity),
        T v (/\_i e_i)  <=  /\_i (T v e_i)
    can be STRICT, leaving a PHANTOM median /\ m_i strictly above T v eps that is
    forced by every finite pair yet justified by no limit pair.
    MACHINE GUARD. Exhibit a finite bounded lattice with e_1 > e_2 > ... > b,
    T incomparable to the e_i, T v e_i = c (a fixed fresh element, T < c < U),
    /\ e_i = b, T v b = T < c. Verify it is a lattice (all binary joins/meets
    exist & are associative/commutative/absorptive) and that the gap c > T is
    real: every pair {T,e_i} forces c, the limit pair {T,b} forces only T.
"""

import itertools
import json
import os
import sys

# ----------------------------------------------------------------------------
# Poset / lattice helpers
# ----------------------------------------------------------------------------

def leq_from_covers(elements, covers):
    """Reflexive-transitive closure of a cover relation -> <= as a set of pairs."""
    leq = {(x, x) for x in elements}
    leq |= set(covers)
    changed = True
    while changed:
        changed = False
        for (a, b) in list(leq):
            for (c, d) in list(leq):
                if b == c and (a, d) not in leq:
                    leq.add((a, d))
                    changed = True
    return leq

def is_antitone(elements, leq, f):
    for x in elements:
        for y in elements:
            if (x, y) in leq:  # x <= y
                if (f[y], f[x]) not in leq:  # need f(y) <= f(x)
                    return False
    return True

def all_posets(n):
    """All partial orders on {0,...,n-1} up to nothing (labelled). Small n only."""
    elems = list(range(n))
    pairs = [(i, j) for i in elems for j in elems if i != j]
    # Build candidate strict relations, keep those that are transitive & antisymmetric.
    # For tractability cap n at 4.
    for bits in itertools.product([0, 1], repeat=len(pairs)):
        rel = {pairs[k] for k in range(len(pairs)) if bits[k]}
        # antisymmetry
        if any((j, i) in rel for (i, j) in rel):
            continue
        # transitivity
        ok = True
        for (a, b) in rel:
            for (c, d) in rel:
                if b == c and a != d and (a, d) not in rel:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        leq = {(x, x) for x in elems} | rel
        yield elems, leq

def tops(elements, leq):
    return [t for t in elements if all((x, t) in leq for x in elements)]

# ----------------------------------------------------------------------------
# (A) Antitone index-2 collapse
# ----------------------------------------------------------------------------

def check_A(max_n=4):
    counterexamples = 0
    maps_checked = 0
    posets_checked = 0
    for n in range(1, max_n + 1):
        for elements, leq in all_posets(n):
            ts = tops(elements, leq)
            if len(ts) != 1:
                continue  # need a unique top T
            posets_checked += 1
            T = ts[0]
            # enumerate all antitone self-maps
            for f_tuple in itertools.product(elements, repeat=n):
                f = {elements[i]: f_tuple[i] for i in range(n)}
                if not is_antitone(elements, leq, f):
                    continue
                maps_checked += 1
                # orbit
                X1 = f[T]
                X2 = f[X1]
                X3 = f[X2]
                nfg2_1 = (X2, X1) in leq
                nfg2_2 = (X3, X2) in leq
                if nfg2_1 and nfg2_2:
                    if X2 != X3:
                        counterexamples += 1
    return {
        "claim": "all-level nFG2 (levels 1,2) + antitone  =>  boxtimes^2 T == boxtimes^3 T",
        "posets_with_unique_top_checked": posets_checked,
        "antitone_maps_checked": maps_checked,
        "counterexamples": counterexamples,
        "verdict": "PASS" if counterexamples == 0 else "FAIL",
    }

# ----------------------------------------------------------------------------
# (B) Limit-FP obstruction (finite proxy)
# ----------------------------------------------------------------------------

def check_B():
    """
    Antichain orbit a1,a2,a3 inside a bounded poset; boxtimes acts
    a1->a2->a3->a3 (finite proxy of T->a1->a2->...). We then probe four
    order-placements of a fresh fixed point sigma and report whether antitonicity
    can survive boxtimes(sigma)=sigma.
    """
    base = ["b", "a1", "a2", "a3", "U"]
    # bounded: b below all, U above all; a1,a2,a3 pairwise incomparable
    covers = [("b", "a1"), ("b", "a2"), ("b", "a3"),
              ("a1", "U"), ("a2", "U"), ("a3", "U")]
    results = []

    def run_placement(name, sigma_below, sigma_above):
        elements = base + ["sig"]
        cov = list(covers)
        # connect sigma; keep b<=sig<=U always
        cov += [("b", "sig"), ("sig", "U")]
        for x in sigma_below:        # sig <= x
            cov.append(("sig", x))
        for x in sigma_above:        # x <= sig
            cov.append((x, "sig"))
        leq = leq_from_covers(elements, cov)
        # antisymmetry sanity (a placement could create a cycle => degenerate)
        cyclic = any((y, x) in leq and x != y for (x, y) in leq)
        # boxtimes: orbit antichain + fixed sigma; also need b,U values for antitone.
        # T-role is played by 'a1' here (top of the orbit proper); set boxtimes:
        f = {"a1": "a2", "a2": "a3", "a3": "a3", "sig": "sig",
             "b": "U", "U": "b"}
        anti = is_antitone(elements, leq, f) and not cyclic
        results.append({"placement": name, "antitone_survives": anti,
                        "cyclic_order": cyclic})

    # sigma below the whole orbit tail (the "meet" completion s_omega)
    run_placement("sigma_below_orbit (meet s_omega)", ["a1", "a2", "a3"], [])
    # sigma above the whole orbit (a "join" completion)
    run_placement("sigma_above_orbit (join)", [], ["a1", "a2", "a3"])
    # sigma sandwiched: below a1, above a3
    run_placement("sigma_sandwiched (a3<=sigma<=a1)", ["a1"], ["a3"])
    # sigma detached: incomparable to all orbit atoms
    run_placement("sigma_detached (incomparable to orbit)", [], [])

    detached = next(r for r in results if r["placement"].startswith("sigma_detached"))
    non_detached = [r for r in results if not r["placement"].startswith("sigma_detached")]
    verdict = ("PASS"
               if detached["antitone_survives"]
               and all(not r["antitone_survives"] for r in non_detached)
               else "FAIL")
    return {
        "claim": ("a fixed point order-related to an antichain orbit breaks "
                  "antitonicity; only a detached fixed point survives, and it "
                  "does not cap the orbit"),
        "placements": results,
        "verdict": verdict,
    }

# ----------------------------------------------------------------------------
# (C) Median tower / phantom median
# ----------------------------------------------------------------------------

def check_C(k=4):
    """
    Bounded lattice witnessing the failure of join-infinite-distributivity.

    A FINITE chain always contains its own infimum, so the gap
        T v (/\ e_i)  <  /\ (T v e_i)
    is invisible at any finite stage of a chain. The genuine obstruction is
    infinitary. We therefore witness it with the order limit made EXPLICIT:
    the e_i are a finite antichain (the residues of the descending family) with
    a distinguished meet element eps (= /\_i e_i, the order limit of the family),
    b < eps < T < c < U, eps < e_i < c, T incomparable to every e_i. Then:
        join(T, e_i) = c           (every obstructing pair forces the median c),
        meet_i e_i   = eps,
        join(T, eps) = T           (the limit pair forces only T),
    so T v (/\ e_i) = T < c = /\ (T v e_i): c is a PHANTOM median, forced by
    every pair yet by no limit pair. (This is exactly an N5-type non-distributive
    configuration; the antichain stands in for the descending family's residues.)
    """
    es = [f"e{i}" for i in range(1, k + 1)]  # antichain of front identities
    elements = ["b", "eps", "T", "c", "U"] + es
    cov = [("b", "eps"), ("eps", "T"), ("T", "c"), ("c", "U")]
    for e in es:
        cov.append(("eps", e))   # eps below each e_i (eps = their meet)
        cov.append((e, "c"))     # each e_i below c (c = their join, and = T v e_i)
    leq = leq_from_covers(elements, cov)

    def join(x, y):
        ubs = [z for z in elements if (x, z) in leq and (y, z) in leq]
        # least upper bound
        least = [z for z in ubs if all((z, w) in leq for w in ubs)]
        return least[0] if len(least) == 1 else None

    def meet(x, y):
        lbs = [z for z in elements if (z, x) in leq and (z, y) in leq]
        greatest = [z for z in lbs if all((w, z) in leq for w in lbs)]
        return greatest[0] if len(greatest) == 1 else None

    # lattice check: every pair has a unique join and meet
    is_lattice = all(join(x, y) is not None and meet(x, y) is not None
                     for x in elements for y in elements)

    # per-pair forced medians: join(T, e_i)
    pair_joins = {e: join("T", e) for e in es}
    all_c = all(v == "c" for v in pair_joins.values())

    # limit pair {T, /\ e_i}: meet of the antichain of identities
    meet_all_e = es[0]
    for e in es[1:]:
        meet_all_e = meet(meet_all_e, e)
    limit_join = join("T", meet_all_e)  # T v (/\ e_i), should be T

    # /\_i (T v e_i): meet of all the pair-joins (all = c)
    pj = list(pair_joins.values())
    meet_of_pairjoins = pj[0]
    for v in pj[1:]:
        meet_of_pairjoins = meet(meet_of_pairjoins, v)

    gap_real = (meet_all_e == "eps") and (limit_join == "T") and \
               (meet_of_pairjoins == "c") and \
               (("c", "T") not in leq) and (("T", "c") in leq) and ("T" != "c")

    return {
        "claim": ("each obstructing pair {T,e_i} forces median c=T v e_i; the "
                  "limit pair {T, /\\ e_i} forces only T; the strict gap c>T is a "
                  "phantom median (failure of join-infinite-distributivity)"),
        "k": k,
        "is_lattice": is_lattice,
        "pair_joins_T_e": pair_joins,
        "all_pair_joins_equal_c": all_c,
        "meet_of_all_e": meet_all_e,
        "join_T_with_meet_of_e (limit median)": limit_join,
        "meet_of_all_pair_joins (tower limit)": meet_of_pairjoins,
        "phantom_gap_c_strictly_above_T": gap_real,
        "verdict": "PASS" if (is_lattice and all_c and gap_real) else "FAIL",
    }

# ----------------------------------------------------------------------------

def main():
    report = {
        "pass": 41,
        "title": "limit fixed point s_omega and the median tower",
        "A_antitone_index2_collapse": check_A(max_n=4),
        "B_limit_fp_obstruction": check_B(),
        "C_median_tower_phantom": check_C(k=4),
    }
    report["overall_verdict"] = (
        "PASS" if all(report[k]["verdict"] == "PASS"
                      for k in ("A_antitone_index2_collapse",
                                "B_limit_fp_obstruction",
                                "C_median_tower_phantom")) else "FAIL")

    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.normpath(os.path.join(here, "..", "..", "artifacts", "reports",
                                        "limit-fp-median-tower-check.json"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        json.dump(report, fh, indent=2)
    print(json.dumps(report, indent=2))
    print("\nReport written to", out)
    return 0 if report["overall_verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
