#!/usr/bin/env python3
"""
Search finite tensor/residual expansions of a preAPS order.

For each selected unit e, the script enumerates binary operations tensor with
e as a two-sided unit, then keeps exactly those that are associative, monotone
in both arguments, and admit both residuals:

    a tensor b <= c  iff  b <= a\\c  iff  a <= c/b.

Residual existence is checked order-theoretically: for each fixed a,c, the set
{b : a tensor b <= c} must be a principal downset, and similarly on the right.
"""

import argparse
import json
from itertools import product


def transitive_closure(carrier, pairs):
    order = {(x, y) for x, y in pairs}
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


def load_model(path):
    with open(path, encoding="utf-8-sig") as handle:
        model = json.load(handle)
    carrier = [str(x) for x in model["carrier"]]
    order = transitive_closure(carrier, [(str(x), str(y)) for x, y in model["order"]])
    return model, carrier, order


def make_downsets(carrier, order):
    def leq(x, y):
        return (x, y) in order

    principal_by_key = {}
    for r in carrier:
        principal_by_key[set_key(x for x in carrier if leq(x, r))] = r
    return principal_by_key


def search_for_unit(carrier, order, unit, max_operations, keep):
    def leq(x, y):
        return (x, y) in order

    unknown = [(a, b) for a in carrier for b in carrier if a != unit and b != unit]
    total = len(carrier) ** len(unknown)
    if total > max_operations:
        return {
            "unit": unit,
            "searched": False,
            "operation_space": total,
            "reason": f"operation space exceeds max_operations={max_operations}",
            "candidate_count": None,
            "examples": [],
        }

    principal_by_key = make_downsets(carrier, order)
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

        for (a, b), value in zip(unknown, values):
            tensor[a][b] = value

        associative = True
        for a in carrier:
            for b in carrier:
                for c in carrier:
                    if tensor[tensor[a][b]][c] != tensor[a][tensor[b][c]]:
                        associative = False
                        break
                if not associative:
                    break
            if not associative:
                break
        if not associative:
            continue

        monotone = True
        for a in carrier:
            for a2 in carrier:
                if leq(a, a2):
                    for b in carrier:
                        if not leq(tensor[a][b], tensor[a2][b]):
                            monotone = False
                            break
                if not monotone:
                    break
            if not monotone:
                break
        if not monotone:
            continue

        for b in carrier:
            for b2 in carrier:
                if leq(b, b2):
                    for a in carrier:
                        if not leq(tensor[a][b], tensor[a][b2]):
                            monotone = False
                            break
                if not monotone:
                    break
            if not monotone:
                break
        if not monotone:
            continue

        left_residual = {a: {} for a in carrier}
        right_residual = {b: {} for b in carrier}
        residuated = True

        for a in carrier:
            for c in carrier:
                downset = [b for b in carrier if leq(tensor[a][b], c)]
                residual = principal_by_key.get(set_key(downset))
                if residual is None:
                    residuated = False
                    break
                left_residual[a][c] = residual
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
                right_residual[b][c] = residual
            if not residuated:
                break
        if not residuated:
            continue

        candidate_count += 1
        if len(examples) < keep:
            examples.append(
                {
                    "unit": unit,
                    "tensor": tensor,
                    "leftResidual": left_residual,
                    "rightResidual": right_residual,
                }
            )

    return {
        "unit": unit,
        "searched": True,
        "operation_space": total,
        "candidate_count": candidate_count,
        "examples": examples,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("--unit", action="append", help="Unit element to test; defaults to every carrier element.")
    parser.add_argument("--max-operations", type=int, default=1_000_000)
    parser.add_argument("--keep", type=int, default=1)
    parser.add_argument("--output")
    args = parser.parse_args()

    model, carrier, order = load_model(args.model_path)
    units = args.unit or carrier
    bad_units = [unit for unit in units if unit not in carrier]
    if bad_units:
        raise SystemExit(f"Unknown unit(s): {', '.join(bad_units)}")

    results = [search_for_unit(carrier, order, unit, args.max_operations, args.keep) for unit in units]
    total_candidates = sum(r["candidate_count"] or 0 for r in results)

    report = {
        "model": model.get("name", args.model_path),
        "modelPath": args.model_path,
        "carrierSize": len(carrier),
        "searchedUnits": units,
        "maxOperations": args.max_operations,
        "totalCandidates": total_candidates,
        "results": results,
        "conclusion": "full-residuated-expansion-found" if total_candidates else "no-full-residuated-expansion-found",
    }

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
