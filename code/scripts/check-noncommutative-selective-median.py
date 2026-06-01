#!/usr/bin/env python3
"""
Pass 38 verification: selective-median escape for a non-abelian front.

This is the two-residual analogue of check-selective-median-bound.py.  It drops
commutativity and tests whether the same one-point median m = T v e_G makes the
left and right diagonal fibers principal for a non-abelian group front.

The seeded non-abelian case is S3.  The tensor is:
  - b is zero, T is the global unit;
  - the front F_k carries the group product, with a1 = e_G;
  - m*m=m, m*g=g and g*m=g for front elements g;
  - front-tail, tail-front, m-tail, tail-m, U-nonzero interactions collapse to U.

Full two-sided residuation is verified by checking that every left and right
fiber is principal in the finite order.
"""

import argparse
import itertools
import json


def compose(p, q):
    """Permutation composition p.q, using tuples of images of 0,1,2."""
    return tuple(p[i] for i in q)


def table_from_op(elements, op, label_of):
    """Generic Cayley-table builder. `elements[0]` MUST be the identity so that
    a1 = e_G in the B_N front. `op(x, y)` returns a group element; `label_of`
    maps an element to its display label."""
    index = {e: i for i, e in enumerate(elements)}
    table = [[index[op(x, y)] for y in elements] for x in elements]
    labels = [label_of(e) for e in elements]
    return labels, table


def s3_table():
    identity = (0, 1, 2)
    elements = [identity] + [p for p in itertools.permutations((0, 1, 2)) if p != identity]
    index = {p: i for i, p in enumerate(elements)}
    table = [[index[compose(x, y)] for y in elements] for x in elements]
    labels = ["e"] + ["".join(str(i + 1) for i in p) for p in elements[1:]]
    return labels, table


def cyclic_table(k):
    """Z/kZ - abelian control with k conjugacy classes (one per element)."""
    elements = list(range(k))
    return table_from_op(
        elements,
        lambda x, y: (x + y) % k,
        lambda e: "e" if e == 0 else f"g{e}",
    )


def dihedral_table(n):
    """D_n of order 2n, elements (r, s) with r in Z/n, s in {0,1};
    (r1,s1)(r2,s2) = (r1 + (-1)^s1 r2 mod n, s1 xor s2). Identity = (0,0).
    For n=4 this is D4 (order 8), non-abelian, 5 conjugacy classes."""
    elements = [(0, 0)] + [(r, s) for s in (0, 1) for r in range(n) if (r, s) != (0, 0)]

    def op(a, c):
        (r1, s1), (r2, s2) = a, c
        return ((r1 + (-1) ** s1 * r2) % n, (s1 + s2) % 2)

    def lab(e):
        r, s = e
        if e == (0, 0):
            return "e"
        return ("r" if s == 0 else "sr") + (str(r) if r else "")

    return table_from_op(elements, op, lab)


def quaternion_table():
    """Q8 = {+-1, +-i, +-j, +-k}, non-abelian, 5 conjugacy classes, a UNIQUE
    involution (-1) and every subgroup normal - a structurally different
    non-abelian witness from D4 (which has non-normal reflections)."""
    # Represent each element as a unit quaternion (w, x, y, z) with entries in
    # {0, +-1} and exactly one nonzero coordinate.
    e = (1, 0, 0, 0)
    elements = [
        e, (-1, 0, 0, 0),
        (0, 1, 0, 0), (0, -1, 0, 0),
        (0, 0, 1, 0), (0, 0, -1, 0),
        (0, 0, 0, 1), (0, 0, 0, -1),
    ]

    def qmul(a, c):
        a1, b1, c1, d1 = a
        a2, b2, c2, d2 = c
        return (
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
        )

    labels = {
        (1, 0, 0, 0): "e", (-1, 0, 0, 0): "-1",
        (0, 1, 0, 0): "i", (0, -1, 0, 0): "-i",
        (0, 0, 1, 0): "j", (0, 0, -1, 0): "-j",
        (0, 0, 0, 1): "k", (0, 0, 0, -1): "-k",
    }
    return table_from_op(elements, qmul, lambda x: labels[x])


def build_order(group_size, median=True, cap=False):
    assert not (median and cap)
    depth = group_size
    names = ["b", "T"] + [f"a{i}" for i in range(1, depth + 2)] + ["s", "U"]
    if median:
        names.append("m")
    if cap:
        names.append("c")

    b = names.index("b")
    T = names.index("T")
    U = names.index("U")
    s = names.index("s")
    extra = len(names) - 1 if (median or cap) else None
    front = [names.index(f"a{i}") for i in range(1, group_size + 1)]
    tail = [names.index(f"a{i}") for i in range(group_size + 1, depth + 2)] + [s]
    e_idx = front[0]

    n = len(names)
    leq = [[i == j for j in range(n)] for i in range(n)]
    for x in range(n):
        leq[b][x] = True
        leq[x][U] = True
    leq[s][names.index(f"a{depth + 1}")] = True

    if median:
        leq[b][extra] = True
        leq[T][extra] = True
        leq[e_idx][extra] = True
        leq[extra][U] = True
    if cap:
        leq[b][extra] = True
        for g in front:
            leq[g][extra] = True
        leq[extra][U] = True

    for mid in range(n):
        for x in range(n):
            if leq[x][mid]:
                for y in range(n):
                    if leq[mid][y]:
                        leq[x][y] = True

    return {
        "names": names,
        "leq": leq,
        "front": front,
        "tail": tail,
        "b": b,
        "T": T,
        "U": U,
        "s": s,
        "extra": extra,
        "e": e_idx,
    }


def build_tensor(group_table, median=True, cap=False):
    group_size = len(group_table)
    data = build_order(group_size, median=median, cap=cap)
    names = data["names"]
    front = data["front"]
    front_set = set(front)
    b = data["b"]
    T = data["T"]
    U = data["U"]
    extra = data["extra"]
    group_pos = {front[i]: i for i in range(group_size)}
    n = len(names)

    def mul(x, y):
        if x == b or y == b:
            return b
        if x == T:
            return y
        if y == T:
            return x
        if x in front_set and y in front_set:
            return front[group_table[group_pos[x]][group_pos[y]]]
        if median and (x == extra or y == extra):
            other = y if x == extra else x
            if other == extra:
                return extra
            if other in front_set:
                return other
            return U
        if cap and (x == extra or y == extra):
            other = y if x == extra else x
            if other == extra:
                return extra
            return U
        return U

    data["mul"] = [[mul(x, y) for y in range(n)] for x in range(n)]
    return data


def maximal_names(data, fiber):
    leq = data["leq"]
    names = data["names"]
    maximal = [x for x in fiber if not any(x != y and leq[x][y] for y in fiber)]
    principal = [x for x in fiber if all(leq[y][x] for y in fiber)]
    return [names[x] for x in maximal], [names[x] for x in principal]


def verify(data):
    names = data["names"]
    leq = data["leq"]
    mul = data["mul"]
    T = data["T"]
    n = len(names)
    failures = []

    for x in range(n):
        if mul[T][x] != x or mul[x][T] != x:
            failures.append({"check": "unit", "witness": [names[x]]})

    for x in range(n):
        for y in range(n):
            for z in range(n):
                if mul[mul[x][y]][z] != mul[x][mul[y][z]]:
                    failures.append(
                        {
                            "check": "associative",
                            "witness": [
                                names[x],
                                names[y],
                                names[z],
                                names[mul[mul[x][y]][z]],
                                names[mul[x][mul[y][z]]],
                            ],
                        }
                    )
                    return failures

    for x in range(n):
        for y in range(n):
            if not leq[x][y]:
                continue
            for z in range(n):
                if not leq[mul[x][z]][mul[y][z]]:
                    failures.append(
                        {
                            "check": "left-monotone",
                            "witness": [names[x], names[y], names[z], names[mul[x][z]], names[mul[y][z]]],
                        }
                    )
                if not leq[mul[z][x]][mul[z][y]]:
                    failures.append(
                        {
                            "check": "right-monotone",
                            "witness": [names[z], names[x], names[y], names[mul[z][x]], names[mul[z][y]]],
                        }
                    )

    for a in range(n):
        for c in range(n):
            left_fiber = [x for x in range(n) if leq[mul[a][x]][c]]
            _maximal, principal = maximal_names(data, left_fiber)
            if len(principal) != 1:
                failures.append(
                    {
                        "check": "left-residual-principal",
                        "witness": [names[a], names[c], [names[x] for x in left_fiber], principal],
                    }
                )
            right_fiber = [x for x in range(n) if leq[mul[x][a]][c]]
            _maximal, principal = maximal_names(data, right_fiber)
            if len(principal) != 1:
                failures.append(
                    {
                        "check": "right-residual-principal",
                        "witness": [names[c], names[a], [names[x] for x in right_fiber], principal],
                    }
                )

    return failures


def diagonal_fibers(data, target_front_index=1):
    names = data["names"]
    leq = data["leq"]
    mul = data["mul"]
    a = data["front"][target_front_index]
    left = [x for x in range(len(names)) if leq[mul[a][x]][a]]
    right = [x for x in range(len(names)) if leq[mul[x][a]][a]]
    left_maximal, left_principal = maximal_names(data, left)
    right_maximal, right_principal = maximal_names(data, right)
    return {
        "frontElement": names[a],
        "leftFiber": [names[x] for x in left],
        "leftMaximal": left_maximal,
        "leftPrincipal": left_principal,
        "rightFiber": [names[x] for x in right],
        "rightMaximal": right_maximal,
        "rightPrincipal": right_principal,
    }


def antitone_median_image(data):
    names = data["names"]
    leq = data["leq"]
    extra = data["extra"]
    front = data["front"]
    if extra is None or names[extra] != "m":
        return None

    # boxtimes(T)=a1 and boxtimes(e_G=a1)=a2 in the B_N orbit.
    constraints = [front[0], front[1]]
    admissible = [names[x] for x in range(len(names)) if all(leq[x][target] for target in constraints)]
    return {
        "constraints": [names[x] for x in constraints],
        "admissibleValues": admissible,
        "forcedValue": admissible[0] if len(admissible) == 1 else None,
    }


def run_case(label, group_labels, group_table, median=True, cap=False):
    data = build_tensor(group_table, median=median, cap=cap)
    failures = verify(data)
    diag = diagonal_fibers(data)
    return {
        "case": label,
        "group": group_labels,
        "carrier": data["names"],
        "median": median,
        "cap": cap,
        "holds": not failures,
        "failureCount": len(failures),
        "failures": failures[:8],
        "diagonalFibers": diag,
        "antitoneMedianImage": antitone_median_image(data),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()

    # Group battery: differing conjugacy-class counts and normal-subgroup
    # structure, to test whether ONE selective median suffices uniformly.
    #   S3   : order 6, non-abelian, 3 conjugacy classes
    #   D4   : order 8, non-abelian, 5 classes, NON-normal reflections
    #   Q8   : order 8, non-abelian, 5 classes, every subgroup normal
    #   Z/4  : order 4, abelian control, 4 classes
    groups = [
        ("S3", *s3_table()),
        ("D4", *dihedral_table(4)),
        ("Q8", *quaternion_table()),
        ("Z4", *cyclic_table(4)),
    ]

    cases = []
    uniformity = []
    for gname, labels, table in groups:
        median_case = run_case(f"{gname}-selective-median", labels, table, median=True)
        no_extra = run_case(f"{gname}-no-extra-control", labels, table, median=False)
        full_cap = run_case(f"{gname}-full-cap-control", labels, table, median=False, cap=True)
        cases.extend([median_case, no_extra, full_cap])
        uniformity.append({
            "group": gname,
            "order": len(table),
            "selectiveMedianHolds": median_case["holds"],
            "mediansNeeded": 1 if median_case["holds"] else None,
            "leftPrincipal": median_case["diagonalFibers"]["leftPrincipal"],
            "rightPrincipal": median_case["diagonalFibers"]["rightPrincipal"],
            "forcedBoxtimesM": median_case["antitoneMedianImage"]["forcedValue"],
            "noMedianControlHolds": no_extra["holds"],
            "fullCapControlHolds": full_cap["holds"],
        })

    all_escape = all(u["selectiveMedianHolds"] for u in uniformity)
    all_controls_fail = all(
        (not u["noMedianControlHolds"]) and (not u["fullCapControlHolds"])
        for u in uniformity
    )
    report = {
        "summary": {
            "target": "non-abelian selective median (group battery)",
            "groups": [u["group"] for u in uniformity],
            "allEscapeWithSingleMedian": all_escape,
            "allControlsFail": all_controls_fail,
            "uniformMediansNeeded": 1 if all_escape else None,
            "uniformity": uniformity,
        },
        "cases": cases,
        "conclusion": (
            "One selective median m=T v e_G makes both diagonal fibers principal "
            "for every tested group (S3, D4, Q8, Z/4): the number of medians "
            "needed is 1, independent of conjugacy-class count, so it is NOT a new "
            "group invariant of the front."
            if all_escape else
            "Single selective median does NOT suffice uniformly; see per-group data."
        ),
    }

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
