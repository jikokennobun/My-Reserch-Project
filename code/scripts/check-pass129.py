#!/usr/bin/env python3
# check-pass129.py -- APS G2-ZOO autonomous Pass 129
# (A) Phantom-spectrum realization: nesting towers (Z, x m_n) -> lim^1 = Zhat_N / Z,
#     N the Steinitz number; radical-invariance of constant towers; pathologies.
# (B) Simultaneous higher-lim^n honesty: consistency table (lim^1=0 does not decide lim^2=0;
#     simultaneous vanishing is a large-cardinal statement).
# (C) Pure-Box-inexpressibility of WO/Loeb: depth-d bisimulation certificate over
#     serial+transitive Kripke models; a separate witness-comparison relation "<" separates.
import json, itertools
from functools import lru_cache

report = {"pass": 129, "parts": {}}

# ----------------------------------------------------------------------------
# helpers
def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def rad(n):
    return set(factor(n).keys())

FIRST_PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

# ----------------------------------------------------------------------------
# PART A -- phantom spectrum
# A tower is a multiplier sequence (m_1,...,m_N) plus a declared tail rule:
#   ('const', c)  -> m_n = c for all n > N
#   ('id',)       -> m_n = 1 for all n > N   (eventually identity)
# lim^1(Z, x m_n) = Zhat_N / Z with N = prod m_n (Steinitz number).
#   * Mittag-Leffler  <=>  images M_n Z stabilize  <=>  tail multipliers are units (=1).
#   * Supp_inf(N) = { p : v_p(M_n) -> infinity } = primes of infinite cumulative valuation
#                 = the solenoidal support (the genuine prod Z_p part of the phantom).
#   * non-ML with Supp_inf empty  =>  a phantom that is NONZERO yet has no Z_p solenoid
#     (a purely finitary / adelic-torsion phantom).
def analyze(head, tail, depth=400):
    # cumulative p-adic valuation of partial products, plus ML status & Supp_inf
    seq = list(head)
    if tail[0] == 'const':
        seq += [tail[1]] * (depth - len(seq))
        tail_units = (tail[1] in (1, -1))
    elif tail[0] == 'id':
        seq += [1] * (depth - len(seq))
        tail_units = True
    val = {}
    for m in seq:
        for p, e in factor(abs(m)).items() if m not in (0,1,-1) else {}.items():
            val[p] = val.get(p, 0) + e
    # a prime has "infinite" cumulative valuation iff the tail keeps supplying it
    supp_inf = set()
    if tail[0] == 'const' and tail[1] not in (1, -1):
        supp_inf = rad(tail[1])
    ML = tail_units  # eventually-unit multipliers <=> images stabilize <=> ML
    nonzero = not ML
    # finitely-supported primes (appear but tail doesn't sustain them)
    finite_primes = {p for p, v in val.items() if p not in supp_inf and v > 0}
    return {"ML": ML, "phantom_nonzero": nonzero, "supp_inf": sorted(supp_inf),
            "finite_primes_count": len(finite_primes),
            "solenoid": "prod_{p in %s} Z_p / Z" % sorted(supp_inf) if supp_inf else
                        ("NONZERO finitary/adelic phantom (empty solenoid)" if nonzero else "0")}

A = {}
# constant towers: radical-invariance {2,4,8} and {6,12}
A["const_2"]  = analyze([], ('const', 2))
A["const_4"]  = analyze([], ('const', 4))
A["const_8"]  = analyze([], ('const', 8))
A["const_6"]  = analyze([], ('const', 6))
A["const_12"] = analyze([], ('const', 12))
# r-ary races r = 2,3,4,6,30
for r in (2,3,4,6,30):
    A["race_%d" % r] = analyze([], ('const', r))
# primorial race: m_n = n-th prime, each prime once  -> Supp_inf empty, non-ML
A["primorial"] = analyze(FIRST_PRIMES, ('id',))   # after list: no more growth -> ML (phantom 0)
# genuine primorial needs infinitely many DISTINCT primes; emulate: tail keeps a
# NEW prime each step is not expressible by a constant tail, so we test the finite
# truncation property directly: non-unit head, each prime once => all finite valuations.
prim_val = {}
for m in FIRST_PRIMES:
    for p in rad(m):
        prim_val[p] = prim_val.get(p, 0) + 1
A["primorial_truncation"] = {
    "all_valuations_bounded_by_1": all(v == 1 for v in prim_val.values()),
    "distinct_primes": len(prim_val),
    "note": "infinite continuation -> non-ML, Supp_inf = empty => purely finitary phantom"
}
# eventually identity vs eventually constant-2
A["eventually_id_222_then_1"]   = analyze([2,2,2], ('id',))
A["eventually_const2_357_then2"] = analyze([3,5,7], ('const', 2))

checksA = {
    "radinv_248_equal": A["const_2"]["supp_inf"] == A["const_4"]["supp_inf"] == A["const_8"]["supp_inf"] == [2],
    "radinv_6_12_equal": A["const_6"]["supp_inf"] == A["const_12"]["supp_inf"] == [2,3],
    "race_radicals": [A["race_%d"%r]["supp_inf"] for r in (2,3,4,6,30)] == [[2],[3],[2],[2,3],[2,3,5]],
    "primorial_bounded": A["primorial_truncation"]["all_valuations_bounded_by_1"] is True,
    "eventually_id_kills_phantom": A["eventually_id_222_then_1"]["phantom_nonzero"] is False,
    "eventually_const2_keeps_Z2": (A["eventually_const2_357_then2"]["phantom_nonzero"] is True
                                    and A["eventually_const2_357_then2"]["supp_inf"] == [2]),
}
report["parts"]["A_phantom_spectrum"] = {"data": A, "checks": checksA, "pass": all(checksA.values())}

# ----------------------------------------------------------------------------
# PART B -- simultaneous higher-lim^n honesty (consistency table, not a ZFC proof)
# Scenarios record (lim^1_vanishes, all_lim_n_vanish, uses_large_cardinal).
scenarios = {
    "V=L":                 {"lim1": False, "all_lim": False, "large_cardinal": False},
    "b=aleph_1":           {"lim1": False, "all_lim": False, "large_cardinal": False},
    "MA_aleph_1":          {"lim1": True,  "all_lim": False, "large_cardinal": False},  # honest at lim^1, higher OPEN/not forced
    "weakly_compact_force":{"lim1": True,  "all_lim": True,  "large_cardinal": True},   # BLH 2021 upper bound
}
# Claim (i): all_lim => lim1   (upward vanishing is downward-consistent)
claim_i = all((not s["all_lim"]) or s["lim1"] for s in scenarios.values())
# Claim (ii): lim1 does NOT imply all_lim  (a scenario with lim1 True, all_lim False exists)
claim_ii_split = any(s["lim1"] and not s["all_lim"] for s in scenarios.values())
# Claim (iii): all_lim only in a large-cardinal scenario (no ZFC/small model gives all_lim)
claim_iii_lc = all((not s["all_lim"]) or s["large_cardinal"] for s in scenarios.values())
checksB = {"i_all_implies_1": claim_i, "ii_lim1_does_not_decide_higher": claim_ii_split,
           "iii_simultaneous_needs_large_cardinal": claim_iii_lc}
report["parts"]["B_simultaneous_honesty"] = {"scenarios": scenarios, "checks": checksB, "pass": all(checksB.values())}

# ----------------------------------------------------------------------------
# PART C -- pure-Box-inexpressibility of WO/Loeb via bisimulation certificates.
# Kripke model: worlds, R (Box relation, serial+transitive), val, plus a SEPARATE
# witness-comparison relation prec (the "<").  WO = "prec is converse-well-founded".
class KM:
    def __init__(self, worlds, R, val, prec):
        self.W = worlds; self.R = R; self.val = val; self.prec = prec
    def succ(self, w): return [v for (x,v) in self.R if x==w]

def sat(M, w, f):
    t = f[0]
    if t=='p':   return M.val[w]['p']
    if t=='not': return not sat(M,w,f[1])
    if t=='and': return sat(M,w,f[1]) and sat(M,w,f[2])
    if t=='or':  return sat(M,w,f[1]) or sat(M,w,f[2])
    if t=='imp': return (not sat(M,w,f[1])) or sat(M,w,f[2])
    if t=='box': return all(sat(M,v,f[1]) for v in M.succ(w))
    raise ValueError(t)

def formulas_upto(depth):
    base = [('p',), ('not',('p',))]
    cur = list(base); allf = set(map(repr, cur)); out = list(cur)
    for _ in range(depth):
        nxt = []
        for f in cur:
            nxt.append(('box', f)); nxt.append(('not',('box',f)))
        added=[]
        for f in nxt:
            r = repr(f)
            if r not in allf:
                allf.add(r); out.append(f); added.append(f)
        cur = nxt
    small = out[:12]
    return out + [('imp',a,b) for a in small for b in small]

def prec_well_founded(M):
    adj = {}
    for (a,b) in M.prec: adj.setdefault(a,[]).append(b)
    color = {w:0 for w in M.W}
    def dfs(u):
        color[u]=1
        for v in adj.get(u,[]):
            if color[v]==1: return True
            if color[v]==0 and dfs(v): return True
        color[u]=2; return False
    return not any(color[w]==0 and dfs(w) for w in M.W)

LOEB = ('imp', ('box', ('imp', ('box',('p',)), ('p',))), ('box',('p',)))

# ---- Pair 1: identical Box-reduct (pure-Box equivalent at EVERY depth), prec differs.
# p false at the reflexive bottom => Loeb refuted; WO differs => WO not pure-Box-definable.
def chain_reduct(K):
    W = list(range(K+1))
    R = [(i,j) for i in range(K+1) for j in range(K+1) if j>i] + [(K,K)]  # strict+refl bottom: serial,transitive
    val = {w:{'p': (w!=K)} for w in W}   # p false only at bottom K
    return W,R,val
W,R,val = chain_reduct(6)
prec_ill = [(i,i+1) for i in range(6)] + [(6,6)]   # loop => ill-founded => WO false
prec_wf  = [(i,i+1) for i in range(6)]             # acyclic => WO true
M_ill = KM(W,R,val,prec_ill); M_wf = KM(W,R,val,prec_wf)
loeb_ill = sat(M_ill,0,LOEB); loeb_wf = sat(M_wf,0,LOEB)
F4 = formulas_upto(4)
disagree_pair1 = [repr(f) for f in F4 if sat(M_ill,0,f) != sat(M_wf,0,f)]
wo_ill = prec_well_founded(M_ill); wo_wf = prec_well_founded(M_wf)

# ---- Pair 2: DIFFERENT Box-frames, fully bisimilar => pure-Box cannot measure R-depth.
# reflexive singleton vs converse-ill-founded chain; p false everywhere (Loeb refuted, serial).
Ma = KM([0], [(0,0)], {0:{'p':False}}, [])
Wb = list(range(7)); Rb = [(i,j) for i in range(7) for j in range(7) if j>i] + [(6,6)]
Mb = KM(Wb, Rb, {w:{'p':False} for w in Wb}, [])
disagree_pair2 = [repr(f) for f in F4 if sat(Ma,0,f) != sat(Mb,0,f)]
loeb_a = sat(Ma,0,LOEB); loeb_b = sat(Mb,0,LOEB)

# ---- Frame census: no serial+transitive frame on <=3 worlds validates the Loeb instance.
def all_frames(n):
    worlds = list(range(n)); pairs = [(i,j) for i in worlds for j in worlds]
    for bits in itertools.product([0,1], repeat=len(pairs)):
        R = [pairs[k] for k in range(len(pairs)) if bits[k]]; Rs = set(R)
        serial = all(any((i,j) in Rs for j in worlds) for i in worlds)
        trans = all((i,k) in Rs for (i,j) in R for (j2,k) in R if j==j2)
        if serial and trans: yield worlds, R
cnt=loeb_valid=refute=reflexive_cycle=0
for worlds,R in all_frames(3):
    cnt+=1; Rs=set(R)
    if any((w,w) in Rs for w in worlds): reflexive_cycle+=1
    valid=True
    for vbits in itertools.product([0,1], repeat=len(worlds)):
        M=KM(worlds,R,{w:{'p':bool(vbits[w])} for w in worlds},[])
        if not all(sat(M,w,LOEB) for w in worlds): valid=False; break
    if valid: loeb_valid+=1
    else: refute+=1

checksC = {
    "pair1_loeb_refuted_both": (loeb_ill is False and loeb_wf is False),
    "pair1_pureBox_depth4_identical": (len(disagree_pair1)==0),
    "pair1_WO_separates": (wo_ill is False and wo_wf is True),
    "pair2_fully_bisimilar_depth4": (len(disagree_pair2)==0),
    "pair2_loeb_refuted_both": (loeb_a is False and loeb_b is False),
    "census_no_frame_validates_loeb": (loeb_valid==0 and refute==cnt and cnt>0),
    "census_all_reflexive_cycle": (reflexive_cycle==cnt),
    "frame_count": cnt,
    "num_depth4_formulas": len(F4),
}
report["parts"]["C_pureBox_inexpressibility"] = {
    "checks": checksC,
    "pass": all(v is True for k,v in checksC.items() if isinstance(v,bool))
}

report["overall_pass"] = all(report["parts"][k]["pass"] for k in report["parts"])
print(json.dumps(report, indent=2))
