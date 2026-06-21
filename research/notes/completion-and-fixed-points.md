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

The current finite-checker convention is
`antitone-dual-lower-cut-v1`:

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
[../../code/models/macneille-reflection-search.md](../../code/models/macneille-reflection-search.md).

## Pass 111 Verification

Pass 111 verified the Claude Code review repair of the finite MacNeille
reflection checker.  The decisive model is
`code/models/examples/three-element-nolattice-nosynt.json`: its carrier is
`{0,a,b}` with `0<a`, `0<b`, and `a` incomparable with `b`; refutability sends
`0` to `a` and both `a,b` to `0`.  It has no syntactic fixed point.

Under `antitone-dual-lower-cut-v1`, the checker reports the non-principal
completion fixed cut `{ 0, a, b }`, classified as
`nonprincipal-without-syntactic`, with no principal-extension failures.  Under
legacy `antitone-dual-lower-cut-v0`, the same model reports `{ 0, a }`,
principal at `a` but unreflected, and fails the principal-extension condition
twice.  This makes the v0/v1 polarity distinction observable in the smallest
non-lattice example.

The three-chain smoke test also matters: under v1 it has syntactic fixed
point `m`, but its completed fixed cut is `{ b, m, t }`, principal at `t` and
not reflected.  Hence the checker must preserve the distinction between
principal fixed cuts and reflected fixed cuts.

Machine certificates:

- `artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v1.json`
- `artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v0.json`
- `artifacts/reports/macneille-reflection-three-chain-antitone-v1.json`
- `artifacts/reports/pass111-macneille-reflection-review-check.json`

## Pass 112 G2/A2 Boundary

Pass 112 added finite `apsAxioms` fields to the MacNeille checker.  These
fields check A1-A4 as finite order/table conditions only; they do not certify
residuals, canonical extension stability, or reflection theorems for completed
fixed cuts.

The v1 non-lattice witness now has a sharper status.  It still has no
syntactic fixed point and has the non-principal completion fixed cut
`{ 0, a, b }`, but its finite `apsAxioms` block satisfies A1-A4.  The witness
fails G2 because `boxtimes(T) <= bottom` holds while `T <= bottom` does not.

The carrier-local search
`artifacts/reports/pass112-macneille-g2-boundary-check.json` exhausts all
total antitone `boxtimes` tables and all total `Box` tables on the same
V-shaped carrier.  It finds:

- 216 tables with v1 non-principal completion separation and no syntactic
  fixed point;
- 54 such tables satisfying G2 only vacuously, after A2 is dropped;
- no such table satisfying G2 and A2 together, hence none satisfying G2 plus
  A124Core or full finite A1-A4 APS.

Thus the smallest non-lattice carrier exhibits an **A2 gate**: G2-compatible
completion separation is available only by leaving the A2 part of APS.  The
next completion-reflection test must determine whether this gate is an artifact
of the three-element carrier or persists in four-element searches.

## Pass 113 Four-Element Witness

Pass 113 shows that the A2 gate is not stable under adding one point.  The
explicit witness has carrier `{0,a,b,c}` and order
$$
0<a<b,\qquad 0<c,
$$
with `b` and `c` incomparable.  Put `T=a`, `bottom=0`,
$$
\boxtimes(0)=\boxtimes(a)=b,\qquad
\boxtimes(b)=\boxtimes(c)=0,
$$
and
$$
\Box(0)=\Box(a)=\Box(c)=0,\qquad \Box(b)=b.
$$

The original carrier has no syntactic $\boxtimes$-fixed point.  Under the v1
MacNeille extension, the whole cut `{ 0, a, b, c }` is fixed and non-principal.
The usual checker report
`artifacts/reports/macneille-reflection-four-element-g2-aps-nosynt-v1.json`
confirms:

- `classification = nonprincipal-without-syntactic`;
- `g2 = true`;
- `fg2 = true`;
- `apsAxioms.APS = true`;
- no principal-extension failures under the v1 convention.

The broader Pass-113 enumeration over labelled four-element posets with a
unique bottom found 2784 separation+G2+finite-APS tables across 240
refutability profiles and 36 posets.  Thus the next reflection question is no
longer whether A2 alone blocks the completion-created fixed cut; it is whether
residual structure or completion-stability blocks this four-element witness.

## Next Tasks

- Write the MacNeille completion of a preorder explicitly as Galois-closed cuts.
- Try to equip the four-element G2+finite-APS witness with tensor and residual
  operations.
- Define canonical extensions of $\Box$, tensor, and residual operations.
- Test whether A1-A4, G2, and FG2 survive completion for the four-element
  witness.
- Formulate a reflection theorem from completion fixed points to formula fixed points.
- Turn the reflection-square work package into a precise theorem/countermodel
  template.
- Compare with Ciabattoni-Galatos-Terui completion stability for cut elimination.

## Related Drive Files

- [APS_dissertation.pdf](https://drive.google.com/file/d/1VtS6tSvhUcoIG01fWprIrxGKZ3vZPjxc)
- [aps_g2_zoo_research_notes_lualatex_proof_complete.pdf](https://drive.google.com/file/d/123SEqYcTrWxkvo2XXvNhUZaN0QTWea3c)
- [algebraic_reverse_math_g2_aps.pdf](https://drive.google.com/file/d/1JoGMqK-9uQqC2Qp3490G2ZJvMj9N5DTe)
