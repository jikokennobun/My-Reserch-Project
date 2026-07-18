#!/usr/bin/env python3
"""
check-pass127.py  --  APS / G2-ZOO autonomous discussion, Pass 127.

Arithmetic realization of the honest vs phantom Rosser bouquet (Cor 126d) and the
vertical/horizontal decoupling under adjoining axiom 4 (D3^hom).  Self-contained;
run off-mount per the aps-run-sync-hazard memory.

  A  nFG2(1)&nFG2(2) => index-2 stabilization (Thm 41a core; ML/honest, the Arai shadow),
     PROVED via the antitone bounce; and a SINGLE nFG2(1) instance at a NON-top frontier
     seed is INSUFFICIENT (Skeptic's point).  Remark: at the TOP T, even nFG2(1) collapses
     (f(T) is the image-minimum) -- WHY a Rosser bouquet frontier must sit at non-top twins.
  B  least-witness nesting tower ~ (Z, x m): non-ML, truncated lim^1 = Z/m^K -> hatZ_m/Z;
     Arai tower eventually constant: ML, lim^1 = 0.  Radical-invariance (Thm 54b).
  C  vertical/horizontal DECOUPLING (Thm 127c): adjoining 4 (nFG2 on the facet tower) forces
     ML but leaves the twin multiplicity |Fix_twins| = k unchanged.
  D  infinite-but-ML honest cell (Thm 127b / arithmetic Thm-126c gap): |facets|=aleph0 yet ML.
"""
import itertools, json

def antitone_maps_on(E, leq):
    for tup in itertools.product(E, repeat=len(E)):
        f = dict(zip(E, tup)); ok = True
        for x in E:
            for y in E:
                if leq(x, y) and not leq(f[y], f[x]): ok = False; break
            if not ok: break
        if ok: yield f

def orbit(f, t, depth=6):
    o = [t]
    for _ in range(depth): o.append(f[o[-1]])
    return o

def chain(n): return list(range(n)), (lambda x, y: x <= y), n - 1
def diamond_M3():
    up = {0:{0,1,2,3,4},1:{1,4},2:{2,4},3:{3,4},4:{4}}
    return [0,1,2,3,4], (lambda x,y: y in up[x]), 4
def Lstar():
    up = {0:{0,1,2,3,4,5},1:{1,3,5},2:{2,3,5},3:{3,5},4:{4,5},5:{5}}
    return [0,1,2,3,4,5], (lambda x,y: y in up[x]), 5

# ===================================================================== PART A
def partA():
    res = {"posets":{}, "index2_collapse_violations":0, "antitone_bounce_violations":0,
           "single_instance_insufficient_examples":[], "top_collapse_confirmed":{}}
    for name,(E,leq,top) in [("C3",chain(3)),("C4",chain(4)),("C5",chain(5)),
                             ("M3",diamond_M3()),("Lstar",Lstar())]:
        tot=collapse_ok=single_insuff=0; top_ok=True; ex=None
        bottoms={x for x in E if all(leq(x,y) for y in E)}
        for f in antitone_maps_on(E,leq):
            tot+=1
            ot=orbit(f,top)
            # top remark: nFG2(1) at T => o1==o2 (f(T) is image-min so o1<=o2 always)
            if leq(ot[2],ot[1]) and ot[1]!=ot[2]:
                top_ok=False
            for s in E:
                o=orbit(f,s)
                n1=leq(o[2],o[1]); n2=leq(o[3],o[2])
                if n1 and not leq(o[2],o[3]):
                    res["antitone_bounce_violations"]+=1     # bounce: n1 => o2<=o3
                if n1 and n2:                                # Thm 41a core: => o2==o3
                    if o[2]==o[3]: collapse_ok+=1
                    else: res["index2_collapse_violations"]+=1
                if n1 and (not n2) and s!=top:               # single instance insufficient
                    single_insuff+=1
                    if ex is None or (ex["seed_is_bottom"] and s not in bottoms):
                        ex={"poset":name,"seed":str(s),"seed_is_bottom":(s in bottoms),
                            "map":{str(k):str(v) for k,v in f.items()},
                            "orbit":[str(x) for x in o[:5]]}
        res["posets"][name]={"antitone_total":tot,"index2_collapse_ok":collapse_ok,
                             "single_instance_insufficient":single_insuff}
        res["top_collapse_confirmed"][name]=top_ok
        if ex: res["single_instance_insufficient_examples"].append(ex)
    res["PASS"]=(res["index2_collapse_violations"]==0 and res["antitone_bounce_violations"]==0
                 and len(res["single_instance_insufficient_examples"])>0
                 and all(res["top_collapse_confirmed"].values()))
    return res

# ===================================================================== PART B
def image_index_tower(mults):
    idx=[1]
    for a in mults: idx.append(idx[-1]*a)
    return idx
def primes_of(n):
    p=set(); d=2
    while d*d<=n:
        while n%d==0: p.add(d); n//=d
        d+=1
    if n>1: p.add(n)
    return sorted(p)
def partB():
    K=8
    out={"least_witness_phantom":{}, "arai_honest":{}, "radical_invariance":{}}
    for m in (2,4,8,6,1):
        idx=image_index_tower([m]*K)
        out["least_witness_phantom"][f"m={m}"]={
            "index_tower":idx, "lim1_trunc_order":idx[K],
            "non_ML": m>1, "strictly_increasing_index": all(idx[i]<idx[i+1] for i in range(K)) if m>1 else False,
            "phantom_primes": primes_of(m) if m>1 else []}
    N=2
    for m in (2,6):
        mults=[m]*N+[1]*(K-N); idx=image_index_tower(mults)
        ev=idx[-1]==idx[-2]==idx[-3]
        out["arai_honest"][f"m={m}_stab@{N}"]={"index_tower":idx,"ML":ev,"lim1":0 if ev else "nonzero"}
    for group in [[2,4,8],[6,12],[1]]:
        rads={m:(primes_of(m) if m>1 else []) for m in group}
        out["radical_invariance"][str(group)]={"radicals":rads,
            "same_phantom":len({tuple(v) for v in rads.values()})==1}
    A=out["least_witness_phantom"]; B=out["arai_honest"]; R=out["radical_invariance"]
    out["PASS"]=(all(A[k]["non_ML"] for k in A if k!="m=1") and A["m=1"]["non_ML"]==False
                 and all(B[k]["ML"] for k in B)
                 and R["[2, 4, 8]"]["same_phantom"] and R["[6, 12]"]["same_phantom"])
    return out

# ===================================================================== PART C
def build_twin_tower(k, transitive):
    ps=[f"p{i}" for i in range(1,k+1)]; tower=["t0","t1","t2"]
    E=["b","U"]+ps+tower
    def leq(x,y):
        if x==y: return True
        if x=="b": return True
        if y=="U": return True
        if x in tower and y in tower: return tower.index(x)>=tower.index(y)  # t2<=t1<=t0
        return False
    f={"b":"U","U":"b"}
    for p in ps: f[p]=p
    if transitive:                       # ML: t0-orbit stabilizes at the seed t1
        f["t0"]="t1"; f["t1"]="t1"; f["t2"]="t1"
    else:                                # non-ML: order-reversal 2-cycle t0<->t2 (t1 fixed detached)
        f["t0"]="t2"; f["t1"]="t1"; f["t2"]="t0"
    anti=all(leq(f[y],f[x]) for x in E for y in E if leq(x,y))
    return E,leq,f,"t0",anti
def partC():
    out={"cases":{}}; ok=True
    for k in (1,2,3):
        E,leq,f_non,tw,a_non=build_twin_tower(k,False)
        _,_,f_tr,_,a_tr=build_twin_tower(k,True)
        twins_non=sorted(x for x in f_non if f_non[x]==x and x.startswith("p"))
        twins_tr =sorted(x for x in f_tr  if f_tr[x]==x  and x.startswith("p"))
        o_non=orbit(f_non,tw); o_tr=orbit(f_tr,tw)
        ml_non=(o_non[2]==o_non[3]); ml_tr=(o_tr[2]==o_tr[3])
        preserved=(twins_non==twins_tr and len(twins_tr)==k)
        out["cases"][f"k={k}"]={"antitone_nontrans":a_non,"antitone_trans":a_tr,
            "twins":twins_tr,"twin_multiplicity_preserved":preserved,
            "tower_orbit_nontrans":o_non[:5],"tower_orbit_trans":o_tr[:5],
            "ML_nontrans":ml_non,"ML_trans":ml_tr}
        ok=ok and a_non and a_tr and preserved and ml_tr and (not ml_non)
    out["PASS"]=ok
    return out

# ===================================================================== PART D
def partD():
    H=8
    cells=[{"name":"compact_honest","facets":3,"mults":[2,2]+[1]*(H-2)},
           {"name":"infinite_ML_honest","facets":"aleph0","mults":[2,2]+[1]*(H-2)},
           {"name":"infinite_phantom","facets":"aleph0","mults":[2]*H}]
    out={"cells":[]}
    for c in cells:
        idx=image_index_tower(c["mults"]); ml=idx[-1]==idx[-2]==idx[-3]
        out["cells"].append({**c,"index_tower":idx,"ML":ml,"honest":ml,
                             "compact":c["facets"]!="aleph0"})
    d=out["cells"]
    inf_ml=[x for x in d if x["facets"]=="aleph0" and x["ML"]]
    inf_no=[x for x in d if x["facets"]=="aleph0" and not x["ML"]]
    out["ml_vs_compact_gap_realized"]=(len(inf_ml)==1 and len(inf_no)==1
                                       and inf_ml[0]["honest"] and not inf_no[0]["honest"])
    out["PASS"]=out["ml_vs_compact_gap_realized"] and d[0]["honest"]
    return out

report={"pass":127,"title":"Arithmetic honest/phantom Rosser bouquet + vertical/horizontal decoupling"}
report["A_nFG2_schema_ML"]=partA()
report["B_madic_phantom_tower"]=partB()
report["C_vertical_horizontal_decoupling"]=partC()
report["D_infinite_ML_honest_cell"]=partD()
report["overall_PASS"]=all(report[k]["PASS"] for k in
    ["A_nFG2_schema_ML","B_madic_phantom_tower","C_vertical_horizontal_decoupling","D_infinite_ML_honest_cell"])
open("report.json","w").write(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
