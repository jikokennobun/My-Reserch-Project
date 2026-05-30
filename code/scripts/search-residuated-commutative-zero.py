#!/usr/bin/env python3
"""
Search commutative finite tensor/residual expansions with a fixed unit and zero.

This is a targeted companion to search-residuated-tensor.py. It reduces the
search space by requiring:

  - a chosen two-sided unit e,
  - a chosen absorbing zero z,
  - commutativity.

The remaining operation entries are still checked for associativity,
monotonicity, and full left/right residuals. The script is useful for bounded
preAPS witnesses where unrestricted tensor enumeration is too large.
"""

import argparse
import json
from itertools import product


def transitive_closure(carrier, pairs):
    order = {(str(x), str(y)) for x, y in pairs}
    for x in carrier:
        order.add((x, x))
    changed = True
    while changed:
        changed = False
        for a, b in list(order):
            for c, d in list(order):
                if b == c and (a, d) not in order:
                    order.add((a, d))
                    changed = True
    return order


def set_key(values):
    return "\x1f".join(sorted(values))


def principal_downsets(carrier, order):
    def leq(x, y):
        return (x, y) in order

    return {
        set_key(x for x in carrier if leq(x, r)): r
        for r in carrier
    }


def search(model, carrier, order, unit, zero, max_operations, keep):
    def leq(x, y):
        return (x, y) in order

    free = [x for x in carrier if x not in (unit, zero)]
    unknown = []
    for index, a in enumerate(free):
        for b in free[index:]:
            unknown.append((a, b))

    operation_space = len(carrier) ** len(unknown)
    if operation_space > max_operations:
        return {
            "searched": False,
            "reason": f"operation space exceeds max_operations={max_operations}",
            "operationSpace": operation_space,
            "candidateCount": None,
            "examples": [],
        }

    principal_by_key = principal_downsets(carrier, order)
    candidate_count = 0
    examples = []

    for values in product(carrier, repeat=len(unknown)):
        tensor = {a: {} for a in carrier}
        for a in carrier:
            for b in carrier:
                if a == unit:
                    tensor[a][b] = b
                elif b == unit:
                    tensor[a][b] = a
                elif a == zero or b == zero:
                    tensor[a][b] = zero

        for (a, b), value in zip(unknown, values):
            tensor[a][b] = value
            tensor[b][a] = value

        if any(
            leq(a, a2) and not leq(tensor[a][b], tensor[a2][b])
            for a in carrier
            for a2 in carrier
            for b in carrier
        ):
            continue

        if any(
            tensor[tensor[a][b]][c] != tensor[a][tensor[b][c]]
            for a in carrier
            for b in carrier
            for c in carrier
        ):
            continue

        left = {a: {} for a in carrier}
        right = {b: {} for b in carrier}
        residuated = True

        for a in carrier:
            for c in carrier:
                downset = [b for b in carrier if leq(tensor[a][b], c)]
                residual = principal_by_key.get(set_key(downset))
                if residual is None:
                    residuated = False
                    break
                left[a][c] = residual
            if not residuated:
                break
        if not residuated:
            continue

        for b in carrier:
            for c in carrier:
                downset = [a for a in carrier if leq(tensor[a][b], c)]
                residual = principal_by_key.get(set_key(downset))
                if residual is None:
                    residuated = False
                    break
                right[b][c] = residual
            if not residuated:
                break
        if not residuated:
            continue

        candidate_count += 1
        if len(examples) < keep:
            examples.append(
                {
                    "unit": unit,
                    "zero": zero,
                    "tensor": tensor,
                    "leftResidual": left,
                    "rightResidual": right,
                }
            )

    return {
        "searched": True,
        "operationSpace": operation_space,
        "candidateCount": candidate_count,
        "examples": examples,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("--unit", required=True)
    parser.add_argument("--zero", required=True)
    parser.add_argument("--max-operations", type=int, default=1_000_000)
    parser.add_argument("--keep", type=int, default=1)
    parser.add_argument("--output")
    parser.add_argument("--expanded-model-output")
    args = parser.parse_args()

    with open(args.model_path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    if args.unit not in carrier:
        raise SystemExit(f"Unknown unit: {args.unit}")
    if args.zero not in carrier:
        raise SystemExit(f"Unknown zero: {args.zero}")

    order = transitive_closure(carrier, model["order"])
    result = search(model, carrier, order, args.unit, args.zero, args.max_operations, args.keep)
    conclusion = (
        "full-residuated-expansion-found"
        if result["searched"] and result["candidateCount"]
        else "no-full-residuated-expansion-found-in-searched-space"
        if result["searched"]
        else "search-not-run-operation-space-too-large"
    )

    report = {
        "model": model.get("name", args.model_path),
        "modelPath": args.model_path,
        "carrierSize": len(carrier),
        "assumptions": {
            "commutative": True,
            "unit": args.unit,
            "zero": args.zero,
        },
        "search": result,
        "conclusion": conclusion,
    }

    if args.expanded_model_output and result["examples"]:
        example = result["examples"][0]
        expanded = dict(model)
        expanded["name"] = f"{model.get('name', 'model')}-residuated"
        expanded["unit"] = example["unit"]
        expanded["tensor"] = example["tensor"]
        expanded["leftResidual"] = example["leftResidual"]
        expanded["rightResidual"] = example["rightResidual"]
        expanded["metadata"] = dict(model.get("metadata", {}))
        expanded["metadata"]["residuation"] = "full"
        expanded["metadata"]["residuation_search_report"] = args.output
        expanded["metadata"]["residuation_assumptions"] = "commutative tensor, fixed unit, fixed zero"
        with open(args.expanded_model_output, "w", encoding="utf-8") as handle:
            handle.write(json.dumps(expanded, indent=2, ensure_ascii=False) + "\n")

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
