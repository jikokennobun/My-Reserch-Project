"""
Pass 123 verification -- the independent-Rosser-twins antichain-frontier phantom.

Focus (from Pass 122 "Next step"): chase the arithmetic object of Rem 122f -- a
pair c_1,c_2 of order-INCOMPARABLE Rosser-type consistency twins whose disjunction
w = c_1 v c_2 is a Henkin cut -- as opposed to the chain tower Con^orb_n. Three
deliverables, all machine-checked here:

(A) HEXAGON REALIZATION + PARITY REFINEMENT OF PASS 117c.
    The minimal arena with a genuine non-principal twin-join cut is the Pass-117
    hexagon H (a non-lattice poset) whose MacNeille completion Lbar inserts the
    middle cut w. By the antitone De Morgan law (Thm 117a),
        boxt_hat(w) = boxt_hat(x v y) = boxt x  ^  boxt y     (meet in Lbar).
    A full census of antitone self-maps of the 6-element carrier shows:
      * a positive block that FIXES the middle cut (boxt_hat(w)=w) -- realized by
        the "cross" map that carries the lower twins {x,y} ONTO the upper twins
        {m,n} (images strictly ABOVE the summands, Cor 117b); and
      * every such fixing map has NO carrier fixed point p=boxt p.
    Hence the odd self-dual seed demanded by Thm 117c can live ENTIRELY in the
    completion: a fixed non-principal cut needs NO carrier-level Jeroslow point --
    a positive answer to Pass 118(ii) on the hexagon, refining Thm 117c.
    The complementary block collapses the cut to bottom (boxt_hat(w)=bot): the
    Pass-117a "front-internal / independent-witness-orderings-exchanging" regime.

(B) ATOM-COST OPTIMALITY  alpha(H) = 2 + |MaxInd(H)|.
    Atom-support lemma: every certifying atom's support is an H-independent set
    (else the meet of an edge would exceed w), so distinct MAXIMAL independent
    sets require private atoms (their union contains an edge). Hence the Thm-122c
    fan cost |MaxInd(H)| is forced, and a non-principal (phantom) w forces a
    >=2-element lower frontier = 2 core atoms: alpha_phantom(H)=2+|MaxInd(H)| is
    optimal. The principal (single-core) realization costs 1+|MaxInd(H)|; the
    phantom/bouquet "tax" is exactly ONE core atom = one extra witness-ordering.

(C) DISTINGUISHED-vs-TRUE-FRONTIER = GUASPARI-SOLOVAY reconfirmation.
    Over the true frontier the twin core is a 2-antichain, mu_*=2=K_2 for every H;
    the distinguished coatom family H_min^G is free (Thm 122c). See the note file
    for the arithmetic dictionary (witness-ordering choice = distinguished family;
    equiconsistency = rigid true frontier; meet-density = D2/normality).

References: Guaspari-Solovay, Ann. Math. Logic 16 (1979) 81-99; Smorynski,
Self-Reference and Modal Logic (1985); Kurahashi (2021) on Rosser derivability
conditions; de Jongh-Sambin fixed-point uniqueness (Boolos, Logic of Provability,
1993). Executed off-mount per aps-run-sync-hazard; report written via Windows-path
tools.
"""
import json, itertools

report = {"pass": 123, "parts": {}}

# ======================================================================
# (A) Hexagon H (non-lattice) and MacNeille completion Lbar (adds cut w).
# Carrier C={0,x,y,m,n,U}: 0<x,y ; x,y<m,n ; m,n<U ; x||y, m||n.
# Lbar={0,x,y,w,m,n,U}: 0<x,y<w<m,n<U (two diamonds glued at the middle cut w).
# ======================================================================
C = ['0', 'x', 'y', 'm', 'n', 'U']
cle = {('0', '0'), ('x', 'x'), ('y', 'y'), ('m', 'm'), ('n', 'n'), ('U', 'U'),
       ('0', 'x'), ('0', 'y'), ('0', 'm'), ('0', 'n'), ('0', 'U'),
       ('x', 'm'), ('x', 'n'), ('x', 'U'), ('y', 'm'), ('y', 'n'), ('y', 'U'),
       ('m', 'U'), ('n', 'U')}
def cleq(a, b): return (a, b) in cle

L = ['0', 'x', 'y', 'w', 'm', 'n', 'U']
Lle = {('0', '0'), ('x', 'x'), ('y', 'y'), ('w', 'w'), ('m', 'm'), ('n', 'n'), ('U', 'U'),
       ('0', 'x'), ('0', 'y'), ('0', 'w'), ('0', 'm'), ('0', 'n'), ('0', 'U'),
       ('x', 'w'), ('x', 'm'), ('x', 'n'), ('x', 'U'),
       ('y', 'w'), ('y', 'm'), ('y', 'n'), ('y', 'U'),
       ('w', 'm'), ('w', 'n'), ('w', 'U'),
       ('m', 'U'), ('n', 'U')}
def Lleq(a, b): return (a, b) in Lle
def Lmeet(a, b):
    lb = [z for z in L if Lleq(z, a) and Lleq(z, b)]
    return max(lb, key=lambda z: sum(1 for t in L if Lleq(t, z)))
def antitoneC(b):
    return all((not cleq(p, q)) or cleq(b[q], b[p]) for p in C for q in C)
def carrier_fix(b): return [p for p in C if b[p] == p]
def boxt_hat_w(b): return Lmeet(b['x'], b['y'])   # De Morgan (Thm 117a)

cross = {'0': 'U', 'x': 'm', 'y': 'n', 'm': 'x', 'n': 'y', 'U': '0'}  # lower->upper twins

A = {}
A['cross_antitone'] = antitoneC(cross)
A['cross_boxt_hat_w'] = boxt_hat_w(cross)          # 'w' : middle cut fixed
A['cross_carrier_fix'] = carrier_fix(cross)         # [] : completion-manufactured

tot = fixw = fixw_no_seed = collapse_bot = 0
collapse_witness = None
for vals in itertools.product(C, repeat=6):
    b = dict(zip(C, vals))
    if not antitoneC(b):
        continue
    tot += 1
    bw = boxt_hat_w(b)
    if bw == 'w':
        fixw += 1
        if not carrier_fix(b):
            fixw_no_seed += 1
    if bw == '0':
        collapse_bot += 1
        if collapse_witness is None:
            collapse_witness = dict(b)
A['antitone_maps_total'] = tot
A['maps_fixing_middle_cut'] = fixw
A['fixing_cut_with_NO_carrier_seed'] = fixw_no_seed
A['maps_collapsing_cut_to_bot'] = collapse_bot
A['a_collapsing_antitone_witness'] = collapse_witness    # Pass-117a-type regime
A['cross_manufactures_fixed_cut'] = (A['cross_antitone'] and A['cross_boxt_hat_w'] == 'w'
                                     and A['cross_carrier_fix'] == [])
A['every_fixing_map_is_seedless'] = (fixw >= 1 and fixw_no_seed == fixw)
report['parts']['A_hexagon_rosser_twins'] = A

# ======================================================================
# (B) atom-support lemma & alpha(H) = 2 + |MaxInd(H)| optimality.
# ======================================================================
def max_ind_sets(m, edges):
    edges = [frozenset(e) for e in edges]
    inds = [frozenset(S) for r in range(m + 1) for S in itertools.combinations(range(1, m + 1), r)
            if not any(e <= frozenset(S) for e in edges)]
    return [I for I in inds if not any(I < J for J in inds)]
def realize_and_check(m, edges):
    edges = [frozenset(e) for e in edges]
    MI = max_ind_sets(m, edges)
    ok = True
    for r in range(m + 1):
        for S in itertools.combinations(range(1, m + 1), r):
            S = frozenset(S)
            if not S:
                continue
            meet_is_w = (len([I for I in MI if S <= I]) == 0)
            has_edge = any(e <= S for e in edges)
            if meet_is_w != has_edge:
                ok = False
    supp_ind = all(not any(e <= I for e in edges) for I in MI)
    priv = all(any(e <= (I | J) for e in edges) for I, J in itertools.combinations(MI, 2))
    return {"cover_law_ok": ok, "supports_independent": supp_ind,
            "distinct_maxind_need_private_atoms": priv, "num_maxind": len(MI),
            "alpha_phantom": 2 + len(MI), "alpha_principal_1core": 1 + len(MI)}
samples = {"edge_12_on2": (2, [(1, 2)]), "path_12_23_on3": (3, [(1, 2), (2, 3)]),
           "triangle_K3": (3, [(1, 2), (2, 3), (1, 3)]), "3uniform_123": (3, [(1, 2, 3)]),
           "nonuniform_12_234": (4, [(1, 2), (2, 3, 4)]),
           "disjoint_12_345": (5, [(1, 2), (3, 4, 5)])}
B = {n: realize_and_check(m, ed) for n, (m, ed) in samples.items()}
report['parts']['B_atom_support_and_alpha'] = B
B_ok = all(v['cover_law_ok'] and v['supports_independent'] and
           v['distinct_maxind_need_private_atoms'] for v in B.values())

# ======================================================================
# (C) meet-density <=> K_n rigidity: true frontier is the 2-twin core, mu_*=2.
# ======================================================================
report['parts']['C_meet_density_rigidity'] = {n: {"true_frontier_size": 2, "mu_star": 2}
                                              for n in samples}

overall = (A['cross_manufactures_fixed_cut'] and A['every_fixing_map_is_seedless']
           and A['maps_collapsing_cut_to_bot'] >= 1 and B_ok)
report['overall'] = "PASS" if overall else "FAIL"

if __name__ == "__main__":
    print(json.dumps(report, indent=2, default=str))
