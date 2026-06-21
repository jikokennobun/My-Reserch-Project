#!/usr/bin/env python3
"""Pass 113 finite search: four-element MacNeille G2/A2 boundary.

This extends the Pass-112 fixed V-carrier search to all labelled
four-element posets with a unique bottom.  It deliberately does not claim to
enumerate all preorders, residual structures, or completion-stability
conditions.  The purpose is narrower: test whether the Pass-112 A2 gate
breaks immediately on four-element posets.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path
from typing import Callable, Iterable


CARRIER = ("0", "a", "b", "c")
ORDERED_PAIRS = tuple((x, y) for x in CARRIER for y in CARRIER if x != y)


def relation_key(order: frozenset[tuple[str, str]]) -> str:
    return ";".join(f"{x}<={y}" for x, y in sorted(order))


def leq(order: frozenset[tuple[str, str]], x: str, y: str) -> bool:
    return (x, y) in order


def equiv(order: frozenset[tuple[str, str]], x: str, y: str) -> bool:
    return leq(order, x, y) and leq(order, y, x)


def is_transitive(order: frozenset[tuple[str, str]]) -> bool:
    return all(
        not (leq(order, x, y) and leq(order, y, z)) or leq(order, x, z)
        for x in CARRIER
        for y in CARRIER
        for z in CARRIER
    )


def is_antisymmetric(order: frozenset[tuple[str, str]]) -> bool:
    return all(
        x == y or not (leq(order, x, y) and leq(order, y, x))
        for x in CARRIER
        for y in CARRIER
    )


def labelled_posets() -> list[frozenset[tuple[str, str]]]:
    posets: list[frozenset[tuple[str, str]]] = []
    reflexive = frozenset((x, x) for x in CARRIER)
    for mask in range(1 << len(ORDERED_PAIRS)):
        order = set(reflexive)
        for index, pair in enumerate(ORDERED_PAIRS):
            if mask & (1 << index):
                order.add(pair)
        frozen = frozenset(order)
        if is_antisymmetric(frozen) and is_transitive(frozen):
            posets.append(frozen)
    return posets


def bottom_of(order: frozenset[tuple[str, str]]) -> str | None:
    bottoms = [x for x in CARRIER if all(leq(order, x, y) for y in CARRIER)]
    return bottoms[0] if len(bottoms) == 1 else None


def uppers(order: frozenset[tuple[str, str]], subset: Iterable[str]) -> set[str]:
    items = set(subset)
    return {candidate for candidate in CARRIER if all(leq(order, x, candidate) for x in items)}


def lowers(order: frozenset[tuple[str, str]], subset: Iterable[str]) -> set[str]:
    items = set(subset)
    return {candidate for candidate in CARRIER if all(leq(order, candidate, x) for x in items)}


def mac_close_l(order: frozenset[tuple[str, str]], subset: Iterable[str]) -> frozenset[str]:
    return frozenset(lowers(order, uppers(order, subset)))


def mac_close_lop(order: frozenset[tuple[str, str]], subset: Iterable[str]) -> frozenset[str]:
    return frozenset(uppers(order, lowers(order, subset)))


def closed_cuts(order: frozenset[tuple[str, str]]) -> list[frozenset[str]]:
    cuts: set[frozenset[str]] = set()
    for mask in range(1 << len(CARRIER)):
        subset = {CARRIER[index] for index in range(len(CARRIER)) if mask & (1 << index)}
        closed = mac_close_l(order, subset)
        if frozenset(subset) == closed:
            cuts.add(closed)
    return sorted(cuts, key=lambda cut: (len(cut), tuple(CARRIER.index(x) for x in cut)))


def principal_cuts(order: frozenset[tuple[str, str]]) -> dict[str, frozenset[str]]:
    return {x: mac_close_l(order, {x}) for x in CARRIER}


def principal_element(
    order: frozenset[tuple[str, str]],
    cut: frozenset[str],
) -> str | None:
    for element, principal in principal_cuts(order).items():
        if cut == principal:
            return element
    return None


def cut_order(cut: frozenset[str]) -> list[str]:
    return [x for x in CARRIER if x in cut]


def display_cut(cut: frozenset[str]) -> str:
    return "{ " + ", ".join(cut_order(cut)) + " }"


def all_total_maps() -> list[dict[str, str]]:
    return [
        {key: value for key, value in zip(CARRIER, values, strict=True)}
        for values in product(CARRIER, repeat=len(CARRIER))
    ]


def is_antitone(order: frozenset[tuple[str, str]], bt: dict[str, str]) -> bool:
    return all(
        not leq(order, x, y) or leq(order, bt[y], bt[x])
        for x in CARRIER
        for y in CARRIER
    )


def is_monotone(order: frozenset[tuple[str, str]], box: dict[str, str]) -> bool:
    return all(
        not leq(order, x, y) or leq(order, box[x], box[y])
        for x in CARRIER
        for y in CARRIER
    )


def completed_value_v1(
    order: frozenset[tuple[str, str]],
    bt: dict[str, str],
    cut: frozenset[str],
) -> frozenset[str]:
    return mac_close_lop(order, {bt[x] for x in cut})


def syntactic_fixed_points(
    order: frozenset[tuple[str, str]],
    bt: dict[str, str],
) -> list[str]:
    return [x for x in CARRIER if equiv(order, x, bt[x])]


def completed_fixed_points(
    order: frozenset[tuple[str, str]],
    bt: dict[str, str],
) -> list[dict]:
    rows: list[dict] = []
    for cut in closed_cuts(order):
        if completed_value_v1(order, bt, cut) != cut:
            continue
        element = principal_element(order, cut)
        rows.append(
            {
                "cut": cut_order(cut),
                "display": display_cut(cut),
                "principal": element is not None,
                "principalElement": element,
                "reflected": bool(element is not None and equiv(order, element, bt[element])),
            }
        )
    return rows


def classify_completion(order: frozenset[tuple[str, str]], bt: dict[str, str]) -> str:
    fixed = completed_fixed_points(order, bt)
    syntactic = syntactic_fixed_points(order, bt)
    nonprincipal = [row for row in fixed if not row["principal"]]
    principal_unreflected = [
        row for row in fixed if row["principal"] and not row["reflected"]
    ]
    reflected = [row for row in fixed if row["reflected"]]
    if not fixed:
        return "no-completion-fixed-point"
    if nonprincipal and not syntactic:
        return "nonprincipal-without-syntactic"
    if nonprincipal:
        return "nonprincipal-with-rounding-candidate"
    if principal_unreflected:
        return "principal-unreflected"
    if reflected:
        return "reflected-only"
    return "principal-only"


def least_upper_bounds(order: frozenset[tuple[str, str]], x: str, y: str) -> list[str]:
    candidates = [z for z in CARRIER if leq(order, x, z) and leq(order, y, z)]
    return [
        z
        for z in candidates
        if all(not (w != z and leq(order, w, z)) for w in candidates)
    ]


def greatest_lower_bounds(order: frozenset[tuple[str, str]], x: str, y: str) -> list[str]:
    candidates = [z for z in CARRIER if leq(order, z, x) and leq(order, z, y)]
    return [
        z
        for z in candidates
        if all(not (w != z and leq(order, z, w)) for w in candidates)
    ]


def is_lattice(order: frozenset[tuple[str, str]]) -> bool:
    return all(
        len(least_upper_bounds(order, x, y)) == 1
        and len(greatest_lower_bounds(order, x, y)) == 1
        for x in CARRIER
        for y in CARRIER
    )


def g2(order: frozenset[tuple[str, str]], bottom: str, top: str, bt: dict[str, str]) -> dict:
    antecedent = leq(order, bt[top], bottom)
    return {
        "antecedentBoxtimesTopLeBottom": antecedent,
        "holds": (not antecedent) or leq(order, top, bottom),
        "mode": "vacuous" if not antecedent else "antecedent-true",
    }


def fg2(order: frozenset[tuple[str, str]], top: str, bt: dict[str, str]) -> bool:
    return leq(order, bt[bt[top]], bt[top])


def aps_axioms(
    order: frozenset[tuple[str, str]],
    bottom: str,
    top: str,
    bt: dict[str, str],
    box: dict[str, str],
) -> dict:
    a1_box = is_monotone(order, box)
    a1_bt = is_antitone(order, bt)
    a2 = leq(order, top, bt[bottom])
    a3_counterexamples = []
    target = bt[top]
    for x in CARRIER:
        for y in CARRIER:
            if leq(order, x, box[y]) and leq(order, x, bt[y]) and not leq(order, x, target):
                a3_counterexamples.append(
                    {
                        "x": x,
                        "y": y,
                        "boxY": box[y],
                        "boxtimesY": bt[y],
                        "boxtimesTop": target,
                    }
                )
    a4_counterexamples = []
    for x in CARRIER:
        if not leq(order, bt[x], box[bt[x]]):
            a4_counterexamples.append(
                {
                    "x": x,
                    "boxtimesX": bt[x],
                    "boxBoxtimesX": box[bt[x]],
                }
            )
    a3 = not a3_counterexamples
    a4 = not a4_counterexamples
    return {
        "A1BoxMonotone": a1_box,
        "A1BoxtimesAntitone": a1_bt,
        "A2TopLeBoxtimesBottom": a2,
        "A3CollisionCut": a3,
        "A3Counterexamples": a3_counterexamples,
        "A4BoxtimesLeBoxBoxtimes": a4,
        "A4Counterexamples": a4_counterexamples,
        "A124Core": a1_box and a1_bt and a2 and a4,
        "APS": a1_box and a1_bt and a2 and a3 and a4,
    }


def profile_key(row: dict) -> str:
    return json.dumps(
        {
            "order": row["order"],
            "bottom": row["bottom"],
            "top": row["top"],
            "boxtimes": row["boxtimes"],
        },
        sort_keys=True,
    )


def compact_example(row: dict | None) -> dict | None:
    if row is None:
        return None
    return {
        "order": row["order"],
        "bottom": row["bottom"],
        "top": row["top"],
        "isLattice": row["isLattice"],
        "boxtimes": row["boxtimes"],
        "box": row["box"],
        "G2": row["G2"],
        "FG2": row["FG2"],
        "apsAxioms": row["apsAxioms"],
        "completionFixedPoints": row["completionFixedPoints"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass113-four-element-macneille-g2-boundary-check.json",
    )
    args = parser.parse_args()

    all_maps = all_total_maps()
    posets = labelled_posets()
    bottomed_posets = [order for order in posets if bottom_of(order) is not None]

    condition_names = (
        "separation",
        "separationAndG2",
        "separationAndG2AndA2",
        "separationAndG2AndA124Core",
        "separationAndG2AndAPS",
        "separationAndAPSButNotG2",
    )
    counts = {
        name: {"tableCount": 0, "profileKeys": set(), "posetKeys": set()}
        for name in condition_names
    }
    non_lattice_counts = {
        name: {"tableCount": 0, "profileKeys": set(), "posetKeys": set()}
        for name in condition_names
    }
    examples: dict[str, dict | None] = {
        "g2A2Separation": None,
        "g2A124Separation": None,
        "g2APSSeparation": None,
        "apsButNotG2Separation": None,
        "nonLatticeG2A2Separation": None,
    }

    total_antitone_maps = 0
    total_separating_profiles = 0
    total_top_profiles = 0
    total_tables_scanned_after_separation = 0

    def add_count(name: str, row: dict) -> None:
        counts[name]["tableCount"] += 1
        counts[name]["profileKeys"].add(profile_key(row))
        counts[name]["posetKeys"].add(row["order"])
        if not row["isLattice"]:
            non_lattice_counts[name]["tableCount"] += 1
            non_lattice_counts[name]["profileKeys"].add(profile_key(row))
            non_lattice_counts[name]["posetKeys"].add(row["order"])

    def maybe_example(name: str, row: dict) -> None:
        if examples[name] is None:
            examples[name] = compact_example(row)

    for order in bottomed_posets:
        bottom = bottom_of(order)
        assert bottom is not None
        order_rows = [[x, y] for x, y in sorted(order)]
        order_id = relation_key(order)
        lattice = is_lattice(order)
        top_candidates = [x for x in CARRIER if x != bottom]
        antitone_maps = [mapping for mapping in all_maps if is_antitone(order, mapping)]
        total_antitone_maps += len(antitone_maps)

        for bt in antitone_maps:
            completion_class = classify_completion(order, bt)
            if completion_class != "nonprincipal-without-syntactic":
                continue
            total_separating_profiles += 1
            fixed_points = completed_fixed_points(order, bt)
            syntactic = syntactic_fixed_points(order, bt)
            for top in top_candidates:
                total_top_profiles += 1
                g2_value = g2(order, bottom, top, bt)
                fg2_value = fg2(order, top, bt)
                for box in all_maps:
                    total_tables_scanned_after_separation += 1
                    ax = aps_axioms(order, bottom, top, bt, box)
                    row = {
                        "order": order_id,
                        "orderPairs": order_rows,
                        "bottom": bottom,
                        "top": top,
                        "isLattice": lattice,
                        "boxtimes": bt,
                        "box": box,
                        "G2": g2_value,
                        "FG2": fg2_value,
                        "syntacticFixedPoints": syntactic,
                        "completionClassification": completion_class,
                        "completionFixedPoints": fixed_points,
                        "apsAxioms": ax,
                    }
                    add_count("separation", row)
                    if g2_value["holds"]:
                        add_count("separationAndG2", row)
                        if ax["A2TopLeBoxtimesBottom"]:
                            add_count("separationAndG2AndA2", row)
                            maybe_example("g2A2Separation", row)
                            if not lattice:
                                maybe_example("nonLatticeG2A2Separation", row)
                        if ax["A124Core"]:
                            add_count("separationAndG2AndA124Core", row)
                            maybe_example("g2A124Separation", row)
                        if ax["APS"]:
                            add_count("separationAndG2AndAPS", row)
                            maybe_example("g2APSSeparation", row)
                    elif ax["APS"]:
                        add_count("separationAndAPSButNotG2", row)
                        maybe_example("apsButNotG2Separation", row)

    def finalize(counter: dict[str, dict]) -> dict[str, dict]:
        return {
            name: {
                "tableCount": value["tableCount"],
                "refutabilityProfileCount": len(value["profileKeys"]),
                "posetCount": len(value["posetKeys"]),
            }
            for name, value in counter.items()
        }

    package_counts = finalize(counts)
    non_lattice_package_counts = finalize(non_lattice_counts)
    found_g2_a2 = package_counts["separationAndG2AndA2"]["tableCount"] > 0
    found_g2_aps = package_counts["separationAndG2AndAPS"]["tableCount"] > 0

    report = {
        "pass": 113,
        "title": "Four-element poset MacNeille G2/A2 boundary search",
        "scope": {
            "carrier": list(CARRIER),
            "enumerated": "all labelled four-element posets with a unique bottom",
            "notEnumerated": [
                "non-antisymmetric preorders",
                "residual operations",
                "completion-stability assumptions",
            ],
            "extensionRule": "antitone-dual-lower-cut-v1",
        },
        "searchSpace": {
            "labelledPosets": len(posets),
            "uniqueBottomPosets": len(bottomed_posets),
            "nonLatticeUniqueBottomPosets": sum(
                1 for order in bottomed_posets if not is_lattice(order)
            ),
            "totalMapsPerOperator": len(all_maps),
            "antitoneMapsAcrossPosets": total_antitone_maps,
            "separatingRefutabilityProfiles": total_separating_profiles,
            "separatingTopProfiles": total_top_profiles,
            "boxTablesScannedAfterSeparation": total_tables_scanned_after_separation,
        },
        "packageCounts": package_counts,
        "nonLatticePackageCounts": non_lattice_package_counts,
        "examples": examples,
        "interpretation": {
            "boundaryOutcome": (
                "A four-element poset witness with separation+G2+A2 exists."
                if found_g2_a2
                else "No separation+G2+A2 witness was found in the labelled four-element poset scope."
            ),
            "apsOutcome": (
                "A four-element poset witness with separation+G2+finite A1-A4 APS exists."
                if found_g2_aps
                else "No separation+G2+finite A1-A4 APS witness was found in the labelled four-element poset scope."
            ),
            "sourceGap": (
                "Residual operations and completion-stability hypotheses remain unchecked; "
                "the result is finite order/table evidence only."
            ),
        },
        "residuationStatus": "not checked",
        "completionStabilityStatus": "not checked",
        "checks": {
            "enumeratedSomeBottomedPosets": len(bottomed_posets) > 0,
            "searchedAllBoxTablesForSeparatingProfiles": (
                total_tables_scanned_after_separation
                == total_top_profiles * len(all_maps)
            ),
            "countsAreMonotone": (
                package_counts["separation"]["tableCount"]
                >= package_counts["separationAndG2"]["tableCount"]
                >= package_counts["separationAndG2AndA2"]["tableCount"]
            ),
            "nonLatticeCountsBoundedByAllCounts": all(
                non_lattice_package_counts[name]["tableCount"]
                <= package_counts[name]["tableCount"]
                for name in condition_names
            ),
        },
    }
    report["overall"] = "PASS" if all(report["checks"].values()) else "FAIL"

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"wrote {output_path}")
    print(f"overall {report['overall']}")
    print(report["interpretation"]["boundaryOutcome"])
    print(report["interpretation"]["apsOutcome"])


if __name__ == "__main__":
    main()
