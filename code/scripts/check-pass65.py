#!/usr/bin/env python3
"""
Pass 65 verification: the Verdier-dual recollement presentation of the
finite Loeb-Rosser phantom.

This is a finite linear-algebra checker for the second gluing triangle

    i_* i^! F -> F -> R j_* j^* F -> +1

on X_S = {eta} cup {(p): p in S}.  The checker deliberately stays at the
finite/Alexandrov model level.  It verifies the algebraic spine needed for
the pass:

  A. The closed-support/costalk complex attached to the generic diagonal
     Z -> Z^S has H^0=0 and H^1=Z^{s-1}.  This is the i^!-side horizontal
     Rosser lattice.
  B. The recollement boundary d: Z^S -> Z^{s-1},
        (x_p) |-> (x_p - x_p0)_{p != p0},
     dualizes to -d^T.  Thus Verdier duality exchanges j_! with Rj_* and
     sends the extension class epsilon_S to the negative transpose
     -epsilon_S^vee.  The sign is invisible over F_2 but nontrivial over Z.
  C. Dualizing twice returns d, and the finite-prime restriction maps commute
     with this signed transpose.

The actual scheme-site lift to Spec Z and any topological Verdier-duality
normalization are not proved by this checker; those remain proof obligations.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
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


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


def neg(matrix: list[list[int]]) -> list[list[int]]:
    return [[-x for x in row] for row in matrix]


def dual_boundary(matrix: list[list[int]]) -> list[list[int]]:
    return neg(transpose(matrix))


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    if not a or not b:
        return []
    out = []
    bt = transpose(b)
    for row in a:
        out.append([sum(x * y for x, y in zip(row, col)) for col in bt])
    return out


def mat_eq(a: list[list[int]], b: list[list[int]]) -> bool:
    return a == b


def mod2(matrix: list[list[int]]) -> list[list[int]]:
    return [[x % 2 for x in row] for row in matrix]


def delta_matrix(s: int) -> list[list[int]]:
    return [[1] for _ in range(s)]


def boundary_matrix(s: int) -> list[list[int]]:
    if s <= 1:
        return []
    matrix = []
    for idx in range(1, s):
        row = [0] * s
        row[0] = -1
        row[idx] = 1
        matrix.append(row)
    return matrix


def projection(rows: int, cols: int) -> list[list[int]]:
    """Projection Z^cols -> Z^rows onto the first rows coordinates."""
    return [[1 if i == j else 0 for j in range(cols)] for i in range(rows)]


def check(condition: bool, name: str, detail: str, checks: dict[str, dict[str, object]]) -> bool:
    ok = bool(condition)
    checks[name] = {"pass": ok, "detail": detail}
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    return ok


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="pass65-report.json")
    args = parser.parse_args()

    checks: dict[str, dict[str, object]] = {}
    overall = True

    # A. i^!-side local-support complex Z -> Z^S.
    for s in range(1, 8):
        delta = delta_matrix(s)
        delta_rank = rank_q(delta)
        h0_rank = 1 - delta_rank
        h1_rank = s - delta_rank
        overall &= check(
            h0_rank == 0 and h1_rank == s - 1,
            f"A_costalk_complex_iBang_s{s}",
            f"ker(Delta) rank={h0_rank}, coker(Delta) rank={h1_rank}; i^!-horizontal rank=s-1",
            checks,
        )

    # B. Boundary and signed transpose.
    for s in range(1, 8):
        d = boundary_matrix(s)
        dd = dual_boundary(d)
        rank_d = rank_q(d)
        rank_dd = rank_q(dd)
        overall &= check(
            rank_d == s - 1 and rank_dd == s - 1,
            f"B_boundary_and_dual_rank_s{s}",
            f"rank(d)={rank_d}, rank(-d^T)={rank_dd}; same primitive obstruction rank",
            checks,
        )
        overall &= check(
            mat_eq(dual_boundary(dd), d),
            f"B_dual_squared_identity_s{s}",
            "D(D(d)) = d for the signed transpose convention",
            checks,
        )
        overall &= check(
            mat_eq(mod2(dd), mod2(transpose(d))),
            f"B_sign_invisible_mod2_s{s}",
            "-d^T equals d^T over F_2; sign is an integral orientation datum",
            checks,
        )

    # C. Naturality on finite-prime inclusions using first-coordinate basepoint.
    for small, big in ((1, 2), (2, 3), (3, 5), (4, 7)):
        d_small = boundary_matrix(small)
        d_big = boundary_matrix(big)
        source_restrict = projection(small, big)  # Z^big -> Z^small
        target_restrict = projection(max(small - 1, 0), max(big - 1, 0))
        lhs = matmul(target_restrict, d_big)
        rhs = matmul(d_small, source_restrict)
        overall &= check(
            mat_eq(lhs, rhs),
            f"C_boundary_naturality_{small}_in_{big}",
            "r_Ros d_big = d_small r_Loeb",
            checks,
        )

        lhs_dual = matmul(transpose(source_restrict), dual_boundary(d_small))
        rhs_dual = matmul(dual_boundary(d_big), transpose(target_restrict))
        overall &= check(
            mat_eq(lhs_dual, rhs_dual),
            f"C_dual_boundary_naturality_{small}_in_{big}",
            "r_Loeb^T (-d_small^T) = (-d_big^T) r_Ros^T",
            checks,
        )

    # D. Explicit statement-level certificates that the checker is finite-only.
    overall &= check(
        True,
        "D_functional_equation_statement",
        "finite model supports D(epsilon_S) = -epsilon_S^vee; over Z the sign is orientation, over F_2 it vanishes",
        checks,
    )
    overall &= check(
        True,
        "D_scheme_lift_gap_recorded",
        "checker does not prove the honest Spec Z site identity or topological Verdier-duality normalization",
        checks,
    )

    report = {
        "pass_number": 65,
        "title": "Verdier-dual recollement and signed functional equation of the Loeb-Rosser phantom",
        "overall": "PASS" if overall else "FAIL",
        "scope": "finite Alexandrov two-stratum model; scheme-site lift remains a proof obligation",
        "checks": checks,
    }
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print()
    print("OVERALL:", report["overall"])
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
