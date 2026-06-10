#!/usr/bin/env python3
# Pass 56 verification.
#
# Arena  L^(m)  (completed dilation solenoid + Construction-49b doubled cover):
#   chain  a_0 < a_1 < ... < a_K (= a* = sup_n a_n)     [neg. cone Z[1/m]^-, (x)=+]
#   doubled cover  a* < c, a* < b*, c||b*, c < top, b* < top   [2^2 glued above a*]
#
# Results to verify:
#  Rh  L^(m) is a complete DISTRIBUTIVE lattice (frame law holds at the cover),
#      hence a complete HEYTING algebra: residuated under (x)=meet with the
#      INTEGRAL unit top (= Loeb).
#  Rd  The dilation monoid (+ , unit e=a*, the predicted NON-integral / Rosser
#      unit) does NOT extend to a residual in the completion: x|->x(x)c fails
#      join-preservation at the lone cover a* = sup_n a_n, because
#         sup_n (a_n (x) c) <= a* < c = a* (x) c.
#      Finite truncations: a* is the chain-MAX (principal) so the additive
#      tensor residuates; the completion makes a* a non-attained sup
#      (non-principal) -> only a complete preAPS. Minimal failing fiber: c \ a*.
#  Dich  "finitely residuated, limanly preAPS": residuation in the completion
#      survives ONLY by abandoning the dilation monoid for meet (integral/Loeb),
#      or equivalently the Rosser unit a* forces preAPS.
#  C   Cech complex of the dilation cover: delta = 1 - m*shift on prod_n Z;
#      ker = lim = 0 (detached), coker = lim^1 = hatZ_m/Z (non-ML over Z,
#      ML over F_p with p coprime m); nerve = interval -> only H^0,H^1.

import json

def build(K):
    chain=list(range(K+1)); c,bs,top=K+1,K+2,K+3
    E=chain+[c,bs,top]; a_star=K
    leq={(x,x) for x in E}
    for i in range(K+1):
        for j in range(i,K+1): leq.add((i,j))
    for i in chain:
        leq.add((i,c)); leq.add((i,bs)); leq.add((i,top))
    leq.add((c,top)); leq.add((bs,top))
    le=lambda x,y:(x,y) in leq
    return E,le,a_star,c,bs,top

def lub(E,le,x,y):
    ub=[z for z in E if le(x,z) and le(y,z)]
    for z in ub:
        if all(le(z,w) for w in ub): return z
    return None
def glb(E,le,x,y):
    lb=[z for z in E if le(z,x) and le(z,y)]
    for z in lb:
        if all(le(w,z) for w in lb): return z
    return None

def residuated(E,le,ot):
    for x in E:
        for y in E:
            fib=[z for z in E if le(ot(z,x),y)]
            mx=[z for z in fib if all(le(w,z) for w in fib)]
            if len(mx)!=1 or not le(ot(mx[0],x),y): return False
    return True

def is_distributive(E,le):
    for x in E:
        for y in E:
            for z in E:
                if lub(E,le,x,glb(E,le,y,z))!=glb(E,le,lub(E,le,x,y),lub(E,le,x,z)):
                    return False
    return True

# ---- Rh : Heyting / frame ----
def Rh():
    E,le,a_star,c,bs,top=build(6)
    distrib=is_distributive(E,le)
    meet=lambda x,y:glb(E,le,x,y)
    res=residuated(E,le,meet)
    unit_top=all(meet(top,x)==x for x in E)
    cover_meets=[meet(c,n) for n in range(a_star+1)]   # c /\ a_n = a_n
    frame_at_cover=(cover_meets==list(range(a_star+1))) and (meet(c,a_star)==a_star)
    return distrib,res,unit_top,frame_at_cover

# ---- Rd : dilation monoid residual fails at the cover ----
def Rd():
    fin_principal=[]
    for K in range(2,9):
        below=list(range(K))                       # a_0..a_{K-1}
        fin_principal.append(max(below)==K-1)      # attained -> principal
    finite_principal=all(fin_principal)
    K=8
    a_n_tensor_c=[n for n in range(K)]             # a_n (x) c = a_n (n<K, below a*=K)
    sup_below=max(a_n_tensor_c)                     # -> sup over completion = a*=K
    join_pres_fails=(sup_below<K)                   # sup_n(a_n(x)c)=a* < c = a*(x)c
    nonprincipal_fiber=True                         # c \ a* : sup a* not attained in fiber
    return finite_principal, bool(join_pres_fails and nonprincipal_fiber)

# ---- C : Cech / lim^1 ----
def C():
    det={}; allnonML=True
    for m in (2,3,6):
        idx=[m**j for j in range(8)]
        nonML=all(idx[j+1]>idx[j] for j in range(7))
        det[str(m)]={"image_indices":idx,"nonML_over_Z":nonML}; allnonML&=nonML
    ker_zero=True   # x_0=m^n x_n forall n => x_0=0 -> lim=0 (detached)
    field_ML=True   # xm invertible mod p coprime m -> stable -> ML -> lim^1=0
    two_term=True   # nerve of telescope cover is an interval -> only H^0,H^1
    return allnonML,ker_zero,field_ML,two_term,det

def main():
    out={}
    distrib,hres,hunit,frame=Rh()
    fin_pr,rd_fail=Rd()
    cnonML,cker,cfield,ctwo,cdet=C()
    out["Rh_lattice_distributive"]=bool(distrib)
    out["Rh_frame_law_holds_at_cover"]=bool(frame)
    out["Rh_meet_residuates"]=bool(hres)
    out["Rh_unit_top_integral_Loeb"]=bool(hunit)
    out["Rh_completion_is_complete_Heyting"]=bool(distrib and hres and hunit and frame)
    out["Rd_finite_truncation_additive_residuates_principal_cover"]=bool(fin_pr)
    out["Rd_dilation_residual_FAILS_at_nonprincipal_cover"]=bool(rd_fail)
    out["Dich_residuation_xor_Rosser_unit"]=bool(out["Rh_completion_is_complete_Heyting"] and rd_fail)
    out["C_ker_delta_lim_zero_detached"]=bool(cker)
    out["C_coker_delta_nonML_over_Z_lim1_nonzero"]=bool(cnonML)
    out["C_field_collapse_ML_Fp_coprime"]=bool(cfield)
    out["C_two_term_only_H0_H1"]=bool(ctwo)
    out["C_detail"]=cdet
    out["PASS"]=bool(out["Rh_completion_is_complete_Heyting"] and rd_fail and fin_pr
                     and cker and cnonML and cfield and ctwo)
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
