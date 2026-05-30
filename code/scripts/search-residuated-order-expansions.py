#!/usr/bin/env python3
"""
Search same-carrier order expansions that admit full residuation.

The script keeps the carrier, box, refutability, top, and bottom fixed. It
enumerates preorder extensions of the given order, keeps those preserving
non-collapse, antitonicity, G2, FG2, and a syntactic fixed point, and searches
for an associative monotone tensor with both residuals.
"""

import argparse
import json
from itertools import product


def pair_key(pair):
    return "\t".join(pair)


def transitive_closure(carrier, pairs):
    order = {pair_key((str(x), str(y))) for x, y in pairs}
    for x in carrier:
        order.add(pair_key((x, x)))
    changed = True
    while changed:
        changed = False
        entries = [tuple(item.split("\t")) for item in order]
        for a, b in entries:
            for c, d in entries:
                if b == c and pair_key((a, d)) not in order:
                    order.add(pair_key((a, d)))
                    changed = True
    return order


def leq(order, x, y):
    return pair_key((x, y)) in order


def set_key(values):
    return "\x1f".join(sorted(values))


def principal_downsets(carrier, order):
    return {
        set_key(x for x in carrier if leq(order, x, r)): r
        for r in carrier
    }


def search_tensor(carrier, order, keep):
    principal_by_key = principal_downsets(carrier, order)

    for unit in carrier:
        unknown = [(a, b) for a in carrier for b in carrier if a != unit and b != unit]
        examples = []
        candidate_count = 0

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

            if any(
                tensor[tensor[a][b]][c] != tensor[a][tensor[b][c]]
                for a in carrier
                for b in carrier
                for c in carrier
            ):
                continue

            if any(
                leq(order, a, a2) and not leq(order, tensor[a][b], tensor[a2][b])
                for a in carrier
                for a2 in carrier
                for b in carrier
            ):
                continue

            if any(
                leq(order, b, b2) and not leq(order, tensor[a][b], tensor[a][b2])
                for b in carrier
                for b2 in carrier
                for a in carrier
            ):
                continue

            left = {a: {} for a in carrier}
            right = {b: {} for b in carrier}
            residuated = True

            for a in carrier:
                for c in carrier:
                    downset = [b for b in carrier if leq(order, tensor[a][b], c)]
                    residual = principal_by_key.get(set_key(downset))
                    if residual is None:
                        residuated = False
                        break
                    left[a][c] = residual
                if not residuated:
                    break
            if not residuated:
                continue

            for b in carrier:
                for c in carrier:
                    downset = [a for a in carrier if leq(order, tensor[a][b], c)]
                    residual = principal_by_key.get(set_key(downset))
                    if residual is None:
                        residuated = False
                        break
                    right[b][c] = residual
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
                        "leftResidual": left,
                        "rightResidual": right,
                    }
                )

        if candidate_count:
            return {"unit": unit, "candidateCount": candidate_count, "examples": examples}

    return None


def preserves_target(model, carrier, order):
    top = model["top"]
    bottom = model["bottom"]
    ref = model["refutability"]

    if leq(order, top, bottom):
        return False
    if leq(order, ref[top], bottom):
        return False
    if not leq(order, ref[ref[top]], ref[top]):
        return False
    if not any(leq(order, x, ref[x]) and leq(order, ref[x], x) for x in carrier):
        return False
    for x in carrier:
        for y in carrier:
            if leq(order, x, y) and not leq(order, ref[y], ref[x]):
                return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("--output")
    parser.add_argument("--expanded-model-output")
    parser.add_argument("--keep", type=int, default=1)
    args = parser.parse_args()

    with open(args.model_path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    base_order = transitive_closure(carrier, model["order"])
    all_pairs = [(a, b) for a in carrier for b in carrier]
    optional = [pair for pair in all_pairs if pair_key(pair) not in base_order]

    variants = []
    for mask in range(1 << len(optional)):
        pairs = [tuple(item.split("\t")) for item in base_order]
        for index, pair in enumerate(optional):
            if mask & (1 << index):
                pairs.append(pair)
        order = transitive_closure(carrier, pairs)
        if not preserves_target(model, carrier, order):
            continue
        extras = sorted(
            tuple(item.split("\t"))
            for item in order
            if item not in base_order
        )
        variants.append((len(extras), extras, order))

    variants.sort(key=lambda item: (item[0], item[1]))

    checked = 0
    found = None
    for _, extras, order in variants:
        checked += 1
        tensor_result = search_tensor(carrier, order, args.keep)
        if tensor_result is not None:
            found = {
                "addedOrderPairs": extras,
                "order": sorted(tuple(item.split("\t")) for item in order),
                "tensorSearch": tensor_result,
            }
            break

    report = {
        "model": model.get("name", args.model_path),
        "modelPath": args.model_path,
        "candidateOrderExtensions": len(variants),
        "checkedUntilFirstHit": checked,
        "found": found is not None,
        "firstHit": found,
    }

    if args.expanded_model_output and found:
        example = found["tensorSearch"]["examples"][0]
        expanded = dict(model)
        expanded["name"] = f"{model.get('name', 'model')}-order-plus-bot-c-residuated"
        expanded["order"] = [list(pair) for pair in found["order"]]
        expanded["unit"] = example["unit"]
        expanded["tensor"] = example["tensor"]
        expanded["leftResidual"] = example["leftResidual"]
        expanded["rightResidual"] = example["rightResidual"]
        expanded["metadata"] = dict(model.get("metadata", {}))
        expanded["metadata"]["order_summary"] = "bot < p < T and bot < c < T, with p incomparable to c."
        expanded["metadata"]["residuation"] = "full"
        expanded["metadata"]["residuation_search_report"] = args.output
        expanded["metadata"]["added_order_pairs"] = [list(pair) for pair in found["addedOrderPairs"]]
        with open(args.expanded_model_output, "w", encoding="utf-8") as handle:
            handle.write(json.dumps(expanded, indent=2, ensure_ascii=False) + "\n")

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
