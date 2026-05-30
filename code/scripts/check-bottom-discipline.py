#!/usr/bin/env python3
"""
Check bottom discipline for finite G2-ZOO models.

Bottom discipline is the order principle:

    bottom <= x for every carrier element x.

For each model, this script reports whether the principle already holds and
what happens if the missing bottom pairs are added while keeping the carrier,
top, bottom, box, and refutability map fixed.
"""

import argparse
import json


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


def equiv(order, x, y):
    return leq(order, x, y) and leq(order, y, x)


def apply_n(refutability, value, count):
    for _ in range(count):
        value = refutability[value]
    return value


def check_antitone(carrier, order, refutability):
    witnesses = []
    for x in carrier:
        for y in carrier:
            if leq(order, x, y) and not leq(order, refutability[y], refutability[x]):
                witnesses.append(
                    {
                        "orderPair": [x, y],
                        "requiredImagePair": [refutability[y], refutability[x]],
                    }
                )
    return witnesses


def properties(model, order, nfg2_depth):
    carrier = [str(x) for x in model["carrier"]]
    top = str(model["top"])
    bottom = str(model["bottom"])
    refutability = {str(k): str(v) for k, v in model["refutability"].items()}
    nfg2 = [leq(order, apply_n(refutability, top, k + 1), apply_n(refutability, top, k)) for k in range(1, nfg2_depth + 1)]
    fp = [x for x in carrier if equiv(order, x, refutability[x])]
    orbit = [top]
    for _ in range(nfg2_depth + 2):
        orbit.append(refutability[orbit[-1]])
    return {
        "collapse": leq(order, top, bottom),
        "G2": (not leq(order, refutability[top], bottom)) or leq(order, top, bottom),
        "G2Antecedent": leq(order, refutability[top], bottom),
        "FG2": nfg2[0],
        "nFG2Pattern": "".join("T" if value else "F" for value in nfg2),
        "FPSyntactic": fp,
        "orbitPrefix": orbit,
    }


def analyze_model(path, nfg2_depth):
    with open(path, encoding="utf-8-sig") as handle:
        model = json.load(handle)

    carrier = [str(x) for x in model["carrier"]]
    bottom = str(model["bottom"])
    base_order = transitive_closure(carrier, model["order"])
    missing = [[bottom, x] for x in carrier if not leq(base_order, bottom, x)]
    enforced_order = transitive_closure(
        carrier,
        [tuple(item.split("\t")) for item in base_order] + [tuple(pair) for pair in missing],
    )
    antitone_witnesses = check_antitone(carrier, enforced_order, {str(k): str(v) for k, v in model["refutability"].items()})
    before = properties(model, base_order, nfg2_depth)
    after = properties(model, enforced_order, nfg2_depth)
    stable_fields = ["collapse", "G2", "FG2", "nFG2Pattern", "FPSyntactic"]

    return {
        "name": model.get("name", path),
        "path": path,
        "carrierSize": len(carrier),
        "bottom": bottom,
        "alreadyBottomDisciplined": not missing,
        "missingBottomPairs": missing,
        "enforcedOrderAdds": missing,
        "enforcedAntitone": not antitone_witnesses,
        "antitoneFailuresAfterEnforcement": antitone_witnesses,
        "before": before,
        "afterEnforcingBottom": after,
        "corePropertiesStable": all(before[field] == after[field] for field in stable_fields),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("models", nargs="+")
    parser.add_argument("--nfg2-depth", type=int, default=8)
    parser.add_argument("--output")
    args = parser.parse_args()

    entries = [analyze_model(path, args.nfg2_depth) for path in args.models]
    valid_after = [entry["name"] for entry in entries if entry["enforcedAntitone"]]
    stable_after = [
        entry["name"]
        for entry in entries
        if entry["enforcedAntitone"] and entry["corePropertiesStable"]
    ]
    invalid_after = [
        entry["name"]
        for entry in entries
        if not entry["enforcedAntitone"]
    ]

    report = {
        "principle": "bottom discipline",
        "formula": "forall x, bottom <= x",
        "nfg2Depth": args.nfg2_depth,
        "summary": {
            "modelsChecked": len(entries),
            "alreadyBottomDisciplined": [
                entry["name"] for entry in entries if entry["alreadyBottomDisciplined"]
            ],
            "validAfterPureOrderEnforcement": valid_after,
            "corePropertiesStableAfterEnforcement": stable_after,
            "invalidAfterPureOrderEnforcement": invalid_after,
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
