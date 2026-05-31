#!/usr/bin/env python3
"""
Pass 35 verification: non-commutative (two-residual) front-group order in B_N.

Pass 34 proved that the *commutative* front of a bottom-disciplined B_N is rigid:
the only finite group that fits on the incomparable front F_k = {a_1,...,a_k}
while preserving a monotone, associative, fully (single-)residuated tensor is the
trivial group (|G| = 1). The proof leaned on commutativity (single residual) via
the integrality lemma a_i (x) a_j <= a_i ^ a_j.

This script tests the genuinely non-commutative loophole: drop commutativity,
keep TWO residuals
    left:   a \ c = max { x : a (x) x <= c }
    right:  c / a = max { x : x (x) a <= c }
and ask whether a NONTRIVIAL finite group -- including a non-abelian one (S_3) --
can sit on the front of the minimal faithful ambient {b, T, a_1,...,a_k, U}.

Both U-actions are searched independently (left U-action U(x)a_i and right
a_i(x)U) so the test never silently assumes a two-sided absorber. A model passes
iff it is associative, two-sided monotone, and BOTH residual fibers are principal
(unique maximum) for every (a,c).

Validation harness: the orthogonal idempotent zero-band must reproduce the
established single-residual data (k=1,2 residuated, k=3 fails) even when checked
with the two-residual predicate, since that band is commutative.
"""
import itertools


def make_order(n):
    b, U = 0, n - 1
    return [[x == y or x == b or y == U for y in range(n)] for x in range(n)]


def assoc(n, mul):
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if mul[mul[x][y]][z] != mul[x][mul[y][z]]:
                    return False
    return True


def two_sided_monotone(n, leq, mul):
    for x in range(n):
        for y in range(n):
            if leq[x][y]:
                for z in range(n):
                    if not leq[mul[x][z]][mul[y][z]]:   # right mult
                        return False
                    if not leq[mul[z][x]][mul[z][y]]:   # left mult
                        return False
    return True


def principal_max(n, leq, fib):
    mx = [x for x in fib if all(leq[y][x] for y in fib)]
    return len(mx) == 1


def two_residuated(n, leq, mul):
    if not assoc(n, mul):
        return False
    if not two_sided_monotone(n, leq, mul):
        return False
    for a in range(n):
        for c in range(n):
            left = [x for x in range(n) if leq[mul[a][x]][c]]   # a (x) x <= c
            right = [x for x in range(n) if leq[mul[x][a]][c]]  # x (x) a <= c
            if not principal_max(n, leq, left):
                return False
            if not principal_max(n, leq, right):
                return False
    return True


def build_mul(n, k, A, cayley, ul, ur):
    """cayley[i][j] = group index of a_i (x) a_j;
    ul[i] = value of U (x) a_i ; ur[i] = value of a_i (x) U."""
    b, T, U = 0, 1, n - 1
    gidx = {A[i]: i for i in range(k)}
    mul = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == b or y == b:
                v = b
            elif x == T:
                v = y
            elif y == T:
                v = x
            elif x == U and y == U:
                v = U
            elif x == U and y in A:
                v = ul[gidx[y]]
            elif x in A and y == U:
                v = ur[gidx[x]]
            elif x in A and y in A:
                v = A[cayley[gidx[x]][gidx[y]]]
            else:
                v = U
            mul[x][y] = v
    return mul


def search_group(k, cayley):
    """Exhaustive two-residual search over BOTH independent U-actions."""
    n = k + 3
    A = list(range(2, 2 + k))
    leq = make_order(n)
    sols = []
    for ul in itertools.product(range(n), repeat=k):
        for ur in itertools.product(range(n), repeat=k):
            mul = build_mul(n, k, A, cayley, ul, ur)
            if two_residuated(n, leq, mul):
                sols.append((ul, ur))
    return n, sols


def forced_uaction_test(k, cayley):
    """Cheap test for large/non-abelian groups.

    Lemma (two-sided, Pass 35): for a group front, left-translation L_{a_i} and
    right-translation R_{a_i} each permute F_k, so {a_i (x) a_j : i} = F_k whose
    only upper bound is U. Two-sided monotonicity then forces U (x) a_j = U and
    a_j (x) U = U. Hence the all-U absorber is the UNIQUE monotone U-action.
    We (1) confirm the all-U tensor is not two-residuated, and (2) confirm the
    'hopeful' non-absorbing identity-action tensor is not even monotone.
    """
    n = k + 3
    A = list(range(2, 2 + k))
    leq = make_order(n)
    forced = tuple([n - 1] * k)            # U (x) a_i = a_i (x) U = U
    hopeful = tuple(A)                      # U (x) a_i = a_i (x) U = a_i
    mul_forced = build_mul(n, k, A, cayley, forced, forced)
    mul_hope = build_mul(n, k, A, cayley, hopeful, hopeful)
    return {
        "n": n,
        "forced_two_residuated": two_residuated(n, leq, mul_forced),
        "hopeful_monotone": two_sided_monotone(n, leq, mul_hope),
    }


def search_orthogonal(k):
    """Validation: a_i^2 = a_i, a_i a_j = b (i!=j); two-residual predicate."""
    n = k + 3
    A = list(range(2, 2 + k))
    leq = make_order(n)
    b, T, U = 0, 1, n - 1
    gidx = {A[i]: i for i in range(k)}
    sols = []
    for ul in itertools.product(range(n), repeat=k):
        for ur in itertools.product(range(n), repeat=k):
            mul = [[0] * n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if x == b or y == b:
                        v = b
                    elif x == T:
                        v = y
                    elif y == T:
                        v = x
                    elif x == U and y == U:
                        v = U
                    elif x == U and y in A:
                        v = ul[gidx[y]]
                    elif x in A and y == U:
                        v = ur[gidx[x]]
                    elif x in A and y in A:
                        v = (x if x == y else b)
                    else:
                        v = U
                    mul[x][y] = v
            if two_residuated(n, leq, mul):
                sols.append((ul, ur))
    return n, sols


def cyclic(m):
    return [[(i + j) % m for j in range(m)] for i in range(m)]


def klein():
    return [[i ^ j for j in range(4)] for i in range(4)]


def symmetric3():
    # S_3 as permutations of {0,1,2}; element list of 3-tuples, compose g.h = g o h
    perms = list(itertools.permutations(range(3)))
    idx = {p: i for i, p in enumerate(perms)}
    cay = [[0] * 6 for _ in range(6)]
    for i, g in enumerate(perms):
        for j, h in enumerate(perms):
            comp = tuple(g[h[t]] for t in range(3))
            cay[i][j] = idx[comp]
    return cay


GROUPS = [
    (2, "Z/2", cyclic(2)),
    (3, "Z/3", cyclic(3)),
    (4, "Z/4", cyclic(4)),
    (4, "V4", klein()),
    (6, "S_3 (non-abelian)", symmetric3()),
]


def decode(n, t):
    U = n - 1
    out = []
    for v in t:
        out.append("U" if v == U else "b" if v == 0 else "T" if v == 1 else f"a{v - 1}")
    return tuple(out)


if __name__ == "__main__":
    print("== validation: orthogonal zero-band under TWO-residual predicate ==")
    for k in (1, 2, 3):
        n, s = search_orthogonal(k)
        tag = (f", (U*a, a*U)={decode(n, s[0][0])}/{decode(n, s[0][1])}"
               if s else " (expected 0 at k=3)")
        print(f"  orthogonal k={k}: {len(s)} solution(s){tag}")

    print("== group fronts: EXHAUSTIVE two-residual search (k<=3) ==")
    for k, name, cay in GROUPS:
        if k > 3:
            continue
        n, s = search_group(k, cay)
        if s:
            print(f"  k={k} {name}: {len(s)} solution(s)"
                  f", e.g. (U*a, a*U)={decode(n, s[0][0])}/{decode(n, s[0][1])}")
        else:
            print(f"  k={k} {name}: NO two-residuated tensor")

    print("== group fronts: FORCED-U-action test (k>=4, incl. non-abelian) ==")
    for k, name, cay in GROUPS:
        if k <= 3:
            continue
        r = forced_uaction_test(k, cay)
        print(f"  k={k} {name}: all-U tensor two-residuated? "
              f"{r['forced_two_residuated']}; non-absorbing action monotone? "
              f"{r['hopeful_monotone']}")
