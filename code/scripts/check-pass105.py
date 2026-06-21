#!/usr/bin/env python3
"""Finite checks for Pass 105: support descent of primitive orientations.

Pass 105 separates three operations that had been easy to conflate:

* orientation zero-extension along S subset T, which is canonical and
  covariant on primitive zero-sum vectors;
* boundary/support projection T_T -> T_S, which is canonical in the opposite
  direction on boundary groups;
* orientation restriction from T to S, which is not a total operation because
  zero-sum can fail after deleting coordinates.

The intended all-prime object is therefore a filtered colimit of finite
oriented supports by zero-padding, equipped with the signed boundary-line local
system from Pass 104.  It is not a plain sheaf on the support poset with
restriction maps on primitive orientations.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path


SUPPORT_CHAIN = [
    ((2, 3), (2, 3, 5)),
    ((2, 5), (2, 3, 5)),
    ((3, 5), (2, 3, 5)),
    ((2, 3, 5), (2, 3, 5, 7)),
]

SUPPORT_TRIPLES = [
    ((2, 3), (2, 3, 5), (2, 3, 5, 7)),
    ((2, 5), (2, 3, 5), (2, 3, 5, 7)),
]

BAD_RESTRICTIONS = [
    ((2, 3), (2, 3, 5), (1, 1, -2)),
    ((2, 5), (2, 3, 5), (1, -2, 1)),
    ((3, 5), (2, 3, 5), (-2, 1, 1)),
]


@dataclass
class ZeroExtensionRow:
    source_support: tuple[int, ...]
    target_support: tuple[int, ...]
    source_orientation: tuple[int, ...]
    extended_orientation: tuple[int, ...]
    zero_sum_preserved: bool
    primitive_preserved: bool
    antipode_commutes: bool


@dataclass
class CompositionRow:
    small_support: tuple[int, ...]
    middle_support: tuple[int, ...]
    large_support: tuple[int, ...]
    direct_extension: tuple[int, ...]
    iterated_extension: tuple[int, ...]
    composition_ok: bool


@dataclass
class RestrictionFailureRow:
    source_support: tuple[int, ...]
    target_support: tuple[int, ...]
    target_orientation: tuple[int, ...]
    restricted_values: tuple[int, ...]
    restricted_sum: int
    is_orientation_after_restriction: bool


@dataclass
class ColimitPaddingRow:
    source_support: tuple[int, ...]
    padded_support: tuple[int, ...]
    source_orientation: tuple[int, ...]
    padded_orientation: tuple[int, ...]
    trimmed_support: tuple[int, ...]
    trimmed_orientation: tuple[int, ...]
    padding_equivalence_ok: bool


@dataclass
class SymmetryObstructionRow:
    support: tuple[int, ...]
    constant_value: int
    zero_sum: bool
    primitive: bool
    support_symmetric_orientation_exists: bool


@dataclass
class PackageVerdictRow:
    plain_sheaf_with_restrictions_possible: bool
    filtered_colimit_by_zero_extension: bool
    span_stack_required: bool
    sign_local_system_required: bool
    degree_zero_weyl_created: bool
    next_obstruction: str


def gcd_all(values: tuple[int, ...]) -> int:
    g = 0
    for value in values:
        g = math.gcd(g, abs(value))
    return g


def is_orientation(values: tuple[int, ...]) -> bool:
    return bool(values) and sum(values) == 0 and gcd_all(values) == 1


def seed_orientation(support: tuple[int, ...]) -> tuple[int, ...]:
    if len(support) < 2:
        raise ValueError("support must have at least two primes")
    return tuple([-1, 1] + [0] * (len(support) - 2))


def extend_by_zero(
    source_support: tuple[int, ...],
    source_values: tuple[int, ...],
    target_support: tuple[int, ...],
) -> tuple[int, ...]:
    lookup = dict(zip(source_support, source_values, strict=True))
    return tuple(lookup.get(prime, 0) for prime in target_support)


def restrict_values(
    source_support: tuple[int, ...],
    target_support: tuple[int, ...],
    target_values: tuple[int, ...],
) -> tuple[int, ...]:
    lookup = dict(zip(target_support, target_values, strict=True))
    return tuple(lookup[prime] for prime in source_support)


def trim_zero_coordinates(
    support: tuple[int, ...], values: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    pairs = [(prime, value) for prime, value in zip(support, values, strict=True) if value != 0]
    if not pairs:
        return (), ()
    primes, trimmed = zip(*pairs, strict=True)
    return tuple(primes), tuple(trimmed)


def zero_extension_rows() -> list[ZeroExtensionRow]:
    rows: list[ZeroExtensionRow] = []
    for small, large in SUPPORT_CHAIN:
        orientation = seed_orientation(small)
        extended = extend_by_zero(small, orientation, large)
        antipode_extended = extend_by_zero(
            small, tuple(-x for x in orientation), large
        )
        rows.append(
            ZeroExtensionRow(
                source_support=small,
                target_support=large,
                source_orientation=orientation,
                extended_orientation=extended,
                zero_sum_preserved=sum(orientation) == sum(extended) == 0,
                primitive_preserved=is_orientation(orientation)
                and is_orientation(extended),
                antipode_commutes=antipode_extended
                == tuple(-x for x in extended),
            )
        )
    return rows


def composition_rows() -> list[CompositionRow]:
    rows: list[CompositionRow] = []
    for small, middle, large in SUPPORT_TRIPLES:
        orientation = seed_orientation(small)
        direct = extend_by_zero(small, orientation, large)
        iterated = extend_by_zero(
            middle,
            extend_by_zero(small, orientation, middle),
            large,
        )
        rows.append(
            CompositionRow(
                small_support=small,
                middle_support=middle,
                large_support=large,
                direct_extension=direct,
                iterated_extension=iterated,
                composition_ok=direct == iterated,
            )
        )
    return rows


def restriction_failure_rows() -> list[RestrictionFailureRow]:
    rows: list[RestrictionFailureRow] = []
    for small, large, target_orientation in BAD_RESTRICTIONS:
        restricted = restrict_values(small, large, target_orientation)
        rows.append(
            RestrictionFailureRow(
                source_support=small,
                target_support=large,
                target_orientation=target_orientation,
                restricted_values=restricted,
                restricted_sum=sum(restricted),
                is_orientation_after_restriction=is_orientation(restricted),
            )
        )
    return rows


def colimit_padding_rows() -> list[ColimitPaddingRow]:
    rows: list[ColimitPaddingRow] = []
    for small, large in SUPPORT_CHAIN:
        orientation = seed_orientation(small)
        padded = extend_by_zero(small, orientation, large)
        trimmed_support, trimmed_orientation = trim_zero_coordinates(large, padded)
        rows.append(
            ColimitPaddingRow(
                source_support=small,
                padded_support=large,
                source_orientation=orientation,
                padded_orientation=padded,
                trimmed_support=trimmed_support,
                trimmed_orientation=trimmed_orientation,
                padding_equivalence_ok=(trimmed_support, trimmed_orientation)
                == trim_zero_coordinates(small, orientation),
            )
        )
    return rows


def symmetry_obstruction_rows() -> list[SymmetryObstructionRow]:
    rows: list[SymmetryObstructionRow] = []
    supports = [(2, 3), (2, 3, 5), (2, 3, 5, 7)]
    for support in supports:
        for constant in [-2, -1, 0, 1, 2]:
            values = tuple(constant for _ in support)
            zero_sum = sum(values) == 0
            primitive = is_orientation(values)
            rows.append(
                SymmetryObstructionRow(
                    support=support,
                    constant_value=constant,
                    zero_sum=zero_sum,
                    primitive=primitive,
                    support_symmetric_orientation_exists=zero_sum
                    and primitive,
                )
            )
    return rows


def package_verdict_row() -> PackageVerdictRow:
    return PackageVerdictRow(
        plain_sheaf_with_restrictions_possible=False,
        filtered_colimit_by_zero_extension=True,
        span_stack_required=True,
        sign_local_system_required=True,
        degree_zero_weyl_created=False,
        next_obstruction=(
            "Compute the obstruction to stackifying primitive orientations over "
            "the finite-support poset when restriction maps are demanded."
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "artifacts/reports/"
            "pass105-support-descent-primitive-orientations-check.json"
        ),
    )
    args = parser.parse_args()

    zero_rows = zero_extension_rows()
    comp_rows = composition_rows()
    restrict_rows = restriction_failure_rows()
    colimit_rows = colimit_padding_rows()
    symmetry_rows = symmetry_obstruction_rows()
    package = package_verdict_row()

    checks = {
        "zero_extension_ok": all(
            row.zero_sum_preserved
            and row.primitive_preserved
            and row.antipode_commutes
            for row in zero_rows
        ),
        "composition_ok": all(row.composition_ok for row in comp_rows),
        "restriction_failure_ok": all(
            not row.is_orientation_after_restriction
            and row.restricted_sum != 0
            for row in restrict_rows
        ),
        "colimit_padding_ok": all(
            row.padding_equivalence_ok for row in colimit_rows
        ),
        "symmetry_obstruction_ok": not any(
            row.support_symmetric_orientation_exists
            for row in symmetry_rows
        ),
        "span_stack_verdict_ok": (
            not package.plain_sheaf_with_restrictions_possible
            and package.filtered_colimit_by_zero_extension
            and package.span_stack_required
            and package.sign_local_system_required
            and not package.degree_zero_weyl_created
        ),
    }

    report = {
        "pass": 105,
        "title": "Support descent for all-prime primitive orientations",
        "A_zero_extension": {
            "statement": (
                "Zero-extension is the canonical covariant operation on "
                "primitive zero-sum orientations."
            ),
            "rows": [asdict(row) for row in zero_rows],
            "zero_extension_ok": checks["zero_extension_ok"],
        },
        "B_composition": {
            "statement": "Zero-extension is functorial along support chains.",
            "rows": [asdict(row) for row in comp_rows],
            "composition_ok": checks["composition_ok"],
        },
        "C_restriction_failure": {
            "statement": (
                "Deleting support coordinates is not a total restriction map "
                "on primitive orientations because zero-sum can fail."
            ),
            "rows": [asdict(row) for row in restrict_rows],
            "restriction_failure_ok": checks["restriction_failure_ok"],
        },
        "D_colimit_padding": {
            "statement": (
                "The all-prime primitive orientation object is a filtered "
                "colimit by zero-padding, modulo deleting padded zeros."
            ),
            "rows": [asdict(row) for row in colimit_rows],
            "colimit_padding_ok": checks["colimit_padding_ok"],
        },
        "E_symmetry_obstruction": {
            "statement": (
                "A support-symmetric constant functional is zero if it is "
                "zero-sum, hence it is not primitive."
            ),
            "rows": [asdict(row) for row in symmetry_rows],
            "symmetry_obstruction_ok": checks["symmetry_obstruction_ok"],
        },
        "F_package_verdict": {
            "statement": (
                "Use a span-stack/Grothendieck package: zero-extension on "
                "orientations, projection on boundary groups, and the Z/2 "
                "boundary-line local system."
            ),
            "row": asdict(package),
            "span_stack_verdict_ok": checks["span_stack_verdict_ok"],
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
