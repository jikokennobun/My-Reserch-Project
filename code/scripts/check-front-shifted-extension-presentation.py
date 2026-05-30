#!/usr/bin/env python3
"""
Check the ideal-extension presentation of the front-shifted B_N tensor.

For the front-shifted models, the front ideal

    I = {b, a1, a2}

is a two-sided tensor ideal.  Collapsing I to the zero b leaves the shifted
tail monoid on {b, T, U, s, a(N+1), a3, ..., aN}.  This script verifies that
presentation for finite generated instances.
"""

import argparse
import json
import re


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


def infer_depth(carrier):
    indices = []
    for element in carrier:
        match = re.fullmatch(r"a([0-9]+)", element)
        if match:
            indices.append(int(match.group(1)))
    if not indices:
        raise ValueError("No ai orbit elements found")
    last = max(indices)
    expected = set(range(1, last + 1))
    if set(indices) != expected:
        raise ValueError(f"Orbit elements are not contiguous: {sorted(indices)}")
    return last - 1


def quotient_name(element):
    return "b" if element in {"b", "a1", "a2"} else element


def tail_product(depth, a, b):
    zero = "b"
    unit = "T"
    absorber = "U"
    if a == zero or b == zero:
        return zero
    if a == unit:
        return b
    if b == unit:
        return a
    if a == absorber or b == absorber:
        return absorber

    last_atom = f"a{depth + 1}"
    exponent = {"s": 1, last_atom: 1}
    by_exponent = {1: last_atom}
    for index in range(3, depth + 1):
        exponent[f"a{index}"] = index - 1
        by_exponent[index - 1] = f"a{index}"

    total = exponent[a] + exponent[b]
    if total <= depth - 1:
        return by_exponent[total]
    return absorber


def analyze(path):
    with open(path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    tensor = model["tensor"]
    depth = infer_depth(carrier)
    order = transitive_closure(carrier, model["order"])

    ideal = {"b", "a1", "a2"}
    front = {"a1", "a2"}
    tail_representatives = [
        "b",
        "T",
        "U",
        "s",
        f"a{depth + 1}",
        *[f"a{index}" for index in range(3, depth + 1)],
    ]
    tail_representatives = [x for x in tail_representatives if x in carrier]

    failures = []

    for y in ideal:
        for x in carrier:
            if leq(order, x, y) and x not in ideal:
                failures.append({"check": "order-ideal", "witness": [x, y]})

    for i in ideal:
        for x in carrier:
            if tensor[i][x] not in ideal or tensor[x][i] not in ideal:
                failures.append(
                    {
                        "check": "two-sided-tensor-ideal",
                        "witness": [i, x, tensor[i][x], tensor[x][i]],
                    }
                )

    expected_front = {
        ("a1", "a1"): "a1",
        ("a2", "a2"): "a2",
        ("a1", "a2"): "b",
        ("a2", "a1"): "b",
    }
    for (a, b), expected in expected_front.items():
        if tensor[a][b] != expected:
            failures.append({"check": "front-zero-band", "witness": [a, b, tensor[a][b], expected]})

    for p in front:
        for x in carrier:
            if x in {"b"}:
                expected = "b"
            elif x in front - {p}:
                expected = "b"
            else:
                expected = p
            if tensor[p][x] != expected:
                failures.append({"check": "front-action", "witness": [p, x, tensor[p][x], expected]})

    for x in tail_representatives:
        for y in tail_representatives:
            actual = quotient_name(tensor[x][y])
            expected = tail_product(depth, x, y)
            if actual != expected:
                failures.append({"check": "tail-quotient-product", "witness": [x, y, actual, expected]})

    quotient_order_failures = []
    for x in tail_representatives:
        for y in tail_representatives:
            if leq(order, x, y) and (x, y) not in {
                (z, z) for z in tail_representatives
            } | {
                ("b", z) for z in tail_representatives
            } | {
                (z, "U") for z in tail_representatives
            } | {
                ("s", f"a{depth + 1}")
            }:
                quotient_order_failures.append([x, y])
    if quotient_order_failures:
        failures.append({"check": "tail-quotient-order-shape", "witnesses": quotient_order_failures[:8]})

    return {
        "model": model.get("name", path),
        "path": path,
        "depth": depth,
        "ideal": sorted(ideal),
        "tailQuotientRepresentatives": tail_representatives,
        "checks": {
            "orderIdeal": not any(f["check"] == "order-ideal" for f in failures),
            "twoSidedTensorIdeal": not any(f["check"] == "two-sided-tensor-ideal" for f in failures),
            "frontZeroBand": not any(f["check"] == "front-zero-band" for f in failures),
            "frontAction": not any(f["check"] == "front-action" for f in failures),
            "tailQuotientProduct": not any(f["check"] == "tail-quotient-product" for f in failures),
            "tailQuotientOrderShape": not any(f["check"] == "tail-quotient-order-shape" for f in failures),
        },
        "failureCount": len(failures),
        "failures": failures[:20],
        "conclusion": "ideal-extension-presentation-verified" if not failures else "presentation-check-failed",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_paths", nargs="+")
    parser.add_argument("--output")
    args = parser.parse_args()

    entries = [analyze(path) for path in args.model_paths]
    report = {
        "presentation": {
            "name": "front-shifted-ideal-extension",
            "ideal": "I={b,a1,a2}",
            "quotient": "collapse I to b; remaining representatives carry the shifted tail tensor",
            "interpretation": "local front contraction lives in I, while the quotient tail preserves resource-sensitive truncated addition",
        },
        "summary": {
            "modelsChecked": len(entries),
            "verified": [entry["model"] for entry in entries if entry["failureCount"] == 0],
            "failed": [entry["model"] for entry in entries if entry["failureCount"] != 0],
        },
        "entries": entries,
    }

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
