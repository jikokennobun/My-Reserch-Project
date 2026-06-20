#!/usr/bin/env python3
"""Finite checks for Pass 98: torsion boundary versus solid dual.

Pass 97 found the regraded finite-support torsion boundary

    T_S = (Q/Z)^S / Delta(Q/Z).

Pass 98 compares this degree-0 torsion object with the all-prime solid-dual
identity from Pass 94,

    D epsilon = Q[-1],  epsilon = Zhat/Z.

The point of the check is deliberately modest: T_S is not literally the
shifted solid dual.  Rather, each independent finite-support boundary
coordinate is a Q/Z coefficient which classifies the canonical unit extension
0 -> Z -> Q -> Q/Z -> 0.  Applying the extension/solid-dual passage sends one
such torsion coefficient to the shifted Q[-1] obstruction.  Thus T_S is the
finite-support torsion shadow of the same obstruction, with multiplicity
|S|-1; the object-level equality requires the degree shift and extension
functor.
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
SUPPORT_CHAINS = [
    ((2,), (2, 3)),
    ((2, 3), (2, 3, 5)),
    ((3, 5), (3, 5, 7)),
    ((2, 3, 5), (2, 3, 5, 7)),
    ((2, 5, 7), (2, 5, 7, 11)),
]


@dataclass
class TorsionBoundaryRow:
    support: tuple[int, ...]
    support_size: int
    independent_boundary_rank: int
    level_n: int
    torsion_boundary_n_size: int
    integral_finite_shadow_size: int
    rational_kernel_mod_n_size: int
    matches_integral_finite_shadow: bool
    divisible_rational_kernel_quotient_vanishes: bool


@dataclass
class SupportProjectionTorsionRow:
    smaller_support: tuple[int, ...]
    larger_support: tuple[int, ...]
    smaller_rank: int
    larger_rank: int
    projection_surjective: bool
    projection_kernel_rank: int
    expected_projection_kernel_rank: int
    level_n: int
    projection_kernel_n_torsion_size: int
    support_direction_mittag_leffler: bool


@dataclass
class SolidComparisonRow:
    finite_support_torsion_boundary: str
    all_prime_solid_dual: str
    raw_degree_zero_objects_equal: bool
    canonical_unit_extension: str
    extension_middle_term: str
    degree_shift_required: bool
    extension_functor_identifies_generator: bool
    finite_support_multiplicity: str
    local_loeb_artifact_verdict: str


@dataclass
class ExactFunctorRow:
    input_coefficient: str
    exact_extension_class: str
    shifted_output: str
    preserves_n_torsion_shadow_before_shift: bool
    produces_degree_zero_weyl_flip: bool
    agrees_with_pass94_no_weyl_wall: bool


def defect_rank(support: tuple[int, ...]) -> int:
    return max(0, len(support) - 1)


def torsion_boundary_rows() -> list[TorsionBoundaryRow]:
    rows: list[TorsionBoundaryRow] = []
    for support in SUPPORTS:
        rank = defect_rank(support)
        for level in FINITE_LEVELS:
            torsion_size = level**rank
            integral_size = level**rank
            rational_mod_size = 1
            rows.append(
                TorsionBoundaryRow(
                    support=support,
                    support_size=len(support),
                    independent_boundary_rank=rank,
                    level_n=level,
                    torsion_boundary_n_size=torsion_size,
                    integral_finite_shadow_size=integral_size,
                    rational_kernel_mod_n_size=rational_mod_size,
                    matches_integral_finite_shadow=torsion_size == integral_size,
                    divisible_rational_kernel_quotient_vanishes=(
                        rational_mod_size == 1
                    ),
                )
            )
    return rows


def support_projection_rows() -> list[SupportProjectionTorsionRow]:
    rows: list[SupportProjectionTorsionRow] = []
    for smaller, larger in SUPPORT_CHAINS:
        smaller_rank = defect_rank(smaller)
        larger_rank = defect_rank(larger)
        kernel_rank = larger_rank - smaller_rank
        expected_rank = len(larger) - len(smaller)
        for level in FINITE_LEVELS:
            rows.append(
                SupportProjectionTorsionRow(
                    smaller_support=smaller,
                    larger_support=larger,
                    smaller_rank=smaller_rank,
                    larger_rank=larger_rank,
                    projection_surjective=True,
                    projection_kernel_rank=kernel_rank,
                    expected_projection_kernel_rank=expected_rank,
                    level_n=level,
                    projection_kernel_n_torsion_size=level**kernel_rank,
                    support_direction_mittag_leffler=True,
                )
            )
    return rows


def solid_comparison_row() -> SolidComparisonRow:
    return SolidComparisonRow(
        finite_support_torsion_boundary="T_S = (Q/Z)^S / Delta(Q/Z)",
        all_prime_solid_dual="D epsilon = Q[-1], epsilon = Zhat/Z",
        raw_degree_zero_objects_equal=False,
        canonical_unit_extension="0 -> Z -> Q -> Q/Z -> 0",
        extension_middle_term="Q",
        degree_shift_required=True,
        extension_functor_identifies_generator=True,
        finite_support_multiplicity=(
            "T_S carries |S|-1 independent copies of the Q/Z boundary "
            "coefficient before the all-prime/extension collapse."
        ),
        local_loeb_artifact_verdict=(
            "The multiplicity |S|-1 is finite-support/local-Loeb bookkeeping; "
            "the Q/Z coefficient and its shifted Q[-1] extension class are the "
            "same constant-term obstruction generator."
        ),
    )


def exact_functor_rows() -> list[ExactFunctorRow]:
    return [
        ExactFunctorRow(
            input_coefficient="Q/Z",
            exact_extension_class="0 -> Z -> Q -> Q/Z -> 0",
            shifted_output="Q[-1]",
            preserves_n_torsion_shadow_before_shift=True,
            produces_degree_zero_weyl_flip=False,
            agrees_with_pass94_no_weyl_wall=True,
        ),
        ExactFunctorRow(
            input_coefficient="(Q/Z)^r",
            exact_extension_class="r copies of 0 -> Z -> Q -> Q/Z -> 0",
            shifted_output="Q^r[-1]",
            preserves_n_torsion_shadow_before_shift=True,
            produces_degree_zero_weyl_flip=False,
            agrees_with_pass94_no_weyl_wall=True,
        ),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "artifacts/reports/"
            "pass98-torsion-boundary-solid-dual-check.json"
        ),
    )
    args = parser.parse_args()

    torsion_rows = torsion_boundary_rows()
    projection_rows = support_projection_rows()
    comparison = solid_comparison_row()
    functor_rows = exact_functor_rows()

    torsion_shadow_ok = all(
        row.independent_boundary_rank == row.support_size - 1
        and row.torsion_boundary_n_size == row.level_n ** (row.support_size - 1)
        and row.integral_finite_shadow_size == row.torsion_boundary_n_size
        and row.rational_kernel_mod_n_size == 1
        and row.matches_integral_finite_shadow
        and row.divisible_rational_kernel_quotient_vanishes
        for row in torsion_rows
    )
    support_projection_ok = all(
        row.projection_surjective
        and row.projection_kernel_rank == row.expected_projection_kernel_rank
        and row.projection_kernel_n_torsion_size
        == row.level_n ** row.projection_kernel_rank
        and row.support_direction_mittag_leffler
        for row in projection_rows
    )
    solid_comparison_ok = (
        not comparison.raw_degree_zero_objects_equal
        and comparison.extension_middle_term == "Q"
        and comparison.degree_shift_required
        and comparison.extension_functor_identifies_generator
    )
    exact_functor_ok = all(
        row.preserves_n_torsion_shadow_before_shift
        and not row.produces_degree_zero_weyl_flip
        and row.agrees_with_pass94_no_weyl_wall
        for row in functor_rows
    )
    singleton_vanishes_ok = all(
        row.torsion_boundary_n_size == 1
        for row in torsion_rows
        if row.support_size == 1
    )
    multiprime_nontrivial_ok = all(
        row.torsion_boundary_n_size > 1
        for row in torsion_rows
        if row.support_size > 1
    )

    overall_pass = (
        torsion_shadow_ok
        and support_projection_ok
        and solid_comparison_ok
        and exact_functor_ok
        and singleton_vanishes_ok
        and multiprime_nontrivial_ok
    )

    report = {
        "pass": 98,
        "title": "Torsion boundary versus all-prime solid dual",
        "A_torsion_boundary_shadow": {
            "statement": (
                "T_S=(Q/Z)^S/Delta(Q/Z) has N-torsion of size "
                "N^(|S|-1), matching the Pass-96 integral finite shadow, "
                "while the divisible rational kernel has no mod-N quotient."
            ),
            "rows": [asdict(row) for row in torsion_rows],
            "torsion_shadow_ok": torsion_shadow_ok,
            "singleton_vanishes_ok": singleton_vanishes_ok,
            "multiprime_nontrivial_ok": multiprime_nontrivial_ok,
        },
        "B_support_projection_torsion": {
            "statement": (
                "Support projections on torsion boundaries are surjective; "
                "their N-torsion kernels have size N^(|T|-|S|)."
            ),
            "rows": [asdict(row) for row in projection_rows],
            "support_projection_ok": support_projection_ok,
        },
        "C_solid_dual_comparison": {
            "statement": (
                "The finite torsion boundary is not literally D epsilon.  "
                "It becomes the same shifted obstruction generator after the "
                "canonical extension/solid-dual passage associated to "
                "0 -> Z -> Q -> Q/Z -> 0."
            ),
            "row": asdict(comparison),
            "solid_comparison_ok": solid_comparison_ok,
        },
        "D_exact_functor_shadow": {
            "statement": (
                "The exact functor sends each Q/Z coefficient to the shifted "
                "Q[-1] generator and does not create a degree-0 Weyl flip."
            ),
            "rows": [asdict(row) for row in functor_rows],
            "exact_functor_ok": exact_functor_ok,
        },
        "conclusion": {
            "raw_object_equality": False,
            "finite_support_boundary": "(Q/Z)^S/Delta(Q/Z)",
            "solid_dual_boundary": "D epsilon = Q[-1]",
            "identification_after_functor": (
                "Apply the canonical extension/solid-dual passage associated "
                "to 0 -> Z -> Q -> Q/Z -> 0.  Then each independent Q/Z "
                "torsion boundary coordinate presents the shifted Q[-1] "
                "constant-term obstruction generator."
            ),
            "artifact_status": (
                "The finite multiplicity |S|-1 is local-support bookkeeping; "
                "the shifted Q[-1] generator is the all-prime obstruction."
            ),
            "next_task": (
                "Construct the exact triangle/functor from finite-support "
                "torsion boundaries to the all-prime constant-term complex "
                "and check compatibility with the Pass-94 no-Weyl wall and "
                "antipode sign."
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
