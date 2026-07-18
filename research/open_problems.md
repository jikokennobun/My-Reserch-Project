# Open Problems

## Arithmetic G2 and Derivability Conditions

- **[Open]** Formalized G1 vs G2 separation: does there exist a provability predicate
  satisfying FedG1 ($T \vdash \neg\square\bot \to \neg\square\neg\square\bot$) but failing G2
  ($T \nvdash \neg\square\bot$)?
- **[Open]** Does $M^U$ (uniform monotonicity) imply $T \nvdash Con_T^L$?
  Equivalently, does $M^U$ imply TM?
- **[Open]** Can the conclusion $T \nvdash Con_T^S$ be obtained under $\{wM, D3\}$ alone?
- **[Open]** Construct the supremum/infimum structure of $\mathrm{ConLat}_T$: classify which
  $\varphi \in \mathrm{ConLat}_T$ are provably equivalent to $\neg\square\bot$ and which
  form an infinite descending chain between $Con_T^G$ and $Con_T^L$.
- **[Open]** Does Ros fail imply Löb fail, or vice versa?
  Known: Löb $\Rightarrow T \vdash Con_T^L$; Ros $\Rightarrow T \vdash Con_T^S$.
- **[Open]** Separate $D$ and each $D_n$ (variants of the seriality axiom $\square\varphi\to\diamond\varphi$
  restricted to $n$-boxed formulas) by explicit predicate models.
- **[Open]** Separate $P$ and each $P_n$ ($n$-boxed existence of unprovable sentences) by
  explicit predicate models.
- **[Open]** Construct a provability predicate with computationally arbitrary complex modal
  principles (i.e., $\Sigma_1$-predicates whose provability logic is undecidable/hard).
- **[Open]** Does there exist a Rosser provability predicate such that no $\diamond$-fixed point
  yields a contradiction?
- **[Open]** Axiomatize $PL_{PA}(Prov_Q)$ (provability logic of $Q$ under $PA$-interpretation).
- **[Open, Pass 69]** Arithmetic lift of the APS consistency tower:
  interpret $C_0=T$, $C_{n+1}=\boxtimes C_n$ as a genuine iterated
  consistency sequence and locate $\mathrm{Con}^{\mathrm{orb}}_n$ inside
  $ConLat_T$.
- **[Open, Pass 69]** Identify the arithmetic counterpart of `CutA3`.
  Candidate locations are $Con_T^S$, $Con_T^H$, Rosser consistency, local
  reflection, and cut-admissibility for BS16-style calculi.
- **[Open, Pass 69]** Decide whether a fully residuated, integral,
  contraction-bearing version of the detached $R_{2k}$ Rosser period models can
  preserve $p=\boxtimes p$ while still failing FG2, or whether A3/contraction
  necessarily pulls the fixed point back into the consistency orbit.

## From Shibuya Seminar 2 (2026-05-08)

- **[Open]** Does Löb imply G2 in APS? That is, is there an APS model where
  Löb holds but G2 fails (non-vacuously: $\boxtimes T\le\bot$ but $T\not\le\bot$)?
  Easy direction: G2 $\Rightarrow$ Löb has a counterexample ($\Box=\mathrm{Id}$).
  The reverse — Löb $\Rightarrow$ G2 — is open.
  Candidate arena: implication-extended APS on $[0,1]$ with Łukasiewicz implication.

- **[Open]** Does FG2 imply G2 (syntactically, not just in finite models)?
  On the 3-point linear order $L_{\mathrm{Id}}$, the separation fails;
  a syntactic proof of FG2 $\Rightarrow$ G2 may be possible.

- **[Open]** Characterize the APS models satisfying $\exists$SC but not Löb,
  and separately those satisfying Löb but not $\exists$SC.

## Core Separations

- **[Resolved]** Separate $\exists p(p=\boxtimes p)$ from $\mathrm{FG2}$:
  model M-001 (¬G2, ¬FG2, FP) and M-101 (G2, ¬FG2, FP) both witness
  $\exists p(p=\boxtimes p)\wedge\neg\mathrm{FG2}$.
- **[Resolved]** Separate FG2 from G2: M-010. Separate G2 from FG2: M-100.
- Separate $\exists p(p=\boxtimes p)$ from $\exists p(p=\neg\Box p)$:
  still open — requires models where $\boxtimes$ is primitive and
  $\neg\Box$ is defined separately.
- Characterize when $MND4$-preAPS plus a Godel-style fixed point collapses.
- **[Resolved]** Find finite nontrivial models with primitive $\boxtimes$-fixed
  points: M-001, M-011, M-101, M-111 all have syntactic $\boxtimes$-FPs.
- **[Resolved]** Find a model with G2+FG2+FP where the FP is not at $T$ or
  $\bot$: `M4-G2FG2FP` has a non-collapsed 4-element preorder with
  $\boxtimes T=p$, $\boxtimes p=p$, G2 true vacuously, FG2 true, and FP at
  the interior point $p$.
- **[Resolved]** Determine whether all-level nFG2 implies G2 or collapse in
  finite preAPS: no. M-011 has all checked and theoretically all nFG2 levels
  true, remains non-collapsed, and fails G2.
- **[Resolved (Pass 41)]** Characterize the infinite analogue of finite orbit
  stabilization. **Theorem 41a (antitone index-2 collapse):** for an antitone
  $\boxtimes$, all-level nFG2 ($\boxtimes^{k+1}T\le\boxtimes^k T$ for all $k\ge1$)
  forces $\boxtimes^2 T=\boxtimes^3 T$, so the orbit stabilizes at index $2$ and
  $p=\boxtimes^2 T$ is a syntactic fixed point — **no** well-foundedness/no-
  infinite-descent hypothesis is needed; nFG2 is self-truncating at depth $2$.
  An infinite strictly nFG2-descending orbit does not exist; an infinite orbit
  must be the $\boxtimes$-antichain regime where nFG2 fails cofinally. Proof =
  three lines (apply antitone $\boxtimes$ to nFG2$(1)$, combine with nFG2$(2)$);
  machine-guarded over all antitone maps on all $\le4$-element posets with a
  unique top (88 posets, 2618 maps, 0 counterexamples) by
  `code/scripts/check-limit-fp-and-median-tower.py`.
- **[Resolved (Pass 42), algebraic half]** Detached fixed points: by Theorem 41b
  the only antitone-compatible $\boxtimes$-fixed point near an infinite antichain
  orbit is order-incomparable to the whole orbit. **Pass 42:** the detached fixed
  point is the *algebraic shadow of a Rosser sentence*. **Theorem 42a
  (reachability/Rosser separation):** classify fixed points as *orbit-attached*
  (comparable to some iterate $\boxtimes^n T$ of the consistency tower — the
  Gödel limit, reachable when the orbit is nFG2, by 41a) vs *detached*
  (incomparable to every iterate — forced when the orbit is an antichain, by 41b,
  hence never reachable). The **Rosser gadget $R_2$** (5-element $M_3$ diamond
  $\{\bot,o_0,o_1,p,\top\}$, $T=o_0$, $\boxtimes$ a 2-cycle $o_0\leftrightarrow
  o_1$ with $\boxtimes p=p$) satisfies FP-synt $\exists q(q=\boxtimes q)$ via the
  *detached* $p$ while the Gödel orbit $\{o_0,o_1\}$ is a fixed-point-free
  antichain — settling the core separation "$\exists p(p=\boxtimes p)$ vs an
  orbit-attached Gödel point" as the detached-vs-orbit-attached distinction.
  **Corollary 42b:** in $R_2$, $T\nleq p$ (unprovable), $p\nleq\bot$
  (irrefutable) and $p$-incomparable-to-every-$\boxtimes^n T$ (not provably
  equivalent to any iterated consistency statement) are the three Rosser
  signatures, all met by the detached point and by no attached one. Machine-
  confirmed (overall PASS) by `code/scripts/check-detached-rosser-fixedpoint.py`:
  $R_2$ verified; over the $M_3$ diamond, of the 14 antitone maps with a
  non-stabilizing antichain $T$-orbit, the 2 carrying a fixed point carry **only**
  detached ones (0 attached). Report
  `artifacts/reports/detached-rosser-fixedpoint-check.json`.
- **[Resolved (Pass 43)]** Arithmetic lift of the detached fixed point (opened
  Pass 42): the
  Pass-42 result is order-theoretic. Construct (or obstruct) a provability
  predicate $\Box_R$ over a base APS-of-arithmetic with $\boxtimes=\neg\Box_R$
  such that the detached $p$ of $R_2$ is realized by a genuine Rosser sentence
  $\rho\leftrightarrow\neg\Box_R\rho$. Find the weakest derivability package
  ($D1$, $\Sigma_1$-completeness, witness-comparison) under which a
  $\boxtimes$-fixed point is *forced* detached rather than orbit-attached, and
  connect to "Does there exist a Rosser provability predicate such that no
  $\diamond$-fixed point yields a contradiction?" (Kurahashi 2021) above.
  *Resolution (Pass 43):* formalized Loeb (D3, GL) forces the Goedel fixed point
  of $x\mapsto\neg\Box x$ to equal $\mathrm{Con}=\boxtimes\bot$ (de Jongh–Sambin),
  hence orbit-attached; monotonicity (D2) alone does not. The $R_2$ detached
  geometry is realizable only by a Rosser-type predicate keeping D1 +
  $\Sigma_1$-completeness but evading Loeb. Verified by
  `artifacts/reports/rosser-arithmetic-lift-check.json`.
- **[Resolved (Pass 45), negatively]** Does the Pass-44 dividing line
  "orbit-descent $\Leftrightarrow$ $\exists$ orbit-attached fixed point" hold for
  an *arbitrary* finite preAPS, or only on $M_3$? **It is $M_3$-local.** One
  direction is a carrier-independent theorem (**Thm 45b**: $o_{k+1}=o_k$ is itself
  a reachable, attached fixed point). The converse **fails**: the order-reversing
  involution $r(x)=2m-x$ on the **odd chain** $C_{2m+1}$ (seeded at an interior
  $T$) has a perpetual non-descending $2$-cycle orbit yet an attached, self-dual
  central fixed point $p=m$ (**Thm 45c**; explicit $C_5$ witness $T=3$, orbit
  $\{3,1\}$, $p=2$). The correct refinement is the **eventual-2-cycle regime
  trichotomy** (**Cor 45d**): degenerate (descends) / antichain (Rosser, detached)
  / chain (NEW, non-descending-yet-attached, via the Bracketing Lemma 45a). The
  Pass-44 equivalence holds iff $T$'s orbit cannot reach a chain-cycle. Claims A/B
  **machine-confirmed (Pass 46)**: the survey
  `code/scripts/check-descent-attachment-general.py` was run, giving **0**
  descent$\Rightarrow$attachment violations over $>4000$ antitone maps on
  $\{M_3,C_3,\dots,C_7,N_5,M_4\}$ and positive non-descending-with-attached
  counts on every carrier with a comparable $2$-cycle. Report
  `artifacts/reports/descent-attachment-general-check.json` (overall PASS).
- **[Resolved (Pass 47)]** Chain-cycle reachability in the bottom-disciplined
  arena. The Pass-45/46 confinement conjecture is **false**: bottom discipline
  does **not** force antichain cycles. The $C_5$ reversal ($\boxtimes=r(x)=4-x$,
  $\bot=0$ genuinely least) is *itself* bottom-disciplined yet its $T=3$ orbit
  reaches the chain-cycle $\{1,3\}$ (attached midpoint $p=2$) — **Thm 47a**, and
  the $C_5$ census has **218** bottom-disciplined antitone maps with a
  $T$-reachable chain-cycle. The genuine gate is **orbit flatness + reachability**
  (**Thm 47b**: the eventual cycle is an antichain), *independent* of bottom
  discipline ($C_5$ is bottom-disciplined-$\wedge\neg$flat; sub-$\bot$-augmented
  $R_2$ is flat-$\wedge\neg$bottom-disciplined). $B_N$ satisfies the Pass-44
  equivalence because it is **flat** (front antichain + degenerate sink $s$), not
  because of bottom discipline (**Prop 47c**); a $\{\bot,U\}$ chain-cycle may
  coexist in $B_N$ but is *unreachable* from $T$, so the correct predicate is
  reachability, not existence. Machine-verified:
  `artifacts/reports/chaincycle-reachability-bottom-discipline-check.json` (PASS).
- **[Resolved (Pass 47)]** The Pass-46 **bracketing obligation** (and the
  "does bottom discipline confine the chain regimes" clause). **Thm 47d (chain
  bracketing criterion):** for a comparable eventual $2$-cycle $\{a,b\}$ ($a<b$)
  on a finite chain, $I=[a,b]$ is $\boxtimes$-invariant and $\boxtimes|_I$ is an
  orientation-reversing self-map of $I$, which has a $\boxtimes$-fixed point
  **iff $|I|$ is odd** (then the central self-dual $p=(a+b)/2$; regime (iii-a)),
  and none iff even (regime (iii-b), the $C_{2m}$ chain-gap). Confinement clause
  decided **negatively** (see Thm 47a). Machine-checked: $C_5,C_7$ bracket;
  $C_6,C_8$ are chain-gaps.
- **[Resolved (Pass 48)]** Thread (i) of the Pass-47 list, **poset bracketing.**
  For a comparable eventual $2$-cycle $\{a,b\}$ on a non-chain $\boxtimes$-invariant
  interval $I=[a,b]$, the controlling invariant is **not** $|I|$ but the cycle type
  of $\boxtimes$ on $F=\mathrm{Fix}(\boxtimes^2)\cap I$: $\tau=\boxtimes|_F$ is an
  order-reversing involution swapping $a\leftrightarrow b$, and $\boxtimes$ has a
  fixed point in $I$ iff $\tau$ does — guaranteed when $|F|$ is **odd**
  (**Thm 48a**). On a chain $F=I$, recovering Thm 47d. The naive interval-parity
  lift is **false**: the **Boolean cube** $2^{[n]}$ under complementation
  ($\boxtimes S=S^c$) is a fat even comparable $2$-cycle $\{\varnothing,[n]\}$
  ($|I|=2^n$) with **no** fixed point ("cube-gap"), while the *same* lattice $2^2$
  carries an order-reversing involution with two fixed points. Machine-verified
  `artifacts/reports/poset-bracketing-period4-check.json` (PASS).
- **[Resolved (Pass 48)]** The secondary **period-$\ge4$** clause. **Prop 48c
  (period-$k$ detachment):** if $\boxtimes p=p$ and $\{o_0,\dots,o_{k-1}\}$ ($k\ge2$)
  is a $\boxtimes$-antichain cycle, then $p$ is incomparable to every $o_i$ — the
  fixed point is **detached** (forcing $p\le o_i$ yields $o_{i+1}\le p\le o_{i+2}$,
  an antichain comparability). Hence FP-synt coexists with an eventual
  period-$2k$ antichain cycle for every $k$, the FP always detached; witness the
  **period-$4$ Rosser gadget $R_4$**, generalizing Pass-42's $R_2$ to the family
  $R_{2k}$. Generalizes Thm 41b (infinite antichain orbit) to finite cycles.
- **[Partially resolved (Pass 48)]** Thread (ii) of the Pass-47 list, **infinite
  lift of flatness.** The lifting axiom is **join-continuity of $\boxtimes$**, not
  well-foundedness of $L$: a join-continuous antitone map with ascending even orbit
  realizes its limit $2$-cycle ($\boxtimes\bigvee o_{2n}=\bigwedge o_{2n+1}$), so
  Thm 47b lifts verbatim (**Thm 48b**). The non-continuous half (the Thm-41c
  phantom limit chain-cycle) remains a construction obligation.
- **[Resolved (Pass 49)]** Pass-48 follow-up (i), **exact homological bracketing.**
  **Thm 49a (Smith bracketing criterion):** $\tau=\boxtimes|_F$ acts simplicially
  on the order complex $\Delta(F)$, which is $\mathbb F_2$-acyclic (cone with apex
  $a=\min F$); by Smith theory $|\Delta(F)|^{\tau}$ is nonempty and
  $\mathbb F_2$-acyclic with $L(\tau)=1$, and
  $$\boxtimes\text{ brackets in }I\iff |\Delta(F)|^{\tau}\text{ meets the }0\text{-skeleton}\iff\exists\ \tau\text{-invariant chain of odd cardinality.}$$
  Smith reduces "does $\tau$ fix *something*" (always, by acyclicity) to the finer
  $0$-cell gate; odd $|F|$ (Thm 48a) is the case $F=$ a single odd invariant chain.
  The **cube-gap** is re-explained homologically: for $2^{[n]}$/complementation
  $|\Delta(F)|^{\tau}$ is the lone barycenter of the flipped edge
  $\{\varnothing,[n]\}$ — nonempty/acyclic per Smith but vertex-free, hence no
  bracket. Machine-verified
  `artifacts/reports/pass49-bracketing-phantom-grouporbit-check.json` (A: PASS).
- **[Resolved (Pass 49)]** Pass-48 follow-up (ii), **explicit phantom.**
  **Construction 49b:** on the complete lattice
  $P=\{o_n\}\cup\{a^\ast=\bigvee_n o_n\}\cup\{m\}\cup\{b^\ast\}\cup\{\top\}$ with a
  doubled cover $a^\ast\prec\{m,b^\ast\}$, the antitone $\boxtimes$ with
  $\boxtimes o_{2n}\uparrow b^\ast$ and $\boxtimes a^\ast=m<b^\ast$ fails
  join-continuity at the **single** cover $a^\ast$, reinstating the Thm-41c
  phantom. **One failed cover suffices** — join-continuity (Thm 48b) cannot be
  relaxed to "continuous off a finite set." Verified on truncations $K=2..6$
  (continuity breaks only at $a^\ast$).
- **[Resolved (Pass 49)]** Pass-48 follow-up (iii), **group-cycle Rosser gadget.**
  **Thm 49d (group-orbit liberation):** $R_4/M_5$ (box$=\mathrm{id}$, refutability
  the free $\mathbb Z/4$-orbit $(o_0o_1o_2o_3)$, detached $\boxtimes p=p$) admits
  $411$ commutative full-residuated tensors with the **non-integral** unit $p$
  (equivalently $o_0$) and **$0$** integral ones (unit $=\top$ fails by the $M_n$,
  $n\ge3$, obstruction: $\top\backslash\bot$ has the non-principal fiber
  $\{b\}\cup(\text{atoms}\setminus\{a\})$). Front rigidity (Pass 34/35) forbids
  group *tensors* on a $B_N$ front but **not** a free group *orbit* carrying a
  detached fixed point on the relation-free diamond; the escape **requires** a
  non-integral unit — the freedom $B_N$'s tail-coupled $\top$-unit lacked. New
  model `code/models/examples/R4-residuated.json`; report C: PASS.
- **[Resolved (Pass 50)]** Pass-49 follow-up (i), **equivariant-Euler refinement.**
  **Thm 50a (Bredon vertex-bracket identity):** the topological
  $\chi(|\Delta(F)|^{\tau})=1$ is blind to the bracket. The vertex-counting
  invariant is $e(F^{\tau}):=\chi(\Delta(F^{\tau}))$, the Euler characteristic of
  the order complex of the *self-dual subposet* $F^{\tau}=\{x\in F:\boxtimes x=x\}$;
  the Hopf-trace split of the simplicial Lefschetz number is
  $L(\tau)=e(F^{\tau})+\Phi(\tau)=1$ ($\Phi$ = signed count of flipped invariant
  chains). $\boxtimes$ brackets iff $F^{\tau}\ne\varnothing$; on every
  comparable-2-cycle test case $e\ne0$ iff bracket, and the **cube-gap** is the
  extremal $e=0,\Phi=1$ (the lone flipped edge $\{\varnothing,[n]\}$ carries all of
  $L$). Verified `pass50-...-check.json` (A: PASS).
- **[Resolved (Pass 50)]** Pass-49 follow-up (ii), **multi-cover phantom.**
  **Constr 50b:** the fan $P_r$ of $r$ order-independent copies of the Constr-49b
  arm (shared $\bot,\top$ only) is globally antitone with discontinuities at
  exactly the $r$ limit covers $a_1^\ast,\dots,a_r^\ast$, and
  $b_{\mathrm{phantom}}(P_r)=\#\{\text{failed covers}\}=r$ — phantoms are
  ADDITIVE, a "phantom Betti number." Verified $r=1,2,3$ (each antitone,
  failed\_covers $=$ phantom\_2cycles $=r$).
- **[Resolved (Pass 50)]** Pass-49 follow-up (iii), **general-group orbit.**
  **Thm 50d (front-cardinality decoupling):** $M_{|G|+1}$ with a free $G$-orbit
  front $+$ detached $\boxtimes p=p$ admits $R(n)$ commutative full-residuated
  tensors with **non-integral** unit $p$ and $0$ integral ones for all $n=|G|\ge3$;
  $R(3)=56$, $R(4)=411$ (reproduces Pass 49), and $R(n)\ge1$ for ALL $n$ via the
  explicit witness family ($o_0$ absorbing, $o_i\otimes o_j=\top$ for $i,j\ge1$,
  unit $p$). The commutative tensor sees only $|G|=n$, **never the group law** —
  abelian vs non-abelian is residuation-invisible (free $S_3$ orbit verified
  antitone with detached $p$). The group lives in the refutability ORBIT, the
  tensor in the front CARDINALITY (decoupling). Verified (C: PASS).
- **[Resolved (Pass 51)]** Pass-50 follow-up (i), **completeness of $e(F^{\tau})$.**
  **Thm 51a (completeness/deflation):** for *any* antitone $\boxtimes$,
  $\mathrm{Fix}(\boxtimes)$ is an **antichain** (Lemma 51a: $p\le q$ both fixed
  $\Rightarrow q=\boxtimes q\le\boxtimes p=p$), so $\Delta(F^{\tau})$ is discrete
  and $e(F^{\tau})=\chi(\Delta(F^{\tau}))=|F^{\tau}|$ identically. Hence $e$ IS a
  complete bracket invariant — $e=0\iff F^{\tau}=\varnothing\iff$ no bracket — but
  *tautologically*: the configuration "$e=0$ with $F^{\tau}\ne\varnothing$" is
  impossible, and the hoped-for order-complex-circle pathology is unrealizable as a
  fixed-vertex set (the 6-crown has $\chi=0$ but is not an antichain). All
  non-vertex homological content is carried by the flipped term
  $\Phi(\tau)=1-|F^{\tau}|$. Verified `pass51-...-check.json` (A: PASS; $0$
  antichain/cardinality/$e0$ violations over all antitone maps on posets of size
  $\le5$).
- **[Resolved (Pass 51)]** Pass-50 follow-up (ii), **phantom as cohomology.**
  **Thm 51b:** $b_{\mathrm{phantom}}(P_r)=\dim_{\mathbb F}H^1(\mathrm{Ob}^\bullet
  (P_r))$ where $\mathrm{Ob}^\bullet(P_r)=[\,0\to C^1\to0\,]$, $C^1=\mathbb
  F^{\{\text{failed covers}\}}$, $C^0=0$ (infinitary rigidity). The phantom is the
  $\varprojlim^1$ of the image tower $(\boxtimes o^i_n)_n$ (failure of $\boxtimes$
  to commute with the directed join), additive over independent arms since
  $\varprojlim^1$ commutes with finite direct sums, giving $\dim H^1=r$. *Open
  obligations:* the integral $\varprojlim^1$ must be shown nonzero (field-coefficient
  $\varprojlim^1$ of finite-dimensional towers vanishes), and $C^0=0$ holds only in
  the completed lattice (every finite truncation is gap-removable). Verified at the
  finite level (B: PASS, $r=1,2,3$).
- **[Resolved (Pass 51)]** Pass-50 follow-up (iii), **arithmetic lift of the
  non-integral unit.** **Thm 51c:** integral unit $1=\top$ $\iff$ the
  $\boxtimes$-fixed point is orbit-attached ($\phi=\boxtimes\bot$) $\iff$ Löb (de
  Jongh–Sambin); non-integral unit $1\ne\top$ $\iff$ detached $\iff$ Rosser
  predicate evading Löb (Guaspari–Solovay 1979; Kurahashi 2021). The attached
  3-chain Gödel model admits an integral-unit ($\top$) full residuated tensor; the
  detached $R_2/M_3$ admits $0$ integral-unit tensors and only non-integral units
  $\{o_0,o_1,p\}$. "Non-integral unit" is the algebraic shadow of "Rosser evades
  Löb". *Open obligation:* promote the dictionary to a functor $L_{(-)}$ from
  derivability packages to residuated APS. Verified (C: PASS).
- **[Resolved (Pass 52)]** Pass-51 follow-up (i), **the flipped invariant
  $\Phi(\tau)$.** **Thm 52a:** $\Phi(\tau)=\sum_{d\ge1}s(d)N_d=1-|F^{\tau}|$, a
  signed count of $\tau$-invariant $d$-chains with period-4 sign
  $s(d)=+\,+\,-\,-$ ($s(d)=(-1)^d(-1)^{d(d+1)/2}$). **Thm 52b (extremal
  dichotomy):** $\sup\Phi=+1$, attained exactly on fixed-point-free $\tau$ (cube
  $2^{[n]}$ / $C_4$); $\inf\Phi=-\infty$, the fixed-antichain fan
  $F_m=(\hat0<a_1,\dots,a_m<\hat1)$ realizing $\Phi=1-m$. **Thm 52c:**
  $\Phi(\tau)=\chi(|\Delta(F)|^{\tau})-\chi(\Delta(F^{\tau}))$, the gap between the
  geometric (Smith-acyclic, $=1$) and combinatorial (vertex, $=|F^{\tau}|$)
  fixed-point Euler characteristics. Machine-verified
  (`pass52-flipped-invariant-check.json`, PASS) over cubes $2^{[1..3]}$, fans
  $m=1..5$, $C_4$, $3$/$4$-chains. *Open obligation:* the Thm-52c cell-level chain
  map (flipped-triangle barycenters $\to$ $\mathrm{sd}(\Delta)$ fixed subcomplex).
- **[Resolved (Pass 53)]** Pass-52 follow-ups (ii) and (iii).
  **(ii) Integral $\varprojlim^1$ nonvanishing — Thm 53a (the $2$-adic phantom).**
  The Pass-50/51 phantom Betti number $b_{\mathrm{phantom}}=r$ is a
  *field-coefficient shadow*: a tower of finite-dimensional vector spaces is
  Mittag-Leffler, so $\varprojlim^1=0$ over any field and $r$ is merely the rank of
  the finitary cochain $C^1=\mathbb F^{\{\text{failed covers}\}}$. The genuine
  derived obstruction lives at integer coefficients with the non-Mittag-Leffler
  tower $\mathbb Z\xleftarrow{\times2}\mathbb Z\xleftarrow{\times2}\cdots$
  (image filtration $2^k\mathbb Z$, index $2^k\uparrow\infty$): the SES of towers
  $0\to(\mathbb Z,\times2)\to(\mathbb Z,\mathrm{id})\to(\mathbb Z/2^n)\to0$
  gives $0\to0\to\mathbb Z\to\widehat{\mathbb Z}_2\to\varprojlim^1(\mathbb
  Z,\times2)\to0$, hence
  $$\varprojlim{}^1(\mathbb Z,\times2)=\widehat{\mathbb Z}_2/\mathbb Z,$$
  uncountable and divisible — invisible to every field and to every finitely
  supported probe (each $b\in\bigoplus\mathbb Z$ lifts, e.g. $(1,1,\dots)\mapsto
  (-1,-1,\dots)$). The phantom is exactly an uncountable $2$-adic residue.
  **(iii) Löb/Rosser functoriality — Thm 53b.** The functor
  $L_{(-)}:\mathbf{Deriv}\to\mathbf{resAPS}$ sends a derivability package to its
  Lindenbaum residuated APS ($\boxtimes=\neg\Box$, unit $=$ chosen
  $\boxtimes$-fixed point). On the Löb subcategory $\mathbf{GL}$ it is canonical
  (de Jongh–Sambin fixed-point uniqueness) with $e=\top\iff$ Löb and essential
  image exactly the integral-unit subcategory $\mathbf{resAPS}_{\mathrm{int}}$;
  Rosser packages (Guaspari–Solovay 1979; Kurahashi 2021) land in the non-integral
  complement as a non-canonical unit-torsor (Rosser fixed points are not unique).
  *Slogan:* Löb $=$ fixed-point uniqueness $=$ unit integrality $=$ canonical
  functoriality. Machine-verified
  `artifacts/reports/pass53-integral-lim1-loeb-rosser-functor-check.json` (PASS):
  $\mathbb Z$-image indices $2,4,\dots,256$ (non-ML), $\mathbb F_2/\mathbb F_3$
  images stable (ML); $3$-chain has $2$ integral-unit tensors, $M_3$ has $0$
  integral-unit and $13$ each non-integral-unit tensors.
- **[Resolved (Pass 54), obligation (i)] / [Partially resolved (Pass 54),
  obligation (ii)]** Two proof obligations from Thm 53a/53b.
  **(i) RESOLVED (Pass 54):** the honest carrier is the negative cone $\mathbb Z^-$
  ($x\otimes y=x+y$, $x\backslash y=\min(0,y-x)$, $e=0=\top$) with the $m$-fold
  dilation $d_m(x)=mx$, an injective non-surjective **residuated-lattice
  endomorphism** (image $m\mathbb Z^-$, cover-fiber multiplicity $m$); the inverse
  system $(\mathbb Z^-\xleftarrow{d_m}\mathbb Z^-\xleftarrow{d_m}\cdots)$ has
  top-cover coefficient tower $(\mathbb Z,\times m)$ and derived limit
  $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$ (**Constr 54a, Thm 54b**). The
  prime $2$ is **not** forced: the phantom is **radical-invariant**,
  $\widehat{\mathbb Z}_m=\prod_{p\mid m}\mathbb Z_p$ depending only on
  $\mathrm{rad}(m)$, so $\times2\sim\times4\sim\times8$ share $\widehat{\mathbb Z}_2
  /\mathbb Z$ as pro-objects (the towers themselves non-isomorphic — inequivalent
  dilations, one phantom) and $\times6\sim\times12$ give $(\mathbb Z_2\times\mathbb
  Z_3)/\mathbb Z$; $m=1$ is the phantom-free boundary. The "$m$-adic arithmetic the
  refutability orbit must carry" is exactly $\widehat{\mathbb Z}_m$ acting by
  dilation on the cover fiber (**Cor 54c**). Machine-verified
  `artifacts/reports/pass54-honest-residuated-2adic-phantom-check.json` (PASS).
  **(ii) PARTIALLY RESOLVED (Pass 54):** fullness of $L_{(-)}|_{\mathbf{GL}}$
  sketched via de Jongh–Sambin term-definability of $\boxtimes$-fixed points
  (homomorphisms lift to interpretation translations), giving an equivalence
  $\mathbf{GL}\simeq\mathbf{resAPS}_{\mathrm{int}}$; the Rosser unit-torsor
  identified with $H^1(\mathbf{Deriv}\setminus\mathbf{GL};\mathrm{Aut(unit)})$ as the
  $\check{C}$ech $H^1=\varprojlim^1$ of the witness-comparison choice tower — the
  **same** derived functor as the phantom (Guaspari–Solovay non-uniqueness). Left
  open: pin $\mathbf{Deriv}$-morphisms to residuated maps and write the choice
  sheaf out.
- **[Resolved (Pass 55)]** _(was [New (Pass 54)])_ Realize the antitone refutability
  $\boxtimes$ on the completed dilation solenoid explicitly. **Carrier correction:**
  the *inverse* limit $\varprojlim_n(\mathbb Z^-,d_m)$ is the **trivial one-point
  lattice** ($x_0=m^nx_n\Rightarrow x_0=0$); the honest object is the directed
  **colimit** $C_m=\varinjlim(\mathbb Z^-,d_m)=\mathbb Z[1/m]^-$ (negative cone of the
  $m$-adic localization), an integral residuated lattice whose MacNeille completion is
  the arena — *literally* the classical $m$-adic solenoid ($\widehat{C_m}=\mathbb S_m=
  (\mathbb R\times\widehat{\mathbb Z}_m)/\mathbb Z$). **Constr 55a** lifts Construction
  49b verbatim (rungs $a_n=-1/m^n\uparrow a^\ast=0^-$, doubled cover $a^\ast\prec\{c,
  b^\ast\}\prec\top$, $\boxtimes_m\top=a_0$, $\boxtimes_m(a_{2k})\uparrow b^\ast$,
  $\boxtimes_m(a^\ast)=c$); the ONE new ingredient vs 49b is $m$-adic rung dilation
  (cover fiber $m$, not $1$), upgrading 49b's rank-$1$ field-phantom ($\varprojlim^1=0$,
  a shadow) to the genuine non-ML $(\mathbb Z,\times m)$, $\varprojlim^1=\widehat{\mathbb
  Z}_m/\mathbb Z$ (**Thm 55b**: the phantom is $\boxtimes_m$'s OWN derived limit, join-
  continuity failing at the lone cover $a^\ast$ with failure module $(\mathbb Z,\times
  m)$). **Thm 55c (ML $=$ nFG2 dichotomy):** Mittag–Leffler $\iff$ orbit stabilizes
  $\iff$ all-level nFG2 (index-$2$, Thm 41a) $\iff$ $\varprojlim^1=0$; all four FAIL for
  $m\ge2$, so $\boxtimes_m$ is a perpetual non-stabilizing orbit ($\neg$FG2) while every
  finite truncation satisfies all four (phantom is strictly **liman**); G2 holds
  **vacuously** ($\boxtimes_m T=a_0\not\le\bot$) — solenoid in $G2\wedge\neg$FG2.
  **Thm 55d (fusion):** finite truncations integral-unit (Löb), but the fixed-point/unit
  tower is the SAME $(\mathbb Z,\times m)$ with $\varprojlim=0$ (detached limit FP $\Rightarrow$
  non-integral $\Rightarrow$ Rosser) and $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$
  (unit-torsor) — so a residuated tensor forces a Rosser unit and Pass-54 obligations
  (1) [phantom] and (2) [Rosser torsor $=H^1$] are ONE statement (join-continuity-failure
  module $=$ Löb$\to$Rosser gluing obstruction). *Slogan: finitely Löb, limanly Rosser.*
  Machine-verified `artifacts/reports/pass55-solenoid-boxtimes-lim1-rosser-fusion-check.json` (PASS).
- **[Resolved (Pass 56)]** _(was [New (Pass 55)])_ Two residues of Constr 55a, both
  closed by a **residuation/Rosser dichotomy**. **(i) Residuation survival — Thm 56a.**
  The completed arena $\overline{L}^{(m)}$ (chain $C_m=\mathbb Z[1/m]^-$ $+$ the doubled
  cover $a^\ast\prec\{c,b^\ast\}\prec\top$) is a complete **distributive** lattice and a
  **frame** (binary meet distributes over the cover join $a^\ast=\bigvee_n a_n$), hence a
  complete **Heyting** algebra: it *does* residuate, but under $\otimes=\wedge$ with the
  **integral** unit $\top$ (Löb regime) — Thm 56a.1. The **dilation monoid** $\otimes=+$
  (unit $e=a^\ast$, the predicted non-integral Rosser unit, $c,b^\ast$ as positive
  infinitesimals above $0=a^\ast$) does **not** extend to a residual: $x\mapsto x\otimes c$
  fails join-preservation at the lone cover, $\bigvee_n(a_n\otimes c)=a^\ast<c=a^\ast\otimes
  c$, so the minimal failing fiber $c\backslash a^\ast=\{a_n\}_n$ is **non-principal**
  (sup $a^\ast$ not attained) — exactly the Pass-49 $M_n$ ($n\ge3$) non-principal-fiber
  obstruction, now at a *non-attained* cover — Thm 56a.2. Every finite truncation
  $\overline{L}^{(m)}_K$ residuates under **both** tensors ($a^\ast=a_K$ is the chain
  maximum, $c\backslash a^\ast=a_{K-1}$ principal); residuation of the dilation monoid is
  *finitely-true, limanly-false*, sharing its obstruction (join-discontinuity at the cover)
  with the phantom (Thm 55b) and nFG2/ML failure (Thm 55c) — Thm 56a.3. **So residuation
  and the Rosser unit are mutually exclusive in the completion: finitely both, limanly only
  a preAPS.** **(ii) Explicit Čech complex — Thm 56b.** The dilation cover's even/odd
  half-telescope cover $\mathcal U=\{U_0,U_1\}$ has interval nerve, so its
  $\check{\mathrm C}$ech complex on $\underline{\mathbb Z}_{\times m}$ ($\mathrm{stalk}=
  \mathbb Z=\mathrm{Aut(unit)}$, restriction $\times m$) is the **two-term**
  $0\to\prod_n\mathbb Z\xrightarrow{\ \delta=\mathrm{id}-m\cdot\mathrm{sh}\ }\prod_n\mathbb
  Z\to0$ with $\check H^0=\ker\delta=\varprojlim=0$ (detached limit fixed point) and
  $\check H^1=\operatorname{coker}\delta=\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$;
  only $H^0,H^1$ occur, so Thm-55d's $H^1=\varprojlim^1$ is a literal cochain identity, the
  Rosser unit-torsor class $=[(1,0,0,\dots)]\in\operatorname{coker}\delta$ (closes Pass-54
  obligation (2) at the cochain level). Machine-verified
  `artifacts/reports/pass56-solenoid-residuation-survival-cech-check.json` (PASS).
- **[Resolved (Pass 57)]** _(was [New (Pass 56)])_ Both residues closed.
  **(i) Carrier-free cancellativity no-go — Lemma 57a / Cor 57a$'$.** In a complete
  residuated lattice ($\otimes$ preserves all joins in each argument) whose unit
  $e=\bigvee_n a_n$ is the non-attained sup of a strictly ascending chain ($a_n<e$),
  if there is a **completely join-irreducible** $c>e$ with $a_n\otimes c<c$
  (cancellativity), then $c=e\otimes c=\bigvee_n(a_n\otimes c)$ with every summand
  $<c$ forces (by join-irreducibility) some $a_n\otimes c=c$ — contradiction. Hence
  **no** complete residuated tensor with a Rosser (sup-of-chain) unit admits a
  join-irreducible cover; Thm 56a.2 becomes absolute (Cor 57a$'$: *every* $\otimes$
  fails on $\overline{L}^{(m)}$, not merely the additive one; residuation forces the
  integral $\top$/Löb unit). **Quantale escape audited — Thm 57c (Phantom $\veebar$
  Quantale):** the ideal/downset (Day-convolution) completion $\mathcal D(C_m)$ IS a
  unital residuated quantale with an additive unit, but it de-singularizes the cover
  ($\bigvee_n{\downarrow}a_n\subsetneq{\downarrow}a^\ast$, now principal), voiding
  Lemma-57a's hypothesis and killing the phantom ($\varprojlim^1=0$, ML). So across
  completions: MacNeille $=\{$phantom, $\neg$additive-residual$\}$, Ideal $=\{$
  additive-residual, $\neg$phantom$\}$ — exclusive or. **(ii) Torsor-level
  identification — Thm 57b (modulo naturality).** The Čech cochain map
  $\Theta:\mathrm{Ros}_m\to\operatorname{coker}\delta$ is $G_m$-equivariant and
  bijective, giving an iso of **torsors** $\mathrm{Ros}_m\cong\widehat{\mathbb Z}_m/
  \mathbb Z$ (not just abelian groups). Machine-verified
  `artifacts/reports/pass57-cancellativity-nogo-quantale-escape-check.json` (PASS):
  L (no-go core $K$-independent), Q (Day-convolution unital quantale), R (residuated,
  adjunction over all triples), D (cover splits, ML, $\varprojlim^1=0$), M (MacNeille
  non-ML, no additive residual), X (exclusive-or).
- **[Resolved (Pass 58), (i)] / [Partially resolved (Pass 58), (ii)]** _(was
  [New (Pass 57)])_ Two residues of Pass 57.
  **(i) RESOLVED (Pass 58) — the non-cancellative edge.** Lemma 57a does **not**
  survive without strictness. The **absorbing Rosser cap** $W=(a_0=\bot<a_1<\cdots<
  e<c<\top)$, $e=\bigvee_n a_n$ non-attained, unit $e$, tensor $x\otimes y=\bot$ if
  $\bot\in\{x,y\}$ / $\min(x,y)$ below $e$ / $\max(x,y)$ once a large operand $\ge c$
  appears, is an explicit **complete commutative residuated lattice** with a
  completely join-irreducible cover $c\succ e$ and **cofinal absorption** $a_n\otimes
  c=c$ ($n\ge1$); the Lemma-57a identity $c=\bigvee_n(a_n\otimes c)$ holds with every
  summand $=c$, so no contradiction — **strictness/cancellativity is essential**
  (**Thm 58a**). The escape's price (**Thm 58b, Phantom trichotomy**): the cover fiber
  $c\backslash e=\bot$ collapses to principal, the image tower is constant
  (Mittag–Leffler), $\varprojlim^1=0$ — the Rosser torsor degenerates (absorbing $=$
  non-free witness-comparison action). The three completions of a Rosser unit realize
  the three pairwise choices among $\{$residuation, join-irreducible cover, phantom$\}$:
  MacNeille $=$ (cover, phantom; $\neg$residual), Ideal/quantale $=$ (residual,
  phantom-free; $\neg$cover), absorbing cap $W=$ (residual, cover; $\neg$phantom) —
  **any two, never all three.**
  **(ii) PARTIALLY RESOLVED (Pass 58) — naturality of $\Theta$.** On the radical-graded
  subcategory $\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ (morphisms $=$
  $\Box$-morphisms that are residuated cover-filtration maps; arrows graded by
  $\mathrm{rad}(m)\mid\mathrm{rad}(m')$, the exact condition for a dilation-tower map
  $(\mathbb Z,\times m)\to(\mathbb Z,\times m')$ to exist), $\Theta:\mathrm{Ros}_{(-)}
  \Rightarrow\varprojlim^1(-)$ is a natural transformation by snake-lemma naturality of
  $\delta$ (**Prop 58c**); off it (rad-incompatible moduli) there is no tower morphism.
  Machine-verified `artifacts/reports/pass58-absorbing-rosser-cover-nogo-edge-check.json`
  (PASS).
- **[Resolved (Pass 59), (i)]** _(was [New (Pass 58)] (i))_ **The non-idempotent
  absorbing cover (intermediate regime).** The mixed regime EXISTS but is
  **phantom-flat**. **Thm 59a (no partial phantom):** for a complete residuated
  tensor with non-attained sup-of-chain unit $e=\bigvee a_n$ and join-irreducible
  cover $c\succ e$, the absorption depth $d=\inf\{n:a_n\otimes c=c\}$ is finite on the
  whole residuated regime (Cor 57a$'$ forbids $d=\infty$), the fiber tower
  $(a_n\otimes c)_n$ is non-decreasing and eventually constant $=c$, hence
  Mittag–Leffler, hence $\varprojlim^1=0$ — the phantom is **genuinely $0$**, not
  finitely supported (a $\varprojlim^1$ class is a tail/pro-invariant; finite support
  carries no content). The idempotence defect $\iota=[c\otimes c\ne c]$ is
  **$\varprojlim^1$-invisible**: it localizes at the *compact* cover above $c$, not at
  the non-compact cover $e\prec c$ where the phantom is pinned. **Cor 59b (trichotomy
  is sharp):** along the absorption axis $\varprojlim^1\in\{0,\widehat{\mathbb Z}_m/
  \mathbb Z\}$ only — by **Gray's dichotomy** ($\varprojlim^1$ of a countable tower is
  $0$ or $2^{\aleph_0}$; Gray 1966, McGibbon–Steiner 1995) no finite-rank intermediate
  exists, so the Pass-58 "any two of $\{$residuation, cover, phantom$\}$, never all
  three" is *not* a spectrum boundary; $(d,\iota)$ are genuine but phantom-flat moduli,
  the phantom jumping $0\to2^{\aleph_0}$ only at the non-residuated wall $d=\infty$.
  **Prop 59c:** depth $=$ nFG2 stabilization index $=$ ML $=$ phantom-free (unifies
  41a/55c/58b). Machine-verified `pass59-...-check.json` (28 models $W_{K;d,\delta}$,
  all residuated; finite-depth ML, dilation non-ML; PASS).
- **[Resolved (Pass 60)]** _(was [New (Pass 58)] (ii))_
  **Rad-obstruction completeness (Prop 58c residue) — the last functorial gap of
  $L_{(-)}$.** **Thm 60a (carrier criterion):** a residuated cover-filtration map of
  dilation-solenoid arenas $C_m\to C_{m'}$ ($C_m=\mathbb Z[1/m]^-$, Pass 55) exists
  $\iff$ $\mathbb Z[1/m]\subseteq\mathbb Z[1/m']$ $\iff$ $\mathrm{rad}(m)\mid
  \mathrm{rad}(m')$ — the rad-grading is **forced by the carrier**, and
  $\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ is (up to grading) the squarefree
  divisibility lattice $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$. **Thm 60b
  (sole obstruction):** wherever an arrow exists the Čech-cochain naturality square for
  $\Theta:\mathrm{Ros}_{(-)}\Rightarrow\varprojlim^1(-)$ commutes (snake-lemma
  naturality of $\delta$, Prop 58c); off the rad-relation the hom-set is empty, so
  rad-divisibility is the *unique* obstruction and $\Theta$ is a natural iso of the
  phantom sheaf $S\mapsto(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ with the Rosser-torsor
  presheaf on the prime spectrum. **Cor 60c:** $m=6,m'=10$ rad-incomparable — no arrow,
  only a common lower bound $C_2$ (shared $2$-adic ghost $\mathbb Z_2/\mathbb Z$).
  Machine-verified `artifacts/reports/pass60-rad-obstruction-naturality-theta-check.json` (PASS).
- **[Resolved (Pass 60)]** _(was [New (Pass 59)])_ **Set-theoretic frontier of the
  no-partial-phantom theorem.** **Thm 60d:** Gray's $0$-or-$2^{\aleph_0}$ dichotomy is
  strictly an $\omega$-cofinality phenomenon and does **not** lift. An $\omega_1$-cofinal
  long cover makes the cover-fiber inverse system pro-isomorphic to the Mardešić–Prasolov
  strong-homology system, whose $\varprojlim^1$ is **nonzero under CH** (Mardešić–Prasolov
  1988) and **zero under PFA** (Dow–Simon–Vaughan 1989); hence "a genuinely
  $\aleph_1$-engendered intermediate phantom exists" is **independent of ZFC** —
  present under CH, killed by $\mathrm{MA}_{\aleph_1}$/PFA. The countable phantom
  $\widehat{\mathbb Z}_m/\mathbb Z$ is ZFC-absolute; the $\omega_1$-phantom is a
  forcing-axiom/Suslin-line invariant.
- **[Resolved (Pass 61), (i)] / [Partially resolved (Pass 61), (ii)]** _(was
  [New (Pass 60)])_ **Sheaf descent for the phantom on $\mathrm{Spec}$, and the exact
  cardinal threshold.**
  **(i) RESOLVED (Pass 61), as a correction.** The phantom presheaf $P(S)=(\prod_{p\in S}
  \mathbb Z_p)/\mathbb Z$ **does not** satisfy descent, and the Rosser-torsor presheaf is
  **not** its sheafification. Resolving $P$ into the presheaf SES $0\to\underline{\mathbb Z}
  \xrightarrow{\Delta}\mathcal F\to P\to0$ ($\mathcal F(S)=\prod_{p\in S}\mathbb Z_p$,
  restriction $=$ projection): $\mathcal F$ is a flasque sheaf but $\underline{\mathbb Z}$
  is non-separated (sheafification $\mathbb Z^{S}$, defect $\mathbb Z^{S}/\Delta\mathbb Z
  \cong\mathbb Z^{|S|-1}$), so **Thm 61a**: $P(S)\to\prod_pP(\{p\})$ is onto with kernel
  $\mathbb Z^{|S|-1}\ne0$ (non-separated), and the **sheafification is the stalkwise sheaf**
  $P^{\#}=L$, $L(S)=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)$. **Thm 61b**: the Rosser torsor
  $\widehat{\mathbb Z}_m/\mathbb Z=P(S)$ is the **failure of descent** (the kernel of
  presheaf$\to$sheafification), split into a horizontal free $\mathbb Z^{|S|-1}=
  \check H^1(\underline{\mathbb Z})$ over the prime cover and a vertical $\varprojlim^1=
  \widehat{\mathbb Z}_p/\mathbb Z$ (dilation tower) per stalk; sheafification *kills* the
  Rosser content. The Pass-60 slogan is correct only after **dualizing**: $P$ is a flabby
  *cosheaf*, Löb $=$ sheaf $L$, Rosser $=$ cosheaf/global ghost.
  **(ii) PARTIALLY RESOLVED (Pass 61) — Thm 61c.** $\mathfrak b=\aleph_1\Rightarrow
  \varprojlim^1\mathbf A_{\omega_1}\ne0$ (weaker than CH; Mardešić–Prasolov 1988) and
  $\mathrm{MA}_{\aleph_1}\Rightarrow0$ (Dow–Simon–Vaughan 1989, forcing $\mathfrak b=\aleph_2$),
  so the threshold is **bracketed** $[\mathfrak b=\aleph_1\Rightarrow\ne0]$,
  $[\mathrm{MA}_{\aleph_1}\Rightarrow0]$ but is **not** a single named cardinal
  characteristic (a genuinely higher additivity-of-ideal invariant, Suslin-sensitive
  below $\mathrm{MA}_{\aleph_1}$); an $\aleph_2$-cofinal cover yields **not** a clean
  $0/\aleph_1/2^{\aleph_0}$ trichotomy but a *sequence* of higher-$\varprojlim^s$ ($s\ge2$)
  independence statements. Machine-verified
  `artifacts/reports/pass61-phantom-sheaf-descent-check.json` (PASS).
- **[Resolved (Pass 62), (i) and (ii); (iii) carried [Open]]** _(was [New (Pass 61)])_
  **The Löb–Rosser bicomplex and the cosheafification of $P$.**
  **(i) RESOLVED (Pass 62).** **Thm 62a (the bicomplex):** the double complex with vertical
  $=$ per-prime Milnor $\varprojlim$-cochain of $(\mathbb Z,\times p)$ and horizontal $=$
  augmented reduced Čech of $\underline{\mathbb Z}$ over the singleton prime cover has
  $H^1(\mathrm{Tot})=\widehat{\mathbb Z}_S/\mathbb Z=P(S)$ and both spectral sequences
  degenerate at $E_2$ to the two cells $E_2^{1,0}=\mathbb Z^{|S|-1}$ (Rosser/horizontal),
  $E_2^{0,1}=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)=L(S)$ (Löb/vertical), all else $0$; the
  Löb/Rosser dictionary **is** the $E_2$ page. **Thm 62b (no $d_2$, a non-split extension):**
  since $E_2^{2,0}=0$ there is no room for any $d_r$ ($r\ge2$), so $E_2=E_\infty$ and the
  "mixed Löb–Rosser class" is the **filtration extension**
  $0\to\mathbb Z^{|S|-1}\to\widehat{\mathbb Z}_S/\mathbb Z\to\prod_p(\mathbb Z_p/\mathbb Z)\to0$,
  **non-split** for $|S|\ge2$ (a retraction would restrict to $\mathrm{Hom}(\mathbb Z_p,\mathbb
  Z)=0$ on each stalk, killing the integer points $e_p$ that generate the quotient) — class
  $\epsilon_S\in\mathrm{Ext}^1_{\mathbb Z}(L(S),\mathbb Z^{|S|-1})\ne0$, a connecting $\partial$,
  not a page $d_2$ (a genuine $d_2$ reappears only after unabridging $\mathbb Z_p$ into its
  $\mathbb Z/p^n$-tower). **(ii) RESOLVED (Pass 62), as a CORRECTION of the Pass-61 slogan.**
  **Thm 62c:** on the singleton (discrete) prime site the cosheafification $\check P(S)=
  \bigoplus_{p\in S}(\mathbb Z_p/\mathbb Z)=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)=L(S)$ for finite
  $S$ ($\bigoplus=\prod$), so **sheafification and cosheafification coincide**, both $=L$; the
  global $\widehat{\mathbb Z}_S/\mathbb Z$ is **neither** — it is irreducibly presheaf-level, the
  descent defect $\ker(P\to L)=\mathbb Z^{|S|-1}$. "Rosser $=$ cosheaf" is **false on the discrete
  site** (too disconnected for $\mathbf{Sh}\ne\mathbf{coSh}$); the slogan needs the coarser
  Zariski/cofinite topology on $\mathrm{Spec}\,\mathbb Z$. Machine-verified
  `artifacts/reports/pass62-loeb-rosser-bicomplex-mixed-class-check.json` (PASS). **(iii) carried
  [Open]:** the exact $\aleph_1$-threshold of Thm 61c (strictly between $\mathfrak b=\aleph_1$ and
  $\mathrm{MA}_{\aleph_1}$; Suslin-tree or $\mathrm{add}(\mathcal M)$ invariant?) is untouched
  this pass.
- **[Resolved (Pass 63)]** _(was [New (Pass 62)])_ **The Zariski cosheaf, the unabridged $d_2$,
  and the explicit $\mathrm{Ext}^1$.**
  **(i) RESOLVED — Thm 63a (Zariski relocation; "$j_!$-cosheaf" form).** On the connected
  generic-point subspace $X=\{\eta\}\cup\{(p):p\in S\}$ (particular-point Zariski topology), the
  cover $\mathcal U=\{U_p=\{\eta,(p)\}\}$ has *all* nonempty overlaps $=\{\eta\}$, so its nerve is
  the **full simplex** $\Delta^{s-1}$ (contractible). Thus (1) the constant sheaf
  $\underline{\mathbb Z}$ is now a genuine sheaf and $\check H^1(\mathcal U,\underline{\mathbb Z})
  =0$ — connectivity **annihilates** the discrete-site horizontal defect $\mathbb Z^{s-1}=
  \check H^0_{\mathrm{red}}$; (2) the Rosser relations **relocate one degree up** to
  $H^1(X,j_!\underline{\mathbb Z})=\mathbb Z^s/\Delta\mathbb Z=\mathbb Z^{s-1}\ne0$ (extension by
  zero from the open generic point $j:\{\eta\}\hookrightarrow X$, via
  $0\to j_!\mathbb Z\to\mathbb Z_X\to i_*\mathbb Z_Z\to0$). Since $j_!$ is the left-adjoint
  (compact-support/cosheaf) extension, **"Rosser $=$ cosheaf" finally holds, in the precise form
  Rosser $=H^1$ of $j_!$ supported at the generic point** (Löb $=$ stalkwise sheaf $L(S)$) — a
  *third correction*: the naive cover-cosheafification still returns $L(S)$ (overlaps carry the
  skyscraper $0$), so the rescuing functor is specifically $j_!$, not $\check{(-)}$ over
  $\mathcal U$.
  **(ii) RESOLVED — Thm 63b (unabridged $d_2$).** Resolving each $\mathbb Z_p=\varprojlim_n
  \mathbb Z/p^n$ by its $\mathbb Z/p^n$-tower opens a third column $E_2^{2,0}=\operatorname{coker}
  (\Delta:\mathbb Z\to\mathbb Z^s)=\mathbb Z^{s-1}$, turning the hidden Pass-62 $E_\infty$
  extension into a genuine page differential $d_2:E_2^{0,1}=L(S)\to E_2^{2,0}=\mathbb Z^{s-1}$,
  $(x_p)\mapsto[(x_p-x_{p_0})_{p\ne p_0}]$ — the **common-integer-lift obstruction** (image rank
  $s-1$). $\epsilon_S=\partial$ and the $d_2$ are *one datum in two resolutions*.
  **(iii) RESOLVED — Thm 63c ($\mathrm{Ext}^1$ ghost line; arithmetic $\succ$ cardinal).**
  $\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=0$ makes $\delta:\mathbb Z\hookrightarrow\mathrm{Ext}^1
  (\mathbb Z_p/\mathbb Z,\mathbb Z)$ injective, $\delta(1)=\epsilon_p$ the **infinite-order**
  ghost class (lacunary witness $u=\sum_k p^{k!}$) generating a canonical $\mathbb Z$-line inside
  the uncountable $\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb Z)$ (an extension of the
  continuum-dimensional $\mathrm{Ext}^1(\mathbb Z_p,\mathbb Z)$ by $\mathbb Z$). So $\epsilon_p$
  is a generator only of the *arithmetic line*, not the whole group. $\epsilon_S\in\bigoplus_{p\in
  S}\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb Z)^{s-1}$ is nonzero of infinite order for
  $s\ge2$; the *target* rank $s-1$ is a **cardinal** invariant ($|S|$ only), but $\epsilon_S$
  lives on the pairwise non-isomorphic $\mathbb Z_p/\mathbb Z$ (torsion subgroup
  $\bigoplus_{q\ne p}\mathbb Z(q^\infty)$ uniquely omitting the $p$-Prüfer), so it is a genuinely
  **arithmetic** invariant of the prime set: $\epsilon_{\{2,3\}}\ne\epsilon_{\{2,5\}}$ under any
  prime-respecting identification. Machine-verified
  `artifacts/reports/pass63-zariski-cosheaf-unabridged-d2-ext1-check.json` (PASS).
- **[Resolved (Pass 64), (i) and (ii); (iii) carried [Open]]** _(was [New (Pass 63)])_
  **The recollement / six-functor packaging, and the prime-spectrum motive.**
  **(i) RESOLVED — Thm 64a/64b (the recollement).** On the finite generic-point model
  $X=\{\eta\}\sqcup Z$, $Z=\{(p):p\in S\}$ ($j$ open, $i$ closed), the six operations form a BBD
  recollement $(j_!,j^*,j_*)\dashv(i^*,i_*,i^!)$ with $j^*=j^!$, $i_*=i_!$, gluing triangles
  $j_!j^*\to\mathrm{id}\to i_*i^*\xrightarrow{+1}$, $i_*i^!\to\mathrm{id}\to Rj_*j^*\xrightarrow{+1}$
  (Thm 64a). Feeding it the **dilation coefficient** $\mathcal V$ (generic stalk $\mathbb Z$, closed
  costalk the per-prime Milnor pro-system $(\mathbb Z,\times p)$: $\varprojlim=0$ detached,
  $\varprojlim^1=\mathbb Z_p/\mathbb Z$), the open/closed triangle on $j_!\mathcal V$ ($j^*j_!=
  \mathrm{id}$, $i^*j_!=0$) collapses to the SES $0\to\mathbb Z^{s-1}\to H^1(X,j_!\mathcal V)\to
  \prod_p(\mathbb Z_p/\mathbb Z)\to0$ with middle $H^1(X,j_!\mathcal V)\cong\widehat{\mathbb Z}_S/
  \mathbb Z$ (Thm 64b). So the total phantom **is** a single $j_!$-cohomology, boundary $\partial=$
  Pass-63 $d_2=$ Pass-62 $\epsilon_S$ (image rank $s-1$, kernel diagonal $\mathbb Z$): the three
  avatars are one morphism. **Löb $=i^*$, Rosser $=j_!$, mixing $=\partial$.**
  **(ii) RESOLVED — Thm 64c (the motive).** $S\subseteq S'\Rightarrow X_S$ *open* in $X_{S'}$
  (complement is closed points), so $M:S\mapsto j_!\mathcal V_S$ is a functor $(\mathcal P_{\mathrm{
  fin}}(\mathbb P),\subseteq)\to D^b(\mathbb Z)$ (weight-filtered $W_0=$ Löb, $\mathrm{gr}^W_1=$
  Rosser), $\epsilon$ natural, genuinely **arithmetic** (Thm 63c) — the "Löb–Rosser motive" (an
  honest constructible-sheaf datum, *not* a Voevodsky motive). **Pathologies:** $s=1\Rightarrow
  H^1(j_!\underline{\mathbb Z})=0$, pure Löb (Rosser needs $\ge2$ primes); $\{2,3\}$/$\{2,5\}$
  rad-incomparable, no arrow; **$S=\mathbb P\Rightarrow H^1(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)=
  \widehat{\mathbb Z}/\mathbb Z$, the integral finite-adele class group.** Machine-verified
  `artifacts/reports/pass64-recollement-six-functor-motive-check.json` (PASS).
  **(iii) carried [Open]:** the exact $\aleph_1$-threshold of Thm 61c (strictly between
  $\mathfrak b=\aleph_1$ and $\mathrm{MA}_{\aleph_1}$; $\mathrm{add}(\mathcal M)$, Suslin tree, or a
  new $\omega_1$-tower invariant?) is untouched this pass.
- **[Partially resolved (Pass 65)]** **The Verdier-dual "functional equation" of the dictionary, and the scheme
  lift.** (i) Pass 64 used only the first gluing triangle $j_!j^*\to\mathrm{id}\to i_*i^*$. Compute
  the closed costalk-dual $i^!\mathcal V$ and the **Verdier dual** $\mathbb D(j_!\mathcal V)=
  Rj_*\,\mathbb D\mathcal V$: does duality exchange the Löb ($i^*$) and Rosser ($j_!$) strata —
  "Löb $\leftrightarrow$ Rosser" $=$ ($j_!\leftrightarrow Rj_*$) Verdier duality — and does it fix or
  invert $\epsilon_S$, giving a $\pm1$ functional equation of the phantom? (ii) Lift the finite
  Alexandrov model to the honest $\mathrm{Spec}\,\mathbb Z$ (generic point $+$ Krull/Zariski
  topology) and verify the adelic identity $H^1(j_!\mathcal V)=\widehat{\mathbb Z}/\mathbb Z$ and the
  weight filtration survive the passage from finite space to scheme. (iii) [carried] the still-[Open]
  $\aleph_1$-threshold of Thm 61c.
  **Finite-model resolution (Pass 65):** (i) is resolved on the finite Alexandrov spine. The
  $i^!$ side is the local-support complex $\mathbb Z\xrightarrow{\Delta}\mathbb Z^S$, with
  $H^0=0$ and $H^1\cong\mathbb Z^{|S|-1}$, so the Rosser lattice has an $i^!$ presentation as well
  as the Pass-63 $j_!$ presentation. The boundary $d_S:(x_p)\mapsto(x_p-x_{p_0})$ dualizes to
  $-d_S^T$, giving the finite functional equation
  $\mathbb D(\epsilon_S)=-\epsilon_S^\vee$; $\mathbb D^2(d_S)=d_S$ and the finite-prime restriction
  squares commute (machine-verified in
  `artifacts/reports/pass65-verdier-dual-recollement-functional-equation-check.json`). (ii) remains
  [Open] at the honest $\mathrm{Spec}\,\mathbb Z$ site: choose the dualizing normalization and
  compute the duals of $\mathbb Z_p/\mathbb Z$ and $\widehat{\mathbb Z}_S/\mathbb Z$ with
  products/sums controlled. (iii) remains [Open].
- **[Partially resolved (Pass 66)]** **Scheme-site Verdier lift and dualizing normalization.** Prove or refute the
  scheme-level equation $\mathbb D(\epsilon_S)=-\epsilon_S^\vee$ for finite $S$ and then
  $S=\mathbb P$. Required subquestions: (a) identify the correct duality
  (Verdier/Pontryagin/Matlis/$R\mathrm{Hom}_{\mathbb Z}$) for the pro-object $\mathcal V$; (b)
  compute the duals of $\mathbb Z_p/\mathbb Z$, $\prod_p(\mathbb Z_p/\mathbb Z)$, and
  $\widehat{\mathbb Z}_S/\mathbb Z$ without losing product/direct-sum information; (c) decide
  whether the integral sign in the finite model survives the scheme-site convention or is absorbed
  by an orientation choice.
  **Finite-prime resolution (Pass 66):** unshifted $R\mathrm{Hom}_{\mathbb Z}(-,\mathbb Z)$ is not
  the degree-preserving duality because finite cyclic layers are killed by
  $\operatorname{Hom}_{\mathbb Z}(-,\mathbb Z)$ and recovered only in
  $\operatorname{Ext}^1_{\mathbb Z}(-,\mathbb Z)$. Character duality
  $D_{\mathrm{ch}}=\operatorname{Hom}(-,\mathbb Q/\mathbb Z)$ preserves finite $\mathbb Z/p^n$
  layers and gives $D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee$ for finite $S$. The all-prime
  case was formulated in Pass 71 as a pro-restricted finite-shadow law. Pass 72 introduced the
  hybrid exact-category candidate $\mathcal H_\epsilon$, Pass 73 proved its presentation-level
  universal property among admissible support-preserving certificate targets, Pass 74 built a
  faithful tagged restricted pro-Ab realization on the five generator families, and Pass 75
  replaced those tags by internal support/stage projectors, and Pass 76 gave those projectors a
  first natural model: the finite-prime stratified pro-site $\mathrm{StratPro}_\epsilon(U,N)$, with
  $e_p$ multiplication by clopen characteristic functions $\mathbf 1_{\{p\}}$ and $q_n$ prefix
  truncations of the lcm tower, through which $\rho_{\mathrm{proj}}$ factors faithfully.
  **Resolved (Pass 77):** the upgrade lands in $\mathrm{Solid}_{\mathbb Z}$ as a degree-$1$ derived
  duality ($\widehat{\mathbb Z}^{\,*}\cong(\mathbb Q/\mathbb Z)[-1]$, phantom nonzero in degree $1$),
  and is provably impossible in $\mathrm{LCA}$ ($Q^{\vee}_{\mathrm{LCA}}=0$ by the dense-subgroup
  barrier); the signed law is honest in $D(\mathrm{Solid})$. See the [Resolved (Pass 77)] entry
  below and `pass77-derived-solid-realization-check.json`.
- **[Partially resolved (Pass 67)]** **Restricted-product adelic duality for the full spectrum.** Define the
  Loeb-Rosser coefficient for $S=\mathbb P$ as a restricted product of local objects rather than a
  bare product. Prove that the finite-adele coefficient is self-dual under a chosen additive
  character, identify the integral lattice annihilator, and check whether the global boundary class
  transforms as $-\epsilon^\vee$ or whether the sign is absorbed by the global orientation
  convention. This is the necessary replacement for the naive all-prime product statement.
  **Finite-conductor resolution (Pass 67):** the conductor windows
  $p^{-k}\mathbb Z_p/p^k\mathbb Z_p\cong\mathbb Z/p^{2k}$ are self-dual, with
  $\mathbb Z_p/p^k\mathbb Z_p$ self-annihilating; finite products preserve this and the signed
  boundary transpose survives conductor normalization. **Remaining obstruction:** fixed finite
  conductor quotients do not see $\widehat{\mathbb Z}/\mathbb Z$, because CRT makes
  $\mathbb Z/N\to\prod_{p\mid N}\mathbb Z/p^{v_p(N)}$ surjective. Pass 68 supplied the derived
  pro-Ab quotient, Pass 71 supplied the support-preserving finite-shadow formulation, Pass 72
  packaged both layers into $\mathcal H_\epsilon$, Pass 73 proved presentation-initiality, and
  Pass 74 verified a faithful tagged pro-Ab realization, Pass 75 internalized the tags as
  projectors, and Pass 76 realized those projectors geometrically on a finite-prime stratified
  pro-site (clopen support strata + lcm prefix-stage truncations).  The remaining task is the full
  categorical duality proof, i.e. lifting that finite stratified site to an established all-prime
  derived/pro exact category and proving the signed law there.
- **[Resolved at algebraic level (Pass 68)]** **Derived/pro quotient formalization of $\widehat{\mathbb Z}/\mathbb Z$.**
  Identify the exact category in which the levelwise-zero CRT quotients assemble into the nonzero
  Loeb-Rosser phantom. Candidate formalisms: (a) pro-abelian derived cokernel of
  $\mathbb Z\to\{\mathbb Z/N\}_N$; (b) condensed/solid quotient of $\widehat{\mathbb Z}$ by dense
  $\mathbb Z$; (c) exact-category extension class recovering the Pass-62/63 $\epsilon_S$ as a
  derived boundary. Required test: recover $\widehat{\mathbb Z}/\mathbb Z$ from the inverse system
  while every finite CRT quotient remains zero.
  **Resolution (Pass 68):** using $N_n=\operatorname{lcm}(1,\ldots,n)$, the levelwise exact sequence
  $0\to N_n\mathbb Z\to\mathbb Z\to\mathbb Z/N_n\mathbb Z\to0$ has zero finite cokernel by CRT, but
  the kernel tower is non-Mittag-Leffler with $\varprojlim N_n\mathbb Z=0$, so the derived exact
  sequence gives $\varprojlim^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z$. The algebraic
  category is therefore derived pro-Ab; topology/Hausdorff refinements may require condensed/LCA
  language but are not needed to recover the group.
- **[Resolved algebraically (Pass 70); pro-restricted finite-shadow formulation added in Pass 71]** **Identify the derived
  pro-cokernel with the recollement class $\epsilon$.**
  Build an explicit comparison between the derived inverse-limit boundary
  $\widehat{\mathbb Z}\to\varprojlim^1(N_n\mathbb Z)$ and the Pass-62/63/64 Loeb-Rosser boundary
  $\epsilon$ (filtration extension / $d_2$ / recollement boundary). Required test: construct a
  chain map from the bicomplex or recollement long exact sequence to the lcm-tower derived
  sequence, and verify that character duality sends the resulting class to $-\epsilon^\vee$.
  **Resolution (Pass 70):** for finite $S$, use $M_{S,k}=\prod_{p\in S}p^k$.  The derived
  pro-cokernel is $\varprojlim^1(M_{S,k}\mathbb Z)\cong\widehat{\mathbb Z}_S/\mathbb Z$, and the
  projection to the product of local derived cokernels
  $\prod_{p\in S}(\mathbb Z_p/\mathbb Z)$ has kernel
  $\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}$.  This is exactly the Pass-62 filtration and
  Pass-64 recollement extension $\epsilon_S$.  The boundary matrix
  $d_S(x)=(x_p-x_{p_0})_{p\ne p_0}$ has kernel $\Delta\mathbb Z$ and dualizes in finite
  character-normalized shadows to $-d_S^T$.
  **Pro-restricted formulation (Pass 71):** $\epsilon_{\mathbb P}$ is the compatible finite-prime
  family $\{\epsilon_S\}_{S\subset\mathbb P,\ |S|<\infty}$ plus the derived pro-cokernel
  $\widehat{\mathbb Z}/\mathbb Z$.  The signed law
  $D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$ means that every finite
  prime/conductor shadow sends $d_S$ to $-d_S^T$, duality squared returns $d_S$, and all restriction
  squares commute.  The bare product duality is rejected because it keeps only finite-support
  characters.
  **Hybrid candidate (Pass 72):** $\mathcal H_\epsilon$ has finite conductor restricted-product
  shadows $(S,k,W_{S,k},L_{S,k},d_S)$ and the derived pro-Ab lcm kernel tower
  $K_n=N_n\mathbb Z$.  A sequence is hybrid-exact when every finite shadow is exact and the pro
  layer supplies $\varprojlim^1K_n\cong\widehat{\mathbb Z}/\mathbb Z$.  Machine verification checks
  finite exactness, restriction composition, conductor bookkeeping, and non-ML pro growth.
  **Presentation initiality (Pass 73):** $\mathcal H_\epsilon$ is initial among admissible
  support-preserving certificate targets receiving the five generator families: finite conductor
  windows, Loeb-Rosser boundaries, restrictions, signed duality, and the derived pro-Ab lcm tower.
  Omitting any family destroys part of $\epsilon_{\mathbb P}$.
  **Tagged realization test (Pass 74):** the functor
  $\rho_{\mathrm{tag}}:\mathcal H_\epsilon\to
  \mathbf{Pro}^{\mathrm{rp}}_{\mathrm{tag}}(\mathbf{Ab}_{\mathrm{fin}})
  \times\mathbf{Pro}_{\mathrm{tag}}(\mathbf{Ab})$ is faithful on the five generator families in
  the checked finite/pro window, while the corresponding tag-forgetting target is not faithful
  because restriction source support and repeated lcm stages collide.  **Remaining open part:**
  **Projector refinement (Pass 75):** explicit tags can be replaced by internal Boolean support
  projectors $e_p$ and lcm-stage projectors $q_n$, with $e_Se_T=e_{S\cap T}$ and
  $q_nq_m=q_{\min(n,m)}$; the projector-enriched realization is faithful on the checked generator
  families.  The companion exact-obstruction report records that an ordinary exact 1-category
  target still cannot carry the $\varprojlim^1$ phantom as a finite exact-cone value.
  **Stratified pro-site model (Pass 76):** $e_p$ and $q_n$ are realized naturally on the finite-prime
  stratified pro-site $\mathrm{StratPro}_\epsilon(U,N)$ -- $e_p=(\cdot)\mathbf 1_{\{p\}}$ on clopen
  prime strata, $q_n$ prefix truncations of the lcm tower -- through which $\rho_{\mathrm{proj}}$
  factors as $\rho_{\mathrm{site}}$, faithfully on all five families (4160 clopen + 576 stage
  relations verified).
  **Resolved (Pass 77) -- two-faced answer.** The lift exists in $\mathrm{Solid}_{\mathbb Z}$ and is
  impossible in $\mathrm{LCA}$, and these are two ends of one $[-1]$ shift. (Thm 77a, LCA no-go)
  $\mathbb Z$ dense in $\widehat{\mathbb Z}$ makes $Q=\widehat{\mathbb Z}/\mathbb Z$ non-Hausdorff and
  not an LCA object; its Pontryagin dual is the annihilator $\ker(\mathbb Q/\mathbb Z\hookrightarrow
  \mathbb T)=0$, so the signed law collapses to $0=0$ in LCA. (Thm 77b, solid degree shift) In
  $\mathrm{Solid}_{\mathbb Z}$, $R\underline{\mathrm{Hom}}(\mathbb Z_p,\mathbb Z)\cong
  (\mathbb Q_p/\mathbb Z_p)[-1]$ and $\widehat{\mathbb Z}^{\,*}\cong(\mathbb Q/\mathbb Z)[-1]$, so the
  phantom $\epsilon_{\mathbb P}$ is nonzero and sits in cohomological degree $1$; support projectors
  upgrade to clopen idempotents of $\beta\mathbb P$ with $e_Se_T=e_{S\cap T}$ for all subsets.
  (Thm 77c) $D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$ is therefore a
  genuine degree-$1$ derived equation, not realizable in degree $0$. Machine-verified
  `artifacts/reports/pass77-derived-solid-realization-check.json` (PASS).
- **[Resolved (Pass 78)]** **Solid reflexivity of the Loeb-Rosser phantom.** Is the canonical
  evaluation $\eta_\epsilon:\epsilon\to\epsilon^{**}$ an isomorphism in $D(\mathrm{Solid}_{\mathbb Z})$
  for $\epsilon=\widehat{\mathbb Z}/\mathbb Z=\varprojlim^1(N_n\mathbb Z)$, or does a
  $\varprojlim^1$-of-$\varprojlim^1$ secondary phantom obstruct it, and what is the surviving sign?
  **Resolution (Pass 78):** reflexivity holds. Dualizing $0\to\mathbb Z\to\widehat{\mathbb Z}\to
  \epsilon\to0$ once gives $\operatorname{Hom}(\epsilon,\mathbb Z)=0$ and $D\epsilon\cong E[-1]$ with
  $E\cong\mathbb Q$ (the extension of class the unit $1\in\widehat{\mathbb Z}^\times=
  \operatorname{Ext}^1(\mathbb Q/\mathbb Z,\mathbb Z)$); dualizing again -- with $\mathbb Q/\mathbb Z=
  \operatorname{colim}\mathbb Z/n$ dualized termwise to $\widehat{\mathbb Z}[-1]$ -- gives a connecting
  map $d:\mathbb Z\hookrightarrow\widehat{\mathbb Z}$ (multiplication by the unit class), so
  $\ker d=0$, $\operatorname{coker}d=\widehat{\mathbb Z}/\mathbb Z=\epsilon$, and $\epsilon^{**}\cong
  \epsilon$ (Thms 78a/78b). **No secondary phantom**: a non-unit (zero-divisor) class -- e.g. the
  idempotent $e_2$ -- would make $\operatorname{coker}=\widehat{\mathbb Z}/c\widehat{\mathbb Z}$ carry
  extra $p$-torsion (machine-exhibited, non-iso from stage $n=3$); the unit class kills it. **Sign:**
  finite shadows give $D^2(d_S)=d_S$ ($+1$), but the phantom's odd shift $[-1]$ contributes Koszul
  sign $-1$, so $\eta_\epsilon=-\mathrm{id}$ = the antipode (Thm 78c). Machine-verified
  `artifacts/reports/pass78-solid-reflexivity-phantom-check.json` (PASS).
- **[Resolved (Pass 79), as a correction]** **(Anti)symmetry of the phantom's self-duality pairing.**
  The Pass-78 phrasing "object-level $[-1]$-shift self-duality $\epsilon\cong D\epsilon[1]$" is
  **false** and is corrected here: Pass 78 proved *reflexivity* $\epsilon^{**}\cong\epsilon$, not
  self-duality; in fact $D\epsilon\cong\mathbb Q[-1]$ and $D\mathbb Q\cong\epsilon[-1]$, so $\epsilon$
  and $\mathbb Q$ are a **dual pair** (as bare abelian groups $\epsilon\cong\mathbb A_f/\mathbb Q$ is a
  $\mathbb Q$-vector space of dimension $2^{\aleph_0}$ while $\dim_{\mathbb Q}\mathbb Q=1$, so no shift
  makes $D\epsilon\cong\epsilon[s]$) — **Thm 79a**. **Forced degree (Thm 79b):**
  $\operatorname{Hom}_{D(\mathrm{Solid})}(\epsilon\otimes^{\blacksquare}\epsilon,\mathbb Z[m])
  =\operatorname{Ext}^{m-1}_{\mathrm{Solid}}(\epsilon,\mathbb Q)$, which is $\mathbb Q$ for $m=2$ and
  $0$ otherwise; the *proposed* target $\mathbb Z[-1]$ carries **only the zero pairing**, and the
  unique nonzero self-pairing $b:\epsilon\otimes^{\blacksquare}\epsilon\to\mathbb Z[2]$ generates
  $\operatorname{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\cong\mathbb Q$ as the **finite-adele class
  extension** $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$ (pushout of the defining sequence along
  $\mathbb Z\hookrightarrow\mathbb Q$). **Type (Thm 79c):** $b$ is **alternating** (degree-$1$ swap
  sign $(-1)^{1\cdot1}=-1$ — the Pass-78 antipode, so the symplectic intuition is correct in sign) but
  **degenerate** (its adjoint $\epsilon\to\mathbb Q[1]$ is not an iso); the nondegenerate symplectic
  object is the hyperbolic plane $H=\epsilon\oplus\mathbb Q$ with $\epsilon,\mathbb Q$ as complementary
  Lagrangians and perfect cross-pairing $\epsilon\otimes^{\blacksquare}\mathbb Q\to\mathbb Z[1]$.
  **Darboux no-go (Thm 79d):** the StratPro support idempotents $e_S$ ($S\subseteq\mathbb P$) act on
  $\widehat{\mathbb Z}$ but descend to $\mathrm{End}_{\mathrm{Solid}}(\epsilon)$ **iff**
  $S\in\{\varnothing,\mathbb P\}$ (else $e_S(1)=\mathbf 1_S\notin\mathbb Z$), so $\epsilon$ is
  **prime-indecomposable** — the unit/diagonal class $1\in\widehat{\mathbb Z}^{\times}$ that drives
  Pass-78 reflexivity is exactly the obstruction; the primes are **not** Darboux coordinates of
  $\epsilon$. Machine-verified `artifacts/reports/pass79-symplectic-lagrangian-phantom-check.json`
  (PASS; $2^6$-subset Darboux enumeration: exactly $2$ descend).
- **[Resolved (Pass 80)]** **Metaplectic/Weil structure of the hyperbolic phantom plane.** Pass 79 shows
  the nondegenerate symplectic object is $H=\epsilon\oplus\mathbb Q$ (Lagrangians $\epsilon,\mathbb Q$;
  pairing $\langle\,,\rangle:\epsilon\otimes^{\blacksquare}\mathbb Q\to\mathbb Z[1]$).
  **Resolution (Pass 80):** the answer is **no** to both $\mathrm{SL}_2$ and metaplectic descent, and
  the obstruction is *not* the one the Pass-79 Next step guessed. A solid endomorphism of $H$ is a
  $2\times2$ matrix with entries $a\in\mathrm{End}(\epsilon)$, $b\in\mathrm{Hom}(\mathbb Q,\epsilon)
  =\epsilon$, $c\in\mathrm{Hom}(\epsilon,\mathbb Q)$, $d\in\mathrm{End}(\mathbb Q)=\mathbb Q$; the
  Pass-79 computation $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=H^0(\mathbb Q[-1])=0$ forces
  $c\equiv0$, so $\mathrm{End}_{\mathrm{Solid}}(H)$ is **upper-triangular** (**Thm 80a**) and
  $\mathrm{Sp}(H)$ is the solid **Borel** $B=\mathbb Q^{\times}\ltimes\epsilon$ — the affine "$ax+b$"
  group / Schrödinger parabolic fixing the polarization $\epsilon$ — *not* $\mathrm{SL}_2$ and *not*
  a nonabelian Heisenberg group ($U$ abelian) (**Thm 80b**). The Weyl flip $w$ (cross-polarization
  Fourier transform) has no solid model. Metaplectic non-descent (**Thm 80c**): the finite-adele Weil
  rep of $\mathrm{SL}_2(\mathbb A_f)$ does not act; at level $N$ the flip is the finite Fourier
  $F_N$ ($F_N^4=I$, $|g_N|^2=N$, $w\in\mathrm{SL}_2(\mathbb Z/N)$), but its only candidate limit lives
  in $\mathrm{Hom}(\epsilon,\mathbb Q)=0$. The **precise wall** is that one-sided vanishing — i.e.
  $\epsilon$ is reflexive (Pass 78) but **not** $\otimes$-dualizable — and explicitly **not** the
  degeneracy of $b$ (the shear-by-$b$ unipotent survives in $B$; only the inverse intertwiner is
  absent). Machine-verified `artifacts/reports/pass80-metaplectic-borel-noflip-check.json` (PASS).
- **[Resolved (Pass 81)]** **Automorphic shadow of the solid Borel.** Pass 80 gives $\mathrm{Sp}(H)=
  B=\mathbb Q^{\times}\ltimes\epsilon$, an affine "$ax+b$" group with $\epsilon$ as its unique stable
  polarization and no Weyl flip. Does $B$ carry the algebraic shadow of a *degenerate principal
  series* / Eisenstein datum, and is the absent cross-polarization intertwiner
  $\in\mathrm{Hom}(\epsilon,\mathbb Q)=0$ exactly the obstruction to a *self-dual functional equation*
  relating the two polarizations? Concretely: realize the $B$-action on sections over $\epsilon$, and
  decide whether "no Fourier flip" is the representation-theoretic face of the Pass-51 Löb (integral)
  vs Rosser (non-integral-unit) dividing line one functor-level up. Record whether the
  reflexive-but-not-dualizable distinction is a clean structural invariant separating $\epsilon$ from
  genuinely dualizable phantoms.
  **Resolution (Pass 81):** yes, but maximally degenerately. Since $\mathrm{Sp}(H)=B$, the principal
  series $I(s)=\mathrm{Ind}_B^{\mathrm{Sp}(H)}\chi_s$ is just $\chi_s$, length $1$, with no Bruhat
  big cell and no Weyl intertwiner. The opposite unipotent
  $\bar U=\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$, so the $s\mapsto -s$ functional
  equation has no nonzero solid operator. Finite levels still have Fourier intertwiners and Gauss
  $c$-factors; the functional equation dies only in the solid limit. Machine-verified
  `artifacts/reports/pass81-degenerate-principal-series-functional-equation-check.json` (PASS).
- **[Resolved (Pass 82)]** **Whittaker model of the degenerate solid Borel.** Does the maximally
  degenerate principal series $I(s)=\chi_s$ carry a nonzero Whittaker or generalized-Whittaker
  functional for a nontrivial character of $U=\epsilon$, and is such a coefficient the carrier of
  the Rosser torsor?
  **Resolution:** no. Since $I(s)$ is trivial on $U$, $\mathrm{Hom}_U(I(s),\psi)$ is one-dimensional
  for $\psi=1$ and zero for every nontrivial $\psi$. The only surviving functional is the constant
  term; the Rosser torsor is the shear parameter $U=\epsilon$ itself, not a generic Whittaker
  coefficient. Finite Fourier shadows of the constant $U_N$-action vanish for all nontrivial
  additive characters. Machine-verified
  `artifacts/reports/pass82-whittaker-archimedean-repair-check.json` (PASS).
- **[Resolved / corrected (Pass 83)]** **Global solenoid versus finite phantom.** Adding the archimedean place gives
  $\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z\cong\mathbb A/\mathbb Q$ and an exact
  comparison with $\epsilon=\widehat{\mathbb Z}/\mathbb Z$.  Pass 83 corrected the exact row:
  $$0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0$$
  is the compact Hausdorff row, while
  $$\mathbb R\to\Sigma\to\epsilon=\widehat{\mathbb Z}/\mathbb Z\to0$$
  is the dense/non-Hausdorff quotient row.  The compact row does not split continuously because its
  dual $0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0$ has no torsion-valued section into
  $\mathbb Q$.  Global Fourier theory restricts to $\mathbb Q/\mathbb Z$ on the closed profinite
  kernel, but only the trivial character descends to $\epsilon$ in degree $0$. Machine-verified
  `artifacts/reports/pass83-solenoid-exact-triangle-correction-check.json` (PASS).
- **[Resolved (Pass 84)]** **Derived-solid boundary of the finite phantom.** Formulate the exact triangle
  behind the dense quotient $\mathbb R\to\Sigma\to\epsilon$ in the solid/condensed derived category.
  Decide whether the boundary quotient $\mathbb Q/\mathbb Z$ (or its shifted solid dual) is precisely
  the replacement for the missing finite-prime Weyl flip $\epsilon\to\mathbb Q$, and whether the
  Borel unipotent $U=\epsilon$ acts only on this quotient boundary rather than by continuous
  translations on $\Sigma$.
  **Resolution:** topologically, $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ is indiscrete, so its
  Hausdorff reflection is $0$ and every continuous homomorphism from $\epsilon$ to a Hausdorff group
  is zero.  Thus $U=\epsilon$ has no nontrivial continuous translation action on $\Sigma$.  The
  replacement for the missing Weyl flip is the degree-$1$ solid boundary
  $D\epsilon\simeq\mathbb Q[-1]$ / $\mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\simeq\mathbb Q$,
  represented by $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$.  Machine-verified
  `artifacts/reports/pass84-dense-phantom-boundary-action-check.json` (PASS).
- **[Resolved (Pass 85)]** **Two-term complex model of the phantom boundary.** Build explicit complexes
  $[\mathbb Z\to\widehat{\mathbb Z}]$, $[\mathbb R\to\Sigma]$, and
  $[\mathbb Q\to\mathbb A_f]$ representing the same finite-prime boundary in the relevant
  solid/condensed derived category.  Prove which maps are quasi-isomorphisms after Hausdorff
  reflection, after solidification, and after applying the Borel shear functor, and isolate the exact
  class preserving $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$.
  **Resolution:** the three complexes all have quotient $\epsilon$ and acyclic finite/Hausdorff
  shadows, but only $[\mathbb Z\to\widehat{\mathbb Z}]\to[\mathbb Q\to\mathbb A_f]$ is the pushout
  preserving the unit/shear class.  The archimedean row $[\mathbb R\to\Sigma]$ preserves the quotient
  but not the finite-adele Borel shear extension.  Machine-verified
  `artifacts/reports/pass85-two-term-boundary-complex-check.json` (PASS).
- **[Resolved (Pass 86)]** **Universal property of the finite-adele shear pushout.** Characterize
  $C_{\mathbb Q}=[\mathbb Q\to\mathbb A_f]$ as the initial divisible-kernel quotient model receiving
  $C_{\mathbb Z}=[\mathbb Z\to\widehat{\mathbb Z}]$ that preserves the unit class
  $1\in\widehat{\mathbb Z}^{\times}$ and kills ordinary finite/Hausdorff cokernels.  Decide whether
  every shear-preserving quotient model factors uniquely through $C_{\mathbb Q}$ in $D(\mathrm{Solid})$,
  and whether this universal property is the categorical replacement for the missing Weyl flip.
  **Resolution:** the statement is true after replacing "divisible" by "uniquely divisible" /
  $\mathbb Q$-linear kernel, or after specifying a $\mathbb Q$-linear kernel map.  Then
  $\mathbb Z\to D$ extends uniquely to $\mathbb Q\to D$, so
  $C_{\mathbb Q}$ is initial among shear-marked pushout models under $C_{\mathbb Z}$, while finite
  residue shadows remain acyclic.  The naive version for arbitrary divisible kernels is false:
  $\mathbb Q/\mathbb Z$ gives distinct maps $q\mapsto kq\bmod\mathbb Z$ that restrict identically on
  $\mathbb Z$.  Machine-verified
  `artifacts/reports/pass86-shear-pushout-universal-property-check.json` (PASS).
- **[Resolved (Pass 87)]** **Derived mapping-space form of the shear-pushout initiality.** Upgrade the
  Pass-86 finite certificate to a statement in $D(\mathrm{Solid})$: identify the homotopy fiber of
  shear-marked maps out of $C_{\mathbb Q}$ over maps out of $C_{\mathbb Z}$, prove contractibility
  for uniquely divisible kernels, and decide whether torsion-divisible summands must be excluded,
  quotiented, or decorated by extra shear data.
  **Resolution:** the homotopy fiber over a fixed shear-marked map is
  $\mathbf R\operatorname{Map}(\mathbb Q/\mathbb Z,D)$, where $D$ is the target kernel.  This fiber is
  contractible for uniquely divisible kernels because
  $\operatorname{Hom}(\mathbb Q/\mathbb Z,D)=0$ and divisible targets are injective.  Torsion-divisible
  summands contribute nontrivial components and therefore must be excluded for strict initiality or
  decorated by a chosen $\mathbb Q/\mathbb Z\to T$ boundary component.  Machine-verified
  `artifacts/reports/pass87-mapping-space-shear-initiality-check.json` (PASS).
- **[Resolved (Pass 88)]** **Derived stabilizer of the finite-adele shear extension.** Compute the
  automorphism/stabilizer of
  $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$ as a shear-marked object under
  $C_{\mathbb Z}$, compare its degree-$0$ part with the solid Borel
  $\mathbb Q^\times\ltimes\epsilon$, and determine whether any derived
  automorphisms survive after the torsion-boundary decoration rule of Pass 87.
  **Resolution:** strict automorphisms under $C_{\mathbb Z}$ are trivial;
  forgetting the integral marking but preserving the finite-adele Ext line gives
  degree-$0$ stabilizer $\mathbb Q^\times$; and the full Borel
  $\mathbb Q^\times\ltimes\epsilon$ is recovered only at the hyperbolic-plane level
  $H=\epsilon\oplus\mathbb Q$, where $\epsilon$ is the unipotent shear parameter rather than an
  automorphism of the bare exact row.  No extra derived automorphisms survive for the final
  $\mathbb Q$-kernel extension after the Pass-87 torsion-boundary rule.  Machine-verified
  `artifacts/reports/pass88-shear-extension-stabilizer-check.json` (PASS).
- **[Resolved (Pass 89)]** **Borel-torsor theorem for the Rosser phantom.** Consolidate Passes 80-88 into
  a theorem: the Rosser/phantom obstruction is a Borel-torsor or finite-adele extension class whose
  strict integral marking is rigid, whose extension-line stabilizer is $\mathbb Q^\times$, and whose
  hyperbolic realization has solid Borel $\mathbb Q^\times\ltimes\epsilon$.  State the exact functorial
  bridge back to the APS/Rosser unit-torsor line and identify which data are invariant under changing
  Guaspari-Solovay witness choices.
  **Resolution:** the Rosser witness-comparison Cech class, the
  $\varprojlim^1(\mathbb Z,\times m)$ or $\epsilon=\widehat{\mathbb Z}/\mathbb Z$
  phantom, the finite-adele extension line
  $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$, and the hyperbolic Borel shear
  orbit are four presentations of one torsor/extension class.  Witness changes
  alter representatives, sections, and finite lifts by coboundaries, but
  preserve the cohomology/torsor class, finite conductor restrictions, radical
  support, and finite-adele extension line.  Machine-verified
  `artifacts/reports/pass89-borel-torsor-rosser-phantom-check.json` (PASS).
- **[Resolved (Pass 90)]** **Conductor-functorial Borel torsors.** Make the
  Pass-89 theorem natural across $m$-adic and all-prime variants.  Specify the
  category of radical-compatible conductor maps, decide when a map
  $\widehat{\mathbb Z}_m/\mathbb Z\to\widehat{\mathbb Z}_{m'}/\mathbb Z$ exists
  or should be replaced by a span/pullback, and prove that the Cech torsor,
  finite-adele extension line, and hyperbolic Borel shear orbit commute in one
  diagram.
  **Resolution:** for squarefree supports $S\subseteq T$, coordinate projection
  descends to a canonical restriction
  $P(T)\to P(S)$ on $P(S)=(\prod_{p\in S}\mathbb Z_p)/\Delta\mathbb Z$, while
  zero-insertion $P(S)\to P(T)$ does not descend when new primes are added.
  Thus the Borel torsor is functorial contravariantly by restriction; support
  enlargement is a span, pullback, or finite-conductor choice.  Finite Borel
  shadows reduce along conductor divisibility and preserve the unit class and
  strict marked stabilizer.  Machine-verified
  `artifacts/reports/pass90-conductor-functorial-borel-torsors-check.json`
  (PASS).
- **[Resolved (Pass 91)]** **Descent/stackification of the Borel torsor.** Decide
  whether the restriction/span Borel-torsor package over the finite prime-cover
  site is a sheaf, a stack of torsors, or an obstruction object like the
  Pass-61 phantom presheaf.  Compute the descent defect for the cover by
  singleton primes, identify whether the Borel shear action kills or preserves
  the $\mathbb Z^S/\Delta\mathbb Z$ diagonal defect, and state the exact
  stackification or obstruction theorem.
  **Resolution:** on the finite singleton-prime cover site, the global-Levi
  Borel prestack $\mathbb Q^\times\ltimes P(S)$ is not a sheaf for
  $|S|\ge2$.  It retains the unipotent Rosser descent kernel
  $\mathbb Z^S/\Delta\mathbb Z$, while sheafification/stackification gives the
  local Borel object
  $(\mathbb Q^\times)^S\ltimes\prod_{p\in S}(\mathbb Z_p/\mathbb Z)$.  The
  hyperbolic shear action transports the descent-kernel lifts but does not
  choose a canonical zero section, so it preserves rather than kills the
  Rosser defect.  Machine-verified
  `artifacts/reports/pass91-borel-torsor-descent-obstruction-check.json`
  (PASS).
- **[Resolved (Pass 92)]** **Zariski/generic Borel descent.** Relocate the Borel
  descent obstruction from the discrete singleton-prime cover site to the
  Zariski/generic-point site of Pass 63.  Define the Borel analogue of the
  $j_!\mathbb Z$ ghost line, decide whether the global-Levi Borel prestack has
  a genuine $H^1(j_!)$ obstruction there, and compare the resulting class with
  the finite-adele extension line and hyperbolic shear orbit.
  **Resolution:** on the connected finite Zariski/generic site
  $X_S=\{\eta\}\cup S$, constant Borel coefficients have no horizontal
  $H^1$ defect.  The Borel obstruction relocates to the unipotent
  $j_!$ ghost coefficient
  $\underline{\mathbb Q^\times}\ltimes j_!\underline{\mathbb Z}$, with
  $$H^1(X_S,j_!\mathbb Z)=\mathbb Z^S/\Delta\mathbb Z.$$
  Modulo $N$ the finite class set has size $N^{|S|-1}$, matching the
  Pass-91 discrete kernel.  With the dilation coefficient $\mathcal V$, this
  horizontal ghost embeds in
  $H^1(X_S,j_!\mathcal V)=\widehat{\mathbb Z}_S/\mathbb Z$; pushout along
  $\mathbb Z\to\mathbb Q$ gives the finite-adele extension line, and the
  hyperbolic Borel shear orbit changes representatives without selecting a
  canonical zero section.  Machine-verified
  `artifacts/reports/pass92-zariski-generic-borel-descent-check.json` (PASS).
- **[Resolved (Pass 93)]** **All-prime Spec-$\mathbb Z$ Borel $j_!$ upgrade.**
  Upgrade the finite-support $j_!$ Borel class to the honest all-prime
  $\mathrm{Spec}\,\mathbb Z$ site.  Identify which finiteness, compact-support,
  continuous-cohomology, or derived-completion hypotheses are needed for
  $$H^1(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)=\widehat{\mathbb Z}/\mathbb Z,$$
  and decide whether the Borel coefficient
  $\underline{\mathbb Q^\times}\ltimes j_!\underline{\mathbb Z}$ must be replaced
  by a pro/solid/condensed coefficient to keep the finite-adele extension line
  and hyperbolic shear comparison functorial.
  **Resolution:** on honest all-prime $\mathrm{Spec}\,\mathbb Z$, $\{\eta\}$
  is not open, so the finite-support $j_!$ notation must be replaced by a
  pro-open/continuous/solid coefficient
  $$\mathfrak B^{\mathrm{cont}}_{j!}
  =\mathbb Q^\times\ltimes R\!\varprojlim_{S\Subset\mathbb P}j_{S,!}\mathcal V_S.$$
  The support-direction restrictions are surjective and Mittag-Leffler, hence
  add no new $\varprojlim^1$; the nonzero derived content remains the per-prime
  dilation tower inside $\mathcal V$.  Consequently
  $$H^1_{\mathrm{cont}}(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)
  \cong\widehat{\mathbb Z}/\mathbb Z,$$
  with global Levi $\mathbb Q^\times$, finite-adele pushout
  $0\to\mathbb Q\to\mathbb A_f\to\widehat{\mathbb Z}/\mathbb Z\to0$, and
  hyperbolic Borel shear compatibility.  Machine-verified
  `artifacts/reports/pass93-all-prime-borel-jshriek-upgrade-check.json` (PASS).
- **[Resolved (Pass 94)]** **Verdier/solid dual of the all-prime Borel $j_!$ class.**
  Compute the Verdier or solid dual of
  $\mathfrak B^{\mathrm{cont}}_{j!}$ and decide whether the antipode sign from
  Passes 65 and 77 yields a functional-equation shadow for the all-prime Borel
  class.  The key constraint is to recover the signed dual boundary without
  creating a forbidden degree-$0$ Weyl flip
  $\epsilon\to\mathbb Q$, which Passes 80-82 ruled out.
  **Resolution:** the unipotent all-prime class is
  $\epsilon=\widehat{\mathbb Z}/\mathbb Z$, so
  $$D\epsilon\simeq\mathbb Q[-1].$$
  Hence the dual of the all-prime Borel $j_!$ coefficient is a Levi-marked
  boundary object with unipotent part $\mathbb Q[-1]$ and contragredient
  $\mathbb Q^\times$ action, not an opposite Borel in degree $0$.  Finite
  shadows retain the signed Verdier rule $D(d_S)=-d_S^T$, and all-prime
  biduality gives the antipode sign $\eta_\epsilon=-\mathrm{id}_\epsilon$.
  This is only a boundary-level functional-equation shadow: the finite-adele
  extension $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$ replaces the missing
  flip, while
  $\operatorname{Hom}^0_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$ keeps the
  no-Weyl wall intact.  Machine-verified
  `artifacts/reports/pass94-all-prime-borel-jshriek-solid-dual-check.json`
  (PASS).
- **[Resolved (Pass 95)]** **Boundary-only functional equation as a Borel complex.**
  Package the signed boundary shadow from Pass 94 as a two-term Borel or
  constant-term complex, probably built from
  $[\mathbb Q\to\mathbb A_f]$ with its $\mathbb Q^\times$ action.  Prove that
  it is natural under conductor restriction and finite support projection, and
  formulate a "functional equation without Weyl operator" theorem that keeps
  the Pass-81 no-standard-intertwiner wall explicit.
  **Resolution:** the package is the two-term Borel constant-term complex
  $$C_B=\mathbb Q^\times\ltimes[\mathbb Q\to\mathbb A_f].$$
  Every fixed finite conductor shadow
  $[\mathbb Z/N\to\prod_{p^e\parallel N}\mathbb Z/p^e]$ is CRT-acyclic, while
  the all-prime solid boundary has
  $$H^1(C_B)=\mathbb A_f/\mathbb Q\cong\widehat{\mathbb Z}/\mathbb Z=\epsilon.$$
  Conductor reductions commute with the diagonal complexes and preserve the
  Borel unit; support projection is canonical; support enlargement is only a
  finite-conductor CRT choice/span.  The theorem is therefore a constant-term
  functional-equation shadow with no nontrivial Whittaker coefficient and no
  standard Weyl/Fourier intertwiner.  Machine-verified
  `artifacts/reports/pass95-boundary-only-borel-constant-term-complex-check.json`
  (PASS).
- **[Resolved (Pass 96)]** **Constant-term Borel complex versus local Loeb sheafification.**
  Compare
  $$C_B=\mathbb Q^\times\ltimes[\mathbb Q\to\mathbb A_f]$$
  with the local Loeb sheafification
  $$(\mathbb Q^\times)^S\ltimes\prod_{p\in S}(\mathbb Z_p/\mathbb Z).$$
  Identify exactly which kernel is lost when global Levi data and the
  finite-adele boundary are replaced by local Levi/stalk data, and decide
  whether this comparison is best formulated as stackification, Hausdorff
  reflection, local constant-term projection, or a map of two-term complexes.
  **Resolution:** on the compact finite-support skeleton, the comparison is
  the map of two-term complexes
  $$[\mathbb Z\to\prod_{p\in S}\mathbb Z_p]\to
  [\mathbb Z^S\to\prod_{p\in S}\mathbb Z_p],$$
  diagonal in degree $0$ and identity in degree $1$.  The induced $H^1$ map
  has exact kernel
  $$K_S=\mathbb Z^S/\Delta\mathbb Z,$$
  with finite shadow size $N^{|S|-1}$.  The Levi map
  $\mathbb Q^\times\to(\mathbb Q^\times)^S$ has trivial kernel; local
  Loebification loses global Levi coherence as the quotient
  $(\mathbb Q^\times)^S/\Delta\mathbb Q^\times$.  Thus the best formulation is
  a map of two-term complexes plus stackification/local constant-term
  projection, not pure Hausdorff reflection.  Machine-verified
  `artifacts/reports/pass96-constant-term-local-loebification-check.json`
  (PASS).
- **[Resolved (Pass 97)]** **Rationalized finite-adele row versus compact Loebification kernel.**
  Lift the compact Pass-96 comparison to the full finite-adele row
  $$[\mathbb Q\to\mathbb A_f].$$
  Decide whether rationalizing the degree-$0$ compact skeleton kills,
  regrades, or transforms the free horizontal kernel
  $\mathbb Z^S/\Delta\mathbb Z$ into $\mathbb Q^S/\Delta\mathbb Q$ boundary
  data.  Determine whether the correct all-prime comparison is a solid
  cohomology cone, a condensed sheafification statement, or a filtered colimit
  of the finite-support maps.
  **Resolution:** for finite support $S$, rationalization gives the map
  $$[\mathbb Q\to\prod_{p\in S}\mathbb Q_p]\to
  [\mathbb Q^S\to\prod_{p\in S}\mathbb Q_p].$$
  Its $H^1$ kernel is
  $$K_{\mathbb Q,S}=\mathbb Q^S/\Delta\mathbb Q.$$
  The integral kernel $K_{\mathbb Z,S}=\mathbb Z^S/\Delta\mathbb Z$ injects
  into it, so the kernel is not killed.  It is regraded: because
  $K_{\mathbb Q,S}$ is divisible, $K_{\mathbb Q,S}/N K_{\mathbb Q,S}=0$, but
  $$K_{\mathbb Q,S}/K_{\mathbb Z,S}
  \cong(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)$$
  has $N$-torsion of size $N^{|S|-1}$.  Support projections remain
  surjective and Mittag-Leffler.  Machine-verified
  `artifacts/reports/pass97-rationalized-finite-adele-row-check.json`
  (PASS).
- **[Resolved (Pass 98)]** **Torsion boundary versus solid dual.**
  Compare the regraded torsion boundary
  $$(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)$$
  with the Pass-94 solid dual identity
  $$D\epsilon=\mathbb Q[-1].$$
  Decide whether the torsion boundary is the finite-support shadow of the
  same shifted constant-term obstruction, or whether it is only a local-Loeb
  artifact introduced by rationalizing the compact comparison.  Formulate the
  exact functor from finite-support torsion quotients to the all-prime solid
  boundary.
  **Resolution:** the torsion boundary is not literally the shifted solid dual
  as a raw object.  It is a degree-$0$ torsion coefficient with
  $|T_S[N]|=N^{|S|-1}$, while $D\epsilon\simeq\mathbb Q[-1]$ is shifted.  The
  bridge is the canonical unit extension
  $$0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0.$$
  Applying the extension/solid-dual passage sends each independent
  $\mathbb Q/\mathbb Z$ coordinate to one shifted $\mathbb Q[-1]$
  constant-term obstruction generator.  Thus the multiplicity $|S|-1$ is
  finite-support/local-Loeb bookkeeping, but the coefficient is the
  finite-support torsion presentation of the same shifted obstruction.
  Machine-verified
  `artifacts/reports/pass98-torsion-boundary-solid-dual-check.json` (PASS).
- **[Resolved (Pass 99)]** **Exact triangle from torsion boundary to all-prime constant term.**
  Construct the exact triangle or functor carrying the finite-support torsion
  boundary
  $$T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)$$
  into the all-prime constant-term complex $[\mathbb Q\to\mathbb A_f]$ and
  its solid boundary.  Verify compatibility with the Pass-94 antipode sign and
  no-Weyl wall $\operatorname{Hom}^0(\epsilon,\mathbb Q)=0$.  Determine which
  support-limit operation collapses the finite multiplicity $|S|-1$ to the
  all-prime universal generator while preserving the finite torsion shadows.
  **Resolution:** the canonical finite-support triangle is
  $$K_{\mathbb Z,S}\to K_{\mathbb Q,S}\to T_S\to K_{\mathbb Z,S}[1].$$
  A collapse to the one-generator unit extension requires a primitive
  zero-sum functional
  $$c\in\mathbb Z^S,\qquad \sum c_p=0,\qquad \gcd(c_p)=1.$$
  Such a $c$ gives a morphism to
  $$\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to\mathbb Z[1]$$
  and hence to $[\mathbb Q\to\mathbb A_f]$.  It maps
  $T_S[N]\twoheadrightarrow(\mathbb Q/\mathbb Z)[N]$ with kernel size
  $N^{|S|-2}$ for $|S|\ge2$.  The collapse is not canonical; it is an
  orientation choice.  The antipode sends $c$ to $-c$, and no degree-$0$
  Weyl map is created.  Machine-verified
  `artifacts/reports/pass99-torsion-boundary-constant-term-triangle-check.json`
  (PASS).
- **[Resolved (Pass 100)]** **Orientation torsor for primitive boundary collapse.**
  Describe the torsor of primitive zero-sum functionals
  $$\{c\in\mathbb Z^S:\sum c_p=0,\ \gcd(c_p)=1\}$$
  under support inclusions, support projections, and antipode sign.  Determine
  whether there is a natural oriented-support groupoid or span category making
  the collapse $T_S\to\mathbb Q/\mathbb Z$ functorial up to sign, and decide
  how this orientation data survives, or is quotiented, in the all-prime
  constant-term generator $D\epsilon\simeq\mathbb Q[-1]$.
  **Resolution:** for
  $$\mathcal O_S=\{c\in\mathbb Z^S:\sum c_p=0,\ \gcd(c_p)=1\},$$
  the canonical transition for $S\subseteq T$ is zero-extension
  $\mathcal O_S\to\mathcal O_T$, i.e. pullback along the boundary projection
  $T_T\to T_S$.  It preserves primitivity, collapse compatibility, finite
  kernel factorization, and the antipode $c\mapsto-c$.  There is no canonical
  reverse projection $\mathcal O_T\to\mathcal O_S$, since restriction can fail
  zero-sum descent; and no support-symmetric primitive orientation exists.
  Therefore the all-prime generator is obtained only after choosing,
  quotienting, or forgetting the orientation torsor.  Machine-verified
  `artifacts/reports/pass100-orientation-torsor-support-functoriality-check.json`
  (PASS).
- **[Resolved (Pass 101)]** **Oriented-support groupoid and antipode quotient.**
  Define the groupoid or stack whose objects are oriented supports $(S,c)$
  with $c\in\mathcal O_S$, whose transition morphisms include zero-extension
  and antipode $c\mapsto-c$.  Compute its antipode quotient and decide whether
  that quotient retains exactly the Pass-94 functional-equation sign or loses
  essential orientation data.  Use this to present the all-prime
  constant-term generator $D\epsilon\simeq\mathbb Q[-1]$ as a quotient or
  colimit of oriented finite-support boundary data.
  **Resolution:** the signed oriented-support action groupoid has objects
  $(S,c)$ and morphisms $(S,c)\to(T,d)$ given by $S\subseteq T$ plus
  $\sigma\in\{\pm1\}$ with $d=\sigma e_{S,T}(c)$.  Signs compose
  multiplicatively; the antipode is the sign $-1$ involution over a fixed
  support.  The coarse quotient $[c]=\{c,-c\}$ presents primitive lines and a
  single generator but loses the signed path label.  To retain exactly the
  Pass-94 functional-equation sign, use the signed groupoid or the quotient
  plus its $\mathbb Z/2$ sign local system.  Finite signs are visible for
  $N>2$ and collapse at $N=2$.  Machine-verified
  `artifacts/reports/pass101-oriented-support-groupoid-antipode-quotient-check.json`
  (PASS).
- **[Resolved (Pass 102)]** **Signed local system through the finite-adele constant term.**
  Push the $\mathbb Z/2$ sign local system from the oriented-support quotient
  through the primitive collapse and the all-prime complex
  $[\mathbb Q\to\mathbb A_f]$.  Identify the exact boundary/Yoneda class that
  represents biduality on $D\epsilon\simeq\mathbb Q[-1]$, and determine how
  the mod-$2$ sign collapse appears in finite conductor shadows.
  **Resolution:** the sign local system acts on the one-generator unit
  extension
  $\beta=[0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0]$ and the
  all-prime boundary
  $\delta_\epsilon=[0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0]$ by
  multiplication: $\beta\mapsto\sigma\beta$ and
  $\delta_\epsilon\mapsto\sigma\delta_\epsilon$.  The finite shadow is the
  signed Bockstein class $\pm1\in\mathbb Z/N$, visible exactly for $N>2$ and
  collapsed for $N=2$.  The class representing
  $D\epsilon\simeq\mathbb Q[-1]$ carries the same one-sided sign, while
  two-sided sign action squares to $+1$.  No extra finite sign bookkeeping
  or degree-$0$ Weyl morphism is produced.  Machine-verified
  `artifacts/reports/pass102-sign-local-system-adele-boundary-check.json`
  (PASS).
- **[Resolved (Pass 103)]** **Signed boundary naturality under conductor reduction.**
  Package the signed boundary/Yoneda class as a natural transformation over
  finite conductor reductions $M\mid N$.  Compare this with the Pass-95
  CRT-acyclic finite constant-term complexes, and decide whether conductor
  reduction introduces any sign-twisted obstruction beyond the mod-$2$
  collapse already recorded.
  **Resolution:** for finite conductor $N$, the signed Bockstein class is
  $b_N^\sigma=\sigma\in\mathbb Z/N$.  For $M\mid N$ it reduces naturally:
  $\rho_{N,M}(b_N^\sigma)=b_M^\sigma$.  Twisting the finite CRT diagonal by
  $\sigma=\pm1$ gives
  $d_N^\sigma(x)=(\sigma x\bmod p^e)_{p^e\parallel N}$, still an isomorphism
  because $\sigma$ is a unit.  Hence fixed finite signed conductor shadows
  are acyclic and conductor reduction introduces no sign-twisted obstruction
  beyond reduction to modulus $2$.  Support enlargement remains only a
  finite CRT choice/span.  Machine-verified
  `artifacts/reports/pass103-signed-boundary-conductor-naturality-check.json`
  (PASS).
- **[Resolved (Pass 104)]** **Signed pro/solid all-prime boundary object.**
  Assemble the signed finite conductor system into a pro/solid all-prime
  boundary object over $\epsilon=\widehat{\mathbb Z}/\mathbb Z$.  Decide
  whether the orientation double cover survives the all-prime limit as a
  genuine cover/torsor or is absorbed by the $\mathbb Z/2$ local system on the
  boundary line, and identify the minimal categorical package carrying
  support, conductor, and sign without reintroducing a degree-$0$ Weyl map.
  **Resolution:** the compatible residues $\{\sigma\bmod N\}_N$ limit to the
  diagonal integer $\sigma\in\widehat{\mathbb Z}$.  Since $\sigma=\pm1$ is in
  the diagonal copy of $\mathbb Z$, both signs map to zero in
  $\epsilon=\widehat{\mathbb Z}/\mathbb Z$.  Hence the orientation double
  cover does not survive as a nontrivial point-cover of $\epsilon$; it is
  absorbed as the $\mathbb Z/2$ local-system action on the boundary/Yoneda
  line generated by $\delta_\epsilon$, equivalently on
  $D\epsilon\simeq\mathbb Q[-1]$.  The minimal package is the
  oriented-support action groupoid over the finite-conductor pro-system with
  a $B\mathbb Z/2$ boundary-line local system.  Machine-verified
  `artifacts/reports/pass104-signed-pro-solid-boundary-object-check.json`
  (PASS).
- **[Resolved (Pass 105)]** **Support descent for all-prime primitive orientations.**
  Compare the signed pro-boundary stack with support projections and
  zero-extension spans.  Isolate the exact descent/colimit statement for
  all-prime primitive orientations, distinguishing canonical support
  projection from noncanonical support enlargement, and decide whether the
  oriented-support groupoid is best presented as a stack over finite supports,
  a span category, or a pro-object with a boundary-line local system.
  **Resolution:** for $S\subseteq T$, zero-extension
  $e_{S,T}:\mathcal O_S\to\mathcal O_T$ is the canonical covariant operation
  on primitive zero-sum orientations; it preserves primitivity, commutes with
  the antipode, and composes strictly.  Boundary support projection points
  oppositely as $T_T\to T_S$.  A total orientation restriction
  $\mathcal O_T\to\mathcal O_S$ does not exist because deleting coordinates
  can destroy zero-sum, e.g. $(1,1,-2)\mapsto(1,1)$.  Hence all-prime
  primitive orientations are a filtered colimit by zero-padding, packaged as
  a span-stack/Grothendieck object with the $B\mathbb Z/2$ boundary-line local
  system rather than as a plain sheaf with restrictions.  Machine-verified
  `artifacts/reports/pass105-support-descent-primitive-orientations-check.json`
  (PASS).
- **[Resolved (Pass 106)]** **Stackification obstruction for primitive orientations.**
  Compute the precise obstruction to sheafifying or stackifying the
  primitive-orientation assignment over finite supports when restriction maps
  $\mathcal O_T\to\mathcal O_S$ are required.  Formulate the universal
  property of the correct span-stack/left-Kan colimit package and compare the
  antipode quotient $[c]=\{c,-c\}$ with a $B\mathbb Z/2$ classifying stack on
  the boundary line.
  **Resolution:** coordinate deletion has additive defect
  $\Delta_{T,S}(d)=\sum_{p\in S}d_p=-\sum_{p\in T\setminus S}d_p$.  It gives
  a primitive restriction only on the partial domain where the defect
  vanishes and the deleted vector remains primitive; primitivity can fail
  separately, e.g. $(2,-2,1,-1)\mapsto(2,-2)$.  Repairing nonzero defect
  requires a section of $\Sigma_S:\mathbb Z^S\to\mathbb Z$, and no
  support-symmetric integer section exists for $|S|>1$.  The universal object
  is the zero-extension filtered colimit/left Kan extension of primitive
  finitely supported zero-sum functions modulo padded zeros, with the
  antipode quotient retaining the $B\mathbb Z/2$ boundary-line local system.
  Machine-verified
  `artifacts/reports/pass106-stackification-obstruction-primitive-orientations-check.json`
  (PASS).
- **[Resolved (Pass 107)]** **Correction torsors for support-defect repairs.**
  Model choices of defect repair as torsors under
  $\ker\Sigma_S=\{a\in\mathbb Z^S:\sum a_p=0\}$.  Compute transition
  functions for these torsors along support inclusions, decide whether they
  define a Cech/cosheaf cohomology class analogous to the Rosser phantom, and
  test whether ordered or basepointed supports trivialize the class in a way
  compatible with the antipode local system.
  **Resolution:** additive repairs form a free transitive
  $K_S=\ker\Sigma_S$ torsor.  The primitive repair locus is only a primitive
  subset of that torsor and is not stable under all of $K_S$.  Basepointed
  splittings $s_b(n)=n e_b$ trivialize the additive torsor, and transitions
  $s_b(1)-s_a(1)$ are $K_S$-valued coboundaries satisfying the cocycle
  identity.  Since the finite exact sequence
  $0\to K_S\to\mathbb Z^S\to\mathbb Z\to0$ splits after a basepoint and no
  non-Mittag-Leffler tower is present, this is ordinary choice data, not a
  Rosser/cosheaf phantom.  Linear repairs commute with the antipode, so the
  $B\mathbb Z/2$ boundary-line local system is unchanged.  Machine-verified
  `artifacts/reports/pass107-correction-torsors-support-defect-check.json`
  (PASS).
- **[Resolved (Pass 108)]** **Integral equivariant obstruction for repair sections.**
  Classify why $\Sigma_S:\mathbb Z^S\to\mathbb Z$ has no support-symmetric
  integral section for $|S|>1$ even though it has a rational barycentric
  section after tensoring with $\mathbb Q$.  Express this as an obstruction
  in the augmentation sequence under the finite symmetric-group action on
  $S$, and decide whether the denominator/equivariance obstruction is
  independent of the antipode $B\mathbb Z/2$ local system.
  **Resolution:** if $|S|=n$, the invariant lattice
  $(\mathbb Z^S)^{\operatorname{Sym}(S)}$ is $\mathbb Z\mathbf 1_S$, and
  $\Sigma_S(k\mathbf 1_S)=nk$.  Thus invariant integral vectors map to
  $n\mathbb Z$, so no equivariant integral section exists for $n>1$.  Over
  $\mathbb Q$, the barycentric section
  $s_{\mathrm{bar}}(1)=\frac1n\mathbf 1_S$ is equivariant.  An equivariant
  integral lift of $m$ exists iff $n\mid m$, so the obstruction is exactly
  the denominator class $\mathbb Z/n\mathbb Z$.  The antipode is a scalar
  boundary-line sign and commutes with support permutations, so it is
  independent of this denominator obstruction.  Machine-verified
  `artifacts/reports/pass108-integral-equivariant-repair-section-check.json`
  (PASS).
- **[Resolved (Pass 109)]** **Barycentric transition denominators under support inclusions.**
  Compute the transition
  $e_{S,T}s_{\mathrm{bar},S}-s_{\mathrm{bar},T}$ for
  $S\subseteq T$ after tensoring with $\mathbb Q$, determine its denominator
  and kernel class, and compare the resulting rational support-normalization
  data with finite conductor/CRT denominator bookkeeping in the signed
  all-prime boundary package.
  **Resolution:** if $|S|=n$ and $|T|=m$, then the transition has entries
  $(m-n)/(nm)$ on $S$ and $-1/m$ on $T\setminus S$, so it lies in
  $K_T\otimes\mathbb Q$.  Its exact denominator is
  $\operatorname{lcm}(n,m)$.  A finite conductor $N$ clears it exactly when
  $\operatorname{lcm}(n,m)\mid N$.  Clearing by the minimal denominator gives
  a primitive integral zero-sum vector with entries $(m-n)/\gcd(n,m)$ on $S$
  and $-n/\gcd(n,m)$ off $S$.  Chain transitions satisfy the rational
  coboundary identity; finite CRT and signed CRT maps at clearing conductors
  remain bijections, so this is normalized support-comparison data rather
  than a new finite CRT cohomology class.  Machine-verified
  `artifacts/reports/pass109-barycentric-transition-denominator-check.json`
  (PASS).
- **[Resolved (Pass 110)]** **Conductor-cleared primitive transition vectors.**
  Study the primitive vectors
  $\eta_{S,T}=\operatorname{lcm}(|S|,|T|)\tau_{S,T}$ along support chains.
  Determine their exact rescaling law under
  $S\subset T\subset U$, whether their primitive lines or common-conductor
  clearings form useful oriented-support edge data, and how this structure
  interacts with the primitive repair locus inside the additive repair
  torsors from Pass 107.
  **Resolution:** each $\eta_{S,T}$ is a primitive zero-sum vector.  For a
  chain $S\subset T\subset U$, let
  $L_{A,B}=\operatorname{lcm}(|A|,|B|)$ and
  $C=\operatorname{lcm}(L_{S,T},L_{T,U},L_{S,U})$.  Then
  $$
  (C/L_{S,T})e_{T,U}\eta_{S,T}
  +(C/L_{T,U})\eta_{T,U}
  =(C/L_{S,U})\eta_{S,U}.
  $$
  Strict primitive composition holds only in the checked equal-conductor
  cases.  In general the common-conductor sum lies in the additive kernel
  but may be a nonprimitive multiple of the endpoint vector, so the useful
  edge datum is the weighted pair $(L_{S,T},\eta_{S,T})$, not the primitive
  line alone.  This matches the Pass-107 warning that primitive loci are not
  closed under additive torsor operations.  Machine-verified
  `artifacts/reports/pass110-primitive-transition-chain-law-check.json`
  (PASS).
- **[New (Pass 110)]** **Weighted support-edge category.**
  Formalize the weighted oriented-support edge datum
  $(L_{S,T},\eta_{S,T})$ as a small category, double category, or labelled
  span system over finite supports.  Determine whether the conductor weights
  form a useful 2-cocycle or normalization system, and whether this package
  interacts nontrivially with the $B\mathbb Z/2$ boundary-line local system.
- **[Resolved (Pass 111)]** **MacNeille reflection checker repair.**
  Incorporate the newest Claude Code review by adding the proposed
  three-element non-lattice witness, correcting or separating the antitone
  completion extension closure as an $L^{op}$ closure, adding a `reflected`
  field and `principal-unreflected` classification, checking the extension
  condition on principal cuts, and updating the MacNeille checker interface
  and completion/fixed-point notes.
  **Resolution:** the checker now has current rule
  `antitone-dual-lower-cut-v1`,
  $\widehat{\boxtimes}(C)=((\boxtimes[C])^{l_L})^{u_L}$, and keeps legacy
  `antitone-dual-lower-cut-v0` only as a wrong-polarity control.  The
  three-element non-lattice witness has no syntactic fixed point and under
  v1 has the non-principal completion fixed cut `{ 0, a, b }`, classified as
  `nonprincipal-without-syntactic`.  Under v0 it instead gives `{ 0, a }`,
  principal at `a` but unreflected, with two principal-extension failures.
  The three-chain smoke test under v1 is also `principal-unreflected`, with
  syntactic fixed point `m` but completed fixed cut principal at `t`.
  Machine-verified by
  `artifacts/reports/pass111-macneille-reflection-review-check.json` (PASS).
- **[Partially resolved (Pass 112)]** **G2/APS boundary for MacNeille
  completion fixed points on the fixed V-carrier.**
  Pass 112 added finite-table APS A1-A4 fields to the MacNeille reflection
  checker.  The v1 witness `three-element-nolattice-nosynt` still has no
  syntactic $\boxtimes$-fixed point and has the non-principal completion fixed
  cut `{ 0, a, b }`; now the report shows finite A1-A4 hold, while G2 fails.
  Exhaustive enumeration on the same three-element non-lattice carrier found
  G2 separating tables only in the vacuous mode where A2 is absent: 216
  separating tables, 54 separation+G2 tables, and zero
  separation+G2+A2/A124Core/A1-A4 APS tables.  Thus A2 is the first gate on
  this carrier.  This is not yet a global reflection theorem, because
  residuals, completion-stability assumptions, and larger carriers remain
  unchecked.  Machine-verified by
  `artifacts/reports/pass112-macneille-g2-boundary-check.json` (PASS).
- **[Resolved by witness (Pass 113)]** **Four-element MacNeille G2/A2 boundary
  search.**
  Adding a fourth point permits a model with v1 non-principal completion fixed
  cut, no syntactic fixed point, G2, A2, and full finite A1-A4.  The explicit
  witness has order `0<a<b` plus `0<c`, `T=a`, `bottom=0`,
  `boxtimes(0)=boxtimes(a)=b`, `boxtimes(b)=boxtimes(c)=0`, and
  `Box(0)=Box(a)=Box(c)=0`, `Box(b)=b`.  Its completed fixed cut is
  `{ 0, a, b, c }`, non-principal.  The labelled four-element poset search
  found 2784 separation+G2+finite-APS tables across 240 refutability profiles
  and 36 posets.  Machine-verified by
  `artifacts/reports/pass113-four-element-macneille-g2-boundary-check.json`
  (PASS) and the standalone witness report
  `artifacts/reports/macneille-reflection-four-element-g2-aps-nosynt-v1.json`.
- **[Partially resolved (Pass 114)]** **Residual and completion-stability
  boundary for the four-element G2+APS witness.**
  Pass 114 resolves the fixed-carrier/fixed-order residual question
  negatively.  Exhaustive enumeration of all two-sided-unit binary tensors on
  the Pass-113 carrier/order scanned 1,048,576 operation tables.  It found 624
  associative tensors and 56 associative+monotone tensors, but zero tensors
  admitting both left and right residuals.  The first named obstruction among
  surviving units is a non-principal residual fiber:
  `{x : 0 tensor x <= 0} = {0,a,b,c}`, the whole carrier, which is not
  principal because the carrier has no greatest element.  This does not rule
  out order expansions, completion-level tensors, or other four-element
  witnesses.  Machine-verified by
  `artifacts/reports/pass114-four-element-residual-boundary-check.json` and
  `artifacts/reports/pass114-four-element-witness-residuated-tensor-search.json`.
- **[Resolved (Pass 115)]** **Order repair and completion-stability test for
  the four-element residual obstruction.**
  Adjoining the one missing join `U = b v c` as a new top turns the Pass-113
  carrier into the pentagon `N5` (`0<a<b<U, 0<c<U`, the canonical non-modular
  lattice; forced `boxt U = 0`, monotone `box U in {b,U}`).  **Thm 115a
  (trilemma):** (i) A1-A4, G2, FG2 and no-syntactic-fixed-point transfer for
  both box-extensions; (ii) the MacNeille completion-separation is
  **destroyed** -- `N5` is a finite lattice, so all 5 closed cuts are
  principal and the sole completion-fixed cut `down(U)` is principal and
  unreflected (`boxt U = 0 != U`), with no non-principal fixed cut surviving;
  (iii) residuation is repaired -- 115 commutative residuated tensors appear
  (units `a:53, b:18, c:44`), but **zero** with the integral unit `U`, the
  meet tensor failing residuation because `N5` is non-distributive.  The named
  obstruction is therefore precisely (ii): collapse of the completion fixed cut
  to a principal (unreflected) cut.  **Cor 115b:** the missing join is a single
  load-bearing defect shared by the Pass-113 separation and the Pass-114
  residual non-principality; a non-principal MacNeille fixed cut *requires* a
  non-lattice carrier, so no residuation-enabling top-repair can preserve the
  separation on this carrier.  **Rem 115c:** the repair lands on Dedekind's
  `N5`, whose non-distributivity forbids the integral (Loeb) unit, forcing
  every residuated tensor Rosser (non-integral, Pass-51c) -- with no syntactic
  `boxt`-fixed point to attach an integral unit to.  Machine-verified
  `code/scripts/check-pass115.py` ->
  `artifacts/reports/pass115-top-repair-n5-check.json`.
- **[Resolved (Pass 116), negatively]** **Join-defect-preserving (non-lattice)
  repair: can a principal residual fiber coexist with a non-principal completion
  fixed cut?**  Thm 115a shows a *lattice* top-repair cannot: finiteness forces
  every cut principal.  The weaker repair -- adjoin a top `U` above two
  incomparable minimal upper bounds `m,n` of `{b,c}` (doubled cover
  `L1 = {0,a,b,c,m,n,U}`, bounded but non-lattice: `b v c` unattained) -- was
  tested and the coexistence **fails** (Thm 116a, join-defect conservation).
  The non-principal cut `{0,a,b,c}` is retained but is **not** `boxt_hat`-fixed:
  the orbit collapse `boxt b = boxt c = 0` forces
  `boxt_hat(b v c) = boxt_hat(b) ^ boxt_hat(c) = bottom < b`, so the unique fixed
  cut is the principal top `down(U)` and separation dies.  Residuation is not
  repaired either -- the integral census (345600/2350/145/**0** residuated)
  finds the Pass-114 fiber merely relocated to `{0,a,b,c,m,n} = L1 minus {U}`,
  non-principal via the antichain `{m,n}`.  The absent join is a conserved charge:
  a single top pushes it into principality (N5, Rosser tax), a doubled cover keeps
  the non-principal cut but pushes the defect into `boxt_hat`-unfixedness and a
  top-less fiber one level down.  Machine-verified
  `code/scripts/check-pass116.py` ->
  `artifacts/reports/pass116-doubled-cover-coexistence-check.json` (PASS).
- **[Resolved (Pass 117), negatively]** **Plateau-join repair: can an incomparable
  `boxt`-2-cycle carry a non-principal completion-fixed cut on a bounded non-lattice
  carrier?**  NO -- for a *parity* reason that unifies Pass 116.  On the minimal
  bounded realization, the **hexagon** `H = {0,x,y,m,n,U}` (`x || y`, `m || n`,
  each of `x,y` below each of `m,n`), the MacNeille completion identifies
  `x v y` with `m ^ n` into a single non-principal middle cut `w = {0,x,y}`, and
  the antitone extension gives
  `boxt_hat(w) = boxt x ^ boxt y = y ^ x = x ^ y = 0 = bottom`, so `w` is **not**
  fixed; in fact `boxt_hat` is globally **fixed-point-free** (Thm 117a).  The
  swap 2-cycle offers a length-2 self-duality, not a fixed point -- the
  `2^n`-complementation phenomenon.  Corollary 117b unifies this with Thm 116a via
  the antitone De Morgan join law `boxt_hat(x v y) = boxt x ^ boxt y`: a fixed
  join needs images ABOVE the summands, which no orbit running *through* the
  summands (chain OR swap) can supply.  Machine-verified for `boxt 0 = U`,
  `boxt 0 = m`, and the antichain-4 double-2-cycle; a control carrier with a
  genuine `p = boxt p` DOES yield a fixed cut, isolating the operative variable.
  `code/scripts/check-pass117.py` ->
  `artifacts/reports/pass117-two-cycle-plateau-fixed-point-free-check.json`.
- **[Resolved (Pass 118)]** **Self-dual-seed necessity.**  Residue (ii) of the
  Pass-117 problem.  Thm 117c's necessity is **NOT strict**: FP-synt is
  UNNECESSARY, and the operative variable is neither oddness nor a carrier fixed
  point but where the antitone map routes the MacNeille frontier.  On the SAME
  hexagon `H`, with NO carrier synt-FP, the **frontier-crossing** map
  `boxt 0=U, boxt x=m, boxt y=n, boxt m=y, boxt n=x, boxt U=0` (orbit
  `(0 U)(x m y n)`, EVEN) is antitone and makes `w = {0,x,y} = x v y = m ^ n` a
  genuine `boxt_hat`-**fixed** cut.  **Lemma 118a** (frontier De Morgan law):
  `boxt_hat(w) = /\_{f in F} boxt f` over the lower frontier `F = max(w)`.
  **Theorem 118b** (frontier-onto criterion): a non-principal cut `w` with
  frontier pair `(F,G)` is fixed **iff** `boxt[F] = G` (lower frontier ONTO
  upper frontier) -- carrier-fixed-point-free.  **Corollary 118c**: the Pass-117
  Tarski-interval criterion stands, but its "seed = Jeroslow point" clause is
  false; the self-dual seed is a NEW cut, completion-generated.  Pass 117's
  plateau failed only because it chose `boxt[F]=F` (images collapse to bottom);
  `boxt[F]=G` puts the image-meet at `w`.  Census: 273 antitone synt-FP-free
  hexagon maps, 22 fix `w` (all `boxt[F]=G`), 4 two-way swaps, 0 needing a
  carrier fixed point.  `code/scripts/check-pass118.py` ->
  `artifacts/reports/pass118-completion-generated-selfdual-seed-check.json`.
- **[Resolved (Pass 119), (i)] / [Partially resolved (Pass 119), (ii)]** _(was
  [New (Pass 118)])_ **Higher-frontier crossing + arithmetic phantom Henkin.**
  **(i) RESOLVED (Pass 119): onto is sufficient but NOT necessary at `|F|=3`.**
  On the complete-bipartite bounded carrier `K33 = {0,f1,f2,f3,g1,g2,g3,U}`
  (`0` bottom, `U` top, `f_i<g_j` for ALL `i,j`), the MacNeille completion has
  9 cuts, exactly ONE non-principal, `w = {0,f1,f2,f3} = f1 v f2 v f3 =
  g1 ^ g2 ^ g3`, frontiers `F={f1,f2,f3}`, `G={g1,g2,g3}`.  **Theorem 119b
  (meet criterion, exact for all `|F|`):** `w` is `boxt_hat`-fixed **iff**
  `/\ boxt[F] = w` (Lemma 118a).  **Theorem 119a:** `boxt[F]=G` still SUFFICES
  (402 census witnesses) but is NOT necessary -- witness `D` maps
  `boxt f1=g1, boxt f2=g2, boxt f3=U` (the NON-frontier top), antitone,
  synt-FP-free, `boxt[F]={g1,g2,U} != G`, yet `/\ boxt[F] = g1 ^ g2 = w`
  (2412 census witnesses non-onto, 1206 with a genuine non-frontier image).
  **Theorem 119c (sharp form):** with `mu(w)=` minimal size of a meet-generator
  `G' subset G` (`/\ G' = w`), `w` is fixed **iff** `|boxt[F] cap G| >= mu(w)`;
  so necessity of `boxt[F]=G` holds IFF `w` is meet-IRREDUNDANT (`mu=|G|`) --
  hexagon `mu=2=|G|` (regression: 22/22 onto), K33 `mu=2<3=|G|` (`G` redundant,
  any two `g`'s meet to `w`).  **Cor 119d:** no fixing map has `boxt[F]` disjoint
  from `G` (`|boxt[F] cap G|` distribution `{2:2412, 3:402}`); `>=2` upper-frontier
  witnesses are mandatory.  Census: 7609 antitone synt-FP-free maps on K33.
  `code/scripts/check-pass119.py` ->
  `artifacts/reports/pass119-triple-crossing-frontier-meet-criterion-check.json`.
  **(ii) PARTIALLY RESOLVED (Pass 119) -- Rem 119e.** The completion-generated
  self-dual `w` is a Henkin/Rosser fixed point realized only in the Lindenbaum
  completion (no carrier `p = neg Box p`); `boxt[F]=G`/`boxt[F] supseteq` a
  meet-generator is the Rosser "route to an ordered higher witness" move (vs
  paradoxical `boxt[F]=F`), and meet-REDUNDANCY (`mu<|G|`) is Rosser economy: a
  meet-generating *pair* of comparison witnesses suffices, not a complete
  matching.  *Left open:* promote this to a functorial Rosser-economy statement
  (a `mu`-graded refinement of the Pass-53/57 Löb/Rosser functor `L_{(-)}`).
- **[Resolved (Pass 120)]** _(was [New (Pass 119)])_ **Asymmetric frontiers and
  the meet-generator hypergraph -- FRONTIER MEET-RIGIDITY.**  Both residues
  settled, the second NEGATIVELY (correcting the anticipation of a variable
  `mu`-spectrum).  **(i) `|F| != |G|` crossing.** On `K_{2,3}^{0,U}` the unique
  non-principal cut `w={0,f1,f2}=f1 v f2 = g1 ^ g2 ^ g3` has `|F|=2`, `|G|=3`,
  yet `mu(w)=2` and `H_min(w)=`complete `K_3`.  The expansion crossing succeeds:
  a 2-element `F` maps onto a meet-generating PAIR `{g1,g2} subsetneq G` and fixes
  `w`.  But the slack `s(w)=|F|-mu=0` FORCES injectivity (Thm 120c): every fixing
  `boxt` sends `f1,f2` to two DISTINCT frontier `g`'s -- census 1362 antitone
  synt-FP-free maps, 174 fix `w`, 0 with a `U`-image, 0 with a repeat,
  `|boxt[F] cap G|` all `=2`; the Pass-119 slack freedom (`f_3 -> U`) is spent.
  **(ii) Meet-generator hypergraph and `mu`-spectrum -- Thm 120a/b/d.** Frontier
  meet-rigidity (Thm 120a): in ANY MacNeille completion distinct upper-frontier
  `g,g'` meet to `w` (else `g ^ g'` is a strict upper bound of `w` below `g`,
  breaking minimality), dually distinct lower-frontier elements join to `w`.
  Hence `H_min(w)=binom(G,2)` and `mu(w)=2` identically (Cor 120b), and the ONLY
  realizable frontier hypergraphs are complete graphs `K_n` (Thm 120d) -- no
  non-uniform and no `k>=3`-uniform antichain occurs; the hypergraph is NOT a
  free invariant, determined by `|G|` alone.  Self-healing (Cor 120e): forcing
  `g2 ^ g3 = z>w` merely inserts `z` into the frontier (`G={g1,z}`), rigidity
  restored.  Rosser-economy (Rem 120f): the minimal witness budget of a
  completion-generated Henkin/Rosser cut is always exactly `2`.  Machine:
  `code/scripts/check-pass120.py` ->
  `artifacts/reports/pass120-asymmetric-frontier-meet-rigidity-check.json`
  (A basic+census, B `K_{3,3}` slack-1 contrast, C rigidity survey over 7
  bipartite carriers with 0 violations, D self-healing; overall PASS).
- **[Resolved (Pass 121), (i) NEGATIVELY] / [Partially resolved (Pass 121), (ii)]**
  _(was [New (Pass 120)])_ **Completion-universality of frontier meet-rigidity,
  and the dual join-rigidity's arithmetic.**
  **(i) RESOLVED (Pass 121), NEGATIVELY -- rigidity is COMPLETION-RELATIVE.**
  Frontier meet-rigidity (Thm 120a) is NOT a completion-universal law; it is a
  consequence of MacNeille's SIMULTANEOUS join+meet density.  Recomputing
  `H_min(w)` for `K_{2,3}^{0,U}` inside three completions (**Thm 121a**):
  MacNeille `overline L` (= canonical extension `L^delta`, since a finite poset
  has only principal filters/ideals -- **Thm 121b**) is meet-rigid, `mu(w)=2`,
  `H_min=K_3` (reproduces Pass 120); the ideal/downset completion `D(L)` (13
  elements) STAYS meet-rigid (`g_i ^ g_j = downset {0,f1,f2} = w`), `mu(w)=2`, but
  is not minimal -- it adjoins the free JOINS `g_i v g_j < U`, breaking the DUAL
  (coatom) join-frontier instead; the filter/upset completion `F(L)` (order-dual,
  reverse inclusion, meet = union of upsets) BREAKS meet-rigidity -- the pairwise
  meets `g_i ^ g_j = {g_i,g_j,U} = z_ij` are THREE distinct new elements strictly
  above `w = {g1,g2,g3,U}`, so `H_min(w) = {{g1,g2,g3}}` is 3-UNIFORM and
  `mu(w)=3=|G|`, UNFREEZING Cor 120b and REALIZING the `k>=3`-uniform hyperedge
  Thm 120d called impossible.  **Thm 121c (`K_{n,m}` law):** each one-sided
  completion unfreezes exactly ONE frontier -- filter `F(K_{n,m})` gives
  `mu(w)=m`, ideal `D(K_{n,m})` keeps `mu(w)=2` but the dual join-multiplicity is
  `n`; MacNeille/`L^delta`, dense on both sides, is the unique completion freezing
  BOTH.  So Thm 120d's "only complete graphs `K_n`" is a MacNeille/canonical
  theorem, silently assuming both densities.  **(ii) PARTIALLY RESOLVED (Pass 121)
  -- Rem 121d.**  The dual join-rigidity `f_i v f_j = w` (pairwise joins of the
  consistency-like lower frontier collapse to the Henkin cut `w`) is the
  completion shadow of "any two `Con^orb` iterates (Pass-69) already generate the
  phantom limit"; but `D(L)` shows this collapse is NOT order-forced (join-free
  completion keeps `f_i v f_j` distinct), so it is a property of MEET-density
  (Lindenbaum both-dense completion), not of the bare consistency order.  *Left
  open:* the exact `Con^orb`-tower identification of the meet-density collapse.
  Machine: `code/scripts/check-pass121.py` ->
  `artifacts/reports/pass121-completion-relative-frontier-rigidity-check.json`
  (PASS: macneille_rigid_mu2, ideal_meet_rigid_mu2, filter_breaks_rigidity_mu3,
  canonical_eq_macneille).
- **[Resolved (Pass 122); (i) POSITIVE at distinguished level / NEGATIVE at true frontier; (ii) REFUTED]**
  _(was [New (Pass 121)])_ **Two-sided-free completion and POSITIVE realization;
  the `Con^orb` identification.**  The realization question splits by WHICH family
  one measures over.  **(i-a) POSITIVE (distinguished family) -- Thm 122c.** Every
  finite antichain hypergraph `H` on `[m]` IS realized exactly as `H_min^G(w)` over
  the distinguished coatom family `G={g_1,...,g_m}` in the ideal completion
  `D(L(H))` of an explicit carrier: atoms `=` core `{c_1,c_2}` (shared by all
  `g_j`, giving `w=c_1 v c_2` non-principal) plus one fan atom `x_I` per maximal
  `H`-independent set `I subseteq [m]`, with `x_I < g_j` iff `j in I`; then
  `/\_{j in S} g_j = w` iff no maximal independent set contains `S` iff `S` contains
  an `H`-edge, so `H_min^G(w)=H` on the nose (atom cost `2+|MaxInd(H)|`).  Verified
  for complete `K_3`, non-uniform `{12,234}` (mu-spectrum `{2,3}`), 3-uniform
  `{123}`, all triples on `[4]`, disjoint `{12,345}`.  So Thm 120d's "only `K_n`"
  becomes "EVERY antichain hypergraph" once meet-density is dropped.  **(i-b)
  NEGATIVE (true frontier) -- Thm 122a.** Over the TRUE frontier
  `G_*(w)=min((w)^u\w)` rigidity is UNCONDITIONAL: the order-theoretic proof
  (`g/\g'` strictly between `w` and `g` contradicts minimality of `g`) uses NO
  MacNeille hypothesis, so distinct true-frontier elements meet to `w` in EVERY
  completion, `H_min^{G_*}(w)=K_{|G_*|}`, `mu_*(w)=2` always (verified MacNeille +
  ideal `K_{n,m}`, 2000 random posets, 0 violations).  **Exact invariant --
  Thm 122d:** `H_min^G(w)=K_{|G|}` iff `G=G_*(w)` iff the completion is meet-dense
  at `w` (no element strictly between `w` and any `g in G`) -- precisely the
  hypothesis Thm 120d silently used.  **Cor 122b:** Pass 121's "completion-relative"
  `mu=3` (filter) was a distinguished-family artifact -- the carrier coatoms cease
  to be minimal upper bounds (`z_ij=g_i/\g_j` sit strictly between `w` and `g_i`).
  **Obstruction 122e:** since Thm 122a is unconditional, NO completion yields a
  non-complete TRUE-frontier meet-hypergraph, so "two-sided-free realization" is
  vacuous for frontier invariants and trivial for distinguished ones.  **(ii)
  REFUTED -- Rem 122f.** The `Con^orb_n` tower (Pass-69) is a CHAIN; a chain-cut is
  frontierless (`max(w cap L)=emptyset`) and its pairwise joins are maxima `=` a
  single iterate, ALWAYS strictly below the limit, in EVERY completion -- so
  "pairwise consistency joins collapse to the phantom limit" NEVER holds for the
  tower; meet-density is irrelevant.  The Pass-120/121 collapse `f_i v f_j = w`
  belongs to the ANTICHAIN-frontier phantom `|F|>=2` incomparable -- a bouquet of
  order-INCOMPARABLE Rosser-type consistency twins `c_1,c_2` (distinct
  witness-orderings) whose disjunction is the Henkin cut, NOT iterated consistency.
  Machine: `code/scripts/check-pass122.py` ->
  `artifacts/reports/pass122-two-sided-realization-check.json` (overall PASS).
- **[Resolved (Pass 123)]** _(was [New (Pass 122)])_ **The independent-Rosser-twins
  phantom inside `ConLat_T`.**  All three sub-questions settled, with a parity
  CORRECTION of Rem 122f.  **(i) Realization + correction (Thm 123a).** On the
  Pass-117 hexagon (carrier `{0,x,y,m,n,U}`, non-lattice) the MacNeille completion
  inserts the middle cut `w=x v y`; by the antitone De Morgan law (Thm 117a)
  `boxt_hat(w)=boxt x ^ boxt y`.  A pure 2-twin frontier is a FIXED cut ONLY via the
  CROSS map (`boxt x=m, boxt y=n`, images strictly ABOVE the summands, Cor 117b); the
  front-internal SWAP (independent witness-orderings EXCHANGING) collapses `w` to
  `bot` (Pass-117a).  So Rem 122f's "Henkin/Rosser FIXED cut" was an overstatement
  for the bare bouquet -- fixedness is the cross regime.  Machine census: of 477
  antitone self-maps 22 fix the middle cut, ALL 22 with NO carrier `p=boxt p`, 38
  collapse to `bot`.  Hence the Thm-117c odd self-dual seed can be
  COMPLETION-MANUFACTURED -- a POSITIVE answer to Pass-118(ii) on the hexagon (see
  next item).  **(ii) Derivability cost + non-artifact (Thm 123b) & dictionary
  (Thm 123c).**  Over GL (`D1+D2+D3`) the consistency fixed point is unique up to
  provable equivalence (de Jongh-Sambin), `|F_*(w)|=1`, no bouquet; a Rosser bouquet
  FORCES `¬D2`.  Guaspari-Solovay 1979 give the arithmetic witness (independent
  Rosser sentences from independent witness-orderings; `Pr_R` satisfies `D1` not
  `D2`).  The bouquet is an ANTI-artifact: arithmetic `Box_T` fails the internalized
  disjunction property `Box(a v b) -> Box a v Box b` = the De Morgan law, so the
  Henkin cut survives precisely in the gap where the abstract MacNeille `boxt_hat`
  (which obeys De Morgan) would collapse it.  The distinguished-vs-true-frontier gap
  (Thm 122d) IS Guaspari-Solovay witness-comparison nonuniqueness: witness ordering =
  distinguished family (free, Thm 122c), `Pi_1` equiconsistency = rigid true frontier
  (`mu_*=2`, Thm 122a), meet-density = `D2`/normality.  **(iii) `alpha(H)` optimal
  (Thm 123d/Cor 123e).**  Atom-support lemma (each certifying atom's support is
  `H`-independent; distinct maximal independent sets need private atoms) forces
  `alpha_phantom(H)=2+|MaxInd(H)|`, matched by Constr 122c hence OPTIMAL; the
  single-core principal realization costs `1+|MaxInd(H)|`, so the phantom/bouquet tax
  is EXACTLY one core atom = one extra witness-ordering.  Machine:
  `code/scripts/check-pass123.py` ->
  `artifacts/reports/pass123-independent-rosser-twins-phantom-check.json` (PASS).
- **[Resolved (Pass 123), positively; carried from Pass 117/118(ii)]** **Can a
  MacNeille completion manufacture a non-principal `boxt_hat`-fixed cut WITHOUT a
  carrier-level Jeroslow point `p=boxt p`?**  YES on the hexagon (Thm 123a census):
  every one of the 22 antitone maps fixing the middle cut is carrier-SEEDLESS, so
  completion-separation is genuine, NOT a conservative shadow of a carrier fixed
  point.  This refines Thm 117c: the "odd self-dual seed" it demands is a property of
  the COMPLETION (the created cut `w` with `boxt_hat(w)=w`), not of the carrier.
  Note the R_{2k} general fixed-point-freeness residue (`boxt[F]=F` front-internal,
  next item) is the COMPLEMENTARY collapsing regime and remains open.
- **[Resolved (Pass 124)]** _(was [New (Pass 123)])_ **The odd-seed Rosser
  bouquet-with-center.**  All three sub-questions settled, plus a naive dichotomy
  REFUTED-then-scoped.  **(i) Carrier-join criterion (Thm 124a).** The Henkin center
  is CARRIER-SEEDED iff the bouquet disjunction `c_1 v c_2` exists in the carrier.
  On the six-element lattice `L*` (`0<c_1,c_2,p`; `c_1,c_2<w`; `w<U`; `p<U`, with
  `w=c_1 v c_2` a GENUINE element) the antitone `boxt: 0->U, c_1->w, c_2->U, w->w,
  p->p, U->0` has `boxt w=w` (carrier Jeroslow fixed cut = Henkin center), separated
  twins (`boxt c_1 != boxt c_2`), AND a detached carrier seed `p=boxt p` -- a SEEDED
  bouquet-with-center, sharply contrasting the hexagon's SEEDLESS completion cut
  (Thm 123a, 22/22 seedless).  Since `ConLat_T` is Boolean/Lindenbaum, `rho_1 v
  rho_2` is a genuine sentence, so the arithmetic bouquet ALWAYS lives in the seeded
  regime; the seedless hexagon cut is an artifact of a non-lattice-complete carrier.
  **(ii) De-Morgan collapse (Thm 124b), the derivability profile (Thm 124c).**  A
  tempting dichotomy -- "`boxt w=w` forces fused twins when `w` is covered only by
  `U`" -- is FALSE for general antitone maps (census: 28 of the 65 `boxt`-`w`-fixing
  `L*` maps are separated; a general antitone `boxt` is NOT a lattice dual-hom and
  ignores the De Morgan law, mirroring non-normal arithmetic `¬Box_R`).  Correctly
  SCOPED to the NORMAL subclass (antitone lattice dual-endomorphisms = the abstract
  shadow of `D2`): 17 normal maps, 4 fix `w`, `0` separated -- so normal `+ boxt w=w
  => FUSED twins`, and the separated seeded bouquet-with-center exists ONLY in the
  `¬D2` regime (the carrier shadow of Thm 123b).  Modal profile `D1 ^ ¬D2` in the
  Guaspari-Solovay logic `R`; the base `Box` stays `GL` and `D3` is NOT forced to
  fail (fixed-point uniqueness needs the full `GL` package -- normality AND Loeb --
  so `¬D2` alone liberates the twins with `D3` free; cf. `K4`/`S4` where `p<->Box p`
  has non-`top` solutions).  **(iii) Phantom tax (Cor 124d).**  `alpha_phantom=
  2+|MaxInd(H)|`, `alpha_principal=1+|MaxInd(H)|`, so the tax `=1` for EVERY `H`:
  the fan atoms are shared, only the core differs (`1->2`); connectedness of the
  independence complex changes `|MaxInd|` (absolute `alpha`) but NOT the tax
  (machine-confirmed on 6 hypergraphs incl. disconnected `MaxInd`-overlap graphs).
  `Fix(boxt)` always an antichain (`L*` 638 maps, hexagon+center 5040 maps).
  Machine: `code/scripts/check-pass124.py` ->
  `artifacts/reports/pass124-odd-seed-bouquet-with-center-check.json` (PASS).
- **[Resolved (Pass 125)]** _(was [New (Pass 124)])_ **Concrete `Box_R`-`D3` status,
  exhaustive `alpha`, and the infinite carrier-join.**  All three settled; Thm 124c's
  non-committal "`D3` not forced to fail" is SHARPENED by splitting `D3`.
  **(i) D3 dichotomy (Thm 125a) + the exact logic (Thm 125b).**  The Rosser box
  `Box_R phi := exists p(Prf(p,phi) ^ forall q<=p ¬Prf(q,¬phi))` is `Sigma_1`
  (bounded guard); hence the HETEROGENEOUS `Box_R phi -> Box(Box_R phi)` is an
  UNCONDITIONAL theorem of every `T >= I Sigma_1` (`Sigma_1`-completeness), while the
  HOMOGENEOUS `Box_R phi -> Box_R Box_R phi` is `R`-INDEPENDENT (Guaspari-Solovay
  completeness + Arai 1990: one Rosser predicate satisfies it, one refutes it).
  Profile: `D1 ^ ¬D2 ^ D3^mix`, `D3^hom` free.  `D2` cannot be re-added:
  `D1^D2^D3^hom = GL` forces de Jongh-Sambin uniqueness, `|F_*(w)|=1`, killing the
  twins.  The logic is GS `R` with `Box_R A := (A -< ¬A)`; the twin-plus-center is a
  model of `R + Con + {two -<-independent fixed points}` (consistent by GS
  non-uniqueness).  Kripke-with-`-<`: `GL` trees (irreflexive, converse-well-founded)
  + a linear witness-priority on successors; the center `w` is a CUT, never a world.
  **(ii) Exhaustive `alpha` identity (Thm 125d).**  Reducing a non-principal bouquet
  to its atom/coatom incidence, `alpha(H) = 2+|MaxInd(H)|` is EXACT (blocking/set-
  cover: each proper fan atom's independent label covers `<=1` maximal independent
  set, forcing `>=|MaxInd|` fan atoms; `mu=2` non-principality forces `>=2` core).
  Exhaustive enumeration of ALL incidence systems below budget: ZERO realizations for
  all six samples; `min_atoms = 2+|MaxInd|` exactly (`single{12}`/`path`=4, `K3`/
  `3-unif`/`nonunif`=5, `disjoint{12,345}`=8).  Upgrades the Thm-123d lemma to an
  identity.  **(iii) Infinite carrier-join dichotomy (Thm 125c).**  For an
  `omega`-bouquet with directed join `w=\/c_n` and `boxt c_n >= w`: join-continuity of
  `boxt` (`<=>` ML `<=>` nFG2, Thm 48b/55c) FORCES `boxt w = /\ boxt c_n`
  (seeded-HONEST iff the directed meet attains `w`); a join-continuity FAILURE at the
  cover gives a FREE `boxt w=w` = a completion-manufactured phantom (Pass-55 solenoid,
  non-ML `(Z,xm)`, `varprojlim^1=hatZ_m/Z`).  So Thm 124a's finite seeded/seedless
  split bifurcates into `{seeded-honest, seeded-phantom, seedless}` -- the middle cell
  invisible on finite carriers.  Cor 125e: across (i)-(iii) the Rosser object is
  honest one level down and free/phantom at the diagonal step (*Löb rigidifies;
  Rosser liberates, by exactly one degree of freedom at self-reference*).  Machine:
  `code/scripts/check-pass125.py` ->
  `artifacts/reports/pass125-rosser-d3-exhaustive-alpha-carrier-join-check.json`
  (PASS).  _(Archival: a 2026-07-06 `pass125-*` report was found orphaned -- clobbered
  append per `aps-run-sync-hazard`; reconfirmed and re-recorded here.)_
- **[Resolved (Pass 126)]** _(was [New (Pass 125)])_ **The `D3^hom` frontier and the
  infinite-fan `alpha`.**  Both parts settled.
  **(i) Concrete `D3^hom` status (Thm 126a).**  The least-witness `Box_R` REFUTES
  `D3^hom`.  `sigma := Box_R phi` is `Sigma_1`, so provable `Sigma_1`-completeness
  yields only the MIXED step `sigma -> Box sigma`; the HOMOGENEOUS step `Box_R sigma`
  requires an internally-certified Rosser guard on a proof of `sigma`, which `T`
  cannot supply (G2 blocks internal consistency).  Explicit failure: in any
  `M |= T + Box_T bot` a spurious short witness `s_0 <= r` for `¬sigma` breaks the
  guard, so `M |= Box_R phi ^ ¬Box_R Box_R phi` and `T |/- Box_R phi -> Box_R Box_R
  phi`.  (The failure is of the CONDITIONAL; for provable `phi` both sides are
  theorems by `D1` -- exactly the `Sigma_1`-completeness vs provable-`Sigma_1`-
  completeness gap.)  Arai (1990) reorders witnesses to REPAIR `D3^hom` while STILL
  dropping `D2` (monotonicity would revive Loeb and refute Rosser consistency
  `T |- ¬Box_R bot`).  Modally `D3^hom = axiom 4`, `D2 = axiom K`: the
  `D3^hom`-compatible Rosser logics are exactly the transitive, Rosser-consistent,
  NON-normal ones (`4 in L`, `¬Box bot in L`, `K notin L`) -- an `4`-containing,
  `K`-omitting band of the Kurahashi (2016) range; the least-witness box realizes an
  `4`-free point, Arai an `4`-containing one.
  **(ii) Infinite `alpha` (Thm 126b) + compactness fusion (Thm 126c, Cor 126d).**
  The identity `alpha(H) = 2 + |MaxInd(H)|` survives VERBATIM once `+` is CARDINAL
  addition; for infinite `|MaxInd|` the `+2` core tax is ABSORBED, `alpha =
  |MaxInd(H)|`.  `alpha` is UNBOUNDED by `|V(H)|`: the countable perfect matching
  `M_omega` (edges `{2i,2i+1}`) has `|MaxInd| = 2^aleph_0`, forcing a continuum-atom
  carrier over `aleph_0` vertices.  The Next-step's naive guess "honest `iff` finitely
  many facets" is FALSE (Thm 126c): seeded-honest `<=>` the descending
  `boxtimes`-facet tower is Mittag-Leffler (`= nFG2` at the frontier, Thm 55c), NOT
  `|MaxInd| < aleph_0`; an infinite fan with eventually-constant images is honest, so
  compactness is SUFFICIENT but not necessary; the strictly seeded-phantom cell is the
  non-ML dilation tower (`lim^1 = hatZ_m/Z`).  Cor 126d: a Rosser bouquet's
  honest/phantom cell is decided by the SAME `4`-vs-`¬4` degree of freedom as `D3^hom`
  (Arai = seeded-honest, least-witness = seeded-phantom).  Machine-verified
  `code/scripts/check-pass126.py` ->
  `artifacts/reports/pass126-d3hom-frontier-infinite-alpha-check.json` (overall PASS).
- **[Resolved (Pass 127), (i)-(ii); (iii) partial]** _(was [New (Pass 126)])_
  **Arithmetic realization of the honest vs phantom Rosser
  bouquet, and the `PL(Box_R^{Arai})` pin.**  (i) Build the seeded-HONEST and
  seeded-PHANTOM Rosser bouquets as genuine arithmetic APS of a SPECIFIC pair --
  Arai's `D3^hom`-predicate (facet tower ML, stabilizing at the Loeb index) versus the
  least-witness one (non-ML tower carrying the `varprojlim^1 = hatZ_m/Z` Rosser
  torsor).  (ii) Realize the Thm-126c ML-vs-compact GAP arithmetically: an infinite
  family of Rosser fixed points with eventually-constant witness comparison (the
  "infinite but ML" honest cell) DISTINCT from the finitely-many-fixed-points compact
  cell.  (iii) Pin `PL(Box_R^{Arai})` inside the Kurahashi (2016) range: is it a
  single named transitive non-normal logic (candidate `R + 4`), and does adjoining `4`
  to `R` REDUCE the multiplicity of `-<`-independent Rosser fixed points that Thm 125b
  needed for the twin-plus-center model (does `D3^hom` partially re-rigidify what `¬D2`
  liberated)?
  **Resolution (Pass 127).** (i)-(ii) DONE. **Thm 127a:** the arithmetic honest/phantom
  dichotomy IS a derivability identity, `D3^hom(Box_R) <=> nFG2-schema(boxtimes_R) <=>
  facet tower Mittag-Leffler <=> no phantom`; Arai's `D3^hom`-predicate realizes the
  seeded-HONEST bouquet (stabilizing at the axiom-`4`/transitivity index -- **corrected:
  NOT the Loeb index**, Arai's box being Rosser-consistent hence non-Loeb), the
  least-witness box the seeded-PHANTOM one (`varprojlim^1 = hatZ_m/Z`). **Thm 127b:** the
  phantom is `rad`-invariant (`m` numbering-dependent, `rad(m)` well-defined; `m>=2 =>`
  phantom, `m=1 =>` none). **Thm 127d:** the ML-vs-compact gap is realized arithmetically
  (an infinite-but-ML Arai-Rosser fixed-point family is honest, distinct from the finite
  compact-honest and the infinite phantom cells); order-isomorphic bouquets split
  honest/phantom by the `4`-vs-`¬4` datum alone, and at `omega_1` twins honesty is
  ZFC-independent (Thm 60d). (iii) PARTIAL. **Prop 127e:** `PL(Box_R^{Arai}) ⊇ R^- + 4 +
  ¬Box bot`, and by **Thm 127c** (vertical/horizontal decoupling: `4` rigidifies the
  nesting tower, `¬K` governs the twin count; de Jongh-Sambin uniqueness needs `K` not
  `4`) adjoining `4` does **NOT** reduce the Thm-125b twin multiplicity -- the
  twin-plus-center model survives verbatim in `R+4`. The single-named-logic
  identification `= R+4` is left open (needs a Solovay/arithmetic-completeness theorem for
  the Arai predicate). Machine-verified `code/scripts/check-pass127.py` ->
  `artifacts/reports/pass127-honest-phantom-rosser-bouquet-decoupling-check.json` (PASS).
- **[Resolved (Pass 128), (i)-(iii) with transferred obligations]** _(was
  [New (Pass 127)])_ **The `R+4` completeness pin, the canonical phantom prime, and the
  `omega_1`-honesty degree.** (i) Prove or refute `PL(Box_R^{Arai}) = R + 4` EXACTLY via a
  Solovay-style arithmetic-completeness theorem for Arai's `D3^hom`-predicate (which
  pure-`Box_R` schemata beyond `4` are forced -- does `4 + ¬K` entail any Loeb-fragment on
  `Sigma_1` sentences?). (ii) Pin the exact phantom multiplier `m` of the standard
  least-witness box under a FIXED numbering: is `rad(m) = {2}` forced, making the canonical
  arithmetic Rosser phantom exactly `hatZ_2/Z`? (iii) Locate the Thm-127d `omega_1`-honesty
  independence degree in the `b = aleph_1` vs `MA_{aleph_1}` bracket: a named statement
  (Suslin tree, `add(M) = aleph_1`)?
  **Resolution (Pass 128).** (i) **Thm 128a:** the pin DISSOLVES at the pure-`Box` level.
  `PL(Box_R^A)` splits as (pure-`Box` part) x (Guaspari-Solovay `-<`-fragment). The only
  candidate separating principle -- a witness-race well-foundedness schema `WO` (proofs are
  finite, every descending witness-race terminates) -- is PURE-`Box`-INEXPRESSIBLE: the
  normal companion is `\subseteq K4D`, and every serial+transitive frame is converse-ILL-
  founded (seriality => infinite ascending `R`-chain), so `WO`/Loeb is unsatisfiable over
  `K4D` (machine: 75/75 finite serial+transitive frames refute a Loeb instance, all
  reflexive-cyclic). Hence pure-`Box` `PL(Box_R^A) = R+4`; axiom `4` adds no pure-`Box`
  content, and the residual completeness is the CLASSICAL GS `-<`-fragment obligation, NOT
  Arai-specific. Full Loeb `notin PL` (would kill `¬Box bot`), so `PL \subsetneq R+4+Loeb`
  strictly. NO Loeb-fragment on `Sigma_1` separates them (the attached-cone "Loeb" is
  ML-stabilization already provable in `R+4`). (ii) **Thm 128b:** `rad(m) = {2}` is NOT
  absolutely forced; `m = m_race * m_enc`, `m_race = 2` the proof-vs-refutation RACE arity
  (numbering-independent, so `2 in rad(m)` ALWAYS), `m_enc` the coding overhead. `rad(m) =
  {2}` `\iff` dyadic coding (canonical phantom `hatZ_2/Z`); Godel prime-power coding gives
  the maximal `hatZ/Z`. The `r`-ary race realizes `(prod_{p|r} Z_p)/Z` (any squarefree
  radical). (iii) **Thm 128c:** NOT equivalent to Suslin-tree existence (honesty `=>
  ¬diamond` only, `SH` orthogonal) nor to `add(M) = aleph_1`; bracketed strictly between
  `b=aleph_1` (dishonest) and `MA_{aleph_1}` (honest), sharp strength = derived-limit
  trivialization principle (Bergfalk 2017; Bergfalk-Lambie-Hanson 2021). Machine-verified
  `code/scripts/check-pass128.py` ->
  `artifacts/reports/pass128-rplus4-pin-phantom-prime-omega1-honesty-check.json` (PASS).
  *Transferred obligations:* the GS `-<`-fragment completeness of `R+4` (classical, not
  Arai-specific); a neighborhood/bisimulation model certifying pure-`Box`-inexpressibility
  of `WO` at modal depth `>= 4`.
- **[Resolved (Pass 129), (i)-(iii) with transferred obligations]** _(was
  [New (Pass 128)])_ **Phantom-spectrum realization, GS `-<`-completeness, and
  simultaneous higher-`lim^n` honesty.** (i) PHANTOM-SPECTRUM: for each squarefree `n`,
  construct a genuine arithmetic Rosser predicate whose canonical phantom is exactly
  `(prod_{p|n} Z_p)/Z` (via an `r`-ary witness race with `rad(r) = {p:p|n}` or a designer
  proof-coding with `rad(m_enc)` prescribed), and decide whether a SINGLE predicate can
  realize a non-squarefree/`p`-power-weighted phantom or whether the phantom functor factors
  absolutely through the squarefree radical lattice (a "phantom spectrum" map
  `Predicates -> P_fin(Primes)`). (ii) Discharge the Thm-128a transferred obligation: the
  pure-`Box` completeness `R+4 = pure-Box PL(Box_R^A)` via the GS `-<`-fragment
  (Guaspari-Solovay/Kurahashi), and build the neighborhood/bisimulation witness at depth
  `>= 4`. (iii) SIMULTANEOUS HONESTY: lift Thm 128c from `lim^1` to `(lim^n)_{n>=1}`
  (Bergfalk-Lambie-Hanson): is "`aleph_1`-twin Arai honest at EVERY finite twin-depth"
  (all `lim^n = 0`) equiconsistent with a weakly compact cardinal, and does single-`lim^1`
  honesty already decide the higher ones or genuinely split (strong-homology additivity
  inside the G2-ZOO)?
  **Resolution (Pass 129).** (i) **Thm 129a:** the phantom is `varprojlim^1(Z,x m_n) =
  hatZ_N/Z` with `N = prod_n m_n` the STEINITZ (supernatural) number; the `r`-ary race
  `r = prod_{p in S} p` realizes every squarefree radical `S` (surjectivity onto
  `P_fin(Primes)`). A SINGLE predicate CANNOT carry a `p`-power-weighted phantom while
  constant-arity: `Phi(p^k) = Phi(p) = Z_p/Z`, so `Phi` factors ABSOLUTELY through the
  squarefree radical lattice ON the uniform (constant-arity) subcategory. But a DEPTH-VARYING
  race escapes the lattice to an arbitrary Steinitz number `N`, so the true "phantom
  spectrum" target is the Steinitz monoid and `P_fin(Primes)` is exactly the uniform-Rosser
  image. **Pathology 129a':** the primorial race `a_k = p_k` has `Supp_infty(N) = emptyset`
  yet is non-ML, giving a NONZERO purely finitary/adelic phantom `(prod_p Z/p)/Z` (honest at
  each prime, phantom collectively); the ML tail dichotomy is sharp (eventually-identity =>
  `Phi = 0`; eventually-const-`2` => `hatZ_2/Z`); an isolated finite `Z/p^k` summand is a
  mirage killed by the dense diagonal `Z`. (ii) PARTIAL/TRANSFERRED: the pure-`Box`
  inexpressibility of `WO` is discharged (**Thm 129c**, two bisimulation certificates, census
  68/68 frames on 3 worlds); the POSITIVE GS `-<`-fragment completeness and the actual
  non-normal neighborhood model realizing `D1^¬D2^D3^hom` remain owed. (iii) **Thm 129b:**
  `h_1` (Thm 128c) does NOT decide `(h_n)_{n>=2}` (`h_1 ^ ¬h_2` consistent via `MA_{aleph_1}`)
  -- honesty STRATIFIES by depth; `(forall n)h_n <=>` strong-homology additivity, a
  large-cardinal statement upper-bounded by a weakly compact (BLH 2021), failing under `V=L`
  and `b=aleph_1`, sharp strength OPEN (equiconsistency-with-weakly-compact conjectured, not
  proved). Machine-verified `code/scripts/check-pass129.py` ->
  `artifacts/reports/pass129-phantom-spectrum-simultaneous-honesty-inexpressibility-check.json`
  (PASS).
- **[Resolved (Pass 130), (i)-(iii) with obligations o1/o2 carried; (i) as a CORRECTION,
  (iii-B) as a CORRECTION of Pass 129]** _(was [New (Pass 129)])_ **Steinitz-image rigor,
  phantom-functor monoid structure, graded-Rosser arithmetization, simultaneous-honesty
  bound, and the positive `WO` model.**
  (i) The naive "`varprojlim^1 = hatZ_{Supp_infty(N)}/Z`, finite-valuation primes DIE" is
  FALSE as a group iso and TRUE only for direct summands. **Thm 130a:** `hatZ_N/Z` is
  DIVISIBLE (`ell`-divisible for every `ell` via the dense diagonal, since
  `hatZ_N/ell.hatZ_N = A_ell/ell.A_ell` and `Z` surjects), so **no finite `Z/q^k` is a direct
  summand** (Cor 130a.1 = the Pass-129 mirage, now a theorem). **Thm 130a.2:**
  `Tor(hatZ_N/Z) = bigoplus_{q notin Supp_inf(N)} Z/q^inf` and `(hatZ_N/Z)/Tor = Q^{(2^aleph0)}`
  -- a finite-valuation prime survives COLLECTIVELY, reincarnated as a Prufer `Z/q^inf`, NOT as
  the bounded `Z/q^{e_q}`; the iso-type forgets ALL finite valuations (incl. `e_q=0`) and
  remembers only `Supp_inf`. **Thm 130b:** `Phi` is NOT a monoid hom into `(Ab,x)`; it factors
  through the surjective IDEMPOTENT semilattice hom `Supp_inf:(Steinitz,x)->(P(Primes),cup)`
  (`Phi(N^2)=Phi(N)`).
  (ii) **Constr 130c:** a graded Rosser `Sigma_1` predicate with disjoint Godel bands and
  `a_k`-ary layer races realizes the facet tower `(Z, x a_k)`, hence `hatZ_{prod a_k}/Z`; the
  primorial schedule `a_k=p_k` arithmetizes `(prod_p Z/p)/Z`. Obligations **o1** (`D1^¬D2`
  uniform across layers) and **o2** (`ConLat`-image tower honestly `(Z,x a_k)`) carried.
  (iii) **Thm 130d CORRECTS Pass-129 Thm 129b(c):** `(forall n)h_n` is NOT a large-cardinal
  statement -- Bergfalk-Hrušák-Lambie-Hanson removed the weakly compact of BLH 2021;
  simultaneous honesty is **equiconsistent with ZFC** (`2^aleph0 >= aleph_2` necessary,
  forcing-axiom not large-cardinal phenomenon).
  (iv) **Thm 130e:** a 3-neighborhood non-normal box (monotone, intersection-open:
  `{0,1} cap {0,2} = {0} notin N`) realizes `D1 ^ ¬D2 ^ D3^hom`; `WO` = Loeb for the `-<`
  modality = converse-well-foundedness. Machine `check-pass130.py` PASS.
- **[Corrected (Pass 130)]** _(Pass-129 Thm 129b(c))_ The claim "`(forall n)h_n` is a
  large-cardinal statement, upper-bounded by a weakly compact, sharp strength the OPEN BLH
  program" is DOWNGRADED: the weakly compact was only BLH 2021's first upper bound;
  Bergfalk-Hrušák-Lambie-Hanson give it in ZFC alone. `(forall n)h_n` is equiconsistent with
  ZFC (Thm 130d).
- **[Resolved (Pass 131), (i)-(iii); (ii) as a SHARPENING of Pass 130]** _(was
  [New (Pass 130)])_ **Prufer-rank rigidity, graded-Rosser witness-counting, the honesty
  ceiling, and bimodal `R+4`.**
  (i) **Thm 131a:** `kappa_q = dim_{F_q}(hatZ_N/Z)[q] = 1` for EVERY finite valuation
  `e_q` (INCLUDING `e_q = 0`) and `= 0` iff `e_q = inf`, by the snake lemma of
  `0->Z->hatZ_N->G->0` at `x q` (`G` divisible `=> G/qG = 0`; diagonal `d(1)=1`). So
  `Tor(hatZ_N/Z) = bigoplus_{q notin Supp_inf} Z/q^inf` is RANK-ONE Prufer; a depth-varying
  overhead permutes finite valuations but CANNOT inflate `kappa_q` -- the continuum lives
  only in the torsion-free `Q^{(2^aleph0)}`. **Pathology 131a':** a `d`-strand facet tower
  gives `kappa_q = #(strands finite at q)`; continuum-rank Prufer torsion is the signature
  of a MULTI-STRAND predicate, not the single-strand graded one. **Lemma 131b:** o1
  (`D1 ^ ¬D2` uniform: each band-disjoint layer is a self-contained GS `a_k`-ary Rosser
  predicate) and o2 (index-`a_k` injective tower map, honest `(Z, x a_k)`) discharged,
  modulo carried o1' (uniform cross-layer GS independence) and o2' (no two orderings
  `T`-provably equivalent).
  (ii) **Thm 131c SHARPENS the Pass-130 `2^aleph0 >= aleph_2`:** `h_n => 2^aleph0 >=
  aleph_{n+1}` (Bergfalk-Lambie-Hanson), so `(forall n)h_n => 2^aleph0 >= aleph_{omega+1}`
  (Konig `cf > omega`). The depth split `h_1 ^ ¬h_2` holds in the ZFC model
  `MA_{aleph1} + 2^aleph0 = aleph_2` (`h_1` by Dow-Simon-Vaughan, `¬h_2` forced by the
  ceiling) -- a LARGE-CARDINAL-FREE stratification. Exact strength = the BBMT `n`-dim
  `Delta`-system / definable additivity principle, NOT a cardinal characteristic.
  (iii) **Thm 131d:** `PL(Box_R^A) = R+4` is the FUSION `[GL]_Box (+) [GL]_{-<}` + bridge
  (`R` = the `-<`-fragment); canonical model = up-closed `-<`-cone neighborhood box fibered
  over a `GL` `-<`-frame (3-world witness `N(w)=up{W,{0,1},{0,2}}` validates
  `D1 ^ RM ^ 4 ^ ¬Box_R bot`, refutes `K`). **Thm 131e:** full `D3` coexists with `¬D2`
  (the `GL`-collapse fusing the twins is `D2`-only), arithmetic full-`D3` realizability
  carried. Machine `check-pass131.py` overall PASS.
- **[Resolved (Pass 136), (ii) primary; (iii) advanced; (i) carried]** _(was
  [New (Pass 135)])_ **The 2-cd BBMT separator consistency, `cd`-vs-`cf` grading, and the
  exotic-ordering `Sigma_1`-induction.**
  **(ii) RESOLVED — Thm 136a (uniform sphere obstruction / `cd`-grading).** For every
  `k >= 1` the minimal k-coherence obstruction of `A^{(a),k}` is `S^k =
  boundary(Delta^{k+1})` with `Htilde_j(S^k; F_a) = F_a` iff `j = k`; hence
  `cd(A^{(a),k}) = k` EXACTLY (strict `cd`-graded tower, no collapse). `Delta^{k+1}` and the
  shared-vertex wedge of two k-simplices are contractible (generalizing Pass-135
  Correction 135b to ALL k), and no simplicial retraction `Delta^{k+1} -> S^k` exists, so
  the `n=1`-vs-`n>=2` non-transfer of Thm 135a is degree-UNIFORM, carried entirely by
  `cd(A) <= 1`. **Thm 136b:** `cd` is ZFC-ABSOLUTE (finite `F_a` simplicial homology, a
  `Delta^0_1` predicate; Shoenfield). **Thm 136c:** `cd` and the Thm-134d `cf`-rank grading
  are INDEPENDENT invariants — `cd` absolute, `cf`-rank not (DSV89/MP88/BLH21) — tied ONLY
  by the one-sided Bergfalk-Lambie-Hanson ceiling `cd >= k => 2^{aleph_0} >= aleph_{k+1}`;
  the converse fails (fixed-`cd` re-indexing along a higher-cofinality cofinal set raises
  the vanishing threshold without touching `cd`), so their lockstep on the standard tower
  `A^{(a),•}` is a construction artifact, not an identity. Machine-verified `F_3`, k=1..4:
  `artifacts/reports/pass136-cohdim-sphere-grading-cd-vs-cf-check.json` (overall PASS).
  **(iii) ADVANCED — Prop 136d.** A `Sigma_1`-definable, non-primitive-recursive TAG map
  `t` gives `n -< m :iff t(n) <_lex t(m)` with per-comparison encoding `m_enc = O(1)` yet
  non-p.r. global order (non-p.r. content quarantined in `t`), exhibiting the
  `m_enc = O(1)` / non-p.r. `-<` combination the Pass-134 Skeptic feared: realizability and
  logic diverge; bounded `m_enc` does not entail p.r. `-<`. *Carried obligation:* `I-Sigma_1`
  linearity of `-<` and box-level preservation of `¬D2 ^ ¬Box_R⊥` (the tag order must not
  restore `D2` via proof-concatenation monotonicity). **(i) CARRIED — Rem 136e.** The
  strictness separator `Con((forall n) h_n(A) ^ varprojlim^2 A^{(a),2} != 0)` is now
  certified genuinely level-2 by 136b (`cd(A^{(a),2}) = 2` absolute), non-vacuous
  (CH-consistent), a concrete 2-cd instance of the OPEN BBMT additivity
  (Bannister-Bergfalk-Moore-Todorcevic; Bergfalk-Lambie-Hanson 2021); target model
  `b = aleph_1` against a BLH21-style simultaneous-vanishing forcing. NOT decided this pass.
- **[Resolved (Pass 139), (b) LIMITATIVE + corrected; (c),(d) carried to
  `[New (Pass 139)]`]** _(was [New (Pass 138)])_ **The 2-cd forcing frontier
  (carried from `[New (Pass 137)]` (b),(c)) and the completed Rosser-box
  dictionary.**
  **(b) RESOLVED (Pass 139) as LIMITATIVE + corrected.** **Thm 139a:** the Pass-138
  target `b = aleph_1` is REFUTED. `b = aleph_1 => varprojlim^1 A != 0`
  (Dow--Simon--Vaughan 1989, "Strong homology and the proper forcing axiom," Proc.
  AMS 106 (1989) 821--828), so `!h_1(A)`, so `!(forall n) h_n(A)`: the first
  conjunct fails in EVERY `b = aleph_1` model, and any witness of the separator has
  `b >= aleph_2`. **Thm 139b (hidden dichotomy):** the literal `(forall n)` either
  (I) is REDUNDANT -- if `cd(A) <= 1` bounds the set-theoretic `varprojlim^{>=2} A`
  (Goblot at the `omega^omega`-index cofinality), then `(forall n) h_n <=> h_1` and
  the separator is `Con(h_1(A) ^ varprojlim^2 A^{(a),2} != 0)`, CONSISTENT -- or
  (II) OVERSHOOTS -- if cd/cf-INDEPENDENT (Thm 136c), then `(forall n) h_n` forces
  `2^{aleph_0} >= aleph_{omega+1}` (BLH ceiling `h_n => 2^{aleph_0} >= aleph_{n+1}`
  + König `cf(2^{aleph_0}) > omega`), a dimension-UNIFORM BBMT additivity regime in
  which even the `cd = 2` sphere obstruction `A^{(a),2}` trivialises, so
  `varprojlim^2 A^{(a),2} = 0` and the LITERAL conjunction is INCONSISTENT. Both
  horns AGREE the `b = aleph_1` target is wrong and that the CORRECTED separator
  `Con(h_1(A) ^ varprojlim^2 A^{(a),2} != 0)` is the right object. **Cor 139c:** it
  is witnessed LARGE-CARDINAL-FREE by `MA_{aleph_1} + 2^{aleph_0} = aleph_2` (the
  Thm-131c depth-split model): `h_1(A)` additive, `aleph_2 < aleph_3` ceiling forces
  `varprojlim^2 A^{(a),2} != 0`, and `cd(A^{(a),2}) = 2` ZFC-absolute (Thm 136b,
  recertified: `H~_j(S^2; F_3) = F_3` iff `j = 2`) certifies genuineness (not a
  re-indexed level-1). Placed on the two governing invariants: a Löb(sheaf,
  deg-1-additive)/Rosser(cosheaf, deg-2-phantom) DEGREE MISMATCH = set-theoretic
  `D2`/`D3` gap (Thm 61a/b, 130e/131e); certified-linearity bit (Thm 138c) =
  `Lin(-<) <=>` chain `<=>` Mittag-Leffler `<=> varprojlim^{>=1} = 0`, OFF for the
  non-linear `omega^omega`-index (so `lim^1 A != 0` at `b = aleph_1`); and the
  level-2 phantom = derived-limit avatar of `nFG2(2)` (`boxtimes^3 T <= boxtimes^2
  T`), its non-vanishing at `aleph_2` a set-theoretic witness that `nFG2(2)` does
  NOT reduce to `nFG2(1) = FG2`. Machine-verified
  `artifacts/reports/pass139-bal1-refutation-cd2-separator-check.json` (A/B/C/D,
  overall PASS) via `code/scripts/check-pass139.py`. *Residual proof obligations
  (carried):* the horn-I-vs-II decision (Goblot cofinality bound vs cd/cf
  independence for the twin tower) and the exact sufficiency of `MA_{aleph_1}` (vs
  full dimension-1 additivity) for `h_1(A)`. **(c),(d) CARRIED** verbatim to
  `[New (Pass 139)]`.
- **[Resolved (Pass 140), (a) horn-I REFUTED; (b),(c) carried to `[New (Pass 140)]`]**
  _(was [New (Pass 139)])_ **Deciding the strictness dichotomy, the `cd = omega`
  diagonal, and the certified-linearity bit inside `ConLat_T`.** Opened by Pass 139.
  **(a) RESOLVED (Pass 140) -- horn I is refuted outright, the dichotomy dissolves.**
  **Thm 140a:** the Mardesic--Prasolov system `A` is indexed by `(omega^omega, <=*)`
  whose directed cofinality `cf = d >= b >= aleph_1` is ALWAYS uncountable (a ZFC
  theorem: no countable subset of `omega^omega` is cofinal under `<=*`). Goblot's
  vanishing theorem (Goblot 1970; Mardesic, *Strong Shape and Homology*, Springer
  2000) then gives `varprojlim^n A = 0` only for `n >= cf-rank + 2 >= 3`, so Goblot
  NEVER forces `varprojlim^{>=2} A = 0`. The graph-nerve `cd(A) <= 1` (a Cech/sheaf
  invariant of the 1-dimensional nerve) and the Goblot cofinality-rank of the index
  poset are DECOUPLED (Thm 136c), and only the latter governs `varprojlim^* A`:
  Horn I's antecedent ("`cd <= 1` bounds `varprojlim^{>=2} A` via Goblot") is
  UNSATISFIABLE. **Cor 140b:** hence `(forall n) h_n` is strictly stronger than
  `h_1` (the literal quantifier is NOT redundant); the LITERAL separator
  `Con((forall n) h_n ^ varprojlim^2 A^{(a),2} != 0)` is INCONSISTENT (Pass-139
  Koenig overshoot `(forall n) h_n => 2^{aleph_0} >= aleph_{omega+1}`), while the
  CORRECTED separator `Con(h_1(A) ^ varprojlim^2 A^{(a),2} != 0)` is CONSISTENT.
  **Cor 140c:** its home is `MA_{aleph_1} + 2^{aleph_0} = aleph_2`, where
  `varprojlim^2 A^{(a),2} != 0` holds by the Bergfalk--Lambie-Hanson ceiling
  CONTRAPOSITIVE (`h_2 => 2^{aleph_0} >= aleph_3`, refuted by `c = aleph_2`), NOT by
  Goblot; `cd(A^{(a),2}) = 2` is ZFC-absolute (Thm 136b, recertified:
  `Htilde_j(S^2; F_3) = F_3` iff `j = 2`). **Rem 140d:** `varprojlim^n A` is the
  derived-limit avatar of `nFG2(n)` (`boxtimes^{n+1} T <= boxtimes^n T`); because
  the orbit index `(omega^omega, <=*)` is uncountable and non-well-founded, the
  Goblot truncation depth `cf-rank + 1` is UNBOUNDED -- the exact set-theoretic
  ANTIPODE of Thm 41a's finite depth-2 self-truncation of the antitone `boxtimes`-
  orbit. Machine-verified `artifacts/reports/pass140-horn-a-goblot-vs-nerve-cd-check.json`
  (overall PASS) via `code/scripts/check-pass140.py`. *Residual proof obligation
  (carried, Cor 140c(i)):* whether `MA_{aleph_1}` ALONE (vs `PFA`, used by
  Dow--Simon--Vaughan 1989) forces `varprojlim^1 A = 0` at `2^{aleph_0} = aleph_2`
  -- the load-bearing `h_1` line, a `MA_{aleph_1}`-trivialisation of the level-1 MP
  obstruction on coherent `aleph_1`-families (Todorcevic 1989). **(b),(c) CARRIED**
  verbatim to `[New (Pass 140)]`.
- **[Resolved (Pass 141), (a) and (c); (b) carried to `[New (Pass 141)]`]**
  _(was [New (Pass 140)])_ **The `cd = omega` diagonal / `nFG2(omega)` limit, and the
  certified-linearity bit inside `ConLat_T`.** Opened by Pass 140.
  (a) THE `cd = omega` DIAGONAL [carried from `[New (Pass 139)]` (b)]: **RESOLVED
  (Pass 141) -- the diagonal RE-TRUNCATES below the ceiling.** **Thm 141a (telescope
  collapse):** the suspension-telescope diagonal `A^{(a),omega}_tel = colim(S^k,
  equatorial)` is `F_3`-acyclic (each `S^k -> S^{k+1}` is `0` on the top class
  `H~_k`, so the homology tower is eventually-zero => Mittag-Leffler =>
  `varprojlim^1 = 0` in every degree, the Thm-55c avatar); the telescoped
  `boxtimes`-tower self-truncates to the TRIVIAL object -- a depth-`omega` echo of
  Thm 41a. **Prop 141b:** the coproduct diagonal `+_k A^{(a),k}` is only the
  phantom-additive UNION of finite levels (Pass 50/51), not a new class. **Thm 141c
  (Goblot ceiling):** over any FIXED index of cofinality `aleph_r`, `varprojlim^n =
  0` for `n >= r+2` (Goblot 1970; Mardesic 2000), so a single object with
  `varprojlim^n != 0` cofinally in `n` needs UNBOUNDED cofinality `cf >= aleph_omega`,
  i.e. `2^{aleph_0} >= aleph_{omega+1}` (BLH ceiling `lim^n != 0 => c >= aleph_{n+1}`
  + Koenig). **Cor 141d (phantom uncertainty principle):** a genuine `nFG2(omega)`
  [`c >= aleph_{omega+1}`] and the sharp level-2 separator at its home `c = aleph_2`
  (Cor 140c) are MUTUALLY EXCLUSIVE -- so at `c = aleph_2` there is NO genuine
  `cd = omega` phantom, only the re-truncating telescope or the splintering union.
  (b) CERTIFIED-LINEARITY BIT [carried from `[New (Pass 139)]` (c)]: **CARRIED** to
  `[New (Pass 141)]` -- locate `T |- Lin(-<)` inside `ConLat_T`, whether the single
  Boolean PL detects (Thm 138c) is the shadow of the `I-Sigma_{k-1}`/`I-Sigma_k`
  boundary (Thm 137d), and whether Rosser `WC` names a point of the `Con^{orb}_n`
  tower (Pass 69).
  (c) DISCHARGE Cor 140c(i): **RESOLVED (Pass 141), POSITIVELY.** **Cor 141e:**
  `MA_{aleph_1}` ALONE forces `varprojlim^1 A = 0` at `2^{aleph_0} = aleph_2` -- the
  level-1 trivialisation poset is `sigma`-centered (ccc), needs only `aleph_1` dense
  sets (Dow--Simon--Vaughan 1989; Bergfalk 2017; Todorcevic 1989); full `PFA`/`OCA`
  is required by DSV only for SIMULTANEOUS higher vanishing, and the same
  `MA_{aleph_1}` does NOT give `varprojlim^2 = 0` (needs `c >= aleph_3` by BLH), so
  the level-2 separator survives. Machine `code/scripts/check-pass141.py` ->
  `artifacts/reports/pass141-cd-omega-diagonal-nfg2omega-check.json` (PASS).
- **[Resolved (Pass 142), (a) reduced + attained, (c) REFUTED; (b) split and carried]**
  _(was [New (Pass 141)])_ **The `aleph_{omega+1}` home: is the `nFG2(omega)` ceiling
  ATTAINED, or does a higher obstruction reappear one cardinal up?**
  (a) ATTAINED, as a pcf REDUCTION. **Thm 142a:** re-base the long diagonal off the
  countable-coordinate product `prod_n omega` (whose `<*`-cofinality is the dominating
  number `d`, a red herring) onto `prod_n aleph_n`; Shelah pcf gives IN ZFC a
  tcf-scale `<f_xi : xi < lambda>`, `lambda = pp(aleph_omega)`, cofinal of length
  `aleph_{omega+1} <= lambda < aleph_{omega_4}`. Mounting `(A^{(a),k})_k` on the walks
  of the scale, `varprojlim^n A^{(a),Omega} != 0` cofinally in `n` **iff** the
  transverse `n`-coherent family is cofinally nontrivial. The pcf skeleton (scale,
  cofinality `aleph_omega`, window) is ZFC-ABSOLUTE; the nonvanishing REDUCES to a
  coherence-nontriviality input (the honest core). (c) REFUTED. **Thm 142b (pcf
  caging):** the home ordinal-index is pinned into the ZFC window `[omega+1, omega_4)`
  (`aleph_omega^{aleph_0} >= aleph_{omega+1}` floor by Koenig; `pp(aleph_omega) <
  aleph_{omega_4}` ceiling by Shelah), so the phantom can be displaced upward only
  within a BOUNDED pcf interval, never to infinity; and the Thm-141a telescope-collapse
  does NOT echo, because an `aleph_omega`-cofinal index carries no cofinal `omega`-chain
  (least cofinal-subset size `aleph_omega > aleph_0`), voiding the Mittag-Leffler
  reduction. (b) SPLIT. **Thm 142c:** the phantom's EXISTENCE is large-cardinal-FREE
  (ZFC pcf + ZFC nontrivial coherence); its DESTRUCTION (all `lim^n = 0`, the
  `omega`-level honesty) is the strength-bearing side (weakly compact upper bound BLH
  2021, since reduced BHLH; exact strength carried). **Pathology 142d (linear-scale
  trap):** indexing by the `<*`-scale ITSELF is cf-rank `1`, so Goblot forces
  `lim^{>=3} = 0` -- worse than the telescope; the phantom lives strictly on the
  `[lambda]^{<omega}`-transverse coherence, the transfinite reprise of "no strictly
  nFG2-descending orbit exists on a linearly reachable chain" (Thm 41a). Antipode of
  Thm 41a: finitely the phantom is impossible-to-have / free-to-destroy; transfinitely
  at the ceiling it is cheap-to-have / expensive-to-destroy. Machine
  `code/scripts/check-pass142.py` ->
  `artifacts/reports/pass142-aleph-omega-plus-1-home-pcf-window-check.json`
  (A finite-directed acyclicity 1183 posets/0 top-violations; B ceiling ladder;
  C pcf window nonempty+bounded; D telescope non-echo; overall PASS). Successor
  `[New (Pass 142)]` opened below.
- **[Resolved (Pass 143), (a) reduced to the CLH weak-diamond ladder + coherence-dimension
  caging; (b) RESOLVED -- ZFC-equiconsistent, weakly compact removed; (c) carried]**
  _(was [New (Pass 142)])_ **The transverse coherence core, and the destruction strength.**
  Opened by Pass 142 (Thm 142a reduces attainment to coherence; the honest content is
  now isolated).
  (a) RESOLVED as a further reduction + a caging. **Thm 143a (walk-lift, dimension-graded):**
  the `n=1` layer is the EXPLICIT Todorcevic `rho_1`/Hausdorff-gap coherent family on the
  `aleph_omega`-scale C-sequence (ultrametric coherence `rho_1(a,g) <= max{rho_1(a,b),
  rho_1(b,g)}` machine-checked, 10660/10660 triples; raw `rho_2` step-count NOT subadditive,
  not certified); the higher-`n` layers are the Casarosa--Lambie-Hanson weak-diamond-fed
  coherent families (`varprojlim^n A[H] != 0` from `d = omega_n` for `H = Z^{(omega_n)}`, or
  from `w-diamond(S^{k+1}_k)` for all `k<n` for `H = Z`), stratifying by dimension.
  Cofinal-in-`n` non-vanishing REDUCES to their conjunction, whose necessary cardinal price
  is exactly `2^{aleph_0} >= aleph_{omega+1}` (CLH 2024, answering Bannister). The phantom
  is a dimension-UNBOUNDED tower of coherent families, never one walk. **Thm 143b (Goblot
  coherence-dimension caging):** any single C-sequence/walk has finite cohomological
  dimension `cd`, so Goblot `H^{>cd}=0` caps its non-trivial coherence at a finite dimension
  -- one walk NEVER carries the phantom cofinally; the caging axis is the COHERENCE dimension,
  ORTHOGONAL to the bounded-pcf cardinal caging of Thm 142b (finite-nerve shadow: path `cd0`
  no coherence, cycle `cd1` `H^1=1`/`H^2=0` caged, octahedron `cd2` `H^2=1` uncaged).
  (b) RESOLVED. **Thm 143c:** kill `lim^1` alone `= MA_{aleph_1}` (Dow--Simon--Vaughan 1989);
  kill ALL `lim^n` simultaneously `=` adjoin `beth_omega` Cohen reals
  (Bergfalk--Hrusak--Lambie-Hanson, J. Math. Logic 23 (2023); arXiv:2102.06699) --
  EQUICONSISTENT with ZFC, the weakly compact of Bergfalk--Lambie-Hanson (2021) a
  removable first-proof artifact; the Pass-130 ledger (equiconsistent ZFC) is CORRECT.
  Necessary-not-sufficient: the `beth_omega`-Cohen model MEETS the floor
  `2^{aleph_0} >= aleph_{omega+1}` yet has all `lim^n = 0` -- the ceiling is the doorframe,
  not the ghost; existence and destruction are both ZFC-equiconsistent and both compatible
  with the ceiling, separated by coherence combinatorics (weak-diamond vs Cohen-generic),
  not cardinal arithmetic. (c) carried to `[New (Pass 143)]`. Machine
  `code/scripts/check-pass143.py` ->
  `artifacts/reports/pass143-transverse-coherence-walk-lift-check.json` (A walk coherence +
  `delta^2=0`; B Goblot caging via nerve cohomology; C ceiling ladder + window + BHLH;
  overall PASS). Refs: Mardesic--Prasolov 1988; Dow--Simon--Vaughan 1989; Todorcevic, Walks
  on Ordinals (2007); BLH Forum Math Pi 9 (2021); BHLH JML 23 (2023); Casarosa--Lambie-Hanson
  arXiv:2411.15856 (2024).
- **[Resolved (Pass 144), level-split: `n>=2` pro-isomorphic across the window; `n=1`
  gap-refinement indexed by `Lambda`, nonvacuous iff `~SCH`]**
  _(was [New (Pass 143)])_ **Does the pcf window stratify the phantom, or is the only genuine
  stratification the CLH coherence-dimension ladder?**
  RESOLVED as a LEVEL-SPLIT. **Def 144.0:** `Lambda := pcf({aleph_n : 1<=n<omega}) cap
  (aleph_omega, aleph_{omega_4})`, the regular scale-lengths, `max Lambda = pp(aleph_omega)`.
  **Thm 144a (level-split of window stratification):** for the transverse cover-fiber system
  `A_mu[H]` of a length-`mu` tcf-scale `S_mu`, (i) for `n >= 2`, `varprojlim^n A_mu[Z] =~
  varprojlim^n A_{mu'}[Z]` for all `mu, mu' in Lambda` -- level-`n` nonvanishing is governed by
  `w-diamond(S^{n+1}_n)` (resp. `d = omega_n` for `H = Z^{(omega_n)}`), a characteristic at
  `omega_{n+1} < aleph_omega` on the FIXED low-index coordinates, INDEPENDENT of the scale
  length `mu`; the higher phantom is PRO-ISOMORPHIC across the whole window (obligation:
  pullback naturality of `[mu]^{<omega} -> [omega_{n+1}]^{<omega}`). (ii) for `n = 1`, the
  Hausdorff-gap / `rho_1` class lives at regular height `mu`, and since cofinality is a
  pro-iso invariant, distinct `mu` give NON-pro-isomorphic classes -- level 1 DOES stratify,
  indexed by `Lambda` (obligation: per-`mu` non-tightness / bad-point). **Thm 144b (nonvacuity
  = failure of SCH):** `|Lambda| >= 2` iff `pp(aleph_omega) > aleph_{omega+1}` iff SCH fails at
  `aleph_omega`; under SCH the window is a single point and both horns collapse to the Pass-143
  dimension-tower. **Cor 144c:** the phantom is BIGRADED `Phi^n_mu` -- unbounded along the
  coherence dimension `n` (Pass 143, every `mu`), collapsing along the pcf-length `mu` for
  `n >= 2` (pro-isomorphic) and surviving only at `n = 1` (a `~SCH`-conditional gap-refinement).
  So prong (c) resolves NEGATIVELY for the substantive `n >= 2` phantom -- the cardinal window
  adds no new HIGHER classes; the genuine stratification is the coherence-DIMENSION ladder.
  **Pathology 144d:** widen the pcf hotel arbitrarily (large `pp(aleph_omega)`, Gitik-Magidor)
  and the `n >= 2` haunting is CONSTANT along it -- the higher-dimensional wardrobe stays in one
  ground-floor closet at `omega_{n+1}`; cross-cofinality transfer to a window cardinal is vacuous.
  Machine `code/scripts/check-pass144.py` ->
  `artifacts/reports/pass144-pcf-window-stratification-level-split-check.json` (A level-1
  girth-split, B level-2 `H^2` constant across window labels, C nonvacuity-iff-`~SCH` gate;
  overall PASS). Refs: Shelah, *Cardinal Arithmetic* (1994); Abraham-Magidor pcf chapter,
  Handbook of Set Theory (2010); Gitik-Magidor on SCH failure; Casarosa-Lambie-Hanson
  arXiv:2411.15856 (2024); BHLH JML 23 (2023).
- **[Resolved (Pass 145), (a),(b) discharged; (c) Con^orb carried to `[New (Pass 145)]`]**
  _(was [New (Pass 144)])_ **Discharge the Thm-144a obligations and place the level-1
  gap-refinement inside the nFG2 hierarchy / `Con^{orb}` tower.** Opened by Pass 144 (Cor
  144c gives a bigraded phantom `Phi^n_mu` with the cardinal axis alive only at `n = 1`).
  RESOLUTION. (a) **Thm 145a (finality pro-iso):** `A_mu[Z] =~ pi_mu^* B[Z]` for
  `pi_mu : [mu]^{<omega} -> [omega_{n+1}]^{<omega}`, `X |-> X cap omega_{n+1}`, which is
  FIBRE-ACYCLIC (fibres up-directed); the Bousfield--Kan/Roos spectral sequence collapses
  (`E_2^{p,q>=1}=0`) to the edge iso `varprojlim^n_{[mu]} A_mu =~ varprojlim^n_{[omega_{n+1}]} B`,
  natural in `mu`, for all `n >= 2` -- naturality of 144a.i is a formal consequence of
  finality. **Cor 145b:** `mu = max Lambda = pp(aleph_omega)` carries NO extra top-generator
  class (`pi` quotients scale-length). (b) **Thm 145c (level-1 faithfulness = badness):**
  `Phi^1_mu != 0` iff `S_mu` has stationarily many bad points (no eub) iff `mu` non-approachable;
  the level-1 stratification is faithful exactly on `Lambda_bad`, and `Lambda_bad = emptyset`
  (Foreman--Magidor very-good-scale / AP) vs `Lambda_bad = Lambda` (Magidor--Shelah tree
  property / `~AP`) are BOTH consistent -- faithfulness is approachability-conditional.
  Machine `code/scripts/check-pass145.py` ->
  `artifacts/reports/pass145-thm144a-obligation-discharge-check.json` (A finality, B good/bad
  level-1, C orientation; overall PASS). Refs: Cummings--Foreman--Magidor, "Canonical structure
  in the universe of set theory" I--II, APAL 129 (2004) / 142 (2006); Foreman--Magidor, "A very
  weak square principle", JSL 62 (1997); Magidor--Shelah, "The tree property at successors of
  singular cardinals", Arch. Math. Logic 35 (1996); Bousfield--Kan, LNM 304 (1972); Roos,
  "Sur les foncteurs derives de lim", CRAS 252 (1961).
- **[Resolved (Pass 146), (a),(b); residues carried to `[New (Pass 146)]`]**
  _(was [New (Pass 145)])_ **Build the `Con^{orb}` functor of Thm 145d and test whether the
  `n >= 2` frozen skeleton has an arithmetic ZFC-absolute avatar.** Opened by Pass 145
  (Thm 145d is a structural conjecture; Pathology 145e gives a frozen `n >= 2` / fluid
  `n = 1` split).
  RESOLUTION. (a) **Thm 146a (Con^orb is a map of DERIVED invariants, not of points):**
  since `|Or-bad(S_mu)| >= aleph_{omega+1} > aleph_0 = |ConLat_T|` and `Fix(boxt)` is a
  countable antichain (Lemma 51a), NO injection `Or-bad(S_mu) hookrightarrow Fix(boxt)`
  exists; the dictionary factors through the countable derived-signature quotient
  `sigma : point |-> (H^1, H^0(sgn))` with three values -- `(0,--)` `|->` Loeb/integral,
  `(Z,0)` `|->` Rosser torsor `Zhat_2/Z`/non-integral, `(Z,Z/2)` `|->` Kripke-Feferman
  (lim^1-detected but Rosser-invisible). Functorial under scale end-extension (`lim^1` is a
  tail/pro-invariant, Pass 59). (b) **Thm 146b (frozen but NOT nFG2-graded):** Thm 41a
  self-truncates `nFG2` at index 2, so `varprojlim^n B[Z]` (`n >= 2`) is NOT an
  `nFG2(n)`-strictness witness -- coherence dimension and `boxt`-orbit index are orthogonal
  gradings; the true avatar is the Japaridze-Beklemishev graded provability algebra, with
  `varprojlim^n B[Z]` realising the PA-provable strictness `<n> !~ <n+1>` (Beklemishev 2004),
  ZFC-absolute (reproduces Cor 145b). **Thm 146c (Feferman path-dependence =
  non-approachability):** the fluid `n = 1` layer is the first limit (`omega`-th) stage of a
  Turing-Feferman transfinite progression, whose notation-path-dependence (Feferman 1962) is
  the arithmetic image of a bad point's `Z/2`-orientation. **Pathology 146d:** the same
  bigraded ghost is a PA-THEOREM on every floor `n >= 2` (Beklemishev strictness) and a
  ZFC-INDEPENDENT statement on floor 1 (Foreman-Magidor vs Magidor-Shelah). Machine
  `code/scripts/check-pass146.py` ->
  `artifacts/reports/pass146-conorb-functor-nfg2-coherence-orthogonality-check.json`
  (A Con^orb signatures/KF/end-extension/non-injectivity; B nFG2 index-2 collapse vs
  `H^n(S^n)=Z` orthogonality; C frozen `H^2` label-independence + fluid girth split + GLP
  strictness; overall PASS). Refs: G. Japaridze, "The polymodal logic of provability", 1988;
  L. Beklemishev, "Provability algebras and proof-theoretic ordinals, I", APAL 128 (2004)
  103--123; S. Feferman, "Transfinite recursive progressions of axiomatic theories", JSL 27
  (1962) 259--316.
- **[Resolved (Pass 147), (a),(b); residues carried to `[New (Pass 147)]`]**
  _(was [New (Pass 146)])_ **Realise the Kripke-Feferman prong arithmetically and construct the
  `Coh : B[Z] -> GLP`-tower functor.** Opened by Pass 146 (Thm 146a leaves the `(Z, Z/2)`
  KF signature realised only algebraically; Thm 146b's GLP identification and Thm 146c's
  Feferman-path correspondence are structural/heuristic, not constructed).
  RESOLUTION. (a) **Thm 147a (explicit KF `(Z,Z/2)` fixed point; KF/Rosser separation):** over
  c.e. `T \supseteq EA`, in the strong-Kleene Kripke-Feferman closure (Feferman 1991) put
  `Box_KF phi = Tr(dot⌜Prov_T phi⌝)`, `boxt = ¬Box_KF`, diagonalize `T |- kappa <-> boxt kappa`.
  `kappa` is UNGROUNDED in the minimal Kripke fixed point while every iterate `boxt^n T` is
  grounded at a finite stage; groundedness is `≡_T`-invariant, so `kappa !≡_T boxt^n T` --
  `kappa` DETACHED, cover-fiber tower non-ML `(Z,×m)`, `varprojlim^1 = Zhat_m/Z != 0`
  (`H^1 = Z`). The Kleene jump commutes with the De Morgan involution `delta`, so the
  orientation `Z/2`-torsor is TRIVIAL, its double cover SPLITS, `H^0(sgn) = Htilde^0(;Z/2) =
  Z/2` -- Rosser-INVISIBLE. In the countable antichain `Fix(boxt)` (Lemma 51a) the signatures
  `(0,--)` Loeb, `(Z,0)` Rosser, `(Z,Z/2)` KF are pairwise distinct; `kappa`/`rho` share
  `H^1=Z` and are separated by `H^0(sgn)` alone. (b) **Thm 147b (`Coh` functor):**
  `Coh([S^n]) = <n>T`, `Coh(sigma_n) =` Beklemishev's reduction `<n+1>T ≡_T <n>^omega T`
  (APAL 2004); a graded monoid map faithful on generators with `H^n(S^n)=Z` matching PA-provable
  strictness `<n> !~ <n+1>` (frozen `n>=2` = ZFC-absolute GLP tower, confirming Thm 146b). The
  reduction spends one `omega` per degree bump: the first limit is at the `n=1->2` passage, so
  `n=1` maps to the finite base `<1>`, NOT `<omega>`; the genuine first LIMIT modality `<omega>`
  (`GLP_Lambda`, Fernandez-Duque--Joosten) is the avatar of the `n=1` layer's transfinite
  regular-height-`mu` home. **Thm 147c (Feferman-Spector non-uniqueness):** `T_omega` of a
  Turing-Feferman uniform-reflection progression is genuinely notation-path-dependent (Feferman
  1962 completeness + Feferman-Spector 1962 incomparable `O`-paths) -- Thm 146c PROMOTED from
  analogy to a proved recursion-theoretic non-uniqueness (parallel to, not identified with, the
  set-theoretic non-absoluteness of Thm 145c). **Pathology 147d:** three modal faces in one
  column -- symmetric-independent (`kappa`, `n=1`), oriented-independent (`rho`, `n=1`),
  provable-absolute (`<n>`, `n>=2`); orientation is a purely ground-floor phenomenon. Machine
  `code/scripts/check-pass147.py` ->
  `artifacts/reports/pass147-kf-signature-glp-functor-check.json` (A double cover `2`->`Z/2`
  symmetric vs connected `1`->`0` Rosser, both `H^1=Z`; B strict GLP chain, `0` collapses,
  degree<->depth bijective, first limit at `n=1->2`; C `c_k` ground at stage `k`, `kappa`
  ungrounded, `delta` fixes `kappa`/breaks `rho`; overall PASS). Refs: Feferman 1962 (JSL 27,
  259-316); Feferman-Spector 1962 (JSL 27, 383-390); Feferman 1991 (JSL 56, 1-49); Kripke 1975;
  Cantini 1990 (JSL 55, 244-259); Beklemishev 2004 (APAL 128, 103-123); Ignatiev 1993;
  Fernandez-Duque-Joosten 2013.
- **[Resolved (Pass 148), (a),(b); residues carried to `[New (Pass 148)]`]** **Descend `kappa`
  to `ConLat_PA` (or prove ascent is forced), and promote `Coh` to a full monoidal functor
  locating `<omega>`.** Opened by Pass 147 (Thm 147a realises `kappa` only in `ConLat_{KF}`;
  Thm 147b's `Coh` is a generator-level monoid map on the positive cone).
  RESOLUTION. (a) **Thm 148a (Sigma_1-orientation dichotomy):** over `T \supseteq EA` with a
  `Delta_0` linear proof order `prec`, the Rosser tie-break `R_prec` is a TOTAL orientation of
  `Fix(boxt)` and `delta R_prec = R_{prec^op} != R_prec` on every non-degenerate fixed point
  (antisymmetry of `prec`), so every detached `Sigma_1` `boxt`-fixed point has monodromy `-1`,
  connected orientation double cover, `H^0(sgn) = 0` -- signature `(Z,0)` Rosser. The symmetric
  `(Z,Z/2)` requires a `delta`-FIXED tie-break, and the unique `delta`-fixed comparison is the
  undirected truth-gap valuation, which is NOT `Sigma_1`. **Thm 148b (forced ascent + descent
  retraction):** `(Z,Z/2)` is intrinsically non-`Sigma_1` -- it requires the strong-Kleene KF
  closure (ordinal `phi_{epsilon_0}(0)`); the Pass-147 embedding is the arithmetic-restriction
  RETRACTION `r : ConLat_{KF} -> ConLat_PA` (not an inclusion of `kappa in L_{Tr}`), and
  `r([kappa])` is a still-DETACHED but RE-ORIENTED `(Z,0)` shadow (the gap collapses under
  two-valued restriction, dropping `H^0(sgn) : Z/2 -> 0`). So `(Z,Z/2)` lives strictly in
  `L_{Tr}`; the KF ascent is FORCED. (b) **Thm 148c (monoidal Coh; law = depth-addition):**
  `Coh : Sph -> GLP^+` (source = free strict symmetric monoidal category on `S^1`,
  `S^n^S^m=S^{n+m}`; target = graded monoid `(<n>)` under `<n>*<m>:=<n+m>`, Ignatiev normal form)
  is strict monoidal, faithful on generators. The law is FORCED to be depth-ADDITION: conjunction
  (`otimes=and`, idempotent) sends `S^1^S^1=S^2 |-> <1>and<1>=<1>`, collapsing `H^2` against the
  frozen strictness `<2> !~ <1>`. Beklemishev's reduction `<n+1> ≡ <n>^omega` is an INTERNAL
  coherence iso of `GLP^+`, not part of `Coh`'s monoidal data (smash stays finite; `omega` spent
  inside the target). `Coh(holim_n S^n = S^omega) = <omega>`, the first limit modality of
  `GLP_Lambda` (Fernandez-Duque--Joosten 2013, ordinal `epsilon_0`), the transfinite cell
  phantom-decorated (`lim^1 = Zhat_m/Z`); the pcf `mu = pp(aleph_omega)` and the ordinal
  `epsilon_0` are torsor-LINKED (Feferman path, Thm 147c), NOT equal. **Pathology 148d:** a
  `Sigma_1` "fair coin" (parity of the least deciding proof) tie-break is STILL an orientation --
  no algorithm can abstain; `Z/2` is the cohomological trace of a non-computable abstention.
  Machine `code/scripts/check-pass148.py` ->
  `artifacts/reports/pass148-sigma1-orientation-coh-monoidal-law-check.json` (A monodromy `-1`
  connected vs `+1` split over `C_6,C_7,C_8`, orientation census 0 of `2/6/24` linear orders
  fails to orient; B conjunction no-climb vs depth-addition climbs; C 0 `delta`-fixed linear
  orders `n=2..5`; overall PASS). Refs: Guaspari-Solovay 1979 (Ann. Math. Logic 16, 81-99);
  Cantini 1990 (JSL 55, 244-259); Feferman 1991 (JSL 56, 1-49); Kripke 1975; Beklemishev 2004
  (APAL 128, 103-123); Ignatiev 1993 (JSL 58, 249-290); Fernandez-Duque-Joosten 2013 (JSL 78,
  543-561).
- **[Resolved (Pass 150), (a),(b); residues carried to `[New (Pass 150)]`]** **Make the schematic
  `Z/2` an honest derived class, and settle the phantom-witness question for reflection antimatter.**
  Opened by Pass 149 (Thm 149b produces the symmetric `(Z,Z/2)` only as a Cech `H^0` over the
  realization diagram, not yet as a `Sigma_1`-definable cohomology object; Thm 149c leaves `-<n>`
  as a formal `K_0`-class with no decided model status).
  RESOLUTION. (a) **Thm 150a (schematic `Z/2` = effective `H^1`, `ISigma_1`-cheap, de-localized):**
  the sign sheaf `sgn` on `Real(boxt)` has, CLASSICALLY, `H^0 != 0` (a separating set exists by
  `AC`) and Cech `H^1 = 0` (the singleton-race cover is discrete), so the schematic `Z/2` is NOT a
  classical class. EFFECTIVELY, the subsheaf `sgn^{Sigma1}` of `Sigma_1`/c.e. sections has
  `H^0(Real; sgn^{Sigma1}) = 0` (a c.e. global section is a recursive separator of the Kleene pair
  `A={e:phi_e(e)=0}`, `B={e:phi_e(e)=1}`, none exists) and represents the NONTRIVIAL class
  `[sgn^{Sigma1}] = 1 in H^1_{eff}(Real; Z/2) = Z/2`; this nonvanishing is `ISigma_1`-provable
  (effective inseparability = uniform diagonal, recursion theorem), whereas concentrating the class
  onto one stalk (`H^0(sgn)(kappa) = Z/2`, Pass 148) costs the KF ordinal `phi_{epsilon_0}(0)`.
  Hence "`Sigma_1`-schematic not `Sigma_1`-pointwise" = the `Z/2` is DE-LOCALIZED (`ISigma_1`-cheap
  global `H^1`, `phi_{epsilon_0}(0)`-expensive pointwise `H^0`). (b) **Prop 150b.1 (`omega`-absolute
  chirality):** every `omega`-sound reflection principle has grade `>= 0` (`GLP^+=(N,+)`
  well-founded, least `<0>`); no negative grade is `omega`-realized. **Thm 150c (phantom witness +
  SW duality):** `A_{-1} := PA + ¬Con(PA)` is consistent (Goedel II), `Pi_1`-sound, and
  INTERPRETABLE in `PA` (Feferman 1960, ACT), carrying a NONSTANDARD proof of `bot` -- the `-<1>`
  phantom witness, `≡_T`-invisible over `N`; `Pi_1`-conservative and interpretability-below `PA`
  but NOT `Sigma_1`-conservative; the phantom fiber over `-<1>` is `2^{aleph_0}` (Lindstrom
  density). `D : Real(boxt)^{op} -> SW^{ph}` is the SW antipode `s:k|->-k` on `K_0=Z` (`D^2=id`,
  fixed locus `{0}=S^0=T`-floor, free off it), sending the Pass-53 `lim^1=Zhat_m/Z` phantom POINT
  to the interpretability ANTIMATTER `-<n>`, landing only in the phantom-completed `SW^{ph}`.
  Chirality is ABSOLUTE over `omega`, PHANTOM-BROKEN over interpretability. **Pathology 150d:**
  `PA+¬Con(PA)` proves its own inconsistency yet never proves a false `Pi_1` fact. Machine
  `code/scripts/check-pass150.py` ->
  `artifacts/reports/pass150-effective-derived-z2-phantom-witness-sw-duality-check.json` (A `K=8`
  all races oriented, 0 indexed separators, uniform defeat, discrete cover `H^1_classical=0`,
  effective class `Z/2`; B grades monotone/least `<0>`/`K_0=Z`; C `PA+¬Con` consistent/`Pi_1`-sound/
  interpretable/grade `-1`/`N`-invisible/fiber `2^{aleph_0}`; D `D^2=id`, fixed `{0}`,
  `{1..4}<->{-1..-4}`, `sw_fixed=1`; overall PASS). Refs: Rogers 1967; Feferman 1960 (Fund. Math.
  49, 35-92); Feferman 1991 (JSL 56, 1-49); Cantini 1990 (JSL 55, 244-259); Lindstrom 2003
  (Aspects of Incompleteness, LNL 10); Beklemishev 2004 (APAL 128, 103-123); Spanier-Whitehead 1955
  (Mathematika 2, 56-80).

- **[New (Pass 150)]** **Realize `(Z,Z/2)` in one explicit bicomplex over an effective site, and
  promote the point/antimatter Spanier-Whitehead duality to an honest functor.** Opened by Pass 150
  (Thm 150a locates the schematic `Z/2` as `H^1_{eff}` but leaves the Ershov/realizability site and
  the `RGamma`-computation as sketches; Thm 150c pins `D` on grades only, not as a natural functor).
  (a) Build the effective site explicitly: give the Ershov/realizability Grothendieck topology on
  `Real(boxt)` in which c.e. families are covers, prove `RGamma` there computes
  `H^0(sgn^{Sigma1}) = 0` and `[sgn^{Sigma1}] = 1 in H^1_{eff} = Z/2`, and assemble the single
  bicomplex whose total cohomology is `(H^1(cover tower) = Z, H^1_{eff}(sgn) = Z/2) = (Z,Z/2)` --
  unifying the detachment phantom (vertical `varprojlim^1 = Zhat_m/Z`) and the orientation gap
  (horizontal effective `Z/2`) as two edges of one derived object, and pinning the exact `ISigma_1`
  vs `phi_{epsilon_0}(0)` proof-theoretic boundary between the horizontal (schematic) and pointwise
  (concentrated) readings.
  (b) Promote `D : Real(boxt)^{op} -> SW^{ph}` to an honest functor: prove naturality of the pairing
  sending each positive-grade `lim^1` phantom point to its negative-grade interpretability-antimatter
  class `-<n>`, decide whether `D` is an equivalence onto `SW^{ph}` or only a faithful embedding, and
  test whether the continuum-width phantom fiber (Lindstrom density downstairs) is `D`-dual to the
  uncountable `Zhat_m/Z` phantom (Pass 53 upstairs) as an iso of `2^{aleph_0}`-torsors -- the final
  Spanier-Whitehead statement that the `G2-ZOO`'s positive detachment spectrum and its negative
  interpretability spectrum are one object seen through the mirror `s`. Connects to the Pass-69
  `Con^{orb}` open problem and the Pass-51/53 integral-unit dictionary.
  (a) Upgrade the SCHEMATIC `Z/2` of Thm 149b to an honest object: define a `Sigma_1`-parametrized
  sheaf of orientation double covers over the realization diagram `Real(boxt)` and prove its first
  Cech/`lim^1` cohomology is a `Sigma_1`-definable `Z/2` -- locate `(Z,Z/2)` NOT as a point of
  `ConLat_PA` but as a class in a DERIVED enhancement `R\Gamma(ConLat_PA; sgn)`, making
  "`Sigma_1`-schematic, not `Sigma_1`-pointwise" precise as `H^0` vs `H^1` of one sheaf; test
  whether the effectively-inseparable carrier of 149b makes this class provably nonzero in `PA` or
  only in a reflection extension.
  (b) Decide the phantom-witness question for `-<n>`: is there a conservative (`Pi^0_1`- or
  interpretability-) extension of `PA` in which the SW co-reflection `-<n>` acquires a NON-standard
  sentential witness (a phantom principle, `≡_T`-invisible over the standard model), or is
  chirality absolute (no model of `GLP` realizes a negative grade)? If a phantom witness exists,
  promote the `s`-conjugacy of Pathology 149e to an honest duality functor
  `Real(boxt)^op -> SW` sending each detached fixed point's `lim^1` phantom point to a
  reflection-antimatter class, closing the "phantom point upstairs / phantom antimatter
  downstairs" loop into a single Spanier-Whitehead duality on the whole `G2-ZOO`. Connects to the
  Pass-69 `Con^{orb}` open problem and the Pass-51/53 integral-unit dictionary.

- **[Resolved (Pass 149), (a),(b); residues carried to `[New (Pass 149)]`]** **Close the
  completeness half of the orientation dichotomy, and promote `Coh` to a functor on the full
  stable/derived category.** Opened by Pass 148 (Thm 148a is proved only for boxes with a
  `Delta_0` linear proof order; Thm 148c is monoidal only on the positive cone).
  *Resolution (Pass 149):* (a) **Thm 149a** proves "admits a `Delta_0` linear proof order" is
  POINTWISE eliminable -- every realized detached fixed point is oriented (`H^0_pt(sgn)=0`,
  signature `(Z,0)`) because its singleton race involves two standard proof codes with a `Delta_0`
  comparison; a non-terminating race is a degenerate oriented (empty-section) stalk, not a gap.
  **Thm 149b** exhibits, via a recursively-inseparable c.e. pair `(A,B)`, a `Sigma_1` proof order
  that is SCHEMATICALLY unorientable and carries a genuine `boxt`-fixed sentence, so `(Z,Z/2)` is
  `Sigma_1`-SCHEMATIC but NOT `Sigma_1`-POINTWISE: Thm 148b PRESERVED and SHARPENED, the pointwise
  gap forces KF ascent while a `Sigma_1` avatar survives one level up. (b) **Thm 149c**: `GLP^+ =
  (N,+)` is not a group (Ignatiev well-order), `K_0 = Z`, and the negatives `-<n>` are reflection
  PHANTOMS (`Pi`-conservativity is a morphism `<n>->0`, not an inverse). **Thm 149d**: the `delta`
  orientation flip IS the Spanier-Whitehead antipode -- one order-2 involution `s:k|->-k` on
  `K_0=Z`, fixed locus `{0}=S^0=T`-floor, free off it; the KF gap cocycle `H^0(sgn)=Z/2` is its
  equivariant class, unifying both prongs. Verified by `code/scripts/check-pass149.py` (overall
  PASS), report `artifacts/reports/pass149-orientation-completeness-sw-antimatter-check.json`.
  (a) Prove or refute that NO `Sigma_1` box over `PA` with a NON-standard (non-`Delta_0`-linear)
  proof predicate `Prf` -- e.g. a recursively-inseparable pair coded as an unorientable partial
  order of proofs -- can carry a `delta`-symmetric detached fixed point with `H^0(sgn) = Z/2`. If
  such unorientable `Sigma_1` proof orders exist, `(Z,Z/2)` descends to `ConLat_PA` after all,
  REFUTING Thm 148b's strict non-`Sigma_1` claim; if not, the KF ascent is absolutely forced and
  "admits a `Delta_0` linear proof order" is eliminable from Thm 148a.
  (b) Promote `Coh` to a monoidal functor on the FULL stable/derived category: give the reflection
  avatar (or prove its absence) of the negative Grothendieck classes `-[S^n]`; note `GLP^+` does
  NOT extend to a graded group (Ignatiev well-order has no inverses), so identify the "reflection
  antimatter" as a Spanier-Whitehead dual / co-reflection (dual GLP, downward modalities), and
  test whether the Spanier-Whitehead involution on `Sph` matches the `delta` orientation flip of
  prong (a) -- unifying both prongs under one duality. Connects to the Pass-69 `Con^{orb}` open
  problem and the Pass-51/53 integral-unit dictionary.
  (a) Decide whether the symmetric `(Z, Z/2)` KF signature is realisable ALREADY inside
  `ConLat_PA` -- is there a Rosser-invisible, `lim^1`-detected `boxt`-fixed point over PA
  itself -- or whether `delta`-symmetry PROVABLY forces ascent to a truth-theoretic / reflection
  extension (KF ordinal `phi_{epsilon_0}(0)`). Sharpen: does a `Sigma_1`-definable well-ordering
  of proofs force EVERY detached fixed point to be orientable (Rosser `(Z,0)`), making unoriented
  detachment `(Z,Z/2)` intrinsically non-`Sigma_1`; and pin the exact embedding
  `ConLat_T \hookrightarrow ConLat_{KF}` carrying `kappa`.
  (b) Promote `Coh` from a generator-level monoid map to a genuine monoidal functor: specify the
  source category (cover-system tower under suspension/smash), decide the target monoidal law
  (GLP concatenation vs conjunction), and construct the transfinite extension sending the first
  TRANSFINITE coherence stage (`varprojlim` over the whole `omega`-tower of suspensions) to the
  first LIMIT modality `<omega>` of `GLP_Lambda`, testing whether the `n=1` layer's
  regular-height-`mu` (`aleph_omega`-analogue) home matches `<omega>`'s proof-theoretic ordinal
  via the Feferman path torsor of Thm 147c. Connects to the Pass-69 `Con^{orb}` open problem and
  the Pass-51/53 integral-unit dictionary.
  (a) Construct an explicit Kripke-Feferman fixed point `kappa` (partial-model / fixed-point
  semantics) and verify it carries BOTH `varprojlim^1 != 0` (not provably equivalent to any
  iterate `boxt^n T`) AND `H^0(sgn) = Z/2` (no witness-comparison orientation) -- separating
  KF from Rosser inside `Fix(boxt) subseteq ConLat_T`.
  (b) Construct `Coh : (B[Z] cover systems) -> GLP`-tower sending `varprojlim^n B[Z]` to the
  `n`-fold reflection layer `<n>`, carrying Bousfield-Kan degree to GLP modality depth, with
  `<n> !~ <n+1>` (Beklemishev 2004) matching `H^n(S^n) = Z`; decide whether the `n = 1` layer
  is the image of the first LIMIT modality `<omega>` (transfinite reflection / `omega`-consistency)
  and whether Thm 146c's Feferman path-dependence is a genuine metamathematical independence
  THEOREM rather than an analogy. Connects to the Pass-69 `Con^{orb}` open problem and the
  Pass-51/53 integral-unit dictionary.
  (a) Construct explicitly `Or-bad(S_mu) -> Fix(boxt) subseteq ConLat_T` sending an oriented
  bad point to a Rosser fixed point and a good point to a Loeb fixed point; verify functoriality
  under scale end-extension and that the `Z/2` orientation torsor maps to the Rosser
  proof-ordering choice. Decide whether a SYMMETRIC bad point lands on a Kripke--Feferman fixed
  point that is `varprojlim^1`-detected but Rosser-invisible.
  (b) Decide whether the ZFC-constant `varprojlim^n B[Z]` (`n >= 2`, Cor 145b) is the shadow of
  an ARITHMETIC absolute object -- e.g. an `nFG2(n)`-strictness witness independent of ambient
  cardinal arithmetic -- so that Pathology 145e becomes a statement about which `nFG2` layers
  are provably strict vs forcing-fragile. Concretely: is there a provability predicate whose
  `n`-th derived-consistency layer realizes `varprojlim^n B[Z]` for `n >= 2` while its `1`-st
  layer's (non)triviality tracks approachability at a metamathematical `aleph_omega`-analogue?
  Connects to the Pass-69 `Con^{orb}` open problem and the Pass-51/53 integral-unit dictionary.
  (a) Prove the pullback naturality of Thm 144a.i: show the coordinate projection
  `pi : [mu]^{<omega} -> [omega_{n+1}]^{<omega}` is cofinal-type-preserving on the CLH sub-nerve,
  so `pi^*` is a pro-isomorphism of the `n >= 2` cover-fiber towers across all `mu in Lambda`;
  identify the failure locus if `mu` is a `pp`-maximal vs sub-maximal generator (does
  `max Lambda = pp(aleph_omega)` carry an EXTRA top-generator class the shorter scales miss?).
  (b) Prove Thm 144a.ii's per-`mu` non-tightness: decide whether EVERY `mu in Lambda` carries a
  nontrivial `(mu, .)`-Hausdorff gap (bad/non-good point of `S_mu`), or whether a `mu` all of
  whose scales are tight/good collapses its level-1 class -- is the level-1 stratification
  faithful on all of `Lambda`, or only on the non-good part of the pcf spectrum? Connect the
  good/bad-point dichotomy to the `Con^{orb}` consistency-tower (Pass-69 open problem): does an
  orbit-attached (good) scale correspond to a Loeb/orbit-attached fixed point and a bad
  (gap-bearing) scale to a detached Rosser fixed point, extending the Pass-51/53
  integral-vs-non-integral unit dictionary to the transfinite pcf setting? The
  `[New (Pass 140)]` (b) certified-linearity bit is carried here.
  *(Original Pass-142 statement, now resolved (a,b) / carried (c) above: (a) construct or
  obstruct the transfinite `n`-coherent family on `[pp(aleph_omega)]^{<omega}` via lifting
  Todorcevic `rho`-functions / minimal-walk oscillation; (b) pin the destruction strength
  ZFC vs weakly compact, split-point single-`lim^1` = `MA_{aleph_1}` (Cor 141e) vs
  simultaneous all-`n`; (c) does the pcf window stratify the phantom.)*
- **[Superseded (Pass 140)]** _(was [New (Pass 139)] original phrasing of the strictness
  dichotomy prong (a); resolved above, prongs (b),(c) re-opened as `[New (Pass 140)]`)_
  Deciding the strictness dichotomy, the `cd = omega` diagonal, and the certified-linearity
  bit. Original Pass-139 statement:
  (a) DECIDE the Thm-139b horn: does `cd(A) <= 1` (graph nerve, absolute) BOUND the
  set-theoretic `varprojlim^{>=2} A`? Compute/bound the cohomological dimension of
  the MP cover-fiber tower AS AN INVERSE SYSTEM over its `omega^omega`-index
  (Goblot's `cf`-bound vs the graph-nerve `cd = 1`), settling whether
  `(forall n) h_n <=> h_1` (horn I) or `(forall n) h_n` overshoots into the
  `aleph_{omega+1}` regime (horn II). Discharge Cor 139c's residual obligation:
  verify `h_1(A)` (not merely `b >= aleph_2`) holds in `MA_{aleph_1} + 2^{aleph_0}
  = aleph_2` at the required additivity strength.
  (b) FRONTIER prong (iii) [carried from `[New (Pass 138)]` (c)]: decide whether the
  `cd`-graded tower `{A^{(a),k}}` admits a diagonal `cd = omega` object (a coherence
  datum of infinite cohomological dimension) and whether its `varprojlim^*` spectrum
  is the union of finite-level phantoms or a genuinely new transfinite obstruction --
  the `nFG2(omega)` limit of the strict `nFG2(k)` tower located by Pass 139.
  (c) [carried from `[New (Pass 138)]` (d)] Locate the "certified-linearity bit"
  `T |- Lin(-<)` inside `ConLat_T`: is the single Boolean that PL detects
  (Thm 138c(b)) the shadow of a consistency-strength jump (the
  `I-Sigma_{k-1}`/`I-Sigma_k` boundary of Thm 137d), and does the Rosser
  weak-consistency principle `WC` correspond to a named point of the `Con^{orb}_n`
  tower (Pass 69)?
- **[Resolved (Pass 138), (a); (b),(c) carried to `[New (Pass 138)]`]** _(was
  [New (Pass 137)])_ **The `I-Sigma_n`-graded Rosser tower, and the two surviving 2-cd
  frontiers.** **(a) RESOLVED (Pass 138).** The explicit Guaspari--Solovay Rosser
  `D2`-countermodel: with the disjunctive consequent `B := A v D` and `A,D` GS
  witness-comparison fixed points over `graph(-<)`, `T |- A -> B`, so
  `T |- Box_R^{-<}(A->B)` by Rosser-`D1` (that conjunct is free); the content is
  `T |- !Con_T -> (Box_R^{-<}A ^ !Box_R^{-<}B)` via the non-monotonicity of `Box_R`
  at `A |-> A v D` (the Rosser opponent shifts `neg A -> neg A ^ neg D`, whose least
  `-<`-proof can precede that of `A v D`), whence
  `T |/- (Box_R(A->B) ^ Box_R A) -> Box_R B` and **every** `M |= T + !Con_T` is a
  countermodel (**Thm 138a**); Rosser consistency `T |- !Box_R_|_` survives.
  **Lemma 138b (`N`-adequacy):** for consistent `T`, `N |= Box_R^{-<}C <=> T |- C`
  INDEPENDENT of `-<` (standard witness = genuine proof; least proof vacuously
  Rosser), so the `D2` conjunction is **false in `N`** for all standard `C` -- the
  countermodel is necessarily NONSTANDARD (a model of `!Con_T`), and Thm 137c's
  "`!D2` in `N`" is the metatheoretic `T`-underivability, EQUIVALENT by completeness
  to the `!Con_T` model. **Thm 138c (PL sees only the bit `T |- Lin`):** over a base
  proving `Lin(-<)` (e.g. `PA`), `PL_T(Box_R^{-<})` is the single Guaspari--Solovay
  Rosser logic for every order-type-`omega` tag order, INVARIANT under the
  `I-Sigma_n` tag-growth rank of Thm 137d; the separating modal principle is Rosser
  weak-consistency `WC(X) := !(Box_R X ^ Box_R neg X)`, which is in `PL_T` iff
  `T |- Lin(-<)` -- valid in every consistent LINEAR world (the `-<`-least element of
  `prf(X) u prf(neg X)` lies on one side only), false under a partial order (two
  incomparable minimal proofs). So the Thm-137d grading collapses, for `PL`, to one
  Boolean; the conjecture "order type only" is CONFIRMED above the linearity
  threshold and SHARPENED below it (`PL` sees the bit, not the finer rank).
  **Pathology 138d:** `WC` separates the p.r. order from the Ackermann order `-<_A`
  (137e) over `I-Sigma_1` (where `Lin(-<_A)` is unprovable) but NOT over `PA`.
  Machine-verified `artifacts/reports/pass138-gs-d2-countermodel-ordertype-invariance-check.json`
  (A/B/C/D, overall PASS) via `code/scripts/check-pass138.py`. **(b),(c) CARRIED**
  verbatim to `[New (Pass 138)]`. Original Pass-137 statement:
  (a) DISCHARGE the Thm-137c(2) carried obligation: write the explicit Guaspari-Solovay
  Rosser `D2`-countermodel over `T[graph(-<)] + Lin(-<)` -- a concrete arithmetic instance
  `Box_R^{-<}(A->B) ^ Box_R^{-<}A ^ !Box_R^{-<}B` -- and DECIDE the question raised by
  Thm 137d: does the provability logic `PL(Box_R^{-<_t})` depend on the tag GROWTH RANK
  (the `I-Sigma_n` certification level) or only on the ORDER TYPE of `-<_t`? *Conjecture:*
  order type only -- all tag orders of type `omega` give the same Guaspari-Solovay `R`, so
  the `I-Sigma_n`-grading (Thm 137d) is a purely metatheoretic filtration invisible to
  `PL`; test against the Ackermann order `-<_A` (Pathology 137e). If instead `PL` DOES see
  the rank, exhibit a modal formula separating two order-type-`omega` tag orders of
  different `I-Sigma_n` strength.
  (b) FRONTIER prong (ii) [carried from `[New (Pass 136)]` (ii)]: attempt the `b = aleph_1`
  simultaneous-vanishing forcing (BLH21-style) deciding
  `Con((forall n) h_n(A) ^ varprojlim^2 A^{(a),2} != 0)`, using Thm 136b (`cd = 2`
  absolute) to certify the target is a genuine level-2 obstruction; either exhibit the
  model (strict gap `A_kappa =/=> (forall n)h_n`) or reduce it to a named higher
  additivity-of-ideal invariant.
  (c) FRONTIER prong (iii) [carried]: decide whether the `cd`-graded tower `{A^{(a),k}}`
  admits a diagonal `cd = omega` object (a coherence datum of infinite cohomological
  dimension) and whether its `varprojlim^*` spectrum is the union of the finite-level
  phantoms or a genuinely new transfinite obstruction.
- **[Resolved (Pass 137), (i) LIMITATIVE + pivot; (ii)/(iii) carried to `[New (Pass 137)]`]**
  _(was [New (Pass 136)])_ **Discharging Prop 136d and opening the 2-cd forcing frontier.**
  **(i) RESOLVED (Pass 137) -- disjunct (b) is VACUOUS; pivot to disjunct (a), graded.**
  **Thm 137a (I-Sigma_1 linearity forces primitive recursion):** if `phi(x,y)` is `Sigma_1`
  and `I-Sigma_1` proves `phi` a strict linear order (irreflexivity, transitivity,
  asymmetry, trichotomy), then the comparison `{(x,y):phi(x,y)}` is PRIMITIVE RECURSIVE --
  provable trichotomy+asymmetry give `I-Sigma_1 |- !phi(x,y) <-> (x=y v phi(y,x))` (RHS
  `Sigma_1`), so `phi` is provably `Delta_1`, `chi_phi` is `I-Sigma_1`-provably-total
  recursive, hence p.r. by Parsons-Mints-Takeuti. **Cor 137b:** there is NO `Sigma_1`,
  non-p.r. strict linear order that is `I-Sigma_1`-provably linear; the Prop-136d obligation
  "verify in `I-Sigma_1` that the non-p.r. tag order `-<` is linear" is UNSATISFIABLE, and
  linearity of a genuinely non-p.r. tag order is a true `Pi_2` sentence of `N` that
  `I-Sigma_1` cannot prove. **Thm 137c (order-robustness):** for ANY linear `-<` with a
  `-<`-least element, `!D2 ^ !Box_R^{-<}_|_` hold in `N` (the Guaspari-Solovay Rosser
  mechanism uses only linearity + least element + the Rosser fixed point, never
  primitive-recursiveness of `-<`); p.r.-ness controls only the `I-Sigma_n` LEVEL that
  certifies them. **Thm 137d (I-Sigma_n-graded Rosser tower):** if the tag map is provably
  total exactly in `I-Sigma_k \ I-Sigma_{k-1}` then `I-Sigma_k |- (Lin(-<) -> !D2 ^ Con_R)`
  for `Box_R^{-<}` while `I-Sigma_{k-1}` does not -- a strictly increasing certification
  hierarchy, all levels sharing the standard-model profile `D1 ^ !D2 ^ !Box_R_|_`.
  **Pathology 137e (Ackermann-scrambled order):** `-<_A` (`t(n) = <A(n), n>` lex, `A`
  Ackermann) is `I-Sigma_2`-provably linear but NOT `I-Sigma_1`-provably linear (`Lin(-<_A)`
  entails `A` total), comparison total-recursive but non-p.r., pinning the
  logic-vs-realizability gap to exactly one `I-Sigma_n` level. So the `m_enc = O(1)`/non-p.r.
  `-<` of Prop 136d is genuine, but its box-level payoff is metatheoretic (finitely
  uncertified, standard-model true) -- a "finitely uncertified, standardly Rosser" echo of
  Pass 55. *Carried obligations (-> `[New (Pass 137)]`):* the explicit GS `D2`-countermodel
  over `T[graph(-<)]`, and the `PL`-rank-vs-order-type question. **(ii)/(iii) CARRIED**
  verbatim to `[New (Pass 137)]` (b),(c). Machine `code/scripts/check-pass137.py` ->
  `artifacts/reports/pass137-isigma1-linearity-pr-shadow-orderrobust-d2-check.json`
  (strict-linear scrambled order on `[0,48)`; composition-non-monotone; `Box_R`-`D2`
  order-sensitive; super-cubic tag growth; overall PASS). Original Pass-136 statement:
  (i) Verify in `I-Sigma_1` that the Prop-136d tag-order `-<` is a linear order and that the
  Rosser box `Box_R^{-<}` preserves `¬D2 ^ ¬Box_R⊥` (confirm the tag map does not restore
  `D2` by respecting proof-concatenation) — thereby closing disjunct (b) of the Pass-134
  Skeptic residue at the BOX level; OR, if it fails, pivot to disjunct (a) and give the
  `I-Sigma_1`-over-`graph(-<)` cofinality proof upgrading Cor 134b to the full `Sigma_1`
  class.
  (ii) Begin the frontier: attempt the `b = aleph_1` simultaneous-vanishing forcing
  (BLH21-style) deciding `Con((forall n) h_n(A) ^ varprojlim^2 A^{(a),2} != 0)`, using
  Thm 136b (`cd = 2` absolute) to certify the target is a genuine level-2 obstruction rather
  than a re-indexed level-1; either exhibit the model (strict gap `A_kappa =/=> (forall n)h_n`)
  or reduce it to a named higher additivity-of-ideal invariant.
  (iii) Decide whether the `cd`-graded tower `{A^{(a),k}}` admits a diagonal `cd = omega`
  object (a coherence datum of infinite cohomological dimension) and whether its
  `varprojlim^*` spectrum is the union of the finite-level phantoms or a genuinely new
  transfinite obstruction.
  (i) Decide the residual additivity consistency
  `Con((forall n)h_n(A) ^ varprojlim^2 A^{(a),2} != 0)` -- does an `omega_1`-cofinal 2-coherent
  a-primary system keep `varprojlim^2 != 0` in a model where the distinguished twin tower `A`
  trivializes at every level (2-cd BBMT additivity; test under `b = aleph_1` against a
  simultaneous-vanishing forcing à la Bergfalk-Lambie-Hanson 2021), thereby DECIDING
  `A_kappa <=> (forall n)h_n` or exhibiting the first strict gap.
  (ii) Discharge the Thm-135a finite `cd`-proxy to a FULL proof that coherence cohomological
  dimension `cd(A^{(a),k)}) = k` for the a-primary `k`-coherent MP systems (a strict `cd`-graded
  tower, no dimension collapse), and decide whether `cd` and the `cf`-rank grading of Thm 134d
  coincide or are independent invariants.
  (iii) Settle the Pass-134 Skeptic residue (i): supply the `I-Sigma_1`-over-`graph(-<)`
  cofinality proof for the exotic non-p.r. ordering (upgrading Cor 134b to the full `Sigma_1`
  class), or construct the pathological `Sigma_1` ordering with `m_enc = O(1)` reopening the
  logic-vs-realizability gap.
- **[Resolved (Pass 135), (ii) primary; (iii) advanced; (i) carried]** _(was [New (Pass 134)])_
  **The exotic-ordering `m_enc` residue, the explicit `A^{(a),2}`
  level-2 separator, and the `cf`-indexed rank-spectrum tower.**
  **(ii) RESOLVED as a structural NON-TRANSFER + a CORRECTION.** **Thm 135a
  (cohomological-dimension non-transfer):** the retract-transfer that trivialized `n=1`
  (Thm 133c/134e -- every 1-coherent `B` is a retract of the twin tower's 1-skeleton, so
  `h_1(A) => varprojlim^1 B = 0`) has NO analogue at `n=2`, for a reason PRIOR to any set theory:
  the distinguished twin tower `A` is a 1-dimensional coherence datum (chain/tree index,
  `cd(A) <= 1`), so `varprojlim^{>=2} A = 0` IDENTICALLY and `h_2(A)` is VACUOUS, transmitting
  nothing to a 2-cd system; since `cd(A^{(a),2}) = 2 > 1 = cd(A)`, no retraction of the
  2-coherent obstruction onto the tower can exist. **Correction 135b:** the Pass-134 heuristic
  modelling `A^{(a),2}` as "two 2-simplices sharing a vertex" is WRONG -- that wedge is
  CONTRACTIBLE (all reduced `Betti_{F_3} = 0`, machine-checked) and hosts no 2-class; the honest
  minimal 2-coherence obstruction is 2-SPHERICAL (`H_2(S^2; F_a) = F_a`), and the no-retraction
  `Delta^{n+1} -> S^n` is degree-UNIFORM -- the `n=1`-vs-`n=2` asymmetry is carried ENTIRELY by
  `cd(A)`, not by any `n`-dependence of the retraction lemma. **Thm 135c (sharpened, not
  resolved):** strictness `(forall n)h_n(A) =/=> A_kappa` reduces to the pure consistency
  `Con((forall n)h_n(A) ^ varprojlim^2 A^{(a),2} != 0)`, a concrete 2-cd instance of the OPEN
  BBMT additivity (Bergfalk-Lambie-Hanson 2021; Bannister-Bergfalk-Moore-Todorcevic),
  NON-VACUOUS since `varprojlim^2 A^{(a),2} != 0` is CH-consistent.
  **(iii) ADVANCED -- Thm 135d (de-arithmetization ladder):** the `cf`-indexed spectrum
  `aleph_0 < aleph_1 < aleph_2 < ...` (Thm 134d) is `cd`-graded; its `cd=0`/`n=0`/`aleph_0`
  FLOOR is EXACTLY the Pass-55 `G2 ^ ¬FG2` solenoid phantom `hatZ_a/Z` (a-primary, Prufer-rigid
  `kappa_a = 1`, Pass 130/131), the ZFC-ABSOLUTE arithmetic bottom of the same tower whose
  `n=1` rung is Suslin-sensitive (MP88/DSV89). **(i) CARRIED:** the exotic `Sigma_1`-but-not-p.r.
  witness-ordering residue is not finitely decidable (Part E dichotomy). Machine-verified
  `artifacts/reports/pass135-cohdim-nontransfer-a2coherent-check.json` (exact `F_3` simplicial
  homology; overall PASS). Successor `[New (Pass 135)]` opened above. Original Pass-134 statement:
  (i) Decide the Thm-134a exotic residue: can a `Sigma_1`-but-not-primitive-recursive witness
  ordering `-<` hide `m_enc`? Either exhibit a pathological box with non-p.r. `-<` and
  `m_enc = O(1)` keeping `¬D2 ^ ¬Box_R⊥` (refuting the universal for all `Sigma_1` boxes and
  reopening the logic-vs-realizability gap), or give a `Sigma_1`-induction proof that the
  Thm-134a plant is cofinal for EVERY `Sigma_1` ordering (upgrading Cor 134b to the full
  `Sigma_1` class).
  (ii) Construct `A^{(a),2}` explicitly as a 2-coherent a-primary system and compute
  `varprojlim^2 A^{(a),2}` under `b = aleph_1` vs `MA_{aleph_1}` (or the 2-dimensional BBMT
  `Delta`-system principle): is it a genuine Thm-134e separator
  (`Con((forall n)h_n(A) ^ varprojlim^2 A^{(a),2} != 0)`) or does level-2 triviality also
  transfer by a 2-skeleton retract, pushing BBMT one dimension?
  (iii) Map the full `cf`-indexed rank spectrum of Thm 134d: for each `n` pin the forcing
  axiom separating rank `aleph_n` from `aleph_{n+1}`, decide whether the spectrum is a strict
  ZFC tower or can collapse (adjacent ranks forced equal), and tie the a-primary torsion tower
  back to the Pass-55 `G2 ^ ¬FG2` solenoid phantom (single-prime `Z_p/Z` = the `n=0`,
  arithmetic `aleph_0` floor of this very tower).
- **[Resolved (Pass 134), (i)-(iii) with two corrections and one carried obligation]** _(was
  [New (Pass 133)])_ **The `m_enc`-unboundedness obligation, the a-primary intermediate
  strong-homology object, and the two-system witness for `A_kappa`.**
  **(i) RESOLVED (with a scope correction).** **Thm 134a:** for every
  PRIMITIVE-RECURSIVE-ordered `Sigma_1` witness-comparison Rosser box with `¬D2 ^ ¬Box_R⊥`,
  `m_enc` is UNBOUNDED -- no p.r. uniform nested-witness bound `B` certifies witness-bounded
  full `D3` -- by the ordering-INTERNALIZATION diagonal (`phi*_k` plants a `Prf`-code of
  `¬Box_R phi*_k` in the gap `(k, B(k)]` defined FROM the Godel numbers of both `-<` and `B`;
  a p.r. re-ordering `pi` only relabels a gap of the same asymptotic width). **Cor 134b:**
  Conj 132d CLOSED for the standard class, pinning `PL(Box_R^A) = R+4` arithmetically
  INCOMPLETE at full `D3`. *Correction:* the open problem's "EVERY `Sigma_1` box" overstates;
  the honest universal is "every p.r.-ordered `Sigma_1` box", the exotic non-p.r. ordering
  carried as `[New (Pass 134)]` (i).
  **(ii) RESOLVED (with a CH correction and a uniqueness REFUTATION).** **Thm 134c:** the
  a-primary MP coherent system `A^{(a)}` on `(^omega omega, <=^*)` has `varprojlim^1 != 0`
  under `b = aleph_1` (Mardesic-Prasolov 1988), `= 0` under `MA_{aleph_1}`
  (Dow-Simon-Vaughan 1989), rank = least non-trivializable coherent family `= aleph_1` at
  `b = aleph_1`; the strictly-INTERMEDIATE witness is NOT CH (`aleph_1 = c` there) but the
  COHEN model `b = aleph_1 < c = aleph_2`. **Thm 134d:** `aleph_1` is NOT the unique
  non-arithmetic layer -- `omega_n`-cofinal systems realize a strictly increasing `cf`-indexed
  spectrum `aleph_0 < aleph_1 < aleph_2 < cdots < 2^aleph0`; `aleph_1` is the FIRST.
  **(iii) REFRAMED.** **Thm 134e:** `A^{(a)}` at level 1 does NOT separate (Thm-133c `n=1`
  retract transfer kills 1-dim `lim^1`); the honest separator is the 2-coherent `A^{(a),2}`,
  reducing the `A_kappa <=> (forall n)h_n` converse to
  `Con((forall n)h_n(A) ^ varprojlim^2 A^{(a),2} != 0)` -- an EXPLICIT instance of the still-OPEN
  BBMT additivity question (carried as `[New (Pass 134)]` (ii)). Machine `check-pass134.py`
  overall PASS.
- **[Superseded (Pass 134)]** _(was [New (Pass 133)] original phrasing)_ **The `m_enc`-unboundedness obligation, the a-primary intermediate
  strong-homology object, and the two-system witness for `A_kappa`.**
  (i) Discharge the sole carried obligation of Thm 133f: prove (or refute) that EVERY `Sigma_1`
  witness-comparison Rosser box has UNBOUNDED coding overhead `m_enc` -- equivalently, that no
  `Sigma_1` Rosser box admits a primitive-recursive uniform nested-witness bound `B`
  certifying witness-bounded full `D3`. A proof upgrades Thm 133f from the least-witness box to
  every `Sigma_1` Rosser box, completing Conj 132d and pinning `PL(Box_R^A) = R+4` as
  arithmetically INCOMPLETE at full `D3`; a pathological box with `m_enc = O(1)` keeping
  `¬D2 ^ ¬Box_R⊥` refutes it and collapses the LOGIC-vs-realizability gap.
  (ii) Construct the a-primary Mardesic-Prasolov coherent system `A^{(a)}` (on `[omega_1]^{<omega}`
  / `omega^omega`, `Z/a^n`-coefficients) explicitly and compute the exact `a`-primary rank of
  `varprojlim^1 A^{(a)}` under `b = aleph_1` vs `MA_{aleph_1}`, deciding whether the CH-realized
  `kappa_q = aleph_1` INTERMEDIATE torsion (Thm 133b) is the UNIQUE non-arithmetic layer strictly
  between the `Sigma_1` `oplus`-sum (`kappa_q <= aleph_0`, Thm 132a) and the ZFC-absolute
  `prod`-tower continuum (`kappa_q = 2^aleph0`, Thm 133a).
  (iii) Decide the Thm-133c placement by exhibiting the two-system separation: build a second
  coherent family `B` non-retractable from the distinguished twin tower at level `n>=2` and
  decide `Con((forall n)h_n(A) ^ varprojlim^1 B != 0)`; test whether `A^{(a)}` of (ii) is itself
  that witness (unifying prongs A/B/C at their successor).
- **[Resolved (Pass 133), A/B/C with two corrections and a reframing; one arithmetic obligation
  carried]** _(was [New (Pass 132)])_ **The analytic location of the continuum phantom, the
  `A_kappa <=> (forall n)h_n` placement, and the explicit `m_enc` `phi`-family.**
  **(A) CORRECTED.** **Thm 133a:** for ANY omega-indexed tower, `varprojlim^1` commutes with
  arbitrary PRODUCTS (product is an exact functor), so
  `varprojlim^1(prod_{i<omega}(Z, x a)) = (hatZ_a/Z)^omega` is ZFC-ABSOLUTE and nonzero
  (`q`-socle `F_q^omega`, dim `2^aleph0` by Erdos-Kaplansky) -- the continuum phantom carries NO
  forcing-axiom sensitivity, REFUTING the Pass-132 Next-step conflation with the strong-homology
  `A_{aleph_1}` limit. **Thm 133b:** Suslin-sensitivity lives in COFINALITY, not strand count:
  `varprojlim^1` fails to commute with uncountable direct SUMS only for an omega_1-cofinal
  COHERENT (Mardesic-Prasolov) index; the INTERMEDIATE `kappa_q = aleph_1` (CH-realized,
  `MA_{aleph_1}`-killed) object is the a-primary MP coherent limit, second-order over omega_1,
  NOT a `Sigma_1` graded predicate nor a strand sum. **(B) REFRAMED.** **Thm 133c:** `A_kappa
  => (forall n)h_n` trivial; the converse <=> the two-system separation
  `Con((forall n)h_n(A) ^ (exists coherent B) varprojlim^1 B != 0)` -- at `n=1` the twin tower is a
  retract of the universal 1-skeleton (transfers), at `n>=2` a non-retractable family blocks it;
  `A_kappa` a priori strictly stronger, exact equivalence the OPEN BBMT additivity question. **(C)
  DISAMBIGUATED + PINNED.** the schema-`4` reading of full `D3` is already Arai (Pass 127a), so
  Conj 132d is non-vacuous only under the WITNESS-BOUNDED reading; **Constr 133e / Thm 133f:** the
  `m_enc`-gap family flips `Box_R Box_R phi_k` cofinally for the least-witness box (dyadic/quadratic
  overhead; O(1) Arai repairs), so uniform witness-bounded full `D3` FAILS for `Box_R^{lw}`,
  reducing Conj 132d to the carried obligation "every `Sigma_1` Rosser box has `m_enc` unbounded"
  (opened as `[New (Pass 133)]` (i)). Machine `check-pass133.py` overall PASS.
- **[Superseded (Pass 133)]** _(was [New (Pass 132)] original phrasing)_ **The analytic location of the continuum phantom, the
  `A_kappa <=> (forall n)h_n` placement, and the explicit `m_enc` `phi`-family.**
  (i) PIN the analytic location of the `prod`-completion continuum phantom: is the
  nonvanishing of `varprojlim^1(prod_{i<omega}(Z, x a))` (equivalently the `kappa_q =
  2^aleph0` torsion of Cor 132a') exactly the strong-homology / `A_{aleph_1}` derived-limit
  statement (Suslin-sensitive, Pass 60d/61c), and does the `bigoplus`->`prod` boundary admit
  an INTERMEDIATE `aleph_1`-strand object with `kappa_q = aleph_1` under CH that is killed by
  `MA_{aleph_1}` -- a torsion analogue of the Pass-60d/61c independence? (ii) Decide the OPEN
  placement `A_kappa <=> (forall n)h_n` (or `A_kappa` strictly stronger) by testing whether
  `A_kappa` decides a `lim^n` of a coherent system OTHER than the distinguished twin tower
  that `(forall n)h_n` leaves open. (iii) Discharge Conj 132d by EXHIBITING the cofinal
  `m_enc`-inflating `phi`-family: explicit `phi_k` whose least-Rosser-witness of `Box_R phi_k`
  is provably below that of `Box_R Box_R phi_k` failing cofinally, thereby proving or refuting
  that uniform full `D3` is arithmetically incompatible with `¬D2 + ¬Box_R⊥`, and settling
  whether `PL(Box_R^A) = R+4` is arithmetically complete for Rosser boxes.
- **[Resolved (Pass 132), (i)-(iii); obligations o1'/o2' argued, positive forcing cited,
  Conj 132d carried]** _(was [New (Pass 131)])_ **Cross-layer independence lemmas, the
  multi-strand continuum phantom, the positive honesty forcing, and the arithmetic full-`D3`
  Rosser predicate.** **Thm 132a:** the `d`-strand graded Rosser predicate realizes
  `Phi = bigoplus_{i<d} hatZ_N/Z`, `kappa_q = d`; **arithmetic ceiling** -- every Sigma_1
  predicate has a recursive band family, so `kappa_q <= aleph_0` (natural limit = direct SUM).
  **Cor 132a':** continuum torsion `kappa_q = 2^aleph0` is realized ONLY by the direct PRODUCT
  completion (socle `F_q^omega`, dim `2^aleph0` by Erdos-Kaplansky), = the `aleph_1`-cofinal
  twin tower of Thm 131c; continuum-rank Prufer torsion has NO arithmetic-hierarchy
  representative, first appearing at the `bigoplus`->`prod` (arithmetic->analytic,
  Suslin-sensitive) boundary. o1'/o2' discharged by uniform band-relativized GS (recursion
  theorem with parameter `(i,k)`). **Thm 132b:** for every `n` a large-cardinal-free ZFC model
  of `h_1 ^...^ h_{n-1} ^ ¬h_n` at `2^aleph0 = aleph_n` (truncated BHLH `A_{n-1}` forcing +
  the Thm-131c ceiling); strict chain `A_kappa => (forall n)h_n => 2^aleph0 >= aleph_{omega+1}`,
  `A_kappa` at NEITHER endpoint, equivalence with `(forall n)h_n` OPEN. **Thm 132c:** over
  consistent `T`, `D1 ^ full-D3 ^ (T|-¬Box_R⊥) => ¬D2` is FORCED (5-line Loeb collapse).
  **Conj 132d:** no Sigma_1 witness-comparison Rosser box has uniform full `D3` (the `m_enc`
  overhead), so `PL(Box_R^A) = R+4` is arithmetically INCOMPLETE for Rosser boxes at full
  `D3` (modal `4 ^ ¬K ^ ¬Box⊥` consistent yet unrealized). Machine
  `check-pass132.py` PASS. Successor `[New (Pass 132)]` opened above.
- **[Historical, superseded by the block above]** **Cross-layer independence lemmas, the
  multi-strand continuum phantom, the positive honesty forcing, and the arithmetic full-`D3`
  Rosser predicate.**
  (i) Close Lemma-131b's o1'/o2' with an explicit uniform-in-`k` band-relativized
  Guaspari-Solovay cross-layer independence proof, and CONSTRUCT a genuine `d`-strand (then
  `omega`-strand) graded Rosser predicate realizing `kappa_q = d` (then `2^aleph0`), pinning
  where in the arithmetic hierarchy continuum-rank Prufer torsion first appears. (ii) Supply
  the POSITIVE half of the honesty ceiling -- a ZFC-only model of
  `h_1 ^ ... ^ h_{n-1} ^ ¬h_n` at `2^aleph0 = aleph_n` for general `n` -- and decide whether
  the BBMT `A_kappa` principle is STRICTLY between `2^aleph0 >= aleph_{omega+1}` and full
  `(forall n)h_n` or coincides with an endpoint. (iii) Attack the Thm-131e arithmetic
  obligation: does a `Sigma_1` Rosser predicate over `T \supseteq ISigma_1` satisfy
  `D1 ^ ¬D2 ^ (full D3)` with `T |- ¬Box_R bot` (a proper strengthening of Arai 1990), or is
  uniform full `D3` arithmetically incompatible with `¬D2 + ¬Box_R bot`, isolating the exact
  derivability content separating `D3^hom` from full `D3` for a Rosser box.
- **[Superseded (Pass 131)]** _(was [New (Pass 130)])_ **Prufer ranks, graded-Rosser obligations, the ZFC-only honesty
  threshold, and bimodal `R+4` completeness.** (i) Discharge Constr-130c obligations o1
  (`D1^¬D2` uniform across graded layers) and o2 (the `ConLat`-image tower is honestly
  `(Z, x a_k)`, a witness-counting lemma), and pin the exact Prufer ranks `kappa_q` of
  `Tor(hatZ_N/Z)` -- is `kappa_q = 1` for every `q notin Supp_inf` (rank-one Prufer, per the
  `Z_2/Z` and primorial evidence), or can depth-varying overhead inflate `kappa_q` to the
  continuum? (ii) Pin the exact cardinal-characteristic threshold of `(forall n)h_n` between
  `2^aleph0 >= aleph_2` and the Bannister-Bergfalk-Moore-Todorcevic descriptive / `A_kappa`
  bound, and decide whether the `h_1 ^ ¬h_2` depth split (Thm 129b) survives in the ZFC-only
  (no large cardinal) models. (iii) Prove bimodal completeness `PL(Box_R^A) = R + 4` in the
  `(Box, Box_{-<})` language with `Box_{-<}` a `GL`-modality (canonical
  neighborhood-`x`-Kripke bimodel; verify the Guaspari-Solovay/Kurahashi Rosser logic `R` is
  exactly the `-<`-fragment), and settle whether full `D3` (not merely `D3^hom`) can be added
  without collapsing `¬D2`.
- **[Open, carried from Pass 117]** **`R_{2k}` general fixed-point-freeness.**
  Residue (i) of the Pass-117 problem, untouched by Pass 118: prove every
  `boxt`-`2k`-cycle plateau `R_{2k}` with `boxt[F]=F` (front-internal) is
  `boxt_hat`-fixed-point-free in its MacNeille completion (verified `k=1` and the
  split `1+1`).  Note Pass 118 shows this is specifically about `boxt[F]=F`, not
  about even orbit length per se.
- **[Closed by Pass 57]** _(was [New (Pass 56)])_ Two residues of Pass 56. (i) **Carrier-free cancellativity lemma:**
  upgrade Thm 56a.2 from "the *natural additive* extension of $\otimes$ fails to residuate"
  to "**no** complete residuated tensor with unit $e=a^\ast$ exists on $\overline{L}^{(m)}$."
  Conjectured form: in a complete residuated lattice whose unit $e$ is the non-attained
  supremum of a strictly ascending cancellative chain $\{a_n\}$ immediately below a
  join-irreducible cover $c\succ e$, the residual $c\backslash e$ is non-principal — hence
  a unit may be a sup-of-chain only if no join-irreducible covers it, a structural
  incompatibility between the "Rosser (non-integral, sup-of-chain) unit" and a residuated
  completion. (ii) **Torsor-level identification:** promote the Thm-56b iso
  $\operatorname{coker}\delta\cong\widehat{\mathbb Z}_m/\mathbb Z$ to an isomorphism of
  **Rosser unit-torsors** (Guaspari–Solovay witness-comparison choices $\to$ Čech
  $1$-cochains), so "phantom" and "Rosser torsor" are one $\varprojlim^1$ *as torsors*, not
  merely as abelian groups — closing the last cochain-level gap of the $L_{(-)}$ functor.
- **[Superseded by the Pass-54 split above]** Two proof obligations from Thm 53a/53b. (i) **Realize the
  $2$-adic phantom inside an honest residuated lattice:** construct a complete
  residuated lattice (or residuated $\mathbb Z$-graded APS) whose failed-cover
  incidence module IS $(\mathbb Z,\times2)$ — the tensor unit acting on the cover
  fiber by doubling — so $b_{\mathrm{phantom}}=\widehat{\mathbb Z}_2/\mathbb Z$
  is the derived limit of a genuine $\boxtimes$, not of an abstract sheaf; decide
  whether the prime $2$ is forced or whether $(\mathbb Z,\times m)$ phantoms
  $=\widehat{\mathbb Z}_m/\mathbb Z$ realize for all $m\ge2$, and what $m$-adic
  arithmetic the refutability orbit must carry. (ii) **Promote Thm 53b to a full
  equivalence and identify the Rosser torsor:** prove $L_{(-)}|_{\mathbf{GL}}$ is
  full onto $\mathbf{resAPS}_{\mathrm{int}}$, and identify the Rosser
  unit-torsor with $H^1(\mathbf{Deriv}\setminus\mathbf{GL};\mathrm{Aut}(\text{unit}))$,
  tying Rosser non-canonicity to the same $\varprojlim^1/H^1$ obstruction theory
  that governs the phantom — are "phantom" and "Rosser torsor" two instances of one
  derived-functor obstruction on $\mathbf{resAPS}$?
- **[Partially resolved (Pass 53)]** _(was [New (Pass 52)]; items (ii) and (iii) RESOLVED by Pass 53, item (i) carried forward)_ Three follow-ups. (i) **Signed-orbit refinement of $\Phi$.**
  Refine $\Phi=\sum_{d\ge1}s(d)N_d$ from a chain count to a *$\tau$-orbit* count:
  express $\Phi$ via the generating function $\sum_d N_d t^d$ of invariant chains
  evaluated at the $4$th roots of unity, and characterize which $f$-vectors
  $(N_d)$ are realizable by an order-reversing involution (a "flipped
  Dehn–Sommerville" constraint). (ii) **Integral $\varprojlim^1$ nonvanishing**
  (carried from Pass-51 (ii)): realize a non-Mittag-Leffler $\mathbb Z$-tower
  $\mathbb Z\xleftarrow{\times2}\mathbb Z\xleftarrow{\times2}\cdots$ inside the
  lattice's incidence module so $b_{\mathrm{phantom}}=\dim_{\mathbb F_p}
  (\varprojlim^1\otimes\mathbb F_p)$ genuinely (Prüfer $\mathbb Z[1/2]/\mathbb Z$).
  (iii) **Löb/Rosser functoriality** (carried from Pass-51 (iii)): build $L_{(-)}$
  from derivability packages to residuated APS; integral-unit subcategory $=$ image
  of the Löb (GL) packages, Rosser packages in the non-integral complement.
- **[Superseded (Pass 52)]** _(original Pass-51 statement; follow-up (i) resolved
  by Pass 52, (ii)/(iii) carried into the [New (Pass 52)] block above.)_ Three
  follow-ups. (i) **The flipped invariant $\Phi(\tau)$.**
  Since $e=|F^{\tau}|$ is deflationary, the homological content is
  $\Phi(\tau)=1-|F^{\tau}|$; characterize $\Phi$ intrinsically (signed count of
  flipped $\tau$-orbits), find the posets maximizing $|\Phi|$ (the cube gives
  $\Phi=1$; is large-negative $\Phi$ achievable?), and tie $\Phi$ to the reduced
  Smith/Lefschetz data of $|\Delta(F)|^{\tau}$. (ii) **Integral $\varprojlim^1$
  nonvanishing.** Discharge Thm 51b(a): realize a non-Mittag-Leffler $\mathbb
  Z$-tower (e.g. $\mathbb Z\xleftarrow{\times2}\mathbb Z\xleftarrow{\times2}\cdots$)
  inside the lattice's incidence module so that $b_{\mathrm{phantom}}=\dim_{\mathbb
  F_p}(\varprojlim^1\otimes\mathbb F_p)$ genuinely. (iii) **Functoriality of the
  Löb/Rosser dictionary.** Discharge Thm 51c: build $L_{(-)}$ from derivability
  packages $\{D1,D2,D3,\Sigma_1\text{-comp.},\text{Rosser witness-comparison}\}$ to
  residuated APS and prove the integral-unit subcategory is exactly the image of the
  Löb (GL) packages.
- **[Superseded (Pass 51)]** _(original Pass-50 statement; resolved by the three
  [Resolved (Pass 51)] entries above — kept for provenance.)_ Three follow-ups.
  (i) **Completeness of $e(F^{\tau})$.**
  Is $e=0$ with $F^{\tau}\ne\varnothing$ possible for some antitone $\boxtimes$?
  Conjecture: no — self-dual fixed sets of comparable-2-cycle intervals are
  contractible-or-empty, so $e$ is a *complete* bracket invariant there; prove,
  or build a pathological $\boxtimes$ whose $F^{\tau}$ is an order-complex circle.
  (ii) **Phantom Betti number as genuine cohomology.** Promote $b_{\mathrm{phantom}}$
  from a count to $\dim H^1$ of an explicit cochain complex on the lattice whose
  $1$-cocycles are failed join-covers, making Constr 50b a theorem about
  $H^1(P_r)=\mathbb F^r$ rather than an enumeration; relate to derived functors of
  the discontinuous $\boxtimes$. (iii) **Arithmetic lift of the non-integral unit.**
  Realize the slogan "non-integral unit $=$ algebraic shadow of Rosser-evades-Löb":
  build the arithmetic APS of the Rosser predicate $\Box_R$ (Guaspari–Solovay 1979;
  Kurahashi 2021) and show its residuated realization forces unit $\ne\top$ exactly
  when $\rho\leftrightarrow\neg\Box_R\rho$ fails Löb, against the de Jongh–Sambin
  Löb-attachment of the standard $\Box$ (Pass 43).
- **[Superseded (Pass 50)]** _(original Pass-49 statement; resolved by the three
  [Resolved (Pass 50)] entries above — kept for provenance.)_ Three follow-ups.
  (i) **Equivariant-Euler refinement of
  Thm 49a.** $\chi(|\Delta(F)|^{\tau})=1$ does not distinguish a fixed vertex from
  an edge-barycenter; find the Bredon / equivariant-Euler invariant (a
  *vertex-counting* Smith inequality on $\dim_{\mathbb F_2}H_\ast(|\Delta(F)|^{\tau})$)
