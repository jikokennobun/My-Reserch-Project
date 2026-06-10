#!/usr/bin/env python3
"""
Pass 51 verification (APS / G2-ZOO). Closes the three [New (Pass 50)] residues.

(A) COMPLETENESS of the vertex-counting invariant e(F^tau) (Thm 50a follow-up).
    For an antitone box, Fix(box) is an ANTICHAIN, hence Delta(F^tau) is DISCRETE
    and e(F^tau) = chi(Delta(F^tau)) = |F^tau| identically. So e = 0 iff
    F^tau = empty iff no bracket: e is a complete (tautological) bracket invariant,
    and "e = 0 with F^tau != empty" is IMPOSSIBLE. The hoped-for order-complex-
    circle pathology cannot occur. 6-crown coda: its order complex is S^1 (chi=0)
    but it is NOT an antichain, so it is the fixed-vertex set of NO order-reversing
    involution.

(B) PHANTOM as cohomology (Constr 50b follow-up).
    Ob^*(P_r) = [0 -> C^1 -> 0], C^1 = F^{failed covers}, C^0 = 0 (infinitary
    rigidity), so H^1 = F^r and b_phantom(P_r) = dim H^1. The phantom is the lim^1
    of the image tower; additive over independent arms. At finite truncation the
    gap is removable (the obstruction is irreducibly infinitary). Verified:
    global antitonicity, exactly r failed covers, gap independence.

(C) ARITHMETIC LIFT: Loeb/Rosser <-> integral/non-integral unit (Thm 50d
    follow-up). Dictionary:
      ORBIT-ATTACHED <-> Loeb (de Jongh-Sambin) <-> INTEGRAL unit (1 = top)
      DETACHED       <-> Rosser-evades-Loeb      <-> NON-INTEGRAL unit (1 != top)
    Verified: the attached 3-chain Goedel model admits a full residuated tensor
    with unit = top; the detached Rosser R_2 (M_3) admits NO integral-unit tensor,
    only non-integral ones.
"""
import json, os
from itertools import combinations, product as iproduct

REPORT = os.path.join(os.path.dirname(__file__), "..", "..",
                      "artifacts", "reports",
                      "pass51-euler-completeness-phantom-cohomology-rosser-unit-check.json")

# ===================================================================
# Poset utilities
# ===================================================================
def is_partial_order(leq, n):
    for x in range(n):
        if not leq[x][x]:
            return False
    for x in range(n):
        for y in range(n):
            if leq[x][y] and leq[y][x] and x != y:
                return False
            for z in range(n):
                if leq[x][y] and leq[y][z] and not leq[x][z]:
                    return False
    return True

def all_posets(n):
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    out = []
    for bits in iproduct([0, 1], repeat=len(pairs)):
        leq = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        for (i, j), b in zip(pairs, bits):
            leq[i][j] = b
        if is_partial_order(leq, n):
            out.append(leq)
    return out

def antitone_maps(leq, n):
    for f in iproduct(range(n), repeat=n):
        ok = True
        for x in range(n):
            for y in range(n):
                if leq[x][y] and not leq[f[y]][f[x]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            yield f

def is_antichain(S, leq):
    return all(x == y or (not leq[x][y] and not leq[y][x])
               for x in S for y in S)

def euler_order_complex(verts, leq):
    chi = 0
    vs = list(verts)
    for r in range(1, len(vs) + 1):
        for S in combinations(vs, r):
            if all(leq[x][y] or leq[y][x] for x, y in combinations(S, 2)):
                chi += (-1) ** (r - 1)
    return chi

# ===================== (A) e completeness =====================
def check_a():
    violations_antichain = 0
    violations_e_eq_card = 0
    violations_e0_nonempty = 0
    total_maps = 0
    e_values = {}
    for n in range(1, 6):
        for leq in all_posets(n):
            for f in antitone_maps(leq, n):
                total_maps += 1
                fix = [x for x in range(n) if f[x] == x]
                if not is_antichain(fix, leq):
                    violations_antichain += 1
                e = euler_order_complex(fix, leq)
                if e != len(fix):
                    violations_e_eq_card += 1
                if e == 0 and len(fix) > 0:
                    violations_e0_nonempty += 1
                e_values.setdefault(len(fix), set()).add(e)

    # 6-crown: 3 minima 0,1,2 ; 3 maxima 3,4,5 ; x_i<y_i and x_i<y_{i-1 mod 3}.
    crown = [[1 if i == j else 0 for j in range(6)] for i in range(6)]
    for i in range(3):
        crown[i][3 + i] = 1
        crown[i][3 + ((i - 1) % 3)] = 1
    assert is_partial_order(crown, 6)
    crown_chi = euler_order_complex(range(6), crown)   # = S^1, chi = 0
    crown_is_antichain = is_antichain(range(6), crown)

    ok = (violations_antichain == 0 and violations_e_eq_card == 0
          and violations_e0_nonempty == 0
          and crown_chi == 0 and not crown_is_antichain)
    return {
        "total_antitone_maps_scanned": total_maps,
        "posets_sizes": "1..5",
        "violations_Fix_is_antichain": violations_antichain,
        "violations_e_equals_cardinality": violations_e_eq_card,
        "violations_e0_with_nonempty_Fix": violations_e0_nonempty,
        "e_values_by_fixcount": {k: sorted(v) for k, v in sorted(e_values.items())},
        "crown_order_complex_chi": crown_chi,
        "crown_is_antichain": crown_is_antichain,
        "note": "Fix(antitone) is always an antichain (p<q fixed => q=box q<=box p=p). "
                "Hence Delta(F^tau) is discrete and e(F^tau)=|F^tau|. e=0 iff Fix empty "
                "iff no bracket: e is a complete bracket invariant; e=0 with Fix nonempty "
                "is impossible. The 6-crown has chi=0 (an order-complex S^1) but is NOT an "
                "antichain, so it is the fixed-vertex set of no order-reversing involution.",
        "PASS": ok,
    }

# ===================== (B) phantom cohomology =====================
def build_P_r(r, K):
    """
    Fan P_r: bottom b, top U, r arms sharing only b,U and pairwise incomparable.
    Arm i: chain o^i_0<...<o^i_{K-1}<a*_i (sup) and output pair g_i<bt_i.
    box: box(o^i_0)=U, box(o^i_n)=bt_i (n>=1), box(a*_i)=g_i, box(g_i)=U,
    box(bt_i)=b, box(b)=U, box(U)=b. Then meet_n box(o^i_n)=bt_i but
    box(a*_i)=g_i<bt_i: join-continuity fails at the single cover a*_i.
    """
    elems = ["b", "U"]
    arm_os = {}
    for i in range(r):
        os_i = [f"o{i}_{n}" for n in range(K)]
        arm_os[i] = os_i
        elems += os_i + [f"a{i}", f"g{i}", f"bt{i}"]
    idx = {e: k for k, e in enumerate(elems)}
    N = len(elems)
    leq = [[1 if a == b else 0 for b in range(N)] for a in range(N)]

    def setle(x, y):
        leq[idx[x]][idx[y]] = 1

    for e in elems:
        setle("b", e)
        setle(e, "U")
    for i in range(r):
        os_i = arm_os[i]
        for n in range(K):
            for nn in range(n, K):
                setle(os_i[n], os_i[nn])
            setle(os_i[n], f"a{i}")
        setle(f"g{i}", f"bt{i}")
    for k in range(N):
        for x in range(N):
            for y in range(N):
                if leq[x][k] and leq[k][y]:
                    leq[x][y] = 1

    def le(x, y):
        return leq[idx[x]][idx[y]] == 1

    box = {"b": "U", "U": "b"}
    for i in range(r):
        os_i = arm_os[i]
        box[os_i[0]] = "U"
        for n in range(1, K):
            box[os_i[n]] = f"bt{i}"
        box[f"a{i}"] = f"g{i}"
        box[f"g{i}"] = "U"
        box[f"bt{i}"] = "b"
    return elems, idx, le, box

def check_b():
    fans = {}
    ok = True
    for r in (1, 2, 3):
        K = 4
        elems, idx, le, box = build_P_r(r, K)
        antitone = all((not le(x, y)) or le(box[y], box[x])
                       for x in elems for y in elems)

        def meet(S):
            cands = [z for z in elems if all(le(z, s) for s in S)]
            for z in cands:
                if all(le(w, z) for w in cands):
                    return z
            return None

        failed = 0
        gaps = []
        for i in range(r):
            os_i = [f"o{i}_{n}" for n in range(K)]
            inf_box = meet([box[o] for o in os_i])
            box_sup = box[f"a{i}"]
            if le(box_sup, inf_box) and box_sup != inf_box:
                failed += 1
                gaps.append((box_sup, inf_box))

        indep = True
        for a in range(len(gaps)):
            for c in range(a + 1, len(gaps)):
                ga, gc = gaps[a], gaps[c]
                if any(le(x, y) or le(y, x) for x in ga for y in gc
                       if x not in ("b", "U") and y not in ("b", "U")):
                    indep = False

        finite_removable = True
        for i in range(r):
            os_i = [f"o{i}_{n}" for n in range(K)]
            inf_box = meet([box[o] for o in os_i])
            trial = dict(box)
            trial[f"a{i}"] = inf_box
            tantitone = all((not le(x, y)) or le(trial[y], trial[x])
                            for x in elems for y in elems)
            if not tantitone:
                finite_removable = False

        H1_dim = failed
        fans[r] = {"antitone": antitone, "failed_covers": failed,
                   "gap_independence": indep,
                   "finite_stage_gap_removable": finite_removable,
                   "dim_H1_infinite_limit": H1_dim, "b_phantom": r}
        ok = ok and antitone and failed == r and indep and H1_dim == r
    return {"fans": fans,
            "note": "Ob^*(P_r)=[0->C^1->0], C^1=F^{failed covers}; in the infinite limit "
                    "C^0=0, so dim H^1 = #failed covers = r = b_phantom. The phantom is the "
                    "lim^1 of the image tower box(o^i_n), additive over independent arms. At "
                    "finite truncation the gap is removable (finite_stage_gap_removable=true): "
                    "the phantom is irreducibly infinitary. Over a field lim^1 of finite-dim'l "
                    "towers vanishes, so the cohomology is genuine over Z; the check verifies "
                    "antitonicity, the failed-cover count r, and gap independence.",
            "PASS": ok}

# ===================== (C) Rosser/Loeb <-> unit =====================
def lattice_from_le(elems, le):
    def join(x, y):
        ub = [z for z in elems if le(x, z) and le(y, z)]
        for z in ub:
            if all(le(z, w) for w in ub):
                return z
        return None
    def meet(x, y):
        lb = [z for z in elems if le(z, x) and le(z, y)]
        for z in lb:
            if all(le(w, z) for w in lb):
                return z
        return None
    return join, meet

def residuated_tensors(elems, le, join, bot, require_unit=None, limit=None):
    def covers(x):
        below = [y for y in elems if le(y, x) and y != x]
        return [y for y in below if not any(le(y, z) and z != y and z != x and le(z, x)
                                            for z in below)]
    jirr = [x for x in elems if x != bot and len(covers(x)) == 1]
    pairs = [(jirr[i], jirr[j]) for i in range(len(jirr)) for j in range(i, len(jirr))]

    def extend(tab):
        prod = {}
        for x in elems:
            jx = [j for j in jirr if le(j, x)]
            for y in elems:
                jy = [j for j in jirr if le(j, y)]
                acc = bot
                for a in jx:
                    for b in jy:
                        key = (a, b) if (a, b) in tab else (b, a)
                        acc = join(acc, tab[key])
                prod[(x, y)] = acc
        return prod

    found = []
    count = 0
    for vals in iproduct(elems, repeat=len(pairs)):
        tab = {p: v for p, v in zip(pairs, vals)}
        prod = extend(tab)
        if any(prod[(x, y)] != prod[(y, x)] for x in elems for y in elems):
            continue
        if any(prod[(bot, x)] != bot for x in elems):
            continue
        if not all((not le(x, y)) or le(prod[(x, z)], prod[(y, z)])
                   for x in elems for y in elems for z in elems):
            continue
        if any(prod[(prod[(x, y)], z)] != prod[(x, prod[(y, z)])]
               for x in elems for y in elems for z in elems):
            continue
        units = [e for e in elems if all(prod[(e, x)] == x for x in elems)]
        if not units:
            continue
        if require_unit is not None and require_unit not in units:
            continue
        resid = True
        for a in elems:
            for b in elems:
                S = [x for x in elems if le(prod[(a, x)], b)]
                if not S:
                    resid = False
                    break
                m = S[0]
                for x in S:
                    m = join(m, x)
                if not le(prod[(a, m)], b):
                    resid = False
                    break
            if not resid:
                break
        if not resid:
            continue
        found.append((units, prod))
        count += 1
        if limit and count >= limit:
            break
    return found, jirr

def check_c():
    # Detached Rosser model R_2 = M_3 diamond
    R = ["bot", "o0", "o1", "p", "top"]
    Rle_pairs = {("bot", x) for x in R} | {(x, "top") for x in R} | {(x, x) for x in R}
    def Rle(x, y): return (x, y) in Rle_pairs
    Rjoin, _ = lattice_from_le(R, Rle)
    Rbox = {"bot": "top", "top": "bot", "o0": "o1", "o1": "o0", "p": "p"}
    R_antitone = all((not Rle(x, y)) or Rle(Rbox[y], Rbox[x]) for x in R for y in R)
    R_detached = (not Rle("p", "o0") and not Rle("o0", "p")
                  and not Rle("p", "o1") and not Rle("o1", "p"))
    integral_R, jirrR = residuated_tensors(R, Rle, Rjoin, "bot",
                                           require_unit="top", limit=1)
    any_R, _ = residuated_tensors(R, Rle, Rjoin, "bot", limit=200)
    nonintegral_units_R = sorted({u for units, _ in any_R for u in units if u != "top"})

    # Attached Loeb model: 3-chain Goedel  bot < c < top
    C = ["bot", "c", "top"]
    order = {"bot": 0, "c": 1, "top": 2}
    def Cle(x, y): return order[x] <= order[y]
    Cjoin, _ = lattice_from_le(C, Cle)
    Cbox = {"bot": "top", "top": "bot", "c": "c"}
    C_antitone = all((not Cle(x, y)) or Cle(Cbox[y], Cbox[x]) for x in C for y in C)
    C_attached = Cle("bot", "c") and Cle("c", "top")
    integral_C, _ = residuated_tensors(C, Cle, Cjoin, "bot",
                                       require_unit="top", limit=1)

    ok = (R_antitone and R_detached and len(integral_R) == 0
          and len(nonintegral_units_R) >= 1
          and C_antitone and C_attached and len(integral_C) >= 1)
    return {
        "rosser_R2_detached": {"antitone": R_antitone, "detached": R_detached,
                               "integral_unit_top_tensors": len(integral_R),
                               "nonintegral_units_available": nonintegral_units_R,
                               "join_irreducibles": jirrR},
        "loeb_C3_attached": {"antitone": C_antitone, "bracketed_attached": C_attached,
                             "integral_unit_top_tensors": len(integral_C)},
        "dictionary": "attached <-> Loeb (de Jongh-Sambin) <-> integral unit (1=top); "
                      "detached <-> Rosser-evades-Loeb <-> non-integral unit (1!=top). "
                      "R_2: 0 integral tensors, non-integral available. C_3 Goedel chain: "
                      "integral unit top works. Integral/non-integral is the algebraic image "
                      "of the Loeb/Rosser gate.",
        "PASS": ok,
    }

def main():
    A = check_a(); B = check_b(); C = check_c()
    report = {"pass": 51,
              "A_euler_completeness": A,
              "B_phantom_cohomology": B,
              "C_rosser_loeb_unit_correspondence": C,
              "overall": {"A": A["PASS"], "B": B["PASS"], "C": C["PASS"],
                          "PASS": A["PASS"] and B["PASS"] and C["PASS"]}}
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w") as f:
        json.dump(report, f, indent=2)
    print(json.dumps(report["overall"]))
    print("A: e by |Fix| =", A["e_values_by_fixcount"],
          "| antichain viol =", A["violations_Fix_is_antichain"],
          "| e0-nonempty viol =", A["violations_e0_with_nonempty_Fix"],
          "| crown chi =", A["crown_order_complex_chi"])
    print("B:", B["fans"])
    print("C: R_2 integral =", C["rosser_R2_detached"]["integral_unit_top_tensors"],
          "non-integral =", C["rosser_R2_detached"]["nonintegral_units_available"],
          "| C_3 integral =", C["loeb_C3_attached"]["integral_unit_top_tensors"])

if __name__ == "__main__":
    main()
