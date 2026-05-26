#!/usr/bin/env python3
"""
Generate bottom-disciplined first-true nFG2 witnesses.

For a requested depth N, the model has orbit

    T -> a1 -> ... -> a(N+1) -> s -> s

so nFG2(k) fails for k <= N and holds from N+1 onward. Unlike the sparse D_N
family, this construction satisfies bottom discipline by adding a genuine bottom
element b below every carrier element and a helper upper bound U above every
carrier element. The refutability map sends b to U and U to b, preserving
antitonicity for the new bottom/top-bounding pairs.
"""

import argparse
import json
from pathlib import Path


def build_model(depth):
    if depth < 1:
        raise ValueError("depth must be at least 1")

    atoms = [f"a{i}" for i in range(1, depth + 2)]
    carrier = ["b", "T", *atoms, "s", "U"]

    order = []
    for element in carrier:
        order.append([element, element])
    for element in carrier:
        order.append(["b", element])
        order.append([element, "U"])
    order.append(["s", f"a{depth + 1}"])

    # Deduplicate while preserving order.
    seen = set()
    unique_order = []
    for pair in order:
        key = tuple(pair)
        if key not in seen:
            seen.add(key)
            unique_order.append(pair)

    box = {element: element for element in carrier}
    refutability = {
        "b": "U",
        "T": "a1",
        "U": "b",
        "s": "s",
    }
    for index in range(1, depth + 1):
        refutability[f"a{index}"] = f"a{index + 1}"
    refutability[f"a{depth + 1}"] = "s"

    false_block = "F" * depth
    expected_prefix = false_block + "TTTT"

    return {
        "name": f"bottom-nfg2-depth-{depth}",
        "carrier": carrier,
        "order": unique_order,
        "top": "T",
        "bottom": "b",
        "box": box,
        "refutability": refutability,
        "metadata": {
            "purpose": (
                "Bottom-disciplined arbitrary-depth nFG2 first-true witness: "
                f"nFG2(k) fails for k <= {depth} and holds at k = {depth + 1}."
            ),
            "construction": (
                f"Orbit T -> a1 -> ... -> a{depth + 1} -> s -> s, with b <= x <= U "
                f"for all x and s <= a{depth + 1}."
            ),
            "first_true_nFG2": depth + 1,
            "expected_nFG2_prefix": expected_prefix,
            "bottom_discipline": True,
            "collapse": False,
            "G2_mode": "vacuous",
            "separation": "G2=true, FG2=false, FP-synt=true, bottom discipline true",
            "note": (
                "The helper bound U absorbs antitonicity requirements from b <= x; "
                "U maps back to b."
            ),
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--output")
    args = parser.parse_args()

    output = args.output or f"models/examples/bottom-nfg2-depth-{args.depth}.json"
    model = build_model(args.depth)
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(model, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"bottom-disciplined nFG2 depth witness written: {path}")


if __name__ == "__main__":
    main()
