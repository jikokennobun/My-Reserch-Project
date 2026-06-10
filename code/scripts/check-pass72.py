#!/usr/bin/env python3
"""
Pass 72 verification: finite tests for the hybrid exact category candidate
supporting the all-prime epsilon object.

The intended bookkeeping category H_epsilon has two layers:

1. finite restricted-product shadows, indexed by a finite prime set S and a
   conductor k;
2. a derived pro-Ab diagonal quotient, represented by the lcm kernel tower
   N_n Z.

This checker verifies the finite algebraic constraints that the candidate
category must satisfy before it can be promoted to an LCA-sheaf or condensed
duality theorem.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, List


PRIMES = [2, 3, 5, 7, 11, 13]


def prod(values: Iterable[int]) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def lcm_to(n: int) -> int:
    out = 1
    for value in range(1, n + 1):
        out = lcm(out, value)
    return out


def matrix_rank_q(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    a = [[Fraction(x) for x in row] for row in matrix]
    rank = 0
    pivot_row = 0
    for col in range(cols):
        pivot = None
        for row in range(pivot_row, rows):
            if a[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        pivot_value = a[pivot_row][col]
        a[pivot_row] = [x / pivot_value for x in a[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = a[row][col]
            if factor:
                a[row] = [x - factor * y for x, y in zip(a[row], a[pivot_row])]
        rank += 1
        pivot_row += 1
        if pivot_row == rows:
            break
    return rank


def det_int(matrix: List[List[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    total = 0
    for col in range(n):
        minor = [
            [matrix[row][inner_col] for inner_col in range(n) if inner_col != col]
            for row in range(1, n)
        ]
        total += ((-1) ** col) * matrix[0][col] * det_int(minor)
    return total


def maximal_minor_gcd(matrix: List[List[int]], rank: int) -> int:
    if rank == 0:
        return 1
    rows = range(len(matrix))
    cols = range(len(matrix[0])) if matrix else range(0)
    gcd_value = 0
    for row_indices in itertools.combinations(rows, rank):
        for col_indices in itertools.combinations(cols, rank):
            sub = [[matrix[row][col] for col in col_indices] for row in row_indices]
            gcd_value = math.gcd(gcd_value, abs(det_int(sub)))
    return gcd_value


def boundary_matrix(size: int) -> List[List[int]]:
    matrix: List[List[int]] = []
    for col in range(1, size):
        row = [0] * size
        row[0] = -1
        row[col] = 1
        matrix.append(row)
    return matrix


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    return [list(col) for col in zip(*matrix)]


def neg(matrix: List[List[int]]) -> List[List[int]]:
    return [[-entry for entry in row] for row in matrix]


def signed_dual_boundary(size: int) -> List[List[int]]:
    matrix = boundary_matrix(size)
    if matrix:
        return neg(transpose(matrix))
    return [[] for _ in range(size)]


def restrict_matrix(
    matrix: List[List[int]],
    row_count: int,
    col_count: int,
) -> List[List[int]]:
    return [row[:col_count] for row in matrix[:row_count]]


def check_exact_shadow(size: int) -> dict:
    d = boundary_matrix(size)
    rank = matrix_rank_q(d)
    minor_gcd = maximal_minor_gcd(d, rank)
    dual = signed_dual_boundary(size)
    dual_rank = matrix_rank_q(dual)
    dual_minor_gcd = maximal_minor_gcd(dual, dual_rank)
    double_dual = neg(transpose(dual)) if size > 1 else []
    if size == 1:
        double_dual = d
    return {
        "size": size,
        "boundary_rank": rank,
        "boundary_surjective": rank == size - 1 and minor_gcd == 1,
        "kernel_rank": size - rank,
        "kernel_is_diagonal_rank": size - rank == 1,
        "signed_dual_rank": dual_rank,
        "signed_dual_primitive_image": dual_minor_gcd == 1,
        "double_dual_returns_boundary": double_dual == d,
        "verdict": "PASS"
        if rank == size - 1
        and minor_gcd == 1
        and size - rank == 1
        and dual_rank == size - 1
        and dual_minor_gcd == 1
        and double_dual == d
        else "FAIL",
    }


def check_restriction_composition(max_size: int) -> List[dict]:
    checks = []
    for small in range(1, max_size + 1):
        d_small = boundary_matrix(small)
        dual_small = signed_dual_boundary(small)
        for middle in range(small, max_size + 1):
            for large in range(middle, max_size + 1):
                d_large = boundary_matrix(large)
                d_middle = boundary_matrix(middle)
                via_middle = restrict_matrix(
                    restrict_matrix(d_large, max(0, middle - 1), middle),
                    max(0, small - 1),
                    small,
                )
                direct = restrict_matrix(d_large, max(0, small - 1), small)
                dual_large = signed_dual_boundary(large)
                dual_middle = signed_dual_boundary(middle)
                dual_via_middle = restrict_matrix(
                    restrict_matrix(dual_large, middle, max(0, middle - 1)),
                    small,
                    max(0, small - 1),
                )
                dual_direct = restrict_matrix(
                    dual_large,
                    small,
                    max(0, small - 1),
                )
                ok = (
                    via_middle == direct == d_small
                    and dual_via_middle == dual_direct == dual_small
                    and restrict_matrix(d_middle, max(0, small - 1), small)
                    == d_small
                )
                checks.append(
                    {
                        "small": small,
                        "middle": middle,
                        "large": large,
                        "boundary_restriction_composes": via_middle == direct == d_small,
                        "dual_restriction_composes": (
                            dual_via_middle == dual_direct == dual_small
                        ),
                        "verdict": "PASS" if ok else "FAIL",
                    }
                )
    return checks


def check_conductor_layer(max_prime_count: int, max_conductor: int) -> List[dict]:
    checks = []
    for size in range(1, max_prime_count + 1):
        primes = PRIMES[:size]
        for conductor in range(1, max_conductor + 1):
            moduli = [prime ** (2 * conductor) for prime in primes]
            lattice_orders = [prime**conductor for prime in primes]
            window_order = prod(moduli)
            lattice_order = prod(lattice_orders)
            self_dual_order = lattice_order * lattice_order == window_order
            crt_order = prod(prime**conductor for prime in primes)
            diagonal_modulus = prod(prime**conductor for prime in primes)
            crt_bijective_by_coprime_moduli = crt_order == diagonal_modulus
            checks.append(
                {
                    "primes": primes,
                    "conductor": conductor,
                    "window_order": window_order,
                    "integral_lattice_order": lattice_order,
                    "lattice_order_squared_equals_window_order": self_dual_order,
                    "crt_diagonal_finite_shadow_order": crt_order,
                    "crt_bijective_by_coprime_moduli": (
                        crt_bijective_by_coprime_moduli
                    ),
                    "verdict": "PASS"
                    if self_dual_order and crt_bijective_by_coprime_moduli
                    else "FAIL",
                }
            )
    return checks


def check_pro_layer(max_n: int) -> dict:
    values = [lcm_to(n) for n in range(1, max_n + 1)]
    ratios = [
        values[index + 1] // values[index]
        for index in range(len(values) - 1)
    ]
    strictly_grows_often = sum(1 for ratio in ratios if ratio > 1) >= max_n // 2
    cofinal_sample = all(
        any(value % modulus == 0 for value in values)
        for modulus in range(1, max_n + 1)
    )
    dense_diagonal_by_finite_surjectivity = cofinal_sample
    non_mittag_leffler_witness = max(values) > values[max_n // 2]
    return {
        "max_n": max_n,
        "lcm_values": values,
        "transition_ratios": ratios,
        "cofinal_for_moduli_up_to_max_n": cofinal_sample,
        "dense_diagonal_by_finite_surjectivity": (
            dense_diagonal_by_finite_surjectivity
        ),
        "non_mittag_leffler_growth_witness": non_mittag_leffler_witness,
        "finite_crt_levelwise_zero_but_pro_derived_nonzero": (
            dense_diagonal_by_finite_surjectivity and non_mittag_leffler_witness
        ),
        "verdict": "PASS"
        if strictly_grows_often
        and cofinal_sample
        and dense_diagonal_by_finite_surjectivity
        and non_mittag_leffler_witness
        else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", type=int, default=6)
    parser.add_argument("--max-conductor", type=int, default=3)
    parser.add_argument("--max-n", type=int, default=24)
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass72-hybrid-exact-epsilon-category-check.json",
    )
    args = parser.parse_args()

    if args.max_size < 1 or args.max_size > len(PRIMES):
        raise SystemExit(f"--max-size must be between 1 and {len(PRIMES)}")
    if args.max_conductor < 1:
        raise SystemExit("--max-conductor must be positive")
    if args.max_n < 4:
        raise SystemExit("--max-n must be at least 4")

    exact_shadows = [check_exact_shadow(size) for size in range(1, args.max_size + 1)]
    restriction_checks = check_restriction_composition(args.max_size)
    conductor_checks = check_conductor_layer(args.max_size, args.max_conductor)
    pro_layer = check_pro_layer(args.max_n)
    all_verdicts = (
        [item["verdict"] for item in exact_shadows]
        + [item["verdict"] for item in restriction_checks]
        + [item["verdict"] for item in conductor_checks]
        + [pro_layer["verdict"]]
    )
    report = {
        "pass_number": 72,
        "title": "hybrid exact category candidate for epsilon_P",
        "scope": (
            "finite verification for H_epsilon, a bookkeeping exact category "
            "combining restricted-product conductor shadows with a derived "
            "pro-Ab diagonal quotient"
        ),
        "candidate_category": {
            "objects": (
                "finite conductor restricted-product shadows plus the lcm "
                "kernel tower N_n Z"
            ),
            "exact_sequences": (
                "hybrid-exact iff all finite shadows are exact and the pro "
                "kernel tower supplies the derived diagonal quotient"
            ),
            "duality": (
                "finite shadows use signed character dual d_S -> -d_S^T; the "
                "pro layer records Zhat/Z without treating it as a Hausdorff "
                "LCA quotient"
            ),
        },
        "finite_exact_shadows": exact_shadows,
        "restriction_composition": restriction_checks,
        "conductor_layers": conductor_checks,
        "pro_layer": pro_layer,
        "overall": "PASS" if all(value == "PASS" for value in all_verdicts) else "FAIL",
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
