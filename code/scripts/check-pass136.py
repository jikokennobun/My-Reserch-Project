#!/usr/bin/env python3
"""
Pass 136 verification: the uniform k-sphere coherence obstruction and the
cd-grading cd(A^{(a),k}) = k.

Claim (Thm 136a, cd-grading): the minimal k-coherence obstruction of the
a-primary MP system A^{(a),k} is modeled by the boundary sphere
S^k = boundary(Delta^{k+1}), whose reduced simplicial homology over F_a satisfies

    Htilde_j(S^k; F_a) = F_a   iff  j == k,   else 0.

Hence coherence cohomological dimension cd = k EXACTLY (no collapse to < k), and the
n=1-vs-n>=2 asymmetry (Pass 135 Thm 135a / Correction 135b) is degree-UNIFORM:
  - full simplex Delta^{k+1} is contractible  => H_k = 0  => no simplicial
    retraction Delta^{k+1} -> S^k (the transfer/retract argument that trivialized
    n=1 has no analogue at n>=2, because cd(A) <= 1 kills the target);
  - the "two k-simplices sharing a vertex" wedge is contractible, generalizing
    Correction 135b (the k=2 wedge is NOT the honest obstruction; S^k is).

We verify over F_3 (a = 3, the Pass-33 escape prime) for k = 1,2,3,4.
Pure GF(3) linear algebra; no external dependencies.

Run OFF-MOUNT (e.g. /tmp) per aps-run-sync-hazard; commit script + report via
Windows-path file tools.
"""
import itertools, json
P = 3  # coefficient field F_3


def rank_modp(M, p=P):
    """rank of matrix M (list of rows) over F_p via Gaussian elimination."""
    M = [row[:] for row in M]
    if not M or not M[0]:
        return 0
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)  # Fermat inverse in F_p
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p != 0:
                f = M[i][c] % p
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def simplices(faces):
    """Given maximal faces, return dict dim -> sorted list of simplices,
       including the empty simplex (dim -1) for the augmented complex."""
    allsimp = set()
    for F in faces:
        F = tuple(sorted(F))
        for r in range(0, len(F) + 1):
            for c in itertools.combinations(F, r):
                allsimp.add(c)
    by_dim = {}
    for s in allsimp:
        by_dim.setdefault(len(s) - 1, []).append(s)
    for d in by_dim:
        by_dim[d].sort()
    return by_dim


def boundary_matrix(by_dim, d):
    """boundary_d : C_d -> C_{d-1} over F_P (augmented: d=0 maps to the empty simplex)."""
    if d not in by_dim or (d - 1) not in by_dim:
        return []
    lower = {s: i for i, s in enumerate(by_dim[d - 1])}
    upper = by_dim[d]
    M = [[0] * len(upper) for _ in range(len(by_dim[d - 1]))]
    for jcol, s in enumerate(upper):
        for k in range(len(s)):
            face = s[:k] + s[k + 1:]
            M[lower[face]][jcol] = ((-1) ** k) % P
    return M


def reduced_homology(faces, maxdim):
    """reduced simplicial homology dims over F_P via the augmented chain complex."""
    by_dim = simplices(faces)
    by_dim.setdefault(-1, [()])
    ranks = {}
    for d in range(-1, maxdim + 2):
        ranks[d] = rank_modp(boundary_matrix(by_dim, d)) if (d in by_dim and (d - 1) in by_dim) else 0
    dims = {}
    for d in range(0, maxdim + 1):
        cd = len(by_dim.get(d, []))
        dims[d] = (cd - ranks.get(d, 0)) - ranks.get(d + 1, 0)  # ker d_d - im d_{d+1}
    return dims


def sphere_faces(k):
    """S^k = boundary of Delta^{k+1}: all (k+1)-subsets (dim-k faces) of {0..k+1}."""
    return [tuple(c) for c in itertools.combinations(range(k + 2), k + 1)]


def simplex_faces(k):
    """full Delta^{k+1}: the single maximal (k+1)-simplex on {0..k+1}."""
    return [tuple(range(k + 2))]


def wedge_two_ksimplices(k):
    """two k-simplices sharing exactly the vertex 0 (Correction 135b, general k)."""
    A = tuple(range(0, k + 1))                # 0..k
    B = (0,) + tuple(range(k + 1, 2 * k + 1))  # 0, k+1..2k
    return [A, B]


report = {"field": "F_%d" % P, "cases": {}, "overall": "PENDING"}
ok = True
for k in [1, 2, 3, 4]:
    sph = reduced_homology(sphere_faces(k), k + 1)
    smp = reduced_homology(simplex_faces(k), k + 2)
    wed = reduced_homology(wedge_two_ksimplices(k), k + 1)
    exp_sphere = {j: (1 if j == k else 0) for j in range(0, k + 1)}
    sphere_ok = all(sph.get(j, 0) == exp_sphere[j] for j in exp_sphere)
    simplex_ok = all(v == 0 for v in smp.values())   # contractible
    wedge_ok = all(v == 0 for v in wed.values())      # contractible
    retract_blocked = (smp.get(k, 0) == 0 and sph.get(k, 0) == 1)
    case_ok = sphere_ok and simplex_ok and wedge_ok and retract_blocked
    ok = ok and case_ok
    report["cases"]["k=%d" % k] = {
        "Htilde_sphere": {str(j): sph.get(j, 0) for j in range(0, k + 1)},
        "expected_sphere": {str(j): exp_sphere[j] for j in exp_sphere},
        "sphere_is_S^k": sphere_ok,
        "Delta_{k+1}_contractible": simplex_ok,
        "wedge_two_ksimplices_contractible": wedge_ok,
        "no_retraction_Delta->S^k": retract_blocked,
        "case_pass": case_ok,
    }
report["overall"] = "PASS" if ok else "FAIL"
print(json.dumps(report, indent=2))
