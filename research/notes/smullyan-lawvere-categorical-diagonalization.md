# Smullyan, Lawvere, and Categorical Diagonalization

Source: https://chatgpt.com/share/6a06498e-c108-83e8-941c-75b1931bbc3a

Imported from Research Project handoff: 2026-05-22

Access note: local relay logs identify this source as `Smullyan-style
diagonalization and category theory`. The reconstruction below records the
mathematical content needed by the APS project: ordinary categorical diagonals,
quotation, substitution, and Lawvere-style fixed-point principles.

## Abstract

APS needs a fixed-point engine explaining when a formula-level operation such
as $\boxtimes$ has a syntactic fixed point:

$$
p=\boxtimes p.
$$

Lawvere's fixed-point theorem supplies a categorical template, while
Smullyan-style diagonalization supplies the syntactic mechanism: quotation plus
self-substitution. The main caution is that the ordinary diagonal map:

$$
\Delta_X:X\to X\times X
$$

does not by itself produce Godel or Jeroslow sentences. It duplicates a
variable; it does not quote a formula, substitute its code into itself, or
interpret the result as a sentence. APS fixed points require all of these
operations.

## Lawvere Fixed-Point Template

In a cartesian closed category, let:

$$
e:A\times A\to Y
$$

be a weakly point-surjective map, meaning that for every morphism
$h:A\to Y$ there is some $a:1\to A$ such that:

$$
h = e\circ(a\times \mathrm{id}_A)
$$

up to the relevant equality. Then every endomorphism:

$$
\alpha:Y\to Y
$$

has a fixed point.

The standard proof defines:

$$
g(a)=\alpha(e(a,a)).
$$

By weak point-surjectivity, choose $b$ representing $g$. Then:

$$
e(b,b)=g(b)=\alpha(e(b,b)).
$$

Thus $e(b,b)$ is a fixed point of $\alpha$.

## Why the Ordinary Diagonal Is Not Enough

The diagonal:

$$
\Delta_X:X\to X\times X
$$

only sends:

$$
x\mapsto(x,x).
$$

In syntax, diagonalization needs a different operation. Given a one-variable
formula $\varphi(x)$, one must form the sentence:

$$
\varphi(\ulcorner\varphi\urcorner).
$$

This requires:

1. a code or name $\ulcorner\varphi\urcorner$;
2. a substitution operation;
3. an interpretation of the substituted expression as a closed formula;
4. an equivalence relation under which the fixed-point equation is checked.

Therefore categorical diagonalization for logic must be formulated in a
category or indexed structure that contains quotation and substitution, not
only finite products.

## Hyperdoctrine Formulation

Let:

$$
P:C^{op}\to\mathbf{Pos}
$$

be an indexed preorder or hyperdoctrine. Objects of $C$ are contexts, and
$P(c)$ is the preorder of predicates over context $c$. For an arrow:

$$
f:c\to d,
$$

reindexing is:

$$
f^\ast:P(d)\to P(c).
$$

The ordinary diagonal:

$$
\Delta_c:c\to c\times c
$$

gives reindexing:

$$
\Delta_c^\ast:P(c\times c)\to P(c).
$$

This models using the same variable twice. It still does not quote a predicate.
Smullyan/Godel diagonalization instead needs a naming operation that sends a
predicate to a code and a substitution operation that feeds that code back into
the predicate.

## Smullyan-Style Self-Substitution

Let $\mathrm{Form}_1$ be a class of one-variable formulas and
$\mathrm{Sent}$ a class of sentences. A diagonalization operator is a map:

$$
\mathrm{diag}:\mathrm{Form}_1\to\mathrm{Sent}
$$

such that:

$$
\mathrm{diag}(\varphi)
\equiv
\varphi(\ulcorner\mathrm{diag}(\varphi)\urcorner)
$$

under the relevant equivalence.

This form emphasizes that the code substituted into $\varphi$ is the code of
the resulting sentence, not merely the code of the open formula. In many
presentations this is implemented by a preliminary self-application operator
followed by a fixed-point lemma.

### Definition: Diagonal Operator Relative to a Theory

Let $T$ be a theory and let $\equiv_T$ denote provable equivalence. A
$T$-diagonal operator for a class $\Gamma$ of one-variable formulas is a map:

$$
D:\Gamma\to\mathrm{Sent}
$$

such that for every $\varphi(x)\in\Gamma$:

$$
T\vdash
D(\varphi)\leftrightarrow
\varphi(\ulcorner D(\varphi)\urcorner).
$$

If the equivalence is represented in APS by equality or preorder equivalence,
this gives:

$$
[D(\varphi)]
=_S
[\varphi(\ulcorner D(\varphi)\urcorner)].
$$

## APS Fixed Points from Diagonalization

Suppose $\boxtimes$ is represented syntactically by a one-variable formula
$B(x)$ such that:

$$
[B(\ulcorner\psi\urcorner)]
=_S
\boxtimes[\psi].
$$

Apply the diagonal operator to $B$. There is a sentence $p$ such that:

$$
p
\leftrightarrow
B(\ulcorner p\urcorner).
$$

Passing to APS equivalence:

$$
[p]=_S\boxtimes[p].
$$

Thus diagonalization supplies `FP-synt`.

This proof uses syntax. It is not an APS axiom. APS axioms later determine
which G2/FG2 consequences follow from the fixed point.

## Lawvere Versus Smullyan

The Lawvere theorem and Smullyan diagonalization have the same abstract shape:

$$
\text{representability}+\text{diagonal/self-application}
\Longrightarrow
\text{fixed point}.
$$

But their data are different.

| Layer | Main object | Fixed-point mechanism |
|---|---|---|
| Lawvere | weakly point-surjective $e:A\times A\to Y$ | categorical self-application |
| Hyperdoctrine | indexed predicates $P:C^{op}\to\mathbf{Pos}$ | reindexing plus naming |
| Smullyan | formula codes and substitution | self-substitution |
| APS | preorder elements and $\boxtimes$ | imported syntactic fixed point |

The APS project should not cite Lawvere alone unless the quotation/substitution
data have been made explicit.

## Theorem Schema for APS

Let $S$ be an APS extracted from a syntactic theory $T$. Assume:

1. a class $\Gamma$ of one-variable formulas is closed under the operation
   representing $\boxtimes$;
2. there is a diagonal operator

   $$
   D:\Gamma\to\mathrm{Sent}
   $$

   satisfying the fixed-point lemma over $T$;
3. APS equality $=_S$ respects $T$-provable equivalence;
4. $\boxtimes$ is represented by a formula $B(x)\in\Gamma$.

Then $S$ has a syntactic refutability fixed point:

$$
\exists p\in L_S\quad p=_S\boxtimes p.
$$

Proof. Apply $D$ to $B(x)$ and pass to APS equivalence.

## Categorical Reconstruction Problem

To make the theorem schema fully categorical, construct:

1. a category $C$ of contexts;
2. an indexed preorder $P:C^{op}\to\mathbf{Preord}$;
3. a code object $\mathrm{Code}$;
4. a quotation or naming operation from predicates to codes;
5. a substitution/reindexing operation:

   $$
   \mathrm{subst}:P(c\times\mathrm{Code})\to P(c);
   $$

6. a representation of $\boxtimes$ as a predicate transformer;
7. a diagonal lemma internal to this structure.

Only after this data is fixed can one safely say that APS fixed points follow
from categorical diagonalization.

## Relation to Existing Notes

- `indexed-aps-fibred-algebra.md` gives the indexed-preorder language needed
  for hyperdoctrines and reindexing.
- `self-mutual-reference-hierarchy.md` generalizes unary diagonalization to
  systems of equations and graph-shaped reference.
- `residuated-fixedpoint-existence.md` studies algebraic fixed-point existence.
  The present note separates syntactic diagonal fixed points from order- or
  completion-generated fixed points.
- `completion-and-fixed-points.md` warns that semantic completion fixed points
  do not automatically reflect to syntax.

## Open Problems

1. Write an explicit indexed-preorder model of the Godel diagonal lemma, with
   quotation and substitution named as structure.
2. Determine whether Jeroslow fixed points for primitive $\boxtimes$ require
   less syntactic structure than Godel fixed points for $\neg\Box$.
3. Compare weak point-surjectivity in Lawvere's theorem with representability
   of formula operations in arithmetic.
4. Formalize mutual-reference diagonalization as a Lawvere theorem over
   products or graph-indexed contexts.
5. Add a source-backed citation note for the precise Lawvere theorem variant
   used by the APS project.
