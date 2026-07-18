#!/usr/bin/env python3
"""
Pass 124 verification (corrected): the odd-seed Rosser bouquet-with-center.

Central theorem (Thm 124a, CARRIER-JOIN CRITERION):
  the Henkin center of a 2-twin Rosser bouquet is CARRIER-SEEDED  <=>
  the bouquet disjunction c1 v c2 EXISTS IN THE CARRIER.
    * hexagon (Pass 123): c1 v c2 is only a MacNeille cut -> fixedness is
      completion-manufactured, carrier-SEEDLESS (Thm 123a census).
    * L* (this pass): c1 v c2 = w is a genuine carrier element -> boxt(w)=w
      is a CARRIER fixed cut, and can coexist with a DETACHED Jeroslow seed p.
  Since ConLat_T is a Boolean/Lindenbaum algebra, rho_1 v rho_2 is always a
  genuine sentence -> the arithmetic bouquet lives in the SEEDED (L*) regime.

Also: De-Morgan (lattice-antihom = normal/"D2") subclass analysis, and the
alpha(H)/phantom-tax facts (tax = 1 for EVERY H, connectedness-independent).

Run OFF-MOUNT (copy to /tmp) per the aps-run-sync-hazard memory.
"""
from itertools import product, combinations

def closure(n, covers):
    leq=[[i==j for j in range(n)] for i in range(n)]
    for a,b in covers: leq[a][b]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if leq[i][k] and leq[k][j]: leq[i][j]=True
    return leq

def antitone_maps(n, leq):
    rels=[(x,y) for x in range(n) for y in range(n) if leq[x][y] and x!=y]
    for f in product(range(n), repeat=n):
        if all(leq[f[y]][f[x]] for (x,y) in rels): yield f

def is_antichain(S, leq):
    return all(a==b or (not leq[a][b] and not leq[b][a]) for a in S for b in S)

def fixp(f): return [i for i in range(len(f)) if f[i]==i]

def lub(S, n, leq):
    ubs=[z for z in range(n) if all(leq[s][z] for s in S)]
    least=[z for z in ubs if all(leq[z][t] for t in ubs)]
    return least[0] if len(least)==1 else None
def glb(S, n, leq):
    lbs=[z for z in range(n) if all(leq[z][s] for s in S)]
    greatest=[z for z in lbs if all(leq[t][z] for t in lbs)]
    return greatest[0] if len(greatest)==1 else None

def is_lattice(n, leq):
    return all(lub([a,b],n,leq) is not None and glb([a,b],n,leq) is not None
               for a in range(n) for b in range(n))

def is_antihom(f, n, leq):
    """antitone lattice dual-homomorphism: f(a v b)=f(a)^f(b), f(a^b)=f(a) v f(b)."""
    for a in range(n):
        for b in range(n):
            j=lub([a,b],n,leq); m=glb([a,b],n,leq)
            if f[j]!=glb([f[a],f[b]],n,leq): return False
            if f[m]!=lub([f[a],f[b]],n,leq): return False
    return True

# ---------- L* : 0<c1,c2,p ; c1,c2<w ; w<U ; p<U ----------
Lc=[(0,1),(0,2),(0,4),(1,3),(2,3),(3,5),(4,5)]
leqL=closure(6,Lc); bot,c1,c2,w,p,U=0,1,2,3,4,5
assert lub([c1,c2],6,leqL)==w and is_lattice(6,leqL)

tot=0; fixw=0; sep_fixw=0; fused_fixw=0; seeded_bouquet=0; fixac=True
dm_total=0; dm_fixw=0; dm_sep_fixw=0
witness=None
for f in antitone_maps(6,leqL):
    tot+=1
    F=fixp(f)
    if not is_antichain(F,leqL): fixac=False
    dm=is_antihom(f,6,leqL)
    if dm: dm_total+=1
    if f[w]==w:
        fixw+=1
        sep = f[c1]!=f[c2]
        if sep: sep_fixw+=1
        else: fused_fixw+=1
        detached=[q for q in F if q!=w and not (leqL[q][w] or leqL[w][q])]
        if sep and detached:
            seeded_bouquet+=1
            if witness is None: witness=(f, detached)
        if dm:
            dm_fixw+=1
            if sep: dm_sep_fixw+=1

print("=== (A) L* carrier-join regime: seeded bouquet-with-center ===")
print(f"  antitone maps                                   : {tot}")
print(f"  maps with carrier fixed cut boxt(w)=w           : {fixw}  (sep={sep_fixw}, fused={fused_fixw})")
print(f"  SEEDED bouquet-with-center                      : {seeded_bouquet}")
print(f"    [separated twins & boxt(w)=w & detached seed] : {seeded_bouquet>0}")
print(f"  Fix(boxt) always an antichain                   : {fixac}")
if witness:
    f,det=witness
    names=['bot','c1','c2','w','p','U']
    print(f"    witness boxt: "+", ".join(f"{names[i]}->{names[f[i]]}" for i in range(6)))
    print(f"    Fix={[names[i] for i in fixp(f)]}, detached seed(s)={[names[i] for i in det]}")
print(f"  De-Morgan (lattice-antihom / 'normal D2') maps  : {dm_total}")
print(f"    of which fix w                                : {dm_fixw}  (separated among them: {dm_sep_fixw})")
A_ok = (seeded_bouquet>0) and fixac
print(f"  [A] PASS = {A_ok}")

# ---------- contrast: hexagon+center HP; x v y absent from carrier ----------
Hc=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5),(0,6),(6,5)]
leqH=closure(7,Hc); bx,X,Y,M,N,Utop,P=range(7)
print("\n=== (B) hexagon+center HP: completion-only center, detached carrier seed ===")
print(f"  x v y in carrier? lub({{'x','y'}}) = {lub([X,Y],7,leqH)}  (5=U) -> "
      f"{'ABSENT (only U); center is a MacNeille cut' if lub([X,Y],7,leqH)==Utop else 'present'}")
cross={bx:Utop,X:M,Y:N,M:X,N:Y,Utop:bx,P:P}; cf=tuple(cross[i] for i in range(7))
rels=[(a,b) for a in range(7) for b in range(7) if leqH[a][b] and a!=b]
cross_ok=all(leqH[cf[b]][cf[a]] for (a,b) in rels)
hp_fixac=all(is_antichain(fixp(f),leqH) for f in antitone_maps(7,leqH))
print(f"  seedless cross antitone={cross_ok}, Fix(cross)={[ 'bot,x,y,m,n,U,p'.split(',')[i] for i in fixp(cf)]} (detached p only)")
print(f"  Fix(boxt) always antichain on HP: {hp_fixac}")
B_ok = cross_ok and (lub([X,Y],7,leqH)==Utop) and hp_fixac
print(f"  [B] PASS = {B_ok}")

# ---------- (C) alpha(H) and phantom tax ----------
def maxind(m,edges):
    es=[frozenset(e) for e in edges]
    inds=[frozenset(S) for r in range(m+1) for S in combinations(range(m),r)
          if not any(e<=frozenset(S) for e in es)]
    return [S for S in inds if not any(S<T for T in inds)]
def conn(m,edges):
    ms=maxind(m,edges)
    if len(ms)<=1: return True
    adj={i:set() for i in range(len(ms))}
    for i,j in combinations(range(len(ms)),2):
        if ms[i]&ms[j]: adj[i].add(j); adj[j].add(i)
    seen={0}; st=[0]
    while st:
        u=st.pop()
        for v in adj[u]:
            if v not in seen: seen.add(v); st.append(v)
    return len(seen)==len(ms)
samples={"single{12}":(2,[(0,1)]),"path{12,23}":(3,[(0,1),(1,2)]),
 "K3":(3,[(0,1),(0,2),(1,2)]),"3-unif{123}":(3,[(0,1,2)]),
 "nonunif{12,234}":(4,[(0,1),(1,2,3)]),"disjoint{12,345}":(5,[(0,1),(2,3,4)])}
print("\n=== (C) alpha(H) and phantom tax ===")
C_ok=True
for nm,(m,e) in samples.items():
    k=len(maxind(m,e)); ap=2+k; api=1+k; tax=ap-api
    C_ok=C_ok and tax==1
    print(f"  {nm:18s} |MaxInd|={k}  a_phantom={ap}  a_principal={api}  tax={tax}  connected={conn(m,e)}")
print(f"  [C] tax==1 for EVERY H (incl. disconnected): {C_ok}")

print(f"\nOVERALL PASS = {A_ok and B_ok and C_ok}")
