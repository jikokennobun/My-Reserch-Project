# Research Questions

## Active

- **(Drive supplement 2026-06-11: A3-stability under cut closure and completion)**
  The new Drive additions `cut_elimination_g2_preaps.pdf` and
  `residuated_completion_goi_notes.pdf` sharpen the same obstruction from two
  sides: preAPS cut closure tends to break A3, while completion/quantale/GoI
  constructions can preserve rich residual structure without yielding genuine
  $\boxtimes$-fixed points. Open:
  (i) classify exactly when reflexive-transitive cut closure of a preAPS still
  satisfies A3;
  (ii) compare that criterion with MacNeille/canonical/quantale completion and
  determine which completions preserve or reflect A3/A4;
  (iii) decide whether the surviving condition is best formulated as
  contraction, interpolation, or a fibered Beck-Chevalley/exactness law.

- **(Pass 69 retarget: arithmetic lift of consistency tower and CutA3)**
  Pass 69 added the APS-level tower $C_0=T$, $C_{n+1}=\boxtimes C_n$, with
  $\mathrm{Con}^{\mathrm{orb}}_n$, $\mathrm{G2}_n$, $\mathrm{FG2}_n$, finite
  `flat-orbit(N)`, and `CutA3`.  Machine checks separate cycle APS models
  $C_m$ (flat, fixed-point-free, nFG2-false) from detached Rosser period
  preAPS models $R_{2k}$ (primitive fixed point, A1/A2/A4, but A3 failure at
  $p$).  Open: identify the arithmetic counterpart of `CutA3`; locate
  $\mathrm{Con}^{\mathrm{orb}}_n$ in $ConLat_T$; and decide whether residuation,
  integrality, and contraction force a detached Rosser fixed point back into
  the consistency orbit.

- **(Pass 71 retarget: exact category for pro-restricted $\epsilon_{\mathbb P}$)**
  Pass 71 formulated the all-prime signed law as a pro-restricted finite-shadow
  theorem: $\epsilon_{\mathbb P}$ is the compatible family
  $\{\epsilon_S\}_{S\subset\mathbb P,\ |S|<\infty}$ together with the derived
  pro-cokernel $\widehat{\mathbb Z}/\mathbb Z$, and
  $D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$ means
  that every finite-prime/conductor shadow sends $d_S$ to $-d_S^T$ compatibly
  with restrictions.  Open: construct the ambient exact category in which this
  is a genuine duality theorem.  Candidate targets are LCA sheaves over finite
  adeles, condensed/solid abelian groups, or a hybrid exact category combining
  restricted products with derived pro-Ab quotients; the proof must preserve
  product support and not replace it by finite-support direct sums.

- **(Drive supplement 2026-06-10: domain/stable APS models and the A3 bottleneck)**
  The new Drive PDF `domain_stable_ams_aps_raps_models.pdf` sharpens the
  analytic/domain-theoretic line in a negative direction. Scott-frame,
  event-structure, coherence, and many residuated semantic models give large
  complete APS/RAPS families, but nontrivial instances typically satisfy
  `\neg G2`, `\neg FG2`, and have no nontrivial $\boxtimes$-fixed point. The
  semantic bottleneck is A3 rather than mere existence of residuals or
  continuity. Open:
  (i) characterize Scott-continuous maps $f$ for which
  $\Box_f(U)=f^{-1}(U)$ and $\boxtimes(U)=U^\ast$ satisfy A3/A4;
  (ii) find a genuinely domain-theoretic or stable-semantic model with a
  nontrivial $\boxtimes$-fixed point;
  (iii) classify which completions create only semantic fixed points and which
  reflect back to definable APS elements.

- **(Pass 63 retarget — the Zariski $j_!$-cosheaf, the unabridged $d_2$, and arithmetic $\succ$ cardinal)**
  Pass 63 discharged the Pass-62 triad. **Thm 63a:** on the connected Zariski generic-point
  subspace $X=\{\eta\}\cup\{(p):p\in S\}$ the cover $\{U_p=\{\eta,(p)\}\}$ has full-simplex nerve,
  so the constant sheaf $\underline{\mathbb Z}$ is a sheaf with $\check H^{\ge1}=0$ (the discrete
  horizontal defect $\mathbb Z^{s-1}$ **vanishes**), and the Rosser relations relocate to
  $H^1(X,j_!\underline{\mathbb Z})=\mathbb Z^{s-1}\ne0$ (extension by zero from the open generic
  point). Since $j_!$ is the compact-support/cosheaf functor, **"Rosser $=$ cosheaf" finally holds
  as Rosser $=H^1$ of $j_!$**, Löb $=$ stalkwise sheaf $L(S)$ (the naive cover-cosheafification
  still $=L$). **Thm 63b:** unabridging each $\mathbb Z_p$ into its $\mathbb Z/p^n$-tower opens
  $E_2^{2,0}=\mathbb Z^{s-1}$ and realizes the hidden Pass-62 extension as a genuine
  $d_2:L(S)\to\mathbb Z^{s-1}$ (common-integer-lift obstruction); $\epsilon_S=\partial$ and the
  $d_2$ are one datum in two resolutions. **Thm 63c:** $\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=0$ gives
  an infinite-order ghost line $\delta(\mathbb Z)\subset\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb Z)$
  (lacunary witness $\sum p^{k!}$); $\epsilon_S\ne0$ for $s\ge2$, with target rank $s-1$ **cardinal**
  but the class **arithmetic** (the $\mathbb Z_p/\mathbb Z$ are pairwise non-isomorphic, uniquely
  omitting the $p$-Prüfer). Now open: (i) the **six-functor/recollement** packaging — is the total
  phantom $H^1(\mathrm{Spec}\,\mathbb Z,\,j_!\mathcal V)$ for the dilation local system $\mathcal V$
  (Löb $=i^*$, Rosser $=j_!$, recollement $(j_!,j^*,j_*)\dashv(i^*,i_*,i^!)$)? (ii) a **prime-spectrum
  motive** — $\epsilon_S$ as a functor on $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$ valued in
  $\mathrm{Ext}^1$-lines; (iii) [carried] the exact $\aleph_1$-threshold of Thm 61c.

- **(Pass 61 retarget — the phantom is NOT a sheaf; Rosser $=$ obstruction to descent)**
  Pass 61 tested the Pass-60 slogan literally and **corrected** it. **Thm 61a:** resolving
  $P(S)=(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ via $0\to\underline{\mathbb Z}\to\mathcal F
  \to P\to0$ ($\mathcal F=\prod_p\mathbb Z_p$ flasque sheaf), $P$ **fails descent**
  (comparison onto with kernel $\mathbb Z^{|S|-1}$) and its **sheafification is the
  stalkwise sheaf** $L(S)=\prod_p(\mathbb Z_p/\mathbb Z)$, not the Rosser torsor.
  **Thm 61b:** the Rosser torsor $=P(S)$ is the **failure of descent** $\ker(P\to L)$ —
  horizontal $\mathbb Z^{|S|-1}=\check H^1(\underline{\mathbb Z})$ (prime cover) $\oplus$
  vertical $\varprojlim^1=\widehat{\mathbb Z}_p/\mathbb Z$ (dilation tower) per stalk; the
  slogan holds only dualized (**Löb $=$ sheaf, Rosser $=$ cosheaf**). **Thm 61c:**
  $\mathfrak b=\aleph_1\Rightarrow\varprojlim^1\ne0$, $\mathrm{MA}_{\aleph_1}\Rightarrow0$;
  threshold bracketed, not a single named characteristic; $\aleph_2$-cofinal $\Rightarrow$
  higher-$\varprojlim^s$ spectrum, not a $0/\aleph_1/2^{\aleph_0}$ trichotomy. Now open:
  (i) the **Löb–Rosser bicomplex** $\check H^p_{\mathrm{prime}}(\varprojlim^q_{\mathrm{dilation}})
  \Rightarrow H^{p+q}$ and its $E_2$ page — is there a $d_2$ linking a horizontal integer
  relation to a vertical $2$-adic ghost (a mixed Löb–Rosser class)? (ii) the explicit
  **cosheafification** of $P$ reconstituting $\widehat{\mathbb Z}_m/\mathbb Z$ as global
  cosections; (iii) the exact $\aleph_1$-threshold between $\mathfrak b=\aleph_1$ and
  $\mathrm{MA}_{\aleph_1}$ (Suslin-tree / $\mathrm{add}(\mathcal M)$?).

- **(Pass 60 retarget — $\Theta$ is natural; the phantom is a sheaf on $\mathrm{Spec}$)**
  Pass 60 **closed the last functorial gap** of $L_{(-)}$ (Pass-58 residue (ii)) and the
  Pass-59 set-theoretic frontier. **Thm 60a (carrier criterion):** a residuated
  cover-filtration map $C_m\to C_{m'}$ exists $\iff\mathbb Z[1/m]\subseteq\mathbb Z[1/m']
  \iff\mathrm{rad}(m)\mid\mathrm{rad}(m')$ — the rad-grading is *forced by the carrier*,
  and $\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ is the squarefree divisibility lattice
  $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$. **Thm 60b:** $\Theta:\mathrm{Ros}_{(-)}
  \Rightarrow\varprojlim^1(-)$ is a natural iso; rad-divisibility is the *sole* obstruction
  (where an arrow exists the Čech square commutes by snake-lemma naturality; off it the
  hom-set is empty). $\Theta$ identifies the phantom presheaf $S\mapsto(\prod_{p\in S}
  \mathbb Z_p)/\mathbb Z$ with the Rosser-torsor presheaf on $\mathrm{Spec}$. **Cor 60c:**
  $6,10$ rad-incomparable — no arrow, only the common lower bound $C_2$ (shared $2$-adic
  ghost). **Thm 60d:** Gray's dichotomy is strictly $\omega$-cofinal; at $\omega_1$ the
  cover-fiber system is the Mardešić–Prasolov system, $\varprojlim^1\ne0$ under CH /
  $=0$ under PFA — the $\aleph_1$-phantom is **independent of ZFC**. Now open:
  (i) **Sheaf descent:** does the phantom presheaf satisfy descent (sheaf for the
  inclusion topology, join $C_{\mathrm{lcm}}$ = glueing, meet $C_{\gcd}$ = restriction),
  and is the Rosser-torsor presheaf its sheafification — so Löb/Rosser becomes the
  cohomology of one sheaf on the prime spectrum?
  (ii) **Exact cardinal threshold:** is the $\aleph_1$-phantom controlled by $\mathfrak b$,
  by a Suslin tree, or by $\mathrm{MA}_{\aleph_1}$ specifically, and does an
  $\aleph_2$-cofinal cover give a genuine three-valued phantom spectrum
  ($0/\aleph_1/2^{\aleph_0}$) or collapse to a dichotomy?

- **(Pass 59 retarget — no partial phantom; the trichotomy is sharp)** Pass 59
  **resolved** Pass-58 residue (i), the intermediate / non-idempotent absorbing cover.
  The mixed regime EXISTS (the two-parameter family $W_{d,\delta}$: 28 machine-checked
  complete commutative residuated lattices with finite absorption depth
  $d=\inf\{n:a_n\otimes c=c\}$ and idempotence defect $c\otimes c=\top\ne c$ when
  $\delta=1$), but it is **phantom-flat**. **Thm 59a:** finite $d\Rightarrow$ eventually-
  constant fiber tower $\Rightarrow$ Mittag–Leffler $\Rightarrow\varprojlim^1=0$ genuinely;
  a $\varprojlim^1$ class is a tail/pro-invariant so "finitely supported phantom" is
  contentless, and the idempotence defect is $\varprojlim^1$-invisible (compact cover,
  not the non-compact cover where the phantom pins). **Cor 59b:** by **Gray's dichotomy**
  ($\varprojlim^1$ of a countable tower is $0$ or $2^{\aleph_0}$) the trichotomy is *not*
  a spectrum boundary — $(d,\iota)$ are phantom-flat moduli, the phantom jumping
  $0\to2^{\aleph_0}$ only at the non-residuated wall $d=\infty$. **Prop 59c:**
  depth $=$ nFG2 index $=$ ML $=$ phantom-free. Now open:
  (i) **The last functorial gap (Pass-58 (ii), carried):** characterize residuated
  $\mathbf{Deriv}$-morphisms and prove radical divisibility is the *sole* obstruction to
  naturality of $\Theta:\mathrm{Ros}_{(-)}\Rightarrow\varprojlim^1(-)$, closing $L_{(-)}$.
  (ii) **Set-theoretic frontier (new):** Gray's dichotomy is about *countable* towers;
  replace the front $\{a_n\}_{n<\omega}$ by an uncountable ($\mathrm{cf}=\omega_1$,
  Suslin-type) ascending chain — can a genuinely $\aleph_1$-sized "intermediate phantom"
  be engineered, and is its existence independent of ZFC?

- **(Pass 58 retarget — the absorbing edge and the Phantom trichotomy)** Pass 58
  **resolved** Pass-57 residue (i) by *refutation*: Lemma 57a's cancellativity is
  essential. The **absorbing Rosser cap** $W=(a_0=\bot<a_1<\cdots<e<c<\top)$,
  $e=\bigvee a_n$, unit $e$, tensor ($\bot$ absorbing; $\min$ below $e$; $\max$ once a
  large operand $\ge c$ appears) is a complete commutative residuated lattice with a
  completely join-irreducible cover $c\succ e$ and cofinal absorption $a_n\otimes c=c$
  ($n\ge1$) — so $\bigvee_n(a_n\otimes c)=c$ holds with every summand $=c$, no
  contradiction (Thm 58a). Cost (Thm 58b): fiber $c\backslash e=\bot$ principal, image
  tower constant/ML, $\varprojlim^1=0$ — the **Phantom trichotomy** over $\{$residuation,
  join-irreducible cover, phantom$\}$: MacNeille (cover, phantom), ideal/quantale
  (residual), absorbing cap $W$ (residual, cover) — any two, never all three. Residue
  (ii) partially closed: $\Theta$ natural on $\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$
  iff $\mathrm{rad}(m)\mid\mathrm{rad}(m')$ (Prop 58c). Now open:
  (i) **Non-idempotent absorbing cover / the trichotomy spectrum:** does a residuated
  cover with $a_n\otimes c=c$ cofinally but $c\otimes c=\top\ne c$ exist, and is its
  phantom $0$ or only finitely supported (a "partial phantom")? Index a *spectrum* by
  absorption depth $\inf\{n:a_n\otimes c=c\}$ vs idempotence defect $c\otimes c\ominus c$.
  (ii) **Rad-obstruction completeness:** is radical divisibility the *sole* obstruction
  to naturality of $\Theta$? Characterize residuated $\mathbf{Deriv}$-morphisms and close
  the $L_{(-)}$ programme's last functorial gap.

- **(Pass 56 retarget — the cancellativity lemma and the Rosser torsor)** Pass 56
  **resolved** both Pass-55 residues with a **residuation/Rosser dichotomy**: the
  completed arena $\overline{L}^{(m)}$ is a complete frame (residuated under $\wedge$ with
  *integral* unit $\top$, Löb), but the **dilation monoid** $+$ (Rosser unit $a^\ast$) has
  no residual — its fiber $c\backslash a^\ast=\{a_n\}_n$ is **non-principal** (sup $a^\ast$
  not attained), so the completion is only a preAPS (Thm 56a); finite truncations
  residuate under both tensors ("finitely residuated, limanly preAPS"). The dilation
  cover's Čech complex is the two-term $\delta=\mathrm{id}-m\cdot\mathrm{sh}$ on
  $\prod_n\mathbb Z$, $H^0=\varprojlim=0$, $H^1=\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb
  Z$ (Thm 56b). Now open:
  (i) **Carrier-free cancellativity lemma:** upgrade Thm 56a.2 from "the *natural additive*
  extension fails" to "**no** residuated tensor with unit $e=a^\ast$ exists" — conjecture:
  a unit that is the non-attained sup of a strictly ascending cancellative chain, sitting
  immediately below a join-irreducible cover, *cannot* be the unit of a residuated
  completion (the cover's residual is non-principal).
  (ii) **Torsor-level identification:** promote $\operatorname{coker}\delta\cong
  \widehat{\mathbb Z}_m/\mathbb Z$ to an iso of **Rosser unit-torsors** (Guaspari–Solovay
  witness-comparison $\to$ Čech $1$-cochains), so "phantom" and "Rosser torsor" are one
  $\varprojlim^1$ *as torsors* — the last cochain-level gap of the $L_{(-)}$ functor.

- **(Pass 55 retarget — RESOLVED by Pass 56 — residuation survival of the solenoid $+$
  explicit Čech complex)** Pass 55 **resolved** the Pass-54 [New] obligation. Carrier correction:
  the honest object is the directed colimit $C_m=\mathbb Z[1/m]^-$ (the *inverse* limit
  is trivial), MacNeille-completed — literally the classical $m$-adic solenoid. **Constr
  55a** lifts Construction 49b with $m$-adic rung dilation (cover fiber $m$), and **Thm
  55b** realizes $\widehat{\mathbb Z}_m/\mathbb Z$ as the derived limit of $\boxtimes_m$
  *itself* (join-continuity failing at the lone cover $a^\ast$). **Thm 55c:** ML $\iff$
  orbit stabilizes $\iff$ all-level nFG2 $\iff$ $\varprojlim^1=0$, all failing for
  $m\ge2$ ($\neg$FG2, perpetual orbit) yet holding at every finite truncation (phantom
  is **liman**); G2 vacuous, solenoid in $G2\wedge\neg$FG2. **Thm 55d:** finitely Löb,
  limanly Rosser — the unit is integral at each finite floor but a $\widehat{\mathbb
  Z}_m/\mathbb Z$-torsor in the limit, fusing Pass-54 obligations (1) and (2) into one
  $\varprojlim^1$-statement. Now open:
  (i) **Residuation survival:** is $\overline{L}^{(m)}$ (MacNeille completion $+$
  Construction-49b doubled cover) a complete **residuated** lattice, or only a preAPS
  (does the doubled cover $a^\ast\prec\{c,b^\ast\}$ kill the residual, echoing the
  $M_n$, $n\ge3$, non-principal fiber)? Compute the unit; confirm non-integral (Rosser).
  (ii) **Explicit Čech complex** of the dilation cover so Thm-55d's $H^1=\varprojlim^1$
  is a computation, closing Pass-54 obligation (2) at the cochain level.

- **(Pass 54 retarget — explicit $\boxtimes$ on the dilation solenoid / fuse
  phantom $+$ Rosser torsor)** Pass 54 **resolved** Pass-53 obligation (1) and
  **partially resolved** (2). **(A) Constr 54a / Thm 54b (honest $m$-adic phantom):**
  the negative cone $\mathbb Z^-$ ($x\otimes y=x+y$, $x\backslash y=\min(0,y-x)$,
  $e=0=\top$) with the dilation $d_m(x)=mx$ — an injective non-surjective residuated
  endomorphism (image $m\mathbb Z^-$, cover-fiber $m$) — realizes the coefficient
  tower $(\mathbb Z,\times m)$ honestly; $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb
  Z$. **Radical-invariant** ($\widehat{\mathbb Z}_m=\prod_{p\mid m}\mathbb Z_p$
  depends only on $\mathrm{rad}(m)$): $\times2\sim\times4\sim\times8$ (non-isomorphic
  towers, one phantom $\widehat{\mathbb Z}_2/\mathbb Z$), $\times6\sim\times12=
  (\mathbb Z_2\times\mathbb Z_3)/\mathbb Z$; prime $2$ not forced, $m=1$ the boundary
  (Cor 54c). **(B)** Rosser torsor advanced to $H^1(\mathbf{Deriv}\setminus
  \mathbf{GL};\mathrm{Aut\,unit})=\varprojlim^1$ of the choice tower, fullness of
  $L_{(-)}|_{\mathbf{GL}}$ sketched. Now open:
  (i) **Write the antitone $\boxtimes$ on $\overline{L_\infty^{(m)}}$ explicitly** so
  the phantom is *its* $\varprojlim^1$ (Construction-49b single-cover collapse lifted
  through $\varprojlim$, join-continuity failing at the one solenoidal limit cover
  $a^\ast=\bigvee a_n$ with failure module $(\mathbb Z,\times m)$).
  (ii) **nFG2/G2-compatibility of the solenoid $\boxtimes$:** does the $\times m$
  self-cover force a perpetual non-stabilizing orbit, or admit index-$2$
  stabilization (Thm 41a)?
  (iii) **Integrality of a solenoid tensor unit** — Löb-attached or Rosser? — fusing
  Pass-54 obligations (1) and (2) into one $\varprojlim^1$-on-$\mathbf{resAPS}$
  statement (Pass-51c dichotomy).

- **(Pass 53 retarget — realize the $2$-adic phantom / full Löb-Rosser
  equivalence)** Pass 53 **resolved** the two carried Pass-51/52 residues.
  **(A) Thm 53a (integral phantom):** $b_{\mathrm{phantom}}=r$ is a field-
  coefficient shadow (finite-dim'l towers are Mittag-Leffler); the genuine
  integral obstruction is $\varprojlim^1(\mathbb Z,\times2)=\widehat{\mathbb
  Z}_2/\mathbb Z$ (uncountable), via the SES $0\to(\mathbb Z,\times2)\to
  (\mathbb Z,\mathrm{id})\to(\mathbb Z/2^n)\to0$; invisible to every field and
  finite probe. **(B) Thm 53b (Löb/Rosser functor):** $L_{(-)}:\mathbf{Deriv}\to
  \mathbf{resAPS}$ is canonical on $\mathbf{GL}$ with $e=\top\iff$ Löb and
  essential image $\mathbf{resAPS}_{\mathrm{int}}$; Rosser packages form a
  non-canonical unit-torsor in the complement. Now open:
  (i) **Realize $(\mathbb Z,\times2)$ as the failed-cover incidence module of an
  honest complete residuated lattice** (tensor unit doubling the cover fiber) so
  $b_{\mathrm{phantom}}=\widehat{\mathbb Z}_2/\mathbb Z$ is the derived limit of
  a genuine $\boxtimes$; decide whether $m$-adic phantoms $\widehat{\mathbb
  Z}_m/\mathbb Z$ realize for all $m\ge2$ and what $m$-adic arithmetic the
  refutability orbit must carry.
  (ii) **Promote Thm 53b to a full equivalence** $L_{(-)}|_{\mathbf{GL}}\simeq
  \mathbf{resAPS}_{\mathrm{int}}$ and identify the Rosser unit-torsor with
  $H^1(\mathbf{Deriv}\setminus\mathbf{GL};\mathrm{Aut}(\text{unit}))$, unifying
  "phantom" and "Rosser torsor" as one derived-functor ($\varprojlim^1/H^1$)
  obstruction on $\mathbf{resAPS}$.
  (iii) **(carried from Pass-52 (i))** Signed-orbit refinement of $\Phi$: express
  $\Phi=\sum_d s(d)N_d$ via the generating function $\sum_d N_d t^d$ at $4$th
  roots of unity and characterize the realizable invariant-chain $f$-vectors
  (a "flipped Dehn–Sommerville" constraint).

- **(Pass 52 retarget — signed-orbit $\Phi$ / integral $\varprojlim^1$ / Löb-Rosser
  functoriality)** Pass 52 **resolved** Pass-51 follow-up (i): the flipped
  invariant. (A) **Thm 52a**: $\Phi(\tau)=\sum_{d\ge1}s(d)N_d=1-|F^\tau|$, signed
  count of $\tau$-invariant $d$-chains with period-4 sign $s(d)=+\,+\,-\,-$. (B)
  **Thm 52b**: $\sup\Phi=+1$ (fixed-point-free; cube/$C_4$), $\inf\Phi=-\infty$
  (fixed-antichain fan $F_m$, $\Phi=1-m$). (C) **Thm 52c**:
  $\Phi=\chi(|\Delta(F)|^\tau)-\chi(\Delta(F^\tau))$, the geometric-minus-
  combinatorial fixed-point Euler gap. Now open:
  (i) **Signed-orbit refinement of $\Phi$** — refine the chain count to a
  $\tau$-orbit count via $\sum_d N_d t^d$ at $4$th roots of unity; which $f$-vectors
  $(N_d)$ are realizable by an order-reversing involution (flipped
  Dehn–Sommerville)?
  (ii) **Integral $\varprojlim^1$ nonvanishing** (carried) — realize a
  non-Mittag-Leffler $\mathbb Z$-tower $\mathbb Z\xleftarrow{\times2}\mathbb Z
  \leftarrow\cdots$ in the incidence module so $b_{\mathrm{phantom}}=\dim_{\mathbb
  F_p}(\varprojlim^1\otimes\mathbb F_p)$ genuinely (Prüfer $\mathbb Z[1/2]/\mathbb
  Z$).
  (iii) **Löb/Rosser functoriality** (carried) — build $L_{(-)}$ from derivability
  packages to residuated APS; integral-unit subcategory $=$ image of Löb (GL)
  packages, Rosser in the non-integral complement.

- **(Pass 51 retarget — flipped invariant $\Phi(\tau)$ / integral $\varprojlim^1$
  / Löb-Rosser functoriality)** Pass 51 **resolved** all three Pass-50 follow-ups.
  (A) **Thm 51a**: $\mathrm{Fix}(\boxtimes)$ is an antichain (Lemma 51a), so
  $e(F^\tau)=|F^\tau|$ identically — $e$ is a complete but *deflationary* bracket
  invariant; the order-complex-circle pathology is unrealizable. (B) **Thm 51b**:
  $b_{\mathrm{phantom}}(P_r)=\dim H^1(\mathrm{Ob}^\bullet(P_r))=r$, the phantom
  being $\varprojlim^1$ of the image tower (additive over arms). (C) **Thm 51c**:
  integral unit $\iff$ Löb-attached, non-integral unit $\iff$ Rosser-evades-Löb.
  Now open:
  (i) **The flipped invariant $\Phi(\tau)=1-|F^\tau|$** — the real homological
  content after the $e$-deflation. Characterize $\Phi$ as a signed count of flipped
  $\tau$-orbits; which $F$ maximize $|\Phi|$ (cube $\Rightarrow\Phi=1$; large
  negative $\Phi$?); tie $\Phi$ to the reduced Smith/Lefschetz data of
  $|\Delta(F)|^\tau$.
  (ii) **Integral $\varprojlim^1$ nonvanishing.** Realize a non-Mittag-Leffler
  $\mathbb Z$-tower ($\mathbb Z\xleftarrow{\times2}\mathbb Z\leftarrow\cdots$) inside
  the lattice's incidence module so $b_{\mathrm{phantom}}=\dim_{\mathbb F_p}
  (\varprojlim^1\otimes\mathbb F_p)$ genuinely (field-coefficient $\varprojlim^1$ of
  finite-dim'l towers vanishes).
  (iii) **Functoriality of the Löb/Rosser dictionary.** Build $L_{(-)}$ from
  derivability packages to residuated APS; prove the integral-unit subcategory is
  exactly the image of the Löb (GL) packages, Rosser packages landing in the
  non-integral complement.

- **(Pass 50 retarget — completeness of $e(F^\tau)$ / phantom cohomology /
  arithmetic Rosser lift)** Pass 50 **resolved** all three Pass-49 follow-ups.
  (A) **Thm 50a** gives the Bredon vertex-bracket identity $L(\tau)=e(F^\tau)+
  \Phi(\tau)=1$ with $e(F^\tau)=\chi(\Delta(F^\tau))$ the vertex-counting
  refinement of the blind topological $\chi(|\Delta(F)|^\tau)=1$; cube-gap $=$
  extremal $e=0,\Phi=1$. (B) **Constr 50b** gives the phantom Betti number
  $b_{\mathrm{phantom}}(P_r)=\#\text{failed covers}=r$ (phantoms add). (C)
  **Thm 50d** gives front-cardinality decoupling: $R(3)=56$, $R(4)=411$, $R(n)\ge1$
  for all $n$ via an explicit witness family, non-integral unit forced, group law
  invisible to the commutative tensor. Now open:
  (i) **Is $e(F^\tau)$ a complete bracket invariant?** Can $e=0$ co-occur with
  $F^\tau\ne\varnothing$ for some antitone $\boxtimes$ (an order-complex-circle
  self-dual set), or are comparable-2-cycle self-dual subposets always
  contractible-or-empty?
  (ii) **Phantom Betti number as genuine cohomology.** Build a cochain complex on
  the lattice whose $1$-cocycles are failed join-covers, upgrading $b_{\mathrm{
  phantom}}(P_r)=r$ to $\dim H^1(P_r)=r$ — a theorem, not an enumeration.
  (iii) **Arithmetic lift of the non-integral unit.** Realize "non-integral unit
  $=$ algebraic shadow of Rosser-evades-Löb": the Rosser predicate $\Box_R$
  (Guaspari–Solovay 1979; Kurahashi 2021) realizes an APS whose residuated form
  forces unit $\ne\top$ exactly when $\rho\leftrightarrow\neg\Box_R\rho$ fails
  Löb, against the de Jongh–Sambin Löb-attachment of the standard $\Box$ (Pass 43).

### Superseded (Pass 49 active block; resolved by Pass 50)


- **(Pass 49 retarget — equivariant-Euler refinement / multi-cover phantom /
  non-abelian orbit + arithmetic lift)** Pass 49 **resolved** all three Pass-48
  follow-ups. (a) **Exact bracketing** is now a Smith-theory criterion (Thm 49a):
  $\tau$ acts on the $\mathbb F_2$-acyclic order complex $\Delta(F)$;
  $|\Delta(F)|^\tau$ is nonempty+acyclic and $\boxtimes$ brackets iff it meets the
  $0$-skeleton (iff a $\tau$-invariant chain has odd cardinality). The cube-gap is
  the lone flipped-edge barycenter $\{\varnothing,[n]\}$ — vertex-free. (b) The
  **explicit phantom** is built (Construction 49b): a single doubled cover at
  $a^\ast=\bigvee o_n$ with $\boxtimes a^\ast=m<b^\ast$ breaks join-continuity —
  *one* failed cover suffices. (c) **Group-orbit liberation** (Thm 49d): $R_4/M_5$
  admits $411$ residuated tensors with non-integral unit $p$ and $0$ integral;
  front rigidity forbids group *tensors* not group *orbits*, the escape requiring a
  non-integral unit. Now open: (a) an **equivariant-Euler / Bredon refinement**
  whose $1$-vs-$0$ value on the $0$-skeleton detects the bracket (since
  $\chi(|\Delta(F)|^\tau)=1$ is blind to vertex-vs-edge-barycenter); (b) a
  **multi-cover phantom calibration** — is the phantom gap a "Betti number"
  counting failed covers? (c) a **non-abelian orbit + arithmetic lift** — push
  Thm 49d from $\mathbb Z/4$ to $\mathbb Z/k$ and non-abelian $G$,
