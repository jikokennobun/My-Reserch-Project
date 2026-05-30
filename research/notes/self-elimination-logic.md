# Self-Elimination Logic

Source: https://chatgpt.com/share/6a143fbc-a1b0-8321-9149-bb06c05af8b7

Imported: 2026-05-30

## Core Idea

This thread explores a "self-elimination" or "self-killing" logic where the
self-reference is not about truth or provability, but about axiomhood itself.

The motivating forms are:

$$
E \leftrightarrow \text{``}E\text{ is not an axiom / is deleted''}
$$

and the global nihilistic sentence:

$$
N \equiv \text{``this system has no axioms.''}
$$

The main warning is that this should not be read as an ordinary static classical
theory. If axiomhood reflection is unrestricted, the system collapses.

The short import recorded the theme but not the mathematical machinery. The
Project discussion is better understood as a proposal for a dynamic axiomhood
semantics: axiomhood is not a fixed predicate but a state that can be revised by
deletion rules.

## Static Collapse

Let $\operatorname{Ax}(x)$ be an axiomhood predicate and put:

$$
N:=\forall x\,\neg \operatorname{Ax}(x).
$$

If $N$ itself is an axiom and the system proves axiomhood of every axiom, then:

$$
\vdash \operatorname{Ax}(\ulcorner N\urcorner)
$$

and also, by instantiating $N$,

$$
\vdash \neg \operatorname{Ax}(\ulcorner N\urcorner).
$$

With classical explosion, the theory becomes trivial.

More explicitly, let $A$ be a set of axioms and suppose:

$$
N\in A,\qquad
N\equiv \forall x\,\neg\operatorname{Ax}(x).
$$

Assume axiomhood reflection:

$$
\varphi\in A\Rightarrow A\vdash \operatorname{Ax}(\ulcorner\varphi\urcorner).
$$

Then $N\in A$ gives:

$$
A\vdash \operatorname{Ax}(\ulcorner N\urcorner).
$$

But $N$ itself gives:

$$
A\vdash \neg\operatorname{Ax}(\ulcorner N\urcorner).
$$

Hence $A$ proves a contradiction. If the underlying logic has explosion, then
for every sentence $\psi$:

$$
A\vdash\psi.
$$

This proposition should be treated as the baseline impossibility theorem for
static self-elimination.

## Dynamic Reading

The proposed nontrivial reading separates:

- candidate axioms;
- active axioms;
- deleted axioms;
- proof closure;
- deletion/update operations.

The logic is therefore closer to nonmonotonic or dynamic semantics than to a
single static consequence relation. It may be modelled by a deletion operator
on axiom states:

$$
A_{n+1}=A_n\setminus D(A_n),
$$

where $D(A)$ is the set of axioms marked for deletion by the current state.

## A Minimal Dynamic Semantics

Let $B$ be a finite or recursively enumerable set of candidate axioms. Let
$\operatorname{Cn}_0(A)$ be the deductive closure of $A$ under a fixed base
logic $\vdash_0$. Introduce a deletion predicate

$$
\operatorname{Del}(\ulcorner\varphi\urcorner).
$$

### Hard Deletion

The hard deletion operator is:

$$
\Gamma_{\mathrm{hard}}(A)
=
B\setminus
\{\varphi\in B:
\operatorname{Cn}_0(A)\vdash
\operatorname{Del}(\ulcorner\varphi\urcorner)\}.
$$

A hard-stable axiom set is a fixed point:

$$
A=\Gamma_{\mathrm{hard}}(A).
$$

### Soft Deletion

A soft version may delete only axioms whose deletion is derivable without using
the axiom itself, or may require an external priority relation:

$$
\Gamma_{\mathrm{soft}}(A)
=
B\setminus
\{\varphi\in B:
\operatorname{Cn}_0(A\setminus\{\varphi\})\vdash
\operatorname{Del}(\ulcorner\varphi\urcorner)\}.
$$

This separates self-attacking axioms from axioms attacked by the rest of the
system.

## Basic Examples

### Self-Deleting Axiom

Let $B=\{E\}$ and let

$$
E\vdash_0 \operatorname{Del}(\ulcorner E\urcorner).
$$

Then:

$$
\Gamma_{\mathrm{hard}}(\{E\})=\varnothing,
$$

while

$$
\Gamma_{\mathrm{hard}}(\varnothing)=\{E\},
$$

assuming no deletion is derivable from the empty state. Thus hard deletion has
a two-cycle:

$$
\{E\}\mapsto\varnothing\mapsto\{E\}.
$$

There is no hard-stable fixed point.

### Global Deletion Axiom

Let $B=\{N,\varphi_1,\ldots,\varphi_k\}$ and let $N$ imply deletion of every
candidate axiom:

$$
N\vdash_0
\operatorname{Del}(\ulcorner\psi\urcorner)
\quad
(\psi\in B).
$$

If $N\in A$, the next state deletes everything. If $N\notin A$ and no other
axiom deletes $N$, then the next state restores $N$. This creates the same
oscillation pattern at a global scale.

### External Stabilization

If an external priority rule says that deletion claims made by $N$ are ignored
after the first collapse, then $\varnothing$ or $B\setminus\{N\}$ can be chosen
as a stable extension. This is analogous to choosing extensions in default
logic or argumentation semantics.

## Monotonicity Failure

The deletion operator is generally nonmonotone. Suppose:

$$
A\subseteq A\cup\{E\}
$$

and $E$ proves deletion of itself or of some $\varphi\in A$. Then:

$$
\Gamma_{\mathrm{hard}}(A\cup\{E\})
\subsetneq
\Gamma_{\mathrm{hard}}(A)\cup\{E\}
$$

can occur. Adding an axiom can reduce the next active set.

This is why ordinary monotone fixed-point theorems are not the right tool.
Antitone maps, stable-model operators, or alternating fixed-point constructions
are better candidates.

## Death Rank

For an iterative deletion process

$$
A_0=B,\qquad A_{n+1}=\Gamma(A_n),
$$

define the death rank of an axiom $\varphi$ by:

$$
\rho(\varphi)=\min\{n:\varphi\notin A_n\},
$$

if such an $n$ exists. If $\varphi$ is never deleted, put
$\rho(\varphi)=\infty$. For cyclic processes, $\rho$ should be refined to
record the orbit:

$$
\mathcal O_\Gamma(\varphi)=
\{n:\varphi\in A_n\}.
$$

This gives a finite invariant analogous in spirit to the n-FG2 orbit profiles
already used in the G2-ZOO.

## Expected Phenomena

- Self-deleting axioms can create two-cycles.
- Global deletion principles may have no stable fixed point.
- Soft deletion and hard deletion should be separated.
- External stabilization may choose among possible stable extensions.
- Monotonicity can fail because adding an axiom may trigger deletion of itself
  or of other axioms.

## Relation to Current Project

This is not currently an APS theorem, but it is relevant as a nearby
fixed-point and anti-fixed-point phenomenon:

$$
\text{fixed point of truth/provability}
\quad\text{versus}\quad
\text{anti-fixed point of axiomhood/deletion}.
$$

It may connect to:

- non-normal modal logics without necessitation or monotonicity;
- default logic and stable-extension semantics;
- argumentation frameworks;
- resource-sensitive accounts where contraction/weakening are not automatic.

## Next Tasks

- Define a minimal self-elimination system with hard and soft deletion.
- Prove the static-collapse proposition as a baseline.
- Build finite-state transition examples showing fixed points, two-cycles, and
  no-fixed-point behavior.
- Decide whether the deletion operator belongs in APS proper, weak APS, or a
  separate "prelogic" layer.
- Implement a finite-state checker for $\Gamma_{\mathrm{hard}}$ and
  $\Gamma_{\mathrm{soft}}$ examples.
