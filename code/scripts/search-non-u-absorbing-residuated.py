#!/usr/bin/env python3
"""
Search B_N for a same-order full-residuated tensor without U-absorption.

This search fixes commutativity, unit T, and zero b, but lets the nonzero
non-unit product table vary. It splits cases by the possible U * x values
allowed by monotonicity from T <= U, then searches the remaining products.
The intended first target is the checked B3 model `bottom-nfg2-depth-3`.
"""

import argparse
import itertools
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


def principal_map(carrier, order):
    return {
        "\t".join(sorted(x for x in carrier if leq(order, x, r))): r
        for r in carrier
    }


def principal_downsets(carrier, order):
    return [
        set(x for x in carrier if leq(order, x, r))
        for r in carrier
    ]


def make_product(unit, zero, assignment):
    def product(a, b):
        if a == zero or b == zero:
            return zero
        if a == unit:
            return b
        if b == unit:
            return a
        return assignment[pair_key(a, b)]

    return product


def known_product(unit, zero, assignment, a, b):
    return a == zero or b == zero or a == unit or b == unit or pair_key(a, b) in assignment


def upper_bounds(carrier, order, element):
    return [candidate for candidate in carrier if leq(order, element, candidate)]


def downset(carrier, order, element):
    return [candidate for candidate in carrier if leq(order, candidate, element)]


def monotone_ok(carrier, order, unit, zero, assignment):
    product = make_product(unit, zero, assignment)
    for a in carrier:
        for a2 in carrier:
            if not leq(order, a, a2):
                continue
            for b in carrier:
                if known_product(unit, zero, assignment, a, b) and known_product(
                    unit, zero, assignment, a2, b
                ):
                    if not leq(order, product(a, b), product(a2, b)):
                        return False
    return True


def associative_ok(carrier, unit, zero, assignment):
    product = make_product(unit, zero, assignment)
    for a in carrier:
        for b in carrier:
            for c in carrier:
                if not known_product(unit, zero, assignment, a, b):
                    continue
                ab = product(a, b)
                if not known_product(unit, zero, assignment, ab, c):
                    continue
                if not known_product(unit, zero, assignment, b, c):
                    continue
                bc = product(b, c)
                if not known_product(unit, zero, assignment, a, bc):
                    continue
                if product(ab, c) != product(a, bc):
                    return False
    return True


def residual_possible(carrier, order, unit, zero, assignment, principal_sets):
    product = make_product(unit, zero, assignment)

    for a in carrier:
        for c in carrier:
            included = set()
            excluded = set()
            for b in carrier:
                if not known_product(unit, zero, assignment, a, b):
                    continue
                if leq(order, product(a, b), c):
                    included.add(b)
                else:
                    excluded.add(b)
            if not any(included <= downset and downset.isdisjoint(excluded) for downset in principal_sets):
                return False

    for b in carrier:
        for c in carrier:
            included = set()
            excluded = set()
            for a in carrier:
                if not known_product(unit, zero, assignment, a, b):
                    continue
                if leq(order, product(a, b), c):
                    included.add(a)
                else:
                    excluded.add(a)
            if not any(included <= downset and downset.isdisjoint(excluded) for downset in principal_sets):
                return False

    return True


def full_check(carrier, order, unit, zero, assignment):
    product = make_product(unit, zero, assignment)
    if not monotone_ok(carrier, order, unit, zero, assignment):
        return None
    if not associative_ok(carrier, unit, zero, assignment):
        return None

    principal = principal_map(carrier, order)
    left = {a: {} for a in carrier}
    right = {b: {} for b in carrier}
    for a in carrier:
        for c in carrier:
            key = "\t".join(sorted(b for b in carrier if leq(order, product(a, b), c)))
            residual = principal.get(key)
            if residual is None:
                return None
            left[a][c] = residual
    for b in carrier:
        for c in carrier:
            key = "\t".join(sorted(a for a in carrier if leq(order, product(a, b), c)))
            residual = principal.get(key)
            if residual is None:
                return None
            right[b][c] = residual
    return left, right


def build_u_patterns(carrier, order, orbit, absorber):
    options = []
    for x in orbit:
        options.append([(x, value) for value in upper_bounds(carrier, order, x)])
    for choices in itertools.product(*options):
        pattern = dict(choices)
        pattern[absorber] = absorber
        if all(value == absorber for value in pattern.values()):
            continue
        yield pattern


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("--unit", default="T")
    parser.add_argument("--zero", default="b")
    parser.add_argument("--absorber", default="U")
    parser.add_argument("--output")
    parser.add_argument("--expanded-model-output")
    parser.add_argument("--max-nodes", type=int, default=1000000)
    args = parser.parse_args()

    with open(args.model_path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    order = transitive_closure(carrier, model["order"])
    unit = args.unit
    zero = args.zero
    absorber = args.absorber
    nonzero_nonunit = [x for x in carrier if x not in {zero, unit}]
    orbit = [x for x in nonzero_nonunit if x != absorber]
    all_pairs = [(a, b) for index, a in enumerate(nonzero_nonunit) for b in nonzero_nonunit[index:]]
    orbit_pairs = [(a, b) for index, a in enumerate(orbit) for b in orbit[index:]]
    principal_sets = principal_downsets(carrier, order)

    node_count = 0
    pattern_count = 0
    pruned_patterns = 0
    residual_prune_count = 0
    complete_assignments_checked = 0
    hit_node_limit = False
    best = None
    best_non_u_products = -1
    best_pattern = None

    for pattern in build_u_patterns(carrier, order, orbit, absorber):
        if node_count >= args.max_nodes:
            hit_node_limit = True
            break
        pattern_count += 1
        base = {pair_key(absorber, absorber): absorber}
        for x, value in pattern.items():
            base[pair_key(absorber, x)] = value
        if (
            not monotone_ok(carrier, order, unit, zero, base)
            or not associative_ok(carrier, unit, zero, base)
            or not residual_possible(carrier, order, unit, zero, base, principal_sets)
        ):
            pruned_patterns += 1
            continue

        domains = {}
        impossible = False
        for a, b in orbit_pairs:
            allowed_by_u = set(downset(carrier, order, base[pair_key(absorber, a)]))
            allowed_by_u &= set(downset(carrier, order, base[pair_key(absorber, b)]))
            values = sorted(allowed_by_u)
            if not values:
                impossible = True
                break
            domains[pair_key(a, b)] = values
        if impossible:
            pruned_patterns += 1
            continue

        ordered_pairs = sorted(orbit_pairs, key=lambda pair: (len(domains[pair_key(*pair)]), pair))

        def search(index, assignment):
            nonlocal node_count, complete_assignments_checked, best, best_non_u_products, best_pattern
            nonlocal hit_node_limit, residual_prune_count
            if node_count >= args.max_nodes:
                hit_node_limit = True
                return
            node_count += 1
            if index == len(ordered_pairs):
                complete_assignments_checked += 1
                checked = full_check(carrier, order, unit, zero, assignment)
                if checked is None:
                    return
                non_u_products = sum(1 for pair in all_pairs if assignment[pair_key(*pair)] != absorber)
                if non_u_products > best_non_u_products:
                    left, right = checked
                    product = make_product(unit, zero, assignment)
                    best = {
                        "assignment": dict(assignment),
                        "tensor": {a: {b: product(a, b) for b in carrier} for a in carrier},
                        "leftResidual": left,
                        "rightResidual": right,
                    }
                    best_non_u_products = non_u_products
                    best_pattern = dict(pattern)
                return

            a, b = ordered_pairs[index]
            key = pair_key(a, b)
            values = sorted(domains[key], key=lambda value: (value == absorber, value))
            for value in values:
                assignment[key] = value
                residual_ok = True
                if monotone_ok(carrier, order, unit, zero, assignment) and associative_ok(
                    carrier, unit, zero, assignment
                ):
                    residual_ok = residual_possible(carrier, order, unit, zero, assignment, principal_sets)
                    if residual_ok:
                        search(index + 1, assignment)
                if not residual_ok:
                    residual_prune_count += 1
                del assignment[key]

        search(0, dict(base))

    report = {
        "model": model.get("name", args.model_path),
        "modelPath": args.model_path,
        "assumptions": {
            "commutative": True,
            "unit": unit,
            "zero": zero,
            "uAbsorptionAssumed": False,
            "orbitProductTableFixed": False,
        },
        "search": {
            "uActionPatternsVisited": pattern_count,
            "uActionPatternsPrunedImmediately": pruned_patterns,
            "residualFiberPrunes": residual_prune_count,
            "nodesVisited": node_count,
            "completeAssignmentsChecked": complete_assignments_checked,
            "maxNodes": args.max_nodes,
            "complete": not hit_node_limit,
            "variables": len(all_pairs),
        },
    }

    if best is None:
        report["conclusion"] = "no-non-u-absorbing-residuated-tensor-found-within-node-bound"
    else:
        report["bestNonUProductCount"] = best_non_u_products
        report["topAbsorbingNonUProductCount"] = 0
        report["bestUPattern"] = best_pattern
        report["tensor"] = best["tensor"]
        report["leftResidual"] = best["leftResidual"]
        report["rightResidual"] = best["rightResidual"]
        report["conclusion"] = "non-u-absorbing-residuated-tensor-found"
        if args.expanded_model_output:
            expanded = dict(model)
            expanded["name"] = f"{model.get('name', 'model')}-non-u-absorbing"
            expanded["unit"] = unit
            expanded["tensor"] = best["tensor"]
            expanded["leftResidual"] = best["leftResidual"]
            expanded["rightResidual"] = best["rightResidual"]
            expanded["metadata"] = dict(model.get("metadata", {}))
            expanded["metadata"]["residuation"] = "full"
            expanded["metadata"]["residuation_template"] = "non-u-absorbing-search"
            expanded["metadata"]["residuation_report"] = args.output
            expanded["metadata"]["residuation_note"] = (
                "Search varied the orbit product table and did not assume U-absorption."
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
