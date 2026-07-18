#!/usr/bin/env python3
"""Enumerate modal principles on small integral commutative residuated chains."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from collections import Counter
from pathlib import Path


PRINCIPLES = (
    "normality", "M", "K", "4", "T", "CP", "C", "CtrBox", "D",
    "Con_L_sem", "Con_EG_elem", "disjunction", "Lob", "sLob", "FLob",
    "SC_elem", "negBoxFP_elem",
)

PRINCIPLES = tuple("D_derived" if name == "D" else name for name in PRINCIPLES)

DEFINITIONS = {
    "normality": "box(top) = top",
    "M": "x <= y implies box(x) <= box(y)",
    "K": "box(x -> y) <= (box(x) -> box(y))",
    "4": "box(x) <= box(box(x))",
    "T": "box(x) <= x",
    "CP": "x <= box(x)",
    "C": "box(x) tensor box(y) <= box(x tensor y)",
    "CtrBox": "box(x) <= box(x) tensor box(x); not global contraction",
    "D_derived": "box(x) <= neg(box(neg(x))); diamond is derived",
    "Con_L_sem": "box(bottom) <= bottom; semantic reading of not box bottom",
    "Con_EG_elem": "there exists an algebra element x with box(x) <= bottom",
    "disjunction": "box(x join y) = box(x) join box(y)",
    "Lob": "box(x) <= x implies top <= x",
    "sLob": "(box(x) -> x) <= x",
    "FLob": "box(box(x) -> x) <= box(x)",
    "SC_elem": "for every algebra element x there is p with p = box(p) -> x",
    "negBoxFP_elem": "there is an algebra element p with p = neg(box(p))",
}

CONDITIONAL_CLAIMS = {
    "M+C=>K": (("M", "C"), "K"),
    "normality+D_derived=>Con_L_sem": (("normality", "D_derived"), "Con_L_sem"),
    "normality+FLob=>Lob": (("normality", "FLob"), "Lob"),
    "M+FLob=>SC_elem": (("M", "FLob"), "SC_elem"),
    "M+normality+K+4+CtrBox+SC_elem=>Lob": (
        ("M", "normality", "K", "4", "CtrBox", "SC_elem"), "Lob"
    ),
    "M+normality+K+4+CtrBox+Lob=>FLob": (
        ("M", "normality", "K", "4", "CtrBox", "Lob"), "FLob"
    ),
}


def algebra(family: str, n: int):
    top = n - 1
    if family == "godel":
        tensor = min

        def implication(x: int, y: int) -> int:
            return top if x <= y else y
    elif family == "lukasiewicz":
        def tensor(x: int, y: int) -> int:
            return max(0, x + y - top)

        def implication(x: int, y: int) -> int:
            return min(top, top - x + y)
    else:
        raise ValueError(family)
    return top, tensor, implication


def evaluate(box: tuple[int, ...], family: str) -> dict[str, bool]:
    n = len(box)
    values = range(n)
    top, tensor, implication = algebra(family, n)
    neg = lambda x: implication(x, 0)

    result = {
        "normality": box[top] == top,
        "M": all(x > y or box[x] <= box[y] for x in values for y in values),
        "K": all(box[implication(x, y)] <= implication(box[x], box[y])
                 for x in values for y in values),
        "4": all(box[x] <= box[box[x]] for x in values),
        "T": all(box[x] <= x for x in values),
        "CP": all(x <= box[x] for x in values),
        "C": all(tensor(box[x], box[y]) <= box[tensor(x, y)]
                 for x in values for y in values),
        "CtrBox": all(box[x] <= tensor(box[x], box[x]) for x in values),
        "D_derived": all(box[x] <= neg(box[neg(x)]) for x in values),
        "Con_L_sem": box[0] == 0,
        "Con_EG_elem": any(box[x] == 0 for x in values),
        "disjunction": all(box[max(x, y)] == max(box[x], box[y])
                           for x in values for y in values),
        "Lob": all(not (box[x] <= x) or x == top for x in values),
        "sLob": all(implication(box[x], x) <= x for x in values),
        "FLob": all(box[implication(box[x], x)] <= box[x] for x in values),
        "SC_elem": all(any(p == implication(box[p], x) for p in values) for x in values),
        "negBoxFP_elem": any(p == neg(box[p]) for p in values),
    }
    return result


def census(max_size: int) -> dict:
    models = []
    counts: dict[str, Counter] = {}
    for family in ("godel", "lukasiewicz"):
        for n in range(2, max_size + 1):
            key = f"{family}-{n}"
            counts[key] = Counter()
            for box in itertools.product(range(n), repeat=n):
                truth = evaluate(box, family)
                for name, holds in truth.items():
                    counts[key][name] += int(holds)
                models.append({"family": family, "size": n, "box": list(box), "truth": truth})

    implications = {}
    for left in PRINCIPLES:
        for right in PRINCIPLES:
            if left == right:
                continue
            witness = next((m for m in models if m["truth"][left] and not m["truth"][right]), None)
            key = f"{left}=>{right}"
            implications[key] = {
                "holds_in_census": witness is None,
                "counterexample": None if witness is None else {
                    "family": witness["family"], "size": witness["size"], "box": witness["box"]
                },
            }

    conditional_claims = {}
    for name, (antecedents, conclusion) in CONDITIONAL_CLAIMS.items():
        witness = next((
            m for m in models
            if all(m["truth"][item] for item in antecedents)
            and not m["truth"][conclusion]
        ), None)
        supporting_models = sum(
            1 for m in models if all(m["truth"][item] for item in antecedents)
        )
        conditional_claims[name] = {
            "holds_in_census": witness is None,
            "supporting_models": supporting_models,
            "counterexample": None if witness is None else {
                "family": witness["family"], "size": witness["size"], "box": witness["box"]
            },
        }

    return {
        "reproducibility": {
            "command": "python code/scripts/check-rams-principles.py --max-size 4",
            "python_version": platform.python_version(),
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "external_dependencies": [],
        },
        "scope": {
            "families": ["finite Godel chains", "finite Lukasiewicz chains"],
            "sizes": list(range(2, max_size + 1)),
            "box_maps": "all unary maps",
            "semantics": "algebra-element semantics; no syntactic definability claim",
            "base": "bounded integral commutative residuated chains",
            "warning": "Census evidence is not a proof of a general implication.",
        },
        "definitions": DEFINITIONS,
        "counts": {key: {name: value for name, value in sorted(counter.items())}
                   for key, counter in counts.items()},
        "implications": implications,
        "conditional_claims": conditional_claims,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", type=int, default=4)
    parser.add_argument("--output", type=Path,
                        default=Path("artifacts/reports/rams-principle-chain-census.json"))
    args = parser.parse_args()
    if args.max_size < 2 or args.max_size > 6:
        parser.error("--max-size must be between 2 and 6")
    report = census(args.max_size)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
