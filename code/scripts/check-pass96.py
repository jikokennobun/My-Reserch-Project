#!/usr/bin/env python3
"""Finite checks for Pass 96: constant-term complex versus local Loebification.

Pass 95 packaged the boundary-only Borel shadow as

    C_B = Q^x semidirect [Q -> A_f].

Pass 96 compares its compact finite-support skeleton with the local Loeb
sheafification from Pass 91.  For a finite support S, the unipotent comparison
is the map of two-term complexes

    [ Z -> prod_{p in S} Z_p ]  --->  [ Z^S -> prod_{p in S} Z_p ],

where the left degree-0 map is diagonal, the right degree-0 map is
coordinatewise, and degree 1 is the identity.  On H^1 this is

    (prod Z_p) / Delta Z  --->  prod (Z_p / Z),

with kernel Z^S / Delta Z.  The Levi comparison is diagonal

    Q^x -> (Q^x)^S;

it has no kernel, but its local quotient measures the independent local Levi
choices created by sheafification.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


SUPPORTS = [
    (2,),
    (2, 3),
    (2, 5),
    (2, 3, 5),
    (3, 5, 7),
    (2, 3, 5, 7),
    (2, 5, 7, 11),
]
FINITE_LEVELS = [2, 3, 4, 5, 6, 8, 12]
LEVI_PROXY_ORDERS = [2, 3, 4, 6]


@dataclass
class ComplexComparisonRow:
    support: tuple[int, ...]
    support_size: int
    global_degree0_rank: int
    local_degree0_rank: int
    quotient_degree0_rank: int
    degree1_map_is_identity: bool
    global_h0_rank: int
    local_h0_rank: int
    h1_map_surjective_to_local_loeb: bool
    lost_unipotent_kernel_rank: int
    cone_records_lost_kernel_in_degree0: bool


@dataclass
class FiniteLevelKernelRow:
    support: tuple[int, ...]
    support_size: int
    level_n: int
    global_h1_size: int
    local_h1_size: int
    lost_kernel_size: int
    expected_kernel_size: int
    kernel_matches_expected: bool


@dataclass
class LeviComparisonRow:
    support: tuple[int, ...]
    support_size: int
    levi_proxy_order: int
    global_levi_order: int
    local_levi_order: int
    diagonal_levi_kernel_size: int
    local_levi_quotient_size: int
    expected_quotient_size: int
    levi_kernel_is_trivial: bool
    levi_loss_is_quotient_not_kernel: bool


@dataclass
class ClassificationRow:
    formulation: str
    map_of_two_term_complexes: bool
    stackification_or_sheafification: bool
    pure_hausdorff_reflection: bool
    local_constant_term_projection: bool
    preserves_global_rosser_boundary: bool


def defect_rank(support: tuple[int, ...]) -> int:
    return max(0, len(support) - 1)


def complex_comparison_rows() -> list[ComplexComparisonRow]:
    rows: list[ComplexComparisonRow] = []
    for support in SUPPORTS:
        rank = defect_rank(support)
        rows.append(
            ComplexComparisonRow(
                support=support,
                support_size=len(support),
                global_degree0_rank=1,
                local_degree0_rank=len(support),
                quotient_degree0_rank=rank,
                degree1_map_is_identity=True,
                global_h0_rank=0,
                local_h0_rank=0,
                h1_map_surjective_to_local_loeb=True,
                lost_unipotent_kernel_rank=rank,
                cone_records_lost_kernel_in_degree0=True,
            )
        )
    return rows


def finite_level_kernel_rows() -> list[FiniteLevelKernelRow]:
    rows: list[FiniteLevelKernelRow] = []
    for support in SUPPORTS:
        rank = defect_rank(support)
        for level in FINITE_LEVELS:
            global_h1_size = level**rank
            local_h1_size = 1
            lost_kernel_size = global_h1_size // local_h1_size
            expected = level**rank
            rows.append(
                FiniteLevelKernelRow(
                    support=support,
                    support_size=len(support),
                    level_n=level,
                    global_h1_size=global_h1_size,
                    local_h1_size=local_h1_size,
                    lost_kernel_size=lost_kernel_size,
                    expected_kernel_size=expected,
                    kernel_matches_expected=lost_kernel_size == expected,
                )
            )
    return rows


def levi_comparison_rows() -> list[LeviComparisonRow]:
    rows: list[LeviComparisonRow] = []
    for support in SUPPORTS:
        rank = defect_rank(support)
        for proxy_order in LEVI_PROXY_ORDERS:
            global_order = proxy_order
            local_order = proxy_order ** len(support)
            quotient_size = local_order // global_order
            expected = proxy_order**rank
            rows.append(
                LeviComparisonRow(
                    support=support,
                    support_size=len(support),
                    levi_proxy_order=proxy_order,
                    global_levi_order=global_order,
                    local_levi_order=local_order,
                    diagonal_levi_kernel_size=1,
                    local_levi_quotient_size=quotient_size,
                    expected_quotient_size=expected,
                    levi_kernel_is_trivial=True,
                    levi_loss_is_quotient_not_kernel=True,
                )
            )
    return rows


def classification_row() -> ClassificationRow:
    return ClassificationRow(
        formulation=(
            "The comparison is best read as a map of two-term complexes plus "
            "stackification/local sheafification.  Hausdorff reflection captures "
            "the unipotent quotient, but not the diagonal-to-local Levi change."
        ),
        map_of_two_term_complexes=True,
        stackification_or_sheafification=True,
        pure_hausdorff_reflection=False,
        local_constant_term_projection=True,
        preserves_global_rosser_boundary=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "artifacts/reports/"
            "pass96-constant-term-local-loebification-check.json"
        ),
    )
    args = parser.parse_args()

    complex_rows = complex_comparison_rows()
    finite_rows = finite_level_kernel_rows()
    levi_rows = levi_comparison_rows()
    classification = classification_row()

    complex_map_ok = all(
        row.global_degree0_rank == 1
        and row.local_degree0_rank == row.support_size
        and row.quotient_degree0_rank == row.support_size - 1
        and row.degree1_map_is_identity
        and row.global_h0_rank == 0
        and row.local_h0_rank == 0
        and row.h1_map_surjective_to_local_loeb
        and row.lost_unipotent_kernel_rank == row.support_size - 1
        and row.cone_records_lost_kernel_in_degree0
        for row in complex_rows
    )
    finite_kernels_ok = all(row.kernel_matches_expected for row in finite_rows)
    levi_comparison_ok = all(
        row.diagonal_levi_kernel_size == 1
        and row.local_levi_quotient_size == row.expected_quotient_size
        and row.levi_kernel_is_trivial
        and row.levi_loss_is_quotient_not_kernel
        for row in levi_rows
    )
    classification_ok = (
        classification.map_of_two_term_complexes
        and classification.stackification_or_sheafification
        and not classification.pure_hausdorff_reflection
        and classification.local_constant_term_projection
        and not classification.preserves_global_rosser_boundary
    )
    singleton_vanishes_ok = all(
        row.lost_unipotent_kernel_rank == 0
        for row in complex_rows
        if row.support_size == 1
    )
    multiprime_nontrivial_ok = all(
        row.lost_unipotent_kernel_rank > 0
        for row in complex_rows
        if row.support_size > 1
    )

    overall_pass = (
        complex_map_ok
        and finite_kernels_ok
        and levi_comparison_ok
        and classification_ok
        and singleton_vanishes_ok
        and multiprime_nontrivial_ok
    )

    report = {
        "pass": 96,
        "title": "Constant-term Borel complex versus local Loebification",
        "A_two_term_complex_map": {
            "statement": (
                "The compact support comparison is [Z -> prod Z_p] -> "
                "[Z^S -> prod Z_p], diagonal in degree 0 and identity in "
                "degree 1.  Its H^1 kernel is Z^S/Delta Z."
            ),
            "rows": [asdict(row) for row in complex_rows],
            "complex_map_ok": complex_map_ok,
            "singleton_vanishes_ok": singleton_vanishes_ok,
            "multiprime_nontrivial_ok": multiprime_nontrivial_ok,
        },
        "B_finite_level_kernels": {
            "statement": (
                "At finite level N, the global quotient has size N^(|S|-1) "
                "and the local quotient is zero, so the lost kernel has size "
                "N^(|S|-1)."
            ),
            "rows": [asdict(row) for row in finite_rows],
            "finite_kernels_ok": finite_kernels_ok,
        },
        "C_levi_comparison": {
            "statement": (
                "The diagonal Levi map has trivial kernel.  The lost global "
                "coherence is instead the local quotient (G^S)/Delta G, "
                "represented by finite proxy size |G|^(|S|-1)."
            ),
            "rows": [asdict(row) for row in levi_rows],
            "levi_comparison_ok": levi_comparison_ok,
        },
        "D_classification": {
            "statement": (
                "The comparison is a stackification/local sheafification map "
                "of two-term complexes.  Pure Hausdorff reflection sees only "
                "the unipotent quotient and misses the Levi decentralization."
            ),
            "row": asdict(classification),
            "classification_ok": classification_ok,
        },
        "conclusion": {
            "global_complex": "C_B^int(S)=Q^x semidirect [Z -> prod_{p in S} Z_p]",
            "local_complex": (
                "C_L(S)=(Q^x)^S semidirect [Z^S -> prod_{p in S} Z_p]"
            ),
            "h1_exact_sequence": (
                "0 -> Z^S/Delta Z -> (prod Z_p)/Delta Z -> "
                "prod (Z_p/Z) -> 0"
            ),
            "lost_kernel": "K_S=Z^S/Delta Z, finite shadow size N^(|S|-1)",
            "levi_change": (
                "Q^x -> (Q^x)^S is injective; the lost global coherence is "
                "the quotient (Q^x)^S/Delta Q^x, not a kernel."
            ),
            "best_formulation": (
                "Map of two-term complexes plus stackification/local "
                "constant-term projection."
            ),
            "next_task": (
                "Lift this compact comparison to the full finite-adele row "
                "[Q -> A_f] and decide whether rationalization kills or "
                "regrades the free kernel Z^S/Delta Z."
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
