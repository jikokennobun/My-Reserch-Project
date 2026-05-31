#!/usr/bin/env python3
"""
Pass 34 verification: maximum front-group order in the B_N schema.

Question: replace the orthogonal idempotent zero-band on the front
F_k = {a_1,...,a_k} of a bottom-disciplined B_N preAPS by a finite group G of
order k (front atoms identified with group elements). Pass 33 claimed the
cyclic group Z/3 succeeds ("Route A"). This script tests, in the minimal
faithful ambient {b, T, a_1,...,a_k, U} that carries every binding
monotonicity / residuation constraint of the front, whether a *commutative,
associative, monotone, fully residuated* tensor with unit T and zero b exists
when the front carries a nontrivial group.

Order: b is bottom, U is top, and {T, a_1, ..., a_k} are pairwise-incomparable
atoms (exactly the B_N order restricted to the front prefix). The U-action on
each front atom U (x) a_i is searched over all carrier elements; everything
else (group product on the front, unit T, zero b, U idempotent) is fixed.

A solution exists iff every fiber {x : a (x) x <= c} has a unique maximum
(principal residual) while monotonicity and associativity hold.

The harness is validated against the ESTABLISHED orthogonal-front results:
orthogonal k=1,2 must be residuated; orthogonal k=3 must fail.
"""
import itertools


def make_order(n):
    b, U = 0, n - 1
    return [[x == y or x == b or y == U for y in range(n)] for x in range(n)]


def build_mul(n, k, A, gprod, uact):
    """gprod(i,j) -> group index; uact[i] = carrier value of U (x) a_i."""
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
                v = uact[gidx[y]]
            elif y == U and x in A:
                v = uact[gidx[x]]
            elif x in A and y in A:
                v = A[gprod(gidx[x], gidx[y])]
            else:
                v = U if (x == U or y == U) else b
            mul[x][y] = v
    return mul


def is_residuated(n, leq, mul):
    if any(mul[x][y] != mul[y][x] for x in range(n) for y in range(n)):
        return False
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if mul[mul[x][y]][z] != mul[x][mul[y][z]]:
                    return False
    for x in range(n):
        for y in range(n):
            if leq[x][y]:
                for z in range(n):
                    if not leq[mul[x][z]][mul[y][z]]:
                        return False
    for a in range(n):
        for c in range(n):
            fib = [x for x in range(n) if leq[mul[a][x]][c]]
            mx = [x for x in fib if all(leq[y][x] for y in fib)]
            if len(mx) != 1:
                return False
    return True


def search_group(k, gprod):
    n = k + 3
    A = list(range(2, 2 + k))
    leq = make_order(n)
    sols = []
    for uact in itertools.product(range(n), repeat=k):
        mul = build_mul(n, k, A, gprod, uact)
        if is_residuated(n, leq, mul):
            sols.append(uact)
    return n, sols


def search_orthogonal(k):
    """Validation harness: a_i^2 = a_i, a_i a_j = b for i != j."""
    n = k + 3
    A = list(range(2, 2 + k))
    leq = make_order(n)
    b, T, U = 0, 1, n - 1
    gidx = {A[i]: i for i in range(k)}
    sols = []
    for uact in itertools.product(range(n), repeat=k):
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
                    v = uact[gidx[y]]
                elif y == U and x in A:
                    v = uact[gidx[x]]
                elif x in A and y in A:
                    v = (x if x == y else b)
                else:
                    v = U if (x == U or y == U) else b
                mul[x][y] = v
        if is_residuated(n, leq, mul):
            sols.append(uact)
    return n, sols


GROUPS = {
    1: [("Z/1", lambda i, j: 0)],
    2: [("Z/2", lambda i, j: (i + j) % 2)],
    3: [("Z/3", lambda i, j: (i + j) % 3)],
    4: [("Z/4", lambda i, j: (i + j) % 4),
        ("V4=Z2xZ2", lambda i, j: i ^ j)],
}


def decode(n, uact):
    U = n - 1
    out = []
    for v in uact:
        out.append("U" if v == U else "b" if v == 0 else "T" if v == 1 else f"a{v - 1}")
    return tuple(out)


if __name__ == "__main__":
    print("== validation: orthogonal idempotent zero-band front ==")
    for k in (1, 2, 3):
        n, s = search_orthogonal(k)
        print(f"  orthogonal k={k}: {len(s)} solution(s)"
              + (f", U*a_i={decode(n, s[0])}" if s else " (expected: 0 for k=3)"))

    print("== group fronts ==")
    for k in (1, 2, 3, 4):
        for name, gp in GROUPS[k]:
            n, s = search_group(k, gp)
            if s:
                print(f"  k={k} {name}: {len(s)} solution(s), U*a_i={decode(n, s[0])}")
            else:
                print(f"  k={k} {name}: NO monotone fully-residuated tensor")
