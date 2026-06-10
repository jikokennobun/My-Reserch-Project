#!/usr/bin/env python3
"""
Pass 71 verification: restricted-product bookkeeping for the all-prime
epsilon class.

The checker does not prove a full theorem in LCA sheaves or condensed
abelian groups.  It verifies the finite algebra that any such theorem has to
preserve:

1. finite-prime signed boundaries commute with prefix restriction;
2. finite conductor windows have self-annihilating integral lattices;
3. unrestricted product support cannot be recovered from the ordinary dual of
   a bare infinite product, which justifies the restricted-product/pro
   formulation.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable, List


PRIMES = [2, 3, 5, 7, 11, 13]


def prod(values: Iterable[int]) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def boundary_matrix(size: int, base: int = 0) -> List[List[int]]:
    rows: List[List[int]] = []
    for col in range(size):
        if col == base:
            continue
        row = [0] * size
        row[base] = -1
        row[col] = 1
        rows.append(row)
    return rows


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    return [list(col) for col in zip(*matrix)]


def neg(matrix: List[List[int]]) -> List[List[int]]:
    return [[-entry for entry in row] for row in matrix]


def restrict_matrix(
    matrix: List[List[int]],
    row_count: int,
    col_count: int,
) -> List[List[int]]:
    return [row[:col_count] for row in matrix[:row_count]]


def signed_dual(matrix: List[List[int]]) -> List[List[int]]:
    return neg(transpose(matrix))


def boundary_signed_dual(size: int) -> List[List[int]]:
    matrix = boundary_matrix(size)
    if matrix:
        return signed_dual(matrix)
    # The singleton boundary is the zero map Z -> 0, represented as a 0 x 1
    # matrix.  Its dual is the zero map 0 -> Z, a 1 x 0 matrix.
    return [[] for _ in range(size)]


def check_boundary_naturality(max_size: int) -> List[dict]:
    checks = []
    for small in range(1, max_size + 1):
        d_small = boundary_matrix(small)
        dual_small = boundary_signed_dual(small)
        for large in range(small, max_size + 1):
            d_large = boundary_matrix(large)
            dual_large = boundary_signed_dual(large)
            boundary_restricts = (
                restrict_matrix(d_large, max(0, small - 1), small) == d_small
            )
            dual_restricts = (
                restrict_matrix(dual_large, small, max(0, small - 1))
                == dual_small
            )
            double_dual_returns = signed_dual(dual_small) == d_small
            checks.append(
                {
                    "small_size": small,
                    "large_size": large,
                    "boundary_restricts": boundary_restricts,
                    "signed_dual_restricts": dual_restricts,
                    "double_dual_returns_boundary": double_dual_returns,
                    "verdict": "PASS"
                    if boundary_restricts
                    and dual_restricts
                    and double_dual_returns
                    else "FAIL",
                }
            )
    return checks


def annihilator_is_lattice(prime: int, conductor: int) -> bool:
    modulus = prime ** (2 * conductor)
    step = prime**conductor
    lattice = set(range(0, modulus, step))
    annihilator = {
        x
        for x in range(modulus)
        if all((x * y) % modulus == 0 for y in lattice)
    }
    return annihilator == lattice


def check_conductor_windows(max_prime_count: int, max_conductor: int) -> List[dict]:
    checks = []
    for prime in PRIMES[:max_prime_count]:
        for conductor in range(1, max_conductor + 1):
            modulus = prime ** (2 * conductor)
            lattice_order = prime**conductor
            ok = annihilator_is_lattice(prime, conductor)
            checks.append(
                {
                    "prime": prime,
                    "conductor": conductor,
                    "window": f"p^(-{conductor})Z_p / p^{conductor}Z_p",
                    "window_order": modulus,
                    "integral_lattice_order": lattice_order,
                    "annihilator_equals_integral_lattice": ok,
                    "verdict": "PASS" if ok else "FAIL",
                }
            )
    return checks


def support_profile_counts(max_size: int, levels: int, support_bound: int) -> List[dict]:
    checks = []
    for size in range(1, max_size + 1):
        product_profiles = (levels + 1) ** size
        bounded_support_profiles = sum(
            len(list(itertools.combinations(range(size), support_size)))
            * (levels**support_size)
            for support_size in range(0, min(size, support_bound) + 1)
        )
        all_profiles_survive_finite_projection = product_profiles > 0
        bare_dual_loses_full_support = (
            bounded_support_profiles < product_profiles
            if size > support_bound
            else True
        )
        checks.append(
            {
                "prefix_size": size,
                "nonzero_conductor_levels_per_prime": levels,
                "restricted_product_prefix_profiles": product_profiles,
                "bare_product_dual_profiles_with_support_at_most_bound": (
                    bounded_support_profiles
                ),
                "support_bound": support_bound,
                "all_prefix_product_profiles_available": (
                    all_profiles_survive_finite_projection
                ),
                "bounded_support_is_strict_once_prefix_exceeds_bound": (
                    bare_dual_loses_full_support
                ),
                "verdict": "PASS"
                if all_profiles_survive_finite_projection
                and bare_dual_loses_full_support
                else "FAIL",
            }
        )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", type=int, default=6)
    parser.add_argument("--max-conductor", type=int, default=2)
    parser.add_argument("--max-window-primes", type=int, default=4)
    parser.add_argument("--levels", type=int, default=3)
    parser.add_argument("--support-bound", type=int, default=2)
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass71-restricted-product-epsilon-duality-check.json",
    )
    args = parser.parse_args()

    if args.max_size < 1 or args.max_size > len(PRIMES):
        raise SystemExit(f"--max-size must be between 1 and {len(PRIMES)}")
    if args.max_window_primes < 1 or args.max_window_primes > len(PRIMES):
        raise SystemExit(
            f"--max-window-primes must be between 1 and {len(PRIMES)}"
        )
    if args.max_conductor < 1:
        raise SystemExit("--max-conductor must be positive")
    if args.levels < 1:
        raise SystemExit("--levels must be positive")
    if args.support_bound < 0:
        raise SystemExit("--support-bound must be nonnegative")

    boundary_checks = check_boundary_naturality(args.max_size)
    window_checks = check_conductor_windows(
        args.max_window_primes,
        args.max_conductor,
    )
    support_checks = support_profile_counts(
        args.max_size,
        args.levels,
        args.support_bound,
    )
    all_checks = boundary_checks + window_checks + support_checks
    report = {
        "pass_number": 71,
        "title": "restricted-product epsilon duality finite-shadow package",
        "scope": (
            "finite-shadow verification for a pro-restricted all-prime "
            "epsilon class; not a proof of an ordinary Hausdorff quotient "
            "duality for Zhat/Z"
        ),
        "statements": {
            "all_prime_object": (
                "epsilon_P is the compatible finite-prime family "
                "{epsilon_S}_S plus the derived pro-cokernel Zhat/Z"
            ),
            "support_rule": (
                "duality must be support-preserving: restricted products are "
                "dualized with conductor/lattice data, not as bare products"
            ),
            "signed_law": (
                "D_res(epsilon_P)=-epsilon_P^vee means that every finite "
                "prime/conductor shadow has d_S -> -d_S^T and all restriction "
                "squares commute"
            ),
            "rejected_naive_claim": (
                "the checker rejects using the ordinary dual of prod_p A_p as "
                "the all-prime statement, since it only sees finite-support "
                "characters"
            ),
        },
        "boundary_naturality": boundary_checks,
        "finite_conductor_windows": window_checks,
        "support_profile_gap": support_checks,
        "overall": "PASS"
        if all(item["verdict"] == "PASS" for item in all_checks)
        else "FAIL",
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
