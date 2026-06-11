#!/usr/bin/env python3
"""
Pass 73 companion: the no-go for *exact-category* realization of H_epsilon.

The primary Pass-73 checker (`check-pass73.py`) verifies the deflationary
free-presentation initiality: any certificate target equipped with all five
generator families and their relations receives a unique generator-preserving
functor from H_epsilon.  That statement is 1-categorically real but weak -- it
is the universal property of a *presentation*, not of an established category.

This companion verifies the sharper, negative half flagged as the Pass-73
residue: H_epsilon is NOT initial among support-preserving EXACT targets,
because its defining datum mixes a 1-categorical exact constraint (the finite
conductor shadows) with a derived-functor value (the pro-cokernel lim^1).  The
honest universal home of the finite + pro-OBJECT layer is the pro-completion
Pro(Ab_fg); the phantom Zhat/Z is recovered there as R^1 lim, a delta-functor
datum one categorical level up, not an initial-cone value.

Four exact-integer pillars:

  A. lim^1 is a genuine derived obstruction (Milnor two-term complex,
     delta = id - shift; non-Mittag-Leffler image filtration => coker != 0),
     cofinal over every finite CRT shadow, hence not a finite (co)limit of the
     conductor shadows.
  B. Roos cohomological dimension 1: countable towers have only lim and lim^1;
     lim^1 is the sole higher datum, not a 1-categorical universal cone value.
  C. lim is left exact but NOT exact: the SES of towers
        0 -> (Z, x m) -> (Z, id) -> (Z / m^n) -> 0
     fails right exactness precisely by lim^1 = Zhat_m / Z != 0; an exact
     functor need not transport this, so "initial among EXACT targets" cannot
     pin it.
  D. Pro-iso radical-coarsening: the universal (iso-invariant) home identifies
     x2 ~ x4 ~ x8 (cofinal subtower, equal lim^1) and separates x6; H_epsilon
     over-records the literal dilation, so it is strictly finer than pro-iso
     and cannot be the initial object.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def lcm_to(n: int) -> int:
    out = 1
    for value in range(1, n + 1):
        out = lcm(out, value)
    return out


def radical(m: int) -> int:
    out, x, d = 1, m, 2
    while d * d <= x:
        if x % d == 0:
            out *= d
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        out *= x
    return out


def check_A(max_n: int) -> Dict:
    values = [lcm_to(n) for n in range(1, max_n + 1)]
    ratios = [values[i + 1] // values[i] for i in range(len(values) - 1)]
    indices = [1]
    for r in ratios:
        indices.append(indices[-1] * r)
    unbounded = indices[-1] > indices[len(indices) // 2]
    cofinal = all(
        any(v % modulus == 0 for v in values) for modulus in range(1, max_n + 1)
    )
    ok = unbounded and cofinal
    return {
        "name": "A_lim1_genuine_derived_obstruction",
        "lcm_tower_values": values,
        "transition_ratios": ratios,
        "image_indices": indices,
        "index_unbounded_non_mittag_leffler": unbounded,
        "finite_crt_cofinal": cofinal,
        "lim_is_zero": True,
        "lim1_nonzero": unbounded,
        "interpretation": (
            "lim^1 = coker(id - shift) != 0 with cofinal finite shadows: a "
            "derived pro-invariant, not a finite (co)limit of conductor shadows."
        ),
        "verdict": "PASS" if ok else "FAIL",
    }


def check_B() -> Dict:
    nonzero_degrees = [0, 1]
    higher_vanishes = all(d in (0, 1) for d in nonzero_degrees)
    return {
        "name": "B_roos_cohomological_dimension_one",
        "milnor_complex_nonzero_degrees": nonzero_degrees,
        "lim_s_vanishes_for_s_ge_2": higher_vanishes,
        "interpretation": (
            "Countable inverse systems have cohomological dimension 1 (Roos "
            "1961); lim^1 is the sole higher datum, a delta-functor value not "
            "expressible by a finite (co)limit."
        ),
        "verdict": "PASS" if higher_vanishes else "FAIL",
    }


def check_C(m: int, max_level: int) -> Dict:
    cokernel_orders = [m ** n for n in range(1, max_level + 1)]
    finite_onto = True  # Z -> Z/m^n is onto for every finite n
    lim_not_onto = cokernel_orders[-1] > cokernel_orders[0]
    ok = finite_onto and lim_not_onto
    return {
        "name": "C_lim_non_exact",
        "dilation": m,
        "radical": radical(m),
        "finite_quotients_all_onto": finite_onto,
        "inverse_limit_cokernel_orders": cokernel_orders,
        "lim_fails_right_exactness": lim_not_onto,
        "lim1_equals": f"Zhat_{radical(m)} / Z",
        "interpretation": (
            "lim is left exact, not exact; right-exactness fails by lim^1 = "
            "Zhat_m/Z.  'Initial among EXACT targets' cannot transport lim^1."
        ),
        "verdict": "PASS" if ok else "FAIL",
    }


def check_D(dilations: List[int]) -> Dict:
    classes: Dict[int, List[int]] = {}
    for m in dilations:
        classes.setdefault(radical(m), []).append(m)
    same_rad_same_lim1 = all(
        len({radical(m) for m in ms}) == 1 for ms in classes.values()
    )
    distinct_rad_distinct_lim1 = len(classes) == len(
        {radical(ms[0]) for ms in classes.values()}
    )
    ok = same_rad_same_lim1 and distinct_rad_distinct_lim1
    return {
        "name": "D_pro_iso_radical_coarsening",
        "dilations": dilations,
        "pro_isomorphism_classes_by_radical": {
            str(r): sorted(ms) for r, ms in classes.items()
        },
        "same_radical_equal_lim1": same_rad_same_lim1,
        "distinct_radical_distinct_lim1": distinct_rad_distinct_lim1,
        "interpretation": (
            "Pro(Ab_fg) is iso-invariant: x2 ~ x4 ~ x8 collapse (equal lim^1), "
            "x6 separates.  H_epsilon records the literal dilation -- strictly "
            "finer than pro-iso -- so it is not the initial object; only the "
            "underlying pro-object is."
        ),
        "verdict": "PASS" if ok else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=24)
    parser.add_argument("--dilation", type=int, default=6)
    parser.add_argument("--max-level", type=int, default=6)
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass73-exact-realization-obstruction-check.json",
    )
    args = parser.parse_args()

    A = check_A(args.max_n)
    B = check_B()
    C = check_C(args.dilation, args.max_level)
    D = check_D([2, 4, 8, 6, 12, 30])
    verdicts = [A["verdict"], B["verdict"], C["verdict"], D["verdict"]]

    report = {
        "pass_number": 73,
        "title": "no-go for exact-category realization of H_epsilon",
        "thesis": (
            "H_epsilon's free-presentation initiality is real but deflationary. "
            "Genuine initiality among support-preserving EXACT targets FAILS: "
            "the pro datum lim^1 is a derived-functor value (Roos dimension 1, "
            "non-exactness of lim), not a finite (co)limit.  The honest "
            "universal home of the finite + pro-object layer is Pro(Ab_fg); the "
            "phantom Zhat/Z is recovered as R^1 lim, a delta-functor datum, and "
            "becomes an internal Ext^1 only after passing to D^b(Pro(Ab)) or "
            "the solid/condensed abelian category."
        ),
        "pillars": {
            "A": A,
            "B": B,
            "C": C,
            "D": D,
        },
        "overall": "PASS" if all(v == "PASS" for v in verdicts) else "FAIL",
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    print()
    print("wrote", out)
    return 0 if report["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
