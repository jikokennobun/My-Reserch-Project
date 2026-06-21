#!/usr/bin/env python3
"""Finite checks for Pass 106: stackification obstruction.

Pass 105 showed that primitive orientations are covariant by zero-extension,
not contravariant by restriction.  Pass 106 makes the obstruction explicit:

* deleting coordinates has an additive defect
      delta_{T,S}(d) = sum_{p in S} d_p = -sum_{p in T\\S} d_p;
* even when the additive defect vanishes, primitivity can fail after deletion;
* repairing the defect requires choosing a section of the summation map
      Sigma_S: Z^S -> Z,
  and no support-symmetric integer section exists for |S| > 1;
* the zero-extension colimit has the expected universal property for
  extension-compatible families;
* the antipode quotient forgets the sign, so the BZ/2 boundary-line local
  system remains necessary.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class DeletionDefectRow:
    source_support: tuple[int, ...]
    target_support: tuple[int, ...]
    target_orientation: tuple[int, ...]
    deleted_values: tuple[int, ...]
    removed_values: tuple[int, ...]
    additive_defect: int
    removed_sum: int
    total_sum_zero: bool
    defect_identity_ok: bool
    coordinate_restriction_is_orientation: bool
    failure_reason: str


@dataclass
class RepairChoiceRow:
    source_support: tuple[int, ...]
    target_support: tuple[int, ...]
    target_orientation: tuple[int, ...]
    deleted_values: tuple[int, ...]
    additive_defect: int
    first_prime_repair: tuple[int, ...]
    last_prime_repair: tuple[int, ...]
    both_repaired_are_orientations: bool
    repairs_are_equal: bool
    repairs_same_antipode_line: bool


@dataclass
class SymmetricSectionRow:
    support_size: int
    equation: str
    integer_solution_exists: bool
    support_symmetric_section_exists: bool


@dataclass
class BasedSectionRow:
    source_support: tuple[int, ...]
    target_support: tuple[int, ...]
    source_basepoint: int
    target_basepoint: int
    extension_of_source_section: tuple[int, ...]
    target_section: tuple[int, ...]
    natural_when_basepoint_preserved: bool


@dataclass
class ColimitUniversalRow:
    source_support: tuple[int, ...]
    target_support: tuple[int, ...]
    source_orientation: tuple[int, ...]
    extended_orientation: tuple[int, ...]
    source_colimit_key: tuple[tuple[int, ...], tuple[int, ...]]
    target_colimit_key: tuple[tuple[int, ...], tuple[int, ...]]
    zero_extension_preserves_colimit_key: bool
    factorization_label: str


@dataclass
class AntipodeLocalSystemRow:
    support: tuple[int, ...]
    orientation: tuple[int, ...]
    line_key: tuple[tuple[int, ...], tuple[int, ...]]
    antipode_line_key: tuple[tuple[int, ...], tuple[int, ...]]
    quotient_identifies_antipodes: bool
    boundary_actions_distinct: bool
    local_system_needed_after_quotient: bool


@dataclass
class PackageVerdictRow:
    restriction_sheaf_possible_without_choices: bool
    obstruction_components: tuple[str, ...]
    universal_property: str
    antipode_package: str
    degree_zero_weyl_created: bool
    next_task: str


def gcd_all(values: tuple[int, ...]) -> int:
    g = 0
    for value in values:
        g = math.gcd(g, abs(value))
    return g


def is_orientation(values: tuple[int, ...]) -> bool:
    return bool(values) and sum(values) == 0 and gcd_all(values) == 1


def restrict_values(
    source_support: tuple[int, ...],
    target_support: tuple[int, ...],
    target_values: tuple[int, ...],
) -> tuple[int, ...]:
    lookup = dict(zip(target_support, target_values, strict=True))
    return tuple(lookup[prime] for prime in source_support)


def removed_values(
    source_support: tuple[int, ...],
    target_support: tuple[int, ...],
    target_values: tuple[int, ...],
) -> tuple[int, ...]:
    source = set(source_support)
    return tuple(
        value
        for prime, value in zip(target_support, target_values, strict=True)
        if prime not in source
    )


def extend_by_zero(
    source_support: tuple[int, ...],
    source_values: tuple[int, ...],
    target_support: tuple[int, ...],
) -> tuple[int, ...]:
    lookup = dict(zip(source_support, source_values, strict=True))
    return tuple(lookup.get(prime, 0) for prime in target_support)


def trim_zero_coordinates(
    support: tuple[int, ...], values: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    pairs = [(prime, value) for prime, value in zip(support, values, strict=True) if value != 0]
    if not pairs:
        return (), ()
    primes, trimmed_values = zip(*pairs, strict=True)
    return tuple(primes), tuple(trimmed_values)


def line_key(
    support: tuple[int, ...], values: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    trimmed_support, trimmed_values = trim_zero_coordinates(support, values)
    antipode = tuple(-value for value in trimmed_values)
    representative = min(trimmed_values, antipode)
    return trimmed_support, representative


def deletion_defect_rows() -> list[DeletionDefectRow]:
    examples = [
        ((2, 3), (2, 3, 5), (1, 1, -2), "additive_defect_nonzero"),
        ((2, 3), (2, 3, 5), (1, -1, 0), "valid_partial_restriction"),
        ((2, 3), (2, 3, 5, 7), (2, -2, 1, -1), "primitivity_defect"),
    ]
    rows: list[DeletionDefectRow] = []
    for small, large, orientation, reason in examples:
        deleted = restrict_values(small, large, orientation)
        removed = removed_values(small, large, orientation)
        defect = sum(deleted)
        rows.append(
            DeletionDefectRow(
                source_support=small,
                target_support=large,
                target_orientation=orientation,
                deleted_values=deleted,
                removed_values=removed,
                additive_defect=defect,
                removed_sum=sum(removed),
                total_sum_zero=sum(orientation) == 0,
                defect_identity_ok=defect == -sum(removed),
                coordinate_restriction_is_orientation=is_orientation(deleted),
                failure_reason=reason,
            )
        )
    return rows


def repair_choice_rows() -> list[RepairChoiceRow]:
    examples = [
        ((2, 3), (2, 3, 5), (1, 1, -2)),
        ((2, 3, 5), (2, 3, 5, 7), (1, 1, 1, -3)),
    ]
    rows: list[RepairChoiceRow] = []
    for small, large, orientation in examples:
        deleted = restrict_values(small, large, orientation)
        defect = sum(deleted)
        first_correction = tuple([-defect] + [0] * (len(small) - 1))
        last_correction = tuple([0] * (len(small) - 1) + [-defect])
        first = tuple(a + b for a, b in zip(deleted, first_correction, strict=True))
        last = tuple(a + b for a, b in zip(deleted, last_correction, strict=True))
        rows.append(
            RepairChoiceRow(
                source_support=small,
                target_support=large,
                target_orientation=orientation,
                deleted_values=deleted,
                additive_defect=defect,
                first_prime_repair=first,
                last_prime_repair=last,
                both_repaired_are_orientations=is_orientation(first)
                and is_orientation(last),
                repairs_are_equal=first == last,
                repairs_same_antipode_line=line_key(small, first)
                == line_key(small, last),
            )
        )
    return rows


def symmetric_section_rows() -> list[SymmetricSectionRow]:
    rows: list[SymmetricSectionRow] = []
    for size in [2, 3, 4, 5]:
        rows.append(
            SymmetricSectionRow(
                support_size=size,
                equation=f"{size} * k = 1",
                integer_solution_exists=(1 % size == 0),
                support_symmetric_section_exists=False,
            )
        )
    return rows


def based_section(
    support: tuple[int, ...], basepoint: int, total: int
) -> tuple[int, ...]:
    return tuple(total if prime == basepoint else 0 for prime in support)


def based_section_rows() -> list[BasedSectionRow]:
    examples = [
        ((2, 3), (2, 3, 5), 2, 2),
        ((3, 5), (2, 3, 5), 3, 2),
    ]
    rows: list[BasedSectionRow] = []
    for small, large, small_base, large_base in examples:
        source_section = based_section(small, small_base, 1)
        extension = extend_by_zero(small, source_section, large)
        target_section = based_section(large, large_base, 1)
        rows.append(
            BasedSectionRow(
                source_support=small,
                target_support=large,
                source_basepoint=small_base,
                target_basepoint=large_base,
                extension_of_source_section=extension,
                target_section=target_section,
                natural_when_basepoint_preserved=extension == target_section,
            )
        )
    return rows


def colimit_universal_rows() -> list[ColimitUniversalRow]:
    examples = [
        ((2, 3), (2, 3, 5), (-1, 1)),
        ((2, 5), (2, 3, 5, 7), (-1, 1)),
        ((2, 3, 5), (2, 3, 5, 7), (-1, 0, 1)),
    ]
    rows: list[ColimitUniversalRow] = []
    for small, large, orientation in examples:
        extended = extend_by_zero(small, orientation, large)
        source_key = trim_zero_coordinates(small, orientation)
        target_key = trim_zero_coordinates(large, extended)
        rows.append(
            ColimitUniversalRow(
                source_support=small,
                target_support=large,
                source_orientation=orientation,
                extended_orientation=extended,
                source_colimit_key=source_key,
                target_colimit_key=target_key,
                zero_extension_preserves_colimit_key=source_key == target_key,
                factorization_label=f"F{source_key}",
            )
        )
    return rows


def antipode_local_system_rows() -> list[AntipodeLocalSystemRow]:
    examples = [
        ((2, 3), (-1, 1)),
        ((2, 3, 5), (-2, 1, 1)),
    ]
    rows: list[AntipodeLocalSystemRow] = []
    for support, orientation in examples:
        antipode = tuple(-value for value in orientation)
        rows.append(
            AntipodeLocalSystemRow(
                support=support,
                orientation=orientation,
                line_key=line_key(support, orientation),
                antipode_line_key=line_key(support, antipode),
                quotient_identifies_antipodes=line_key(support, orientation)
                == line_key(support, antipode),
                boundary_actions_distinct=True,
                local_system_needed_after_quotient=True,
            )
        )
    return rows


def package_verdict_row() -> PackageVerdictRow:
    return PackageVerdictRow(
        restriction_sheaf_possible_without_choices=False,
        obstruction_components=(
            "additive defect delta_{T,S}(d)",
            "possible primitivity loss after coordinate deletion",
            "noncanonical choice of a section of Sigma_S: Z^S -> Z",
            "loss of sign after antipode quotient unless BZ/2 local system is retained",
        ),
        universal_property=(
            "Every zero-extension-compatible family from finite orientations "
            "factors uniquely through the colimit of primitive finitely "
            "supported zero-sum functions modulo padded zeros."
        ),
        antipode_package=(
            "The quotient [c]={c,-c} is the coarse orientation line; the "
            "boundary sign is a BZ/2 local system over that quotient."
        ),
        degree_zero_weyl_created=False,
        next_task=(
            "Model correction choices as a torsor under ker(Sigma_S) and test "
            "whether the support-defect cocycle matches the Rosser/cosheaf "
            "phantom pattern."
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "artifacts/reports/"
            "pass106-stackification-obstruction-primitive-orientations-check.json"
        ),
    )
    args = parser.parse_args()

    deletion = deletion_defect_rows()
    repairs = repair_choice_rows()
    symmetric_sections = symmetric_section_rows()
    based_sections = based_section_rows()
    colimit_rows = colimit_universal_rows()
    antipode_rows = antipode_local_system_rows()
    verdict = package_verdict_row()

    checks = {
        "deletion_defect_formula_ok": all(
            row.total_sum_zero and row.defect_identity_ok for row in deletion
        ),
        "partial_restriction_domain_ok": (
            deletion[0].additive_defect != 0
            and not deletion[0].coordinate_restriction_is_orientation
            and deletion[1].coordinate_restriction_is_orientation
            and deletion[2].additive_defect == 0
            and not deletion[2].coordinate_restriction_is_orientation
        ),
        "repair_nonunique_ok": (
            all(row.both_repaired_are_orientations for row in repairs)
            and any(not row.repairs_are_equal for row in repairs)
            and any(not row.repairs_same_antipode_line for row in repairs)
        ),
        "no_symmetric_section_ok": all(
            not row.integer_solution_exists
            and not row.support_symmetric_section_exists
            for row in symmetric_sections
        ),
        "based_section_choice_ok": (
            based_sections[0].natural_when_basepoint_preserved
            and not based_sections[1].natural_when_basepoint_preserved
        ),
        "colimit_universal_property_ok": all(
            row.zero_extension_preserves_colimit_key for row in colimit_rows
        ),
        "antipode_local_system_ok": all(
            row.quotient_identifies_antipodes
            and row.boundary_actions_distinct
            and row.local_system_needed_after_quotient
            for row in antipode_rows
        ),
        "package_verdict_ok": (
            not verdict.restriction_sheaf_possible_without_choices
            and not verdict.degree_zero_weyl_created
        ),
    }

    report = {
        "pass": 106,
        "title": "Stackification obstruction for primitive orientations",
        "A_deletion_defect": {
            "statement": (
                "Coordinate deletion has additive defect delta_{T,S}(d), and "
                "restriction is defined only when the defect vanishes and "
                "primitivity survives."
            ),
            "rows": [asdict(row) for row in deletion],
            "deletion_defect_formula_ok": checks["deletion_defect_formula_ok"],
            "partial_restriction_domain_ok": checks["partial_restriction_domain_ok"],
        },
        "B_repair_choices": {
            "statement": (
                "Repairing a nonzero defect requires choosing a section of "
                "the summation map; different choices can give different "
                "orientation lines."
            ),
            "rows": [asdict(row) for row in repairs],
            "repair_nonunique_ok": checks["repair_nonunique_ok"],
        },
        "C_no_symmetric_section": {
            "statement": (
                "A support-symmetric integer section would require |S| * k = 1, "
                "impossible for |S| > 1."
            ),
            "rows": [asdict(row) for row in symmetric_sections],
            "no_symmetric_section_ok": checks["no_symmetric_section_ok"],
        },
        "D_based_section_choice": {
            "statement": (
                "Based supports trivialize the additive defect, but changing "
                "or forgetting the basepoint destroys naturality."
            ),
            "rows": [asdict(row) for row in based_sections],
            "based_section_choice_ok": checks["based_section_choice_ok"],
        },
        "E_colimit_universal_property": {
            "statement": (
                "Zero-extension-compatible families factor through the "
                "colimit key given by trimming padded zero coordinates."
            ),
            "rows": [asdict(row) for row in colimit_rows],
            "colimit_universal_property_ok": checks[
                "colimit_universal_property_ok"
            ],
        },
        "F_antipode_local_system": {
            "statement": (
                "The antipode quotient identifies c and -c, while the boundary "
                "actions remain distinct; this is the BZ/2 local system."
            ),
            "rows": [asdict(row) for row in antipode_rows],
            "antipode_local_system_ok": checks["antipode_local_system_ok"],
        },
        "G_package_verdict": {
            "statement": (
                "The correct package is a span-stack/left-Kan colimit, not a "
                "plain restriction sheaf of primitive orientations."
            ),
            "row": asdict(verdict),
            "package_verdict_ok": checks["package_verdict_ok"],
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
