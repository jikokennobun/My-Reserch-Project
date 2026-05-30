#!/usr/bin/env python3
"""
Analyze structural rules for finite residuated APS tensors.

The report follows the G2-ZOO note's Axis III conventions:

    E: exchange/commutativity, a*b = b*a
    C: contraction, a*a <= a
    W: weakening, a <= b implies a*c <= b

The script also reports the reflexive-instance form of weakening
("discarding"), a*c <= a, because W fails exactly there in many resource
examples and those witnesses are easier to inspect.
"""

import argparse
import json


def order_key(a, b):
    return f"{a}\t{b}"


def transitive_closure(carrier, pairs):
    order = {order_key(str(a), str(b)) for a, b in pairs}
    for x in carrier:
        order.add(order_key(x, x))
    changed = True
    while changed:
        changed = False
        entries = [tuple(item.split("\t")) for item in order]
        for a, b in entries:
            for c, d in entries:
                if b == c and order_key(a, d) not in order:
                    order.add(order_key(a, d))
                    changed = True
    return order


def leq(order, a, b):
    return order_key(a, b) in order


def analyze_model(path, max_witnesses):
    with open(path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    tensor = model.get("tensor")
    if tensor is None:
        return {
            "model": model.get("name", path),
            "path": path,
            "hasTensor": False,
            "conclusion": "no-tensor-to-analyze",
        }

    order = transitive_closure(carrier, model["order"])

    exchange_failures = []
    for a in carrier:
        for b in carrier:
            if tensor[a][b] != tensor[b][a]:
                exchange_failures.append(
                    {"a": a, "b": b, "aTensorB": tensor[a][b], "bTensorA": tensor[b][a]}
                )

    contraction_failures = []
    for a in carrier:
        product = tensor[a][a]
        if not leq(order, product, a):
            contraction_failures.append({"a": a, "aTensorA": product, "required": [product, a]})

    discarding_failures = []
    for a in carrier:
        for c in carrier:
            product = tensor[a][c]
            if not leq(order, product, a):
                discarding_failures.append({"a": a, "c": c, "aTensorC": product, "required": [product, a]})

    weakening_failures = []
    comparable_pairs = 0
    for a in carrier:
        for b in carrier:
            if not leq(order, a, b):
                continue
            comparable_pairs += 1
            for c in carrier:
                product = tensor[a][c]
                if not leq(order, product, b):
                    weakening_failures.append(
                        {
                            "a": a,
                            "b": b,
                            "c": c,
                            "aTensorC": product,
                            "assumption": [a, b],
                            "required": [product, b],
                        }
                    )

    return {
        "model": model.get("name", path),
        "path": path,
        "hasTensor": True,
        "carrierSize": len(carrier),
        "rules": {
            "E_exchange": {
                "holds": not exchange_failures,
                "failureCount": len(exchange_failures),
                "witnesses": exchange_failures[:max_witnesses],
            },
            "C_contraction": {
                "holds": not contraction_failures,
                "failureCount": len(contraction_failures),
                "witnesses": contraction_failures[:max_witnesses],
            },
            "W_weakening": {
                "holds": not weakening_failures,
                "failureCount": len(weakening_failures),
                "comparablePairsChecked": comparable_pairs,
                "witnesses": weakening_failures[:max_witnesses],
            },
            "discarding_reflexive_W": {
                "holds": not discarding_failures,
                "failureCount": len(discarding_failures),
                "witnesses": discarding_failures[:max_witnesses],
            },
        },
        "conclusion": "structural-rules-analyzed",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_paths", nargs="+")
    parser.add_argument("--output")
    parser.add_argument("--max-witnesses", type=int, default=8)
    args = parser.parse_args()

    entries = [analyze_model(path, args.max_witnesses) for path in args.model_paths]
    summary = {
        "modelsChecked": len(entries),
        "exchangeHolds": [entry["model"] for entry in entries if entry.get("rules", {}).get("E_exchange", {}).get("holds")],
        "contractionHolds": [entry["model"] for entry in entries if entry.get("rules", {}).get("C_contraction", {}).get("holds")],
        "weakeningHolds": [entry["model"] for entry in entries if entry.get("rules", {}).get("W_weakening", {}).get("holds")],
        "discardingHolds": [
            entry["model"] for entry in entries if entry.get("rules", {}).get("discarding_reflexive_W", {}).get("holds")
        ],
    }
    report = {
        "rules": {
            "E": "exchange/commutativity: a tensor b = b tensor a",
            "C": "contraction: a tensor a <= a",
            "W": "weakening: a <= b implies a tensor c <= b",
            "discarding": "reflexive weakening instance: a tensor c <= a",
        },
        "summary": summary,
        "entries": entries,
    }

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
