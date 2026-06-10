#!/usr/bin/env python3
"""Pass 45 verification: is "orbit-descent <=> exists attached fixed point"
a theorem for an *arbitrary* finite preAPS, or only on the M3 carrier where
Pass 44 verified it?

We enumerate all antitone self-maps of several small posets, classify the
T-orbit's eventual behavior, and test the candidate equivalence.

Key definitions (Pass 41/42/44):
  * orbit          o_n = boxtimes^n(T)
  * descends       exists k with o_{k+1} = o_k  (eventual constancy)
  * eventual cycle the set the orbit is trapped in once it becomes periodic
  * fixed point p  boxtimes(p) = p
  * attached       p comparable to some o_n
  * detached       p incomparable to every o_n

Regime trichotomy on the eventual 2-cycle {e*, o*} (boxtimes swaps them):
  (i)   degenerate  e* = o*           -> orbit DESCENDS
  (ii)  antichain   e* || o*          -> Rosser/R2 regime (detached only)
  (iii) chain       o* < e* (distinct)-> NEW: non-descending yet attachable

Claim under test (Pass 44 "exact gate", generalized off M3):
        non-descending orbit  ==>  no attached fixed point.
The C5 order-reversing involution is the intended counterexample.
"""

import itertools
import json
import os

# ----------------------------------------------------------------------
# Poset machinery
# ----------------------------------------------------------------------

def leq_from_covers(elements, covers):
    """Reflexive-transitive closure of a cover relation -> leq predicate set."""
    leq = {(x, x) for x in elements}
    leq |= set(covers)
    changed = True
    while changed:
        changed = False
        for (a, b) in list(leq):
            for (c, d) in list(leq):
                if b == c and (a, d) not in leq:
                    leq.add((a, d))
                    changed = True
    return leq


def make_poset(elements, covers):
    leq = leq_from_covers(elements, covers)
    return {"elements": list(elements), "leq": leq}


def is_leq(P, x, y):
    return (x, y) in P["leq"]


def comparable(P, x, y):
    return is_leq(P, x, y) or is_leq(P, y, x)


def is_antitone(P, f):
    els = P["elements"]
    for x in els:
        for y in els:
            if is_leq(P, x, y) and not is_leq(P, f[y], f[x]):
                return False
    return True


def antitone_maps(P):
    els = P["elements"]
    for image in itertools.product(els, repeat=len(els)):
        f = dict(zip(els, image))
        if is_antitone(P, f):
            yield f


def orbit(f, T):
    """Return (prefix, cycle) with the eventual cycle as a list."""
    seen = []
    x = T
    while x not in seen:
        seen.append(x)
        x = f[x]
    start = seen.index(x)
    return seen[:start], seen[start:]


def classify(P, f, T):
    pre, cyc = orbit(f, T)
    orbit_set = set(pre) | set(cyc)
    descends = len(cyc) == 1            # eventual constancy
    period = len(cyc)
    fixed = [x for x in P["elements"] if f[x] == x]
    attached = [p for p in fixed if any(comparable(P, p, o) for o in orbit_set)]
    detached = [p for p in fixed if p not in attached]

    # eventual-cycle order type (only meaningful for period 2)
    cycle_type = None
    if period == 1:
        cycle_type = "degenerate"
    elif period == 2:
        a, b = cyc
        if comparable(P, a, b):
            cycle_type = "chain"
        else:
            cycle_type = "antichain"
    else:
        cycle_type = f"period-{period}"

    return {
        "orbit_prefix": pre,
        "cycle": cyc,
        "period": period,
        "descends": descends,
        "cycle_type": cycle_type,
        "fixed_points": fixed,
        "attached": attached,
        "detached": detached,
        "has_attached": len(attached) > 0,
    }


# ----------------------------------------------------------------------
# Posets under test
# ----------------------------------------------------------------------

def chain(n):
    els = list(range(n))
    covers = [(i, i + 1) for i in range(n - 1)]
    return make_poset(els, covers), els


def m3_diamond():
    # bot < x,y,z < top  (three incomparable middles)
    els = ["bot", "x", "y", "z", "top"]
    covers = [("bot", "x"), ("bot", "y"), ("bot", "z"),
              ("x", "top"), ("y", "top"), ("z", "top")]
    return make_poset(els, covers), els


def m4_diamond():
    els = ["bot", "a", "b", "c", "d", "top"]
    covers = [("bot", m) for m in ("a", "b", "c", "d")] + \
             [(m, "top") for m in ("a", "b", "c", "d")]
    return make_poset(els, covers), els


def n5():
    # N5: bot < a < c < top, bot < b < top, a||b, c||b
    els = ["bot", "a", "c", "b", "top"]
    covers = [("bot", "a"), ("a", "c"), ("c", "top"),
              ("bot", "b"), ("b", "top")]
    return make_poset(els, covers), els


# ----------------------------------------------------------------------
# Experiments
# ----------------------------------------------------------------------

def survey(P, name, Ts):
    """For each designated T, enumerate antitone maps and test the equivalence."""
    out = {}
    for T in Ts:
        total = 0
        descend_cnt = 0
        nondescend_cnt = 0
        # the dangerous regime: non-descending orbit WITH an attached FP
        counterexamples = []
        # descent-half check: every descending map has an attached FP
        descent_half_violations = []
        cycle_type_counts = {}
        for f in antitone_maps(P):
            total += 1
            c = classify(P, f, T)
            ct = c["cycle_type"]
            cycle_type_counts[ct] = cycle_type_counts.get(ct, 0) + 1
            if c["descends"]:
                descend_cnt += 1
                if not c["has_attached"]:
                    descent_half_violations.append({"map": f, "info": c})
            else:
                nondescend_cnt += 1
                if c["has_attached"]:
                    counterexamples.append({
                        "map": {k: f[k] for k in P["elements"]},
                        "cycle": c["cycle"],
                        "cycle_type": c["cycle_type"],
                        "attached_fixed_points": c["attached"],
                    })
        out[str(T)] = {
            "antitone_maps": total,
            "descending": descend_cnt,
            "non_descending": nondescend_cnt,
            "cycle_type_counts": cycle_type_counts,
            "descent_implies_attachment_violations": len(descent_half_violations),
            "nondescent_with_attached_FP": len(counterexamples),
            "counterexample_sample": counterexamples[:3],
        }
    return {"poset": name, "results": out}


def reversal_witness():
    """Explicit C5 order-reversing involution: the pathological 'third regime'."""
    P, els = chain(5)              # 0 < 1 < 2 < 3 < 4
    f = {i: 4 - i for i in els}    # r(x) = 4 - x  (antitone involution)
    T = 3                          # interior seed; orbit 3 -> 1 -> 3 -> ...
    c = classify(P, f, T)
    return {
        "carrier": "C5 chain 0<1<2<3<4",
        "boxtimes": "reversal r(x)=4-x",
        "T": T,
        "antitone": is_antitone(P, f),
        "involution": all(f[f[x]] == x for x in els),
        "orbit_of_T": c["orbit_prefix"] + c["cycle"],
        "cycle": c["cycle"],
        "cycle_type": c["cycle_type"],
        "descends": c["descends"],
        "fixed_points": c["fixed_points"],
        "attached": c["attached"],
        "detached": c["detached"],
        "verdict": ("COUNTEREXAMPLE: non-descending orbit with an ATTACHED "
                    "fixed point" if (not c["descends"] and c["attached"])
                    else "no counterexample here"),
    }


def main():
    report = {
        "pass": 45,
        "title": ("descent<=>attachment is FALSE for general finite preAPS: "
                  "the order-reversing chain involution is the pathological "
                  "chain-cycle third regime"),
        "explicit_C5_reversal_counterexample": reversal_witness(),
        "surveys": [],
    }

    Pm3, _ = m3_diamond()
    report["surveys"].append(survey(Pm3, "M3 diamond", ["x"]))

    for n in (3, 4, 5, 6, 7):
        Pc, els = chain(n)
        # seed at the interior point just below the centre when possible
        Ts = sorted(set([els[-1], els[len(els) // 2], els[max(0, len(els) - 2)]]))
        report["surveys"].append(survey(Pc, f"C{n} chain", Ts))

    Pn5, _ = n5()
    report["surveys"].append(survey(Pn5, "N5", ["top", "c"]))

    Pm4, _ = m4_diamond()
    report["surveys"].append(survey(Pm4, "M4 diamond", ["a"]))

    # Overall verdict: at least one non-descending+attached counterexample exists,
    # and the descent->attachment half is never violated.
    any_counter = False
    any_descent_violation = False
    for s in report["surveys"]:
        for r in s["results"].values():
            if r["nondescent_with_attached_FP"] > 0:
                any_counter = True
            if r["descent_implies_attachment_violations"] > 0:
                any_descent_violation = True
    cw = report["explicit_C5_reversal_counterexample"]
    report["overall"] = {
        "explicit_counterexample_found": cw["verdict"].startswith("COUNTEREXAMPLE"),
        "survey_counterexample_found": any_counter,
        "descent_implies_attachment_half_holds_everywhere": not any_descent_violation,
        "conclusion": ("The clean equivalence is REFUTED: descent => attachment "
                       "is universally valid (carrier-independent), but "
                       "attachment => descent FAILS via chain-cycles. The "
                       "eventual-2-cycle order type (degenerate/antichain/chain) "
                       "is the correct refinement."),
        "verdict": ("PASS"
                    if (cw["verdict"].startswith("COUNTEREXAMPLE")
                        and not any_descent_violation)
                    else "FAIL"),
    }

    here = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.normpath(os.path.join(
        here, "..", "..", "artifacts", "reports",
        "descent-attachment-general-check.json"))
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    print(json.dumps(report["overall"], indent=2))
    print("explicit C5 witness:",
          json.dumps(report["explicit_C5_reversal_counterexample"], indent=2))
    print("written:", out_path)


if __name__ == "__main__":
    main()
