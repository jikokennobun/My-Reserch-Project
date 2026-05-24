# MacNeille Reflection Search

This note specifies the first finite search target for completion-generated
versus syntactic fixed points.

## Goal

Find a small finite APS/preAPS candidate where MacNeille completion produces a
fixed point of the completed refutability operator, then classify whether that
fixed point is principal.

The desired outcomes are:

1. a principal reflected fixed point \(q=i(p)\), confirming that the search
   setup can recover syntactic fixed points; or
2. a non-principal fixed cut \(q\neq i(p)\), giving a concrete test case for
   failure of reflection.

## Search Space

Start with carriers of size \(3\) and \(4\). For each candidate:

- choose a preorder \(\le\);
- choose distinguished \(T\) and \(\bot\);
- choose \(\Box:L\to L\);
- choose antitone \(\boxtimes:L\to L\);
- optionally choose negation, tensor, and residuals only after the bare APS
  search is stable.

## MacNeille Step

For \(X\subseteq L\), compute:

\[
X^u=\{a:\forall x\in X,\ x\le a\},
\qquad
X^l=\{a:\forall x\in X,\ a\le x\}.
\]

The MacNeille completion consists of cuts \(C=(C^u)^l\), ordered by inclusion.
The principal embedding is:

\[
i(a)=(\{a\}^u)^l.
\]

## Extension Discipline

For every candidate, record the exact extension rule for \(\boxtimes\). Because
\(\boxtimes\) is antitone on \(L\), treat it first as a monotone map

\[
L\to L^{op}
\]

before comparing any completed value back with \(\widehat L\). A result is not
usable unless its polarity convention is explicit.

The planned checker interface is specified in
[macneille-checker-interface.md](macneille-checker-interface.md). Its first
extension rule is only provisional and should be recorded as part of every
result.

## Classification Fields

Each candidate should record:

- carrier size;
- preorder;
- \(T\), \(\bot\), \(\Box\), and \(\boxtimes\);
- which APS/preAPS axioms or fragments are checked;
- whether G2 holds;
- whether FG2 holds;
- whether \(p=\boxtimes p\) has a solution in \(L\);
- whether \(q=\widehat{\boxtimes}q\) has a solution in \(\widehat L\);
- whether each completion fixed point is principal;
- if non-principal, whether any compact/definable rounding path is visible.

## First Target

The first target is a 3-element preorder with no primitive
\(\boxtimes\)-fixed point in \(L\) but with a non-principal completion fixed
point in \(\widehat L\), if such a candidate exists under the chosen extension
rule.

If no 3-element candidate exists, move to 4 elements and keep the failed search
as useful evidence about the strength of the reflection condition.

## First Checker Result

Report:
[../outputs/macneille-reflection-three-chain-antitone.json](../outputs/macneille-reflection-three-chain-antitone.json).

- Model: `three-chain-antitone`
- Extension rule: `antitone-dual-lower-cut-v0`
- Classification: `principal-only`
- Syntactic fixed point: `m`
- Completed fixed point: `{ b, m, t }`, principal at `t`
- G2: false
- FG2: false
- A1-A4: not checked by the first milestone

This is a smoke-test baseline, not a reflection counterexample. The next
substantive search should enumerate additional 3-element preorders and antitone
maps, or first review whether the provisional extension rule should be replaced
before enumeration.
