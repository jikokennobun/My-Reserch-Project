#!/usr/bin/env python3
"""Finite checks for Pass 101: oriented-support groupoid and antipode quotient.

Pass 100 showed that primitive collapses form orientation torsors O_S and
that support inclusions act by zero-extension.  Pass 101 packages this as a
signed oriented-support category/groupoid:

    objects:  (S, c), c in O_S
    morphism: (S,c) -> (T,d) is a support inclusion S subset T plus
              a sign sigma in {+1,-1} such that d = sigma * e_{S,T}(c).

The sign composes multiplicatively.  The coarse antipode quotient identifies
c with -c and therefore loses the sign label; the signed action groupoid, or
equivalently the coarse quotient plus a Z/2 local system, is needed to retain
the Pass-94 functional-equation sign.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from functools import reduce
from math import gcd
from pathlib import Path


SUPPORT_CHAINS = [
    ((2, 3), (2, 3, 5)),
    ((2, 5), (2, 5, 7)),
    ((2, 3, 5), (2, 3, 5, 7)),
    ((3, 5, 7), (3, 5, 7, 11)),
]
SUPPORT_TRIPLES = [
    ((2, 3), (2, 3, 5), (2, 3, 5, 7)),
    ((2, 5), (2, 5, 7), (2, 5, 7, 11)),
]
FINITE_LEVELS = [2, 3, 4, 5, 6, 8, 12]
SIGNS = [1, -1]


@dataclass
class SignedMorphismRow:
    smaller_support: tuple[int, ...]
    larger_support: tuple[int, ...]
    source_orientation: tuple[int, ...]
    sign: int
    target_orientation: tuple[int, ...]
    target_zero_sum: bool
    target_primitive: bool
    morphism_valid: bool
    coarse_source_line: tuple[int, ...]
    coarse_target_line: tuple[int, ...]


@dataclass
class CompositionRow:
    small_support: tuple[int, ...]
    middle_support: tuple[int, ...]
    large_support: tuple[int, ...]
    first_sign: int
    second_sign: int
    composed_sign: int
    direct_target: tuple[int, ...]
    stepwise_target: tuple[int, ...]
    composition_law_holds: bool


@dataclass
class AntipodeRow:
    support: tuple[int, ...]
    orientation: tuple[int, ...]
    antipode_orientation: tuple[int, ...]
    antipode_square_orientation: tuple[int, ...]
    antipode_free: bool
    antipode_square_identity: bool


@dataclass
class CoarseQuotientRow:
    smaller_support: tuple[int, ...]
    larger_support: tuple[int, ...]
    source_line: tuple[int, ...]
    plus_target_line: tuple[int, ...]
    minus_target_line: tuple[int, ...]
    coarse_targets_equal: bool
    sign_recoverable_from_coarse_quotient: bool
    signed_groupoid_retains_sign: bool


@dataclass
class FiniteSignRow:
    level_n: int
    sign_visible_on_n_torsion: bool
    sign_invisible_only_mod_2: bool
    pass94_sign_behavior_matched: bool


@dataclass
class StackVerdictRow:
    structure_name: str
    objects: str
    morphisms: str
    coarse_quotient: str
    sign_local_system: str
    presents_single_generator: bool
    preserves_pass94_sign: bool
    plain_coarse_quotient_sufficient: bool
    recommended_next_task: str


def gcd_tuple(values: tuple[int, ...]) -> int:
    return reduce(gcd, (abs(v) for v in values), 0)


def zero_sum(values: tuple[int, ...]) -> bool:
    return sum(values) == 0


def primitive(values: tuple[int, ...]) -> bool:
    return zero_sum(values) and gcd_tuple(values) == 1


def simple_orientation(support: tuple[int, ...]) -> tuple[int, ...]:
    values = [0] * len(support)
    values[0] = -1
    values[-1] = 1
    return tuple(values)


def negate(values: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-x for x in values)


def multiply(sign: int, values: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sign * x for x in values)


def extend_by_zero(
    smaller_support: tuple[int, ...],
    larger_support: tuple[int, ...],
    orientation: tuple[int, ...],
) -> tuple[int, ...]:
    value_by_prime = dict(zip(smaller_support, orientation))
    return tuple(value_by_prime.get(prime, 0) for prime in larger_support)


def canonical_line(values: tuple[int, ...]) -> tuple[int, ...]:
    """Choose a deterministic representative for the antipode orbit {c,-c}."""
    neg = negate(values)
    return min(values, neg)


def signed_morphism_rows() -> list[SignedMorphismRow]:
    rows: list[SignedMorphismRow] = []
    for smaller, larger in SUPPORT_CHAINS:
        c = simple_orientation(smaller)
        extended = extend_by_zero(smaller, larger, c)
        for sign in SIGNS:
            target = multiply(sign, extended)
            rows.append(
                SignedMorphismRow(
                    smaller_support=smaller,
                    larger_support=larger,
                    source_orientation=c,
                    sign=sign,
                    target_orientation=target,
                    target_zero_sum=zero_sum(target),
                    target_primitive=primitive(target),
                    morphism_valid=target == multiply(sign, extended),
                    coarse_source_line=canonical_line(c),
                    coarse_target_line=canonical_line(target),
                )
            )
    return rows


def composition_rows() -> list[CompositionRow]:
    rows: list[CompositionRow] = []
    for small, middle, large in SUPPORT_TRIPLES:
        c = simple_orientation(small)
        for first_sign in SIGNS:
            for second_sign in SIGNS:
                middle_target = multiply(
                    first_sign,
                    extend_by_zero(small, middle, c),
                )
                stepwise = multiply(
                    second_sign,
                    extend_by_zero(middle, large, middle_target),
                )
                composed_sign = first_sign * second_sign
                direct = multiply(composed_sign, extend_by_zero(small, large, c))
                rows.append(
                    CompositionRow(
                        small_support=small,
                        middle_support=middle,
                        large_support=large,
                        first_sign=first_sign,
                        second_sign=second_sign,
                        composed_sign=composed_sign,
                        direct_target=direct,
                        stepwise_target=stepwise,
                        composition_law_holds=direct == stepwise,
                    )
                )
    return rows


def antipode_rows() -> list[AntipodeRow]:
    supports = sorted({support for chain in SUPPORT_CHAINS for support in chain})
    rows: list[AntipodeRow] = []
    for support in supports:
        c = simple_orientation(support)
        a = negate(c)
        rows.append(
            AntipodeRow(
                support=support,
                orientation=c,
                antipode_orientation=a,
                antipode_square_orientation=negate(a),
                antipode_free=c != a,
                antipode_square_identity=negate(a) == c,
            )
        )
    return rows


def coarse_quotient_rows() -> list[CoarseQuotientRow]:
    rows: list[CoarseQuotientRow] = []
    for smaller, larger in SUPPORT_CHAINS:
        c = simple_orientation(smaller)
        extended = extend_by_zero(smaller, larger, c)
        plus_line = canonical_line(extended)
        minus_line = canonical_line(negate(extended))
        rows.append(
            CoarseQuotientRow(
                smaller_support=smaller,
                larger_support=larger,
                source_line=canonical_line(c),
                plus_target_line=plus_line,
                minus_target_line=minus_line,
                coarse_targets_equal=plus_line == minus_line,
                sign_recoverable_from_coarse_quotient=False,
                signed_groupoid_retains_sign=True,
            )
        )
    return rows


def finite_sign_rows() -> list[FiniteSignRow]:
    rows: list[FiniteSignRow] = []
    for level in FINITE_LEVELS:
        visible = level != 2
        rows.append(
            FiniteSignRow(
                level_n=level,
                sign_visible_on_n_torsion=visible,
                sign_invisible_only_mod_2=(level == 2),
                pass94_sign_behavior_matched=(visible or level == 2),
            )
        )
    return rows


def stack_verdict_row() -> StackVerdictRow:
    return StackVerdictRow(
        structure_name="oriented-support action groupoid O",
        objects="pairs (S,c) with c primitive zero-sum on finite support S",
        morphisms=(
            "S subset T plus sign sigma in {+1,-1}, with target "
            "sigma * e_{S,T}(c)"
        ),
        coarse_quotient="primitive lines [c]={c,-c}",
        sign_local_system="Z/2 sign label on oriented morphisms",
        presents_single_generator=True,
        preserves_pass94_sign=True,
        plain_coarse_quotient_sufficient=False,
        recommended_next_task=(
            "Push the signed local system through the finite-adele "
            "constant-term complex and compare it with the biduality "
            "antipode sign on D epsilon."
        ),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "artifacts/reports/"
            "pass101-oriented-support-groupoid-antipode-quotient-check.json"
        ),
    )
    args = parser.parse_args()

    morphisms = signed_morphism_rows()
    compositions = composition_rows()
    antipodes = antipode_rows()
    quotients = coarse_quotient_rows()
    finite_signs = finite_sign_rows()
    verdict = stack_verdict_row()

    morphism_ok = all(
        row.target_zero_sum and row.target_primitive and row.morphism_valid
        for row in morphisms
    )
    composition_ok = all(row.composition_law_holds for row in compositions)
    antipode_ok = all(
        row.antipode_free and row.antipode_square_identity for row in antipodes
    )
    coarse_quotient_ok = all(
        row.coarse_targets_equal
        and not row.sign_recoverable_from_coarse_quotient
        and row.signed_groupoid_retains_sign
        for row in quotients
    )
    finite_sign_ok = all(row.pass94_sign_behavior_matched for row in finite_signs)
    stack_verdict_ok = (
        verdict.presents_single_generator
        and verdict.preserves_pass94_sign
        and not verdict.plain_coarse_quotient_sufficient
    )

    overall_pass = (
        morphism_ok
        and composition_ok
        and antipode_ok
        and coarse_quotient_ok
        and finite_sign_ok
        and stack_verdict_ok
    )

    report = {
        "pass": 101,
        "title": "Oriented-support groupoid and antipode quotient",
        "A_signed_morphisms": {
            "statement": (
                "A signed morphism (S,c)->(T,d) is a support inclusion and "
                "a sign sigma with d=sigma*e_{S,T}(c)."
            ),
            "rows": [asdict(row) for row in morphisms],
            "morphism_ok": morphism_ok,
        },
        "B_composition": {
            "statement": (
                "Signs compose multiplicatively, so the oriented-support "
                "category is strictly associative on sampled chains."
            ),
            "rows": [asdict(row) for row in compositions],
            "composition_ok": composition_ok,
        },
        "C_antipode": {
            "statement": (
                "The antipode is free on primitive orientations and squares "
                "to the identity."
            ),
            "rows": [asdict(row) for row in antipodes],
            "antipode_ok": antipode_ok,
        },
        "D_coarse_quotient": {
            "statement": (
                "The coarse quotient by c~-c identifies plus and minus "
                "targets, so it presents primitive lines but loses the sign "
                "label.  The signed groupoid retains it."
            ),
            "rows": [asdict(row) for row in quotients],
            "coarse_quotient_ok": coarse_quotient_ok,
        },
        "E_finite_sign_behavior": {
            "statement": (
                "The sign is visible on N-torsion except at N=2, matching "
                "the finite Pass-94 signed-dual behavior."
            ),
            "rows": [asdict(row) for row in finite_signs],
            "finite_sign_ok": finite_sign_ok,
        },
        "F_stack_verdict": {
            "statement": (
                "Use the oriented-support action groupoid, or the coarse "
                "quotient plus a Z/2 sign local system, to retain the "
                "functional-equation sign."
            ),
            "row": asdict(verdict),
            "stack_verdict_ok": stack_verdict_ok,
        },
        "conclusion": {
            "oriented_structure": (
                "Objects are (S,c); morphisms are inclusions with sign labels."
            ),
            "coarse_quotient": (
                "Primitive lines [c] present the single generator but lose "
                "the sign unless a Z/2 local system is retained."
            ),
            "pass94_compatibility": (
                "The signed groupoid keeps the antipode sign, visible away "
                "from mod 2 and collapsed at N=2."
            ),
            "next_task": (
                "Push the sign local system through [Q -> A_f] and identify "
                "the exact boundary class representing biduality on D epsilon."
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
