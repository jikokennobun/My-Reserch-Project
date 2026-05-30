#!/usr/bin/env python3
"""
Build and verify a top-absorbing full-residuated expansion.

The tensor template is:

    z * x = z
    e * x = x
    x * y = u   otherwise

where e is the monoid unit, z is the zero, and u is the chosen absorbing upper
element. The script checks associativity, monotonicity, and both residual laws
before writing an expanded model.
"""

import argparse
import json


def pair_key(a, b):
    return f"{a}\t{b}"


def transitive_closure(carrier, pairs):
    order = {pair_key(str(a), str(b)) for a, b in pairs}
    for x in carrier:
        order.add(pair_key(x, x))
    changed = True
    while changed:
        changed = False
        entries = [tuple(item.split("\t")) for item in order]
        for a, b in entries:
            for c, d in entries:
                if b == c and pair_key(a, d) not in order:
                    order.add(pair_key(a, d))
                    changed = True
    return order


def leq(order, a, b):
    return pair_key(a, b) in order


def downset_key(values):
    return "\t".join(sorted(values))


def principal_downsets(carrier, order):
    return {
        downset_key(x for x in carrier if leq(order, x, r)): r
        for r in carrier
    }


def build_tensor(carrier, unit, zero, absorber):
    def product(a, b):
        if a == zero or b == zero:
            return zero
        if a == unit:
            return b
        if b == unit:
            return a
        return absorber

    return {
        a: {b: product(a, b) for b in carrier}
        for a in carrier
    }


def verify(carrier, order, tensor, unit, zero):
    failures = []

    for x in carrier:
        if tensor[unit][x] != x or tensor[x][unit] != x:
            failures.append({"check": "unit", "element": x})
        if tensor[zero][x] != zero or tensor[x][zero] != zero:
            failures.append({"check": "zero", "element": x})

    for a in carrier:
        for b in carrier:
            if tensor[a][b] != tensor[b][a]:
                failures.append({"check": "commutative", "witness": [a, b]})

    for a in carrier:
        for b in carrier:
            for c in carrier:
                left = tensor[tensor[a][b]][c]
                right = tensor[a][tensor[b][c]]
                if left != right:
                    failures.append({"check": "associative", "witness": [a, b, c, left, right]})

    for a in carrier:
        for a2 in carrier:
            for b in carrier:
                if leq(order, a, a2) and not leq(order, tensor[a][b], tensor[a2][b]):
                    failures.append(
                        {
                            "check": "monotone-left",
                            "witness": [a, a2, b, tensor[a][b], tensor[a2][b]],
                        }
                    )
                if leq(order, a, a2) and not leq(order, tensor[b][a], tensor[b][a2]):
                    failures.append(
                        {
                            "check": "monotone-right",
                            "witness": [b, a, a2, tensor[b][a], tensor[b][a2]],
                        }
                    )

    principal = principal_downsets(carrier, order)
    left_residual = {a: {} for a in carrier}
    right_residual = {b: {} for b in carrier}

    for a in carrier:
        for c in carrier:
            fiber = [b for b in carrier if leq(order, tensor[a][b], c)]
            residual = principal.get(downset_key(fiber))
            if residual is None:
                failures.append({"check": "left-residual-principal", "witness": [a, c, fiber]})
            else:
                left_residual[a][c] = residual

    for b in carrier:
        for c in carrier:
            fiber = [a for a in carrier if leq(order, tensor[a][b], c)]
            residual = principal.get(downset_key(fiber))
            if residual is None:
                failures.append({"check": "right-residual-principal", "witness": [b, c, fiber]})
            else:
                right_residual[b][c] = residual

    if not failures:
        for a in carrier:
            for b in carrier:
                for c in carrier:
                    product_leq = leq(order, tensor[a][b], c)
                    left_leq = leq(order, b, left_residual[a][c])
                    right_leq = leq(order, a, right_residual[b][c])
                    if product_leq != left_leq or product_leq != right_leq:
                        failures.append(
                            {
                                "check": "residuation-law",
                                "witness": [a, b, c, product_leq, left_leq, right_leq],
                            }
                        )

    return failures, left_residual, right_residual


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("--unit", required=True)
    parser.add_argument("--zero", required=True)
    parser.add_argument("--absorber", required=True)
    parser.add_argument("--output")
    parser.add_argument("--expanded-model-output")
    args = parser.parse_args()

    with open(args.model_path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    for role, value in {"unit": args.unit, "zero": args.zero, "absorber": args.absorber}.items():
        if value not in carrier:
            raise SystemExit(f"Unknown {role}: {value}")
    if len({args.unit, args.zero, args.absorber}) != 3:
        raise SystemExit("unit, zero, and absorber must be distinct")

    order = transitive_closure(carrier, model["order"])
    tensor = build_tensor(carrier, args.unit, args.zero, args.absorber)
    failures, left_residual, right_residual = verify(carrier, order, tensor, args.unit, args.zero)
    if failures:
        raise SystemExit(json.dumps({"conclusion": "template-failed", "failures": failures[:20]}, indent=2))

    example = {
        "unit": args.unit,
        "zero": args.zero,
        "absorber": args.absorber,
        "tensor": tensor,
        "leftResidual": left_residual,
        "rightResidual": right_residual,
    }
    report = {
        "model": model.get("name", args.model_path),
        "modelPath": args.model_path,
        "carrierSize": len(carrier),
        "assumptions": {
            "template": "top-absorbing",
            "commutative": True,
            "unit": args.unit,
            "zero": args.zero,
            "absorber": args.absorber,
        },
        "checks": {
            "unit": True,
            "zero": True,
            "commutative": True,
            "associative": True,
            "monotone": True,
            "leftResiduals": True,
            "rightResiduals": True,
            "residuationLaw": True,
        },
        "example": example,
        "conclusion": "full-residuated-expansion-found-by-template",
    }

    if args.expanded_model_output:
        expanded = dict(model)
        expanded["name"] = f"{model.get('name', 'model')}-residuated"
        expanded["unit"] = args.unit
        expanded["tensor"] = tensor
        expanded["leftResidual"] = left_residual
        expanded["rightResidual"] = right_residual
        expanded["metadata"] = dict(model.get("metadata", {}))
        expanded["metadata"]["residuation"] = "full"
        expanded["metadata"]["residuation_template"] = "top-absorbing"
        expanded["metadata"]["residuation_report"] = args.output
        expanded["metadata"]["residuation_assumptions"] = (
            f"commutative tensor with unit {args.unit}, zero {args.zero}, "
            f"and absorber {args.absorber}"
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
