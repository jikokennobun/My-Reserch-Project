#!/usr/bin/env python3
"""
Check how large an orthogonal front ideal can be in the shifted-tail schema.

For a bottom-disciplined B_N carrier and a chosen front size k, define

    F_k = {a1, ..., ak}

as an orthogonal idempotent zero-band.  Front elements project multiplication
with nonzero non-front elements back to themselves, while U fixes front elements
and absorbs the shifted tail.  The quotient tail uses shifted exponents on
{s, a(N+1), a(k+1), ..., aN}.

The pass-30 template is k=2.  This checker tests finite depths and front sizes
to locate the first obstruction to full residuation on the same order.
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


def principal_map(carrier, order):
    return {
        "\t".join(sorted(x for x in carrier if leq(order, x, r))): r
        for r in carrier
    }


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


def build_product(depth, front_size, unit="T", zero="b", absorber="U"):
    if front_size < 0 or front_size > depth:
        raise ValueError(f"front_size must be between 0 and depth {depth}")

    front = {f"a{i}" for i in range(1, front_size + 1)}
    last_atom = f"a{depth + 1}"
    tail_exponent = {"s": 1, last_atom: 1}
    by_exponent = {1: last_atom}
    for index in range(front_size + 1, depth + 1):
        element = f"a{index}"
        tail_exponent[element] = index - front_size + 1
        by_exponent[index - front_size + 1] = element
    threshold = depth - front_size + 1

    def product(a, b):
        if a == zero or b == zero:
            return zero
        if a == unit:
            return b
        if b == unit:
            return a
        if a in front and b in front:
            return a if a == b else zero
        if a in front and b != unit:
            return a
        if b in front and a != unit:
            return b
        if a == absorber or b == absorber:
            return absorber
        total = tail_exponent[a] + tail_exponent[b]
        if total <= threshold:
            return by_exponent[total]
        return absorber

    return product, {
        "front": sorted(front),
        "tail": sorted(tail_exponent, key=lambda x: (tail_exponent[x], x)),
        "tailExponent": tail_exponent,
        "threshold": threshold,
    }


def verify(carrier, order, product, unit="T", zero="b", max_failures=8):
    failures = []
    left = {a: {} for a in carrier}
    right = {b: {} for b in carrier}

    def add_failure(item):
        failures.append(item)

    for x in carrier:
        if product(unit, x) != x or product(x, unit) != x:
            add_failure({"check": "unit", "element": x})
        if product(zero, x) != zero or product(x, zero) != zero:
            add_failure({"check": "zero", "element": x})

    for a in carrier:
        for b in carrier:
            if product(a, b) != product(b, a):
                add_failure({"check": "commutative", "witness": [a, b]})

    for a in carrier:
        for b in carrier:
            for c in carrier:
                if product(product(a, b), c) != product(a, product(b, c)):
                    add_failure({"check": "associative", "witness": [a, b, c]})

    for a in carrier:
        for a2 in carrier:
            if not leq(order, a, a2):
                continue
            for b in carrier:
                if not leq(order, product(a, b), product(a2, b)):
                    add_failure(
                        {
                            "check": "monotone",
                            "witness": [a, a2, b, product(a, b), product(a2, b)],
                        }
                    )

    principal = principal_map(carrier, order)
    for a in carrier:
        for c in carrier:
            fiber = sorted(b for b in carrier if leq(order, product(a, b), c))
            key = "\t".join(fiber)
            residual = principal.get(key)
            if residual is None:
                add_failure({"check": "left-residual-principal", "witness": [a, c, fiber]})
            else:
                left[a][c] = residual

    for b in carrier:
        for c in carrier:
            fiber = sorted(a for a in carrier if leq(order, product(a, b), c))
            key = "\t".join(fiber)
            residual = principal.get(key)
            if residual is None:
                add_failure({"check": "right-residual-principal", "witness": [b, c, fiber]})
            else:
                right[b][c] = residual

    if not failures:
        for a in carrier:
            for b in carrier:
                for c in carrier:
                    product_leq = leq(order, product(a, b), c)
                    left_leq = leq(order, b, left[a][c])
                    right_leq = leq(order, a, right[b][c])
                    if product_leq != left_leq or product_leq != right_leq:
                        add_failure(
                            {
                                "check": "residuation-law",
                                "witness": [a, b, c, product_leq, left_leq, right_leq],
                            }
                        )

    return failures[:max_failures], len(failures)


def analyze_model(path, front_sizes):
    with open(path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    depth = infer_depth(carrier)
    order = transitive_closure(carrier, model["order"])
    entries = []

    for front_size in front_sizes:
        product, data = build_product(depth, front_size)
        failures, failure_count = verify(carrier, order, product)
        entries.append(
            {
                "frontSize": front_size,
                "front": data["front"],
                "tail": data["tail"],
                "threshold": data["threshold"],
                "holds": failure_count == 0,
                "failureCount": failure_count,
                "failures": failures,
            }
        )

    return {
        "model": model.get("name", path),
        "path": path,
        "depth": depth,
        "entries": entries,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_paths", nargs="+")
    parser.add_argument("--max-front-size", type=int, default=5)
    parser.add_argument("--output")
    args = parser.parse_args()

    model_entries = []
    for path in args.model_paths:
        with open(path, encoding="utf-8-sig") as handle:
            depth = infer_depth([str(x) for x in json.load(handle)["carrier"]])
        front_sizes = list(range(0, min(depth, args.max_front_size) + 1))
        model_entries.append(analyze_model(path, front_sizes))

    successful_by_depth = {
        str(entry["depth"]): [case["frontSize"] for case in entry["entries"] if case["holds"]]
        for entry in model_entries
    }
    first_failures_by_depth = {}
    for entry in model_entries:
        failures = [case for case in entry["entries"] if not case["holds"]]
        first_failures_by_depth[str(entry["depth"])] = failures[0]["frontSize"] if failures else None

    report = {
        "schema": "orthogonal-front-ideal plus shifted-tail quotient",
        "summary": {
            "modelsChecked": len(model_entries),
            "successfulFrontSizesByDepth": successful_by_depth,
            "firstFailureFrontSizeByDepth": first_failures_by_depth,
            "interpretation": "within this schema and same order, front sizes 0, 1, and 2 are residuated in the checked depths; size 3 first fails by non-principal residual fibers",
        },
        "models": model_entries,
    }

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
