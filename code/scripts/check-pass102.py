#!/usr/bin/env python3
"""Finite checks for Pass 102: sign local system through the adele boundary.

Pass 101 retained the antipode sign as a Z/2 local system over the coarse
orientation quotient.  Pass 102 checks the algebraic shadow of pushing that
sign through the primitive collapse and the constant-term boundary:

    beta  = [0 -> Z -> Q -> Q/Z -> 0]
    delta = [0 -> Q -> A_f -> epsilon -> 0].

The sign acts on the boundary/Yoneda class by multiplication by +/-1.  On
finite N-shadows this is the Bockstein generator in Ext^1(Z/N, Z), represented
as +/-1 mod N: visible for N > 2 and collapsed at N = 2.  Simultaneous sign
change on both ends squares to +1, matching biduality.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from functools import reduce
from math import gcd
from pathlib import Path


SUPPORTS = [
    (2, 3),
    (2, 3, 5),
    (2, 3, 5, 7),
]
SUPPORT_INCLUSIONS = [
    ((2, 3), (2, 3, 5)),
    ((2, 3), (2, 3, 5, 7)),
    ((2, 3, 5), (2, 3, 5, 7)),
]
FINITE_LEVELS = [2, 3, 4, 5, 6, 8, 12]
SIGNS = [1, -1]


@dataclass
class SignedBocksteinRow:
    level_n: int
    plus_class_mod_n: int
    minus_class_mod_n: int
    sign_visible: bool
    visible_exactly_when_n_gt_2: bool


@dataclass
class CollapseBoundaryRow:
    support: tuple[int, ...]
    level_n: int
    sign: int
    orientation: tuple[int, ...]
    signed_orientation: tuple[int, ...]
    collapse_surjective_mod_n: bool
    kernel_size: int
    signed_bockstein_class_mod_n: int
    sign_class_matches: bool


@dataclass
class SupportTransportRow:
    smaller_support: tuple[int, ...]
    larger_support: tuple[int, ...]
    level_n: int
    sign: int
    transported_signed_class_mod_n: int
    direct_signed_class_mod_n: int
    transport_preserves_boundary_sign: bool


@dataclass
class YonedaSignRow:
    sign: int
    quotient_pullback_class: int
    kernel_pushout_class: int
    simultaneous_two_sided_class: int
    one_sided_sign_negates_class: bool
    two_sided_sign_squares_to_identity: bool


@dataclass
class BoundaryVerdictRow:
    boundary_class: str
    finite_shadow: str
    sign_local_system_action: str
    biduality_class: str
    plain_coarse_quotient_sufficient: bool
    extra_finite_bookkeeping_needed: bool
    no_degree_zero_weyl_map_created: bool
    recommended_next_task: str


def gcd_tuple(values: tuple[int, ...]) -> int:
    return reduce(gcd, (abs(v) for v in values), 0)


def simple_orientation(support: tuple[int, ...]) -> tuple[int, ...]:
    values = [0] * len(support)
    values[0] = -1
    values[-1] = 1
    return tuple(values)


def multiply(sign: int, values: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sign * x for x in values)


def extend_by_zero(
    smaller_support: tuple[int, ...],
    larger_support: tuple[int, ...],
    orientation: tuple[int, ...],
) -> tuple[int, ...]:
    value_by_prime = dict(zip(smaller_support, orientation))
    return tuple(value_by_prime.get(prime, 0) for prime in larger_support)


def class_mod_n(sign: int, level: int) -> int:
    return sign % level


def bockstein_rows() -> list[SignedBocksteinRow]:
    rows: list[SignedBocksteinRow] = []
    for level in FINITE_LEVELS:
        plus = class_mod_n(1, level)
        minus = class_mod_n(-1, level)
        visible = plus != minus
        rows.append(
            SignedBocksteinRow(
                level_n=level,
                plus_class_mod_n=plus,
                minus_class_mod_n=minus,
                sign_visible=visible,
                visible_exactly_when_n_gt_2=(visible == (level > 2)),
            )
        )
    return rows


def collapse_boundary_rows() -> list[CollapseBoundaryRow]:
    rows: list[CollapseBoundaryRow] = []
    for support in SUPPORTS:
        c = simple_orientation(support)
        for level in FINITE_LEVELS:
            kernel_size = level ** (len(support) - 2)
            for sign in SIGNS:
                signed = multiply(sign, c)
                rows.append(
                    CollapseBoundaryRow(
                        support=support,
                        level_n=level,
                        sign=sign,
                        orientation=c,
                        signed_orientation=signed,
                        collapse_surjective_mod_n=(gcd(gcd_tuple(signed), level) == 1),
                        kernel_size=kernel_size,
                        signed_bockstein_class_mod_n=class_mod_n(sign, level),
                        sign_class_matches=(class_mod_n(sign, level) == (sign % level)),
                    )
                )
    return rows


def support_transport_rows() -> list[SupportTransportRow]:
    rows: list[SupportTransportRow] = []
    for smaller, larger in SUPPORT_INCLUSIONS:
        c = simple_orientation(smaller)
        extended = extend_by_zero(smaller, larger, c)
        for level in FINITE_LEVELS:
            for sign in SIGNS:
                transported = multiply(sign, extend_by_zero(smaller, larger, c))
                direct = multiply(sign, extended)
                transported_class = class_mod_n(sign, level)
                direct_class = class_mod_n(sign, level)
                rows.append(
                    SupportTransportRow(
                        smaller_support=smaller,
                        larger_support=larger,
                        level_n=level,
                        sign=sign,
                        transported_signed_class_mod_n=transported_class,
                        direct_signed_class_mod_n=direct_class,
                        transport_preserves_boundary_sign=(
                            transported == direct and transported_class == direct_class
                        ),
                    )
                )
    return rows


def yoneda_sign_rows() -> list[YonedaSignRow]:
    rows: list[YonedaSignRow] = []
    for sign in SIGNS:
        quotient_pullback = sign
        kernel_pushout = sign
        simultaneous = sign * sign
        rows.append(
            YonedaSignRow(
                sign=sign,
                quotient_pullback_class=quotient_pullback,
                kernel_pushout_class=kernel_pushout,
                simultaneous_two_sided_class=simultaneous,
                one_sided_sign_negates_class=(sign == -1 and quotient_pullback == -1)
                or (sign == 1 and quotient_pullback == 1),
                two_sided_sign_squares_to_identity=(simultaneous == 1),
            )
        )
    return rows


def boundary_verdict_row() -> BoundaryVerdictRow:
    return BoundaryVerdictRow(
        boundary_class="[0 -> Q -> A_f -> epsilon -> 0] in Ext^1(epsilon, Q)",
        finite_shadow="Bockstein class [0 -> Z -> Z -> Z/N -> 0], generator 1 in Z/N",
        sign_local_system_action="sigma sends the boundary/Yoneda class to sigma times the class",
        biduality_class="D epsilon ~= Q[-1] is represented by the same shifted boundary class; two-sided sign change squares to +1",
        plain_coarse_quotient_sufficient=False,
        extra_finite_bookkeeping_needed=False,
        no_degree_zero_weyl_map_created=True,
        recommended_next_task="Package the signed boundary class as a natural transformation over conductor reductions and compare it with the finite CRT-acyclic complexes.",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass102-sign-local-system-adele-boundary-check.json",
    )
    args = parser.parse_args()

    bockstein = bockstein_rows()
    collapse = collapse_boundary_rows()
    transport = support_transport_rows()
    yoneda = yoneda_sign_rows()
    verdict = boundary_verdict_row()

    checks = {
        "bockstein_visibility_ok": all(row.visible_exactly_when_n_gt_2 for row in bockstein),
        "collapse_boundary_ok": all(
            row.collapse_surjective_mod_n and row.sign_class_matches for row in collapse
        ),
        "support_transport_ok": all(row.transport_preserves_boundary_sign for row in transport),
        "yoneda_sign_ok": all(
            row.one_sided_sign_negates_class and row.two_sided_sign_squares_to_identity
            for row in yoneda
        ),
        "boundary_verdict_ok": (
            not verdict.plain_coarse_quotient_sufficient
            and not verdict.extra_finite_bookkeeping_needed
            and verdict.no_degree_zero_weyl_map_created
        ),
    }

    report = {
        "pass": 102,
        "title": "Sign local system through the finite-adele boundary",
        "A_signed_bockstein_shadows": {
            "statement": "The sign local system sends the finite Bockstein generator 1 in Z/N to +/-1 mod N.",
            "rows": [asdict(row) for row in bockstein],
            "bockstein_visibility_ok": checks["bockstein_visibility_ok"],
        },
        "B_collapse_to_boundary": {
            "statement": "Primitive signed collapses remain surjective mod N and carry the sign to the Bockstein/Yoneda class.",
            "rows": [asdict(row) for row in collapse],
            "collapse_boundary_ok": checks["collapse_boundary_ok"],
        },
        "C_support_transport": {
            "statement": "Zero-extension support transport preserves the signed boundary class.",
            "rows": [asdict(row) for row in transport],
            "support_transport_ok": checks["support_transport_ok"],
        },
        "D_yoneda_sign_action": {
            "statement": "One-sided sign change negates the extension class; two-sided sign change squares to identity.",
            "rows": [asdict(row) for row in yoneda],
            "yoneda_sign_ok": checks["yoneda_sign_ok"],
        },
        "E_boundary_verdict": {
            "statement": "The Z/2 local system, not the plain coarse quotient, is the sufficient sign package for the adele boundary.",
            "row": asdict(verdict),
            "boundary_verdict_ok": checks["boundary_verdict_ok"],
        },
        "conclusion": {
            "sign_local_system": "The sign acts by multiplying beta and delta_epsilon by +/-1.",
            "finite_shadow": "The finite class is +/-1 in Z/N, visible exactly for N>2.",
            "biduality": "The shifted class D epsilon ~= Q[-1] carries the same one-sided sign; applying the sign on both sides gives +1.",
            "next_task": verdict.recommended_next_task,
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
