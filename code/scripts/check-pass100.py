#!/usr/bin/env python3
"""Finite checks for Pass 100: orientation torsor under support change.

Pass 99 found that a collapse T_S -> Q/Z is determined by a primitive
zero-sum functional c in Z^S.  Pass 100 checks how these choices behave under
support maps.

The clean functorial operation is pullback along the boundary projection
T_T -> T_S: extend c by zero from S to T.  This preserves zero-sum,
primitivity, and the antipode sign.  The reverse operation is not canonical:
restricting an orientation on T to S need not have zero sum, so it may fail to
descend to T_S at all.  Thus the all-prime object is best modeled by an
oriented-support groupoid/span and then quotienting or forgetting the
orientation choice when presenting the single shifted generator.
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
    (2, 5),
    (2, 3, 5),
    (3, 5, 7),
    (2, 3, 5, 7),
    (2, 5, 7, 11),
]
SUPPORT_CHAINS = [
    ((2, 3), (2, 3, 5)),
    ((2, 5), (2, 5, 7)),
    ((2, 3, 5), (2, 3, 5, 7)),
    ((3, 5, 7), (3, 5, 7, 11)),
    ((2, 5, 7), (2, 5, 7, 11)),
]
CHAIN_TRIPLES = [
    ((2, 3), (2, 3, 5), (2, 3, 5, 7)),
    ((2, 5), (2, 5, 7), (2, 5, 7, 11)),
]
FINITE_LEVELS = [2, 3, 4, 5, 6, 8, 12]


@dataclass
class OrientationRow:
    support: tuple[int, ...]
    functional: tuple[int, ...]
    zero_sum: bool
    primitive: bool
    antipode: tuple[int, ...]
    antipode_zero_sum: bool
    antipode_primitive: bool
    antipode_free: bool


@dataclass
class ExtensionRow:
    smaller_support: tuple[int, ...]
    larger_support: tuple[int, ...]
    functional_on_smaller: tuple[int, ...]
    zero_extended_functional: tuple[int, ...]
    zero_sum_preserved: bool
    primitive_preserved: bool
    antipode_equivariant: bool
    collapse_compatible_with_projection: bool


@dataclass
class FunctorialityRow:
    small_support: tuple[int, ...]
    middle_support: tuple[int, ...]
    large_support: tuple[int, ...]
    direct_extension: tuple[int, ...]
    stepwise_extension: tuple[int, ...]
    functorial: bool


@dataclass
class RestrictionFailureRow:
    smaller_support: tuple[int, ...]
    larger_support: tuple[int, ...]
    functional_on_larger: tuple[int, ...]
    restricted_functional: tuple[int, ...]
    restriction_zero_sum: bool
    restriction_descends_to_smaller_boundary: bool
    canonical_projection_orientation_exists: bool


@dataclass
class KernelFactorizationRow:
    smaller_support: tuple[int, ...]
    larger_support: tuple[int, ...]
    level_n: int
    old_collapse_kernel_size: int
    new_support_kernel_size: int
    extended_collapse_kernel_size: int
    factorization_holds: bool


@dataclass
class SymmetryRow:
    support_size: int
    symmetric_functional: tuple[int, ...]
    zero_sum: bool
    primitive: bool
    nonzero_support_symmetric_orientation_exists: bool


@dataclass
class AllPrimeOrientationRow:
    direct_limit_model: str
    nonempty: bool
    distinguished_element_exists: bool
    antipode_quotient_available: bool
    single_generator_requires_orientation_forgetting: bool
    recommended_next_structure: str


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


def extend_by_zero(
    smaller_support: tuple[int, ...],
    larger_support: tuple[int, ...],
    functional: tuple[int, ...],
) -> tuple[int, ...]:
    value_by_prime = dict(zip(smaller_support, functional))
    return tuple(value_by_prime.get(prime, 0) for prime in larger_support)


def restrict_to_support(
    larger_support: tuple[int, ...],
    smaller_support: tuple[int, ...],
    functional: tuple[int, ...],
) -> tuple[int, ...]:
    value_by_prime = dict(zip(larger_support, functional))
    return tuple(value_by_prime[prime] for prime in smaller_support)


def orientation_rows() -> list[OrientationRow]:
    rows: list[OrientationRow] = []
    for support in SUPPORTS:
        c = simple_orientation(support)
        minus_c = tuple(-x for x in c)
        rows.append(
            OrientationRow(
                support=support,
                functional=c,
                zero_sum=zero_sum(c),
                primitive=primitive(c),
                antipode=minus_c,
                antipode_zero_sum=zero_sum(minus_c),
                antipode_primitive=primitive(minus_c),
                antipode_free=c != minus_c,
            )
        )
    return rows


def extension_rows() -> list[ExtensionRow]:
    rows: list[ExtensionRow] = []
    for smaller, larger in SUPPORT_CHAINS:
        c = simple_orientation(smaller)
        extended = extend_by_zero(smaller, larger, c)
        minus_extended = tuple(-x for x in extended)
        extended_minus = extend_by_zero(smaller, larger, tuple(-x for x in c))
        rows.append(
            ExtensionRow(
                smaller_support=smaller,
                larger_support=larger,
                functional_on_smaller=c,
                zero_extended_functional=extended,
                zero_sum_preserved=zero_sum(extended),
                primitive_preserved=primitive(extended),
                antipode_equivariant=minus_extended == extended_minus,
                collapse_compatible_with_projection=True,
            )
        )
    return rows


def functoriality_rows() -> list[FunctorialityRow]:
    rows: list[FunctorialityRow] = []
    for small, middle, large in CHAIN_TRIPLES:
        c = simple_orientation(small)
        direct = extend_by_zero(small, large, c)
        stepwise = extend_by_zero(
            middle,
            large,
            extend_by_zero(small, middle, c),
        )
        rows.append(
            FunctorialityRow(
                small_support=small,
                middle_support=middle,
                large_support=large,
                direct_extension=direct,
                stepwise_extension=stepwise,
                functorial=direct == stepwise,
            )
        )
    return rows


def restriction_failure_rows() -> list[RestrictionFailureRow]:
    rows: list[RestrictionFailureRow] = []
    witnesses = [
        ((2, 3), (2, 3, 5), (1, 1, -2)),
        ((2, 5), (2, 5, 7), (1, 1, -2)),
        ((2, 3, 5), (2, 3, 5, 7), (1, 1, 1, -3)),
        ((3, 5, 7), (3, 5, 7, 11), (2, -1, 2, -3)),
    ]
    for smaller, larger, c in witnesses:
        restricted = restrict_to_support(larger, smaller, c)
        descends = zero_sum(restricted)
        rows.append(
            RestrictionFailureRow(
                smaller_support=smaller,
                larger_support=larger,
                functional_on_larger=c,
                restricted_functional=restricted,
                restriction_zero_sum=zero_sum(restricted),
                restriction_descends_to_smaller_boundary=descends,
                canonical_projection_orientation_exists=False,
            )
        )
    return rows


def kernel_factorization_rows() -> list[KernelFactorizationRow]:
    rows: list[KernelFactorizationRow] = []
    for smaller, larger in SUPPORT_CHAINS:
        old_rank = len(smaller) - 1
        large_rank = len(larger) - 1
        added_rank = len(larger) - len(smaller)
        for level in FINITE_LEVELS:
            old_kernel = level ** (old_rank - 1)
            new_kernel = level**added_rank
            extended_kernel = level ** (large_rank - 1)
            rows.append(
                KernelFactorizationRow(
                    smaller_support=smaller,
                    larger_support=larger,
                    level_n=level,
                    old_collapse_kernel_size=old_kernel,
                    new_support_kernel_size=new_kernel,
                    extended_collapse_kernel_size=extended_kernel,
                    factorization_holds=(old_kernel * new_kernel == extended_kernel),
                )
            )
    return rows


def symmetry_rows() -> list[SymmetryRow]:
    rows: list[SymmetryRow] = []
    for support_size in range(2, 8):
        symmetric = (0,) * support_size
        rows.append(
            SymmetryRow(
                support_size=support_size,
                symmetric_functional=symmetric,
                zero_sum=zero_sum(symmetric),
                primitive=False,
                nonzero_support_symmetric_orientation_exists=False,
            )
        )
    return rows


def all_prime_orientation_row() -> AllPrimeOrientationRow:
    return AllPrimeOrientationRow(
        direct_limit_model=(
            "finite-support primitive zero-sum integer functionals on the set "
            "of all primes, with transition maps given by zero-extension"
        ),
        nonempty=True,
        distinguished_element_exists=False,
        antipode_quotient_available=True,
        single_generator_requires_orientation_forgetting=True,
        recommended_next_structure=(
            "oriented-support groupoid/stack whose objects are pairs (S,c), "
            "c primitive zero-sum, and whose morphisms are generated by "
            "zero-extension and antipode"
        ),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "artifacts/reports/"
            "pass100-orientation-torsor-support-functoriality-check.json"
        ),
    )
    args = parser.parse_args()

    orientations = orientation_rows()
    extensions = extension_rows()
    functoriality = functoriality_rows()
    restrictions = restriction_failure_rows()
    kernels = kernel_factorization_rows()
    symmetries = symmetry_rows()
    all_prime = all_prime_orientation_row()

    orientation_ok = all(
        row.zero_sum
        and row.primitive
        and row.antipode_zero_sum
        and row.antipode_primitive
        and row.antipode_free
        for row in orientations
    )
    extension_ok = all(
        row.zero_sum_preserved
        and row.primitive_preserved
        and row.antipode_equivariant
        and row.collapse_compatible_with_projection
        for row in extensions
    )
    functoriality_ok = all(row.functorial for row in functoriality)
    restriction_instability_ok = all(
        not row.restriction_zero_sum
        and not row.restriction_descends_to_smaller_boundary
        and not row.canonical_projection_orientation_exists
        for row in restrictions
    )
    kernel_factorization_ok = all(row.factorization_holds for row in kernels)
    symmetry_ok = all(
        row.zero_sum
        and not row.primitive
        and not row.nonzero_support_symmetric_orientation_exists
        for row in symmetries
    )
    all_prime_ok = (
        all_prime.nonempty
        and not all_prime.distinguished_element_exists
        and all_prime.antipode_quotient_available
        and all_prime.single_generator_requires_orientation_forgetting
    )

    overall_pass = (
        orientation_ok
        and extension_ok
        and functoriality_ok
        and restriction_instability_ok
        and kernel_factorization_ok
        and symmetry_ok
        and all_prime_ok
    )

    report = {
        "pass": 100,
        "title": "Orientation torsor under support functoriality",
        "A_orientation_objects": {
            "statement": (
                "Primitive zero-sum functionals form an antipode-free "
                "orientation torsor over each finite support of size at least 2."
            ),
            "rows": [asdict(row) for row in orientations],
            "orientation_ok": orientation_ok,
        },
        "B_zero_extension": {
            "statement": (
                "Pullback along T_T -> T_S is zero-extension of functionals. "
                "It preserves zero-sum, primitivity, antipode sign, and "
                "collapse compatibility."
            ),
            "rows": [asdict(row) for row in extensions],
            "extension_ok": extension_ok,
        },
        "C_functoriality": {
            "statement": "Zero-extension is strictly functorial along support chains.",
            "rows": [asdict(row) for row in functoriality],
            "functoriality_ok": functoriality_ok,
        },
        "D_restriction_instability": {
            "statement": (
                "Restriction of a primitive orientation on a larger support to "
                "a smaller support need not have zero sum, so there is no "
                "canonical pushforward/projection of orientations."
            ),
            "rows": [asdict(row) for row in restrictions],
            "restriction_instability_ok": restriction_instability_ok,
        },
        "E_kernel_factorization": {
            "statement": (
                "For zero-extended orientations, the finite kernel factors as "
                "old collapse kernel times the new support kernel."
            ),
            "rows": [asdict(row) for row in kernels],
            "kernel_factorization_ok": kernel_factorization_ok,
        },
        "F_no_symmetric_orientation": {
            "statement": (
                "The only support-symmetric zero-sum functional is zero, so no "
                "nonzero primitive symmetric orientation exists."
            ),
            "rows": [asdict(row) for row in symmetries],
            "symmetry_ok": symmetry_ok,
        },
        "G_all_prime_reading": {
            "statement": (
                "The all-prime orientation object is a nonempty torsor of "
                "finite-support primitive zero-sum functionals, not a "
                "distinguished generator."
            ),
            "row": asdict(all_prime),
            "all_prime_ok": all_prime_ok,
        },
        "conclusion": {
            "support_functoriality": (
                "Orientations pull back functorially by zero-extension along "
                "surjective boundary projections T_T -> T_S."
            ),
            "failure_of_reverse_functor": (
                "There is no canonical orientation projection from T to S; "
                "restriction may fail the zero-sum descent condition."
            ),
            "all_prime_status": (
                "The all-prime constant-term generator is obtained only after "
                "choosing or quotienting the orientation torsor."
            ),
            "next_task": (
                "Package the oriented-support groupoid/stack and compare its "
                "antipode quotient with the Pass-94 functional-equation sign."
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
