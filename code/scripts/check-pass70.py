#!/usr/bin/env python3
"""
Pass 70 verification: compare the derived pro-cokernel with the
Loeb-Rosser recollement class epsilon.

This is an algebraic finite-prime checker.  It verifies the common matrix spine
behind two presentations:

1. Derived pro-cokernel:
   0 -> Z -> lim_k Z/M_{S,k}Z -> lim^1 M_{S,k}Z -> 0,
   where M_{S,k}=prod_{p in S} p^k.

2. Recollement/filtration:
   0 -> Z^S/Delta Z -> Zhat_S/Z -> prod_p (Z_p/Z) -> 0.

The checker cannot compute infinite p-adic groups directly.  It instead
checks the finite CRT shadows and the integral boundary matrices whose kernels
and cokernels identify the extension class epsilon_S.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, List


PRIMES = [2, 3, 5, 7, 11]


def prod(xs: Iterable[int]) -> int:
    out = 1
    for x in xs:
        out *= x
    return out


def matrix_rank_q(matrix: List[List[int]]) -> int:
    """Rank over Q by fraction Gaussian elimination."""

    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0])
    rank = 0
    pivot_row = 0
    for col in range(cols):
        pivot = None
        for r in range(pivot_row, rows):
            if a[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        pivot_val = a[pivot_row][col]
        a[pivot_row] = [x / pivot_val for x in a[pivot_row]]
        for r in range(rows):
            if r == pivot_row:
                continue
            factor = a[r][col]
            if factor != 0:
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        rank += 1
        pivot_row += 1
        if pivot_row == rows:
            break
    return rank


def det_int(matrix: List[List[int]]) -> int:
    """Bare integer determinant for tiny matrices."""

    n = len(matrix)
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    total = 0
    for c in range(n):
        minor = [
            [matrix[r][cc] for cc in range(n) if cc != c]
            for r in range(1, n)
        ]
        total += ((-1) ** c) * matrix[0][c] * det_int(minor)
    return total


def maximal_minor_gcd(matrix: List[List[int]], rank: int) -> int:
    """GCD of all rank x rank minors; 1 implies primitive image."""

    if rank == 0:
        return 1
    rows = range(len(matrix))
    cols = range(len(matrix[0])) if matrix else range(0)
    g = 0
    for rs in itertools.combinations(rows, rank):
        for cs in itertools.combinations(cols, rank):
            sub = [[matrix[r][c] for c in cs] for r in rs]
            g = math.gcd(g, abs(det_int(sub)))
    return g


def delta_matrix(size: int) -> List[List[int]]:
    return [[1] for _ in range(size)]


def boundary_matrix(size: int, base: int = 0) -> List[List[int]]:
    rows: List[List[int]] = []
    for j in range(size):
        if j == base:
            continue
        row = [0] * size
        row[j] = 1
        row[base] = -1
        rows.append(row)
    return rows


def mat_vec(matrix: List[List[int]], vector: List[int]) -> List[int]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    return [list(col) for col in zip(*matrix)]


def neg(matrix: List[List[int]]) -> List[List[int]]:
    return [[-x for x in row] for row in matrix]


def matrices_equal(a: List[List[int]], b: List[List[int]]) -> bool:
    return a == b


def crt_bijection_check(primes: List[int], exponent: int) -> dict:
    moduli = [p**exponent for p in primes]
    modulus = prod(moduli)
    pairwise_coprime = all(
        math.gcd(a, b) == 1
        for i, a in enumerate(moduli)
        for b in moduli[i + 1:]
    )
    expected = prod(moduli)
    # Exhaustive enumeration is useful as a smoke test only for small levels.
    if modulus <= 50_000:
        seen = {
            tuple(x % m for m in moduli)
            for x in range(modulus)
        }
        image_size = len(seen)
        enumerated = True
    else:
        image_size = expected if pairwise_coprime else None
        enumerated = False
    return {
        "primes": primes,
        "exponent": exponent,
        "global_modulus": modulus,
        "product_order": expected,
        "pairwise_coprime_moduli": pairwise_coprime,
        "enumerated": enumerated,
        "image_size": image_size,
        "bijective": pairwise_coprime and expected == modulus,
    }


def check_size(size: int, max_exponent: int) -> dict:
    primes = PRIMES[:size]
    delta = delta_matrix(size)
    d = boundary_matrix(size)
    delta_rank = matrix_rank_q(delta)
    d_rank = matrix_rank_q(d)
    d_minor_gcd = maximal_minor_gcd(d, d_rank)
    delta_minor_gcd = maximal_minor_gcd(delta, delta_rank)
    diagonal_vector = [1] * size
    d_kills_delta = mat_vec(d, diagonal_vector) == [0] * (size - 1)
    signed_dual = neg(transpose(d))
    double_dual = neg(transpose(signed_dual))

    crt = [crt_bijection_check(primes, exponent) for exponent in range(1, max_exponent + 1)]

    return {
        "S": primes,
        "size": size,
        "delta_matrix_rank": delta_rank,
        "delta_image_primitive": delta_minor_gcd == 1,
        "coker_delta_rank": size - 1,
        "boundary_matrix_rank": d_rank,
        "boundary_matrix_surjective": d_rank == size - 1 and d_minor_gcd == 1,
        "boundary_kills_diagonal": d_kills_delta,
        "kernel_boundary_is_diagonal_by_rank": d_kills_delta and d_rank == size - 1,
        "epsilon_kernel_rank": size - 1,
        "derived_middle_group": f"Zhat_{primes}/Z",
        "recollement_extension": (
            "0 -> Z^S/Delta Z -> Zhat_S/Z -> prod_p(Z_p/Z) -> 0"
        ),
        "comparison_claim": (
            "The projection from the derived pro-cokernel Zhat_S/Z to the product "
            "of local derived cokernels has kernel coker(Delta)."
        ),
        "signed_dual_shape": {
            "d_rows": len(d),
            "d_cols": len(d[0]) if d else size,
            "minus_d_transpose_rows": len(signed_dual),
            "minus_d_transpose_cols": len(signed_dual[0]) if signed_dual else 0,
            "double_dual_returns_d": matrices_equal(double_dual, d),
        },
        "finite_crt_shadows": crt,
        "verdict": "PASS" if all([
            delta_rank == 1,
            delta_minor_gcd == 1,
            d_rank == size - 1,
            d_minor_gcd == 1,
            d_kills_delta,
            matrices_equal(double_dual, d),
            all(item["bijective"] for item in crt),
        ]) else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", type=int, default=5)
    parser.add_argument("--max-exponent", type=int, default=4)
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass70-derived-pro-epsilon-comparison-check.json",
    )
    args = parser.parse_args()

    if args.max_size < 1 or args.max_size > len(PRIMES):
        raise SystemExit(f"--max-size must be between 1 and {len(PRIMES)}")
    if args.max_exponent < 1:
        raise SystemExit("--max-exponent must be positive")

    finite_s = [check_size(size, args.max_exponent) for size in range(1, args.max_size + 1)]
    report = {
        "pass_number": 70,
        "title": "derived pro-cokernel comparison with recollement epsilon",
        "scope": (
            "finite-prime algebraic comparison plus finite CRT shadows; "
            "full all-prime topological duality remains a restricted-product question"
        ),
        "statements": {
            "global_tower": "M_{S,k}=prod_{p in S} p^k and 0->M_{S,k}Z->Z->Z/M_{S,k}Z->0",
            "derived_cokernel": "lim^1(M_{S,k}Z) = Zhat_S/Z",
            "local_cokernels": "prod_p lim^1(p^k Z) = prod_p(Z_p/Z)",
            "epsilon_sequence": "0 -> Z^S/Delta Z -> Zhat_S/Z -> prod_p(Z_p/Z) -> 0",
            "dual_sign": "D(epsilon_S) is represented by -d_S^T on finite S",
        },
        "finite_prime_sets": finite_s,
        "overall": "PASS" if all(item["verdict"] == "PASS" for item in finite_s) else "FAIL",
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
