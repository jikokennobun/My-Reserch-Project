# APS Cardinal Invariants and Fixed-Point Spectrum

## Source and Provenance

- Primary share source: <https://chatgpt.com/share/6a0b7536-836c-83ab-ae90-5eb16748d05e>
- Imported from Research Project handoff: 2026-05-22
- Rechecked from the share watchlist: 2026-06-14
- Share access status: reachable and unchanged at `2026-06-13T18:07:51+09:00`
- Durable Drive supplements:
  - `aps_classification.pdf` (Drive created `2026-06-13T08:21:54Z`)
  - `ams_aps_fixed_point_classification.pdf` (Drive created `2026-06-13T10:26:47Z`)
  - `ams_aps_infinite_models_research_note.pdf` (Drive created `2026-06-13T13:17:39Z`)
- Reconstruction note: the share itself is still only a relay stub. The mathematical content below is reconstructed from the unchanged share together with the newer accessible Drive PDFs, which make the fixed-point spectrum line substantially more explicit.

## Abstract

The fixed-point side of APS should be treated as a spectrum problem rather than as a single yes/no self-reference test. For an APS

$$
S=(L,\le,\Box,\boxtimes,T,\bot),
$$

one studies not only existence of $p=\boxtimes p$, but the size, order type, definability, and ambient regularity of

$$
\mathrm{Fix}_{\boxtimes}(S)=\{p\in L : p =_S \boxtimes p\}.
$$

The June 13 Drive supplements sharpen this into a classification program across finite, computable, non-computable, topological, domain-theoretic, and residuated models. The central point is that APS principles such as G2, FG2, Jeroslow existence, Santa Claus solvability, and Loeb behavior can be re-expressed as spectrum constraints on $\mathrm{Fix}_{\boxtimes}(S)$ and related witness families. This turns G2-ZOO from a loose list of examples into a cardinal-invariant and realization problem.

## Background and Notation

Repository-wide notation follows [definitions.md](../definitions.md). We use

$$
S=(L,\le,\Box,\boxtimes,T,\bot)
$$

with $T$ the designated theoremhood point, $\bot$ the designated contradiction point, $\Box$ the provability modality, and $\boxtimes$ the refutability modality. Equality up to the ambient preorder is written

$$
x =_S y \quad:\Longleftrightarrow\quad x\le y \text{ and } y\le x.
$$

The basic fixed-point spectra are

$$
\mathrm{Fix}_{\Box}(S)=\{x : x =_S \Box x\},
\qquad
\mathrm{Fix}_{\boxtimes}(S)=\{x : x =_S \boxtimes x\}.
$$

We also use

$$
\mathrm{FG2}(S):\quad \boxtimes\boxtimes T \le \boxtimes T,
$$

and

$$
\mathrm{G2}(S):\quad \boxtimes T \le \bot \Rightarrow T \le \bot.
$$

For a theory class $\Gamma$ of APS axioms, define the spectrum

$$
\mathrm{SpecFix}_{\boxtimes}(\Gamma)
=
\left\{\kappa :
\exists S\models \Gamma\,
\bigl|\mathrm{Fix}_{\boxtimes}(S)\bigr|=\kappa
\right\}.
$$

The Drive supplements suggest that one should refine this by order type, definability class, topological closure, and orbit structure under $\boxtimes^2$.

## Definitions

### Fixed-point spectrum

The simplest invariant is

$$
\kappa_{\boxtimes}(S)=\bigl|\mathrm{Fix}_{\boxtimes}(S)\bigr|.
$$

But the June 13 classification drafts make clear that this is only the first coordinate. A fuller spectrum package is

$$
\Sigma_{\boxtimes}(S)=
\bigl(
\kappa_{\boxtimes},
\operatorname{OrdType}(\mathrm{Fix}_{\boxtimes}),
\operatorname{Def}(\mathrm{Fix}_{\boxtimes}),
\operatorname{Top}(\mathrm{Fix}_{\boxtimes}),
\operatorname{Osc}_{\boxtimes}
\bigr),
$$

where $\operatorname{Osc}_{\boxtimes}$ records non-fixed periodic orbits of the antitone map $\boxtimes$.

### Witness-family invariant

The share and classification draft both point toward a relational-system reformulation. For a relation

$$
R \subseteq X\times Y,
$$

define

$$
\kappa(R)=
\min\left\{
|D| :
D\subseteq Y\text{ and }
\forall x\in X\,\exists y\in D\,R(x,y)
\right\}.
$$

This is the abstract form of classical cardinal characteristics such as $\mathfrak d$. The proposal is that many G2-ZOO principles can be rewritten as witness problems of this shape and then compared via Tukey-style reductions.

### Bouquet realization problem

The handoff sketch also suggests a "bouquet APS" principle: encode a relational system by a family of named fixed points or near-fixed points whose interaction pattern reproduces $R$. In that language, reductions between cardinal invariants become APS realization morphisms.

## Main Claims Reconstructed from the Drive Supplements

### Proposition 1. Fixed-point existence is not the same problem as fixed-point spectrum.

The June 13 PDFs emphasize that APS classification cannot stop at the question

$$
\exists p\,(p=_S\boxtimes p).
$$

Even when such a $p$ exists, the surrounding structure may differ drastically:

- finite models may have one, several, or finitely many fixed points;
- computable infinite models may realize countably many fixed points in a controlled way;
- non-computable or saturated models may realize very large spectra;
- domain and topological models may have semantic fixed points without giving definable ones.

Proof sketch. This is a synthesis claim rather than a single theorem. The June 13 fixed-point classification draft organizes the repository's existing examples precisely along those axes: finite toy separations, infinite anti-chain models, function-space explosions, and analytic/domain models where continuity creates semantic fixed points but not necessarily APS-style Jeroslow fixed points.

### Proposition 2. The right invariant is a spectrum of realizable cardinalities under axiom packages.

For each axiom package $\Gamma$ one should ask for

$$
\mathrm{SpecFix}_{\boxtimes}(\Gamma),
$$

not just whether a fixed point exists.

Expected examples from the current note ecology:

- weak finite APS fragments realize $0,1,n$ for small $n$;
- richer non-C5 or anti-chain constructions plausibly realize countably infinite spectra;
- function-space and model-theoretic amplifications suggest continuum-sized spectra;
- residuated or topological regularity may constrain which spectra remain compatible with A3/A4 or with Santa Claus equations.

Proof sketch. The accessible `ams_aps_fixed_point_classification.pdf` explicitly reframes the program this way, and `ams_aps_infinite_models_research_note.pdf` adds the infinite-model mechanism: once a model has multiple fixed points, function-space amplification and anti-chain-style constructions can push the spectrum upward dramatically.

### Proposition 3. Cardinal invariants in the G2-ZOO should be treated as witness-family sizes, not only as fixed-point counts.

The share's original suggestion survives the newer Drive material: one should associate to an APS principle a relational system

$$
\forall x\in X\,\exists y\in Y\,R(x,y)
$$

and then study $\kappa(R)$ as the invariant. Fixed-point cardinality is one special case, but not the only one.

Proof sketch. The share already compared this setup with $\mathfrak d$. The newer classification draft strengthens the point by sorting principles according to how much witnessing data is needed: a single fixed point, a family of local witnesses, a dense spectrum, or an entire ambient semantic space.

### Proposition 4. Infinite-model behavior is governed by more than cardinality.

The infinite-model note highlights at least four independent axes:

1. cardinality of $\mathrm{Fix}_{\boxtimes}(S)$;
2. whether the fixed-point set is chain-like, anti-chain-like, dense, or oscillatory;
3. whether the points are definable/computable or only externally present;
4. whether the ambient semantics is continuous, Scott-continuous, residuated, or set-theoretically pathological.

In particular, continuum many semantic fixed points do not automatically yield an APS-style diagonal phenomenon, and definability can fail even when topological existence is abundant.

## Examples and Counterexamples

### Example 1. Empty spectrum

Natural Heyting/Boolean-style APS candidates may satisfy the structural clauses of APS while having

$$
\mathrm{Fix}_{\boxtimes}(S)=\varnothing.
$$

This gives the zero point of the spectrum and shows that APS alone does not force Jeroslow fixed points.

### Example 2. Finite nonzero spectrum

The existing finite-model program in this repository already treats small models with one or several designated fixed points as separation witnesses for G2/FG2 and related schemes. These should be recast as the first layer of $\mathrm{SpecFix}_{\boxtimes}(\Gamma)$.

### Example 3. Function-space amplification

The June 13 infinite-model note stresses that once an APS has at least two fixed points, suitable function-space constructions can amplify the spectrum to continuum size. This is not just "more of the same"; it changes the geometry of the fixed-point set from a finite witness set to a high-dimensional semantic family.

### Counterexample 1. Continuity does not imply definability.

Analytic or domain-theoretic fixed-point theorems can provide semantic solutions to fixed-point equations, yet those solutions need not correspond to definable Jeroslow sentences. Hence "there is a fixed point" and "there is an APS self-reference principle" separate.

### Counterexample 2. Residuated richness does not by itself force APS fixed points.

The residuated side can support implication, resource sensitivity, or Santa Claus solvability without making A3/A4-compatible Jeroslow fixed points plentiful. The classification drafts repeatedly warn that residuation and continuity often pull against the strict APS collision axiom A3.

## Finite-Model and Computation Tasks

The spectrum program should be made machine-checkable in the repository.

### Task 1. Spectrum enumeration

For each finite model in `code/models/`, compute

$$
\bigl|\mathrm{Fix}_{\boxtimes}(S)\bigr|,
\qquad
\bigl|\mathrm{Fix}_{\Box}(S)\bigr|,
\qquad
\bigl|\mathrm{Osc}_{\boxtimes}(S)\bigr|.
$$

### Task 2. Spectrum under axiom filters

Partition the finite-model catalog by satisfaction of A1-A4, G2, FG2, C5, and residuation. Then estimate the initial finite fragments of

$$
\mathrm{SpecFix}_{\boxtimes}(\Gamma).
$$

### Task 3. Bouquet realization search

Attempt to realize small relational systems $(X,Y,R)$ inside finite APS by assigning named fixed points or named $\boxtimes^2$-orbits. This would turn the share's Tukey-reduction idea into a concrete model-search problem.

### Task 4. Definability versus existence

For infinite or analytic candidates, separate:

- semantic fixed-point existence;
- definable fixed-point existence;
- computable fixed-point existence.

This is required before any cardinal characteristic extracted from the model can be interpreted as a self-reference invariant.

## Relation to Existing Notes

This note sits at the intersection of several existing lines.

- [g2-fg2-hierarchy.md](g2-fg2-hierarchy.md): fixed-point spectra should refine the hierarchy rather than merely accompany it.
- [analytic-aps.md](analytic-aps.md): analytic models produce semantic fixed points and continuity constraints, but definability remains separate.
- [completion-and-fixed-points.md](completion-and-fixed-points.md): completion methods may enlarge semantic fixed-point spectra without preserving APS-style diagonal content.
- [local-fg2-pullback-aps-zoo.md](local-fg2-pullback-aps-zoo.md): local comparison and no-leak constraints can be reframed as restrictions on which spectra survive pullback.
- [self-mutual-reference-hierarchy.md](self-mutual-reference-hierarchy.md): mutual-reference and periodic-reference strata suggest that one should track $\boxtimes^2$-orbits and not only strict fixed points.

## Inaccessible or Deferred Artifacts

The original share referenced `g2_zoo_cardinal_invariants.pdf` and `g2_zoo_cardinal_invariants.tex` as `sandbox:/mnt/data/...` artifacts. Those paths remain inaccessible from the repository. They should still be routed through the local Google Drive artifact inbox:

```text
C:\Users\20010215fjii\マイドライブ\ChatGPT Project Inbox\My-Reserch-Project
```

Once exported there, they can be imported by

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-chatgpt-project-artifacts.ps1
```

## Open Problems

1. Determine the smallest realistic axiom packages $\Gamma$ for which $\mathrm{SpecFix}_{\boxtimes}(\Gamma)$ contains $0,1,n,\aleph_0,2^{\aleph_0}$.
2. Decide which order types of fixed-point sets are realizable under A1-A4: anti-chains, dense chains, scattered chains, periodic-orbit bouquets, or mixed spectra.
3. Formalize the witness-family invariant $\kappa(R)$ for G2-ZOO principles and prove that Tukey-style reductions can be implemented by APS bouquet constructions.
4. Separate semantic, definable, and computable fixed-point spectra in analytic/domain and residuated settings.
5. Compare fixed-point cardinal spectra with the self/mutual-reference hierarchy: does large $\mathrm{Fix}_{\boxtimes}(S)$ force anything about periodic or mutual reference, or are these orthogonal axes?
