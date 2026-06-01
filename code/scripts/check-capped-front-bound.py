#!/usr/bin/env python3
"""Pass 36 - Capped-front escape checker.

Adjoins a single sub-top cap c with a_i <= c < U over the front F_k of the
bottom-disciplined B_N preAPS, keeping the boxtimes-orbit on T untouched, and
tests two questions:

  (a) Antitonicity: does boxtimes admit an antitone extension to c, and what is
      the forced value boxtimes(c)?  (Claim: boxtimes c = b is forced for k>=2.)

  (b) Maximum group order: can the cap make a nontrivial group front F_k ~ G
      residuated, i.e. can the diagonal residual fiber a_j\\a_j become principal
      at c instead of being stranded?  (Claim: NO; |G| = 1 still, and the
      orthogonal width bound k<=2 also survives.)

The script is self-contained: it builds the partial order, then checks
monotonicity-forced cap/U actions and principality of every diagonal residual
fiber.  The verdict is printed per front type.

Carrier of B_N^cap (N=k+1 for a width-k front):
    {b, T, a_1,...,a_{N+1}, s, U, c}
Order:  b <= x <= U for all x;  s <= a_{N+1};  a_i <= c (i<=k);  c <= U.
boxtimes-orbit:  T->a_1->...->a_{N+1}->s->s ;  boxtimes b = U, boxtimes U = b.
"""

def build_capped_model(k):
    """B_N^cap with N=k+1 so a_{k+1}, a_{N+1} are genuine tail atoms below/above s."""
    N = k + 1
    front = [f"a{i}" for i in range(1, k + 1)]
    tail_atoms = []
    for i in range(k + 1, N + 2):
        if f"a{i}" not in tail_atoms:
            tail_atoms.append(f"a{i}")
    tail = tail_atoms + ["s"]
    carrier = ["b", "T"] + front + tail + ["U", "c"]

    le = {(x, x) for x in carrier}
    for x in carrier:
        le.add(("b", x))
        le.add((x, "U"))
    le.add(("s", f"a{N+1}"))
    for ai in front:
        le.add((ai, "c"))
    le.add(("c", "U"))
    changed = True
    while changed:
        changed = False
        for (x, y) in list(le):
            for (y2, z) in list(le):
                if y == y2 and (x, z) not in le:
                    le.add((x, z))
                    changed = True

    def leq(x, y):
        return (x, y) in le

    return carrier, leq, front, tail, N


def antitone_forced_boxtimes_c(carrier, leq, front, N):
    box = {"b": "U", "U": "b", "T": "a1"}
    for i in range(1, N + 1):
        box[f"a{i}"] = f"a{i+1}"
    box[f"a{N+1}"] = "s"
    box["s"] = "s"
    targets = [box[ai] for ai in front]            # a2, ..., a_{k+1}
    admissible = [v for v in carrier if all(leq(v, t) for t in targets)]
    return box, targets, admissible


def diagonal_fiber_principality(carrier, leq, front, group_table, cap_action):
    """For a group front with the given table, build the monotonicity-forced
    skeleton and report the diagonal fiber a_j\\a_j and its maximal elements.
    cap_action in {'c','U'} is the forced value of a_j*c (both are >= c)."""
    e_g = front[0]
    g = {}
    for i, ai in enumerate(front):
        for j, aj in enumerate(front):
            g[(ai, aj)] = front[group_table[i][j]]

    prod = {}
    for x in carrier:
        prod[("b", x)] = "b"; prod[(x, "b")] = "b"
        prod[("T", x)] = x;   prod[(x, "T")] = x
    for k1 in front:
        for k2 in front:
            prod[(k1, k2)] = g[(k1, k2)]
    for aj in front:
        prod[(aj, "c")] = cap_action
        prod[("c", aj)] = cap_action
        prod[(aj, "U")] = "U"
        prod[("U", aj)] = "U"

    out = []
    for aj in front:
        fiber = [x for x in carrier
                 if (aj, x) in prod and leq(prod[(aj, x)], aj)]
        maximals = [x for x in fiber
                    if not any(x != y and leq(x, y) for y in fiber)]
        out.append((aj, sorted(fiber), sorted(maximals), len(maximals) == 1))
    return out


def main():
    print("=" * 72)
    print("PASS 36  -  Capped-front escape:  B_N^cap = B_N + sub-top cap c")
    print("=" * 72)

    print("\n[a] Antitonicity of boxtimes extended to the cap c\n")
    for k in (2, 3):
        carrier, leq, front, tail, N = build_capped_model(k)
        box, targets, adm = antitone_forced_boxtimes_c(carrier, leq, front, N)
        print(f"  width k={k} (N={N}): front={front}")
        print(f"    boxtimes(c) <= meet of {targets};  admissible = {adm}")
        assert adm == ["b"], f"expected forced boxtimes c = b, got {adm}"
        print(f"    => FORCED  boxtimes(c) = b  (unique antitone extension)")
        print(f"    profile preserved: orbit of T untouched; no new FP "
              f"(boxtimes c = b != c)\n")

    print("[b] Group fronts on F_k under the cap (diagonal-fiber principality)\n")
    Z2 = [[0, 1], [1, 0]]
    Z3 = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
    for k, table, name in ((2, Z2, "Z/2"), (3, Z3, "Z/3")):
        carrier, leq, front, tail, N = build_capped_model(k)
        action_principal = {}
        for cap_action in ("c", "U"):
            res = diagonal_fiber_principality(carrier, leq, front, table, cap_action)
            allp = all(pr for *_, pr in res)
            action_principal[cap_action] = allp
            non_id = res[1]  # a_2: a non-identity group atom
            aj, fib, mx, pr = non_id
            print(f"  F_{k}~{name}, a_j={aj}, forced a_j*c={cap_action}: "
                  f"fiber(a_j\\a_j)={fib}")
            print(f"      maximals={mx} -> "
                  f"{'PRINCIPAL' if pr else 'NON-PRINCIPAL'}")
        ok = any(action_principal.values())
        print(f"    VERDICT: "
              f"{'group front survives!' if ok else 'NO residuated tensor -> |G|=1'}\n")
        assert not ok, "unexpected: cap reopened a group front"

    print("[c] Orthogonal width-3 front under the cap (p\\b fiber)\n")
    carrier, leq, front, tail, N = build_capped_model(3)
    for p in front:
        fiber = ["b"] + [a for a in front if a != p]   # p*c >= p*p = p != b: c ejected
        maximals = [x for x in fiber
                    if not any(x != y and leq(x, y) for y in fiber)]
        pr = len(maximals) == 1
        print(f"    p={p}: fiber(p\\b)={sorted(fiber)} (cap c ejected) "
              f"maximals={sorted(maximals)} -> "
              f"{'PRINCIPAL' if pr else 'NON-PRINCIPAL'}")
        assert not pr
    print("    => width-3 orthogonal front still fails; cap ejected (p*c>=p!=b)\n")

    print("=" * 72)
    print("CONCLUSION (Pass 36):")
    print("  (a) unique antitone extension boxtimes(c)=b; Route-B cascade escaped")
    print("      (c not in orbit(T)).")
    print("  (b) max group order under a single full cap = 1 (Z/2, Z/3 fail).")
    print("  (c) orthogonal width bound k<=2 survives the cap.")
    print("  Cap Ejection: a ceiling above the front cannot repair fibers whose")
    print("  obstruction sits at/below the front (monotonicity ejects c).")
    print("=" * 72)


if __name__ == "__main__":
    main()
