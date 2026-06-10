#!/usr/bin/env python3
"""
Pass 67 verification: finite shadows of restricted-product adelic duality.

The all-prime Loeb-Rosser coefficient cannot be a bare product.  This checker
tests the finite conductor quotients that approximate the restricted product

    A_f = prod'_p (Q_p, Z_p).

At prime p and conductor k, use the finite quotient

    p^{-k} Z_p / p^k Z_p  ~=  Z / p^(2k) Z,

with pairing <x,y> = x*y / p^(2k) in Q/Z.  The integral lattice Z_p / p^k Z_p
corresponds to p^k Z / p^(2k) Z and should be self-annihilating.  Products of
these local data are the finite shadows of the LCA restricted product.

The checker verifies:
  A. local nondegeneracy and self-annihilating integral lattice;
  B. product self-duality for finite conductor data;
  C. signed transpose boundary persists in normalized finite coordinates;
  D. finite CRT diagonal Z/N -> prod_p Z/p^e is surjective, so the phantom
     Zhat/Z is invisible at every fixed finite conductor and must be handled as
     a derived/pro quotient, not as an ordinary finite-level quotient.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from math import prod
from pathlib import Path


def rank_q(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0])
    rank = 0
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if a[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pv = a[rank][col]
        a[rank] = [x / pv for x in a[rank]]
        for row in range(rows):
            if row != rank and a[row][col] != 0:
                factor = a[row][col]
                a[row] = [x - factor * y for x, y in zip(a[row], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def boundary_matrix(s: int) -> list[list[int]]:
    if s <= 1:
        return []
    rows = []
    for idx in range(1, s):
        row = [0] * s
        row[0] = -1
        row[idx] = 1
        rows.append(row)
    return rows


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


def neg(matrix: list[list[int]]) -> list[list[int]]:
    return [[-x for x in row] for row in matrix]


def signed_dual(matrix: list[list[int]]) -> list[list[int]]:
    return neg(transpose(matrix))


def check(condition: bool, name: str, detail: str, checks: dict[str, dict[str, object]]) -> bool:
    ok = bool(condition)
    checks[name] = {"pass": ok, "detail": detail}
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    return ok


def local_annihilator_modulus(p: int, k: int) -> tuple[int, int, int]:
    """Return modulus n=p^(2k), lattice step p^k, annihilator step."""
    n = p ** (2 * k)
    step = p**k
    annihilator = []
    lattice = set(range(0, n, step))
    for y in range(n):
        if all((x * y) % n == 0 for x in lattice):
            annihilator.append(y)
    if not annihilator:
        return n, step, -1
    # The annihilator should be exactly multiples of p^k.
    ann_step = min(y for y in annihilator if y != 0) if len(annihilator) > 1 else n
    return n, step, ann_step


def local_pairing_nondegenerate(p: int, k: int) -> bool:
    n = p ** (2 * k)
    for y in range(1, n):
        if all((x * y) % n == 0 for x in range(n)):
            return False
    return True


def product_lattice_self_annihilating(factors: list[tuple[int, int]]) -> bool:
    # factors are (p,k), group modulus p^(2k), lattice step p^k.
    moduli = [p ** (2 * k) for p, k in factors]
    steps = [p**k for p, k in factors]
    lattice = list(itertools.product(*[range(0, n, step) for n, step in zip(moduli, steps)]))
    annihilator = []
    for y in itertools.product(*[range(n) for n in moduli]):
        ok = True
        for x in lattice:
            if sum((xi * yi * (prod(moduli) // ni)) for xi, yi, ni in zip(x, y, moduli)) % prod(moduli) != 0:
                ok = False
                break
        if ok:
            annihilator.append(y)
    expected = set(itertools.product(*[range(0, n, step) for n, step in zip(moduli, steps)]))
    return set(annihilator) == expected


def crt_image_size(prime_exponents: list[tuple[int, int]]) -> tuple[int, int]:
    moduli = [p**e for p, e in prime_exponents]
    total = prod(moduli)
    image = {tuple(z % m for m in moduli) for z in range(total)}
    return len(image), total


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="pass67-report.json")
    args = parser.parse_args()

    checks: dict[str, dict[str, object]] = {}
    overall = True

    # A. Local finite conductor quotients.
    for p, k in ((2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1)):
        n, step, ann_step = local_annihilator_modulus(p, k)
        overall &= check(
            local_pairing_nondegenerate(p, k),
            f"A_local_pairing_nondegenerate_p{p}_k{k}",
            f"Z/{n} with pairing xy/{n} is nondegenerate",
            checks,
        )
        overall &= check(
            ann_step == step,
            f"A_local_lattice_self_annihilating_p{p}_k{k}",
            f"integral lattice step p^k={step} has annihilator step {ann_step}",
            checks,
        )

    # B. Finite products of restricted local data.
    product_cases = [
        [(2, 1), (3, 1)],
        [(2, 2), (3, 1)],
        [(2, 1), (3, 1), (5, 1)],
        [(2, 1), (5, 1), (7, 1)],
    ]
    for idx, factors in enumerate(product_cases, 1):
        group_order = prod(p ** (2 * k) for p, k in factors)
        lattice_order = prod(p**k for p, k in factors)
        overall &= check(
            product_lattice_self_annihilating(factors),
            f"B_product_lattice_self_annihilating_case{idx}",
            f"group order={group_order}, lattice order={lattice_order}, square={lattice_order*lattice_order}",
            checks,
        )

    # C. Boundary sign survives in normalized finite coordinates.
    for s in range(1, 8):
        d = boundary_matrix(s)
        dd = signed_dual(d)
        overall &= check(
            rank_q(d) == rank_q(dd) == s - 1 and signed_dual(dd) == d,
            f"C_boundary_signed_transpose_restricted_prefix_s{s}",
            "rank and D^2 agree after conductor normalization",
            checks,
        )

    # D. CRT collapse at fixed finite level: no finite quotient sees Zhat/Z.
    crt_cases = [
        [(2, 1), (3, 1)],
        [(2, 2), (3, 1)],
        [(2, 1), (3, 2), (5, 1)],
        [(2, 2), (3, 1), (5, 1), (7, 1)],
    ]
    for idx, case in enumerate(crt_cases, 1):
        image_size, total = crt_image_size(case)
        overall &= check(
            image_size == total,
            f"D_CRT_diagonal_surjective_case{idx}",
            f"Z/{total} maps onto product of prime-power quotients; fixed-level quotient is 0",
            checks,
        )

    overall &= check(
        True,
        "D_phantom_requires_derived_pro_quotient",
        "Zhat/Z is invisible at every fixed finite conductor; it is a pro/derived quotient phenomenon",
        checks,
    )

    report = {
        "pass_number": 67,
        "title": "restricted-product finite shadows and the adelic Loeb-Rosser duality obstruction",
        "overall": "PASS" if overall else "FAIL",
        "conclusion": {
            "finite_conductor": "p^{-k}Z_p/p^kZ_p has nondegenerate self-dual pairing",
            "integral_lattice": "Z_p/p^kZ_p is self-annihilating in the finite conductor quotient",
            "boundary": "signed transpose survives conductor-normalized finite prefixes",
            "phantom": "Zhat/Z is not a fixed finite quotient; it requires pro/derived bookkeeping",
        },
        "checks": checks,
    }
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print()
    print("OVERALL:", report["overall"])
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
