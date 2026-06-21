#!/usr/bin/env python3
"""Pass 112 finite search: G2/APS boundary for MacNeille reflection.

The search is intentionally narrow.  It fixes the three-element non-lattice
carrier from Pass 111,

    0 < a, 0 < b,    a || b,

then enumerates distinguished non-bottom truth objects T in {a,b}, all total
antitone refutability maps, and all total Box maps.  For each finite table it
checks:

* v1 MacNeille completion fixed cuts;
* absence/presence of syntactic boxtimes fixed points;
* G2, FG2;
* finite-table APS axioms A1--A4.

This answers the first small boundary question: can the Pass-111
non-principal completion fixed point coexist with G2 on the same minimal
non-lattice carrier, and if so which APS axioms fail?
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path
from typing import Callable


Carrier = tuple[str, ...]
Map = dict[str, str]


CARRIER: Carrier = ("0", "a", "b")
ORDER = {
    ("0", "0"),
    ("a", "a"),
    ("b", "b"),
    ("0", "a"),
    ("0", "b"),
}
BOTTOM = "0"
TOP_CANDIDATES = ("a", "b")


def leq(x: str, y: str) -> bool:
    return (x, y) in ORDER


def equiv(x: str, y: str) -> bool:
    return leq(x, y) and leq(y, x)


def uppers(subset: set[str]) -> set[str]:
    return {candidate for candidate in CARRIER if all(leq(x, candidate) for x in subset)}


def lowers(subset: set[str]) -> set[str]:
    return {candidate for candidate in CARRIER if all(leq(candidate, x) for x in subset)}


def mac_close_l(subset: set[str]) -> frozenset[str]:
    return frozenset(lowers(uppers(subset)))


def mac_close_lop(subset: set[str]) -> frozenset[str]:
    return frozenset(uppers(lowers(subset)))


def all_closed_cuts() -> list[frozenset[str]]:
    out: set[frozenset[str]] = set()
    for mask in range(1 << len(CARRIER)):
        subset = {CARRIER[index] for index in range(len(CARRIER)) if mask & (1 << index)}
        closed = mac_close_l(subset)
        if frozenset(subset) == closed:
            out.add(closed)
    return sorted(out, key=lambda c: (len(c), tuple(CARRIER.index(x) for x in c)))


CLOSED_CUTS = all_closed_cuts()
PRINCIPAL_CUTS = {x: mac_close_l({x}) for x in CARRIER}


def principal_element(cut: frozenset[str]) -> str | None:
    for element, principal in PRINCIPAL_CUTS.items():
        if cut == principal:
            return element
    return None


def completed_value_v1(bt: Map, cut: frozenset[str]) -> frozenset[str]:
    image = {bt[x] for x in cut}
    return mac_close_lop(image)


def completed_fixed_points(bt: Map) -> list[dict]:
    rows: list[dict] = []
    for cut in CLOSED_CUTS:
        if completed_value_v1(bt, cut) != cut:
            continue
        element = principal_element(cut)
        reflected = bool(element is not None and equiv(element, bt[element]))
        rows.append(
            {
                "cut": list(cut_order(cut)),
                "display": display_cut(cut),
                "principal": element is not None,
                "principalElement": element,
                "reflected": reflected,
            }
        )
    return rows


def classify_completion(bt: Map) -> str:
    fixed = completed_fixed_points(bt)
    syntactic = syntactic_fixed_points(bt)
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


def cut_order(cut: frozenset[str]) -> list[str]:
    return [x for x in CARRIER if x in cut]


def display_cut(cut: frozenset[str]) -> str:
    return "{ " + ", ".join(cut_order(cut)) + " }"


def all_total_maps() -> list[Map]:
    maps = []
    for values in product(CARRIER, repeat=len(CARRIER)):
        maps.append({key: value for key, value in zip(CARRIER, values, strict=True)})
    return maps


def is_antitone(bt: Map) -> bool:
    return all(
        not leq(x, y) or leq(bt[y], bt[x])
        for x in CARRIER
        for y in CARRIER
    )


def is_monotone(box: Map) -> bool:
    return all(
        not leq(x, y) or leq(box[x], box[y])
        for x in CARRIER
        for y in CARRIER
    )


def syntactic_fixed_points(bt: Map) -> list[str]:
    return [x for x in CARRIER if equiv(x, bt[x])]


def g2(top: str, bt: Map) -> dict:
    antecedent = leq(bt[top], BOTTOM)
    return {
        "antecedentBoxtimesTopLeBottom": antecedent,
        "holds": (not antecedent) or leq(top, BOTTOM),
        "mode": "vacuous" if not antecedent else "antecedent-true",
    }


def fg2(top: str, bt: Map) -> bool:
    return leq(bt[bt[top]], bt[top])


def aps_axioms(top: str, bt: Map, box: Map) -> dict:
    a1_box = is_monotone(box)
    a1_bt = is_antitone(bt)
    a2 = leq(top, bt[BOTTOM])
    a3_counterexamples = []
    target = bt[top]
    for x in CARRIER:
        for y in CARRIER:
            if leq(x, box[y]) and leq(x, bt[y]) and not leq(x, target):
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
        if not leq(bt[x], box[bt[x]]):
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


def package_counts(rows: list[dict], predicate: Callable[[dict], bool]) -> dict:
    selected = [row for row in rows if predicate(row)]
    profile_keys = {
        json.dumps({"top": row["top"], "boxtimes": row["boxtimes"]}, sort_keys=True)
        for row in selected
    }
    return {
        "tableCount": len(selected),
        "refutabilityProfileCount": len(profile_keys),
    }


def first_row(rows: list[dict], predicate: Callable[[dict], bool]) -> dict | None:
    for row in rows:
        if predicate(row):
            return {
                "top": row["top"],
                "boxtimes": row["boxtimes"],
                "box": row["box"],
                "G2": row["G2"],
                "FG2": row["FG2"],
                "apsAxioms": row["apsAxioms"],
                "completionFixedPoints": row["completionFixedPoints"],
            }
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass112-macneille-g2-boundary-check.json",
    )
    args = parser.parse_args()

    all_maps = all_total_maps()
    rows: list[dict] = []
    for top in TOP_CANDIDATES:
        for bt in all_maps:
            if not is_antitone(bt):
                continue
            cfp_class = classify_completion(bt)
            if cfp_class != "nonprincipal-without-syntactic":
                continue
            for box in all_maps:
                ax = aps_axioms(top, bt, box)
                row = {
                    "top": top,
                    "bottom": BOTTOM,
                    "boxtimes": bt,
                    "box": box,
                    "G2": g2(top, bt),
                    "FG2": fg2(top, bt),
                    "syntacticFixedPoints": syntactic_fixed_points(bt),
                    "completionClassification": cfp_class,
                    "completionFixedPoints": completed_fixed_points(bt),
                    "apsAxioms": ax,
                }
                rows.append(row)

    sep = lambda row: row["completionClassification"] == "nonprincipal-without-syntactic"
    g2_sep = lambda row: sep(row) and row["G2"]["holds"]
    g2_a2_sep = lambda row: g2_sep(row) and row["apsAxioms"]["A2TopLeBoxtimesBottom"]
    g2_a124_sep = lambda row: g2_sep(row) and row["apsAxioms"]["A124Core"]
    g2_aps_sep = lambda row: g2_sep(row) and row["apsAxioms"]["APS"]
    aps_not_g2_sep = lambda row: sep(row) and row["apsAxioms"]["APS"] and not row["G2"]["holds"]

    report = {
        "pass": 112,
        "title": "G2/APS boundary for MacNeille completion-only fixed cuts",
        "carrier": list(CARRIER),
        "order": [[x, y] for x, y in sorted(ORDER)],
        "bottom": BOTTOM,
        "topCandidates": list(TOP_CANDIDATES),
        "closedCuts": [
            {
                "cut": list(cut_order(cut)),
                "display": display_cut(cut),
                "principalElement": principal_element(cut),
            }
            for cut in CLOSED_CUTS
        ],
        "searchSpace": {
            "totalMapsPerOperator": len(all_maps),
            "antitoneRefutabilityProfilesWithSeparation": package_counts(rows, sep)[
                "refutabilityProfileCount"
            ],
            "boxTablesPerProfile": len(all_maps),
            "rowsWithSeparation": package_counts(rows, sep)["tableCount"],
        },
        "packageCounts": {
            "separation": package_counts(rows, sep),
            "separationAndG2": package_counts(rows, g2_sep),
            "separationAndG2AndA2": package_counts(rows, g2_a2_sep),
            "separationAndG2AndA124Core": package_counts(rows, g2_a124_sep),
            "separationAndG2AndAPS": package_counts(rows, g2_aps_sep),
            "separationAndAPSButNotG2": package_counts(rows, aps_not_g2_sep),
        },
        "examples": {
            "g2Separation": first_row(rows, g2_sep),
            "g2A2Separation": first_row(rows, g2_a2_sep),
            "g2A124Separation": first_row(rows, g2_a124_sep),
            "g2APSSeparation": first_row(rows, g2_aps_sep),
            "apsButNotG2Separation": first_row(rows, aps_not_g2_sep),
        },
        "interpretation": {
            "smallPositive": (
                "On the Pass-111 three-element non-lattice carrier, there are "
                "vacuous-G2 separation rows if A2 is not required."
            ),
            "smallNoGo": (
                "No row on this carrier has nonprincipal-without-syntactic "
                "completion fixed cut, G2, and A2 simultaneously; hence none "
                "has G2 plus A124Core or full A1-A4 APS."
            ),
            "reason": (
                "The Pass-111 APS witness uses A2 and no syntactic fixed point, "
                "but its refutability sends the distinguished top to bottom, "
                "making the G2 antecedent true while the model is non-collapsed."
            ),
        },
        "checks": {
            "foundBareG2Separation": package_counts(rows, g2_sep)["tableCount"] > 0,
            "noG2A2SeparationOnCarrier": package_counts(rows, g2_a2_sep)["tableCount"]
            == 0,
            "noG2A124SeparationOnCarrier": package_counts(rows, g2_a124_sep)[
                "tableCount"
            ]
            == 0,
            "noG2APSSeparationOnCarrier": package_counts(rows, g2_aps_sep)[
                "tableCount"
            ]
            == 0,
            "pass111APSWitnessStillFailsG2": package_counts(rows, aps_not_g2_sep)[
                "tableCount"
            ]
            > 0,
        },
    }
    report["overall"] = "PASS" if all(report["checks"].values()) else "FAIL"

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"wrote {output_path}")
    print(f"overall {report['overall']}")


if __name__ == "__main__":
    main()
