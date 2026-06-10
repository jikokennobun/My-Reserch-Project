#!/usr/bin/env python3
"""
Pass 42 verification: the detached fixed point as the algebraic Rosser sentence.

Background (Pass 41, Theorem 41b). For an antitone boxtimes whose orbit
o_0 = T, o_1 = boxtimes T, ... is a boxtimes-ANTICHAIN, the only fixed point
boxtimes p = p that is compatible with antitonicity is order-INCOMPARABLE to
every orbit element (a *detached* fixed point); no below/above/sandwiched
placement survives. Pass 42 reads this proof-theoretically:

    orbit-attached fixed point   ~   Goedel sentence (limit of the iterated
                                     consistency tower boxtimes^n T = Con^(n));
    detached fixed point         ~   Rosser sentence (a genuine boxtimes-fixed
                                     point INDEPENDENT of the consistency orbit:
                                     incomparable to every Con^(n), i.e.
                                     unprovable, irrefutable, and not provably
                                     equivalent to any iterated consistency
                                     statement).

We verify three machine-confirmable claims.

(A) The Rosser gadget R_2.
    Carrier  L = {bot, o0, o1, p, top}  with the M3-diamond order:
        bot <= everything <= top ,  and  o0, o1, p pairwise INCOMPARABLE.
    Designated truth  T := o0.  Antitone map
        boxtimes:  bot |-> top,  top |-> bot,  o0 |-> o1,  o1 |-> o0,  p |-> p.
    Claims:
      - boxtimes is antitone;
      - p is a fixed point (boxtimes p = p) and is DETACHED (incomparable to
        every orbit iterate boxtimes^n T);
      - the orbit of T is the 2-cycle {o0, o1}, an antichain with NO fixed
        point inside it (no order-attached Goedel fixed point exists);
      - hence FP-synt (exists q. boxtimes q = q) holds, witnessed ONLY by the
        detached/Rosser point p.

(B) Reachability separation.
    p is NOT reachable from T: for every n, boxtimes^n T != p. The Goedel-style
    "fixed point as a limit of the consistency orbit" does not exist here, yet a
    primitive boxtimes-fixed point does. This realizes the long-open core
    separation  exists q (q = boxtimes q)  WITHOUT an orbit-attached
    (Goedel) fixed point.

(C) Exhaustive dichotomy guard on M3.
    Over the 5-element M3 diamond (bot, three pairwise-incomparable middle
    atoms x,y,z, top) enumerate ALL antitone self-maps. For each map whose
    orbit of T:=x is a genuine non-stabilizing antichain (contains an
    incomparable pair and no fixed point), verify that EVERY fixed point of the
    map is detached (incomparable to the whole orbit). Report the counts; the
    dichotomy is confirmed iff the count of "antichain-orbit maps with an
    orbit-ATTACHED fixed point" is zero.
"""

import itertools
import json
import os

# ---------------------------------------------------------------------------
# Poset helpers
# ---------------------------------------------------------------------------

def leq_from_covers(elements, covers):
    """Reflexive-transitive closure of a cover relation."""
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
    """a <= b  ==>  f(b) <= f(a)."""
    for a in elements:
        for b in elements:
            if (a, b) in leq and (f[b], f[a]) not in leq:
                return False
    return True


def incomparable(leq, a, b):
    return a != b and (a, b) not in leq and (b, a) not in leq


def orbit(f, start):
    """Iterate f from start until a value repeats; return the list of distinct
    iterates in visitation order (the eventually-periodic trajectory's support)."""
    seen = []
    x = start
    while x not in seen:
        seen.append(x)
        x = f[x]
    return seen


def fixed_points(elements, f):
    return [e for e in elements if f[e] == e]


# ---------------------------------------------------------------------------
# (A)+(B)  The Rosser gadget R_2
# ---------------------------------------------------------------------------

def check_R2():
    elements = ["bot", "o0", "o1", "p", "top"]
    middles = ["o0", "o1", "p"]
    covers = [("bot", m) for m in middles] + [(m, "top") for m in middles]
    leq = leq_from_covers(elements, covers)

    boxtimes = {"bot": "top", "top": "bot", "o0": "o1", "o1": "o0", "p": "p"}
    T = "o0"

    antitone = is_antitone(elements, leq, boxtimes)
    fps = fixed_points(elements, boxtimes)
    orb = orbit(boxtimes, T)                       # support of the T-trajectory

    # p detached: incomparable to every orbit element
    p_detached = all(incomparable(leq, "p", o) for o in orb)
    # orbit is an antichain (every distinct pair incomparable)
    orbit_antichain = all(
        incomparable(leq, a, b) for a in orb for b in orb if a != b
    )
    # no fixed point inside the orbit (no order-attached Goedel FP)
    orbit_has_fp = any(boxtimes[o] == o for o in orb)

    # reachability: is p ever an iterate of T?
    reach = [T]
    x = boxtimes[T]
    steps = 0
    while x not in reach and steps < 100:
        reach.append(x)
        x = boxtimes[x]
        steps += 1
    p_reachable = "p" in reach

    return {
        "carrier": elements,
        "order": "M3 diamond (o0,o1,p pairwise incomparable, bot<all<top)",
        "boxtimes": boxtimes,
        "T": T,
        "antitone": antitone,
        "fixed_points": fps,
        "p_is_fixed": boxtimes["p"] == "p",
        "T_orbit_support": orb,
        "orbit_is_antichain": orbit_antichain,
        "orbit_contains_fixed_point": orbit_has_fp,
        "p_detached_from_orbit": p_detached,
        "FP_synt_holds": len(fps) > 0,
        "FP_synt_witness_is_only_detached_p": fps == ["p"],
        "p_reachable_from_T": p_reachable,
        "reachable_iterates_of_T": reach,
        "verdict": "PASS" if (
            antitone and boxtimes["p"] == "p" and p_detached
            and orbit_antichain and not orbit_has_fp
            and fps == ["p"] and not p_reachable
        ) else "FAIL",
    }


# ---------------------------------------------------------------------------
# (C)  Exhaustive dichotomy guard on M3
# ---------------------------------------------------------------------------

def check_M3_dichotomy():
    elements = ["bot", "x", "y", "z", "top"]
    middles = ["x", "y", "z"]
    covers = [("bot", m) for m in middles] + [(m, "top") for m in middles]
    leq = leq_from_covers(elements, covers)
    T = "x"

    antitone_maps = 0
    maps_with_fp = 0
    antichain_orbit_maps = 0           # orbit of T is a genuine non-stab antichain
    antichain_orbit_with_fp = 0
    attached_fp_in_antichain_regime = 0
    sample_witness = None

    for image in itertools.product(elements, repeat=len(elements)):
        f = dict(zip(elements, image))
        if not is_antitone(elements, leq, f):
            continue
        antitone_maps += 1
        fps = fixed_points(elements, f)
        if fps:
            maps_with_fp += 1

        orb = orbit(f, T)
        orbit_antichain = all(
            incomparable(leq, a, b) for a in orb for b in orb if a != b
        ) and len(orb) >= 2
        orbit_has_fp = any(f[o] == o for o in orb)

        if orbit_antichain and not orbit_has_fp:
            antichain_orbit_maps += 1
            if fps:
                antichain_orbit_with_fp += 1
                # are all fixed points detached from the orbit?
                attached = [
                    e for e in fps
                    if any(not incomparable(leq, e, o) for o in orb)
                ]
                if attached:
                    attached_fp_in_antichain_regime += 1
                elif sample_witness is None:
                    sample_witness = {
                        "boxtimes": f, "T_orbit": orb,
                        "detached_fixed_points": fps,
                    }

    return {
        "carrier": elements,
        "order": "M3 diamond (x,y,z pairwise incomparable)",
        "antitone_maps_checked": antitone_maps,
        "antitone_maps_with_a_fixed_point": maps_with_fp,
        "maps_with_nonstabilizing_antichain_orbit_of_T": antichain_orbit_maps,
        "of_those_having_a_fixed_point": antichain_orbit_with_fp,
        "of_those_with_an_ORBIT_ATTACHED_fixed_point": attached_fp_in_antichain_regime,
        "claim": "in the antichain-orbit regime every fixed point is detached",
        "sample_detached_witness": sample_witness,
        "verdict": "PASS" if attached_fp_in_antichain_regime == 0 else "FAIL",
    }


def main():
    report = {
        "pass": 42,
        "title": "detached fixed point as the algebraic Rosser sentence",
        "A_rosser_gadget_R2": check_R2(),
        "C_M3_detached_dichotomy_guard": check_M3_dichotomy(),
    }
    report["overall_verdict"] = (
        "PASS"
        if report["A_rosser_gadget_R2"]["verdict"] == "PASS"
        and report["C_M3_detached_dichotomy_guard"]["verdict"] == "PASS"
        else "FAIL"
    )

    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.normpath(os.path.join(
        here, "..", "..", "artifacts", "reports",
        "detached-rosser-fixedpoint-check.json"))
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    print(json.dumps(report, indent=2))
    print("\nwrote", out)


if __name__ == "__main__":
    main()
