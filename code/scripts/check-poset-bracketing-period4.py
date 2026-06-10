#!/usr/bin/env python3
"""
Pass 48 verification.

Three independent claims about antitone self-maps boxtimes of finite posets and
their eventual cycles {a,b} (comparable 2-cycle) or antichain k-cycles:

(A) Poset bracketing reduction + parity criterion (Thm 48a):
    For an antitone boxtimes on a finite poset L with comparable eventual 2-cycle
    {a,b}, a<b, the interval I=[a,b] is boxtimes-invariant; let F = Fix(boxtimes^2)
    cap I. Then boxtimes|_F is an order-reversing INVOLUTION of F, and boxtimes has
    a fixed point in I  <=>  boxtimes|_F has a fixed point in F.
    Sufficient: |F| odd  =>  fixed point (an involution of an odd set fixes a point).

(B) The Boolean-cube pathology (病的な例): on 2^[n] with boxtimes = complementation,
    {emptyset,[n]} is the unique COMPARABLE 2-cycle, |I| = 2^n, and boxtimes has NO
    fixed point ("cube-gap"); yet the SAME poset 2^2 carries a DIFFERENT order-
    reversing involution with fixed points. Hence |I| (and its parity) does NOT
    control bracketing; the controlling invariant is the cycle type of boxtimes on
    Fix(boxtimes^2).

(C) General-period antichain detachment (Prop 48c):
    If boxtimes p = p and {o_0,...,o_{k-1}} is an antichain k-cycle (k>=2) under
    boxtimes, then p is comparable to NO o_i (the fixed point is forced detached).
    Witness: the period-4 Rosser gadget R_4.
"""
import itertools, json, sys

# ---------- generic poset / antitone machinery ----------

def leq_closure(carrier, covers):
    """Reflexive-transitive closure of a cover relation -> leq dict-of-set."""
    leq = {x: {x} for x in carrier}
    for a, b in covers:
        leq[a].add(b)
    changed = True
    while changed:
        changed = False
        for x in carrier:
            for y in list(leq[x]):
                for z in leq[y]:
                    if z not in leq[x]:
                        leq[x].add(z); changed = True
    return leq

def is_antitone(carrier, leq, box):
    for x in carrier:
        for y in carrier:
            if y in leq[x]:           # x <= y
                if box[x] not in leq[box[y]]:   # need box[y] <= box[x]
                    return False
    return True

def orbit(box, T):
    seen = []
    x = T
    while x not in seen:
        seen.append(x); x = box[x]
    start = seen.index(x)
    return seen, seen[start:]          # full prefix+cycle, eventual cycle

def fixed_points(carrier, box):
    return [x for x in carrier if box[x] == x]

def interval(carrier, leq, a, b):
    return [x for x in carrier if (x in leq[a]) and (b in leq[x])]  # a<=x<=b

def comparable(leq, x, y):
    return (y in leq[x]) or (x in leq[y])

# ---------- (B) Boolean cube under complementation ----------

def boolean_cube(n):
    carrier = list(range(1 << n))
    full = (1 << n) - 1
    # subset leq = bitmask subset
    leq = {x: {y for y in carrier if (x & y) == x} for x in carrier}
    box = {x: full ^ x for x in carrier}          # complementation
    return carrier, leq, box, 0, full

def check_B():
    out = {}
    for n in (1, 2, 3, 4):
        carrier, leq, box, bot, top = boolean_cube(n)
        assert is_antitone(carrier, leq, box)
        # comparable 2-cycles reachable: seed at emptyset
        _, cyc = orbit(box, bot)
        comp2 = (len(cyc) == 2 and comparable(leq, cyc[0], cyc[1]))
        I = interval(carrier, leq, bot, top)      # whole cube
        fps = fixed_points(carrier, box)
        # count comparable vs antichain 2-cycles over all seeds
        comp_cycles = set(); anti_cycles = set()
        for T in carrier:
            _, c = orbit(box, T)
            if len(c) == 2:
                key = frozenset(c)
                if comparable(leq, c[0], c[1]): comp_cycles.add(key)
                else: anti_cycles.add(key)
        out[f"2^{n}"] = {
            "antitone": True,
            "seed_empty_cycle_len": len(cyc),
            "empty_top_comparable_2cycle": comp2,
            "interval_size": len(I),
            "boxtimes_fixed_points": fps,        # complementation has none
            "num_comparable_2cycles": len(comp_cycles),
            "num_antichain_2cycles": len(anti_cycles),
        }
    # the alternative order-reversing involution on 2^2 WITH fixed points:
    # carrier {0:00,1:01,2:10,3:11}; tau swaps 0<->3, FIXES 1 and 2.
    carrier, leq, _, bot, top = boolean_cube(2)
    tau = {0: 3, 3: 0, 1: 1, 2: 2}
    out["2^2_alt_involution"] = {
        "antitone": is_antitone(carrier, leq, tau),
        "is_involution": all(tau[tau[x]] == x for x in carrier),
        "fixed_points": fixed_points(carrier, tau),   # expect [1,2]
        "comment": "same poset 2^2, order-reversing involution with FPs => |I| parity not the invariant",
    }
    return out

# ---------- (A) parity criterion over all antitone maps on small carriers ----------

def all_antitone_maps(carrier, leq):
    n = len(carrier)
    for img in itertools.product(carrier, repeat=n):
        box = {carrier[i]: img[i] for i in range(n)}
        if is_antitone(carrier, leq, box):
            yield box

def check_A(carrier, leq, name):
    """For every antitone map with a comparable eventual 2-cycle reachable from
    some seed, verify: boxtimes|_F is an involution of F=Fix(box^2) cap I, FP-in-I
    <=> FP of that involution, and |F| odd => FP-in-I."""
    viol = 0
    examined = 0
    parity_sufficient_hits = 0
    for box in all_antitone_maps(carrier, leq):
        box2 = {x: box[box[x]] for x in carrier}
        F_all = [x for x in carrier if box2[x] == x]
        for T in carrier:
            _, cyc = orbit(box, T)
            if len(cyc) == 2 and comparable(leq, cyc[0], cyc[1]):
                a, b = (cyc[0], cyc[1]) if cyc[1] in leq[cyc[0]] else (cyc[1], cyc[0])
                I = interval(carrier, leq, a, b)
                F = [x for x in I if box2[x] == x]
                # box restricted to F is an involution of F
                inv_ok = all(box[x] in F and box[box[x]] == x for x in F)
                fp_in_I = any(box[x] == x for x in I)
                fp_of_inv = any(box[x] == x for x in F)
                examined += 1
                if not inv_ok or (fp_in_I != fp_of_inv):
                    viol += 1
                if len(F) % 2 == 1:
                    parity_sufficient_hits += 1
                    if not fp_in_I:           # parity criterion must guarantee FP
                        viol += 1
                break  # one comparable-2-cycle seed per map suffices
    return {"carrier": name, "comparable_2cycle_maps_examined": examined,
            "odd_F_cases": parity_sufficient_hits, "violations": viol}

# small carriers
def chain(n):
    carrier = list(range(n))
    covers = [(i, i + 1) for i in range(n - 1)]
    return carrier, leq_closure(carrier, covers)

def diamond_2x2():
    # 0 < 1,2 < 3  (= 2^2)
    carrier, leq, _, _, _ = boolean_cube(2)
    return carrier, leq

# ---------- (C) period-k antichain detachment + R_4 gadget ----------

def check_C():
    out = {}
    # R_4: carrier b(ot), o0,o1,o2,o3 (4-antichain), p (detached FP), U(top)
    carrier = ["b", "o0", "o1", "o2", "o3", "p", "U"]
    covers = []
    # bottom below everything, U above everything; o_i and p pairwise incomparable
    for x in ["o0", "o1", "o2", "o3", "p"]:
        covers.append(("b", x)); covers.append((x, "U"))
    covers.append(("b", "U"))
    leq = leq_closure(carrier, covers)
    box = {"b": "U", "U": "b",
           "o0": "o1", "o1": "o2", "o2": "o3", "o3": "o0",
           "p": "p"}
    _, cyc = orbit(box, "o0")
    antichain = all(not comparable(leq, x, y)
                    for x in cyc for y in cyc if x != y)
    p_detached = all(not comparable(leq, "p", o) for o in cyc)
    out["R_4"] = {
        "antitone": is_antitone(carrier, leq, box),
        "eventual_cycle": cyc,
        "cycle_len": len(cyc),
        "cycle_is_antichain": antichain,
        "fixed_points": fixed_points(carrier, box),
        "p_detached_from_cycle": p_detached,
    }
    # general claim: enumerate antitone maps on a pure k-antichain + bottom/top + p,
    # for k in 2..5, with boxtimes p = p and a k-cycle on the antichain; check p
    # is ALWAYS incomparable to the cycle (it is, by construction; we instead test
    # the CONTRAPOSITIVE: forcing p <= o_0 makes the map non-antitone OR collapses).
    detach_forced = {}
    for k in range(2, 6):
        anti = [f"o{i}" for i in range(k)]
        carrier2 = ["b"] + anti + ["p", "U"]
        # try to make p comparable to o0 and keep a genuine k-cycle + boxtimes p=p
        covers2 = [("b", x) for x in anti + ["p"]] + [(x, "U") for x in anti + ["p"]] + [("b", "U")]
        covers2.append(("p", "o0"))          # force p <= o0
        leq2 = leq_closure(carrier2, covers2)
        box2 = {"b": "U", "U": "b", "p": "p"}
        for i in range(k):
            box2[anti[i]] = anti[(i + 1) % k]
        detach_forced[f"k={k}"] = {
            "forced_p<=o0_keeps_antitone": is_antitone(carrier2, leq2, box2),
            "expected": False,   # Prop 48c: comparability is impossible -> not antitone
        }
    out["forced_comparability_breaks_antitone"] = detach_forced
    return out

# ---------- run ----------
if __name__ == "__main__":
    results = {"pass": 48}
    results["A_parity_bracketing"] = [
        check_A(*chain(2), "C2"),
        check_A(*chain(3), "C3"),
        check_A(*chain(4), "C4"),
        check_A(*chain(5), "C5"),
        check_A(*diamond_2x2(), "2^2"),
    ]
    results["B_boolean_cube"] = check_B()
    results["C_period_detachment"] = check_C()

    # overall verdict
    A_ok = all(r["violations"] == 0 for r in results["A_parity_bracketing"])
    B = results["B_boolean_cube"]
    B_ok = (all(B[f"2^{n}"]["boxtimes_fixed_points"] == [] for n in (1, 2, 3, 4))
            and B["2^2"]["empty_top_comparable_2cycle"]
            and B["2^2_alt_involution"]["fixed_points"] == [1, 2]
            and B["2^2_alt_involution"]["antitone"]
            and B["2^2_alt_involution"]["is_involution"])
    C = results["C_period_detachment"]
    C_ok = (C["R_4"]["antitone"] and C["R_4"]["cycle_len"] == 4
            and C["R_4"]["cycle_is_antichain"]
            and C["R_4"]["fixed_points"] == ["p"]
            and C["R_4"]["p_detached_from_cycle"]
            and all(v["forced_p<=o0_keeps_antitone"] is False
                    for v in C["forced_comparability_breaks_antitone"].values()))
    results["overall"] = {"A_parity": A_ok, "B_cube": B_ok, "C_detachment": C_ok,
                          "PASS": bool(A_ok and B_ok and C_ok)}
    print(json.dumps(results, indent=2))
    sys.exit(0 if results["overall"]["PASS"] else 1)
