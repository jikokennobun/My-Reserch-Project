#!/usr/bin/env python3
"""
Pass 116 verification: doubled-cover top-repair of the Pass-113 four-element
MacNeille witness.

Carrier L = {0,a,b,c,m,n,U}, covers:
   0<a, a<b, 0<c, b<m, b<n, c<m, c<n, m<U, n<U   (m || n).
Bounded (bottom 0, top U) but NOT a lattice: {b,c} has minimal upper bounds
m,n which are incomparable, so b v c is not attained.  This is the
"one dimension up" doubled cover of the Pass-49 phantom a* < {m,b*}.

Question (Pass-114 -> 115 -> 116 thread): can a *bounded but non-lattice*
order simultaneously
   (R) make every residual fiber principal (residuation repaired), and
   (S) keep a non-principal MacNeille completion-fixed cut (separation kept)?
"""
import json, itertools

E = ['0','a','b','c','m','n','U']
N = len(E)
Z,A,B,C,M,Nn,U = 0,1,2,3,4,5,6
covers = [(Z,A),(A,B),(Z,C),(B,M),(B,Nn),(C,M),(C,Nn),(M,U),(Nn,U)]

leq = [[False]*N for _ in range(N)]
for i in range(N): leq[i][i]=True
for x,y in covers: leq[x][y]=True
for _ in range(N):
    for i in range(N):
        for j in range(N):
            if leq[i][j]:
                for k in range(N):
                    if leq[j][k]: leq[i][k]=True
def le(x,y): return leq[x][y]

po_ok = all((not(le(i,j) and le(j,i))) or i==j for i in range(N) for j in range(N))
bottom = [x for x in range(N) if all(le(x,y) for y in range(N))]
top    = [x for x in range(N) if all(le(y,x) for y in range(N))]
def upper_bounds(S): return [z for z in range(N) if all(le(s,z) for s in S)]
def lower_bounds(S): return [z for z in range(N) if all(le(z,s) for s in S)]
def join(x,y):
    ub=upper_bounds([x,y]); least=[z for z in ub if all(le(z,w) for w in ub)]
    return least[0] if len(least)==1 else None
def meet(x,y):
    lb=lower_bounds([x,y]); grt=[z for z in lb if all(le(w,z) for w in lb)]
    return grt[0] if len(grt)==1 else None
missing_joins=[(E[x],E[y]) for x in range(N) for y in range(N) if x<y and join(x,y) is None]
missing_meets=[(E[x],E[y]) for x in range(N) for y in range(N) if x<y and meet(x,y) is None]
is_lattice=(not missing_joins) and (not missing_meets)

boxt={Z:B,A:B,B:Z,C:Z,M:Z,Nn:Z,U:Z}
antitone=all((not le(x,y)) or le(boxt[y],boxt[x]) for x in range(N) for y in range(N))
synt_fp=[E[x] for x in range(N) if boxt[x]==x]

box_base={Z:Z,A:Z,C:Z,B:B}
def box_monotone(bx): return all((not le(x,y)) or le(bx[x],bx[y]) for x in range(N) for y in range(N))
def A2(): return le(A, boxt[Z])
def A3(bx):
    bt=boxt[A]
    for x in range(N):
        for y in range(N):
            if le(x,bx[y]) and le(x,boxt[y]) and not le(x,bt): return False
    return True
def A4(bx): return all(le(boxt[x],bx[boxt[x]]) for x in range(N))
def G2(): return (not le(boxt[A],Z)) or le(A,Z)
def FG2(): return le(boxt[boxt[A]],boxt[A])
admissible_box=[]
for bm in range(N):
    for bn in range(N):
        for bu in range(N):
            bx=dict(box_base); bx[M]=bm; bx[Nn]=bn; bx[U]=bu
            if not box_monotone(bx): continue
            if antitone and A2() and A3(bx) and A4(bx) and G2() and FG2():
                admissible_box.append({'box_m':E[bm],'box_n':E[bn],'box_U':E[bu]})

def uset(S): return frozenset(z for z in range(N) if all(le(s,z) for s in S))
def lset(S): return frozenset(z for z in range(N) if all(le(z,s) for s in S))
def closure(S): return lset(uset(S))
cuts=set()
for r in range(N+1):
    for S in itertools.combinations(range(N),r): cuts.add(closure(S))
cuts=sorted(cuts,key=lambda c:(len(c),sorted(c)))
downset={x:frozenset(z for z in range(N) if le(z,x)) for x in range(N)}
principal={c: next((E[x] for x in range(N) if downset[x]==c),None) for c in cuts}
def boxt_hat(c): return uset(lset(frozenset(boxt[x] for x in c)))
def show(c): return '{'+','.join(E[x] for x in sorted(c))+'}'
fixed=[c for c in cuts if boxt_hat(c)==c]
fixed_info=[{'cut':show(c),'principal_element':principal[c],'is_principal':principal[c] is not None} for c in fixed]
nonprincipal_fixed=[f for f in fixed_info if not f['is_principal']]
separation_survives=len(nonprincipal_fixed)>0 and len(synt_fp)==0

noncore=[A,B,C,M,Nn]
pairs=[(x,y) for i,x in enumerate(noncore) for y in noncore[i:]]
choices=[lower_bounds([x,y]) for (x,y) in pairs]
def build_tensor(assign):
    t=[[None]*N for _ in range(N)]
    for z in range(N):
        t[U][z]=z; t[z][U]=z; t[Z][z]=Z; t[z][Z]=Z
    for (px,py),v in zip(pairs,assign):
        t[px][py]=v; t[py][px]=v
    return t
def is_monotone(t):
    for x in range(N):
        for xp in range(N):
            if le(x,xp):
                for y in range(N):
                    if not le(t[x][y],t[xp][y]): return False
    return True
def is_assoc(t):
    return all(t[t[x][y]][z]==t[x][t[y][z]] for x in range(N) for y in range(N) for z in range(N))
def residuated(t):
    for x in range(N):
        for z in range(N):
            fib=[y for y in range(N) if le(t[x][y],z)]
            g=[y for y in fib if all(le(w,y) for w in fib)]
            if len(g)!=1: return False
    return True
count_assoc=count_mono=count_res=0
example_res=None; example_nonprincipal_fiber=None
total=1
for c in choices: total*=len(c)
for assign in itertools.product(*choices):
    t=build_tensor(assign)
    if not is_assoc(t): continue
    count_assoc+=1
    if not is_monotone(t): continue
    count_mono+=1
    if residuated(t):
        count_res+=1
        if example_res is None:
            example_res={(E[px],E[py]):E[v] for (px,py),v in zip(pairs,assign)}
    elif example_nonprincipal_fiber is None:
        for x in range(N):
            for z in range(N):
                fib=frozenset(y for y in range(N) if le(t[x][y],z))
                g=[y for y in fib if all(le(w,y) for w in fib)]
                if len(g)!=1:
                    example_nonprincipal_fiber={'x':E[x],'z':E[z],'fiber':show(fib)}; break
            if example_nonprincipal_fiber: break

report={'pass':116,'is_lattice':is_lattice,'missing_joins':missing_joins,
 'missing_meets':missing_meets,'boxt_antitone':antitone,'syntactic_fixed_points':synt_fp,
 'A2':A2(),'G2':G2(),'FG2':FG2(),'num_admissible_box_extensions':len(admissible_box),
 'num_macneille_cuts':len(cuts),'num_nonprincipal_cuts':sum(1 for c in cuts if principal[c] is None),
 'fixed_cuts':fixed_info,'separation_survives':separation_survives,
 'residuation_census':{'total':total,'associative':count_assoc,'assoc_monotone':count_mono,
   'residuated':count_res,'example_nonprincipal_fiber':example_nonprincipal_fiber}}
print(json.dumps(report,indent=2))
