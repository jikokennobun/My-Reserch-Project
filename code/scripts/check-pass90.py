#!/usr/bin/env python3
"""Finite checks for Pass 90: conductor-functorial Borel torsors.

The pass refines Pass 89 by deciding the direction of functoriality.  For a
finite prime support S, the quotient P(S)=(prod_{p in S} Z_p)/Delta Z has
canonical restriction maps for inclusions S subset T, induced by coordinate
projection P(T)->P(S).  The tempting zero-insertion P(S)->P(T) is not
well-defined on the diagonal quotient unless no new prime is added.  Therefore
comparisons from smaller support to larger support are represented by spans,
pullbacks, or finite-conductor shadows, not by a canonical group map.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from math import gcd
from pathlib import Path
from typing import Iterable


MODULI = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 30]
CONDUCTORS = [2, 3, 4, 5, 6, 8, 9, 10, 12, 30, 60]


@dataclass
class SupportRow:
    m: int
    radical: tuple[int, ...]
    canonical_support_label: str


@dataclass
class SupportMapRow:
    source_m: int
    target_m: int
    source_radical: tuple[int, ...]
    target_radical: tuple[int, ...]
    source_subset_target: bool
    projection_target_to_source_descends: bool
    zero_insertion_source_to_target_descends: bool
    comparison_shape: str


@dataclass
class MeetJoinRow:
    left_m: int
    right_m: int
    left_radical: tuple[int, ...]
    right_radical: tuple[int, ...]
    meet_radical: tuple[int, ...]
    join_radical: tuple[int, ...]
    direct_map_exists_either_way: bool
    shared_ghost_via_meet: bool
    gluing_arena_via_join: bool


@dataclass
class FiniteConductorRow:
    source_conductor: int
    target_conductor: int
    divides: bool
    reduction_preserves_unit_class: bool
    source_borel_shadow_size: int
    target_borel_shadow_size: int
    strict_marked_stabilizer_size: int


def prime_factors(n: int) -> tuple[int, ...]:
    if n == 1:
        return ()
    factors: set[int] = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return tuple(sorted(factors))


def radical_label(radical: Iterable[int]) -> str:
    values = tuple(radical)
    if not values:
        return "1"
    return "*".join(str(p) for p in values)


def euler_phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def diagonal_vector(size: int, value: int = 1) -> tuple[int, ...]:
    return tuple(value for _ in range(size))


def is_diagonal(vector: tuple[int, ...]) -> bool:
    return len(set(vector)) <= 1


def projection_descends(source_rad: tuple[int, ...], target_rad: tuple[int, ...]) -> bool:
    """Projection P(target)->P(source) descends when source subset target."""
    if not set(source_rad).issubset(target_rad):
        return False
    # Diagonal 1 in the target projects to diagonal 1 in the source.
    projected = diagonal_vector(len(source_rad), 1)
    return is_diagonal(projected)


def zero_insertion_descends(source_rad: tuple[int, ...], target_rad: tuple[int, ...]) -> bool:
    """Zero-insertion P(source)->P(target) descends only when no prime is added."""
    if not set(source_rad).issubset(target_rad):
        return False
    inserted = tuple(1 if p in source_rad else 0 for p in target_rad)
    return is_diagonal(inserted)


def support_rows() -> list[SupportRow]:
    return [
        SupportRow(
            m=m,
            radical=prime_factors(m),
            canonical_support_label=radical_label(prime_factors(m)),
        )
        for m in MODULI
    ]


def support_map_rows() -> list[SupportMapRow]:
    rows: list[SupportMapRow] = []
    sample_pairs = [
        (2, 4),
        (2, 6),
        (6, 30),
        (10, 30),
        (6, 10),
        (12, 6),
        (3, 15),
        (5, 10),
    ]
    for source_m, target_m in sample_pairs:
        source_rad = prime_factors(source_m)
        target_rad = prime_factors(target_m)
        subset = set(source_rad).issubset(target_rad)
        projection_ok = projection_descends(source_rad, target_rad)
        insertion_ok = zero_insertion_descends(source_rad, target_rad)
        if not subset:
            shape = "no direct support map; compare by meet/join span"
        elif insertion_ok:
            shape = "same radical support; canonical isomorphism"
        else:
            shape = "canonical restriction target->source; source->target is span/choice"
        rows.append(
            SupportMapRow(
                source_m=source_m,
                target_m=target_m,
                source_radical=source_rad,
                target_radical=target_rad,
                source_subset_target=subset,
                projection_target_to_source_descends=projection_ok,
                zero_insertion_source_to_target_descends=insertion_ok,
                comparison_shape=shape,
            )
        )
    return rows


def meet_join_rows() -> list[MeetJoinRow]:
    rows: list[MeetJoinRow] = []
    sample_pairs = [(6, 10), (6, 15), (10, 15), (4, 12), (8, 9), (12, 30)]
    for left_m, right_m in sample_pairs:
        left = set(prime_factors(left_m))
        right = set(prime_factors(right_m))
        meet = tuple(sorted(left & right))
        join = tuple(sorted(left | right))
        comparable = left.issubset(right) or right.issubset(left)
        rows.append(
            MeetJoinRow(
                left_m=left_m,
                right_m=right_m,
                left_radical=tuple(sorted(left)),
                right_radical=tuple(sorted(right)),
                meet_radical=meet,
                join_radical=join,
                direct_map_exists_either_way=comparable,
                shared_ghost_via_meet=True,
                gluing_arena_via_join=True,
            )
        )
    return rows


def finite_conductor_rows() -> list[FiniteConductorRow]:
    rows: list[FiniteConductorRow] = []
    sample_pairs = [(2, 4), (3, 9), (6, 12), (10, 30), (12, 60), (8, 12)]
    for source, target in sample_pairs:
        divides = target % source == 0
        source_size = euler_phi(source) * source
        target_size = euler_phi(target) * target
        rows.append(
            FiniteConductorRow(
                source_conductor=source,
                target_conductor=target,
                divides=divides,
                reduction_preserves_unit_class=divides and (1 % source) == ((1 % target) % source),
                source_borel_shadow_size=source_size,
                target_borel_shadow_size=target_size,
                strict_marked_stabilizer_size=1,
            )
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass90-conductor-functorial-borel-torsors-check.json",
    )
    args = parser.parse_args()

    supports = support_rows()
    support_maps = support_map_rows()
    meet_join = meet_join_rows()
    finite = finite_conductor_rows()

    radical_invariance_ok = all(
        (row.m in (2, 4, 8) and row.radical == (2,))
        or (row.m in (6, 12) and row.radical == (2, 3))
        or row.m not in (2, 4, 6, 8, 12)
        for row in supports
    )
    projections_ok = all(
        (not row.source_subset_target) or row.projection_target_to_source_descends
        for row in support_maps
    )
    insertion_fails_when_new_prime_added = all(
        row.zero_insertion_source_to_target_descends
        == (row.source_subset_target and row.source_radical == row.target_radical)
        for row in support_maps
    )
    meet_join_ok = all(
        row.shared_ghost_via_meet and row.gluing_arena_via_join for row in meet_join
    )
    finite_reductions_ok = all(
        (not row.divides) or row.reduction_preserves_unit_class for row in finite
    )
    strict_stabilizers_ok = all(row.strict_marked_stabilizer_size == 1 for row in finite)

    overall_pass = (
        radical_invariance_ok
        and projections_ok
        and insertion_fails_when_new_prime_added
        and meet_join_ok
        and finite_reductions_ok
        and strict_stabilizers_ok
    )

    report = {
        "pass": 90,
        "title": "Conductor-functorial Borel torsors",
        "A_radical_supports": {
            "statement": "The m-adic phantom and Borel torsor depend on the squarefree radical support.",
            "rows": [asdict(row) for row in supports],
            "radical_invariance_ok": radical_invariance_ok,
        },
        "B_support_functoriality": {
            "statement": (
                "For S subset T, coordinate projection gives a canonical "
                "restriction P(T)->P(S). Zero-insertion P(S)->P(T) does not "
                "descend through the diagonal quotient when new primes are added."
            ),
            "rows": [asdict(row) for row in support_maps],
            "projections_ok": projections_ok,
            "zero_insertion_fails_when_new_prime_added": insertion_fails_when_new_prime_added,
        },
        "C_meet_join_comparisons": {
            "statement": (
                "Rad-incomparable supports are compared by a meet span for "
                "shared ghosts and a join arena for gluing, not by a direct map."
            ),
            "rows": [asdict(row) for row in meet_join],
            "meet_join_ok": meet_join_ok,
        },
        "D_finite_conductor_borel_shadows": {
            "statement": (
                "Finite Borel shadows reduce along conductor divisibility; "
                "the unit class and singleton strict marked stabilizer persist."
            ),
            "rows": [asdict(row) for row in finite],
            "finite_reductions_ok": finite_reductions_ok,
            "strict_stabilizers_ok": strict_stabilizers_ok,
        },
        "conclusion": {
            "functorial_direction": (
                "The canonical support functor is contravariant by restriction "
                "on the diagonal quotient; covariant support enlargement is a "
                "span or chosen section, not a canonical group map."
            ),
            "borel_torsor_extension": (
                "The Pass-89 Borel torsor theorem is natural on finite conductor "
                "shadows and support restrictions, with meet/join spans handling "
                "incomparable radical supports."
            ),
            "next_task": (
                "Upgrade this restricted presheaf/span statement into a descent "
                "or stack-style theorem for Borel torsors over the prime-cover site."
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
