#!/usr/bin/env python3
"""
Pass 75 verification: replace external tags by intrinsic projectors.

Pass 74 showed that a tagged restricted pro-Ab certificate target is faithful,
while the tag-forgetting target is not.  Pass 75 tests the next refinement:
support tags are replaced by a Boolean algebra of commuting support
idempotents, and pro-stage tags are replaced by a chain of stage projectors.

This is still a certificate target, not yet an LCA-sheaf or condensed
realization.  The point is that the formerly external tags can be represented
as internal idempotent/projector structure.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List, Tuple


PRIMES = [2, 3, 5, 7, 11, 13]


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def lcm_to(n: int) -> int:
    out = 1
    for value in range(1, n + 1):
        out = lcm(out, value)
    return out


def support_projector(size: int, universe: int) -> Tuple[int, ...]:
    return tuple(1 if index < size else 0 for index in range(universe))


def stage_projector(stage: int, max_stage: int) -> Tuple[int, ...]:
    return tuple(1 if index < stage else 0 for index in range(max_stage))


def meet(left: Tuple[int, ...], right: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(min(a, b) for a, b in zip(left, right))


def boundary_matrix(size: int) -> Tuple[Tuple[int, ...], ...]:
    rows = []
    for col in range(1, size):
        row = [0] * size
        row[0] = -1
        row[col] = 1
        rows.append(tuple(row))
    return tuple(rows)


def transpose(matrix: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
    if not matrix:
        return tuple()
    return tuple(tuple(col) for col in zip(*matrix))


def neg(matrix: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
    return tuple(tuple(-entry for entry in row) for row in matrix)


def signed_dual_boundary(size: int) -> Tuple[Tuple[int, ...], ...]:
    matrix = boundary_matrix(size)
    if matrix:
        return neg(transpose(matrix))
    return (tuple(),)


def restrict_matrix(
    matrix: Tuple[Tuple[int, ...], ...],
    rows: int,
    cols: int,
) -> Tuple[Tuple[int, ...], ...]:
    return tuple(tuple(row[:cols]) for row in matrix[:rows])


def window_generator(size: int, conductor: int, universe: int) -> dict:
    support = support_projector(size, universe)
    valuations = tuple(conductor if bit else 0 for bit in support)
    elementary = tuple(2 * value if value else 0 for value in valuations)
    return {
        "family": "finite_conductor_windows",
        "name": f"W_{size},{conductor}",
        "projector_signature": ("window", support, valuations, elementary),
        "plain_signature": ("window", valuations, elementary),
    }


def boundary_generator(size: int, universe: int) -> dict:
    support = support_projector(size, universe)
    return {
        "family": "loeb_rosser_boundaries",
        "name": f"d_{size}",
        "projector_signature": ("boundary", support, boundary_matrix(size)),
        "plain_signature": ("boundary", boundary_matrix(size)),
    }


def restriction_generator(small: int, large: int, universe: int) -> dict:
    source = support_projector(large, universe)
    target = support_projector(small, universe)
    matrix = restrict_matrix(boundary_matrix(large), max(0, small - 1), small)
    return {
        "family": "restriction_functoriality",
        "name": f"res_{large}_to_{small}",
        "projector_signature": ("restriction", source, target, matrix),
        "plain_signature": ("restriction", target, matrix),
    }


def signed_duality_generator(size: int, universe: int) -> dict:
    support = support_projector(size, universe)
    return {
        "family": "signed_duality",
        "name": f"signed_dual_{size}",
        "projector_signature": ("signed_duality", support, signed_dual_boundary(size)),
        "plain_signature": ("signed_duality", signed_dual_boundary(size)),
    }


def pro_stage_generator(stage: int, max_stage: int) -> dict:
    value = lcm_to(stage)
    previous = lcm_to(stage - 1) if stage > 1 else 1
    projector = stage_projector(stage, max_stage)
    return {
        "family": "derived_pro_lcm_tower",
        "name": f"K_{stage}",
        "projector_signature": ("pro_stage", projector, value, value // previous),
        "plain_signature": ("pro_stage", value),
    }


def build_generators(max_size: int, max_conductor: int, max_stage: int) -> List[dict]:
    generators: List[dict] = []
    for size in range(1, max_size + 1):
        for conductor in range(1, max_conductor + 1):
            generators.append(window_generator(size, conductor, max_size))
    for size in range(1, max_size + 1):
        generators.append(boundary_generator(size, max_size))
        generators.append(signed_duality_generator(size, max_size))
    for small in range(1, max_size + 1):
        for large in range(small, max_size + 1):
            generators.append(restriction_generator(small, large, max_size))
    for stage in range(1, max_stage + 1):
        generators.append(pro_stage_generator(stage, max_stage))
    return generators


def collision_report(generators: List[dict], key: str) -> dict:
    buckets = defaultdict(list)
    for generator in generators:
        buckets[generator[key]].append(generator["name"])
    collisions = [
        {"signature": repr(signature), "names": names}
        for signature, names in buckets.items()
        if len(names) > 1
    ]
    return {
        "signature_key": key,
        "generator_count": len(generators),
        "unique_signature_count": len(buckets),
        "collision_count": len(collisions),
        "collisions": collisions[:12],
        "injective": not collisions,
    }


def family_reports(generators: List[dict], key: str) -> List[dict]:
    reports = []
    for family in sorted({generator["family"] for generator in generators}):
        subset = [generator for generator in generators if generator["family"] == family]
        report = collision_report(subset, key)
        report["family"] = family
        report["verdict"] = "PASS" if report["injective"] else "FAIL"
        reports.append(report)
    return reports


def check_support_projector_relations(max_size: int) -> List[dict]:
    checks = []
    projectors = [support_projector(size, max_size) for size in range(1, max_size + 1)]
    for i, left in enumerate(projectors, start=1):
        for j, right in enumerate(projectors, start=1):
            product = meet(left, right)
            expected = support_projector(min(i, j), max_size)
            checks.append(
                {
                    "left_size": i,
                    "right_size": j,
                    "idempotent_when_equal": product == left if i == j else True,
                    "meet_is_intersection": product == expected,
                    "commutes": meet(left, right) == meet(right, left),
                    "verdict": "PASS"
                    if product == expected and meet(left, right) == meet(right, left)
                    else "FAIL",
                }
            )
    return checks


def check_stage_projector_relations(max_stage: int) -> List[dict]:
    checks = []
    projectors = [
        stage_projector(stage, max_stage) for stage in range(1, max_stage + 1)
    ]
    for i, left in enumerate(projectors, start=1):
        for j, right in enumerate(projectors, start=1):
            product = meet(left, right)
            expected = stage_projector(min(i, j), max_stage)
            checks.append(
                {
                    "left_stage": i,
                    "right_stage": j,
                    "meet_is_min_stage": product == expected,
                    "commutes": meet(left, right) == meet(right, left),
                    "verdict": "PASS"
                    if product == expected and meet(left, right) == meet(right, left)
                    else "FAIL",
                }
            )
    return checks


def check_restriction_projector_actions(max_size: int) -> List[dict]:
    checks = []
    for small in range(1, max_size + 1):
        target = support_projector(small, max_size)
        for large in range(small, max_size + 1):
            source = support_projector(large, max_size)
            checks.append(
                {
                    "small": small,
                    "large": large,
                    "target_meet_source_is_target": meet(target, source) == target,
                    "source_records_domain": source != target if large != small else True,
                    "verdict": "PASS"
                    if meet(target, source) == target
                    and (source != target if large != small else True)
                    else "FAIL",
                }
            )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", type=int, default=6)
    parser.add_argument("--max-conductor", type=int, default=3)
    parser.add_argument("--max-stage", type=int, default=24)
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass75-intrinsic-projector-realization-check.json",
    )
    args = parser.parse_args()

    if args.max_size < 1 or args.max_size > len(PRIMES):
        raise SystemExit(f"--max-size must be between 1 and {len(PRIMES)}")
    if args.max_conductor < 1:
        raise SystemExit("--max-conductor must be positive")
    if args.max_stage < 4:
        raise SystemExit("--max-stage must be at least 4")

    generators = build_generators(args.max_size, args.max_conductor, args.max_stage)
    projector_global = collision_report(generators, "projector_signature")
    plain_global = collision_report(generators, "plain_signature")
    projector_family = family_reports(generators, "projector_signature")
    support_checks = check_support_projector_relations(args.max_size)
    stage_checks = check_stage_projector_relations(args.max_stage)
    restriction_checks = check_restriction_projector_actions(args.max_size)

    all_projector_families_pass = all(
        report["verdict"] == "PASS" for report in projector_family
    )
    all_relations_pass = all(
        item["verdict"] == "PASS"
        for item in support_checks + stage_checks + restriction_checks
    )
    plain_has_collisions = not plain_global["injective"]

    report = {
        "pass_number": 75,
        "title": "intrinsic projector realization of support and stage data",
        "scope": (
            "finite generator-family faithfulness test after replacing external "
            "tags by internal Boolean support projectors and stage projectors"
        ),
        "candidate_target": {
            "name": "projector-enriched restricted pro-Ab certificate target",
            "support_structure": "commuting Boolean idempotents e_p",
            "stage_structure": "chain projectors q_n with q_n q_m = q_min(n,m)",
            "limitation": (
                "still a projector-enriched certificate target; the next step "
                "is realization of these projectors in LCA sheaves, condensed "
                "objects, or an exact pro-category"
            ),
        },
        "generator_count": len(generators),
        "projector_global_injectivity": projector_global,
        "plain_global_injectivity": plain_global,
        "projector_family_faithfulness": projector_family,
        "support_projector_relations": support_checks,
        "stage_projector_relations_sample_count": len(stage_checks),
        "stage_projector_relations_all_pass": all(
            item["verdict"] == "PASS" for item in stage_checks
        ),
        "restriction_projector_actions": restriction_checks,
        "conclusion": {
            "projector_realization_faithful_on_five_families": (
                projector_global["injective"] and all_projector_families_pass
            ),
            "plain_target_still_not_faithful": plain_has_collisions,
            "projector_relations_valid": all_relations_pass,
            "next_obligation": (
                "interpret the Boolean support and stage projectors as natural "
                "structure in an established analytic/categorical target"
            ),
        },
        "overall": "PASS"
        if projector_global["injective"]
        and all_projector_families_pass
        and plain_has_collisions
        and all_relations_pass
        else "FAIL",
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    print()
    print("wrote", out)
    return 0 if report["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
