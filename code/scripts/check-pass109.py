#!/usr/bin/env python3
"""Finite checks for Pass 109: barycentric transition denominators.

For an inclusion of finite supports S subset T with |S| = n and |T| = m,
compare the zero-extended S-barycenter with the T-barycenter:

    tau_{S,T} = e_{S,T}(1/n * 1_S) - 1/m * 1_T.

The transition lies in ker(Sigma_T) tensor Q and has exact denominator
lcm(n, m).  Clearing this denominator gives a primitive integral zero-sum
vector on T.  These rational transitions satisfy the expected coboundary
identity on chains, while finite CRT shadows remain ordinary isomorphism
checks; the denominator records which conductor clears the rational
normalization rather than a new finite CRT cohomology class.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path


PAIRS = [(2, 3), (2, 4), (3, 5), (4, 6), (4, 8), (5, 8), (6, 9), (6, 10)]
CHAINS = [(2, 3, 5), (2, 4, 8), (3, 6, 10), (4, 6, 9)]


@dataclass
class TransitionRow:
    source_size: int
    target_size: int
    gcd_size: int
    transition: tuple[str, ...]
    transition_sum: str
    transition_in_kernel: bool
    exact_denominator: int
    expected_denominator: int
    denominator_formula_ok: bool
    conductor_clearance_rule_ok: bool
    cleared_transition: tuple[int, ...]
    expected_cleared_on_source: int
    expected_cleared_off_source: int
    cleared_integral_zero_sum: bool
    cleared_transition_primitive: bool


@dataclass
class ChainRow:
    source_size: int
    middle_size: int
    target_size: int
    rational_coboundary_identity_ok: bool
    endpoint_denominator: int
    common_conductor: int
    common_conductor_clears_all_terms: bool
    integral_identity_after_common_clearance_ok: bool


@dataclass
class CtrRow:
    conductor: int
    prime_power_factors: tuple[int, ...]
    crt_map_is_bijection: bool
    signed_crt_map_is_bijection: bool


@dataclass
class VerdictRow:
    transition_class: str
    conductor_comparison: str
    normalized_use: str
    deferred_review: str
    next_task: str


def frac_tuple(values: tuple[Fraction, ...]) -> tuple[str, ...]:
    return tuple(str(value) for value in values)


def denominator_of_tuple(values: tuple[Fraction, ...]) -> int:
    den = 1
    for value in values:
        den = lcm(den, value.denominator)
    return den


def transition(n: int, m: int) -> tuple[Fraction, ...]:
    return tuple(Fraction(1, n) - Fraction(1, m) for _ in range(n)) + tuple(
        -Fraction(1, m) for _ in range(m - n)
    )


def extend(values: tuple[Fraction, ...], length: int) -> tuple[Fraction, ...]:
    return values + tuple(Fraction(0) for _ in range(length - len(values)))


def integer_gcd(values: tuple[int, ...]) -> int:
    current = 0
    for value in values:
        current = gcd(current, abs(value))
    return current


def transition_rows() -> list[TransitionRow]:
    rows: list[TransitionRow] = []
    for n, m in PAIRS:
        g = gcd(n, m)
        tau = transition(n, m)
        den = denominator_of_tuple(tau)
        expected_den = lcm(n, m)
        cleared = tuple(int(expected_den * value) for value in tau)
        expected_on_source = (m - n) // g
        expected_off_source = -n // g
        conductor_checks = [
            (N * value).denominator == 1
            for N in range(1, 2 * expected_den + 1)
            for value in tau
        ]
        conductor_rule = all(
            (all((N * value).denominator == 1 for value in tau))
            == (N % expected_den == 0)
            for N in range(1, 2 * expected_den + 1)
        )
        rows.append(
            TransitionRow(
                source_size=n,
                target_size=m,
                gcd_size=g,
                transition=frac_tuple(tau),
                transition_sum=str(sum(tau)),
                transition_in_kernel=sum(tau) == 0,
                exact_denominator=den,
                expected_denominator=expected_den,
                denominator_formula_ok=den == expected_den,
                conductor_clearance_rule_ok=conductor_rule and any(conductor_checks),
                cleared_transition=cleared,
                expected_cleared_on_source=expected_on_source,
                expected_cleared_off_source=expected_off_source,
                cleared_integral_zero_sum=sum(cleared) == 0,
                cleared_transition_primitive=integer_gcd(cleared) == 1,
            )
        )
    return rows


def chain_rows() -> list[ChainRow]:
    rows: list[ChainRow] = []
    for n, mid, m in CHAINS:
        tau_n_mid = transition(n, mid)
        tau_mid_m = transition(mid, m)
        tau_n_m = transition(n, m)
        left = tuple(
            a + b
            for a, b in zip(
                extend(tau_n_mid, m),
                tau_mid_m,
                strict=True,
            )
        )
        common = lcm(denominator_of_tuple(tau_n_mid), denominator_of_tuple(tau_mid_m))
        right_common = tuple(int(common * value) for value in tau_n_m)
        left_common = tuple(int(common * value) for value in left)
        rows.append(
            ChainRow(
                source_size=n,
                middle_size=mid,
                target_size=m,
                rational_coboundary_identity_ok=left == tau_n_m,
                endpoint_denominator=denominator_of_tuple(tau_n_m),
                common_conductor=common,
                common_conductor_clears_all_terms=all(
                    (common * value).denominator == 1
                    for value in extend(tau_n_mid, m) + tau_mid_m + tau_n_m
                ),
                integral_identity_after_common_clearance_ok=left_common == right_common,
            )
        )
    return rows


def prime_power_factors(n: int) -> tuple[int, ...]:
    factors: list[int] = []
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            power = 1
            while remaining % p == 0:
                remaining //= p
                power *= p
            factors.append(power)
        p += 1
    if remaining > 1:
        factors.append(remaining)
    return tuple(factors)


def crt_is_bijection(n: int, sign: int = 1) -> bool:
    factors = prime_power_factors(n)
    seen = {
        tuple((sign * residue) % factor for factor in factors)
        for residue in range(n)
    }
    return len(seen) == n


def crt_rows() -> list[CtrRow]:
    conductors = sorted({lcm(n, m) for n, m in PAIRS})
    return [
        CtrRow(
            conductor=N,
            prime_power_factors=prime_power_factors(N),
            crt_map_is_bijection=crt_is_bijection(N, sign=1),
            signed_crt_map_is_bijection=crt_is_bijection(N, sign=-1),
        )
        for N in conductors
    ]


def verdict_row() -> VerdictRow:
    return VerdictRow(
        transition_class=(
            "tau_{S,T}=e_{S,T}s_bar,S-s_bar,T is a rational K_T-valued "
            "coboundary transition with exact denominator lcm(|S|,|T|)."
        ),
        conductor_comparison=(
            "A finite conductor N clears tau_{S,T} exactly when "
            "lcm(|S|,|T|) divides N; CRT shadows remain bijective and "
            "ordinary-acyclic after this clearance."
        ),
        normalized_use=(
            "Clearing the minimal denominator gives a primitive integral "
            "zero-sum vector on T, so the rational barycentric transition is "
            "a useful normalized comparison even without an integral symmetric section."
        ),
        deferred_review=(
            "The newest Claude Code review concerns MacNeille reflection "
            "checker defects; it is deferred because this pass follows the "
            "active support-transition line."
        ),
        next_task=(
            "Study the primitive conductor-cleared transition vectors along "
            "support chains and decide whether their rescaled cocycle law "
            "defines useful oriented-support edge data."
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass109-barycentric-transition-denominator-check.json",
    )
    args = parser.parse_args()

    transitions = transition_rows()
    chains = chain_rows()
    crt = crt_rows()
    verdict = verdict_row()

    checks = {
        "transition_kernel_ok": all(row.transition_in_kernel for row in transitions),
        "exact_denominator_lcm_ok": all(
            row.denominator_formula_ok and row.exact_denominator == row.expected_denominator
            for row in transitions
        ),
        "conductor_clearance_rule_ok": all(
            row.conductor_clearance_rule_ok for row in transitions
        ),
        "cleared_transition_primitive_ok": all(
            row.cleared_integral_zero_sum and row.cleared_transition_primitive
            for row in transitions
        ),
        "chain_coboundary_ok": all(
            row.rational_coboundary_identity_ok
            and row.common_conductor_clears_all_terms
            and row.integral_identity_after_common_clearance_ok
            for row in chains
        ),
        "crt_bijection_unchanged_ok": all(
            row.crt_map_is_bijection and row.signed_crt_map_is_bijection
            for row in crt
        ),
    }

    report = {
        "pass": 109,
        "title": "Barycentric transition denominators under support inclusions",
        "A_transition_formula": {
            "statement": (
                "For |S|=n<|T|=m, tau_{S,T} has entries "
                "(m-n)/(nm) on S and -1/m on T\\S."
            ),
            "rows": [asdict(row) for row in transitions],
        },
        "B_chain_coboundary": {
            "statement": (
                "The rational transitions satisfy "
                "e_{T,U}tau_{S,T}+tau_{T,U}=tau_{S,U}; after any common "
                "clearing conductor the integral identity remains true."
            ),
            "rows": [asdict(row) for row in chains],
        },
        "C_finite_conductor_crt": {
            "statement": (
                "The minimal conductor clearing tau_{S,T} is lcm(|S|,|T|); "
                "ordinary and signed CRT maps are still bijections at these "
                "finite conductors."
            ),
            "rows": [asdict(row) for row in crt],
        },
        "D_verdict": {
            "statement": (
                "Barycentric transitions are normalized rational support "
                "comparison data, not a new finite CRT cohomology class."
            ),
            "row": asdict(verdict),
        },
        "checks": checks,
        "overall": "PASS" if all(checks.values()) else "FAIL",
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"wrote {output_path}")
    print(f"overall {report['overall']}")


if __name__ == "__main__":
    main()
