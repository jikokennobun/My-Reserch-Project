#!/usr/bin/env python3
"""
Build a truncated-exponent U-absorbing residuated expansion for B_N.

For the bottom-disciplined B_N carrier

    {b, T, a1, ..., a(N+1), s, U}

the tensor fixes T as unit, b as zero, and U as absorbing over nonzero
non-units. On the orbit/fixed-point elements, assign exponents

    exp(a(N+1)) = exp(s) = 1
    exp(ai) = i + 1 for 1 <= i <= N.

Products add exponents when the sum is at most N+1 and otherwise return U.
The script verifies associativity, monotonicity, and principal residual fibers
before writing the expanded model.
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


def build_product(carrier, depth, unit, zero, absorber):
    last_atom = f"a{depth + 1}"
    exponent = {"s": 1, last_atom: 1}
    by_exponent = {1: last_atom}
    for index in range(1, depth + 1):
        element = f"a{index}"
        exponent[element] = index + 1
        by_exponent[index + 1] = element

    def product(a, b):
        if a == zero or b == zero:
            return zero
        if a == unit:
            return b
        if b == unit:
            return a
        if a == absorber or b == absorber:
            return absorber
        total = exponent[a] + exponent[b]
        if total <= depth + 1:
            return by_exponent[total]
        return absorber

    return product, exponent


def verify(carrier, order, product, unit, zero):
    failures = []

    for x in carrier:
        if product(unit, x) != x or product(x, unit) != x:
            failures.append({"check": "unit", "element": x})
        if product(zero, x) != zero or product(x, zero) != zero:
            failures.append({"check": "zero", "element": x})

    for a in carrier:
        for b in carrier:
            if product(a, b) != product(b, a):
                failures.append({"check": "commutative", "witness": [a, b]})

    for a in carrier:
        for b in carrier:
            for c in carrier:
                if product(product(a, b), c) != product(a, product(b, c)):
                    failures.append({"check": "associative", "witness": [a, b, c]})

    for a in carrier:
        for a2 in carrier:
            if not leq(order, a, a2):
                continue
            for b in carrier:
                if not leq(order, product(a, b), product(a2, b)):
                    failures.append(
                        {
                            "check": "monotone",
                            "witness": [a, a2, b, product(a, b), product(a2, b)],
                        }
                    )

    principal = principal_map(carrier, order)
    left = {a: {} for a in carrier}
    right = {b: {} for b in carrier}
    for a in carrier:
        for c in carrier:
            key = "\t".join(sorted(b for b in carrier if leq(order, product(a, b), c)))
            residual = principal.get(key)
            if residual is None:
                failures.append({"check": "left-residual-principal", "witness": [a, c, key]})
            else:
                left[a][c] = residual
    for b in carrier:
        for c in carrier:
            key = "\t".join(sorted(a for a in carrier if leq(order, product(a, b), c)))
            residual = principal.get(key)
            if residual is None:
                failures.append({"check": "right-residual-principal", "witness": [b, c, key]})
            else:
                right[b][c] = residual

    return failures, left, right


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("--unit", default="T")
    parser.add_argument("--zero", default="b")
    parser.add_argument("--absorber", default="U")
    parser.add_argument("--output")
    parser.add_argument("--expanded-model-output")
    args = parser.parse_args()

    with open(args.model_path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    depth = infer_depth(carrier)
    order = transitive_closure(carrier, model["order"])
    product, exponent = build_product(carrier, depth, args.unit, args.zero, args.absorber)
    failures, left, right = verify(carrier, order, product, args.unit, args.zero)
    if failures:
        raise SystemExit(json.dumps({"conclusion": "template-failed", "failures": failures[:20]}, indent=2))

    tensor = {a: {b: product(a, b) for b in carrier} for a in carrier}
    searched = [x for x in carrier if x not in {args.unit, args.zero, args.absorber}]
    u_count = sum(
        1
        for index, a in enumerate(searched)
        for b in searched[index:]
        if tensor[a][b] == args.absorber
    )
    variable_count = len(searched) * (len(searched) + 1) // 2
    report = {
        "model": model.get("name", args.model_path),
        "modelPath": args.model_path,
        "depth": depth,
        "assumptions": {
            "template": "truncated-exponent-u-absorbing",
            "commutative": True,
            "unit": args.unit,
            "zero": args.zero,
            "absorber": args.absorber,
            "exponent": exponent,
        },
        "searchClassComparison": {
            "variables": variable_count,
            "topAbsorbingUCount": variable_count,
            "templateUCount": u_count,
        },
        "tensor": tensor,
        "leftResidual": left,
        "rightResidual": right,
        "conclusion": "full-residuated-expansion-found-by-template",
    }

    if args.expanded_model_output:
        expanded = dict(model)
        expanded["name"] = f"{model.get('name', 'model')}-truncated-u-absorbing"
        expanded["unit"] = args.unit
        expanded["tensor"] = tensor
        expanded["leftResidual"] = left
        expanded["rightResidual"] = right
        expanded["metadata"] = dict(model.get("metadata", {}))
        expanded["metadata"]["residuation"] = "full"
        expanded["metadata"]["residuation_template"] = "truncated-exponent-u-absorbing"
        expanded["metadata"]["residuation_report"] = args.output
        expanded["metadata"]["residuation_note"] = (
            f"Template has {u_count} U-valued nonzero non-unit products "
            f"versus {variable_count} in the top-absorbing template."
        )
        with open(args.expanded_model_output, "w", encoding="utf-8") as handle:
            handle.write(json.dumps(expanded, indent=2, ensure_ascii=False) + "\n")

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
