#!/usr/bin/env python3
"""
Search for less top-collapsing B_N tensors under a U-absorbing constraint.

The script fixes:

  - commutativity,
  - unit T,
  - zero b,
  - U * x = U for nonzero x not equal to T.

It then searches the remaining orbit/fixed-point products for associative,
monotone operations whose left/right residual fibers are principal. The
objective is to minimize how many nonzero non-unit products are forced to U.
"""

import argparse
import json


def pair_key(a, b):
    return "\t".join(sorted((a, b)))


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


def principal_downset_keys(carrier, order):
    return {
        "\t".join(sorted(x for x in carrier if leq(order, x, r)))
        for r in carrier
    }


def is_principal_downset(carrier, order, elements):
    return "\t".join(sorted(elements)) in principal_downset_keys(carrier, order)


def make_product(unit, zero, absorber, assignment):
    def product(a, b):
        if a == zero or b == zero:
            return zero
        if a == unit:
            return b
        if b == unit:
            return a
        if a == absorber or b == absorber:
            return absorber
        return assignment[pair_key(a, b)]

    return product


def known_product(unit, zero, absorber, assignment, a, b):
    return (
        a == zero
        or b == zero
        or a == unit
        or b == unit
        or a == absorber
        or b == absorber
        or pair_key(a, b) in assignment
    )


def partial_monotone_ok(carrier, order, unit, zero, absorber, assignment):
    product = make_product(unit, zero, absorber, assignment)
    for a in carrier:
        for a2 in carrier:
            if not leq(order, a, a2):
                continue
            for b in carrier:
                if known_product(unit, zero, absorber, assignment, a, b) and known_product(
                    unit, zero, absorber, assignment, a2, b
                ):
                    if not leq(order, product(a, b), product(a2, b)):
                        return False
    return True


def partial_associative_ok(carrier, unit, zero, absorber, assignment):
    product = make_product(unit, zero, absorber, assignment)
    for a in carrier:
        for b in carrier:
            for c in carrier:
                if not known_product(unit, zero, absorber, assignment, a, b):
                    continue
                ab = product(a, b)
                if not known_product(unit, zero, absorber, assignment, ab, c):
                    continue
                if not known_product(unit, zero, absorber, assignment, b, c):
                    continue
                bc = product(b, c)
                if not known_product(unit, zero, absorber, assignment, a, bc):
                    continue
                if product(ab, c) != product(a, bc):
                    return False
    return True


def complete_ok(carrier, order, unit, zero, absorber, assignment):
    product = make_product(unit, zero, absorber, assignment)
    principal_keys = principal_downset_keys(carrier, order)

    for a in carrier:
        for a2 in carrier:
            if not leq(order, a, a2):
                continue
            for b in carrier:
                if not leq(order, product(a, b), product(a2, b)):
                    return False

    for a in carrier:
        for b in carrier:
            for c in carrier:
                if product(product(a, b), c) != product(a, product(b, c)):
                    return False

    for a in carrier:
        for c in carrier:
            fiber = [b for b in carrier if leq(order, product(a, b), c)]
            if "\t".join(sorted(fiber)) not in principal_keys:
                return False
    return True


def residual_tables(carrier, order, product):
    principal = {
        "\t".join(sorted(x for x in carrier if leq(order, x, r))): r
        for r in carrier
    }
    left = {a: {} for a in carrier}
    right = {b: {} for b in carrier}
    for a in carrier:
        for c in carrier:
            key = "\t".join(sorted(b for b in carrier if leq(order, product(a, b), c)))
            left[a][c] = principal[key]
    for b in carrier:
        for c in carrier:
            key = "\t".join(sorted(a for a in carrier if leq(order, product(a, b), c)))
            right[b][c] = principal[key]
    return left, right


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("--unit", default="T")
    parser.add_argument("--zero", default="b")
    parser.add_argument("--absorber", default="U")
    parser.add_argument("--output")
    parser.add_argument("--expanded-model-output")
    parser.add_argument("--max-nodes", type=int, default=500000)
    args = parser.parse_args()

    with open(args.model_path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    order = transitive_closure(carrier, model["order"])
    unit = args.unit
    zero = args.zero
    absorber = args.absorber
    orbit = [x for x in carrier if x not in {unit, zero, absorber}]
    pairs = [(a, b) for index, a in enumerate(orbit) for b in orbit[index:]]

    domains = {}
    for a, b in pairs:
        values = []
        for value in [*orbit, absorber]:
            # If a <= value, then the residual fiber at value would contain T
            # and b, plus b's nonunit partner, which is not principal unless
            # value is U. The same holds symmetrically for b.
            if value == absorber or (not leq(order, a, value) and not leq(order, b, value)):
                values.append(value)
        domains[pair_key(a, b)] = values

    pairs.sort(key=lambda pair: (len(domains[pair_key(*pair)]), pair))
    best = None
    best_u_count = len(pairs) + 1
    node_count = 0
    complete_assignments_checked = 0
    hit_node_limit = False

    def search(index, assignment, u_count):
        nonlocal best, best_u_count, node_count, complete_assignments_checked, hit_node_limit
        if node_count >= args.max_nodes:
            hit_node_limit = True
            return
        node_count += 1
        if u_count >= best_u_count:
            return
        if index == len(pairs):
            complete_assignments_checked += 1
            if complete_ok(carrier, order, unit, zero, absorber, assignment):
                best = dict(assignment)
                best_u_count = u_count
            return

        a, b = pairs[index]
        key = pair_key(a, b)
        values = sorted(domains[key], key=lambda value: (value == absorber, value))
        for value in values:
            assignment[key] = value
            if partial_monotone_ok(carrier, order, unit, zero, absorber, assignment) and partial_associative_ok(
                carrier, unit, zero, absorber, assignment
            ):
                search(index + 1, assignment, u_count + (1 if value == absorber else 0))
            del assignment[key]

    search(0, {}, 0)

    report = {
        "model": model.get("name", args.model_path),
        "modelPath": args.model_path,
        "assumptions": {
            "commutative": True,
            "unit": unit,
            "zero": zero,
            "absorber": absorber,
            "absorberRule": "absorber * x = absorber for nonzero x != unit",
        },
        "search": {
            "nodesVisited": node_count,
            "completeAssignmentsChecked": complete_assignments_checked,
            "maxNodes": args.max_nodes,
            "variables": len(pairs),
            "topAbsorbingUCount": len(pairs),
            "bestUCount": best_u_count if best is not None else None,
            "complete": not hit_node_limit,
        },
    }

    if best is None:
        report["conclusion"] = "no-u-absorbing-candidate-found-within-node-bound"
    else:
        product = make_product(unit, zero, absorber, best)
        tensor = {a: {b: product(a, b) for b in carrier} for a in carrier}
        left, right = residual_tables(carrier, order, product)
        report["bestAssignment"] = best
        report["tensor"] = tensor
        report["leftResidual"] = left
        report["rightResidual"] = right
        report["conclusion"] = "less-top-collapsing-u-absorbing-expansion-found"

        if args.expanded_model_output:
            expanded = dict(model)
            expanded["name"] = f"{model.get('name', 'model')}-u-absorbing-minU"
            expanded["unit"] = unit
            expanded["tensor"] = tensor
            expanded["leftResidual"] = left
            expanded["rightResidual"] = right
            expanded["metadata"] = dict(model.get("metadata", {}))
            expanded["metadata"]["residuation"] = "full"
            expanded["metadata"]["residuation_template"] = "u-absorbing-minU-search"
            expanded["metadata"]["residuation_report"] = args.output
            expanded["metadata"]["residuation_note"] = (
                f"Search found {best_u_count} U-valued nonzero non-unit products "
                f"versus {len(pairs)} in the top-absorbing template."
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
