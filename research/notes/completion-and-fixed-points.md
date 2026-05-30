# Completion and Fixed Points

Source: https://chatgpt.com/share/6a0fbc8e-e630-8324-91df-73add1286869

Imported: 2026-05-22

## Core Idea

Completions can be used to create fixed points, but completeness alone is not enough.

For monotone operators, standard fixed point theorems apply:

$$
F:L\to L,\quad F\text{ monotone},\quad L\text{ complete lattice}
\Longrightarrow
\mathrm{Fix}(F)\neq\varnothing.
$$

This covers positive operators such as:

$$
x\mapsto \Box x,\qquad
x\mapsto a\otimes x\vee b.
$$

But APS Jeroslow fixed points

$$
p=\boxtimes p
$$

are difficult because $\boxtimes$ is typically antitone.

## Completion Candidates

- Dedekind-MacNeille completion
- ideal completion
- canonical extension
- quantale completion
- domain-theoretic dcpo completion

These can supply joins/meets or least fixed points, but the central issue is preservation and reflection:

1. Does the completion preserve APS axioms?
2. Do $\Box$, $\boxtimes$, and residuals extend canonically?
3. Does a fixed point in the completion reflect back to a definable/formula-level fixed point?

## Antitone Problem

For an antitone map $r$, Tarski's monotone theorem does not directly apply. Possible workarounds:

- study $r^2$, which is monotone,
- use bilattice or doubled-order structures,
- use topological connectedness and continuity,
- impose a special involutive or duality condition.

Even if completion gives a fixed point, it may be an ideal, cut, or limit object rather than a formula.

## Research Slogan

$$
\text{completion fixed point}
\neq
\text{syntactic fixed point}.
$$

The real problem is to characterize when completion-created fixed points are definable or reflected back into the Lindenbaum/pre-APS structure.

## Reflection Square Work Package

The next formal target is a completion-reflection square:

$$
L \xrightarrow{i} \widehat L,
\qquad
\boxtimes:L\to L,
\qquad
\widehat{\boxtimes}:\widehat L\to(\widehat L)^{op}
\quad\text{for antitone }\boxtimes.
$$

Given a completion fixed point

$$
q=\widehat{\boxtimes}q,
$$

the reflection problem asks for conditions under which either:

1. $q=i(p)$ for some $p\in L$ with $p=\boxtimes p$, or
2. $q$ has a definable/compact approximation that can be rounded back to an
   actual formula-level fixed point in $L$.

This separates four proof obligations:

- specify the completion and embedding $i$;
- specify the chosen extension of $\Box$, $\boxtimes$, and residuals;
- define which elements of $\widehat L$ count as principal, compact, or
  formula-definable;
- prove the rounding/reflection lemma, or exhibit a counterexample where a
  non-definable completion fixed point exists.

## MacNeille First Test

Use MacNeille completion as the first concrete test case. For $X\subseteq L$,
write:

$$
X^u=\{a:\forall x\in X,\ x\le a\},
\qquad
X^l=\{a:\forall x\in X,\ a\le x\}.
$$

The completion consists of closed lower cuts:

$$
C=(C^u)^l,
$$

with principal embedding:

$$
i(a)=(\{a\}^u)^l.
$$

The first extension question is variance-sensitive. A monotone $\Box:L\to L$
can be tested by a direct MacNeille-style extension, but an antitone
$\boxtimes:L\to L$ should first be regarded as a monotone map

$$
L\to L^{op}.
$$

Only after extending along this polarity should one compare the result back to
$\widehat L$. This prevents the extension step from silently treating an
antitone operation as monotone.

The current finite-checker convention is:

$$
\widehat{\boxtimes}(C)=\bigl((\boxtimes[C])^{l_L}\bigr)^{u_L},
$$

the MacNeille closure in $L^{op}$. The earlier
`antitone-dual-lower-cut-v0` rule used $((\boxtimes[C])^{u_L})^{l_L}$, which
has the wrong polarity for non-lattice examples and is retained only as a
legacy smoke-test rule.

MacNeille reflection target:

1. Build or choose $\widehat{\boxtimes}$ with the polarity convention stated.
2. Find $q\in\widehat L$ such that $q=\widehat{\boxtimes}q$.
3. Check whether $q=i(p)$ for any $p\in L$, and whether that $p$ is a
   syntactic fixed point $p=\boxtimes p$.
4. If not reflected, decide whether compact/definable approximants can recover a
   genuine $p=\boxtimes p$, or record it as a non-syntactic completion fixed
   point.

## Finite Search Target

The first computational target is a 3- or 4-element APS/preAPS candidate. For
each candidate, record the preorder, $T$, $\bot$, $\Box$, $\boxtimes$,
the antitone extension convention, and the resulting MacNeille cuts.

Classify candidates into:

1. no completion fixed point;
2. reflected principal completion fixed points;
3. principal but unreflected completion fixed points;
4. a non-principal completion fixed point with no syntactic fixed point;
5. a non-principal completion fixed point with a possible compact/definable
   rounding path.

The working protocol lives in
[../models/macneille-reflection-search.md](../models/macneille-reflection-search.md).

## Next Tasks

- Write the MacNeille completion of a preorder explicitly as Galois-closed cuts.
- Define canonical extensions of $\Box$ and residual operations.
- Add APS axiom-package checks to the finite MacNeille reflection search.
- Search for G2-holding variants of the size-3 non-lattice separation example.
- Test whether A1-A4 survive completion.
- Formulate a reflection theorem from completion fixed points to formula fixed points.
- Turn the reflection-square work package into a precise theorem/countermodel
  template.
- Compare with Ciabattoni-Galatos-Terui completion stability for cut elimination.

## Related Drive Files

- [APS_dissertation.pdf](https://drive.google.com/file/d/1VtS6tSvhUcoIG01fWprIrxGKZ3vZPjxc)
- [aps_g2_zoo_research_notes_lualatex_proof_complete.pdf](https://drive.google.com/file/d/123SEqYcTrWxkvo2XXvNhUZaN0QTWea3c)
- [algebraic_reverse_math_g2_aps.pdf](https://drive.google.com/file/d/1JoGMqK-9uQqC2Qp3490G2ZJvMj9N5DTe)
