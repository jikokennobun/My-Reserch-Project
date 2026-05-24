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
- Define \(n\)-FG2.
- Define primitive versus definitional \(\boxtimes\).
- Define indexed/fibered APS.
- Define completion-generated fixed points versus syntactic fixed points.
