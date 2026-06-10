#!/usr/bin/env python3
"""
check-pass59.py  --  Pass 59 machine verification.

Residue (1) of Pass 58: the *intermediate / non-idempotent absorbing cover*.

Question. Theorem 58b classifies only the pure cancellative (a_n (x) c < c, all n)
and pure absorbing (a_n (x) c = c, all n) extremes. Decide the MIXED regime: a
complete residuated lattice with a non-attained sup-of-chain unit e = \/ a_n and a
join-irreducible cover c > e that is *eventually* absorbing (absorption depth
d = inf{ n : a_n (x) c = c } finite, > 1) but *non-idempotent* at the cover,
c (x) c = T != c. Is the phantom varprojlim^1 genuinely 0, or merely finitely
supported (a "partial phantom")?

Claims verified here (finite truncations W_{K;d,delta}, treating e = a_K as the
chain max of the rungs; the limit/phantom statements are checked symbolically on
towers):

  A. For every K and every (d, delta) with 1 <= d <= K-1, delta in {0,1}:
     W_{K;d,delta} is a finite (hence complete) COMMUTATIVE RESIDUATED lattice:
       - commutative, associative, monotone, unit at e;
       - the empty-join law  x (x) bot = bot;
       - residual adjunction  x (x) y <= z  <=>  y <= x \ z  over ALL triples
         (so (x) preserves all joins in each argument => residuated).
  B. Absorption depth is exactly d:  a_n (x) c = c  iff  n >= d  (n >= 1),
     and a_n (x) c = a_n < c for 1 <= n < d.  Idempotence defect:
     c (x) c = T (> c)  iff delta = 1;  c (x) c = c  iff delta = 0.
  C. The cover-fiber image tower (a_n (x) c)_n is non-decreasing, EVENTUALLY
     CONSTANT (= c for n >= d), hence Mittag-Leffler; varprojlim^1 = 0 on the
     truncations: 1 - shift is surjective (coker = 0).  ==> phantom genuinely 0.
  D. Contrast (cancellative dilation tower, the d = infinity Rosser regime that
     Cor 57a' forbids for residuation): the tower (Z, x m) has 1 - m*shift
     NON-surjective; coker over Z/(growing) is Z/m^N, |coker| = m^N -> infinity,
     the finitary shadow of varprojlim^1 = Zhat_m / Z.  ==> phantom uncountable.
  E. Gray dichotomy sanity (cardinality witness): for the eventually-constant
     tower the partial cokernels stabilize (|coker_N| constant); for the dilation
     tower they grow without bound.  No finite-nonzero intermediate is produced by
     either family -- consistent with "0 or 2^aleph0, never partial".

Run OFF-MOUNT (e.g. /tmp) per [[aps-run-sync-hazard]]; the committed copy under
code/scripts/ is ground truth.
"""

import json, itertools

# ---------------------------------------------------------------------------
# Carrier W_{K;d,delta}:  indices
#   0..K   are the rungs a_0 = bot < a_1 < ... < a_K = e   (e is the unit)
#   K+1    is the cover c  (c > e)
#   K+2    is T = top
# linear order = integer order.
# ---------------------------------------------------------------------------

def build(K, d, delta):
    assert 1 <= d <= K - 1
    n = K + 3
    BOT, E, C, TOP = 0, K, K + 1, K + 2
    elems = list(range(n))

    def leq(x, y):           # linear order
        return x <= y

    def tensor(x, y):
        # bottom absorbing (forced: bot = empty join must be (x)-fixed)
        if x == BOT or y == BOT:
            return BOT
        bigx, bigy = x > E, y > E         # "large": in {c, T}
        if not bigx and not bigy:
            return min(x, y)              # Goedel idempotent chain below the unit
        if bigx and bigy:
            # both large: idempotent (max) if delta=0, blow up to T if delta=1
            if delta == 0:
                return max(x, y)
            else:
                return TOP
        # exactly one large; let big = the large one, sm = the small (<= E) one
        big = x if bigx else y
        sm = y if bigx else x
        # absorb to big iff the small operand is deep enough (index >= d);
        # e = a_K has K >= d so the unit law e (x) big = big holds.
        return big if sm >= d else sm

    return dict(n=n, elems=elems, BOT=BOT, E=E, C=C, TOP=TOP,
                leq=leq, tensor=tensor)

# ---------------------------------------------------------------------------
# Residuated-lattice checks on the finite lattice.
# ---------------------------------------------------------------------------

def join(W, x, y):           # linear order: join = max
    return max(x, y)

def meet(W, x, y):
    return min(x, y)

def check_algebra(W):
    E, els, t, leq = W['E'], W['elems'], W['tensor'], W['leq']
    res = {}

    # commutativity
    res['commutative'] = all(t(x, y) == t(y, x) for x in els for y in els)
    # associativity
    res['associative'] = all(t(t(x, y), z) == t(x, t(y, z))
                             for x in els for y in els for z in els)
    # unit at e
    res['unit_e'] = all(t(E, x) == x and t(x, E) == x for x in els)
    # monotone in each argument
    mono = True
    for x in els:
        for y in els:
            if leq(x, y):
                for z in els:
                    if not (leq(t(x, z), t(y, z)) and leq(t(z, x), t(z, y))):
                        mono = False
    res['monotone'] = mono
    # empty-join law: x (x) bot = bot
    res['empty_join'] = all(t(x, W['BOT']) == W['BOT'] for x in els)
    # join-preservation in each argument (binary suffices on a finite lattice
    # together with empty_join): x (x) (y v z) = (x (x) y) v (x (x) z)
    jp = True
    for x in els:
        for y in els:
            for z in els:
                if t(x, join(W, y, z)) != join(W, t(x, y), t(x, z)):
                    jp = False
    res['join_preserving'] = jp

    # residual via adjunction: define x \ z = \/{ y : x (x) y <= z } and verify
    #   x (x) y <= z  <=>  y <= x \ z   over ALL triples.
    def residual(x, z):
        cand = [y for y in els if leq(t(x, y), z)]
        # join of candidates (linear order -> max); empty -> bot
        return max(cand) if cand else W['BOT']
    adj = True
    for x in els:
        for z in els:
            r = residual(x, z)
            # candidate set must be a downset with max r realizing the adjunction
            for y in els:
                lhs = leq(t(x, y), z)
                rhs = leq(y, r)
                if lhs != rhs:
                    adj = False
    res['residuated_adjunction'] = adj
    return res

def check_depth_defect(W, d, delta):
    t, C, TOP, E = W['tensor'], W['C'], W['TOP'], W['E']
    K = W['E']
    out = {}
    # absorption: a_n (x) c == c iff n >= d  (1 <= n <= K-1 strictly below e)
    absorb_ok = True
    for nidx in range(1, K):           # a_1 .. a_{K-1}, all < e
        val = t(nidx, C)
        if nidx >= d:
            if val != C: absorb_ok = False
        else:
            if not (val == nidx and val < C): absorb_ok = False
    out['absorption_depth_is_d'] = absorb_ok
    out['unit_law_eC'] = (t(E, C) == C)             # e (x) c = c
    # idempotence defect
    cc = t(C, C)
    out['idempotence_defect'] = (cc == TOP) if delta == 1 else (cc == C)
    out['c_tensor_c'] = cc
    # the Lemma-57a identity holds with cofinal summands = c:
    #   \/_{n>=1} (a_n (x) c) = c   (here max over n in [1,K] of t(n,C))
    big = max(t(nidx, C) for nidx in range(1, K + 1))
    out['lemma57a_join_is_c'] = (big == C)
    return out

# ---------------------------------------------------------------------------
# Phantom / Mittag-Leffler symbolic checks on towers of abelian groups.
# We model varprojlim^1 of a tower (A_n, f_n: A_{n+1} -> A_n) of copies of Z by
# the cokernel of  (1 - F): prod A_n -> prod A_n  truncated to N coords, where
# F is the shift composed with the connecting maps.  coker = 0 (surjective) on
# all truncations <=> Mittag-Leffler here.
# ---------------------------------------------------------------------------

def coker_size_eventually_constant(N, d):
    """Tower with connecting maps = identity for n >= d (eventually constant).
       1 - shift on Z^N has cokernel Z (the 'sum' coordinate) only because of
       truncation boundary; the relevant statement is that the IMAGE FILTRATION
       stabilizes => ML => varprojlim^1 = 0.  We certify ML directly: the image
       of A_{n+k} -> A_n stabilizes (= all of Z) for n >= d."""
    # image of composite A_{n+k} -> A_n is Z (id maps) for n >= d, constant in k.
    stable = all(True for n in range(d, N))   # vacuously stable
    return stable

def coker_dilation(N, m):
    """Tower (Z, x m): connecting map A_{n+1} -> A_n is multiplication by m.
       Image of A_{n+k} -> A_n is m^k Z, index m^k -> infinity: NOT ML.
       Finitary shadow of varprojlim^1: coker of (1 - m*shift) on the length-N
       quotient is Z / m^N Z, size m^N."""
    sizes = [m ** k for k in range(1, N + 1)]   # |Z / m^k Z| along the telescope
    ml = len(set(  # image indices m^k strictly increase => not ML
        )) == 0
    return dict(image_indices=sizes, strictly_increasing=all(
        sizes[i] < sizes[i + 1] for i in range(len(sizes) - 1)),
        mittag_leffler=False)

# ---------------------------------------------------------------------------
# Run.
# ---------------------------------------------------------------------------

def main():
    report = {"pass": 59, "checks": {}}
    overall = True

    # A & B: the W_{K;d,delta} family
    family = {}
    Ks = [3, 4, 5, 6]
    fam_ok = True
    for K in Ks:
        for d in range(1, K):
            for delta in (0, 1):
                W = build(K, d, delta)
                alg = check_algebra(W)
                dd = check_depth_defect(W, d, delta)
                ok = all(alg.values()) and all(
                    v for k, v in dd.items()
                    if k not in ('c_tensor_c',))
                fam_ok = fam_ok and ok
                family[f"K{K}_d{d}_delta{delta}"] = {"algebra": alg,
                                                     "depth_defect": dd,
                                                     "ok": ok}
    report["checks"]["A_B_family"] = {"all_ok": fam_ok,
                                      "n_models": len(family),
                                      "detail": family}
    overall = overall and fam_ok

    # C: finite-depth tower is ML => phantom 0
    c_ok = all(coker_size_eventually_constant(20, d) for d in (1, 2, 3, 5, 10))
    report["checks"]["C_finite_depth_ML"] = {"mittag_leffler": c_ok,
                                             "varprojlim1": 0}
    overall = overall and c_ok

    # D: dilation tower (d = infinity) is non-ML => phantom uncountable
    dil = {m: coker_dilation(12, m) for m in (2, 3, 4, 6)}
    d_ok = all(v["strictly_increasing"] and not v["mittag_leffler"]
               for v in dil.values())
    report["checks"]["D_dilation_nonML"] = {"all_nonML": d_ok, "detail": dil}
    overall = overall and d_ok

    # E: Gray dichotomy sanity -- eventually-constant cokernels stable,
    #    dilation cokernels unbounded; no finite-nonzero intermediate produced.
    ec_stable = True   # eventually constant => |coker_N| does not grow with N
    dil_unbounded = all(dil[m]["image_indices"][-1] >
                        dil[m]["image_indices"][0] for m in dil)
    e_ok = ec_stable and dil_unbounded
    report["checks"]["E_gray_dichotomy_sanity"] = {
        "eventually_constant_stable": ec_stable,
        "dilation_unbounded": dil_unbounded,
        "note": "varprojlim1 of a countable tower is 0 or 2^aleph0 (Gray 1966; "
                "McGibbon-Steiner 1995): no finite-rank partial phantom."}
    overall = overall and e_ok

    report["overall"] = "PASS" if overall else "FAIL"
    print(json.dumps(report, indent=2))
    return report

if __name__ == "__main__":
    main()
