#!/usr/bin/env python3
"""
Check the closed residual table for the front-shifted B_N tensor.

The input model should already contain tensor, leftResidual, and rightResidual
fields produced by build-front-shifted-non-u-absorbing-residuated.py.  This
checker compares those residual tables with the symbolic formula recorded in
definitions.md and the topic notes.
"""

import argparse
import json
import re


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


def residual_formula(depth, m, c, unit="T", zero="b", absorber="U"):
    front = {"a1", "a2"}
    last_atom = f"a{depth + 1}"
    tail = {"s", last_atom, *[f"a{i}" for i in range(3, depth + 1)]}
    tau = {"s": 1, last_atom: 1}
    for index in range(3, depth + 1):
        tau[f"a{index}"] = index - 1

    if m == zero:
        return absorber
    if m == unit:
        return c

    if m in front:
        if c in {m, absorber}:
            return absorber
        return "a2" if m == "a1" else "a1"

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
        if c in {zero, unit}:
            return zero
        if c == "s":
            return unit if m == "s" else zero
        if c == last_atom:
            return unit if m in {"s", last_atom} else zero

        match = re.fullmatch(r"a([0-9]+)", c)
        if match:
            index = int(match.group(1))
            if 3 <= index <= depth:
                if m == c:
                    return unit
                difference = index - 1 - tau[m]
                if difference == 1:
                    return last_atom
                if 2 <= difference <= depth - 1:
                    return f"a{difference + 1}"
                return zero

    raise ValueError(f"unhandled residual case: {m} \\ {c}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("--output")
    args = parser.parse_args()

    with open(args.model_path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    depth = infer_depth(carrier)
    left = model["leftResidual"]
    right = model["rightResidual"]

    mismatches = []
    for m in carrier:
        for c in carrier:
            expected = residual_formula(depth, m, c)
            if left[m][c] != expected:
                mismatches.append(
                    {"side": "left", "factor": m, "target": c, "expected": expected, "actual": left[m][c]}
                )
            if right[m][c] != expected:
                mismatches.append(
                    {"side": "right", "factor": m, "target": c, "expected": expected, "actual": right[m][c]}
                )

    report = {
        "model": model.get("name", args.model_path),
        "modelPath": args.model_path,
        "depth": depth,
        "formula": "front-shifted-non-u-absorbing-residual-table",
        "checks": {
            "leftResidualMatchesFormula": not any(m["side"] == "left" for m in mismatches),
            "rightResidualMatchesFormula": not any(m["side"] == "right" for m in mismatches),
        },
        "mismatchCount": len(mismatches),
        "mismatches": mismatches[:20],
        "conclusion": "residual-formula-verified" if not mismatches else "residual-formula-mismatch",
    }

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
