# Definitions

This file normalizes recurring definitions for the APS/G2-ZOO project.

## Abstract Provability Structure

An abstract provability structure is treated as preorder-like data

\[
S=(L_S,\le_S,\Box,\boxtimes,T,\bot).
\]

The intended readings are:

\[
T\le_S x
\quad\text{means}\quad
x\text{ is provable},
\]

\[
x\le_S\bot
\quad\text{means}\quad
x\text{ is refutable}.
\]

## G2

\[
\mathrm{G2}(S):
\quad
\boxtimes T\le_S\bot
\Rightarrow
T\le_S\bot.
\]

Read: if the consistency-like assertion is refutable, then the system is already inconsistent.

## FG2

\[
\mathrm{FG2}(S):
\quad
\boxtimes\boxtimes T\le_S\boxtimes T.
\]

Read: a formalized second incompleteness principle internal to the APS order.

For \(k\ge 1\), define:

\[
\mathrm{nFG2}(k):
\quad
\boxtimes^{k+1}T\le_S\boxtimes^kT.
\]

Thus FG2 is \(\mathrm{nFG2}(1)\). The \(T\)-orbit of \(\boxtimes\) is:

\[
T,\boxtimes T,\boxtimes^2T,\ldots
\]

All-level nFG2 means \(\mathrm{nFG2}(k)\) holds for every \(k\ge 1\). In finite
preAPS models this is equivalent to eventual stabilization of the tail orbit at
a syntactic \(\boxtimes\)-fixed point.

The **first-true nFG2 depth** of a model is the least \(d\ge 1\) such that
\(\mathrm{nFG2}(d)\) holds, if such a \(d\) exists. The family \(D_N\) in
`notes/g2-fg2-hierarchy.md` has first-true depth \(N+1\).

If \(S\) is non-collapsed, i.e. \(T\not\le_S\bot\), then G2 holds iff
\(\boxtimes T\not\le_S\bot\). Thus G2 in non-collapsed finite preAPS models is
always vacuous in the material-implication sense.

## Fixed Point Principles

Jeroslow/refutability fixed point:

\[
\exists p\,(p=_S\boxtimes p).
\]

Godel/negated provability fixed point:

\[
\exists p\,(p=_S\neg\Box p).
\]

These must be kept distinct unless \(\boxtimes\) is explicitly defined from \(\neg\Box\).

## Completion Vocabulary

For a preorder \(L\) and \(X\subseteq L\), write:

\[
X^u=\{a\in L:\forall x\in X,\ x\le a\},
\qquad
X^l=\{a\in L:\forall x\in X,\ a\le x\}.
\]

A MacNeille-closed lower cut is a set \(C\subseteq L\) such that:

\[
C=(C^u)^l.
\]

The MacNeille completion \(\widehat L\) is the ordered collection of these
closed lower cuts, with the principal embedding:

\[
i(a)=(\{a\}^u)^l.
\]

A completion-generated fixed point for \(\boxtimes\) is an element
\(q\in\widehat L\) satisfying:

\[
q=\widehat{\boxtimes}q.
\]

A syntactic fixed point is a formula-level or APS-level element \(p\in L\)
satisfying:

\[
p=\boxtimes p.
\]

A completion fixed point is reflected when \(q=i(p)\) for such a \(p\), or when
a stated definable/compact rounding lemma recovers such a \(p\) from \(q\).

For antitone \(\boxtimes\), the extension should be treated as a monotone map
into the order dual before any comparison back with \(\widehat L\).

The **correct lower extension** of an antitone \(\boxtimes:L\to L\) to
MacNeille cuts is the map \(\widehat{\boxtimes}:\widehat L\to(\widehat L)^{op}\)
defined by:

\[
\widehat{\boxtimes}(C) = \bigl((\boxtimes[C])^{l_L}\bigr)^{u_L},
\]

i.e., the \(L^{op}\)-MacNeille closure of the pointwise image \(\boxtimes[C]\).
This satisfies the extension condition
\(\widehat{\boxtimes}(i(a))=i_{L^{op}}(\boxtimes a)\) for all \(a\in L\).

**Warning**: computing \(((\boxtimes[C])^{u_L})^{l_L}\) instead (the
\(L\)-MacNeille closure) is the wrong polarity. It agrees with the correct
formula on lattice models (where every cut is principal) but diverges on
non-lattice models, producing spurious completion fixed points.

A completion fixed point \(q\) is **reflected** iff \(q=i(p)\) for some
syntactic fixed point \(p\in L\) (i.e., \(\boxtimes p = p\)).

A completion fixed point is **principal-unreflected** iff \(q=i(a)\) for some
\(a\in L\) but \(\boxtimes a \neq a\). Principal-unreflected fixed points can
appear even in lattice models (as in `three-chain-antitone` where \(q=i(t)\)
with \(\boxtimes t = b\neq t\)).

## Residuated APS

A residuated APS adds a resource composition and residuals:

\[
(L,\le,\otimes,\mathbf 1,\backslash,/,\Box,\boxtimes,T,\bot).
\]

The residuation law is:

\[
a\otimes b\le c
\iff
b\le a\backslash c
\iff
a\le c/b.
\]

## Open Definition Tasks

- Define ACR precisely.
- Normalize A1-A4 and variants.
- Define primitive versus definitional \(\boxtimes\).
- Define indexed/fibered APS.
- Define completion-generated fixed points versus syntactic fixed points.
