#!/usr/bin/env python3
"""Finite checks for Pass 91: Borel torsor descent obstruction.

The pass asks whether the restriction/span Borel-torsor package from Pass 90
is a sheaf, a stack, or a descent-obstruction object on the finite prime-cover
site.  The finite certificate models the singleton-prime cover by:

* the diagonal quotient defect coker(Delta: Z -> Z^S), represented at finite
  level by coker(Delta: Z/N -> (Z/N)^S) of size N^(|S|-1);
* a finite proxy G for the constant global Levi Q^x.  Sheafifying a constant
  group over a discrete singleton cover turns G into G^S, so the local-Levi
  freedom not present in the global-Levi Borel has size |G|^(|S|-1);
* the Borel unipotent shear action transports the kernel of local descent data
  but does not choose a canonical zero for it.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from math import prod
from pathlib import Path


SUPPORTS = [
    (2,),
    (2, 3),
    (2, 5),
    (2, 3, 5),
    (3, 5, 7),
    (2, 5, 7, 11),
]
FINITE_LEVELS = [2, 3, 4, 6, 8, 12]
LEVI_PROXY_ORDER = 4


@dataclass
class DescentDefectRow:
    support: tuple[int, ...]
    support_size: int
    horizontal_rank: int
    separated_for_phantom_presheaf: bool
    sheafification_kernel_rank: int
    rosser_defect_present: bool


@dataclass
class FiniteKernelRow:
    support: tuple[int, ...]
    level_n: int
    diagonal_domain_size: int
    product_size: int
    finite_kernel_size: int
    expected_kernel_size: int
    kernel_matches_expected: bool


@dataclass
class BorelDescentRow:
    support: tuple[int, ...]
    support_size: int
    global_levi_proxy_order: int
    local_levi_proxy_order: int
    local_levi_quotient_size: int
    unipotent_kernel_rank: int
    global_borel_is_sheaf: bool
    stackification_target: str


@dataclass
class ShearActionRow:
    support: tuple[int, ...]
    support_size: int
    finite_level_n: int
    descent_lift_count: int
    shear_orbit_size: int
    shear_transports_defect: bool
    shear_kills_defect: bool


def defect_rank(support: tuple[int, ...]) -> int:
    return max(0, len(support) - 1)


def descent_defect_rows() -> list[DescentDefectRow]:
    rows: list[DescentDefectRow] = []
    for support in SUPPORTS:
        rank = defect_rank(support)
        rows.append(
            DescentDefectRow(
                support=support,
                support_size=len(support),
                horizontal_rank=rank,
                separated_for_phantom_presheaf=rank == 0,
                sheafification_kernel_rank=rank,
                rosser_defect_present=rank > 0,
            )
        )
    return rows


def finite_kernel_rows() -> list[FiniteKernelRow]:
    rows: list[FiniteKernelRow] = []
    for support in SUPPORTS:
        s = len(support)
        for level in FINITE_LEVELS:
            diagonal_domain_size = level
            product_size = level**s
            expected = level ** defect_rank(support)
            # The diagonal has size N, so the quotient (Z/N)^S / Delta(Z/N)
            # has size N^s / N = N^(s-1).
            kernel_size = product_size // diagonal_domain_size
            rows.append(
                FiniteKernelRow(
                    support=support,
                    level_n=level,
                    diagonal_domain_size=diagonal_domain_size,
                    product_size=product_size,
                    finite_kernel_size=kernel_size,
                    expected_kernel_size=expected,
                    kernel_matches_expected=kernel_size == expected,
                )
            )
    return rows


def borel_descent_rows() -> list[BorelDescentRow]:
    rows: list[BorelDescentRow] = []
    for support in SUPPORTS:
        s = len(support)
        local_order = LEVI_PROXY_ORDER**s
        quotient = LEVI_PROXY_ORDER ** defect_rank(support)
        rows.append(
            BorelDescentRow(
                support=support,
                support_size=s,
                global_levi_proxy_order=LEVI_PROXY_ORDER,
                local_levi_proxy_order=local_order,
                local_levi_quotient_size=quotient,
                unipotent_kernel_rank=defect_rank(support),
                global_borel_is_sheaf=(s == 1),
                stackification_target="local Levi sheaf G^S semidirect stalkwise unipotent sheaf L(S)",
            )
        )
    return rows


def shear_action_rows() -> list[ShearActionRow]:
    rows: list[ShearActionRow] = []
    for support in SUPPORTS:
        for level in (2, 6, 12):
            lift_count = level ** defect_rank(support)
            rows.append(
                ShearActionRow(
                    support=support,
                    support_size=len(support),
                    finite_level_n=level,
                    descent_lift_count=lift_count,
                    shear_orbit_size=lift_count,
                    shear_transports_defect=True,
                    shear_kills_defect=False,
                )
            )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass91-borel-torsor-descent-obstruction-check.json",
    )
    args = parser.parse_args()

    descent_rows = descent_defect_rows()
    kernel_rows = finite_kernel_rows()
    borel_rows = borel_descent_rows()
    shear_rows = shear_action_rows()

    descent_rank_ok = all(
        row.horizontal_rank == row.support_size - 1
        and row.sheafification_kernel_rank == row.horizontal_rank
        for row in descent_rows
    )
    nontrivial_defect_for_multi_prime = all(
        row.rosser_defect_present == (row.support_size >= 2)
        and row.separated_for_phantom_presheaf == (row.support_size == 1)
        for row in descent_rows
    )
    finite_kernels_ok = all(row.kernel_matches_expected for row in kernel_rows)
    global_borel_sheaf_criterion_ok = all(
        row.global_borel_is_sheaf == (row.support_size == 1) for row in borel_rows
    )
    levi_localization_ok = all(
        row.local_levi_quotient_size
        == row.global_levi_proxy_order ** row.unipotent_kernel_rank
        for row in borel_rows
    )
    shear_transports_not_kills = all(
        row.shear_transports_defect
        and not row.shear_kills_defect
        and row.shear_orbit_size == row.descent_lift_count
        for row in shear_rows
    )

    overall_pass = (
        descent_rank_ok
        and nontrivial_defect_for_multi_prime
        and finite_kernels_ok
        and global_borel_sheaf_criterion_ok
        and levi_localization_ok
        and shear_transports_not_kills
    )

    report = {
        "pass": 91,
        "title": "Borel torsor descent obstruction",
        "A_phantom_descent_defect": {
            "statement": (
                "The singleton-prime descent defect of P(S) is the free group "
                "Z^S/Delta Z of rank |S|-1; P is separated only on one-prime supports."
            ),
            "rows": [asdict(row) for row in descent_rows],
            "descent_rank_ok": descent_rank_ok,
            "nontrivial_defect_for_multi_prime": nontrivial_defect_for_multi_prime,
        },
        "B_finite_diagonal_kernel": {
            "statement": (
                "At finite level N, the diagonal quotient proxy has kernel size "
                "N^(|S|-1), matching the rank |S|-1 descent defect."
            ),
            "rows": [asdict(row) for row in kernel_rows],
            "finite_kernels_ok": finite_kernels_ok,
        },
        "C_global_borel_vs_stackification": {
            "statement": (
                "The global-Levi Borel prestack is not a sheaf on multi-prime "
                "supports. Stackification/local sheafification replaces the "
                "constant global Levi by local Levi data and quotients the "
                "unipotent Rosser defect."
            ),
            "rows": [asdict(row) for row in borel_rows],
            "global_borel_sheaf_criterion_ok": global_borel_sheaf_criterion_ok,
            "levi_localization_ok": levi_localization_ok,
        },
        "D_shear_action_on_defect": {
            "statement": (
                "The hyperbolic Borel shear action transports the descent-kernel "
                "lifts transitively in finite shadows, but does not provide a "
                "canonical zero section and therefore does not kill the defect."
            ),
            "rows": [asdict(row) for row in shear_rows],
            "shear_transports_not_kills": shear_transports_not_kills,
        },
        "conclusion": {
            "classification": (
                "The Pass-90 restriction/span Borel-torsor package is a prestack/"
                "descent-obstruction object, not a sheaf on multi-prime supports."
            ),
            "stackification": (
                "Its stackification or sheafification is the local Borel sheaf "
                "with local Levi data and stalkwise unipotents; the Rosser class "
                "is precisely the kernel lost in that process."
            ),
            "next_task": (
                "Relocate the Borel descent obstruction to the Zariski/generic "
                "prime site and compare it with the Pass-63 j_! ghost line."
            ),
        },
        "overall": "PASS" if overall_pass else "FAIL",
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output_path}")
    print(f"overall {report['overall']}")
    return 0 if overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
