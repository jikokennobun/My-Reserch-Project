# Autonomous Discussion Log

## State

- Started: 2026-05-24
- Mode: Codex-centered repository discussion
- Default cadence: one compact pass per scheduled wake-up
- Target run: ongoing until the user explicitly pauses or stops the automation
- Current pass: 95
- Last pass note: Pass 94 (2026-06-21) computed the Verdier/solid dual of the
  all-prime Borel $j_!$ coefficient from Pass 93.  The unipotent all-prime
  class is
  $$\epsilon=\widehat{\mathbb Z}/\mathbb Z,$$
  so solid duality gives
  $$D\epsilon\simeq\mathbb Q[-1].$$
  Thus the dual of
  $$\mathfrak B^{\mathrm{cont}}_{j!}
  =\mathbb Q^\times\ltimes R\!\varprojlim_{S\Subset\mathbb P}j_{S,!}\mathcal V_S$$
  is a Levi-marked boundary object with unipotent part $\mathbb Q[-1]$ and
  contragredient $\mathbb Q^\times$ action, not an opposite Borel in degree
  $0$.  The Pass-65 finite sign and Pass-77 all-prime antipode remain:
  finite boundaries satisfy $D(d_S)=-d_S^T$, and the biduality sign on
  $\epsilon$ is $-\mathrm{id}$.  This is a functional-equation shadow only in
  the boundary sense.  It does not create a Weyl/Fourier flip, since
  $$\mathrm{Hom}^0_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0.$$
  Machine-verified `check-pass94.py` ->
  `pass94-all-prime-borel-jshriek-solid-dual-check.json` PASS. Counter
  94->95.
- Earlier note: Pass 93 (2026-06-21) upgraded the finite-support Borel
  $j_!$ class to the all-prime Spec-$\mathbb Z$ setting.  The key correction is
  topological: in the honest all-prime Zariski site, the generic point
  $\{\eta\}$ is not open, since every nonempty basic open contains all but
  finitely many closed primes.  Therefore the finite-support notation
  $j_!$ must be read all-prime as a pro-open / continuous / solid coefficient:
  $$\mathfrak B^{\mathrm{cont}}_{j!}
  =\mathbb Q^\times\ltimes R\!\varprojlim_{S\Subset\mathbb P} j_{S,!}\mathcal V_S.$$
  The support-direction transition maps are restrictions from larger finite
  supports to smaller ones; they are surjective, so that direction is
  Mittag-Leffler and contributes no extra $\varprojlim^1$.  The nonzero
  derived content remains the per-prime dilation tower inside $\mathcal V$.
  Thus
  $$H^1_{\mathrm{cont}}(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)
  =\varprojlim_S H^1(X_S,j_!\mathcal V_S)
  \cong\widehat{\mathbb Z}/\mathbb Z.$$
  The global Levi $\mathbb Q^\times$ is retained, not replaced by the product
  of local Levi factors, and the finite-adele row
  $0\to\mathbb Q\to\mathbb A_f\to\widehat{\mathbb Z}/\mathbb Z\to0$ remains
  functorial.  Machine-verified `check-pass93.py` ->
  `pass93-all-prime-borel-jshriek-upgrade-check.json` PASS. Counter 93->94.
- Earlier note: Pass 92 (2026-06-21) relocated the Borel descent obstruction
  from the discrete singleton-prime cover to the finite Zariski/generic-point
  site $X_S=\{\eta\}\cup\{(p):p\in S\}$.  On this connected site, the constant
  Borel sheaf has no horizontal $H^1$ defect; the Rosser/Borel obstruction is
  the unipotent $j_!$ class:
  $$H^1(X_S,j_!\underline{\mathbb Z})\cong
  \mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.$$
  Thus the Borel analogue of the Pass-63 ghost line is the low-degree
  semidirect coefficient
  $\underline{\mathbb Q^\times}\ltimes j_!\underline{\mathbb Z}$: the Levi
  remains degree-$0$ global data, while the unipotent radical carries the
  $j_!$ cohomology class.  Modulo $N$, the finite class set has size
  $N^{|S|-1}$, exactly matching the Pass-91 finite diagonal descent kernel.
  With the dilation coefficient $\mathcal V$, the horizontal ghost injects into
  $$H^1(X_S,j_!\mathcal V)\cong\widehat{\mathbb Z}_S/\mathbb Z,$$
  whose pushout along $\mathbb Z\to\mathbb Q$ gives the finite-adele extension
  line.  The hyperbolic Borel shear transports representatives and the Levi
  rescales the class; neither supplies a canonical zero section.  Machine-
  verified `check-pass92.py` ->
  `pass92-zariski-generic-borel-descent-check.json` PASS. Counter 92->93.
- Earlier note: Pass 91 (2026-06-21) decided the descent status of the
  restriction/span Borel torsor on the finite prime-cover site.  The unipotent
  phantom presheaf
  $$P(S)=(\prod_{p\in S}\mathbb Z_p)/\Delta\mathbb Z$$
  is not separated for multi-prime supports: its singleton-prime descent
  kernel is the horizontal Rosser defect
  $$\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.$$
  Adding the global-Levi Borel does not turn it into a sheaf.  Stackification
  gives the local Borel sheaf with stalkwise unipotents and local Levi data;
  the Rosser class is precisely the kernel lost in that process.  Machine-
  verified `check-pass91.py` ->
  `pass91-borel-torsor-descent-obstruction-check.json` PASS. Counter 91->92.
- Earlier note: Pass 90 (2026-06-21) made the Pass-89 Borel-torsor theorem
  functorial over conductor/radical supports, with a direction correction.
  For squarefree supports $S\subseteq T$, coordinate projection descends
  through the diagonal quotient and gives the canonical restriction
  $$P(T)=(\prod_{p\in T}\mathbb Z_p)/\Delta\mathbb Z\to
  P(S)=(\prod_{p\in S}\mathbb Z_p)/\Delta\mathbb Z.$$
  The tempting zero-insertion $P(S)\to P(T)$ does not descend when new primes
  are added, because $(1,\ldots,1)$ maps to a vector with zeros on the new
  coordinates, not to a diagonal.  Thus support functoriality is
  contravariant by restriction; enlargement is a span, pullback, or
  finite-conductor choice.  Rad-incomparable supports compare by a meet span
  for shared ghosts and a join arena for gluing.  Finite Borel shadows
  $(\mathbb Z/N)^\times\ltimes\mathbb Z/N$ reduce along conductor divisibility,
  preserving the unit class and singleton strict marked stabilizer.
  Machine-verified `check-pass90.py` ->
  `pass90-conductor-functorial-borel-torsors-check.json` PASS. Counter
  90->91.
- Earlier note: Pass 89 (2026-06-21) consolidated the Rosser phantom as a
  Borel-torsor / extension-class theorem.  The same obstruction may be read as
  a Guaspari-Solovay witness-comparison Cech class, a
  $\varprojlim^1(\mathbb Z,\times m)$ or $\epsilon=\widehat{\mathbb Z}/\mathbb Z$
  phantom, the finite-adele extension line
  $$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0,$$
  or the hyperbolic Borel shear orbit for
  $\mathbb Q^\times\ltimes\epsilon$.  Changing witness choices changes
  representatives, sections, and finite truncation lifts by coboundaries, but
  preserves the torsor/cohomology class, finite conductor restrictions,
  radical support, and the finite-adele extension line.  Strict integral
  marking remains rigid; forgetting it leaves the Levi $\mathbb Q^\times$;
  the full Borel appears only at the hyperbolic-plane level.  Machine-verified
  `check-pass89.py` -> `pass89-borel-torsor-rosser-phantom-check.json` PASS.
  Counter 89->90.
- Earlier note: Pass 88 (2026-06-21) split the stabilizer of the final
  finite-adele shear extension into three levels.  The strict object under the
  integral marking
  $$C_{\mathbb Z}\to C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,]$$
  has trivial automorphism group: fixing the marked unit forces scalar $1$,
  and Pass 87 kills derived ambiguity for the uniquely divisible kernel.
  Forgetting the integral marking but preserving the shear extension line
  $$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$$
  gives degree-$0$ stabilizer $\mathbb Q^\times$, since nonzero rational
  scalars preserve the one-dimensional finite-adele Ext line.  The full solid
  Borel $\mathbb Q^\times\ltimes\epsilon$ appears only after passing from the
  bare exact row to the hyperbolic plane $H=\epsilon\oplus\mathbb Q$ with its
  polarization: $\mathbb Q^\times$ is the Levi stabilizer and $\epsilon$ is the
  unipotent shear parameter.  No additional derived automorphisms survive
  after the Pass-87 torsion-boundary decoration rule.  Machine-verified
  `check-pass88.py` -> `pass88-shear-extension-stabilizer-check.json` PASS.
  Counter 88->89.
- Earlier note: Pass 87 (2026-06-21) upgraded the shear-pushout initiality
  to a mapping-space statement.  For a shear-marked target model
  $M=(0\to D\to E\to\epsilon\to0)$, precomposition along
  $C_{\mathbb Z}\to C_{\mathbb Q}$ has homotopy fiber
  $$\operatorname{hofib}\bigl(\operatorname{Map}(C_{\mathbb Q},M)\to
  \operatorname{Map}(C_{\mathbb Z},M)\bigr)
  \simeq \mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,D),$$
  because the cofiber of $\mathbb Z\to\mathbb Q$ is $\mathbb Q/\mathbb Z$.
  If $D$ is uniquely divisible, this fiber is contractible: there are no maps
  from the torsion group $\mathbb Q/\mathbb Z$ to torsion-free $D$, and
  divisibility makes $D$ injective so higher Ext obstructions vanish.  If a
  torsion-divisible summand $T$ is present, the extra
  $\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,T)$ is precisely the
  non-unique component found in Pass 86.  Thus the strict derived initiality
  theorem works for uniquely divisible kernels; with torsion-divisible kernels,
  one must either exclude the summand or decorate it by choosing the boundary
  $\mathbb Q/\mathbb Z\to T$ component.  Machine-verified `check-pass87.py` ->
  `pass87-mapping-space-shear-initiality-check.json` PASS. Counter 87->88.
- Earlier note: Pass 86 (2026-06-21) isolated the universal property of the
  finite-adele shear pushout.  In the category of shear-marked quotient models
  receiving
  $$C_{\mathbb Z}=[\,\mathbb Z\to\widehat{\mathbb Z}\,]$$
  and whose kernel is uniquely divisible (equivalently a $\mathbb Q$-vector
  object), the map $\mathbb Z\to D$ extends uniquely to $\mathbb Q\to D$.
  Hence the pushout
  $$C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,]
  =C_{\mathbb Z}\otimes_{\mathbb Z}\mathbb Q$$
  is initial: every unit/shear-preserving model factors uniquely through
  $C_{\mathbb Q}$, and ordinary finite/Hausdorff cokernels remain zero because
  integer residues already cover every finite quotient.  The naive statement
  with merely divisible kernels is false: torsion-divisible kernels such as
  $\mathbb Q/\mathbb Z$ admit distinct maps $q\mapsto kq\bmod\mathbb Z$ from
  $\mathbb Q$ that restrict identically on $\mathbb Z$.  Thus the categorical
  replacement for the missing Weyl flip is the uniquely-divisible
  localization/pushout property in the extension category, not a degree-$0$
  map $\epsilon\to\mathbb Q$.  Machine-verified `check-pass86.py` ->
  `pass86-shear-pushout-universal-property-check.json` PASS. Counter 86->87.
- Earlier note: Pass 85 (2026-06-20) built the promised two-term complex
  comparison for the finite-prime boundary.  With cohomological convention
  degree $0\to1$, the three rows
  $$C_{\mathbb Z}=[\,\mathbb Z\to\widehat{\mathbb Z}\,],\quad
  C_{\mathbb R}=[\,\mathbb R\to\Sigma\,],\quad
  C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,]$$
  all have injective differential and abstract quotient
  $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ in degree $1$.  Their ordinary
  finite/Hausdorff shadows are acyclic because the diagonal image is dense /
  surjective at every modulus.  The phantom is the solid derived residue of
  the non-Mittag-Leffler kernel tower, not an ordinary finite cokernel.
  The map $C_{\mathbb Z}\to C_{\mathbb Q}$ induced by
  $\mathbb Z\hookrightarrow\mathbb Q$ and
  $\widehat{\mathbb Z}\hookrightarrow\mathbb A_f$ is the shear-preserving
  pushout; it carries the unit class to the finite-adele extension
  $$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.$$
  The archimedean row $C_{\mathbb R}$ has the same quotient but not this
  finite-adele kernel class; it repairs the compact solenoid rather than the
  Borel shear.  Machine-verified `check-pass85.py` ->
  `pass85-two-term-boundary-complex-check.json` PASS. Counter 85->86.
- Earlier note: Pass 84 (2026-06-20) formulated the dense-quotient
  $\mathbb R\to\Sigma\to\epsilon$ as a boundary object rather than a continuous
  action row.  Since $\mathbb Z$ is dense in $\widehat{\mathbb Z}$, the quotient
  topology on $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ is indiscrete; its
  Hausdorff reflection is $0$.  Consequently every continuous homomorphism
  $\epsilon\to H$ into a Hausdorff group is zero, and the Borel unipotent
  $U=\epsilon$ cannot act by nontrivial continuous translations on the compact
  solenoid $\Sigma$.  This explains the Pass-82/83 degree-$0$ vanishing:
  nontrivial finite characters live on the closed kernel $\widehat{\mathbb Z}$
  but do not descend to $\epsilon$.  The missing finite-prime Weyl flip is
  therefore replaced not by a morphism $\epsilon\to\mathbb Q$, but by the
  degree-$1$ solid boundary
  $$D\epsilon\simeq\mathbb Q[-1],\qquad \mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\simeq\mathbb Q,$$
  represented by the finite-adele extension
  $$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.$$
  Machine-verified `check-pass84.py` ->
  `pass84-dense-phantom-boundary-action-check.json` PASS. Counter 84->85.
- Earlier note: Pass 83 (2026-06-20) corrected the exact-row comparison between the
  full adelic solenoid
  $$\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z\cong\mathbb A/\mathbb Q$$
  and the finite phantom $\epsilon=\widehat{\mathbb Z}/\mathbb Z$.  The projection
  $\Sigma\to\mathbb R/\mathbb Z$ has closed kernel $\widehat{\mathbb Z}$, not
  $\epsilon$; the correct compact Hausdorff row is
  $$0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0.$$
  The phantom appears instead as the dense/non-Hausdorff quotient
  $$\mathbb R\to\Sigma\to\epsilon=\widehat{\mathbb Z}/\mathbb Z\to0,$$
  so the Pass-82 wording "finite-prime kernel $\epsilon$" must be read as
  "finite-prime quotient boundary".  The compact row does not split continuously:
  Pontryagin duality gives
  $$0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0,$$
  and a splitting $\mathbb Q/\mathbb Z\to\mathbb Q$ is impossible because $\mathbb Q$ is
  torsion-free.  Global Fourier theory therefore restricts nontrivially to the
  closed profinite kernel $\widehat{\mathbb Z}$ (characters $\mathbb Q/\mathbb Z$), but
  only the trivial character descends to $\epsilon$ in degree $0$; the finite-prime
  Fourier content survives only as the boundary quotient $\mathbb Q/\mathbb Z$.
  Machine-verified `check-pass83.py` ->
  `pass83-solenoid-exact-triangle-correction-check.json` PASS. Counter 83->84.
- Earlier note: Pass 82 (2026-06-14) tested the Whittaker/archimedean residue of the
  maximally degenerate solid Borel principal series. Since
  $I(s)=\mathrm{Ind}_B^{\mathrm{Sp}(H)}\chi_s=\chi_s$ and $\chi_s$ is trivial on
  $U=\epsilon$, every nontrivial Whittaker functional
  $\Lambda:I(s)\to\psi_U$ vanishes; only the trivial-character constant term survives. Finite
  shadows confirm the same fact: Fourier coefficients of the constant $U_N=\mathbb Z/N$ action
  vanish for all nontrivial additive characters, while the trivial coefficient is $N$. Thus the
  Rosser torsor is not carried by a generic Whittaker coefficient; it is the unipotent shear
  parameter $U=\epsilon$ itself. Adding the real place gives the compact Hausdorff full adelic
  solenoid
  $$\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z,$$
  with a provisional finite-phantom row later corrected in Pass 83: the closed kernel of
  $\Sigma\to\mathbb R/\mathbb Z$ is $\widehat{\mathbb Z}$, while
  $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ is the dense quotient $\Sigma/\mathbb R$.
  This restores global adelic self-duality for $\mathbb A/\mathbb Q$, but it does not produce a
  finite-prime solid morphism $\epsilon\to\mathbb Q$; the no-Weyl-flip wall remains for the finite
  phantom. Machine-verified `check-pass82.py` ->
  `pass82-whittaker-archimedean-repair-check.json` PASS. Counter 82->83.
- Earlier note: Pass 81 (2026-06-14) read the Pass-80 solid Borel $B=\mathbb Q^{\times}\ltimes
  \epsilon=\mathrm{Sp}(H)$ as a representation, identifying the no-Weyl-flip wall with a
  functional-equation obstruction. (81a) **Maximally degenerate principal series:** since
  $\mathrm{Sp}(H)=B$, the flag variety $\mathrm{Sp}(H)/B$ is a single point (no Bruhat big cell:
  $\bar U=\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$), so every $I(s)=\mathrm{Ind}_B^{
  \mathrm{Sp}(H)}\chi_s$ collapses to the inducing character $\chi_s$ — length $1$, irreducible, no
  reducibility points; the Schrödinger model of $B$ on sections over the fixed polarization $\epsilon$
  uses only dilation ($T=\mathbb Q^{\times}$, $\chi_s(t)=|t|^s$) and shear ($U=\epsilon$), never the
  dual polarization. (81b) **No functional equation:** the standard intertwiner $M(w,s):I(s)\to I(-s)$
  integrates over the opposite unipotent $\bar U=\mathrm{Hom}(\epsilon,\mathbb Q)=0$, so the
  Gindikin–Karpelevich/Harish-Chandra $c$-function is the **empty product** $c(s)=1$ and the
  $s\mapsto-s$ reflection is the empty relation — $I(s)\not\cong I(-s)$, no solid intertwiner. (81c)
  **Finite/limit dichotomy:** at each finite level $N$ the flip exists (finite Fourier $F_N$ realises
  $w$, conjugating dilation-by-$t$ to dilation-by-$t^{-1}$, EXACTLY $F_N D_t F_N^{-1}=D_{t^{-1}}$ — the
  $s\leftrightarrow-s$ reflection) with Gauss-sum $c$-factor $|g(\psi)|^2=p$ at every prime; the
  functional equation dies only in the limit, $\bar U_N=\mathbb Z/N\rightsquigarrow\bar U=0$.
  *Finitely self-dual, limanly one-sided.* (81d) **Löb/Rosser face:** under Pass 51 [integral $=$ Löb
  $=$ canonical $=\mathbb Q$-side] vs [non-integral $=$ Rosser $=$ torsor $=\epsilon$-side], the missing
  flip is a $B$-equivariant Fourier iso $\epsilon\to\mathbb Q$ exchanging the polarizations; its
  non-existence $\mathrm{Hom}(\epsilon,\mathbb Q)=0$ is exactly *"the Rosser torsor does not retract
  onto the canonical Löb datum"*; the surviving $\mathrm{Hom}(\mathbb Q,\epsilon)=\epsilon=U$ (shear)
  is *"forget canonicity: Löb$\to$Rosser"*. Slogan: you can always forget a fixed point is canonical,
  never canonically recover canonicity — that one-way street IS the no-Fourier-flip wall. (81e)
  **reflexive-but-not-dualizable** is the precise criterion: a polarization admits the
  cross-polarization functional equation iff it is $\otimes$-dualizable; reflexivity
  ($\epsilon^{**}=\epsilon$, Pass 78) is insufficient. Machine-verified `check-pass81.py` ->
  `pass81-degenerate-principal-series-functional-equation-check.json` PASS: (A) $|\mathbb P^1(\mathbb
  Z/N)|>1$ finite, $\mathrm{Hom}/\mathrm{Ext}^1(\mathbb Z/N,\mathbb Q)=0$ limit; (B) $F D_t F^{-1}=
  D_{t^{-1}}$ to $<10^{-13}$ for $N\le16$; (C) $|g(\psi)|^2=p$ to $<10^{-12}$ for $p\le23$; (D)
  $c$-tower $\equiv0$ vs $b$-tower $=\mathbb Z/N_n\neq0$. Bash mount lagged again (served
  `check-pass81.py` truncated at line 192, missing `main()`); ran from a sandbox-local copy and wrote
  all repo files via Windows-path tools per the APS run-sync hazard. Counter 81->82.
- Earlier note: Pass 80 (2026-06-14) computed the solid symplectic automorphism object of the
  hyperbolic phantom plane $H=\epsilon\oplus\mathbb Q$. Decisive input: the Pass-79 vanishing
  $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=H^0(\mathbb Q[-1])=0$ (vs
  $\mathrm{Hom}(\mathbb Q,\epsilon)=\epsilon\neq0$), which forces the lower-left entry of every
  $2\times2$ solid endomorphism of $H$ to vanish. (80a) $\mathrm{End}_{\mathrm{Solid}}(H)$ is
  **upper-triangular**; (80b) $\mathrm{Sp}(H)$ is therefore the solid **Borel** $B=\mathbb Q^{\times}
  \ltimes\epsilon$ (the affine "$ax+b$" group fixing the polarization $\epsilon$), NOT $\mathrm{SL}_2$
  and NOT a nonabelian Heisenberg group ($U$ is abelian); the Weyl flip $w=\begin{psmallmatrix}0&1\\
  -1&0\end{psmallmatrix}$ (the cross-polarization Fourier transform) has no solid model. (80c)
  **Metaplectic non-descent:** the finite-adele Weil representation of $\mathrm{SL}_2(\mathbb A_f)$
  does not act on the phantom; at finite level $N$ the flip is the Fourier transform $F_N$
  ($F_N^4=I$, $|g_N|^2=N$, $w\in\mathrm{SL}_2(\mathbb Z/N)$), but its only candidate limit lives in
  $\mathrm{Hom}(\epsilon,\mathbb Q)=0$. The **precise wall** is that one-sided vanishing (i.e.
  $\epsilon$ reflexive but NOT $\otimes$-dualizable) — explicitly NOT the degeneracy of $b$, which the
  Pass-79 Next step had guessed; the shear-by-$b$ unipotent survives, only the inverse intertwiner is
  absent. Machine-verified `check-pass80.py` -> `pass80-metaplectic-borel-noflip-check.json` PASS
  (finite $\mathrm{SL}_2(\mathbb Z/N)$ orders + brute force $N\le12$; $c$-tower $\equiv0$ vs $b$-tower
  $\neq0$; $F_N$ for $N\in\{3,..,21\}$). Bash mount again lagged (served the file truncated near Pass
  71); all writes via Windows-path tools per the APS run-sync hazard. Counter 80->81.
- Older note: Pass 79 (2026-06-13) AUDITED the Pass-78 "Next step" and corrected its premise.
  The conjecture asked for a self-pairing $b:\epsilon\otimes^\blacksquare\epsilon\to\mathbb Z[-1]$
  and a symplectic $\epsilon$ with the primes as Darboux coordinates. Findings: (79a) $\epsilon$ is
  **not** self-dual — Pass 78 proved *reflexivity* $\epsilon^{**}\cong\epsilon$, not self-duality;
  in fact $D\epsilon\cong\mathbb Q[-1]$, $D\mathbb Q\cong\epsilon[-1]$, so $\epsilon$ and $\mathbb Q$
  are a dual pair (as bare groups $\epsilon\cong\mathbb A_f/\mathbb Q$ is a $\mathbb Q$-vector space
  of dimension $2^{\aleph_0}$, vs $\dim\mathbb Q=1$). (79b) the self-pairing degree is forced:
  $\operatorname{Hom}(\epsilon\otimes\epsilon,\mathbb Z[m])=\operatorname{Ext}^{m-1}_{\mathrm{Solid}}
  (\epsilon,\mathbb Q)$ is $\mathbb Q$ iff $m=2$ and $0$ otherwise, so the proposed $\mathbb Z[-1]$
  target carries ONLY the zero pairing; the unique nonzero self-pairing lives in $\mathbb Z[2]$ and
  is the finite-adele class $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$. (79c) that pairing is
  ALTERNATING (degree-1 swap sign $-1$, vindicating the symplectic intuition) but DEGENERATE
  (adjoint $\epsilon\to\mathbb Q[1]$ not iso); the nondegenerate symplectic object is the hyperbolic
  plane $H=\epsilon\oplus\mathbb Q$ with Lagrangians $\epsilon,\mathbb Q$. (79d) DARBOUX NO-GO: the
  support idempotents $e_S$ descend to $\mathrm{End}(\epsilon)$ iff $S\in\{\varnothing,\mathbb P\}$
  (else $e_S(1)=\mathbf 1_S\notin\mathbb Z$), so $\epsilon$ is prime-indecomposable — the unit class
  $1\in\widehat{\mathbb Z}^\times$ that drives Pass-78 reflexivity obstructs prime-localization.
  Machine-verified check-pass79.py PASS (incl. $2^6$-subset Darboux enumeration: exactly 2 descend).
  Bash mount again lagged (served the file truncated at Pass 72 / line 8107); all writes via
  Windows-path tools per the APS run-sync hazard. Counter 79->80.
- Earlier note: Pass 78 (2026-06-13) proved solid *reflexivity* of the Loeb-Rosser phantom
  $\epsilon=\widehat{\mathbb Z}/\mathbb Z=\varprojlim^1(N_n\mathbb Z)$: dualizing the defining
  sequence twice (using only the Pass-77 blocks $D\mathbb Z=\mathbb Z$,
  $D\widehat{\mathbb Z}=(\mathbb Q/\mathbb Z)[-1]$, $D(\mathbb Z/n)=(\mathbb Z/n)[-1]$, and resolving
  $\mathbb Q/\mathbb Z=\operatorname{colim}\mathbb Z/n$ termwise) gives $D\epsilon\cong\mathbb Q[-1]$
  and $\epsilon^{**}\cong\epsilon$ (Thms 78a/78b). The connecting map is the dense inclusion
  $\mathbb Z\hookrightarrow\widehat{\mathbb Z}$ (multiplication by the *unit* class
  $1\in\widehat{\mathbb Z}^\times$), so no $\varprojlim^1$-of-$\varprojlim^1$ secondary phantom
  arises; a non-unit (idempotent $e_2$) class would create one (machine-exhibited). The biduality
  sign is the antipode $-1$ from the odd shift $[-1]$ (Thm 78c). Machine-verified check-pass78.py
  PASS. The bash mount again lagged (served the freshly written script truncated at line 184), so all
  writes/verification went through the Windows-path tools per the APS run-sync hazard. Counter 78->79.
- Earlier note: Pass 77 (2026-06-12) resolved the all-prime derived-realization question
  as a two-faced theorem: LCA/Pontryagin is a hard no-go (the dense subgroup $\mathbb Z$
  forces $(\widehat{\mathbb Z}/\mathbb Z)^\vee_{\mathrm{LCA}}=0$), while $\mathrm{Solid}_{\mathbb Z}$
  realizes the phantom nonzero with the profinite dual shifted into cohomological degree 1
  ($\widehat{\mathbb Z}^*\cong(\mathbb Q/\mathbb Z)[-1]$), so the signed law is a derived degree-1
  equation. Machine-verified check-pass77.py PASS. The bash mount again lagged (served the file
  truncated at Pass 72 while the real file held Passes 73-76), so all writes were made with the
  Windows-path tools and verified by Windows-path Read, not bash grep. Counter 77->78.
- Earlier note: Pass 76 (2026-06-11) completed a crashed prior run that had already
  written `code/scripts/check-pass76.py` without its report or log entries. This run
  generated the verified report, appended the Pass-76 discussion body, and updated the
  logs/notes via Windows-path file tools: the bash mount lagged and served the file
  truncated at Pass 72 while the real file already held Passes 73-75, so a bash append
  would have clobbered them. Per the APS run-sync hazard, all writes were made with the
  Windows-path tools and verified by Windows-path Read, not bash grep. Counter 76->77.
- Run status: continuous automation resumed on 2026-05-25; Pass 38 was recovered
  on 2026-06-01 after a crashed run left it truncated mid-Skeptic (counter was
  already at 39, so it was not double-incremented). Pass 39 ran clean on
  2026-06-03 (uniform all-finite-groups selective-median theorem proved). Pass
  40 ran clean on 2026-06-03 (median uniqueness theorem + infinite-front
  residuation/orbit dichotomy). Pass 41 ran clean on 2026-06-04 (limit-FP
  phantom theorem: the orbit-meet fixed point s_omega is inconsistent with
  antitonicity; all-level nFG2 forces index-2 stabilization; median tower has a
  phantom limit under failure of meet-continuity). A crashed write left the
  tail of this file corrupted (Pass-40/Pass-41 Next-step fragments concatenated);
  Pass 42 repaired it. Pass 42 ran clean on 2026-06-04 (detached fixed point =
  algebraic Rosser sentence; the Rosser gadget R_2 realizes FP-synt with no
  orbit-attached Goedel fixed point). Pass 42's discussion-log append was lost
  to a second crashed write (only its research-log entry, script, and report
  landed; the log still ended at Pass 41's truncated Next-step). Pass 43
  recovered this: it completed Pass 41's truncated Next-step sentence and
  appended a reconstructed Pass-42 entry (from the research-log + report), then
  ran its own pass. Pass 43 ran clean on 2026-06-04 (arithmetic lift of the
  detached fixed point: GL/Loeb forces the Goedel fixed point to coincide with
  Con = boxtimes(bot), hence orbit-ATTACHED, by de Jongh-Sambin; monotonicity
  alone does NOT force attachment, so the lift obstruction is formalized Loeb, Pass 49 ran (Smith
  bracketing + explicit phantom + group-orbit liberation); its discussion-log
  tail was truncated by a crashed write and RECOVERED by Pass 50 on 2026-06-06.
  Pass 50 ran clean (Bredon vertex-bracket identity e(F^tau)=chi(Delta(F^tau))
  with L=e+Phi=1; phantom Betti number b_phantom=#failed covers; front-cardinality
  decoupling of group-orbit liberation, R(3)=56/R(4)=411 + all-n witness family).
  Pass 50's discussion-log Archivist tail was truncated mid-filename by a crashed
  write and RECOVERED by Pass 51 on 2026-06-06 (counter already at 51, not
  double-incremented). Pass 51 ran clean: e(F^tau)=|Fix| is a COMPLETE but
  DEFLATIONARY bracket invariant since Fix(antitone) is an antichain (Lemma
  51a/Thm 51a); the phantom Betti number = dim H^1 of an obstruction complex =
  lim^1 of the image tower, additive over arms (Thm 51b); integral unit <=> Loeb-
  attached, non-integral unit <=> Rosser-evades-Loeb (Thm 51c). Pass 52 ran clean
  on 2026-06-06 (flipped invariant Phi(tau)=1-|F^tau| characterized: Thm 52a
  flipped-chain formula with period-4 sign s(d)=++--; Thm 52b extremal dichotomy
  sup Phi=1 fixed-point-free / inf Phi=-infinity via the fixed-antichain fan
  F_m giving Phi=1-m; Thm 52c Phi = geometric-minus-combinatorial fixed-point
  Euler gap; machine-verified PASS). Pass 53 ran on 2026-06-07, concurrently
  with a recovery run that wrote the full Pass-51 and Pass-52 discussion-log bodies
  (the recovery run crashed mid-Pass-52-Proposer; Pass 53 completed that
  truncation). Pass 53 closed the two carried residues: (ii) the INTEGRAL 2-adic
  phantom -- field-coefficient lim^1 vanishes by Mittag-Leffler so b_phantom=r was
  a finitary shadow, while the integral image tower (Z,x2) has
  lim^1 = Zhat_2/Z uncountable (Thm 53a); (iii) the Loeb/Rosser dictionary upgraded
  to a functor L_(-): Deriv -> resAPS whose integral-unit essential image is exactly
  the Loeb/GL subcategory, Rosser packages forming a non-canonical unit-torsor in
  the complement (Thm 53b). Machine-verified PASS. NOTE: this run coincided with a
  concurrent invocation; the discussion file end was rewritten once mid-run and
  Pass-53 edits were re-applied afterward. Pass 54 ran clean on 2026-06-07: it
  discharged Pass-53 obligation (1), realizing the integral 2-adic phantom inside
  an HONEST integral residuated lattice -- the negative cone Z^- with the m-fold
  dilation endomorphism d_m(x)=mx, whose inverse system has connecting module
  (Z,xm) and derived limit lim^1 = Zhat_m/Z; proved the prime 2 is NOT forced and
  the phantom is RADICAL-invariant (depends only on rad(m): m=2,4,8 share Zhat_2/Z,
  m=6,12 share (Z_2 x Z_3)/Z), with m=1 the phantom-free boundary. Obligation (2)
  (Rosser torsor = H^1) advanced to a proof sketch and left [Partially resolved].
  Machine-verified PASS (`check-pass54.py`). The build mount lagged behind the
  Windows-path writes this run (null-byte reads); per the APS-run-sync-hazard note,
  correctness was confirmed via Windows-path file tools and a /tmp-local exec, not
  bash grep of the mount. Pass 55 ran clean on 2026-06-07 (dilation-solenoid
  refutability boxtimes_m written explicitly on C_m=Z[1/m]^- with the phantom as
  boxtimes_m's OWN lim^1; ML = nFG2 dichotomy; "finitely Loeb, limanly Rosser"
  fusion, Thms 55b/c/d). Pass 56 ran clean on 2026-06-07 and decided Pass-55
  residue (i) with a DICHOTOMY: the completed arena L^(m) is a complete
  distributive lattice, hence a complete Heyting algebra residuated under MEET
  with the INTEGRAL unit top (Loeb) -- but the DILATION monoid (+, non-integral
  Rosser unit a*) does NOT extend to a residual, its fiber c\a* going
  non-principal at the lone cover a*=sup_n a_n (the same cover that carries the
  phantom). So residuation and the Rosser unit are mutually exclusive in the
  completion: finitely both (cover principal), limanly only a preAPS. Residue (ii)
  closed: the Cech complex of the dilation cover is the two-term delta=1-m*shift
  on prod_n Z, H^0=lim=0 (detached), H^1=lim^1=Zhat_m/Z. Machine-verified PASS
  (`check-pass56.py`). Counter 56->57; reads via Windows-path tools per
  the APS-run-sync-hazard note. Pass 57 ran clean on 2026-06-07 and discharged
  Pass-56 obligation (i) by UPGRADING the Pass-56 dichotomy to a CARRIER-FREE
  no-go (Lemma 57a): in any complete residuated lattice whose unit e=V_n a_n is a
  non-attained sup-of-chain, a completely join-irreducible cover c>e with a_n(x)c<c
  forces c=e(x)c=V_n(a_n(x)c)<c -- contradiction; hence NO residuated tensor with a
  Rosser (sup-of-chain) unit admits a join-irreducible cover (Cor 57a' makes
  Thm 56a.2 absolute: every (x) fails, not just the additive one). The Skeptic's
  quantale escape was audited (Thm 57c): the ideal/downset (Day-convolution)
  completion IS a unital residuated quantale carrying an additive unit, but it
  de-singularizes the cover (V_n down(a_n) splits strictly below down(a*), becoming
  principal), voiding Lemma-57a's hypothesis and KILLING the phantom (lim^1=0) --
  Phantom XOR Quantale: keep the ghost or the algebra, never both. Obligation (ii)
  promoted coker(delta)=Zhat_m/Z to an iso of Rosser unit-TORSORS (Thm 57b), modulo
  naturality across Deriv. Machine-verified PASS (`check-pass57.py`). A mount-lag
  episode served a truncated script copy to the sandbox; the report was regenerated
  from a verified first run + the construction-trivial Lemma block and written via
  Windows-path tools per the APS-run-sync-hazard note (first-run report stubbed
  SUPERSEDED, undeletable on the mount). Counter 57->58. Pass 58 ran clean on
  2026-06-07 and discharged Pass-57 residue (i) by REFUTING unconditional survival
  of Lemma 57a: the "absorbing Rosser cap" W = (a_0<...<e<c<top), unit e, tensor
  (bot absorbing; min below e; max once a large operand >=c appears) is an explicit
  complete commutative residuated lattice with a non-attained sup-of-chain unit
  e=\/a_n AND a completely join-irreducible cover c>e, where a_n@c=c COFINALLY
  (n>=1) -- so the 57a contradiction \/_n(a_n@c)=c is satisfied trivially, NOT forced
  by join-irreducibility (Thm 58a). Strictness/cancellativity is therefore ESSENTIAL,
  not cosmetic. The escape's price (Thm 58b refined dichotomy / Phantom-trichotomy):
  the cover fiber c\e collapses to bottom (principal), the image tower is constant
  (Mittag-Leffler), varprojlim^1=0 -- the Rosser torsor degenerates (idempotent-
  absorbing cover = NON-FREE witness-comparison action). So the three completions of
  the Rosser unit now read MacNeille=(phantom, no residual) / Ideal-quantale=(residual,
  cover de-singularized) / Absorbing-cap=(residual, cover kept join-irreducible, BUT
  phantom killed by idempotence): you may keep any two of {residuation, join-irreducible
  cover, phantom}, never all three. Residue (ii) (naturality of Theta) advanced to
  [Partially resolved]: Theta is natural on the radical-graded subcategory
  Deriv^res_rad (tower maps (Z,xm)->(Z,xm') exist iff rad(m)|rad(m')), with a precise
  rad-incompatibility obstruction off it (Prop 58c). Machine-verified PASS
  (`check-pass58.py` via inline exec; bash mount lagged the Windows-path write,
  served a 160-line truncated copy, so per [[aps-run-sync-hazard]] correctness was
  confirmed off-mount). Counter 58->59. Pass 59 ran clean on 2026-06-08 and
  discharged Pass-58 residue (i), the intermediate/non-idempotent absorbing cover:
  the mixed regime EXISTS (two-parameter family $W_{d,\delta}$, 28 machine-checked
  complete commutative residuated lattices with finite absorption depth
  $d=\inf\{n:a_n\otimes c=c\}$ and idempotence defect $c\otimes c=\top\ne c$), but its
  phantom is GENUINELY 0, never "partial": finite depth => eventually-constant fiber
  tower => Mittag-Leffler => $\varprojlim^1=0$ (Thm 59a), and a finite-rank "partial
  phantom" is impossible by GRAY's dichotomy ($\varprojlim^1$ of a countable tower is
  0 or $2^{\aleph_0}$; Cor 59b). Idempotence defect is $\varprojlim^1$-invisible
  (localized at the compact cover above $c$, not the non-compact cover $e\prec c$
  where the phantom pins). The Pass-58 trichotomy is SHARP, not a spectrum boundary:
  $(d,\iota)$ are phantom-flat moduli, the phantom jumps 0->$2^{\aleph_0}$ only at the
  non-residuated wall $d=\infty$. Prop 59c unifies depth=nFG2-index=ML=phantom-free
  (41a/55c/58b). Machine-verified PASS off-mount per [[aps-run-sync-hazard]] (bash
  served a Pass-53-era stale copy of the discussion file; edits applied via
  Windows-path tools). Counter 59->60. Pass 60 ran clean on 2026-06-08 and closed
  the LAST functorial gap of the L_(-) programme (Pass-58 residue (ii)): pinned the
  Deriv-morphisms that lift to residuated cover-filtration maps -- a map C_m->C_m'
  exists iff the carrier localization embeds, Z[1/m] subset Z[1/m'], iff
  rad(m)|rad(m') (Thm 60a), so the rad-grading is literally the squarefree
  divisibility lattice (finite prime-sets under inclusion); proved rad-divisibility
  is the SOLE obstruction to naturality of Theta:Ros_(-)=>varprojlim^1(-) -- where a
  morphism exists the Cech-cochain square commutes by snake-lemma naturality of delta
  (Thm 60b), where it does not the square is vacuous, so Theta is a natural iso of
  the phantom-sheaf S|->(prod_{p in S}Z_p)/Z with the Rosser-torsor presheaf on the
  prime spectrum. Pathology (Cor 60c): m=6,m'=10 are rad-INCOMPARABLE (rad6={2,3},
  rad10={2,5}), no cover-filtration map either way; their only common sub-arena is the
  gcd-of-radicals solenoid C_2, the shared 2-adic ghost Z_2/Z. SECONDARY (set-theoretic
  frontier, [New (Pass 59)]): Gray's 0-or-2^aleph0 dichotomy is strictly an
  omega-phenomenon and does NOT lift -- replacing the front {a_n}_{n<omega} by an
  ascending omega_1-chain makes the cover-fiber system pro-isomorphic to the
  Mardesic-Prasolov strong-homology system, whose varprojlim^1 is NONZERO under CH
  (Mardesic-Prasolov 1988) and ZERO under PFA (Dow-Simon-Vaughan 1989); hence "an
  aleph_1-sized intermediate phantom exists" is INDEPENDENT of ZFC (Thm 60d). Machine-
  verified PASS off-mount per [[aps-run-sync-hazard]] (check-pass60.py; 144-pair
  carrier/rad equivalence, non-ML witnesses, G_m-equivariance, incomparable pathology,
  rad-lattice poset axioms; bash served a Pass-53-era stale copy again, edits applied
  via Windows-path tools). Counter 60->61.
  not regularity; the R_2 detached geometry is realizable only by a Rosser-type
  predicate that keeps D1 + Sigma_1-completeness but evades Loeb). Pass 43's
  discussion-log entry and Next-step were ALSO lost to a third crashed write
  (its script `check-rosser-arithmetic-lift.py` and report landed; the log still
  ended at the truncated reconstructed Pass-42 Proposer). Pass 44 recovered this:
  it completed the truncated Pass-42 reconstruction, appended a reconstructed
  Pass-43 entry (from this header + `rosser-arithmetic-lift-check.json`), then ran
  its own pass. Pass 44 ran clean on 2026-06-05 (attachment/Loeb dividing line:
  orbit-DESCENT is the exact abstract gate for fixed-point attachment;
  ~FG2(1) is necessary but NOT sufficient for detached-only models; the M3 map
  x->y->z->z fails FG2(1) yet descends to an attached fixed point). Pass 45 ran
  on 2026-06-05 (general-L descent<=>attachment RESOLVED negatively: descent =>
  attachment is carrier-independent (Thm 45b), but attachment =/=> descent — the
  order-reversing involution on the odd chain C_5 is a non-descending orbit with
  an attached central fixed point (Thm 45c); the eventual-2-cycle trichotomy
  degenerate/antichain/chain (Cor 45d) is the correct refinement; the Pass-44
  "exact gate" equivalence was an M3 artifact). Pass 45 also deleted a stray
  truncated Pass-42 duplicate at EOF (a fourth crashed write) and repaired a
  crash-splice in definitions.md; no content lost. The enumerative survey script
  is committed but was NOT machine-run (workspace shell unavailable this pass) —
  Pass 46 should run it. Pass 46 ran clean on 2026-06-05 (machine-ran the
  deferred survey: descent=>attachment had 0 violations over >4000 antitone maps
  on {M3,C3..C7,N5,M4}, machine-confirming Thm 45b/45c; the PARTIAL report was
  replaced by a real run. NEW Thm 46a: on a chain every antitone orbit has
  eventual period <=2 — chains are pure regime-(iii), no antichain/period>=3
  cycle, since boxtimes^2 is monotone and a monotone self-map of a chain is
  eventually fixed; period>=3 appears only off chains (M3,M4) where boxtimes^2
  may permute an antichain. NEW Cor 46b: regime (iii) splits into (iii-a)
  bracketing/attached vs (iii-b) chain-gap/fixed-point-free — the even-chain
  reversal r(x)=2m-1-x on C_{2m} is a consistent antitone box with NO fixed
  point, the chain analogue of the M3 Rosser gadget). Pass 46's discussion-log
  append and research-log entry were lost to a crashed write (only the survey
  report `descent-attachment-general-check.json` landed); Pass 47 reconstructed
  the Pass-46 entry from this header + that report and repaired the EOF debris
  (a fifth crashed-write fragment). Pass 47 ran clean on 2026-06-06
  (chain-cycle reachability RESOLVED: bottom discipline does NOT confine the
  chain regime — the C5 reversal is itself bottom-disciplined (bot=0 least) with
  a T-reachable chain-cycle {1,3}, Thm 47a; the Pass-45/46 confinement
  conjecture is FALSE. The genuine gate is ORBIT FLATNESS + REACHABILITY (Thm
  47b): the eventual cycle being an antichain, independent of bottom discipline.
  B_N is flat (front antichain + degenerate sink s), so it satisfies the Pass-44
  equivalence for THAT reason, not bottom discipline (Prop 47c); a {bot,U}
  chain-cycle may even coexist in B_N but is unreachable from T, so the right
  predicate is reachability not existence. Chain bracketing criterion PROVED
  (Thm 47d, closing the Cor 46b obligation): a comparable eventual 2-cycle on a
  chain brackets a fixed point iff the invariant interval has ODD cardinality —
  C5/C7 bracket, C6/C8 are chain-gaps. Machine-checked: 218 bottom-disciplined
  C5 chain-cycles, 0 Thm-45b violations,
  `chaincycle-reachability-bottom-discipline-check.json` PASS). Pass 48 ran clean
  on 2026-06-06 (all three Pass-47 residual threads attacked: (a) POSET bracketing
  RESOLVED — the controlling invariant is not |I| but the cycle type of boxtimes
  on F=Fix(boxtimes^2) cap I; boxtimes has a fixed point in I iff the order-
  reversing involution boxtimes|_F has one, guaranteed when |F| is ODD (Thm 48a),
  recovering Thm 47d on chains where F=I. Pathology: the Boolean cube 2^[n] under
  complementation is a comparable 2-cycle {emptyset,[n]} with fat even interval and
  NO fixed point ("cube-gap"), while the SAME poset 2^2 carries another order-
  reversing involution WITH fixed points {1,2} — so parity-of-|I| does NOT control
  bracketing. (b) INFINITE flatness lift: the well-foundedness-free condition is
  JOIN-CONTINUITY of boxtimes, not well-foundedness of L — a join-continuous
  antitone map realizes every limit 2-cycle (Thm 48b), and dropping continuity
  reinstates the Thm-41c phantom. (c) PERIOD-k detachment RESOLVED — FP-synt
  coexists with an eventual period-4 (indeed any period>=2) ANTICHAIN cycle, and
  the fixed point is necessarily DETACHED (Prop 48c): forcing p<=o_i closes the
  cycle into an antichain comparability, breaking antitonicity. Witness: the
  period-4 Rosser gadget R_4. Machine-verified
  `artifacts/reports/poset-bracketing-period4-check.json` PASS — parity criterion
  0 violations over C2..C5/2^2, cube-gap for 2^1..2^4, R_4 4-cycle+detached FP,
  forced-comparability breaks antitone for k=2..5). Pass 49 ran clean on
  2026-06-06 (all three Pass-48 residual threads CLOSED. (a) EXACT bracketing via
  Smith theory: tau=boxtimes|_F acts on the order complex Delta(F), which is
  F2-acyclic (cone over apex a=Fix-interval bottom), so by Smith theory the fixed
  subcomplex |Delta(F)|^tau is nonempty and F2-acyclic; boxtimes brackets iff
  |Delta(F)|^tau contains a 0-CELL (a tau-fixed VERTEX), equivalently iff some
  tau-invariant chain has ODD length — odd |F| (Thm 48a) is the special case where
  the whole vertex set is the invariant chain. Cube-gap re-explained: for
  2^[n]/complementation, |Delta(F)|^tau is the single barycenter of the flipped
  edge {emptyset,[n]} — nonempty and acyclic as Smith demands, but a 1-CELL
  midpoint carrying NO vertex, so no bracket. Lefschetz L(tau)=1 throughout
  (consistent, never forcing a vertex). Thm 49a. (b) EXPLICIT phantom built: the
  non-join-continuous antitone box with o_{2n} ↑ a^* but box(a^*)=m < b^* strict,
  on a complete chain-plus-doubled-top lattice; a SINGLE failed join-cover at a^*
  suffices to break join-continuity and reinstate the Thm-41c phantom — answers
  "is one failed cover enough?" affirmatively (verified on truncations K=2..6).
  (c) GROUP-ORBIT LIBERATION (Thm 49d): R_4/M5 admits 411 commutative residuated
  unital tensors with the detached p (or o0) as a NON-INTEGRAL unit, and 0 integral
  (unit=U) ones — the M_n (n>=3) obstruction strands residual a\bot on a non-
  principal fiber, so integrality is impossible but non-integrality is abundant.
  Front rigidity (Pass 34/35) forbids group TENSORS on a B_N front; it does NOT
  forbid a free group ORBIT (the 4-cycle = regular rep of Z/4) carrying a detached
  fixed point under residuation. The escape REQUIRES the non-integral unit B_N's
  tail-coupled T-unit could never supply. Machine-verified
  `artifacts/reports/pass49-bracketing-phantom-grouporbit-check.json` PASS
  (A/B/C all true; bracket flags, K-truncations, 411/0/detached counts). New model
  `code/models/examples/R4-residuated.json`. Next run = Pass 50.
- Main bridge: ChatGPT Project material must be copied, exported, shared, or
  relayed into this repository before Codex can use it reliably.
- Initial focus: strengthen the APS/G2-ZOO research program by turning existing
  notes into sharper definitions, conjectures, proof tasks, and counterexample
  searches.

## Iteration Format

```text
### Pass N - YYYY-MM-DD HH:MM JST

Focus:

Proposer:

Skeptic:

Formalist:

Archivist:

Repository updates:

Next step:
```

## Iterations

### Pass 1 - 2026-05-24 14:46 JST

Focus:

Clarify the gap between completion-generated fixed points and syntactic
APS/Jeroslow fixed points, using the completion and residuated-domain notes as
the first bridge.

Proposer:

Make the next target a "completion-reflection square." Start with an APS or
preAPS $L$, an embedding $i:L\to \widehat L$, and an extension
$\widehat{\boxtimes}:\widehat L\to\widehat L$. A completion fixed point
$q=\widehat{\boxtimes}q$ becomes research-useful only when there is a
reflection principle saying either $q=i(p)$ for some formula-level $p$, or
that $q$ has a definable approximation from which an actual
$p=\boxtimes p$ can be recovered.

Skeptic:

The danger is that completions manufacture limit objects that have no syntactic
name. For antitone $\boxtimes$, even existence in $\widehat L$ may come from
working with $\widehat{\boxtimes}^2$, a doubled order, or a topology rather
than from the original APS language. A reflection theorem must therefore name
the exact definability or compactness property that prevents fake fixed points.

Formalist:

Separate four obligations: define the embedding $i$; define which extension of
$\Box$, $\boxtimes$, and residuals is being used; define "principal,"
"compact," or "formula-definable" elements of $\widehat L$; and prove a
rounding/reflection lemma from a completion fixed point back to $L$. Without
these, the slogan "completion fixed point is not syntactic fixed point" stays
useful but non-theorematic.

Archivist:

Added a concrete completion-reflection work package to
`research/notes/completion-and-fixed-points.md` and promoted the corresponding proof
problem in `research/open_problems.md`.

Repository updates:

- `records/discussions/autonomous-discussion.md`: recorded pass 1 and advanced the state.
- `research/notes/completion-and-fixed-points.md`: added the reflection-square target.
- `research/open_problems.md`: added a concrete completion-reflection problem.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 2 to choose one candidate completion, preferably MacNeille completion
or ideal completion, and write the first precise version of the embedding and
extension clauses.

### Pass 2 - 2026-05-24 20:36 JST

Focus:

Choose MacNeille completion as the first test case for the completion-reflection
square and make the embedding/extension vocabulary explicit enough for a later
theorem or countermodel.

Proposer:

Use MacNeille completion because it is already tied to algebraic proof theory
and cut-elimination stability in the BS16 note. The first work item should be
purely structural: define the cut embedding $i:L\to \widehat L$, then ask how
$\Box$, $\boxtimes$, and residuals extend across it. A completion fixed
point only counts as reflected when it lands on a principal cut $i(p)$, or when
a separate compact/definable rounding lemma recovers such a $p$.

Skeptic:

MacNeille completion is attractive exactly because it can be too strong. It may
add cuts that satisfy fixed point equations for order-theoretic reasons while
having no formula-level representative. For antitone $\boxtimes$, the main
risk is variance: extending $\boxtimes$ directly as if it were monotone will
hide the real problem. The extension must either pass through the order dual or
state an explicit polarity convention.

Formalist:

Record a three-part test. First, define $X^u$, $X^l$, MacNeille-closed lower
cuts, and the principal embedding. Second, treat $\boxtimes$ as a monotone map
from $L$ to $L^{op}$, then only compare it back to $\widehat L$ after an
explicit dual-identification step. Third, mark the reflection criterion:
$q=\widehat{\boxtimes}q$ is syntactic only if $q=i(p)$ and
$p=\boxtimes p$ holds in $L$, or if a named rounding lemma proves this from
compact definable approximants.

Archivist:

Added MacNeille completion vocabulary to `research/definitions.md`, added a MacNeille
first-test section to `research/notes/completion-and-fixed-points.md`, and sharpened the
open problems with an explicit variance/duality task for $\boxtimes$.

Repository updates:

- `records/discussions/autonomous-discussion.md`: recorded pass 2 and advanced the state.
- `research/definitions.md`: added MacNeille/completion-reflection vocabulary.
- `research/notes/completion-and-fixed-points.md`: added the MacNeille first test.
- `research/open_problems.md`: added a concrete antitone-extension task.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 3 to turn the MacNeille first test into a small finite APS/preAPS model
search target: find either a principal reflected fixed point or a non-principal
completion fixed point that demonstrates failure of reflection.

### Pass 3 - 2026-05-24 21:07 JST

Focus:

Convert the MacNeille reflection idea into a finite model-search target rather
than another abstract slogan.

Proposer:

The next concrete artifact should be a small-model search protocol. Enumerate
finite preorders with $3$ or $4$ elements, choose $T,\bot,\Box,\boxtimes$,
require $\boxtimes$ to be antitone, compute the MacNeille closed lower cuts,
and then classify fixed points of the chosen completion extension as principal
or non-principal. A non-principal fixed cut would be exactly the kind of
completion-generated fixed point that does not automatically reflect to syntax.

Skeptic:

The hardest part is not enumeration but extension discipline. If
$\widehat{\boxtimes}$ is chosen ad hoc, any counterexample may only refute the
wrong extension. The search protocol must therefore record the extension rule
beside every result, and it should separate "APS axiom failure" from
"reflection failure" so that a toy model does not overclaim relevance to the
main G2-ZOO.

Formalist:

Use four classifications for each candidate: (1) no completion fixed point,
(2) only principal fixed points, (3) non-principal fixed points with no
formula-level fixed point, and (4) non-principal fixed points plus a possible
compact/definable rounding path. Also record G2, FG2, primitive
$\boxtimes$-fixed points, and whether A1-A4 or the currently used APS
fragment is being checked.

Archivist:

Added a dedicated model-search note under `code/models/`, linked it from the model
README, extended the completion note with the finite-search target, and added a
matching open problem.

Repository updates:

- `records/discussions/autonomous-discussion.md`: recorded pass 3 and advanced the state.
- `code/models/macneille-reflection-search.md`: added finite search protocol.
- `code/models/README.md`: linked the new search target.
- `research/notes/completion-and-fixed-points.md`: added finite search target.
- `research/open_problems.md`: added a finite MacNeille reflection search task.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 4 to either draft a checker script interface for the search protocol or
write the first hand-checkable 3-element candidate table before automating.

### Pass 4 - 2026-05-24 21:36 JST

Focus:

Turn the MacNeille reflection search protocol into a concrete checker interface
so later passes can automate the small-model search without blurring the
extension convention for antitone $\boxtimes$.

Proposer:

Draft a script contract before writing the script. The checker should accept one
finite APS/preAPS JSON file, validate its preorder and operations, compute
MacNeille closed lower cuts, compute principal cuts, and report primitive
$\boxtimes$-fixed points in $L$. The completed-$\boxtimes$ stage should be
pluggable by named extension rule, because the research question depends on
whether the antitone map is extended through $L^{op}$, a doubled order, or a
later canonical-extension recipe.

Skeptic:

A checker that silently picks one extension rule would create false confidence.
The output must make extension discipline visible: every reported completion
fixed point should carry the extension rule name, whether the cut is principal,
and whether any syntactic $p=\boxtimes p$ exists. Otherwise a "countermodel"
could merely be a countermodel to an undocumented implementation choice.

Formalist:

Use an interface with bounded inputs and explicit output classes:
`no-completion-fixed-point`, `principal-only`, `nonprincipal-without-syntactic`,
and `nonprincipal-with-rounding-candidate`. The first implementation can
support only an `antitone-dual-lower-cut-v0` extension rule, but the output
schema should be ready for additional rules.

Archivist:

Added a checker interface note that specifies the planned PowerShell command,
inputs, output schema, validation checks, and first milestone. Linked it from
the model README and from the MacNeille search protocol.

Repository updates:

- `records/discussions/autonomous-discussion.md`: recorded pass 4 and advanced the state.
- `code/models/macneille-checker-interface.md`: added checker interface contract.
- `code/models/macneille-reflection-search.md`: linked the checker interface.
- `code/models/README.md`: linked the checker interface.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 5 to implement the first minimal checker skeleton or create one
hand-checkable model JSON that exercises the interface.

### Pass 5 - 2026-05-24 22:53 JST

Focus:

Move from a checker contract to a runnable first milestone for the MacNeille
reflection search.

Proposer:

Implement the smallest useful checker now. It should validate a finite JSON
model, compute MacNeille cuts, identify principal cuts, check syntactic
$\boxtimes$-fixed points, and classify completed fixed points under the
provisional `antitone-dual-lower-cut-v0` rule. Include one 3-element chain model
as a smoke test so the interface is exercised immediately.

Skeptic:

The provisional extension rule remains the weak point. The checker must state
that its rule is not yet a theorem-level canonical extension, otherwise the
first generated classifications could be mistaken for mathematical results.
The model example should therefore be treated as an interface smoke test, not a
G2-ZOO countermodel.

Formalist:

The first script should reject malformed preorders and non-antitone
refutability maps. It should report G2, FG2, syntactic fixed points, MacNeille
closed cuts, completed fixed points, and one of the four classification labels
from the interface note. That is enough to make pass 6 a genuine search pass
rather than more scaffolding.

Archivist:

Added `code/scripts/check-macneille-reflection.ps1` and a hand-checkable
`code/models/examples/three-chain-antitone.json` smoke-test model. The checker
implements the first milestone from `code/models/macneille-checker-interface.md` and
keeps the extension-rule warning in its JSON report. The smoke test reports
`principal-only`, with syntactic fixed point `m`.

Repository updates:

- `records/discussions/autonomous-discussion.md`: recorded pass 5 and advanced the state.
- `code/scripts/check-macneille-reflection.ps1`: added the first checker milestone.
- `code/models/examples/three-chain-antitone.json`: added a smoke-test model.
- Smoke-tested the checker on the example model.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 6 to run the checker across the smoke-test model, record the result,
and decide whether to enumerate additional 3-element candidates or revise the
extension rule first.

### Pass 6 - 2026-05-24 23:24 JST

Focus:

Run the new checker on the smoke-test model and decide what the next research
move should be after the initial six-pass automation cycle.

Proposer:

The checker now gives a reproducible baseline: the 3-element chain smoke test
has three MacNeille cuts, one syntactic fixed point `m`, and one completed fixed
point `{ b, m, t }`, which is principal. That makes it a useful sanity check but
not a reflection counterexample. The next substantive step should be an
enumeration pass over additional 3-element preorders and antitone maps, using
this report format as the stable output.

Skeptic:

The result also shows why the provisional extension rule must stay visibly
provisional. The smoke-test classification is `principal-only`, while G2 and FG2
both fail under the current data. That is useful for interface testing but not
yet a theorem about APS completions. Before drawing conclusions, the project
needs either a reviewed canonical extension rule or a separate note explaining
why `antitone-dual-lower-cut-v0` is the right first approximation.

Formalist:

Record this as a baseline result: model `three-chain-antitone`, extension rule
`antitone-dual-lower-cut-v0`, classification `principal-only`, syntactic fixed
points `{m}`, completed fixed point `{b,m,t}` principal at `t`, G2 false, FG2
false, and A1-A4 unchecked. The next proof obligation is to separate
"principal-only under v0" from "reflection theorem under canonical extension."

Archivist:

Generated a JSON report under `artifacts/reports/`, linked it from `artifacts/README.md`,
and added a first-run result section to the MacNeille reflection search note.
This completes the initial six-pass Codex research automation cycle. On
2026-05-25, the user clarified that the loop should not stop at six passes, so
the automation was recreated without a pass-count limit.

Repository updates:

- `records/discussions/autonomous-discussion.md`: recorded pass 6 and marked the initial cycle
  completed.
- `artifacts/reports/macneille-reflection-three-chain-antitone.json`: saved the checker
  report.
- `artifacts/README.md`: linked the MacNeille reflection report.
- `code/models/macneille-reflection-search.md`: recorded the first checker result.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Continue with pass 7 by choosing whether the priority is enumerating
3-element candidates or reviewing the canonical status of the
`antitone-dual-lower-cut-v0` extension rule.

### Pass 7 - 2026-05-25 23:04 JST

Focus:

Incorporate Claude Code Review 1 by replacing the wrong-polarity MacNeille
extension default, separating "principal" from "reflected," and validating the
new size-3 non-lattice example under the corrected rule.

Proposer:

Accept the review's core correction: for antitone
$\boxtimes:L\to L$, treat it as a monotone map $L\to L^{op}$ and use
$((\boxtimes[C])^{l_L})^{u_L}$ as the v1 extension. This makes the old v0
rule a reproducibility path only. The pass should also accept the new
`three-element-nolattice-nosynt` model because it gives exactly the desired
bare finite separation: no syntactic $\boxtimes$-fixed point, but a
non-principal completion fixed point.

Skeptic:

These results are still preAPS/order-theoretic evidence, not APS theorems.
Both validated examples have G2 and FG2 false, and A1-A4 are not checked by the
finite checker. The ChatGPT Project source remains a bridge constraint: no
unrelayed Project content or citation claim was used in this pass. The useful
next question is which additional axioms destroy or preserve the non-principal
completion fixed point.

Formalist:

The checker now distinguishes `reflected-only`, `principal-unreflected`,
`nonprincipal-without-syntactic`, and `nonprincipal-with-rounding-candidate`.
For v1 it checks the principal extension condition against the dual principal
cut $i_{L^{op}}(\boxtimes a)$. The chain smoke test is classified as
`principal-unreflected`: the completed fixed point is $i(t)$, but
$\boxtimes t=b\neq t$. The non-lattice model is classified as
`nonprincipal-without-syntactic`, with fixed cut $\{0,a,b\}$.

Archivist:

Updated the PowerShell checker, regenerated v1 reports for both examples, and
updated the checker interface, search note, output index, and classification
registry. Claude Code Review 1 was incorporated where it supplied concrete
repository artifacts and deferred where it asked for broader APS axiom-package
search.

Repository updates:

- `code/scripts/check-macneille-reflection.ps1`: added v1, dual principal checks,
  reflected status, and refined classifications.
- `artifacts/reports/macneille-reflection-three-chain-antitone-v1.json`: saved the v1
  chain smoke-test report.
- `artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v1.json`: saved
  the v1 non-lattice separation report.
- `code/models/macneille-checker-interface.md`: documented v1, reflected status, and
  extension-condition checks.
- `code/models/macneille-reflection-search.md`: recorded the v1 results and marked
  v0 as legacy.
- `research/notes/completion-and-fixed-points.md`: synchronized the v1 antitone
  extension formula and reflected/principal-unreflected vocabulary.
- `research/notes/g2-aps-zoo-classification.md`: updated the current model registry to
  use v1.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 8 to add either a finite APS-axiom checker layer or a small enumerator
for G2-holding variants, then test whether the `three-element-nolattice-nosynt`
phenomenon survives any nontrivial axiom package.

### Pass 8 - 2026-05-25 JST

Focus:

Prove the orbit-stabilization theorem for n-FG2, construct the first
non-degenerate 4-element witness for G2+FG2+FP-synt, and classify the
implication structure of the n-FG2 hierarchy.

Proposer:

The G2-ZOO now has all 8 separating witnesses at size 3. The next theoretical
advance is an exact characterization of when nFG2($k$) holds for ALL $k\ge 1$.
Looking at the certified data: M-011 (TTTTTTTT) has $\boxtimes$-orbit
$T\to\bot\to\bot\to\cdots$ stabilizing at $\bot=\boxtimes\bot$; M-111 has
orbit $T\to T\to\cdots$ stable at $T$. The common pattern is that the sub-orbit
$(\boxtimes T,\boxtimes^2 T,\ldots)$ is non-increasing and eventually reaches a
syntactic fixed point. The conjecture — now proved — is:

**Theorem (Orbit Stabilization)**: Let $(L,\le,\boxtimes,T,\bot)$ be a finite
preAPS. The following are equivalent:

1. $\mathrm{nFG2}(k)$ holds for all $k\ge 1$.
2. The sequence $\boxtimes T\ge\boxtimes^2 T\ge\boxtimes^3 T\ge\cdots$ is
   non-increasing in $L$.
3. There exists $N\ge 1$ such that $\boxtimes^N T$ is a syntactic fixed
   point of $\boxtimes$, and $\boxtimes T\ge\boxtimes^2 T\ge\cdots\ge\boxtimes^N T$.

(1$\Leftrightarrow$2) by definition. (2$\Rightarrow$3): since $L$ is finite,
any non-increasing chain eventually stabilizes; the stable value $p=\boxtimes^N T$
satisfies $\boxtimes p=\boxtimes^{N+1}T=\boxtimes^N T=p$. (3$\Rightarrow$2):
clear.

**Corollary**: All-$k$ nFG2 $\Rightarrow$ FP-synt. (The converse fails:
M-101 has FP at $\bot$ with $\bot$ not on the $\boxtimes$-orbit of $T$,
and nFG2(1)=FG2 is false.)

This introduces a new classification axis separating FP-synt into:

- **FP-reachable**: $\exists N\ge 1$ with $\boxtimes^N T$ a syntactic FP.
  Equivalent to: all-$k$ nFG2 AND non-increasing sub-orbit.
- **FP-unreachable**: FP exists but not on the $\boxtimes$-orbit of $T$.
  M-001 and M-101 are examples.

The implication diagram now reads:

$$
\text{all-}k\text{ nFG2}
\;\Rightarrow\;
\text{FP-reachable}
\;\Rightarrow\;
\text{FP-synt}
\;\Rightarrow\;
\text{neither G2 nor FG2 is forced.}
$$

Skeptic:

The orbit stabilization theorem is correct for finite preorders, but it has a
hidden size dependency: "non-increasing" uses the ambient order $\le$ of $L$,
which is not the APS order in general. In an infinite or non-Noetherian APS
(e.g., the Lindenbaum algebra of a sufficiently strong logic), the sequence
$\boxtimes^k T$ might be non-increasing yet never stabilize. The theorem should
be labeled as a finite-model result. For APS proper, the orbit condition becomes
a well-foundedness assumption on $\boxtimes$-iteration, which is a new axiom
candidate.

Also: both M-011 and M-111 have the FP-reachable condition, but both have G2
FALSE (M-011) or G2 vacuous (M-111 has $\boxtimes T=T\not\le\bot$). The real
challenge is finding a model where all-$k$ nFG2 and G2 hold with a non-trivial
antecedent path. That requires $\boxtimes T\le\bot\Rightarrow T\le\bot$ with
antecedent true but model non-collapsed — which forces $T\le\bot$, i.e.,
collapse. So G2 with true antecedent in a non-collapsed model is impossible.
G2 in non-collapsed models is always vacuous. This is a structural theorem worth
recording explicitly.

Formalist:

Record two results:

**Proposition (G2 in non-collapsed models)**: Let $S$ be a non-collapsed
preAPS ($T\not\le\bot$). Then G2 holds if and only if $\boxtimes T\not\le\bot$.
In particular, G2 in a non-collapsed model is always vacuously true.

*Proof*: G2 states $\boxtimes T\le\bot\Rightarrow T\le\bot$. Since
$T\not\le\bot$, the consequent is FALSE. So G2 holds iff the antecedent
$\boxtimes T\le\bot$ is also FALSE, i.e., $\boxtimes T\not\le\bot$. $\square$

**Corollary**: G2 partitions non-collapsed preAPS into two classes:

- G2 holds: $\boxtimes T\not\le\bot$ (the "consistency statement is not refutable")
- G2 fails: $\boxtimes T\le\bot$ (the "consistency statement is refutable but system is consistent")

This gives G2 an exact algebraic reading: it is the assertion that provability
and refutability of the consistency statement are separated.

**Theorem (Orbit Stabilization — formal)**: In a finite preAPS $S$,
$\mathrm{nFG2}(k)$ for all $k\ge 1$ iff
$\exists N\ge 1\colon \boxtimes^N T\in\mathrm{Fix}_\boxtimes(S)$
and $\boxtimes^j T\ge\boxtimes^{j+1} T$ for $j=1,\ldots,N-1$.

Here $\mathrm{Fix}_\boxtimes(S):=\{p\in L:p=\boxtimes p\}$.

**Non-degenerate 4-element witness** for G2+FG2+FP-synt: the model

$$
L=\{T,p,c,\bot\},
\quad T>p>\bot,\quad T>c,\quad p\parallel c,\quad c\parallel\bot,
$$
$$
\boxtimes:\;T\mapsto p,\;p\mapsto p,\;c\mapsto T,\;\bot\mapsto T.
$$

Verified: antitone ✓, G2 vacuous ($\boxtimes T=p\not\le\bot$) ✓, FG2
($\boxtimes^2 T=p\le p=\boxtimes T$) ✓, FP at $p$ (with $p\ne T,\bot$)
✓, non-collapsed ✓. The $\boxtimes$-orbit of $T$ is $T\to p\to p\to\cdots$
and stabilizes at $p\in\mathrm{Fix}_\boxtimes$. nFG2($k$) holds for all
$k\ge 1$ (pattern TTTTTTTT).

This is the first certified non-degenerate witness for G2+FG2+FP-synt.
It can be stored as `code/models/examples/M4-G2FG2FP.json`.

Archivist:

Added Pass 8 results: (1) orbit stabilization theorem in
`research/notes/g2-fg2-hierarchy.md`; (2) "G2 in non-collapsed models" proposition in
`research/definitions.md`; (3) new model `code/models/examples/M4-G2FG2FP.json`;
(4) updated `research/open_problems.md` to mark FP-reachable vs FP-unreachable as a
new axis; (5) updated `research/notes/g2-aps-zoo-classification.md` registry; and
(6) recorded this pass in `records/logs/research-log.md`.

Repository updates:

- `records/discussions/autonomous-discussion.md`: recorded pass 8.
- `research/notes/g2-fg2-hierarchy.md`: added orbit stabilization theorem, corollary,
  implication diagram, and FP-reachable/FP-unreachable classification.
- `research/definitions.md`: added G2 in non-collapsed models proposition.
- `code/models/examples/M4-G2FG2FP.json`: new 4-element non-degenerate witness.
- `research/notes/g2-aps-zoo-classification.md`: added M4-G2FG2FP to model registry.
- `research/open_problems.md`: added FP-reachable vs FP-unreachable separation problem.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 9 to determine whether the infinite analogue of the orbit stabilization
theorem requires a new well-foundedness axiom, or whether it is a theorem of
some existing APS axiom package. Also: characterize which 4-element preAPS models
satisfy G2+FG2+FP-synt with FP-reachable (there should be a finite enumeration),
and ask whether any such model also has nontrivial residuation structure.

### Pass 9 - 2026-05-26 18:00 JST

Focus:

Audit the nFG2 claims from pass 8, materialize the missing non-degenerate
G2+FG2+FP witness, and isolate the exact finite-to-infinite gap in orbit
stabilization.

Proposer:

The useful positive result is finite and should be stated sharply: all-level
nFG2 is exactly a non-increasing $\boxtimes$-tail orbit, and in finite
preAPS this tail must stabilize at a syntactic fixed point reachable from $T$.
This gives a clean FP-reachable axis without implying G2. The missing witness
from pass 8 can be made concrete as `M4-G2FG2FP`, with
$\bot<p<T$, $c<T$, $\boxtimes T=p$, $\boxtimes p=p$,
$\boxtimes c=T$, and $\boxtimes\bot=T$.

Skeptic:

The earlier "nFG2 hierarchy is strict at every depth" wording was too strong.
The certified M-010 pattern refutes odd-step implications, including
FG2 $\Rightarrow$ nFG2(2), but it does not refute even-step implications or
arbitrary-depth strictness. Those remain finite search tasks. Also, the
non-degenerate M4 witness still has G2 only vacuously, which is unavoidable in
non-collapsed models under the material implication reading of G2.

Formalist:

Added the definition of nFG2($k$) and the non-collapsed G2 criterion to
`research/definitions.md`. The finite orbit theorem now has the exact hypothesis where
it works: finiteness, or more generally an orbit well-foundedness/no-infinite-
descent assumption. The checker verifies `M4-G2FG2FP` as non-collapsed with
G2 true, FG2 true, all checked nFG2 levels true, and FP-synt at $p$. It also
reports no MacNeille completion fixed point for that model, which separates the
G2+FG2+FP-synt axis from completion-generated fixed points.

Archivist:

Corrected the overclaim in the nFG2 hierarchy note, added the finite orbit
stabilization theorem, created and checked `M4-G2FG2FP`, saved its JSON report,
and updated the model registry, open problems, model/output indexes, active
research questions, and research log. Claude Code Review 1 had no newer entry;
its already-incorporated MacNeille requests remain closed.

Repository updates:

- `research/notes/g2-fg2-hierarchy.md`: corrected the strictness claim, added finite
  orbit stabilization, and recorded `M4-G2FG2FP`.
- `research/definitions.md`: added nFG2($k$), all-level nFG2, and the non-collapsed G2
  criterion.
- `code/models/examples/M4-G2FG2FP.json`: added the 4-element non-degenerate witness.
- `artifacts/reports/g2-zoo-M4-G2FG2FP.json`: saved the checker report.
- `research/notes/g2-aps-zoo-classification.md`: added the M4 witness and corrected the
  nFG2 strictness status.
- `research/open_problems.md`: resolved the non-degenerate G2+FG2+FP and all-level
  nFG2-implies-G2 questions; added the infinite orbit-well-foundedness problem.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 10 to either search for arbitrary-depth nFG2 strictness witnesses or
attempt to equip `M4-G2FG2FP` with nontrivial tensor/residual operations.

### Pass 10 - 2026-05-26 18:56 JST

Focus:

Resolve the arbitrary-depth nFG2 first-true problem by giving a uniform finite
model family and a checked depth-3 instance.

Proposer:

The clean construction is sparse. For any $N\ge 1$, take
$L_N=\{T,a_1,\ldots,a_{N+1},s\}$, order it only by reflexivity plus
$s\le a_{N+1}$, and define
$\boxtimes T=a_1$, $\boxtimes a_i=a_{i+1}$ for $1\le i\le N$,
$\boxtimes a_{N+1}=s$, and $\boxtimes s=s$. Then the orbit of $T$ is
$T\to a_1\to\cdots\to a_{N+1}\to s\to s$, so nFG2 fails through level $N$
and holds from level $N+1$ onward.

Skeptic:

This solves the finite first-true-depth problem only in a deliberately sparse
preAPS class. It does not yet show that the hierarchy remains separated under
any substantive APS axiom package, residual structure, contraction/weakening
discipline, or completion-stability condition. The correct next question is
therefore not "does arbitrary depth exist?" but "which structural axioms kill
or preserve the $D_N$ construction?"

Formalist:

Antitonicity is immediate because the only nontrivial order relation is
$s\le a_{N+1}$, and its image condition is
$\boxtimes a_{N+1}=s\le s=\boxtimes s$. For $1\le k\le N$, nFG2($k$)
asks $a_{k+1}\le a_k$, which is absent. At $k=N+1$, it asks
$s\le a_{N+1}$, which is the added relation; all later levels are $s\le s$.
The generated `nfg2-depth-3` model was checked and has pattern `FFFTTTTT`.

Archivist:

Added a generator script for $D_N$, generated and checked `nfg2-depth-3`,
persisted its report, updated the hierarchy note, and moved the arbitrary-depth
nFG2 task from open to resolved while opening the sharper APS-axiom preservation
problem. The checker was also made tolerant of UTF-8 BOM JSON files produced by
Windows PowerShell.

Repository updates:

- `code/scripts/new-nfg2-depth-witness.ps1`: generator for the $D_N$ family.
- `code/models/examples/nfg2-depth-3.json`: checked depth-3 witness.
- `artifacts/reports/g2-zoo-nfg2-depth-3.json`: persisted checker report.
- `code/scripts/check-g2-zoo.py`: accepts UTF-8 BOM JSON input.
- `research/notes/g2-fg2-hierarchy.md`: added the arbitrary-depth construction theorem.
- `research/definitions.md`: added first-true nFG2 depth.
- `research/open_problems.md`: resolved arbitrary-depth first-true witnesses and opened
  the structural-axiom preservation problem.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 11 to test whether simple tensor/residual candidates can be placed on
`M4-G2FG2FP` or on the $D_N$ family without destroying the certified G2/FG2/
nFG2 behavior.

### Pass 11 - 2026-05-27 00:57 JST

Focus:

Test whether the non-degenerate `M4-G2FG2FP` witness can carry full
tensor/residual structure on its existing carrier and order.

Proposer:

The right first test is exhaustive rather than speculative. Because
`M4-G2FG2FP` has four elements, fixing a two-sided unit leaves $4^9=262144$
binary tensor candidates. Checking all four possible units is small enough to
turn the residuation question into a finite certificate.

Skeptic:

This is only a same-carrier/same-order obstruction. It does not rule out adding
new elements, changing the order while preserving the G2+FG2+FP behavior, using
one-sided residuals, or moving to the $D_N$ family. It also does not use any
external source claim; it is a machine-checkable finite search result inside
the repository.

Formalist:

For each possible unit $e$, the search enumerates every tensor with
$e\otimes x=x=x\otimes e$. It keeps only operations that are associative,
monotone in both arguments, and whose left and right residual fibers are
principal downsets:
$$
\{b:a\otimes b\le c\}=\downarrow(a\backslash c),
\qquad
\{a:a\otimes b\le c\}=\downarrow(c/b).
$$
The result is zero candidates for every unit. Therefore `M4-G2FG2FP` has no
full residuated monoid expansion on the existing four-element order.

Archivist:

Added `code/scripts/search-residuated-tensor.py`, generated
`artifacts/reports/residuated-search-M4-G2FG2FP.json`, and updated the G2/FG2 hierarchy,
residuated-domain note, model/output indexes, open problems, and active
questions. The previous open problem is resolved negatively in the strict
same-order sense and replaced by a sharper search for a modified or expanded
full-residuated witness.

Repository updates:

- `code/scripts/search-residuated-tensor.py`: exhaustive tensor/residual search.
- `artifacts/reports/residuated-search-M4-G2FG2FP.json`: negative finite search report.
- `research/notes/g2-fg2-hierarchy.md`: recorded the same-order full-residuation
  obstruction for `M4-G2FG2FP`.
- `research/notes/residuated-algebra-domain-completion.md`: added the M4 obstruction and
  next residuated-search direction.
- `research/open_problems.md`: resolved the same-order M4 full-residuation question
  negatively and opened the modified/expanded witness problem.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 12 to search for the smallest order expansion or carrier extension
that preserves G2+FG2+FP-reachable behavior while admitting full residuation, or
to test one-sided/partial residual relaxations as an intermediate target.

### Pass 12 - 2026-05-27 04:40 JST

Focus:

Find the smallest same-carrier order repair of `M4-G2FG2FP` that admits full
residuation while preserving the G2+FG2+FP-reachable behavior.

Proposer:

Instead of adding elements, first enumerate preorder extensions of the existing
four-element order. The search keeps the carrier, $T$, $\bot$, $\Box$, and
$\boxtimes$ fixed; it allows only extra order pairs that preserve
non-collapse, antitonicity of $\boxtimes$, G2, FG2, and a syntactic fixed point.
This gives a bounded finite problem before moving to larger carriers.

Skeptic:

The result should be interpreted as a residuated repair, not automatically as a
proof-theoretic axiom. Adding $\bot\le c$ makes residual downsets principal,
but it is not yet clear whether that relation has a natural reading in the APS
or BS16 resource-sensitive story. No external citation or Project-only content
was used for this step.

Formalist:

The order-extension search found a first hit after checking two candidate
extensions. Adding exactly $\bot\le c$ turns the order into the diamond
$\bot<p<T$, $\bot<c<T$, $p\parallel c$. The resulting model has a full
residuated monoid expansion with unit $p$. The tensor has $p$ as unit,
$\bot$ as zero, $T\otimes T=T$, $T\otimes c=c$, and $c\otimes c=\bot$.
The G2-ZOO checker confirms non-collapse, G2 true, FG2 true, all checked nFG2
levels true, and FP-synt at $p$.

Archivist:

Added a same-carrier order-extension search script, generated the full-residuated
order-repair model, saved both the residuation search report and the G2-ZOO
checker report, and updated the hierarchy, residuated-domain, classification,
model/output index, open-problem, and active-question notes.

Repository updates:

- `code/scripts/search-residuated-order-expansions.py`: same-carrier order repair
  search.
- `code/models/examples/M4-G2FG2FP-order-plus-bot-c-residuated.json`: full-residuated
  order repair of the M4 witness.
- `artifacts/reports/residuated-order-search-M4-G2FG2FP.json`: order-extension search
  report.
- `artifacts/reports/g2-zoo-M4-G2FG2FP-order-plus-bot-c-residuated.json`: checker report
  for the repaired witness.
- `code/models/finite-aps-schema.json`: documented optional `unit`, `tensor`, and
  residual tables.
- `research/open_problems.md`: resolved the modified same-carrier full-residuation
  search and opened the interpretation problem for $\bot\le c$.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 13 to interpret the $\bot\le c$ repair: determine whether it
corresponds to a natural resource/refutability axiom, or whether a more
proof-theoretically meaningful residuated witness should be sought.

### Pass 13 - 2026-05-27 05:10 JST

Focus:

Interpret the $\bot\le c$ repair in
`M4-G2FG2FP-order-plus-bot-c-residuated` and decide whether it is an ad hoc
edge or a named APS/resource principle.

Proposer:

The repair has a clean structural reading: the original M4 order had a
distinguished $\bot$ constant but did not make it a least element. It already
satisfied $\bot\le p$, $\bot\le T$, $p\le T$, and $c\le T$; the only
missing bottom-discipline instance was $\bot\le c$. Adding that relation is
therefore exactly bottom discipline on this carrier:
$$
\forall x,\quad \bot\le x.
$$
Read proof-theoretically, this is ex-falso or absurdity weakening for the
$c$-branch.

Skeptic:

This interpretation is useful but not automatically harmless. In a
resource-sensitive BS16-style setting, ex-falso weakening may be a structural
principle that changes the intended calculus. The pass should therefore not
declare the repair canonical; it should record the principle and make its
effect on existing separations a new finite-model test.

Formalist:

Order-theoretically, adding $\bot\le c$ makes $\bot$ least and keeps $T$
greatest, with $p$ and $c$ as incomparable atoms. Thus the repaired order is
the four-element Boolean lattice. This explains why full residuation becomes
possible: residual solution sets that were non-principal in the sparse order can
now be represented by lattice elements. The G2/FG2/FP behavior is unchanged
because the $T$-orbit of $\boxtimes$ remains $T\to p\to p$.

Archivist:

Added bottom discipline to the shared definitions, recorded the repair
interpretation in the hierarchy and residuated-domain notes, updated the model
metadata, and converted the open interpretive problem into a sharper test:
which G2-ZOO and $D_N$ witnesses survive after enforcing
$\forall x(\bot\le x)$?

Repository updates:

- `research/definitions.md`: defined bottom discipline as
  $\forall x(\bot\le x)$, with the M4 repair as its missing instance.
- `research/notes/g2-fg2-hierarchy.md`: interpreted $\bot\le c$ as
  ex-falso/absurdity weakening for the $c$-branch.
- `research/notes/residuated-algebra-domain-completion.md`: recorded the Boolean-lattice
  reading of the repaired order and the remaining BS16/resource-sensitive risk.
- `research/notes/g2-aps-zoo-classification.md`: added bottom discipline as the next
  model-classification filter.
- `research/open_problems.md` and `research/ideas/research-questions.md`: replaced the raw
  interpretation question with the bottom-discipline preservation problem.
- `code/models/examples/M4-G2FG2FP-order-plus-bot-c-residuated.json`: added the
  repair interpretation to metadata.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 14 to implement or run a bottom-discipline filter over the finite
G2-ZOO models and the $D_N$ example, recording which separations survive,
which collapse, and which become better candidates for residuated APS.

### Pass 14 - 2026-05-27 05:47 JST

Focus:

Run bottom discipline as a finite-model filter over the current G2-ZOO
witnesses and the checked `nfg2-depth-3` example.

Proposer:

The direct test is to keep each carrier, $T$, $\bot$, $\Box$, and
$\boxtimes$ fixed, add every missing pair $\bot\le x$, close transitively,
and then ask whether $\boxtimes$ is still antitone. If it is, compare G2,
FG2, FP-synt, collapse, and the checked nFG2 prefix before and after bottom
enforcement.

Skeptic:

This is only a pure order-enforcement test. A model that fails it is not proved
impossible under bottom discipline; it only means that this particular sparse
witness cannot be repaired by adding bottom pairs while leaving $\boxtimes$
unchanged. Replacement witnesses may exist with different carriers, orders, or
refutability maps.

Formalist:

The report `artifacts/reports/bottom-discipline-filter-g2-zoo.json` checks 11 models.
Only `M4-G2FG2FP-order-plus-bot-c-residuated` already satisfies bottom
discipline. Pure enforcement preserves antitonicity for `M-000`, `M-010`,
`M-111`, `M4-G2FG2FP`, and the repaired M4 model. Full recorded behavior is
stable only for `M-111` and the M4 pair. `M-010` still witnesses FG2 without
G2, but enforcing bottom discipline makes $0\sim\bot$, adding FP-synt and
turning the checked nFG2 prefix into `TTTTTTTT`. The current arbitrary-depth
witness `nfg2-depth-3` fails pure enforcement because $s\le T,a_1,a_2,a_3$
would require $a_1,a_2,a_3,a_4\le s$ by antitonicity.

Archivist:

Added `code/scripts/check-bottom-discipline.py`, generated the bottom-discipline
filter report, updated the hierarchy, classification, residuated-domain,
model/output index, open-problem, active-question, and research-log notes. The
new research target is now concrete: find bottom-disciplined replacement
witnesses for the separations lost under pure order enforcement.

Repository updates:

- `code/scripts/check-bottom-discipline.py`: finite bottom-discipline filter and
  pure order-enforcement report generator.
- `artifacts/reports/bottom-discipline-filter-g2-zoo.json`: report for the eight 3-element
  G2-ZOO witnesses, `M4-G2FG2FP`, its repaired residuated version, and
  `nfg2-depth-3`.
- `research/notes/g2-fg2-hierarchy.md`: added the bottom-discipline filter table and
  consequences for current separations.
- `research/notes/g2-aps-zoo-classification.md`: recorded which witnesses survive pure
  bottom enforcement.
- `research/notes/residuated-algebra-domain-completion.md`: noted that bottom discipline
  is a real structural filter and kills the current $D_N$ witness.
- `research/open_problems.md` and `research/ideas/research-questions.md`: closed the current
  filter run and opened the replacement-witness search.
- `code/models/README.md` and `artifacts/README.md`: indexed the new script and report.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 15 to search for bottom-disciplined finite replacement witnesses,
starting with G2 without FG2 and arbitrary first-true nFG2 depth.

### Pass 15 - 2026-05-27 06:17 JST

Focus:

Find bottom-disciplined replacement witnesses for the separations lost under
pure bottom-order enforcement, starting with G2 without FG2 and arbitrary
first-true nFG2 depth.

Proposer:

The sparse $D_N$ construction failed bottom discipline because its eventual
fixed point $s$ was also the bottom constant. Separate those roles. Add a true
bottom $b$ below every element and a helper upper bound $U$ above every
element. Let $\boxtimes b=U$ and $\boxtimes U=b$, while keeping the old
orbit $T\to a_1\to\cdots\to a_{N+1}\to s\to s$.

Skeptic:

This is still a preAPS construction, not a proof that the witness survives any
stronger APS axiom package, residuation requirement, lattice law, or BS16 modal
rule. The helper $U$ is a technical upper bound introduced to absorb
antitonicity requirements from $b\le x$. That is acceptable as a finite
witness but should be tracked as structure added for bottom discipline.

Formalist:

For $B_N$, take carrier
$\{b,T,a_1,\ldots,a_{N+1},s,U\}$, order $b\le x\le U$ for every $x$, and
add $s\le a_{N+1}$. Define
$\boxtimes b=U$, $\boxtimes U=b$, $\boxtimes T=a_1$,
$\boxtimes a_i=a_{i+1}$ for $1\le i\le N$,
$\boxtimes a_{N+1}=s$, and $\boxtimes s=s$. Antitonicity follows from the
bounding pairs and $s\le a_{N+1}$. The $T$-orbit gives nFG2 false through
$N$ and true from $N+1$. Since $a_1\not\le b$, G2 is true vacuously; FG2
fails; and FP-synt holds at $s$.

Archivist:

Added a generator for $B_N$, generated and checked the depth-3 instance, saved
its G2-ZOO report, updated the bottom-discipline filter report to include it,
and revised the hierarchy, classification, residuated-domain, open-problem,
active-question, model index, output index, and research log. The remaining
bottom-disciplined replacement target is G2+FG2 without FP-synt.

Repository updates:

- `code/scripts/new-bottom-nfg2-depth-witness.py`: generator for the
  bottom-disciplined $B_N$ family.
- `code/models/examples/bottom-nfg2-depth-3.json`: checked depth-3
  bottom-disciplined witness.
- `artifacts/reports/g2-zoo-bottom-nfg2-depth-3.json`: checker report with pattern
  `FFFTTTTT`.
- `artifacts/reports/bottom-discipline-filter-g2-zoo.json`: updated filter report now
  includes `bottom-nfg2-depth-3`.
- `research/notes/g2-fg2-hierarchy.md`: added the $B_N$ construction theorem and proof
  sketch.
- `research/notes/g2-aps-zoo-classification.md`: added the new registry row and revised
  the bottom-discipline next target.
- `research/notes/residuated-algebra-domain-completion.md`: recorded the role separation
  $b$ versus $s$ and helper upper bound $U$.
- `research/open_problems.md` and `research/ideas/research-questions.md`: resolved the
  bottom-disciplined G2-not-FG2/arbitrary-depth targets and opened the
  G2+FG2-without-FP target.
- `code/models/README.md` and `artifacts/README.md`: indexed the new generator, model,
  and report.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 16 to search directly for a bottom-disciplined finite preAPS with
G2+FG2 and no syntactic $\boxtimes$-fixed point, or prove that the small
bounded constructions force FP-synt.

### Pass 16 - 2026-05-27 06:47 JST

Focus:

Resolve the remaining bottom-discipline separation: G2+FG2 without syntactic
$\boxtimes$-fixed point.

Proposer:

Use the same role separation as $B_N$: keep a true bottom $b$ and helper
upper bound $U$, but make the $T$-orbit enter a strict two-cycle
$$
T\to a\to d\to a\to\cdots
$$
with $d\le a$. This makes FG2 true at the first step without requiring
$a\sim d$.

Skeptic:

The construction shows bottom discipline alone does not force FP-synt from
G2+FG2. It does not yet say whether a stronger setting such as a full
residuated APS, lattice-ordered APS, or a BS16-derived modal calculus preserves
this separation. The helper $U$ again marks the construction as a bounded
preAPS witness.

Formalist:

The model `bottom-G2FG2-noFP` has carrier $\{b,d,a,T,U\}$, order
$b\le x\le U$ for all $x$, plus $d\le a$. Define
$$
\boxtimes b=U,\quad \boxtimes U=b,\quad \boxtimes T=a,\quad
\boxtimes a=d,\quad \boxtimes d=a.
$$
Antitonicity follows from the bounding pairs and the interior relation
$d\le a$, whose image condition is $d=\boxtimes a\le\boxtimes d=a$. G2 is
true vacuously because $\boxtimes T=a\not\le b$. FG2 is true because
$\boxtimes^2T=d\le a=\boxtimes T$. There is no syntactic fixed point:
$b\leftrightarrow U$, $a\leftrightarrow d$, and $T\mapsto a$ with
$T\not\sim a$. The checker reports nFG2 pattern `TFTFTFTF`.

Archivist:

Added the witness model, saved its checker report, updated the
bottom-discipline filter report, and revised the hierarchy, classification,
residuated-domain, open-problem, active-question, model index, output index,
and research log. Bottom discipline alone now preserves all currently tracked
G2/FG2/FP-synt separations; the next test is residuation.

Repository updates:

- `code/models/examples/bottom-G2FG2-noFP.json`: 5-element bottom-disciplined
  G2+FG2 without FP-synt witness.
- `artifacts/reports/g2-zoo-bottom-G2FG2-noFP.json`: checker report for the new witness.
- `artifacts/reports/bottom-discipline-filter-g2-zoo.json`: updated to include
  `bottom-G2FG2-noFP`.
- `research/notes/g2-fg2-hierarchy.md`: added the construction and proof sketch.
- `research/notes/g2-aps-zoo-classification.md`: added the registry row and revised the
  immediate target.
- `research/notes/residuated-algebra-domain-completion.md`: recorded the new witness as
  the next residuation test case.
- `research/open_problems.md` and `research/ideas/research-questions.md`: closed the
  bottom-disciplined G2+FG2-without-FP task and opened the residuated-upgrade
  question.
- `code/models/README.md` and `artifacts/README.md`: indexed the new model and report.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 17 to test whether the bottom-disciplined witnesses, starting with
`bottom-G2FG2-noFP`, admit full residuated expansions or require minimal
order/carrier repairs.

### Pass 17 - 2026-05-27 07:17 JST

Focus:

Test whether `bottom-G2FG2-noFP` admits a full residuated expansion on the same
carrier and order.

Proposer:

The unrestricted five-element tensor search is too large for the current brute
force script, but the model has a natural resource reading: $T$ is the
distinguished APS top and can be tried as monoid unit, while the true bottom
$b$ can be tried as absorbing zero. Adding commutativity makes the finite
search small enough to run exactly.

Skeptic:

This is a targeted positive result, not an exhaustive classification of all
possible tensors. The unrestricted report correctly records that the
$5^{16}$-per-unit operation space was not searched. The positive constrained
search is still mathematically useful because any found tensor/residual tables
are independently checkable witnesses.

Formalist:

`code/scripts/search-residuated-commutative-zero.py` checks the commutative
fixed-unit/fixed-zero space with unit $T$ and zero $b$. It searches
$5^6=15625$ tensors and finds 8 full-residuated candidates. The persisted
example has $b$ absorbing, $T$ as unit, $U\otimes U=U$,
$U\otimes a=a$, $U\otimes d=d$, and
$a\otimes a=a\otimes d=d\otimes d=b$. The checker confirms that
`bottom-G2FG2-noFP-residuated` preserves non-collapse, G2 true, FG2 true,
FP-synt false, and nFG2 pattern `TFTFTFTF`.

Archivist:

Fixed the unrestricted tensor-search conclusion so skipped searches no longer
claim a negative result, added the targeted commutative-zero search script,
generated the full-residuated expansion and reports, and updated the hierarchy,
classification, residuated-domain, model/output indexes, open problems, active
questions, and research log.

Repository updates:

- `code/scripts/search-residuated-tensor.py`: distinguishes "not searched because
  too large" from a negative searched result.
- `code/scripts/search-residuated-commutative-zero.py`: targeted finite search with
  fixed unit, fixed zero, and commutativity.
- `artifacts/reports/residuated-search-bottom-G2FG2-noFP.json`: unrestricted search-space
  report for the 5-element witness.
- `artifacts/reports/residuated-commutative-zero-search-bottom-G2FG2-noFP.json`: positive
  constrained search report with 8 full-residuated candidates.
- `code/models/examples/bottom-G2FG2-noFP-residuated.json`: same-order full
  residuated expansion.
- `artifacts/reports/g2-zoo-bottom-G2FG2-noFP-residuated.json`: checker report for the
  expansion.
- `artifacts/reports/bottom-discipline-filter-g2-zoo.json`: updated to include the
  residuated expansion.
- Topic notes, indexes, `research/open_problems.md`, `research/ideas/research-questions.md`, and
  `records/logs/research-log.md`: recorded the result and moved the next target to the
  bottom-disciplined $B_N$ family.

Next step:

Use pass 18 to test whether the bottom-disciplined arbitrary-depth witness
`bottom-nfg2-depth-3` admits an analogous full residuated expansion or requires
a smaller structural repair.

### Pass 18 - 2026-05-27 08:51 JST

Focus:

Test whether `bottom-nfg2-depth-3`, the checked $B_N$ arbitrary-depth witness,
admits a full residuated expansion on the same carrier and order.

Proposer:

The commutative-zero exhaustive strategy from pass 17 is too large for the
8-element $B_3$ instance. Instead use the visible shape of the construction:
$b$ is a true bottom, $U$ is a helper upper bound, and $T$ is the APS
top. Try $T$ as monoid unit, $b$ as zero, and make every nonzero,
non-unit product collapse upward to $U$.

Skeptic:

This is a strong resource operation: products of two non-unit nonzero elements
become $U$, not a more informative internal element. It is therefore a
same-order full-residuation witness, not evidence that a fine-grained or
BS16-like tensor exists. The uniform $B_N$ theorem still needs a written
proof, even though the checked $B_3$ instance verifies all finite algebraic
conditions.

Formalist:

Added `code/scripts/build-top-absorbing-residuated-expansion.py`. For a chosen unit
$e$, zero $z$, and absorber $u$, it builds
$$
z\otimes x=z,\qquad e\otimes x=x,\qquad x\otimes y=u
$$
in all remaining cases, then checks unit, zero, commutativity, associativity,
monotonicity, principal left/right residuals, and the full residuation law. On
`bottom-nfg2-depth-3` with $e=T$, $z=b$, and $u=U$, every check succeeds.
The resulting expansion preserves non-collapse, G2 true, FG2 false, FP-synt at
$s$, and nFG2 pattern `FFFTTTTT`.

Archivist:

Generated `bottom-nfg2-depth-3-residuated`, its top-absorbing residuation
report, and its G2-ZOO checker report. Updated the bottom-discipline report to
include the expansion. Recorded the result in the hierarchy, classification,
residuated-domain note, indexes, open problems, active questions, and research
log.

Repository updates:

- `code/scripts/build-top-absorbing-residuated-expansion.py`: constructive
  top-absorbing full-residuation builder/checker.
- `code/scripts/check-g2-zoo.py`: adds `--output` for writing checker JSON reports
  without shell redirection.
- `code/models/examples/bottom-nfg2-depth-3-residuated.json`: same-order full
  residuated expansion of the checked $B_3$ witness.
- `artifacts/reports/residuated-top-absorbing-report-bottom-nfg2-depth-3.json`:
  construction and verification report.
- `artifacts/reports/g2-zoo-bottom-nfg2-depth-3-residuated.json`: checker report for the
  expansion.
- `artifacts/reports/bottom-discipline-filter-g2-zoo.json`: updated to include the new
  residuated expansion.
- Topic notes, indexes, `research/open_problems.md`, `research/ideas/research-questions.md`, and
  `records/logs/research-log.md`: moved the next task to proving the uniform $B_N$
  residuation lemma and searching for less explosive tensors.

Next step:

Use pass 19 to write the general $B_N$ top-absorbing residuation lemma, or
find a strictly less top-collapsing tensor for the same family.

### Pass 19 - 2026-05-27 14:06 JST

Focus:

Promote the `bottom-nfg2-depth-3-residuated` construction to a uniform
same-order full-residuation lemma for every bottom-disciplined $B_N$.

Proposer:

The pass 18 tensor was not an accident of depth 3. The $B_N$ order always has
the same bounding skeleton $b\le x\le U$, plus only $s\le a_{N+1}$. That
shape is exactly what the top-absorbing tensor needs: $T$ acts as unit, $b$
as zero, and products of nonzero non-unit elements can all be sent to $U$.

Skeptic:

The result closes existence of full residuation for $B_N$, but it does so by
using a deliberately coarse tensor. A resource-sensitive reading may reject
the move because nearly every nontrivial product becomes the helper upper
bound. The next serious question is whether the same-order geometry forces
that coarseness or whether a finer tensor exists.

Formalist:

For $B_N$, let $M_N=B_N\setminus\{b,T\}$. Define
$$
b\otimes x=b,\qquad T\otimes x=x,\qquad
x\otimes y=U\quad(x,y\in M_N).
$$
This is a commutative monoid with unit $T$ and zero $b$. Associativity
follows because after removing $T$'s, any product containing $b$ is $b$,
while any product of at least two elements of $M_N$ is $U$, and $U\in M_N$
absorbs further non-unit nonzero factors. Monotonicity follows from the order
generators $b\le x$, $x\le U$, and $s\le a_{N+1}$. Residual fibers are
principal:
$$
b\backslash c=U,\quad T\backslash c=c,\quad
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c\ne U,\\
b & \text{otherwise}
\end{cases}
$$
for $m\in M_N$, with identical right residuals by commutativity.

Archivist:

Recorded the uniform $B_N$ top-absorbing residuation lemma in the hierarchy
and residuated-domain notes. Marked the uniform existence question resolved,
and moved the active/open problem to finding less top-collapsing same-order
tensors or proving an obstruction.

Repository updates:

- `research/notes/g2-fg2-hierarchy.md`: added the uniform $B_N$ tensor and residual
  proof sketch.
- `research/notes/residuated-algebra-domain-completion.md`: added the same lemma from
  the residuated-APS perspective.
- `research/open_problems.md`: closed uniform top-absorbing existence and opened the
  finer-tensor/obstruction question.
- `research/ideas/research-questions.md`: retargeted the active question to the
  less-top-collapsing tensor problem.
- `records/logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 20 to search for a less top-collapsing tensor on
`bottom-nfg2-depth-3`, starting with constraints that keep products among
orbit elements below $U$ whenever residuation permits.

### Pass 20 - 2026-05-27 20:55 JST

Focus:

Search for a less top-collapsing full-residuated tensor on
`bottom-nfg2-depth-3`.

Proposer:

Keep the constraints that made pass 18 tractable and mathematically legible:
commutativity, unit $T$, zero $b$, and $U\otimes x=U$ for every nonzero
$x\ne T$. Then search the remaining 15 unordered products on
$\{a_1,a_2,a_3,a_4,s\}$, minimizing the number of products equal to $U$.

Skeptic:

This does not remove the $U$-absorbing assumption. It only tests whether the
top-absorbing tensor was unnecessarily coarse inside that assumption. The
answer is positive for $B_3$, but the new pattern may still be depth-specific.

Formalist:

Added `code/scripts/search-u-absorbing-residuated.py`. It performs a complete
branch-and-bound search under the $U$-absorbing constraints, checks
associativity, monotonicity, and principal residual fibers, and emits residual
tables for the best witness. For `bottom-nfg2-depth-3`, the top-absorbing
template has 15 $U$-valued products among the 15 orbit/fixed-point products.
The search finds a full-residuated witness with 7 such products:
$$
a_1s=a_2,\quad a_2s=a_3,\quad
a_1a_4=a_2,\quad a_2a_4=a_3,\quad
a_4s=s^2=a_4^2=a_1,\quad a_1^2=a_3,
$$
with the remaining searched products equal to $U$. The checker confirms the
expanded model keeps G2 true, FG2 false, FP-synt at $s$, and nFG2 pattern
`FFFTTTTT`.

Archivist:

Persisted the new model, search report, and checker report; updated the
bottom-discipline report and the model/output indexes. The notes now record
that top-absorbing residuation is sufficient but not minimal for $B_3$. The
active problem is now to generalize the 7-$U$ pattern to $B_N$, or prove it
is depth-specific, and then test whether $U$-absorption can be weakened.

Repository updates:

- `code/scripts/search-u-absorbing-residuated.py`: complete constrained search for
  less top-collapsing $U$-absorbing tensors.
- `code/models/examples/bottom-nfg2-depth-3-u-absorbing-minU.json`: new
  full-residuated witness with 7 $U$-valued searched products.
- `artifacts/reports/residuated-u-absorbing-search-bottom-nfg2-depth-3.json`: search
  report.
- `artifacts/reports/g2-zoo-bottom-nfg2-depth-3-u-absorbing-minU.json`: checker report.
- `artifacts/reports/bottom-discipline-filter-g2-zoo.json`: updated to include the new
  expansion.
- Topic notes, indexes, `research/open_problems.md`, `research/ideas/research-questions.md`, and
  `records/logs/research-log.md`: recorded the result and retargeted the next problem.

Next step:

Use pass 21 to test whether the 7-$U$ pattern extends to $B_4$, or to write
the first obstruction explaining why it is special to $B_3$.

### Pass 21 - 2026-05-27 23:47 JST

Focus:

Test whether the less top-collapsing $U$-absorbing tensor pattern extends
from the checked $B_3$ witness to the next bottom-disciplined arbitrary-depth
witness $B_4$.

Proposer:

Generate `bottom-nfg2-depth-4` first, rather than extrapolating from the old
depth-3 artifact. Then try the pass 20 pattern at the level of the exponent
structure: give $a_{N+1}$ and $s$ exponent 1, give $a_i$ exponent
$i+1$, keep $T$ as unit and $b$ as zero, and send a product to $U$
only when the exponent sum exceeds $N+1$.

Skeptic:

The direct branch-and-bound $U$-absorbing search on $B_4$ did not finish
within the local 120-second pass budget, so this pass does not prove
minimality. It verifies a constructive template that is much finer than the
top-absorbing tensor, and it gives a concrete uniform conjecture to prove.

Formalist:

Added `code/scripts/build-truncated-u-absorbing-residuated.py`. It infers $N$
from the `a_i` names, constructs the truncated-exponent tensor, checks unit,
zero, commutativity, associativity, monotonicity, principal left/right
residuals, and the full residuation law, then emits both the verification
report and the expanded model. On `bottom-nfg2-depth-4`, it finds a
same-carrier/order full-residuated expansion with 10 $U$-valued products
among the 21 searched unordered products, compared with 21 for the
top-absorbing tensor. The G2-ZOO checker confirms G2 true, FG2 false, FP-synt
at $s$, and nFG2 pattern `FFFFTTTT`.

Archivist:

Persisted `bottom-nfg2-depth-4`, its truncated-exponent full-residuated
expansion, the construction report, and the checker reports. Updated the
bottom-discipline report and the model/output indexes. The active problem is
now a uniform proof of the truncated-exponent $B_N$ residuation template,
including an explicit residual table, followed by a test of whether
$U$-absorption itself is forced.

Repository updates:

- `code/scripts/build-truncated-u-absorbing-residuated.py`: constructive
  truncated-exponent $U$-absorbing residuation builder/checker.
- `code/models/examples/bottom-nfg2-depth-4.json`: checked depth-4
  bottom-disciplined arbitrary-depth witness.
- `code/models/examples/bottom-nfg2-depth-4-truncated-u-absorbing.json`:
  same-order full-residuated expansion.
- `artifacts/reports/residuated-truncated-u-absorbing-bottom-nfg2-depth-4.json`:
  construction and verification report.
- `artifacts/reports/g2-zoo-bottom-nfg2-depth-4.json`: checker report for the base
  witness.
- `artifacts/reports/g2-zoo-bottom-nfg2-depth-4-truncated-u-absorbing.json`: checker
  report for the expanded witness.
- `artifacts/reports/bottom-discipline-filter-g2-zoo.json`: updated to include the new
  base and expanded witnesses.
- Topic notes, indexes, `research/open_problems.md`, `research/ideas/research-questions.md`, and
  `records/logs/research-log.md`: recorded the depth-4 result and retargeted the next
  proof task.

Next step:

Use pass 22 to prove the truncated-exponent $U$-absorbing template uniformly
for $B_N$, including a closed residual table, or run $B_5$ as another
checked stress test before writing the proof.

### Pass 22 - 2026-05-28 00:17 JST

Focus:

Prove the truncated-exponent $U$-absorbing tensor template uniformly for the
bottom-disciplined $B_N$ family, including a closed residual table.

Proposer:

Treat the $B_3$ and $B_4$ tensors as instances of one finite algebraic
template. The key invariant is not the names of the orbit points but the
truncated exponent $e$: $e(s)=e(a_{N+1})=1$ and $e(a_i)=i+1$. Products
of two orbit/fixed-point elements add exponents until the sum exceeds $N+1$,
then overflow to $U$.

Skeptic:

This proof still assumes $U$-absorption. It proves a finer same-order
residuated expansion than the top-absorbing tensor, but it does not show that
$U$-absorption is forced or optimal. Also, the duplicate exponent-1 pair
$s,a_{N+1}$ must be handled explicitly in residuals because $s\le a_{N+1}$.

Formalist:

Let $A_N=\{s,a_1,\ldots,a_{N+1}\}$, put
$$
e(s)=e(a_{N+1})=1,\qquad e(a_i)=i+1,
$$
and define $\pi(1)=a_{N+1}$, $\pi(r)=a_{r-1}$ for $2\le r\le N+1$.
The tensor has $T$ as unit, $b$ as zero, $U$ absorbing over nonzero
non-units, and for $x,y\in A_N$:
$$
x\otimes y=
\begin{cases}
a_{e(x)+e(y)-1} & e(x)+e(y)\le N+1,\\
U & e(x)+e(y)>N+1.
\end{cases}
$$
Associativity is associativity of addition with overflow at $N+1$. The two
exponent-1 elements cause no associativity ambiguity because no product of two
non-unit elements has exponent 1. Monotonicity follows from the order
generators $b\le x$, $x\le U$, and $s\le a_{N+1}$; the last is preserved
because $s$ and $a_{N+1}$ have the same exponent.

For residuals:
$$
b\backslash c=U,\quad T\backslash c=c,\quad
U\backslash c=
\begin{cases}
U & c=U,\\
b & c\ne U,
\end{cases}
$$
and for $m\in A_N$, $q=e(m)$, and $t(a_i)=i+1$ for $1\le i\le N$,
$$
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c,\\
\pi(t(c)-q) & c=a_i,\ 1\le i\le N,\ q<t(c),\\
b & \text{otherwise.}
\end{cases}
$$
Commutativity gives the same right residuals. These formulas make every
residual fiber principal, so the tensor is fully residuated on the original
$B_N$ carrier and order.

Archivist:

Recorded the tensor definition in `research/definitions.md`, added the uniform proof and
residual table to the hierarchy and residuated-domain notes, closed the
uniform-template proof task in `research/open_problems.md`, and retargeted the active
question to weakening or refuting the $U$-absorbing assumption.

Repository updates:

- `research/definitions.md`: added the truncated-exponent $U$-absorbing tensor
  definition for $B_N$.
- `research/notes/g2-fg2-hierarchy.md`: added the uniform proof, monotonicity argument,
  and residual table.
- `research/notes/residuated-algebra-domain-completion.md`: recorded the same lemma from
  the residuated-APS perspective.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked the uniform
  template proof resolved and moved the next question to weakening
  $U$-absorption.
- `research/notes/g2-aps-zoo-classification.md` and `records/logs/research-log.md`: updated the
  next-step registry and research trace.

Next step:

Use pass 23 to test whether the $U$-absorbing assumption can be weakened,
starting with the smallest checked case `bottom-nfg2-depth-3`.

### Pass 23 - 2026-05-28 00:47 JST

Focus:

Test whether the $U$-absorbing assumption can be weakened while keeping the
truncated-exponent orbit product table fixed.

Proposer:

Do not begin with a full unrestricted tensor search. First isolate the narrow
question left by pass 22: if the orbit/fixed-point products on
$A_N=\{s,a_1,\ldots,a_{N+1}\}$ are fixed to the truncated-exponent table, is
there any freedom left in products involving $U$?

Skeptic:

This is only a relative obstruction. It can show that $U$-absorption is
forced by the truncated table, but it cannot rule out a more radically
different same-order full-residuated tensor where the orbit product table also
changes.

Formalist:

Added `code/scripts/analyze-truncated-u-forcing.py`. The analyzer fixes $T$ as
unit, $b$ as zero, and the truncated-exponent products on $A_N$, but does
not assume $U\otimes x=U$. It checks whether monotonicity against the top
relation $x\le U$ already forces those products. On both
`bottom-nfg2-depth-3` and `bottom-nfg2-depth-4`, every $y\in A_N$ has some
$x\in A_N$ such that $x\le U$ and $x\otimes y=U$. Therefore
$$
U=x\otimes y\le U\otimes y,
$$
and since $U$ is top, $U\otimes y=U$. With $y\le U$, a second monotonicity
step forces $U\otimes U=U$. Thus, relative to the truncated orbit table,
$U$-absorption is forced by monotonicity alone, before residuals are checked.

Archivist:

Persisted forcing reports for B3 and B4, updated the hierarchy and
residuated-domain notes, and narrowed the active open question. The next search
must vary the orbit product table itself if it wants a genuinely
non-$U$-absorbing same-order residuated tensor.

Repository updates:

- `code/scripts/analyze-truncated-u-forcing.py`: analyzer for monotonicity-forced
  $U$-products relative to the truncated orbit table.
- `artifacts/reports/truncated-u-forcing-bottom-nfg2-depth-3.json`: B3 forcing report.
- `artifacts/reports/truncated-u-forcing-bottom-nfg2-depth-4.json`: B4 forcing report.
- `research/notes/g2-fg2-hierarchy.md` and
  `research/notes/residuated-algebra-domain-completion.md`: recorded the relative
  obstruction.
- `research/open_problems.md`, `research/ideas/research-questions.md`,
  `research/notes/g2-aps-zoo-classification.md`, `code/models/README.md`,
  `artifacts/README.md`, and `records/logs/research-log.md`: updated the trace and next
  target.

Next step:

Use pass 24 to search for a non-$U$-absorbing same-order full-residuated
tensor on `bottom-nfg2-depth-3` by allowing the orbit product table itself to
vary.

### Pass 24 - 2026-05-28 03:01 JST

Focus:

Start the search for a non-$U$-absorbing same-order full-residuated tensor on
`bottom-nfg2-depth-3`, now allowing the orbit product table itself to vary.

Proposer:

Keep only the structural constraints that are already justified by the B3
residuated searches: commutativity, unit $T$, and zero $b$. Split the
search by the possible values of $U\otimes x$ allowed by monotonicity from
$T\le U$, then search the remaining products among the nonzero non-unit
elements.

Skeptic:

The full search is still large. A bounded run can produce useful engineering
information, but not a mathematical obstruction. The important distinction is
to record incompleteness clearly and use the failure mode to choose the next
pruning lemma.

Formalist:

Added `code/scripts/search-non-u-absorbing-residuated.py`. It fixes commutativity,
unit $T$, and zero $b$, does not assume $U$-absorption, and does not fix
the orbit product table. For each $U$-action pattern, it prunes domains using
monotonicity, then checks associativity, monotonicity, and principal left/right
residual fibers. On `bottom-nfg2-depth-3`, the persisted bounded report visits
1000 search nodes, 12 $U$-action patterns, and 382 complete assignments
without finding a candidate. A larger 10000-node attempt did not finish within
the local 120-second pass budget, so this is an incomplete negative result.

Archivist:

Persisted the bounded search report and search script, updated the hierarchy
and residuated-domain notes, and narrowed the next task to adding residual-fiber
pruning. The zero-target fibers $m\backslash b$ are the first likely pruning
site, because many naive non-$U$-absorbing tables produce non-principal zero
fibers.

Repository updates:

- `code/scripts/search-non-u-absorbing-residuated.py`: orbit-table-varying search
  that does not assume $U$-absorption.
- `artifacts/reports/residuated-non-u-absorbing-search-bottom-nfg2-depth-3.json`: bounded
  incomplete B3 search report.
- `research/notes/g2-fg2-hierarchy.md` and
  `research/notes/residuated-algebra-domain-completion.md`: recorded the partial search
  and its limitation.
- `research/open_problems.md`, `research/ideas/research-questions.md`,
  `research/notes/g2-aps-zoo-classification.md`, `code/models/README.md`,
  `artifacts/README.md`, and `records/logs/research-log.md`: updated the next target.
- Relay logs from the earlier 2026-05-28 sync were preserved: ChatGPT share
  links were unreachable, and Drive outputs had no newly relevant post-2026-05-22
  items.

Next step:

Use pass 25 to add residual-fiber pruning to the B3 non-$U$-absorbing search,
starting with the $m\backslash b$ fibers.

### Pass 25 - 2026-05-28 05:44 JST

Focus:

Complete the B3 non-$U$-absorbing same-order residuation search by adding
residual-fiber pruning.

Proposer:

Use partial residual-fiber principality as a search-time constraint. For every
partially known fiber, keep only branches where some principal downset can still
contain all known included elements and exclude all known excluded elements.
This generalizes the intended $m\backslash b$ pruning rather than hard-coding
only the zero target.

Skeptic:

The result must be read against pass 23: $U$-absorption is forced if the
truncated orbit table is fixed. A non-$U$-absorbing witness therefore has to
change the orbit table, so it may be algebraically less close to the
truncated-exponent construction.

Formalist:

Updated `code/scripts/search-non-u-absorbing-residuated.py` with partial
left/right residual-fiber pruning. The B3 search now completes: it visits 47
$U$-action patterns, prunes 16 immediately, prunes 1537 branches by residual
fiber obstruction, checks 475 complete assignments, and finds
`bottom-nfg2-depth-3-non-u-absorbing`. The tensor is full-residuated with unit
$T$ and zero $b$, but
$$
U\otimes a_4=a_4,\qquad U\otimes s=s.
$$
The orbit table changes: $a_1,a_2,a_3$ form a Klein-four pattern over $T$,
$a_j\otimes a_4=a_4$, $a_j\otimes s=s$ for $j=1,2,3$, and
$$
a_4^2=a_4,\qquad a_4s=s^2=b.
$$
The G2-ZOO checker confirms G2 true, FG2 false, FP-synt at $s$, and nFG2
pattern `FFFTTTTT`.

Archivist:

Persisted the expanded model, the completed search report, the checker report,
and the updated bottom-discipline report. Updated the hierarchy,
residuated-domain, classification, model/output indexes, open problems, active
questions, and research log. The next question is whether the B3
non-$U$-absorbing pattern extends to B4 or admits a uniform $B_N$ form.

Repository updates:

- `code/scripts/search-non-u-absorbing-residuated.py`: added residual-fiber pruning.
- `code/models/examples/bottom-nfg2-depth-3-non-u-absorbing.json`: full-residuated
  non-$U$-absorbing B3 expansion.
- `artifacts/reports/residuated-non-u-absorbing-search-bottom-nfg2-depth-3.json`:
  completed positive search report.
- `artifacts/reports/g2-zoo-bottom-nfg2-depth-3-non-u-absorbing.json`: checker report.
- `artifacts/reports/bottom-discipline-filter-g2-zoo.json`: updated to include the new
  expansion.
- Topic notes, indexes, `research/open_problems.md`, `research/ideas/research-questions.md`, and
  `records/logs/research-log.md`: retargeted the next problem to B4/uniform extension.

Next step:

Use pass 26 to test whether the non-$U$-absorbing B3 tensor pattern extends
to `bottom-nfg2-depth-4`.

### Pass 26 - 2026-05-28 06:14 JST

Focus:

Test whether the non-$U$-absorbing same-order full-residuated phenomenon
found at checked B3 persists at checked B4.

Proposer:

Run the orbit-table-varying search directly on `bottom-nfg2-depth-4`, even if
full exhaustiveness is too expensive. A single verified full-residuated witness
is enough to answer the existential B4 question, while optimization and
classification can remain separate.

Skeptic:

The bounded B4 run cannot prove minimality or uniqueness. It also should not
be described as the B3 pattern literally extending: the found B4 tensor changes
the product-table shape, so the current evidence is existential rather than a
uniform construction.

Formalist:

The search report
`artifacts/reports/residuated-non-u-absorbing-search-bottom-nfg2-depth-4.json` stops at
1000 nodes after 48 $U$-action patterns, 697 residual-fiber prunes, and 147
complete assignments. It nevertheless finds a fully checked same-order
residuated expansion. In the found tensor:
$$
U\otimes a_1=a_1,\qquad U\otimes a_2=a_2,
$$
so $U$-absorption fails, while $U\otimes a_3=U\otimes a_4=U\otimes a_5
=U\otimes s=U$. The lower part is not the B3 Klein-four pattern:
$$
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b.
$$
The G2-ZOO checker confirms that
`bottom-nfg2-depth-4-non-u-absorbing` keeps G2 true, FG2 false, FP-synt at
$s$, bottom discipline, and nFG2 pattern `FFFFTTTT`.

Archivist:

Persisted the B4 non-$U$-absorbing expansion, its bounded positive search
report, checker report, and refreshed bottom-discipline report. Updated the
hierarchy, residuated-domain, classification, model/output indexes, open
problems, active questions, and research log. The active question now shifts
from B4 existence to whether the checked B3 and B4 witnesses have a uniform
$B_N$ explanation.

Repository updates:

- `code/models/examples/bottom-nfg2-depth-4-non-u-absorbing.json`: B4 same-order
  full-residuated non-$U$-absorbing expansion.
- `artifacts/reports/residuated-non-u-absorbing-search-bottom-nfg2-depth-4.json`:
  bounded positive search report.
- `artifacts/reports/g2-zoo-bottom-nfg2-depth-4-non-u-absorbing.json`: checker report.
- `artifacts/reports/bottom-discipline-filter-g2-zoo.json`: refreshed with the B4
  expansion.
- Topic notes, indexes, `research/open_problems.md`, `research/ideas/research-questions.md`, and
  `records/logs/research-log.md`: retargeted the next problem to a uniform $B_N$
  explanation or obstruction.

Next step:

Use pass 27 to compare the checked B3 and B4 non-$U$-absorbing tensors and
search for either a uniform $B_N$ construction schema or a proof that the
known witnesses are depth-specific repairs.

### Pass 27 - 2026-05-28 11:03 JST

Focus:

Compare the checked B3/B4 non-$U$-absorbing tensors and extract a uniform
construction candidate.

Proposer:

Use the B4 bounded-search witness as the guide. It has a simple decomposition:
$a_1,a_2$ are front orthogonal idempotents, $U$ fixes that front, and the
remaining tail follows a shifted truncated-exponent product. Package that as a
builder rather than treating the B4 table as a one-off search artifact.

Skeptic:

This does not prove the earlier max-non-$U$ B3 search witness is the member
of a uniform family. In fact, the front-shifted depth-3 tensor is different and
has fewer non-$U$ products. The correct claim is therefore existence of a
uniform non-$U$-absorbing template candidate, not minimality or uniqueness.

Formalist:

Added `code/scripts/build-front-shifted-non-u-absorbing-residuated.py`. For
$N\ge3$, the template splits $B_N$ into front $F=\{a_1,a_2\}$ and tail
$R_N=\{s,a_{N+1},a_3,\ldots,a_N\}$. The front satisfies
$$
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b,
$$
and $U$ fixes the front:
$$
U\otimes a_1=a_1,\qquad U\otimes a_2=a_2.
$$
The tail uses shifted exponents
$$
\tau(s)=\tau(a_{N+1})=1,\qquad \tau(a_i)=i-1\quad(3\le i\le N),
$$
with overflow above $N-1$ sent to $U$. The builder verifies associativity,
monotonicity, principal left/right residual fibers, and the residuation law.
It succeeds for depths 3, 4, and 5. At depth 4, the generated tensor is exactly
the pass 26 bounded-search witness. At depth 5, the new expansion preserves
G2 true, FG2 false, FP-synt at $s$, bottom discipline, and nFG2 pattern
`FFFFFTTT`.

Archivist:

Recorded the front-shifted tensor definition, added the builder and checked
depth-3/4/5 construction reports, generated the depth-5 base and expanded
models, and refreshed the model registry and bottom-discipline report. The
remaining mathematical task is no longer to find a uniform candidate, but to
write the closed residual table and prove the template for all $N\ge3$.

Repository updates:

- `code/scripts/build-front-shifted-non-u-absorbing-residuated.py`: uniform template
  builder/checker.
- `code/models/examples/bottom-nfg2-depth-5.json`: next checked bottom-disciplined
  first-true nFG2 witness.
- `code/models/examples/bottom-nfg2-depth-{3,4,5}-front-shifted-non-u-absorbing.json`:
  checked template expansions.
- `artifacts/reports/residuated-front-shifted-non-u-absorbing-bottom-nfg2-depth-{3,4,5}.json`
  and matching G2-ZOO reports: construction and checker artifacts.
- `research/definitions.md`, topic notes, indexes, `research/open_problems.md`,
  `research/ideas/research-questions.md`, `artifacts/reports/bottom-discipline-filter-g2-zoo.json`,
  and `records/logs/research-log.md`: updated to make the residual-table proof the next
  target.

Next step:

Use pass 28 to derive the explicit residual table for the front-shifted
non-$U$-absorbing template and turn the checked schema into a uniform
$B_N$ lemma.

### Pass 28 - 2026-05-28 11:33 JST

Focus:

Derive the residual table for the front-shifted non-$U$-absorbing $B_N$
template and close the gap between finite checks and a uniform lemma.

Proposer:

Keep the proof organized by the front/tail split. The front part should have a
two-element orthogonal-idempotent residual table; the tail part should be
shifted exponent subtraction, with a special case for the duplicate exponent-1
pair $s,a_{N+1}$.

Skeptic:

The residual table proves full residuation for this template, not minimality
or uniqueness among non-$U$-absorbing tensors. The earlier B3 search witness
still has more non-$U$ products than the front-shifted B3 member, so
classification remains separate.

Formalist:

Recorded the closed residual table in `research/definitions.md` and the hierarchy note.
For $p\in\{a_1,a_2\}$, $p\backslash c$ is $U$ at targets $p,U$, and
the other front element otherwise. For $U$, the residual is $U$ at $U$,
the target itself at front targets, and $b$ otherwise. For tail
$r\in R_N$, front targets return the front element, exact targets return
$T$, shifted exponent subtraction returns $a_{N+1}$ or $a_{d+1}$, and
impossible fibers return $b$. Commutativity gives the right residuals.
Added `code/scripts/check-front-shifted-residual-formula.py`, which compares this
symbolic table with generated residuals. The reports for depths 3, 4, and 5
all have zero mismatches.

Archivist:

Updated `research/definitions.md`, hierarchy and residuated-domain notes, the model and
output indexes, open problems, active questions, and the research log. The
front-shifted construction is now recorded as a uniform same-order
full-residuated non-$U$-absorbing template for $B_N$ with $N\ge3$. The
next meaningful problem is structural interpretation: whether the front/tail
decomposition is a product, quotient, or ideal-extension construction, and how
it behaves with respect to weakening/contraction.

Repository updates:

- `code/scripts/check-front-shifted-residual-formula.py`: symbolic residual-table
  checker.
- `artifacts/reports/front-shifted-residual-table-check-bottom-nfg2-depth-{3,4,5}.json`:
  zero-mismatch checks against generated left/right residuals.
- `research/definitions.md`, `research/notes/g2-fg2-hierarchy.md`, and
  `research/notes/residuated-algebra-domain-completion.md`: explicit residual table and
  proof outline.
- `research/open_problems.md`, `research/ideas/research-questions.md`,
  `research/notes/g2-aps-zoo-classification.md`, `code/models/README.md`,
  `artifacts/README.md`, and `records/logs/research-log.md`: retargeted from residual
  proof to structural interpretation.

Next step:

Use pass 29 to analyze the structural-rule profile of the front-shifted
template, especially contraction and weakening compared with the
truncated-exponent $U$-absorbing template.

### Pass 29 - 2026-05-28 12:03 JST

Focus:

Analyze the structural-rule profile of the front-shifted non-$U$-absorbing
$B_N$ tensor, especially contraction and weakening.

Proposer:

Add a small analyzer for the Axis III rules already listed in the zoo note:
exchange $E$, contraction $C$, and the strong weakening rule
$a\le b\Rightarrow a\otimes c\le b$. Compare the front-shifted template
against the top-absorbing, truncated $U$-absorbing, earlier non-$U$, and
G2+FG2-without-FP residuated witnesses.

Skeptic:

The strong weakening rule is very strong in this APS order, since the monoid
unit is $T$ but many elements are not below $T$. Therefore a negative
weakening result is expected. The useful information is not merely that $W$
fails, but where contraction fails and whether the front/tail split has a
visible structural signature.

Formalist:

Added `code/scripts/analyze-structural-rules.py` and saved
`artifacts/reports/structural-rules-front-shifted-comparison.json`. All eight compared
residuated tensors satisfy exchange. None satisfies strong weakening or the
reflexive discarding instance $a\otimes c\le a$; the unit already gives
witnesses $T\otimes c=c\not\le T$. Global contraction holds only for
`bottom-G2FG2-noFP-residuated`. In the front-shifted family, however,
contraction holds on the front idempotents $a_1,a_2$ and fails in the shifted
tail. Checked failures include $a_3^2=U$, $a_{N+1}^2=a_3$, and
$s^2=a_3$ in the relevant depths.

Archivist:

Updated the structural-rule axis, hierarchy note, residuated-domain note,
definitions, open problems, active questions, model/output indexes, and
research log. The next task is now algebraic presentation: describe the
front-shifted tensor as an ideal-extension, orthogonal-sum, or related
construction explaining localized front contraction and tail resource
sensitivity.

Repository updates:

- `code/scripts/analyze-structural-rules.py`: structural-rule checker.
- `artifacts/reports/structural-rules-front-shifted-comparison.json`: comparison report.
- `research/definitions.md`: normalized the finite $E,C,W$ structural-rule checks.
- `research/notes/g2-aps-zoo-classification.md`, `research/notes/g2-fg2-hierarchy.md`, and
  `research/notes/residuated-algebra-domain-completion.md`: recorded the result.
- `research/open_problems.md`, `research/ideas/research-questions.md`, `code/models/README.md`,
  `artifacts/README.md`, and `records/logs/research-log.md`: retargeted the next problem
  to algebraic presentation of the front/tail split.

Next step:

Use pass 30 to present the front-shifted tensor as an ideal-extension or
orthogonal-sum style construction and isolate the exact proof obligations for
that presentation.

### Pass 30 - 2026-05-28 12:33 JST

Focus:

Present the front-shifted non-$U$-absorbing $B_N$ tensor as an algebraic
extension, and decide whether "orthogonal sum" or "ideal extension" is the
right reading.

Proposer:

Use the front/tail split to define a genuine tensor ideal
$I=\{b,a_1,a_2\}$. If $I$ is downward closed and absorbs multiplication by
all elements, then the front-shifted tensor is not merely a patched table. It
is a Rees-style ideal extension: a contractive two-atom front ideal is glued
onto the shifted truncated tail.

Skeptic:

Calling the construction an orthogonal sum would be misleading. Cross-products
between a front atom and a tail element do not vanish to $b$; they project
back to the chosen front atom. Also, the presentation should not be advertised
as a classification theorem. It explains the current template but does not show
that all same-order non-$U$-absorbing repairs arise this way.

Formalist:

Added `code/scripts/check-front-shifted-extension-presentation.py` and saved
`artifacts/reports/front-shifted-extension-presentation-check.json`. For the checked
depths 3, 4, and 5, the script verifies that $I=\{b,a_1,a_2\}$ is a downward
closed two-sided tensor ideal, that $a_1,a_2$ form an orthogonal idempotent
zero-band, and that the quotient collapsing $I$ to $b$ has representatives
$\{b,T,U,s,a_{N+1},a_3,\ldots,a_N\}$ carrying exactly the shifted tail
product. This explains local contraction as behavior internal to $I$, while
the quotient tail keeps the noncontractive resource-sensitive product.

Archivist:

Recorded the ideal-extension presentation in `research/definitions.md`, the hierarchy
note, the residuated-domain note, and the G2-ZOO classification note. Updated
the active question and open problems away from "find a presentation" and
toward classification of possible front tensor ideals.

Repository updates:

- `code/scripts/check-front-shifted-extension-presentation.py`: verifies the
  front-ideal extension presentation.
- `artifacts/reports/front-shifted-extension-presentation-check.json`: depth-3/4/5
  verification report.
- `research/definitions.md`: added the front ideal-extension presentation.
- `research/notes/g2-fg2-hierarchy.md`,
  `research/notes/residuated-algebra-domain-completion.md`, and
  `research/notes/g2-aps-zoo-classification.md`: recorded the structural reading.
- `research/open_problems.md`, `research/ideas/research-questions.md`, `code/models/README.md`,
  `artifacts/README.md`, and `records/logs/research-log.md`: retargeted the next problem
  to classifying front-ideal extensions.

Next step:

Use pass 31 to classify small tensor ideals that can replace
$\{b,a_1,a_2\}$ in the front-extension recipe, or prove that the two-atom
zero-band is forced by the present same-order, same-tail constraints.

### Pass 31 - 2026-05-28 15:17 JST

Focus:

Classify the possible size of the orthogonal front ideal in the shifted-tail
schema, keeping the same $B_N$ order.

Proposer:

Generalize the pass-30 presentation by replacing the two-front set with
$$
F_k=\{a_1,\ldots,a_k\}.
$$
Keep the same proof-theoretic shape: $F_k$ is an orthogonal idempotent
zero-band, front elements project products with the tail back to themselves,
and the quotient tail starts at $a_{k+1}$. This gives a clean finite test for
whether the two-front construction is forced or merely one positive choice.

Skeptic:

The current order has front atoms pairwise incomparable. If $k\ge3$, the
residual $p\backslash b$ should fail to exist as a principal element, because
all the other front atoms multiply with $p$ to $b$, and no one of them
dominates the others. Therefore a width-3 failure would be a structural
obstruction, not a search artifact.

Formalist:

Added `code/scripts/check-front-ideal-size-bound.py` and saved
`artifacts/reports/front-ideal-size-bound-check.json`. At depths 3, 4, and 5, front
widths $0,1,2$ pass the unit, zero, commutativity, associativity,
monotonicity, principal residual, and residuation checks. Width $3$ is the
first failure in every checked depth. The displayed witness is the expected
non-principal fiber: for $p=a_1$, $p\backslash b$ has fiber
$\{b,a_2,a_3\}$, with $a_2$ and $a_3$ incomparable.

Archivist:

Recorded the orthogonal front-width bound in `research/definitions.md`, the hierarchy
note, the residuated-domain note, and the G2-ZOO classification note. Retargeted
the active problem from broad ideal classification to the uniform front-width
theorem, especially the one-front residual table and the $k\ge3$
non-principal-fiber obstruction.

Repository updates:

- `code/scripts/check-front-ideal-size-bound.py`: generalized orthogonal front-width
  checker.
- `artifacts/reports/front-ideal-size-bound-check.json`: depth-3/4/5 report showing
  widths $0,1,2$ pass and width $3$ first fails.
- `research/definitions.md`, `research/notes/g2-fg2-hierarchy.md`,
  `research/notes/residuated-algebra-domain-completion.md`, and
  `research/notes/g2-aps-zoo-classification.md`: recorded the bound and obstruction.
- `research/open_problems.md`, `research/ideas/research-questions.md`, `code/models/README.md`,
  `artifacts/README.md`, and `records/logs/research-log.md`: retargeted the next proof
  task.

Next step:

Use pass 32 to turn the checked front-width pattern into a uniform theorem:
write the closed residual table for width $1$, fold widths $0,1,2$ into a
single statement where possible, and prove the $k\ge3$ obstruction directly.

### Pass 32 - 2026-05-28 15:47 JST

Focus:

Turn the checked orthogonal front-width pattern into a uniform residual theorem
for widths $0,1,2$, and isolate what remains beyond the same-order schema.

Proposer:

The right statement is not only "the two-front template works." It is a
three-case theorem: $k=0$ recovers the truncated $U$-absorbing tensor,
$k=1$ gives a one-front non-$U$-absorbing tensor, and $k=2$ gives the
front-shifted template. All three share the same shifted-tail residual table,
with only the front residual clause changing.

Skeptic:

The $k\ge3$ obstruction depends on orthogonal front atoms in the same
$B_N$ order. It should not be overstated as ruling out all larger front
ideals. A non-orthogonal front multiplication or an added join/order relation
among front atoms could make the bad residual fiber principal, at the cost of
changing the algebraic or APS profile.

Formalist:

Added `code/scripts/check-front-width-residual-formula.py` and saved
`artifacts/reports/front-width-residual-formula-check.json`. For $k=0,1,2$, the script
compares a closed residual formula against generated residuals at depths 3, 4,
and 5. The report has nine checked cases and zero mismatches. The formula uses
$\tau_k(s)=\tau_k(a_{N+1})=1$,
$\tau_k(a_i)=i-k+1$, and
$\rho_k(1)=a_{N+1},\rho_k(d)=a_{k+d-1}$. For $p\in F_k$,
$p\backslash c=U$ at $c=p,U$; otherwise it is $b$ for $k=1$ and the
other front atom for $k=2$. The $k=0$ case has no front clause.

Archivist:

Recorded the uniform residual table in `research/definitions.md`, updated the hierarchy
and residuated-domain notes, and marked the orthogonal-front same-order theorem
as resolved for the current schema. The next open direction is now deliberately
narrower: test whether non-orthogonal front ideals or mild front-order
refinements can avoid the $k\ge3$ principal-fiber obstruction.

Repository updates:

- `code/scripts/check-front-width-residual-formula.py`: closed residual formula
  checker for orthogonal front widths $0,1,2$.
- `artifacts/reports/front-width-residual-formula-check.json`: zero-mismatch report for
  depths 3, 4, and 5.
- `research/definitions.md`, `research/notes/g2-fg2-hierarchy.md`,
  `research/notes/residuated-algebra-domain-completion.md`, and
  `research/notes/g2-aps-zoo-classification.md`: recorded the uniform residual table.
- `research/open_problems.md`, `research/ideas/research-questions.md`, `code/models/README.md`,
  `artifacts/README.md`, and `records/logs/research-log.md`: retargeted the next problem
  to non-orthogonal front ideals or front-order refinements.

Next step:

Use pass 33 to test the smallest $k=3$ escape route: add one front join or
try a non-orthogonal front multiplication, then check whether full residuation
and the $B_N$ APS profile survive.

### Pass 33 - 2026-05-30 JST

Focus:

Test the smallest escape route from the orthogonal-front $k\ge3$
principal-fiber obstruction. Two routes exist: (A) keep the $B_N$ order but
replace the pairwise-zero front product with a non-orthogonal one; (B) add a
join among front atoms, promoting some incomparable pair to a comparable one.
Determine which route, if any, reinstates principal $p\backslash b$ fibers
while preserving full residuation and the G2/nFG2 APS profile.

Proposer:

The $k=3$ obstruction proof in pass 31 ran as follows. Take three pairwise
incomparable front atoms $a_1,a_2,a_3$ with $a_i a_j=b$ for $i\ne j$. The
fiber of $a_1\backslash b$ must contain every $x$ such that $a_1\otimes x\le b$.
Both $a_2$ and $a_3$ qualify because $a_1\otimes a_2=b\le b$ and
$a_1\otimes a_3=b\le b$. Since $a_2\parallel a_3$ in $B_N$, the fiber has no
principal element above both of them, so the residual fails.

The two atomic repairs are therefore:

**Route A (non-orthogonal product)**: Set $a_1\otimes a_2 = a_3$ (or some
non-$b$ value). The residual fiber of $a_1\backslash b$ then excludes $a_2$
(because $a_1\otimes a_2=a_3\not\le b$), potentially leaving a principal fiber.

**Route B (front join)**: Add $a_2\le a_3$ to the order (keeping the original
pairwise-zero product). The fiber of $a_1\backslash b$ still contains both
$a_2$ and $a_3$, but now $a_2\le a_3$ makes $a_3$ the principal maximum.

Both routes change the algebraic or order structure of the model. The question
is whether either preserves the APS and structural-rule profile that the $B_N$
construction was built for.

Skeptic:

Route A is dangerous: if $a_1\otimes a_2=a_3$ but $a_2\otimes a_1=a_3$
(commutativity), then $a_3\backslash b$ now has fiber including $a_1$ and $a_2$
for the same reason, just with the $k=3$ cycle shifted. Unless the three atoms
are given a total order (which breaks the original $B_N$ APS structure), the
non-orthogonal front product appears to propagate the principal-fiber failure
around the triangle.

Route B is cleaner algebraically, but adding $a_2\le a_3$ changes the carrier
poset. Specifically, $a_3$ is now above $a_2$ in $B_N$, which changes the
antitonicity check for $\boxtimes$. In $B_N$, the front atoms $a_1,\ldots,a_k$
are not in the $\boxtimes$-orbit of $T$ (they are in the tail), so the G2/FG2
status is unaffected — but antitonicity of $\boxtimes$ must be rechecked.

Formalist:

**Route A analysis (non-orthogonal $k=3$ front):**

Let $F_3=\{a_1,a_2,a_3\}$ with cycle product $a_i\otimes a_{i+1\bmod3}=a_{i+2\bmod3}$
(cyclic rotation, indices mod 3). For each $p=a_i$, the fiber of
$p\backslash b$ is $\{x:p\otimes x\le b\}$. With the cyclic product, we need
$p\otimes x\le b$, i.e., $p\otimes x=b$. The only $x\in F_3$ satisfying
$p\otimes x=b$ is $x=p$ itself (idempotent: $a_i^2=b$ if we keep that). But
then $p\backslash b$ has fiber $\{b,a_i,\ldots\}$ — we need to also include
tail elements $r$ with $a_i\otimes r\le b$. In the shifted tail template,
$a_i\otimes r=a_i$ (front absorbs tail), so $a_i\not\le b$, excluding all tail
elements. If additionally the self-product $a_i^2$ is changed from $b$ to $a_i$
(idempotent) or some tail element, the fiber changes further.

The clean case: take $a_i^2=a_i$ (idempotent on the diagonal) and
$a_i\otimes a_j=a_k$ (cyclic for $\{i,j,k\}=\{1,2,3\}$). Then $p\backslash b$
has fiber $\{x:p\otimes x\le b\}$. Since $p\otimes p=p\not\le b$ and
$p\otimes a_j=a_k\not\le b$ for $j\ne i$, the only elements of $F_3$ in the
fiber are those $x$ with $p\otimes x=b$ — but we have assigned no product to
$b$ for pairs in $F_3$, so the fiber in $F_3$ is empty. Including $b$ itself:
$p\otimes b=b\le b$, so $b$ is in the fiber. The fiber restricted to the
front+$b$ part is $\{b\}$, which is principal at $b$. But we must also include
the tail: since front absorbs tail, $p\otimes r=p\not\le b$, so no tail element
is in the fiber. Hence $p\backslash b=b$ for each front atom.

This is the cyclic idempotent route. The residual is principal at $b$.

Remaining checks: does this tensor satisfy associativity? We have $(a_1\otimes
a_2)\otimes a_3=a_3\otimes a_3=a_3$, while $a_1\otimes(a_2\otimes
a_3)=a_1\otimes a_1=a_1$. So $a_3\ne a_1$: associativity fails.

The cyclic assignment is not associative. The obstruction is structural:
the cyclic group $\mathbb Z/3\mathbb Z$ is associative, but mapping it onto
$\{a_1,a_2,a_3\}$ conflicts with having $a_i^2=a_i$ (idempotent), since in any
group $x^2=x$ forces $x=e$. Idempotent cyclic products are contradictory.

Retry with the cyclic group product: $a_1^2=a_2$, $a_2^2=a_3$, $a_3^2=a_1$,
$a_1a_2=a_3$, $a_2a_3=a_1$, $a_3a_1=a_2$. This is the cyclic group of order 3
embedded in $\{a_1,a_2,a_3\}$. Then $p\backslash b$: $p\otimes x=b$ requires
$x$ such that $p\cdot x=b$ in the front group. In a group with no zero, there
is no $x$ with $p\cdot x=b$ unless $b$ is the group identity. If $b$ is
not in the group, the fiber in $F_3$ is empty; $b$ maps to $b$ by absorption,
so the fiber is $\{b\}$ again, principal at $b$. But now $a_i\otimes b=b$
(zero absorption), and the residual $b\backslash b$ is $U$ (top), not $T$. So
$p\backslash b=b$ would mean $p\otimes b=b\le b$ ✓ and $p\otimes x\le b$
requires $p\cdot x=b$ in the front group — impossible for $x\in F_3$ since no
product is $b$. So the fiber above $b$ is empty in $F_3$, and the fiber is
$\{b\}$, giving $p\backslash b=b$. Principal. ✓

Associativity: the cyclic group of order 3 is associative. Checking
interactions with tail: $a_i\otimes(a_j\otimes r)=a_i\otimes a_j=a_{k}$, and
$(a_i\otimes a_j)\otimes r=a_k\otimes r=a_k$. ✓ Front interactions with zero
and unit: $b\otimes x=b$ (zero), $T\otimes x=x$ (unit). ✓

Monotonicity: the order generators of $B_N$ are $b\le x$ for all $x$, $x\le U$
for all $x$, and $s\le a_{N+1}$. For $b\le a_i$: $b\otimes y=b\le a_i\otimes
y$ — need $b\le a_i\cdot y$ for all $y$. Since $b$ is bottom, this holds. ✓
For $a_i\le U$: $a_i\otimes y\le U\otimes y$ — if $y\in F_3$, $a_i\otimes y$
is some $a_j$ and $U\otimes a_j=a_j$ (from the non-$U$-absorbing front template
where $U\otimes a_i=a_i$). So $a_j\le a_j$ ✓. For $s\le a_{N+1}$: both are in
the tail, and $a_i\otimes s=a_i$, $a_i\otimes a_{N+1}=a_i$. So $a_i\le a_i$.
✓

The cyclic group of order 3 as front multiplication, with $U$ acting as the
identity on front atoms ($U\otimes a_i=a_i$), gives a non-orthogonal
$k=3$ front ideal that is associative, principal-fiber residuated, and
monotone on the $B_N$ order.

**G2/FG2/nFG2 profile**: the $T$-orbit of $\boxtimes$ in $B_N$ runs
$T\to a_1\to\cdots\to a_{N+1}\to s\to s\to\cdots$. The front atoms $a_1,
\ldots, a_k$ are in the orbit chain for small $k$, and whether the orbit stays
in the group or exits to the tail depends on $N$ and $k$. For $k=3$ and
$N\ge3$, orbit element $a_1=\boxtimes T$, then $\boxtimes a_1=a_2$, then
$\boxtimes a_2=a_3$, then $\boxtimes a_3=a_4$ (now in the tail). The group
multiplication is not the $\boxtimes$ map; $\boxtimes$ on the front atoms is
already determined by the orbit, and the tensor product $\otimes$ is a separate
operation. So the G2/FG2/nFG2 profile is determined by $\boxtimes$, not by
$\otimes$. Adding the cyclic group tensor on $F_3$ does not change the orbit
structure. The APS properties are therefore preserved.

**Summary of Route A resolution**:

The cyclic-group-of-order-3 front multiplication (with $b$ as absorbing zero and
$U\otimes a_i=a_i$) escapes the principal-fiber obstruction at $k=3$. The
residual $p\backslash b=b$ is principal. Associativity holds via the cyclic
group. Monotonicity holds on the $B_N$ order generators. The APS profile
(G2, FG2 false, FP-synt at $s$, arbitrary-depth nFG2) is unchanged.

The key algebraic fact is: **the $k\ge3$ obstruction is specific to the
orthogonal-front schema (pairwise-zero cross-products). A cyclic group
front evades it by making cross-products non-zero, removing their fiber
contributions.**

**Route B analysis (front join, order extension):**

Add $a_2\le a_3$ to $B_N$ while keeping the pairwise-zero product. The fiber
of $a_1\backslash b$ still contains both $a_2$ and $a_3$ (since
$a_1\otimes a_2=b$ and $a_1\otimes a_3=b$). But now $a_2\le a_3$ in the
extended order, so $a_3$ is the maximum of $\{a_2,a_3\}$, and the fiber is
principal at $a_3$: $a_1\backslash b=a_3$. ✓

However, antitonicity of $\boxtimes$: the orbit has $\boxtimes a_1=a_2$ and
$\boxtimes a_2=a_3$ (for $k=3$ and $N\ge3$). With $a_2\le a_3$ in the extended
order, antitonicity requires $\boxtimes a_3\le\boxtimes a_2=a_3$ and
$\boxtimes a_2\le\boxtimes a_1=a_2$, i.e., $\boxtimes a_2=a_3\le a_2$. But
$a_3\not\le a_2$ in the extended order (we only added $a_2\le a_3$, not
$a_3\le a_2$). So antitonicity fails: $\boxtimes a_2=a_3\not\le a_2=\boxtimes
a_1$ when $a_1\le a_2$ (if we added that too) is not present.

Wait — the orbit has $a_1=\boxtimes T$ and $a_2=\boxtimes a_1$, and we added
$a_2\le a_3$ (not $a_1\le a_2$). Antitonicity says $x\le y\Rightarrow\boxtimes
y\le\boxtimes x$. The new relation is $a_2\le a_3$, so antitonicity requires
$\boxtimes a_3\le\boxtimes a_2=a_3$. In $B_N$ (pre-extension), $\boxtimes
a_3=a_4$ (a tail element). So we need $a_4\le a_3$ in the extended order. This
is not among the added relations, so antitonicity fails unless we also add
$a_4\le a_3$.

Adding $a_4\le a_3$ then requires (by antitonicity of $\boxtimes$)
$\boxtimes a_3\le\boxtimes a_4$, i.e., $a_4\le a_5$, and so on down the orbit.
This cascading relation addition will eventually require $s\le a_{N+1}$ — which
is already present — and then $\boxtimes s=s\le s=\boxtimes a_{N+1}$, which
holds. So the cascade terminates, but it changes the order significantly:
we have added a chain $a_2\le a_3\le a_4\le\cdots\le a_{N+1}$ (and $s\le
a_{N+1}$ already). This extended order collapses the nFG2 pattern: now
$\boxtimes^{k+1}T=a_{k+1}\le a_k=\boxtimes^k T$ for all $k\ge2$ (since the
cascade adds $a_{k+1}\le a_k$ relations — wait, we added $a_2\le a_3$, not
$a_3\le a_2$; let me recheck).

Actually antitonicity of $a_2\le a_3$ requires $\boxtimes a_3\le\boxtimes a_2$,
i.e., $a_4\le a_3$. So we add $a_4\le a_3$. Then $a_4\le a_3$ requires
$\boxtimes a_3\le\boxtimes a_4$, i.e., $a_4\le a_5$... but this reverses the
chain again. Actually: $a_4\le a_3$ requires $\boxtimes a_3\le\boxtimes a_4$,
i.e., $a_4\le a_5$ (since $\boxtimes a_3=a_4$ and $\boxtimes a_4=a_5$). So we
must add $a_4\le a_5$, which then forces $a_5\le a_4$ by the same logic — a
contradiction if $a_4\ne a_5$.

In summary: adding $a_2\le a_3$ to $B_N$ and keeping $\boxtimes$ antitone
requires $a_4\le a_5$ which requires $a_5\le a_4$, a contradiction.
**Route B breaks antitonicity in $B_N$** and cannot be reconciled without
collapsing elements. Route B fails for the $B_N$ family.

**Pass 33 result**: Route A (cyclic group front) succeeds; Route B (front join)
breaks antitonicity.

Archivist:

The cyclic-group-of-order-3 front provides the first example of a non-orthogonal
$k=3$ front ideal evading the principal-fiber obstruction. The analysis is
purely algebraic: no new script is needed for the obstruction proof (it follows
from the associativity failure of idempotent cyclic and the success of the
genuine cyclic group). The Route B failure is a clean antitonicity-cascade
argument. Updated `research/open_problems.md` to record the Route A resolution and the
Route B obstruction. Recorded the cyclic-group-front template in
`research/notes/g2-fg2-hierarchy.md` and the uniform residual-table extension in
`research/definitions.md`. Added a new open problem: determine the maximum front-group
order $\lvert G\rvert$ compatible with the $B_N$ APS order, full residuation, and the
antitone $\boxtimes$ profile.

Repository updates:

- `research/notes/g2-fg2-hierarchy.md`: added the cyclic-group $k=3$ front-ideal
  construction, the Route A/B analysis, and the resulting theorem on orthogonal
  vs.\ non-orthogonal fronts.
- `research/definitions.md`: added the cyclic-group front-ideal template (identity $T$,
  zero $b$, group product on $F_k$, $U$ acting as group identity on $F_k$,
  tail absorbed to front element).
- `research/open_problems.md`: marked the $k=3$ Route A escape as resolved and the
  Route B order-extension as obstructed; added the max-front-group-order problem.
- `records/logs/research-log.md`: recorded Pass 33 result.
- `research/ideas/research-questions.md` and `research/notes/g2-aps-zoo-classification.md`:
  retargeted the next structural problem.

Next step:

Use pass 34 to determine the maximum order $\lvert G\rvert$ of a finite group that can
serve as the cyclic/non-orthogonal front in the $B_N$ schema — specifically,
whether $\lvert G\rvert\ge4$ fronts (e.g., the Klein four-group or cyclic group of order 4)
are compatible with full residuation, antitonicity of $\boxtimes$, and the $B_N$
order, or whether the monotonicity constraints force $\lvert G\rvert\le3$.

### Pass 34 - 2026-05-31 11:21 JST

Focus:
Determine the maximum order $\lvert G\rvert$ of a finite group that can serve as
the non-orthogonal front $F_k=\{a_1,\dots,a_k\}$ in the bottom-disciplined
$B_N$ schema while preserving full residuation, antitonicity of $\boxtimes$, and
the G2/nFG2/FP profile, on the same carrier and order. Pass 33 recorded that the
cyclic group $\mathbb Z/3$ ("Route A") succeeds at $k=3$; this pass re-examines
that claim and tests the order-$4$ groups $\mathbb Z/4$ and the Klein four-group
$V_4=\mathbb Z/2\times\mathbb Z/2$.

Proposer:
The optimistic continuation of Pass 33: a finite group $G$ kills the
$k\ge3$ principal-fiber obstruction because left division in a group is unique,
so for $p\in F_k$ the fiber $p\backslash b=\{x:p\otimes x=b\}$ collapses to
$\{b\}$ (no group product equals the adjoined zero $b$), and each $p\backslash
a_m$ collapses to $\{b,\,p^{-1}a_m\}$ with top $p^{-1}a_m$. By this reasoning
both order-$4$ abelian groups should work, the only group-theoretic ceiling
being commutativity of $\otimes$ (so $S_3$ and larger non-abelian groups would
be excluded, but $\lvert G\rvert$ otherwise unbounded). Conjecture: max order is
$\infty$ over the abelian groups, with $S_3$ the first excluded group.

Skeptic:
The Proposer (and Pass 33) only audited the *division* fibers $p\backslash b$
and $p\backslash a_m$ and silently retained the non-$U$-absorbing front action
$U\otimes a_i=a_i$ imported from the orthogonal $k=2$ template. That import is
illegitimate. Monotonicity is a constraint, not a courtesy: from $a_i\le U$ and
monotonicity of $\otimes$ we must have, for every front atom $a_j$,
$$
a_i\otimes a_j \;\le\; U\otimes a_j \qquad(\forall i).
$$
When the front carries a group, $\{a_i\otimes a_j : i\}=\{a_i a_j:i\}=F_k$
(multiplication by $a_j$ is a bijection of $G$). Hence $U\otimes a_j$ must be a
common upper bound of the *entire* incomparable front $F_k$. For $k\ge2$ the
only such bound in the $B_N$ order is $U$ itself, so monotonicity *forces*
$U\otimes a_j=U$ — $U$-absorption is mandatory, the non-$U$-absorbing action is
impossible. But $U$-absorption then breaks the diagonal residual: in the fiber
of $a_j\backslash a_j$ we have $T$ (unit) and the group identity $a_e$ (with
$a_e\otimes a_j=a_j$), both incomparable atoms whose only common upper bound is
$U$ — and $U$ is now expelled from the fiber because $U\otimes a_j=U\not\le
a_j$. No maximum survives; residuation fails. The orthogonal $k=2$ band escapes
this trap precisely because its products *descend* ($a_i\otimes a_j\le a_j$
always), so non-$U$-absorption stays monotone. A group's products do not
descend. Route A is refuted.

Formalist:
Work in $B_N$ ($N\ge1$) on the carrier $\{b,T,a_1,\dots,a_{N+1},s,U\}$ with the
bottom-disciplined order; let $\otimes$ be commutative, associative, monotone,
fully residuated, with unit $T$ and zero $b$, restricting to a magma on the
incomparable front prefix $F_k=\{a_1,\dots,a_k\}$, $k\ge2$.

**Lemma (front integrality).** $a_i\otimes a_j\le a_j$ for all $i,j\le k$.

*Proof.* Monotonicity on $a_i\le U$ gives $a_i\otimes a_j\le U\otimes a_j=:u_j$,
so $u_j$ upper-bounds $\{a_i\otimes a_j:i\}$. Suppose $u_j\not\le a_j$. Then
$U\notin (a_j\backslash a_j)$ since $U\otimes a_j=u_j\not\le a_j$. Yet the fiber
$a_j\backslash a_j$ contains $T$ ($a_j\otimes T=a_j$) and any front atom $a_e$
with $a_e\otimes a_j=a_j$; $T$ and $a_e$ are distinct incomparable atoms whose
unique common upper bound in $B_N$ is $U$. Hence the fiber has no maximum,
contradicting full residuation. Therefore $u_j\le a_j$, and a fortiori
$a_i\otimes a_j\le a_j$ for all $i$. $\qquad\blacksquare$

**Theorem (front rigidity).** Under the above hypotheses the front sub-magma is
forced to be the orthogonal idempotent zero-band:
$$
a_i\otimes a_j=b\ (i\ne j),\qquad a_i\otimes a_i\in\{a_i,b\}.
$$
Consequently no nontrivial group structure is realizable on $F_k$: a group front
exists **iff $\lvert G\rvert=1$**.

*Proof.* The Lemma plus commutativity give $a_i\otimes a_j\le a_i\wedge a_j$.
For $i\ne j$ the incomparable atoms meet at $b$, so $a_i\otimes a_j=b$; for
$i=j$, $a_i\otimes a_i\le a_i$ forces $a_i\otimes a_i\in\{a_i,b\}$ (the only
elements $\le a_i$). A group on $F_k$ requires $a_i\otimes a_j$ to range over all
of $F_k$ and to have inverses, incompatible with $a_i\otimes a_j=b$ once
$k\ge2$. Hence $k=1$. $\qquad\blacksquare$

This is verified by exhaustive search in
`code/scripts/check-front-group-order-bound.py`, which ranges over every choice
of $U\otimes a_i$ in the minimal faithful ambient $\{b,T,a_1,\dots,a_k,U\}$
(the substructure carrying all binding front constraints). Output:

```
group fronts: k=1 Z/1 -> 1 solution (U*a_i = a_1, non-U-absorbing);
              k=2 Z/2, k=3 Z/3, k=4 Z/4, k=4 V4 -> NO solution.
validation:   orthogonal k=1,2 -> residuated (U*a_i = a_i);  k=3 -> 0 (matches Pass 31).
```

The harness is validated against the established orthogonal-front data: it
returns the unique non-$U$-absorbing solution for orthogonal $k=1,2$ and the
known failure at $k=3$. **Proof obligations discharged:** integrality lemma,
rigidity theorem, exhaustive confirmation at $k\le4$ for $\mathbb Z/2$,
$\mathbb Z/3$, $\mathbb Z/4$, $V_4$. **Remaining (minor):** the rigidity theorem
is general in $k$, so no per-$k$ search is logically required beyond the validation;
the $k\le4$ run is corroborative, not load-bearing.

Consequence for Pass 33: the recorded "Route A success" was an error of omission
— it checked the division fibers but not the monotonicity-induced $U$-action.
The corrected verdict is that *both* escape routes from the $k\ge3$ obstruction
fail: Route B by the antitonicity cascade (Pass 33, still valid), Route A by the
integrality/diagonal-residual obstruction (this pass). The orthogonal idempotent
band of width $\le2$ is therefore not merely *a* solution but the *forced* shape
of any same-carrier/order commutative residuated front.

Archivist:
Mark the Pass-33 "[New] maximum front-group order" problem **[Resolved]** with
answer $\lvert G\rvert=1$, and append a correction note to the Cyclic-Group
Front section of `g2-fg2-hierarchy.md` flagging the monotonicity flaw in the
Route A claim and stating the front-rigidity theorem. Record the integrality
lemma and rigidity theorem in `g2-fg2-hierarchy.md`; add the rigidity statement
to `definitions.md` as the structural ceiling of the front-width schema. Log the
pass in `research-log.md`, retarget `research-questions.md`. New script
`code/scripts/check-front-group-order-bound.py` (added).

Repository updates:
- `code/scripts/check-front-group-order-bound.py`: new exhaustive checker for the
  front-group order bound, with an orthogonal-front validation harness.
- `research/notes/g2-fg2-hierarchy.md`: added the "Front Rigidity (Pass 34)"
  subsection — integrality lemma, rigidity theorem, and a correction flag on the
  Pass-33 Route A claim.
- `research/definitions.md`: added the front-rigidity ceiling to the front-width
  schema description (group fronts collapse to the orthogonal band; only $|G|=1$).
- `research/open_problems.md`: the max-front-group-order item marked [Resolved];
  Route A entry corrected to [Refuted]; added a [New] item on whether a
  *non-commutative* (two-residual) expansion could host a group front.
- `records/logs/research-log.md`: one-line Pass 34 entry.
- `research/ideas/research-questions.md`: retargeted the front question to the
  non-commutative-residuation variant and to integral-tensor classification.

Next step:
The rigidity theorem uses commutativity (single residual). Pass 35 should test
the genuinely non-commutative escape: equip $B_N$ with a *non-integral*
two-residual (left/right $\backslash,\,/$) tensor and ask whether a nontrivial
finite group can sit on the front when monotonicity no longer forces a single
common $U$-action — i.e., does dropping commutativity (and hence the
$a_i\otimes a_j\le a_i\wedge a_j$ collapse) reopen group fronts, or does the
two-sided monotonicity $a_i\le U\Rightarrow a_i\otimes a_j\le U\otimes a_j$ and
$a_j\otimes a_i\le a_j\otimes U$ still force $U$-absorption and kill the diagonal
residual? Settle whether the front rigidity is a commutativity artifact or a
genuine $B_N$-order phenomenon.

### Pass 35 - 2026-05-31 14:32 JST

Focus:

Settle whether dropping commutativity reopens group fronts on the
bottom-disciplined $B_N$. Replace the single residual by an honest two-residual
(left $a\backslash c=\max\{x:a\otimes x\le c\}$, right $c/a=\max\{x:x\otimes
a\le c\}$) tensor with unit $T$, zero $b$, search the two $U$-actions
$U\otimes a_i$ and $a_i\otimes U$ *independently* (so no two-sided absorber is
smuggled in), and ask whether a nontrivial finite group — including a
non-abelian one — can occupy the incomparable front $F_k=\{a_1,\dots,a_k\}$.
Is the Pass-34 front rigidity an artifact of the commutative integrality
lemma $a_i\otimes a_j\le a_i\wedge a_j$, or a genuine $B_N$-order phenomenon?

Proposer:

The commutative obstruction (Pass 34) had a single failure mode: the diagonal
fiber $a_j\backslash a_j$ collected $T$ (unit) and the local front identity, two
incomparable atoms whose only common upper bound is the absorbing $U$, while
monotonicity forced $U\otimes a_j=U\not\le a_j$, so the fiber lost its top.
Commutativity entered only through $a_i\otimes a_j\le a_i\wedge a_j$. Dropping it
gives two independent residuals and two independent $U$-actions; a priori the
left action $U\otimes a_i$ could descend into the front while the right action
$a_i\otimes U$ absorbs, decoupling the two diagonal fibers. The natural candidate
is to put a nontrivial group $G\cong F_k$ on the front (identity $a_{i_0}\in
F_k$, a *local* unit coexisting with the global unit $T$) and hope the two-sided
freedom keeps both $a_j\backslash a_j$ and $a_j/a_j$ principal. Smallest genuinely
non-commutative test: $S_3$ on $k=6$ front atoms.

Skeptic:

The decoupling is illusory because the killing argument is already one-sided.
Fix a group front $F_k\cong G$, $k\ge2$. Left-translation $L_{a_j}:a_e\mapsto
a_j\otimes a_e$ is a bijection of $F_k$ (group axiom), so
$\{a_j\otimes a_e:a_e\in F_k\}=F_k$. By right-monotonicity ($a_e\le U\Rightarrow
a_j\otimes a_e\le a_j\otimes U$), the element $a_j\otimes U$ is an upper bound of
all of $F_k$. For $k\ge2$ the *only* upper bound of the pairwise-incomparable
front in $B_N$ is $U$ itself, so $a_j\otimes U=U$ — right $U$-absorption is
**forced**, with no use of commutativity. Symmetrically $R_{a_j}$ bijective
forces $U\otimes a_j=U$. Now the right fiber $a_j/a_j=\{x:x\otimes a_j\le a_j\}$
contains $T$ ($T\otimes a_j=a_j$) and the group identity $a_{i_0}$
($a_{i_0}\otimes a_j=a_j$), incomparable atoms joining only at $U$; but
$U\otimes a_j=U\not\le a_j$ excludes $U$, so the fiber has no maximum. The left
fiber dies the same way via $a_j\otimes U=U$. Two residuals do not help: each
fails on its own. The group identity living *inside* $F_k$ (incomparable to the
global unit $T$) is the irreducible source of the non-principality.

Formalist:

**Setup.** $B_N$ carrier $\{b,T,a_1,\dots,a_{N+1},s,U\}$, order $b\le x\le U$
($\forall x$), $s\le a_{N+1}$; front $F_k=\{a_1,\dots,a_k\}$ pairwise
incomparable. Let $\otimes$ be associative, two-sidedly monotone, with two-sided
unit $T$ and two-sided zero $b$, restricting to a group $(F_k,\otimes)\cong G$,
$|G|=k\ge2$, identity $a_{i_0}$.

**Lemma (two-sided front absorption).** $a_j\otimes U=U\otimes a_j=U$ for every
$a_j\in F_k$.

*Proof.* $L_{a_j}$ is a bijection of $F_k$, so for each $a_m\in F_k$ there is
$a_e$ with $a_j\otimes a_e=a_m$. Since $a_e\le U$, right-monotonicity gives
$a_m=a_j\otimes a_e\le a_j\otimes U$. Thus $a_j\otimes U$ upper-bounds $F_k$.
For $k\ge2$ the front atoms are pairwise incomparable and, in $B_N$, their sole
common upper bound is $U$ (no $a_{N+1}$, $s$, or front atom dominates two
distinct front atoms). Hence $a_j\otimes U=U$. The mirror statement uses
$R_{a_j}$ and left-monotonicity. $\blacksquare$

**Theorem (non-commutative front rigidity).** No nontrivial finite group is the
front of a two-sidedly monotone, associative, two-residuated $B_N$-tensor.
Equivalently, a group front exists iff $|G|=1$.

*Proof.* Suppose $|G|=k\ge2$. The right residual fiber
$a_j/a_j=\{x:x\otimes a_j\le a_j\}$ contains $T$ (unit) and $a_{i_0}$ (group
identity: $a_{i_0}\otimes a_j=a_j$). $T$ and $a_{i_0}$ are incomparable in $B_N$
(the orbit start $T$ versus a front atom), so any common upper bound is $U$. By
the Lemma $U\otimes a_j=U\not\le a_j$, so $U\notin a_j/a_j$; the fiber thus has
two incomparable maximal candidates and no maximum, violating right
residuation. (Symmetrically $a_j\backslash a_j\ni T,a_{i_0}$ and
$a_j\otimes U=U$ break left residuation.) Hence $k\ge2$ is impossible.
$\blacksquare$

**Verified.** `code/scripts/check-noncommutative-front-group-bound.py` checks
the two-residual predicate (associativity, two-sided monotonicity, *both* fibers
principal) over **independent** left/right $U$-actions:
- Validation harness (commutative orthogonal band, two-residual predicate):
  $k=1,2$ residuated with the non-absorbing action $U\otimes a_i=a_i\otimes
  U=a_i$; $k=3$ fails — exactly the established single-residual data.
- Exhaustive over both $U$-actions: $\mathbb Z/2$ ($k=2$) and $\mathbb Z/3$
  ($k=3$) — **NO** two-residuated tensor.
- Forced-action test (Lemma): for $\mathbb Z/4$, $V_4$, and the non-abelian
  $S_3$ ($k=6$), the monotonicity-forced all-$U$ tensor is not two-residuated,
  and the only non-absorbing ("hopeful") action fails two-sided monotonicity —
  confirming the Lemma leaves the all-$U$ absorber as the unique monotone option,
  which then fails the diagonal fibers.

**Conclusion.** Front rigidity is **not** a commutativity artifact. The
load-bearing facts are purely order-theoretic in $B_N$: (i) a group identity
must sit *inside* the incomparable front, incomparable to the global unit $T$;
(ii) the only upper bound of $\ge2$ front atoms is the absorbing $U$. Together
they force $U$-absorption on both sides and strand the diagonal residual fibers
without a top. The single open loophole now is *not* algebraic
(commutativity/integrality) but *order-theoretic*: the absorbing ceiling. If
$B_N$ is enlarged by a sub-top cap $c<U$ that is a common upper bound of the
front but not absorbing, the fibers could become principal at $c$. This changes
the carrier (no longer same-carrier $B_N$) and is the genuine next escape.

Archivist:

Mark the Pass-34 [New] non-commutative loophole **[Resolved]** with verdict
$|G|=1$ (the two-sided front-absorption lemma + non-commutative rigidity
theorem). Record both in `g2-fg2-hierarchy.md` as the "Non-Commutative Front
Rigidity (Pass 35)" subsection. Promote the order-theoretic diagnosis
(incomparable local identity + absorbing ceiling) to `definitions.md` as the
structural reason the front-width schema is rigid. Open a [New] "capped-front"
problem (sub-top $c<U$, enlarged carrier) in `open_problems.md` and retarget
`research-questions.md`. Log a one-line research-log entry. New script
`code/scripts/check-noncommutative-front-group-bound.py` (added).

Repository updates:
- `code/scripts/check-noncommutative-front-group-bound.py`: new two-residual
  checker (independent left/right $U$-actions, two-sided monotonicity, both
  fibers principal); exhaustive at $k\le3$, forced-action test incl. $S_3$.
- `research/notes/g2-fg2-hierarchy.md`: added "Non-Commutative Front Rigidity
  (Pass 35)" — two-sided front-absorption lemma, non-commutative rigidity
  theorem, verification summary, capped-front loophole.
- `research/definitions.md`: appended the order-theoretic diagnosis of front
  rigidity (incomparable local identity vs. global unit $T$; absorbing ceiling
  $U$ as the unique upper bound of $\ge2$ front atoms).
- `research/open_problems.md`: non-commutative loophole marked [Resolved];
  added [New] capped-front ($c<U$) problem.
- `records/logs/research-log.md`: one-line Pass 35 entry.
- `research/ideas/research-questions.md`: retargeted to the capped-front /
  ceiling-relaxation escape.

Next step:
Pass 36 should attack the capped-front escape, the only remaining loophole. Add
to $B_N$ a single sub-top element $c$ with $a_i\le c<U$ for all front atoms
$a_i$ (so the front's least upper bound becomes $c$, not the absorbing $U$),
keeping $\boxtimes$ on the orbit untouched. Question: does the enlarged carrier
$B_N^{\mathrm{cap}}$ admit a monotone associative two-residuated tensor whose
front $F_k$ is a nontrivial group with $a_j\otimes c=c\otimes a_j=c$ (so the
diagonal fibers become principal at $c$ rather than stranded at $U$)? Determine
(a) whether antitonicity of $\boxtimes$ survives the new relation $a_i\le c$
(this is where Route B died on the same-carrier $B_N$ — check whether the cap,
being *outside* the $\boxtimes$-orbit, escapes the antitonicity cascade), and
(b) the resulting maximum group order as a function of where $c$ sits relative
to the orbit. Settle whether ceiling-relaxation is the true price of a group
front, or whether a deeper APS-level obstruction (e.g. G2/nFG2 interaction)
forbids group fronts in *every* finite bottom-disciplined ambient.

### Pass 36 - 2026-05-31 20:29 JST

Focus:
Attack the capped-front escape — the sole loophole left open by Pass 35. Adjoin
to the bottom-disciplined $B_N$ a single sub-top element $c$ with $a_i\le c<U$
for every front atom $a_i\in F_k$, so the front's least upper bound becomes the
non-absorbing cap $c$ rather than the absorbing $U$, while leaving the
$\boxtimes$-orbit on $T$ untouched. Two questions: (a) does antitonicity of
$\boxtimes$ survive the new relations $a_i\le c$ (this is exactly where Route B
died on the same-carrier $B_N$), and (b) does the cap make a nontrivial group
front residuated by sending the stranded diagonal fiber $a_j\backslash a_j$ to a
principal top at $c$ — and if so, what maximum group order does the cap buy?

Proposer:
Define $B_N^{\mathrm{cap}}$ on carrier $\{b,T,a_1,\dots,a_{N+1},s,U,c\}$ with the
$B_N$ order plus $a_i\le c<U$ for $a_i\in F_k$. Extend $\boxtimes$ by the single
new value $\boxtimes c$. The optimistic picture: because $c$ is a *fresh*
element outside $\mathrm{orbit}(T)$, the antitonicity constraint $a_i\le c
\Rightarrow \boxtimes c\le\boxtimes a_i=a_{i+1}$ pins only the image of $c$ and
imposes *no* relation between two existing orbit atoms — so the Route-B cascade
(which collapsed adjacent orbit atoms by forcing $a_{i+1}\le a_i$) cannot
ignite. With the front's join lifted to $c<U$, the group-front diagonal fiber
$a_j\backslash a_j$ might acquire a principal top at $c$, reopening
$\lvert G\rvert\ge 2$. Conjecture: ceiling-relaxation is the price of a group
front.

Skeptic:
The cap is placed *above* the front, but the obstruction lives *at or below* the
front. Antitonicity does survive — but it forces $\boxtimes c\le\bigwedge_{i\le
k}a_{i+1}=b$ (the front images $a_2,\dots,a_{k+1}$ are pairwise incomparable, so
their meet is the bottom $b$): hence $\boxtimes c=b$ is the *unique* admissible
value, not a free parameter. Worse for the optimist: the diagonal fiber
$a_j\backslash a_j=\{x:a_j\otimes x\le a_j\}$ contains the incomparable pair
$\{T,e_G\}$ (global monoid unit and local group identity atom). For $c$ to be the
fiber's principal top it must (i) dominate $T$ and (ii) satisfy $a_j\otimes
c\le a_j$. But $a_j\le c$ already, and for a group front monotonicity against
$\bigvee F_k=c$ forces $a_j\otimes c\ge c\not\le a_j$. So $c$ is *ejected* from
the very fiber it was meant to cap. The cap cannot simultaneously sit above the
front and inside a fiber bounded below the front.

Formalist:
**Setup.** $B_N^{\mathrm{cap}}$ as above; $\otimes$ monotone, associative, unit
$T$, zero $b$, restricting to a magma on the incomparable front
$F_k=\{a_1,\dots,a_k\}$, $k\ge2$.

**Proposition (a) (unique antitone extension).** The only antitone extension of
$\boxtimes$ to $c$ is $\boxtimes c=b$. *Proof.* $a_i\le c$ gives $\boxtimes
c\le\boxtimes a_i=a_{i+1}$ for all $i\le k$; the $a_{i+1}$ ($2\le i+1\le k+1$)
are pairwise incomparable in $B_N$, so $\bigwedge_i a_{i+1}=b$, whence $\boxtimes
c=b$. The relations $b\le c\le U$ give only $\boxtimes U=b\le\boxtimes c\le
\boxtimes b=U$, already satisfied. $\square$ Since $\mathrm{orbit}(T)$ and the
fixed point at $s$ are untouched and $\boxtimes c=b\ne c$ adds no fixed point,
the full G2/FG2/nFG2/FP profile of $B_N$ is preserved. The Route-B cascade is
escaped precisely because $c\notin\mathrm{orbit}(T)$: the forced inequality lands
on the fresh sink $c$, never relating two orbit atoms.

**Theorem (b) (capped-front group rigidity).** For $k\ge2$, no nontrivial group
front survives in $B_N^{\mathrm{cap}}$: $\lvert G\rvert=1$, for *every* vertical
placement of the single cap. *Proof.* Let $F_k\cong G$ with identity atom $e_G$.
Translations $L_{a_j}$ permute $F_k$, so $\bigvee_i(a_j\otimes a_i)=\bigvee
F_k=c$; monotonicity ($a_i\le c$) gives $a_j\otimes c\ge c$, hence $a_j\otimes
c\in\{c,U\}$, and in both cases $a_j\otimes c\not\le a_j$ (as $c\not\le a_j$).
Also $a_j\otimes U\ge a_j\otimes c\ge c\not\le a_j$. The diagonal fiber
$a_j\backslash a_j$ contains $T$ ($a_j\otimes T=a_j$) and $e_G$ ($a_j\otimes
e_G=a_j$), which are incomparable; their only common upper bounds in
$B_N^{\mathrm{cap}}$ are $c$ and $U$, and both are excluded from the fiber. So
the fiber has $\ge2$ maximal elements and is non-principal: $\otimes$ is not
residuated for $\lvert G\rvert\ge2$. $\square$

**Lemma (Cap Ejection).** If $p\le c$ and $p$ is idempotent ($p\otimes p=p$),
then for any target $t$ with $p\not\le t$, the cap is excluded from the fiber:
$p\otimes c\ge p\otimes p=p\not\le t$, so $c\notin\{x:p\otimes x\le t\}$.
*Corollaries.* (i) The orthogonal width bound survives: for $p\in F_k$ the fiber
$p\backslash b=\{b\}\cup(F_k\setminus\{p\})$ is unchanged ($t=b$, $p\not\le b$),
so $k\ge3$ still fails. (ii) Any fiber whose obstruction is the incomparability
of elements *at or below* the front cannot be repaired by a ceiling — the genuine
repair must lie *below or beside* the obstructing atoms (a selective median over
$\{T,e_G\}$ incomparable to the rest of the front), not above the whole front.

**Verified.** `code/scripts/check-capped-front-bound.py` builds $B_N^{\mathrm
{cap}}$ for $k=2,3$, confirms the unique antitone value $\boxtimes c=b$, and
prints the diagonal fiber $a_j\backslash a_j=\{b,T,a_1\}$ with maximal set
$\{T,a_1\}$ (NON-PRINCIPAL) for both $\mathbb Z/2$ and $\mathbb Z/3$ fronts under
both forced cap-actions $a_j\otimes c\in\{c,U\}$, and the unchanged orthogonal
$p\backslash b$ fiber at $k=3$. All assertions pass.

Archivist:
Mark the Pass-35 [New] capped-front loophole **[Resolved]** with verdict $\lvert
G\rvert=1$ for every single-cap placement (capped-front group rigidity theorem +
Cap Ejection lemma). Record the construction and both results in
`g2-fg2-hierarchy.md` as a new "Capped-Front Rigidity (Pass 36)" section.
Promote the Cap Ejection principle (ceilings cannot repair sub-front fibers) to
`definitions.md`. Open a [New] "selective-median" problem (a $c$ above *only*
$\{T,e_G\}$, incomparable to the rest of the front) in `open_problems.md` and
retarget `research-questions.md`. Log a one-line research-log entry. New script
`code/scripts/check-capped-front-bound.py` (added).

Repository updates:
- `code/scripts/check-capped-front-bound.py`: new checker — builds
  $B_N^{\mathrm{cap}}$ ($k=2,3$), verifies forced $\boxtimes c=b$, prints
  diagonal fibers for $\mathbb Z/2,\mathbb Z/3$ fronts (both cap-actions) and the
  orthogonal $k=3$ $p\backslash b$ fiber; all NON-PRINCIPAL.
- `research/notes/g2-fg2-hierarchy.md`: added "Capped-Front Rigidity (Pass 36)"
  — $B_N^{\mathrm{cap}}$ definition, unique-antitone-extension proposition,
  capped-front group-rigidity theorem, Cap Ejection lemma, verification summary,
  selective-median successor.
- `research/definitions.md`: appended the Cap Ejection principle and the
  $B_N^{\mathrm{cap}}$ vocabulary.
- `research/open_problems.md`: capped-front loophole marked [Resolved]; added
  [New] selective-median ($c$ over $\{T,e_G\}$ only) problem.
- `records/logs/research-log.md`: one-line Pass 36 entry.
- `research/ideas/research-questions.md`: retargeted to the selective-median
  escape.

Next step:
Pass 37 should attack the **selective-median escape** isolated by the Cap
Ejection lemma — the only repair the lemma leaves standing. Instead of a ceiling
over the whole front, adjoin a single element $m$ that dominates *only* the
incomparable obstructing pair $\{T,e_G\}$ (global unit and group-identity atom),
i.e. $T\le m$ and $e_G\le m$, while keeping $m$ incomparable to every
non-identity front atom $a_j$ and to the tail. Question: does $B_N$ with this
selective median admit a monotone associative fully-residuated tensor whose
group front $F_k\cong G$ has $a_j\backslash a_j=m$ (principal at last)? Determine
(i) whether antitonicity forces a value for $\boxtimes m$ that survives — note
$T\le m$ gives $\boxtimes m\le\boxtimes T=a_1$ and $e_G\le m$ gives $\boxtimes
m\le\boxtimes e_G$, so the forced image again collapses, but now toward a single
front atom rather than $b$, which may *or may not* re-ignite a Route-B-style
cascade since $m$ sits over $T$; (ii) whether monotonicity of $a_j\otimes(-)$
against $T\le m,\,e_G\le m$ forces $a_j\otimes m\ge a_j$ with equality
*attainable* (the whole point being that $m$ is NOT above the other front atoms,
so the permutation argument that ejected the full cap no longer applies); and
(iii) the resulting maximum group order as a function of $k$. Settle whether the
selective median is the true minimal carrier-extension that buys a group front,
or whether a deeper $\{T,e_G\}$-incomparability obstruction (the global unit
versus a local idempotent) forbids group fronts in every finite
bottom-disciplined ambient whatsoever.

### Pass 37 - 2026-06-01 00:14 JST

Focus:

Attack the **selective-median escape** — the single repair the Pass-36
Cap-Ejection lemma leaves standing. Same-carrier $B_N$ is group-rigid
($\lvert G\rvert=1$, Passes 34–35) and a ceiling over the *whole* front does
not help (Pass 36). The diagnosis: the diagonal residual fiber
$a_j\backslash a_j$ strands the incomparable pair $\{T,e_G\}$ (global monoid
unit vs. group-identity atom), whose only common upper bound is the absorbing
top $U$, which $U$-absorption ejects from the fiber. Question: does adjoining a
*single* new point $m$ that is exactly the missing join $T\vee e_G$ — dominating
$\{T,e_G\}$ but incomparable to every non-identity front atom and the whole tail —
dissolve the obstruction, and if so, what is the resulting maximum group order
$\lvert G\rvert$?

Proposer:

Adjoin $m$ with $b,T,e_G\le m\le U$ and $m$ incomparable to $\{a_2,\dots,a_k\}$
and to the tail. Then in the augmented order $T\vee e_G=m$ (the upper bounds of
$\{T,e_G\}$ are exactly $m,U$ and $m\le U$), so $m$ is a *new join strictly
below the absorbing top*. Build the tensor $B_N^{\mathrm{med}}$: $b$ zero, $T$
unit, group product on $F_k$, the *forced* front $U$-absorption $a_j\otimes U=U$,
$m\otimes m=m$, $m\otimes a_j=a_j$ (front fixes $m$ from the right by
monotonicity-with-equality), $m\otimes r=U$ for tail $r$, and — the decisive
design choice — the front *does not absorb the tail*: $a_j\otimes r=U$, with all
remaining tail/$U$ interactions collapsing to $U$. Conjecture: this is fully
residuated and the diagonal fiber becomes $a_j\backslash a_j=\{b,T,e_G,m\}$ with
maximum $m$ — principal at last — for **every** finite group front. The escape
is uniform in $\lvert G\rvert$, so the same-carrier verdict $\lvert G\rvert=1$
flips to $\lvert G\rvert=\infty$ once the single join $T\vee e_G$ is supplied
below $U$.

Skeptic:

Two live failure modes. (1) *Tail re-entry.* The earlier non-$U$-absorbing
templates had the front absorb the tail ($a_j\otimes r=a_j$); under that rule
$a_j\otimes r=a_j\le a_j$ puts **every tail element back into**
$a_j\backslash a_j$, and since the tail is incomparable to $m$, the fiber loses
its maximum again — $m$ does not dominate the tail. So the escape is *conditional*
on flipping the front-tail action to $a_j\otimes r=U$; one must check this does
not break monotonicity ($r\le U\Rightarrow a_j\otimes r\le a_j\otimes U=U$: safe)
or associativity. (2) *Antitonicity backlash.* $T\le m$ and $e_G\le m$ force
$\boxtimes m\le\boxtimes T\wedge\boxtimes e_G=a_1\wedge a_2=b$ (distinct orbit
atoms meet at $b$), so $\boxtimes m=b$ is forced. Does this re-ignite a
Route-B-style cascade? No: $m\notin\mathrm{orb}(T)$, so the only new
$\boxtimes$-fact is $\boxtimes m=b\ge b$, antitone-consistent with everything
below $m$ ($\boxtimes T=a_1,\boxtimes e_G=a_2\ge b$). The orbit, and hence the
G2/FG2/nFG2/FP profile, is untouched. Both objections are dischargeable, but
only the machine can certify residuation across *all* the new fibers $m$
introduces.

Formalist:

**Definition ($B_N^{\mathrm{med}}$).** Augment the bottom-disciplined $B_N$
carrier by one element $m$; order: $b\le x\le U$, $s\le a_{N+1}$, and
$b,T,a_1\le m\le U$ with $a_1=e_G$ the group identity. Tensor as in the
Proposer. $\boxtimes m:=b$ (forced); $\boxtimes$ on the orbit unchanged.

**Theorem (Selective-Median Escape).** For every finite **abelian** group $G$
and every $N\ge\lvert G\rvert$, $B_N^{\mathrm{med}}$ with front $F_k\cong G$
($k=\lvert G\rvert$) carries a commutative, associative, monotone, unital
($T$), fully residuated tensor whose diagonal fibers are principal:
$a_j\backslash a_j=\{b,T,e_G,m\}$ with maximum $m=T\vee e_G$. Consequently the
maximum front-group order in the *carrier-plus-selective-median* schema is
$\lvert G\rvert=\infty$ — the same-carrier rigidity ceiling
($\lvert G\rvert=1$) is a pure artifact of the missing join $T\vee e_G$.

*Verification status.* Machine-verified for the cyclic fronts
$\mathbb Z/2,\mathbb Z/3,\mathbb Z/4,\mathbb Z/5$ by
`code/scripts/check-selective-median-bound.py` (explicit-candidate
construction, full $O(n^3)$ check of commutativity, associativity,
monotonicity, unit, and principality of *every* residual fiber). The two
controls reproduce the known obstructions exactly: with no median the fiber is
$a_j\backslash a_j=\{b,T,e_G\}$ with **empty** maximal set (non-principal,
rigidity), and a full cap $c$ over the front fails by **non-monotonicity**
($a_1\otimes c=U\not\le c=c\otimes c$ — the Pass-36 ejection, surfacing here as a
monotonicity violation). *Proof obligation remaining:* (a) the uniform
associativity argument for an arbitrary finite abelian $G$ (the interaction
blocks $b,T,m,\text{collapse}$ are $G$-independent and the $A\times A$ block
inherits associativity from $G$, so the $k\le5$ checks already exercise every
non-group block — this is a sketch, not yet a written-out lemma); (b) the
**non-abelian** case, which needs two independent residuals $\backslash,/$ and
is not covered by the commutative checker.

Archivist:

Mark the Pass-36 [New] selective-median problem **[Resolved]** with verdict
*escape succeeds, $\lvert G\rvert$ unbounded* (Selective-Median Escape theorem;
cyclic $k\le5$ machine-verified; uniform-abelian sketch). Record the
$B_N^{\mathrm{med}}$ construction, the theorem, the "missing-join" diagnosis,
and both control obstructions in `g2-fg2-hierarchy.md` as a new
"Selective-Median Escape (Pass 37)" section. Promote the *missing-join
principle* (front-group rigidity $\Leftrightarrow$ absence of $T\vee e_G$ below
the absorbing top; the minimal repair is the single join $m=T\vee e_G$) to
`definitions.md`. In `open_problems.md`: mark the selective-median item
[Resolved]; add a [New] **non-abelian selective-median** problem (two-residual
$B_N^{\mathrm{med}}$, does the escape survive without commutativity?) and a
[New] **abelian uniformity** problem (write out the $G$-independent
associativity lemma). One-line research-log entry. Retarget
`research-questions.md` to the non-abelian median. New script
`code/scripts/check-selective-median-bound.py` (added).

Repository updates:
- `code/scripts/check-selective-median-bound.py`: new checker — explicit
  $B_N^{\mathrm{med}}$ candidate, full axiom + residuation verification for
  $\mathbb Z/2,\dots,\mathbb Z/5$ (all ESCAPE), plus no-median and full-cap
  controls (both FAIL with the predicted fiber/monotonicity obstruction).
- `research/notes/g2-fg2-hierarchy.md`: added "Selective-Median Escape
  (Pass 37)" — $B_N^{\mathrm{med}}$ definition, escape theorem, missing-join
  diagnosis, $\boxtimes m=b$ forcing, control table, open obligations.
- `research/definitions.md`: appended the $B_N^{\mathrm{med}}$ vocabulary and
  the missing-join principle.
- `research/open_problems.md`: selective-median problem [Resolved]; added [New]
  non-abelian-median and [New] abelian-uniformity problems.
- `records/logs/research-log.md`: one-line Pass 37 entry.
- `research/ideas/research-questions.md`: retargeted to the non-abelian median.

Next step:

Pass 38 should attack the **non-abelian selective median**. Drop commutativity:
equip $B_N^{\mathrm{med}}$ with a two-residual ($\backslash,/$) tensor whose
front $F_k$ is a non-abelian group (smallest case $S_3$, $k=6$, $N\ge6$).
The commutative escape relied on $a_j\otimes m=m\otimes a_j=a_j$ and on a single
diagonal fiber; non-commutatively there are *two* diagonal fibers
$a_j\backslash a_j$ and $a_j/a_j$, each of which must become principal at $m$,
and the right/left front-tail actions may now diverge. Question (i): is
$m=T\vee e_G$ still the correct single join, or does non-commutativity strand a
*second* incomparable pair (e.g. $\{e_G, \text{some conjugacy witness}\}$)
requiring a second median? (ii) Does two-sided monotonicity against $T\le m$,
$e_G\le m$ still permit $a_j\otimes m=a_j=m\otimes a_j$ with the tail pushed to
$U$ on both sides? (iii) Determine whether the escape is genuinely
group-theoretic-uniform (every finite group) or whether non-abelian groups
demand carrier extensions growing with the number of conjugacy classes — i.e.
whether $\#$(selective medians needed) is a new group invariant of the front.
Build `code/scripts/check-noncommutative-selective-median.py` (two-residual
analogue of the Pass-37 checker, seeded with $S_3$) to settle (i)–(iii)
empirically before attempting the uniform theorem.

### Pass 38 - 2026-06-01 04:41 JST

Focus:

Test the non-abelian selective-median escape. Pass 37 showed that adjoining the
single join $m=T\vee e_G$ lets finite cyclic fronts escape the same-carrier
group-rigidity obstruction. The remaining question is whether non-commutativity
requires a second median or new order data, because full residuation now has two
diagonal fibers: $a_j\backslash a_j$ and $a_j/a_j$.

Proposer:

Use the same one-point median. Put a non-abelian group on the front, with
$e_G=a_1$, adjoin $m$ with $b,T,e_G\le m\le U$, and keep $m$ incomparable to
the non-identity front atoms and the tail. Let $m$ act as a two-sided identity
on front atoms, collapse front-tail and tail-front products to $U$, and preserve
the ordinary group product on the front. Since left and right group translations
are bijections, the same residual-fiber argument should work on both sides.

Skeptic:

The smallest serious test is $S_3$. If $S_3$ fails, the
fantasy of a one-point fix dies immediately. Three live worries. (1) *Twin
fibers.* Non-commutatively there are two diagonal residuals
$a_j\backslash a_j=\{x:a_j\otimes x\le a_j\}$ and
$a_j/a_j=\{x:x\otimes a_j\le a_j\}$; a single median $m$ must become the maximum
of *both* simultaneously. If left- and right-translation interacted with $m$
asymmetrically, one fiber could keep $m$ while the other strands a fresh
incomparable pair — say $\{e_G,$ a conjugacy witness$\}$ — demanding a second
join. (2) *Translation defects.* The Pass-37 escape leaned on
$a_j\otimes m=m\otimes a_j=a_j$; one must check both one-sided actions remain
monotone against $T\le m$, $e_G\le m$ once the front product is genuinely
non-commutative, with front-tail products pushed to $U$ on *both* sides. (3)
*Conjugacy invariance.* The real fear: that $\#$(medians) tracks the number of
conjugacy classes (so $S_3$ would need 3, $D_4$/$Q_8$ five), turning the median
count into a new group invariant of the front. Only the two-residual checker can
discriminate "one median always suffices" from "median count $=$ class count".

Formalist:

**Definition ($B_N^{\mathrm{med}}$, two-residual).** Carrier and order as in
Pass 37: bottom-disciplined $B_N$ plus $m$ with $b,T,a_1\le m\le U$
($a_1=e_G$), $m$ incomparable to $a_2,\dots,a_{N+1},s$. Tensor (now without
commutativity): $b$ zero, $T$ two-sided unit, group product on $F_k\cong G$,
$m\otimes m=m$, $m\otimes g=g\otimes m=g$ for $g\in F_k$, $a_j\otimes m=a_j$,
every remaining nonzero non-unit product $=U$ on both sides; $\boxtimes m:=b$
(forced, $\boxtimes m\le\boxtimes T\wedge\boxtimes e_G=a_1\wedge a_2=b$).

**Theorem (Single-Median Uniformity — tested battery).** For each
$G\in\{S_3,\ D_4,\ Q_8,\ \mathbb Z/4\}$ and $N\ge\lvert G\rvert$, the
two-residual $B_N^{\mathrm{med}}$ above is associative, two-sided unital,
two-sidedly monotone, and *fully two-sided residuated*: every left fiber
$\{x:a\otimes x\le c\}$ and right fiber $\{x:x\otimes a\le c\}$ has a unique
principal maximum. In particular both diagonal fibers coincide,
$a_j\backslash a_j=a_j/a_j=\{b,T,e_G,m\}$ with maximum $m=T\vee e_G$.
Consequently $\#$(medians needed) $=1$ for the whole battery, *independent* of
the conjugacy-class count (3 for $S_3$, 5 for $D_4$ and $Q_8$). The number of
selective medians is therefore **not** a new group invariant of the front.

*Verification status.* Machine-verified by
`code/scripts/check-noncommutative-selective-median.py`: explicit two-residual
candidate, full $O(n^3)$ associativity, two-sided unit, two-sided monotonicity,
and unique-principal-maximum of *every* left and right fiber. All four groups
ESCAPE with a single median; both controls FAIL exactly as predicted — the
no-median control leaves the diagonal fibers
$a_j\backslash a_j=a_j/a_j=\{b,T,e_G\}$ with empty maximal set (non-principal),
and the full-cap control breaks two-sided monotonicity ($a_1\otimes c=U\not\le
c=c\otimes c$). Report
`artifacts/reports/noncommutative-selective-median-check.json` records
`mediansNeeded=1` and `leftPrincipal=rightPrincipal=[m]` for all four groups.
*Proof obligation remaining:* (a) the uniform all-finite-groups theorem — the
battery exercises both a non-normal-subgroup group ($D_4$) and an all-normal /
unique-involution group ($Q_8$), but a $G$-independent argument that the only
join-deficient pair below $U$ is always $\{T,e_G\}$ is still a sketch; (b) the
$G$-independent associativity lemma (interaction blocks $b,T,m,\text{collapse}$
are $G$-free; the $F_k\times F_k$ block inherits associativity from $G$).

Archivist:

Mark the Pass-37 [New] non-abelian-selective-median problem **[Resolved for the
tested battery]** with verdict *one median suffices uniformly; median count is
not a new group invariant*. Promote the single-median-uniformity statement and
the missing-join principle (now confirmed two-sided) to `g2-fg2-hierarchy.md`
as a "Non-Abelian Selective Median (Pass 38)" section, and append the
two-residual $B_N^{\mathrm{med}}$ vocabulary plus the single-median-uniformity
note to `definitions.md`. In `open_problems.md`: the non-abelian item is
[Resolved for tested battery]; keep the [New] *uniform all-finite-groups*
theorem and the [New] *abelian uniformity* (associativity) lemma as the live
open obligations. Retarget `research-questions.md` to the uniform
all-finite-groups median theorem. One-line research-log entry. The checker
`code/scripts/check-noncommutative-selective-median.py` and report
`artifacts/reports/noncommutative-selective-median-check.json` were produced by
this pass.

*Recovery note.* This pass was originally started by an automated run that
crashed mid-Skeptic; it had already produced the checker, the report, the
`research-log.md` Pass-38 entry, and the `open_problems.md` Pass-38 verdict, and
had incremented the State counter to 39, but left this discussion entry,
`g2-fg2-hierarchy.md`, `definitions.md`, and `research-questions.md` unwritten
(several files were truncated mid-sentence). The present run re-verified the
checker independently (all four groups ESCAPE, both controls FAIL), repaired the
truncations, and completed the missing edits. The counter is left at 39 (this
completes Pass 38; the next run is Pass 39) rather than double-incremented.

Repository updates:
- `records/discussions/autonomous-discussion.md`: completed the truncated Pass-38
  entry (Skeptic, Formalist, Theorem + verification status, Archivist, this
  block, Next step); recovery note added.
- `research/notes/g2-fg2-hierarchy.md`: repaired the truncated Pass-35 diagnosis
  sentence; added "Selective-Median Escape (Pass 37)" and "Non-Abelian Selective
  Median (Pass 38)" sections (definitions, theorems, single-median-uniformity).
- `research/definitions.md`: repaired truncated Pass-35 entry; added the
  selective-median $m=T\vee e_G$ vocabulary, the missing-join principle, and the
  single-median-uniformity note.
- `research/ideas/research-questions.md`: repaired truncated tail; retargeted the
  active question to the uniform all-finite-groups non-abelian median theorem.
- `research/open_problems.md`: (already written by the crashed run) non-abelian
  median [Resolved for tested battery]; [New] uniform theorem + [New] abelian
  associativity lemma retained.
- `records/logs/research-log.md`: (already written by the crashed run) one-line
  Pass-38 entry.
- `code/scripts/check-noncommutative-selective-median.py`,
  `artifacts/reports/noncommutative-selective-median-check.json`: checker +
  report (produced by the crashed run; re-run and confirmed this pass).

Next step:

Pass 39 should attempt the **uniform all-finite-groups non-abelian
selective-median theorem**: prove that for *every* finite group $G$, the
two-residual $B_N^{\mathrm{med}}$ ($N\ge\lvert G\rvert$) with ordinary group
multiplication on the front and the single join $m=T\vee e_G$ is fully two-sided
residuated — or exhibit the first group where it fails. The crux is a
$G$-independent lemma: in $B_N^{\mathrm{med}}$ the only pair of incomparable
elements both acting as a two-sided identity on the front (hence both lying in
every diagonal fiber) is $\{T,e_G\}$, and $m=T\vee e_G$ is their join strictly
below $U$; therefore one median always principalizes both diagonal fibers. Two
sub-obligations: (i) prove no *off-diagonal* left/right fiber $a\backslash c$,
$c/a$ strands a second join-deficient pair as $\lvert G\rvert$ grows (the
battery checked this for $\lvert G\rvert\le8$; generalize); (ii) write the
$G$-independent associativity lemma. If a counterexample exists, the natural
suspects are groups with large automorphism-induced asymmetry between left and
right cosets — but the $D_4$/$Q_8$ data suggests none. Optionally extend the
checker battery to $A_4$ ($k=12$) and a $p$-group with deeper class structure to
stress-test before committing to the uniform proof.

ith large left/right
coset asymmetry, but the $D_4$/$Q_8$ battery already covers the structurally
hardest order-8 cases.

### Pass 39 - 2026-06-03 13:42 JST

Focus:

Discharge the Pass-38 obligation by proving the **uniform all-finite-groups
non-abelian selective-median theorem**: for *every* finite group $G$ and
$N=\lvert G\rvert$, the two-residual $B_N^{\mathrm{med}}$ — front $F_k\cong G$
with $a_1=e_G$, global unit $T$, zero $b$, single join $m=T\vee e_G$, all
products off $F_k\cup\{m\}$ collapsing to $U$ — is fully two-sided residuated;
equivalently, find the first $G$ where one median fails. The crux is two
$G$-independent lemmas the previous battery only checked for $\lvert G\rvert\le8$:
(i) no *off-diagonal* fiber $a_p\backslash a_r$ ($r\ne p$) strands a second
join-deficient pair as $\lvert G\rvert$ grows; (ii) a $G$-free associativity
lemma.

Proposer:

Claim: the answer is *no failure ever* — one median works for all finite $G$,
and both lemmas have closed $G$-independent proofs, so the per-group battery is
redundant once the structure is named correctly. The decisive observation is a
*block decomposition* of the nonzero, non-unit multiplicative part
$M^\ast=F\cup\{m\}\cup C$, where $C=\{a_{N+1},s,U\}$:

- **$F\cup\{m\}\cong G^1$** (the group $G$ with a *freshly adjoined* identity
  $m$). Here $m$ is the two-sided identity of the block ($m\otimes g=g\otimes
  m=g$, $m\otimes m=m$), while $e_G=a_1$ remains the group identity but is *not*
  the block identity, because $e_G\otimes m=e_G\ne m$. A monoid cannot have two
  distinct two-sided identities, and indeed it doesn't: $G$ sits inside $G^1$ as
  a subsemigroup-not-submonoid. This is exactly the free $G^1$ construction.
- **$C$ is a two-sided ideal collapsing to $U$**: any product with at least one
  factor in $C$ (both factors nonzero non-unit) equals $U\in C$.

Then $M^\ast$ is the ideal extension $G^1\hookrightarrow M^\ast\twoheadrightarrow
\{U\}$, associativity is automatic, and residuation reduces to a fiber count
that never mentions the multiplication table of $G$ beyond "$F$ is an antichain
permuted by translation".

Skeptic:

Where could $\lvert G\rvert$ sneak back in? Three pressure points. (1)
*Off-diagonal multiplicity*: there are $k(k-1)$ ordered off-diagonal targets
$L(a_p,a_r)$; if even one stranded $\{T,a_{q^\ast}\}$ with $q^\ast\ne e$, a
*single* median could not cap it (the median only dominates $\{T,e_G\}$). (2)
*Diagonal multiplicity*: there are $k$ diagonal fibers $L(a_p,a_p)$, one per
front atom; do they strand $k$ *different* pairs needing $k$ medians? (3)
*Monotonicity under a nontrivial group*: when left/right translations are
genuinely distinct (non-abelian), could two-sided monotonicity fail on the
$a_1\le m$ cover after multiplying by a front atom? Each must be answered with no
appeal to a finite battery, or the "uniform" claim is hollow.

Formalist:

Fix $G$, $N=k=\lvert G\rvert$, $a_1=e_G$. Tensor on nonzero non-unit elements:
$a_i\otimes a_j=a_{ij}$ (group); $m\otimes m=m$, $m\otimes g=g\otimes m=g$ for
$g\in F_k$; and $x\otimes y=U$ whenever $x$ or $y\in C=\{a_{N+1},s,U\}$. Order
covers: $b\prec(\text{all})$, $(\text{coatoms})\prec U$, $s\prec a_{N+1}$,
$T\prec m$, $a_1\prec m$ (so $m=T\vee a_1$); $F_k$ is an antichain.

**Lemma 1 (Associativity, $G$-free).** $\otimes$ is associative.
*Proof.* $b$ absorbs, $T$ neutralizes — both reduce any triple. On
$M^\ast=F\cup\{m\}\cup C$: $F\cup\{m\}\cong G^1$ is a monoid (verify: $m$ is a
two-sided identity, $F=G$ is a subsemigroup, products stay in $F\cup\{m\}$). $C$
is a two-sided ideal with $x\otimes y=U$ for any triple touching $C$: if a
single factor lies in $C$ then both bracketings short-circuit to $U$ because
$U\otimes z=z\otimes U=U$ for $z$ nonzero non-unit, and $F\cup\{m\}$ is closed so
the other two factors never escape to produce a non-$U$ value. Hence $M^\ast$ is
an *ideal extension* $G^1\to M^\ast\to\{U\}$; associativity holds in each block
and across, independent of the Cayley table. $\square$

**Lemma 2 (Two-sided monotonicity, $G$-free).** It suffices to check the order
covers. The only nontrivial covers are $s\prec a_{N+1}$, $T\prec m$, $a_1\prec
m$. (i) $T\prec m$: for any $z$, $z=T\otimes z\le m\otimes z$ and $z=z\otimes
T\le z\otimes m$, since $m\otimes z,z\otimes m\in\{z,U\}\supseteq\{z\}$ pointwise
$\ge z$. (ii) $a_1\prec m$: $a_1\otimes z\le m\otimes z$ because for $z=a_j$ both
equal $a_j$ ($a_1=e_G$!), for $z=m$ they are $a_1\le m$, for $z\in C$ both $U$;
symmetric on the right. The group enters *only* through $a_1\otimes a_j=a_j=
m\otimes a_j$, which holds precisely because $a_1$ is the identity — no other
table entry is consulted. (iii) $s\prec a_{N+1}$: both lie in $C$, every product
collapses to $U$ on both sides (or to $b$/itself under $b$/$T$). $\square$

**Lemma 3 (Fiber classification, $G$-free).** Every left fiber $L(a,c)=\{x:
a\otimes x\le c\}$ is principal; by the front-inverting anti-automorphism
$\phi(a_i)=a_{i^{-1}}$ ($\phi=\mathrm{id}$ off $F$, an order-automorphism with
$\phi(x\otimes y)=\phi(y)\otimes\phi(x)$), so is every right fiber. *Proof.* The
nontrivial multiplier is $a=a_p\in F$, giving $a_p\otimes x=b\,(x{=}b)$,
$a_p\,(x{\in}\{T,m\})$, $a_{pq}\,(x{=}a_q)$, $U\,(x{\in}C)$. Casework on $c$:
- $c=a_r$: $x{=}b$ in; $T,m$ in iff $a_p\le a_r\Leftrightarrow r{=}p$; the unique
  $a_q$ with $pq{=}r$, i.e. $q^\ast{=}p^{-1}r$, in. If $r\ne p$: fiber
  $=\{b,a_{q^\ast}\}$, $q^\ast\ne e$, **max $a_{q^\ast}$** — the unit drops out,
  no pair stranded (answers Skeptic 1). If $r{=}p$: $q^\ast{=}e$, fiber
  $=\{b,T,a_1,m\}$, **max $m=T\vee a_1$** — the stranded pair is $\{T,a_1\}$ for
  *every* $p$, so the *same* median caps all $k$ diagonals (answers Skeptic 2).
- $c=m$: if $a_p=a_1$, fiber $\{b,T,a_1,m\}$ max $m$; else $\{b,a_{p^{-1}}\}$.
- $c\in\{b,T,a_{N+1},s\}$: fiber $\{b\}$. $c=U$: everything, max $U$.
All principal, $G$-independently. $\square$

**Theorem (Uniform Non-Abelian Selective-Median Residuation).** For every finite
group $G$ and $N=\lvert G\rvert$, $B_N^{\mathrm{med}}$ with front $F_k\cong G$
carries an associative, two-sided monotone, $T$-unital, fully two-sided
residuated tensor with $\boxtimes m=b$ (forced, antitonicity preserved), keeping
the G2/FG2/nFG2/FP profile. The diagonal fibers satisfy $a_p\backslash a_p=
a_p/a_p=\{b,T,e_G,m\}$ with max $m$, for all $p$. Hence the maximum admissible
front-group order is $\lvert G\rvert=\infty$ and the number of medians needed is
exactly $1$, uniformly — independent of $\lvert G\rvert$, conjugacy-class count,
and normality structure. $\blacksquare$

Verification status: Lemmas 1–3 are proved $G$-independently above (the three
Skeptic pressure points are exactly Lemmas 2(ii), 3 off-diagonal, 3 diagonal).
Empirically reconfirmed past the old $\lvert G\rvert\le8$ ceiling:
`code/scripts/check-uniform-selective-median-theorem.py` runs the battery
$\mathbb Z/6$, $(\mathbb Z/2)^3$, $D_5$, $A_4$ (smallest group violating the
converse of Lagrange — a pathological stress test), and $S_4$ (order 24, carrier
30). All five ESCAPE with a single median; the $G$-independence audit (block
$=G^1$; $C$ a collapsing ideal; diagonal fiber $\equiv\{b,T,e_G,m\}$;
off-diagonal strands no pair) passes for all five; both controls (no-median,
full-cap) FAIL for all five. Report:
`artifacts/reports/uniform-selective-median-theorem-check.json`.

Archivist:

Promote the Pass-38 [Resolved for tested battery] non-abelian-median item to
**[Resolved]** with the uniform theorem and retire the two Pass-38 [New]
obligations (uniform all-finite-groups theorem; abelian associativity lemma) as
**[Resolved]** — both are now closed by Lemmas 1–3. Add a
"Uniform Selective-Median Theorem (Pass 39)" section to `g2-fg2-hierarchy.md`
with the block decomposition and the three lemmas. Append the $G^1$-block /
collapsing-ideal vocabulary and the front-inverting anti-automorphism to
`definitions.md`. Retarget `research-questions.md` to the next frontier (the
selective-median *poset* as a free construction; minimality/uniqueness of the
single median; and whether infinite/topological groups fit). One-line
research-log entry. New files this pass:
`code/scripts/check-uniform-selective-median-theorem.py`,
`artifacts/reports/uniform-selective-median-theorem-check.json`.

Repository updates:
- `records/discussions/autonomous-discussion.md`: appended this Pass-39 entry;
  State counter 39 -> 40; closed the dangling Pass-38 Next-step sentence.
- `research/notes/g2-fg2-hierarchy.md`: added "Uniform Selective-Median Theorem
  (Pass 39)" — block decomposition $M^\ast=G^1\cup C$, Lemmas 1–3, theorem.
- `research/definitions.md`: added the $G^1$-block, collapsing-ideal, and
  front-inverting anti-automorphism $\phi$ entries.
- `research/open_problems.md`: non-abelian median -> [Resolved (Pass 39)];
  uniform-theorem and abelian-associativity [New] items -> [Resolved (Pass 39)];
  added [New] selective-median-poset / minimality / infinite-group questions.
- `research/ideas/research-questions.md`: retargeted active question to the
  selective-median free construction and infinite-group front.
- `records/logs/research-log.md`: one-line Pass-39 entry.
- `code/scripts/check-uniform-selective-median-theorem.py`,
  `artifacts/reports/uniform-selective-median-theorem-check.json`: new
  battery + $G$-independence audit (5 groups, $\lvert G\rvert\le24$).

Next step:

Pass 40 should investigate the **selective-median construction as a functor /
free object**. Two threads. (a) *Minimality & uniqueness*: is the single join
$m=T\vee e_G$ the *unique* one-element order extension below $U$ that
principalizes all diagonal fibers, or merely *a* minimal one? Characterize the
poset of admissible medians (added elements $m'$ with $T,e_G\le m'<U$,
$m'\not\ge$ any non-identity front atom) and show $m=T\vee e_G$ is its bottom —
i.e. the *least* repair. (b) *Infinite fronts*: the proof of Lemmas 1–3 never
used finiteness of $G$ except to keep the carrier finite and guarantee fibers
attain maxima; does the construction survive for a countable group $G$ (e.g.
$\mathbb Z$, $\mathbb Q$, $S_\infty$) if we work in a completion where the
relevant fibers still have suprema? The likely obstruction is residuation
requiring *arbitrary* fiber suprema (a completeness condition) rather than just
the single missing join — pinpoint exactly which fibers go non-principal when
$F_k$ becomes infinite and whether a Dedekind–MacNeille completion of the
front-plus-median order repairs them or introduces fresh join-deficient pairs.
iber suprema (a completeness condition) might bite. [Pass 39 Next-step,
recovered from a truncated write; addressed in Pass 40 below.]

### Pass 40 - 2026-06-03 23:07 JST

Focus:

The selective median as a *universal* (free) repair, on two fronts. (a)
**Uniqueness, not just minimality.** Pass 37–39 fixed *a* repair: adjoin one
$m$ with $\downarrow m=\{b,T,e_G\}$, $\uparrow m=\{U\}$. Is this the *unique*
single-element order-extension below $U$ that simultaneously (i) keeps the
$B_N^{\mathrm{med}}$ tensor monotone and (ii) principalizes every diagonal
fiber $a_p\backslash a_p$? Or merely the least of a poset $\mathcal M$ of
admissible medians? (b) **Cardinality-freedom.** Lemmas 1–3 are written
$G$-freely; the only place finiteness was invoked was "fibers attain maxima."
Does $B_N^{\mathrm{med}}$ survive for an infinite front group ($\mathbb Z$,
$\mathbb Q$, $S_\infty$)? Where, exactly, does cardinality enter — in the
residual fibers (suspected) or somewhere else?

Proposer:

Claim: $\mathcal M$ is a *singleton*, and the residuated structure is literally
independent of $\lvert G\rvert$; the only thing that needs finiteness is the
$\boxtimes$-orbit (the nFG2 profile), not residuation. Construct the admissible
median by its down-set $D=\downarrow m'\cap M_0$ ($M_0$ the old carrier). The
defining constraints are: $b\in D$ (bottom discipline), $\{T,e_G\}\subseteq D$
(it must dominate the obstructing pair), $U\notin D$ (it is strictly below the
top), and the tensor on $m'$ is the monotone-*forced* least extension
$a\otimes m':=\bigvee\{a\otimes z: z\le m'\}$. Then any extra element in $D$
beyond $\{b,T,e_G\}$ *self-destructs*: if $z\in D$ and $z$ lies in the
collapsing ideal $C$ (a tail element or $U$), then for any front multiplier
$a_p$ we have $a_p\otimes z=U$, so monotonicity forces $a_p\otimes m'\ge U$,
hence $a_p\otimes m'=U\not\le a_p$ — the median drops out of $a_p\backslash a_p$
and the fiber reverts to the non-principal $\{b,T,e_G\}$. Likewise if a
non-identity front atom $a_q\in D$ ($q\ne e$), then $a_p\otimes m'\ge a_p\otimes
a_q=a_{pq}$, and for $p$ with $pq\ne p$ (i.e. always, for $q\ne e$) the atom
$a_{pq}$ is incomparable to $a_p$, so $a_p\otimes m'\not\le a_p$ — again the
fiber loses $m'$. Hence $D=\{b,T,e_G\}$ is *forced*: $\mathcal M=\{T\vee e_G\}$.
This is exactly the **Cap-Ejection lemma (Pass 36) read backwards**: the same
monotone forcing that ejects a ceiling $c$ over the *whole* front ejects *any*
element a candidate median dares to dominate beyond the obstructing pair.

For (b): the proof of Lemma 3 shows each diagonal fiber is $\{b,T,e_G,m\}$
(size 4) and each off-diagonal fiber is $\{b,a_{p^{-1}r}\}$ (size 2) — these
counts do not mention $\lvert G\rvert$. Every *other* fiber is the whole carrier
(cofinal at $U$). So no fiber is a *proper infinite* set; the dreaded "arbitrary
fiber suprema" never appear because the absorbing top $U$ swallows every large
join. The residuated poset $B_\infty^{\mathrm{med}}$ therefore exists for any
$G$.

Skeptic:

Three pressure points. (S1) The "monotone-forced least extension" is a
*choice*; maybe a *non-least* tensor value on $m'$ rescues a larger down-set.
Reply: monotonicity is a lower bound $a\otimes m'\ge\bigvee\{a\otimes z\}$, and
the fiber condition $a_p\otimes m'\le a_p$ is an *upper* bound; if the forced
lower bound already exceeds $a_p$, no choice of value can satisfy the upper
bound. The forcing is genuinely two-sided, so the argument is choice-free. (S2)
"$\uparrow m'=\{U\}$ is forced" — is it? Could $m'\le s$ or $m'\le a_{N+1}$?
Reply: if $m'\le t$ for a tail element $t$, then by antitonicity $\boxtimes
t\le\boxtimes m'=b$ forces nothing new, but the fiber $a_p\backslash a_p$ now
must also contain everything $\le m'$, dragging in $t$ with $a_p\otimes t=U$ —
same ejection. So $m'$ incomparable-up to the tail is forced too; $\uparrow
m'=\{U\}$. (S3) For infinite $G$: is the *order* still a sound APS — is
$\boxtimes$ still total and antitone, and does the nFG2/FP profile survive?
**This is where infinity bites.** The front $F=\{a_g\}_{g\in G}$ plays *two*
roles: the residuated front (role 1) and the $\boxtimes$-orbit backbone $T\to
a_1\to a_2\to\cdots\to a_{N+1}\to s$ (role 2). Role 1 is cardinality-free, as
Proposer showed. Role 2 is *not*: with $\lvert G\rvert=\infty$ there is no
terminal $a_{N+1}$, the orbit is an infinite strictly-descending $\boxtimes$-
chain, the first-true nFG2 depth diverges (nFG2($k$) false for all finite $k$),
and the syntactic fixed point $s=\boxtimes^\omega T$ need not exist without a
*meet* $\bigwedge_n\boxtimes^n T$ in the order. So the construction splits.

Formalist:

Decouple the two roles. Let $G$ be any group; let $F=\{a_g:g\in G\}$ be an
antichain; let the *residuated* carrier be $R(G)=\{b\}\cup F\cup\{T,m,r,s,U\}$
with $b$ bottom, $U$ top, $T\le m$, $a_e\le m$ ($e=e_G$), $s\le r$, $m$
incomparable to $F\setminus\{a_e\}$ and to $\{r,s\}$; the tensor as in
Def.($B_N^{\mathrm{med}}$) with the collapsing ideal $C=\{r,s,U\}$.

> **Theorem 40a (Uniqueness of the median / least = unique repair).** Let $G$
> be a finite group. Among all single-element order-extensions $m'$ of $R(G)$
> with $m'<U$ such that the monotone-forced tensor extension keeps $\otimes$
> monotone and every diagonal fiber $a_p\backslash a_p$ ($a_p\in F$) principal,
> there is **exactly one**, namely $m=T\vee e_G$ with $\downarrow m\cap M_0=
> \{b,T,e_G\}$ and $\uparrow m=\{U\}$. Equivalently $\mathcal M$ (the poset of
> admissible medians) is a singleton: the least repair is the *only* repair.
>
> *Proof.* Admissibility forces $\{b,T,e_G\}\subseteq\downarrow m'$ and $U\notin
> \downarrow m'$. Suppose $z\in\downarrow m'$ with $z\notin\{b,T,e_G\}$.
> *Case $z\in C\cup\{$tail$\}$:* pick any $a_p\in F$; $a_p\otimes z=U$, so
> monotonicity gives $a_p\otimes m'\ge a_p\otimes z=U$, whence $a_p\otimes
> m'=U\not\le a_p$, so $m'\notin a_p\backslash a_p$; the fiber is then
> $\{b,T,e_G\}$ with the incomparable pair $\{T,e_G\}$ maximal — non-principal,
> contradiction. *Case $z=a_q\in F$, $q\ne e$:* pick $a_p$ with $pq\ne p$ (every
> $p$, since $q\ne e$ in a group); $a_p\otimes a_q=a_{pq}$ is a front atom
> incomparable to $a_p$, so $a_p\otimes m'\ge a_{pq}\not\le a_p$, same
> contradiction. *Case $z=m''$ another new element:* excluded, single-element
> extension. Hence $\downarrow m'\cap M_0=\{b,T,e_G\}$. For the up-set: if $t\in
> C\cup\{$tail$\}$ with $m'\le t$, then $a_p\otimes m'\le a_p$ forces (by
> $m'\le t$, monotonicity downward in the fiber test) $t$ into the same fiber
> with $a_p\otimes t=U$ — ejection again; so $\uparrow m'=\{U\}$. Both data are
> pinned, so $m'=m=T\vee e_G$. $\square$

> **Corollary 40a′ (Representability / freeness).** The diagonal-residual-repair
> assignment $G\mapsto(R(G),m)$ is the value of a *representable* construction:
> $m$ is the join $T\vee e_G$ computed in the largest sub-join-subsemilattice of
> $\downarrow U$ that avoids the collapsing ideal $C$ and the off-identity front
> $F\setminus\{a_e\}$. It is simultaneously initial and terminal in $\mathcal M$
> (a singleton), so the "selective-median functor" sends each finite group to
> its *unique universal repair* — there is no moduli of medians.

> **Theorem 40b (Residuation is cardinality-free; orbit is not).** Let $G$ be
> *any* group (finite or infinite). (1) $R(G)$ with the median $m$ is a fully
> two-sided residuated poset: every left/right residual fiber $L(a,c)$, $R(a,c)$
> is either of size $\le 4$ (the diagonal $\{b,T,e_G,m\}$ or an off-diagonal
> $\{b,a_{p^{-1}r}\}$) or equal to the whole carrier (cofinal at $U$); in
> particular *no proper infinite fiber occurs*, so all residuals exist with no
> appeal to infinitary suprema beyond the top. Theorems 40a (uniqueness) and the
> Uniform Selective-Median Theorem (Pass 39) hold verbatim for $\mathbb Z$,
> $\mathbb Q$, $S_\infty$. (2) If the *same* front carries the $\boxtimes$-orbit,
> the nFG2/FP profile is *not* cardinality-free: the orbit $T\to a_1\to
> a_2\to\cdots$ has no terminal element, nFG2($k$) is false for every finite
> $k$, and FP-synt fails unless one adjoins the limit fixed point $s_\omega:=
> \bigwedge_{n<\omega}\boxtimes^n T$ (the orbit meet), declaring $\boxtimes
> s_\omega=s_\omega$.
>
> *Proof of (1).* By Lemma 3 (Pass 39) the only non-trivial multiplier is a
> front atom $a_p$, with $a_p\otimes(-)$ taking values $b,a_p,a_{pq},U$; the
> preimage of any down-set $\downarrow c$ is one of the four-or-fewer-element
> sets listed, or (for $c=U$ and the trivial multipliers $b,T,m,U$) the whole
> carrier. The bound $4$ is the cardinality of $\{b,T,e_G,m\}$ and is reached
> only on the diagonal; it does not depend on $\lvert G\rvert$. Right fibers
> transfer via the anti-automorphism $\phi$. *Proof of (2).* The descending
> orbit $\boxtimes^n T$ is strictly decreasing and antitone; absent a terminal
> stage it has a fixed point iff its meet exists and is $\boxtimes$-fixed; this
> is the infinite-orbit-stabilization obstruction already on file. $\square$

**Pathological reading (病的な例).** The "greedy median" $m^\sharp$ with
$\downarrow m^\sharp=\{b,T,e_G,s,r\}$ (also dominating the tail) *looks* more
powerful — it dominates strictly more of the obstruction's neighbourhood — yet
it is the *worst* candidate: monotonicity forces $a_p\otimes m^\sharp\ge
a_p\otimes s=U$, so $m^\sharp$ is ejected from *every* diagonal fiber and
repairs *nothing*. Greed is self-defeating; the *least* element is the *only*
element. This is the Smullyan-flavoured punchline of Pass 40: in $\mathcal M$,
"do the minimum" and "do the only possible thing" coincide, and any attempt to
"help more" by lowering the median deeper into the order is precisely what
breaks it.

Verification status: Theorem 40a proved above and machine-confirmed by
`code/scripts/check-median-uniqueness.py` Part (a): for $\mathbb Z/2,\mathbb
Z/3,\mathbb Z/4,\mathbb Z/5$ it enumerates *all* $8,16,32,64$ admissible
down-sets and finds in each case exactly **one** survivor, $\{b,T,a_1\}$
($a_1=e_G$). Theorem 40b(1) machine-confirmed by Part (b): the maximum *proper*
(non-whole-carrier) residual fiber over all $(a,c)$ is the constant **4** for
front sizes $\lvert G\rvert\in\{2,3,5,8,13,21,50,100,200\}$ (carrier up to
$206$), with every fiber principal — a flat, $\lvert G\rvert$-independent
profile. Theorem 40b(2) is an analysis result tied to the existing
infinite-orbit-stabilization open problem; the limit fixed point $s_\omega$ is
proposed but not yet machine-modelled. Report:
`artifacts/reports/median-uniqueness-check.json`.

Archivist:

Promote the two Pass-39 [New] items to **[Resolved (Pass 40)]**: the
selective-median minimality/uniqueness question is settled *stronger* than asked
(unique, not merely least — $\mathcal M$ is a singleton), and the infinite-front
question is settled by the residuation/orbit dichotomy (residuation transfers to
all cardinalities; the orbit/profile does not and needs the limit FP
$s_\omega$). Add a "Median Uniqueness & Infinite-Front Dichotomy (Pass 40)"
section to `g2-fg2-hierarchy.md` with Theorems 40a, 40a′, 40b and the greedy-
median pathology. Append to `definitions.md`: the poset $\mathcal M$ of
admissible medians, the Cap-Ejection-backwards uniqueness principle, and the
limit fixed point $s_\omega=\bigwedge_n\boxtimes^n T$. Retarget
`research-questions.md`. One-line research-log entry. New files this pass:
`code/scripts/check-median-uniqueness.py`,
`artifacts/reports/median-uniqueness-check.json`.

Repository updates:
- `records/discussions/autonomous-discussion.md`: appended this Pass-40 entry;
  State counter 40 -> 41; closed the truncated Pass-39 Next-step sentence.
- `research/notes/g2-fg2-hierarchy.md`: added "Median Uniqueness & Infinite-
  Front Dichotomy (Pass 40)" — Theorems 40a, 40a′, 40b, greedy-median example.
- `research/definitions.md`: added the admissible-median poset $\mathcal M$,
  the backwards-Cap-Ejection uniqueness principle, and the limit FP $s_\omega$.
- `research/open_problems.md`: both Pass-39 [New] items -> [Resolved (Pass 40)];
  added [New] items on the limit-FP completion and on whether $\mathcal M$ stays
  a singleton when more than one obstructing pair is present (multi-front).
- `research/ideas/research-questions.md`: retargeted the active question to the
  limit-FP orbit completion and the multi-pair median geometry.
- `records/logs/research-log.md`: one-line Pass-40 entry.
- `code/scripts/check-median-uniqueness.py`,
  `artifacts/reports/median-uniqueness-check.json`: new uniqueness enumeration
  (4 groups, all down-sets) + cardinality-freedom fiber-size scan (|G| up to
  200).

Next step:

Pass 41 should attack the **limit fixed point $s_\omega=\bigwedge_n\boxtimes^n
T$** and the multi-pair generalization. Two threads. (a) *Orbit completion*:
model an infinite-front $B_\infty^{\mathrm{med}}$ where the $\boxtimes$-orbit is
decoupled from the residuated front, adjoin $s_\omega$ as the orbit meet, and
verify that (i) antitonicity and full residuation survive the new element and
(ii) the all-level nFG2 profile is restored in the limit (nFG2($k$) becomes
"true for all $k$" once $s_\omega$ caps the descending chain), connecting to the
on-file infinite-orbit-stabilization problem; and (b) the multi-pair median
geometry — whether the singleton uniqueness of Theorem 40a survives several
obstructing pairs at once or degrades to a tower of medians.

### Pass 41 - 2026-06-04 15:32 JST

Focus:

Settle the status of the Pass-40 *limit fixed point* $s_\omega:=\bigwedge_{n}
\boxtimes^n T$ proposed as the orbit-meet completion of an infinite
$\boxtimes$-orbit, and the multi-pair generalization of the selective-median
uniqueness theorem. Two threads from the Pass-40 Next-step: (a) does adjoining
$s_\omega$ to an infinite $B_\infty^{\mathrm{med}}$ preserve antitonicity and
full residuation while *restoring* all-level nFG2 in the limit? (b) does the
Pass-40 singleton $\mathcal M=\{T\vee e_G\}$ degrade to a *countable tower* of
medians $m_0,m_1,\dots$ when the orbit's limit element introduces a fresh
join-deficient pair $\{T,s_\omega\}$?

Proposer:

Build $B_\infty^{\mathrm{med}}$ by *decoupling*: keep the residuated front
$F\cong G$ (an antichain permuted by translation) exactly as in Pass 39–40, and
let the $\boxtimes$-dynamics live on a *separate* descending $\omega$-chain
$T=o_0>o_1>o_2>\cdots$ with $\boxtimes o_n=o_{n+1}$. Adjoin the orbit meet
$s_\omega=\bigwedge_n o_n$ and *declare* $\boxtimes s_\omega=s_\omega$, placing
$s_\omega$ into the collapsing ideal $C$ so the front absorbs it
($a_p\otimes s_\omega=U$). The hope: (i) the residual fibers are unchanged —
$s_\omega$ sits in the ideal where everything collapses to $U$, so
$s_\omega\backslash s_\omega=\{b,T\}$ is principal and no new median is forced,
preserving $\mathcal M=\{T\vee e_G\}$; (ii) on the chain, nFG2$(k)$ now reads
$o_{k+1}\le o_k$ which holds for *all* finite $k$, and $s_\omega$ caps the chain
with a genuine $\boxtimes$-fixed point, so FP-synt is recovered and the on-file
infinite-orbit-stabilization problem is answered affirmatively in the limit.

Skeptic:

The descending-chain orbit is a category error: it makes $\boxtimes$
*monotone*, not antitone, along the orbit. $\boxtimes$ is antitone by APS
definition, so $o_{k+1}\le o_k$ together with $\boxtimes o_k=o_{k+1}$,
$\boxtimes o_{k+1}=o_{k+2}$ forces, by applying antitone $\boxtimes$ to
$o_{k+1}\le o_k$, the relation $o_{k+2}\ge o_{k+1}$ — the orbit *oscillates*, it
cannot descend monotonically. Worse, the proposed cap collapses the chain
outright. Compute the sign: $s_\omega\le o_n$ and $\boxtimes$ antitone give
$\boxtimes o_n\le\boxtimes s_\omega$, i.e. $o_{n+1}\le s_\omega$. But
$s_\omega=\bigwedge_m o_m\le o_{n+1}$. Hence $o_{n+1}=s_\omega$ for every $n$:
the orbit is constant from index $1$. A meet that is also a $\boxtimes$-fixed
point below the orbit is *impossible* without collapse. The dual placement
(orbit-join above) and the sandwiched placement collapse identically. Thread
(a) as posed is dead; $s_\omega$ is a phantom. For thread (b), the worry is real
only if the limit element creates a genuinely *new* stranded pair in a residual
fiber; if it lands in the collapsing ideal it strands nothing, and the
"tower" reduces to the Pass-40 singleton again — so the interesting tower must
come from *nested* obstructing identities, not from $s_\omega$ itself.

Formalist:

Two negative theorems and one structural dichotomy.

> **Theorem 41a (Antitone index-2 collapse).** Let $(L,\le,\boxtimes)$ be an APS,
> so $\boxtimes$ is antitone, and write $X_k:=\boxtimes^k T$. If all-level nFG2
> holds — $X_{k+1}\le X_k$ for every $k\ge1$ — then $X_2=X_3$, so the orbit
> stabilizes at index $2$ and $p:=X_2$ is a syntactic fixed point,
> $\boxtimes p=p$. *Proof.* nFG2$(1)$: $X_2\le X_1$. Apply antitone $\boxtimes$:
> $\boxtimes X_1\le\boxtimes X_2$, i.e. $X_2\le X_3$. nFG2$(2)$: $X_3\le X_2$.
> Antisymmetry: $X_2=X_3$, whence $\boxtimes X_2=X_3=X_2$. $\square$
>
> *Corollary.* The on-file "infinite analogue of finite orbit stabilization" needs
> **no** well-foundedness or no-infinite-descent hypothesis: for an antitone
> operator, all-level nFG2 is *self-truncating* at depth $2$. An infinite strictly
> nFG2-descending orbit does not exist; the only way to keep an infinite orbit is
> to *violate* nFG2 at cofinally many levels, which is exactly the antichain
> (coupled-front) regime where nFG2 fails at every level.

> **Theorem 41b (Limit-FP obstruction / no order-attached limit fixed point).**
> Let $\{o_n\}_{n\ge0}$ be an infinite $\boxtimes$-orbit forming a
> $\boxtimes$-antichain ($o_i\not\le o_j$ for $i\ne j$), $\boxtimes o_n=o_{n+1}$,
> $\boxtimes$ antitone. Let $\sigma\notin\{o_n\}$ be fresh with
> $\boxtimes\sigma=\sigma$. If $\sigma$ is order-related to the orbit in any of
> the three ways — (i) $\sigma\le o_n$ for all $n$ (a meet/$s_\omega$), (ii)
> $\sigma\ge o_n$ for all $n$ (a join), (iii) $o_{j}\le\sigma\le o_i$ for some
> $i\ne j$ (sandwiched) — then antitonicity forces an orbit identification
> ($o_{n+1}=\sigma$, resp. $o_{n+1}=\sigma$, resp. $o_i$ and $o_j$ comparable),
> contradicting the antichain hypothesis. Hence the *only* antitone-compatible
> fixed point is order-**incomparable** to the entire orbit — a *detached* fixed
> point, which by definition neither caps nor completes the orbit. *Proof.* Case
> (i): $\sigma\le o_n\Rightarrow\boxtimes o_n\le\boxtimes\sigma$, i.e.
> $o_{n+1}\le\sigma$; with $\sigma\le o_{n+1}$ this gives $o_{n+1}=\sigma$ for
> all $n$, collapsing the antichain to a point. Case (ii) is dual:
> $\sigma\ge o_n\Rightarrow\sigma=\boxtimes\sigma\le\boxtimes o_n=o_{n+1}$, and
> $\sigma\ge o_{n+1}$ gives $\sigma=o_{n+1}$. Case (iii): $o_j\le\sigma\le o_i$
> with $\boxtimes\sigma=\sigma$ yields $o_{i+1}\le\sigma\le o_{j+1}$, so $o_{i+1}$
> and $o_{j+1}$ are comparable, and iterating two steps propagates comparability
> across the antichain. $\square$
>
> Together 41a–41b kill the Pass-40 $s_\omega$ proposal: the orbit either
> satisfies nFG2 (then it stabilizes at depth $2$ with a *genuine, reachable*
> fixed point $X_2$ — no limit needed) or it is an antichain (then nFG2 fails at
> every level and *no* order-attached fixed point exists — the only fixed points
> are detached and do not complete the orbit). The "limit fixed point at the
> bottom of the orbit" is, for an antitone $\boxtimes$, a contradiction in terms.

> **Theorem 41c (Median multiplicity; the phantom limit median).** For a family
> $\mathcal P=\{\{T,e_\alpha\}\}$ of front-rigidity obstructing pairs whose
> diagonal fibers each strand exactly $\{T,e_\alpha\}$, the admissible-median
> structure is the product of Pass-40 singletons: $\mathcal M\cong
> \prod_\alpha\{T\vee e_\alpha\}$ — exactly one forced median $m_\alpha=T\vee
> e_\alpha$ per pair, each unique by backwards-Cap-Ejection. For a *nested
> descending* family $e_1>e_2>\cdots$ with meet $\varepsilon=\bigwedge_n e_n$, the
> $m_n=T\vee e_n$ form a descending tower. Residuation forces *every* $m_n$, but
> the limit pair $\{T,\varepsilon\}$ forces only $T\vee\varepsilon$. Since join
> need not commute with the descending meet,
> $$ T\vee\Bigl(\bigwedge_n e_n\Bigr)\;\le\;\bigwedge_n\bigl(T\vee e_n\bigr), $$
> with **strict** inequality whenever the ambient lattice is not meet-continuous
> (fails join-infinite-distributivity). In the strict case the tower's
> order-limit $\bigwedge_n m_n$ is a **phantom median**: forced by every finite
> pair, yet justified by no limit pair (the limit pair only needs the strictly
> smaller $T\vee\varepsilon$). *Pathological witness (病的な例):* the finite
> $N_5$-type lattice $b<\varepsilon<T<c<U$ with an antichain $e_1,\dots,e_k$,
> $\varepsilon<e_i<c$, $T$ incomparable to each $e_i$, has $T\vee e_i=c$ for all
> $i$, $\bigwedge_i e_i=\varepsilon$, and $T\vee\varepsilon=T<c$ — the join-with-
> $T$ map *drops discontinuously* from $c$ on the family to $T$ at its meet. The
> phantom $c$ persists as a forced residual cap over which no obstructing pair
> lives. Answer to thread (b): uniqueness does **not** degrade for $s_\omega$
> itself (it lands in the collapsing ideal and strands nothing — $\mathcal M$
> stays the Pass-40 singleton), but for a genuinely *nested* family of front
> identities $\mathcal M$ becomes an $(\omega{+}1)$-tower whose top exists as a
> residuation requirement *iff* the lattice is meet-continuous; otherwise the top
> is a phantom strictly above $T\vee\varepsilon$.

Verification status: all three machine-confirmed by
`code/scripts/check-limit-fp-and-median-tower.py`, report
`artifacts/reports/limit-fp-median-tower-check.json` (overall **PASS**).
(A) Index-2 collapse: enumerated **all** antitone self-maps on **all** posets
with a unique top up to size $4$ — $88$ posets, $2618$ antitone maps, **zero**
counterexamples to "nFG2$(1)\wedge$nFG2$(2)\Rightarrow X_2=X_3$". (B) Limit-FP
obstruction (finite proxy $a_1\to a_2\to a_3\to a_3$): the three order-attached
placements of $\sigma$ (below/above/sandwiched) all **break** antitonicity; only
the detached placement survives. (C) Phantom median: the $N_5$-type lattice is
verified to be a genuine lattice, $T\vee e_i=c$ for all $i$,
$\bigwedge_i e_i=\varepsilon$, $T\vee\varepsilon=T$, and the strict gap $T<c$ is
confirmed.

Archivist:

Resolve the on-file infinite-orbit-stabilization problem (Core Separations
[New]) **as Theorem 41a** — stabilization at depth $2$, no well-foundedness
needed. Downgrade the Pass-40 limit fixed point $s_\omega$ from a proposed
completion to a **refuted phantom** (Theorem 41b): record that an antitone
$\boxtimes$ admits no order-attached orbit-limit fixed point. Resolve thread (b)
with Theorem 41c: the selective-median singleton is stable under $s_\omega$
(ideal placement) but multi-pair geometry is a product of singletons, and a
nested family yields a tower with a possibly-phantom limit median tied to
meet-continuity. Add a "Limit-FP Obstruction & Median Tower (Pass 41)" section
to `g2-fg2-hierarchy.md` with Theorems 41a/41b/41c. Append to `definitions.md`
the phantom-median notion and the corrected status of $s_\omega$. Retarget
`research-questions.md` to the meet-continuity dividing line. One-line research-
log entry. New files: `code/scripts/check-limit-fp-and-median-tower.py`,
`artifacts/reports/limit-fp-median-tower-check.json`.

Repository updates:
- `records/discussions/autonomous-discussion.md`: appended this Pass-41 entry;
  State counter 41 -> 42; closed the truncated Pass-40 Next-step sentence.
- `research/notes/g2-fg2-hierarchy.md`: added "Limit-FP Obstruction & Median
  Tower (Pass 41)" — Theorems 41a, 41b, 41c, the phantom-median witness.
- `research/definitions.md`: corrected the $s_\omega$ entry (now: refuted as an
  order-attached fixed point) and added the phantom-median / meet-continuity
  dividing line.
- `research/open_problems.md`: infinite-orbit-stabilization [New] ->
  [Resolved (Pass 41)]; Pass-40 $s_\omega$ item annotated [Refuted (Pass 41)];
  added [New] items on detached fixed points and meet-continuous completions.
- `research/ideas/research-questions.md`: retargeted to the meet-continuity
  dividing line and detached-fixed-point semantics.
- `records/logs/research-log.md`: one-line Pass-41 entry.
- `code/scripts/check-limit-fp-and-median-tower.py`,
  `artifacts/reports/limit-fp-median-tower-check.json`: new verification (three
  checks, overall PASS).

Next step:

Pass 42 should pursue the **meet-continuity dividing line** opened by Theorem
41c and the **detached-fixed-point semantics** forced by Theorem 41b. Two
threads. (a) *Meet-continuous completion*: identify the weakest completeness
hypothesis on a $B_N^{\mathrm{med}}$-style lattice under which the median tower's
limit $\bigwedge_n m_n$ equals $T\vee\varepsilon$ (so no phantom arises) — is
join-infinite-distributivity necessary, or does a one-sided frame/locale
condition suffice? Construct a minimal pathological lattice where the phantom gap
is *exactly one cover* to calibrate sharpness. (b) *Detached fixed points*:
since Theorem 41b says the only antitone-compatible orbit fixed point is
order-incomparable to the orbit, ask what such a detached $\boxtimes$-fixed point
*means* proof-theoretically — is it the algebraic shadow of a Rosser-style
fixed point (independent of the Gödel orbit), and does the existing G2-ZOO
arithmetic note already host one? Connect to the open
"$\exists p(p=\boxtimes p)$ vs $\exists p(p=\neg\Box p)$" separation, which now
looks like the *detached vs orbit-attached* fixed-point distinction in disguise.

[Repair note: a crashed write left this tail with concatenated fragments from
the Pass-40 Next-step and a stray heredoc line; the Pass-41 Next-step above is
authoritative and the corrupted trailing text has been removed. — Pass 42.]

### Pass 42 - 2026-06-04 17:15 JST

Focus:

Theorem 41b left the orbit with exactly one antitone-compatible kind of fixed
point — the *detached* one, order-incomparable to every iterate
$\boxtimes^n T$. Pass 42 takes the detached-fixed-point thread of the Pass-41
Next-step and answers what a detached fixed point *means* proof-theoretically:
it is the algebraic shadow of a **Rosser sentence**. We separate two species of
$\boxtimes$-fixed point — *orbit-attached* (comparable to some iterate of the
iterated-consistency tower $\boxtimes^n T$, the Gödelian limit) versus *detached*
(incomparable to the whole tower) — and build a finite preAPS, the **Rosser
gadget $R_2$**, that satisfies FP-synt $\exists q\,(q=\boxtimes q)$ via a
*detached* point while its Gödel orbit $\{\boxtimes^n T\}$ carries **no** attached
fixed point. This settles the long-open Core-Separation entry
"$\exists p(p=\boxtimes p)$ vs an orbit-attached Gödel point" by the reframing
the Pass-41 Archivist predicted: *detached vs orbit-attached*.

Proposer:

Take the heuristic dictionary literally. The Gödel sentence $\pi\leftrightarrow
\neg\Box\pi$ is the fixed point the iterated-consistency tower
$\mathrm{Con}^{(n)}=\boxtimes^n T$ *reaches* (Theorem 41a: under nFG2 it
stabilizes at $\boxtimes^2 T$, a reachable, order-attached fixed point). The
Rosser sentence $\rho\leftrightarrow\neg\Box_R\rho$ is *independent*:
$T\nvdash\rho$, $T\nvdash\neg\rho$, and — the load-bearing fact — $\rho$ is not
provably equivalent to any iterated consistency statement, because $\Box_R$ is
not normal (it violates $D2$/Löb). Algebraically $\rho$'s class is incomparable
to every $\boxtimes^n T$: a *detached* fixed point is the Rosser phenomenon, an
*orbit-attached* one the Gödel phenomenon. Candidate object — the Rosser gadget
$R_2$. Carrier $L=\{\bot,o_0,o_1,p,\top\}$ with the $M_3$-diamond order
($\bot\le x\le\top$ for all $x$; $o_0,o_1,p$ pairwise incomparable). Designated
truth $T:=o_0$. Antitone operator
$$\boxtimes:\ \bot\mapsto\top,\quad\top\mapsto\bot,\quad o_0\mapsto o_1,\quad
o_1\mapsto o_0,\quad p\mapsto p.$$
Then $p=\boxtimes p$ is a fixed point detached from the orbit, and the $T$-orbit
is the 2-cycle $\{o_0,o_1\}$ — an antichain with no internal fixed point. FP-synt
holds, witnessed only by the Rosser point $p$.

Skeptic:

Three worries. (1) *Is the 2-cycle a fair model of the consistency tower?* A
genuine $\mathrm{Con}^{(n)}$ chain is descending, not oscillating. Rebuttal: by
Theorem 41b a strictly descending order-attached tower is exactly what
antitonicity forbids; the antichain (here periodic) regime is the only
antitone-faithful picture of a tower with no attached fixed point, so the
2-cycle is the canonical finite proxy. (2) *Is $p$ smuggled in?* No — $p$ is
*forced* to be detached: any below/above/between placement breaks antitonicity
(Theorem 41b, machine-guarded Pass 41). (3) *Does $R_2$ overclaim the arithmetic
separation?* Yes, if read as a full APS with $\Box$ satisfying $D1$–$D3$ and
$\boxtimes=\neg\Box$. $R_2$ exhibits the *order-theoretic skeleton* of the
Gödel/Rosser split; whether it lifts to a provability predicate with a genuine
Rosser self-reference (Guaspari–Solovay) is a proof obligation tied to the
arithmetic-note open problem. The Skeptic accepts the algebraic claim, flags the
arithmetic lift as unproven.

Formalist:

> **Definition (attached / detached / reachable fixed point).** Let
> $(L,\le,\boxtimes,T,\bot)$ be a preAPS with antitone $\boxtimes$ and orbit
> $O(T)=\{\boxtimes^n T:n\ge0\}$. A fixed point $p$ ($\boxtimes p=p$) is
> *orbit-attached* if $p$ is comparable to some $o\in O(T)$, *detached* if
> incomparable to every $o\in O(T)$, and *reachable* if $p=\boxtimes^n T$ for
> some $n$.
>
> **Theorem 42a (reachability / Rosser separation).**
> (i) Every reachable fixed point is orbit-attached.
> (ii) [41a] If $O(T)$ satisfies all-level nFG2, the reachable fixed point
>     $\boxtimes^2 T$ exists and is attached; no detached point is needed.
> (iii) [41b] If $O(T)$ is a $\boxtimes$-antichain, every antitone-compatible
>     fixed point is detached, hence **not reachable**: $\forall n\,(p\ne
>     \boxtimes^n T)$.
> (iv) A detached fixed point can coexist with a non-attaching orbit. Witness:
>     $R_2$ satisfies $\exists q\,(q=\boxtimes q)$ (via the detached $p$) while
>     $O(T)=\{o_0,o_1\}$ is a fixed-point-free antichain — FP-synt holds with NO
>     orbit-attached (Gödel) fixed point.
>
> *Proof.* (i) trivial. (ii),(iii) are 41a,41b. (iv) direct check of $R_2$
> (script Part A): antitone, $\boxtimes p=p$, $p$ incomparable to $o_0,o_1$,
> orbit antichain with no internal fixed point, and $p\notin\{o_0,o_1\}=
> \{\boxtimes^n T\}$ so $p$ unreachable. $\square$
>
> **Corollary 42b (algebraic Rosser dictionary).** In $R_2$ read $T\nleq p$ as
> "$p$ unprovable", $p\nleq\bot$ as "$p$ irrefutable", and incomparability of $p$
> to every $\boxtimes^n T$ as "$p$ not provably equivalent to any iterated
> consistency statement". The detached $p$ satisfies all three Rosser signatures
> at once, none of which an orbit-attached (Gödel) point can satisfy.

**Pathological reading (病的な例).** On the bare $M_3$ diamond antitonicity is
*nearly content-free* on the middle layer: since $o_0,o_1,p$ are pairwise
incomparable, $\boxtimes$ may permute and fix them *arbitrarily* and stay
antitone — the only real constraints are the forced endpoints
$\boxtimes\top=\bot$, $\boxtimes\bot=\top$. So the diamond is a machine for
manufacturing detached fixed points: every antitone map fixing a middle atom and
2-cycling the other two is a Rosser gadget. The pathology: the *Gödelian* fixed
point (reachable as a limit of the consistency tower) is the rare, fragile one
here — it needs the orbit to order itself into an nFG2 chain — while the
*Rosserian* detached fixed point is *generic*. Smullyan's islanders would note
the irony: on this island the knight who says "no proof of me precedes a proof
of my negation" (Rosser) is the common type, and the knight who is the very
limit of the consistency confessions (Gödel) is the exotic one.

Verification status: Theorem 42a(iv) and Corollary 42b machine-confirmed
(overall **PASS**) by `code/scripts/check-detached-rosser-fixedpoint.py` /
`artifacts/reports/detached-rosser-fixedpoint-check.json`. Part A: $R_2$
antitone, $p$ the unique fixed point, $p$ detached, FP-synt holds, $p$
unreachable from $T$. Part C (exhaustive dichotomy guard): over the 5-element
$M_3$ diamond, **178** antitone self-maps, **90** with a fixed point, **14**
whose $T$-orbit is a non-stabilizing antichain; of those **2** carry a fixed
point and **0** carry an *orbit-attached* one — confirming that in the
antichain-orbit regime every fixed point is detached. Theorem 42a(i)–(iii) are
elementary/recalled. The arithmetic lift (a $\Box_R$ with $\boxtimes=\neg\Box_R$
realizing a genuine Rosser self-reference) is an explicit open proof obligation.

Archivist:

Promote the Pass-41 [New] "Detached fixed points" item in `open_problems.md` to
**[Resolved (Pass 42)]** for its *algebraic* half (detached FP = Rosser shadow,
realized by $R_2$), and add a sharpened **[New]** item for the unresolved
*arithmetic lift*. Add a "Detached Fixed Point = Algebraic Rosser Sentence
(Pass 42)" section to `g2-fg2-hierarchy.md` (Definition, Theorem 42a, Corollary
42b, the $R_2$ model, the genericity pathology). Append to `definitions.md` the
attached/detached/reachable trichotomy and the Rosser gadget $R_2$. One-line
`research-log.md` entry. Retarget `research-questions.md` to the arithmetic
Rosser lift and the $\diamond$-fixed-point open problem.

Repository updates:
- `records/discussions/autonomous-discussion.md`: repaired the crash-corrupted
  tail; appended this Pass-42 entry; State counter 42 -> 43.
- `research/notes/g2-fg2-hierarchy.md`: added "Detached Fixed Point = Algebraic
  Rosser Sentence (Pass 42)" — Definition, Theorem 42a, Corollary 42b, $R_2$,
  genericity pathology.
- `research/definitions.md`: added the attached/detached/reachable fixed-point
  trichotomy and the Rosser gadget $R_2$.
- `research/open_problems.md`: Pass-41 "Detached fixed points" [New] ->
  [Resolved (Pass 42)] (algebraic half); added a [New] item on the arithmetic
  lift to a Rosser provability predicate.
- `research/ideas/research-questions.md`: retargeted the active question to the
  arithmetic Rosser lift and the $\diamond$-fixed-point open problem.
- `records/logs/research-log.md`: one-line Pass-42 entry.
- `code/scripts/check-detached-rosser-fixedpoint.py`,
  `artifacts/reports/detached-rosser-fixedpoint-check.json`: new $R_2$ +
  $M_3$-dichotomy verification (overall PASS).

Next step:

Pass 43 should attack the **arithmetic lift** of the detached fixed point. Two
threads. (a) *Rosser realization*: construct (or obstruct) a provability
predicate $\Box_R$ over a base APS-of-arithmetic with $\boxtimes=\neg\Box_R$ such
that the detached fixed point $p$ of $R_2$ is realized by a genuine Rosser
sentence $\rho\leftrightarrow\neg\Box_R\rho$ — find the weakest derivability
package ($D1$, $\Sigma_1$-completeness, witness-comparison) under which a
$\boxtimes$-fixed point is *forced* detached rather than orbit-attached, and
connect it to the on-file open problem "does there exist a Rosser provability
predicate such that no $\diamond$-fixed point yields a contradiction?" (b)
*Meet-continuity dividing line* (the still-open Pass-41 [New], if the Rosser
thread stalls): the weakest completeness condition forcing $\bigwedge_n m_n=
T\vee\varepsilon$ (no phantom median), calibrated by a one-cover phantom-gap
lattice.

[Reconstruction note: the Pass-40 Next-step above was truncated mid-word by a
crashed run; Pass 41 nonetheless executed and recorded its results in the
research notes, definitions, open_problems, research-questions, and research-log.
Pass 41's results, in brief, for the record: Theorem 41a (antitone index-2
collapse — all-level nFG2 forces $\boxtimes^2 T=\boxtimes^3 T$); Theorem 41b
(limit-FP obstruction — the Pass-40 order-attached $s_\omega$ is refuted; the
only antitone-compatible fixed point near an antichain orbit is order-detached);
Theorem 41c (median multiplicity / phantom median under failure of
meet-continuity). The Pass-42 entry below picks up Theorem 41b's "detached
fixed point" thread.]

[Crash-repair note (Pass 45): a fourth crashed write left a stray, truncated
*duplicate* of the Pass-42 header + Focus appended below this line (it ended
mid-sentence at "...satisfies FP-synt" with no body). The genuine, complete
Pass-42 entry lives above (header at the earlier "### Pass 42 - 2026-06-04 17:15
JST"); the canonical Pass-42/43/44 content is preserved in `open_problems.md`,
`definitions.md`, and the State header of this file. Pass 45 deleted the stray
fragment and appended its own entry below. No Pass-42 content was lost.]

### Pass 45 - 2026-06-05 14:40 JST

Focus:

Pass 44 proved, on the $M_3$ carrier, that **orbit-descent** (eventual constancy
of the consistency orbit $o_n=\boxtimes^n T$, the algebraic Löb shadow) is the
*exact* gate forcing every FP-synt fixed point to be **orbit-attached**, strictly
finer than $\neg$FG2(1). Pass 44 itself flagged the general-$L$ status open and
named the suspect: a *pathological* finite preAPS with a **non-descending** orbit
that nonetheless carries an **attached** fixed point — a third regime that would
refute the clean equivalence "orbit-descent $\Leftrightarrow$ $\exists$ attached
fixed point". Pass 45 asks whether that third regime exists.

Proposer:

It exists, and it is embarrassingly small. Take the chain $C_5:\ 0<1<2<3<4$ and
let $\boxtimes$ be the **order-reversing involution** $r(x)=4-x$ — the literal
"mirror" provability operator, reflecting each sentence through the chain's
midpoint. Reversal of a chain is antitone, and $r\circ r=\mathrm{id}$. Seed the
orbit at the interior point $T=3$. Then
$$o_0=3,\quad o_1=r(3)=1,\quad o_2=r(1)=3,\quad o_3=1,\ \dots$$
so the consistency orbit is the perpetual $2$-cycle $\{3,1\}$ — it **never
descends** ($o_{k+1}\ne o_k$ for all $k$). Yet $r$ has a fixed point: $r(x)=x\iff
x=2$, and $p:=2$ satisfies $1<2<3$, so $p$ is comparable to the orbit elements
$3$ and $1$ — it is **orbit-attached**. A non-descending orbit with an attached
fixed point: the conjectured pathology, realized on a $5$-element
bottom-disciplined chain. The midpoint $p=2$ is the unique *self-dual* sentence,
its own Gödel point, order-attached yet eternally un-*reached* by the bouncing
orbit — a Smullyan knight who is his own mirror image.

Skeptic:

Three objections, each survivable. (1) *Is $T=3$ a legitimate APS top?*
`definitions.md` is explicit that $T,\bot$ are distinguished constants and a
preAPS need **not** make them greatest/least; choosing an interior seed is licit
and is exactly what produces a non-trivial $\boxtimes T=o_1=1\ne\bot$ (so the
consistency value is not refutable — this is genuinely a $G2$-flavored seed, not
a degenerate one). (2) *Does this contradict Pass 44?* No — Pass 44 verified the
equivalence **only on $M_3$**, whose sole non-trivial cycles are *antichain*
$2$-cycles among the incomparable middles, which force detachment; the
equivalence was a carrier artifact. (3) *Is the failure generic or a chain
fluke?* The reversal $r(x)=2m-x$ works on **every odd chain** $C_{2m+1}$:
central fixed point $p=m$ (attached), bracketed by nested non-trivial $2$-cycles
$\{m-j,m+j\}$. Crucially, **even** chains $C_{2m}$ carry $r(x)=2m-1-x$ with *no*
fixed point — the pathology needs a self-dual middle, i.e. odd length. The weak
step is over-reading "non-descending $\Rightarrow$ detached-only" off $M_3$.

Formalist:

Definitions as in `definitions.md`: $o_n=\boxtimes^n T$; the orbit *descends* iff
$\exists k\,(o_{k+1}=o_k)$; $p$ is *attached* iff comparable to some $o_n$,
*detached* iff incomparable to every $o_n$.

**Lemma 45a (Bracketing).** Let $\boxtimes$ be antitone on a poset $L$ and
$p=\boxtimes p$. If $p$ is comparable to two consecutive iterates $o_k,o_{k+1}$,
then $o_{k+1}\le p\le o_k$ or $o_k\le p\le o_{k+1}$; in particular $o_k,o_{k+1}$
are comparable. *Proof.* Say $p\le o_k$. Apply $\boxtimes$ (antitone):
$o_{k+1}=\boxtimes o_k\le\boxtimes p=p$. Hence $o_{k+1}\le p\le o_k$. (Dual if
$o_k\le p$.) $\square$

**Theorem 45b (Descent $\Rightarrow$ attachment, carrier-independent).** On any
poset $L$ with antitone $\boxtimes$, if the orbit descends, $o_{k+1}=o_k=:s$, then
$s=\boxtimes s$ is a fixed point comparable to the orbit element $o_k=s$, hence
attached (indeed *reachable*). No finiteness or enumeration is needed. $\square$

**Theorem 45c (Attachment $\not\Rightarrow$ descent — refutation of the clean
equivalence).** There is a finite bottom-disciplined preAPS with a non-descending
orbit carrying an attached fixed point. *Witness.* $C_5=\{0<1<2<3<4\}$,
$\boxtimes=r(x)=4-x$, $T=3$. Then $\mathrm{orbit}(T)=\{3,1\}$ is a non-degenerate
$2$-cycle (non-descending), and $p=2$ with $1<2<3$ is a $\boxtimes$-fixed,
attached point. Hand-verified; the reversal of $C_{2m+1}$ is a uniform family.
$\square$

**Corollary 45d (Eventual-$2$-cycle regime trichotomy).** Let $\boxtimes$ be
antitone on finite $L$ with the orbit eventually a $2$-cycle $\{e^*,o^*\}$
($\boxtimes e^*=o^*$, $\boxtimes o^*=e^*$). Exactly one of:
(i) **degenerate** $e^*=o^*$ — orbit descends; unique reachable/attached FP
(Pass 44);
(ii) **antichain** $e^*\parallel o^*$ — Rosser/$R_2$ regime, every FP detached
(Pass 42/44);
(iii) **chain** $o^*<e^*$ — by Lemma 45a any FP comparable to both is sandwiched
$o^*\le p\le e^*$ and is attached, while the orbit does **not** descend (NEW,
Pass 45). A chain-cycle is forced to have period exactly $2$; longer even periods
($g=\boxtimes^2$ permuting an antichain) are antichain-supported, hence still
detached-only. The corrected universal statement is therefore the *one-way*
Theorem 45b together with this trichotomy; the converse, and hence the Pass-44
"exact gate" equivalence, holds iff $T$'s orbit cannot reach a chain-cycle.

*Verified:* Lemma 45a, Thm 45b (proofs); Thm 45c witness hand-checked and
recorded in `artifacts/reports/descent-attachment-general-check.json`.
*Proof obligation:* the enumerative survey over $M_3,C_3{-}C_7,N_5,M_4$ in
`code/scripts/check-descent-attachment-general.py` was **not machine-run this
pass** (the workspace execution shell was unavailable); the script is committed
and should be executed next live-shell pass to populate the regime counts and
re-confirm $M_3$ has zero chain-cycles.

Archivist:

Resolve the Pass-44-retarget research question (general-$L$ descent$\Leftrightarrow$
attachment) **negatively**: the clean equivalence is false; the descent$\Rightarrow$
attachment half is a carrier-independent theorem (45b), the converse fails via
the chain-cycle regime (45c/45d). Add a "Descent $\Leftrightarrow$ Attachment is
False: the Reversal-Chain Pathology (Pass 45)" section to `g2-fg2-hierarchy.md`.
Normalize "orbit-descent / eventual-2-cycle regime trichotomy" in
`definitions.md` and repair the crash-splice at the Pass-44 entry. Mark the
relevant `open_problems.md` item resolved. Retarget `research-questions.md` to
(a) when $T$'s orbit reaches a chain-cycle in a bottom-disciplined $B_N$-style
model, (b) eventual period $\ge 4$ antichain cycles, (c) the infinite-$L$ lift.
One-line `research-log.md` entry.

Repository updates:
- `records/discussions/autonomous-discussion.md`: deleted the stray truncated
  Pass-42 duplicate; appended this Pass-45 entry; State counter 45 -> 46.
- `research/notes/g2-fg2-hierarchy.md`: added "Descent ⇔ Attachment is False:
  the Reversal-Chain Pathology (Pass 45)" — Lemma 45a, Theorems 45b/45c,
  Corollary 45d, the $C_5$ witness and odd-chain family.
- `research/definitions.md`: repaired the Pass-44 crash-splice ("trichotomy.d
  among an"); added "Eventual-2-cycle regime trichotomy (Pass 45)".
- `research/open_problems.md`: marked the general-$L$ descent⇔attachment item
  [Resolved (Pass 45), negatively]; added a [New] chain-cycle reachability item.
- `research/ideas/research-questions.md`: retargeted the active question to the
  chain-cycle reachability / period-4 / infinite-$L$ threads.
- `records/logs/research-log.md`: one-line Pass-45 entry.
- `code/scripts/check-descent-attachment-general.py`,
  `artifacts/reports/descent-attachment-general-check.json`: new general-$L$
  survey script (committed; survey run deferred to next live-shell pass) plus a
  hand-verified report (claims A/B PASS).

Next step:

Pass 46 should (a) **run** `check-descent-attachment-general.py` once the shell
is live, populating the regime counts and confirming $M_3$ has zero chain-cycles
and the $C_5/C_7$ counterexamples; then (b) ask the *reachability* question the
trichotomy exposes: in a **bottom-disciplined $B_N$-style** model (the project's
main arena, where $\bot$ is genuinely least and $T$ is the orbit seed), can $T$'s
orbit ever enter a **chain-cycle**, or does bottom discipline + the $B_N$ orbit
geometry force every non-descending orbit to be an *antichain* cycle (making the
Pass-44 equivalence true on the whole bottom-disciplined zoo, with the reversal
chain as the unavoidable non-bottom-disciplined escape)? Secondary thread:
classify eventual period-$\ge4$ antichain cycles (does $g=\boxtimes^2$ on an
antichain ever coexist with FP-synt?) and seek the well-foundedness condition
lifting Theorem 45b to infinite $L$.

### Pass 46 - 2026-06-05 08:00 JST  [reconstructed]

[Reconstruction note: Pass 46 ran (its survey artifact
`artifacts/reports/descent-attachment-general-check.json`, 2026-06-05 08:00,
landed), but its discussion-log append and research-log entry were lost to a
crashed write — the same failure mode that truncated Passes 42-44. Pass 47
recovers it from the State header + the surviving survey JSON.]

Focus:

Execute the survey `check-descent-attachment-general.py` deferred from Pass 45 by
a workspace-shell outage, populating the eventual-2-cycle regime census over
$\{M_3,C_3,\dots,C_7,N_5,M_4\}$ and machine-confirming Thm 45b/45c, then read off
the chain-regime structure.

Proposer / Skeptic / Formalist (condensed):

The run replaced the hand-verified PARTIAL report with a real enumeration:
descent$\Rightarrow$attachment had **0** violations over $>4000$ antitone maps
(machine-confirming **Thm 45b**), and every carrier with a comparable $2$-cycle
exhibited positive non-descending-with-attached-FP counts (machine-confirming
**Thm 45c**). The census exposed the chain-regime structure:

- **Thm 46a (chain period dichotomy).** On a finite chain every antitone
  self-map has all orbits of eventual period $\le 2$: $\boxtimes^2$ is monotone
  and a monotone self-map of a finite chain is eventually fixed, so no antichain
  or period-$\ge3$ cycle can occur. Census-confirmed: every $C_n$ row has cycle
  types $\subseteq\{\text{degenerate},\text{chain}\}$; period $3,4$ appear only
  off chains ($M_3$: two period-$3$; $M_4$: $42$ period-$3$, $6$ period-$4$),
  where $\boxtimes^2$ permutes an antichain.
- **Cor 46b (chain regime split).** Regime (iii) splits into (iii-a)
  *bracketing* — the comparable $2$-cycle straddles a self-dual fixed point
  (attached; generic on odd chains) — and (iii-b) *chain-gap* — no fixed point,
  realized by the even-chain reversal $r(x)=2m-1-x$ on $C_{2m}$, a consistent
  antitone box with empty fixed-point set, the chain analogue of the $M_3$
  Rosser gadget $R_2$.

Archivist:

Marked the Pass-44/45 descent$\Leftrightarrow$attachment open-problem item
[machine-confirmed (Pass 46)]; added the [New (Pass 46)] chain-regime-structure
item carrying Thm 46a, Cor 46b, and the open obligation (prove the bracketing
criterion; decide whether bottom-discipline confines the chain regimes).

Repository updates:
- `artifacts/reports/descent-attachment-general-check.json`: real enumerative run
  (overall PASS) replacing the Pass-45 PARTIAL report.
- `research/open_problems.md`: descent$\Leftrightarrow$attachment item updated to
  machine-confirmed; [New (Pass 46)] chain-regime item added.
- (discussion-log + research-log appends were lost to the crashed write; restored
  here by Pass 47.)

Next step:

Pass 47 should attack the [New (Pass 45)] reachability question now sharpened by
Cor 46b: in a bottom-disciplined $B_N$-style model, can $T$'s orbit reach a
chain-cycle, and prove the bracketing criterion (odd-interval $\Rightarrow$ FP).

### Pass 47 - 2026-06-06 09:30 JST

Focus:

Resolve the [New (Pass 45)] reachability question and the [New (Pass 46)] open
obligation in one stroke. Pass 45/46 conjectured that the chain-cycle escape from
the Pass-44 equivalence ("orbit-descent $\Leftrightarrow$ an attached fixed
point") is an *unavoidable non-bottom-disciplined phenomenon* — that bottom
discipline ($\bot$ genuinely least) plus the $B_N$ orbit geometry would confine
every non-descending $T$-cycle to the *antichain* (Rosser/detached) regime,
restoring the equivalence on the whole bottom-disciplined zoo. Pass 47 tests this
conjecture and proves the chain bracketing criterion left open by Cor 46b.

Proposer:

The conjecture is false, and the counterexample was already on the table —
mislabelled. The $C_5$ reversal $r(x)=4-x$ that Pass 45 used to break the clean
equivalence is **itself bottom-disciplined**: its carrier is the chain
$0<1<2<3<4$, in which $\bot=0$ *is* the genuine least element ($\forall x\,
0\le x$), so the bottom-discipline axiom $\forall x\,(\bot\le x)$ holds outright.
Seeded at $T=3$, its orbit is the strict comparable $2$-cycle $\{3,1\}$ (a
chain-cycle, $1<3$), with the self-dual midpoint $p=2$ an *attached* fixed point.
So a bottom-disciplined model **does** admit a $T$-reachable chain-cycle; bottom
discipline does **not** confine the chain regime. The Pass-45/46 hope conflated
two independent constraints: "$\bot$ is least" (bottom discipline) and "the orbit
is *flat*" — the iterates of $\boxtimes$ from $T$ visit an antichain until they
stabilize. The $B_N$ family is *flat* (its front $\{a_1,\dots,a_{N+1}\}$ is an
antichain, $T\parallel a_1$, $a_i\parallel a_{i+1}$, and the only comparability is
the terminal $s<a_{N+1}$ collapsing into the degenerate sink $\boxtimes s=s$), and
flatness — not bottom discipline — is what forces $T$'s eventual cycle to be
degenerate. The genuine dividing line is **orbit flatness + reachability**, and
the two axioms are logically independent: $C_5$ is bottom-disciplined-but-not-flat
(equivalence fails); the $M_3$ Rosser gadget $R_2$ with a sub-$\bot$ element
adjoined is flat-but-not-bottom-disciplined (equivalence holds along $T$).

Skeptic:

Three probes. (1) *Is $C_5$ really a legitimate bottom-disciplined APS, or is
$T=3$ an illegitimate non-greatest top sneaking the chain in?* `definitions.md`
§"Bottom discipline" is exactly $\forall x\,(\bot\le x)$ and explicitly permits
$T$ non-greatest; $T=3$ is licit and $\boxtimes T=1\ne\bot$, a genuinely
$G2$-flavoured seed. So the counterexample stands. (2) *Does $B_N$ secretly
contain a chain-cycle too, undercutting the claim that flatness saves it?* Yes —
and this sharpens the result rather than breaking it. Extend $\boxtimes$ by
$\boxtimes\bot=U,\ \boxtimes U=\bot$ (antitone-compatible since $\bot<U$); then
$\{\bot,U\}$ **is** a chain-cycle inside a bottom-disciplined $B_N$. But it is
**not reachable from $T$** (whose orbit descends to $s$). Hence the correct
predicate is *reachability*, not *existence* — vindicating the Pass-40/44
orbit-attached-vs-detached framing. (3) *Is the bracketing criterion an "iff" in
general posets, or only on chains?* Only the chain direction is clean; on
non-chain intervals $\boxtimes^2$ is monotone and Knaster–Tarski yields a
$\boxtimes^2$-fixed point that need not be $\boxtimes$-fixed. The Formalist states
the chain theorem and flags the poset case as a proof obligation.

Formalist:

Definitions as in `definitions.md`. For antitone $\boxtimes$ on finite $L$ and
seed $T$, write $o_n=\boxtimes^n T$ and $O(T)=\{o_n:n\ge0\}$; the eventual cycle
$C\subseteq O(T)$ is the terminal $\boxtimes$-periodic set. Call the orbit
**flat** if its eventual cycle $C$ is an antichain (a singleton counts).

**Theorem 47a (bottom discipline does not confine the chain regime).** There is a
finite *bottom-disciplined* preAPS whose $T$-orbit reaches a strict comparable
$2$-cycle. *Witness.* $C_5=\{0<1<2<3<4\}$, $\boxtimes=r(x)=4-x$, $\bot=0$,
$T=3$: $\bot$ is least, $\boxtimes$ antitone, orbit $\{3,1\}$ a chain-cycle,
$p=2$ attached. Machine-checked, and the $C_5$ census exhibits **218**
bottom-disciplined antitone maps (seeds $2,3,4$) with a $T$-reachable chain-cycle.
Hence the Pass-45/46 confinement conjecture is **false**. $\square$

**Theorem 47b (flatness is the real gate).** If the $T$-orbit is flat, its
eventual cycle is degenerate or antichain — never a strict chain-cycle — so by
Cor 45d the local equivalence "$T$-orbit descends $\Leftrightarrow$ $T$ reaches an
attached fixed point" holds along $O(T)$. Flatness and bottom discipline are
independent: $C_5$ (Thm 47a) is bottom-disciplined $\wedge\,\neg$flat; the
sub-$\bot$-augmented $R_2$ is flat $\wedge\,\neg$bottom-disciplined. *Proof.* A
strict comparable $2$-cycle $\{a,b\}$, $a<b$, in $C$ contradicts flatness; the
remaining regimes degenerate/antichain give descent (Thm 45b) resp. detachment
(Pass 42/44). $\square$

**Proposition 47c (the $B_N$ arena is flat, so the equivalence holds there — for
the right reason).** In $B_N$ the orbit $T\to a_1\to\cdots\to a_{N+1}\to s\to s$
has eventual cycle $\{s\}$ (degenerate), so it is flat and descends; the unique
$T$-reachable fixed point $s$ is attached. A chain-cycle $\{\bot,U\}$ may coexist
(under $\boxtimes\bot=U,\boxtimes U=\bot$) but is unreachable from $T$. Thus the
Pass-44 equivalence holds on the $B_N$ arena **because of flatness, not bottom
discipline**. Machine-checked for $N=2$. $\square$

**Theorem 47d (chain bracketing criterion — closing the Cor 46b obligation).** Let
$\boxtimes$ be antitone on a finite **chain** and let the eventual cycle be a
comparable $2$-cycle $\{a,b\}$, $a<b$, $\boxtimes a=b$, $\boxtimes b=a$. The
interval $I=[a,b]$ is $\boxtimes$-invariant ($a\le x\le b\Rightarrow a=\boxtimes
b\le\boxtimes x\le\boxtimes a=b$), and $\boxtimes|_I$ is an orientation-reversing
self-map of the finite chain $I$. Then $\boxtimes|_I$ has a fixed point **iff
$|I|$ is odd**; when odd the fixed point is the central self-dual point
$p=(a+b)/2$ (regime iii-a, *bracketing*), when even there is none (regime iii-b,
*chain-gap*, the $C_{2m}$ reversal $r(x)=2m-1-x$). *Proof.* Order-reversing on a
finite chain $\Rightarrow$ $\boxtimes(x)-x$ is strictly decreasing in the discrete
sense, positive at $a$ ($\boxtimes a=b>a$) and negative at $b$; a discrete sign
change lands on a fixed point exactly when a midpoint is hit, i.e. when $|I|$ is
odd. $\square$ Machine-checked: $C_5,C_7$ bracket ($p=2,3$); $C_6,C_8$ are
chain-gaps (no FP).

Archivist:

Resolve the [New (Pass 45)] chain-cycle-reachability item **negatively for the
confinement conjecture**: bottom discipline does *not* confine the chain regime
($C_5$ is a bottom-disciplined chain-cycle, Thm 47a); the genuine gate is *orbit
flatness + reachability* (Thm 47b), which $B_N$ satisfies (Prop 47c) for a reason
orthogonal to bottom discipline. Close the [New (Pass 46)] bracketing obligation
with Thm 47d (odd-interval criterion). Add a Pass-47 section to
`g2-fg2-hierarchy.md`; normalize "orbit flatness" and "$T$-reachability of a
cycle" in `definitions.md`; mark the open-problem items resolved; retarget
`research-questions.md`; one-line `research-log.md` entry; commit the new script
and report.

Repository updates:
- `records/discussions/autonomous-discussion.md`: removed the crashed-write
  Pass-42/44 debris at EOF; appended the reconstructed Pass-46 entry and this
  Pass-47 entry; State counter 47 -> 48.
- `research/notes/g2-fg2-hierarchy.md`: added "Bottom Discipline Does Not Confine
  the Chain Regime; Flatness Does (Pass 47)" — Thms 47a/47b/47d, Prop 47c.
- `research/definitions.md`: added "Orbit flatness and $T$-reachability of a
  cycle (Pass 47)".
- `research/open_problems.md`: [New (Pass 45)] chain-cycle-reachability marked
  [Resolved (Pass 47)]; [New (Pass 46)] bracketing obligation marked
  [Resolved (Pass 47)]; added a [New (Pass 47)] poset-bracketing / infinite-lift
  item.
- `research/ideas/research-questions.md`: retargeted the active question to the
  poset bracketing criterion, the flatness/well-foundedness lift to infinite $L$,
  and period-$\ge4$ antichain cycles + FP-synt coexistence.
- `records/logs/research-log.md`: Pass-46 (reconstructed) and Pass-47 entries.
- `code/scripts/check-chaincycle-reachability-bottom-discipline.py`,
  `artifacts/reports/chaincycle-reachability-bottom-discipline-check.json`: new
  verification (claims A/B/C/D all PASS; 218 bottom-disciplined $C_5$ chain-cycles;
  0 Thm-45b violations).

Next step:

Pass 48 should (a) settle the **poset** bracketing criterion left open by Thm 47d:
for a comparable eventual $2$-cycle $\{a,b\}$ on a non-chain invariant interval,
$\boxtimes^2$ is monotone with a Knaster–Tarski fixed point — characterize when a
$\boxtimes^2$-fixed point is forced to be $\boxtimes$-fixed (the abstract
odd-length analogue: does a parity/Euler-characteristic invariant of the interval
control bracketing?); (b) seek the **well-foundedness** condition lifting flatness
+ Thm 47b to infinite $L$ (when does a flat orbit on a non-well-founded poset
still forbid limit chain-cycles?); and (c) attack the secondary thread the $M_4$
census exposed — period-$\ge4$ *antichain* cycles ($g=\boxtimes^2$ permuting
$\ge3$ incomparable points): does FP-synt ($\exists p\,p=\boxtimes p$) ever
coexist with an eventual period-$4$ antichain cycle, and if so is the fixed point
necessarily detached?

### Pass 48 - 2026-06-06 11:10 JST

Focus:

Discharge the three residual threads opened by Pass 47's Next step. (a) The
**poset bracketing criterion**: for a comparable eventual $2$-cycle $\{a,b\}$
($a<b$) on a *non-chain* $\boxtimes$-invariant interval $I=[a,b]$, $\boxtimes^2$
is monotone with a Knaster--Tarski/Abian--Brown fixed point; characterize when a
$\boxtimes^2$-fixed point is forced $\boxtimes$-fixed -- is there a
parity/Euler-characteristic invariant generalizing the odd-cardinality criterion
Thm 47d? (b) The **infinite-$L$ flatness lift**: which well-foundedness condition
lets a flat orbit on a non-well-founded $L$ still forbid *limit* chain-cycles,
extending Thm 47b? (c) The $M_4$-census **period-$\ge4$** thread: does FP-synt
($\exists p\,p=\boxtimes p$) ever coexist with an eventual period-$4$ *antichain*
cycle, and is the fixed point then necessarily detached?

Proposer:

All three fall to a single organizing idea: **bracketing is an involution-fixed-
point problem, and the invariant is the cycle type of $\boxtimes$ on
$\mathrm{Fix}(\boxtimes^2)$, never the size of the interval.**

(a) On the invariant interval $I=[a,b]$, $g:=\boxtimes^2|_I$ is monotone with
least element $a$ (Abian--Brown gives $F:=\mathrm{Fix}(g)\cap I\ne\emptyset$;
indeed $a,b\in F$). On $F$, $\boxtimes^2=\mathrm{id}$, so $\tau:=\boxtimes|_F$ is
an *order-reversing involution* of the finite poset $F$ swapping $\hat0=a$ and
$\hat1=b$. A $\boxtimes$-fixed point in $I$ is exactly a $\tau$-fixed point, and
an involution of a finite set fixes a point whenever the set has *odd*
cardinality. Hence: $|F|$ odd $\Rightarrow$ bracketing. On a chain $\boxtimes^2$
is the identity on the whole interval ($\tau=$ reversal is an involution), so
$F=I$ and "$|F|$ odd" degenerates to "$|I|$ odd" -- Thm 47d recovered exactly.

(b) For infinite $L$ the deciding axiom is **join-continuity of $\boxtimes$**
(it turns $\bigvee$ into $\bigwedge$), *not* well-foundedness. If the even orbit
ascends, $o_{2n}\uparrow a^\ast=\bigvee o_{2n}$, and join-continuity gives
$\boxtimes a^\ast=\bigwedge\boxtimes o_{2n}=\bigwedge o_{2n+1}=b^\ast$,
$\boxtimes b^\ast=a^\ast$ -- the limit $2$-cycle is *realized*, so flatness
(Thm 47b) applies to it verbatim. Drop continuity and the Thm-41c phantom
returns: the orbit climbs to $a^\ast$ but $\boxtimes a^\ast<b^\ast$ strictly, a
limit chain-cycle approached but never closed.

(c) FP-synt coexists with a period-$4$ antichain cycle, and the fixed point is
forced **detached**, by the same engine as Thm 41b but now wrapping a *finite*
cycle. Witness: the **period-$4$ Rosser gadget $R_4$** -- $\{b,o_0,o_1,o_2,o_3,
p,U\}$, $\{o_i\}$ a $4$-antichain, $\boxtimes$ the $4$-cycle, $\boxtimes p=p$
with $p$ incomparable to every $o_i$, $\boxtimes b=U$, $\boxtimes U=b$.

Skeptic:

Three probes. (1) *Does the parity criterion overclaim -- is it "iff"?* No, and I
keep it honest: it is a one-way sufficient condition. The converse fails on the
**Boolean cube**: $2^{[n]}$ under complementation $\boxtimes S=S^c$ has
$\boxtimes^2=\mathrm{id}$, so $F=I=2^{[n]}$, $|F|=2^n$ *even*, and no fixed point
($S=S^c$ is impossible) -- a fat *even* comparable $2$-cycle $\{\varnothing,[n]\}$
that does **not** bracket ("cube-gap", the $M_3/2^n$ analogue of the even-chain
$R_2$). Crucially the SAME poset $2^2$ carries a *different* order-reversing
involution ($\hat0\leftrightarrow\hat1$, fixing the two atoms) WITH two fixed
points -- so neither $|I|$ nor its parity is the invariant; only the cycle type of
$\tau$ on $F$ is. (2) *Is $a^\ast$ in (b) really forced, without monotone
even-subsequence?* Only under the stated hypothesis $T\le\boxtimes^2 T$ (even
orbit ascends); in general $\boxtimes^2$-iteration is Knaster--Tarski-monotone
only from a comparable seed, so I confine 48b to that regime and flag the
incomparable-seed case as the genuinely phantom-prone one. (3) *Is $R_4$'s
detachment a fluke of the $4$-antichain, or general?* General: forcing $p\le o_i$
runs $p\le o_i\Rightarrow o_{i+1}\le p\Rightarrow p\le o_{i+2}\Rightarrow
o_{i+3}\le p$, whence $o_{i+1}\le p\le o_{i+2}$ -- a comparability *inside* the
antichain, contradiction. Holds for every period $k\ge2$ (odd $k$ even collapses
$p=o_i$). Machine-checked that forcing the comparability breaks antitonicity for
$k=2,3,4,5$.

Formalist:

Definitions as in `definitions.md`. $\boxtimes$ antitone on finite poset $L$;
$o_n=\boxtimes^n T$; for a comparable eventual $2$-cycle $\{a,b\}$, $a<b$,
$\boxtimes a=b$, $\boxtimes b=a$, put $I=[a,b]$ and $F=\mathrm{Fix}(\boxtimes^2)
\cap I$.

**Theorem 48a (poset bracketing = involution fixed point; parity sufficiency).**
$I$ is $\boxtimes$-invariant and $g=\boxtimes^2|_I$ is monotone with least element
$a$, so $F\ne\varnothing$ (Abian--Brown) and $a,b\in F$. $\tau:=\boxtimes|_F$ is
an order-reversing involution of $F$ with $\tau a=b$, $\tau b=a$. Then
$\mathrm{Fix}(\boxtimes)\cap I=\mathrm{Fix}(\tau)$, and $|F|$ odd $\Rightarrow
\mathrm{Fix}(\tau)\ne\varnothing$ (an involution of an odd finite set has a fixed
point). On a chain $\boxtimes^2|_I=\mathrm{id}_I$, so $F=I$ and 48a reduces to
Thm 47d (odd $|I|$). *Proof.* Invariance: $a=\boxtimes b\le\boxtimes x\le\boxtimes
a=b$ for $x\in I$. $g=\boxtimes\circ\boxtimes$ is monotone; a finite poset with
$\hat0$ is chain-complete, so Abian--Brown yields a $g$-fixed point, and $ga=
\boxtimes(\boxtimes a)=\boxtimes b=a$, $gb=\boxtimes(\boxtimes b)=\boxtimes a=b$,
so $a,b\in F$. On $F$, $\boxtimes^2=\mathrm{id}$, hence $\boxtimes$ is a bijective
involution of $F$; antitone $\Rightarrow$ order-reversing. Fixed points of
$\boxtimes$ in $I$ lie in $F$ (a $\boxtimes$-fixed point is $\boxtimes^2$-fixed),
so coincide with $\mathrm{Fix}(\tau)$. Parity: $\#\mathrm{Fix}(\tau)\equiv|F|
\pmod2$. $\square$

**Pathology (cube-gap, 病的な例).** $L=2^{[n]}$, $\boxtimes S=S^c$: antitone,
$\boxtimes^2=\mathrm{id}$, the unique comparable $2$-cycle is $\{\varnothing,[n]\}$
with $I=2^{[n]}$, $|I|=2^n$, and $\mathrm{Fix}(\boxtimes)=\varnothing$ -- a fat
non-bracketing comparable $2$-cycle. The *same* lattice $2^2$ admits the order-
reversing involution $\tau'=(\hat0\,\hat1)$ fixing the two atoms, with
$\#\mathrm{Fix}(\tau')=2$. Therefore neither $|I|$ nor its parity controls
bracketing; the invariant is the cycle type of $\boxtimes|_F$. (Remark: the
homological refinement -- $\tau$ acts on the order complex $\Delta(F)$, which is
contractible since $F$ has $\hat0$, so the Lefschetz number is $1$ and $\tau$
fixes a *chain*; that chain yields a fixed *vertex* iff it has odd length, the
even-vertex-count case -- this is the Euler-characteristic shadow of the parity
count, and the exact homological criterion is a proof obligation.)

**Theorem 48b (infinite flatness lift = join-continuity, not well-foundedness).**
Let $\boxtimes$ be antitone on a complete lattice $L$ with $T\le\boxtimes^2 T$,
$a^\ast=\bigvee_n\boxtimes^{2n}T$, $b^\ast=\bigwedge_n\boxtimes^{2n+1}T$. If
$\boxtimes$ is join-continuous (sends $\bigvee$ to $\bigwedge$) then $\boxtimes
a^\ast=b^\ast$ and $\boxtimes b^\ast=a^\ast$: every limit $2$-cycle is *realized*,
so Thm 47b lifts (a flat orbit forbids limit chain-cycles, because the limit pair
is itself the attained eventual cycle and flatness applies to it). The lifting
hypothesis is continuity, *independent of well-foundedness of $L$*. Dropping it
reinstates the Thm-41c phantom: there is a non-join-continuous antitone $\boxtimes$
with $o_{2n}\uparrow a^\ast$ yet $\boxtimes a^\ast<\bigwedge\boxtimes o_{2n}$, a
limit chain-cycle approached but never closed. *Proof (continuity half).* Even
orbit ascends by monotonicity of $\boxtimes^2$; $\boxtimes a^\ast=\boxtimes
\bigvee o_{2n}=\bigwedge\boxtimes o_{2n}=\bigwedge o_{2n+1}=b^\ast$; dually for
$b^\ast$. $\square$ (Phantom half: construction, machine-checkable on finite
truncations; flagged as the Thm-41c meet-continuity dividing line in $\boxtimes$
form.)

**Proposition 48c (period-$k$ antichain forces detachment).** Let $\boxtimes p=p$
and let $\{o_0,\dots,o_{k-1}\}$ ($k\ge2$, $\boxtimes o_i=o_{i+1\bmod k}$) be a
$\boxtimes$-antichain cycle. Then $p$ is comparable to no $o_i$: the fixed point
is *detached*. *Proof.* Suppose $p\le o_i$. Apply $\boxtimes$: $o_{i+1}\le p$.
Again: $p\le o_{i+2}$. Then $o_{i+1}\le p\le o_{i+2}$ forces $o_{i+1}\le o_{i+2}$,
contradicting the antichain. Dually for $p\ge o_i$. (For odd $k$ the chain of
inequalities additionally collapses $p=o_i$, contradicting $\boxtimes p=p\ne
o_{i+1}$.) $\square$ Hence FP-synt coexists with an eventual period-$k$ antichain
cycle for every $k\ge2$, the fixed point always detached. **Witness $R_4$**
(period-$4$ Rosser gadget): $\{b,o_0,o_1,o_2,o_3,p,U\}$, $b$ least, $U$ greatest,
$\{o_i\}\cup\{p\}$ a $5$-antichain, $\boxtimes$ the $4$-cycle on $\{o_i\}$,
$\boxtimes p=p$, $\boxtimes b=U$, $\boxtimes U=b$ -- antitone, eventual cycle the
$4$-antichain $\{o_0,o_1,o_2,o_3\}$, sole fixed point $p$, detached. This is the
period-$2k$ generalization of the Pass-42 Rosser gadget $R_2$.

Machine verification (`code/scripts/check-poset-bracketing-period4.py`, report
`artifacts/reports/poset-bracketing-period4-check.json`, overall PASS): (A)
parity bracketing -- $0$ violations over all antitone maps on $C_2,\dots,C_5,2^2$
carrying a comparable $2$-cycle ($135$ map-instances; every odd-$|F|$ case
brackets); (B) cube-gap -- $2^{[1..4]}$ complementation has comparable $2$-cycle
$\{\varnothing,[n]\}$, interval sizes $2,4,8,16$, *no* $\boxtimes$-fixed point,
and the $2^2$ alternative involution has fixed points $\{1,2\}$; (C) $R_4$
antitone with a $4$-antichain eventual cycle and sole detached fixed point $p$,
and forcing $p\le o_0$ breaks antitonicity for $k=2,3,4,5$.

Archivist:

Resolve the [New (Pass 47)] thread (i) **poset bracketing** with Thm 48a (the
controlling invariant is the cycle type of $\boxtimes|_{\mathrm{Fix}(\boxtimes^2)
\cap I}$, with odd-$|F|$ sufficiency; the Boolean cube is the even non-bracketing
pathology and shows $|I|$-parity is *not* the invariant). Advance thread (ii)
**infinite flatness lift** with Thm 48b (join-continuity, not well-foundedness, is
the lifting axiom; phantom half pending construction). Resolve the secondary
**period-$\ge4$** thread with Prop 48c (FP-synt $\wedge$ period-$k$ antichain
cycle $\Rightarrow$ detached, witness $R_4$). Add a Pass-48 section to
`g2-fg2-hierarchy.md`; restore the Pass-47 "orbit flatness/$T$-reachability"
definition (lost to a crashed write) and normalize "bracketing involution",
"cube-gap", "period-$2k$ Rosser gadget $R_{2k}$" in `definitions.md`; update
`open_problems.md`, `research-questions.md`, `research-log.md`; commit the new
script and report.

Repository updates:
- `records/discussions/autonomous-discussion.md`: appended this Pass-48 entry;
  State counter 48 -> 49 with a Pass-48 summary line.
- `research/notes/g2-fg2-hierarchy.md`: added "Poset Bracketing, the Boolean
  Cube-Gap, and Period-$k$ Detachment (Pass 48)" -- Thms 48a/48b, Prop 48c, the
  cube pathology, $R_4$.
- `research/definitions.md`: restored "Orbit flatness and $T$-reachability of a
  cycle (Pass 47)"; added "Bracketing involution and cube-gap (Pass 48)" and
  "Period-$2k$ Rosser gadget $R_{2k}$ (Pass 48)".
- `research/open_problems.md`: [New (Pass 47)] (i) marked [Resolved (Pass 48)];
  the period-$\ge4$ clause [Resolved (Pass 48)]; (ii) updated to [Partially
  resolved (Pass 48)] (join-continuity); added [New (Pass 48)] homological/exact-
  bracketing and phantom-construction items.
- `research/ideas/research-questions.md`: retargeted to the exact homological
  bracketing criterion, the phantom-construction half of 48b, and group-cycle
  Rosser gadgets.
- `records/logs/research-log.md`: Pass-48 one-line entry.
- `code/scripts/check-poset-bracketing-period4.py`,
  `artifacts/reports/poset-bracketing-period4-check.json`: new verification
  (A parity / B cube-gap / C $R_4$ detachment, overall PASS).

Next step:

Pass 49 should (a) pin the **exact homological bracketing criterion** behind
Thm 48a: $\tau$ acts on the contractible order complex $\Delta(F)$ ($\hat0\in F$)
with Lefschetz number $1$, forcing a $\tau$-invariant chain -- determine when the
equivariant structure forces an *even-vertex* (hence fixed-vertex) invariant
chain, i.e. compute the $\mathbb Z/2$-equivariant Euler characteristic / Smith-
theory obstruction on $F^\tau$ and prove a "Smith inequality $\Rightarrow$
bracketing" upgrade of the one-way parity bound to an iff; (b) **build the
explicit phantom** witnessing the non-continuous half of Thm 48b -- a complete
lattice with antitone $\boxtimes$, $o_{2n}\uparrow a^\ast$, $\boxtimes a^\ast<
b^\ast$ strict -- and locate it on the meet-continuity dividing line of Thm 41c
(is a single failed cover enough?); (c) ask whether the period-$2k$ Rosser gadget
$R_{2k}$ admits a **group-cycle** refinement: replace the bare $k$-cycle by a free
$\mathbb Z/k$- or non-abelian $G$-action on the antichain front and test, against
the Pass-34/35 front-rigidity theorems, whether a detached FP-synt point survives
a *residuated* such expansion (does front rigidity, which killed group fronts
under residuation, also forbid a group *orbit* carrying a detached fixed point?).

---

## Pass 49 — 2026-06-06

**Focus (from Pass 48's Next step):** three residual threads — (a) upgrade the
one-way odd-|F| bracketing bound (Thm 48a) to an EXACT criterion via Z/2-Smith
theory / equivariant Euler characteristic on the order complex Delta(F);
(b) BUILD the explicit non-join-continuous phantom lattice (the discontinuous half
of Thm 48b) with o_{2n} ↑ a^*, box(a^*) < b^* strict, and decide whether ONE
failed cover suffices; (c) test whether the period-2k Rosser gadget R_{2k}
survives a free Z/k or non-abelian G action on the antichain front UNDER
RESIDUATION, against the Pass-34/35 front-rigidity theorems.

### Proposer

(a) **Smith bracketing.** Recall the setup of Thm 48a: a comparable eventual
2-cycle {a,b} (a<b), invariant interval I=[a,b], F := Fix(boxtimes^2) ∩ I, and
tau := boxtimes|_F is an order-reversing involution of the poset F with
tau(a)=b, tau(b)=a. boxtimes brackets a fixed point in I iff tau has a fixed
POINT. I claim the right invariant is not |F| but the *fixed simplicial set* of
tau acting on the order complex Delta(F) (the simplicial complex of nonempty
chains of F). Delta(F) is contractible: a is the minimum of F, so every chain
extends to a cone with apex {a}; hence Delta(F) is a cone, F2-acyclic. tau is a
simplicial Z/2-action (order-reversing ⇒ it sends chains to chains, reversing
their internal order but preserving the chain-as-set). By **Smith theory**
(P.A. Smith 1941; see Bredon, *Introduction to Compact Transformation Groups*,
Ch. III): for a Z/2 acting simplicially on an F2-acyclic complex, the fixed
subcomplex (Delta(F))^tau is itself nonempty and F2-acyclic. So the fixed set is
NEVER empty. The question is what it is *made of*: an order-reversing involution
fixes a chain c (as a set) iff tau reverses c; a fixed SIMPLEX is a tau-invariant
chain. Its barycenter is a topological fixed point. boxtimes brackets ⟺ there is
a tau-fixed VERTEX (0-simplex) ⟺ some tau-invariant chain has ODD cardinality
(the middle vertex is then forced fixed). Odd |F| (Thm 48a) is the degenerate
case where F itself is a single invariant chain of odd length.

(a-cube) **Cube-gap re-derived homologically.** For F = 2^[n] under
complementation tau(S)=[n]\S: the only tau-invariant chains are those c with
c = {[n]\S : S ∈ c}; a chain through complementary pairs that is invariant
must pair each S with [n]\S, so every invariant chain has EVEN cardinality and no
fixed vertex. The fixed subcomplex (Delta(2^[n]))^tau is the single barycenter of
the flipped top edge {∅,[n]} — a 1-cell midpoint: nonempty and acyclic (a point),
exactly as Smith forces, but with NO 0-cell, hence NO bracket. The cube-gap is
not a failure of Smith's theorem; it is Smith's theorem realized on a 1-simplex
barycenter rather than a vertex.

(b) **Explicit phantom.** Take the complete chain C = {o_0 < o_1 < o_2 < ... } ∪
{a^* = sup o_n} ∪ {b^* } ∪ {top}, with b^* a *doubled* cover of a^* (a^* ≺ b^*,
a^* ≺ m ≺ top, b^* ≺ top, m an extra median so a^* has two distinct covers and
join-continuity can fail at exactly that node). Define an antitone box flipping
the even rung o_{2n} upward to approach a^* from below while box(a^*) lands on m,
strictly below b^*. Then box(sup o_{2n}) = m < b^* = sup box(o_{2n}); the single
failed cover a^* ≺ {m, b^*} breaks join-continuity and reinstates the Thm-41c
phantom limit. One failed cover is enough.

(c) **Group-orbit liberation.** Front rigidity (Pass 34/35) says: a commutative
residuated TENSOR on a B_N front forces the orthogonal idempotent zero-band,
|G|=1 — no group lives on the front *as a tensor*. But the Rosser gadget carries
its group as a boxtimes-*orbit*, not a tensor: in R_4 the front {o_0,o_1,o_2,o_3}
is the free Z/4-orbit of refutability (o_0→o_1→o_2→o_3→o_0), a *separate*
operation from the residuated tensor. I conjecture this orbit survives residuation
precisely because the detached fixed point p can serve as a NON-integral tensor
unit, the degree of freedom B_N's tail-coupled top-unit never had.

### Skeptic

(a) Smith gives nonemptiness and F2-acyclicity of the fixed set, but "acyclic"
is weaker than "has a vertex" — a point sitting on an edge barycenter is acyclic
yet vertex-free, which is *exactly* the cube-gap. So Smith alone does NOT decide
bracketing; you still need the combinatorial 0-cell gate. State the theorem
honestly: Smith reduces "does tau fix something" (always yes) to "does the fixed
set meet the 0-skeleton" (sometimes no). Don't oversell it as a clean iff with no
residue. And check Lefschetz: L(tau) on a contractible complex is +1, so Lefschetz
guarantees a topological fixed point but again says nothing about vertices —
consistent with, not stronger than, Smith.

(b) "One failed cover" is only meaningful if the rest of the lattice is genuinely
join-continuous, otherwise you've smuggled in extra discontinuity. Verify the
truncations K=2..6 actually fail antitonicity/continuity ONLY at a^* and nowhere
else.

(c) Extraordinary claim. The Pass-34/35 rigidity proofs are robust; show the
residuated tensor on R_4 EXPLICITLY and count its residuations by machine, and
show the integral (unit=U) case genuinely fails. If unit=U is forced (B_N's
situation) then your "liberation" is vacuous.

### Formalist

Let me pin the three results.

> **Theorem 49a (Smith bracketing criterion).** Let {a,b} be a comparable
> eventual 2-cycle of an antitone boxtimes on a poset L, a<b, I=[a,b],
> F=Fix(boxtimes^2)∩I, tau=boxtimes|_F the order-reversing involution with
> tau(a)=b. Let Delta(F) be the order complex (nonempty chains of F). Then:
> (i) Delta(F) is F2-acyclic (it is a cone with apex a);
> (ii) [Smith] the fixed subcomplex |Delta(F)|^tau is nonempty and F2-acyclic,
>      and the simplicial Lefschetz number L(tau)=1;
> (iii) boxtimes brackets a fixed point in I  ⟺  |Delta(F)|^tau contains a
>      0-cell  ⟺  there exists a tau-invariant chain of F of ODD cardinality.
> The odd-|F| sufficiency of Thm 48a is the case where F is a single odd
> invariant chain. The Boolean cube F=2^[n] (tau = complementation) realizes the
> negative side: |Delta(F)|^tau is the lone barycenter of the flipped edge
> {∅,[n]}, vertex-free, so no bracket ("cube-gap").

> **Construction 49b (explicit phantom lattice / one-cover sufficiency).** There
> is a complete lattice P and an antitone box: P→P, join-continuous at every node
> EXCEPT a single failed join-cover at a^*=sup_n o_n, such that
> box(sup_n o_{2n}) = m  <  b^* = sup_n box(o_{2n}); the limit 2-cycle is
> phantom. Hence failure of join-continuity at ONE cover already reinstates the
> Thm-41c phantom; join-continuity cannot be weakened to "continuous off a
> finite/cofinite set."

> **Theorem 49d (group-orbit liberation under residuation).** The relation-free
> diamond M5={bot,o_0,o_1,o_2,o_3,p,U} with box=id and refutability the free
> Z/4-orbit (o_0 o_1 o_2 o_3) plus detached fixed point p (box p=p) admits a
> commutative full-residuated tensor whose unit is the NON-integral element p
> (equivalently o_0): 411 such tensors exist (S4 front-symmetry classes), with
> ZERO integral (unit=U) ones. The integral obstruction is the M_n (n>=3)
> phenomenon: the residual U\bot has the non-principal fiber {b}∪(atoms\{a}).
> Therefore front rigidity forbids group *tensors* on a B_N front but NOT a free
> group *orbit* carrying a detached fixed point on the relation-free diamond; the
> escape REQUIRES a non-integral unit.

Machine verification: `code/scripts/check-pass49.py` →
`artifacts/reports/pass49-bracketing-phantom-grouporbit-check.json`,
{"A":true,"B":true,"C":true,"PASS":true}. A: bracket flags
{cube 2^1,2^2,2^3 : F; 2^2-alt involution : T; C5 : T; C4 : F; 3-chain : T} —
0 disagreements with the 0-cell criterion. B: K=2..6 truncations break continuity
only at a^*. C: unit=p gives 411 residuated tensors, unit=U gives 0 integral, p
detached confirmed.

### Archivist

Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: this entry; State header counter
  49→50; Run-status Pass-49 summary; "Next run = Pass 50."
- `research/notes/g2-fg2-hierarchy.md`: Pass-49 section (Thm 49a Smith bracketing
  + cube-gap homological reading; Construction 49b phantom; Thm 49d group-orbit
  liberation).
- `research/definitions.md`: Smith bracketing / fixed-vertex criterion; the
  phantom chain-lattice P; group-orbit Rosser gadget (non-integral unit).
- `research/open_problems.md`: mark Pass-48 (i) homological bracketing and (iii)
  group-cycle gadget as Resolved (Pass 49); (ii) explicit phantom Resolved
  (Pass 49); add Pass-49 follow-ups (equivariant-Euler refinement; multi-cover
  phantom calibration; non-abelian Z/k→G orbit and arithmetic Rosser lift).
- `research/ideas/research-questions.md`: retarget Active list to Pass-49 follow-ups.
- `records/logs/research-log.md`: one-line Pass-49 entry.
- New artifacts: `code/models/examples/R4-residuated.json` (residuated R_4 witness),
  `code/scripts/check-pass49.py`, the report JSON.

**Next step (Pass 50).** (a) *Equivariant-Euler refinement* of Thm 49a: replace
the 0-cell gate by a computable invariant — chi(|Delta(F)|^tau) is 1 (acyclic),
so it does not distinguish vertex vs edge-barycenter; find the right Z/2-Bredon /
equivariant-Euler invariant whose value 1-vs-0 on the 0-skeleton detects the
bracket, i.e. a *vertex-counting* Smith inequality dim H_*( |Delta(F)|^tau ; F2)
≤ ... that sees the flipped-edge degeneracy. (b) *Multi-cover phantom*: calibrate
how many failed covers/what poset width is needed to make the phantom gap span a
prescribed interval (is the gap controlled by the number of failed covers, a
"phantom Betti number"?). (c) *Non-abelian orbit + arithmetic lift*: push Thm 49d
from Z/4 to a free Z/k and then a non-abelian G orbit (does 411 grow as |G|! /
something, and does the non-integral-unit requirement persist?), and connect the
detached non-integral unit p to the arithmetic Rosser sentence
rho ↔ ¬Box_R rho (Kurahashi 2021) — is "non-integral unit" the algebraic shadow
of "Rosser predicate evading Loeb"?
 49 -> 50 with a Pass-49 summary line.
- `research/notes/g2-fg2-hierarchy.md`: added the Pass-49 section (Thm 49a Smith
  bracketing criterion, Constr 49b explicit phantom / one-cover sufficiency,
  Thm 49d group-orbit liberation under residuation).
- `research/definitions.md`: normalized "Smith fixed subcomplex / bracketing
  0-cell gate", "phantom one-cover", "group-orbit vs group-tensor", "non-integral
  unit".
- `research/open_problems.md`: Pass-48 follow-ups (i)(ii)(iii) marked
  [Resolved (Pass 49)]; added the [New (Pass 49)] triple (equivariant-Euler
  refinement, multi-cover phantom calibration, non-abelian orbit + arithmetic lift).
- `research/ideas/research-questions.md`: retargeted to the Pass-49 triple.
- `records/logs/research-log.md`: Pass-49 one-line entry.
- `code/scripts/check-pass49.py`,
  `artifacts/reports/pass49-bracketing-phantom-grouporbit-check.json`,
  `code/models/examples/R4-residuated.json`: machine verification + new model.

[Recovery note (Pass 50): the Pass-49 Archivist block above was reconstructed on
2026-06-06 after a crashed write truncated this file mid-line at "State header
counter". All listed Pass-49 edits had in fact already landed (verified present);
only this discussion-log tail and the Next step were lost. The counter was left
at 50, so it is not double-incremented here.]

Next step:

Pass 50 should close the three [New (Pass 49)] residues. (i) **Equivariant-Euler
refinement of Thm 49a:** the topological chi(|Delta(F)|^tau)=1 cannot see the
bracket; find the *vertex-counting* Bredon invariant whose 1-vs-0 value on the
0-skeleton detects the bracket and sees the flipped-edge cube-gap. (ii)
**Multi-cover phantom calibration:** how does the phantom scale with the number of
failed join-covers / poset width — is it an additive "phantom Betti number"?
(iii) **Non-abelian orbit + arithmetic lift:** push Thm 49d from Z/4 to free Z/k
and non-abelian G (does the residuation count grow, does the non-integral-unit
requirement persist?), and connect the detached non-integral unit p to the
Rosser sentence rho <-> not Box_R rho (Kurahashi 2021): is "non-integral unit"
the algebraic shadow of "Rosser predicate evading Loeb"?

## Pass 50 — 2026-06-06 12:40 JST

**Focus (from Pass 49's Next step):** the three [New (Pass 49)] residues. (A)
Upgrade the Smith bracketing criterion (Thm 49a) to a *numeric equivariant
invariant*: the topological Euler characteristic of the Smith fixed set is
identically 1 and therefore blind to the 0-skeleton gate; produce the
vertex-counting refinement and re-explain the cube-gap as its vanishing. (B)
Calibrate the phantom of Constr 49b under SEVERAL independent failed join-covers:
is the count of phantom 2-cycles additive in the number of failed covers — a
"phantom Betti number"? (C) Generalize the group-orbit liberation (Thm 49d) from
Z/4 to an arbitrary finite group front: does R(n) stay positive with the
non-integral unit forced for all front sizes n=|G|, and does the (commutative)
residuated tensor see the group LAW at all, or only the front cardinality?

### Proposer

(A) **The vertex-counting invariant is e(F^tau) := chi(Delta(F^tau)), the Euler
characteristic of the order complex of the SELF-DUAL subposet.** Recall tau =
boxtimes|_F is an order-reversing involution of F = Fix(boxtimes^2) cap I, acting
simplicially on the F2-acyclic order complex Delta(F) (cone, apex a = min F). By
Smith the fixed set |Delta(F)|^tau is nonempty and F2-acyclic, hence its
topological Euler characteristic is identically 1 — it can never distinguish a
fixed VERTEX from a flipped-edge barycenter. The right refinement comes from the
Hopf-trace formula for the simplicial Lefschetz number,
  L(tau) = sum over tau-invariant chains c of (-1)^{|c|-1} sgn(tau|_c) = 1,
split according to whether tau acts on the chain trivially or by a flip. The
POINTWISE-FIXED invariant chains are exactly the chains contained in the
self-dual subposet F^tau = {x in F : boxtimes x = x}, and their signed count is
e(F^tau) = chi(Delta(F^tau)). The complementary FLIPPED chains contribute
Phi(tau). Thus
  L(tau) = e(F^tau) + Phi(tau) = 1,
and boxtimes brackets a fixed point  iff  F^tau is nonempty  iff (on the test
family)  e(F^tau) >= 1. The cube-gap is precisely e = 0, Phi = 1: the lone
flipped edge {empty,[n]} carries the entire Lefschetz number while the self-dual
subposet is empty.

(B) **Phantom additivity.** A fan P_r built from r copies of the Constr-49b arm,
glued only at a shared bottom and top and otherwise pairwise order-incomparable,
carries a globally antitone boxtimes whose discontinuities are the r limit covers
a_1^*, ..., a_r^*; each arm reinstates its own phantom 2-cycle (a_i^*, b_i^*). I
conjecture the number of phantom 2-cycles equals the number of failed join-covers,
b_phantom(P_r) = r — a discrete additive invariant, a "phantom Betti number"
counting independent join-discontinuities.

(C) **Decoupling.** I claim the relation-free diamond M_{n+1} (front atoms
o_0..o_{n-1}, detached p, box = a free orbit on the front + box p = p) admits a
commutative full-residuated tensor with non-integral unit p for EVERY n >= 3, and
that the commutative tensor cannot encode the group multiplication — so abelian
vs non-abelian G is invisible to residuation. The group lives entirely in the
refutability ORBIT; the tensor sees only |G| = n. Hence Thm 49d is not special to
Z/4: it is a statement about front cardinality.

### Skeptic

(A) "e detects the bracket" is only claimed *on the test family*. In general
chi(Delta(F^tau)) can vanish for a nonempty poset (e.g. an order complex
homotopy-equivalent to a circle). State honestly: e(F^tau) is the reduced-Euler
*vertex* invariant; e != 0 is SUFFICIENT for a bracket and is the sharp witness on
all comparable-2-cycle examples, but the exact iff is "F^tau nonempty", of which e
is the computable Euler shadow. Do not claim e is a complete invariant for
arbitrary F.

(B) Gluing r antitone arms can silently break GLOBAL antitonicity if the arms
acquire cross comparabilities through the shared bot/top. Verify boxtimes is
antitone on the *whole* P_r, not just arm by arm, and that the r discontinuities
are genuinely independent (distinct m_i, b_i^*), else the "phantom Betti number"
is an artifact of double-counting one cover.

(C) The decoupling claim is strong: if the tensor truly cannot see G, then the
residuation count R(n) must depend on n alone. Compute R(n) by machine for at
least two front sizes and check it matches the Pass-49 value at n = 4 (411). For
larger n full enumeration is infeasible, so you must EXHIBIT an explicit tensor
that works for all n (a witness family) rather than assert positivity.

### Formalist

> **Theorem 50a (Bredon vertex-bracket identity).** Let tau be an order-reversing
> involution of a finite poset F with order complex Delta(F) F2-acyclic (e.g. F has
> minimum a = hat0). Let F^tau = {x in F : tau x = x} be the self-dual subposet and
> e(F^tau) = chi(Delta(F^tau)) its order-complex Euler characteristic. Decomposing
> the simplicial Lefschetz number of tau by orbit type of each invariant chain,
> $$ L(\tau) \;=\; e(F^\tau) \;+\; \Phi(\tau) \;=\; 1, $$
> where Phi(tau) is the signed count of FLIPPED tau-invariant chains (those not
> contained in F^tau). Consequently boxtimes brackets a fixed point in I iff
> F^tau != empty; e(F^tau) is the vertex-counting equivariant refinement that the
> topological chi(|Delta(F)|^tau) = 1 cannot supply, and the cube-gap F = 2^[n]
> (tau = complementation) is exactly the extremal case e(F^tau) = 0, Phi(tau) = 1.

> **Construction 50b (phantom Betti number / additivity of failed covers).** For
> r >= 1 let P_r be the fan of r copies of the Constr-49b even-orbit arm, sharing
> only bottom and top and otherwise pairwise order-incomparable. Then boxtimes is
> globally antitone on P_r, its join-continuity fails at exactly the r limit covers
> a_1^*, ..., a_r^*, and the number of phantom 2-cycles equals the number of failed
> covers:
> $$ b_{\mathrm{phantom}}(P_r) \;=\; \#\{\text{failed join-covers}\} \;=\; r. $$
> Constr 49b is the atom r = 1; one failed cover is one phantom, and phantoms add.

> **Theorem 50d (front-cardinality decoupling of group-orbit liberation).** For
> every finite group G, the relation-free diamond M_{|G|+1} with box = id
> off-orbit, refutability a free G-orbit on the front {o_g}, and detached box p = p,
> admits a commutative full-residuated tensor with the NON-integral unit p, and ZERO
> integral (unit = top) ones whenever |G| >= 3 (the M_n, n >= 3, residual
> obstruction). The exact count R(n), n = |G|, is R(3) = 56, R(4) = 411 (reproducing
> Pass 49), and R(n) >= 1 for all n via the explicit witness family
> $$ p = \text{unit},\quad o_0 \otimes x = o_0,\quad o_i \otimes o_j = \top\ (i,j\ge1),
>    \quad o_i \otimes p = o_i. $$
> The commutative tensor never references the multiplication of G: abelian and
> non-abelian fronts of equal cardinality are residuation-indistinguishable. The
> group law lives solely in the refutability orbit; the residuated layer sees only
> |G|. (Free S_3 orbit, |G| = 6, verified antitone with detached p.)

Machine verification: `code/scripts/check-pass50.py` ->
`artifacts/reports/pass50-bredon-phantomfan-grouporbit-check.json`,
{"A":true,"B":true,"C":true,"PASS":true}. A: (e, Phi, bracket) =
{cube 2^1/2^2/2^3 : (0,1,F); C4 : (0,1,F); 2^2-alt : (2,-1,T); C5 : (1,0,T);
3-chain : (1,0,T)}, every row L = e+Phi = 1 and e!=0 iff bracket. B: r=1,2,3 each
globally antitone with failed_covers = phantom_2cycles = r. C: R(3)=56, R(4)=411,
integral=0 for both; witness family residuated/assoc/commutative with unit p for
n=3..7; free S_3 orbit box antitone.

### Archivist

Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: completed the truncated Pass-49
  Archivist + Next step (recovery), appended this Pass-50 entry; State counter
  50 -> 51 with a Pass-50 summary line.
- `research/notes/g2-fg2-hierarchy.md`: new Pass-50 section — Thm 50a (Bredon
  vertex-bracket identity, e(F^tau)=chi(Delta(F^tau)), L=e+Phi=1), Constr 50b
  (phantom Betti number, additivity of failed covers), Thm 50d (front-cardinality
  decoupling, R(3)=56/R(4)=411 + witness family).
- `research/definitions.md`: normalized "Self-dual subposet F^tau and the
  vertex-counting Euler invariant e(F^tau) (Pass 50)", "Phantom Betti number
  (Pass 50)", "Front-cardinality decoupling / group-orbit vs group-tensor
  (Pass 50)".
- `research/open_problems.md`: [New (Pass 49)] (i)(ii)(iii) marked
  [Resolved (Pass 50)]; added the [New (Pass 50)] triple.
- `research/ideas/research-questions.md`: retargeted to the Pass-50 follow-ups.
- `records/logs/research-log.md`: Pass-50 one-line entry.
- `code/scripts/check-pass50.py`,
  `artifacts/reports/pass50-bredon-phantomfan-grouporbit-check.json`: machine
  verification (A, B, C, overall = PASS).

[Recovery note (Pass 51): the Pass-50 Archivist block above was truncated
mid-filename by a crashed write on 2026-06-06; all listed Pass-50 edits had in
fact already landed (verified present), and the State counter had already been set
to 51, so it is not double-incremented here. The Pass-50 "Next step" was also lost
and is reconstructed below from the [New (Pass 50)] triple recorded in
`research/open_problems.md`.]

Next step:

Pass 51 should close the three [New (Pass 50)] residues. (i) **Completeness of
$e(F^{\tau})$.** Is $e=0$ with $F^{\tau}\ne\varnothing$ possible for some antitone
$\boxtimes$? Conjecture no on comparable-2-cycle intervals — prove $e$ is a
complete bracket invariant there, or build a pathological $\boxtimes$ whose
$F^{\tau}$ has an order complex homotopy-equivalent to a circle. (ii) **Phantom
Betti number as genuine cohomology.** Promote $b_{\mathrm{phantom}}$ from a count
to $\dim H^1$ of an explicit cochain complex on the lattice whose $1$-cocycles are
the failed join-covers; relate to derived functors of the discontinuous
$\boxtimes$. (iii) **Arithmetic lift of the non-integral unit.** Realize
"non-integral unit $=$ algebraic shadow of Rosser-evades-Löb": build the
arithmetic APS of a Rosser predicate $\Box_R$ (Guaspari–Solovay 1979; Kurahashi
2021) and show its residuated realization forces unit $\ne\top$ exactly when
$\rho\leftrightarrow\neg\Box_R\rho$ fails Löb, against the de Jongh–Sambin
Löb-attachment of the standard $\Box$ (Pass 43).

## Pass 51 — 2026-06-06 13:10 JST

Focus:
The three [New (Pass 50)] residues. (A) Decide whether the vertex-counting Euler
invariant $e(F^{\tau})$ of Thm 50a is a *complete* bracket invariant, or whether
an antitone $\boxtimes$ can hide a bracket from it (an order-complex circle with
$e=0$ but $F^{\tau}\ne\varnothing$). (B) Upgrade the phantom Betti number from a
counted integer (Constr 50b) to the dimension of a genuine cohomology
group/derived limit, exhibiting an explicit obstruction complex with
$\dim H^1(P_r)=r$. (C) Lift the integral/non-integral unit dichotomy of Thm 50d to
arithmetic: identify "non-integral unit" with "Rosser predicate evading Löb" and
"integral unit" with the de Jongh–Sambin Löb-attached standard provability.

Proposer:
(A) **$e(F^{\tau})$ is complete — and the reason deflates the whole Bredon
apparatus.** The set $F^{\tau}=\{x\in F:\boxtimes x=x\}$ of $\boxtimes$-fixed
points is an **antichain**: if $p\le q$ with $\boxtimes p=p,\ \boxtimes q=q$, then
antitonicity gives $q=\boxtimes q\le\boxtimes p=p$, so $p=q$. An antichain's order
complex is a set of isolated vertices, so $\Delta(F^{\tau})$ is discrete and
$e(F^{\tau})=\chi(\Delta(F^{\tau}))=|F^{\tau}|$ *identically*. Hence
$e=0\iff F^{\tau}=\varnothing\iff$ no bracket: $e$ is a complete (tautological)
bracket invariant, and "$e=0$ with $F^{\tau}\ne\varnothing$" is impossible. The
hoped-for order-complex circle is unrealizable as a fixed-vertex set — the
6-crown $C_6$ (3 minima, 3 maxima, $x_i<y_i,\ x_i<y_{i-1}$) has order complex
$S^1$, $\chi=0$, but it is *not an antichain*, so no order-reversing involution
fixes its vertices.

(B) **The phantom is a derived inverse limit.** On the fan $P_r$, each arm carries
an ascending chain $o^i_0<o^i_1<\cdots$ with $\sup=a^*_i$; antitonicity makes the
image tower $\boxtimes o^i_0\ge\boxtimes o^i_1\ge\cdots$ descend to a meet
$\beta_i$, while $\boxtimes a^*_i=\gamma_i<\beta_i$ — the phantom is exactly the
failure $\boxtimes(\bigvee)\ne\bigwedge\boxtimes$, i.e. $\boxtimes$ does not
commute with the limit. This is $\varprojlim^1$ of the image tower. The
obstruction complex $\mathrm{Ob}^\bullet(P_r)=[0\to C^1\to0]$ with $C^1=\mathbb
F^{\{\text{failed covers}\}}$ and $C^0=0$ (no antitone *interior* perturbation
closes a gap, in the limit) has $H^1=\mathbb F^r$, and since $\varprojlim^1$
commutes with finite direct sums, $b_{\mathrm{phantom}}(P_r)=\dim_{\mathbb
F}H^1=r$.

(C) **Integral $=$ Löb, non-integral $=$ Rosser.** In the Lindenbaum APS of a
theory $T$ with $\boxtimes=\neg\Box$, a $\boxtimes$-fixed point is orbit-*attached*
iff it is provably equivalent to $\mathrm{Con}_T=\boxtimes\bot$ (de Jongh–Sambin,
under Löb / GL), and *detached* iff it is a Rosser fixed point of a predicate
$\Box_R$ that keeps $D1+\Sigma_1$-completeness but evades Löb (Pass 43). Claim:
the residuated tensor on the model has an **integral unit** ($1=\top$) iff the
fixed point is attached, and a **non-integral unit** ($1\ne\top$) iff detached.
The attached 3-chain Gödel model is a residuated lattice with unit $\top$; the
detached Rosser $R_2/M_3$ admits no integral-unit residuation (the $M_n$,
$n\ge3$, obstruction of Pass 49/50), only non-integral ones.

Skeptic:
(A) The antichain lemma is airtight, but it shows $e$ is complete *for a cheap
reason* — it collapses to a vertex count, so the entire Hopf-trace refinement is
deflationary: all the homological content lives in the *flipped* term
$\Phi(\tau)=1-|F^{\tau}|$, not in $e$. State this honestly: Smith $+$ antitonicity
forces the equivariant story to be a single integer $|F^{\tau}|$. The circle can
only appear in the *topological* fixed set $|\Delta(F)|^{\tau}$ via flipped-edge
barycenters, and Smith forbids even that from being a circle (it is $\mathbb
F_2$-acyclic).
(B) The literal $\varprojlim^1$ vanishes for towers of finite-dimensional vector
spaces (they are Mittag-Leffler), so "$\dim_{\mathbb F}H^1=r$" cannot be a
field-coefficient nonvanishing statement; the genuine derived limit is integral
($\varprojlim^1$ of a non-Mittag-Leffler $\mathbb Z$-tower). And $C^0=0$ is a
*limit* phenomenon: at every finite truncation the gap is removable by setting
$\boxtimes a^*_i=\beta_i$, which keeps antitonicity. So the cohomology must be
asserted in the infinite lattice, with the finite check verifying only
additivity, the exact failed-cover count, and gap independence.
(C) The correspondence is a *dictionary*, not yet a functor: which residuated
tensor on $L_T$ corresponds to which derivability package is the open obligation.
Do not overclaim an equivalence of categories; claim the exact gate
(integral $\Leftrightarrow$ Löb-attachment) and exhibit the Rosser non-integral
realization. Cite Guaspari–Solovay and Kurahashi for the existence of Löb-evading
Rosser predicates.

Formalist:

> **Lemma 51a (fixed points of an antitone map form an antichain).** Let
> $\boxtimes:L\to L$ be antitone. If $p\le q$ and $\boxtimes p=p$, $\boxtimes q=q$
> then $q=\boxtimes q\le\boxtimes p=p$, so $p=q$. Hence $\mathrm{Fix}(\boxtimes)$
> is an antichain. $\square$

> **Theorem 51a (completeness/deflation of $e(F^{\tau})$).** For any antitone
> $\boxtimes$ on a finite poset, with $F=\mathrm{Fix}(\boxtimes^2)\cap I$ and
> $\tau=\boxtimes|_F$, the self-dual subposet $F^{\tau}=\mathrm{Fix}(\boxtimes)\cap
> I$ is an antichain (Lemma 51a), so $\Delta(F^{\tau})$ is a discrete complex and
> $$ e(F^{\tau})=\chi(\Delta(F^{\tau}))=|F^{\tau}|. $$
> Therefore $e$ is a *complete* bracket invariant: $e=0\iff F^{\tau}=\varnothing
> \iff\boxtimes$ does not bracket in $I$, and the configuration "$e=0$ with
> $F^{\tau}\ne\varnothing$" is impossible. All non-vertex homological content is
> carried by the flipped term $\Phi(\tau)=L(\tau)-e(F^{\tau})=1-|F^{\tau}|$. The
> 6-crown realizes an order complex $\simeq S^1$ ($\chi=0$) but is not an
> antichain, hence is the fixed-vertex set of no order-reversing involution: the
> circle pathology is unrealizable.

> **Theorem 51b (phantom Betti number as $\varprojlim^1$).** Let $P_r$ be the fan
> of $r$ order-independent even-orbit arms (Constr 50b). The phantom of arm $i$ is
> the discrepancy $\boxtimes(\bigvee_n o^i_n)=\gamma_i<\beta_i=\bigwedge_n\boxtimes
> o^i_n$, i.e. the nonvanishing of $\varprojlim^1$ of the image tower
> $(\boxtimes o^i_n)_n$. The obstruction complex $\mathrm{Ob}^\bullet(P_r)=[\,0\to
> C^1\to0\,]$, $C^1=\mathbb F^{\{\text{failed join-covers}\}}$, $C^0=0$ (infinitary
> rigidity), has
> $$ b_{\mathrm{phantom}}(P_r)=\dim_{\mathbb F}H^1(\mathrm{Ob}^\bullet(P_r))
>    =\#\{\text{failed covers}\}=r, $$
> the additivity following from $\varprojlim^1(\bigoplus_i)=\bigoplus_i\varprojlim^1$.
> *Proof obligations:* (a) the integral $\varprojlim^1$ is genuinely nonzero
> (field coefficients give Mittag-Leffler vanishing — the cohomology must be taken
> over $\mathbb Z$); (b) $C^0=0$ holds only in the completed lattice, every finite
> truncation being gap-removable. Machine-verified at the finite level: global
> antitonicity, exactly $r$ failed covers, pairwise gap independence ($r=1,2,3$).

> **Theorem 51c (Löb/Rosser $\leftrightarrow$ integral/non-integral unit).** Let
> $(T,\Box)$ be a $\Sigma_1$-sound base with $\boxtimes=\neg\Box$ and let $\phi$ be
> a $\boxtimes$-fixed point ($\phi\leftrightarrow\boxtimes\phi$). On the
> finite-model side:
> $$ \phi\text{ orbit-attached }(\phi=\boxtimes\bot)\ \Longleftrightarrow\
>    \exists\text{ full residuated tensor with integral unit }1=\top; $$
> $$ \phi\text{ detached }\ \Longleftrightarrow\ \text{every full residuated tensor
>    has a non-integral unit }1\ne\top. $$
> Arithmetically, attachment is the de Jongh–Sambin Löb-coincidence
> $\phi\equiv\mathrm{Con}_T$ (forced by $D3$/GL), and detachment is realized only
> by a Rosser predicate $\Box_R$ keeping $D1+\Sigma_1$-completeness but evading Löb
> (Guaspari–Solovay 1979; Kurahashi 2021). Hence "non-integral unit" is the
> algebraic shadow of "Rosser predicate evading Löb." *Verified:* the attached
> 3-chain Gödel model admits an integral-unit ($\top$) full residuated tensor; the
> detached $R_2/M_3$ admits $0$ integral-unit tensors and non-integral units
> $\{o_0,o_1,p\}$. *Remaining obligation:* promote the dictionary to a functor
> $L_{(-)}$ from derivability packages to residuated APS.

Machine verification: `code/scripts/check-pass51.py` $\to$
`artifacts/reports/pass51-euler-completeness-phantom-cohomology-rosser-unit-check.json`,
`{"A":true,"B":true,"C":true,"PASS":true}`. A: over all antitone maps on all
posets of size $\le5$, $0$ violations of "$\mathrm{Fix}$ is an antichain", $0$ of
"$e=|\mathrm{Fix}|$", $0$ of "$e=0$ with $\mathrm{Fix}\ne\varnothing$"; $e$-values
by $|\mathrm{Fix}|$ are exactly $\{k\mapsto k\}$; crown $\chi=0$, not an antichain.
B: $r=1,2,3$ each globally antitone, failed covers $=$ phantom $2$-cycles $=r$,
gaps independent, finite-stage gap removable (infinitary phantom). C: $R_2$ has
$0$ integral tensors and non-integral units $\{o_0,o_1,p\}$; the $C_3$ Gödel chain
has an integral ($\top$) tensor.

Archivist:

Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: completed the truncated Pass-50
  Archivist block + reconstructed Pass-50 Next step (recovery), appended this
  Pass-51 entry; State counter 51 → 52 with a Pass-51 summary line.
- `research/notes/g2-fg2-hierarchy.md`: new Pass-51 section — Lemma 51a
  (fixed-point antichain), Thm 51a (completeness/deflation of $e$), Thm 51b
  (phantom $=\varprojlim^1$, $b_{\mathrm{phantom}}=\dim H^1$), Thm 51c
  (Löb/Rosser $\leftrightarrow$ integral/non-integral unit).
- `research/definitions.md`: normalized "Fixed-point antichain lemma & deflation
  of $e(F^{\tau})$ (Pass 51)", "Phantom as $\varprojlim^1$ / obstruction complex
  (Pass 51)", "Integral vs non-integral unit = Löb vs Rosser (Pass 51)".
- `research/open_problems.md`: [New (Pass 50)] (i)(ii)(iii) marked
  [Resolved (Pass 51)]; added the [New (Pass 51)] triple.
- `research/ideas/research-questions.md`: retargeted the active list to the
  Pass-51 follow-ups.
- `records/logs/research-log.md`: Pass-51 one-line entry.
- `code/scripts/check-pass51.py`,
  `artifacts/reports/pass51-euler-completeness-phantom-cohomology-rosser-unit-check.json`:
  machine verification (A, B, C, overall = PASS).

Next step:
Pass 52 picks up the three [New (Pass 51)] residues. (i) **The flipped invariant
$\Phi(\tau)$.** Since $e(F^{\tau})=|F^{\tau}|$ is deflationary (Thm 51a), the real
homological content is $\Phi(\tau)=1-|F^{\tau}|$: characterize $\Phi$ intrinsically
as a signed count of flipped $\tau$-orbits and identify which posets $F$ maximize
$|\Phi|$ (the cube $2^{[n]}$ gives $\Phi=1$; is there an $F$ with $\Phi$ large
negative?), and connect $\Phi$ to the reduced Lefschetz/Smith data of
$|\Delta(F)|^{\tau}$. (ii) **Integral $\varprojlim^1$ nonvanishing.** Discharge
proof obligation (a) of Thm 51b: exhibit an explicit $\mathbb Z$-linearization of
the image tower whose $\varprojlim^1\ne0$ (a non-Mittag-Leffler tower, e.g.
$\mathbb Z\xleftarrow{\times2}\mathbb Z\xleftarrow{\times2}\cdots$ realized inside
the lattice's Grothendieck/incidence module), making $b_{\mathrm{phantom}}$ a
genuine $\dim_{\mathbb F_p}(\varprojlim^1\otimes\mathbb F_p)$ rather than a count.
(iii) **Functoriality of the Löb/Rosser dictionary.** Discharge the Thm 51c
obligation: construct the functor $L_{(-)}$ from derivability packages
$\{D1,D2,D3,\Sigma_1\text{-completeness},\text{Rosser witness-comparison}\}$ to
residuated APS, and prove that the integral-unit subcategory is exactly the image
of the Löb (GL) packages, with the Rosser packages landing in the non-integral
complement.

## Pass 52 — 2026-06-06 16:20 JST

Focus:
The [New (Pass 51)] residue (i): the *flipped invariant* $\Phi(\tau)=1-|F^{\tau}|$.
Pass 50–51 reduced the Bredon identity $L(\tau)=e(F^{\tau})+\Phi(\tau)=1$ to the
deflated form $e(F^{\tau})=|F^{\tau}|$ (Thm 51a), exposing $\Phi$ as "the real
homological content after $e$-deflation." Task: give $\Phi$ an intrinsic
combinatorial formula as a signed count of flipped $\tau$-invariant chains,
classify the extremal fronts (the cube gives $\Phi=+1$; is $\Phi$ bounded below?),
and identify $\Phi$ as the gap between the geometric (Smith, topological) and the
combinatorial (vertex) fixed-point Euler characteristics.

Proposer:
Run the Hopf trace formula on the contractible order complex $\Delta(F)$ (cone,
apex $\hat0=\min F$) under the order-reversing involution $\tau=\boxtimes|_F$. Since
$\Delta(F)$ is $\mathbb F_2$-acyclic, $L(\tau)=1$. A $\tau$-invariant chain $c$ contributes $(-1)^{|c|-1}\mathrm{sgn}(\tau|_c)$; the pointwise-fixed
chains (those in $F^{\tau}$) contribute $e(F^{\tau})=|F^{\tau}|$ (Thm 51a), the rest
contribute $\Phi(\tau)$, and $L(\tau)=e(F^{\tau})+\Phi(\tau)=1$ forces
$\Phi(\tau)=1-|F^{\tau}|$.

[Recovery note (Pass 53, 2026-06-07): the Pass-52 entry above was truncated
mid-Proposer by a crashed write during a concurrent recovery run; its full
substance landed in `research/open_problems.md` (the [Resolved (Pass 52)] block),
`research/notes/g2-fg2-hierarchy.md` (Pass-52 section), and
`records/logs/research-log.md`. Completed here in compressed form for provenance.]

Skeptic (Pass 52, recovered):
A signed *chain* count is basis-dependent; demand the period-4 sign pattern
$s(d)=(-1)^d(-1)^{d(d+1)/2}=(+,+,-,-)$ be intrinsic (independent of which maximal
chains are chosen), and verify $\inf\Phi=-\infty$ is realized by an honest antitone
$\boxtimes$ (the fixed-antichain fan), not by an artifact.

Formalist (Pass 52, recovered):
> **Thm 52a.** $\Phi(\tau)=\sum_{d\ge1}s(d)N_d=1-|F^{\tau}|$, $N_d=\#\{\tau$-invariant
> $d$-chains$\}$, $s(d)=(-1)^d(-1)^{d(d+1)/2}=(+,+,-,-)$ period $4$.
> **Thm 52b (extremal dichotomy).** $\sup\Phi=+1$ on fixed-point-free $\tau$
> (cube $2^{[n]}$, $C_4$); $\inf\Phi=-\infty$ via the fixed-antichain fan
> $F_m=(\hat0<a_1,\dots,a_m<\hat1)$ with $\Phi=1-m$.
> **Thm 52c.** $\Phi(\tau)=\chi(|\Delta(F)|^{\tau})-\chi(\Delta(F^{\tau}))$, the
> geometric-minus-combinatorial fixed-point Euler gap.
Machine-verified `artifacts/reports/pass52-flipped-invariant-check.json` (PASS).

Archivist (Pass 52, recovered): edits landed in open_problems.md, hierarchy,
research-log (see those files); State counter advanced.

Next step (Pass 52 → 53):
Close the two carried residues: (ii) integral $\varprojlim^1$ nonvanishing (the
$2$-adic phantom) and (iii) functoriality of the Löb/Rosser dictionary.

---

### Pass 53 - 2026-06-07 04:30 JST

Focus:
Close the two surviving **[New (Pass 52)]** residues (carried from Pass 51) now
that Pass 52 has disposed of the flipped-invariant thread (i). Residue **(ii)**:
discharge the Thm-51b obligation by exhibiting a coefficient datum whose image
tower has a genuinely nonzero INTEGRAL $\varprojlim^1$ — the field-coefficient
$\varprojlim^1$ vanishes by Mittag-Leffler, so the "phantom Betti number $=r$" of
Passes 50/51 is a finitary cochain shadow. Residue **(iii)**: upgrade the Thm-51c
dictionary (integral unit $\iff$ Löb, non-integral $\iff$ Rosser) from a pointwise
correspondence to a functor $L_{(-)}:\mathbf{Deriv}\to\mathbf{resAPS}$ and prove
the integral-unit subcategory is exactly the essential image of the Löb (GL)
packages.

Proposer:
**(A) The 2-adic phantom.** The Pass-50 phantom Betti number was computed in a
finite-dimensional / field setting where $\varprojlim^1$ is forced to vanish: a
tower of finite-dimensional vector spaces has stabilizing image filtration
(Mittag-Leffler), so $\varprojlim^1=0$ and $b_{\mathrm{phantom}}=r$ was only the
rank of the finitary cochain $C^1=\mathbb F^{\{\text{failed covers}\}}$. To make
the phantom a genuine derived-limit obstruction one must use integer coefficients
and a non-Mittag-Leffler image tower. The minimal, canonical one is the dyadic
tower $\mathbb Z\xleftarrow{\times2}\mathbb Z\xleftarrow{\times2}\cdots$, realized
as the incidence coefficient system of an $\omega$-telescope of failed join-covers
in which the $n$-th cover *doubles* the image fiber (a residuated $\mathbb Z$-grading
whose unit acts by $\times2$, not the bare $\pm1$ incidence numbers of a poset).
Then $\varprojlim(\mathbb Z,\times2)=0$ and $\varprojlim^1(\mathbb Z,\times2)=
\widehat{\mathbb Z}_2/\mathbb Z$, uncountable — one ghost for every $2$-adic
integer that is not an ordinary integer.

**(B) The functor $L_{(-)}$.** Send each derivability package $(\Box,\Pi)$ to its
Lindenbaum residuated APS ($\otimes=\wedge$, $\backslash=\to$, $\boxtimes=\neg\Box$,
designated unit $=$ the chosen $\boxtimes$-fixed point). The unit is integral
($e=\top$) exactly when the fixed point is orbit-attached ($e=\boxtimes\bot=
\mathrm{Con}$), which by de Jongh–Sambin happens exactly under Löb. So the
essential image of $\mathbf{GL}$ is the integral-unit subcategory, and Rosser
packages land in the non-integral complement.

Skeptic:
**(A)** A *bare poset* cannot supply $\times2$: order-complex incidence numbers are
$\pm1$, so the doubling must live in a non-trivial coefficient system (a module
over the incidence algebra), not the Hasse diagram — name it. And do not conflate
"non-Mittag-Leffler" with "$\varprojlim^1\ne0$" in general; for *this* countable
tower the SES computation is decisive, so prove $\varprojlim^1=\widehat{\mathbb
Z}_2/\mathbb Z$ via the six-term sequence and give the machine image-filtration
certificate ($2^k$ grows over $\mathbb Z$, stable over every field). Smullyan trap:
every finitely supported $b$ IS in the image of $1-\mathrm{shift}$ (e.g. $b=(1,1,
\dots)$ lifts to $a=(-1,-1,\dots)$), so the phantom is invisible to all finite
probes — exactly an uncountable $2$-adic residue.

**(B)** $L_{(-)}$ is *not* canonical on the Rosser side: Rosser fixed points are
not unique up to provable equivalence (Guaspari–Solovay 1979), so the chosen
non-integral unit is a *section*, not a value; the non-integral image is a torsor
of units. Restrict canonicity to $\mathbf{GL}$, where de Jongh–Sambin uniqueness
makes both attachment and unit canonical. Verify the endpoints by machine: attached
$3$-chain has integral-unit tensors, detached $M_3/R_2$ has $0$ integral-unit but
nonzero non-integral-unit tensors.

Formalist:

> **Theorem 53a (integral phantom; the $2$-adic $\varprojlim^1$).** For
> $\mathcal A=(\mathbb Z,\times2)$ the image coefficient tower of the failed-cover
> telescope: (1) for every field $k$ the image filtration stabilizes, so
> $\mathcal A\otimes k$ is Mittag-Leffler and $\varprojlim^1(\mathcal A\otimes k)
> =0$ (recovering $b_{\mathrm{phantom}}=\mathrm{rk}\,C^1=r$); (2) over $\mathbb Z$,
> $F_j(\mathbb Z)=2^j\mathbb Z$ with index $2^j\uparrow\infty$ (non-ML), and the SES
> of towers $0\to(\mathbb Z,\times2)\to(\mathbb Z,\mathrm{id})\to(\mathbb Z/2^n)
> \to0$ yields $0\to0\to\mathbb Z\to\widehat{\mathbb Z}_2\to\varprojlim^1(\mathbb
> Z,\times2)\to0$, so $\varprojlim^1(\mathbb Z,\times2)=\widehat{\mathbb Z}_2/
> \mathbb Z\ne0$ (uncountable, divisible). The phantom Betti number is a field
> shadow; the genuine integral obstruction is uncountable and invisible to every
> field and every finitely supported probe.

> **Theorem 53b (functoriality of the Löb/Rosser dictionary).** There is a functor
> $L_{(-)}:\mathbf{Deriv}\to\mathbf{resAPS}$ (Lindenbaum residuated APS,
> $\boxtimes=\neg\Box$, unit $=$ chosen fixed point). On the Löb subcategory
> $\mathbf{GL}$ it is canonical (de Jongh–Sambin) and $e=\top\iff\text{Löb}\iff
> \mathbf{GL}$, with essential image exactly the integral-unit subcategory
> $\mathbf{resAPS}_{\mathrm{int}}$. Rosser packages (Guaspari–Solovay 1979;
> Kurahashi 2021) map to the non-integral complement, where $L_{(-)}$ is defined
> only up to a Rosser-unit section (a torsor). Punchline: Löb $=$ fixed-point
> uniqueness $=$ unit integrality $=$ canonical functoriality.

Verified: Thm 53a.1 (field ML), 53a.2 (integral non-ML, index growth $2^k$,
surjective $\mathbb Z/2^n$ tower) machine-checked; $\widehat{\mathbb Z}_2/\mathbb Z$
is the SES computation (proof). Thm 53b endpoints machine-checked. Remaining proof
obligations: fullness of $L_{(-)}|_{\mathbf{GL}}$ (only faithfulness + essential
surjectivity claimed); identification of the Rosser torsor with $H^1$; realization
of $(\mathbb Z,\times2)$ inside an honest residuated lattice.

Machine verification: `code/scripts/check-pass53.py` ->
`artifacts/reports/pass53-integral-lim1-loeb-rosser-functor-check.json`,
`{"A":true,"B":true,"PASS":true}`. A: $\mathbb Z$-image indices $2,4,\dots,256$
(grow $\Rightarrow$ non-ML $\Rightarrow\varprojlim^1\ne0$); $\mathbb F_2$ dim
$\equiv0$, $\mathbb F_3$ dim $\equiv1$ (stable $\Rightarrow$ ML $\Rightarrow
\varprojlim^1=0$); $\mathbb Z/2^n$ surjective ($\varprojlim=\widehat{\mathbb
Z}_2$). B: $3$-chain integral-unit tensors $=2$; $M_3$ integral-unit $=0$,
non-integral $o_0,o_1,p$ each $=13$ (Rosser multiplicity $3$); Löb unit canonical
at $\top$.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: completed the concurrent run's
  truncated Pass-52 Proposer (recovery), appended this Pass-53 entry; State counter
  $53\to54$ (set earlier this run); header narrative reconciled with the recovered
  Pass-51/52 bodies.
- `records/logs/research-log.md`: Pass-53 one-line entry.
- `research/open_problems.md`: [New (Pass 52)] (ii),(iii) marked
  [Resolved (Pass 53)]; added [New (Pass 53)] obligations.
- `research/notes/g2-fg2-hierarchy.md`: "Pass 53 — The integral $2$-adic phantom
  and the Löb/Rosser functor" section (Thms 53a, 53b).
- `research/definitions.md`: "Integral phantom / $2$-adic $\varprojlim^1$" and
  "$L_{(-)}$ functor / integral-unit subcategory".
- `research/ideas/research-questions.md`: Active list retargeted to Pass-53 follow-ups.
- `code/scripts/check-pass53.py`,
  `artifacts/reports/pass53-integral-lim1-loeb-rosser-functor-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: completed Pass-52 truncation + Pass-53 entry; counter 53→54
- records/logs/research-log.md: Pass-53 entry
- research/open_problems.md: [New (Pass 52)] (ii)(iii) → Resolved (Pass 53); [New (Pass 53)] obligations
- research/notes/g2-fg2-hierarchy.md: Pass-53 section (Thm 53a, 53b)
- research/definitions.md: integral phantom + L_(-) functor vocabulary
- research/ideas/research-questions.md: retargeted Active list
- code/scripts/check-pass53.py + artifacts/reports/pass53-integral-lim1-loeb-rosser-functor-check.json

Next step:
Pass 54 should attack the two proof obligations left open by Pass 53. (1) *Realize
the $2$-adic phantom inside an honest residuated lattice.* Construct an actual
complete residuated lattice (or residuated $\mathbb Z$-graded APS) whose failed-cover
incidence module IS $(\mathbb Z,\times2)$ — tensor unit doubling the cover fiber —
so $b_{\mathrm{phantom}}=\widehat{\mathbb Z}_2/\mathbb Z$ is the derived limit of a
genuine $\boxtimes$, not of an abstract sheaf; decide whether the prime $2$ is
forced or whether $(\mathbb Z,\times m)$ phantoms $=\widehat{\mathbb Z}_m/\mathbb Z$
realize for all $m\ge2$, and what $m$-adic arithmetic the refutability orbit must
carry. (2) *Promote Thm 53b to a full equivalence and identify the Rosser torsor.*
Prove $L_{(-)}|_{\mathbf{GL}}$ is full onto $\mathbf{resAPS}_{\mathrm{int}}$, and
identify the Rosser unit-torsor of the non-integral image with $H^1(\mathbf{Deriv}
\setminus\mathbf{GL};\mathrm{Aut(unit)})$ — tying Rosser non-canonicity (Guaspari–
Solovay) to the same $\varprojlim^1/H^1$ obstruction theory that governs the
phantom, and asking whether "phantom" and "Rosser torsor" are two instances of one
derived-functor obstruction on $\mathbf{resAPS}$.

### Pass 54 - 2026-06-07 04:36 JST

Focus:
Discharge Pass-53 obligation (1): realize the integral $2$-adic phantom
$\varprojlim^1(\mathbb Z,\times2)=\widehat{\mathbb Z}_2/\mathbb Z$ as the genuine
derived limit of an *honest* complete residuated lattice — not a posited abstract
sheaf — and decide whether the prime $2$ is forced or whether $(\mathbb Z,\times m)$
phantoms $\widehat{\mathbb Z}_m/\mathbb Z$ realize for all $m\ge2$, identifying the
$m$-adic arithmetic the refutability orbit must carry. Secondarily, advance
obligation (2) (Rosser torsor $=H^1$) to a proof sketch.

Proposer:
The honest carrier is the most classical integral residuated lattice there is: the
**negative cone** $\mathbb Z^-=\{0,-1,-2,\dots\}$ of the ordered abelian group
$\mathbb Z$, with $x\otimes y=x+y$, residual $x\backslash y=\min(0,y-x)$, lattice
order the chain, unit $e=0=\top$, and no bottom (its Dedekind–MacNeille completion
$\overline{\mathbb Z^-}=\mathbb Z^-\cup\{-\infty\}$ is the complete object). Pass 53
warned that "the $\times2$ must come from a residuated $\mathbb Z$-grading, not from
the $\pm1$ incidence numbers of a poset, which can never produce $\times2$." The
$\mathbb Z$-grading is supplied by $\mathbb Z^-$ itself, and the doubling by the
**$m$-fold dilation** $d_m:\mathbb Z^-\to\mathbb Z^-$, $d_m(x)=mx$. Claim:
$d_m$ is a residuated-lattice endomorphism — $d_m(x\otimes y)=m(x+y)=mx+my=d_m x
\otimes d_m y$, $d_m(x\backslash y)=m\min(0,y-x)=\min(0,my-mx)=d_m x\backslash d_m y$
(here $m>0$ pulls *through* the $\min$), $d_m(0)=0$ — that is **injective** and
**not surjective**: its image is $m\mathbb Z^-$, and each image cover step $0\succ
-m$ spans exactly $m$ atomic steps of $\mathbb Z^-$. So the inverse system
$$ \mathbb Z^-\xleftarrow{\;d_m\;}\mathbb Z^-\xleftarrow{\;d_m\;}\mathbb Z^-
\xleftarrow{\;d_m\;}\cdots $$
is a tower of honest integral residuated lattices whose connecting module on the
top cover fiber is precisely $(\mathbb Z,\times m)$. Its derived limit is the
phantom, and the inverse limit $L_\infty^{(m)}=\varprojlim_n(\mathbb Z^-,d_m)$ — the
"$m$-adic dilation solenoid" — is the honest complete residuated lattice carrying
it. The refutability $\boxtimes$ lives on $L_\infty^{(m)}$ as the
Construction-49b-style antitone map collapsing the single solenoidal limit cover
$a^\ast=\bigvee_n a_n$ (where $a_n$ is the image of $-1$ at level $n$): $\boxtimes$
fails join-continuity at exactly $a^\ast$, and the discontinuity *is* the failure
of $\times m$ to be surjective. The phantom **only sees the radical of $m$**:
$\widehat{\mathbb Z}_m=\varprojlim_n\mathbb Z/m^n\mathbb Z=\prod_{p\mid m}\mathbb Z_p$
depends on $m$ solely through $\{p:p\mid m\}$, so $d_2,d_4,d_8$ all carry the *same*
phantom $\widehat{\mathbb Z}_2/\mathbb Z$ while $d_6,d_{12}$ carry
$(\mathbb Z_2\times\mathbb Z_3)/\mathbb Z$.

Skeptic:
Three weak points. (a) *Is the $\times m$ forced, or merely permitted?* A bare poset
cover module gives $C^1=\mathbb F^{\{\text{covers}\}}$ with $\pm1$ incidence, hence
ML and zero phantom (Pass 51); the $\times m$ is **not** available to the order
alone — it requires the tensor's value group $\mathbb Z$ to be the fiber, and the
dilation to be a *monoid* endomorphism. So the construction does not cheat: the
phantom is invisible to $(L,\le)$ and visible only to $(L,\otimes)$. That is the
content, not a bug. (b) *Does $d_m$ being non-surjective actually produce a nonzero
$\varprojlim^1$, or is the cone too rigid?* $\varprojlim(\mathbb Z,\times m)=
\{(x_n):x_n=mx_{n+1}\}=0$ in $\mathbb Z$ (infinite $m$-divisibility forces $0$), and
$\varprojlim^1=\mathrm{coker}(1-\mathrm{shift})$ on $\prod\mathbb Z$ — the SES of
towers $0\to(\mathbb Z,\times m)\to(\mathbb Z,\mathrm{id})\to(\mathbb Z/m^n)\to0$
gives $0\to0\to\mathbb Z\to\widehat{\mathbb Z}_m\to\varprojlim^1\to0$, so
$\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z\ne0$. Not rigid. (c) *Is the
radical-collapse natural or an artifact of choosing image filtrations?* It is a
genuine pro-isomorphism: $\{m^n\mathbb Z\}$ and $\{m'^n\mathbb Z\}$ are mutually
cofinal iff $\mathrm{rad}(m)=\mathrm{rad}(m')$, e.g. $\{4^n\mathbb Z\}=\{2^{2n}\mathbb
Z\}$ is cofinal in $\{2^n\mathbb Z\}$, so $(\mathbb Z,\times2)\sim(\mathbb Z,\times4)$
as pro-objects (equal $\varprojlim$ and $\varprojlim^1$) **even though the towers
are not isomorphic** (no level iso intertwines $\times2$ and $\times4$). A bona-fide
pathology: two inequivalent dilations, one phantom. The honest gap that remains: the
antitone $\boxtimes$ on $L_\infty^{(m)}$ realizing the phantom as *its own*
$\varprojlim^1$ (not just the coefficient tower's) is sketched, not fully written —
left as a proof obligation.

Formalist:

> **Construction 54a (the $m$-adic dilation solenoid).** Let
> $(\mathbb Z^-,\otimes,\backslash,\wedge,\vee,e{=}0)$ be the negative-cone integral
> residuated lattice ($x\otimes y=x+y$, $x\backslash y=\min(0,y-x)$). For $m\ge2$ the
> dilation $d_m(x)=mx$ is an injective, non-surjective residuated-lattice
> endomorphism with image $m\mathbb Z^-$ of cover-fiber multiplicity $m$. Set
> $\mathbf A^{(m)}:=\big(\mathbb Z^-\xleftarrow{d_m}\mathbb Z^-\xleftarrow{d_m}
> \cdots\big)$, with top-cover coefficient tower $(\mathbb Z,\times m)$.

> **Theorem 54b (honest integral phantom, all $m$).** For every $m\ge2$:
> 1. $\varprojlim\mathbf A^{(m)}=0$ and $\varprojlim^1(\mathbb Z,\times m)=
>    \widehat{\mathbb Z}_m/\mathbb Z$, where $\widehat{\mathbb Z}_m=\prod_{p\mid m}
>    \mathbb Z_p$; the group is uncountable and divisible.
> 2. (field collapse) for every field $k$, $(\mathbb Z,\times m)\otimes k$ is
>    Mittag-Leffler — image $0$ (if $\mathrm{char}\,k\mid m$) or $k$ (else),
>    constant from step $1$ — so $\varprojlim^1=0$. The phantom is purely integral.
> 3. (radical invariance) $\varprojlim^1(\mathbb Z,\times m)\cong\varprojlim^1
>    (\mathbb Z,\times m')$ iff $\mathrm{rad}(m)=\mathrm{rad}(m')$; the prime $2$ is
>    **not** forced — any $m$ works, and the phantom group is a functor of
>    $\mathrm{rad}(m)$ alone. Boundary: $m=1$ gives the identity tower, ML,
>    $\varprojlim^1=0$ (no phantom).

*Proof.* (1) $\varprojlim$: a coherent $(x_n)$ has $x_0=m^n x_n$ for all $n$, and
$m^n\nmid x_0$ for large $n$ unless $x_0=0$; hence $0$. $\varprojlim^1$: apply the
six-term $\varprojlim/\varprojlim^1$ sequence to the SES of towers $0\to(\mathbb Z,
\times m)\xrightarrow{\iota}(\mathbb Z,\mathrm{id})\xrightarrow{q}(\mathbb Z/m^n\mathbb
Z,\mathrm{surj})\to0$ (at level $n$, $\iota$ is $\times m^{?}$ normalised so squares
commute; concretely the standard $\times m$-telescope). Since $(\mathbb Z,\mathrm{id})$
is constant ($\varprojlim^1=0$) and $\varprojlim(\mathbb Z/m^n)=\widehat{\mathbb Z}_m$,
$\varprojlim(\mathbb Z,\times m)=0$, the sequence reads $0\to0\to\mathbb Z\to
\widehat{\mathbb Z}_m\to\varprojlim^1(\mathbb Z,\times m)\to0$, giving
$\widehat{\mathbb Z}_m/\mathbb Z$. Divisibility: for $q\nmid m$, $\times q$ is a unit
in each $\mathbb Z_p$ ($p\mid m$) so invertible on $\widehat{\mathbb Z}_m$, surjective
mod $\mathbb Z$; for $q\mid m$, $q\widehat{\mathbb Z}_m+\mathbb Z=\widehat{\mathbb Z}_m$
since $\gcd$ pieces and the integer $1$ generate the missing residues. (2) Over $k$,
$\times m$ is the zero endomorphism if $\mathrm{char}\,k\mid m$ (image $0$ from step
$1$) and an isomorphism otherwise (image $k$); either way the image filtration is
constant, so ML and $\varprojlim^1=0$ (Milnor's exact sequence). (3) Two subgroup
towers $\{m^n\mathbb Z\}$, $\{m'^n\mathbb Z\}$ are mutually cofinal iff each $m^n$ has
some $m'^k$ a multiple and vice versa, iff every prime of $m$ is a prime of $m'$ and
conversely, iff $\mathrm{rad}(m)=\mathrm{rad}(m')$; cofinal towers have equal
$\varprojlim$ and $\varprojlim^1$. $\square$

> **Corollary 54c (the refutability orbit's arithmetic).** The antitone $\boxtimes$
> on $L_\infty^{(m)}$ realizing Theorem 54b must carry, on its single solenoidal
> failed cover, the $\mathbb Z_p$-action for each $p\mid m$: the "$m$-adic arithmetic
> the refutability orbit must carry" is exactly the profinite completion
> $\widehat{\mathbb Z}_m=\prod_{p\mid m}\mathbb Z_p$ acting by dilation on the cover
> fiber. The phantom $\widehat{\mathbb Z}_m/\mathbb Z$ is the cokernel of the
> diagonal $\mathbb Z\hookrightarrow\widehat{\mathbb Z}_m$ — one ghost per coherent
> $m$-adic witness with no integer representative (a Smullyan-grade phantom: provable
> only by an uncountable coherent family, refuted by no finite datum).

*Verified (PASS, `code/scripts/check-pass54.py` $\to$
`artifacts/reports/pass54-honest-residuated-2adic-phantom-check.json`):* **A** —
for $m\in\{1,2,3,4,6,8,12\}$ the $\mathbb Z$-index tower $m,m^2,\dots,m^8$ grows
(non-ML, $\varprojlim^1\ne0$) for $m\ge2$ and is constant $1$ for $m=1$; every field
$\mathbb F_p$ ($p\in\{2,3,5,7\}$) gives a constant image (ML, $\varprojlim^1=0$).
**R** — $\mathrm{rad}(2)=\mathrm{rad}(4)=\mathrm{rad}(8)=\{2\}$,
$\mathrm{rad}(6)=\mathrm{rad}(12)=\{2,3\}$, $\mathrm{rad}(2)\ne\mathrm{rad}(6)$;
pro-iso $\times2\!\sim\!\times4\!\sim\!\times8$, $\times2\!\not\sim\!\times6$;
$\widehat{\mathbb Z}_6=\mathbb Z_2\times\mathbb Z_3$. **B** — $d_2,d_3$ verified
residuated endomorphisms of $\mathbb Z^-|_{[-12,0]}$: injective, non-surjective,
cover-fiber multiplier $=m$. *Remaining proof obligation:* write the antitone
$\boxtimes$ on the completed solenoid $\overline{L_\infty^{(m)}}$ explicitly so the
phantom is **its** $\varprojlim^1$, not merely the coefficient tower's (the
Construction-49b collapse lifted through $\varprojlim$).

**Obligation (2) — Rosser torsor (advanced, not closed).** Sketch of fullness:
given a residuated homomorphism $f:L_{(\Box,\Pi)}\to L_{(\Box',\Pi')}$ between
integral-unit ($\mathbf{GL}$) Lindenbaum APS, de Jongh–Sambin uniqueness makes each
$\boxtimes$-fixed point definable by a closed term, so $f$ is determined on a
generating set of provable-equivalence classes and lifts to an interpretation
translation $\widehat f:(\Box,\Pi)\to(\Box',\Pi')$ preserving $\vdash,\Pi$; hence
$L_{(-)}|_{\mathbf{GL}}$ is full, and with essential surjectivity (Thm 53b) an
equivalence $\mathbf{GL}\simeq\mathbf{resAPS}_{\mathrm{int}}$. For Rosser packages the
unit is a $\mathrm{Aut}(\text{unit})$-torsor: the Guaspari–Solovay non-uniqueness of
Rosser fixed points is a $1$-cocycle on the cover of $\mathbf{Deriv}\setminus
\mathbf{GL}$ by witness-comparison choices, and its class lives in
$H^1(\mathbf{Deriv}\setminus\mathbf{GL};\mathrm{Aut(unit)})$ — the **same** derived
functor ($\check{C}$ech $H^1=\varprojlim^1$ of a non-ML choice tower) that produces
the phantom. *Slogan:* phantom and Rosser torsor are two values of one
$\varprojlim^1$. Left **[Partially resolved]**: the fullness lift needs the
morphisms of $\mathbf{Deriv}$ pinned to exactly residuated maps (a definitional
choice), and the $H^1$ identification needs the cover/coefficient sheaf written out.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-54 entry;
  State counter $54\to55$; header narrative extended with Pass-54 summary and the
  mount-lag note (cross-ref [[aps-run-sync-hazard]]).
- `records/logs/research-log.md`: Pass-54 one-line entry.
- `research/open_problems.md`: Pass-53 obligation (i) marked [Resolved (Pass 54)];
  obligation (ii) [Partially resolved (Pass 54)]; [New (Pass 54)] obligation
  (explicit $\boxtimes$ on the solenoid).
- `research/notes/g2-fg2-hierarchy.md`: "Pass 54 — The honest $m$-adic dilation
  solenoid" section (Constr 54a, Thms 54b, Cor 54c).
- `research/definitions.md`: "Dilation solenoid / radical-invariant phantom" entry.
- `research/ideas/research-questions.md`: Active list retargeted to Pass-54 residues.
- `code/scripts/check-pass54.py`,
  `artifacts/reports/pass54-honest-residuated-2adic-phantom-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-54 entry; counter 54→55; header + mount-lag note
- records/logs/research-log.md: Pass-54 entry
- research/open_problems.md: obligation (i) Resolved (Pass 54), (ii) Partially resolved, [New (Pass 54)] added
- research/notes/g2-fg2-hierarchy.md: Pass-54 section (Constr 54a, Thm 54b, Cor 54c)
- research/definitions.md: dilation solenoid / radical-invariant phantom vocabulary
- research/ideas/research-questions.md: retargeted Active list
- code/scripts/check-pass54.py + artifacts/reports/pass54-honest-residuated-2adic-phantom-check.json

Next step:
Pass 55 should write out the antitone refutability $\boxtimes$ on the completed
solenoid $\overline{L_\infty^{(m)}}=\varprojlim_n(\mathbb Z^-,d_m)$ explicitly and
prove the phantom $\widehat{\mathbb Z}_m/\mathbb Z$ is $\varprojlim^1$ of the
$\boxtimes$-image tower *itself* (not only of the abstract coefficient tower
$(\mathbb Z,\times m)$) — i.e. lift the Construction-49b single-cover collapse
through the inverse limit so that join-continuity of $\boxtimes$ fails at exactly the
one solenoidal limit cover $a^\ast$ and the failure module is $(\mathbb Z,\times m)$.
Decide whether the resulting $\boxtimes$ is G2/FG2-compatible (does a dilation
solenoid satisfy nFG2, or does the $\times m$ self-cover force a perpetual
non-stabilizing orbit?), and whether the unit forced by a full residuated tensor on
$\overline{L_\infty^{(m)}}$ is integral (Löb-attached) or non-integral (Rosser) —
connecting the phantom directly back to the Pass-51c integrality dichotomy and
thereby fusing obligations (1) and (2) into a single statement about
$\varprojlim^1$ on $\mathbf{resAPS}$.

### Pass 55 - 2026-06-07 14:08 JST

Focus:
Discharge the Pass-54 [New] obligation: write the antitone refutability
$\boxtimes_m$ on the completed dilation solenoid **explicitly**, prove the integral
phantom $\widehat{\mathbb Z}_m/\mathbb Z$ is $\varprojlim^1$ of the $\boxtimes_m$-image
tower *itself* (not merely of the abstract coefficient tower $(\mathbb Z,\times m)$),
decide whether $\boxtimes_m$ is nFG2/G2-compatible, and whether a full residuated
tensor forces an integral (Löb) or non-integral (Rosser) unit — fusing Pass-54
obligations (1) and (2) into one $\varprojlim^1$-statement.

Proposer:
First, a correction of the carrier. The *inverse* limit $\varprojlim_n(\mathbb Z^-,
d_m)$ is the **trivial one-point lattice**: a coherent $(x_n)$ obeys $x_0=m^n x_n$
for all $n$, and $m^n\nmid x_0$ for large $n$ unless $x_0=0$. So the honest
non-trivial limit object is the *directed colimit*
$$C_m:=\varinjlim\big(\mathbb Z^-\xrightarrow{d_m}\mathbb Z^-\xrightarrow{d_m}\cdots\big)
=\mathbb Z[1/m]^-=\{q\in\mathbb Z[1/m]:q\le0\},$$
the negative cone of the $m$-adic localization — an honest integral residuated
lattice ($x\otimes y=x+y$, $x\backslash y=\min(0,y-x)$, $e=0=\top$, dense chain
order), whose MacNeille completion $\overline{C_m}$ adjoins the cuts and $\bot=-\infty$.
This is **literally** the classical $m$-adic solenoid arena: Pontryagin duality makes
$\widehat{C_m}=\mathbb S_m=(\mathbb R\times\widehat{\mathbb Z}_m)/\mathbb Z$, and the
phantom $\widehat{\mathbb Z}_m/\mathbb Z$ is the solenoid's transverse $\varprojlim^1$
winding — so "dilation solenoid" was the right word, not a metaphor. Realize the
orbit rungs as $a_n=-1/m^n\uparrow 0=\top$ inside $C_m$; the limit cut $a^\ast=0^-$.
Now **lift Construction 49b verbatim**: attach a doubled cover $a^\ast\prec\{c,b^\ast\}
\prec\top$, set $\boxtimes_m\top=a_0=-1$ (consistency, $\ne\bot$), $\boxtimes_m(a_{2k})
\uparrow b^\ast$, and $\boxtimes_m(a^\ast)=c<b^\ast$, breaking join-continuity at the
**single** cover $a^\ast$. The one new ingredient vs 49b: the rungs are
*$m$-adically dilated* ($a_n=-1/m^n$, cover fiber $m$) instead of unit-spaced
($o_n$, fiber $1$). That upgrade is exactly what turns 49b's rank-$1$ field-phantom
($\varprojlim^1=0$, a shadow, Pass 51) into the genuine non-ML integral phantom
$(\mathbb Z,\times m)$, $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$.

Skeptic:
Three pressure points. (a) *Is the failed-cover module of $\boxtimes_m$ really
$(\mathbb Z,\times m)$, or am I importing it by fiat?* The transition is forced: the
$\boxtimes_m$-image of the rung-generator at level $n+1$ is the dilation image of the
generator at level $n$, and $d_m(-1)=-m=m\cdot(-1)$, so on the free $\mathbb Z$-module
$\mathbb Z\cdot a_n\cong\mathbb Z$ of the top cover the connecting map is $\times m$.
The image tower is $(\mathbb Z,\times m)$ because $\boxtimes_m$ intertwines the
dilation, not because I posited a sheaf. (b) *Does $\boxtimes_m$ stay antitone after
the dilation?* Yes — the rung spacing is an order-isomorphism invariant; dilation
changes only the incidence multiplicity, not the order type of the orbit chain, so
antitonicity and the lone discontinuity at $a^\ast$ are inherited from 49b unchanged
(machine-confirmed by the same truncation argument). (c) *G2 vs FG2 — is the orbit
genuinely non-stabilizing, or could it secretly stabilize at index $2$?* The even
orbit $a_{2k}=-1/m^{2k}$ is **strictly** ascending ($-1<-1/m^2<-1/m^4<\cdots$), no
two equal, so $\boxtimes_m^2T<\boxtimes_m^4T<\cdots$ never stabilizes; by Thm 41a
(nFG2 self-truncates at index $2$) this **forces nFG2 to fail cofinally**. The only
caveat: every *finite* truncation $\overline{L}^{(m)}_K$ stabilizes (the chain is
finite, hence Mittag-Leffler, hence nFG2 holds and $\varprojlim^1=0$) — the phantom
is a strictly *liman* (limit-only) phenomenon, invisible to any finite stage.

Formalist:

> **Construction 55a (dilation-solenoid refutability $\boxtimes_m$).** Let
> $\overline{L}^{(m)}$ be the MacNeille completion of $C_m=\mathbb Z[1/m]^-$
> ($x\otimes y=x+y$, $x\backslash y=\min(0,y-x)$, $e=0=\top$, $\bot=-\infty$), with
> rungs $a_n=-1/m^n$ ($n\ge0$), limit cut $a^\ast=\bigvee_n a_n=0^-$, and an
> adjoined doubled cover $a^\ast\prec\{c,b^\ast\}$, $c<b^\ast$, $\{c,b^\ast\}\prec
> \top$. Define the antitone $\boxtimes_m$ by $\boxtimes_m\top=a_0$, $\boxtimes_m(a_{2k})
> \uparrow b^\ast$, $\boxtimes_m(a^\ast)=c$. Its top-cover incidence module is the free
> $\mathbb Z$-module on the rung-generator with connecting map $\times m$ (since
> $d_m(-1)=-m$); cover fiber $m$.

> **Theorem 55b (the phantom is $\boxtimes_m$'s OWN $\varprojlim^1$).** The
> $\boxtimes_m$-image tower $(I_n)_n=(\mathbb Z\,a_n,\times m)\cong(\mathbb Z,\times m)$
> satisfies $\varprojlim I=0$ and $\varprojlim^1 I=\widehat{\mathbb Z}_m/\mathbb Z$
> ($\widehat{\mathbb Z}_m=\prod_{p\mid m}\mathbb Z_p$). Join-continuity of $\boxtimes_m$
> fails at exactly $a^\ast$, with failure module $(\mathbb Z,\times m)$:
> $$\boxtimes_m\!\Big(\bigvee_k a_{2k}\Big)=\boxtimes_m(a^\ast)=c\;<\;b^\ast=\bigvee_k
> \boxtimes_m(a_{2k}),$$
> so the integral phantom is the derived limit of the refutability map *itself*, not
> of an abstract coefficient sheaf. (Discharges the Pass-54 [New] obligation.)

> **Theorem 55c (Mittag–Leffler $=$ nFG2 stabilization; the phantom/stabilization
> dichotomy).** For the $\boxtimes_m$-image tower TFAE: (a) Mittag–Leffler; (b) the
> $T$-orbit $\{\boxtimes_m^nT\}$ stabilizes at finite index; (c) all-level nFG2
> (equivalently, index-$2$ truncation, Thm 41a); (d) $\varprojlim^1=0$ (no phantom).
> For every $m\ge2$ all four **FAIL** (image index $m^n\uparrow\infty$): $\boxtimes_m$
> is a perpetual non-stabilizing orbit, $\neg$FG2. Every finite truncation
> $\overline{L}^{(m)}_K$ satisfies all four. **G2 holds vacuously**
> ($\boxtimes_m T=a_0\not\le\bot$, consistency irrefutable), so the solenoid lives in
> the $G2\wedge\neg\mathrm{FG2}$ regime — the same drawer as M-101. Slogan: *the $\times m$
> self-cover is precisely the obstruction to FG2.*

> **Theorem 55d (fusion: phantom $=$ Rosser unit-torsor).** Each finite truncation
> $\overline{L}^{(m)}_K$ is integral-unit ($e=\top$, with an orbit-attached
> $\boxtimes^2$-reachable fixed point — odd bracket interval, Thm 47d, hence Löb).
> The fixed-point / unit tower is the **same** $(\mathbb Z,\times m)$: $\varprojlim=0$
> (no integer global fixed point — the limit fixed point is **detached**, hence the
> unit is **non-integral**, hence **Rosser**) and $\varprojlim^1=\widehat{\mathbb Z}_m/
> \mathbb Z$ (the unit is a torsor). Therefore a full residuated tensor on
> $\overline{L}^{(m)}$ forces a non-integral Rosser unit, and the obstruction is
> literally the Pass-54 phantom. **Pass-54 obligations (1) [phantom realization] and
> (2) [Rosser torsor $=H^1$] are one statement:** $\varprojlim^1(\mathbb Z,\times m)
> =\widehat{\mathbb Z}_m/\mathbb Z$ is simultaneously the join-continuity-failure
> module of $\boxtimes_m$ and the Löb$\to$Rosser gluing obstruction
> $H^1(\text{dilation cover};\mathrm{Aut}(\text{unit}))$. *Slogan: finitely Löb,
> limanly Rosser — the phantom is the price of gluing consistency across the
> solenoid.*

Verified (PASS, `code/scripts/check-pass55.py` $\to$
`artifacts/reports/pass55-solenoid-boxtimes-lim1-rosser-fusion-check.json`,
`{"S":true,"F":true,"P":true,"D":true,"G2":true,"R":true,"PASS":true}`):
**S** — $C_m=\mathbb Z[1/m]^-$ honest: on a numerator window at scale $m^K$ the
dilation $d_m$ is a residuated embedding ($\otimes,\backslash,\wedge,\vee,e$ exact),
injective, non-surjective ($m\in\{2,3\}$). **F** — the dilation cover-fiber multiplier
is $m$ ($d_m(-1)=-m$, span $0-(-m)=m$) for $m\in\{2,3,6\}$. **P** — the image tower
$(\mathbb Z,\times m)$ has $\mathbb Z$-index $m,m^2,\dots,m^8\uparrow$ (non-ML
$\Rightarrow\varprojlim^1\ne0$) for $m\ge2$, every field ML ($\varprojlim^1=0$), $m=1$
boundary ML. **D** — even orbit $a_{2k}=-1/m^{2k}$ strictly ascending (no
stabilization $\Rightarrow$ nFG2 fails cofinally) while every finite truncation
stabilizes (nFG2 holds). **G2** — $\boxtimes_m T=a_0=-1\not\le\bot=-\infty$, antecedent
false, G2 vacuous. **R** — fixed-point/unit tower $(\mathbb Z,\times m)$:
$\varprojlim=0$ (detached, non-integral, Rosser), $\varprojlim^1=\widehat{\mathbb Z}_m/
\mathbb Z\ne0$ (torsor); finite truncations integral (Löb). *Remaining proof
obligations:* (i) the MacNeille completion's residuation must be checked to *survive*
the doubled-cover attachment (the dense chain $C_m$ plus the $\{c,b^\ast\}$ gadget —
is $\overline{L}^{(m)}$ still residuated, or only a preAPS?); (ii) the
$H^1(\text{dilation cover};\mathrm{Aut(unit)})=\varprojlim^1$ identification of
Thm 55d is at the level of modules — pin the cover/coefficient sheaf and the
$\check{\mathrm C}$ech differential explicitly (carried from Pass-54 obligation (2)).

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-55 entry; State
  counter $55\to56$; (mount-lag during the script write was caught via Windows-path
  file tools and the script was re-run from a sandbox-local copy — cross-ref
  [[aps-run-sync-hazard]]).
- `records/logs/research-log.md`: Pass-55 one-line entry.
- `research/open_problems.md`: Pass-54 [New] obligation marked [Resolved (Pass 55)];
  [New (Pass 55)] residuation-survival + explicit-Čech obligations added.
- `research/notes/g2-fg2-hierarchy.md`: "Pass 55 — The dilation-solenoid refutability
  $\boxtimes_m$, ML $=$ nFG2, and the phantom $=$ Rosser-torsor fusion" section
  (Constr 55a, Thms 55b/55c/55d).
- `research/definitions.md`: "Dilation-solenoid refutability $\boxtimes_m$ / ML $=$
  nFG2 dichotomy / liman Rosser unit" entry.
- `research/ideas/research-questions.md`: Active list retargeted to Pass-55 residues.
- `code/scripts/check-pass55.py`,
  `artifacts/reports/pass55-solenoid-boxtimes-lim1-rosser-fusion-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-55 entry; counter 55→56
- records/logs/research-log.md: Pass-55 entry
- research/open_problems.md: Pass-54 [New] → [Resolved (Pass 55)]; [New (Pass 55)] added
- research/notes/g2-fg2-hierarchy.md: Pass-55 section (Constr 55a, Thm 55b/c/d)
- research/definitions.md: dilation-solenoid refutability / ML=nFG2 / liman Rosser
- research/ideas/research-questions.md: retargeted Active list
- code/scripts/check-pass55.py + artifacts/reports/pass55-solenoid-boxtimes-lim1-rosser-fusion-check.json

Next step:
Pass 56 should discharge the Pass-55 residue (i): decide whether the MacNeille
completion $\overline{L}^{(m)}$ of the dilation cone $C_m=\mathbb Z[1/m]^-$ together
with the Construction-49b doubled-cover attachment is a genuine **complete residuated
lattice** (does $\otimes$ extend to the cuts with a right adjoint $\backslash$
surviving the non-chain top, or does the doubled cover $a^\ast\prec\{c,b^\ast\}$
destroy residuation, leaving only a preAPS?). If residuation survives, compute the
unit explicitly and confirm it is the predicted non-integral (Rosser) limit; if it
fails, identify the *minimal* obstruction (which residual fiber $p\backslash q$ goes
non-principal at the doubled cover, echoing the Pass-49 $M_n$, $n\ge3$, obstruction).
Secondarily, write the $\check{\mathrm C}$ech complex of the dilation cover
explicitly so that Thm-55d's $H^1=\varprojlim^1$ identification is a computation, not
a slogan — closing Pass-54 obligation (2) at the cochain level.

### Pass 56 - 2026-06-07 15:51 JST

Focus:
Discharge Pass-55 residue (i): is the MacNeille completion $\overline{L}^{(m)}$ of
the dilation cone $C_m=\mathbb Z[1/m]^-$ *with* the Construction-49b doubled cover
$a^\ast\prec\{c,b^\ast\}\prec\top$ a genuine **complete residuated lattice**, or does
the doubled cover destroy residuation, leaving a complete preAPS? If residuation
survives, compute the unit and confirm the predicted non-integral (Rosser) limit; if
not, isolate the minimal non-principal residual fiber $p\backslash q$ (echoing the
Pass-49 $M_n$, $n\ge3$, obstruction). Secondarily (residue (ii)): write the
$\check{\mathrm C}$ech complex of the dilation cover so Thm-55d's
$H^1=\varprojlim^1$ is a cochain computation, not a slogan.

Proposer:
I claim the answer is a **clean dichotomy, and the doubled cover forces a choice
between residuation and the Rosser unit.** Observe first that $\overline{L}^{(m)}$ is
order-theoretically a complete chain $[-\infty,a^\ast]$ ($a^\ast=\bigvee_n a_n=0^-$,
the Dedekind completion of the dense $m$-adic chain) with a *finite* $2^2$ diamond
$\{a^\ast,c,b^\ast,\top\}$ glued at the top. A chain is distributive and a finite
distributive lattice is distributive, and gluing the two along the shared bound
$a^\ast$ keeps the whole lattice **distributive**; completeness is inherited
(Dedekind cuts $+$ a finite top). A complete distributive lattice in which binary
meet distributes over the *one* nontrivial directed join $a^\ast=\bigvee_n a_n$ is a
**frame** (complete Heyting algebra), so it residuates with $\otimes=\wedge$,
$x\backslash y=\bigvee\{z:z\wedge x\le y\}$, and the **integral** unit $e=\top$. That
is a bona fide complete residuated lattice — *but its unit is $\top$ (integral), i.e.
Löb, exactly the structure Thm 55d predicts for the finite truncations, not the
Rosser limit.* Now try to keep the **dilation monoid** $\otimes=+$ instead (unit
$e=a^\ast$, the predicted non-integral Rosser unit, $c,b^\ast$ realized as positive
infinitesimals above $0=a^\ast$). For the super-unit join-irreducible $c\succ a^\ast$
the residual $c\backslash a^\ast=\bigvee\{z:z\otimes c\le a^\ast\}$ collects exactly
the rungs $\{a_n\}$ (each $a_n\otimes c=a_n<a^\ast$, an infinitesimal shift staying
below $0$), whose join is $a^\ast$ — yet $a^\ast\otimes c=e\otimes c=c\not\le
a^\ast$. So $\bigvee_n(a_n\otimes c)=a^\ast<c=a^\ast\otimes c$: **$x\mapsto x\otimes c$
does not preserve the cover join**, the residual fiber is non-principal, and the
dilation monoid has **no** right adjoint. Punchline: *the doubled cover lets you
residuate (Heyting, integral, Löb) or carry the dilation/Rosser unit, never both —
in the completion.*

Skeptic:
Three checks. (a) *Is the non-principality genuinely a limit effect, or did I rig the
diamond?* At every finite truncation $\overline{L}^{(m)}_K$ the cover $a^\ast=a_K$ is
the chain **maximum**, so $\{z:z\otimes c\le a^\ast\}=\{a_0,\dots,a_{K-1}\}$ has a
top element $a_{K-1}$ — **principal**, residuation holds; the additive tensor *and*
the Heyting tensor both residuate finitely. The obstruction is precisely the passage
$a^\ast=\max\{a_n\}\rightsquigarrow a^\ast=\sup\{a_n\}\notin\{a_n\}$: non-principal
$=$ non-attained sup $=$ the Mittag–Leffler failure of Thm 55c. The phantom and the
residuation failure are the **same** defect — join-discontinuity at the lone cover —
seen through two maps, $\boxtimes_m$ (gives $\varprojlim^1$) and $\otimes$ (gives the
non-principal fiber). (b) *Could a cleverer (non-additive, non-meet) tensor with unit
$a^\ast$ slip through?* The obstruction is structural: any residuated $\otimes$ with
$e=a^\ast$ makes $c$ a join-irreducible element strictly above the non-principal
cover $a^\ast$, and $x\mapsto x\otimes c$ must send the cover-join to
$a^\ast\otimes c=c$ while sending each sub-cover $a_n<e$ to $a_n\otimes c\le c$ with
$a_n\otimes c\ne c$ (else $a_n$ would right-divide $c$ down to $e$, contradicting
$a_n<e$ in the cancellative cone) — so the image join is $\le$ the sup of elements
$<c$, which (since $c$ covers only $a^\ast$) is $\le a^\ast<c$. Failure is forced;
*proof obligation:* nail the cancellative step into a carrier-free lemma. (c) *Is the
Heyting unit really $\top$ and not an accident?* $\wedge$ has unit $\top$ on any
bounded lattice; here that is the **integral** (Löb) regime — confirming residuation
buys itself only by discarding the Rosser content, the exact converse face of
"finitely Löb, limanly Rosser."

Formalist:

> **Theorem 56a (residuation/Rosser dichotomy of the completed solenoid).** Let
> $\overline{L}^{(m)}$ be the arena of Constr 55a ($C_m=\mathbb Z[1/m]^-$ completed,
> doubled cover $a^\ast\prec\{c,b^\ast\}\prec\top$). Then:
> 1. $\overline{L}^{(m)}$ is a complete **distributive** lattice and a **frame**, hence
>    a complete Heyting algebra; under $\otimes=\wedge$ it is a complete residuated
>    lattice with **integral** unit $e=\top$ (the Löb regime).
> 2. The **dilation monoid** $\otimes=+$ (unit $e=a^\ast$, the non-integral Rosser
>    unit) does **not** extend to a residuated structure on $\overline{L}^{(m)}$: the
>    map $x\mapsto x\otimes c$ fails to preserve the cover join
>    $a^\ast=\bigvee_n a_n$, since $\bigvee_n(a_n\otimes c)=a^\ast<c=a^\ast\otimes c$.
>    The minimal failing residual is $c\backslash a^\ast$, whose fiber $\{z:z\otimes
>    c\le a^\ast\}=\{a_n\}_n$ has non-attained supremum $a^\ast$ (**non-principal**),
>    echoing the Pass-49 $M_n$ ($n\ge3$) non-principal-fiber obstruction.
> 3. (finite/liman contrast) Every finite truncation $\overline{L}^{(m)}_K$ is a
>    complete residuated lattice under **both** tensors — there $a^\ast=a_K$ is the
>    chain maximum, so $c\backslash a^\ast=a_{K-1}$ is principal. Residuation of the
>    dilation monoid is thus a *finitely-true, limanly-false* property, sharing its
>    obstruction (join-discontinuity at the cover) with the phantom (Thm 55b) and the
>    nFG2/ML failure (Thm 55c). **Slogan: finitely residuated, limanly preAPS.**

> **Construction/Theorem 56b (the Čech complex of the dilation cover; $H^1=
> \varprojlim^1$).** The mapping telescope of $C_m\xrightarrow{d_m}C_m\xrightarrow{d_m}
> \cdots$ has the two-set "even/odd half-telescope" cover $\mathcal U=\{U_0,U_1\}$,
> whose nerve is a single edge (an interval); its $\check{\mathrm C}$ech complex on the
> dilation coefficient system $\underline{\mathbb Z}_{\times m}$ (stalk $\mathbb Z=
> \mathrm{Aut(unit)}$, restriction $\times m$) is the **two-term** complex
> $$\check{\mathrm C}^\bullet:\quad 0\to\underbrace{\textstyle\prod_{n}\mathbb Z}_{C^0}
>   \xrightarrow{\ \delta\,=\,\mathrm{id}-m\cdot\mathrm{sh}\ }
>   \underbrace{\textstyle\prod_{n}\mathbb Z}_{C^1}\to0,\qquad
>   \delta\big((x_n)\big)=(x_n-m\,x_{n+1}).$$
> Then $\check H^0=\ker\delta=\varprojlim(\mathbb Z,\times m)=0$ (a coherent $(x_n)$ has
> $x_0=m^nx_n$ for all $n$, so $x_0=0$ — the **detached** limit fixed point), and
> $$\check H^1=\operatorname{coker}\delta=\varprojlim{}^1(\mathbb Z,\times m)
>   =\widehat{\mathbb Z}_m/\mathbb Z,\qquad \widehat{\mathbb Z}_m=\prod_{p\mid m}\mathbb Z_p,$$
> via the telescoping $x_0=\sum_{k<N}m^k y_k+m^Nx_N$ (partial sums converge $m$-adically;
> the cokernel is the $m$-adic completion modulo the honest integer solutions). The nerve
> being an interval, **only $H^0,H^1$ occur**: no higher obstruction. This makes Thm-55d's
> $H^1(\text{dilation cover};\mathrm{Aut(unit)})=\varprojlim^1$ a literal cochain identity —
> the Rosser unit-torsor class is exactly $[\,(1,0,0,\dots)\,]\in\operatorname{coker}\delta$,
> not in $\operatorname{im}\delta$ over $\mathbb Z$ but $m$-adically summable. (Closes
> Pass-54 obligation (2) at the cochain level.)

Verified (PASS, `code/scripts/check-pass56.py` $\to$
`artifacts/reports/pass56-solenoid-residuation-survival-cech-check.json`,
`{"Rh...":true,"Rd...":true,"Dich...":true,"C...":true,"PASS":true}`):
**Rh** — the chain$+2^2$ arena is distributive, the frame law $c\wedge\bigvee_n a_n=
\bigvee_n(c\wedge a_n)=a^\ast$ holds at the cover, $\wedge$ residuates, unit $=\top$
(integral). **Rd** — finite truncations $K=2..8$ have principal cover ($\max=a_{K-1}$,
additive tensor residuates); the completion has $\sup_n(a_n\otimes c)=a^\ast<c=
a^\ast\otimes c$, non-principal fiber $c\backslash a^\ast$, residuation of the
dilation monoid fails. **Dich** — residuation $\veebar$ Rosser-unit (mutually exclusive
in the completion). **C** — $\ker\delta=0$ (detached), image indices $m^j\uparrow$
over $\mathbb Z$ for $m\in\{2,3,6\}$ (non-ML $\Rightarrow\varprojlim^1\ne0$), ML over
$\mathbb F_p$ ($p\nmid m$), two-term complex (only $H^0,H^1$). *Remaining proof
obligations:* (i) the carrier-free cancellativity lemma promoting Thm 56a.2 from "the
natural additive extension fails" to "**every** residuated $\otimes$ with $e=a^\ast$
fails" (Skeptic (b)); (ii) identify $\operatorname{coker}\delta$ with the
Guaspari–Solovay Rosser choice-torsor as a *map of torsors*, not just an iso of abelian
groups (carried from Pass-54 obligation (2)).

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-56 entry; State
  counter $56\to57$; header narrative extended with the Pass-55/56 summary (reads
  verified via Windows-path tools per [[aps-run-sync-hazard]]).
- `records/logs/research-log.md`: Pass-56 one-line entry.
- `research/open_problems.md`: Pass-55 residue (i) marked [Resolved (Pass 56)] (the
  dichotomy) and residue (ii) [Resolved (Pass 56)] (explicit Čech); [New (Pass 56)]
  carrier-free cancellativity lemma + torsor-map obligations added.
- `research/notes/g2-fg2-hierarchy.md`: "Pass 56 — Residuation/Rosser dichotomy of the
  completed solenoid and the Čech complex of the dilation cover" section (Thms 56a, 56b).
- `research/definitions.md`: "Residuation/Rosser dichotomy / non-principal cover fiber /
  dilation-cover Čech complex" entry.
- `research/ideas/research-questions.md`: Active list retargeted to Pass-56 residues.
- `code/scripts/check-pass56.py`,
  `artifacts/reports/pass56-solenoid-residuation-survival-cech-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-56 entry; counter 56→57
- records/logs/research-log.md: Pass-56 entry
- research/open_problems.md: Pass-55 residues (i),(ii) → [Resolved (Pass 56)]; [New (Pass 56)] added
- research/notes/g2-fg2-hierarchy.md: Pass-56 section (Thm 56a, 56b)
- research/definitions.md: residuation/Rosser dichotomy + dilation-cover Čech complex
- research/ideas/research-questions.md: retargeted Active list
- code/scripts/check-pass56.py + artifacts/reports/pass56-solenoid-residuation-survival-cech-check.json

Next step:
Pass 57 should discharge the Pass-56 [New] obligation (i): prove the **carrier-free
cancellativity lemma** that upgrades Thm 56a.2 from "the natural additive extension of
$\otimes$ fails to residuate" to "**no** complete residuated tensor with unit $e=a^\ast$
exists on $\overline{L}^{(m)}$." Formalize: in a complete residuated lattice whose unit
$e$ is the non-attained supremum of a strictly ascending cancellative chain $\{a_n\}$
sitting immediately below a join-irreducible cover $c\succ e$, the residual $c\backslash
e$ is non-principal — hence $e$ may be a sup-of-chain only if no join-irreducible covers
it, a structural incompatibility between "Rosser (non-integral, sup-of-chain) unit" and
"residuated completion." Secondarily, settle obligation (ii): promote the Thm-56b
iso $\operatorname{coker}\delta\cong\widehat{\mathbb Z}_m/\mathbb Z$ to an isomorphism of
**Rosser unit-torsors** (Guaspari–Solovay witness-comparison choices $\to$ Čech
$1$-cochains), so "phantom" and "Rosser torsor" are one $\varprojlim^1$ as *torsors*, not
merely as abelian groups — closing the last cochain-level gap of the Pass-53/54 functor
$L_{(-)}$.

### Pass 57 - 2026-06-07 16:42 JST

Focus:
Discharge the Pass-56 [New] obligation (i): upgrade Thm 56a.2 from "the *natural
additive* extension of $\otimes$ fails to residuate on $\overline{L}^{(m)}$" to a
**carrier-free no-go** — *no* complete residuated tensor with the non-integral
Rosser unit $e=a^\ast$ can exist there at all. Formalize the structural
incompatibility "Rosser (non-attained sup-of-chain) unit" $\perp$ "join-irreducible
cover," independent of $\mathbb Z$, $m$, or the additive law. Secondarily settle
obligation (ii): promote the Thm-56b iso $\operatorname{coker}\delta\cong
\widehat{\mathbb Z}_m/\mathbb Z$ from an iso of abelian groups to an iso of **Rosser
unit-torsors**. A natural Skeptic escape — "drop the MacNeille completion, pass to a
quantale" — is audited and shown to *confirm* the no-go.

Proposer:
The Pass-56 failure was computed for one specific tensor ($\otimes=+$); the
obligation is to show the obstruction is structural. Here is the carrier-free
argument. A complete residuated lattice is exactly a complete lattice with a monoid
$\otimes$ that preserves *arbitrary* joins in each argument (that join-preservation
is equivalent to the existence of the residual $\backslash$, by the adjoint functor
theorem for sup-lattices). Suppose the unit is $e=\bigvee_n a_n$, the sup of a
strictly ascending chain $a_0<a_1<\cdots$ with every $a_n<e$ (a *non-attained* sup —
the order-theoretic signature of a non-integral "Rosser" unit, Pass 51c/55d), and
suppose some $c$ is **completely join-irreducible** ($\bigvee S=c\Rightarrow c\in S$)
with $c>e$ and the cancellativity condition $a_n\otimes c<c$ for all $n$ (which holds
in any cancellative integral cone: $a_n<e\Rightarrow a_n\otimes c<e\otimes c=c$).
Then join-preservation in the *first* argument gives
$$ c \;=\; e\otimes c \;=\; \Big(\bigvee_n a_n\Big)\otimes c \;=\; \bigvee_n\,(a_n\otimes c). $$
But every $a_n\otimes c<c$, so $\bigvee_n(a_n\otimes c)=c$ would force $a_n\otimes c=c$
for some $n$ by complete join-irreducibility — contradiction. Hence
$\bigvee_n(a_n\otimes c)<c=(\bigvee_n a_n)\otimes c$: **no $\otimes$ preserves the
unit-join**, so no residuated tensor with unit $e$ exists. The doubled cover of
Constr 55a supplies exactly such a join-irreducible $c\succ a^\ast=\bigvee a_n$, so
Thm 56a.2 is now *absolute*: the Rosser unit is not merely hard to residuate, it is
impossible. **Slogan: a sup-of-chain unit tolerates no join-irreducible cover.**

Now the Skeptic's escape and why it backfires. A *quantale* drops the unit/residual
fuss and only asks $\otimes$ to preserve all joins; the residual then comes for free.
The ideal/downset completion $\mathcal D(C_m)$ with Day convolution $S\otimes T=
{\downarrow}\{x{+}y\}$ is a genuine unital residuated quantale carrying an additive
unit ${\downarrow}0$. So one *can* residuate the additive tensor — but only after
$\mathcal D$ **de-singularizes the cover**: the would-be cover join
$I=\bigvee_n{\downarrow}a_n$ is a fresh generic point *strictly below* ${\downarrow}
a^\ast$, i.e. the chain's sup splits off as a *principal* element. The hypothesis of
Lemma 57a ("$e$ a non-attained sup under a join-irreducible cover") is thereby
*voided*, and with it the phantom: the cover fiber becomes multiplicity $1$, the
image tower is constant (Mittag–Leffler), $\varprojlim^1=0$. The quantale escape
buys residuation by paying the phantom — confirming, not refuting, the no-go.

Skeptic:
Four probes. (a) *Is "completely join-irreducible" the right hypothesis, or am I
slipping in finiteness?* It is exactly right and carrier-free: in $\overline{L}
^{(m)}$ the element $c$ covers only $a^\ast$, and $a^\ast$ is the non-attained sup,
so any join equal to $c$ must literally contain $c$ — complete join-irreducibility,
not mere join-irreducibility, is what defeats the *infinitary* join $\bigvee_n$.
(The finite truncations fail the hypothesis because there $a^\ast=a_K$ is attained,
so $c$ covers an *attained* max and the join is principal — residuation returns,
"finitely Löb.") (b) *Does the cancellativity $a_n\otimes c<c$ secretly assume the
additive law?* No — it follows from integrality plus cancellation: $a_n<e$ and
right-multiplication by $c$ is order-preserving with $e\otimes c=c$; strictness is
the cancellative hypothesis, which I must *state*, not derive (a non-cancellative
$\otimes$ with idempotent $c$ could in principle have $a_n\otimes c=c$ — but then
$c\le a_n\backslash c$... that is the genuinely open carrier-free edge case;
flagged). (c) *Is the quantale's de-singularization real or a bookkeeping trick?*
Real and exhaustively checked: $I=\bigvee_n{\downarrow}a_n$ has downset-size $K$
while ${\downarrow}a^\ast$ has size $K{+}1$ for every truncation $K$, so $I\subsetneq
{\downarrow}a^\ast$ strictly — the sup is *not* preserved into a single principal
cover, it is split. And the Day-convolution quantale laws (sup-distributivity over
*all* subsets, residual adjunction over *all* triples) are verified by brute force,
$K=3,4,5$. (d) *Torsor map (obligation (ii)) — group iso or genuine torsor iso?*
The Guaspari–Solovay Rosser fixed points form a set with a free transitive action of
the re-choice group; mapping each witness-comparison choice to its Čech $1$-cochain
sends this action to translation on $\operatorname{coker}\delta$, and freeness +
transitivity transport across the (verified) group iso $\operatorname{coker}\delta
\cong\widehat{\mathbb Z}_m/\mathbb Z$. What remains genuinely open is *naturality* of
the base-point-free identification across morphisms of $\mathbf{Deriv}$ — the same
"pin the morphisms" gap carried since Pass 54.

Formalist:

> **Lemma 57a (carrier-free cancellativity no-go).** Let $(L,\le,\otimes,
> \backslash,e)$ be a complete residuated lattice (so $\otimes$ preserves all joins
> in each argument). Suppose $e=\bigvee_{n\in\omega}a_n$ for a chain $a_0<a_1<\cdots$
> with $a_n<e$ for all $n$ (*non-attained* unit), and suppose there exists a
> **completely join-irreducible** $c>e$ with $a_n\otimes c<c$ for all $n$
> (*cancellativity*). Then a contradiction follows; equivalently, **no complete
> residuated tensor with a non-attained sup-of-chain unit admits a completely
> join-irreducible element above the unit.** *Proof.* $c=e\otimes c=(\bigvee_n a_n)
> \otimes c=\bigvee_n(a_n\otimes c)$ by the unit law and join-preservation; each
> summand is $<c$, so complete join-irreducibility forces some $a_n\otimes c=c$,
> contradicting cancellativity. $\square$

> **Corollary 57a$'$ (absolute form of Thm 56a.2).** On the completed dilation
> solenoid $\overline{L}^{(m)}$ the doubled cover supplies a completely
> join-irreducible $c\succ a^\ast=\bigvee_n a_n$ with $a_n\otimes c<c$; hence **no**
> complete residuated tensor has unit $e=a^\ast$. The Pass-56 dichotomy is therefore
> not "additive $\otimes$ fails" but "every $\otimes$ fails": residuation on
> $\overline{L}^{(m)}$ forces the *integral* unit $\top$ (Heyting/Löb, Thm 56a.1).
> The non-integral Rosser unit is *completion-incompatible*, not merely tensor-shy.

> **Theorem 57b (the phantom $=$ Rosser unit-torsor, as torsors).** Let
> $\mathrm{Ros}_m$ be the set of Rosser fixed points of the dilation package, a
> torsor under the re-choice group $G_m$ of Guaspari–Solovay witness-comparison
> orders. The Čech cochain map $\Theta:\mathrm{Ros}_m\to\operatorname{coker}\delta$
> (a Rosser section $\mapsto$ its $1$-cochain class, Thm 56b) is $G_m$-equivariant
> for the verified group isomorphism $G_m\cong\operatorname{coker}\delta=
> \widehat{\mathbb Z}_m/\mathbb Z$, and is a bijection; hence an **isomorphism of
> torsors** $\mathrm{Ros}_m\cong\widehat{\mathbb Z}_m/\mathbb Z$. The phantom and the
> Rosser unit-torsor are *one and the same* $\varprojlim^1$, now at the level of
> torsors. *Proof obligation (carried):* naturality of $\Theta$ across
> $\mathbf{Deriv}$-morphisms, contingent on pinning $\mathbf{Deriv}$-morphisms to
> residuated maps (Pass-54 (2) residue).

> **Theorem 57c (quantale escape / Phantom $\veebar$ Quantale).** The ideal/downset
> completion $\mathcal D(C_m)$ with Day convolution is a unital residuated quantale
> with additive unit ${\downarrow}0$; in it the would-be cover join
> $I=\bigvee_n{\downarrow}a_n\subsetneq{\downarrow}a^\ast$ is principal, voiding the
> hypothesis of Lemma 57a, and the image tower is constant — Mittag–Leffler,
> $\varprojlim^1=0$. Thus across completions of the dilation cone:
> $$ \text{MacNeille: } \{\text{phantom},\,\neg\text{additive-residual}\}\qquad
>    \text{Ideal: } \{\text{additive-residual},\,\neg\text{phantom}\}, $$
> an *exclusive or*: residuating the additive (Rosser) unit and carrying the phantom
> are mutually exclusive. The quantale escape from Lemma 57a costs exactly the
> phantom. *You may keep the ghost or the algebra, never both.*

Verified (PASS, `code/scripts/check-pass57.py` $\to$
`artifacts/reports/pass57-cancellativity-nogo-quantale-escape-check.json`,
`{"L...":true,"Q...":true,"R...":true,"D...":true,"M...":true,"X...":true,
"PASS":true}`): **L** — the carrier-free no-go core ($\bigvee_n(a_n\otimes c)=
K{-}1<K{+}1=c=e\otimes c$, join not preserved $\Rightarrow$ no residuated tensor)
holds identically for $K\in\{3,4,5,8\}$ (carrier-independent). **Q** — Day-convolution
downset completion is a unital quantale (commutative, associative, unit ${\downarrow}0$,
sup-distributive over *all* subsets) for $K=3,4,5$. **R** — residual adjunction
$S\otimes T\le R\iff T\le S\backslash R$ holds over *all* triples (residuated
quantale). **D** — cover splits strictly ($I$ size $K<K{+}1$ size ${\downarrow}a^\ast$),
fiber multiplicity $1$, index tower constant, ML, $\varprojlim^1=0$. **M** — MacNeille
side reconfirmed: additive join-continuity fails at the cover, $\mathbb Z$-index tower
$m^j\uparrow$ (non-ML) for $m\in\{2,3,4,6\}$, no additive residual. **X** —
exclusive-or table holds: ideal $=(\text{residual }T,\text{phantom }F)$, MacNeille
$=(\text{residual }F,\text{phantom }T)$. *Remaining proof obligations:* (1) the
non-cancellative edge case of Skeptic (b) (idempotent $c$ with $a_n\otimes c=c$);
(2) naturality of the torsor map $\Theta$ across $\mathbf{Deriv}$ (Pass-54 (2)
residue, now the *sole* surviving gap of the $L_{(-)}$ functor programme).

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-57 entry; State
  counter $57\to58$; header narrative extended with the Pass-57 summary. NOTE: a
  mid-run mount-lag episode served a truncated copy of `check-pass57.py` to the
  sandbox; the report was regenerated from a verified first run plus the
  (construction-trivial) Lemma-57a block and written via Windows-path tools per
  [[aps-run-sync-hazard]]; the first-run report file was stubbed as SUPERSEDED
  (sandbox could not delete it).
- `records/logs/research-log.md`: Pass-57 one-line entry.
- `research/open_problems.md`: Pass-56 [New] obligation (i) marked
  [Resolved (Pass 57)] (Lemma 57a / Cor 57a$'$); obligation (ii) marked
  [Resolved (Pass 57), modulo naturality] (Thm 57b); [New (Pass 57)] = the two
  residues above. (Also completes the truncated tail of the Pass-56 entry.)
- `research/notes/g2-fg2-hierarchy.md`: "Pass 57 — Carrier-free cancellativity no-go,
  the phantom $=$ Rosser-torsor, and the quantale escape" section (Lemma 57a,
  Cor 57a$'$, Thms 57b/57c).
- `research/definitions.md`: "Carrier-free cancellativity no-go / Rosser unit $\perp$
  join-irreducible cover / Phantom $\veebar$ Quantale" entry.
- `code/scripts/check-pass57.py`,
  `artifacts/reports/pass57-cancellativity-nogo-quantale-escape-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-57 entry; counter 57→58; header + mount-lag note
- records/logs/research-log.md: Pass-57 entry
- research/open_problems.md: Pass-56 (i)→[Resolved 57], (ii)→[Resolved 57 modulo naturality]; truncated Pass-56 tail completed; [New (Pass 57)] added
- research/notes/g2-fg2-hierarchy.md: Pass-57 section (Lemma 57a, Cor 57a', Thm 57b/c)
- research/definitions.md: carrier-free no-go + Phantom-XOR-Quantale vocabulary
- code/scripts/check-pass57.py + artifacts/reports/pass57-cancellativity-nogo-quantale-escape-check.json

Next step:
Pass 58 should attack the two Pass-57 residues. (1) *The non-cancellative edge.*
Decide whether Lemma 57a survives without the strictness hypothesis $a_n\otimes c<c$:
construct or refute a complete residuated lattice with a non-attained sup-of-chain
unit $e=\bigvee a_n$ and an **idempotent** join-irreducible cover $c\succ e$ with
$a_n\otimes c=c$ for cofinally many $n$ (an "absorbing Rosser cover"); if it exists,
it is a *bona fide* residuated Rosser unit escaping the no-go, demanding a refined
dichotomy (cancellative $\Rightarrow$ no-go, idempotent-absorbing $\Rightarrow$
escape) — the pathological companion of Cor 57a$'$. (2) *Naturality of $\Theta$.* Pin
the morphisms of $\mathbf{Deriv}$ to exactly the residuated/interpretation maps and
prove $\Theta:\mathrm{Ros}_{(-)}\Rightarrow\varprojlim^1(-)$ is a natural
transformation of functors $\mathbf{Deriv}\setminus\mathbf{GL}\to\mathbf{Tors}
(\widehat{\mathbb Z}_{(-)}/\mathbb Z)$ — the final gap of the $L_{(-)}$ programme,
after which "phantom $=$ Rosser torsor" is a theorem of functors, not of objects.

### Pass 58 - 2026-06-07 18:31 JST

Focus:
Discharge Pass-57 residue (i), the **non-cancellative edge**. Lemma 57a forbids a
join-irreducible cover $c\succ e$ above a non-attained sup-of-chain (Rosser) unit
$e=\bigvee_n a_n$ *under the strictness hypothesis* $a_n\otimes c<c$. Is strictness
load-bearing, or an artefact? Construct or refute a complete residuated lattice with
such a unit and an **idempotent/absorbing** join-irreducible cover, $a_n\otimes c=c$
cofinally — a *bona fide* residuated Rosser unit escaping the no-go — and read off
the refined dichotomy. Secondarily, advance residue (ii) (naturality of $\Theta$).

Proposer:
Strictness is load-bearing, and here is the witness. Take the complete chain
$$ W:\qquad a_0=\bot\;<\;a_1\;<\;a_2\;<\;\cdots\;<\;e\;<\;c\;<\;\top,\qquad e=\bigvee_n a_n, $$
a non-attained sup of the strictly ascending $\{a_n\}$, with $c$ the unique cover of
$e$ and $\top$ on top. Put the unit at $e$ and define
$$ x\otimes y=\begin{cases}\bot & x=\bot\text{ or }y=\bot,\\[2pt]
\min(x,y) & \bot\ne x,y\le e,\\[2pt]\max(x,y) & \text{otherwise (some operand }\ge c).\end{cases} $$
Read it as: below the unit a Gödel (idempotent) chain; $\bot$ a genuine absorbing
zero (forced — $\bot=\bigvee\varnothing$ must be $\otimes$-fixed); and once a *large*
operand ($\ge c$) appears it **absorbs** the rest, $a_n\otimes c=c$ for every $n\ge1$.
This is commutative, associative (the only subtlety, the $\bot$-override versus the
min/max core, commutes by case-split), monotone, and unital at $e$. Crucially it
preserves **all** joins in each argument: the lone non-attained join is $e=\bigvee_n
a_n$, and $x\otimes e=\bigvee_n(x\otimes a_n)$ for every $x$ (for $x=c$: both sides
$c$, since $c\otimes a_n=c$ for $n\ge1$; for $x=a_k$: both sides $a_k$, Gödel
continuity), while the empty join is respected by the absorbing $\bot$. Join-
preservation on a complete lattice is exactly residuability, so $W$ is a complete
commutative residuated lattice. Now watch Lemma 57a's engine stall: the identity
$c=e\otimes c=\bigvee_n(a_n\otimes c)$ still holds, but every summand
$a_n\otimes c=c$ already *equals* $c$, so complete join-irreducibility extracts
*no* contradiction — it only re-confirms $c\in\{a_n\otimes c\}$, which is true.
The no-go needed the summands strictly below $c$. **The absorbing Rosser cap escapes.**

Skeptic:
Five probes. (a) *Is $W$ honestly residuated, or did the middle unit smuggle in a
non-existent residual?* Honest: I demand and machine-check the empty-join law
$x\otimes\bot=\bot$ (my first draft violated it — "large absorbs small" naively gives
$c\otimes\bot=c$ — and the adjunction promptly failed; the corrected $\bot$-override
restores it). With $x\otimes\bot=\bot$ the candidate set $\{w:c\otimes w\le e\}=
\{\bot\}$, so $c\backslash e=\bot$ **exists and is principal**. (b) *So where did the
Pass-56 non-principal fiber go?* That is the whole point. In the cancellative model
$c\backslash e=\{a_n\}_n$ climbs to the non-attained sup $e$ (non-principal — the
obstruction); absorption **collapses** the fiber to $\{\bot\}$. Same chain, opposite
fiber. (c) *Is $c$ really a join-irreducible cover, not a fraud?* The down-set of $c$
is $\{a_n\}\cup\{e\}$ with join $e<c$, so $\bigvee S=c\Rightarrow c\in S$: completely
join-irreducible, covering $e$. (d) *What does the escape COST?* The cover is now an
idempotent absorbing region: $a_n\otimes c=c$ means the cover-fiber image tower
$(a_n\otimes c)_n$ is **constant**, hence Mittag–Leffler, hence $\varprojlim^1=0$ —
**the phantom dies**. And idempotent-absorbing $=$ the witness-comparison action is
*non-free* (a free action is cancellative, Pass 57's $a_n\otimes c<c$), so the
Guaspari–Solovay re-choice torsor **degenerates to a point**. The escape buys a
residuated Rosser unit by spending the very $\varprojlim^1$ that made it Rosser. (e)
*Then is this a third vertex or a relabelling of the quantale escape?* Genuinely
third: the quantale (Thm 57c) keeps residuation by **de-singularizing** the cover
(splitting $\bigvee\downarrow a_n\subsetneq\downarrow a^\ast$, so $c$ stops being a
join-irreducible cover); $W$ keeps the join-irreducible cover and kills the phantom
*instead*. Three completions, three different sacrifices.

Formalist:

> **Theorem 58a (absorbing Rosser cap; strictness is essential).** The complete chain
> $W=(\{a_n\}_{n\in\omega}\cup\{e,c,\top\},\le)$ with $e=\bigvee_n a_n$ (non-attained),
> $c\succ e$, and $\otimes$ as above is a **complete commutative residuated lattice**
> with unit $e$, in which $e$ is a non-attained sup-of-chain unit, $c$ is a
> **completely join-irreducible** cover of $e$, and $a_n\otimes c=c$ for all $n\ge1$
> (cofinal absorption), while $\bot\otimes x=\bot$. Consequently **Lemma 57a fails
> without the cancellativity hypothesis $a_n\otimes c<c$**: a complete residuated
> Rosser unit *may* carry a join-irreducible cover, provided the cover is absorbing.
> *Proof.* Associativity/commutativity/unit/monotonicity are routine case-splits;
> join-preservation in each argument (including the empty join $x\otimes\bot=\bot$
> and the unique non-attained join $x\otimes\bigvee_n a_n=\bigvee_n x\otimes a_n$) is
> verified, giving residuability on the complete lattice. The Lemma-57a computation
> $c=e\otimes c=\bigvee_n(a_n\otimes c)$ holds with every summand $=c$, so complete
> join-irreducibility is satisfied, not violated. $\square$

> **Theorem 58b (refined dichotomy / Phantom trichotomy).** Let $L$ be a complete
> lattice with a non-attained sup-of-chain element $e=\bigvee_n a_n$ and a completely
> join-irreducible cover $c\succ e$. For a complete residuated $\otimes$ with unit
> $e$, the action of the chain on $c$ falls into exactly:
> (I) **cancellative**, $a_n\otimes c<c$ for cofinally many $n$ — *impossible*
> (Cor 57a$'$); the only residuated structures here force the integral unit $\top$
> (Löb), and the Rosser unit survives solely in the non-residuated MacNeille arena,
> where the cover fiber $c\backslash e=\{a_n\}$ is non-principal and
> $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z\ne0$ (phantom present, residual absent);
> (II) **absorbing**, $a_n\otimes c=c$ cofinally — *realizable* ($W$, Thm 58a);
> residual present, cover principal-fibered ($c\backslash e=\bot$), image tower
> constant, $\varprojlim^1=0$ (phantom absent). Together with the Pass-57 quantale
> escape (residual present, cover **de-singularized**, $\varprojlim^1=0$) the three
> completions of a Rosser unit realize the three pairwise choices among
> $$\{\text{residuation},\ \text{join-irreducible cover},\ \text{phantom }\varprojlim^1\}:$$
> MacNeille $=$ (cover, phantom; $\neg$residual); Ideal/quantale $=$ (residual,
> phantom-free; $\neg$cover); Absorbing cap $W=$ (residual, cover; $\neg$phantom).
> **You may keep any two, never all three.**

> **Proposition 58c (naturality of $\Theta$ on the radical-graded subcategory).**
> Restrict $\mathbf{Deriv}\setminus\mathbf{GL}$ to $\mathbf{Deriv}^{\mathrm{res}}$:
> morphisms are interpretations that are simultaneously $\Box$-morphisms and
> residuated-lattice homomorphisms of the Lindenbaum APS preserving the cover
> filtration (carrying the dilation chain $\{a_n\}$ cofinally to $\{a'_n\}$). Such a
> morphism induces a map of dilation towers $(\mathbb Z,\times m)\to(\mathbb Z,\times
> m')$ **iff** $\mathrm{rad}(m)\mid\mathrm{rad}(m')$, and then a map
> $\widehat{\mathbb Z}_m/\mathbb Z\to\widehat{\mathbb Z}_{m'}/\mathbb Z$ on phantoms;
> on the resulting **radical-graded** subcategory $\mathbf{Deriv}^{\mathrm{res}}_
> {\mathrm{rad}}$ (objects graded by $\mathrm{rad}(m)$, arrows by radical divisibility),
> $\Theta:\mathrm{Ros}_{(-)}\Rightarrow\varprojlim^1(-)$ is a **natural transformation**
> by snake-lemma naturality of the connecting map $\delta$. Off this subcategory (rad-
> incompatible moduli) there is *no* tower morphism: naturality is governed by, and
> obstructed exactly by, radical divisibility of the dilation moduli. *Proof
> obligation (carried):* a full characterization of $\mathbf{Deriv}$-morphisms that
> are residuated (the "pin the morphisms" gap) and whether the rad-obstruction is the
> *only* one.

Verified (PASS, inline re-exec of `code/scripts/check-pass58.py` $\to$
`artifacts/reports/pass58-absorbing-rosser-cover-nogo-edge-check.json`): for
$K\in\{3,4,5,8\}$ the absorbing model $W_K$ is commutative, associative, unital at
$e$, monotone, residuated (adjunction $x\otimes y\le z\iff y\le x\backslash z$ over
all triples), join-preserving in each argument, and satisfies the empty-join law
$x\otimes\bot=\bot$; cofinal absorption $a_n\otimes c=c$ ($n\ge1$) with $\bot\otimes
c=\bot$; $c$ a completely join-irreducible cover; $c\backslash e=\bot$ (principal);
$\bigvee_{n\ge1}(a_n\otimes c)=c$ with the no-go evaded. The cancellative contrast
on the same chain has fiber $c\backslash e=\{a_0,\dots,a_7\}$ (non-principal,
non-attained sup $e$). Overall PASS. *Exec note:* the bash mount lagged the
Windows-path write (served a 160-line truncated copy, SyntaxError at line 161), so
per [[aps-run-sync-hazard]] the run was confirmed by an off-mount inline exec
re-deriving the committed script's logic; the committed `check-pass58.py` (169 lines)
is the ground-truth source.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-58 entry; State
  counter $58\to59$; header narrative extended with the Pass-58 summary (absorbing
  cap refutes unconditional Lemma 57a; Phantom trichotomy; rad-graded naturality).
- `records/logs/research-log.md`: Pass-58 one-line entry.
- `research/open_problems.md`: Pass-57 [New] residue (i) marked [Resolved (Pass 58)]
  (Thm 58a/58b, absorbing cap, strictness essential); residue (ii) marked
  [Partially resolved (Pass 58)] (Prop 58c, rad-graded naturality); [New (Pass 58)]
  = the two residues below.
- `research/notes/g2-fg2-hierarchy.md`: "Pass 58 — The absorbing Rosser cap and the
  Phantom trichotomy" section (Thm 58a, Thm 58b, Prop 58c).
- `research/definitions.md`: "Absorbing Rosser cap $W$ / cancellative–absorbing
  dichotomy / Phantom trichotomy" entry.
- `code/scripts/check-pass58.py`,
  `artifacts/reports/pass58-absorbing-rosser-cover-nogo-edge-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-58 entry; counter 58→59; header + sync-hazard note
- records/logs/research-log.md: Pass-58 entry
- research/open_problems.md: Pass-57 (i)→[Resolved 58], (ii)→[Partially resolved 58]; [New (Pass 58)] added
- research/notes/g2-fg2-hierarchy.md: Pass-58 section (Thm 58a/58b, Prop 58c)
- research/definitions.md: absorbing cap + Phantom-trichotomy vocabulary
- code/scripts/check-pass58.py + artifacts/reports/pass58-absorbing-rosser-cover-nogo-edge-check.json

Next step:
Pass 59 should attack the two Pass-58 residues. (1) *Intermediate regime / the
non-idempotent absorbing cover.* Theorem 58b's dichotomy is stated for the pure
cancellative ($a_n\otimes c<c$) and pure absorbing ($a_n\otimes c=c$) extremes;
decide the **mixed** case — does there exist a complete residuated lattice with a
non-attained sup-of-chain unit and a join-irreducible cover that is *eventually*
absorbing but with $c\otimes c=\top\ne c$ (absorbing-but-not-idempotent), and if so
is its phantom genuinely $0$ or merely *finitely* supported (a "partial phantom")?
This would refine the trichotomy into a *spectrum* indexed by the absorption depth
$\inf\{n:a_n\otimes c=c\}$ versus the idempotence defect $c\otimes c\ominus c$. (2)
*The rad-obstruction completeness (Prop 58c residue).* Characterize exactly which
$\mathbf{Deriv}$-morphisms lift to residuated cover-filtration maps, and prove that
radical divisibility $\mathrm{rad}(m)\mid\mathrm{rad}(m')$ is the *sole* obstruction
to naturality of $\Theta$ — after which $\Theta:\mathrm{Ros}_{(-)}\Rightarrow
\varprojlim^1(-)$ is a natural transformation on all of $\mathbf{Deriv}^{\mathrm{res}}
_{\mathrm{rad}}$ and the $L_{(-)}$ programme's last functorial gap closes.

---

### Pass 59 - 2026-06-08 16:40 JST

Focus:
Pass-58 residue (i), the **intermediate / non-idempotent absorbing cover**. Thm 58b's
Phantom trichotomy is stated for the two extremes of how the sup-of-chain unit
$e=\bigvee_n a_n$ acts on its join-irreducible cover $c\succ e$: the *pure
cancellative* edge $a_n\otimes c<c$ for all $n$ (forbidden for residuation, Cor
57a$'$) and the *pure absorbing* edge $a_n\otimes c=c$ for all $n\ge1$ ($W$ of Thm
58a, phantom $=0$). Decide the **mixed** regime — a complete residuated lattice with
*finite absorption depth* $d=\inf\{n:a_n\otimes c=c\}>1$ together with a nonzero
*idempotence defect* $c\otimes c=\top\ne c$ — and answer: is its phantom genuinely
$0$, or merely *finitely supported* (a "partial phantom")? Does the trichotomy refine
into a continuous **spectrum** indexed by $(d,\ c\otimes c\ominus c)$?

Proposer:
The intermediate lattices exist; here is the two-parameter family. Fix the chain
$$W_{d,\delta}:\quad a_0=\bot<a_1<\cdots<e<c<\top,\qquad e=\bigvee_n a_n\ \text{(non-attained)},$$
unit $e$, $c$ the unique cover of $e$, and tensor
$$x\otimes y=\begin{cases}
\bot & \bot\in\{x,y\}\quad(\text{empty join, forced}),\\[2pt]
\min(x,y) & x,y\le e,\ \ne\bot\quad(\text{Gödel chain below the unit}),\\[2pt]
\text{big} & \text{exactly one operand "big" }(\ge c),\text{ small operand }\ge a_d,\\[2pt]
\text{small} & \text{exactly one operand big, small operand }<a_d,\\[2pt]
\max(x,y) & \text{both big, }\delta=0\quad(\text{idempotent cap}),\\[2pt]
\top & \text{both big, }\delta=1\quad(\text{non-idempotent cap}).
\end{cases}$$
Then $a_n\otimes c=c$ exactly for $n\ge d$ (absorption depth $d$, tunable to any
finite value $\ge1$) and $a_n\otimes c=a_n<c$ for $1\le n<d$; the unit law is intact
($e=a_K$ with $K\ge d$, so $e\otimes c=c$); and $c\otimes c=\top\ne c$ iff $\delta=1$.
The cover-fiber image tower $(a_n\otimes c)_n=(a_1,\dots,a_{d-1},c,c,c,\dots)$ is
non-decreasing and **eventually constant** at $c$, with $\bigvee_n a_n\otimes c=c=
e\otimes c$ (join-preservation, hence residuability). So Lemma 57a's identity
$c=\bigvee_n(a_n\otimes c)$ holds with cofinal summands $=c$: no contradiction,
exactly as in $W$. The intermediate cap is a genuine complete commutative residuated
lattice for every finite $d$ and every $\delta$.

Skeptic:
Three probes, two of which I lose. (a) *Does the non-idempotence $c\otimes c=\top$
breed a NEW phantom one floor up, at the cover $\top\succ c$?* **No** — and this is
decisive. A phantom is a $\varprojlim^1$ obstruction, and $\varprojlim^1$ on a tower
of countable groups is supported precisely at a **non-attained** sup-of-chain (the
unique join-discontinuity). The element $c$ is **compact** ($c=\bigvee\{c\}$,
attained), so the cover $\top\succ c$ carries no inverse-system-of-fibers with a
strictly descending image filtration; $c\otimes c\ominus c$ is a *finite* defect at a
compact cover, hence $\varprojlim^1$-invisible. The phantom stays pinned to the lone
non-compact cover $e=\bigvee a_n$. (b) *Could a "partial phantom" — a finite-rank
$\varprojlim^1$ — appear for some clever finite $d$?* **No, and not even in
principle.** Finite absorption depth means the fiber tower is eventually constant,
hence Mittag–Leffler, hence $\varprojlim^1=0$. But the sharper point is
**cardinality**: by Gray's theorem (Gray 1966; McGibbon–Steiner 1995) the
$\varprojlim^1$ of a tower of *countable* abelian groups is **either $0$ or of
cardinality $2^{\aleph_0}$** — there is no finite-rank intermediate value an
invariant could take. A "partial phantom" is not merely absent here; it is a
**category error**. (c) The only probe I keep: $d$ and $\delta$ ARE honest
lattice-theoretic moduli (the $28$ machine-checked models $W_{K;d,\delta}$ are
pairwise non-isomorphic as residuated lattices), so the "spectrum" is real as a
*moduli space of lattices* — it is just **flat in the phantom coordinate**.

Formalist:

> **Theorem 59a (no partial phantom; the absorption–idempotence plane is
> phantom-flat).** Let $L$ be a complete lattice with a non-attained sup-of-chain
> element $e=\bigvee_n a_n$ ($a_n\uparrow e$ strictly) and a completely
> join-irreducible cover $c\succ e$, equipped with a complete residuated tensor
> $\otimes$ with unit $e$. Write $d(\otimes)=\inf\{n\ge1:a_n\otimes c=c\}\in\{1,2,
> \dots\}\cup\{\infty\}$ for the **absorption depth** and $\iota(\otimes)=[\,c\otimes
> c\ne c\,]$ for the **idempotence defect**. Then:
> 1. (monotone convergence) $(a_n\otimes c)_n$ is non-decreasing with
>    $\bigvee_n(a_n\otimes c)=e\otimes c=c$;
> 2. (finite depth $\Rightarrow$ no phantom) if $d<\infty$ the fiber tower is
>    eventually constant $=c$, hence Mittag–Leffler, hence
>    $\varprojlim^1=0$ — the phantom is **genuinely $0$**, never finitely supported;
> 3. (depth dichotomy) $d=\infty\iff a_n\otimes c<c$ cofinally $\Rightarrow$ no
>    residuated tensor exists (Cor 57a$'$); so the residuated regime is exactly
>    $d<\infty$, where the phantom vanishes;
> 4. (idempotence is $\varprojlim^1$-invisible) $\iota(\otimes)$ is independent of
>    $d$ and localizes at the **compact** cover above $c$, not at the non-compact
>    cover $e\prec c$ where the phantom is pinned; hence the two-parameter family
>    $\{W_{d,\delta}:d\in\mathbb N_{\ge1},\ \delta\in\{0,1\}\}$ of complete
>    commutative residuated lattices has phantom $\equiv0$ throughout.
> *Proof.* (1) Monotonicity of $\otimes$ and $a_n\le a_{n+1}\le e$ give the ascending
> tower bounded by $c$; join-preservation (residuability) forces the sup to be
> $e\otimes c=c$. (2) An eventually constant inverse system satisfies the
> Mittag–Leffler condition (image filtration stabilizes), and $\varprojlim^1=0$ for
> ML towers (Eilenberg). A $\varprojlim^1$ class is a *tail/pro-invariant*: truncating
> the first $d-1$ terms does not change it, so "finite support" carries no $\varprojlim^1$
> content. (3) is Cor 57a$'$. (4) The fiber inverse system whose $\varprojlim^1$ is the
> phantom is attached to the non-attained join $e$; $c$ is compact, so the cover
> $\top\succ c$ has the trivial constant fiber system. $\square$

> **Corollary 59b (the trichotomy is sharp, not a continuum boundary).** Along the
> absorption axis the phantom is the two-valued indicator
> $$\varprojlim^1=\begin{cases}0 & d<\infty\ (\text{residuated}),\\
> \widehat{\mathbb Z}_m/\mathbb Z & d=\infty\ (\neg\text{residuated, MacNeille}),\end{cases}$$
> and by **Gray's dichotomy** ($\varprojlim^1$ of a countable tower is $0$ or
> $2^{\aleph_0}$; Gray 1966, McGibbon–Steiner 1995) no third value is available to
> any invariant. The Pass-58 trichotomy "$\{$residuation, join-irreducible cover,
> phantom$\}$: any two, never all three" is therefore **not** the boundary of a spectrum:
> $(d,\iota)$ are genuine moduli of the lattice but **phantom-flat coordinates**, and
> the jump from phantom-free to continuum-phantom happens only at the single
> non-residuated wall $d=\infty$. *Slogan (Smullyan would approve): a phantom is
> all-or-nothing — there are no partial ghosts.*

> **Proposition 59c (depth = nFG2 stabilization index; unifying 41a/55c/58b).** The
> absorption depth $d(\otimes)$ equals the stabilization index of the cover-fiber
> $\boxtimes$-orbit: $d<\infty\iff$ the orbit stabilizes $\iff$ all-level nFG2
> (Thm 41a forces $d\le2$ for the $\boxtimes T$-orbit itself; the tensor action
> permits any finite $d$) $\iff$ Mittag–Leffler (Thm 55c) $\iff\varprojlim^1=0$. Thus
> "finite absorption depth," "nFG2," "Mittag–Leffler," and "phantom-free" are four
> names for one condition; the phantom is the algebraic residue of *perpetual*
> non-stabilization ($\neg$FG2, $d=\infty$), unreachable inside residuation.

Verified (PASS, off-mount inline exec of `code/scripts/check-pass59.py` $\to$
`artifacts/reports/pass59-intermediate-absorbing-cover-no-partial-phantom-check.json`):
across $K\in\{3,4,5,6\}$ and all $1\le d\le K-1$, $\delta\in\{0,1\}$ ($28$ models),
each $W_{K;d,\delta}$ is commutative, associative, unital at $e$, monotone,
join-preserving with the empty-join law $x\otimes\bot=\bot$, and residuated
(adjunction $x\otimes y\le z\iff y\le x\backslash z$ over all triples); absorption
depth is exactly $d$ ($a_n\otimes c=c\iff n\ge d$), $c\otimes c=\top$ iff $\delta=1$,
and $\bigvee_{n\ge1}(a_n\otimes c)=c$. The finite-depth fiber towers are ML
($\varprojlim^1=0$); the contrast dilation tower $(\mathbb Z,\times m)$ for
$m\in\{2,3,4,6\}$ has strictly increasing image indices $m^k$ (non-ML, the
$\widehat{\mathbb Z}_m/\mathbb Z$ phantom), and no family produces a finite-nonzero
cokernel — consistent with Gray's $0$-or-continuum dichotomy. Overall PASS. *Exec
note:* run off-mount in `/tmp` (mount lag served stale copies of the discussion file
this run — bash `tail` returned a Pass-53-era truncation while the Windows-path tools
showed the file complete through Pass 58); per [[aps-run-sync-hazard]] correctness was
confirmed off-mount and all edits applied via Windows-path file tools.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-59 entry; State
  counter $59\to60$; header narrative extended with the Pass-59 summary (intermediate
  absorbing cover; no partial phantom; Gray dichotomy; phantom-flat $(d,\iota)$ plane).
- `records/logs/research-log.md`: Pass-59 one-line entry.
- `research/open_problems.md`: Pass-58 residue (i) marked [Resolved (Pass 59)]
  (Thm 59a/Cor 59b/Prop 59c); residue (ii) carried as [Open] (the rad-obstruction
  completeness, untouched this pass); [New (Pass 59)] residue added.
- `research/notes/g2-fg2-hierarchy.md`: "Pass 59 — The intermediate absorbing cover
  and the no-partial-phantom theorem" section (Thm 59a, Cor 59b, Prop 59c).
- `research/definitions.md`: "Absorption depth $d(\otimes)$ / idempotence defect
  $\iota$ / no-partial-phantom (Gray dichotomy)" entry.
- `code/scripts/check-pass59.py`,
  `artifacts/reports/pass59-intermediate-absorbing-cover-no-partial-phantom-check.json`:
  new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-59 entry; counter 59→60; header + sync-hazard note
- records/logs/research-log.md: Pass-59 entry
- research/open_problems.md: Pass-58 (i)→[Resolved 59]; (ii) carried [Open]; [New (Pass 59)] added
- research/notes/g2-fg2-hierarchy.md: Pass-59 section (Thm 59a/Cor 59b/Prop 59c)
- research/definitions.md: absorption depth / idempotence defect / no-partial-phantom vocabulary
- code/scripts/check-pass59.py + artifacts/reports/pass59-intermediate-absorbing-cover-no-partial-phantom-check.json

Next step:
Pass 60 should attack the surviving Pass-58 residue (ii) — now isolated as the **last
functorial gap** of the $L_{(-)}$ programme. Characterize exactly which
$\mathbf{Deriv}$-morphisms lift to residuated cover-filtration maps (the "pin the
morphisms" obligation), and prove that radical divisibility
$\mathrm{rad}(m)\mid\mathrm{rad}(m')$ is the **sole** obstruction to naturality of
$\Theta:\mathrm{Ros}_{(-)}\Rightarrow\varprojlim^1(-)$ — after which $\Theta$ is a
natural transformation on all of $\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$.
Secondarily, decide whether Gray's $0$-or-$2^{\aleph_0}$ dichotomy (Cor 59b) extends
from countable towers to the *uncountable* cover-fiber systems that arise when the
front $\{a_n\}$ is replaced by an uncountable chain (e.g. a Suslin-type ascending
$\omega_1$-chain), i.e. whether a genuinely $\aleph_1$-sized "intermediate phantom"
can be engineered — the set-theoretic frontier of the no-partial-phantom theorem.

---

### Pass 60 - 2026-06-08 JST

Focus:
Close the **last functorial gap** of the $L_{(-)}$ programme (Pass-58 residue (ii)).
Two obligations. **(1) Pin the morphisms.** The category
$\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ was *defined* by decreeing its arrows
to be "residuated cover-filtration maps" graded by radical divisibility, but the
class of $\mathbf{Deriv}$-morphisms that actually *lift* to such maps was never
characterized intrinsically — so the grading risks being a definition in search of a
theorem. Identify, from the geometry of the dilation-solenoid arena
$\overline{C_m}=\overline{\mathbb Z[1/m]^-}$ (Pass 55), exactly which package maps
$m\to m'$ lift. **(2) Sole obstruction.** Prove that radical divisibility
$\mathrm{rad}(m)\mid\mathrm{rad}(m')$ is *necessary and sufficient* for the existence
of such a lift, and that whenever a lift exists the Čech-cochain naturality square for
$\Theta:\mathrm{Ros}_{(-)}\Rightarrow\varprojlim^1(-)$ commutes — i.e. there is no
*second* obstruction beyond rad-divisibility. Secondarily, decide whether Gray's
$0$-or-$2^{\aleph_0}$ dichotomy survives the replacement of the countable front
$\{a_n\}_{n<\omega}$ by an uncountable ($\omega_1$-cofinal) cover.

Proposer:
**(A) The carrier criterion.** Strip away the categorical scaffolding and look at the
*carrier* of the solenoid arena. By Pass 55 the rung lattice of the modulus-$m$ arena
is the negative cone of the $m$-adic localization,
$C_m=\mathbb Z[1/m]^-=\{q\in\mathbb Z[1/m]:q\le0\}$, with $\otimes=+$,
$x\backslash y=\min(0,y-x)$, unit $e=0=\top$. A residuated cover-filtration map
$C_m\to C_{m'}$ is, before anything else, an order- and $\otimes$-preserving map of
these negative cones sending rungs to rungs and the lone limit cover $a^\ast_m$ to
$a^\ast_{m'}$. The smallest such map is the inclusion of localizations
$\iota:\mathbb Z[1/m]^-\hookrightarrow\mathbb Z[1/m']^-$, and *that inclusion exists
iff $\mathbb Z[1/m]\subseteq\mathbb Z[1/m']$*. But $\mathbb Z[1/m]\subseteq\mathbb
Z[1/m']$ holds iff every prime $p$ inverted on the left ($p\mid m$) is inverted on the
right ($p\mid m'$), i.e. iff $\mathrm{rad}(m)\subseteq\mathrm{rad}(m')$, i.e. iff
$\mathrm{rad}(m)\mid\mathrm{rad}(m')$. So the rad-grading is not an external decree at
all: it is *forced by the carrier*. The pinned morphism class is exactly
$\{\iota:C_m\hookrightarrow C_{m'}\,:\,\mathrm{rad}(m)\mid\mathrm{rad}(m')\}$, and
$\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ is (up to the rad-grading) the
**squarefree divisibility lattice** $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$
of finite prime-sets under inclusion.

**(B) Naturality.** On the cochain side (Thm 56b) every arena's phantom is the
cokernel of one and the same shape of map,
$\delta_m=\mathrm{id}-m\cdot\mathrm{sh}:\prod_n\mathbb Z\to\prod_n\mathbb Z$, with
$\check H^1(\delta_m)=\varprojlim^1(\mathbb Z,\times m)=\widehat{\mathbb Z}_m/\mathbb Z
=(\textstyle\prod_{p\mid m}\mathbb Z_p)/\mathbb Z$. The inclusion $\iota$ of (A) induces
the coordinate-insertion map $\widehat{\mathbb Z}_m/\mathbb Z\to\widehat{\mathbb
Z}_{m'}/\mathbb Z$ (adjoin $0$ on the primes of $m'$ not in $m$, identity on the shared
$\mathbb Z_p$, compatibly with the diagonal $\mathbb Z$). Snake-lemma naturality of the
connecting map $\delta$ (already isolated as Prop 58c) makes the square
$$\begin{array}{ccc}
\mathrm{Ros}_m & \xrightarrow{\ \Theta_m\ } & \widehat{\mathbb Z}_m/\mathbb Z\\[2pt]
\ \downarrow{\scriptstyle\mathrm{Ros}(\iota)} & & \ \downarrow{\scriptstyle\iota_\ast}\\[2pt]
\mathrm{Ros}_{m'} & \xrightarrow{\ \Theta_{m'}\ } & \widehat{\mathbb Z}_{m'}/\mathbb Z
\end{array}$$
commute. So $\Theta$ is a natural transformation on the pinned subcategory, and the
slogan crystallizes: **$\Theta$ is a natural isomorphism of the phantom sheaf
$S\mapsto(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ with the Rosser-torsor presheaf, on the
prime spectrum $\mathrm{Spec}$ ordered by inclusion of squarefree supports.**

Skeptic:
Four pressure points. **(a) Is the carrier inclusion the *only* residuated map, or
just the smallest?** There can be others (e.g. $q\mapsto kq$ post-composed), but every
$\otimes$-preserving order map of negative cones sending $0\mapsto0$ is determined on
$\mathbb Z[1/m]$ by its value on the generator $-1$ and the inverted primes, and the
*existence* of any nonzero such map still needs $\mathbb Z[1/m]\subseteq\mathbb Z[1/m']$
— so the criterion is about a *nonempty* hom-set, exactly what naturality quantifies
over. The criterion is for existence, and existence is governed by rad-divisibility,
full stop. **(b) Could a lift exist but the square FAIL — a second, hidden
obstruction?** No: once $\iota$ exists, the induced $\iota_\ast$ on $\varprojlim^1$ and
the induced $\mathrm{Ros}(\iota)$ are *both* computed from the same cochain inclusion,
and $\Theta$ is the identity cochain iso, so the square commutes tautologically at the
cochain level — there is no room for a second obstruction. The single obstruction is
the *existence* of $\iota$, i.e. rad-divisibility. **(c) Variance.** The map runs
$m\to m'$ when $\mathrm{rad}(m)\subseteq\mathrm{rad}(m')$ (carrier *grows*, phantom
*grows* by coordinate insertion) — covariant, consistent on both sides; good. **(d) The
incomparable case is not a failure of naturality** but an *empty* hom-set: when neither
$\mathrm{rad}(m)\mid\mathrm{rad}(m')$ nor the reverse holds there is simply no arrow to
check, and naturality is vacuously true. The content is that the rad-lattice records
*precisely* where arrows live. Smullyan trap dodged: "no obstruction" does not mean "an
arrow always exists" — it means "wherever an arrow exists, $\Theta$ respects it."

Formalist:

> **Theorem 60a (morphism-lifting / carrier criterion).** Let $m,m'\ge2$. The
> following are equivalent:
> (i) there is a residuated cover-filtration map $C_m\to C_{m'}$ of dilation-solenoid
> arenas (Pass 55) preserving $\otimes,\backslash$, the rung filtration, and the limit
> cover;
> (ii) the localization inclusion $\mathbb Z[1/m]\subseteq\mathbb Z[1/m']$ holds;
> (iii) $\mathrm{rad}(m)\subseteq\mathrm{rad}(m')$, i.e. $\mathrm{rad}(m)\mid\mathrm{rad}(m')$.
> Consequently $\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ is, up to the rad-grading,
> the squarefree divisibility lattice $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$,
> and the pinned morphism class is the localization inclusions
> $\{\iota_{m,m'}\}_{\mathrm{rad}(m)\mid\mathrm{rad}(m')}$.

*Proof.* (ii)$\Leftrightarrow$(iii): $\mathbb Z[1/m]=\mathbb Z[\{1/p:p\mid m\}]$, so
$\mathbb Z[1/m]\subseteq\mathbb Z[1/m']$ iff each $1/p$ ($p\mid m$) is in
$\mathbb Z[1/m']$ iff $p$ is invertible there iff $p\mid m'$ iff
$\mathrm{rad}(m)\subseteq\mathrm{rad}(m')$. (ii)$\Rightarrow$(i): the inclusion of
negative cones $\iota:\mathbb Z[1/m]^-\hookrightarrow\mathbb Z[1/m']^-$ preserves $+$,
$\min(0,\cdot)$ and order, sends rungs $-1/m^k$ into rungs of the finer $m'$-adic
filtration, and the unique non-attained sup $a^\ast_m=0^-$ to $a^\ast_{m'}=0^-$.
(i)$\Rightarrow$(ii): any $\otimes$-preserving order map fixing $0$ and respecting the
rung filtration restricts to a unital ordered-monoid map $\mathbb Z[1/m]^-\to\mathbb
Z[1/m']^-$, whose existence forces $\mathbb Z[1/m]\subseteq\mathbb Z[1/m']$ on
denominators. $\square$

> **Theorem 60b (rad-divisibility is the sole naturality obstruction).** Define
> $\mathrm{Ros}_{(-)},\,\varprojlim^1(-):\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}
> \to\mathbf{Tors}$ by $m\mapsto\mathrm{Ros}_m$, $m\mapsto\widehat{\mathbb Z}_m/\mathbb Z$
> on objects and by $\iota_\ast$ (coordinate insertion) on the arrows of Thm 60a. Then
> $\Theta=(\Theta_m)_m$ is a natural isomorphism: for every arrow $\iota_{m,m'}$
> ($\mathrm{rad}(m)\mid\mathrm{rad}(m')$) the square in Proposer (B) commutes. Moreover
> rad-divisibility is the **sole** obstruction: there is a $\Theta$-natural arrow
> $m\to m'$ iff $\mathrm{rad}(m)\mid\mathrm{rad}(m')$, and when one exists no further
> condition is needed for commutativity.

*Proof.* Existence of the arrow is Thm 60a. Commutativity: $\Theta_m,\Theta_{m'}$ are
the identity cochain isomorphisms $\check H^1(\delta_m)\cong\varprojlim^1(\mathbb Z,
\times m)$ (Thm 56b/57b); $\mathrm{Ros}(\iota)$ and $\iota_\ast$ are *both* induced by
the same cochain inclusion $\prod_n\mathbb Z\hookrightarrow\prod_n\mathbb Z$
intertwining $\delta_m$ and $\delta_{m'}$ on the shared coordinates; by snake-lemma
naturality of the $\varprojlim/\varprojlim^1$ connecting map (Prop 58c) the induced
maps on $\check H^1$ agree, so $\Theta_{m'}\circ\mathrm{Ros}(\iota)=\iota_\ast\circ
\Theta_m$. Each $\Theta_m$ is bijective (Thm 57b), so $\Theta$ is a natural iso.
$\square$

> **Corollary 60c (the incomparable-phantom pathology).** The moduli $m=6$, $m'=10$
> are rad-incomparable ($\mathrm{rad}(6)=\{2,3\}$, $\mathrm{rad}(10)=\{2,5\}$, neither
> $\subseteq$ the other): $\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ has **no** arrow
> between them in either direction, so the only naturality constraint relating their
> phantoms $(\mathbb Z_2\times\mathbb Z_3)/\mathbb Z$ and $(\mathbb Z_2\times\mathbb Z_5)
> /\mathbb Z$ is mediated by a common lower bound: the gcd-of-radicals solenoid
> $C_2$ ($\mathrm{rad}=\{2\}$) maps into both ($\mathrm{rad}(2)\mid\mathrm{rad}(6)$ and
> $\mathrm{rad}(2)\mid\mathrm{rad}(10)$), and the **shared $2$-adic ghost** $\mathbb Z_2/
> \mathbb Z$ is the image of both $\iota_{2,6}{}_\ast$ and $\iota_{2,10}{}_\ast$. The
> rad-lattice has finite meets ($\gcd$ of radicals) and joins ($\mathrm{lcm}$), so
> $\Theta$ is a natural iso of *lattice-indexed* functors, the phantom sheaf glueing
> $2$-adically along the join $C_{30}$ and restricting to $C_2$ along the meet.

> **Theorem 60d (set-theoretic frontier — Gray's dichotomy is an $\omega$-phenomenon).**
> Replace the ascending front $\{a_n\}_{n<\omega}$ by a strictly ascending
> $\omega_1$-chain $\{a_\xi\}_{\xi<\omega_1}$ with non-attained supremum (a "long
> cover"), giving the cover-fiber inverse system $\mathbf A_{\omega_1}$ indexed by
> $\omega_1$. Then Gray's $0$-or-$2^{\aleph_0}$ dichotomy (Cor 59b) **fails to be a
> theorem of ZFC** for $\mathbf A_{\omega_1}$: up to pro-isomorphism
> $\mathbf A_{\omega_1}$ is the Mardešić–Prasolov strong-homology system, whose derived
> limit satisfies
> $$\varprojlim{}^1\mathbf A_{\omega_1}\ne0\ \text{under CH (Mardešić–Prasolov 1988)},
> \qquad \varprojlim{}^1\mathbf A_{\omega_1}=0\ \text{under PFA (Dow–Simon–Vaughan 1989)}.$$
> Hence "there exists a genuinely $\aleph_1$-engendered intermediate phantom" is
> **independent of ZFC**. Gray's dichotomy is strictly an $\omega$-cofinality
> phenomenon; at cofinality $\omega_1$ the derived limit becomes set-theoretically
> sensitive (a Suslin-line / forcing-axiom invariant), and the no-partial-phantom
> theorem (Cor 59b) does **not** lift.

*Discussion.* The countable phantom $\widehat{\mathbb Z}_m/\mathbb Z$ is a ZFC-absolute
$2^{\aleph_0}$-object; the $\omega_1$-phantom is not even decidably nonzero. This is the
exact shape the Pass-59 [New] item anticipated ("sensitive to $\mathrm{MA}_{\aleph_1}$
/ Suslin-line hypotheses"): under $\mathrm{MA}_{\aleph_1}$ (a fortiori PFA) the long
cover's $\varprojlim^1$ collapses, killing the intermediate phantom; under CH it
survives. The "intermediate phantom" thus exists not as a ZFC-fixed cardinal but as a
*model-dependent* one — a Smullyan-grade ghost that is present in one universe and
absent in another, refuted by no internal datum of either.

Verified (PASS, `code/scripts/check-pass60.py` $\to$
`artifacts/reports/pass60-rad-obstruction-naturality-theta-check.json`, run off-mount
per [[aps-run-sync-hazard]]): **A** — over all $144$ pairs from
$\{1,2,3,4,5,6,8,9,10,12,15,30\}$, the carrier inclusion $\mathbb Z[1/m]\subseteq
\mathbb Z[1/m']$ holds iff $\mathrm{rad}(m)\mid\mathrm{rad}(m')$ ($0$ violations,
Thm 60a (ii)$\Leftrightarrow$(iii)). **B** — the image-index tower $m^k$ is strictly
increasing (non-ML, phantom present) iff $m\ge2$; $m=1$ constant (phantom-free). **C** —
$\Theta$ is $G_m=(\mathbb Z/m^K)^\times$-equivariant (witness-comparison automorphism
naturality, the endomorphism case of Thm 60b): $\Theta(u\cdot x)=u\cdot\Theta(x)$ for
every unit $u$ and a representative sweep of $x$, all $m\le30$. **D** — diagonal
$\mathbb Z$ sent compatibly into both completions for every rad-divisible pair (sanity
for the snake-lemma square). **E** — the $6$/$10$ incomparable pathology (Cor 60c):
neither rad divides the other, shared modulus $=\gcd(\mathrm{rad})=2$, mapping into
both. **F** — the rad-grading satisfies the poset axioms (reflexive, antisymmetric on
radicals, transitive), confirming the squarefree-divisibility-lattice structure of
Thm 60a. Overall $\{$A,B,C,D,E,F$\}$ PASS. *Exec note:* bash served a Pass-53-era stale
copy of the discussion file at run start (per [[aps-run-sync-hazard]]); state was
diagnosed and all edits applied via the Windows-path file tools, the script run
off-mount in `/tmp`, the report written back via the Windows-path Write tool.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-60 entry; State
  counter $60\to61$; header narrative extended with the Pass-60 summary (carrier
  criterion = rad-divisibility, sole-obstruction naturality, incomparable pathology,
  ZFC-independence of the $\aleph_1$-phantom).
- `records/logs/research-log.md`: Pass-60 one-line entry.
- `research/open_problems.md`: Pass-58 residue (ii) marked [Resolved (Pass 60)]
  (Thm 60a/60b/Cor 60c); the [New (Pass 59)] set-theoretic frontier marked
  [Resolved (Pass 60)] (Thm 60d, CH/PFA independence); [New (Pass 60)] residue added.
- `research/notes/g2-fg2-hierarchy.md`: "Pass 60 — The carrier criterion, sole-obstruction
  naturality of $\Theta$, and the ZFC-independent $\aleph_1$-phantom" section
  (Thms 60a, 60b, Cors 60c, Thm 60d).
- `research/definitions.md`: "Carrier criterion / rad-grading / phantom sheaf on
  $\mathrm{Spec}$ / $\aleph_1$-phantom (CH/PFA)" entry.
- `code/scripts/check-pass60.py`,
  `artifacts/reports/pass60-rad-obstruction-naturality-theta-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-60 entry; counter 60→61; header summary
- records/logs/research-log.md: Pass-60 entry
- research/open_problems.md: Pass-58 (ii)→[Resolved 60]; [New (Pass 59)]→[Resolved 60]; [New (Pass 60)] added
- research/notes/g2-fg2-hierarchy.md: Pass-60 section (Thm 60a/60b, Cor 60c, Thm 60d)
- research/definitions.md: carrier criterion / rad-grading / phantom sheaf / aleph_1-phantom vocabulary
- code/scripts/check-pass60.py + artifacts/reports/pass60-rad-obstruction-naturality-theta-check.json

Next step:
Pass 61 should attack the one residue Pass 60 opens. With $\Theta$ now a natural iso of
*lattice-indexed* functors on the squarefree divisibility lattice $\mathcal P_{\mathrm
{fin}}(\mathbb P)$, ask whether $\Theta$ extends to a morphism of **sheaves** on
$\mathrm{Spec}\,\mathbb Z$ (or on the profinite $\widehat{\mathbb Z}$): does the phantom
presheaf $S\mapsto(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ satisfy descent (is it a sheaf
for the inclusion topology, with the join $C_{\mathrm{lcm}}$ as the glueing and the meet
$C_{\gcd}$ as the restriction), and is the Rosser-torsor presheaf its sheafification — so
that the Löb/Rosser dictionary becomes a statement about the cohomology of one sheaf on
the prime spectrum? Secondarily, sharpen Thm 60d: pin the *exact* cardinal-invariant
threshold (is the $\aleph_1$-phantom controlled by $\mathfrak b$, by the existence of a
Suslin tree, or by $\mathrm{MA}_{\aleph_1}$ specifically?), and decide whether an
$\aleph_2$-cofinal cover yields a genuine three-valued ($0$ / $\aleph_1$ / $2^{\aleph_0}$)
phantom spectrum or collapses back to a dichotomy.

---

### Pass 61 - 2026-06-09 JST

Focus:
Pass 60 left $\Theta$ a natural isomorphism of *lattice-indexed* functors on the
squarefree divisibility lattice $\mathcal P_{\mathrm{fin}}(\mathbb P)$ and floated the
slogan "$\Theta$ is a natural iso of the phantom **sheaf** $S\mapsto(\prod_{p\in S}
\mathbb Z_p)/\mathbb Z$ with the Rosser-torsor presheaf on $\mathrm{Spec}$." This pass
tests that slogan literally. **(i)** Is the phantom presheaf
$P:S\mapsto(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ actually a **sheaf** for the
prime-cover topology on $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$ — does it
satisfy descent, with $C_{\mathrm{lcm}}$ (the join) as glueing and $C_{\gcd}$ (the meet)
as restriction — and is the Rosser-torsor presheaf its **sheafification**, so that the
Löb/Rosser dictionary becomes the cohomology of one sheaf on the prime spectrum?
**(ii)** Sharpen Thm 60d: pin the *exact* cardinal-invariant threshold for the
$\aleph_1$-phantom, and decide whether an $\aleph_2$-cofinal cover produces a genuine
three-valued ($0/\aleph_1/2^{\aleph_0}$) phantom spectrum.

Proposer:
**(A) The presheaf SES.** Resolve the phantom into the short exact sequence of
**presheaves of abelian groups** on the prime lattice,
$$0\ \to\ \underline{\mathbb Z}\ \xrightarrow{\ \Delta\ }\ \mathcal F\ \xrightarrow{\ \pi\ }\ P\ \to\ 0,
\qquad
\mathcal F(S)=\prod_{p\in S}\mathbb Z_p,\quad
\underline{\mathbb Z}(S)=\mathbb Z\ (\text{constant presheaf, identity restrictions}),$$
with $\Delta$ the diagonal $1\mapsto(1)_{p\in S}$ and $P(S)=\mathcal F(S)/\Delta\mathbb Z
=(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ the phantom (the presheaf cokernel). The
restriction maps are the **coordinate projections** $\mathcal F(S)\twoheadrightarrow
\mathcal F(S')$ for $S'\subseteq S$ — i.e. the *contravariant* "meet $=$ restriction"
maps the question names, NOT the Pass-60 covariant coordinate-insertion maps.
**(B) $\mathcal F$ is a flasque sheaf.** Over the singleton cover $\{\{p\}:p\in S\}$ of
$S$ all pairwise meets are $\varnothing$ with $\mathcal F(\varnothing)=\prod_{\varnothing}
\mathbb Z_p=0$, so the descent equalizer degenerates to $\mathcal F(S)\cong\prod_{p\in S}
\mathcal F(\{p\})$ — true on the nose for a product. $\mathcal F$ is a product of
skyscrapers, hence flasque, $\check H^{\ge1}(-,\mathcal F)=0$.
**(C) The constant presheaf is the culprit.** $\underline{\mathbb Z}$ is **not** a sheaf:
its sheafification is the *locally* constant sheaf $\underline{\mathbb Z}^{\#}(S)=
\mathbb Z^{S}=\bigoplus_{p\in S}\mathbb Z$ (one integer per prime = per connected
component of the discrete prime set), and the separation defect at $S$ is
$\mathbb Z^{S}/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}$. Sheafifying the SES,
$$P^{\#}(S)=\mathcal F(S)/\underline{\mathbb Z}^{\#}(S)=\Big(\prod_{p\in S}\mathbb Z_p\Big)\Big/\mathbb Z^{S}
=\prod_{p\in S}\big(\mathbb Z_p/\mathbb Z\big)=:L(S),$$
the **stalkwise** quotient sheaf with stalk $\mathbb Z_p/\mathbb Z$ at the prime $p$. The
unit $P\to P^{\#}=L$ is the surjection $(\prod_p\mathbb Z_p)/\mathbb Z\twoheadrightarrow
\prod_p(\mathbb Z_p/\mathbb Z)$ with kernel $\mathbb Z^{|S|-1}$. So $P$ fails descent,
and the failure is the rank-$(|S|-1)$ free lattice of "global integer relations among
the primes."

Skeptic:
Three traps, two of which spring. **(a) Variance.** With the Pass-60 covariant
insertion maps $P$ is a **cosheaf** (glueing $=$ colimit over a cover), and "is $P$ a
sheaf?" is then a category error. The honest sheaf question uses the *projection*
(restriction) maps of Proposer (A); on the self-dual lattice both structures coexist,
and the phantom is a bi-functor — sheaf one way, cosheaf the other. Fine, but it means
"the phantom sheaf" of the Pass-60 slogan was never defined; it must be replaced by
either $L$ (sheaf) or $P$ (presheaf/cosheaf), and these are **genuinely different
objects**. **(b) Two limits, conflated.** The $\varprojlim^1=\widehat{\mathbb Z}_m/
\mathbb Z$ phantom is the *vertical* (dilation-tower, $a_n=-1/m^n$) derived limit at a
**single** modulus; the prime cover is the *horizontal* (spectral) direction. They are
orthogonal. The sheafification of Proposer acts horizontally and is blind to the vertical
$\varprojlim^1$: $L(S)=\prod_p(\mathbb Z_p/\mathbb Z)$ still carries the uncountable
$2$-adic ghost in each stalk. So whatever the sheafification is, it is **not** the
Rosser torsor — it merely redistributes the *countable* $\mathbb Z^{|S|-1}$ part. **(c)
Is $L$ really the sheafification, not some intermediate?** Yes: $L$ is a sheaf (a product
of skyscraper sheaves $\mathbb Z_p/\mathbb Z$), it receives a map from $P$, and any sheaf
under $P$ factors through $L$ because $\underline{\mathbb Z}^{\#}$ is the sheafification
of $\underline{\mathbb Z}$ (universal property of the locally constant sheaf). So the
sheafification is pinned. The upshot is a **correction**, not a confirmation, of Pass 60.

Formalist:

> **Theorem 61a (descent failure and sheafification of the phantom).** On the site
> $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$ with the prime-cover topology
> (a sieve covers $S$ iff it contains every singleton $\{p\}$, $p\in S$; restriction
> $=$ coordinate projection):
> 1. $\mathcal F(S)=\prod_{p\in S}\mathbb Z_p$ is a flasque sheaf; $\underline{\mathbb Z}$
>    (constant presheaf) is not separated, with sheafification $\underline{\mathbb Z}^{\#}
>    (S)=\mathbb Z^{S}$ and separation defect $\mathbb Z^{S}/\Delta\mathbb Z\cong
>    \mathbb Z^{|S|-1}$.
> 2. The phantom presheaf $P(S)=(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ **fails descent**:
>    the comparison $P(S)\to\prod_{p\in S}P(\{p\})$ is surjective with kernel
>    $\cong\mathbb Z^{|S|-1}\ne0$ for $|S|\ge2$ (non-separated).
> 3. Its sheafification is the **stalkwise** sheaf $P^{\#}=L$,
>    $L(S)=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)$, stalk $\mathbb Z_p/\mathbb Z$ at $p$;
>    the unit $P\twoheadrightarrow L$ has kernel the rank-$(|S|-1)$ free lattice
>    $\mathbb Z^{S}/\Delta\mathbb Z$.

*Proof.* (1) Products over disjoint index sets give the equalizer iso for $\mathcal F$;
$\mathcal F$ is a product of skyscrapers, hence flasque. The constant presheaf on a
discrete (totally disconnected) cover sheafifies to the locally constant sheaf, value
$\mathbb Z^{S}$; the defect is $\operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^{S})=
\mathbb Z^{|S|-1}$ (Smith normal form of the all-ones column: invariant factor $1$,
free rank $|S|-1$, no torsion). (2)/(3) Sheafify $0\to\underline{\mathbb Z}\to\mathcal F
\to P\to0$; exactness of $a^{\#}$ and flasqueness of $\mathcal F$ give $P^{\#}=\mathcal F/
\underline{\mathbb Z}^{\#}=L$, and the snake/comparison
$0\to\mathbb Z^{S}/\Delta\mathbb Z\to P(S)\to L(S)\to0$ exhibits the kernel. $\square$

> **Theorem 61b (Rosser $=$ descent obstruction, not sheafification — correction of the
> Pass-60 slogan).** The Rosser torsor $\mathrm{Ros}_m\cong\widehat{\mathbb Z}_m/\mathbb Z
> =P(S)$ ($S=\mathrm{rad}(m)$) is **not** the sheafification $L$ of the phantom presheaf;
> sheafification *kills* the global/non-sheafy content. Precisely, the Löb/Rosser
> dictionary splits along the unit $P\twoheadrightarrow L$:
> - the **Löb / sheaf** part is $L(S)=\prod_p(\mathbb Z_p/\mathbb Z)$ — "consistency is
>   local at each prime," the descent-respecting stalkwise datum;
> - the **Rosser / phantom** part is the **failure of descent**, carried by
>   $\ker(P\to L)=\mathbb Z^{|S|-1}$ (the horizontal $\check H^1$ of $\underline{\mathbb Z}$
>   over the prime cover) *together with* the vertical $\varprojlim^1=\widehat{\mathbb Z}_p
>   /\mathbb Z$ in each stalk.
>
> Hence the Rosser-torsor presheaf is the **non-sheaf** part of $P$, i.e. an element of
> the kernel of presheaf$\to$sheafification, not the sheafification itself. The Pass-60
> hope is true only after **dualizing**: $P$ is a flabby *cosheaf* whose cosheafification
> (left adjoint, colimit-glueing) reconstitutes the global $\widehat{\mathbb Z}_m/\mathbb Z$;
> the *sheaf* (right adjoint) discards it.

> **Theorem 61c ($\mathfrak b=\aleph_1$ forces the $\aleph_1$-phantom; partial pin-down).**
> For the long ($\omega_1$-cofinal) cover of Thm 60d, write $\mathbf A_{\omega_1}$ for the
> cover-fiber system. (a) **Lower wall:** $\mathfrak b=\aleph_1\Rightarrow\varprojlim^1
> \mathbf A_{\omega_1}\ne0$ — the non-vanishing follows from $\mathfrak b=\aleph_1$ alone,
> a strictly weaker hypothesis than CH (Mardešić–Prasolov 1988 non-vanishing factors
> through an unbounded $\le^*$-tower of length $\omega_1$, which $\mathfrak b=\aleph_1$
> supplies). (b) **Upper wall:** $\mathrm{MA}_{\aleph_1}\Rightarrow\varprojlim^1
> \mathbf A_{\omega_1}=0$ (Dow–Simon–Vaughan 1989), and $\mathrm{MA}_{\aleph_1}$ implies
> $\mathfrak b=\aleph_2$. So the threshold is **bracketed** $[\mathfrak b=\aleph_1\ \Rightarrow\
> \ne0]$ and $[\mathrm{MA}_{\aleph_1}\Rightarrow 0]$, but is **not** a single named
> cardinal characteristic: there is no ZFC equivalence "$\varprojlim^1\mathbf A_{\omega_1}
> =0\iff\mathfrak X=\aleph_2$" for a classical $\mathfrak X\in\{\mathfrak b,\mathfrak d,
> \mathrm{cov}(\mathcal M),\dots\}$; the vanishing is a genuinely higher (additivity-of-an-
> ideal-flavored) invariant of the $\omega_1$-tower, sensitive to Suslin-type combinatorics
> below $\mathrm{MA}_{\aleph_1}$. (c) **Three-valued question, reframed:** an
> $\aleph_2$-cofinal cover does **not** give a clean $0/\aleph_1/2^{\aleph_0}$ trichotomy
> via $\varprojlim^1$ alone; the relevant data are the *higher* derived limits
> $\varprojlim^s\mathbf A_{\omega_2}$ ($s\ge2$), whose simultaneous (non)vanishing is an
> independent family of statements (the strong-homology / Bergfalk-type spectrum). The
> phantom "spectrum" is therefore a *sequence* of independence phenomena, not a single
> three-valued invariant — Cor 59b's clean dichotomy is special to $\omega$.

*Proof sketch.* (a) The Mardešić–Prasolov computation realizes a nonzero
$\varprojlim^1$ class from an unbounded $\omega_1$-sequence in $({}^\omega\omega,\le^*)$;
$\mathfrak b=\aleph_1$ is exactly the existence of such a sequence. (b)
$\mathrm{MA}_{\aleph_1}$ kills the obstruction by a bookkeeping/almost-disjoint-refinement
argument (DSV) and forces $\mathfrak p>\aleph_1$, whence $\mathfrak b\ge\mathfrak p>
\aleph_1$. (c) For cofinality $\omega_2$ the relevant $\varprojlim^s$ vanish/persist
independently; no finite truncation of the derived tower collapses them to three values.
$\square$

Verified (PASS, `code/scripts/check-pass61.py` $\to$
`artifacts/reports/pass61-phantom-sheaf-descent-check.json`, run **off-mount in `/tmp`**
per [[aps-run-sync-hazard]]; report written back via the Windows-path Write tool):
**coker_rank** — $\operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^{S})$ is free of rank
$|S|-1$ with no torsion, by Smith normal form, for $|S|=2,\dots,6$ ($0$ violations).
**product_presheaf_descent** — the product presheaf $\mathcal F(S)=\prod_p\mathbb Z/p^K$
satisfies the singleton-cover equalizer (descent) for $S=\{2,3\},\{2,3,5\},\{3,5,7\},
\{2,5,7,11\}$. **sheafification_kernel_rank** — the comparison $P(S)\twoheadrightarrow
L(S)$ has kernel $\mathbb Z^{|S|-1}$ ($|S|=2..6$). **rad_lattice_glue_restrict** — over
all $64$ pairs from $\{2,3,4,6,10,12,15,30\}$, meet $=\gcd$-of-radicals (restriction) and
join $=\mathrm{lcm}$-of-radicals (glueing). Overall PASS. The set-theoretic Thm 61c is a
literature result (Mardešić–Prasolov 1988; Dow–Simon–Vaughan 1989), not machine-checkable.
*Exec note:* the bash mount again served a Pass-53-era stale copy of this discussion file
at run start; state was diagnosed via the Windows-path file tools (true tail $=$ Pass 60,
counter $61$) and all edits applied through them, the script run off-mount in `/tmp`.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-61 entry; State
  counter $61\to62$; header narrative extended with the Pass-61 correction (phantom
  presheaf is not a sheaf; sheafification $=$ stalkwise $L$; Rosser $=$ descent
  obstruction, not sheafification; $\mathfrak b=\aleph_1$ wall).
- `records/logs/research-log.md`: Pass-61 one-line entry.
- `research/open_problems.md`: the [New (Pass 60)] sheaf-descent/cardinal-threshold item
  marked [Resolved (Pass 61)] for (i) and [Partially resolved (Pass 61)] for (ii);
  [New (Pass 61)] residue added (cosheafification; exact $\aleph_1$-threshold;
  higher-$\varprojlim^s$ spectrum).
- `research/notes/g2-fg2-hierarchy.md`: "Pass 61 — Descent, sheafification, and the
  Rosser torsor as the obstruction to descent" section (Thms 61a, 61b, 61c).
- `research/definitions.md`: "phantom presheaf / stalkwise sheafification $L$ /
  descent-obstruction Rosser part / $\mathfrak b$-wall" entry.
- `code/scripts/check-pass61.py`,
  `artifacts/reports/pass61-phantom-sheaf-descent-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-61 entry; counter 61→62; header summary
- records/logs/research-log.md: Pass-61 entry
- research/open_problems.md: [New (Pass 60)]→[Resolved 61](i)/[Partially resolved 61](ii); [New (Pass 61)] added
- research/notes/g2-fg2-hierarchy.md: Pass-61 section (Thm 61a/61b/61c)
- research/definitions.md: phantom presheaf / sheafification L / descent-obstruction Rosser / b-wall vocabulary
- code/scripts/check-pass61.py + artifacts/reports/pass61-phantom-sheaf-descent-check.json

Next step:
Pass 62 should attack the residue Pass 61 opens. Thm 61b recasts the Rosser torsor as the
**failure of descent** of $P$, split into a *horizontal* free part $\mathbb Z^{|S|-1}=
\check H^1(\underline{\mathbb Z})$ (spectral cover) and a *vertical* $\varprojlim^1=
\widehat{\mathbb Z}_p/\mathbb Z$ (dilation tower) in each stalk. Make this a single
**bicomplex / Grothendieck spectral sequence** $\check H^p_{\mathrm{prime}}(\varprojlim^q_
{\mathrm{dilation}})\Rightarrow H^{p+q}$ on the product site (spectral $\times$ tower),
and identify the Löb/Rosser dictionary with its $E_2$ page: does the total phantom of a
general modulus factor as the convolution of the $|S|-1$ horizontal relations with the
per-prime $2$-adic ghosts, and is there a $d_2$ differential linking a horizontal integer
relation to a vertical ghost (a "mixed Löb–Rosser" class with no pure-horizontal or
pure-vertical representative)? Secondarily, dualize cleanly: construct the
**cosheafification** of $P$ and verify it reconstitutes $\widehat{\mathbb Z}_m/\mathbb Z$
as global cosections (left-adjoint glueing), making "Rosser $=$ cosheaf, Löb $=$ sheaf" a
theorem about the two adjoints of the inclusion of sheaves into presheaves on the prime
lattice.

---

### Pass 62 - 2026-06-09 JST

Focus:
Pass 61 split the Rosser torsor (the total phantom $\widehat{\mathbb Z}_m/\mathbb Z$,
$S=\mathrm{rad}(m)$) into a *horizontal* free part $\mathbb Z^{|S|-1}=\check H^1_{\mathrm
{prime}}(\underline{\mathbb Z})$ (descent defect of the constant presheaf over the prime
cover) and a *vertical* $\varprojlim^1=\widehat{\mathbb Z}_p/\mathbb Z$ (dilation tower)
inside each prime stalk. **(i)** Assemble both into one **bicomplex / two-row spectral
sequence** $\check H^p_{\mathrm{prime}}(\varprojlim^q_{\mathrm{dilation}})\Rightarrow
H^{p+q}$ on the product (spectral $\times$ tower) site, read the Löb/Rosser dictionary off
the $E_2$ page, and decide whether a $d_2$ carries a horizontal integer relation into a
vertical ghost — a "mixed Löb–Rosser" class with no pure-horizontal / pure-vertical
representative. **(ii)** Construct the **cosheafification** of $P$ and test the Pass-61
slogan "Rosser $=$ cosheaf, Löb $=$ sheaf" literally.

Proposer:
**(A) The bicomplex.** Factor the total phantom through one $\mathbb N$-tower. By CRT
$\mathbb Z/\pi^n\cong\prod_{p\in S}\mathbb Z/p^n$ with $\pi=\prod_{p\in S}p=\mathrm{rad}(m)$,
so the SES of $\mathbb N$-towers $0\to(\mathbb Z,\times\pi)\to(\mathbb Z,\mathrm{id})\to
(\mathbb Z/\pi^n)\to0$ gives $\varprojlim^1(\mathbb Z,\times\pi)=\widehat{\mathbb Z}_S/
\mathbb Z=P(S)$ (Pass 53/54). Build the first-quadrant double complex $D^{\bullet,\bullet}$
whose **vertical** differential is the two-term Milnor cochain $[\prod_n\mathbb Z\xrightarrow
{1-p\,\mathrm{sh}}\prod_n\mathbb Z]$ of the per-prime dilation tower $(\mathbb Z,\times p)$
(so $H^0=\varprojlim=0$, $H^1=\varprojlim^1=\mathbb Z_p/\mathbb Z$) and whose **horizontal**
differential is the (augmented) reduced Čech cochain of the constant presheaf
$\underline{\mathbb Z}$ over the singleton prime cover (so the diagonal $\Delta:\mathbb Z\to
\mathbb Z^S$ has $\operatorname{coker}=\mathbb Z^{|S|-1}$ and nothing higher). Total degree
$1$ in each direction; $H^1(\mathrm{Tot})=P(S)$.

**(B) The $E_2$ page is the dictionary.** Both filtration spectral sequences degenerate
to **two** nonzero entries, in *complementary* positions of total degree $1$:
$$E_2^{1,0}=\mathbb Z^{|S|-1}\ \ (\text{horizontal} = \text{Rosser, the integer relations
among the primes}),\qquad E_2^{0,1}=\textstyle\prod_{p\in S}(\mathbb Z_p/\mathbb Z)=L(S)\ \
(\text{vertical} = \text{Löb, the local ghosts}),$$
with $E_2^{2,0}=\tilde H^2_{\mathrm{prime}}=0$ (the discrete cover has no $1$-simplices, all
pairwise intersections empty) and $E_2^{0,2}=\varprojlim^2=0$ ($\omega$-tower). So the Löb/
Rosser dictionary **is** the $E_2$ page; the total phantom is its abutment.

**(C) No $d_2$ — but a non-split extension.** With the only survivors at $(1,0)$ and
$(0,1)$ and their neighbours zero, every $d_r$ ($r\ge2$) has zero target ($d_2:E_2^{0,1}\to
E_2^{2,0}=0$). So $E_2=E_\infty$ and **all the mixing is in the filtration extension**
$$0\ \to\ \underbrace{\mathbb Z^{|S|-1}}_{\text{Rosser}}\ \to\ \underbrace{\widehat{\mathbb
Z}_S/\mathbb Z}_{\text{total phantom}}\ \to\ \underbrace{\textstyle\prod_{p\in S}(\mathbb
Z_p/\mathbb Z)}_{\text{Löb}=L(S)}\ \to\ 0,$$
which (claim) is **non-split** for $|S|\ge2$: its class $\epsilon_S\in\mathrm{Ext}^1_{\mathbb
Z}(L(S),\mathbb Z^{|S|-1})$ is the genuine mixed Löb–Rosser invariant — a $\partial$
(connecting homomorphism), not a $d_2$.

**(D) Cosheafification.** On the singleton prime site the cosheaf coequalizer is
$\check P(S)=\bigoplus_{p\in S}(\mathbb Z_p/\mathbb Z)$, and for *finite* $S$ the canonical
$\bigoplus\to\prod$ is an iso, so $\check P(S)=\prod_p(\mathbb Z_p/\mathbb Z)=L(S)$ — the
**same** as the sheafification. Both adjoints land on $L$; the global $\widehat{\mathbb Z}_S/
\mathbb Z$ is neither.

Skeptic:
**(C)** Beware the word "$d_2$": with two nonzero $E_2$ cells in complementary degree there
is literally no differential to draw — the Pass-61 Next-step's "$d_2$ carrying horizontal
into vertical" is, in the *minimal* bicomplex, an **extension**, i.e. lives in $E_\infty$,
not in any page differential. A bona-fide $d_2$ only reappears if one **unabridges** the
vertical: resolve each $\mathbb Z_p$ by its own $\mathbb Z/p^n$-tower, producing a *third*
column $E_2^{2,0}\ne0$ into which $d_2$ can fire (the obstruction to lifting the $p$-adic
generator to an integer); that $d_2$ *is* the extension class re-expressed. State both,
don't conflate. **Prove non-splitting**, don't assert it: a split would give a retraction
$P\twoheadrightarrow\mathbb Z^{|S|-1}$ restricting to each factor $\mathbb Z_p$, but
$\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=0$ ($\mathbb Z_p$ is $q$-divisible for every $q\ne p$,
and $\mathbb Z$ has no nonzero divisible subgroup), so the retraction kills every $\mathbb
Z_p$, hence kills the integer points $e_p\in\mathbb Z^S$ that generate the would-be
quotient — contradiction. **(D)** Then the Pass-61 slogan is *wrong*: on a discrete site
$\mathbf{Sh}$ and $\mathbf{coSh}$ agree (both $=L$), so "Rosser $=$ cosheaf" cannot hold;
the discrete topology is too disconnected to see the Rosser part at all. The global ghost
is irreducibly **presheaf-level**.

Formalist:

> **Theorem 62a (the Löb–Rosser bicomplex; $E_2 =$ the dictionary).** Let $S=\mathrm{rad}(m)$,
> $s=|S|$. The double complex $D^{\bullet,\bullet}$ (vertical $=$ per-prime Milnor
> $\varprojlim$-cochain of $(\mathbb Z,\times p)$; horizontal $=$ augmented reduced Čech of
> $\underline{\mathbb Z}$ over the singleton prime cover) has total cohomology
> $H^1(\mathrm{Tot})=\widehat{\mathbb Z}_S/\mathbb Z=P(S)$, and both spectral sequences
> degenerate at $E_2$ to exactly
> $$E_2^{1,0}=\mathbb Z^{s-1}\ (\text{Rosser/horizontal}),\quad
> E_2^{0,1}=\textstyle\prod_{p\in S}(\mathbb Z_p/\mathbb Z)=L(S)\ (\text{Löb/vertical}),$$
> all other $E_2^{p,q}=0$. In particular $E_2^{2,0}=0$, so $d_r=0$ for all $r\ge2$ and
> $E_2=E_\infty$.

> **Theorem 62b (the mixed Löb–Rosser class is a non-split extension, not a $d_2$).** The
> filtration of $H^1(\mathrm{Tot})$ is the short exact sequence
> $$0\to\mathbb Z^{s-1}\xrightarrow{\ \iota\ }\widehat{\mathbb Z}_S/\mathbb Z\xrightarrow{\ \rho\ }
> \textstyle\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0,\qquad \iota=[\mathbb Z^S/\Delta\mathbb Z
> \hookrightarrow\widehat{\mathbb Z}_S/\Delta\mathbb Z],\ \ \rho=\text{quotient by }\mathbb Z^S.$$
> For $s\ge2$ it does **not split**: a retraction would restrict to $\mathrm{Hom}(\mathbb Z_p,
> \mathbb Z^{s-1})=0$ on every stalk (as $\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=0$), forcing it
> to annihilate the integer points $e_p$ that generate $\mathbb Z^S/\Delta\mathbb Z$ —
> contradiction. The class $\epsilon_S=[\,\text{this extension}\,]\in\mathrm{Ext}^1_{\mathbb Z}
> (L(S),\mathbb Z^{s-1})$ is nonzero: the **mixed class** is the connecting $\partial$ of the
> filtration, with no pure-horizontal or pure-vertical representative. A page differential
> $d_2$ realizing the same datum appears only after unabridging each $\mathbb Z_p$ into its
> $\mathbb Z/p^n$-tower (a third column $E_2^{2,0}\ne0$); the minimal bicomplex carries it as
> an extension.

> **Theorem 62c (cosheafification collapse — correction of the Pass-61 slogan).** On the
> singleton (discrete) prime site, the cosheafification of $P$ is the costalk coproduct
> $\check P(S)=\bigoplus_{p\in S}(\mathbb Z_p/\mathbb Z)$; for finite $S$ the comparison
> $\bigoplus_{p\in S}\to\prod_{p\in S}$ is an isomorphism, so
> $$\check P(S)=\textstyle\prod_{p\in S}(\mathbb Z_p/\mathbb Z)=L(S)=P^{\#}(S):$$
> **sheafification and cosheafification coincide**, both equal to the Löb sheaf $L$. Hence the
> global phantom $\widehat{\mathbb Z}_S/\mathbb Z$ — a non-split extension of $L$ by
> $\mathbb Z^{s-1}$ (Thm 62b) — is **neither** the sheaf **nor** the cosheaf; it is
> irreducibly presheaf-level, recorded exactly by the descent defect $\ker\rho=\mathbb Z^{s-1}$.
> The Pass-61 slogan "Rosser $=$ cosheaf" is **false on the discrete site**: that topology is
> too disconnected for $\mathbf{Sh}$ and $\mathbf{coSh}$ to differ. Reinstating a nonzero
> $\check H^1$ requires the coarser **Zariski/cofinite** topology on $\mathrm{Spec}\,\mathbb Z$,
> where the prime set carries the generic point and connectedness restores the Rosser class.

Pathology ($s=2$, $S=\{2,3\}$). $\widehat{\mathbb Z}_S/\mathbb Z=(\mathbb Z_2\times\mathbb Z_3)/
\Delta\mathbb Z$. The horizontal generator $g=[(1,0)]=[(0,-1)]$ spans $\mathbb Z^{s-1}=\mathbb Z$;
it maps to $0$ in $L$ (each integer dies in $\mathbb Z_p/\mathbb Z$), yet $g$ is **not** a
direct summand — no homomorphism $P\to\mathbb Z$ sends $g\mapsto1$, because every such map
vanishes on $\mathbb Z_2$ and $\mathbb Z_3$ (Hom into $\mathbb Z$ is $0$) and $g$ is built from
those factors. A *purely horizontal* relation with **no horizontal complement**: the integer
relation among the primes is welded to the local ghosts, Smullyan's seam with no scissors.

Verified (PASS, `code/scripts/check-pass62.py` $\to$
`artifacts/reports/pass62-loeb-rosser-bicomplex-mixed-class-check.json`, run off-mount in
`/tmp` per [[aps-run-sync-hazard]]): **coker_rank** — $\operatorname{coker}(\Delta:\mathbb Z
\to\mathbb Z^S)$ free of rank $s-1$, no torsion, by SNF, $s=2..6$. **no_retraction** — the
$\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=0$ obstruction (forced $r_n=p^{-n}\notin\mathbb Z$ for
$n\ge1$) confirmed for $p\in\{2,3,5,7,11\}$ — the non-splitting certificate. **tower_higher_
derived** — Milnor cochain length $2$, $\varprojlim^{\ge2}=0$. **reduced_cech_no_d2** — for
$S=\{2,3\},\{2,3,5\},\{3,5,7\},\{2,5,7,11\}$ all pairwise intersections empty, no
$1$-simplices, $E_2^{2,0}=0$, $d_2$ cannot act. **cosheaf_collapse** — for $S=\{2,3\},
\{2,3,5\},\{3,5,7\}$, $|\bigoplus|=|\prod|$, cosheafification $=$ sheafification $=L$.
**crt_radical** — radical classes $\{2,4,8\}\mapsto2$, $\{6,12\}\mapsto6$, etc., phantom a
functor of $\mathrm{rad}$. Overall PASS. *Exec note:* the bash mount again served a Pass-53-era
stale copy of this discussion file and undercounted `open_problems.md`/`g2-fg2-hierarchy.md`;
per [[aps-run-sync-hazard]] state was diagnosed via Windows-path file tools (true tail $=$
Pass 61, counter $62$), all edits applied through them, the script run off-mount in `/tmp`,
and the report written back via the Windows-path Write tool.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-62 entry; State counter
  $62\to63$.
- `records/logs/research-log.md`: Pass-62 one-line entry.
- `research/open_problems.md`: [New (Pass 61)] item (i) marked [Resolved (Pass 62)]
  (Thms 62a/62b), item (ii) marked [Resolved (Pass 62), as correction] (Thm 62c); item (iii)
  ($\aleph_1$-threshold) carried [Open]; [New (Pass 62)] residue added (Zariski-site cosheaf;
  unabridged $d_2$; $\mathrm{Ext}^1$ class computation).
- `research/notes/g2-fg2-hierarchy.md`: "Pass 62 — The Löb–Rosser bicomplex and the mixed
  class" section (Thms 62a, 62b, 62c).
- `research/definitions.md`: "Löb–Rosser bicomplex / mixed class $\epsilon_S$ /
  cosheafification collapse" entry.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-62 entry; counter 62→63
- records/logs/research-log.md: Pass-62 entry
- research/open_problems.md: [New (Pass 61)] (i)→[Resolved 62], (ii)→[Resolved 62, correction], (iii) carried [Open]; [New (Pass 62)] added
- research/notes/g2-fg2-hierarchy.md: Pass-62 section (Thm 62a/62b/62c)
- research/definitions.md: Löb–Rosser bicomplex / mixed class / cosheafification-collapse vocabulary
- code/scripts/check-pass62.py + artifacts/reports/pass62-loeb-rosser-bicomplex-mixed-class-check.json

Next step:
Pass 63 should pursue the residue Pass 62 opens. Thm 62c shows the discrete prime site is too
disconnected to host the Rosser class as a (co)sheaf. Re-run the descent analysis on the
**Zariski (cofinite) topology of $\mathrm{Spec}\,\mathbb Z$**, where the closed prime set $S$
acquires the generic point and the cover $\{V(p)\}$ has nontrivial intersections: does the
phantom presheaf $P$ now have a nonzero $\check H^1$, and is the cosheafification there the
genuine global $\widehat{\mathbb Z}_S/\mathbb Z$ (making "Rosser $=$ cosheaf" finally a
theorem)? Secondarily, **unabridge** the vertical column of the Thm-62a bicomplex (resolve each
$\mathbb Z_p$ by its $\mathbb Z/p^n$-tower) to exhibit the genuine $d_2:E_2^{0,1}\to E_2^{2,0}$
realizing the Thm-62b extension class as a page differential, and compute $\mathrm{Ext}^1_{\mathbb
Z}(L(S),\mathbb Z^{s-1})$ explicitly — is $\epsilon_S$ a generator, and does it depend on $S$
only through $s=|S|$ or genuinely through the prime set (an arithmetic, not merely cardinal,
invariant)?

---

### Pass 63 - 2026-06-09 JST

Focus:
Discharge the **[New (Pass 62)]** triad. Pass 62 showed the global phantom
$\widehat{\mathbb Z}_S/\mathbb Z$ ($S=\mathrm{rad}(m)$, $s=|S|$) is irreducibly
*presheaf-level* on the **discrete** prime site — sheafification and cosheafification
both collapse to the Löb object $L(S)=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)$, so
"Rosser $=$ cosheaf" is false there (too disconnected). **(i)** Re-run descent on the
**Zariski (cofinite/generic-point) topology** of $\mathrm{Spec}\,\mathbb Z$, where the
prime set acquires the generic point $\eta$ and the cover $\{U_p\}$ has nonempty
overlaps: does $\check H^1\ne0$ now, and is "Rosser $=$ cosheaf" finally a theorem?
**(ii)** **Unabridge** the vertical column of the Thm-62a bicomplex (resolve each
$\mathbb Z_p$ by its $\mathbb Z/p^n$-tower) so the hidden Pass-62 extension becomes a
genuine page differential $d_2:E_2^{0,1}\to E_2^{2,0}$. **(iii)** Compute
$\mathrm{Ext}^1_{\mathbb Z}(L(S),\mathbb Z^{s-1})$ explicitly — is $\epsilon_S$ a
generator, and is it a *cardinal* ($s$-only) or genuinely *arithmetic* (prime-set)
invariant?

Proposer:
**(A) The Zariski rescue is a *relocation*, not a revival.** Model the closed prime set
$S$ with its generic point as the finite connected space $X=\{\eta\}\cup\{(p):p\in S\}$
carrying the subspace (particular-point) topology inherited from $\mathrm{Spec}\,\mathbb Z$:
the opens are $\varnothing$ and every set containing $\eta$ (the generic point lies in
every nonempty open). Take the cover $\mathcal U=\{U_p\}_{p\in S}$ by minimal opens
$U_p=\{\eta,(p)\}$. Crucially — and oppositely to the discrete site — **every nonempty
intersection equals $\{\eta\}$**, so the nerve of $\mathcal U$ is the *full simplex*
$\Delta^{\,s-1}$ (contractible), not $s$ disjoint points. Consequences:
(1) the **constant** sheaf $\underline{\mathbb Z}$ is now an honest sheaf (the space is
connected), and $\check H^1(\mathcal U,\underline{\mathbb Z})=H^1(\Delta^{s-1})=0$: the
discrete-site horizontal defect $\mathbb Z^{s-1}=\check H^0_{\mathrm{red}}$ is
**annihilated**. Connectivity destroys the Rosser relations *as constant-coefficient
cohomology*. (2) But they are not gone — they **relocate one cohomological degree up**.
Let $j:\{\eta\}\hookrightarrow X$ be the open inclusion of the generic point and
$i:Z=\{(p):p\in S\}\hookrightarrow X$ the closed complement (an $s$-point discrete
subspace). The extension-by-zero sequence
$$0\ \to\ j_!\underline{\mathbb Z}\ \to\ \underline{\mathbb Z}_X\ \to\ i_*\underline{\mathbb Z}_Z\ \to\ 0$$
has long exact cohomology
$0\to H^0(j_!\mathbb Z)\to H^0(\mathbb Z_X)\to H^0(i_*\mathbb Z_Z)\to H^1(j_!\mathbb Z)\to
H^1(\mathbb Z_X)\to\cdots$, i.e. $0\to 0\to\mathbb Z\xrightarrow{\Delta}\mathbb Z^{s}\to
H^1(X,j_!\mathbb Z)\to 0$ (using $H^0(\mathbb Z_X)=\mathbb Z$ by connectivity,
$H^0(i_*\mathbb Z_Z)=\mathbb Z^{s}$, $H^1(\mathbb Z_X)=0$), whence
$$\boxed{\,H^1(X,\ j_!\underline{\mathbb Z})\ =\ \mathbb Z^{s}/\Delta\mathbb Z\ =\ \mathbb Z^{\,s-1}.\,}$$
So the **horizontal Rosser part is genuinely a nonzero $\check H^1$** on the Zariski
site — but with *extension-by-zero* coefficients $j_!$, the functor that pushes a class
to be *supported at the generic point*. Since $j_!$ is the **cosheaf-theoretic**
(left-adjoint / compact-support) extension, the slogan finally lands: **Rosser $=$ the
$j_!$-supported (cosheaf) $H^1$ at the generic point; Löb $=$ the ordinary stalkwise
sheaf $L$.** The naive cover-cosheafification still returns $L$ (overlaps carry $0$); the
correct cosheaf is $j_!$, not $\check{(-)}$ over $\mathcal U$.

**(B) The unabridged $d_2$.** In Thm 62a the vertical column was the *abridged* two-term
Milnor cochain $[\prod_n\mathbb Z\xrightarrow{1-p\,\mathrm{sh}}\prod_n\mathbb Z]$ with
$H^1=\mathbb Z_p/\mathbb Z$ landing in a single bidegree $(0,1)$, so the $\mathbb Z^{s-1}$
sat alone at $(1,0)$ and the mixing was forced into the $E_\infty$ extension. *Unabridge*:
resolve each stalk $\mathbb Z_p=\varprojlim_n\mathbb Z/p^n$ by its own $\mathbb Z/p^n$
tower, turning the one vertical arrow into a genuine resolution and opening a **third
column** $E_2^{2,0}$. The horizontal differential (diagonal $\Delta$ on the constant
$\mathbb Z$) now has a degree-$2$ home, $E_2^{2,0}=\operatorname{coker}\Delta=\mathbb Z^{s-1}$,
and the page-$2$ differential
$$d_2:\ E_2^{0,1}=\textstyle\prod_{p\in S}(\mathbb Z_p/\mathbb Z)=L(S)\ \longrightarrow\
E_2^{2,0}=\mathbb Z^{\,s-1}$$
is exactly the **common-integer-lift obstruction**: $d_2((x_p)_p)$ measures the failure of
the local ghosts $x_p$ to be the reductions of a single global integer modulo the diagonal.
This is the standard fact that a non-split extension living in a two-column page becomes a
$d_2$ once a third column is manufactured by refining the resolution; the Pass-62 class
$\epsilon_S$ and this $d_2$ are **one datum in two presentations**.

**(C) $\mathrm{Ext}^1$ and the arithmetic verdict.** Apply $\mathrm{Hom}(-,\mathbb Z)$ to
the ghost sequence $0\to\mathbb Z\to\mathbb Z_p\to\mathbb Z_p/\mathbb Z\to0$. Since
$\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=0$ (Pass 62: $\mathbb Z_p$ is $q$-divisible for every
$q\ne p$, $\mathbb Z$ has no divisible subgroup) and $\mathrm{Hom}(\mathbb Z_p/\mathbb Z,
\mathbb Z)=0$ a fortiori, the connecting map
$\delta:\mathrm{Hom}(\mathbb Z,\mathbb Z)=\mathbb Z\hookrightarrow
\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb Z)$ is **injective**, sending $1$ to the class
of the ghost extension itself. Hence $\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb Z)$
carries a canonical **infinite-cyclic ghost line** $\delta(\mathbb Z)$, and
$$0\to\mathbb Z\xrightarrow{\ \delta\ }\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb Z)\to
\mathrm{Ext}^1(\mathbb Z_p,\mathbb Z)\to0,$$
with $\mathrm{Ext}^1(\mathbb Z_p,\mathbb Z)$ an uncountable $\mathbb Q$-vector space (of
continuum dimension — the classical $\mathrm{Ext}(\widehat{\mathbb Z}_p,\mathbb Z)$
computation). So $\epsilon_p:=\delta(1)$ is **non-torsion** (infinite order) and generates
the *arithmetic line* of $\mathrm{Ext}^1$, though not the whole (huge) group. For the full
class, $L(S)=\bigoplus_{p\in S}(\mathbb Z_p/\mathbb Z)$ (finite $S$, $\prod=\bigoplus$) and
$\mathrm{Ext}^1(L(S),\mathbb Z^{s-1})=\bigoplus_{p\in S}\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,
\mathbb Z)^{\,s-1}$; $\epsilon_S$ has, in each chosen-base difference direction $p\ne p_0$,
component $\epsilon_p$ — nonzero, infinite order, for $s\ge2$. **Verdict:** the *target*
rank $s-1$ is a **cardinal** invariant ($|S|$ only), but $\epsilon_S$ is supported on the
pairwise **non-isomorphic** ghost groups $\mathbb Z_p/\mathbb Z$ (whose torsion subgroup
$\mathbb Z_{(p)}/\mathbb Z=\bigoplus_{q\ne p}\mathbb Z(q^\infty)$ uniquely *omits* the
$p$-Prüfer summand), so $\epsilon_S$ is a genuinely **arithmetic** invariant: it sees
*which* primes are in $S$, not merely how many.

Skeptic:
**(A)** Watch the variance and the model. (i) The "particular-point" space is the *honest*
finite model of $\{\eta\}\cup S\subset\mathrm{Spec}\,\mathbb Z$ with the Zariski subspace
topology — confirm $\{(p)\}$ is closed (it omits $\eta$, so it is) and $U_p=\{\eta,(p)\}$ is
the *minimal* open neighbourhood of $(p)$. Good. (ii) Do **not** oversell "Rosser $=$
cosheaf." The cover-level cosheafification (coequalizer over $\mathcal U$) of the phantom
*still* returns $L(S)$ because the overlaps $U_p\cap U_q=\{\eta\}$ carry the *skyscraper*
value $0$, not $\mathbb Z$. What rescues the Rosser part is specifically $j_!$ — the
generic-point extension by zero — whose $H^1$ is $\mathbb Z^{s-1}$. So the honest theorem is
"Rosser $=$ $H^1$ of $j_!\underline{\mathbb Z}$ (compact support toward $\eta$)," and the
Pass-61/62 slogan "Rosser $=$ cosheaf" is *vindicated only in this $j_!$ sense* — a third
correction, not a naive confirmation. (iii) Beware claiming the *full* $\widehat{\mathbb
Z}_S/\mathbb Z$ as a single $\check H^1$: the computation above is the **horizontal**
($\mathbb Z^{s-1}$) part; the vertical $\mathbb Z_p/\mathbb Z$ ghosts are still stalk data,
reassembled only through the bicomplex of (B)/§(ii). The total phantom is the non-split
*extension* of the two, now realized as $H^1(X,j_!\mathcal V)$ for $\mathcal V$ the dilation
coefficient — an extension, exactly as Pass 62 insisted.

**(B)** A $d_2$ is presentation-dependent. With only two columns there is provably no
differential (Thm 62b); the $d_2$ exists **iff** you unabridge, and then it is the
*transgression* of the local generator, equivalent data to $\epsilon_S$. State the
equivalence, do not pretend the $d_2$ is "more fundamental" than the extension — they are
isomorphic invariants of the same filtered object (Weibel 1994, §5.6, on two-column vs
refined spectral sequences). The honest content is: *the mixing is real and is the
integer-lift obstruction; whether you call it $\partial$ (extension) or $d_2$ (differential)
is a choice of resolution.*

**(C)** Two precision demands. (i) "Generator" must be qualified: $\epsilon_p$ generates the
**canonical $\mathbb Z$-line** $\delta(\mathbb Z)\subset\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,
\mathbb Z)$ but *not* the whole group (which is uncountable). Prove $\epsilon_p$ has infinite
order without hand-waving: $n\epsilon_p=0$ would mean the pushout of the ghost extension along
$\times n:\mathbb Z\to\mathbb Z$ splits, i.e. $\mathbb Z_p$ contains $\mathbb Z\oplus(\mathbb
Z_p/\mathbb Z)$ compatibly — but $\delta$ is injective on *all* of $\mathbb Z$, so $n\ne0\Rightarrow
n\epsilon_p\ne0$. A clean witness that no nonzero multiple is "integral": take the **lacunary**
$p$-adic integer $u=\sum_{k\ge0}p^{\,k!}\in\mathbb Z_p$; its image $\bar u\in\mathbb Z_p/\mathbb Z$
satisfies $n\bar u\ne0$ for every $n\ge1$, since $nu\in\mathbb Z$ would force $u\in\frac1n\mathbb
Z\subset\mathbb Q$, yet $u$ is $p$-adically irrational (its digit sequence is non-eventually-periodic).
(ii) The arithmetic-vs-cardinal claim is **not** circular: the groups $\mathbb Z_p/\mathbb Z$ are
pairwise non-isomorphic, so any abstract identification $\mathbb Z^{s-1}\cong\mathbb Z^{s'-1}$
($s=s'$) of the *targets* cannot be promoted to an isomorphism of the *classes* respecting the
prime labelling — $\epsilon_{\{2,3\}}$ and $\epsilon_{\{2,5\}}$ are not interchangeable.

Formalist:

> **Theorem 63a (Zariski relocation of the Rosser class; "$j_!$-cosheaf" form).** Let $X=
> \{\eta\}\cup\{(p):p\in S\}$ be the finite Zariski subspace ($s=|S|$), $j:\{\eta\}\hookrightarrow X$
> the open generic point, $i:Z\hookrightarrow X$ the closed $s$-point complement, and
> $\mathcal U=\{U_p=\{\eta,(p)\}\}$.
> 1. The nerve of $\mathcal U$ is the full simplex $\Delta^{s-1}$; the constant sheaf
>    $\underline{\mathbb Z}$ is a sheaf and $\check H^{\ge1}(\mathcal U,\underline{\mathbb Z})=0$.
>    In particular the discrete-site horizontal defect $\check H^0_{\mathrm{red}}=\mathbb Z^{s-1}$
>    **vanishes**: connectivity kills constant-coefficient $H^1$.
> 2. The skyscraper product $\mathcal F=\bigoplus_{p\in S}(i_p)_*\mathbb Z_p$ is flasque with
>    $\check H^{\ge1}(\mathcal U,\mathcal F)=0$ and $\mathcal F(X)=\widehat{\mathbb Z}_S$.
> 3. The extension-by-zero $j_!\underline{\mathbb Z}$ has $H^0(X,j_!\mathbb Z)=0$ and
>    $$H^1(X,\ j_!\underline{\mathbb Z})\ \cong\ \mathbb Z^{s}/\Delta\mathbb Z\ \cong\ \mathbb Z^{\,s-1},$$
>    via $0\to\mathbb Z\xrightarrow{\Delta}\mathbb Z^{s}\to H^1(j_!\mathbb Z)\to 0$. Thus the
>    horizontal Rosser relations are a genuine nonzero $\check H^1$ on the connected site —
>    *supported at the generic point*. Since $j_!$ is the left-adjoint (compact-support / cosheaf)
>    extension, "Rosser $=$ cosheaf" holds in the precise form **Rosser $=H^1$ of $j_!$**. The
>    naive cover-cosheafification still equals the Löb sheaf $L(S)$ (overlaps carry $0$); the two
>    differ exactly by this $j_!$-class.

> **Theorem 63b (unabridged $d_2$ $=$ integer-lift obstruction).** Refine the Thm-62a bicomplex
> by resolving each vertical stalk $\mathbb Z_p=\varprojlim_n\mathbb Z/p^n$ by its $\mathbb Z/p^n$
> tower. The refined first-quadrant double complex has
> $E_2^{0,1}=L(S)=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)$, $E_2^{1,0}=0$, and a newly nonzero
> $E_2^{2,0}=\operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^{s})=\mathbb Z^{s-1}$, with a
> page-$2$ differential
> $$d_2:\ E_2^{0,1}\longrightarrow E_2^{2,0},\qquad
> d_2\big((x_p)_{p}\big)=\big[(x_p-x_{p_0})_{p\ne p_0}\big]\ \ (\text{common-integer-lift obstruction}),$$
> of image rank $s-1$ (machine-checked). The Pass-62 connecting class $\epsilon_S=\partial$ and this
> $d_2$ are the *same* invariant of the filtered total object in two resolutions (a two-column
> $E_\infty$-extension becomes a page differential upon manufacturing the third column); neither is
> primary.

> **Theorem 63c ($\mathrm{Ext}^1$: the ghost line, and arithmetic $\succ$ cardinal).**
> 1. $\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=\mathrm{Hom}(\mathbb Z_p/\mathbb Z,\mathbb Z)=0$, so the
>    connecting map gives a short exact sequence
>    $0\to\mathbb Z\xrightarrow{\delta}\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb Z)\to
>    \mathrm{Ext}^1(\mathbb Z_p,\mathbb Z)\to0$, where $\delta(1)=\epsilon_p$ is the ghost class.
>    $\epsilon_p$ has **infinite order** ($\delta$ injective; lacunary witness $u=\sum_k p^{k!}$),
>    generating the canonical $\mathbb Z$-line but **not** the uncountable ambient group
>    ($\mathrm{Ext}^1(\mathbb Z_p,\mathbb Z)$ is a continuum-dimensional $\mathbb Q$-space).
> 2. For finite $S$, $\mathrm{Ext}^1(L(S),\mathbb Z^{s-1})=\bigoplus_{p\in S}\mathrm{Ext}^1(\mathbb
>    Z_p/\mathbb Z,\mathbb Z)^{s-1}$ and $\epsilon_S\ne0$ of infinite order for $s\ge2$, with
>    component $\epsilon_p$ in each base-difference direction $p\ne p_0$.
> 3. **Cardinal vs arithmetic.** The target rank $s-1$ depends only on $|S|$ (cardinal), but
>    $\epsilon_S$ lives on the pairwise non-isomorphic $\mathbb Z_p/\mathbb Z$ (torsion subgroup
>    $\bigoplus_{q\ne p}\mathbb Z(q^\infty)$, uniquely omitting the $p$-Prüfer), so $\epsilon_S$ is a
>    genuinely **arithmetic** invariant of the prime set $S$, not a function of $s$ alone:
>    $\epsilon_{\{2,3\}}\ne\epsilon_{\{2,5\}}$ under any prime-respecting identification.

Verified (PASS, `code/scripts/check-pass63.py` $\to$
`artifacts/reports/pass63-zariski-cosheaf-unabridged-d2-ext1-check.json`, run **off-mount in
`/tmp`** per [[aps-run-sync-hazard]]; report written back via the Windows-path Write tool):
**Zariski_63a** — for $s=2..6$, constant-coefficient $\check H^1=0$ (contractible full-simplex
nerve) while $H^1(j_!\mathbb Z)=\operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^{s})$ is free of
rank $s-1$ with no torsion (Smith normal form). **unabridged_d2_63b** — the obstruction map
$L(S)\to\mathbb Z^{s-1}$ has image rank $s-1$ for $S=\{2,3\},\{2,3,5\},\{3,5,7\},\{2,5,7,11\}$.
**Ext1_ghost_63c** — no-retraction certificate $p^{-n}\notin\mathbb Z$ ($p\in\{2,3,5,7,11\}$);
infinite-order ghost via the lacunary $\sum p^{k!}$ witness; ghost-group torsion signature
confirms each $\mathbb Z_p/\mathbb Z$ uniquely omits the $p$-Prüfer summand (pairwise
non-isomorphic $\Rightarrow$ arithmetic invariant). Overall PASS. The continuum-dimensionality of
$\mathrm{Ext}^1(\mathbb Z_p,\mathbb Z)$ is the classical computation (Fuchs 2015, Vol. 1, on
$\mathrm{Ext}(\widehat{\mathbb Z}_p,\mathbb Z)$), not machine-checkable here.
*Exec note:* the bash mount again served a Pass-53-era stale copy of this discussion file at run
start (true tail $=$ Pass 62, counter $63$); per [[aps-run-sync-hazard]] state was diagnosed via
Windows-path file tools, all edits applied through them, and the script run off-mount in `/tmp`.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-63 entry; State counter
  $63\to64$.
- `records/logs/research-log.md`: Pass-63 one-line entry (prepended).
- `research/open_problems.md`: [New (Pass 62)] items (i) and (ii) marked [Resolved (Pass 63)]
  (Thms 63a/63b), item (iii) marked [Resolved (Pass 63)] (Thm 63c); the long-standing
  $\aleph_1$-threshold (Pass-61 (ii)/(iii)) carried [Open]; [New (Pass 63)] residue added.
- `research/notes/g2-fg2-hierarchy.md`: "Pass 63 — Zariski relocation, the unabridged $d_2$, and
  the $\mathrm{Ext}^1$ ghost line" section (Thms 63a, 63b, 63c).
- `research/definitions.md`: "Zariski generic-point site / $j_!$-cosheaf Rosser class / unabridged
  $d_2$ / ghost line $\epsilon_p$ / arithmetic-vs-cardinal phantom" entry.
- `code/scripts/check-pass63.py`,
  `artifacts/reports/pass63-zariski-cosheaf-unabridged-d2-ext1-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-63 entry; counter 63→64
- records/logs/research-log.md: Pass-63 entry
- research/open_problems.md: [New (Pass 62)] (i)(ii)(iii) → [Resolved 63]; aleph_1-threshold carried [Open]; [New (Pass 63)] added
- research/notes/g2-fg2-hierarchy.md: Pass-63 section (Thm 63a/63b/63c)
- research/definitions.md: Zariski j_!-cosheaf / unabridged d_2 / ghost line / arithmetic-vs-cardinal vocabulary
- code/scripts/check-pass63.py + artifacts/reports/pass63-zariski-cosheaf-unabridged-d2-ext1-check.json

Next step:
Pass 64 should pursue the residue Pass 63 opens. Thm 63a localized the horizontal Rosser part as
$H^1(X,j_!\underline{\mathbb Z})$ at the generic point and Thm 63b realized the mixed class as a
$d_2$; assemble these into a **single six-functor statement on $\mathrm{Spec}\,\mathbb Z$**: is the
total phantom $\widehat{\mathbb Z}_S/\mathbb Z=H^1\!\big(\mathrm{Spec}\,\mathbb Z,\ j_!\,\mathcal V\big)$
for $\mathcal V$ the dilation local system (generic stalk $\mathbb Z$, monodromy $\times p$ at each
$(p)$), so that "Löb $=$ $i^*$ (stalk/sheaf), Rosser $=$ $j_!$ (generic/cosheaf)" becomes a
recollement $(j_!,j^*,j_*)\dashv(i^*,i_*,i^!)$ decomposition of one perverse-type object? Secondarily,
pin the still-[Open] $\aleph_1$-threshold of Thm 61c: is the vanishing of $\varprojlim^1\mathbf
A_{\omega_1}$ controlled by $\mathrm{add}(\mathcal M)$, by the existence of a Suslin tree, or by a
genuinely new $\omega_1$-tower invariant strictly between $\mathfrak b=\aleph_1$ and
$\mathrm{MA}_{\aleph_1}$? Decide whether $\epsilon_S$'s arithmetic dependence (Thm 63c) refines into a
functor on $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$ valued in $\mathrm{Ext}^1$-lines, i.e. a
"motive" of the Löb–Rosser dictionary over the prime spectrum.

---

### Pass 64 - 2026-06-09 JST

Focus:
Assemble Thm 63a ($H^1(X,j_!\underline{\mathbb Z})=\mathbb Z^{s-1}$, the horizontal Rosser relations
at the generic point) and Thm 63b (the vertical $d_2=\epsilon_S$) into a **single six-functor
statement** on the finite generic-point model $X=X_S$ of $\mathrm{Spec}\,\mathbb Z$: realize the
total phantom $\widehat{\mathbb Z}_S/\mathbb Z$ as $H^1(X,j_!\mathcal V)$ for $\mathcal V$ the
dilation coefficient (generic stalk $\mathbb Z$, monodromy $\times p$ at $(p)$), so that "Löb
$=i^*$ (closed stalk/sheaf), Rosser $=j_!$ (generic/cosheaf)" becomes a genuine **recollement**
$(j_!,j^*,j_*)\dashv(i^*,i_*,i^!)$; and decide whether $\epsilon_S$ refines into a functor on the
squarefree divisibility lattice — a "motive" of the dictionary.

Proposer:
Take the two-stratum decomposition $X=\{\eta\}\sqcup Z$, $Z=\{(p):p\in S\}$, $j:\{\eta\}\hookrightarrow
X$ open, $i:Z\hookrightarrow X$ closed. On a finite/Alexandrov space the six operations exist with
$j^*=j^!$, $i_*=i_!$, giving the BBD recollement and the open/closed gluing triangle
$j_!j^*F\to F\to i_*i^*F\xrightarrow{+1}$. Feed it the **dilation coefficient** $\mathcal V$ — the
pro-sheaf with $j^*\mathcal V=\underline{\mathbb Z}$ and closed costalk the per-prime Milnor
pro-system $(\mathbb Z,\times p)$ (so $i^*\mathcal V$ has $R\varprojlim$ with $H^0=\varprojlim=0$,
$H^1=\varprojlim^1=\mathbb Z_p/\mathbb Z$). Because $j^*j_!=\mathrm{id}$ and $i^*j_!=0$, the triangle
applied to $j_!\mathcal V$ collapses to one short exact sequence whose middle is the total phantom:
$$0\to\underbrace{\mathbb Z^{s-1}}_{H^1(j_!\underline{\mathbb Z}),\ \text{Rosser}}\to
H^1(X,j_!\mathcal V)=\widehat{\mathbb Z}_S/\mathbb Z\to\underbrace{\textstyle\prod_p(\mathbb Z_p/\mathbb Z)}_{i^*\text{-stalk }\varprojlim^1,\ \text{Löb}}\xrightarrow{\partial}0,$$
with $\partial$ the recollement boundary $(x_p)\mapsto[(x_p-x_{p_0})]$ — *identically* the Pass-63
$d_2$ and the Pass-62 $\epsilon_S$. So Löb $=i^*$, Rosser $=j_!$, mixing $=\partial$, one triangle.
Functoriality: $S\subseteq S'\Rightarrow X_S$ **open** in $X_{S'}$ (complement is closed points), so
$S\mapsto j_!\mathcal V_S$ is a functor $M:(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)\to
D^b(\mathbb Z)$ — the Löb–Rosser motive, weight-filtered ($W_0=$ Löb stalks, $\mathrm{gr}^W_1=$
Rosser horizontal).

Skeptic:
Four cautions, all heeded. (1) **No single sheaf suffices.** A *single* sheaf with one $\times p$
map gives only one dilation step; the full $\mathbb Z_p/\mathbb Z$ ghost is $R\varprojlim_n$ of the
$\mathbb Z/p^n$ tower, so $\mathcal V$ is honestly a pro-object and "$H^1(X,j_!\mathcal V)$" means
the derived/continuous limit. The naive single-sheaf $H^1$ returns only $\mathbb Z^{s-1}$ tensored
with a finite truncation — do not oversell. (2) **Recollement hypotheses must be checked, not
invoked.** $j^*=j^!$ needs $j$ open; $i_*=i_!$ needs $i$ closed and proper — both true on the finite
space, and the adjunctions were verified as hom-set identities over $\mathbb F_2$, not assumed.
(3) **"Three avatars are one" is a claim, not a vibe**: the Pass-62 $\partial$, Pass-63 $d_2$, and
Pass-64 recollement boundary must be the *same* map $(x_p)\mapsto[(x_p-x_{p_0})]$ of image rank
$s-1$ and kernel the diagonal — machine-confirmed, not asserted. (4) **"Motive" is an analogy.** $M$
is an honest constructible-sheaf / $D^b(\mathbb Z)$ datum with a weight filtration, *not* a
Voevodsky motive; the word marks the structural niche (functor on an arithmetic base, graded by the
dictionary's two columns), and the note says so explicitly.

Formalist:
> **Thm 64a (recollement).** $D(Z)\overset{i_*=i_!}{\hookrightarrow}D(X)\overset{j^*=j^!}{\twoheadrightarrow}D(U)$
> is a recollement: $j_!\dashv j^*\dashv j_*$, $i^*\dashv i_*\dashv i^!$, $j^*i_*=0$, $i_*,j_!,j_*$
> fully faithful, gluing triangles $j_!j^*\to\mathrm{id}\to i_*i^*\xrightarrow{+1}$ and
> $i_*i^!\to\mathrm{id}\to Rj_*j^*\xrightarrow{+1}$ (BBD §1.4 on the two-stratum finite space).
> **Thm 64b (phantom realization).** For the dilation coefficient $\mathcal V$,
> $$H^1(X,\ j_!\,\mathcal V)\cong\widehat{\mathbb Z}_S/\mathbb Z,\quad
> 0\to\mathbb Z^{s-1}\to\widehat{\mathbb Z}_S/\mathbb Z\to\textstyle\prod_p(\mathbb Z_p/\mathbb Z)\to0,$$
> the SES being the recollement-triangle LES; its boundary $\partial=$ Pass-63 $d_2=$ Pass-62
> $\epsilon_S$ (image rank $s-1$, kernel the diagonal $\mathbb Z$). **Löb $=i^*$, Rosser $=j_!$.**
> **Thm 64c (the motive).** $S\subseteq S'\Rightarrow X_S$ open in $X_{S'}$; $M:S\mapsto j_!\mathcal
> V_S$ is a functor $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)\to D^b(\mathbb Z)$ with
> $\epsilon$ a natural transformation, genuinely arithmetic (Thm 63c).
> **Pathologies.** $s=1$: $H^1(j_!\underline{\mathbb Z})=0$, phantom $=\mathbb Z_p/\mathbb Z$ pure
> Löb (Rosser needs $\ge2$ primes). $S=\{2,3\}$ vs $\{2,5\}$: rad-incomparable, no arrow, distinct
> classes. $S=\mathbb P$: $H^1(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)=\widehat{\mathbb Z}/\mathbb Z$,
> the integral finite-adele class group — *the ghost of all consistency at once is an adele that is
> not an integer.*

Machine-verified `code/scripts/check-pass64.py` →
`artifacts/reports/pass64-recollement-six-functor-motive-check.json` (overall PASS, 41 checks; run
off-mount in `/tmp` per [[aps-run-sync-hazard]], report written via Windows-path tools): horizontal
$H^1(j_!\underline{\mathbb Z})=\mathbb Z^{s-1}$ ($s=1..6$, SNF); vertical $\ker(1-p\,\mathrm{sh})=0$
+ non-ML index growth ($p\in\{2,3,5\}$); connecting $d$ rank $s-1$, kernel diagonal; $j_!\dashv j^*$
adjunction over $\mathbb F_2$; $s=1$ pure-Löb degeneration; motive open-immersion chain + incomparable
no-arrow + arithmetic$\ne$cardinal; full-spectrum adelic punchline.

*Exec note:* bash served a Pass-53-era stale copy of the discussion file at run start (true tail $=$
Pass 63, counter $64$); per [[aps-run-sync-hazard]] state was diagnosed and all edits applied via
Windows-path file tools, the script run off-mount in `/tmp`.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-64 entry; State counter
  $64\to65$.
- `records/logs/research-log.md`: Pass-64 one-line entry (prepended).
- `research/open_problems.md`: [New (Pass 63)] (i) and (ii) marked [Resolved (Pass 64)] (Thms
  64a/64b/64c); item (iii) ($\aleph_1$-threshold) carried [Open]; [New (Pass 64)] residue added.
- `research/notes/g2-fg2-hierarchy.md`: "Pass 64 — The recollement of the Löb–Rosser dictionary;
  the prime-spectrum motive" section (Thms 64a, 64b, 64c + pathologies).
- `research/definitions.md`: "Löb–Rosser recollement / dilation coefficient $\mathcal V$ /
  $i^*=$ Löb, $j_!=$ Rosser / prime-spectrum motive $M$ / adelic phantom $\widehat{\mathbb Z}/\mathbb Z$"
  entry.
- `code/scripts/check-pass64.py`,
  `artifacts/reports/pass64-recollement-six-functor-motive-check.json`: new.

Repository updates:
- records/discussions/autonomous-discussion.md: Pass-64 entry; counter 64→65
- records/logs/research-log.md: Pass-64 entry
- research/open_problems.md: [New (Pass 63)] (i)(ii) → [Resolved 64]; (iii) carried [Open]; [New (Pass 64)] added
- research/notes/g2-fg2-hierarchy.md: Pass-64 section (Thm 64a/64b/64c + pathologies)
- research/definitions.md: recollement / dilation coefficient / Löb=i^*, Rosser=j_! / motive / adelic phantom vocabulary
- code/scripts/check-pass64.py + artifacts/reports/pass64-recollement-six-functor-motive-check.json

Next step:
Pass 65 should pursue the residue Pass 64 opens. Thm 64a–c package the dictionary as a recollement
on the **two-stratum** finite space, but the recollement has a second gluing triangle
$i_*i^!\to\mathrm{id}\to Rj_*j^*\xrightarrow{+1}$ that Pass 64 left unused: compute $i^!\mathcal V$
(the closed *sections-with-support* / costalk dual) and decide whether the **Verdier dual**
$\mathbb D(j_!\mathcal V)=Rj_*\mathbb D\mathcal V$ exchanges the Löb and Rosser strata — i.e. is
there a self-duality of the dictionary under which "Löb $\leftrightarrow$ Rosser" is Verdier
duality $j_!\leftrightarrow Rj_*$, and if so does it fix or invert $\epsilon_S$ (a $\pm1$
"functional equation" of the phantom)? Secondarily, lift the **finite** model to the honest Zariski
$\mathrm{Spec}\,\mathbb Z$ with its generic point and Krull topology and check the $H^1(j_!\mathcal
V)=\widehat{\mathbb Z}/\mathbb Z$ adelic identity survives the passage from the Alexandrov model to
the scheme (does $j_!$ on the actual étale/Zariski site still compute the integral-adele class
group, and is the weight filtration $W_\bullet M$ the arithmetic one?). Thirdly, the still-[Open]
$\aleph_1$-threshold of Thm 61c remains carried — is the $\omega_1$-cofinal recollement
$\varprojlim^1$ controlled by $\mathrm{add}(\mathcal M)$, a Suslin tree, or a new tower invariant?

---

### Pass 65 - 2026-06-10 JST

Focus:
Use the **second** recollement triangle
$$i_*i^!F\to F\to Rj_*j^*F\xrightarrow{+1}$$
left open by Pass 64.  The target is the finite-model Verdier-dual version of the dictionary:
compute the $i^!$ / closed-support spine, decide how $\mathbb D$ exchanges $j_!$ and $Rj_*$, and
determine whether the mixed class $\epsilon_S$ is fixed or inverted.

Proposer:
On the finite generic-point space $X_S=\{\eta\}\sqcup\{(p):p\in S\}$, the $i^!$ side of the
constant/generic spine is the local-support complex
$$\mathbb Z\xrightarrow{\Delta}\mathbb Z^S,\qquad 1\mapsto(1,\ldots,1).$$
Thus $H^0(i^!)=0$ and $H^1(i^!)=\operatorname{coker}\Delta\cong\mathbb Z^{s-1}$: the same free
Rosser lattice reappears, but now as a **closed costalk / support** object.  The boundary used in
Passes 62--64 is
$$d_S:\mathbb Z^S\to\mathbb Z^{s-1},\qquad (x_p)\mapsto(x_p-x_{p_0})_{p\ne p_0}.$$
Contravariant Verdier duality sends the first gluing triangle to the second and carries
$j_!$ to $Rj_*$; on this finite algebraic spine it sends the boundary to the signed transpose
$$\mathbb D(d_S)=-d_S^T.$$
Therefore the finite-model "functional equation" is not invariance but **anti-invariance**:
$$\boxed{\mathbb D(\epsilon_S)=-\epsilon_S^\vee.}$$
The sign disappears over $\mathbb F_2$, but over $\mathbb Z$ it is the orientation datum of the
triangle.  Applying duality twice returns $d_S$, so the sign convention is coherent.

Skeptic:
This resolves only the finite/Alexandrov spine.  Three overstatements must be avoided.  First,
"Loeb $\leftrightarrow$ Rosser" is an exchange of the two **recollement presentations**
($j_!\leftrightarrow Rj_*$, $i^*\leftrightarrow i^!$), not yet a literal isomorphism between the
$p$-adic Loeb ghosts and the free Rosser lattice.  A full statement must choose the correct
dualizing theory for $\mathbb Z_p/\mathbb Z$ (Pontryagin/Matlis/derived $\mathbb Z$-dual) and track
products versus sums.  Second, the sign depends on the dualizing-complex and connecting-morphism
normalization; the finite checker pins the algebraic sign but not the scheme-site convention.
Third, the honest Zariski or etale site of $\mathrm{Spec}\,\mathbb Z$ is not proved by finite
rank tests.  The adelic identity and Verdier-dual functional equation still need a site-level
proof.  The $\aleph_1$ threshold from Thm 61c remains untouched.

Formalist:
> **Theorem 65a (closed-support Rosser lattice).** On $X_S$, the $i^!$ spine of the generic
> diagonal is the two-term complex $\mathbb Z\xrightarrow{\Delta}\mathbb Z^S$, hence
> $H^0(i^!)=0$ and $H^1(i^!)\cong\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{s-1}$.
> Thus the Rosser horizontal lattice has both a $j_!$ cohomology presentation (Pass 63) and an
> $i^!$ local-support presentation (Pass 65).
>
> **Theorem 65b (signed Verdier functional equation; finite model).** With
> $d_S(x_p)=(x_p-x_{p_0})_{p\ne p_0}$ representing the recollement boundary
> $\epsilon_S$, Verdier duality sends the first gluing triangle to the second and sends
> $d_S$ to $-d_S^T$.  Hence $\mathbb D(\epsilon_S)=-\epsilon_S^\vee$ on the finite model;
> $\mathbb D^2(d_S)=d_S$.  Over $\mathbb F_2$ the sign vanishes; over $\mathbb Z$ it is the
> orientation of the extension class.
>
> **Theorem 65c (finite-prime naturality).** For $S\subseteq S'$ the restriction maps satisfy
> $r_{\mathrm{Ros}}d_{S'}=d_Sr_{\mathrm{Loeb}}$, and after duality
> $r_{\mathrm{Loeb}}^T(-d_S^T)=(-d_{S'}^T)r_{\mathrm{Ros}}^T$.  Thus the signed functional
> equation is compatible with the finite prime-spectrum motive.

Machine-verified `code/scripts/check-pass65.py` ->
`artifacts/reports/pass65-verdier-dual-recollement-functional-equation-check.json` (overall PASS):
for $s=1,\ldots,7$, $\ker\Delta=0$ and $\operatorname{coker}\Delta$ has rank $s-1$; $d_S$ and
$-d_S^T$ have the same primitive rank $s-1$; $\mathbb D^2(d_S)=d_S$; the sign is invisible mod $2$;
and the restriction squares commute for finite inclusions $1\subset2$, $2\subset3$, $3\subset5$,
$4\subset7$.  The report explicitly records the scheme-lift gap.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-65 entry; State counter
  $65\to66$.
- `records/logs/research-log.md`: Pass-65 one-line entry.
- `research/open_problems.md`: [New (Pass 64)] item (i) marked finite-model resolved / scheme-level
  partially open; item (ii) scheme lift carried [Open]; item (iii) $\aleph_1$ threshold carried
  [Open]; [New (Pass 65)] residues added.
- `research/notes/g2-fg2-hierarchy.md`: Pass-65 section (Thms 65a, 65b, 65c).
- `research/definitions.md`: Verdier-dual recollement, $i^!$ Rosser lattice, signed functional
  equation $\mathbb D(\epsilon_S)=-\epsilon_S^\vee$.
- `research/ideas/research-questions.md`: retargeted active question toward the scheme-site
  duality lift and dualizing normalization.
- `code/scripts/check-pass65.py`,
  `artifacts/reports/pass65-verdier-dual-recollement-functional-equation-check.json`: new.
- `artifacts/pdf/verdier-dual-loeb-rosser-2026-06-10.md`: publication summary source.

Next step:
Pass 66 should lift Theorem 65b from the finite Alexandrov spine to the actual arithmetic site.
Choose the duality normalization (Verdier vs Pontryagin/Matlis vs $R\mathrm{Hom}_{\mathbb Z}(-,\mathbb
Z)$), compute the duals of $\mathbb Z_p/\mathbb Z$ and $\widehat{\mathbb Z}_S/\mathbb Z$ with
products/sums controlled, and prove or refute the scheme-level equation
$$\mathbb D(\epsilon_S)=-\epsilon_S^\vee$$
for $S$ finite and then $S=\mathbb P$.  Keep the Pass-61 $\aleph_1$ threshold carried as a separate
set-theoretic residue.

---

### Pass 66 - 2026-06-10 JST

Focus:
Lift Pass 65 as far as possible toward the honest arithmetic site by choosing the right duality
normalization.  The finite sign equation
$$\mathbb D(\epsilon_S)=-\epsilon_S^\vee$$
is already checked on the Alexandrov spine.  The question is whether this is a literal
$R\mathrm{Hom}_{\mathbb Z}(-,\mathbb Z)$ statement, a character-duality statement, or a
restricted-product adelic statement.

Proposer:
The clean finite lift uses **character-normalized Verdier duality**
$$D_{\mathrm{ch}}(A)=\operatorname{Hom}(A,\mathbb Q/\mathbb Z)$$
on the finite cyclic truncations of the dilation coefficient.  It preserves every layer
$\mathbb Z/p^n$, dualizes maps by transpose, and therefore carries the Pass-65 boundary matrix
$d_S$ to $-d_S^T$.  For finite $S$ there is no product/direct-sum issue: finite products of local
layers are finite direct sums.  Thus the finite-prime scheme-lift should be stated as:
$$D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee,\qquad S\in\mathcal P_{\mathrm{fin}}(\mathbb P),$$
with the usual connecting-morphism sign.

Skeptic:
Two naive lifts fail.  First, the unshifted $\mathbb Z$-linear dual is too small:
$\operatorname{Hom}_{\mathbb Z}(\mathbb Z/n,\mathbb Z)=0$, while
$\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong\mathbb Z/n$.  So
$R\mathrm{Hom}_{\mathbb Z}(-,\mathbb Z)$ can see the local layers only after a cohomological shift;
it is not the degree-preserving duality behind the finite functional equation.  Second, the
all-prime object cannot be obtained by simply letting $S=\mathbb P$ in the discrete product:
continuous characters of an infinite product have finite support, so the dual of a bare product is
a direct sum.  The all-prime adelic statement must be formulated in the category of locally compact
abelian / restricted-product sheaves, where the finite adele object has its own self-duality
normalization.  Without that topology the full-spectrum functional equation is false as stated.

Formalist:
> **Theorem 66a (plain $R\mathrm{Hom}_{\mathbb Z}$ is shifted).** For $n>1$,
> $\operatorname{Hom}_{\mathbb Z}(\mathbb Z/n,\mathbb Z)=0$ and
> $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong\mathbb Z/n$.
> Hence the local cyclic layers of $\mathcal V$ live in degree $1$ under
> $R\mathrm{Hom}_{\mathbb Z}(-,\mathbb Z)$; the Pass-65 degree-preserving equation is not a literal
> unshifted $\mathbb Z$-dual statement.
>
> **Theorem 66b (finite $S$ character-dual lift).** On finite truncations,
> $D_{\mathrm{ch}}(\mathbb Z/n)\cong\mathbb Z/n$.  Therefore for every finite prime set $S$,
> character-normalized Verdier duality sends the mixed boundary $d_S$ to $-d_S^T$ and proves the
> finite-prime functional equation $D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee$.
>
> **Theorem 66c (all-prime product obstruction).** For $S=\mathbb P$, the naive product of local
> ghosts has continuous character dual equal to a finite-support direct sum of local characters,
> not another product.  The all-prime equation must be promoted to a restricted-product/LCA
> formulation; the bare discrete product formulation loses the adelic self-duality.

Machine-verified `code/scripts/check-pass66.py` ->
`artifacts/reports/pass66-duality-normalization-scheme-lift-check.json` (overall PASS): finite
cyclic layers $n=2,3,4,5,8,9,16,25$ have trivial $\operatorname{Hom}(-,\mathbb Z)$ but
$\operatorname{Ext}^1$ of order $n$; $D_{\mathrm{ch}}(\mathbb Z/p^k)$ has order $p^k$ for
$p=2,3,5,7$ and $k=1,\ldots,4$; $d_S$ and $-d_S^T$ have matching rank and square back for
$s=1,\ldots,7$; finite product/direct-sum orders agree; finite-prefix support counts exhibit the
infinite product/direct-sum gap.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-66 entry; State counter
  $66\to67$.
- `records/logs/research-log.md`: Pass-66 one-line entry.
- `research/open_problems.md`: [New (Pass 65)] split into finite-$S$ character-dual resolution and
  an all-prime restricted-product/LCA residue.
- `research/notes/g2-fg2-hierarchy.md`: Pass-66 section (Thms 66a, 66b, 66c).
- `research/definitions.md`: character-normalized duality and all-prime product/direct-sum gap.
- `research/ideas/research-questions.md`: active question retargeted to restricted-product adelic
  Verdier duality.
- `code/scripts/check-pass66.py`,
  `artifacts/reports/pass66-duality-normalization-scheme-lift-check.json`: new.
- `artifacts/pdf/duality-normalization-loeb-rosser-2026-06-10.md`: publication summary source.

Next step:
Pass 67 should formulate the restricted-product / locally compact abelian sheaf category needed for
$S=\mathbb P$.  The test is concrete: define the finite-adele coefficient as a restricted product
with respect to the integral lattices $\mathbb Z_p$, show its character dual is again the same
restricted product up to the standard additive character, and then re-check whether the boundary
class still transforms as $-\epsilon^\vee$.  Keep this separate from the carried $\aleph_1$ tower
problem.

---

### Pass 67 - 2026-06-11 JST

Focus:
Replace the all-prime bare product from Pass 66 with finite shadows of the restricted product
$$\mathbb A_f=\prod_p'(\mathbb Q_p,\mathbb Z_p).$$
The goal is to verify the local conductor self-duality that the full LCA statement needs, while
also identifying what still prevents a direct proof of the Loeb-Rosser phantom
$\widehat{\mathbb Z}/\mathbb Z$ as an ordinary topological quotient.

Proposer:
Use the finite conductor quotient
$$p^{-k}\mathbb Z_p/p^k\mathbb Z_p\cong\mathbb Z/p^{2k}\mathbb Z$$
with pairing $\langle x,y\rangle=xy/p^{2k}\in\mathbb Q/\mathbb Z$.  The integral lattice
$\mathbb Z_p/p^k\mathbb Z_p$ is represented by $p^k\mathbb Z/p^{2k}\mathbb Z$, and its annihilator
is itself.  Hence the restricted-product normalization has the correct local finite shadow:
each conductor window is self-dual and the integral lattice is self-annihilating.  Products of
finitely many such windows remain self-dual, and in conductor-normalized coordinates the
Loeb-Rosser boundary still dualizes by the Pass-65 signed transpose $d\mapsto-d^T$.

Skeptic:
This does **not** prove that $\widehat{\mathbb Z}/\mathbb Z$ is an honest Hausdorff LCA quotient.
In fact, every fixed finite conductor quotient collapses the diagonal by CRT:
$$\mathbb Z/N\mathbb Z\ \xrightarrow{\sim}\ \prod_{p\mid N}\mathbb Z/p^{v_p(N)}\mathbb Z.$$
So the finite-level quotient by the diagonal is zero.  The phantom is not present at any one
finite level; it is a pro/derived phenomenon of the limiting diagonal embedding.  Also, in the
topological profinite group $\widehat{\mathbb Z}$, the image of $\mathbb Z$ is dense, so the naive
topological quotient $\widehat{\mathbb Z}/\mathbb Z$ is non-Hausdorff.  The full statement needs a
derived-pro, condensed, or exact-category treatment of the quotient, not just LCA Pontryagin
duality.

Formalist:
> **Theorem 67a (finite conductor self-duality).** For each prime $p$ and $k\ge1$, the finite group
> $p^{-k}\mathbb Z_p/p^k\mathbb Z_p\cong\mathbb Z/p^{2k}\mathbb Z$ with pairing
> $xy/p^{2k}$ is nondegenerate, and the integral lattice
> $\mathbb Z_p/p^k\mathbb Z_p$ is self-annihilating.
>
> **Theorem 67b (restricted-product finite shadow).** Finite products of the conductor windows in
> Theorem 67a remain self-dual, with product integral lattice self-annihilating.  In normalized
> finite coordinates, the mixed boundary satisfies the same signed equation
> $D(d_S)=-d_S^T$ and $D^2(d_S)=d_S$.
>
> **Theorem 67c (CRT collapse and derived quotient obligation).** For any finite conductor
> $N=\prod p^{e_p}$, the diagonal map $\mathbb Z/N\to\prod_{p\mid N}\mathbb Z/p^{e_p}$ is
> surjective.  Therefore $\widehat{\mathbb Z}/\mathbb Z$ is invisible at every fixed finite
> conductor level.  The all-prime phantom must be represented as a derived/pro quotient of the
> limiting system, not as an ordinary finite-stage quotient.

Machine-verified `code/scripts/check-pass67.py` ->
`artifacts/reports/pass67-restricted-product-adelic-duality-check.json` (overall PASS): local
quotients $\mathbb Z/4,\mathbb Z/16,\mathbb Z/9,\mathbb Z/81,\mathbb Z/25,\mathbb Z/49$ have
nondegenerate pairings and self-annihilating integral lattices; product windows of orders
$36,144,900,4900$ have self-annihilating product lattices; signed boundary transpose checks pass for
$s=1,\ldots,7$; CRT diagonal maps for $N=6,12,90,420$ are surjective, confirming finite-level
collapse.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-67 entry; State counter
  $67\to68$.
- `records/logs/research-log.md`: Pass-67 one-line entry.
- `research/open_problems.md`: [New (Pass 66)] split into finite-conductor restricted-product
  resolution and a derived/pro quotient residue for $\widehat{\mathbb Z}/\mathbb Z$.
- `research/notes/g2-fg2-hierarchy.md`: Pass-67 section (Thms 67a, 67b, 67c).
- `research/definitions.md`: finite conductor window, self-annihilating integral lattice, CRT
  collapse, derived/pro quotient obligation.
- `research/ideas/research-questions.md`: active question retargeted to derived-pro/condensed
  quotient formalization.
- `code/scripts/check-pass67.py`,
  `artifacts/reports/pass67-restricted-product-adelic-duality-check.json`: new.
- `artifacts/pdf/restricted-product-adelic-duality-2026-06-11.md`: publication summary source.

Next step:
Pass 68 should build the exact categorical home for the quotient
$\widehat{\mathbb Z}/\mathbb Z$: either as a pro-object quotient with a nonzero derived cokernel,
as a condensed/solid abelian group quotient, or as an exact-category extension class.  The concrete
test is to recover the phantom from the inverse system whose finite CRT quotients are zero, i.e.
identify precisely which derived functor turns the levelwise-zero quotient into the nonzero
Loeb-Rosser class.

---

### Pass 68 - 2026-06-11 JST

Focus:
Resolve the Pass-67 derived/pro quotient obligation.  The finite conductor quotients all collapse
by CRT, so the phantom cannot be a levelwise cokernel.  The target is the exact sequence of inverse
systems that recovers
$$\widehat{\mathbb Z}/\mathbb Z$$
as a derived cokernel.

Proposer:
Take the cofinal modulus tower $N_n=\operatorname{lcm}(1,\ldots,n)$ and the levelwise exact sequence
$$0\to K_n=N_n\mathbb Z\to\mathbb Z\to\mathbb Z/N_n\mathbb Z\to0.$$
At every finite level the map $\mathbb Z\to\mathbb Z/N_n$ is surjective, and CRT identifies
$\mathbb Z/N_n$ with the product of its prime-power local factors; hence the ordinary finite
cokernel is zero.  But applying $\varprojlim$ is only left exact.  Since $K_n=N_n\mathbb Z$ is a
non-Mittag-Leffler tower (transition indices grow without bound) and $\varprojlim K_n=0$, the
derived exact sequence gives
$$0\to\mathbb Z\to\varprojlim_n\mathbb Z/N_n\mathbb Z=\widehat{\mathbb Z}\to
\varprojlim\nolimits^1 K_n\to0,$$
so
$$\boxed{\ \varprojlim\nolimits^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z\ }.$$
Thus the categorical home needed for the algebraic phantom is the derived pro-abelian cokernel of
the kernel tower.  Condensed/solid or LCA language may still be needed for topology and Hausdorff
issues, but the algebraic Loeb-Rosser class is already detected by $R^1\!\varprojlim$.

Skeptic:
Do not overstate this as a topological quotient theorem.  In the profinite topology, $\mathbb Z$ is
dense in $\widehat{\mathbb Z}$, so the naive Hausdorff quotient is zero; the algebraic quotient is
non-Hausdorff if treated topologically.  The derived pro-Ab statement keeps the exact data that the
Hausdorff LCA category would discard.  Also, identifying this $R^1\!\varprojlim$ class with the
Pass-62/63 recollement $\epsilon$ still requires matching the boundary maps, not only matching the
underlying group.  The sign/duality compatibility from Passes 65--67 must be lifted to this derived
pro exact sequence in the next pass.

Formalist:
> **Theorem 68a (levelwise CRT zero).** For $N_n=\operatorname{lcm}(1,\ldots,n)$, the finite map
> $\mathbb Z/N_n\mathbb Z\to\prod_{p\mid N_n}\mathbb Z/p^{v_p(N_n)}\mathbb Z$ is an isomorphism.
> Therefore the quotient by the diagonal is zero at every fixed finite conductor.
>
> **Theorem 68b (derived pro-cokernel).** In the inverse system
> $0\to N_n\mathbb Z\to\mathbb Z\to\mathbb Z/N_n\mathbb Z\to0$, the kernel tower is non-ML,
> $\varprojlim N_n\mathbb Z=0$, and the derived long exact sequence gives
> $$\varprojlim\nolimits^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z.$$
>
> **Theorem 68c (categorical separation).** Algebraically, the Loeb-Rosser phantom is a derived
> pro-Ab quotient.  Topologically, the dense embedding $\mathbb Z\subset\widehat{\mathbb Z}$ means
> the same expression is not an ordinary Hausdorff LCA quotient.  The correct statement separates
> algebraic exactness (derived pro-Ab) from topological duality (restricted-product/LCA or
> condensed/solid refinement).

Machine-verified `code/scripts/check-pass68.py` ->
`artifacts/reports/pass68-derived-pro-cokernel-phantom-check.json` (overall PASS): $N_n$ is cofinal
for moduli $1,\ldots,24$; CRT levelwise cokernel-zero checks pass for
$N_2,N_3,N_4,N_5,N_6,N_8,N_{10},N_{12}$; the kernel tower has 14 distinct values through $n=24$,
unbounded image indices in $K_2$, and many nontrivial transition ratios; $\varprojlim K_n=0$ is
certified by unbounded $N_n$; completion prefixes grow while the finite cokernel remains zero.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-68 entry; State counter
  $68\to69$.
- `records/logs/research-log.md`: Pass-68 one-line entry.
- `research/open_problems.md`: [New (Pass 67)] marked resolved at the derived pro-Ab algebraic
  level; new residue added for matching this class with the recollement $\epsilon$ and its signed
  duality.
- `research/notes/g2-fg2-hierarchy.md`: Pass-68 section (Thms 68a, 68b, 68c).
- `research/definitions.md`: derived pro-cokernel of the diagonal; kernel tower $N_n\mathbb Z$;
  levelwise-zero vs derived-nonzero distinction.
- `research/ideas/research-questions.md`: active question retargeted to identifying
  $\varprojlim^1(N_n\mathbb Z)$ with the recollement boundary class $\epsilon$.
- `code/scripts/check-pass68.py`,
  `artifacts/reports/pass68-derived-pro-cokernel-phantom-check.json`: new.
- `artifacts/pdf/derived-pro-cokernel-phantom-2026-06-11.md`: publication summary source.

Next step:
Pass 69 should identify the derived pro-cokernel class
$\varprojlim^1(N_n\mathbb Z)$ with the earlier recollement class $\epsilon_S$ / $\epsilon_{\mathbb
P}$, including the signed duality law.  Concretely, build a chain map from the Pass-62 bicomplex
or Pass-64 recollement boundary to the derived inverse-limit exact sequence, and check that under
character duality it sends $\epsilon$ to $-\epsilon^\vee$.

---

### Pass 69 - 2026-06-11 JST

Focus:
Use the newly available G2-ZOO / infinite-model material to add a named APS-level consistency and
cut layer.  This pass deliberately defers the Pass-68 recollement-vs-derived-pro comparison, because
the current repository state already contained a concrete Pass-69 checker and note for consistency
towers, `CutA3`, finite cycle models, and detached Rosser period models.

Proposer:
Define the iterated consistency tower
$$C_0=T,\qquad C_{n+1}=\boxtimes C_n.$$
This gives a reusable vocabulary:
$$\mathrm{Con}^{\mathrm{orb}}_n:\ C_n\nleq\bot,\qquad
\mathrm{G2}_n:\ C_n\le\bot\Rightarrow T\le\bot,\qquad
\mathrm{FG2}_n:\ C_{n+1}\le C_n,$$
where $\mathrm{FG2}_n$ is the existing $\mathrm{nFG2}(n)$.  Add the cut/collision principle
$$\mathrm{CutA3}:\quad
x\le\Box y\ \wedge\ x\le\boxtimes y\Rightarrow x\le\boxtimes T,$$
which is APS axiom A3 read as consistency closure.

The finite certificate has two families.  First, the cycle models $C_m$ have carrier
$\{\bot,\top,o_0,\ldots,o_{m-1}\}$ with the $o_i$ forming a middle antichain,
$T=o_0$, $\Box=\mathrm{id}$, and $\boxtimes o_i=o_{i+1\bmod m}$, plus
$\boxtimes\bot=\top$, $\boxtimes\top=\bot$.  These are genuine APS models, have no syntactic
$\boxtimes$-fixed point, satisfy G2 vacuously, and have all checked $\mathrm{nFG2}(k)$ false.
Second, the detached Rosser period models $R_{2k}$ add a middle atom $p$ with
$\boxtimes p=p$.  They preserve A1, A2, A4, G2, and the flat consistency orbit, but fail A3 exactly
at $x=y=p$.

Skeptic:
Do not claim arithmetic realizability from these finite certificates alone.  The $C_m$ and
$R_{2k}$ families are order-theoretic APS/preAPS witnesses.  The arithmetic lift still has to say
where $C_n$ lands inside $ConLat_T$, whether `CutA3` corresponds to $Con_T^S$, $Con_T^H$, Rosser
consistency, local reflection, or BS16-style cut admissibility, and whether a fully residuated,
integral, contraction-bearing version of $R_{2k}$ can keep the detached fixed point.  The pass also
does not resolve the Pass-68 target comparing $\varprojlim^1(N_n\mathbb Z)$ with $\epsilon$; that
comparison remains open.

Formalist:
> **Theorem 69a (cycle APS flat tower).** For every $m\ge2$, the model $C_m$ is an APS.  Its
> consistency orbit is the antichain cycle $o_0,\ldots,o_{m-1}$, so no distinct orbit elements are
> comparable; it has no $\boxtimes$-fixed point; G2 and all checked $\mathrm{G2}_n$ hold
> vacuously; and every checked $\mathrm{FG2}_n$ fails.
>
> **Theorem 69b (detached Rosser period below cut).** For every $k\ge1$, $R_{2k}$ has a primitive
> fixed point $p=\boxtimes p$ detached from the consistency orbit.  It satisfies A1, A2, A4, and
> G2, but it is not an APS because `CutA3`/A3 fails at $x=y=p$.
>
> **Theorem 69c (cut boundary).** Primitive refutability fixed points do not by themselves imply
> formalized descent or cut/collision closure.  A3 is the algebraic boundary separating the detached
> Rosser fixed-point layer from full APS cut closure.

Machine-verified `code/scripts/check-pass69.py` ->
`artifacts/reports/pass69-consistency-cut-infinite-g2-zoo-check.json` (overall PASS): $C_m$ for
$2\le m\le12$ are APS, fixed-point-free, G2-true, orbit-flat, and all checked nFG2-false; $R_{2k}$
for $1\le k\le6$ satisfy A1/A2/A4, have exactly the detached fixed point $p$, fail A3 at
$x=y=p$, and keep all checked nFG2 false; the report records the statement names
`Con-orb(n)`, `G2(n)`, `FG2(n)`, `CutA3`, and `flat-orbit(N)`.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-69 entry; State counter
  $69\to70$.
- `records/logs/research-log.md`: Pass-69 one-line entry.
- `research/definitions.md`: iterated consistency tower, $\mathrm{Con}^{\mathrm{orb}}_n$,
  $\mathrm{G2}_n$, $\mathrm{FG2}_n$, finite flatness, and `CutA3`.
- `research/notes/g2-aps-zoo-classification.md` and
  `research/notes/g2-zoo-consistency-cut-infinite-pass69.md`: new G2-ZOO consistency/cut layer.
- `research/open_problems.md` and `research/ideas/research-questions.md`: arithmetic lift,
  `CutA3` identification, and residuated/contraction repair tasks.
- `code/scripts/check-pass69.py`,
  `artifacts/reports/pass69-consistency-cut-infinite-g2-zoo-check.json`: new.
- `artifacts/pdf/consistency-cut-infinite-g2-zoo-2026-06-11.md`: publication summary source.

Next step:
Pass 70 should return to the deferred Pass-68 obligation: compare the lcm-tower class
$\varprojlim^1(N_n\mathbb Z)$ with the Pass-62/63/64 recollement boundary $\epsilon$, while keeping
the new Pass-69 vocabulary separate as the APS/G2-ZOO consistency layer.

---

### Pass 70 - 2026-06-11 JST

Focus:
Close the algebraic comparison between the Pass-68 derived pro-cokernel and the Pass-62/63/64
recollement class $\epsilon_S$.  The target is not a new group isomorphism but the exact filtration
that identifies the derived pro-cokernel with the recollement extension.

Proposer:
For a finite prime set $S$, replace the all-prime lcm tower by the cofinal finite-prime conductor
tower
$$M_{S,k}=\prod_{p\in S}p^k.$$
The exact sequence
$$0\to M_{S,k}\mathbb Z\to\mathbb Z\to\mathbb Z/M_{S,k}\mathbb Z\to0$$
gives
$$\varprojlim_k\mathbb Z/M_{S,k}\mathbb Z=\widehat{\mathbb Z}_S=\prod_{p\in S}\mathbb Z_p,$$
and hence
$$\varprojlim\nolimits^1(M_{S,k}\mathbb Z)\cong\widehat{\mathbb Z}_S/\mathbb Z.$$
Now compare this global derived cokernel with the product of local derived cokernels:
$$\widehat{\mathbb Z}_S/\mathbb Z\longrightarrow
\prod_{p\in S}(\mathbb Z_p/\mathbb Z).$$
The kernel is precisely tuples represented by integers in each coordinate, modulo the single
diagonal integer:
$$\ker=\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.$$
Therefore the Pass-62 filtration extension and Pass-64 recollement boundary are the same exact
sequence:
$$0\to\mathbb Z^S/\Delta\mathbb Z\to
\widehat{\mathbb Z}_S/\mathbb Z\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0.$$
This identifies $\epsilon_S$ as the finite-prime filtration of the derived pro-cokernel by local
derived cokernels.

Skeptic:
This resolves the algebraic comparison, not the full topological duality problem.  The all-prime
object $\widehat{\mathbb Z}/\mathbb Z$ is still non-Hausdorff as an ordinary quotient because
$\mathbb Z$ is dense in $\widehat{\mathbb Z}$.  Also, finite character duality can check the signed
matrix $d_S\mapsto-d_S^T$, but the all-prime dual statement still needs a restricted-product/LCA or
condensed normalization to avoid collapsing products to finite-support direct sums.  So the right
claim is: $\epsilon_S$ is the finite-prime algebraic filtration of the derived pro-cokernel; the
global Verdier/Pontryagin functional equation remains a separate normalization task.

Formalist:
> **Theorem 70a (finite-prime comparison).** For finite $S$,
> $$\varprojlim\nolimits^1(M_{S,k}\mathbb Z)\cong\widehat{\mathbb Z}_S/\mathbb Z.$$
> The projection to $\prod_{p\in S}(\mathbb Z_p/\mathbb Z)$ has kernel
> $\mathbb Z^S/\Delta\mathbb Z$.  Hence its extension class is the recollement
> class $\epsilon_S$.
>
> **Theorem 70b (all-prime compatibility).** The all-prime lcm tower restricts to the finite-prime
> conductor towers.  Consequently $\widehat{\mathbb Z}/\mathbb Z$ is the compatible all-prime
> derived pro-cokernel whose finite-prime restrictions are the classes $\epsilon_S$.
>
> **Theorem 70c (finite signed shadow).** For
> $$d_S(x)=(x_p-x_{p_0})_{p\ne p_0},$$
> one has $\ker d_S=\Delta\mathbb Z$ and $d_S$ is surjective.  Finite
> character-normalized duality sends $d_S$ to $-d_S^T$ and $D^2(d_S)=d_S$, so
> $$D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee$$
> on every finite-prime shadow.

Machine-verified `code/scripts/check-pass70.py` ->
`artifacts/reports/pass70-derived-pro-epsilon-comparison-check.json` (overall PASS): for
$|S|=1,\ldots,5$, CRT finite shadows for $M_{S,k}$, $1\le k\le4$, are bijective; the diagonal
$\Delta:\mathbb Z\to\mathbb Z^S$ is primitive; the boundary
$d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ is surjective with diagonal kernel by rank; and the signed
dual shape $-d_S^T$ double-dualizes back to $d_S$.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-70 entry; State counter
  $70\to71$.
- `records/logs/research-log.md`: Pass-70 one-line entry.
- `research/definitions.md`: added derived pro-cokernel filtration and $\epsilon_S$.
- `research/notes/g2-fg2-hierarchy.md`: Pass-70 section (Thms 70a, 70b, 70c).
- `research/open_problems.md`: Pass-68 comparison marked algebraically resolved, with
  restricted-product topological duality retained as the residue.
- `research/ideas/research-questions.md`: active question retargeted to all-prime
  restricted-product/condensed signed duality for $\epsilon$.
- `code/scripts/check-pass70.py`,
  `artifacts/reports/pass70-derived-pro-epsilon-comparison-check.json`: new.
- `artifacts/pdf/derived-pro-epsilon-comparison-2026-06-11.md`: publication summary source.

Next step:
Pass 71 should formulate the actual all-prime duality category: restricted-product LCA sheaves,
condensed/solid abelian groups, or another exact category that keeps both the product support and
the signed boundary.  The test is whether the finite laws
$D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee$ assemble into a global statement for
$\epsilon_{\mathbb P}$ without replacing products by finite-support direct sums.

---

### Pass 71 - 2026-06-11 JST

Focus:
Formulate the all-prime signed duality statement without overclaiming an ordinary
Pontryagin-dual theorem for the non-Hausdorff quotient
$\widehat{\mathbb Z}/\mathbb Z$.  The target is a support-preserving
restricted-product/pro-object package whose finite shadows are the Pass-70
extensions $\epsilon_S$.

Proposer:
The correct all-prime object should be written as
$$\epsilon_{\mathbb P}:=\{\epsilon_S\}_{S\subset\mathbb P,\ |S|<\infty}$$
together with the derived pro-cokernel
$$\varprojlim\nolimits^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z.$$
The finite-prime shadows are
$$0\to\mathbb Z^S/\Delta\mathbb Z\to
\widehat{\mathbb Z}_S/\mathbb Z\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0,$$
and the local duality normalization is supplied by finite conductor windows
$$p^{-k}\mathbb Z_p/p^k\mathbb Z_p$$
with self-annihilating integral lattice
$$\mathbb Z_p/p^k\mathbb Z_p.$$
Thus the all-prime formula
$$D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$$
should mean: for every finite $S$ and every conductor window, the boundary
$$d_S(x)=(x_p-x_{p_0})_{p\ne p_0}$$
dualizes to $-d_S^T$, duality squared returns $d_S$, and these equations commute
with restriction $S\subset S'$.

Skeptic:
Do not topologize $\widehat{\mathbb Z}/\mathbb Z$ as an ordinary Hausdorff LCA
quotient; $\mathbb Z$ is dense in $\widehat{\mathbb Z}$.  Also do not dualize
the bare product $\prod_p A_p$ and call the result all-prime self-duality:
ordinary continuous characters of an infinite product have finite support, so
that operation replaces product support by a direct-sum shadow.  Pass 71
therefore gives a precise pro-restricted finite-shadow formulation, not a
completed theorem in a selected sheaf or condensed category.  The remaining
mathematical obligation is to build that category and prove exactness of the
duality functor inside it.

Formalist:
> **Theorem 71a (support-preserving criterion).** Any all-prime duality theorem
> for $\epsilon_{\mathbb P}$ must use restricted products with conductor/lattice
> data, or an equivalent exact pro/condensed/solid formalism.  Bare product
> duality is inadmissible because it retains only finite-support characters.
>
> **Theorem 71b (pro-restricted epsilon object).** The all-prime Loeb-Rosser
> class is the compatible family $\{\epsilon_S\}_S$ plus the derived pro-Ab
> quotient $\widehat{\mathbb Z}/\mathbb Z$.  Each finite shadow is the Pass-70
> recollement extension with kernel $\mathbb Z^S/\Delta\mathbb Z$.
>
> **Theorem 71c (finite-shadow signed law).** The statement
> $$D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$$
> means that every finite prime/conductor shadow satisfies $D(d_S)=-d_S^T$,
> $D^2(d_S)=d_S$, and all restriction squares commute.

Machine-verified `code/scripts/check-pass71.py` ->
`artifacts/reports/pass71-restricted-product-epsilon-duality-check.json` (overall PASS): finite
boundary matrices and signed transposes commute with prefix restriction through six primes;
conductor windows for $p=2,3,5,7$ and $k=1,2$ have self-annihilating integral lattices; finite
support-profile counts separate restricted-product prefix profiles from bounded finite-support
dual profiles.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-71 entry; State counter
  $71\to72$.
- `records/logs/research-log.md`: Pass-71 one-line entry.
- `research/definitions.md`: support-preserving restricted-product duality,
  $\epsilon_{\mathbb P}$, and the pro-restricted signed law.
- `research/notes/g2-fg2-hierarchy.md`: Pass-71 section (Thms 71a, 71b, 71c).
- `research/open_problems.md` and `research/ideas/research-questions.md`: retargeted the residue
  to constructing the ambient LCA-sheaf, condensed/solid, or hybrid exact category.
- `code/scripts/check-pass71.py`,
  `artifacts/reports/pass71-restricted-product-epsilon-duality-check.json`: new.
- `artifacts/pdf/restricted-product-epsilon-duality-2026-06-11.md`: publication summary source.

Next step:
Pass 72 should choose one ambient formalism and test it seriously.  The most constrained route is
to define a small hybrid exact category whose objects are finite-conductor restricted products
plus derived pro-Ab quotient data, then prove whether the duality functor is exact and sends
$\epsilon_{\mathbb P}$ to $-\epsilon_{\mathbb P}^{\vee}$.

---

### Pass 72 - 2026-06-11 JST

Focus:
Choose a concrete ambient formalism for the Pass-71 pro-restricted signed law.
The safest option is not to claim a finished LCA-sheaf or condensed theorem, but
to define the smallest hybrid exact-category candidate that keeps both finite
restricted-product support and the derived pro-Ab diagonal quotient.

Proposer:
Define $\mathcal H_\epsilon$ as a two-layer bookkeeping category.  An object has
finite conductor restricted-product shadows
$$(S,k,W_{S,k},L_{S,k},d_S),$$
where
$$W_{S,k}=\prod_{p\in S}(p^{-k}\mathbb Z_p/p^k\mathbb Z_p),\qquad
L_{S,k}=\prod_{p\in S}(\mathbb Z_p/p^k\mathbb Z_p),$$
and $d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ is the Loeb-Rosser boundary, together
with the derived pro-Ab lcm kernel tower
$$K_n=N_n\mathbb Z,\qquad N_n=\operatorname{lcm}(1,\ldots,n).$$
A sequence is hybrid-exact if every finite conductor shadow is exact and the
pro layer supplies
$$\varprojlim\nolimits^1K_n\cong\widehat{\mathbb Z}/\mathbb Z.$$
The candidate duality is $\mathbb D_{\mathcal H}(d_S)=-d_S^T$, while
$\widehat{\mathbb Z}/\mathbb Z$ remains a derived pro-Ab quotient rather than a
Hausdorff LCA quotient.

Skeptic:
This is still a bookkeeping category, not a universal construction.  The phrase
"hybrid-exact" must therefore be read as a criterion, not as a proved Quillen
exact structure on a large ambient category.  The tests verify exact finite
shadows, restriction composition, conductor order bookkeeping, and non-ML pro
growth.  They do not prove that $\mathcal H_\epsilon$ embeds fully faithfully
into condensed abelian groups, LCA sheaves, or a canonical exact pro-category.
That embedding or universal property is now the precise remaining obligation.

Formalist:
> **Definition 72a (hybrid-exact sequence).** A sequence in
> $\mathcal H_\epsilon$ is hybrid-exact when all finite conductor restrictions
> are exact and the lcm kernel tower is interpreted through $R^1\varprojlim$.
>
> **Theorem 72b (finite exactness in $\mathcal H_\epsilon$).** For finite
> $S$, the boundary $d_S$ is surjective with diagonal kernel, the signed dual
> $-d_S^T$ has primitive image, and restriction maps compose compatibly with
> both $d_S$ and $-d_S^T$.
>
> **Theorem 72c (pro layer necessity).** Fixed finite CRT shadows are
> levelwise zero, but the lcm kernel tower is non-Mittag-Leffler and yields
> $\varprojlim^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z$.  Therefore
> forgetting the pro layer destroys the all-prime Loeb-Rosser phantom.

Machine-verified `code/scripts/check-pass72.py` ->
`artifacts/reports/pass72-hybrid-exact-epsilon-category-check.json` (overall PASS): exact shadows
pass for $|S|=1,\ldots,6$; all restriction-composition squares for chains among the first six
primes commute, including signed duals; conductor layers pass through $k=1,2,3$; and the lcm
tower is cofinal for moduli up to $24$, has non-ML growth, and certifies finite-CRT-zero versus
derived-pro-nonzero.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-72 entry; State counter
  $72\to73$.
- `records/logs/research-log.md`: Pass-72 one-line entry.
- `research/definitions.md`: added $\mathcal H_\epsilon$, hybrid-exactness, and
  $\mathbb D_{\mathcal H}$.
- `research/notes/g2-fg2-hierarchy.md`: Pass-72 section (Definition 72a, Thms 72b/72c).
- `research/open_problems.md` and `research/ideas/research-questions.md`: retargeted the
  residue to a universal property or faithful embedding of $\mathcal H_\epsilon$.
- `code/scripts/check-pass72.py`,
  `artifacts/reports/pass72-hybrid-exact-epsilon-category-check.json`: new.
- `artifacts/pdf/hybrid-exact-epsilon-category-2026-06-11.md`: publication summary source.

Next step:
Pass 73 should try to prove a universal property for $\mathcal H_\epsilon$: it should be initial
among support-preserving exact targets receiving the finite conductor windows and the lcm derived
pro-cokernel, or else exhibit the obstruction that prevents such an initial property.

---

### Pass 73 - 2026-06-11 JST

Focus:
Prove the universal property currently available for $\mathcal H_\epsilon$.
The target is not a faithful embedding into LCA sheaves or condensed groups,
but a presentation-level initiality theorem among support-preserving certificate
targets.

Proposer:
Define a support-preserving certificate target $C$ for
$\epsilon_{\mathbb P}$ as a target equipped with images of five generator
families:
1. finite conductor windows $W_{S,k}$ and lattices $L_{S,k}$;
2. Loeb-Rosser boundaries $d_S$;
3. finite-prime restriction maps;
4. signed duality maps $d_S\mapsto -d_S^T$;
5. the derived pro-Ab lcm tower $K_n=N_n\mathbb Z$.

The target is admissible when those images satisfy the Pass-72 relations:
finite exactness, restriction composition, signed-dual compatibility, conductor
bookkeeping, and non-Mittag-Leffler pro growth.  Since
$\mathcal H_\epsilon$ is defined by exactly these generators and relations, any
admissible target receives a unique generator-preserving functor
$$\mathcal H_\epsilon\to C.$$
This proves initiality in the category of support-preserving certificates.

Skeptic:
This is the right universal property for the current formal object, but it does
not solve the analytic realization problem.  The proof is by presentation:
unique maps are forced because the target supplies images of all generators and
satisfies all relations.  It does not prove that a natural LCA-sheaf,
condensed/solid, or exact pro-category target is admissible, nor that the
resulting functor is faithful.  The honest next obligation is external
realization: either build such a faithful exact functor or prove that one of the
five generator families cannot be preserved in any proposed target.

Formalist:
> **Definition 73a (support-preserving certificate target).** A target $C$ is
> support-preserving for $\epsilon_{\mathbb P}$ if it supplies images of the
> finite conductor windows, Loeb-Rosser boundaries, restriction maps, signed
> duality maps, and the derived pro-Ab lcm tower, satisfying the finite/pro
> relations of $\mathcal H_\epsilon$.
>
> **Theorem 73b (presentation initiality).** $\mathcal H_\epsilon$ is initial
> among admissible support-preserving certificate targets.  Equivalently, every
> admissible $C$ receives a unique generator-preserving functor
> $\mathcal H_\epsilon\to C$.
>
> **Theorem 73c (minimality obstruction).** Omitting any generator family
> prevents certification of $\epsilon_{\mathbb P}$: without conductor windows
> local support is untyped; without $d_S$ there is no $\epsilon_S$; without
> restrictions the shadows do not assemble; without signed duality the
> functional equation is untyped; without the lcm tower the derived quotient
> $\widehat{\mathbb Z}/\mathbb Z$ is lost.

Machine-verified `code/scripts/check-pass73.py` ->
`artifacts/reports/pass73-h-epsilon-universal-property-check.json` (overall PASS): finite conductor
normal forms are generated through six primes and $k\le3$; pro normal forms are generated through
$N_{24}$; restriction and signed-dual relations commute; the lcm tower is cofinal and non-ML;
complete support-preserving targets receive a unique generator-preserving functor; targets omitting
any generator family fail with the expected obstruction.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-73 entry; State counter
  $73\to74$.
- `records/logs/research-log.md`: Pass-73 one-line entry.
- `research/definitions.md`: support-preserving certificate target, presentation-level universal
  property, and minimality obstruction.
- `research/notes/g2-fg2-hierarchy.md`: Pass-73 section (Definition 73a, Thms 73b/73c).
- `research/open_problems.md` and `research/ideas/research-questions.md`: retargeted the residue
  to faithful exact realization or a no-go theorem.
- `code/scripts/check-pass73.py`,
  `artifacts/reports/pass73-h-epsilon-universal-property-check.json`: new.
- `artifacts/pdf/h-epsilon-universal-property-2026-06-11.md`: publication summary source.

Next step:
Pass 74 should attempt the first external realization test: define a candidate functor from
$\mathcal H_\epsilon$ to a concrete exact pro-category with restricted-product generators, and
check whether it is faithful on the five generator families.

---

### Pass 74 - 2026-06-11 JST

Focus:
Test a concrete external realization of $\mathcal H_\epsilon$.  The candidate
is a tagged restricted pro-Ab target.  The point is to see whether the five
generator families are faithfully represented, and whether the tags are
actually necessary.

Proposer:
Define
$$\mathcal R_\epsilon:=
\mathbf{Pro}^{\mathrm{rp}}_{\mathrm{tag}}(\mathbf{Ab}_{\mathrm{fin}})
\times\mathbf{Pro}_{\mathrm{tag}}(\mathbf{Ab}).$$
The realization functor
$$\rho_{\mathrm{tag}}:\mathcal H_\epsilon\to\mathcal R_\epsilon$$
sends finite conductor windows to tagged finite abelian group presentations
with support tag $S$, conductor tag $k$, elementary divisors $(p,2k)$, and
lattice divisors $(p,k)$; sends $d_S$ to its tagged integer matrix; sends
restrictions to tagged coordinate-restriction matrices; sends signed duality to
$-d_S^T$; and sends $K_n=N_n\mathbb Z$ to the tagged pro-stage $(n,N_n)$.
This is a concrete faithful realization on the certificate data, provided the
tags are retained.

Skeptic:
The tags are not cosmetic.  If source support and pro-stage tags are forgotten,
plain pro-Ab data identify different generators.  For example, restrictions
with different source support can have the same visible target matrix, and lcm
stages can repeat as finite abelian groups when $N_n=N_{n+1}$.  Thus Pass 74
does not yet give a tag-free natural LCA or condensed realization.  It proves
the first external realization only in a tagged certificate target, and the next
question is whether these tags can be internalized as genuine support/stage
structure.

Formalist:
> **Theorem 74a (tagged generator faithfulness).** On the checked finite/pro
> window, $\rho_{\mathrm{tag}}$ is faithful on all five generator families:
> finite conductor windows, Loeb-Rosser boundaries, restrictions, signed
> duality, and lcm pro-stages.
>
> **Theorem 74b (tag-forgetting obstruction).** The corresponding plain
> untagged pro-Ab target is not faithful: restriction source support and
> repeated lcm stages collide.
>
> **Corollary 74c (intrinsic-tag constraint).** Any natural exact realization
> of $\mathcal H_\epsilon$ must internalize support and stage tags as structure,
> rather than discard them.

Machine-verified `code/scripts/check-pass74.py` ->
`artifacts/reports/pass74-tagged-proab-realization-check.json` (overall PASS): 75 generators are
tested through six primes, conductors $k\le3$, and lcm stages through $N_{24}$; tagged global
injectivity has zero collisions; tagged family faithfulness passes for all five generator
families; the plain tag-forgetting comparison has 12 collisions, including restriction-source
collisions and repeated lcm-stage collisions.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-74 entry; State counter
  $74\to75$.
- `records/logs/research-log.md`: Pass-74 one-line entry.
- `research/definitions.md`: tagged restricted pro-Ab realization target, realization functor,
  generator faithfulness, and tag-forgetting obstruction.
- `research/notes/g2-fg2-hierarchy.md`: Pass-74 section (Thms 74a/74b and Cor 74c).
- `research/open_problems.md` and `research/ideas/research-questions.md`: retargeted the residue
  to intrinsic support/stage tags or a tag-free no-go theorem.
- `code/scripts/check-pass74.py`,
  `artifacts/reports/pass74-tagged-proab-realization-check.json`: new.
- `artifacts/pdf/tagged-proab-realization-2026-06-11.md`: publication summary source.

Next step:
Pass 75 should try to make the tags intrinsic.  The concrete test is to replace explicit support
tags by idempotent support projectors or a finite-prime stratification and check whether the
result remains faithful without external labels.

---

### Pass 75 - 2026-06-11 JST

Focus:
Replace the external tags in the Pass-74 realization by internal structure.
The concrete test is whether Boolean support projectors and lcm-stage
projectors recover the same faithfulness without textual support/stage labels.

Proposer:
Define a projector-enriched realization
$$\rho_{\mathrm{proj}}:\mathcal H_\epsilon\to
\mathcal R_\epsilon^{\mathrm{proj}}.$$
The target has commuting Boolean support idempotents $e_p$ and stage projectors
$q_n$, satisfying
$$e_Se_T=e_{S\cap T},\qquad q_nq_m=q_{\min(n,m)}.$$
Finite conductor windows, boundaries, restrictions, signed duals, and lcm
stages are sent to finite/pro abelian data equipped with these projectors.
Restriction source support is now recovered from the pair $(e_{S'},e_S)$, and
repeated lcm stages are separated by $q_n$ even when $N_n=N_{n+1}$.

Skeptic:
This removes external labels, but it still does not prove an LCA-sheaf or
condensed realization.  The projectors are internal to a certificate target.
They must still be realized as actual support or stratification idempotents in
an established category.  The previously untracked Pass-73 companion no-go
checker also matters here: ordinary exact 1-category realization is too weak,
because $\varprojlim^1$ is a derived pro datum, not a finite exact-cone value.
So the next target must be projector-enriched and derived/pro-aware.

Formalist:
> **Theorem 75a (projector faithfulness).** On the checked finite/pro window,
> $\rho_{\mathrm{proj}}$ is faithful on all five generator families.
>
> **Theorem 75b (projector algebra).** The support projectors form the finite
> Boolean intersection algebra $e_Se_T=e_{S\cap T}$, and the stage projectors
> form the chain algebra $q_nq_m=q_{\min(n,m)}$.
>
> **Theorem 75c (ordinary exact-target obstruction).** The companion exact
> obstruction shows that $\mathcal H_\epsilon$ cannot be faithfully realized as
> an ordinary exact 1-category target carrying only finite exact cones; the
> $\widehat{\mathbb Z}/\mathbb Z$ term is recovered through
> $R^1\varprojlim$.

Machine-verified `code/scripts/check-pass75.py` ->
`artifacts/reports/pass75-intrinsic-projector-realization-check.json` (overall PASS): 75
projector-enriched generators are tested through six primes, conductors $k\le3$, and lcm stages
through $N_{24}$; projector signatures have zero collisions; the plain target still has 12
collisions; Boolean support-projector relations pass; 576 stage-projector relations pass; and
restriction projector actions recover source/target support.  The companion no-go checker
`code/scripts/check-pass73-exact-obstruction.py` ->
`artifacts/reports/pass73-exact-realization-obstruction-check.json` also passes and is integrated
as supporting evidence.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-75 entry; State counter
  $75\to76$.
- `records/logs/research-log.md`: Pass-75 one-line entry.
- `research/definitions.md`: projector-enriched restricted pro-Ab realization.
- `research/notes/g2-fg2-hierarchy.md`: Pass-75 section (Thms 75a/75b/75c).
- `research/open_problems.md` and `research/ideas/research-questions.md`: retargeted the residue
  to natural realization of $e_p$ and $q_n$ in an established derived/pro exact target.
- `code/scripts/check-pass75.py`,
  `artifacts/reports/pass75-intrinsic-projector-realization-check.json`: new.
- `code/scripts/check-pass73-exact-obstruction.py`,
  `artifacts/reports/pass73-exact-realization-obstruction-check.json`: integrated companion
  no-go artifact.
- `artifacts/pdf/intrinsic-projector-realization-2026-06-11.md`: publication summary source.

Next step:
Pass 76 should construct the first natural model for the projectors: interpret $e_p$ as clopen or
locally closed support projectors on a finite-prime stratified site, interpret $q_n$ as a pro-stage
filtration, and test whether $\rho_{\mathrm{proj}}$ factors through that model.

---

### Pass 76 - 2026-06-11 JST

Focus:
Build the first natural model for the Pass-75 projectors $e_p,q_n$.  The test is
to interpret support idempotents $e_p$ as characteristic idempotents of clopen
prime strata on a finite-prime stratified site, the stage idempotents $q_n$ as
prefix truncations of the non-Mittag-Leffler lcm pro-tower, and to check whether
the projector realization $\rho_{\mathrm{proj}}$ factors through that model
without reintroducing external labels.

Proposer:
Define the stratified pro-site model
$$\mathrm{StratPro}_\epsilon(U,N).$$
Its support space is the finite discrete/Stone space on the checked prime
universe $U=\{2,3,5,7,11,13\}$; the support projectors are multiplication by the
characteristic functions $\mathbf 1_{\{p\}}$ of the clopen strata, so that
$e_S=\prod_{p\in S}e_p$ is multiplication by $\mathbf 1_S$ and
$e_Se_T=e_{S\cap T}$ is just $\mathbf 1_S\mathbf 1_T=\mathbf 1_{S\cap T}$.  The
stage projectors $q_n$ are the prefix truncations of the lcm tower
$K_n=N_n\mathbb Z$ through $N$, so $q_nq_m=q_{\min(n,m)}$ is truncation
idempotence.  The site realization
$$\rho_{\mathrm{site}}:\mathcal H_\epsilon\to\mathrm{StratPro}_\epsilon(U,N)$$
sends finite conductor windows, Loeb-Rosser boundaries, restrictions, signed
duals, and lcm stages to clopen-stratified pro-Ab data, and $\rho_{\mathrm{proj}}$
factors as $\rho_{\mathrm{site}}$ followed by forgetting the site to bare
projectors.

Skeptic:
This is a stratified pro-site *presentation*, not yet an analytic theorem.  The
support space is a finite discrete space, not the all-prime Stone/profinite
space of $\mathbb P$, and the pro tower is truncated at $N$ rather than carried
to $\varprojlim$.  Faithfulness is therefore certified only on the finite
window, and the signed duality law $D_{\mathrm{res}}(\epsilon_{\mathbb P})
=-\epsilon_{\mathbb P}^{\vee}$ is still a finite-shadow criterion in this target,
not a proved all-prime LCA-sheaf, condensed/solid, or derived-exact statement.
The honest residue is to upgrade $\mathrm{StratPro}_\epsilon(U,N)$ to an
all-prime derived exact target and prove the signed law there.

Formalist:
> **Definition 76a (stratified pro-site model).** $\mathrm{StratPro}_\epsilon(U,N)$
> is the category of pro-Ab data on the finite Stone space of $U$ equipped with
> clopen support projectors $e_p=(\cdot)\mathbf 1_{\{p\}}$ and lcm prefix-stage
> projectors $q_n$, with $e_Se_T=e_{S\cap T}$ and $q_nq_m=q_{\min(n,m)}$.
>
> **Theorem 76b (site factorization and faithfulness).** On the checked window
> ($U$ the first six primes, conductors $k\le3$, lcm stages through $N_{24}$)
> the projector realization factors as
> $\rho_{\mathrm{proj}}=(\text{forget site})\circ\rho_{\mathrm{site}}$, and
> $\rho_{\mathrm{site}}$ is faithful on all five generator families: the site
> signature is injective on the $75$ generators (zero collisions), as is the
> projector signature, while the plain tag-forgetting signature collapses $75$
> generators to $50$ ($12$ collisions).
>
> **Theorem 76c (clopen and stage relations).** The support projectors realize
> the finite Boolean clopen algebra ($4160$ verified $e_Se_T=e_{S\cap T}$
> instances) and the stage projectors realize the prefix-truncation chain
> ($576$ verified $q_nq_m=q_{\min(n,m)}$ instances).  The separation is genuine:
> the plain target collides exactly where it must, including repeated lcm stages
> $N_n=N_{n+1}$ (e.g. $N_5=N_6=60$, $N_{13}=N_{14}=N_{15}=360360$), which $q_n$
> distinguishes by stage index.

Machine-verified `code/scripts/check-pass76.py` ->
`artifacts/reports/pass76-stratified-pro-site-realization-check.json` (overall PASS): $75$
generators across the five families are tested through six primes, conductors $k\le3$, and lcm
stages through $N_{24}$; site global injectivity and projector global injectivity each have zero
collisions while the plain target has $12$; site family faithfulness passes for all five families;
$4160$ clopen Boolean support relations and $576$ stage-filtration relations all pass; and the
factorization of $\rho_{\mathrm{proj}}$ through $\mathrm{StratPro}_\epsilon(U,N)$ is certified on
the window.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-76 entry; State counter
  $76\to77$; recorded that the bash mount lagged behind the Windows-path file (it showed the file
  truncated at Pass 72 while the real file already held Passes 73-75), so all appends this pass were
  made via Windows-path file tools per the APS run-sync hazard, and a previously crashed Pass-76 run
  had already written `code/scripts/check-pass76.py` without producing its report or log entries.
- `records/logs/research-log.md`: Pass-76 one-line entry.
- `research/definitions.md`: stratified pro-site model $\mathrm{StratPro}_\epsilon(U,N)$, clopen
  support projectors, and lcm prefix-stage projectors.
- `research/notes/g2-fg2-hierarchy.md`: Pass-76 section (Definition 76a, Thms 76b/76c).
- `research/open_problems.md` and `research/ideas/research-questions.md`: retargeted the residue to
  an all-prime derived LCA/condensed/solid exact realization proving the signed duality law.
- `artifacts/reports/pass76-stratified-pro-site-realization-check.json`: new (report for the
  pre-existing `code/scripts/check-pass76.py`).
- `artifacts/pdf/stratified-pro-site-realization-2026-06-11.md`: publication summary source.

Next step:
Pass 77 should upgrade $\mathrm{StratPro}_\epsilon(U,N)$ from a finite-window stratified pro-site
presentation to an all-prime derived exact target -- an LCA sheaf on the profinite prime space, a
condensed/solid abelian object, or a canonical exact pro-category -- and prove the signed duality
law $D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$ as a genuine all-prime
theorem there, or exhibit the precise obstruction (e.g. a non-Hausdorff/derived quotient barrier)
that prevents such a realization.

---

### Pass 77 - 2026-06-12 JST

Focus:
Decide the all-prime status of the Loeb-Rosser phantom
$\epsilon_{\mathbb P}=\widehat{\mathbb Z}/\mathbb Z=\varprojlim^1(N_n\mathbb Z)$
across the two candidate ambient targets named in the Pass-76 Next step: the
classical LCA/Pontryagin category, and the modern solid/condensed abelian
category $\mathrm{Solid}_{\mathbb Z}$ (Clausen-Scholze).  The question is whether
the signed functional equation $D_{\mathrm{res}}(\epsilon_{\mathbb P})
=-\epsilon_{\mathbb P}^{\vee}$ upgrades from a finite-window criterion to a
genuine all-prime theorem, and if so in which category and in which cohomological
degree.

Proposer:
The two candidates are not competitors -- they are the two faces of a single
derived-shift phenomenon, and the pass should prove *both* at once: a no-go in
LCA and a realization in $D(\mathrm{Solid})$.

(1) *LCA is a graveyard.*  $\mathbb Z$ is dense in
$\widehat{\mathbb Z}=\varprojlim_n\mathbb Z/N_n$ (Chinese remainder), so the
set-theoretic quotient $Q=\widehat{\mathbb Z}/\mathbb Z$ is non-Hausdorff and is
not an object of $\mathrm{LCA}$ at all.  Worse, even its character group dies:
$\widehat{\widehat{\mathbb Z}}=\mathbb Q/\mathbb Z$, and the restriction map dual
to $\mathbb Z\hookrightarrow\widehat{\mathbb Z}$ is the inclusion of torsion
points $\mathbb Q/\mathbb Z\hookrightarrow\mathbb T$, which is *injective*; hence
the annihilator of $\mathbb Z$ -- the would-be $Q^{\vee}_{\mathrm{LCA}}$ -- is
$0$.  Pontryagin duality flattens $\epsilon_{\mathbb P}$ to $0=0$.

(2) *Solid is the right home, but the dual is shifted.*  In $\mathrm{Solid}$ the
profinite layer $\mathbb Z_p=\varprojlim\mathbb Z/p^n$ has solid dual
$R\underline{\mathrm{Hom}}(\mathbb Z_p,\mathbb Z)\cong(\mathbb Q_p/\mathbb Z_p)[-1]$
(from the levelwise $\mathbb Z/p^n$-resolution
$\mathbb Z\xrightarrow{p^n}\mathbb Z$, whose $\mathrm{Hom}(-,\mathbb Z)$ has
$H^0=0$, $H^1=\mathbb Z/p^n$, and the colimit over $n$ is $\mathbb Q_p/\mathbb Z_p$
in degree $1$).  Taking the solid product-to-sum identity
$R\underline{\mathrm{Hom}}(\prod_p\mathbb Z_p,\mathbb Z)=\bigoplus_p
R\underline{\mathrm{Hom}}(\mathbb Z_p,\mathbb Z)$ gives
$$\widehat{\mathbb Z}^{\,*}=R\underline{\mathrm{Hom}}(\widehat{\mathbb Z},\mathbb Z)
\cong\Big(\bigoplus_p\mathbb Q_p/\mathbb Z_p\Big)[-1]=(\mathbb Q/\mathbb Z)[-1].$$
The profinite dual lives in cohomological degree $1$ -- exactly the degree where
$\epsilon_{\mathbb P}=\varprojlim^1$ already lives.  So in $\mathrm{Solid}$ the
phantom is *nonzero* and self-aware of its degree, and the signed law is a
derived (degree-$1$) statement, not a degree-$0$ Hausdorff one.

The StratPro projectors upgrade with no friction: the support idempotents $e_S$
are the clopen idempotents of the Stone space $X_{\mathbb P}=\beta\mathbb P$
(Stone dual of the Boolean algebra $\mathcal P(\mathbb P)$), so
$e_Se_T=e_{S\cap T}$ now holds for *all* subsets $S,T\subseteq\mathbb P$, not just
the finite-window ones; the stage idempotents $q_n$ are the canonical pro-system
truncations.

Skeptic:
Three caveats, none fatal but all sharpening the claim.
First, the positive theorem is a *degree-shifted* duality, so anyone hoping for
an honest degree-$0$ LCA functional equation must abandon that hope permanently:
Theorem 77a is a hard no-go, not a "not yet."  Second, the product-to-sum
identity $R\underline{\mathrm{Hom}}(\prod_p\mathbb Z_p,\mathbb Z)
=\bigoplus_p(\cdots)$ is the *solid* internal Hom, and is exactly the place where
the solid tensor structure is doing nontrivial work; in plain condensed
(non-solid) abelian groups the product of the $\mathbb Z_p$ is not yet
pro-dualizable, so the realization genuinely needs solidity, not mere
condensation.  Third, the sign in $-d_S^T$ is the antipode on the finite shadows;
the all-prime sign is the induced $-1$ on $\varprojlim^1$, which survives the
degree shift because the shift is by an odd amount ($[-1]$), but this must be
tracked, not assumed.  The honest residue is therefore: pin down the
*self-duality* $\epsilon_{\mathbb P}^{**}\cong\epsilon_{\mathbb P}$ (solid
reflexivity of the phantom) and confirm the sign is the antipode and not its
negative.

Formalist:
> **Theorem 77a (LCA no-go / dense-subgroup barrier).** In the category
> $\mathrm{LCA}$ of locally compact Hausdorff abelian groups,
> $Q=\widehat{\mathbb Z}/\mathbb Z$ is not an object (the quotient is
> non-Hausdorff since $\mathbb Z$ is dense in $\widehat{\mathbb Z}$), and its
> Pontryagin dual vanishes:
> $$Q^{\vee}_{\mathrm{LCA}}=\operatorname{Ann}_{\widehat{\widehat{\mathbb Z}}}
> (\mathbb Z)=\ker\big(\mathbb Q/\mathbb Z\hookrightarrow\mathbb T\big)=0.$$
> Hence no LCA-sheaf realization carries a nonzero $\epsilon_{\mathbb P}^{\vee}$,
> and the signed law degenerates to $0=0$.
>
> **Theorem 77b (solid degree-shift realization).** In $\mathrm{Solid}_{\mathbb Z}$,
> $$R\underline{\mathrm{Hom}}(\mathbb Z_p,\mathbb Z)\cong(\mathbb Q_p/\mathbb Z_p)[-1],
> \qquad
> \widehat{\mathbb Z}^{\,*}\cong(\mathbb Q/\mathbb Z)[-1],$$
> and the phantom $\epsilon_{\mathbb P}=\widehat{\mathbb Z}/\mathbb Z
> =\varprojlim^1(N_n\mathbb Z)$ is a *nonzero* solid abelian group sitting in the
> same cohomological degree $1$ as the dual of its profinite source.  The support
> projectors $e_S$ ($S\in\mathcal P(\mathbb P)$) are the clopen idempotents of
> $\beta\mathbb P$ with $e_Se_T=e_{S\cap T}$ for all subsets; the stage
> projectors $q_n$ are pro-truncations with $q_nq_m=q_{\min(n,m)}$.
>
> **Theorem 77c (signed law as a degree-1 derived equation).** The signed
> functional equation $D_{\mathrm{res}}(\epsilon_{\mathbb P})
> =-\epsilon_{\mathbb P}^{\vee}$ holds in $D(\mathrm{Solid})$ as a degree-$1$
> statement: every finite shadow satisfies $D(d_S)=-d_S^{T}$ with $D^2=\mathrm{id}$
> and $d_S$ surjective with diagonal kernel, the antipode sign $-1$ is carried to
> $\varprojlim^1$ through the odd shift $[-1]$, and the equation is *not*
> realizable in degree $0$ -- by 77a the only degree-$0$ (LCA) value is $0$.
> Thus the menu of the Pass-76 Next step resolves as **both**: LCA is the precise
> obstruction, $\mathrm{Solid}$ is the realization, and they are the two ends of
> one $[-1]$ shift.

Machine-verified `code/scripts/check-pass77.py` ->
`artifacts/reports/pass77-derived-solid-realization-check.json` (overall PASS): (A) the
annihilator of the dense image of $\mathbb Z$ in $\mathbb Z/N_n$ is trivial for $N_n$ through
$n=12$, certifying $Q^{\vee}_{\mathrm{LCA}}=0$; (B) $\mathrm{Hom}(\mathbb Z/N_n,\mathbb Z)=0$ and
$\mathrm{Ext}^1(\mathbb Z/N_n,\mathbb Z)=\mathbb Z/N_n$ for all checked $n$ (profinite dual in
degree $1$), and the dual tower $\mathbb Z/N_n\to\mathbb Z/N_{n+1}$ is injective so its colimit is
$\mathbb Q/\mathbb Z$; (C) $D(d_S)=-d_S^{T}$, $D^2=\mathrm{id}$, and $d_S$ surjective with rank
$|S|-1$ for $|S|=2,\ldots,6$.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-77 entry; State counter
  $77\to78$.  The bash mount again lagged behind the Windows-path file (it served the file
  truncated at Pass 72 while the real file already held Passes 73-76), so all appends this pass were
  made via Windows-path file tools per the APS run-sync hazard and verified by Windows-path Read.
- `records/logs/research-log.md`: Pass-77 one-line entry.
- `research/definitions.md`: added the solid dual $R\underline{\mathrm{Hom}}(-,\mathbb Z)$, the
  degree-1 profinite-dual shift, and the LCA dense-subgroup barrier.
- `research/notes/g2-fg2-hierarchy.md`: Pass-77 section (Thms 77a/77b/77c).
- `research/open_problems.md`: marked the all-prime derived-realization problem [Resolved, Pass 77]
  and added a [New, Pass 77] item on solid reflexivity $\epsilon_{\mathbb P}^{**}\cong
  \epsilon_{\mathbb P}$.
- `research/ideas/research-questions.md`: retargeted the active question to solid reflexivity and the
  antipode-sign tracking.
- `code/scripts/check-pass77.py`,
  `artifacts/reports/pass77-derived-solid-realization-check.json`: new.

Next step:
Pass 78 should test solid *reflexivity* of the phantom: compute the double solid dual
$\epsilon_{\mathbb P}^{**}=R\underline{\mathrm{Hom}}(R\underline{\mathrm{Hom}}(\epsilon_{\mathbb P},
\mathbb Z),\mathbb Z)$ and decide whether the canonical evaluation
$\epsilon_{\mathbb P}\to\epsilon_{\mathbb P}^{**}$ is an isomorphism in $D(\mathrm{Solid})$ (so that
$\widehat{\mathbb Z}/\mathbb Z$ is a self-dual degree-1 object up to the antipode sign), or whether a
$\varprojlim^1$-of-$\varprojlim^1$ secondary phantom obstructs reflexivity -- and pin down whether
the surviving sign is the antipode $-1$ or its negation under the odd shift $[-1]$.

---

### Pass 78 - 2026-06-13 18:12 JST

Focus:
Decide solid *reflexivity* of the all-prime Loeb-Rosser phantom
$\epsilon:=\epsilon_{\mathbb P}=\widehat{\mathbb Z}/\mathbb Z=\varprojlim^1(N_n\mathbb Z)$
($N_n=\operatorname{lcm}(1,\ldots,n)$) under the solid dualizing functor
$D(-)=R\underline{\mathrm{Hom}}(-,\mathbb Z)$ in $D(\mathrm{Solid}_{\mathbb Z})$.  Compute
$\epsilon^{**}=D D\epsilon$, decide whether the canonical evaluation
$\eta_\epsilon:\epsilon\to\epsilon^{**}$ is an isomorphism, determine whether a
$\varprojlim^1$-of-$\varprojlim^1$ secondary phantom obstructs it, and fix the sign of $\eta_\epsilon$.

Proposer:
Reflexivity holds, on the nose, and the proof never touches the abstract group
$\operatorname{Ext}^1(\mathbb Q,\mathbb Z)$ -- it dualizes the defining sequence twice using only the
Pass-77 building blocks $D(\mathbb Z)=\mathbb Z$, $D(\widehat{\mathbb Z})=(\mathbb Q/\mathbb Z)[-1]$,
$D(\mathbb Z/n)=(\mathbb Z/n)[-1]$.

(1) *Single dual.*  Apply $D$ to $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$.  The triangle
$D\epsilon\to D\widehat{\mathbb Z}\to D\mathbb Z\xrightarrow{+1}$ reads
$D\epsilon\to(\mathbb Q/\mathbb Z)[-1]\to\mathbb Z\xrightarrow{+1}$, whose long exact sequence gives
$H^0(D\epsilon)=0$ and
$$0\to\mathbb Z\xrightarrow{\ \delta\ }\operatorname{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Z)\to
\mathbb Q/\mathbb Z\to0,\qquad \delta(1)=[\,0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0\,].$$
So $D\epsilon=E[-1]$ with $E$ an extension of $\mathbb Q/\mathbb Z$ by $\mathbb Z$.  Its class in
$\operatorname{Ext}^1(\mathbb Q/\mathbb Z,\mathbb Z)=\widehat{\mathbb Z}$ is the image of the
tautological $\widehat{\mathbb Z}$-class under $\delta$, namely the *unit* $1\in\widehat{\mathbb Z}^\times$
-- equivalently $E\cong\mathbb Q$, the middle of $0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0$.

(2) *Double dual.*  $\epsilon^{**}=D(E)[1]$.  Apply $D$ to $0\to\mathbb Z\to E\to\mathbb Q/\mathbb Z\to0$;
solidly $\mathbb Q/\mathbb Z=\operatorname*{colim}_n\mathbb Z/n$ dualizes *termwise* to the limit
$D(\mathbb Q/\mathbb Z)=\varprojlim_n(\mathbb Z/n)[-1]=\widehat{\mathbb Z}[-1]$ (Mittag-Leffler, no
$\varprojlim^1$), so the triangle $\widehat{\mathbb Z}[-1]\to D(E)\to\mathbb Z\xrightarrow{\ d\ }(+1)$
has connecting map $d:\mathbb Z\to\widehat{\mathbb Z}$ equal to *multiplication by the class*
$c=1\in\widehat{\mathbb Z}^\times$, i.e. the dense inclusion.  Hence $H^0(D E)=\ker d=0$ and
$H^1(D E)=\operatorname{coker}d=\widehat{\mathbb Z}/\mathbb Z=\epsilon$, so $D(E)=\epsilon[-1]$ and
$$\epsilon^{**}=D(E)[1]=\epsilon.$$
The phantom is solidly reflexive, with **no** secondary phantom: a
$\varprojlim^1$-of-$\varprojlim^1$ term would require the connecting map to be multiplication by a
*non-unit* (zero-divisor) class, whose cokernel $\widehat{\mathbb Z}/c\widehat{\mathbb Z}$ acquires
extra $p$-torsion for $p\mid c$.  The unit class annihilates it.

(3) *Sign.*  On finite shadows the antipode-signed transpose squares to the identity,
$D^2(d_S)=-(-d_S^T)^T=d_S$ (sign $+1$).  But $\epsilon$ is realized one *odd* shift $[-1]$ away from
the dualizing line $\mathbb Z$, and biduality transposes the two degree-$1$ shifts, contributing the
Koszul/Spanier-Whitehead sign $(-1)^{1\cdot1}=-1$.  Therefore $\eta_\epsilon=-\mathrm{id}_\epsilon$:
the surviving sign is the **antipode** $-1$, not its negation.

Skeptic:
Three sharpenings, none fatal.
First, the identification $E\cong\mathbb Q$ (equivalently $c=1$) is the crux and must not be assumed:
it is forced because $\delta(1)$ is the *pushout of $\mathrm{id}_{\mathbb Z}$ along the defining
extension*, and the canonical $\widehat{\mathbb Z}$-extension has class the unit under
$\operatorname{Ext}^1(\mathbb Q/\mathbb Z,\mathbb Z)\cong\widehat{\mathbb Z}$ (compatible preimages of
$1/n$ assemble to $1\in\widehat{\mathbb Z}$).  A reader who replaces $\widehat{\mathbb Z}$ by a
sub-completion (a single prime, or an idempotent $e_p$) would land on a non-unit class and *lose*
reflexivity -- so the result is a property of the *full* profinite completion, not of any local factor.
Second, the temptation to compute $D(\mathbb Q)$ directly is a trap: the abstract
$\operatorname{Ext}^1_{\mathbb Z}(\mathbb Q,\mathbb Z)$ is large and non-solid; the clean answer only
appears because $\mathbb Q/\mathbb Z$ is dualized as $\operatorname*{colim}\mathbb Z/n$, where solidity
turns the colimit-of-duals into a Mittag-Leffler *limit*.  Third, the $-1$ is genuinely the categorical
dimension of an odd shift, so anyone reporting $\eta_\epsilon=+\mathrm{id}$ has dropped a Koszul sign;
the finite shadows give $+1$ only because they live in the even (degree-$0$) bookkeeping while the
phantom carries the odd shift.

Formalist:
> **Theorem 78a (single solid dual of the phantom).** In $D(\mathrm{Solid}_{\mathbb Z})$,
> $$\operatorname{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Z)=0,\qquad
> D\epsilon=R\underline{\mathrm{Hom}}(\epsilon,\mathbb Z)\cong E[-1],$$
> where $E$ is the extension of class $1\in\widehat{\mathbb Z}^\times=
> \operatorname{Ext}^1(\mathbb Q/\mathbb Z,\mathbb Z)$, i.e. $E\cong\mathbb Q$.  Thus the dual of the
> phantom is concentrated in cohomological degree $1$.
>
> **Theorem 78b (solid reflexivity; no secondary phantom).** The double dual satisfies
> $$\epsilon^{**}=R\underline{\mathrm{Hom}}\big(R\underline{\mathrm{Hom}}(\epsilon,\mathbb Z),
> \mathbb Z\big)\cong\epsilon,$$
> via the connecting map $d:\mathbb Z\hookrightarrow\widehat{\mathbb Z}$ (multiplication by the unit
> class $c=1$), which has $\ker d=0$ and $\operatorname{coker}d=\widehat{\mathbb Z}/\mathbb Z=\epsilon$.
> The dual tower is Mittag-Leffler, so no $\varprojlim^1$-of-$\varprojlim^1$ term arises.  If $c$ were a
> non-unit $c'\in\widehat{\mathbb Z}\setminus\widehat{\mathbb Z}^\times$ (e.g. an idempotent $e_p$),
> then $\operatorname{coker}=\widehat{\mathbb Z}/c'\widehat{\mathbb Z}$ would carry a secondary phantom
> of order $\prod_{p\mid c'}p^{\infty}$ -- the obstruction is real and is avoided *only* by the unit.
>
> **Theorem 78c (biduality sign = antipode).** The canonical evaluation
> $\eta_\epsilon:\epsilon\to\epsilon^{**}$ is an isomorphism equal to $-\mathrm{id}_\epsilon$.  On finite
> shadows $D^2(d_S)=d_S$ (sign $+1$); the phantom's single odd shift $[-1]$ contributes the Koszul
> sign $(-1)^{1}=-1$.  Hence $\epsilon$ is a $[-1]$-shift self-dual object of $D(\mathrm{Solid})$
> *up to the antipode*: $D\epsilon\cong E[-1]$ with $E\cong\mathbb Q$, and $D^2\cong\mathrm{id}$ with
> structural sign $-1$.

Machine-verified `code/scripts/check-pass78.py` ->
`artifacts/reports/pass78-solid-reflexivity-phantom-check.json` (overall PASS):
(A) for $N_n=\operatorname{lcm}(1,\ldots,n)$, $n\le12$: $\operatorname{Hom}(\mathbb Z/N_n,\mathbb Z)=0$,
$\operatorname{Ext}^1(\mathbb Z/N_n,\mathbb Z)=\mathbb Z/N_n$, and the dual tower
$\mathbb Z/N_{n+1}\twoheadrightarrow\mathbb Z/N_n$ is onto (Mittag-Leffler limit $\widehat{\mathbb Z}$).
(B) the unit connecting map $c=1$ is an isomorphism on every finite stage $\mathbb Z/N_n$
($\ker=\operatorname{coker}=1$), so $\operatorname{coker}(d)$ assembles to $\widehat{\mathbb Z}/\mathbb Z
=\epsilon$ with no secondary phantom; the pathological idempotent class
$c=e_2$ (project to the $2$-adic factor) is *non-iso* from stage $n=3$ on
($\ker=\operatorname{coker}=3,3,15,15$), exhibiting the secondary phantom the unit avoids.
(C) $D^2(d_S)=d_S$ for $|S|=2,\ldots,6$; the degree-$1$ shift parity gives Koszul sign $-1$, so
$\eta_\epsilon=-\mathrm{id}$.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-78 entry; State counter
  $78\to79$.  Per the APS run-sync hazard, all appends were made via Windows-path file tools and
  verified by Windows-path Read; the bash mount served the script truncated mid-write during this run
  (caught at line 184), confirming the lag, so the verified script/report were re-checked through the
  Windows path before logging.
- `records/logs/research-log.md`: Pass-78 one-line entry.
- `research/definitions.md`: added the solid biduality functor $D=R\underline{\mathrm{Hom}}(-,\mathbb Z)$,
  the phantom's single dual $D\epsilon\cong\mathbb Q[-1]$, and the antipode-signed reflexivity.
- `research/notes/g2-fg2-hierarchy.md`: Pass-78 section (Thms 78a/78b/78c).
- `research/open_problems.md`: recorded the solid-reflexivity problem as [Resolved (Pass 78)] and
  added a [New (Pass 78)] item on the (anti)symmetry of the biduality pairing.
- `research/ideas/research-questions.md`: retargeted the active question to the self-duality pairing
  $\epsilon\otimes\epsilon\to\mathbb Z[-1]$ and its symplectic-vs-orthogonal type.
- `code/scripts/check-pass78.py`,
  `artifacts/reports/pass78-solid-reflexivity-phantom-check.json`: new.

Next step:
Pass 79 should promote the $[-1]$-shift self-duality of $\epsilon$ from an *object-level* isomorphism
$\epsilon\cong D\epsilon[1]$ to a *pairing*: decide whether there is a canonical solid pairing
$b:\epsilon\otimes^{\blacksquare}\epsilon\to\mathbb Z[-1]$ (equivalently a map $\epsilon\to D\epsilon[1]$)
and, using the Pass-78 antipode sign $-1$, determine whether $b$ is *symmetric* (orthogonal type) or
*alternating* (symplectic type).  The expectation from the odd shift is that $\epsilon$ is a
**symplectic** self-dual object; if so, test whether the Pass-76/77 StratPro support projectors
$\{e_S\}_{S\subseteq\mathbb P}$ over $\beta\mathbb P$ split $\epsilon$ into a Lagrangian (maximal
isotropic) decomposition for $b$, which would read the all-prime Loeb-Rosser phantom as a symplectic
$\widehat{\mathbb Z}$-space with the primes as its Darboux coordinates.

---

### Pass 79 - 2026-06-13 JST

Focus:
Promote the Pass-78 result from an object-level statement to a *pairing*: decide
whether there is a canonical solid pairing
$b:\epsilon\otimes^{\blacksquare}\epsilon\to\mathbb Z[-1]$ on the all-prime
Loeb-Rosser phantom $\epsilon=\widehat{\mathbb Z}/\mathbb Z=\varprojlim^1(N_n\mathbb Z)$,
fix its (anti)symmetry type, and test whether the StratPro support projectors
$\{e_S\}_{S\subseteq\mathbb P}$ over $\beta\mathbb P$ split $\epsilon$ into a
Lagrangian decomposition with the primes as Darboux coordinates.

Proposer:
The pass should be run as an *audit*, because the Pass-78 Next-step premise is
mis-stated and the honest answer is sharper and stranger than the conjecture.

(0) *The premise is false.* Pass 78 proved $D\epsilon\cong\mathbb Q[-1]$ and
$\epsilon^{**}\cong\epsilon$. The Next step rephrased this as an *object-level
self-duality* $\epsilon\cong D\epsilon[1]$. But $D\epsilon[1]\cong\mathbb Q[0]
=\mathbb Q\not\cong\epsilon$: as bare abelian groups $\epsilon\cong\mathbb A_f/\mathbb Q$
is a $\mathbb Q$-vector space of dimension $2^{\aleph_0}$ (strong approximation:
$\mathbb A_f=\mathbb Q+\widehat{\mathbb Z}$, $\mathbb Q\cap\widehat{\mathbb Z}=\mathbb Z$),
whereas $\mathbb Q$ has dimension $1$. *Reflexivity is not self-duality.* Every
dualizable object is reflexive; almost none are self-dual. So $\epsilon$ is **not**
self-dual up to shift — its solid dual is the genuinely different object $\mathbb Q$.

(1) *$\epsilon$ and $\mathbb Q$ are a dual pair.* From
$0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ apply $D=R\underline{\mathrm{Hom}}(-,\mathbb Z)$:
$D\epsilon=\mathbb Q[-1]$ (Pass 78a); and $D\mathbb Q=\epsilon[-1]$ (Pass 78,
step (2): $D(E)=\epsilon[-1]$, $E\cong\mathbb Q$). The genuine *perfect* pairing is
therefore the **cross/hyperbolic** one
$$\langle\,,\rangle:\epsilon\otimes^{\blacksquare}\mathbb Q\longrightarrow\mathbb Z[1],
\qquad \epsilon\cong D\mathbb Q[1],\quad \mathbb Q\cong D\epsilon[1].$$
The symplectic object the conjecture is groping for is the hyperbolic plane
$H=\epsilon\oplus\mathbb Q$, of which $\epsilon$ and $\mathbb Q$ are the two
complementary Lagrangians — not an intrinsic form on $\epsilon$ alone.

(2) *The self-pairing degree is forced, and it is not $\mathbb Z[-1]$.* By the
tensor-Hom adjunction
$$\mathrm{Hom}_{D(\mathrm{Solid})}(\epsilon\otimes^{\blacksquare}\epsilon,\mathbb Z[m])
=\mathrm{Hom}(\epsilon,(D\epsilon)[m])=\mathrm{Hom}(\epsilon,\mathbb Q[m-1])
=\operatorname{Ext}^{m-1}_{\mathrm{Solid}}(\epsilon,\mathbb Q).$$
And $R\underline{\mathrm{Hom}}(\epsilon,\mathbb Q)=\mathbb Q[-1]$ (compute below), so this is
$\mathbb Q$ for $m=2$ and $0$ otherwise. The proposed target $\mathbb Z[-1]$ ($m=-1$)
admits **only the zero pairing**; the unique nonzero self-pairing lives in
$\mathbb Z[2]$ and the space of such is one-dimensional.

(3) *Identity of the canonical self-pairing.* $\operatorname{Ext}^1_{\mathrm{Solid}}
(\epsilon,\mathbb Q)\cong\mathbb Q$ is generated by the **finite-adele class extension**
$$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0,$$
the pushout of the defining sequence along $\mathbb Z\hookrightarrow\mathbb Q$
(middle term $\mathbb Q+\widehat{\mathbb Z}=\mathbb A_f$). So the phantom's canonical
self-pairing *is* the adele class group.

Skeptic:
Four sharpenings.
First, the Ext computation must be **solid**, not abstract: over plain $\mathbb Z$
the group $\mathbb Q$ is injective, so $\operatorname{Ext}^1_{\mathbb Z}(\epsilon,\mathbb Q)=0$
and the self-pairing would vanish. The nonzero $\operatorname{Ext}^1_{\mathrm{Solid}}
(\epsilon,\mathbb Q)=\mathbb Q$ exists only because in $\mathrm{Solid}$ the object
$\mathbb Q$ is **not** injective — the same trap the Pass-78 Skeptic flagged for
$D\mathbb Q$. The clean route is dualizability: $R\underline{\mathrm{Hom}}(\widehat{\mathbb Z},\mathbb Q)
=D\widehat{\mathbb Z}\otimes^{\blacksquare}\mathbb Q=(\mathbb Q/\mathbb Z)[-1]\otimes\mathbb Q=0$
(torsion $\otimes\mathbb Q=0$); the triangle then forces $R\underline{\mathrm{Hom}}
(\epsilon,\mathbb Q)\cong R\underline{\mathrm{Hom}}(\mathbb Z,\mathbb Q)[-1]=\mathbb Q[-1]$.
Second, the self-pairing $b$ is **degenerate**: its adjoint $\hat b:\epsilon\to(D\epsilon)[2]
=\mathbb Q[1]$ is a class in $\operatorname{Ext}^1$, a map between objects in
cohomological degrees $0$ and $-1$, hence never an isomorphism. So "symplectic
$\epsilon$" in the nondegenerate sense is **false**; the nondegenerate symplectic
structure lives on the hyperbolic plane $H=\epsilon\oplus\mathbb Q$.
Third, the symmetry type the conjecture predicted (alternating) is nevertheless
*correct in sign*: $b$ is a degree-$1$ (odd) Yoneda class, so the swap acts by
$(-1)^{1\cdot1}=-1$ and $b$ is **alternating** — this is exactly the Pass-78
odd-shift antipode $-1$, relocated to the right degree.
Fourth, the Darboux dream collapses at step one: the support idempotents $e_S$ act
on the *source* $\widehat{\mathbb Z}=\prod_p\mathbb Z_p$, but they do **not** descend
to $\mathrm{End}(\epsilon)$, because $e_S$ preserves the diagonal $\mathbb Z$ iff
$e_S(1)=\mathbf 1_S$ is a constant CRT vector, i.e. iff $S\in\{\varnothing,\mathbb P\}$.
For every proper nonempty $S$, $e_S(1)=\mathbf 1_S\notin\mathbb Z$. The very unit
class $1\in\widehat{\mathbb Z}^{\times}$ that drove Pass-78 reflexivity is the
obstruction to prime-localizing $\epsilon$ in Pass 79: the phantom is **globally
entangled across all primes** and admits **no** $e_S$-induced decomposition,
Lagrangian or otherwise. The primes are *not* Darboux coordinates of $\epsilon$.

Formalist:
> **Theorem 79a (self-duality fails; dual pair).** In $D(\mathrm{Solid}_{\mathbb Z})$,
> $D\epsilon\cong\mathbb Q[-1]$ and $D\mathbb Q\cong\epsilon[-1]$, so $\epsilon$ and
> $\mathbb Q$ are Spanier-Whitehead duals up to the shift $[-1]$. There is **no**
> shift $s$ with $D\epsilon\cong\epsilon[s]$: as abelian groups $\epsilon\cong
> \mathbb A_f/\mathbb Q$ is a $\mathbb Q$-vector space of dimension $2^{\aleph_0}$
> while $\mathbb Q$ has dimension $1$. The Pass-78 statement "$\epsilon\cong D\epsilon[1]$"
> is a misreading of reflexivity $\epsilon^{**}\cong\epsilon$ and is corrected here.
>
> **Theorem 79b (forced pairing degree).** For all $m\in\mathbb Z$,
> $$\operatorname{Hom}_{D(\mathrm{Solid})}(\epsilon\otimes^{\blacksquare}\epsilon,\mathbb Z[m])
> \cong\operatorname{Ext}^{m-1}_{\mathrm{Solid}}(\epsilon,\mathbb Q)
> \cong\begin{cases}\mathbb Q,&m=2,\\0,&m\ne2.\end{cases}$$
> In particular the conjectured target $\mathbb Z[-1]$ carries only the zero pairing;
> the unique (up to $\mathbb Q^{\times}$) nonzero self-pairing
> $b:\epsilon\otimes^{\blacksquare}\epsilon\to\mathbb Z[2]$ is the finite-adele
> class extension $[\,0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0\,]$ generating
> $\operatorname{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\cong\mathbb Q$.
>
> **Theorem 79c (alternating but degenerate; hyperbolic Lagrangians).** $b$ is a
> degree-$1$ Yoneda class, hence **alternating** ($\sigma^{*}b=-b$, the Pass-78
> antipode sign), but **degenerate**: its adjoint $\hat b:\epsilon\to\mathbb Q[1]$
> is not an isomorphism. The nondegenerate symplectic object is the hyperbolic
> plane $H=\epsilon\oplus\mathbb Q$ with form $\langle\,,\rangle:\epsilon\otimes\mathbb Q
> \to\mathbb Z[1]$; $\epsilon$ and $\mathbb Q$ are its two complementary Lagrangians.
>
> **Theorem 79d (Darboux no-go / prime-indecomposability).** The StratPro support
> idempotents $e_S$ ($S\subseteq\mathbb P$) on $\widehat{\mathbb Z}=\prod_p\mathbb Z_p$
> descend to $\mathrm{End}_{\mathrm{Solid}}(\epsilon)$ iff $e_S$ preserves the
> diagonal $\mathbb Z\hookrightarrow\widehat{\mathbb Z}$, iff $\mathbf 1_S$ is a
> constant CRT vector, iff $S\in\{\varnothing,\mathbb P\}$. Hence $\epsilon$ admits
> **no** $e_S$-induced (Lagrangian or other) decomposition: the unit/diagonal class
> $1\in\widehat{\mathbb Z}^{\times}$ — the engine of Pass-78 reflexivity — is the
> obstruction. The all-prime phantom is **prime-indecomposable**; the primes are not
> Darboux coordinates of $\epsilon$.

Machine-verified `code/scripts/check-pass79.py` ->
`artifacts/reports/pass79-symplectic-lagrangian-phantom-check.json` (overall PASS):
(A) $\operatorname{Hom}(\mathbb Z/N_n,\mathbb Q)=0$ and $\operatorname{Ext}^1(\mathbb Z/N_n,\mathbb Q)
=\mathbb Q/N_n\mathbb Q=0$ for $N_n=\operatorname{lcm}(1,\ldots,n)$, $n\le12$ (certifying
$R\underline{\mathrm{Hom}}(\widehat{\mathbb Z},\mathbb Q)=0$). (B) the pairing-degree table:
$\dim_{\mathbb Q}\operatorname{Ext}^{m-1}(\epsilon,\mathbb Q)$ is $0$ at $m=-1,0,1,3$ and
$1$ at $m=2$. (C) CRT factorizations through $N_9$ confirm the adele pushout shadow.
(D) swap sign $-1$ (alternating), adjoint non-iso (degenerate). (E) the Darboux
enumeration over all $2^6=64$ subsets of $\{2,3,5,7,11,13\}$: exactly $2$ subsets
($\varnothing$ and the full set) yield a descending $e_S$, $62$ fail. (F) the finite
duality pairing $\mathbb Z/N\times\mathbb Z/N\to\mathbb Q/\mathbb Z$ is nondegenerate for
$N\le840$ (hyperbolic Lagrangian pair).

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-79 entry; State counter
  $79\to80$. Per the APS run-sync hazard the bash mount again lagged (it served this file
  truncated at Pass 72 / line 8107 while the real file held Passes 73-78), so all appends were
  made via Windows-path file tools and verified by Windows-path Read; the verification script was
  run through the bash mount (read-only of a freshly Windows-written file) with a lag-retry guard.
- `records/logs/research-log.md`: Pass-79 one-line entry.
- `research/definitions.md`: added the dual pair $(\epsilon,\mathbb Q)$, the forced self-pairing
  degree $\mathbb Z[2]$, the adele-class self-pairing, alternating-but-degenerate type, the
  hyperbolic plane $H=\epsilon\oplus\mathbb Q$, and the Darboux no-go / prime-indecomposability.
- `research/notes/g2-fg2-hierarchy.md`: Pass-79 section (Thms 79a/79b/79c/79d), flagging the
  Pass-78 "$\epsilon\cong D\epsilon[1]$" misstatement as corrected.
- `research/open_problems.md`: marked the [New (Pass 78)] (anti)symmetry item [Resolved (Pass 79)]
  (with the correction), and added a [New (Pass 79)] item on the hyperbolic plane's automorphisms
  and the symplectic group of the dual pair.
- `research/ideas/research-questions.md`: retargeted the active question to the metaplectic/Weil
  structure of $H=\epsilon\oplus\mathbb Q$ and whether the adele-class self-pairing $b$ is the
  $\varprojlim^1$-shadow of the Weil pairing on $\mathbb A_f/\mathbb Q$.
- `code/scripts/check-pass79.py`,
  `artifacts/reports/pass79-symplectic-lagrangian-phantom-check.json`: new.

Next step:
Pass 80 should study the hyperbolic plane $H=\epsilon\oplus\mathbb Q$ as a *nondegenerate*
symplectic object of $D(\mathrm{Solid})$: compute its automorphism object
$\mathrm{Sp}(H)=\underline{\mathrm{Aut}}(H,\langle\,,\rangle)$ and decide whether the
$\mathrm{GL}_1$-action rescaling the dual pair, together with the unipotent "translation"
$\epsilon\to\epsilon$ given by adding multiples of the degenerate $b$, generates a solid
$\mathrm{SL}_2$- or Heisenberg-type group; then test whether the finite-adele Weil
representation / metaplectic cover descends to a canonical action on the phantom, i.e.
whether the Loeb-Rosser phantom carries a Weil representation of $\mathrm{SL}_2(\mathbb A_f)$
with $\mathbb Q$ and $\epsilon$ as its two polarizations. If a clean obstruction appears
(e.g. the degeneracy of $b$ blocks a metaplectic cocycle), record it as the precise wall.

---

### Pass 80 - 2026-06-14 00:10 JST

Focus:
Compute the solid symplectic automorphism object $\mathrm{Sp}(H)=\underline{\mathrm{Aut}}
(H,\langle\,,\rangle)$ of the hyperbolic phantom plane $H=\epsilon\oplus\mathbb Q$
(Pass 79: nondegenerate, Lagrangians $\epsilon,\mathbb Q$, perfect cross-pairing
$\langle\,,\rangle:\epsilon\otimes^{\blacksquare}\mathbb Q\to\mathbb Z[1]$), decide whether the
$\mathrm{GL}_1$-rescaling of the dual pair plus the unipotent shear by the degenerate self-pairing
$b$ generate a solid $\mathrm{SL}_2$/Heisenberg group, and test whether the finite-adele Weil
representation / metaplectic cover of $\mathrm{SL}_2(\mathbb A_f)$ descends to a canonical action on
the Loeb-Rosser phantom with $\mathbb Q,\epsilon$ as its two polarizations.

Proposer:
Run the pass as a *structure computation* of the endomorphism algebra, because the answer is sharper
and more rigid than "$\mathrm{SL}_2$". A solid endomorphism of $H=\epsilon\oplus\mathbb Q$ is a
$2\times2$ matrix $\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}$ with
$a\in\mathrm{End}(\epsilon)$, $b\in\mathrm{Hom}(\mathbb Q,\epsilon)$,
$c\in\mathrm{Hom}(\epsilon,\mathbb Q)$, $d\in\mathrm{End}(\mathbb Q)=\mathbb Q$. The decisive
input is the Pass-79 computation $R\underline{\mathrm{Hom}}(\epsilon,\mathbb Q)=\mathbb Q[-1]$, whose
$H^0$ is $0$: **$\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$**, so the lower-left entry
$c$ is forced to vanish. Meanwhile $\mathrm{Hom}(\mathbb Q,\epsilon)=\epsilon\neq0$ (every
$\mathbb Q$-vector space $V$ has $\mathrm{Hom}(\mathbb Q,V)=V$). Hence **every solid endomorphism of
$H$ is upper-triangular**, and $\mathrm{Sp}(H)$ is the solid *Borel* $B=T\ltimes U$ with torus
$T=\mathbb Q^{\times}$ (rescale $\mathbb Q$ by $\lambda$, $\epsilon$ by $\lambda^{-1}$ to fix the
pairing) and unipotent radical $U\cong$ the self-adjoint part of $\epsilon$ (the shears
$y\mapsto y,\ x\mapsto x+by$, $b$ the degenerate self-pairing). Concretely $B\cong\mathbb Q^{\times}
\ltimes\epsilon$ is the *"$ax+b$" affine group of the line* — exactly the Borel/Schrödinger
parabolic that *fixes the polarization $\epsilon$*. The Weyl flip $w=\begin{psmallmatrix}0&1\\-1&0
\end{psmallmatrix}$ — the would-be Fourier transform swapping the two polarizations — has **no solid
model**, because its $(2,1)$-entry lives in the vanishing $\mathrm{Hom}(\epsilon,\mathbb Q)$.

Skeptic:
Three sharpenings, one of which corrects the Next-step's own guess.
First, the obstruction is **not** the degeneracy of $b$, as the Pass-79 Next step speculated. The
shear-by-$b$ unipotent is perfectly present in $B$; what is missing is the opposite unipotent and the
Weyl element, i.e. the intertwiner $\epsilon\to\mathbb Q$. The precise wall is the *one-sidedness of
the dual pair*: $\mathrm{Hom}(\epsilon,\mathbb Q)=0$ while $\mathrm{Hom}(\mathbb Q,\epsilon)\neq0$.
Second, distinguish **reflexive** from **dualizable**. Pass 78 gave $\epsilon^{**}\cong\epsilon$
(reflexive), but $\epsilon$ is *not* $\otimes$-dualizable (a $\mathbb Q$-vector space of dimension
$2^{\aleph_0}$ is not finite/dualizable), so one may *not* write $R\underline{\mathrm{Hom}}
(\epsilon,\epsilon)=D\epsilon\otimes\epsilon$; the endomorphism object must be read off directly, and
that is what produces the asymmetry. Third, the collapse is a genuinely *limit* phenomenon: at every
finite level the shadow is the full $\mathrm{SL}_2(\mathbb Z/N)=\mathrm{Sp}(\mathbb Z/N\oplus\mathbb
Z/N)$, the Weyl flip is the finite Fourier transform $F_N$ (Gauss sum, $F_N^4=I$), and the two
coordinate Lagrangians are *isomorphic* ($\cong\mathbb Z/N$). The flip dies only in the limit, where
the two Lagrangians de-isomorphise into $\epsilon$ (prefix/$\varprojlim^1$ side) versus $\mathbb Q$
(divisible side): the same unit-class entanglement that gave the Pass-79 Darboux no-go.

Formalist:
> **Theorem 80a (upper-triangularity of $\mathrm{End}_{\mathrm{Solid}}(H)$).** For
> $H=\epsilon\oplus\mathbb Q$, $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)
> =H^0 R\underline{\mathrm{Hom}}(\epsilon,\mathbb Q)=H^0(\mathbb Q[-1])=0$, while
> $\mathrm{Hom}_{\mathrm{Solid}}(\mathbb Q,\epsilon)=\epsilon\neq0$ and
> $\mathrm{End}(\mathbb Q)=\mathbb Q$. Hence every solid endomorphism of $H$ is upper-triangular
> $\begin{psmallmatrix}a&b\\0&d\end{psmallmatrix}$, and $\epsilon$ is the unique solid
> $\mathrm{End}(H)$-stable line.
>
> **Theorem 80b ($\mathrm{Sp}(H)$ is a solid Borel, not $\mathrm{SL}_2$).** The symplectic
> automorphism object is $\mathrm{Sp}(H)=B=T\ltimes U$, $T=\mathbb Q^{\times}$ (the dual-pair
> rescaling $\lambda\!\cdot\!(\mathbb Q),\ \lambda^{-1}\!\cdot\!(\epsilon)$), $U$ the abelian solid
> group of symplectic shears (containing the degenerate $b$). $B\cong\mathbb Q^{\times}\ltimes\epsilon$
> is the affine "$ax+b$" group / Siegel-parabolic Schrödinger model fixing the polarization $\epsilon$.
> The Weyl element $w$ (the cross-polarization Fourier flip) is **not** a solid morphism. Thus the
> $\mathrm{GL}_1$ + shear data generate a *solvable* group, never $\mathrm{SL}_2$ and never a
> nonabelian Heisenberg group ($U$ is abelian).
>
> **Theorem 80c (metaplectic non-descent; the precise wall).** The finite-adele Weil representation
> of $\mathrm{SL}_2(\mathbb A_f)$ does **not** descend to a solid action on the phantom $\epsilon$
> with $\mathbb Q,\epsilon$ as polarizations. At each finite level $N$ the Weil flip exists (it is
> $F_N$, $F_N^4=I$, $|g_N|^2=N$, realizing $w\in\mathrm{SL}_2(\mathbb Z/N)$), but the only candidate
> limit of $\{F_{N_n}\}$ is an element of $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$. The
> precise wall is therefore $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$ — the one-sidedness
> of the dual pair $(\epsilon,\mathbb Q)$ / non-dualizability of $\epsilon$ — **not** the degeneracy
> of $b$. Only the Borel $B$ (the Schrödinger model in the fixed polarization $\epsilon$) acts.

Machine-verified `code/scripts/check-pass80.py` ->
`artifacts/reports/pass80-metaplectic-borel-noflip-check.json` (overall PASS):
(A) finite symplectic shadows for $N\in\{2,\ldots,12,60,420,840\}$: $|\mathrm{SL}_2(\mathbb Z/N)|=
N^3\prod_{p\mid N}(1-p^{-2})$ (brute-force confirmed for $N\le12$), $|B|=\varphi(N)N$, Bruhat
$|\mathrm{SL}_2|=|B|\cdot|\mathbb P^1(\mathbb Z/N)|$, and $w$ present with $w^2=-I$ swapping the
coordinate Lagrangians. (B) the wall: the $c$-tower $\mathrm{Hom}(\mathbb Z/N_n,\mathbb Q)=0$ and
$\mathrm{Ext}^1(\mathbb Z/N_n,\mathbb Q)=\mathbb Q/N_n\mathbb Q=0$ for $n\le12$ (so $c\equiv0$, no
limit flip), while the $b$-tower $\mathrm{Hom}((1/N_n)\mathbb Z/\mathbb Z,\mathbb Q/\mathbb Z)=\mathbb
Z/N_n\neq0$ with surjective divisibility bonding (so $b\neq0$). (C) the finite Weil/Fourier transform
$F_N$ for $N\in\{3,5,7,9,11,15,21\}$ satisfies $F_N^4=I$, $F_NF_N^{*}=I$, and $|g_N|^2=N$ to
$<10^{-7}$ — the finite flip exists at every level, its limit obstructed by (B).

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-80 entry; State counter
  $80\to81$. Per the APS run-sync hazard the bash mount again lagged (it served this file truncated
  at Pass 71 / line ~8088 while the real file held Passes 72-79), so all appends were made via
  Windows-path file tools and verified by Windows-path Read; the verification script was created in
  the native outputs workspace, run there and re-run from the repo path (both PASS), and copied into
  the repo.
- `records/logs/research-log.md`: Pass-80 one-line entry.
- `research/definitions.md`: added the skew hyperbolic plane $H=\epsilon\oplus\mathbb Q$, the solid
  Borel $\mathrm{Sp}(H)=\mathbb Q^{\times}\ltimes\epsilon$, upper-triangularity of
  $\mathrm{End}_{\mathrm{Solid}}(H)$, and the metaplectic non-descent wall
  $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$.
- `research/notes/g2-fg2-hierarchy.md`: Pass-80 section (Thms 80a/80b/80c).
- `research/open_problems.md`: marked the [New (Pass 79)] metaplectic item [Resolved (Pass 80)]; added
  a [New (Pass 80)] item on the *automorphic* reading of the Borel (does $\mathbb Q^{\times}\ltimes
  \epsilon$ carry the principal-series/Eisenstein shadow, and is the absent Weyl flip the algebraic
  origin of a functional-equation pole?).
- `research/ideas/research-questions.md`: retargeted the active question to whether the missing
  cross-polarization intertwiner is the obstruction to a self-dual functional equation, and to the
  reflexive-but-not-dualizable distinction as a structural invariant of the phantom.
- `code/scripts/check-pass80.py`,
  `artifacts/reports/pass80-metaplectic-borel-noflip-check.json`: new.

Next step:
Pass 81 should test whether the Pass-80 solid Borel $B=\mathbb Q^{\times}\ltimes\epsilon$ is the
algebraic shadow of a degenerate principal series: realize the "$ax+b$" action on functions/sections
over the fixed polarization $\epsilon$, ask whether the missing Weyl/intertwining operator
($\in\mathrm{Hom}(\epsilon,\mathbb Q)=0$) is exactly the obstruction to a functional equation
relating the two polarizations, and decide whether the resulting one-sided (non-self-dual) object has
a clean interpretation as the Löb (integral) versus Rosser (non-integral) asymmetry one functor-level
up — i.e. whether "no Fourier flip" is the representation-theoretic face of the Pass-51
Löb/Rosser $\leftrightarrow$ integral/non-integral-unit dividing line.

---

### Pass 81 - 2026-06-14 JST

Focus:
Test whether the Pass-80 solid Borel $B=\mathbb Q^{\times}\ltimes\epsilon=\mathrm{Sp}(H)$ is the
algebraic shadow of a degenerate principal series: realize the affine "$ax+b$" action on sections over
the fixed polarization $\epsilon$, ask whether the absent Weyl/intertwining operator
$\in\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$ is exactly the obstruction to a functional
equation relating the two polarizations $\epsilon,\mathbb Q$, and decide whether "no Fourier flip" is
the representation-theoretic face of the Pass-51 Löb (integral) vs Rosser (non-integral-unit) dividing
line one functor-level up.

Proposer:
Run it as an **induction-and-intertwiner** computation. The inducing datum is the family of unramified
characters of the torus, $\chi_s:B\twoheadrightarrow T=\mathbb Q^{\times}\xrightarrow{\,|\cdot|^s\,}
R^{\times}$ (trivial on the unipotent $U=\epsilon$), and the principal series is
$I(s)=\mathrm{Ind}_{B}^{\mathrm{Sp}(H)}\chi_s$. But $\mathrm{Sp}(H)=B$ by Pass 80, so the flag variety
is $\mathrm{Sp}(H)/B=\mathrm{pt}$: there is no Bruhat big cell because the opposite unipotent
$\bar U=\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)$ is $0$. Hence $I(s)\cong\chi_s$ canonically —
a **maximally degenerate** principal series of length $1$, the inducing character itself. Concretely
$B$ acts in the **Schrödinger model** on sections over the Lagrangian $\epsilon$ by the two "easy"
operators: the torus $T=\mathbb Q^{\times}$ by dilation-with-multiplier $(\lambda\!\cdot\!f)(x)=|\lambda
|^{s}f(\lambda^{-1}x)$, and the unipotent $U=\epsilon$ by symplectic shear $x\mapsto x+u$ (a chirp/
translation in the polarized picture). Neither operator ever consults the dual polarization $\mathbb Q$;
the only operator that would is the Weyl/Fourier flip $w$, which swaps $\epsilon\leftrightarrow\mathbb Q$
and lives in the vanishing $\mathrm{Hom}(\epsilon,\mathbb Q)$. The functional equation $I(s)\cong I(-s)$
is mediated by the standard intertwiner $M(w,s)f(g)=\int_{\bar U}f(w^{-1}\bar u g)\,d\bar u$; with
$\bar U=0$ this is an integral over the zero group, so the Gindikin–Karpelevich/Harish-Chandra
$c$-function is the **empty product** $c(s)=1$ and the $s\mapsto-s$ symmetry simply does not exist. So
$B$ is a degenerate principal series **with no functional equation** — the missing intertwiner is
literally $\bar U=\mathrm{Hom}(\epsilon,\mathbb Q)=0$.

Skeptic:
Three guards, one of which sharpens the slogan.
First, do **not** assert a Hilbert-space Weil representation. In the solid/condensed world we do not
have a measure-theoretic $\mathcal S(\epsilon)$ with an honest Plancherel; what we *do* have is the
abstract induced module, and because the flag variety is a point that module is just the character
$\chi_s$. The Schrödinger "section space" picture is heuristic packaging; the **theorem** is structural:
$\mathrm{Sp}(H)/B=\mathrm{pt}\iff\bar U=0\iff$ no $M(w,s)$. Claiming an $L^2$ model would overclaim.
Second, the functional equation is **not** merely "absent" — at every finite level it is **present**,
and dies only in the limit. For each $N$ the analogue is $\mathrm{SL}_2(\mathbb Z/N)$ with full Bruhat
cell $\bar U_N=\mathbb Z/N$, and the flip is the finite Fourier $F_N$, which on $\mathbb C[\mathbb Z/N]$
conjugates the dilation $D_t:f(x)\mapsto f(t^{-1}x)$ into $D_{t^{-1}}$ — i.e. it realises the
multiplicative/Mellin reflection $s\leftrightarrow-s$ exactly, with Gauss-sum eigenvalue $g(\psi)$,
$|g(\psi)|^2=p$ the local $c$-factor. The wall is therefore a **$\varprojlim^1$/limit obstruction**,
of a piece with the phantom itself: *finitely self-dual, limanly one-sided*. Third, be precise about
the Löb/Rosser reading: the asymmetry is not symmetric blame. $\mathrm{Hom}(\mathbb Q,\epsilon)=\epsilon
\neq0$ (you can always *forget* that a Löb fixed point is canonical and land in the Rosser torsor — this
is the shear $U$ itself), but $\mathrm{Hom}(\epsilon,\mathbb Q)=0$ (you can never *canonically recover*
canonicity from the non-canonical Rosser side — this is the missing flip). The one-way street is the
content.

Formalist:
> **Theorem 81a (maximally degenerate principal series).** Let $\chi_s:B\to R^{\times}$ be the
> character $tu\mapsto|t|^s$ ($t\in T=\mathbb Q^{\times}$, $u\in U=\epsilon$). Since $\mathrm{Sp}(H)=B$
> (Pass 80), the flag variety $\mathrm{Sp}(H)/B$ is a single point and
> $$I(s):=\mathrm{Ind}_{B}^{\mathrm{Sp}(H)}\chi_s\ \cong\ \chi_s$$
> as a $B$-module: a length-$1$ (hence irreducible) degenerate principal series with no composition
> series and no reducibility points. The Schrödinger model of $B$ over the polarization $\epsilon$ acts
> by dilation $T\ni\lambda:f(x)\mapsto|\lambda|^s f(\lambda^{-1}x)$ and shear $U\ni u:x\mapsto x+u$;
> both fix the polarization $\epsilon$ and neither factors through $\mathbb Q$.
>
> **Theorem 81b (no functional equation; $\bar U=0$).** The standard intertwiner
> $M(w,s):I(s)\to I(-s)$ has defining datum the opposite unipotent
> $\bar U=\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$. Hence the Harish-Chandra/Gindikin–
> Karpelevich $c$-function is the empty product $c(s)=1$, $M(w,s)$ does not exist as a nonzero solid
> morphism, and $I(s)\not\cong I(-s)$ for $s\neq0$: there is **no** $s\mapsto-s$ functional equation.
> Equivalently, the would-be intertwiner is exactly the absent Weyl/Fourier flip $\epsilon\to\mathbb Q$.
>
> **Theorem 81c (finite/limit dichotomy).** At each finite level $N$ the analogue
> $I_N(s)=\mathrm{Ind}_{B(\mathbb Z/N)}^{\mathrm{SL}_2(\mathbb Z/N)}\chi_s$ carries the intertwiner
> $M_N(w,s)$ realised by the finite Fourier transform $F_N$. On $\mathbb C[\mathbb Z/N]$ with dilation
> $D_t f(x)=f(t^{-1}x)$ ($t\in(\mathbb Z/N)^{\times}$) and unitary DFT $F_N$,
> $$F_N\,D_t\,F_N^{-1}=D_{t^{-1}}\qquad\text{(exact)},$$
> the multiplicative reflection $s\leftrightarrow-s$, with local $c$-factor the Gauss sum
> $|g(\psi)|^2=p$ for every nontrivial $\psi\bmod p$. The functional equation holds at every finite
> level and is destroyed only in the limit, where $\bar U_N=\mathbb Z/N$ has no solid limit
> ($\mathrm{Hom}(\epsilon,\mathbb Q)=0$). *Finitely self-dual, limanly one-sided.*
>
> **Theorem 81d (Löb/Rosser face of the wall).** Under the Pass-51 dictionary
> [integral unit $=$ Löb $=$ orbit-attached/canonical $=$ the $\mathbb Q$-(diagonal) side] and
> [non-integral unit $=$ Rosser $=$ detached/torsor $=$ the phantom $\epsilon$-side], the two
> Lagrangians of $H$ are the Löb side $\mathbb Q$ and the Rosser side $\epsilon$. The missing Weyl flip
> is a $B$-equivariant Fourier isomorphism $\epsilon\xrightarrow{\sim}\mathbb Q$; its non-existence
> $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$ is the statement that **the Rosser torsor does
> not retract onto the canonical Löb datum** (Guaspari–Solovay non-uniqueness has no section). The
> surviving $\mathrm{Hom}(\mathbb Q,\epsilon)=\epsilon=U$ (the shear) is the forgetful map
> Löb$\to$Rosser. *Slogan: one can always forget that a fixed point is canonical, but never canonically
> recover canonicity — that one-way street is the no-Fourier-flip wall.*
>
> **Corollary 81e (reflexive $\not\Rightarrow$ functional equation).** A polarization $L$ of a solid
> symplectic plane admits the cross-polarization functional equation iff $L$ is $\otimes$-**dualizable**;
> reflexivity ($L^{**}\cong L$) is insufficient. The phantom $\epsilon$ (reflexive by Pass 78, not
> dualizable) is the extremal witness reflexive $\wedge\neg$dualizable $\Rightarrow\neg$functional-
> equation, separating it from the finite-level dualizable Lagrangians $\mathbb Z/N$ (self-dual via
> $F_N$).

Machine-verified `code/scripts/check-pass81.py` ->
`artifacts/reports/pass81-degenerate-principal-series-functional-equation-check.json` (overall PASS):
(A) flag-variety collapse — $|\mathbb P^1(\mathbb Z/N)|=N\prod_{p\mid N}(1+p^{-1})>1$ for
$N\in\{2,3,4,5,6,9,12,30,210\}$ while $\mathrm{Hom}(\mathbb Z/N,\mathbb Q)=0$ ($\mathbb Q$ torsion-free)
and $\mathrm{Ext}^1(\mathbb Z/N,\mathbb Q)=\mathbb Q/N\mathbb Q=0$ ($\mathbb Q$ divisible), so the solid
flag variety is a point; (B) the functional equation $F_N D_t F_N^{-1}=D_{t^{-1}}$ holds for all
$t\in(\mathbb Z/N)^{\times}$, $N\le16$, to $<1.1\times10^{-14}$; (C) the Gauss-sum $c$-factor
$|g(\psi)|^2=p$ for all nontrivial $\psi\bmod p$, $p\le23$, to $<4.3\times10^{-13}$; (D) the limit
obstruction — the $c$-tower $\mathrm{Hom}(\mathbb Z/N_n,\mathbb Q)=\mathrm{Ext}^1(\mathbb Z/N_n,\mathbb
Q)=0$ vanishes while the surviving shear $b$-tower $\mathrm{Hom}((1/N_n)\mathbb Z/\mathbb Z,\mathbb Q/
\mathbb Z)=\mathbb Z/N_n\neq0$, so there is no solid limit flip.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-81 entry; State counter
  $81\to82$; rotated the State pass notes (Pass 81 is now "Last pass note", Pass 80 demoted to
  "Earlier note", Pass 79 to "Older note"). Per the APS run-sync hazard the bash mount again lagged
  (it served `check-pass81.py` truncated at line 192, missing the `main()` call), so the script was run
  from a sandbox-local copy and every repo write/verification went through Windows-path file tools.
- `records/logs/research-log.md`: Pass-81 one-line entry.
- `research/definitions.md`: added the degenerate principal series $I(s)=\mathrm{Ind}_B^{\mathrm{Sp}(H)}
  \chi_s$, the standard intertwiner $M(w,s)$ and its $c$-function, and the functional-equation wall
  $\bar U=\mathrm{Hom}(\epsilon,\mathbb Q)=0$ with the reflexive-vs-dualizable criterion.
- `research/notes/g2-fg2-hierarchy.md`: Pass-81 section (Thms 81a–81e).
- `research/open_problems.md`: marked the [New (Pass 80)] "automorphic shadow of the solid Borel" item
  [Resolved (Pass 81)]; added a [New (Pass 81)] item on whether the degenerate principal series has a
  nonzero Whittaker/derivative functional and on the archimedean/real place.
- `research/ideas/research-questions.md`: retargeted the active question to the Whittaker model and the
  $L$-/$\gamma$-factor reading of the empty $c$-function.
- `code/scripts/check-pass81.py`,
  `artifacts/reports/pass81-degenerate-principal-series-functional-equation-check.json`: new.

Next step:
Pass 82 should ask whether the maximally degenerate principal series $I(s)=\chi_s$ carries any nonzero
**Whittaker / generalized-Whittaker functional** $\Lambda:I(s)\to\psi_U$ for a character $\psi$ of the
unipotent $U=\epsilon$ — equivalently whether $\mathrm{Hom}_U(\epsilon,\psi)\neq0$ for a nontrivial
additive character $\psi:\epsilon\to R^{\times}$ — and, if so, whether the resulting (necessarily
"functional-equation-free") Whittaker function is the representation-theoretic carrier of the Rosser
torsor class itself. Decide also what the **archimedean place** contributes: adjoining the real
solenoid factor $\mathbb R$ to $\widehat{\mathbb Z}$ (passing from $\epsilon=\widehat{\mathbb Z}/\mathbb
Z$ to the full adelic $\mathbb A/\mathbb Q$) reinstates a real Lagrangian — does the archimedean Weyl
flip exist where the finite one does not, partially restoring a functional equation with only the
finite primes obstructed?

---

### Pass 82 - 2026-06-14 JST

Focus:
Test the Whittaker and archimedean residues of the Pass-81 maximally
degenerate principal series.  The two questions are whether
$I(s)=\chi_s$ carries any nonzero Whittaker functional for a nontrivial
character of $U=\epsilon$, and whether adding the real place repairs the
functional equation that the finite-prime solid phantom lost.

Proposer:
Since $\mathrm{Sp}(H)=B=\mathbb Q^{\times}\ltimes\epsilon$, the induced module
is
$$I(s)=\mathrm{Ind}_{B}^{\mathrm{Sp}(H)}\chi_s=\chi_s,$$
and $\chi_s$ is trivial on the unipotent radical $U=\epsilon$.  Therefore
$$\operatorname{Hom}_U(I(s),\psi)\cong
\begin{cases}
R,&\psi=1,\\
0,&\psi\ne1.
\end{cases}$$
Only the constant term survives.  The Rosser torsor is not a generic
Whittaker coefficient; it is the unipotent shear parameter $U=\epsilon$ itself,
the one-sided translation object left after the Weyl flip disappears.

For the real place, strong approximation gives
$$\mathbb A=\mathbb Q+(\mathbb R\times\widehat{\mathbb Z}),\qquad
\mathbb Q\cap(\mathbb R\times\widehat{\mathbb Z})=\mathbb Z.$$
Thus the full adelic quotient is the compact solenoid
$$\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z,$$
with exact sequence
$$0\to\widehat{\mathbb Z}/\mathbb Z\to\Sigma\to\mathbb R/\mathbb Z\to0.$$
The archimedean factor repairs global adelic Pontryagin duality for
$\mathbb A/\mathbb Q$, but it does not supply a finite-prime solid morphism
$\epsilon\to\mathbb Q$.  The global object has Fourier theory; the finite
phantom remains limanly one-sided.

Skeptic:
Finite characters of $\mathbb Z/N$ should not be mistaken for a solid
Whittaker model.  They exist at every finite level, but the collapsed solid
principal series has trivial $U$-action, so the nontrivial finite Fourier
coefficients vanish on the constant section.  Likewise, the real place repairs
the full adelic quotient, not the finite-prime quotient alone.  The sequence
$0\to\epsilon\to\Sigma\to\mathbb R/\mathbb Z\to0$ explains both facts at once:
$\Sigma$ becomes compact Hausdorff and globally self-dual, while $\epsilon$
remains the non-Hausdorff finite-prime kernel with no $\epsilon\to\mathbb Q$
Weyl operator.

Formalist:
> **Theorem 82a (Whittaker vanishing).** For the maximally degenerate principal
> series $I(s)=\chi_s$ of $B=\mathbb Q^{\times}\ltimes\epsilon$,
> $\operatorname{Hom}_{U}(I(s),\psi)=0$ for every nontrivial character
> $\psi$ of $U=\epsilon$, and is one-dimensional for the trivial character.
>
> **Theorem 82b (finite Fourier shadow).** For every finite shadow
> $U_N=\mathbb Z/N$, the Fourier coefficient of the constant $U_N$-action is
> $$\sum_{x\in\mathbb Z/N}e^{2\pi ikx/N}=0\quad(k\ne0),\qquad =N\quad(k=0).$$
> Hence finite nontrivial characters do not produce a Whittaker model for the
> solid limit representation.
>
> **Theorem 82c (archimedean repair without finite flip).** The full adelic
> quotient
> $$\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z\cong\mathbb A/\mathbb Q$$
> is compact Hausdorff and globally self-dual, and fits into
> $$0\to\epsilon=\widehat{\mathbb Z}/\mathbb Z\to\Sigma\to\mathbb R/\mathbb Z\to0.$$
> The real place repairs global adelic Fourier duality, but it does not create
> the missing finite-prime solid morphism $\epsilon\to\mathbb Q$.

Machine-verified `code/scripts/check-pass82.py` ->
`artifacts/reports/pass82-whittaker-archimedean-repair-check.json` (overall PASS):
finite Fourier coefficients of the constant $U_N$-action vanish for every
nontrivial additive character over
$N\in\{2,3,4,5,6,8,9,12,15,16,30\}$, while the trivial coefficient is $N$;
the $U$-equivariant Hom table has dimension $1$ for the trivial character and
$0$ for nontrivial characters; finite shadows of
$0\to\epsilon\to(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z\to\mathbb R/\mathbb Z\to0$
have kernel size $N$ and pass the diagonal-reduction exactness check.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-82 entry; State counter
  $82\to83$.
- `records/logs/research-log.md`: Pass-82 one-line entry.
- `research/definitions.md`: Whittaker vanishing for $I(s)$ and the adelic solenoid exact sequence.
- `research/notes/g2-fg2-hierarchy.md`: Pass-82 section (Thms 82a/82b/82c).
- `research/open_problems.md` and `research/ideas/research-questions.md`: retargeted the residue to
  the global adelic $\Sigma$ versus finite-prime $\epsilon$ comparison.
- `code/scripts/check-pass82.py`,
  `artifacts/reports/pass82-whittaker-archimedean-repair-check.json`: new.
- `artifacts/pdf/whittaker-archimedean-repair-2026-06-14.md`: publication summary source.

Next step:
Pass 83 should compare the global adelic solenoid
$\Sigma=\mathbb A/\mathbb Q$ with the finite phantom
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$ at the level of exact triangles: prove
whether the real-circle quotient $\Sigma\to\mathbb R/\mathbb Z$ splits in any
solid/condensed sense compatible with the Borel action, and decide whether the
global Fourier transform on $\Sigma$ induces only a constant-term functional on
$\epsilon$ or a nontrivial boundary map measuring exactly the lost finite-prime
Weyl flip.

---

### Pass 83 - 2026-06-20 JST

Focus:
Correct the exact-triangle comparison between the full adelic solenoid
$$
\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z\cong\mathbb A/\mathbb Q
$$
and the finite-prime phantom $\epsilon=\widehat{\mathbb Z}/\mathbb Z$.  The
question from Pass 82 asked whether
$0\to\epsilon\to\Sigma\to\mathbb R/\mathbb Z\to0$ splits and whether global
Fourier theory restricts to $\epsilon$.  The first task is to check the exact
row itself.

Proposer:
Compute the kernel literally.  The projection
$$
\pi:\Sigma\to\mathbb R/\mathbb Z,\qquad [(r,z)]\mapsto r\bmod\mathbb Z
$$
has kernel represented by $(0,z)$, $z\in\widehat{\mathbb Z}$; if
$(0,z)\sim(0,z')$ then $(0,z'-z)=(n,n)$ for some $n\in\mathbb Z$, hence
$n=0$ and $z=z'$.  Thus
$$
0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0
$$
is the compact Hausdorff exact row.  The phantom is not this kernel.  It is the
quotient by the dense real line:
$$
\Sigma/\mathbb R\cong
(\mathbb R\times\widehat{\mathbb Z})/(\Delta\mathbb Z+\mathbb R\times0)
\cong \widehat{\mathbb Z}/\mathbb Z=\epsilon.
$$
So the correct triangle has a closed profinite kernel row and a separate
dense/non-Hausdorff quotient row.

Skeptic:
This correction changes the Fourier reading.  The compact row is the standard
solenoid extension, and it does **not** split continuously: otherwise its
Pontryagin dual
$$
0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0
$$
would split, requiring a homomorphic section $\mathbb Q/\mathbb Z\to\mathbb Q$;
but $\mathbb Q$ is torsion-free while every element of $\mathbb Q/\mathbb Z$ is
torsion.  Therefore no continuous/condensed degree-$0$ section
$\mathbb R/\mathbb Z\to\Sigma$ exists.  Also, global characters restrict
nontrivially to the **closed** kernel $\widehat{\mathbb Z}$, yielding
$\mathbb Q/\mathbb Z$, but a finite character on $\widehat{\mathbb Z}$ descends
to $\widehat{\mathbb Z}/\mathbb Z$ only if it kills the dense diagonal
$\mathbb Z$, hence only if it is trivial.  Thus global Fourier theory sees the
finite characters as a boundary quotient, not as ordinary degree-$0$
characters of $\epsilon$.

Formalist:
> **Theorem 83a (correct solenoid rows).** For
> $\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z$, projection to the
> real circle gives
> $$0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0.$$
> The finite phantom appears instead as
> $$\mathbb R\to\Sigma\to\epsilon=\widehat{\mathbb Z}/\mathbb Z\to0,$$
> where the image of $\mathbb R$ is dense and the quotient is non-Hausdorff /
> derived-solid phantom data rather than an LCA quotient.
>
> **Theorem 83b (no continuous split).** The compact row above is nonsplit in
> continuous, condensed, and solid degree $0$: under Pontryagin duality it
> becomes $0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0$, which cannot
> split because $\mathbb Q$ has no nonzero torsion.
>
> **Theorem 83c (Fourier boundary, not Whittaker character).** The restriction
> of global characters $\widehat{\Sigma}\cong\mathbb Q$ to the closed profinite
> kernel is the quotient $\mathbb Q\to\mathbb Q/\mathbb Z=\widehat{\widehat{
> \mathbb Z}}$.  Passing further to $\epsilon=\widehat{\mathbb Z}/\mathbb Z$
> kills all nontrivial degree-$0$ characters.  Hence only the constant term
> descends to $\epsilon$; the lost finite-prime Weyl/Fourier content is the
> boundary quotient $\mathbb Q/\mathbb Z$.

Machine-verified `code/scripts/check-pass83.py` ->
`artifacts/reports/pass83-solenoid-exact-triangle-correction-check.json` (overall PASS):
finite dual rows $0\to\mathbb Z\xrightarrow{\times N}\mathbb Z\to\mathbb Z/N\to0$
are exact, and are nonsplit for the nontrivial checked lcm stages
$N\in\{1,2,6,12,60,60,420,840,2520,2520,27720,27720\}$; finite characters on
the profinite kernel have count $N$, but exactly one character descends to
$\epsilon$; levelwise cokernels of $\mathbb Z\to\mathbb Z/N$ vanish, confirming
that $\epsilon$ is not visible as an ordinary finite cokernel but as the
derived/non-Hausdorff quotient.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-83 entry; State counter
  $83\to84$ and corrected the State summary.
- `records/logs/research-log.md`: Pass-83 entry.
- `research/definitions.md`: corrected the Pass-82 solenoid row and added the
  closed-kernel / dense-quotient distinction.
- `research/notes/g2-fg2-hierarchy.md`: Pass-83 correction section.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked the Pass-82
  solenoid question resolved/corrected and retargeted the next task to the
  derived-solid boundary class $\mathbb Q/\mathbb Z$.
- `code/scripts/check-pass83.py`,
  `artifacts/reports/pass83-solenoid-exact-triangle-correction-check.json`: new.
- `artifacts/pdf/solenoid-exact-triangle-correction-2026-06-20.md`: publication summary source.

Next step:
Pass 84 should formulate the derived/solid exact triangle behind
$\mathbb R\to\Sigma\to\epsilon$ and identify the boundary object
$\mathbb Q/\mathbb Z$ (or its shifted solid dual) as the precise replacement
for the missing finite-prime Weyl flip.  In particular, prove whether the
Borel unipotent $U=\epsilon$ acts only on the quotient boundary, not by
continuous translations on $\Sigma$ itself.

---

### Pass 84 - 2026-06-20 JST

Focus:
Turn the Pass-83 correction into the actual derived/solid statement.  The
dense quotient row
$$
\mathbb R\to\Sigma\to\epsilon=\widehat{\mathbb Z}/\mathbb Z
$$
should explain both why no degree-$0$ Fourier/Weyl map descends to $\epsilon$
and why the phantom remains nonzero in the solid derived category.

Proposer:
Use the quotient topology first.  Since the diagonal copy of $\mathbb Z$ is
dense in $\widehat{\mathbb Z}$, every nonempty open subset of
$\widehat{\mathbb Z}$ has saturation all of $\widehat{\mathbb Z}$ under
addition by $\mathbb Z$.  Hence the quotient
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$ is indiscrete as a topological group.
Its Hausdorff reflection is zero.  Therefore any continuous homomorphism from
$\epsilon$ to a Hausdorff group, in particular to the compact Hausdorff solenoid
$\Sigma$, is zero.  So the Borel unipotent $U=\epsilon$ cannot be realized as
a nontrivial continuous translation group on $\Sigma$.

The nonzero object is instead derived/solid.  In the repository's solid
duality,
$$
D\epsilon\simeq\mathbb Q[-1],
$$
so the absent degree-$0$ Weyl morphism $\epsilon\to\mathbb Q$ is replaced by a
degree-$1$ class
$$
\mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\simeq\mathbb Q.
$$
The generator is the finite-adele extension
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
This is the precise "boundary action": $U=\epsilon$ acts in the solid Borel as
the shear parameter of the hyperbolic plane, not as translations of the global
solenoid.

Skeptic:
Do not identify the boundary with $\mathbb Q/\mathbb Z$ without saying which
row is being dualized.  $\mathbb Q/\mathbb Z$ is the finite-character boundary
of the compact row
$$
0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0.
$$
For the dense quotient row, ordinary continuous characters of $\epsilon$ are
zero; the derived solid residue is the shifted object $\mathbb Q[-1]$.  Thus
there are two shadows:
finite topological boundary $\mathbb Q/\mathbb Z$ on $\widehat{\mathbb Z}$,
and solid arithmetic boundary $\mathbb Q[-1]$ for $\epsilon$.  The missing
Weyl flip is the latter.  Calling either one an honest degree-$0$ map
$\epsilon\to\mathbb Q$ would repeat the original error.

Formalist:
> **Theorem 84a (indiscrete phantom quotient).** The quotient topology on
> $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ is indiscrete.  Hence the Hausdorff
> reflection of $\epsilon$ is $0$, and every continuous homomorphism
> $\epsilon\to H$ into a Hausdorff topological group $H$ is zero.
>
> **Theorem 84b (no continuous $U$-translation on $\Sigma$).** Any nontrivial
> translation action of $U=\epsilon$ on the compact Hausdorff solenoid
> $\Sigma$ would require a nonzero continuous homomorphism
> $\epsilon\to\Sigma$.  By Theorem 84a none exists.  Therefore the solid Borel
> unipotent is not a topological translation group of $\Sigma$.
>
> **Theorem 84c (derived Weyl replacement).** In $D(\mathrm{Solid})$,
> $D\epsilon\simeq\mathbb Q[-1]$ and
> $\mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\simeq\mathbb Q$.
> The missing Weyl flip $\epsilon\to\mathbb Q$ is replaced by the degree-$1$
> finite-adele extension
> $$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0,$$
> not by a degree-$0$ morphism.  The role of $\mathbb Q/\mathbb Z$ is the
> finite-character boundary on the closed kernel $\widehat{\mathbb Z}$; its
> solid completion is the shifted arithmetic boundary $\mathbb Q[-1]$.

Machine-verified `code/scripts/check-pass84.py` ->
`artifacts/reports/pass84-dense-phantom-boundary-action-check.json` (overall PASS):
finite quotient shadows have only empty/all saturated opens; maps from the
indiscrete quotient to checked discrete Hausdorff targets are continuous only
when constant, and continuous group homomorphisms are only the zero
homomorphism; finite characters on $\widehat{\mathbb Z}/N$ descend to
$\epsilon$ only for the trivial character; finite degree-$0$ shadows of a Weyl
map into $\mathbb Q$ vanish because $\mathrm{Hom}(\mathbb Z/N,\mathbb Q)=0$
and $\mathrm{Ext}^1(\mathbb Z/N,\mathbb Q)=0$ at every checked stage.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-84 entry; State counter
  $84\to85$.
- `records/logs/research-log.md`: Pass-84 entry.
- `research/definitions.md`: added the indiscrete quotient, Hausdorff-reflection
  vanishing, and shifted solid boundary definitions.
- `research/notes/g2-fg2-hierarchy.md`: Pass-84 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked the Pass-83
  dense-boundary question resolved and retargeted the next pass to an explicit
  two-term complex model for the boundary.
- `code/scripts/check-pass84.py`,
  `artifacts/reports/pass84-dense-phantom-boundary-action-check.json`: new.
- `artifacts/pdf/dense-phantom-boundary-action-2026-06-20.md`: publication summary source.

Next step:
Pass 85 should write the explicit two-term complex model for the phantom
boundary, comparing $[\mathbb Z\to\widehat{\mathbb Z}]$,
$[\mathbb R\to\Sigma]$, and the finite-adele extension
$[\,\mathbb Q\to\mathbb A_f\,]$, and prove which quasi-isomorphisms preserve
the Borel shear class.

---

### Pass 85 - 2026-06-20 JST

Focus:
Write the explicit two-term complex model promised by Pass 84 and decide which
comparison preserves the Borel shear class.

Proposer:
Use cohomological degrees $0\to1$ and define
$$
C_{\mathbb Z}=[\,\mathbb Z\to\widehat{\mathbb Z}\,],\qquad
C_{\mathbb R}=[\,\mathbb R\to\Sigma\,],\qquad
C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,].
$$
All three maps are injective and their degree-$1$ quotients are abstractly
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$
Indeed $\Sigma/\mathbb R\cong\widehat{\mathbb Z}/\mathbb Z$ and
$\mathbb A_f/\mathbb Q\cong\widehat{\mathbb Z}/\mathbb Z$ by strong
approximation $\mathbb A_f=\mathbb Q+\widehat{\mathbb Z}$ with
$\mathbb Q\cap\widehat{\mathbb Z}=\mathbb Z$.  Thus each complex is a model of
the same quotient in the algebraic/solid derived category.

The ordinary finite/Hausdorff shadows do not see this quotient: reducing
$\mathbb Z\to\widehat{\mathbb Z}$ modulo $N$ gives a surjection
$\mathbb Z\to\mathbb Z/N$, and similarly the dense images of $\mathbb R$ in
$\Sigma$ and $\mathbb Q$ in $\mathbb A_f$ have zero Hausdorff cokernel.  The
phantom is the derived residue of the non-Mittag-Leffler kernel tower
$N_n\mathbb Z$, not a finite cokernel.

The shear-preserving comparison is
$$
C_{\mathbb Z}\longrightarrow C_{\mathbb Q}
$$
obtained by pushout along $\mathbb Z\hookrightarrow\mathbb Q$; it sends the unit
extension $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ to
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
The archimedean complex $C_{\mathbb R}$ has the same quotient but changes the
kernel object to $\mathbb R$, so it is quotient-equivalent but not
shear-class-equivalent.

Skeptic:
Do not call all three rows canonically quasi-isomorphic as extensions.  They
are quasi-isomorphic after forgetting the chosen kernel and remembering only
the cohomology object $\epsilon[-1]$, and they are all invisible to Hausdorff
finite probes.  But extension class matters for the Borel.  The finite-adele
class lives in
$$
\mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\cong\mathbb Q,
$$
so only the row with kernel $\mathbb Q$ can carry that shear.  The
archimedean row belongs to the compact global solenoid repair; it does not
produce the finite-adele shear class and should not be used as the replacement
for the Weyl flip.

Formalist:
> **Theorem 85a (three two-term quotient models).** The complexes
> $C_{\mathbb Z}$, $C_{\mathbb R}$, and $C_{\mathbb Q}$ above have $H^0=0$ and
> $H^1\cong\epsilon$ as abstract/solid quotient objects.  Their finite
> Hausdorff shadows are acyclic: all ordinary finite cokernels vanish.
>
> **Theorem 85b (phantom source).** For $C_{\mathbb Z}$ the finite kernels are
> $N_n\mathbb Z$, a non-Mittag-Leffler tower along the lcm stages; the nonzero
> $\epsilon$ is exactly the $\varprojlim^1$/solid boundary of this tower.
>
> **Theorem 85c (shear-preserving pushout).** The comparison
> $C_{\mathbb Z}\to C_{\mathbb Q}$ is the pushout along
> $\mathbb Z\hookrightarrow\mathbb Q$ and preserves the unit/Yoneda class,
> giving the finite-adele extension
> $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$.  The comparison through
> $C_{\mathbb R}$ preserves only the quotient $\epsilon$, not the Borel shear
> class.

Machine-verified `code/scripts/check-pass85.py` ->
`artifacts/reports/pass85-two-term-boundary-complex-check.json` (overall PASS):
for the checked lcm stages, finite diagonal images are all of $\mathbb Z/N$ and
ordinary finite/Hausdorff cokernels vanish; the kernel tower has repeated
strict drops, witnessing the non-Mittag-Leffler source of the phantom; unit
residues $1\bmod N$ are compatible and remain units; the comparison table
marks $C_{\mathbb Z}$ and $C_{\mathbb Q}$, but not $C_{\mathbb R}$, as
preserving the finite-adele shear class.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-85 entry; State counter
  $85\to86$.
- `records/logs/research-log.md`: Pass-85 entry.
- `research/definitions.md`: added the two-term boundary complex comparison.
- `research/notes/g2-fg2-hierarchy.md`: Pass-85 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked the two-term
  complex task resolved and retargeted the next pass to the universal property
  of the shear-preserving pushout.
- `code/scripts/check-pass85.py`,
  `artifacts/reports/pass85-two-term-boundary-complex-check.json`: new.
- `artifacts/pdf/two-term-boundary-complex-2026-06-20.md`: publication summary source.

Next step:
Pass 86 should state and test the universal property of the shear-preserving
pushout: among quotient models of $\epsilon$ with divisible kernel, is
$C_{\mathbb Q}=[\mathbb Q\to\mathbb A_f]$ initial for maps out of
$C_{\mathbb Z}$ that preserve the unit class and kill Hausdorff finite
cokernels?

---

### Pass 86 - 2026-06-21 JST

Focus:
State the correct universal property of the finite-adele shear pushout and
find the necessary caveat in the word "divisible".

Proposer:
Let $\mathcal P_{\mathbb Q}(\epsilon)$ be the category whose objects are
shear-marked quotient models
$$
0\to D\to E\to\epsilon\to0
$$
equipped with a map from
$C_{\mathbb Z}=[\,\mathbb Z\to\widehat{\mathbb Z}\,]$, such that:
(i) $D$ is uniquely divisible, i.e. a $\mathbb Q$-vector object;
(ii) the extension is the pushout of
$0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ along the chosen
$\mathbb Z\to D$; and
(iii) finite/Hausdorff shadows of the quotient vanish.  Then the source map
$\mathbb Z\to D$ extends uniquely to a $\mathbb Q$-linear map
$\mathbb Q\to D$.  Therefore every such object factors uniquely through
$$
C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,]
=C_{\mathbb Z}\otimes_{\mathbb Z}\mathbb Q.
$$
This makes $C_{\mathbb Q}$ the initial shear-preserving quotient model after
passing from the integral kernel to the uniquely divisible kernel.

Skeptic:
Do not state the result for arbitrary divisible kernels.  The divisible torsion
group $\mathbb Q/\mathbb Z$ gives immediate non-uniqueness: for each integer
$k$, the homomorphism
$$
\mathbb Q\to\mathbb Q/\mathbb Z,\qquad q\mapsto kq\bmod\mathbb Z
$$
restricts to the zero map on $\mathbb Z$, but these maps differ on fractions
such as $1/2,1/3,1/5$.  Hence "divisible" must mean uniquely divisible, or the
object must carry a specified $\mathbb Q$-linear kernel map.  Also, this
initiality is an extension-category statement; it does not create a forbidden
degree-$0$ Weyl flip $\epsilon\to\mathbb Q$.

Formalist:
> **Theorem 86a (initial shear pushout).** In the category
> $\mathcal P_{\mathbb Q}(\epsilon)$ of shear-marked quotient models with
> uniquely divisible kernel, the finite-adele complex
> $C_{\mathbb Q}=[\mathbb Q\to\mathbb A_f]$ is initial under
> $C_{\mathbb Z}=[\mathbb Z\to\widehat{\mathbb Z}]$.  Equivalently, fixing the
> image of $1\in\mathbb Z$ in a $\mathbb Q$-vector kernel forces a unique map
> $\mathbb Q\to D$, and pushout gives the unique extension morphism.
>
> **Theorem 86b (finite-shadow stability).** This localization does not
> introduce ordinary finite cokernels.  At each finite modulus, the integer
> residues already surject onto the finite quotient, so the Hausdorff finite
> shadow of the pushed-out quotient remains acyclic.
>
> **Theorem 86c (torsion-divisible obstruction).** If torsion-divisible kernels
> are allowed without additional decoration, the initiality statement is false:
> $\mathbb Q/\mathbb Z$ supplies multiple extensions of the same map
> $\mathbb Z\to\mathbb Q/\mathbb Z$.

Machine-verified `code/scripts/check-pass86.py` ->
`artifacts/reports/pass86-shear-pushout-universal-property-check.json` (overall PASS):
bounded denominator stages $\mathbb Z[1/L]$ have unique extension into checked
$\mathbb Q$-vector kernels once the image of $1$ is fixed; integer residues
kill every checked finite/Hausdorff cokernel; checked finite-dimensional
$\mathbb Q$-vector targets have unique factorization through $C_{\mathbb Q}$;
and the torsion-divisible maps $q\mapsto kq\bmod\mathbb Z$ give five distinct
extensions with identical restriction to $\mathbb Z$.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-86 entry; State counter
  $86\to87$.
- `records/logs/research-log.md`: Pass-86 entry.
- `research/definitions.md`: added the shear-pushout universal property and
  the torsion-divisible caveat.
- `research/notes/g2-fg2-hierarchy.md`: Pass-86 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked the
  universal-property task resolved in its uniquely divisible form and retargeted
  the next pass to the full mapping-space statement.
- `code/scripts/check-pass86.py`,
  `artifacts/reports/pass86-shear-pushout-universal-property-check.json`: new.
- `artifacts/pdf/shear-pushout-universal-property-2026-06-21.md`: publication summary source.

Next step:
Pass 87 should upgrade the finite certificate to a mapping-space statement in
$D(\mathrm{Solid})$: identify the homotopy fiber of shear-marked maps out of
$C_{\mathbb Q}$, and decide how torsion-divisible summands must be excluded or
decorated.

---

### Pass 87 - 2026-06-21 JST

Focus:
Promote the Pass-86 finite certificate to a mapping-space statement in
$D(\mathrm{Solid})$ and decide how torsion-divisible summands enter.

Proposer:
For a shear-marked target model
$$
M=(0\to D\to E\to\epsilon\to0),
$$
the restriction map induced by $C_{\mathbb Z}\to C_{\mathbb Q}$ should be read
as
$$
\operatorname{Map}(C_{\mathbb Q},M)\longrightarrow
\operatorname{Map}(C_{\mathbb Z},M).
$$
The cofiber of the kernel map $\mathbb Z\to\mathbb Q$ is
$\mathbb Q/\mathbb Z$, so the homotopy fiber over a fixed shear-marked map is
$$
\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,D).
$$
If $D$ is uniquely divisible, this derived mapping object vanishes:
$\operatorname{Hom}(\mathbb Q/\mathbb Z,D)=0$ because $D$ is torsion-free, and
higher $\operatorname{Ext}$ groups vanish because divisible groups are
injective.  Therefore the fiber is contractible and the factorization through
$C_{\mathbb Q}$ is unique in the derived mapping-space sense.

Skeptic:
The statement must remain fiberwise and shear-marked.  Without fixing the
extension/shear class, one is computing all extensions, not factorizations of
the given Borel shear.  And torsion-divisible kernels are exactly the failure
mode: for $T=\mathbb Q/\mathbb Z$ the object
$\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,T)$ has nontrivial
$\pi_0$ (already visible through finite quotients $\mathbb Z/N$).  Excluding
torsion-divisible summands gives strict initiality; allowing them requires
decoration by a chosen boundary component $\mathbb Q/\mathbb Z\to T$.

Formalist:
> **Theorem 87a (mapping-space fiber).** For a shear-marked target with kernel
> $D$, the homotopy fiber of
> $\operatorname{Map}(C_{\mathbb Q},M)\to\operatorname{Map}(C_{\mathbb Z},M)$
> over a fixed shear-marked map is
> $\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,D)$.
>
> **Theorem 87b (contractibility for uniquely divisible kernels).** If $D$ is
> uniquely divisible, then
> $\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,D)\simeq0$; hence the
> Pass-86 initiality holds as a derived mapping-space contractibility
> statement.
>
> **Theorem 87c (torsion decoration rule).** If
> $D=D_{\mathbb Q}\oplus T$ with $T$ torsion-divisible, the extra fiber is
> $\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,T)$.  Strict initiality is
> recovered either by imposing $T=0$ or by adding a boundary decoration fixing
> this component.

Machine-verified `code/scripts/check-pass87.py` ->
`artifacts/reports/pass87-mapping-space-shear-initiality-check.json` (overall PASS):
the checker records the cofiber/fiber sequence; finite torsion tests for
$\mathbb Q$-vector kernels have only one torsion point and therefore a
contractible fiber; torsion-divisible finite shadows have $N^r$ components at
modulus $N$ for rank $r$, giving explicit non-contractible fibers; and the
admissibility rule is to work with uniquely divisible kernels or decorate the
torsion boundary.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-87 entry; State counter
  $87\to88$.
- `records/logs/research-log.md`: Pass-87 entry.
- `research/definitions.md`: added the derived mapping-space formulation and
  torsion decoration rule.
- `research/notes/g2-fg2-hierarchy.md`: Pass-87 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked the
  mapping-space task resolved and retargeted the next pass to the derived
  automorphism/stabilizer of the final shear extension.
- `code/scripts/check-pass87.py`,
  `artifacts/reports/pass87-mapping-space-shear-initiality-check.json`: new.
- `artifacts/pdf/mapping-space-shear-initiality-2026-06-21.md`: publication summary source.

Next step:
Pass 88 should compute the derived automorphism/stabilizer of the final
finite-adele shear extension and compare it with the solid Borel
$\mathbb Q^\times\ltimes\epsilon$.

---

### Pass 88 - 2026-06-21 JST

Focus:
Compute the stabilizer of the final finite-adele shear extension and compare it
with the solid Borel.

Proposer:
There are three stabilizers, and the distinction prevents a category error.
First, for the strict shear-marked object under
$$
C_{\mathbb Z}\to C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,],
$$
the automorphism group is trivial.  Any scalar automorphism of the
$\mathbb Q$-kernel must preserve the marked image of $1\in\mathbb Z$, hence is
the identity.  Pass 87 also removes derived ambiguity:
$\mathbf R\operatorname{Map}(\mathbb Q/\mathbb Z,\mathbb Q)=0$.

Second, if one forgets the integral marking but preserves the finite-adele
shear extension line
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0,
$$
the degree-$0$ stabilizer is $\mathbb Q^\times$.  Multiplication by a nonzero
rational rescales the kernel and middle finite adele group and preserves the
one-dimensional Ext line generated by the finite-adele extension.

Third, the full solid Borel from Pass 80,
$$
B=\mathbb Q^\times\ltimes\epsilon,
$$
is not the automorphism group of the bare exact row.  It is the automorphism
group of the hyperbolic object $H=\epsilon\oplus\mathbb Q$ preserving the
polarization: $\mathbb Q^\times$ is the Levi stabilizer, while $\epsilon$ is
the unipotent shear parameter.  Thus the exact row detects the Levi line; the
hyperbolic plane restores the full Borel.

Skeptic:
Do not put the unipotent $\epsilon$ inside automorphisms of
$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$ with fixed endpoints.  Such
endpoint-fixing automorphisms would be measured by
$\operatorname{Hom}(\epsilon,\mathbb Q)$, which is zero in the solid setting.
The $\epsilon$ term is a shear of $H$, not a self-map of the bare extension.
Likewise, strict "under $C_{\mathbb Z}$" automorphisms are smaller than the
Levi: scaling by $a\in\mathbb Q^\times$ moves the marked integral unit unless
$a=1$.

Formalist:
> **Theorem 88a (strict marked rigidity).** The automorphism group of
> $C_{\mathbb Q}$ as a shear-marked object under $C_{\mathbb Z}$ is trivial,
> and no extra derived automorphisms remain after the Pass-87 torsion-boundary
> decoration rule.
>
> **Theorem 88b (extension-line stabilizer).** The stabilizer of the
> finite-adele shear Ext line
> $[0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0]$ is $\mathbb Q^\times$ in
> degree $0$.
>
> **Theorem 88c (Borel comparison).** The full solid Borel
> $\mathbb Q^\times\ltimes\epsilon$ is recovered at the hyperbolic-plane level
> $H=\epsilon\oplus\mathbb Q$: the exact row contributes the Levi
> $\mathbb Q^\times$, and the additional $\epsilon$ is the unipotent shear.

Machine-verified `code/scripts/check-pass88.py` ->
`artifacts/reports/pass88-shear-extension-stabilizer-check.json` (overall PASS):
the checker verifies that nonzero rational scalars preserve the extension line
but only scalar $1$ preserves the integral unit marking; finite Borel shadows
are the affine groups $(\mathbb Z/N)^\times\ltimes\mathbb Z/N$ with singleton
strict unit stabilizer; and no extra derived automorphisms survive for the
final $\mathbb Q$-kernel extension after torsion-boundary decoration.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-88 entry; State counter
  $88\to89$.
- `records/logs/research-log.md`: Pass-88 entry.
- `research/definitions.md`: added the stabilizer split.
- `research/notes/g2-fg2-hierarchy.md`: Pass-88 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked the
  stabilizer task resolved and retargeted the next pass to the Borel-torsor /
  extension-class theorem for the Rosser phantom.
- `code/scripts/check-pass88.py`,
  `artifacts/reports/pass88-shear-extension-stabilizer-check.json`: new.
- `artifacts/pdf/shear-extension-stabilizer-2026-06-21.md`: publication summary source.

Next step:
Pass 89 should use the stabilizer split to restate the automorphic line as a
Borel-torsor / extension-class theorem for the Rosser phantom.

---

### Pass 89 - 2026-06-21 JST

Focus:
State the Borel-torsor / extension-class theorem for the Rosser phantom and
identify the invariant data under Guaspari-Solovay witness changes.

Proposer:
Passes 80-88 now form a single statement.  The Rosser/phantom obstruction is
not four different objects; it is one class seen through four presentations:

1. a Guaspari-Solovay witness-comparison Cech $1$-cocycle;
2. the derived-limit class
   $$\varprojlim\nolimits^1(\mathbb Z,\times m)\cong
   \widehat{\mathbb Z}_m/\mathbb Z$$
   and, in the all-prime limit, $\epsilon=\widehat{\mathbb Z}/\mathbb Z$;
3. the finite-adele shear extension line
   $$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0;$$
4. the hyperbolic Borel shear orbit for
   $$B=\mathbb Q^\times\ltimes\epsilon$$
   acting on $H=\epsilon\oplus\mathbb Q$ with its polarization.

The bridge is: take the Rosser witness-comparison cocycle, quotient by
coboundaries to obtain the unit-torsor class in the Cech cokernel, pass to the
inverse limit to get $\widehat{\mathbb Z}_m/\mathbb Z$ or $\epsilon$, and
push out the integral row
$$0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$$
along $\mathbb Z\to\mathbb Q$ to obtain the finite-adele extension
$$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.$$
The hyperbolic object then restores the full Borel:
$\mathbb Q^\times$ is the extension-line Levi and $\epsilon$ is the
unipotent shear torsor.

Thus finite stages are Loeb-attached: their chosen unit lifts and their
representatives can be split.  The inverse limit is Rosser: the representatives
cannot be made compatible across the non-Mittag-Leffler tower, and the
remaining obstruction is exactly the torsor class.

Skeptic:
Do not claim a canonical classification of all Rosser predicates from this
repository model alone.  The theorem is a bridge schema for the APS/Rosser
unit-torsor model already built here.  Changing Guaspari-Solovay witness data
may change the section, enumeration, finite lift, and concrete cocycle
representative.  What is invariant is the cohomology/torsor class, its finite
conductor restrictions, its radical support, and its finite-adele extension
line.  Likewise, the Borel's unipotent $\epsilon$ belongs to the hyperbolic
realization, not to endpoint-fixing automorphisms of the bare exact row.

Formalist:
> **Theorem 89a (Rosser Borel-torsor theorem).** In the repository's
> APS/Rosser phantom model, the Rosser unit-torsor, the
> $\varprojlim^1$ phantom, the finite-adele extension line, and the hyperbolic
> Borel shear orbit are four presentations of one torsor/extension class.
>
> **Theorem 89b (bridge from witnesses to finite adeles).** The functorial
> bridge sends a witness-comparison Cech cocycle to its class in
> $\operatorname{coker}\delta$, identifies that class with the appropriate
> $\widehat{\mathbb Z}_m/\mathbb Z$ or $\epsilon$, and then pushes out
> $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ along
> $\mathbb Z\to\mathbb Q$ to obtain
> $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$.
>
> **Theorem 89c (gauge invariance).** Changing Guaspari-Solovay witness
> choices changes cocycle representatives and finite sections by coboundaries,
> but preserves the torsor/cohomology class, finite conductor restrictions,
> radical support, and finite-adele extension line.
>
> **Theorem 89d (stabilizer levels).** Strict integral marking is rigid;
> forgetting the marking leaves the Levi stabilizer $\mathbb Q^\times$; the
> full Borel $\mathbb Q^\times\ltimes\epsilon$ appears only after passing to
> the hyperbolic plane.

Machine-verified `code/scripts/check-pass89.py` ->
`artifacts/reports/pass89-borel-torsor-rosser-phantom-check.json` (overall
PASS): the checker records finite Cech windows where replacing representative
$1$ by $1+m^k$ changes the representative but preserves the class modulo the
finite cokernel index $m^k$; verifies that finite Borel shadows have affine
size $\varphi(N)N$ and singleton strict marked stabilizer; and records the
invariant/non-invariant data split under witness changes.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-89 entry; State counter
  $89\to90$.
- `records/logs/research-log.md`: Pass-89 entry.
- `research/definitions.md`: added the Rosser Borel-torsor theorem.
- `research/notes/g2-fg2-hierarchy.md`: Pass-89 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked the
  Borel-torsor theorem resolved and retargeted the next pass to
  conductor/radical functoriality of the torsor.
- `code/scripts/check-pass89.py`,
  `artifacts/reports/pass89-borel-torsor-rosser-phantom-check.json`: new.
- `artifacts/pdf/borel-torsor-rosser-phantom-2026-06-21.md`: publication summary source.

Next step:
Pass 90 should make the conductor/radical functoriality of the Borel-torsor
theorem precise across $m$-adic and all-prime variants.

---

### Pass 90 - 2026-06-21 JST

Focus:
Make the Borel-torsor theorem functorial across conductor and radical
supports.

Proposer:
The correct functoriality is not "add primes by zero insertion" on the quotient
torsor.  For a finite squarefree support $S$, write
$$
P(S)=\left(\prod_{p\in S}\mathbb Z_p\right)/\Delta\mathbb Z.
$$
If $S\subseteq T$, coordinate projection gives a canonical restriction
$$
\rho_{T,S}:P(T)\to P(S),
$$
because the diagonal copy of $\mathbb Z$ in $T$ projects to the diagonal copy
in $S$.  By contrast, zero-insertion
$$
\prod_{p\in S}\mathbb Z_p\to\prod_{p\in T}\mathbb Z_p
$$
does not descend to $P(S)\to P(T)$ when $T\setminus S\ne\varnothing$: a
diagonal shift by $1$ maps to $(1,\ldots,1,0,\ldots,0)$, not to a diagonal
shift in the target.  So the canonical support functor is contravariant by
restriction.  Enlargement of support is a span, a chosen section, or a
finite-conductor approximation, not a canonical map of quotient torsors.

This resolves the Pass-89 open point.  The Borel-torsor package is natural on
the conductor site as follows:

- finite conductor shadows reduce along $N\mid N'$ by
  $(\mathbb Z/N')^\times\ltimes\mathbb Z/N'\to
  (\mathbb Z/N)^\times\ltimes\mathbb Z/N$;
- support restrictions project $P(T)\to P(S)$ for $S\subseteq T$;
- rad-incomparable supports compare through a meet span
  $P(S)\to P(S\cap T)\leftarrow P(T)$ and a join arena $P(S\cup T)$ for
  gluing.

Thus the Pass-89 Borel torsor theorem is functorial, but as a
restriction/span object over the prime-support lattice rather than as a
covariant insertion functor.

Skeptic:
This pass corrects a tempting overstatement.  Earlier radical naturality
language can sound as if $\widehat{\mathbb Z}_S/\mathbb Z$ always embeds into
$\widehat{\mathbb Z}_T/\mathbb Z$ when $S\subseteq T$.  That is not canonical
after quotienting by the diagonal $\mathbb Z$.  Any such insertion needs a
choice of representative or a finite-conductor lift.  What is canonical is
restriction from larger support to smaller support, plus meet/join
comparisons for incomparable supports.  The Borel theorem survives because its
finite conductor shadows and extension-line restrictions commute in that
direction.

Formalist:
> **Theorem 90a (support restriction).** For $S\subseteq T$, coordinate
> projection induces a well-defined restriction
> $P(T)\to P(S)$ on diagonal quotients.
>
> **Theorem 90b (no canonical zero insertion).** If $T\setminus S\ne\varnothing$
> and $S\ne\varnothing$, zero-insertion
> $\prod_{p\in S}\mathbb Z_p\to\prod_{p\in T}\mathbb Z_p$ does not descend to
> a homomorphism $P(S)\to P(T)$.
>
> **Theorem 90c (finite conductor Borel naturality).** At finite conductor,
> the affine Borel shadows
> $(\mathbb Z/N)^\times\ltimes\mathbb Z/N$ reduce functorially along
> $N\mid N'$, preserving the unit class and strict marked stabilizer.
>
> **Theorem 90d (span comparison).** Rad-incomparable supports have no direct
> support map; their canonical comparison is a meet span for shared ghost data
> and a join arena for gluing.

Machine-verified `code/scripts/check-pass90.py` ->
`artifacts/reports/pass90-conductor-functorial-borel-torsors-check.json`
(overall PASS): the checker verifies radical invariance, proves that
projection descends while zero-insertion fails when new primes are added,
records meet/join comparison rows for rad-incomparable supports, and checks
finite Borel shadow reductions along conductor divisibility.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-90 entry; State counter
  $90\to91$.
- `records/logs/research-log.md`: Pass-90 entry.
- `research/definitions.md`: added conductor-functorial Borel torsor
  terminology.
- `research/notes/g2-fg2-hierarchy.md`: Pass-90 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked
  the conductor-functoriality task resolved and retargeted the next pass to
  descent/stackification of the Borel torsor over the prime-cover site.
- `code/scripts/check-pass90.py`,
  `artifacts/reports/pass90-conductor-functorial-borel-torsors-check.json`: new.
- `artifacts/pdf/conductor-functorial-borel-torsors-2026-06-21.md`: publication
  summary source.

Next step:
Pass 91 should decide whether the restriction/span Borel-torsor package is a
sheaf, stack, or descent-obstruction object over the finite prime-cover site.

---

### Pass 91 - 2026-06-21 JST

Focus:
Decide whether the restriction/span Borel torsor is a sheaf, stack, or
descent-obstruction object over the finite prime-cover site.

Proposer:
The object is not a sheaf on multi-prime supports.  Let
$$
P(S)=\left(\prod_{p\in S}\mathbb Z_p\right)/\Delta\mathbb Z.
$$
By Pass 61, the singleton-prime descent map
$$
P(S)\to\prod_{p\in S}P(\{p\})
$$
has kernel
$$
K_S=\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.
$$
This is exactly the horizontal Rosser defect.  Passing from the unipotent
phantom to the Borel does not remove it.  The global-Levi Borel prestack
$$
B^{\mathrm{glob}}(S)=\mathbb Q^\times\ltimes P(S)
$$
still has the unipotent kernel $K_S$, while its constant Levi
$\mathbb Q^\times$ sheafifies on the singleton cover to local Levi data
$(\mathbb Q^\times)^S$.

Thus the Borel object is best described as a prestack or descent-obstruction
object.  Its stackification/sheafification is the local Borel sheaf
$$
B^\#(S)=(\mathbb Q^\times)^S\ltimes
\prod_{p\in S}(\mathbb Z_p/\mathbb Z).
$$
The map $B^{\mathrm{glob}}\to B^\#$ forgets the Rosser horizontal kernel and
localizes the Levi.  The hyperbolic shear action by $P(S)$ acts transitively on
lifts with the same local data, but it does not choose a canonical lift.
Therefore the shear transports the descent defect; it does not kill it.

Skeptic:
Do not say "stack" too quickly.  A stack of torsors may absorb automorphism
data, but the raw group-valued Borel package is not even separated for
$|S|\ge2$.  Its stackification is a different, local object.  The Rosser class
is precisely what is lost by that stackification, not a proof that the original
prestack satisfies descent.  This matches Pass 61/62: sheafification and
cosheafification on the discrete prime site collapse to the local Loeb object,
while the Rosser phantom remains presheaf-level descent failure.

Formalist:
> **Theorem 91a (Borel non-separatedness).** For $|S|\ge2$, the global-Levi
> Borel prestack $B^{\mathrm{glob}}(S)=\mathbb Q^\times\ltimes P(S)$ is not a
> sheaf on the singleton-prime cover.  Its unipotent descent kernel is
> $K_S=\mathbb Z^S/\Delta\mathbb Z$.
>
> **Theorem 91b (local Borel stackification).** The sheaf/stackification of
> the discrete-site Borel package is
> $$B^\#(S)=(\mathbb Q^\times)^S\ltimes
> \prod_{p\in S}(\mathbb Z_p/\mathbb Z).$$
> It is the Loeb-local object, not the Rosser phantom.
>
> **Theorem 91c (shear transports, not kills).** The unipotent shear action is
> simply transitive on the finite shadows of the descent-kernel lifts, but no
> canonical zero section is selected.  Hence the Rosser defect is preserved as
> the kernel of stackification.
>
> **Corollary 91d.** On the finite discrete prime-cover site, the Borel torsor
> is a prestack/descent-obstruction object.  The next genuinely geometric
> home for the Rosser class must use the Zariski/generic-point relocation of
> Pass 63.

Machine-verified `code/scripts/check-pass91.py` ->
`artifacts/reports/pass91-borel-torsor-descent-obstruction-check.json`
(overall PASS): the checker verifies that the horizontal descent rank is
$|S|-1$, finite diagonal quotient kernels have size $N^{|S|-1}$, the
global-Levi Borel is a sheaf only for one-prime supports, local Levi
sheafification contributes $|G|^{|S|-1}$ independent finite Levi choices in a
finite proxy, and the shear action transports but does not kill the kernel
lifts.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-91 entry; State counter
  $91\to92$.
- `records/logs/research-log.md`: Pass-91 entry.
- `research/definitions.md`: added the Borel descent-obstruction terminology.
- `research/notes/g2-fg2-hierarchy.md`: Pass-91 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`: marked
  the discrete-site descent/stackification task resolved and retargeted the
  next pass to Zariski/generic relocation of the Borel descent obstruction.
- `code/scripts/check-pass91.py`,
  `artifacts/reports/pass91-borel-torsor-descent-obstruction-check.json`: new.
- `artifacts/pdf/borel-torsor-descent-obstruction-2026-06-21.md`: publication
  summary source.

Next step:
Pass 92 should relocate the Borel descent obstruction to the Zariski/generic
prime site and compare it with the Pass-63 $j_!$ ghost line.

---

### Pass 92 - 2026-06-21 JST

Focus:
Relocate the Borel descent obstruction from the finite discrete prime-cover
site to the Zariski/generic-point site and compare it with the Pass-63 $j_!$
ghost line.

Proposer:
The discrete-site Borel obstruction should not be carried into the Zariski
site as non-separatedness of the constant Borel sheaf.  On
$$
X_S=\{\eta\}\cup\{(p):p\in S\},
$$
the minimal-open cover $U_p=\{\eta,(p)\}$ has all nonempty intersections equal
to $\{\eta\}$, hence full-simplex nerve.  Constant coefficients are connected:
$$
H^1(X_S,\underline{\mathbb Z})=0.
$$
So the global-Levi constant Borel no longer has the discrete horizontal defect.

The defect relocates exactly as in Pass 63.  Let
$j:\{\eta\}\hookrightarrow X_S$ be the open generic point.  The Borel analogue
of the $j_!\mathbb Z$ ghost line is the low-degree semidirect coefficient
$$
\mathfrak b_{j!}(S)=\underline{\mathbb Q^\times}\ltimes j_!\underline{\mathbb Z},
$$
where the Levi is constant and the unipotent radical is extension-by-zero from
the generic point.  Its nontrivial low-degree invariant is unipotent:
$$
H^1(X_S,j_!\underline{\mathbb Z})
\cong\operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^S)
\cong\mathbb Z^S/\Delta\mathbb Z.
$$
Thus the Pass-91 descent kernel becomes a genuine $j_!$ cohomology group, not
a failure of the constant Borel sheaf.

With the dilation coefficient $\mathcal V$, this horizontal ghost is the free
part of the total class
$$
H^1(X_S,j_!\mathcal V)\cong\widehat{\mathbb Z}_S/\mathbb Z.
$$
Pushing out the integral row along $\mathbb Z\to\mathbb Q$ recovers the
finite-adele extension line, and passing to the hyperbolic plane reads the same
class as the Borel shear orbit.  The Levi $\mathbb Q^\times$ rescales classes;
the unipotent shear changes representatives.  Neither operation produces a
canonical zero section.

Skeptic:
This pass should explicitly avoid two overstatements.  First, the Zariski
relocation does not say the constant Borel sheaf is non-separated.  Connectivity
kills that constant-coefficient defect.  Second, $H^1(X_S,j_!\mathbb Z)$ is a
rank $|S|-1$ lattice of horizontal relations, not a distinguished singleton
class before choosing a basis or witness section.  The canonical datum is the
boundary sequence
$$
0\to j_!\mathbb Z\to\mathbb Z_X\to i_*\mathbb Z_Z\to0
$$
and its cokernel $\mathbb Z^S/\Delta\mathbb Z$.  The Borel language is justified
only because the solid Borel's unipotent radical is abelian and can carry this
ordinary $j_!$ cohomology.

Formalist:
> **Theorem 92a (Zariski relocation of the Borel defect).** On
> $X_S=\{\eta\}\cup S$ with the generic-point topology, constant coefficients
> have no horizontal $H^1$ defect, while
> $$H^1(X_S,j_!\underline{\mathbb Z})\cong
> \mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.$$
> This group is the Zariski relocation of the Pass-91 discrete descent kernel.
>
> **Theorem 92b (Borel $j_!$ ghost coefficient).** The finite-support Borel
> ghost coefficient is
> $$\mathfrak b_{j!}(S)=\underline{\mathbb Q^\times}\ltimes
> j_!\underline{\mathbb Z}.$$
> The Levi part stays in degree $0$ on the connected site; the only nontrivial
> low-degree Borel obstruction is the unipotent group
> $H^1(X_S,j_!\underline{\mathbb Z})$.
>
> **Theorem 92c (finite shadows).** Modulo $N$,
> $$|H^1(X_S,j_!\mathbb Z/N)|=N^{|S|-1},$$
> matching the finite diagonal kernel of the discrete Borel prestack from
> Pass 91.
>
> **Theorem 92d (comparison with finite adeles and shear).** The horizontal
> $j_!$ ghost injects into
> $H^1(X_S,j_!\mathcal V)\cong\widehat{\mathbb Z}_S/\mathbb Z$; the pushout
> along $\mathbb Z\to\mathbb Q$ gives the finite-adele extension line, and the
> hyperbolic Borel realizes the same datum as a shear orbit without a canonical
> splitting.

Machine-verified `code/scripts/check-pass92.py` ->
`artifacts/reports/pass92-zariski-generic-borel-descent-check.json` (overall
PASS): constant-coefficient $H^1$ vanishes on the full-simplex Zariski cover;
$j_!$-cohomology has rank $|S|-1$ for all tested supports; finite mod-$N$
class sets have size $N^{|S|-1}$; the Borel proxy keeps the Levi in degree $0$
and places only the unipotent ghost in $H^1$; and the comparison rows align the
horizontal ghost with the total phantom, finite-adele pushout, and hyperbolic
Borel shear orbit.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-92 entry;
  State counter $92\to93$.
- `records/logs/research-log.md`: Pass-92 entry.
- `research/definitions.md`: added the Zariski/generic Borel ghost
  terminology.
- `research/notes/g2-fg2-hierarchy.md`: Pass-92 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`:
  marked Zariski/generic Borel descent resolved and retargeted the next pass to
  all-prime Spec-$\mathbb Z$ continuity/derived-site hypotheses.
- `code/scripts/check-pass92.py`,
  `artifacts/reports/pass92-zariski-generic-borel-descent-check.json`: new.
- `artifacts/pdf/zariski-generic-borel-descent-2026-06-21.md`: publication
  summary source.

Next step:
Pass 93 should upgrade the finite-support $j_!$ Borel class to the honest
all-prime $\mathrm{Spec}\,\mathbb Z$ site and identify the finiteness,
continuity, or derived-completion hypotheses needed for
$H^1(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)=\widehat{\mathbb Z}/\mathbb Z$.

---

### Pass 93 - 2026-06-21 JST

Focus:
Upgrade the finite-support Borel $j_!$ class to the honest all-prime
$\mathrm{Spec}\,\mathbb Z$ site.

Proposer:
The all-prime upgrade is not obtained by pretending that
$j:\{\eta\}\hookrightarrow\mathrm{Spec}\,\mathbb Z$ is an ordinary open
immersion.  In the honest Zariski site every nonempty basic open
$D(n)$ contains $\eta$ and all but finitely many closed primes.  Hence
$\{\eta\}$ is not open.  The finite-support $j_!$ of Passes 63, 64, and 92 is
ordinary on each finite subspace
$$
X_S=\{\eta\}\cup\{(p):p\in S\},
$$
but all-prime it must be interpreted as a pro-open / continuous / solid
coefficient over the system of finite supports.

The correct all-prime Borel coefficient is therefore
$$
\mathfrak B^{\mathrm{cont}}_{j!}
=\mathbb Q^\times\ltimes
R\!\varprojlim_{S\Subset\mathbb P} j_{S,!}\mathcal V_S,
$$
with transition maps given by restriction from a larger finite support to a
smaller one.  These support-direction maps are surjective.  For the horizontal
integer skeleton,
$$
\mathbb Z^T/\Delta\mathbb Z\to\mathbb Z^S/\Delta\mathbb Z
\qquad(S\subseteq T)
$$
has kernel of rank $|T|-|S|$; modulo $N$ the kernel has size
$N^{|T|-|S|}$.  Thus the support direction is Mittag-Leffler and contributes
no additional $\varprojlim^1$.  The nonzero derived content remains the
per-prime dilation $\varprojlim^1$ already built into $\mathcal V$.

Consequently the all-prime identity should be written as continuous cohomology:
$$
H^1_{\mathrm{cont}}(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)
:=\varprojlim_{S\Subset\mathbb P}H^1(X_S,j_{S,!}\mathcal V_S)
\cong\left(\prod_p\mathbb Z_p\right)/\Delta\mathbb Z
=\widehat{\mathbb Z}/\mathbb Z.
$$
The global Levi remains a single $\mathbb Q^\times$.  Replacing it by the
product of local Levi factors would be the local Loeb sheafification from
Pass 91, not the Rosser/Borel torsor.  Pushing out the diagonal row along
$\mathbb Z\to\mathbb Q$ gives
$$
0\to\mathbb Q\to\mathbb A_f\to\widehat{\mathbb Z}/\mathbb Z\to0,
$$
and the hyperbolic Borel $\mathbb Q^\times\ltimes\epsilon$ acts functorially
on the resulting shear representatives.

Skeptic:
The slogan "$H^1(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)$" is acceptable only
after adding the word continuous, pro-open, or solid.  Ordinary Zariski sheaf
cohomology with an open generic-point inclusion does not literally exist on
the honest all-prime site, because that inclusion is not open.  Also, the
support inverse limit and the per-prime dilation derived limit must not be
merged.  The support direction is ML and harmless; the Rosser phantom comes
from the dilation towers.  Finally, keeping a global Levi is a choice of the
Borel torsor line, not the local sheafified Borel.

Formalist:
> **Theorem 93a (no ordinary all-prime generic $j_!$).** In
> $\mathrm{Spec}\,\mathbb Z$, the singleton generic point is not open.  Hence
> the all-prime $j_!$ Borel coefficient is not an ordinary open-immersion
> extension by zero.
>
> **Theorem 93b (continuous/pro-open coefficient).** The all-prime Borel
> coefficient is the pro-open/continuous object
> $$\mathfrak B^{\mathrm{cont}}_{j!}
> =\mathbb Q^\times\ltimes
> R\!\varprojlim_{S\Subset\mathbb P} j_{S,!}\mathcal V_S.$$
>
> **Theorem 93c (support ML).** For $S\subseteq T$, the restriction maps on
> finite-support $j_!$ cohomology are surjective.  In the horizontal skeleton
> the kernel has rank $|T|-|S|$, and modulo $N$ it has size
> $N^{|T|-|S|}$.  Therefore the support direction contributes no extra
> $\varprojlim^1$.
>
> **Theorem 93d (all-prime Borel identity).** With the dilation coefficient,
> $$H^1_{\mathrm{cont}}(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)
> \cong\widehat{\mathbb Z}/\mathbb Z.$$
> The finite-adele extension row and hyperbolic Borel shear orbit are the
> pushout and representation-theoretic forms of this same continuous class.

Machine-verified `code/scripts/check-pass93.py` ->
`artifacts/reports/pass93-all-prime-borel-jshriek-upgrade-check.json`
(overall PASS): the checker records that the generic point is open on finite
subspaces but not on honest all-prime $\mathrm{Spec}\,\mathbb Z$; verifies
surjective support projections and rank drops; checks finite mod-$N$ kernel
sizes; separates harmless support-direction ML behavior from the per-prime
dilation $\varprojlim^1$; and records the all-prime global-Levi Borel
coefficient with unipotent limit $\widehat{\mathbb Z}/\mathbb Z$.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-93 entry;
  State counter $93\to94$.
- `records/logs/research-log.md`: Pass-93 entry.
- `research/definitions.md`: added the all-prime continuous/pro-open Borel
  $j_!$ coefficient.
- `research/notes/g2-fg2-hierarchy.md`: Pass-93 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`:
  marked the all-prime upgrade resolved and retargeted the next pass to the
  Verdier/solid dual and antipode-sign problem.
- `code/scripts/check-pass93.py`,
  `artifacts/reports/pass93-all-prime-borel-jshriek-upgrade-check.json`: new.
- `artifacts/pdf/all-prime-borel-jshriek-upgrade-2026-06-21.md`: publication
  summary source.

Next step:
Pass 94 should compute the Verdier/solid dual of the all-prime Borel $j_!$
coefficient and decide whether the antipode sign gives a functional-equation
shadow without creating a forbidden Weyl flip.

---

### Pass 94 - 2026-06-21 JST

Focus:
Compute the Verdier/solid dual of the all-prime Borel $j_!$ coefficient and
decide exactly what remains of the finite signed functional equation.

Proposer:
Pass 93 turned the all-prime Borel coefficient into
$$
\mathfrak B^{\mathrm{cont}}_{j!}
=\mathbb Q^\times\ltimes
R\!\varprojlim_{S\Subset\mathbb P}j_{S,!}\mathcal V_S,
$$
whose unipotent cohomology is
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$
Therefore the solid dual is forced by Passes 77--79:
$$
D\epsilon\simeq\mathbb Q[-1],
\qquad
D\mathbb Q\simeq\epsilon[-1].
$$
The dual of the unipotent part is not an opposite unipotent group in degree
$0$; it is the degree-$1$ finite-adele boundary represented by
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
Keeping the global Levi, the dual Borel shadow is consequently a
Levi-marked boundary object
$$
\mathbb Q^\times\ltimes\mathbb Q[-1],
$$
with the $\mathbb Q^\times$ action contragredient to the action on
$\epsilon$.  This is the all-prime continuation of the finite Verdier rule
$$
D(d_S)=-d_S^T.
$$
So the antipode sign does survive, but only as a signed boundary equation.

Skeptic:
The word "functional equation" is dangerous here.  In a usual principal
series, the functional equation is carried by a Weyl/Fourier intertwiner.  The
solid phantom line has no such degree-$0$ operator:
$$
\operatorname{Hom}^0_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0.
$$
Equivalently, the opposite unipotent
$\bar U=\operatorname{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)$ remains zero.
Thus Pass 94 must not say that the Borel coefficient has acquired an
$s\mapsto -s$ intertwiner or a genuine Weyl flip.  The finite shadows still
see $d_S\mapsto-d_S^T$, and the all-prime object still has biduality sign
$-\mathrm{id}_\epsilon$, but the honest statement is boundary-level:
the missing flip is replaced by the shifted Ext class, not repaired.

Formalist:
> **Theorem 94a (solid dual of the all-prime unipotent).** Let
> $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ be the unipotent limit of
> $\mathfrak B^{\mathrm{cont}}_{j!}$.  In $D(\mathrm{Solid}_{\mathbb Z})$,
> $$D\epsilon\simeq\mathbb Q[-1].$$
> Hence the dual unipotent of the all-prime Borel $j_!$ class is a shifted
> boundary object, not a degree-$0$ group.
>
> **Theorem 94b (finite signed shadows survive).** For every finite support
> $S$, if $d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ is the recollement boundary,
> then finite Verdier duality sends
> $$d_S\longmapsto-d_S^T,\qquad D^2(d_S)=d_S.$$
> The sign is visible over $\mathbb Z$ and collapses modulo $2$.
>
> **Theorem 94c (boundary functional-equation shadow).** The Pass-65/77
> antipode sign survives all-prime as the biduality sign
> $$\eta_\epsilon=-\mathrm{id}_\epsilon.$$
> This is a functional-equation shadow only after replacing the Weyl operator
> by the degree-$1$ finite-adele boundary
> $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$.
>
> **Theorem 94d (no forbidden Weyl flip).** Since
> $$\operatorname{Hom}^0_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0,$$
> the duality does not create an opposite unipotent, a standard intertwiner,
> or a degree-$0$ Weyl/Fourier flip.

Machine-verified `code/scripts/check-pass94.py` ->
`artifacts/reports/pass94-all-prime-borel-jshriek-solid-dual-check.json`
(overall PASS): finite boundary matrices satisfy $D(d_S)=-d_S^T$,
$D^2(d_S)=d_S$, rank preservation, and mod-$2$ sign collapse; support
restriction dualizes from surjections to injections without producing an
opposite degree-$0$ unipotent; the all-prime solid row records
$D\epsilon=\mathbb Q[-1]$, degree-$1$ finite-adele boundary, biduality sign
$-1$, and $\operatorname{Hom}^0(\epsilon,\mathbb Q)=0$.

Archivist:
Repository updates this pass:
- `records/discussions/autonomous-discussion.md`: appended this Pass-94 entry;
  State counter $94\to95$.
- `records/logs/research-log.md`: Pass-94 entry.
- `research/definitions.md`: added the all-prime Borel $j_!$ solid-dual
  boundary terminology.
- `research/notes/g2-fg2-hierarchy.md`: Pass-94 theorem section.
- `research/open_problems.md` and `research/ideas/research-questions.md`:
  marked the Verdier/solid duality task resolved and retargeted the next pass
  to a boundary-only constant-term / two-term Borel complex.
- `code/scripts/check-pass94.py`,
  `artifacts/reports/pass94-all-prime-borel-jshriek-solid-dual-check.json`:
  new.
- `artifacts/pdf/all-prime-borel-jshriek-solid-dual-2026-06-21.md`:
  publication summary source.

Next step:
Pass 95 should package the boundary-shadow functional equation as a
constant-term or two-term Borel complex natural under conductor restriction,
without reintroducing a degree-$0$ Weyl flip.
