#!/usr/bin/env python3
r"""
Pass 37 verification: the SELECTIVE-MEDIAN escape from front-group rigidity.

Background (Passes 34-36). In a bottom-disciplined B_N preAPS the incomparable
front F_k = {a_1,...,a_k} cannot carry a nontrivial finite group under any
same-carrier/same-order commutative monotone fully-residuated tensor: the
diagonal residual fiber  a_j \ a_j  strands the incomparable pair {T, e_G}
(global monoid unit T vs. group-identity atom e_G), whose only common upper
bound U is forced OUT of the fiber by U-absorption, so the fiber is
non-principal (|G| = 1). Pass 36 showed a CEILING c over the WHOLE front does
not help: c is "ejected" (a_j (x) c >= a_j (x) a_j ... leaves the fiber).

The Cap-Ejection lemma leaves exactly one repair standing: adjoin a SELECTIVE
MEDIAN m that dominates ONLY the obstructing pair {T, e_G} (T <= m, e_G <= m),
while m stays incomparable to every non-identity front atom and to the whole
tail. Then m is a candidate maximum of each diagonal fiber strictly BELOW U,
so the U-absorption that killed the cap need not kill m -- PROVIDED the front
no longer absorbs the tail downward (else tail elements re-enter the diagonal
fiber and m fails to dominate them).

This script (1) builds an EXPLICIT candidate tensor B_N^med and verifies, in
O(n^3), that it is commutative / associative / monotone / unital (T) / fully
residuated for the cyclic group fronts Z/k, k = 2,3,4,5; and (2) re-runs the
same explicit-candidate construction WITHOUT a median and WITH a full cap to
exhibit the precise non-principal fiber that rigidity predicts.

Carrier:  b, T, a_1,...,a_{N+1}, s, U  (+ m or c)
Order:    b bottom, U top, s <= a_{N+1}; median:  b,T,a_1 <= m <= U ;
          cap:  b,a_1,...,a_k <= c <= U.   a_1 is the group identity e_G.

The candidate tensor (median present):
    b zero, T unit, group product on the front F_k,
    U (x) x = U for x not in {b},           (forced absorption)
    m (x) m = m,  m (x) a_j = a_j (front),  m (x) r = U (tail), m (x) U = U,
    a_j (x) r = U (front does NOT absorb tail),  and  everything else
    involving a tail element or U (and not b,T) collapses to U.
"""


def build(N, k, median=False, cap=False):
    assert not (median and cap)
    names = (["b", "T"] + [f"a{i}" for i in range(1, N + 2)] + ["s", "U"]
             + (["m"] if median else (["c"] if cap else [])))
    b, T = 0, 1
    a = {i: 1 + i for i in range(1, N + 2)}     # a_i at index i+1
    s = a[N + 1] + 1
    U = s + 1
    extra = (U + 1) if (median or cap) else None
    n = len(names)
    e_idx = a[1]
    front = [a[i] for i in range(1, k + 1)]
    tail = [a[i] for i in range(k + 1, N + 2)] + [s]

    leq = [[i == j for j in range(n)] for i in range(n)]
    for x in range(n):
        leq[b][x] = True
        leq[x][U] = True
    leq[s][a[N + 1]] = True
    if median:
        leq[b][extra] = leq[T][extra] = leq[e_idx][extra] = True
        leq[extra][U] = True
    if cap:
        leq[b][extra] = True
        for j in front:
            leq[j][extra] = True
        leq[extra][U] = True
    for mm in range(n):                          # transitive closure
        for x in range(n):
            if leq[x][mm]:
                for y in range(n):
                    if leq[mm][y]:
                        leq[x][y] = True
    return names, leq, front, e_idx, tail, U, T, b, extra


def candidate(N, k, median=False, cap=False):
    """Explicit candidate tensor. Returns (names, leq, mul, info)."""
    names, leq, front, e_idx, tail, U, T, b, extra = build(N, k, median, cap)
    n = len(names)
    fset, tset = set(front), set(tail)
    gidx = {front[i]: i for i in range(k)}

    def f(x, y):
        if x == b or y == b:
            return b
        if x == T:
            return y
        if y == T:
            return x
        if x in fset and y in fset:
            return front[(gidx[x] + gidx[y]) % k]
        if median and (x == extra or y == extra):
            o = y if x == extra else x
            if o == extra:
                return extra              # m (x) m = m
            if o in fset:
                return o                  # m (x) a_j = a_j
            return U                      # m (x) tail = m (x) U = U
        if cap and (x == extra or y == extra):
            o = y if x == extra else x
            if o == extra:
                return extra              # c (x) c = c
            # cap sits above the front: c (x) a_j >= a_j (x) a_j, and the cap
            # is forced upward; collapse to U (the only consistent value once
            # the front is a group). This is what "ejects" c.
            return U
        # remaining: at least one of x,y in tail or = U, none b/T, not both
        # front, not the extra element  ->  collapse to U.
        return U

    mul = [[f(x, y) for y in range(n)] for x in range(n)]
    info = dict(names=names, front=front, e_idx=e_idx, tail=tail,
                U=U, T=T, b=b, extra=extra)
    return names, leq, mul, info


def verify(names, leq, mul):
    n = len(names)
    nm = lambda i: names[i]
    # commutativity
    for x in range(n):
        for y in range(n):
            if mul[x][y] != mul[y][x]:
                return False, f"noncommutative: {nm(x)}(x){nm(y)}"
    # associativity
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if mul[mul[x][y]][z] != mul[x][mul[y][z]]:
                    return False, (f"nonassoc: ({nm(x)}{nm(y)}){nm(z)}="
                                   f"{nm(mul[mul[x][y]][z])} vs "
                                   f"{nm(x)}({nm(y)}{nm(z)})="
                                   f"{nm(mul[x][mul[y][z]])}")
    # unit (find T = 1)
    for x in range(n):
        if mul[1][x] != x:
            return False, f"T not unit: T(x){nm(x)}={nm(mul[1][x])}"
    # monotonicity
    for x in range(n):
        for y in range(n):
            if leq[x][y]:
                for z in range(n):
                    if not leq[mul[x][z]][mul[y][z]]:
                        return False, (f"non-monotone: {nm(x)}<={nm(y)} but "
                                       f"{nm(x)}{nm(z)}={nm(mul[x][z])} !<= "
                                       f"{nm(y)}{nm(z)}={nm(mul[y][z])}")
    # full residuation: every fiber principal
    for aa in range(n):
        for cc in range(n):
            fib = [x for x in range(n) if leq[mul[aa][x]][cc]]
            mx = [x for x in fib if all(leq[y][x] for y in fib)]
            if len(mx) != 1:
                return False, (f"NON-PRINCIPAL fiber {nm(aa)}\\{nm(cc)} = "
                               f"{{{', '.join(nm(x) for x in fib)}}}, "
                               f"maximal = {{{', '.join(nm(x) for x in mx)}}}")
    return True, "all axioms hold"


def diag(names, leq, mul, j):
    n = len(names)
    fib = [x for x in range(n) if leq[mul[j][x]][j]]
    mx = [x for x in fib if all(leq[y][x] for y in fib)]
    return ([names[x] for x in fib], [names[x] for x in mx])


def run(label, N, k, median=False, cap=False):
    names, leq, mul, info = candidate(N, k, median, cap)
    ok, msg = verify(names, leq, mul)
    extra = info["extra"]
    tag = f"[{label}] N={N}, Z/{k} front"
    if extra is not None:
        tag += f", +{names[extra]}"
    verdict = "FULLY RESIDUATED" if ok else "FAILS"
    print(f"{tag}: {verdict}")
    print(f"        -> {msg}")
    gen = info["front"][1]
    fib, mx = diag(names, leq, mul, gen)
    print(f"        diagonal fiber {names[gen]}\\{names[gen]} = "
          f"{{{', '.join(fib)}}}   max = {{{', '.join(mx)}}}")
    if extra is not None and not cap:
        ex = names[extra]
        print("        front-on-m : "
              + ", ".join(f"{names[j]}(x){ex}={names[mul[j][extra]]}"
                          for j in info["front"]))
    if info["tail"]:
        t0 = info["tail"][0]
        print(f"        front-on-tail({names[t0]}): "
              + ", ".join(f"{names[j]}(x){names[t0]}={names[mul[j][t0]]}"
                          for j in info["front"]))
    print()
    return ok



if __name__ == "__main__":
    print("=" * 72)
    print("CONTROLS  (explicit candidate; rigidity must surface a bad fiber)")
    print("=" * 72)
    run("control:no-extra", 2, 2)
    run("control:full-cap", 2, 2, cap=True)
    print("=" * 72)
    print("SELECTIVE MEDIAN  m  over {T, e_G=a_1}")
    print("=" * 72)
    results = {kk: run("median", kk, kk, median=True) for kk in (2, 3, 4, 5)}
    print("=" * 72)
    print("SUMMARY:", {f"Z/{kk}": ("ESCAPES" if v else "rigid")
                       for kk, v in results.items()})
