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
- **[New (Pass 65)]** **Scheme-site Verdier lift and dualizing normalization.** Prove or refute the
  scheme-level equation $\mathbb D(\epsilon_S)=-\epsilon_S^\vee$ for finite $S$ and then
  $S=\mathbb P$. Required subquestions: (a) identify the correct duality
  (Verdier/Pontryagin/Matlis/$R\mathrm{Hom}_{\mathbb Z}$) for the pro-object $\mathcal V$; (b)
  compute the duals of $\mathbb Z_p/\mathbb Z$, $\prod_p(\mathbb Z_p/\mathbb Z)$, and
  $\widehat{\mathbb Z}_S/\mathbb Z$ without losing product/direct-sum information; (c) decide
  whether the integral sign in the finite model survives the scheme-site convention or is absorbed
  by an orientation choice.
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
