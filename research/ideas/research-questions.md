# Research Questions

## Active

- **(Pass 147 -> 148: `[New (Pass 147)]`.)** Pass 147 gave the explicit Kripke-Feferman
  `(Z,Z/2)` fixed point `kappa` (ungrounded=detached, `delta`-symmetric, Rosser-invisible;
  Thm 147a), the `Coh : B[Z] -> GLP` functor (degree = modality depth, `H^n(S^n)=Z` =
  strictness `<n> !~ <n+1>`, first limit at `n=1->2`; Thm 147b), and promoted Feferman
  path-dependence to a non-uniqueness theorem (Feferman-Spector 1962; Thm 147c). **Next
  (Pass 148):** (a) is the symmetric `(Z,Z/2)` signature realisable ALREADY in `ConLat_PA`,
  or does `delta`-symmetry provably force ascent to a truth-theoretic / reflection extension
  (KF ordinal `phi_{epsilon_0}(0)`)? Does a `Sigma_1`-definable proof well-ordering force
  every detached fixed point Rosser-orientable, making unoriented detachment intrinsically
  non-`Sigma_1`? Pin the `ConLat_T -> ConLat_{KF}` descent of `kappa`. (b) Promote `Coh` from
  a generator-level monoid map to a genuine monoidal functor with a specified source category,
  and construct the transfinite extension sending the first TRANSFINITE coherence stage to the
  first LIMIT modality `<omega>` of `GLP_Lambda` (Fernandez-Duque--Joosten), testing whether
  the `n=1` layer's regular-height-`mu` home matches `<omega>`'s proof-theoretic ordinal via
  the Feferman path torsor.

- **(Pass 140 -> 141: horn (a) DECIDED -- horn I refuted; the `cd = omega` diagonal
  is next.)** Pass 140 discharged `[New (Pass 139)]` prong (a). **Thm 140a:** horn I is
  REFUTED. The Mardešić–Prasolov system `A` is indexed by `(omega^omega, <=*)` with
  `cf = d >= b >= aleph_1` ALWAYS uncountable, so Goblot's threshold `cf-rank + 2` is
  `>= 3` in every ZFC model and NEVER forces `lim^{>=2}A = 0`; the graph-nerve
  `cd(A)<=1` and the Goblot cofinality-rank are decoupled (Thm 136c), and only the
  latter governs `lim^*A`. **Reconciliation of the flagged 135a-vs-136c tension:** the
  `A` naming collision is the whole illusion -- Thm 135a's "`cd<=1 => lim^{>=2}A=0`
  IDENTICALLY" is correct for the genuinely 1-dimensional *twin nerve* (a nice
  finite/countable-cofinality index), whereas Horn I illegitimately transfers that
  identical vanishing to the *MP system indexed over `omega^omega`* (uncountable
  cofinality), where Goblot leaves `lim^1, lim^2` open; Thm 136c's independence is
  exactly the assertion that this transfer fails. **Cor 140b:** hence `(forall n)h_n`
  is strictly stronger than `h_1` (not redundant); the LITERAL separator is
  inconsistent (König overshoot to `aleph_{omega+1}`), the CORRECTED separator
  `Con(h_1 ^ lim^2 A^{(a),2} != 0)` consistent. **Cor 140c:** home
  `MA_{aleph_1}+2^{aleph_0}=aleph_2`; `lim^2 A^{(a),2}!=0` by the BLH-ceiling
  CONTRAPOSITIVE (`h_2 => c>=aleph_3`, `c=aleph_2`), NOT Goblot; `cd=2` ZFC-absolute
  (Thm 136b recert). **Rem 140d:** `lim^n A` = derived-limit avatar of `nFG2(n)`; the
  uncountable non-well-founded index makes the Goblot truncation depth UNBOUNDED --
  the set-theoretic antipode of Thm 41a's finite depth-2 self-truncation. Machine
  `check-pass140.py` overall PASS. **Next (Pass 141):** `[New (Pass 140)]` prong (a),
  the `cd = omega` diagonal -- does the strict `cd`-graded tower `{A^{(a),k}}` admit a
  diagonal `A^{(a),omega}` of infinite cohomological dimension whose `lim^*` is a
  genuine `nFG2(omega)` transfinite phantom, or does an `S^infty`-contractibility
  analogue re-truncate it? In passing, discharge Cor 140c(i): does `MA_{aleph_1}`
  alone (vs PFA) force `lim^1 A = 0` at `c = aleph_2`?

- **(Pass 135 -> 136: the 2-cd BBMT separator consistency, the `cd`-vs-`cf` grading, and the
  exotic-ordering `Sigma_1`-induction.)**  Pass 135 executed the Pass-134 successor, prong (ii)
  primary, with a structural non-transfer theorem and a correction of the Pass-134 simplicial
  heuristic.  **Thm 135a (cohomological-dimension non-transfer):** the retract-transfer that
  trivialized `n=1` (Thm 133c/134e) has NO analogue at `n=2` for a reason PRIOR to any set theory
  -- the distinguished twin tower `A` is a 1-dimensional coherence datum (`cd(A) <= 1`), so
  `varprojlim^{>=2} A = 0` IDENTICALLY and `h_2(A)` is VACUOUS; since `cd(A^{(a),2}) = 2`, no
  coherence retraction of the 2-obstruction onto the tower exists.  **Correction 135b:** the
  Pass-134 "two 2-simplices sharing a vertex" model of `A^{(a),2}` is CONTRACTIBLE (all reduced
  `Betti_{F_3} = 0`) and hosts no 2-class; the honest obstruction is 2-spherical
  (`H_2(S^2; F_a) = F_a`), the no-retraction `Delta^{n+1} -> S^n` degree-UNIFORM -- the asymmetry
  is carried entirely by `cd(A)`.  **Thm 135c:** strictness reduces to
  `Con((forall n)h_n(A) ^ varprojlim^2 A^{(a),2} != 0)`, a concrete 2-cd instance of the OPEN
  BBMT additivity, non-vacuous (CH-consistent).  **Thm 135d:** the `cf`-spectrum
  `aleph_0<aleph_1<aleph_2<...` is `cd`-graded; its `cd=0`/`aleph_0` FLOOR is the Pass-55
  `G2 ^ ¬FG2` solenoid `hatZ_a/Z` (Prufer-rigid).  Machine `check-pass135.py` PASS (exact `F_3`
  homology).  Next (Pass 136): (i) decide the residual consistency
  `Con((forall n)h_n(A) ^ varprojlim^2 A^{(a),2} != 0)` against a Bergfalk-Lambie-Hanson
  simultaneous-vanishing forcing, settling `A_kappa <=> (forall n)h_n` or the first strict gap;
  (ii) full proof that `cd(A^{(a),k)}) = k` (strict `cd`-graded tower) and whether `cd` and the
  `cf`-rank grading coincide; (iii) the `I-Sigma_1`-over-`graph(-<)` cofinality proof for the
  exotic non-p.r. ordering, or the pathological `m_enc=O(1)` box.
- **(Pass 134 -> 135: the exotic-ordering `m_enc` residue, the explicit 2-coherent
  `A^{(a),2}` separator, and the `cf`-indexed rank-spectrum tower.)**  Pass 134 executed the
  three prongs of the Pass-133 successor with a scope correction, a CH correction, and a
  dimensional reframing.  **Thm 134a / Cor 134b:** for every PRIMITIVE-RECURSIVE-ordered
  `Sigma_1` Rosser box with `¬D2 ^ ¬Box_R⊥`, `m_enc` is UNBOUNDED (ordering-internalization
  diagonal: the `phi*_k` gap `(k,B(k)]` is defined from the Godel numbers of both `-<` and `B`,
  so re-ordering only relabels a same-width gap), closing Conj 132d for the standard class and
  pinning `PL(Box_R^A)=R+4` arithmetically INCOMPLETE at full `D3`; residue = exotic non-p.r.
  orderings, correcting "EVERY Sigma_1 box" to "every p.r.-ordered Sigma_1 box".  **Thm 134c/d:**
  the a-primary MP system `A^{(a)}` has `lim^1 != 0` under `b=aleph_1`, `=0` under `MA_{aleph_1}`,
  rank `aleph_1`; the strictly-intermediate witness is the COHEN model `b=aleph_1<c=aleph_2`
  (NOT CH, where `aleph_1=c`); and `aleph_1` is the FIRST, not unique, non-arithmetic layer -- a
  strict `cf`-indexed spectrum `aleph_0<aleph_1<...<2^aleph0`.  **Thm 134e:** `A^{(a)}` at level 1
  does NOT separate (n=1 retract transfer); the honest separator is the 2-coherent `A^{(a),2}`,
  giving `Con((forall n)h_n(A) ^ lim^2 A^{(a),2} != 0)`, an explicit BBMT instance (equivalence
  still OPEN).  Machine `check-pass134.py` PASS.  Next (Pass 135): (i) decide the exotic
  `Sigma_1`-but-not-p.r. ordering (pathological `m_enc=O(1)` box, or `Sigma_1`-induction proof of
  plant cofinality); (ii) construct `A^{(a),2)` and compute `varprojlim^2` under `b=aleph_1` vs
  `MA_{aleph_1}`, deciding whether it genuinely separates or level-2 triviality also transfers;
  (iii) map the full `cf`-indexed rank spectrum -- per-`n` forcing axiom separating `aleph_n` from
  `aleph_{n+1}`, strictness vs collapse, tying back to the Pass-55 solenoid `n=0` floor.
- **(Pass 133 -> 134: `m_enc`-unboundedness, the a-primary intermediate strong-homology
  object, and the two-system witness for `A_kappa`.)**  Pass 133 executed the three-part
  Pass-132 successor with two corrections and a reframing.  **Thm 133a:** for ANY omega-indexed
  tower `varprojlim^1` commutes with PRODUCTS (product is exact), so
  `varprojlim^1(prod_{i<omega}(Z,x a)) = (hatZ_a/Z)^omega` is ZFC-ABSOLUTE and nonzero (socle
  `F_q^omega`, dim `2^aleph0`) -- REFUTING the Pass-132 Next-step conflation of the continuum
  phantom with the Suslin-sensitive `A_{aleph_1}` limit.  **Thm 133b:** Suslin-sensitivity is a
  COFINALITY phenomenon (`varprojlim^1` fails to commute with uncountable direct SUMS only for an
  omega_1-cofinal COHERENT index); the intermediate `kappa_q=aleph_1` (CH-realized,
  `MA_{aleph_1}`-killed) object is the a-primary Mardesic-Prasolov coherent limit, NOT arithmetic.
  **Thm 133c:** `A_kappa => (forall n)h_n` trivially, converse <=> the two-system separation
  `Con((forall n)h_n(A) ^ exists coherent B lim^1 B != 0)` (n=1 retract transfers, n>=2 blocked);
  equivalence OPEN.  **Constr 133e / Thm 133f:** the schema-`4` reading of full `D3` is already
  Arai (Pass 127a), so Conj 132d is non-vacuous only WITNESS-BOUNDED; the `m_enc`-gap family flips
  `Box_R Box_R phi_k` cofinally for the least-witness box (O(1) Arai repairs), reducing Conj 132d
  to "every Sigma_1 Rosser box has `m_enc` unbounded".  Machine `check-pass133.py` PASS.  Next
  (Pass 134): (i) discharge the `m_enc`-unboundedness obligation (prove no Sigma_1 Rosser box has
  a prim-rec uniform nested-witness bound, completing Conj 132d; or find an `m_enc=O(1)`
  pathological box refuting it); (ii) construct `A^{(a)}` explicitly and compute its a-primary
  `varprojlim^1` rank under `b=aleph_1` vs `MA_{aleph_1}`, deciding whether `kappa_q=aleph_1` is
  the unique non-arithmetic layer between the Sigma_1 `oplus`-sum and the ZFC `prod`-continuum;
  (iii) exhibit the two-system witness `B` for the Thm-133c separation and test whether `A^{(a)}`
  is it (unifying A/B/C).

- **(Pass 132 -> 133: the analytic location of the continuum phantom, the `A_kappa <=>
  (forall n)h_n` placement, and the explicit `m_enc` `phi`-family.)**  Pass 132 RESOLVED the
  three-part Pass-131 successor.  **Thm 132a:** the `d`-strand graded Rosser predicate realizes
  `kappa_q = d`; and the ARITHMETIC ceiling `kappa_q <= aleph_0` for every `Sigma_1` predicate
  (recursive band family, natural limit = direct SUM).  **Cor 132a':** continuum torsion
  `kappa_q = 2^aleph0` lives ONLY at the direct PRODUCT completion (socle `F_q^omega`, dim
  `2^aleph0` by Erdos-Kaplansky) = the `aleph_1`-cofinal twin tower of Thm 131c; continuum-rank
  Prufer torsion has NO arithmetic-hierarchy representative, first appearing at the
  `bigoplus`->`prod` (arithmetic->analytic, Suslin-sensitive) boundary; o1'/o2' discharged by
  uniform band-relativized GS.  **Thm 132b:** general-`n` large-cardinal-free ZFC model of
  `h_1^...^h_{n-1}^¬h_n` at `2^aleph0=aleph_n` (truncated BHLH + ceiling); strict chain
  `A_kappa => (forall n)h_n => aleph_{omega+1}`, `A_kappa` at neither endpoint, equivalence
  OPEN.  **Thm 132c:** `D1^full-D3^(T|-¬Box_R⊥) => ¬D2` FORCED (Lob collapse).  **Conj 132d:**
  uniform full `D3` arithmetically incompatible with a Rosser box (`m_enc` overhead), so
  `PL(Box_R^A)=R+4` is arithmetically INCOMPLETE at full `D3`.  Machine `check-pass132.py` PASS.
  Next (Pass 133): (i) pin the analytic location of the `prod`-completion continuum phantom
  (= strong-homology / `A_{aleph_1}` derived limit?) and test an INTERMEDIATE `aleph_1`-strand
  `kappa_q=aleph_1` object under CH killed by `MA_{aleph_1}` (torsion analogue of Pass 60d/61c);
  (ii) decide `A_kappa <=> (forall n)h_n` or `A_kappa` strictly stronger, by testing whether
  `A_kappa` decides a `lim^n` of a coherent system OTHER than the twin tower; (iii) discharge
  Conj 132d by exhibiting the explicit cofinal `m_enc`-inflating `phi`-family, settling whether
  `PL(Box_R^A)=R+4` is arithmetically complete for Rosser boxes.

- **(Pass 131 -> 132: cross-layer independence, the multi-strand continuum phantom, the
  positive honesty forcing, and the arithmetic full-`D3` predicate.)**  Pass 131 RESOLVED the
  three-part Pass-130 successor.  **Thm 131a:** the Prufer rank is RIGID -- `kappa_q =
  dim_{F_q}(hatZ_N/Z)[q] = 1` for every finite `e_q` (incl. `e_q=0`), `= 0` iff `e_q=inf`
  (snake lemma, `G` divisible); so `Tor` is rank-one Prufer and depth-varying overhead cannot
  inflate `kappa_q` (continuum only in the torsion-free `Q^{(2^aleph0)}`).  **Pathology
  131a':** a `d`-strand tower gives `kappa_q = #(strands finite at q)` -- continuum-rank
  Prufer torsion = the multi-strand signature.  **Lemma 131b:** o1 (`D1^¬D2` uniform, GS per
  band) and o2 (index-`a_k`, honest `(Z,x a_k)`) discharged mod o1'/o2'.  **Thm 131c
  SHARPENS Pass 130:** `h_n => 2^aleph0>=aleph_{n+1}`, so `(forall n)h_n =>
  2^aleph0>=aleph_{omega+1}` (Konig); `h_1^¬h_2` holds in `MA_{aleph1}+2^aleph0=aleph_2`
  (large-cardinal-FREE); strength = BBMT `Delta`-system, not a cardinal characteristic.
  **Thm 131d:** `PL(Box_R^A)=R+4` = fusion `[GL]_Box(+)[GL]_{-<}` + bridge; **Thm 131e:** full
  `D3` coexists with `¬D2` (collapse is `D2`-only).  Machine `check-pass131.py` PASS.  Next
  (Pass 132): (i) close o1'/o2' with a uniform band-relativized GS cross-layer independence
  proof and CONSTRUCT a `d`-strand (then `omega`-strand) graded predicate realizing
  `kappa_q=d` (then `2^aleph0`), pinning the arithmetic hierarchy of continuum-rank torsion;
  (ii) supply the POSITIVE ZFC-only model of `h_1^...^h_{n-1}^¬h_n` at `2^aleph0=aleph_n`, and
  place BBMT `A_kappa` strictly between `2^aleph0>=aleph_{omega+1}` and `(forall n)h_n` or at
  an endpoint; (iii) decide whether a `Sigma_1` Rosser predicate satisfies `D1^¬D2^(full D3)`
  with `T|-¬Box_R bot` (strengthening Arai 1990) or full `D3` is arithmetically incompatible
  with `¬D2+¬Box_R bot`.

- **(Pass 130 -> 131: Prufer ranks, graded-Rosser obligations, the ZFC-only honesty
  threshold, and bimodal `R+4`.)**  Pass 130 RESOLVED the three-part Pass-129 successor.
  **Thm 130a:** `hatZ_N/Z` is DIVISIBLE (`ell`-divisible via the dense diagonal), so no
  finite `Z/q^k` splits off (Cor 130a.1 = the mirage-as-theorem); **Thm 130a.2:**
  `Tor(hatZ_N/Z)=bigoplus_{q notin Supp_inf}Z/q^inf`, torsion-free part `Q^{(2^aleph0)}` --
  the iso-type forgets every finite valuation, keeping only `Supp_inf`.  **Thm 130b:** `Phi`
  factors through the IDEMPOTENT semilattice hom `Supp_inf:(Steinitz,x)->(P(Primes),cup)`
  (`Phi(N^2)=Phi(N)`); not a hom into `(Ab,x)`.  **Constr 130c:** a graded Rosser `Sigma_1`
  predicate (disjoint bands, `a_k`-ary layers) realizes `(Z, x a_k)` and the primorial phantom.
  **Thm 130d CORRECTS Pass-129:** `(forall n)h_n` is EQUICONSISTENT WITH ZFC (Bergfalk-Hrušák-
  Lambie-Hanson kill the large cardinal), not a large-cardinal statement.  **Thm 130e:** a
  non-normal 3-neighborhood box is `D1^¬D2^D3^hom`; `WO` = Loeb for `-<`.  Machine
  `check-pass130.py` PASS.  Next (Pass 131): (i) discharge Constr-130c obligations o1
  (`D1^¬D2` uniform across layers) and o2 (`ConLat`-tower honestly `(Z,x a_k)`) and pin the
  exact Prufer ranks `kappa_q` (is `kappa_q=1` always, or can depth-varying overhead inflate it
  to the continuum?); (ii) pin the exact cardinal-characteristic threshold of `(forall n)h_n`
  between `2^aleph0>=aleph_2` and the Bannister-Bergfalk-Moore-Todorcevic `A_kappa` bound, and
  decide whether the `h_1^¬h_2` depth split survives in the ZFC-only (no large cardinal)
  models; (iii) prove bimodal completeness `PL(Box_R^A)=R+4` in `(Box, Box_{-<})` with
  `Box_{-<}` a `GL`-modality, and settle whether full `D3` can be added without collapsing
  `¬D2`.

- **(Pass 129 -> 130: the Steinitz image, graded-Rosser arithmetization, and the
  simultaneous-honesty bound.)**  Pass 129 RESOLVED the Pass-128 successor.  Thm 129a: the
  phantom functor `Phi(T=(Z,x m_n)) = hatZ_N/Z` factors through the STEINITZ monoid; every
  squarefree radical is realized by the `r`-ary race `r=prod_{p in S}p`; constant-arity
  predicates factor absolutely through `P_fin(Primes)` (`Phi(p^k)=Phi(p)`), and depth-varying
  arity escapes to an arbitrary `N`.  Pathology 129a': primorial race gives a NONZERO purely
  finitary phantom `(prod_p Z/p)/Z` (`Supp_infty=emptyset`), and the ML tail dichotomy is
  sharp.  Thm 129b: `h_1` does NOT decide `(h_n)_{n>=2}` (honesty stratifies by depth);
  simultaneous honesty `(forall n)h_n <=>` strong-homology additivity, a large-cardinal
  statement (weakly-compact upper bound, sharp bound OPEN).  Thm 129c: `WO` is
  pure-`Box`-inexpressible (two bisimulation certificates; census 68/68 frames on 3 worlds).
  Machine `check-pass129.py` PASS.  Next (Pass 130): (i) prove
  `varprojlim^1(Z,tower) = hatZ_{Supp_infty(N)}/Z` (finite-valuation primes die) or exhibit a
  surviving finite `Z/p^k`; is `Phi` a monoid HOMOMORPHISM (do composed races multiply their
  Steinitz numbers)?; (ii) ARITHMETIZE the depth-varying race as a genuine `Sigma_1` graded
  Rosser predicate whose `k`-th layer runs an `a_k`-ary race, realizing the primorial phantom
  by an ACTUAL predicate; (iii) settle the sharp lower bound for `(forall n)h_n` (weakly
  compact, or an inaccessible / tree property at `aleph_omega`?) via Bergfalk-Hrušák-
  Lambie-Hanson; (iv) build the non-normal NEIGHBORHOOD model realizing `D1^¬D2^D3^hom` +
  refuting `WO`, and pin the `-<`-fragment logic (`R`) in which `WO` is expressible.

- **(Pass 125 -> 126: the `D3^hom` frontier and the infinite-fan `alpha`.)**  Pass
  125 RESOLVED the three-part Pass-124 successor (and recovered a clobbered 2026-07-06
  run per `aps-run-sync-hazard`).  Thm 125a SPLIT `D3` for the Rosser box: the mixed
  `Box_R phi -> Box(Box_R phi)` is an unconditional theorem (`Box_R phi` is `Sigma_1`),
  the homogeneous `Box_R phi -> Box_R Box_R phi` is `R`-independent (Arai 1990) -- so
  the profile is `D1 ^ ¬D2 ^ D3^mix`, `D3^hom` free; `D2` re-added collapses to `GL`
  (kills the twins).  Thm 125b: the logic is Guaspari-Solovay `R`, `Box_R A := A -< ¬A`;
  the center is a CUT not a `GL`-world.  Thm 125d: exhaustive `alpha(H)=2+|MaxInd(H)|`
  IDENTITY (blocking/set-cover; zero realizations below budget, six samples).  Thm 125c:
  infinite carrier-join DICHOTOMY -- join-continuous (=ML=nFG2) forces
  `boxt w=/\ boxt c_n` (seeded-honest iff meet attained), discontinuous cover gives a
  free completion-manufactured phantom (Pass-55 solenoid); the finite seeded/seedless
  split bifurcates into seeded-honest/seeded-phantom/seedless.  Cor 125e: *Löb
  rigidifies, Rosser liberates -- by one degree of freedom at self-reference.*  Machine
  `check-pass125.py` PASS.  Next (Pass 126): (i) pin the CONCRETE least-witness `Box_R`
  at `D3^hom` (does it hold or fail? -- if fail, exhibit the `Sigma_1` sentence + the
  spurious short witness for `¬Box_R phi` breaking the guard, vs Arai's repairing
  predicate; classify `D3^hom`-compatible `PL(Box_R)` in the Kurahashi 2016 range);
  (ii) promote Thm 125d to a CLOSED-FORM `alpha` for INFINITE antichain hypergraphs
  (does `alpha=2+|MaxInd|` survive with an `omega`-fan and a directed-join `w`?),
  fusing with Thm 125c: is an infinite-fan bouquet FORCED seeded-phantom by a
  join-continuity failure, and does `/\_n boxt c_n = w` coincide with `H` having a
  "compact" independence complex (finitely many cofinal maximal independent sets)?

  _(Prior, Pass 124 -> 125, RESOLVED: concrete `Box_R`-`D3` (split into `D3^mix`
  theorem / `D3^hom` `R`-independent, Thm 125a-b), exhaustive `alpha` identity
  (Thm 125d), infinite carrier-join bifurcation (Thm 125c), Cor 125e slogan.)_

- **(Pass 124 -> 125: concrete `Box_R`-`D3`, exhaustive `alpha`, and the infinite
  carrier-join.)**  Pass 124 RESOLVED the odd-seed bouquet-with-center.  Thm 124a
  (carrier-join criterion): the Henkin center is CARRIER-SEEDED iff the disjunction
  `c_1 v c_2` exists in the carrier; on the six-element lattice `L*` (`w=c_1 v c_2` a
  genuine element) `boxt w=w` coexists with a detached seed `p` (SEEDED bouquet),
  contrasting the hexagon's seedless completion cut (Thm 123a); `ConLat_T` Boolean =>
  `rho_1 v rho_2` always exists => arithmetic bouquet ALWAYS seeded.  Thm 124b
  (De-Morgan collapse): a naive "boxt w=w forces fused twins" dichotomy is FALSE for
  general antitone maps (28/65 `L*` fixing maps separated -- an antitone map is not a
  lattice dual-hom, ignores De Morgan); correctly SCOPED to the 17 NORMAL (De-Morgan =
  `D2`-shadow) maps, 4 fix `w`, 0 separated => normal + `boxt w=w` => FUSED twins, so
  the separated seeded bouquet lives ONLY in `¬D2` (carrier shadow of Thm 123b).
  Thm 124c: profile `D1 ^ ¬D2`, base `Box` remains `GL`, `D3` NOT forced to fail
  (uniqueness needs full `GL`; `¬D2` alone liberates the twins).  Cor 124d: phantom
  tax = 1 for EVERY `H`, connectedness-blind.  Machine `check-pass124.py` PASS.  Next:
  (i) pin the CONCRETE Guaspari-Solovay `Box_R` `D3`-status (prove/refute
  `Box_R A -> Box_R Box_R A` while failing `D2`), and name the exact extension of `R`
  with witness-comparison `-<` whose theorems are the twin-plus-center profile (exhibit
  the Kripke-with-`-<` frame if `D3` holds, else the forcing argument);
  (ii) replace the lemma-level `alpha(H) >= 2+|MaxInd(H)|` bound with an EXHAUSTIVE
  brute force over all carriers up to a fixed atom budget for the six sample `H`;
  (iii) decide whether the seeded/seedless dichotomy (Thm 124a: frontier
  join-completeness) survives to INFINITE carriers -- can an `omega`-indexed Rosser
  bouquet whose disjunction is a DIRECTED join be carrier-seeded, or is it forced
  completion-manufactured by a join-continuity failure of `boxt` (tying back to the
  Pass-55 solenoid phantom and the Thm-48b/55c join-continuity <=> nFG2/ML dichotomy)?
  [RESOLVED by Pass 125 -- see the active item above: Thm 125a-e.]

  _(Prior, Pass 123 -> 124, RESOLVED: the odd-seed bouquet-with-center -- Thm 124a
  carrier-join criterion, Thm 124b De-Morgan collapse (refuted-then-scoped dichotomy),
  Thm 124c `D1 ^ ¬D2` with `D3` not forced, Cor 124d tax=1 connectedness-blind.)_

- **(Pass 123 -> 124: the odd-seed Rosser bouquet-with-center, and its Rosser
  modal logic.)**  Pass 123 RESOLVED the independent-Rosser-twins question with three
  theorems + a parity correction of Rem 122f.  Thm 123a: on the Pass-117 hexagon the
  2-twin disjunction `w=c_1 v c_2` is a `boxt_hat`-FIXED cut only via the CROSS map
  (twins onto the dual pair, images above the summands, Cor 117b); the front-internal
  SWAP collapses `w` to `bot` (Pass-117a).  Census: 477 antitone maps, 22 fix the cut
  ALL carrier-SEEDLESS, 38 collapse -- so the Thm-117c odd seed is
  COMPLETION-MANUFACTURED (positive answer to Pass-118(ii)).  Thm 123b: a bouquet
  FORCES `¬D2`; Guaspari-Solovay 1979 realize it arithmetically; it is an
  ANTI-artifact (arithmetic `Box` fails the internalized disjunction property = the
  De Morgan law).  Thm 123c: distinguished-vs-true-frontier (Thm 122d) = the
  Guaspari-Solovay witness-comparison nonuniqueness (witness ordering = free
  distinguished family; `Pi_1` equiconsistency = rigid true frontier; meet-density =
  `D2`).  Thm 123d/Cor 123e: `alpha_phantom(H)=2+|MaxInd(H)|` optimal, principal
  single-core `1+|MaxInd(H)|`, tax = one core atom = one witness-ordering.  [RESOLVED
  by Pass 124 -- see the active item above.]

  _(Prior, Pass 122 -> 123, RESOLVED: the independent-Rosser-twins phantom is realized
  on the hexagon (Thm 123a, with the parity correction of Rem 122f), forces `¬D2` and
  is an anti-artifact (Thm 123b), its distinguished-vs-frontier gap is the
  Guaspari-Solovay shadow (Thm 123c), and `alpha(H)=2+|MaxInd(H)|` is optimal
  (Thm 123d/Cor 123e); Pass-118(ii) answered positively -- fixed cuts are
  completion-manufactured and carrier-seedless.)_

- **(Drive supplement 2026-06-28: can APS be organized as a CAAL-style doctrine?)**
  The new Drive PDF `caal_article.pdf` presents categorical abstract algebraic
  logic through closure operators, theory lattices, logical matrices,
  Leibniz/Suszko congruences, pi-institutions, institutions, and doctrine
  equivalence. Open:
  (i) formulate an indexed APS doctrine whose fibers are theoremhood and
  refutability closure structures over a signature/category of contexts;
  (ii) decide whether `\Box`, `\boxtimes`, `T`, and `\bot` can be transported
  by signature morphisms as closure-preserving doctrine maps without forcing
  the G2/FG2 distinctions to collapse;
  (iii) identify the Leibniz or Suszko-style congruence that should quotient
  APS matrices while preserving primitive refutability rather than replacing
  it by provability of negation.

- **(Drive supplement 2026-06-25: can abstract-interpretation widening be internalized as APS approximation?)**
  The new reference PDF `abstractInter_コピー.pdf` presents abstract
  interpretation as complete-lattice fixed-point approximation through Galois
  connections and widening. Open:
  (i) formulate an APS or preAPS analogue of a widening operator
  $\nabla:S\times S\to S$ that preserves enough of A3/A4 to approximate
  $\boxtimes$-orbits without forcing a spurious fixed point;
  (ii) decide whether Galois connections between concrete and abstract
  theoremhood/refutability lattices preserve G2, FG2, or only weaker
  safety-style invariants;
  (iii) build a finite interval/polyhedral-domain-inspired APS example where
  widening terminates while exact fixed-point iteration remains non-stable, to
  compare with the repository's finite truncation versus liman obstruction.

- **(Drive supplement 2026-06-18: when does Scott-topos coherence force APS A3?)**
  The new Drive PDF `karazeris_categorical_domain_theory_commentary.pdf`
  sharpens the domain-semantics line into a categorical approximation problem.
  Open:
  (i) identify the weakest finitely accessible/coherent hypotheses on a
  category `K` that let Scott-topos or powercategory semantics support
  APS-style A3/A4 rather than only refutability/conflict structure;
  (ii) decide whether Karazeris's `2/3-SFP` coherence condition is the exact
  categorical shadow of the repository's repeated A3-stability obstruction
  under cut closure, completion, and domain semantics;
  (iii) build finite or algebraic Scott-APS witnesses where coherence holds
  but `FG2` still fails, to separate finite-limit stability from genuine
  diagonal fixed-point creation.

- **(Drive supplement 2026-06-17: when do Santa Claus, formalized Loeb, and primitive fixed points separate?)**
  The new Drive PDF `ams_residuated_complete_analysis.pdf` shows that bounded
  residuated AMS cleanly separates three diagonal packages that several older
  notes blurred together: `SC_\Box`, `FL_\Box/L_\Box`, and
  `FP_{\boxtimes} <=> FG2_{\boxtimes}`. Open:
  (i) classify the weakest non-bounded or non-residuated settings where the
  bounded equivalence `FP_{\boxtimes} <=> FG2_{\boxtimes}` breaks again;
  (ii) isolate a sharp finite-model or proof-theoretic witness for
  `SC_\Box /\ not FL_\Box` under weak `K/C` or weak `4`;
  (iii) decide whether Rosser- or Feferman-style weak provability predicates
  realize a stable region with `SC_\Box`, primitive `\boxtimes`, and
  `\neg FG2_{\boxtimes}` simultaneously.

- **(Drive supplement 2026-06-15: when does primitive refutability collapse to provability of negation?)**
  The new Drive PDFs `box_neg_vs_boxtimes_models.pdf` and
  `mnd4_residuated_ams_independence_report.pdf` expose a gap that several older
  notes blurred. Open:
  (i) classify the weakest extra hypotheses on a negation-equipped APS forcing
  `\boxtimes x = \Box\neg x` for all `x`;
  (ii) determine whether the needed hypotheses are best expressed as
  extensionality of `\Box` on provable equivalence classes, as a classical
  explosion package, or as a reflective/no-leak condition on a safe fragment;
  (iii) build finite witness families separating primitive `\boxtimes` fixed
  points, collapsed `\Box\neg` fixed points, and full six-condition MND4
  inconsistency.

- **(Pass 117 -> 118: self-dual-seed necessity -- is completion-separation
  inseparable from FP-synt?)**
  Pass 117 answered the Pass-116 plateau-join question **negatively**, and did the
  "upgrade Thm 116a to an orbit-independent conservation law" branch: the 2-cycle
  plateau fails too, by a **parity** law.  On the minimal bounded carrier -- the
  hexagon `H = {0,x,y,m,n,U}` -- the completion identifies `x v y` with `m ^ n`
  into one non-principal middle cut `w`, and the **antitone De Morgan join law**
  `boxt_hat(x v y) = boxt x ^ boxt y` gives `boxt_hat(w) = y ^ x = x ^ y = bottom`,
  so `w` is not fixed and `boxt_hat` is globally **fixed-point-free** (Thm 117a).
  **Cor 117b** unifies Thm 116a (chain: images at bottom) and Thm 117a (swap:
  images at the other summand): a fixed join needs images ABOVE the summands, which
  no orbit through the summands supplies.  **Thm 117c:** a non-principal fixed cut
  requires an ODD self-dual seed -- effectively a Jeroslow FP-synt point
  `p = boxt p`.  Open (Pass 118):
  (i) **`R_{2k}` general:** prove every even-cycle plateau (verified `k=1`, split
  `1+1`) is `boxt_hat`-fixed-point-free -- even combinatorial orbit length forces
  fixed-point-freeness;
  (ii) **necessity strictness:** build the smallest carrier with FP-synt
  DELIBERATELY REMOVED but an ODD self-dual geometry (3-cycle-with-center) and test
  whether its MacNeille completion can *manufacture* a non-principal fixed cut
  WITHOUT a carrier-level `p = boxt p` -- i.e. is Thm 117c's necessity strict, or
  is completion-separation genuinely a conservative shadow of refutability fixed
  points (a conservativity theorem)?
  (iii) residuation half inherits Pass-116 relocation verbatim (integral fiber
  keeps the antichain `{m,n}`, non-principal); re-census only if (ii) succeeds.

- **(Drive supplement 2026-06-14: fixed-point spaces versus APS self-reference)**
  The June 13 Drive PDFs `unary_operator_fixed_point_spaces.pdf` and
  `ams_aps_domain_theory_research_note.pdf` suggest a sharper meta-question
  behind several existing notes. Open:
  (i) isolate which properties of `Fix(f)` for an antitone or Scott-continuous
  operator `f` transfer to APS statements about `Fix_{\boxtimes}(S)` and
  `\boxtimes^2`-orbits;
  (ii) determine when compact-basis locality of A3 is enough to recover global
  APS behavior in algebraic Scott-APS;
  (iii) separate the natural negative domain models (Scott opens,
  orthogonality, stable conflict) from engineered `Star_\kappa`-style positive
  models that realize arbitrary fixed-point anti-chains.

- **(Drive supplement 2026-06-14: fixed-point spectrum under APS axiom packages)**
  The June 13 Drive PDFs `aps_classification.pdf`,
  `ams_aps_fixed_point_classification.pdf`, and
  `ams_aps_infinite_models_research_note.pdf` sharpen the old cardinal-spectrum
  idea into a concrete classification problem. Open:
  (i) determine `SpecFix_{\boxtimes}(\Gamma)` for core axiom packages `\Gamma`
  built from A1-A4, G2, FG2, C5, and residuation;
  (ii) separate cardinality, order type, definability, and periodic-orbit data
  of `Fix_{\boxtimes}(S)` rather than collapsing them to one count;
  (iii) formalize the share's Tukey-style witness-family invariant
  `\kappa(R)` by building bouquet APS realizations of small relational systems.

- **(Resolved Passes 80-82: automorphic shadow of the solid Borel; functional-equation wall)**
  Pass 80 computed $\mathrm{Sp}(H)$ for the hyperbolic plane $H=\epsilon\oplus\mathbb Q$ and settled
  the metaplectic question. **Resolved:** $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$ forces
  every solid endomorphism of $H$ to be upper-triangular (Thm 80a), so $\mathrm{Sp}(H)=B=\mathbb
  Q^{\times}\ltimes\epsilon$ is the solid **Borel** / affine "$ax+b$" group fixing the polarization
  $\epsilon$ — **not** $\mathrm{SL}_2$, **not** a nonabelian Heisenberg group (Thm 80b); the Weyl flip
  $w$ has no solid model. The finite-adele Weil representation of $\mathrm{SL}_2(\mathbb A_f)$
  **does not descend** to $\epsilon$ (Thm 80c): at level $N$ the flip is the finite Fourier $F_N$
  ($F_N^4=I$, $|g_N|^2=N$), but its only candidate limit lies in $\mathrm{Hom}(\epsilon,\mathbb Q)=0$.
  The **precise wall** is that one-sided vanishing ($\epsilon$ reflexive but not $\otimes$-dualizable)
  — explicitly **not** the degeneracy of $b$, which the Pass-79 Next step had guessed; the shear-by-$b$
  unipotent survives in $B$, only the inverse intertwiner $\epsilon\to\mathbb Q$ is absent.
  **Resolved by Passes 81-82:**
  the $B$-action is the maximally degenerate principal series $I(s)=\chi_s$;
  $\bar U=\mathrm{Hom}(\epsilon,\mathbb Q)=0$ is exactly the missing standard intertwiner and functional
  equation wall; nontrivial Whittaker functionals vanish, leaving only the constant term; the remaining
  question is now the global solenoid $\Sigma=\mathbb A/\mathbb Q$ versus finite phantom $\epsilon$
  comparison tracked above.

- **(Drive supplement 2026-06-13: extensionality-collapse dichotomy for APS comprehension)**
  The new Drive PDF `material_predicative_comprehension_nonclassical.pdf`
  turns the old monad/effects line into a sharper obstruction question. Open:
  (i) define a precise `AMS/MPC^\delta_R` semantics in which comprehension
  objects, observation, and APS modalities coexist;
  (ii) identify the exact threshold where observation/extensionality restores
  enough hidden contraction for self-comprehension to become a genuine G2-style
  obstruction;
  (iii) compare that threshold against the repository's existing safe-fragment,
  A3-stability, and cut-stability obstructions to decide whether these are
  equivalent or only analogous failure mechanisms.

- **(Drive supplement 2026-06-12: strictness of the self/mutual-reference hierarchy)**
  The new Drive PDF `ams_aps_self_reference_hierarchy.pdf` turns the old
  self/mutual-reference handoff into an explicit implication chain
  `FSR => MR_omega => MR_<omega => SR(C) => J => FG2 => G2 => Taut`. Open:
  (i) find a clean finite or computable APS/preAPS witness separating
  `Per_2` from `Per_1`, hence mutual/periodic reference from primitive
  Jeroslow self-reference;
  (ii) decide which parts of the chain can already be separated inside the
  existing G2-ZOO finite models and which require indexed/code-space structure;
  (iii) align the repository's `nFG2`, fixed-point cardinal, and
  Lawvere/Smullyan notes with one common hierarchy of principles.

- **(Drive supplement 2026-06-11: safe fragments and no-leak self-reference for MND4)**
  The accessible Drive PDFs `Double APS と MND4-preAPS における固定点・崩壊・定義可能性`
  and `Relative MND4-APS` sharpen the old MND4 note from a vague "fixed points
  outside the core" slogan into a concrete two-level semantics problem.  Open:
  (i) find an arithmetically natural safe class $D$ with
  $MND4 \subseteq PL_D(\operatorname{Pr})$ while diagonal fixed points still
  exist in the ambient sentence universe;
  (ii) formalize the no-leak condition
  $\operatorname{Diag}_{\boxtimes}(S)\cap i[D]=\varnothing$ in algebraic,
  fibred, or categorical terms;
  (iii) compare this safe-fragment obstruction with the repository's A3 and
  cut-stability obstructions to see whether they are the same saturation
  phenomenon in different guises.

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

- **(Drive supplement 2026-06-11: no-leak relative comparison for local FG2)**
  The new Drive PDF `relative_ams_variable_model.pdf` adds a sharper failure
  mode to the local-FG2/pullback line.  A relative comparison
  $f:M\to A$ should preserve `\Box`, `\boxtimes`, `T`, and `\bot`, but only as
  a theoremhood-preserving valuation map.  If a variable-bearing source element
  already lies above `T`, arbitrary valuations collapse the ambient model by
  forcing every target element to become provable.  Open:
  (i) formalize a `no-leak` pullback condition separating the closed theorem
  chain from the variable-generated region;
  (ii) characterize which local-FG2 profiles survive pullback under this
  weaker theoremhood-only comparison notion;
  (iii) decide whether the resulting obstruction is equivalent to the
  MND4 safe-fragment/no-leak condition or to the repository's A3-stability
  failure in disguise.

- **(Drive supplement 2026-06-13: separating self-reference from mutual reference)**
  The new Drive PDF `selfref_mutref.pdf` sharpens the reference hierarchy in a
  way the older handoff note did not.  With weakening/projections in the
  definable clone one has `MR_2 => SR`, and in a pure unary APS signature one
  even gets `SR <=> MR`; yet the same source claims a finite five-point APS
  model `M_5` with `SR /\ not MR_2` and a continuous Lopez-style witness
  `ALop` showing the same separation from fixed-point-property failure of
  products. Open:
  (i) reconstruct `M_5` explicitly inside `code/models/` and verify `SR`,
  `not MR_2`, and A1-A4 in repository notation;
  (ii) identify the weakest non-unary definability resource needed for
  `SR /\ not MR_2`;
  (iii) decide whether the topological `ALop` obstruction can be reformulated
  as a fibred/pullback or no-leak condition alongside the local-FG2 program.

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

- **(Pass 76 retarget: all-prime upgrade of the stratified pro-site model)**
  Pass 76 realized the Pass-75 projectors geometrically on the finite-prime
  stratified pro-site $\mathrm{StratPro}_\epsilon(U,N)$: support idempotents
  $e_p=(\cdot)\mathbf 1_{\{p\}}$ are multiplication by characteristic functions of
  clopen prime strata ($e_Se_T=e_{S\cap T}$), and stage idempotents $q_n$ are
  prefix truncations of the non-ML lcm tower ($q_nq_m=q_{\min(n,m)}$); the
  projector realization $\rho_{\mathrm{proj}}$ factors through this site
  faithfully on all five generator families.  The model is finite, discrete in
  $U$, and truncated at depth $N$.  Open: upgrade $\mathrm{StratPro}_\epsilon(U,N)$
  to an all-prime derived exact target -- an LCA sheaf on the profinite prime
  space, a condensed/solid abelian object, or a canonical exact pro-category
  carrying $\varprojlim^1$ -- and prove the signed duality law
  $D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$ there, or
  exhibit the derived/non-Hausdorff barrier that blocks it.

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
  a $\varprojlim^1$ class is a tail/pro-in

- **(Pass 138 retarget — active question)** Pass 138 discharged `[New (Pass 137)]`
  prong (a): the explicit Guaspari–Solovay Rosser $D2$-countermodel (**Thm 138a**,
  $B:=A\vee D$, witnessed in any $M\models T+\neg\mathrm{Con}_T$), $N$-adequacy
  (**Lemma 138b**: the failure is nonstandard-only), and the decision that
  $\mathrm{PL}_T(\Box_R^{\prec})$ sees only the certified-linearity bit
  $T\vdash\mathrm{Lin}(\prec)$ (**Thm 138c**, separator $\mathrm{WC}=\neg(\Box_R X\wedge
  \Box_R\neg X)$), the $I\Sigma_n$ tag rank collapsing to one Boolean (**Pathology
  138d**). **Now active (`[New (Pass 138)]` prong (b)):** the $\mathfrak b=\aleph_1$
  simultaneous-vanishing forcing (Bergfalk–Lambie-Hanson 2021) deciding
  $\mathrm{Con}((\forall n)\,h_n(A)\wedge\varprojlim^2 A^{(a),2}\ne0)$, using Thm 136b
  ($cd=2$ absolute) to certify a genuine level-2 obstruction — exhibit the strict gap
  $A_\kappa\not\Rightarrow(\forall n)h_n$ or reduce to a named higher
  additivity-of-ideal invariant. Governing invariants to carry: the Löb=sheaf /
  Rosser=cosheaf dictionary (Thm 61a/b) and the certified-linearity bit (Thm 138c).variant so "finitely supported phantom" is
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
