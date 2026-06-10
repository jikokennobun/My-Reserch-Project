#!/usr/bin/env python3
"""
Pass 69 verification: consistency-tower, cut/A3, and infinite-model layer.

The checker gives finite certificates for the new G2-ZOO layer:

1. Cycle APS C_m:
   bot < o_i < top, boxtimes cycles the o_i, Box=id.
   These are genuine APS models with no boxtimes fixed point, G2 true
   vacuously, and nFG2(k) false at every checked level.

2. Detached Rosser period models R_{2k}:
   add a detached atom p with boxtimes(p)=p to C_{2k}.
   A1, A2, and A4 still hold, but A3 fails exactly at the detached fixed
   point. Thus primitive fixed points do not imply formalized G2 or cut
   closure.

3. The report records the APS-level consistency statement names introduced in
   the accompanying note.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple


Element = str
Leq = Set[Tuple[Element, Element]]
Map = Dict[Element, Element]


def diamond_order(elements: List[Element], atoms: Iterable[Element]) -> Leq:
    atoms = list(atoms)
    leq: Leq = {(x, x) for x in elements}
    for a in atoms:
        leq.add(("bot", a))
        leq.add((a, "top"))
    leq.add(("bot", "top"))
    return leq


def leq(leq_rel: Leq, x: Element, y: Element) -> bool:
    return (x, y) in leq_rel


def incomparable(leq_rel: Leq, x: Element, y: Element) -> bool:
    return x != y and not leq(leq_rel, x, y) and not leq(leq_rel, y, x)


def iterate(f: Map, x: Element, n: int) -> Element:
    for _ in range(n):
        x = f[x]
    return x


def orbit_support(f: Map, start: Element, max_steps: int = 200) -> List[Element]:
    seen: List[Element] = []
    x = start
    for _ in range(max_steps):
        if x in seen:
            return seen
        seen.append(x)
        x = f[x]
    raise RuntimeError("orbit did not repeat inside max_steps")


def is_monotone(elements: List[Element], leq_rel: Leq, f: Map) -> bool:
    for a in elements:
        for b in elements:
            if leq(leq_rel, a, b) and not leq(leq_rel, f[a], f[b]):
                return False
    return True


def is_antitone(elements: List[Element], leq_rel: Leq, f: Map) -> bool:
    for a in elements:
        for b in elements:
            if leq(leq_rel, a, b) and not leq(leq_rel, f[b], f[a]):
                return False
    return True


def a3_counterexamples(elements: List[Element], leq_rel: Leq, box: Map, bt: Map, T: Element) -> List[dict]:
    out: List[dict] = []
    target = bt[T]
    for x in elements:
        for y in elements:
            if leq(leq_rel, x, box[y]) and leq(leq_rel, x, bt[y]) and not leq(leq_rel, x, target):
                out.append({
                    "x": x,
                    "y": y,
                    "Box_y": box[y],
                    "boxtimes_y": bt[y],
                    "boxtimes_T": target,
                })
    return out


def aps_axioms(elements: List[Element], leq_rel: Leq, box: Map, bt: Map, T: Element) -> dict:
    a1_box = is_monotone(elements, leq_rel, box)
    a1_bt = is_antitone(elements, leq_rel, bt)
    a2 = leq(leq_rel, T, bt["bot"])
    a3_bad = a3_counterexamples(elements, leq_rel, box, bt, T)
    a4 = all(leq(leq_rel, bt[x], box[bt[x]]) for x in elements)
    return {
        "A1_Box_monotone": a1_box,
        "A1_boxtimes_antitone": a1_bt,
        "A2_T_le_boxtimes_bot": a2,
        "A3": len(a3_bad) == 0,
        "A3_counterexamples": a3_bad,
        "A4_boxtimes_x_le_Box_boxtimes_x": a4,
        "A124_core": a1_box and a1_bt and a2 and a4,
        "APS": a1_box and a1_bt and a2 and len(a3_bad) == 0 and a4,
    }


def g2(leq_rel: Leq, bt: Map, T: Element) -> dict:
    antecedent = leq(leq_rel, bt[T], "bot")
    return {
        "antecedent_boxtimes_T_le_bot": antecedent,
        "G2": (not antecedent) or leq(leq_rel, T, "bot"),
        "mode": "vacuous" if not antecedent else "antecedent-true",
    }


def nfg2_profile(leq_rel: Leq, bt: Map, T: Element, depth: int) -> dict:
    values = {}
    for k in range(1, depth + 1):
        lhs = iterate(bt, T, k + 1)
        rhs = iterate(bt, T, k)
        values[str(k)] = {
            "holds": leq(leq_rel, lhs, rhs),
            "lhs": lhs,
            "rhs": rhs,
        }
    return values


def fixed_points(elements: List[Element], bt: Map) -> List[Element]:
    return [x for x in elements if bt[x] == x]


def consistency_tower_profile(leq_rel: Leq, bt: Map, T: Element, depth: int) -> dict:
    tower = {}
    for n in range(1, depth + 1):
        c = iterate(bt, T, n)
        tower[str(n)] = {
            "Con_orb_n": c,
            "irrefutable": not leq(leq_rel, c, "bot"),
            "G2_n": (not leq(leq_rel, c, "bot")) or leq(leq_rel, T, "bot"),
        }
    return tower


def build_cycle_model(period: int, detached_fp: bool) -> dict:
    atoms = [f"o{i}" for i in range(period)]
    if detached_fp:
        atoms.append("p")
    elements = ["bot"] + atoms + ["top"]
    leq_rel = diamond_order(elements, atoms)
    box = {x: x for x in elements}
    bt: Map = {"bot": "top", "top": "bot"}
    for i in range(period):
        bt[f"o{i}"] = f"o{(i + 1) % period}"
    if detached_fp:
        bt["p"] = "p"

    T = "o0"
    depth = 2 * period + 2
    aps = aps_axioms(elements, leq_rel, box, bt, T)
    orb = orbit_support(bt, T)
    fps = fixed_points(elements, bt)
    detached_fps = [
        p for p in fps
        if all(incomparable(leq_rel, p, o) for o in orb)
    ]
    nfg2 = nfg2_profile(leq_rel, bt, T, depth)
    all_nfg2_false = all(not item["holds"] for item in nfg2.values())

    return {
        "period": period,
        "detached_fp_added": detached_fp,
        "carrier_size": len(elements),
        "T": T,
        "boxtimes_T": bt[T],
        "APS_axioms": aps,
        "G2": g2(leq_rel, bt, T),
        "orbit_support": orb,
        "orbit_flat_antichain": all(
            incomparable(leq_rel, a, b) for a in orb for b in orb if a != b
        ),
        "fixed_points": fps,
        "detached_fixed_points": detached_fps,
        "FP_synt": len(fps) > 0,
        "nFG2_depth_checked": depth,
        "nFG2": nfg2,
        "all_checked_nFG2_false": all_nfg2_false,
        "consistency_tower": consistency_tower_profile(leq_rel, bt, T, depth),
    }


def summarize_cycle_family(max_period: int) -> dict:
    models = [build_cycle_model(period, detached_fp=False) for period in range(2, max_period + 1)]
    return {
        "family": "C_m cycle APS, m=2..max_period",
        "max_period": max_period,
        "models": {f"C_{m['period']}": m for m in models},
        "all_APS": all(m["APS_axioms"]["APS"] for m in models),
        "all_no_FP": all(not m["FP_synt"] for m in models),
        "all_G2_true": all(m["G2"]["G2"] for m in models),
        "all_checked_nFG2_false": all(m["all_checked_nFG2_false"] for m in models),
        "verdict": "PASS" if all(
            m["APS_axioms"]["APS"]
            and not m["FP_synt"]
            and m["G2"]["G2"]
            and m["orbit_flat_antichain"]
            and m["all_checked_nFG2_false"]
            for m in models
        ) else "FAIL",
    }


def summarize_rosser_family(max_k: int) -> dict:
    models = [build_cycle_model(2 * k, detached_fp=True) for k in range(1, max_k + 1)]
    return {
        "family": "R_{2k} detached Rosser period preAPS, k=1..max_k",
        "max_k": max_k,
        "models": {f"R_{m['period']}": m for m in models},
        "all_A124_core": all(m["APS_axioms"]["A124_core"] for m in models),
        "all_A3_fail": all(not m["APS_axioms"]["A3"] for m in models),
        "all_FP_only_detached_p": all(m["fixed_points"] == ["p"] and m["detached_fixed_points"] == ["p"] for m in models),
        "all_G2_true": all(m["G2"]["G2"] for m in models),
        "all_checked_nFG2_false": all(m["all_checked_nFG2_false"] for m in models),
        "verdict": "PASS" if all(
            m["APS_axioms"]["A124_core"]
            and not m["APS_axioms"]["A3"]
            and m["fixed_points"] == ["p"]
            and m["detached_fixed_points"] == ["p"]
            and m["G2"]["G2"]
            and m["all_checked_nFG2_false"]
            for m in models
        ) else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-period", type=int, default=12)
    parser.add_argument("--max-k", type=int, default=6)
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass69-consistency-cut-infinite-g2-zoo-check.json",
    )
    args = parser.parse_args()

    if args.max_period < 2:
        raise SystemExit("--max-period must be >= 2")
    if args.max_k < 1:
        raise SystemExit("--max-k must be >= 1")

    cycle = summarize_cycle_family(args.max_period)
    rosser = summarize_rosser_family(args.max_k)

    report = {
        "pass_number": 69,
        "title": "consistency-tower, cut/A3, and infinite-model expansion of G2-ZOO",
        "statement_names": {
            "C_n": "C_0=T and C_{n+1}=boxtimes(C_n), the iterated APS consistency tower",
            "Con_orb_n": "C_n is not refutable, i.e. C_n not <= bot",
            "G2_n": "C_n <= bot implies T <= bot",
            "FG2_n": "C_{n+1} <= C_n; this is nFG2(n)",
            "Con_cut_A3": "x<=Box(y) and x<=boxtimes(y) imply x<=boxtimes(T)",
            "Con_flat_le_N": "the checked initial C_0..C_N orbit is flat except for equality",
        },
        "A_cycle_APS_no_fixed_point_family": cycle,
        "B_detached_rosser_period_family": rosser,
        "C_cut_boundary_diagnosis": {
            "minimal_failure": "Adding one detached boxtimes-fixed point p preserves A1/A2/A4 but breaks A3 at x=y=p.",
            "repair": "Deleting p returns the cycle model C_m, a genuine APS with the same flat consistency orbit.",
            "interpretation": "A3 is the algebraic cut/collision closure missing from the detached Rosser fixed point layer.",
        },
        "overall": "PASS" if cycle["verdict"] == "PASS" and rosser["verdict"] == "PASS" else "FAIL",
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
