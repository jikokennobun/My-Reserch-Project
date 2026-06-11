#!/usr/bin/env python3
"""
Pass 74 verification: first external realization test for H_epsilon.

The tested target is a tagged restricted pro-Ab certificate category.  It is
more concrete than the presentation H_epsilon: finite conductor windows are
sent to tagged finite abelian group data, boundary and duality maps are sent to
integer matrices with source/target tags, and the lcm tower is sent to a tagged
pro-system.

The test is deliberately modest.  It verifies faithfulness on the five
generator families.  It also checks that if the same data are sent to a plain
untagged pro-Ab target, some generator families collide.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List, Tuple


PRIMES = [2, 3, 5, 7, 11, 13]


def prod(values: Iterable[int]) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def lcm_to(n: int) -> int:
    out = 1
    for value in range(1, n + 1):
        out = lcm(out, value)
    return out


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


def finite_window_generator(size: int, conductor: int) -> dict:
    primes = tuple(PRIMES[:size])
    elementary_divisors = tuple((prime, 2 * conductor) for prime in primes)
    lattice_divisors = tuple((prime, conductor) for prime in primes)
    return {
        "family": "finite_conductor_windows",
        "name": f"W_{primes},{conductor}",
        "tagged_signature": (
            "window",
            primes,
            conductor,
            elementary_divisors,
            lattice_divisors,
        ),
        "plain_signature": (
            "window",
            elementary_divisors,
            lattice_divisors,
        ),
    }


def boundary_generator(size: int) -> dict:
    return {
        "family": "loeb_rosser_boundaries",
        "name": f"d_{size}",
        "tagged_signature": ("boundary", size, boundary_matrix(size)),
        "plain_signature": ("boundary", boundary_matrix(size)),
    }


def restriction_generator(small: int, large: int) -> dict:
    matrix = restrict_matrix(boundary_matrix(large), max(0, small - 1), small)
    return {
        "family": "restriction_functoriality",
        "name": f"res_{large}_to_{small}",
        "tagged_signature": ("restriction", large, small, matrix),
        "plain_signature": ("restriction", small, matrix),
    }


def signed_duality_generator(size: int) -> dict:
    return {
        "family": "signed_duality",
        "name": f"signed_dual_{size}",
        "tagged_signature": ("signed_duality", size, signed_dual_boundary(size)),
        "plain_signature": ("signed_duality", signed_dual_boundary(size)),
    }


def pro_stage_generator(n: int) -> dict:
    value = lcm_to(n)
    previous = lcm_to(n - 1) if n > 1 else 1
    return {
        "family": "derived_pro_lcm_tower",
        "name": f"K_{n}",
        "tagged_signature": ("pro_lcm_stage", n, value, value // previous),
        "plain_signature": ("pro_lcm_stage", value),
    }


def build_generators(max_size: int, max_conductor: int, max_n: int) -> List[dict]:
    generators: List[dict] = []
    for size in range(1, max_size + 1):
        for conductor in range(1, max_conductor + 1):
            generators.append(finite_window_generator(size, conductor))
    for size in range(1, max_size + 1):
        generators.append(boundary_generator(size))
        generators.append(signed_duality_generator(size))
    for small in range(1, max_size + 1):
        for large in range(small, max_size + 1):
            generators.append(restriction_generator(small, large))
    for n in range(1, max_n + 1):
        generators.append(pro_stage_generator(n))
    return generators


def collision_report(generators: List[dict], signature_key: str) -> dict:
    buckets = defaultdict(list)
    for generator in generators:
        buckets[generator[signature_key]].append(generator["name"])
    collisions = [
        {"signature": repr(signature), "names": names}
        for signature, names in buckets.items()
        if len(names) > 1
    ]
    return {
        "signature_key": signature_key,
        "generator_count": len(generators),
        "unique_signature_count": len(buckets),
        "collision_count": len(collisions),
        "collisions": collisions[:12],
        "injective": not collisions,
    }


def family_faithfulness(generators: List[dict], signature_key: str) -> List[dict]:
    reports = []
    families = sorted({generator["family"] for generator in generators})
    for family in families:
        family_generators = [
            generator for generator in generators if generator["family"] == family
        ]
        report = collision_report(family_generators, signature_key)
        report["family"] = family
        report["verdict"] = "PASS" if report["injective"] else "FAIL"
        reports.append(report)
    return reports


def check_boundary_relations(max_size: int) -> List[dict]:
    checks = []
    for size in range(1, max_size + 1):
        d = boundary_matrix(size)
        dual = signed_dual_boundary(size)
        double_dual = neg(transpose(dual)) if size > 1 else d
        checks.append(
            {
                "size": size,
                "double_dual_returns_boundary": double_dual == d,
                "verdict": "PASS" if double_dual == d else "FAIL",
            }
        )
    return checks


def check_pro_growth(max_n: int) -> dict:
    values = [lcm_to(n) for n in range(1, max_n + 1)]
    repeated_plain_stages = []
    for index in range(len(values) - 1):
        if values[index] == values[index + 1]:
            repeated_plain_stages.append((index + 1, index + 2, values[index]))
    ratios = [values[index + 1] // values[index] for index in range(len(values) - 1)]
    return {
        "max_n": max_n,
        "lcm_values": values,
        "transition_ratios": ratios,
        "plain_stage_repetitions": repeated_plain_stages,
        "has_plain_stage_collisions": bool(repeated_plain_stages),
        "non_mittag_leffler_growth_witness": max(values) > values[max_n // 2],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", type=int, default=6)
    parser.add_argument("--max-conductor", type=int, default=3)
    parser.add_argument("--max-n", type=int, default=24)
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass74-tagged-proab-realization-check.json",
    )
    args = parser.parse_args()

    if args.max_size < 1 or args.max_size > len(PRIMES):
        raise SystemExit(f"--max-size must be between 1 and {len(PRIMES)}")
    if args.max_conductor < 1:
        raise SystemExit("--max-conductor must be positive")
    if args.max_n < 4:
        raise SystemExit("--max-n must be at least 4")

    generators = build_generators(args.max_size, args.max_conductor, args.max_n)
    tagged_global = collision_report(generators, "tagged_signature")
    plain_global = collision_report(generators, "plain_signature")
    tagged_family = family_faithfulness(generators, "tagged_signature")
    plain_family = family_faithfulness(generators, "plain_signature")
    boundary_relations = check_boundary_relations(args.max_size)
    pro_growth = check_pro_growth(args.max_n)

    tagged_faithful_on_families = all(
        item["verdict"] == "PASS" for item in tagged_family
    )
    plain_has_expected_collisions = (
        not plain_global["injective"]
        and pro_growth["has_plain_stage_collisions"]
    )
    relation_checks_pass = all(
        item["verdict"] == "PASS" for item in boundary_relations
    )

    report = {
        "pass_number": 74,
        "title": "tagged restricted pro-Ab realization test",
        "scope": (
            "finite generator-family faithfulness test for a tagged pro-Ab "
            "certificate target with restricted-product generators"
        ),
        "candidate_target": {
            "name": "Pro_tag^rp(Ab_fin) x Pro_tag(Ab)",
            "description": (
                "finite conductor windows, boundaries, restrictions, signed "
                "duals, and lcm tower stages are realized as tagged finite "
                "abelian group data and tagged pro-system stages"
            ),
            "limitation": (
                "faithfulness uses support and stage tags; this is not yet a "
                "tag-free LCA-sheaf or condensed realization"
            ),
        },
        "generator_count": len(generators),
        "tagged_global_injectivity": tagged_global,
        "plain_global_injectivity": plain_global,
        "tagged_family_faithfulness": tagged_family,
        "plain_family_faithfulness": plain_family,
        "boundary_relations": boundary_relations,
        "pro_growth": pro_growth,
        "conclusion": {
            "tagged_realization_faithful_on_five_families": (
                tagged_global["injective"] and tagged_faithful_on_families
            ),
            "plain_untagged_target_not_faithful": plain_has_expected_collisions,
            "next_obligation": (
                "remove or justify the support/stage tags by embedding them in "
                "a natural LCA-sheaf, condensed, or exact pro-category target"
            ),
        },
        "overall": "PASS"
        if tagged_global["injective"]
        and tagged_faithful_on_families
        and plain_has_expected_collisions
        and relation_checks_pass
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
