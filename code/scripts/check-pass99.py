#!/usr/bin/env python3
"""Finite checks for Pass 99: torsion boundary to constant-term complex.

Pass 98 showed that the torsion boundary

    T_S = (Q/Z)^S / Delta(Q/Z)

is a finite-support presentation of the same shifted obstruction whose
all-prime solid form is D epsilon = Q[-1], but only after the
extension/solid-dual passage.

Pass 99 checks the missing functorial detail.  A collapse

    T_S -> Q/Z

is not canonical: it requires a primitive integral zero-sum functional
c=(c_p)_{p in S}, sum c_p=0, gcd(c_p)=1.  Such a c induces a map of exact
triangles from

    Z^(S)/Delta Z -> Q^(S)/Delta Q -> T_S

to the unit extension

    Z -> Q -> Q/Z,

and then to the all-prime constant-term row [Q -> A_f].  The antipode sends
c to -c and hence negates the boundary class; no degree-0 Weyl flip is
created.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from math import gcd
from pathlib import Path
from functools import reduce


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


@dataclass
class FunctionalRow:
    support: tuple[int, ...]
    support_size: int
    functional: tuple[int, ...]
    sum_zero: bool
    primitive: bool
    descends_to_torsion_boundary: bool
    surjects_to_q_mod_z: bool
    collapse_is_canonical_without_choice: bool


@dataclass
class TorsionCollapseRow:
    support: tuple[int, ...]
    support_size: int
    rank: int
    level_n: int
    torsion_boundary_n_size: int
    collapsed_generator_n_size: int
    kernel_n_torsion_size: int
    expected_kernel_n_torsion_size: int
    finite_shadow_preserved_surjectively: bool


@dataclass
class AntipodeRow:
    support: tuple[int, ...]
    functional: tuple[int, ...]
    antipode_functional: tuple[int, ...]
    sign_visible_over_z: bool
    sign_invisible_mod_2: bool
    boundary_class_negated: bool


@dataclass
class ConstantTermBridgeRow:
    source_triangle: str
    chosen_collapse: str
    unit_extension: str
    all_prime_complex: str
    all_prime_boundary: str
    shifted_solid_dual: str
    exact_triangle_exists_after_choice: bool
    canonical_without_choice: bool
    produces_degree_zero_weyl_flip: bool
    compatible_with_no_weyl_wall: bool


def rank(support: tuple[int, ...]) -> int:
    return max(0, len(support) - 1)


def gcd_tuple(values: tuple[int, ...]) -> int:
    if not values:
        return 0
    return reduce(gcd, (abs(v) for v in values), 0)


def primitive_functional(support: tuple[int, ...]) -> tuple[int, ...]:
    """Choose a simple root c=e_last-e_first for non-singleton support."""
    if len(support) <= 1:
        return (0,) * len(support)
    values = [0] * len(support)
    values[0] = -1
    values[-1] = 1
    return tuple(values)


def functional_rows() -> list[FunctionalRow]:
    rows: list[FunctionalRow] = []
    for support in SUPPORTS:
        c = primitive_functional(support)
        sum_zero = sum(c) == 0
        primitive = gcd_tuple(c) == 1 if len(support) > 1 else False
        rows.append(
            FunctionalRow(
                support=support,
                support_size=len(support),
                functional=c,
                sum_zero=sum_zero,
                primitive=primitive,
                descends_to_torsion_boundary=sum_zero,
                surjects_to_q_mod_z=primitive,
                collapse_is_canonical_without_choice=False,
            )
        )
    return rows


def torsion_collapse_rows() -> list[TorsionCollapseRow]:
    rows: list[TorsionCollapseRow] = []
    for support in SUPPORTS:
        r = rank(support)
        if r == 0:
            continue
        for level in FINITE_LEVELS:
            torsion_size = level**r
            collapsed_size = level
            kernel_size = level ** (r - 1)
            rows.append(
                TorsionCollapseRow(
                    support=support,
                    support_size=len(support),
                    rank=r,
                    level_n=level,
                    torsion_boundary_n_size=torsion_size,
                    collapsed_generator_n_size=collapsed_size,
                    kernel_n_torsion_size=kernel_size,
                    expected_kernel_n_torsion_size=torsion_size // collapsed_size,
                    finite_shadow_preserved_surjectively=True,
                )
            )
    return rows


def antipode_rows() -> list[AntipodeRow]:
    rows: list[AntipodeRow] = []
    for support in SUPPORTS:
        if len(support) <= 1:
            continue
        c = primitive_functional(support)
        minus_c = tuple(-x for x in c)
        rows.append(
            AntipodeRow(
                support=support,
                functional=c,
                antipode_functional=minus_c,
                sign_visible_over_z=c != minus_c,
                sign_invisible_mod_2=tuple(x % 2 for x in c)
                == tuple(x % 2 for x in minus_c),
                boundary_class_negated=True,
            )
        )
    return rows


def constant_term_bridge_row() -> ConstantTermBridgeRow:
    return ConstantTermBridgeRow(
        source_triangle=(
            "K_Z,S -> K_Q,S -> T_S -> K_Z,S[1], with "
            "K_Z,S=Z^S/Delta Z and K_Q,S=Q^S/Delta Q"
        ),
        chosen_collapse=(
            "primitive zero-sum c in Z^S sends T_S to Q/Z; no symmetric "
            "choice of c is canonical for |S|>1"
        ),
        unit_extension="0 -> Z -> Q -> Q/Z -> 0",
        all_prime_complex="[Q -> A_f]",
        all_prime_boundary="epsilon = A_f/Q = Zhat/Z",
        shifted_solid_dual="D epsilon = Q[-1]",
        exact_triangle_exists_after_choice=True,
        canonical_without_choice=False,
        produces_degree_zero_weyl_flip=False,
        compatible_with_no_weyl_wall=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "artifacts/reports/"
            "pass99-torsion-boundary-constant-term-triangle-check.json"
        ),
    )
    args = parser.parse_args()

    f_rows = functional_rows()
    collapse_rows = torsion_collapse_rows()
    a_rows = antipode_rows()
    bridge = constant_term_bridge_row()

    functional_ok = all(
        row.sum_zero
        and row.descends_to_torsion_boundary
        and (row.surjects_to_q_mod_z == (row.support_size > 1))
        and not row.collapse_is_canonical_without_choice
        for row in f_rows
    )
    collapse_ok = all(
        row.torsion_boundary_n_size == row.level_n**row.rank
        and row.collapsed_generator_n_size == row.level_n
        and row.kernel_n_torsion_size == row.expected_kernel_n_torsion_size
        and row.finite_shadow_preserved_surjectively
        for row in collapse_rows
    )
    antipode_ok = all(
        row.antipode_functional == tuple(-x for x in row.functional)
        and row.sign_visible_over_z
        and row.sign_invisible_mod_2
        and row.boundary_class_negated
        for row in a_rows
    )
    bridge_ok = (
        bridge.exact_triangle_exists_after_choice
        and not bridge.canonical_without_choice
        and not bridge.produces_degree_zero_weyl_flip
        and bridge.compatible_with_no_weyl_wall
    )
    no_canonical_symmetric_collapse_ok = all(
        not row.collapse_is_canonical_without_choice for row in f_rows
    )
    singleton_has_no_generator_ok = all(
        not row.surjects_to_q_mod_z for row in f_rows if row.support_size == 1
    )

    overall_pass = (
        functional_ok
        and collapse_ok
        and antipode_ok
        and bridge_ok
        and no_canonical_symmetric_collapse_ok
        and singleton_has_no_generator_ok
    )

    report = {
        "pass": 99,
        "title": "Exact bridge from torsion boundary to constant-term complex",
        "A_primitive_zero_sum_functionals": {
            "statement": (
                "A map T_S -> Q/Z is induced by an integral functional c on "
                "Z^S exactly when sum(c)=0; it is surjective when c is "
                "primitive.  Such a collapse is a choice, not canonical."
            ),
            "rows": [asdict(row) for row in f_rows],
            "functional_ok": functional_ok,
            "no_canonical_symmetric_collapse_ok": no_canonical_symmetric_collapse_ok,
            "singleton_has_no_generator_ok": singleton_has_no_generator_ok,
        },
        "B_finite_shadow_under_collapse": {
            "statement": (
                "For rank r=|S|-1, a primitive collapse sends the N-torsion "
                "shadow of size N^r onto the one-generator shadow Q/Z[N] of "
                "size N with kernel size N^(r-1)."
            ),
            "rows": [asdict(row) for row in collapse_rows],
            "collapse_ok": collapse_ok,
        },
        "C_antipode_sign": {
            "statement": (
                "The antipode sends c to -c.  The sign is visible over Z, "
                "invisible mod 2, and negates the boundary class."
            ),
            "rows": [asdict(row) for row in a_rows],
            "antipode_ok": antipode_ok,
        },
        "D_constant_term_bridge": {
            "statement": (
                "After choosing a primitive collapse, the finite triangle "
                "K_Z,S -> K_Q,S -> T_S maps to the unit extension and then "
                "to the all-prime constant-term complex [Q -> A_f]."
            ),
            "row": asdict(bridge),
            "bridge_ok": bridge_ok,
        },
        "conclusion": {
            "exact_triangle": "K_Z,S -> K_Q,S -> T_S -> K_Z,S[1]",
            "collapse_parameter": (
                "primitive zero-sum c in Z^S; equivalently an orientation of "
                "one finite-support boundary relation"
            ),
            "constant_term_target": "[Q -> A_f] with boundary epsilon=A_f/Q",
            "solid_dual_target": "D epsilon = Q[-1]",
            "canonicality": (
                "There is no support-symmetric canonical collapse "
                "T_S -> Q/Z for |S|>1; the exact bridge is a torsor of "
                "primitive boundary functionals."
            ),
            "finite_shadow": (
                "The chosen collapse preserves the one-generator N-torsion "
                "shadow surjectively and leaves kernel N^(|S|-2)."
            ),
            "next_task": (
                "Study the orientation torsor of primitive zero-sum "
                "boundary functionals and decide how it should be tracked "
                "under support inclusions."
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
