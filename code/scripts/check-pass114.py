#!/usr/bin/env python3
"""
Pass 114 residual-boundary checker for the four-element MacNeille witness.

The checker keeps the Pass 113 carrier and order fixed, enumerates every
two-sided-unit tensor for each possible unit, and counts where candidates fail:
associativity, monotonicity, or existence of both order-theoretic residuals.
"""

import argparse
import json
from itertools import product
from pathlib import Path


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


def load_model(path):
    with open(path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    order_pairs = [(str(x), str(y)) for x, y in model["order"]]
    return model, carrier, transitive_closure(carrier, order_pairs)


def make_order_helpers(carrier, order):
    carrier_index = {value: index for index, value in enumerate(carrier)}

    def leq(left, right):
        return (left, right) in order

    def set_key(values):
        return tuple(value for value in carrier if value in values)

    principal_by_key = {}
    principal_downsets = {}
    for value in carrier:
        downset = set(x for x in carrier if leq(x, value))
        key = set_key(downset)
        principal_by_key[key] = value
        principal_downsets[value] = list(key)

    def ordered(values):
        return sorted(values, key=lambda value: carrier_index[value])

    return leq, set_key, principal_by_key, principal_downsets, ordered


def build_tensor(carrier, unit, unknown, values):
    tensor = {a: {} for a in carrier}
    for a in carrier:
        for b in carrier:
            if a == unit:
                tensor[a][b] = b
            elif b == unit:
                tensor[a][b] = a

    for (a, b), value in zip(unknown, values):
        tensor[a][b] = value
    return tensor


def is_associative(carrier, tensor):
    for a in carrier:
        for b in carrier:
            for c in carrier:
                if tensor[tensor[a][b]][c] != tensor[a][tensor[b][c]]:
                    return False
    return True


def monotonicity_obstruction(carrier, tensor, leq):
    for a in carrier:
        for a2 in carrier:
            if leq(a, a2):
                for b in carrier:
                    if not leq(tensor[a][b], tensor[a2][b]):
                        return {
                            "side": "left-argument",
                            "lower": a,
                            "upper": a2,
                            "fixed": b,
                            "lowerValue": tensor[a][b],
                            "upperValue": tensor[a2][b],
                        }

    for b in carrier:
        for b2 in carrier:
            if leq(b, b2):
                for a in carrier:
                    if not leq(tensor[a][b], tensor[a][b2]):
                        return {
                            "side": "right-argument",
                            "lower": b,
                            "upper": b2,
                            "fixed": a,
                            "lowerValue": tensor[a][b],
                            "upperValue": tensor[a][b2],
                        }
    return None


def residual_obstruction(carrier, tensor, leq, set_key, principal_by_key, ordered):
    left_residual = {a: {} for a in carrier}
    right_residual = {b: {} for b in carrier}

    for a in carrier:
        for c in carrier:
            fiber = set(b for b in carrier if leq(tensor[a][b], c))
            residual = principal_by_key.get(set_key(fiber))
            if residual is None:
                return {
                    "side": "left",
                    "fixedLeft": a,
                    "bound": c,
                    "fiber": ordered(fiber),
                    "condition": "{b : a tensor b <= c} is not a principal downset",
                }, None, None
            left_residual[a][c] = residual

    for b in carrier:
        for c in carrier:
            fiber = set(a for a in carrier if leq(tensor[a][b], c))
            residual = principal_by_key.get(set_key(fiber))
            if residual is None:
                return {
                    "side": "right",
                    "fixedRight": b,
                    "bound": c,
                    "fiber": ordered(fiber),
                    "condition": "{a : a tensor b <= c} is not a principal downset",
                }, None, None
            right_residual[b][c] = residual

    return None, left_residual, right_residual


def search_for_unit(carrier, unit, leq, set_key, principal_by_key, ordered, keep):
    unknown = [(a, b) for a in carrier for b in carrier if a != unit and b != unit]
    operation_space = len(carrier) ** len(unknown)
    result = {
        "unit": unit,
        "operationSpace": operation_space,
        "associativeCount": 0,
        "associativeMonotoneCount": 0,
        "fullResiduatedCount": 0,
        "firstMonotonicityObstruction": None,
        "firstResidualObstruction": None,
        "examples": [],
    }

    for values in product(carrier, repeat=len(unknown)):
        tensor = build_tensor(carrier, unit, unknown, values)
        if not is_associative(carrier, tensor):
            continue
        result["associativeCount"] += 1

        mono_obstruction = monotonicity_obstruction(carrier, tensor, leq)
        if mono_obstruction is not None:
            if result["firstMonotonicityObstruction"] is None:
                result["firstMonotonicityObstruction"] = {
                    "tensor": tensor,
                    "obstruction": mono_obstruction,
                }
            continue
        result["associativeMonotoneCount"] += 1

        resid_obstruction, left_residual, right_residual = residual_obstruction(
            carrier,
            tensor,
            leq,
            set_key,
            principal_by_key,
            ordered,
        )
        if resid_obstruction is not None:
            if result["firstResidualObstruction"] is None:
                result["firstResidualObstruction"] = {
                    "tensor": tensor,
                    "obstruction": resid_obstruction,
                }
            continue

        result["fullResiduatedCount"] += 1
        if len(result["examples"]) < keep:
            result["examples"].append(
                {
                    "tensor": tensor,
                    "leftResidual": left_residual,
                    "rightResidual": right_residual,
                }
            )

    return result


def summarize(results):
    totals = {
        "operationSpace": sum(item["operationSpace"] for item in results),
        "associativeCount": sum(item["associativeCount"] for item in results),
        "associativeMonotoneCount": sum(item["associativeMonotoneCount"] for item in results),
        "fullResiduatedCount": sum(item["fullResiduatedCount"] for item in results),
    }

    if totals["fullResiduatedCount"] > 0:
        obstruction = "full-residuated-expansion-found"
    elif totals["associativeMonotoneCount"] == 0:
        obstruction = "no-associative-monotone-two-sided-unit-tensor"
    else:
        obstruction = "non-principal-residual-fiber"

    return {
        **totals,
        "firstNamedObstruction": obstruction,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        default="code/models/examples/four-element-g2-aps-nosynt.json",
        help="Finite APS model to check.",
    )
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass114-four-element-residual-boundary-check.json",
        help="Where to write the JSON report.",
    )
    parser.add_argument("--keep", type=int, default=1)
    args = parser.parse_args()

    model, carrier, order = load_model(args.model)
    leq, set_key, principal_by_key, principal_downsets, ordered = make_order_helpers(carrier, order)

    results = [
        search_for_unit(carrier, unit, leq, set_key, principal_by_key, ordered, args.keep)
        for unit in carrier
    ]

    report = {
        "pass": 114,
        "model": model.get("name", Path(args.model).name),
        "modelPath": args.model,
        "scope": {
            "sameCarrier": True,
            "sameOrder": True,
            "twoSidedUnit": True,
            "associative": True,
            "monotoneInBothArguments": True,
            "leftAndRightResiduals": "principal-downset test",
        },
        "carrier": carrier,
        "principalDownsets": principal_downsets,
        "summary": summarize(results),
        "results": results,
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, indent=2, ensure_ascii=False)
    output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
