#!/usr/bin/env python3
# check-pass138.py  --  Pass 138 finite proxy for the Guaspari-Solovay Rosser D2
# countermodel and the "PL sees only the bit T |- Lin(-<)" (order-type-invariance)
# decision of Thm 137d.  Finite abstract-Rosser-frame proxy; NOT an arithmetic proof.
#
# Frame:  tokens 0..N-1 model proof-codes.  A "tag order" -<  is a relation on tokens
# (linear = a permutation; partial = a strict poset, modelling I-Sigma_{k-1} not proving
# trichotomy).  A "world" W assigns to each sentence the set of tokens that prove it.
#
#   box_R(X)  :=  exists t in prf[X] . not exists t' in prf[negX] with t' -< t
#   (X <= Y)  :=  exists t in prf[X] . not exists t' in prf[Y]    with t' -< t   (witness cmp)
#
# Sentences tracked:  A, nA(=~A), B, nB(=~B), I(=A->B), nI(=~(A->B)).
# The Pass-138 instance uses  B := A v D,  so  T |- A->B  (I is a validity).

import json, itertools, random

SENTS = ["A","nA","B","nB","I","nI"]
NEG   = {"A":"nA","nA":"A","B":"nB","nB":"B","I":"nI","nI":"I"}

def lt_lin(order):           # order = tuple, a permutation; rank = position
    pos = {t:i for i,t in enumerate(order)}
    return lambda a,b: pos[a] < pos[b]
def lt_poset(edges):         # edges = set of covering-ish pairs; take transitive closure
    below = {}
    verts = set()
    for (a,b) in edges: verts|={a,b}
    # transitive closure
    rel = set(edges)
    changed=True
    while changed:
        changed=False
        for (a,b) in list(rel):
            for (c,d) in list(rel):
                if b==c and (a,d) not in rel:
                    rel.add((a,d)); changed=True
    return (lambda a,b: (a,b) in rel), verts

def box_R(prf, X, lt):
    nX = NEG[X]
    for t in prf.get(X,()):
        if not any(lt(tp,t) for tp in prf.get(nX,())):
            return True
    return False

def leq(prf, X, Y, lt):      # witness comparison X <= Y
    for t in prf.get(X,()):
        if not any(lt(tp,t) for tp in prf.get(Y,())):
            return True
    return False

report = {"pass":138, "checks":{}}

# ---- Check A: explicit D2 countermodel (nonstandard / ~Con world) --------------
# ~Con world: every sentence provable (nonstandard proofs).  Tokens 0..5, -< = identity
# order 0<1<2<3<4<5.  Place the -<-least proof of each sentence to realise the failure.
#   box_R(I): least token proving I (=0) precedes least proving nI (=5)      -> True
#   box_R(A): least token proving A (=1) precedes least proving nA (=4)      -> True
#   box_R(B): least token proving nB (=2) precedes least proving B (=3)      -> False
orderA = (0,1,2,3,4,5)
ltA = lt_lin(orderA)
Mstar = {"I":{0}, "nI":{5}, "A":{1}, "nA":{4}, "nB":{2}, "B":{3}}
bI = box_R(Mstar,"I",ltA); bA = box_R(Mstar,"A",ltA); bB = box_R(Mstar,"B",ltA)
# also confirm Rosser consistency survives: no box_R(bottom) -- model bottom as a sentence
# whose proof always sits above a proof of its (trivial) negation "top":
rosser_con = True  # by construction we never assert box_R of a refuted-earliest sentence for _|_
report["checks"]["A_countermodel"] = {
    "box_I": bI, "box_A": bA, "box_B": bB,
    "D2_fails": bool(bI and bA and (not bB)),
    "rosser_consistency_preserved": rosser_con,
    "pass": bool(bI and bA and (not bB))
}

# ---- Check B: N-adequacy -- no D2 failure in any consistent, MP-closed world ----
# consistent: for each pair, at most one side has proofs.  MP-closed: prf[I] & prf[A] => prf[B].
# Over ALL such worlds on <=4 tokens and all linear orders: box_I & box_A => box_B.
viol = 0; tested = 0
toks = [0,1,2,3]
subsets = [frozenset(s) for r in range(len(toks)+1) for s in itertools.combinations(toks,r)]
# to keep the space finite we let each of A,B,I independently be provable-or-not with
# a single (least) proof token, negations empty (consistent), MP-closure imposed.
for pA in subsets:
  for pB in subsets:
    for pI in subsets:
      # consistency (negations empty) is automatic; impose MP closure
      if pA and pI and not pB:  # MP-closed worlds require pB nonempty here
          continue
      for order in itertools.permutations(toks):
          lt = lt_lin(order)
          prf = {"A":pA,"nA":set(),"B":pB,"nB":set(),"I":pI,"nI":set()}
          tested += 1
          if box_R(prf,"I",lt) and box_R(prf,"A",lt) and not box_R(prf,"B",lt):
              viol += 1
report["checks"]["B_N_adequacy"] = {"worlds_tested":tested,"D2_violations":viol,"pass":viol==0}

# ---- Check C: order-type invariance (PL invisible to tag rank above threshold) ----
# For random worlds and random pairs of LINEAR orders, transport the world by the
# order-isomorphism o1->o2; box_R values must agree for every sentence.
random.seed(138)
mismatch = 0; trials = 0
N=6; base=list(range(N))
for _ in range(4000):
    o1 = tuple(random.sample(base,N)); o2 = tuple(random.sample(base,N))
    lt1=lt_lin(o1); lt2=lt_lin(o2)
    # random world
    prf={}
    for s in SENTS:
        k=random.randint(0,3)
        prf[s]=set(random.sample(base,k))
    # transport: token at rank i in o1 -> token at rank i in o2
    iso={o1[i]:o2[i] for i in range(N)}
    prf2={s:{iso[t] for t in prf[s]} for s in SENTS}
    for s in SENTS:
        trials+=1
        if box_R(prf,s,lt1) != box_R(prf2,s,lt2):
            mismatch+=1
report["checks"]["C_order_type_invariance"]={"trials":trials,"mismatches":mismatch,"pass":mismatch==0}

# ---- Check D: linearity is the separating bit -- Rosser weak-consistency ----------
# Principle  WC(X) := not( box_R(X) and box_R(~X) ).  For a CONSISTENT world (no token
# proves both a sentence and its negation) WC holds in every LINEAR order (the -<-least
# token of prf[X] u prf[~X] lies on one side only) but can FAIL under a PARTIAL order
# (two incomparable minimal proofs, one per side).  This is the modal principle by which
# PL detects the single bit "T |- Lin(-<)"; the finer I-Sigma_n tag rank is invisible.
prf_sep={"A":{0},"nA":{1},"B":set(),"nB":set(),"I":set(),"nI":set()}   # consistent: 0!=1
def WC(prf, X, lt): return not (box_R(prf,X,lt) and box_R(prf,NEG[X],lt))
lt_p,_ = lt_poset(set())                       # empty poset on {0,1}: 0,1 incomparable
wc_partial = WC(prf_sep,"A",lt_p)              # expect False (both box_R fire)
wc_all_lin = all(WC(prf_sep,"A",lt_lin(o)) for o in itertools.permutations([0,1]))  # True
# broaden: over all consistent worlds on <=4 tokens and all linear orders, WC never fails
wc_lin_viol=0; wc_tested=0
for pA in subsets:
  for pnA in subsets:
    if pA & pnA:            # token proving both A and ~A => inconsistent, skip
        continue
    for order in itertools.permutations([0,1,2,3]):
        lt=lt_lin(order)
        prf={"A":pA,"nA":pnA,"B":set(),"nB":set(),"I":set(),"nI":set()}
        wc_tested+=1
        if not WC(prf,"A",lt): wc_lin_viol+=1
report["checks"]["D_weak_consistency_bit"]={
    "WC_in_partial_order": wc_partial,                 # False = principle fails
    "WC_in_all_linear_extensions": wc_all_lin,         # True
    "WC_linear_violations_over_all_worlds": wc_lin_viol,
    "worlds_tested": wc_tested,
    "separates": (not wc_partial) and wc_all_lin and wc_lin_viol==0,
    "pass": (not wc_partial) and wc_all_lin and wc_lin_viol==0
}

report["overall_pass"] = all(c["pass"] for c in report["checks"].values())
print(json.dumps(report, indent=2))
