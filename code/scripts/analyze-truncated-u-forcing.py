#!/usr/bin/env python3
"""
Analyze whether U-absorption is forced once the truncated B_N orbit table is fixed.

This is not a full unrestricted tensor search. It fixes the truncated-exponent
products on A_N = {s, a1, ..., a(N+1)} and asks whether monotonicity against the
order x <= U already forces U * x = U for all nonzero non-unit x.
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
    if set(indices) != set(range(1, last + 1)):
        raise ValueError(f"Orbit elements are not contiguous: {sorted(indices)}")
    return last - 1


def truncated_orbit_product(depth):
    last_atom = f"a{depth + 1}"
    exponent = {"s": 1, last_atom: 1}
    by_exponent = {1: last_atom}
    for index in range(1, depth + 1):
        element = f"a{index}"
        exponent[element] = index + 1
        by_exponent[index + 1] = element

    def product(a, b):
        total = exponent[a] + exponent[b]
        if total <= depth + 1:
            return by_exponent[total]
        return "U"

    return product, exponent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("--unit", default="T")
    parser.add_argument("--zero", default="b")
    parser.add_argument("--absorber", default="U")
    parser.add_argument("--output")
    args = parser.parse_args()

    with open(args.model_path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    depth = infer_depth(carrier)
    order = transitive_closure(carrier, model["order"])
    unit = args.unit
    zero = args.zero
    absorber = args.absorber
    orbit = [x for x in carrier if x not in {unit, zero, absorber}]
    product, exponent = truncated_orbit_product(depth)

    if not all(leq(order, x, absorber) for x in carrier):
        raise SystemExit("Expected U to be top in the bottom-disciplined B_N model")

    forced = {}
    for y in orbit:
        witnesses = []
        for x in orbit:
            if leq(order, x, absorber) and product(x, y) == absorber:
                witnesses.append(
                    {
                        "lowerFactor": x,
                        "fixedProduct": f"{x} * {y} = {absorber}",
                        "monotoneStep": f"{x} <= {absorber} implies {absorber} <= {absorber} * {y}",
                    }
                )
        forced[y] = {
            "forcedValue": absorber if witnesses else None,
            "witnesses": witnesses,
        }

    forced_u_u = []
    for y, result in forced.items():
        if result["forcedValue"] == absorber and leq(order, y, absorber):
            forced_u_u.append(
                {
                    "lowerFactor": y,
                    "fixedOrForcedProduct": f"{absorber} * {y} = {absorber}",
                    "monotoneStep": f"{y} <= {absorber} implies {absorber} <= {absorber} * {absorber}",
                }
            )

    forced[absorber] = {
        "forcedValue": absorber if forced_u_u else None,
        "witnesses": forced_u_u,
    }

    all_forced = all(result["forcedValue"] == absorber for result in forced.values())

    report = {
        "model": model.get("name", args.model_path),
        "modelPath": args.model_path,
        "depth": depth,
        "assumptions": {
            "fixedOrbitTable": "truncated-exponent",
            "commutative": True,
            "unit": unit,
            "zero": zero,
            "absorber": absorber,
            "orderFact": "every carrier element is <= U",
            "notAssumed": "U * x = U",
        },
        "exponent": exponent,
        "forcedProducts": {f"{absorber} * {key}": value for key, value in forced.items()},
        "conclusion": (
            "u-absorption-forced-by-monotonicity-relative-to-truncated-orbit-table"
            if all_forced
            else "u-absorption-not-fully-forced-by-this-test"
        ),
    }

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
