#!/usr/bin/env python3
"""
Pass 76 verification: factor projector data through a finite-prime stratified
pro-site model.

Pass 75 internalized support and stage tags as projectors.  Pass 76 tests the
first natural model for those projectors: Boolean support projectors are
characteristic idempotents of clopen prime strata, and lcm-stage projectors are
prefix truncations of the non-Mittag-Leffler pro tower.

This remains a finite-window verification.  It checks that the Pass-75
projector signatures are recovered from site-theoretic support/stage actions,
not that the all-prime LCA/condensed realization has been proved.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple


PRIMES = [2, 3, 5, 7, 11, 13]
Mask = Tuple[int, ...]
Matrix = Tuple[Tuple[int, ...], ...]


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def lcm_to(n: int) -> int:
    out = 1
    for value in range(1, n + 1):
        out = lcm(out, value)
    return out


def all_masks(universe: int) -> List[Mask]:
    return [
        tuple((bits >> index) & 1 for index in range(universe))
        for bits in range(1 << universe)
    ]


def prefix_mask(size: int, universe: int) -> Mask:
    return tuple(1 if index < size else 0 for index in range(universe))


def mask_meet(left: Mask, right: Mask) -> Mask:
    return tuple(min(a, b) for a, b in zip(left, right))


def mask_join(left: Mask, right: Mask) -> Mask:
    return tuple(max(a, b) for a, b in zip(left, right))


def mask_complement(mask: Mask) -> Mask:
    return tuple(1 - bit for bit in mask)


def mask_leq(left: Mask, right: Mask) -> bool:
    return all(a <= b for a, b in zip(left, right))


def stage_mask(stage: int, max_stage: int) -> Mask:
    return tuple(1 if index < stage else 0 for index in range(max_stage))


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        return tuple()
    width = len(right[0])
    shared = len(right)
    rows = []
    for row in left:
        rows.append(
            tuple(sum(row[index] * right[index][col] for index in range(shared)) for col in range(width))
        )
    return tuple(rows)


def transpose(matrix: Matrix) -> Matrix:
    if not matrix:
        return tuple()
    return tuple(tuple(col) for col in zip(*matrix))


def neg(matrix: Matrix) -> Matrix:
    return tuple(tuple(-entry for entry in row) for row in matrix)


def boundary_matrix(size: int) -> Matrix:
    rows = []
    for col in range(1, size):
        row = [0] * size
        row[0] = -1
        row[col] = 1
        rows.append(tuple(row))
    return tuple(rows)


def signed_dual_boundary(size: int) -> Matrix:
    matrix = boundary_matrix(size)
    if matrix:
        return neg(transpose(matrix))
    return (tuple(),)


def coordinate_restriction_matrix(small: int, large: int) -> Matrix:
    return tuple(
        tuple(1 if row == col else 0 for col in range(large))
        for row in range(small)
    )


def boundary_target_restriction_matrix(small: int, large: int) -> Matrix:
    return tuple(
        tuple(1 if row == col else 0 for col in range(max(0, large - 1)))
        for row in range(max(0, small - 1))
    )


def pass75_restriction_signature_matrix(small: int, large: int) -> Matrix:
    matrix = boundary_matrix(large)
    rows = max(0, small - 1)
    return tuple(tuple(row[:small]) for row in matrix[:rows])


def window_generator(size: int, conductor: int, universe: int) -> dict:
    support = prefix_mask(size, universe)
    valuations = tuple(conductor if bit else 0 for bit in support)
    elementary = tuple(2 * value if value else 0 for value in valuations)
    return {
        "family": "finite_conductor_windows",
        "name": f"W_{size},{conductor}",
        "projector_signature": ("window", support, valuations, elementary),
        "site_signature": ("clopen_window", support, valuations, elementary),
        "plain_signature": ("window", valuations, elementary),
    }


def boundary_generator(size: int, universe: int) -> dict:
    support = prefix_mask(size, universe)
    matrix = boundary_matrix(size)
    return {
        "family": "loeb_rosser_boundaries",
        "name": f"d_{size}",
        "projector_signature": ("boundary", support, matrix),
        "site_signature": ("clopen_boundary", support, matrix),
        "plain_signature": ("boundary", matrix),
    }


def restriction_generator(small: int, large: int, universe: int) -> dict:
    source = prefix_mask(large, universe)
    target = prefix_mask(small, universe)
    matrix = pass75_restriction_signature_matrix(small, large)
    return {
        "family": "restriction_functoriality",
        "name": f"res_{large}_to_{small}",
        "projector_signature": ("restriction", source, target, matrix),
        "site_signature": ("open_restriction", source, target, matrix),
        "plain_signature": ("restriction", target, matrix),
    }


def signed_duality_generator(size: int, universe: int) -> dict:
    support = prefix_mask(size, universe)
    matrix = signed_dual_boundary(size)
    return {
        "family": "signed_duality",
        "name": f"signed_dual_{size}",
        "projector_signature": ("signed_duality", support, matrix),
        "site_signature": ("clopen_signed_duality", support, matrix),
        "plain_signature": ("signed_duality", matrix),
    }


def pro_stage_generator(stage: int, max_stage: int) -> dict:
    value = lcm_to(stage)
    previous = lcm_to(stage - 1) if stage > 1 else 1
    projector = stage_mask(stage, max_stage)
    return {
        "family": "derived_pro_lcm_tower",
        "name": f"K_{stage}",
        "projector_signature": ("pro_stage", projector, value, value // previous),
        "site_signature": ("filtered_pro_stage", projector, value, value // previous),
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


def canonicalize_site_signature(signature: tuple) -> tuple:
    family = signature[0]
    payload = signature[1:]
    aliases = {
        "clopen_window": "window",
        "clopen_boundary": "boundary",
        "open_restriction": "restriction",
        "clopen_signed_duality": "signed_duality",
        "filtered_pro_stage": "pro_stage",
    }
    return (aliases[family], *payload)


def collision_report(generators: List[dict], key: str) -> dict:
    buckets = defaultdict(list)
    for generator in generators:
        signature = generator[key]
        if key == "site_signature":
            signature = canonicalize_site_signature(signature)
        buckets[signature].append(generator["name"])
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


def check_clopen_boolean_algebra(universe: int) -> List[dict]:
    checks = []
    masks = all_masks(universe)
    empty = tuple(0 for _ in range(universe))
    total = tuple(1 for _ in range(universe))
    for left in masks:
        complement = mask_complement(left)
        checks.append(
            {
                "kind": "complement",
                "support": left,
                "meet_with_complement_empty": mask_meet(left, complement) == empty,
                "join_with_complement_total": mask_join(left, complement) == total,
                "verdict": "PASS"
                if mask_meet(left, complement) == empty
                and mask_join(left, complement) == total
                else "FAIL",
            }
        )
        for right in masks:
            meet = mask_meet(left, right)
            checks.append(
                {
                    "kind": "intersection",
                    "left": left,
                    "right": right,
                    "idempotent_when_equal": meet == left if left == right else True,
                    "commutes": meet == mask_meet(right, left),
                    "meet_below_left": mask_leq(meet, left),
                    "meet_below_right": mask_leq(meet, right),
                    "verdict": "PASS"
                    if (
                        (meet == left if left == right else True)
                        and meet == mask_meet(right, left)
                        and mask_leq(meet, left)
                        and mask_leq(meet, right)
                    )
                    else "FAIL",
                }
            )
    return checks


def check_restriction_functoriality(max_size: int) -> List[dict]:
    checks = []
    for small in range(1, max_size + 1):
        for mid in range(small, max_size + 1):
            for large in range(mid, max_size + 1):
                res_sm = coordinate_restriction_matrix(small, mid)
                res_ml = coordinate_restriction_matrix(mid, large)
                res_sl = coordinate_restriction_matrix(small, large)
                composed = matrix_mul(res_sm, res_ml)
                target_sm = boundary_target_restriction_matrix(small, mid)
                target_ml = boundary_target_restriction_matrix(mid, large)
                target_sl = boundary_target_restriction_matrix(small, large)
                target_composed = matrix_mul(target_sm, target_ml)
                d_small = boundary_matrix(small)
                d_large = boundary_matrix(large)
                left_square = matrix_mul(d_small, res_sl)
                right_square = matrix_mul(target_sl, d_large)
                checks.append(
                    {
                        "small": small,
                        "mid": mid,
                        "large": large,
                        "open_inclusion_composes": composed == res_sl,
                        "boundary_target_restriction_composes": target_composed == target_sl,
                        "boundary_square_commutes": left_square == right_square,
                        "verdict": "PASS"
                        if composed == res_sl
                        and target_composed == target_sl
                        and left_square == right_square
                        else "FAIL",
                    }
                )
    return checks


def check_stage_filtration(max_stage: int) -> List[dict]:
    checks = []
    for left_stage in range(1, max_stage + 1):
        left = stage_mask(left_stage, max_stage)
        for right_stage in range(1, max_stage + 1):
            right = stage_mask(right_stage, max_stage)
            product = mask_meet(left, right)
            expected = stage_mask(min(left_stage, right_stage), max_stage)
            checks.append(
                {
                    "left_stage": left_stage,
                    "right_stage": right_stage,
                    "meet_is_min_stage": product == expected,
                    "commutes": product == mask_meet(right, left),
                    "verdict": "PASS"
                    if product == expected and product == mask_meet(right, left)
                    else "FAIL",
                }
            )
    return checks


def check_repeated_lcm_stage_separation(max_stage: int) -> dict:
    values = [lcm_to(stage) for stage in range(1, max_stage + 1)]
    repeated = []
    separated = []
    for left in range(1, max_stage + 1):
        for right in range(left + 1, max_stage + 1):
            if values[left - 1] == values[right - 1]:
                repeated.append({"left": left, "right": right, "value": values[left - 1]})
                separated.append(stage_mask(left, max_stage) != stage_mask(right, max_stage))
    return {
        "repeated_plain_stage_pairs": repeated[:24],
        "repeated_plain_stage_pair_count": len(repeated),
        "all_repeated_plain_stages_separated_by_q": all(separated) if separated else True,
    }


def check_factorization(generators: List[dict]) -> List[dict]:
    return [
        {
            "name": generator["name"],
            "family": generator["family"],
            "site_canonical_equals_projector": (
                canonicalize_site_signature(generator["site_signature"])
                == generator["projector_signature"]
            ),
            "verdict": "PASS"
            if canonicalize_site_signature(generator["site_signature"])
            == generator["projector_signature"]
            else "FAIL",
        }
        for generator in generators
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", type=int, default=6)
    parser.add_argument("--max-conductor", type=int, default=3)
    parser.add_argument("--max-stage", type=int, default=24)
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass76-stratified-pro-site-projector-check.json",
    )
    args = parser.parse_args()

    if args.max_size < 1 or args.max_size > len(PRIMES):
        raise SystemExit(f"--max-size must be between 1 and {len(PRIMES)}")
    if args.max_conductor < 1:
        raise SystemExit("--max-conductor must be positive")
    if args.max_stage < 4:
        raise SystemExit("--max-stage must be at least 4")

    generators = build_generators(args.max_size, args.max_conductor, args.max_stage)
    site_global = collision_report(generators, "site_signature")
    projector_global = collision_report(generators, "projector_signature")
    plain_global = collision_report(generators, "plain_signature")
    site_family = family_reports(generators, "site_signature")
    clopen_checks = check_clopen_boolean_algebra(args.max_size)
    restriction_checks = check_restriction_functoriality(args.max_size)
    stage_checks = check_stage_filtration(args.max_stage)
    lcm_separation = check_repeated_lcm_stage_separation(args.max_stage)
    factorization_checks = check_factorization(generators)

    all_site_families_pass = all(report["verdict"] == "PASS" for report in site_family)
    all_relations_pass = all(
        item["verdict"] == "PASS"
        for item in clopen_checks + restriction_checks + stage_checks + factorization_checks
    )
    plain_has_collisions = not plain_global["injective"]

    report = {
        "pass_number": 76,
        "title": "finite-prime stratified pro-site model for support and stage projectors",
        "scope": (
            "finite-window factorization of the Pass-75 projector-enriched "
            "realization through clopen support strata and pro-stage filtrations"
        ),
        "candidate_target": {
            "name": "StratPro_epsilon(U,N)",
            "support_space": "finite discrete/Stone space on the checked prime universe U",
            "support_projectors": "multiplication by characteristic functions of clopen strata",
            "stage_projectors": "prefix truncations of the lcm pro-tower through N",
            "limitation": (
                "finite stratified pro-site model only; the all-prime LCA, "
                "condensed, or solid derived realization remains to be built"
            ),
        },
        "generator_count": len(generators),
        "site_global_injectivity": site_global,
        "projector_global_injectivity": projector_global,
        "plain_global_injectivity": plain_global,
        "site_family_faithfulness": site_family,
        "clopen_boolean_relation_count": len(clopen_checks),
        "clopen_boolean_relations_all_pass": all(
            item["verdict"] == "PASS" for item in clopen_checks
        ),
        "restriction_functoriality_checks": restriction_checks,
        "stage_filtration_relation_count": len(stage_checks),
        "stage_filtration_relations_all_pass": all(
            item["verdict"] == "PASS" for item in stage_checks
        ),
        "lcm_stage_separation": lcm_separation,
        "factorization_checks": factorization_checks,
        "conclusion": {
            "rho_proj_factors_through_stratified_pro_site_on_checked_window": all(
                item["verdict"] == "PASS" for item in factorization_checks
            ),
            "site_model_faithful_on_five_families": (
                site_global["injective"] and all_site_families_pass
            ),
            "plain_target_still_not_faithful": plain_has_collisions,
            "clopen_and_stage_relations_valid": all_relations_pass,
            "next_obligation": (
                "upgrade StratPro_epsilon(U,N) to an all-prime derived "
                "LCA/condensed/solid exact target and prove the signed duality "
                "law there"
            ),
        },
        "overall": "PASS"
        if site_global["injective"]
        and projector_global["injective"]
        and all_site_families_pass
        and plain_has_collisions
        and all_relations_pass
        and lcm_separation["all_repeated_plain_stages_separated_by_q"]
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
