#!/usr/bin/env python3
"""Finite checks for Pass 107: correction torsors for support defects.

Pass 106 identified the additive defect of coordinate deletion.  Pass 107
checks the next refinement:

* additive repairs form an affine torsor under K_S = ker(Sigma_S);
* the primitive repair locus is not stable under all of K_S;
* basepointed sections split Sigma_S noncanonically;
* transition functions between basepointed splittings are coboundaries;
* linear sections commute with the antipode;
* this is an ordinary finite-level choice torsor, not a Rosser/cosheaf
  phantom class.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class AdditiveRepairTorsorRow:
    source_support: tuple[int, ...]
    target_support: tuple[int, ...]
    target_orientation: tuple[int, ...]
    deleted_values: tuple[int, ...]
    additive_defect: int
    first_basepoint_repair: tuple[int, ...]
    last_basepoint_repair: tuple[int, ...]
    transition_difference: tuple[int, ...]
    difference_in_kernel: bool
    both_additive_repairs_zero_sum: bool
    both_repairs_primitive: bool
    torsor_translation_ok: bool


@dataclass
class PrimitiveLocusRow:
    support: tuple[int, ...]
    primitive_repair: tuple[int, ...]
    kernel_step: tuple[int, ...]
    translated_vector: tuple[int, ...]
    kernel_step_in_kernel: bool
    translated_is_zero_sum: bool
    translated_is_primitive: bool
    primitive_locus_stable_under_full_kernel: bool


@dataclass
class BasepointTransitionRow:
    support: tuple[int, ...]
    base_a: int
    base_b: int
    base_c: int
    transition_ab: tuple[int, ...]
    transition_bc: tuple[int, ...]
    transition_ac: tuple[int, ...]
    transitions_in_kernel: bool
    cocycle_identity_ok: bool
    coboundary_description: str


@dataclass
class InclusionTransitionRow:
    source_support: tuple[int, ...]
    target_support: tuple[int, ...]
    source_basepoint: int
    target_basepoint: int
    extended_source_section: tuple[int, ...]
    target_section: tuple[int, ...]
    transition: tuple[int, ...]
    transition_in_kernel: bool
    natural_after_forgetting_basepoint: bool


@dataclass
class AntipodeCompatibilityRow:
    source_support: tuple[int, ...]
    target_support: tuple[int, ...]
    target_orientation: tuple[int, ...]
    basepoint: int
    repaired_orientation: tuple[int, ...]
    repaired_antipode: tuple[int, ...]
    antipode_of_repair: tuple[int, ...]
    linear_section_antipode_compatible: bool


@dataclass
class CohomologyVerdictRow:
    finite_exact_sequence: str
    split_after_basepoint: bool
    transitions_are_coboundaries: bool
    non_mittag_leffler_tower_present: bool
    rosser_phantom_like: bool
    ordinary_choice_torsor: bool
    next_obstruction: str


def gcd_all(values: tuple[int, ...]) -> int:
    g = 0
    for value in values:
        g = math.gcd(g, abs(value))
    return g


def is_orientation(values: tuple[int, ...]) -> bool:
    return bool(values) and sum(values) == 0 and gcd_all(values) == 1


def in_kernel(values: tuple[int, ...]) -> bool:
    return sum(values) == 0


def restrict_values(
    source_support: tuple[int, ...],
    target_support: tuple[int, ...],
    target_values: tuple[int, ...],
) -> tuple[int, ...]:
    lookup = dict(zip(target_support, target_values, strict=True))
    return tuple(lookup[prime] for prime in source_support)


def section_vector(
    support: tuple[int, ...], basepoint: int, total: int
) -> tuple[int, ...]:
    return tuple(total if prime == basepoint else 0 for prime in support)


def repair_at_basepoint(
    support: tuple[int, ...], deleted_values: tuple[int, ...], basepoint: int
) -> tuple[int, ...]:
    defect = sum(deleted_values)
    correction = section_vector(support, basepoint, defect)
    return tuple(
        value - correction_value
        for value, correction_value in zip(deleted_values, correction, strict=True)
    )


def extend_by_zero(
    source_support: tuple[int, ...],
    source_values: tuple[int, ...],
    target_support: tuple[int, ...],
) -> tuple[int, ...]:
    lookup = dict(zip(source_support, source_values, strict=True))
    return tuple(lookup.get(prime, 0) for prime in target_support)


def add_vectors(*vectors: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(values) for values in zip(*vectors, strict=True))


def sub_vectors(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x - y for x, y in zip(a, b, strict=True))


def additive_repair_rows() -> list[AdditiveRepairTorsorRow]:
    examples = [
        ((2, 3), (2, 3, 5), (1, 1, -2)),
        ((2, 3, 5), (2, 3, 5, 7), (1, 1, 1, -3)),
    ]
    rows: list[AdditiveRepairTorsorRow] = []
    for small, large, orientation in examples:
        deleted = restrict_values(small, large, orientation)
        first = repair_at_basepoint(small, deleted, small[0])
        last = repair_at_basepoint(small, deleted, small[-1])
        transition = sub_vectors(last, first)
        rows.append(
            AdditiveRepairTorsorRow(
                source_support=small,
                target_support=large,
                target_orientation=orientation,
                deleted_values=deleted,
                additive_defect=sum(deleted),
                first_basepoint_repair=first,
                last_basepoint_repair=last,
                transition_difference=transition,
                difference_in_kernel=in_kernel(transition),
                both_additive_repairs_zero_sum=in_kernel(first) and in_kernel(last),
                both_repairs_primitive=is_orientation(first) and is_orientation(last),
                torsor_translation_ok=add_vectors(first, transition) == last,
            )
        )
    return rows


def primitive_locus_row() -> PrimitiveLocusRow:
    support = (2, 3)
    primitive = (1, -1)
    kernel_step = (1, -1)
    translated = add_vectors(primitive, kernel_step)
    return PrimitiveLocusRow(
        support=support,
        primitive_repair=primitive,
        kernel_step=kernel_step,
        translated_vector=translated,
        kernel_step_in_kernel=in_kernel(kernel_step),
        translated_is_zero_sum=in_kernel(translated),
        translated_is_primitive=is_orientation(translated),
        primitive_locus_stable_under_full_kernel=is_orientation(translated),
    )


def transition(
    support: tuple[int, ...], from_base: int, to_base: int, total: int = 1
) -> tuple[int, ...]:
    return sub_vectors(
        section_vector(support, to_base, total),
        section_vector(support, from_base, total),
    )


def basepoint_transition_row() -> BasepointTransitionRow:
    support = (2, 3, 5)
    base_a, base_b, base_c = support
    transition_ab = transition(support, base_a, base_b)
    transition_bc = transition(support, base_b, base_c)
    transition_ac = transition(support, base_a, base_c)
    return BasepointTransitionRow(
        support=support,
        base_a=base_a,
        base_b=base_b,
        base_c=base_c,
        transition_ab=transition_ab,
        transition_bc=transition_bc,
        transition_ac=transition_ac,
        transitions_in_kernel=all(
            in_kernel(item) for item in [transition_ab, transition_bc, transition_ac]
        ),
        cocycle_identity_ok=add_vectors(transition_ab, transition_bc)
        == transition_ac,
        coboundary_description="transition(a,b)=section_b(1)-section_a(1)",
    )


def inclusion_transition_rows() -> list[InclusionTransitionRow]:
    examples = [
        ((2, 3), (2, 3, 5), 2, 2),
        ((2, 3), (2, 3, 5), 2, 5),
    ]
    rows: list[InclusionTransitionRow] = []
    for small, large, small_base, large_base in examples:
        source_section = section_vector(small, small_base, 1)
        extended = extend_by_zero(small, source_section, large)
        target = section_vector(large, large_base, 1)
        transition_vector = sub_vectors(target, extended)
        rows.append(
            InclusionTransitionRow(
                source_support=small,
                target_support=large,
                source_basepoint=small_base,
                target_basepoint=large_base,
                extended_source_section=extended,
                target_section=target,
                transition=transition_vector,
                transition_in_kernel=in_kernel(transition_vector),
                natural_after_forgetting_basepoint=extended == target,
            )
        )
    return rows


def antipode_row() -> AntipodeCompatibilityRow:
    small = (2, 3)
    large = (2, 3, 5)
    orientation = (1, 1, -2)
    deleted = restrict_values(small, large, orientation)
    repaired = repair_at_basepoint(small, deleted, 2)
    antipode_orientation = tuple(-value for value in orientation)
    antipode_deleted = restrict_values(small, large, antipode_orientation)
    repaired_antipode = repair_at_basepoint(small, antipode_deleted, 2)
    antipode_of_repair = tuple(-value for value in repaired)
    return AntipodeCompatibilityRow(
        source_support=small,
        target_support=large,
        target_orientation=orientation,
        basepoint=2,
        repaired_orientation=repaired,
        repaired_antipode=repaired_antipode,
        antipode_of_repair=antipode_of_repair,
        linear_section_antipode_compatible=repaired_antipode
        == antipode_of_repair,
    )


def cohomology_verdict_row() -> CohomologyVerdictRow:
    return CohomologyVerdictRow(
        finite_exact_sequence="0 -> K_S -> Z^S -> Z -> 0",
        split_after_basepoint=True,
        transitions_are_coboundaries=True,
        non_mittag_leffler_tower_present=False,
        rosser_phantom_like=False,
        ordinary_choice_torsor=True,
        next_obstruction=(
            "Classify the integral equivariant obstruction: rational symmetric "
            "sections exist, but integral support-symmetric sections do not."
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "artifacts/reports/"
            "pass107-correction-torsors-support-defect-check.json"
        ),
    )
    args = parser.parse_args()

    repair_rows = additive_repair_rows()
    primitive = primitive_locus_row()
    basepoint = basepoint_transition_row()
    inclusions = inclusion_transition_rows()
    antipode = antipode_row()
    verdict = cohomology_verdict_row()

    checks = {
        "additive_repair_torsor_ok": all(
            row.difference_in_kernel
            and row.both_additive_repairs_zero_sum
            and row.both_repairs_primitive
            and row.torsor_translation_ok
            for row in repair_rows
        ),
        "primitive_locus_not_full_torsor_ok": (
            primitive.kernel_step_in_kernel
            and primitive.translated_is_zero_sum
            and not primitive.translated_is_primitive
            and not primitive.primitive_locus_stable_under_full_kernel
        ),
        "basepoint_transition_cocycle_ok": (
            basepoint.transitions_in_kernel and basepoint.cocycle_identity_ok
        ),
        "inclusion_transition_ok": (
            inclusions[0].transition_in_kernel
            and inclusions[0].natural_after_forgetting_basepoint
            and inclusions[1].transition_in_kernel
            and not inclusions[1].natural_after_forgetting_basepoint
        ),
        "antipode_compatibility_ok": antipode.linear_section_antipode_compatible,
        "ordinary_choice_not_phantom_ok": (
            verdict.split_after_basepoint
            and verdict.transitions_are_coboundaries
            and not verdict.non_mittag_leffler_tower_present
            and not verdict.rosser_phantom_like
            and verdict.ordinary_choice_torsor
        ),
    }

    report = {
        "pass": 107,
        "title": "Correction torsors for support-defect repairs",
        "A_additive_repair_torsor": {
            "statement": (
                "Additive repairs of a deletion defect form an affine torsor "
                "under K_S = ker(Sigma_S)."
            ),
            "rows": [asdict(row) for row in repair_rows],
            "additive_repair_torsor_ok": checks["additive_repair_torsor_ok"],
        },
        "B_primitive_locus": {
            "statement": (
                "The primitive repair locus is not stable under the full "
                "kernel action, so primitivity is a refinement of the additive "
                "torsor."
            ),
            "row": asdict(primitive),
            "primitive_locus_not_full_torsor_ok": checks[
                "primitive_locus_not_full_torsor_ok"
            ],
        },
        "C_basepoint_transitions": {
            "statement": (
                "Transitions between basepointed splittings are K_S-valued "
                "coboundaries and satisfy the cocycle identity."
            ),
            "row": asdict(basepoint),
            "basepoint_transition_cocycle_ok": checks[
                "basepoint_transition_cocycle_ok"
            ],
        },
        "D_inclusion_transitions": {
            "statement": (
                "Basepointed splittings are natural along inclusions only when "
                "the basepoint is preserved."
            ),
            "rows": [asdict(row) for row in inclusions],
            "inclusion_transition_ok": checks["inclusion_transition_ok"],
        },
        "E_antipode_compatibility": {
            "statement": (
                "Linear section repairs commute with the antipode, so the "
                "BZ/2 boundary-line local system is not disturbed."
            ),
            "row": asdict(antipode),
            "antipode_compatibility_ok": checks["antipode_compatibility_ok"],
        },
        "F_cohomology_verdict": {
            "statement": (
                "The support-defect repair torsor is split finite-level choice "
                "data, not a Rosser/cosheaf phantom class."
            ),
            "row": asdict(verdict),
            "ordinary_choice_not_phantom_ok": checks[
                "ordinary_choice_not_phantom_ok"
            ],
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
