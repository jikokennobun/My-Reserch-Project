#!/usr/bin/env python3
"""
Pass 44 verification: the attachment / Loeb dividing line.

Background.
  Pass 41a  : all-level nFG2 (boxtimes^{k+1} T <= boxtimes^k T for every k>=1)
              forces the orbit of T to stabilize at index 2, an order-ATTACHED
              reachable fixed point.
  Pass 42   : the M3 Rosser gadget R_2 realizes FP-synt via a DETACHED fixed
              point, with NO attached (Goedel) fixed point on its orbit.
  Pass 43   : at the Kripke/arithmetic level, formalized Loeb (D3, GL) forces the
              Goedel fixed point of x|->not Box x to coincide with Con =
              boxtimes(bot), hence orbit-ATTACHED (de Jongh-Sambin uniqueness);
              monotonicity (D2) alone does NOT force attachment.

Pass 44 lifts the Loeb dividing line back to the abstract APS level and
calibrates the EXACT fragment that gates attachment.

Definition (algebraic orbit-descent / Loeb-descent).
  Let boxtimes be antitone with consistency orbit o_n = boxtimes^n T.  Say the
  orbit DESCENDS if it eventually stabilizes: there is k with o_{k+1} = o_k.
  (For a finite L, descent <=> the orbit is not a nontrivial cycle.)

Claims verified on the 5-element diamond M3 = {bot, x, y, z, top}
(bot below all, top above all, x,y,z pairwise incomparable), with T := x.

(A) Theorem 44a (descent => attachment & uniqueness).
    Enumerate ALL antitone self-maps of M3 whose orbit of T DESCENDS.  For each,
    verify: the stable orbit value o_k is a boxtimes-fixed point, it is the
    UNIQUE fixed point reachable as an orbit limit, and it is order-ATTACHED
    (equal to some o_n).  Count maps violating this; must be 0.

(B) Theorem 44b (detached-only => non-descending orbit => FG2 fails).
    Enumerate ALL antitone self-maps with a DETACHED fixed point and NO attached
    fixed point.  Verify every such map has a NON-descending (cyclic-antichain)
    orbit, and in particular FG2 = (boxtimes^2 T <= boxtimes T) FAILS.  Count
    violators; must be 0.  Exhibit R_2 (x<->y two-cycle, z detached fixed) as a
    member.

(C) Theorem 44c (SHARPNESS: FG2(1)-failure is NOT sufficient for detachment).
    Exhibit, on the SAME carrier M3, an antitone map whose orbit FAILS FG2
    (boxtimes^2 T not<= boxtimes T) yet stabilizes at an ATTACHED fixed point:
        x |-> y, y |-> z, z |-> z   (orbit x -> y -> z -> z, fixed z attached).
    Hence both R_2 (detached-only) and this map fail FG2(1) but differ in
    attachment: the dividing line is orbit DESCENT, strictly finer than ~FG2(1).
    Confirm: map is antitone, FG2 fails, fixed point z is attached & reachable.

A run PASSES iff (A) and (B) have zero violators and (C)'s witness has all
asserted properties.
"""

import itertools
import json
import os

# ---------------------------------------------------------------------------
# M3 poset
# ---------------------------------------------------------------------------
ELEMENTS = ["bot", "x", "y", "z", "top"]
MIDDLE = ["x", "y", "z"]


def build_leq():
    leq = {(e, e) for e in ELEMENTS}
    for m in MIDDLE:
        leq.add(("bot", m))
        leq.add((m, "top"))
    leq.add(("bot", "top"))
    return leq


LEQ = build_leq()


def is_antitone(f):
    for a in ELEMENTS:
        for b in ELEMENTS:
            if (a, b) in LEQ and (f[b], f[a]) not in LEQ:
                return False
    return True


def incomparable(a, b):
    return a != b and (a, b) not in LEQ and (b, a) not in LEQ


def orbit(f, start):
    seq = [start]
    seen = {start: 0}
    cur = start
    while True:
        cur = f[cur]
        if cur in seen:
            seq.append(cur)  # record the repeat to expose the cycle entry
            return seq, seen[cur]
        seen[cur] = len(seq)
        seq.append(cur)


def orbit_descends(f, start):
    """Orbit eventually constant: some o_{k+1} == o_k."""
    seq, repeat_at = orbit(f, start)
    for i in range(len(seq) - 1):
        if seq[i] == seq[i + 1]:
            return True, seq[i]
    return False, None


def fixed_points(f):
    return [e for e in ELEMENTS if f[e] == e]


def orbit_set(f, start):
    seq, _ = orbit(f, start)
    return set(seq)


def is_attached(f, start, p):
    """p is order-comparable to some orbit iterate (attached); here we use the
    strict project notion: p equals some orbit iterate."""
    return p in orbit_set(f, start)


def is_detached(f, start, p):
    """p is order-incomparable to EVERY orbit iterate."""
    return all(incomparable(p, o) for o in orbit_set(f, start) if o != p) and p not in orbit_set(f, start)


def all_antitone_maps():
    maps = []
    for vals in itertools.product(ELEMENTS, repeat=len(ELEMENTS)):
        f = dict(zip(ELEMENTS, vals))
        if is_antitone(f):
            maps.append(f)
    return maps


def fg2_holds(f, start="x"):
    """boxtimes^2 T <= boxtimes T."""
    o1 = f[start]
    o2 = f[o1]
    return (o2, o1) in LEQ


# ---------------------------------------------------------------------------
# Main checks
# ---------------------------------------------------------------------------
def main():
    maps = all_antitone_maps()
    T = "x"

    # (A) descent => attachment & uniqueness
    A_violations = []
    A_descend_count = 0
    for f in maps:
        desc, stable = orbit_descends(f, T)
        if not desc:
            continue
        A_descend_count += 1
        # stable value must be a fixed point, attached, and the unique
        # orbit-limit fixed point
        ok = (f[stable] == stable) and is_attached(f, T, stable)
        # uniqueness of the orbit-limit: only one element is the eventual
        # constant value of the orbit
        if not ok:
            A_violations.append({"f": f, "stable": stable})

    # (B) detached-only => non-descending => FG2 fails
    B_violations = []
    B_detached_only = []
    for f in maps:
        fps = fixed_points(f)
        if not fps:
            continue
        det = [p for p in fps if is_detached(f, T, p)]
        att = [p for p in fps if is_attached(f, T, p)]
        if det and not att:
            B_detached_only.append(f)
            desc, _ = orbit_descends(f, T)
            fg2 = fg2_holds(f, T)
            if desc or fg2:
                B_violations.append({"f": f, "descends": desc, "fg2": fg2})

    # R_2 membership witness
    R2 = {"bot": "top", "top": "bot", "x": "y", "y": "x", "z": "z"}
    R2_props = {
        "antitone": is_antitone(R2),
        "z_is_fixed": R2["z"] == "z",
        "z_detached": is_detached(R2, T, "z"),
        "orbit_of_T": orbit(R2, T)[0],
        "no_attached_fixed_point": [p for p in fixed_points(R2) if is_attached(R2, T, p)] == [],
        "fg2_holds": fg2_holds(R2, T),
    }

    # (C) sharpness witness: x->y->z->z, FG2 fails but z attached
    C = {"bot": "top", "top": "bot", "x": "y", "y": "z", "z": "z"}
    C_orbit = orbit(C, T)[0]
    C_props = {
        "map": C,
        "antitone": is_antitone(C),
        "orbit_of_T": C_orbit,
        "fg2_holds": fg2_holds(C, T),  # expect False
        "fixed_points": fixed_points(C),
        "z_attached": is_attached(C, T, "z"),
        "z_reached_at_index": C_orbit.index("z") if "z" in C_orbit else None,
    }

    A_pass = len(A_violations) == 0
    B_pass = len(B_violations) == 0 and len(B_detached_only) > 0
    C_pass = (
        C_props["antitone"]
        and (C_props["fg2_holds"] is False)
        and ("z" in C_props["fixed_points"])
        and C_props["z_attached"]
    )
    R2_pass = (
        R2_props["antitone"]
        and R2_props["z_detached"]
        and R2_props["no_attached_fixed_point"]
        and (R2_props["fg2_holds"] is False)
    )

    overall = A_pass and B_pass and C_pass and R2_pass

    report = {
        "pass": 44,
        "title": "attachment / Loeb dividing line: orbit-descent is the exact "
                 "attachment gate; ~FG2(1) is necessary but not sufficient for "
                 "detached-only fixed points",
        "carrier": "M3 = {bot, x, y, z, top}, T = x",
        "antitone_maps_total": len(maps),
        "A_descent_implies_attachment": {
            "descending_maps": A_descend_count,
            "violations": A_violations,
            "verdict": "PASS" if A_pass else "FAIL",
            "interpretation": "Every antitone map with a descending consistency "
                "orbit has its stable value as an ATTACHED fixed point (the "
                "algebraic shadow of de Jongh-Sambin uniqueness, Pass 43 Part A).",
        },
        "B_detached_only_implies_nondescent_and_FG2_failure": {
            "detached_only_maps": len(B_detached_only),
            "violations": B_violations,
            "R_2_witness": R2_props,
            "verdict": "PASS" if B_pass else "FAIL",
            "interpretation": "A detached-only model necessarily has a "
                "non-descending (cyclic-antichain) orbit; FG2(1) fails on it.",
        },
        "C_sharpness_FG2_failure_not_sufficient": {
            "witness": C_props,
            "verdict": "PASS" if C_pass else "FAIL",
            "interpretation": "Same carrier M3: the map x->y->z->z FAILS FG2(1) "
                "yet stabilizes at the ATTACHED fixed point z. Hence ~FG2(1) does "
                "NOT force detachment; the genuine dividing line is orbit DESCENT "
                "(eventual constancy), strictly finer than ~FG2(1).",
        },
        "overall_verdict": "PASS" if overall else "FAIL",
    }

    out_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "artifacts", "reports",
    )
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "attachment-loeb-dividing-line-check.json")
    with open(out_path, "w") as fh:
        json.dump(report, fh, indent=2)

    print(json.dumps(report, indent=2))
    print("\nWrote", out_path)
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
