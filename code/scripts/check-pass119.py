#!/usr/bin/env python3
"""
Pass 119 verification: does the frontier-onto criterion (Thm 118b, |F|=|G|=2)
survive to a THREE-element frontier crossing?

Carrier K33 = complete-bipartite bounded poset:
    elements: 0, f1,f2,f3, g1,g2,g3, U
    order:    0 <= everything;  everything <= U;  f_i <= g_j for ALL i,j.
The MacNeille completion adjoins exactly one non-principal cut
    w = {0,f1,f2,f3} = f1 v f2 v f3 = g1 ^ g2 ^ g3,
with lower frontier F = {f1,f2,f3}, upper frontier G = {g1,g2,g3}.

We test whether boxt[F]=G is necessary for w to be boxt_hat-fixed, or whether
the strictly weaker meet criterion  /\ boxt[F] = w  (Lemma 118a) admits fixed
cuts with boxt[F] != G (an image landing on a non-frontier element).

A hexagon regression (|F|=|G|=2) reproduces Pass 118: there boxt[F]=G IS
necessary (w is meet-irredundant).
"""
import itertools, json

# ---------- generic finite-poset / MacNeille machinery ----------
def make_poset(elems, less):
    leq = {(x,x) for x in elems}
    leq |= set(less)
    changed=True
    while changed:
        changed=False
        for (a,b) in list(leq):
            for (c,d) in list(leq):
                if b==c and (a,d) not in leq:
                    leq.add((a,d)); changed=True
    return leq

def upper(A, elems, leq):
    return frozenset(z for z in elems if all((a,z) in leq for a in A))
def lower(A, elems, leq):
    return frozenset(z for z in elems if all((z,a) in leq for a in A))
def cut(A, elems, leq):
    return lower(upper(A, elems, leq), elems, leq)

def all_cuts(elems, leq):
    cuts=set()
    for r in range(len(elems)+1):
        for S in itertools.combinations(elems, r):
            cuts.add(cut(frozenset(S), elems, leq))
    return cuts

def maxima(S, leq):
    return frozenset(x for x in S if not any((x,y) in leq and x!=y for y in S))
def minima(S, leq):
    return frozenset(x for x in S if not any((y,x) in leq and x!=y for y in S))

def antitone_maps(elems, leq, synt_fp_free=True):
    """Backtracking enumerator of antitone self-maps.
       Assign images bottom-up; boxt(x) must be <= boxt(z) for every z<x already set."""
    order = sorted(elems, key=lambda e: sum(1 for a in elems if (a,e) in leq))
    strictly_below = {x: [z for z in elems if (z,x) in leq and z!=x] for x in elems}
    result=[]
    img={}
    def rec(i):
        if i==len(order):
            result.append(dict(img)); return
        x=order[i]
        belows=[z for z in strictly_below[x] if z in img]
        for v in elems:
            if synt_fp_free and v==x:
                continue
            if all((v, img[z]) in leq for z in belows):
                img[x]=v
                rec(i+1)
        img.pop(x, None)
    rec(0)
    return result

def is_antitone(boxt, elems, leq):
    for x in elems:
        for y in elems:
            if (x,y) in leq and x!=y:
                if (boxt[y], boxt[x]) not in leq:
                    return False
    return True

def boxt_hat(C, boxt, elems, leq):
    img = frozenset(boxt[a] for a in C)
    return lower(img, elems, leq)

# ================= K33 carrier =================
K33 = ['0','f1','f2','f3','g1','g2','g3','U']
less=[]
for x in K33:
    if x!='0': less.append(('0',x))
    if x!='U': less.append((x,'U'))
for i in '123':
    for j in '123':
        less.append(('f'+i,'g'+j))
leqK = make_poset(K33, less)
cutsK = all_cuts(K33, leqK)
principal = {frozenset(z for z in K33 if (z,a) in leqK) for a in K33}
nonprincipal = [c for c in cutsK if c not in principal]

w = frozenset({'0','f1','f2','f3'})
F = maxima(w, leqK)
ub = set(upper(w,K33,leqK)) - set(w)
Gset = minima(frozenset(ub), leqK)

report={"model":"K33_bipartite_bounded",
        "carrier":K33,
        "num_cuts":len(cutsK),
        "num_nonprincipal_cuts":len(nonprincipal),
        "nonprincipal_cuts":[sorted(c) for c in nonprincipal],
        "w":sorted(w),"F":sorted(F),"G":sorted(Gset)}

# ---- explicit witnesses ----
witnesses={}
A  = {'0':'U','f1':'g1','f2':'g2','f3':'g3','g1':'0','g2':'0','g3':'0','U':'0'}
D  = {'0':'U','f1':'g1','f2':'g2','f3':'U','g1':'0','g2':'0','g3':'0','U':'0'}
E  = {'0':'U','f1':'g1','f2':'g2','f3':'g2','g1':'0','g2':'0','g3':'0','U':'0'}
C0 = {'0':'U','f1':'g1','f2':'g1','f3':'g1','g1':'0','g2':'0','g3':'0','U':'0'}
for name,mp in [("A_onto",A),("D_top_nonfrontier",D),("E_repeat_frontier",E),("C0_collapse_principal",C0)]:
    anti=is_antitone(mp,K33,leqK)
    fpfree=all(mp[x]!=x for x in K33)
    bh=boxt_hat(w,mp,K33,leqK)
    imgF=sorted({mp[x] for x in F})
    witnesses[name]={"map":mp,"antitone":anti,"synt_fp_free":fpfree,
                     "boxt[F]":imgF,"boxt[F]==G":set(imgF)==set(sorted(Gset)),
                     "boxt_hat(w)":sorted(bh),"fixes_w":bh==w}
report["witnesses"]=witnesses

# ---- full census over antitone synt-FP-free maps on K33 ----
maps = antitone_maps(K33, leqK, synt_fp_free=True)
n_total=len(maps)
fix_maps=[m for m in maps if boxt_hat(w,m,K33,leqK)==w]
fix_onto=[m for m in fix_maps if {m[x] for x in F}==set(Gset)]
fix_not_onto=[m for m in fix_maps if {m[x] for x in F}!=set(Gset)]
frontier_elts=set(F)|set(Gset)
fix_nonfrontier_img=[m for m in fix_not_onto if any(m[x] not in frontier_elts for x in F)]
inter_sizes={}
disjoint=0
for m in fix_maps:
    k=len({m[x] for x in F}&set(Gset))
    inter_sizes[k]=inter_sizes.get(k,0)+1
    if k==0: disjoint+=1
report["census_K33"]={
    "antitone_syntFPfree_total":n_total,
    "fix_w_total":len(fix_maps),
    "fix_w_boxtF_eq_G":len(fix_onto),
    "fix_w_boxtF_neq_G":len(fix_not_onto),
    "fix_w_with_nonfrontier_image":len(fix_nonfrontier_img),
    "intersection_size_distribution_|boxtF_cap_G|":inter_sizes,
    "fix_w_with_boxtF_disjoint_from_G":disjoint,
    "necessity_of_boxtF_eq_G_holds": len(fix_not_onto)==0,
}

# ================= hexagon regression (|F|=|G|=2) =================
HEX=['0','x','y','m','n','U']
lessH=[('0','x'),('0','y'),('x','m'),('x','n'),('y','m'),('y','n'),('m','U'),('n','U')]
leqH=make_poset(HEX,lessH)
wH=frozenset({'0','x','y'})
FH=maxima(wH,leqH)
ubH=set(upper(wH,HEX,leqH))-set(wH)
GH=minima(frozenset(ubH),leqH)
mapsH=antitone_maps(HEX,leqH,synt_fp_free=True)
fixH=[m for m in mapsH if boxt_hat(wH,m,HEX,leqH)==wH]
fixH_onto=[m for m in fixH if {m[a] for a in FH}==set(GH)]
report["hexagon_regression"]={
    "F":sorted(FH),"G":sorted(GH),
    "antitone_syntFPfree_total":len(mapsH),
    "fix_w_total":len(fixH),
    "fix_w_boxtF_eq_G":len(fixH_onto),
    "necessity_of_boxtF_eq_G_holds": len(fixH)==len(fixH_onto),
}

# ---- overall PASS conditions ----
checks = {
  "K33_has_unique_nonprincipal_cut": len(nonprincipal)==1 and nonprincipal[0]==w,
  "F_and_G_size_3": len(F)==3 and len(Gset)==3,
  "witness_A_onto_fixes": witnesses["A_onto"]["fixes_w"] and witnesses["A_onto"]["antitone"] and witnesses["A_onto"]["boxt[F]==G"],
  "witness_D_nonfrontier_fixes_but_not_onto": witnesses["D_top_nonfrontier"]["fixes_w"] and witnesses["D_top_nonfrontier"]["antitone"] and not witnesses["D_top_nonfrontier"]["boxt[F]==G"],
  "witness_E_repeat_fixes_but_not_onto": witnesses["E_repeat_frontier"]["fixes_w"] and not witnesses["E_repeat_frontier"]["boxt[F]==G"],
  "control_C0_not_fixed": not witnesses["C0_collapse_principal"]["fixes_w"],
  "necessity_FAILS_at_triple": report["census_K33"]["fix_w_boxtF_neq_G"]>0,
  "no_fix_disjoint_from_G": report["census_K33"]["fix_w_with_boxtF_disjoint_from_G"]==0,
  "hexagon_necessity_HOLDS": report["hexagon_regression"]["necessity_of_boxtF_eq_G_holds"],
}
report["checks"]=checks
report["overall"]="PASS" if all(checks.values()) else "FAIL"
print(json.dumps(report, indent=2))
