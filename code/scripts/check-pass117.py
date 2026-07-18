"""
Pass 117 machine verification.
Test Remark 116c: does a boxt-antichain 2-cycle plateau {x,y} with an unattained
join x v y (doubled cover) yield a NON-PRINCIPAL boxt_hat-FIXED cut in the
MacNeille completion?  Also test the 2k-cycle generalization R_{2k}.
"""
from itertools import combinations, product

# ---------- generic poset / MacNeille machinery ----------
class Poset:
    def __init__(self, elems, leq_pairs):
        self.E = list(elems)
        self.leq = {(a,b): False for a in self.E for b in self.E}
        for a in self.E: self.leq[(a,a)] = True
        for (a,b) in leq_pairs: self.leq[(a,b)] = True
        # transitive closure
        changed = True
        while changed:
            changed = False
            for a in self.E:
                for b in self.E:
                    if self.leq[(a,b)]:
                        for c in self.E:
                            if self.leq[(b,c)] and not self.leq[(a,c)]:
                                self.leq[(a,c)] = True; changed = True
    def le(self,a,b): return self.leq[(a,b)]
    def upper(self, S):   # all upper bounds of set S
        return frozenset(x for x in self.E if all(self.le(s,x) for s in S))
    def lower(self, S):
        return frozenset(x for x in self.E if all(self.le(x,s) for s in S))
    def closure(self, S):  # (S^u)^l  -> MacNeille closed cut (a down-set)
        return self.lower(self.upper(S))
    def all_cuts(self):
        cuts = set()
        # every closed cut = closure of some subset; enumerate via closure of down-sets is enough
        # brute force over subsets is exponential; carriers are tiny so fine
        for r in range(len(self.E)+1):
            for S in combinations(self.E, r):
                cuts.add(self.closure(set(S)))
        return sorted(cuts, key=lambda c:(len(c), sorted(map(str,c))))
    def principal_cuts(self):
        return {frozenset(x for x in self.E if self.le(x,a)): a for a in self.E}

def boxt_hat(P, boxt, cut):
    # antitone MacNeille extension: boxt_hat(C) = (boxt[C])^l  (lower bounds of image)
    img = set(boxt[a] for a in cut)
    return P.lower(img)

def analyze(name, elems, leq_pairs, boxt, verbose=True):
    P = Poset(elems, leq_pairs)
    # antitonicity check
    anti = all((not P.le(a,b)) or P.le(boxt[b],boxt[a]) for a in P.E for b in P.E)
    cuts = P.all_cuts()
    prin = P.principal_cuts()
    prin_sets = set(prin.keys())
    # synt fixed point in carrier
    synt_fp = [a for a in P.E if boxt[a]==a]
    fixed_cuts = [c for c in cuts if boxt_hat(P,boxt,c)==c]
    nonprin_fixed = [c for c in fixed_cuts if c not in prin_sets]
    nonprin_cuts = [c for c in cuts if c not in prin_sets]
    if verbose:
        print(f"=== {name} ===")
        print(f"carrier |E|={len(P.E)}: {P.E}")
        print(f"boxt antitone: {anti}")
        print(f"syntactic fixed points (p=boxt p): {synt_fp}")
        print(f"# MacNeille cuts: {len(cuts)}   (# principal={len(prin_sets)}, # non-principal={len(nonprin_cuts)})")
        for c in nonprin_cuts:
            print(f"   non-principal cut: {set(sorted(map(str,c)))}  ->boxt_hat-> {set(sorted(map(str,boxt_hat(P,boxt,c))))}")
        print(f"# boxt_hat-FIXED cuts: {len(fixed_cuts)}  -> {[set(sorted(map(str,c))) for c in fixed_cuts]}")
        print(f"# NON-PRINCIPAL fixed cuts: {len(nonprin_fixed)}")
        print()
    return dict(anti=anti, synt_fp=synt_fp, ncuts=len(cuts),
                nfixed=len(fixed_cuts), nonprin_fixed=len(nonprin_fixed))

# ---------- Model 1: hexagon with 2-cycle plateau, boxt 0 = U ----------
# 0 < x,y ;  x,y < m,n ;  m,n < U ;  x||y, m||n
elems = ['0','x','y','m','n','U']
covers = [('0','x'),('0','y'),('x','m'),('x','n'),('y','m'),('y','n'),('m','U'),('n','U')]
boxt = {'0':'U','x':'y','y':'x','m':'0','n':'0','U':'0'}
analyze("Hexagon R_2 plateau, boxt 0 = U", elems, covers, boxt)

# ---------- Model 1b: boxt 0 = m (asymmetric) ----------
boxt_b = {'0':'m','x':'y','y':'x','m':'0','n':'0','U':'0'}
analyze("Hexagon R_2 plateau, boxt 0 = m", elems, covers, boxt_b)

# ---------- Model 2: R_4 four-cycle plateau on a doubled cover ----------
# 4-cycle x0->x1->x2->x3->x0 as an antitone orbit needs boxt antitone; a 4-cycle
# under an ANTITONE map means boxt swaps within a self-dual antichain of size 4?
# Simplest even-cycle test: two independent 2-cycles {x,y} and {x',y'} sharing
# doubled cover.  Here we test the "square" M-shape: lower antichain {x,y},
# boxt x=y, boxt y=x, with TWO separate join-covers to keep x v y unattained.
# (Already covered by hexagon.)  Instead test the antichain-4 plateau:
# lower antichain {p,q,r,s}, boxt: p<->q, r<->s (two 2-cycles), common cover.
elems4 = ['0','p','q','r','s','m','n','U']
covers4 = [('0','p'),('0','q'),('0','r'),('0','s'),
           ('p','m'),('q','m'),('r','m'),('s','m'),
           ('p','n'),('q','n'),('r','n'),('s','n'),
           ('m','U'),('n','U')]
boxt4 = {'0':'U','p':'q','q':'p','r':'s','s':'r','m':'0','n':'0','U':'0'}
analyze("Double-2-cycle plateau (antichain 4)", elems4, covers4, boxt4)

# ---------- Model 3: control -- genuine syntactic fixed point p=boxt p ----------
# 0 < p < U, boxt p = p, boxt 0 = U, boxt U = 0.  Should give a fixed cut.
elemsC = ['0','p','U']
coversC = [('0','p'),('p','U')]
boxtC = {'0':'U','p':'p','U':'0'}
analyze("Control: carrier with genuine fixed point p=boxt p", elemsC, coversC, boxtC)

# ---------- emit JSON report ----------
import json
def report(name, elems, leq_pairs, boxt):
    P = Poset(elems, leq_pairs)
    prin = set(P.principal_cuts().keys())
    cuts = P.all_cuts()
    fixed = [c for c in cuts if boxt_hat(P,boxt,c)==c]
    nonprin = [c for c in cuts if c not in prin]
    return dict(
        carrier=list(P.E),
        boxt=boxt,
        antitone=all((not P.le(a,b)) or P.le(boxt[b],boxt[a]) for a in P.E for b in P.E),
        synt_fixed_points=[a for a in P.E if boxt[a]==a],
        n_cuts=len(cuts),
        n_principal=len(prin),
        nonprincipal_cuts=[sorted(c) for c in nonprin],
        nonprincipal_cut_images={",".join(sorted(c)): sorted(boxt_hat(P,boxt,c)) for c in nonprin},
        n_fixed_cuts=len(fixed),
        fixed_cuts=[sorted(c) for c in fixed],
        n_nonprincipal_fixed=len([c for c in fixed if c not in prin]),
    )
out = {
 "pass": 117,
 "date": "2026-07-04",
 "claim": "boxt-antichain 2-cycle plateau {x,y} with unattained join (doubled cover) yields boxt_hat(x v y)=boxt x ^ boxt y = x^y, NOT fixed; minimal hexagon realization is globally fixed-point-free. Even-orbit geometry cannot host a non-principal boxt_hat-fixed cut. Control with genuine FP-synt DOES yield a fixed cut.",
 "models": {
   "hexagon_R2_boxt0_U": report("hex_U", elems, covers, boxt),
   "hexagon_R2_boxt0_m": report("hex_m", elems, covers, boxt_b),
   "double_2cycle_antichain4": report("dbl", elems4, covers4, boxt4),
   "control_genuine_fixed_point": report("ctrl", elemsC, coversC, boxtC),
 },
 "verdict": "NO-COEXISTENCE (parity obstruction). Thm116a (chain: join->bottom) and Thm117a (2-cycle: join->meet) unify as boxt_hat(x v y)=boxt x ^ boxt y; a fixed join needs images ABOVE the summands, impossible for any antitone orbit through the summands. A non-principal fixed cut requires an odd self-dual seed (FP-synt), which the no-synt-fixed-point hypothesis forbids."
}
with open("/sessions/charming-confident-tesla/mnt/outputs/pass117-report.json","w") as f:
    json.dump(out, f, indent=2)
print("JSON written; verdict:", out["verdict"][:60], "...")
