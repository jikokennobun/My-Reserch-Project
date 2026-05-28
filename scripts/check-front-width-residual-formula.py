#!/usr/bin/env python3
"""
Check the closed residual formula for orthogonal front widths k=0,1,2.

The schema uses a front zero-band F_k={a1,...,ak} and a shifted tail
{s, a(N+1), a(k+1), ..., aN}.  Width k=0 is the truncated U-absorbing tensor,
k=1 is the one-front non-U-absorbing variant, and k=2 is the current
front-shifted template.
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


def schema_data(depth, front_size):
    front = {f"a{i}" for i in range(1, front_size + 1)}
    last_atom = f"a{depth + 1}"
    tail_exponent = {"s": 1, last_atom: 1}
    by_exponent = {1: last_atom}
    for index in range(front_size + 1, depth + 1):
        exponent = index - front_size + 1
        element = f"a{index}"
        tail_exponent[element] = exponent
        by_exponent[exponent] = element
    return front, tail_exponent, by_exponent, depth - front_size + 1


def build_product(depth, front_size, unit="T", zero="b", absorber="U"):
    front, tail_exponent, by_exponent, threshold = schema_data(depth, front_size)

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

    return product


def generated_residuals(carrier, order, product):
    principal = principal_map(carrier, order)
    left = {a: {} for a in carrier}
    for a in carrier:
        for c in carrier:
            fiber = sorted(b for b in carrier if leq(order, product(a, b), c))
            key = "\t".join(fiber)
            if key not in principal:
                raise ValueError(f"Non-principal generated fiber for {a}\\{c}: {fiber}")
            left[a][c] = principal[key]
    return left


def rho(by_exponent, d):
    return by_exponent[d]


def formula_residual(depth, front_size, m, c):
    front, tail_exponent, by_exponent, _threshold = schema_data(depth, front_size)
    zero = "b"
    unit = "T"
    absorber = "U"
    tail = set(tail_exponent)
    last_atom = f"a{depth + 1}"

    if m == zero:
        return absorber
    if m == unit:
        return c
    if m in front:
        if c in {m, absorber}:
            return absorber
        if front_size == 1:
            return zero
        if front_size == 2:
            return next(p for p in front if p != m)
        raise ValueError("closed formula is only stated for front_size <= 2")
    if m == absorber:
        if c == absorber:
            return absorber
        if c in front:
            return c
        return zero
    if m in tail:
        if c == absorber:
            return absorber
        if c in front:
            return c
        if c == "s" and m == "s":
            return unit
        if c == last_atom and m in {"s", last_atom}:
            return unit
        if c in tail and c not in {"s", last_atom}:
            if m == c:
                return unit
            diff = tail_exponent[c] - tail_exponent[m]
            if diff >= 1:
                return rho(by_exponent, diff)
        return zero
    raise ValueError(f"Unexpected element {m}")


def analyze(path, front_sizes):
    with open(path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    depth = infer_depth(carrier)
    order = transitive_closure(carrier, model["order"])
    cases = []

    for front_size in front_sizes:
        product = build_product(depth, front_size)
        generated = generated_residuals(carrier, order, product)
        mismatches = []
        for m in carrier:
            for c in carrier:
                expected = generated[m][c]
                actual = formula_residual(depth, front_size, m, c)
                if actual != expected:
                    mismatches.append(
                        {
                            "m": m,
                            "c": c,
                            "formula": actual,
                            "generated": expected,
                        }
                    )
        cases.append(
            {
                "frontSize": front_size,
                "mismatchCount": len(mismatches),
                "mismatches": mismatches[:20],
                "conclusion": "formula-matches-generated-residuals" if not mismatches else "formula-mismatch",
            }
        )

    return {
        "model": model.get("name", path),
        "path": path,
        "depth": depth,
        "cases": cases,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_paths", nargs="+")
    parser.add_argument("--front-sizes", default="0,1,2")
    parser.add_argument("--output")
    args = parser.parse_args()

    front_sizes = [int(item) for item in args.front_sizes.split(",") if item]
    entries = [analyze(path, front_sizes) for path in args.model_paths]
    report = {
        "formula": {
            "schema": "orthogonal front-width residual formula",
            "frontSizes": front_sizes,
            "scope": "front sizes 0, 1, and 2 on the same B_N order",
            "kGe3Obstruction": "for p in F_k, the p\\b fiber contains b plus at least two incomparable front atoms",
        },
        "summary": {
            "modelsChecked": len(entries),
            "totalCases": sum(len(entry["cases"]) for entry in entries),
            "totalMismatches": sum(case["mismatchCount"] for entry in entries for case in entry["cases"]),
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
