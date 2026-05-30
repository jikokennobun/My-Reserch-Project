# Sequential Pair Theory and Indexed APS

Source: https://chatgpt.com/share/6a1aca33-434c-8323-b77c-3f8158ecf52a

Imported: 2026-05-30

## Core Idea

This thread asks how Visser-style Sequential Theory and Pair Theory can be
abstracted in algebraic or categorical language and placed together with
Beklemishev--Shamkanov APS.

The recommended split is:

$$
\text{syntax/coding layer}
\quad+\quad
\text{provability/refutability layer}.
$$

Pairing and finite sequences should not simply be added as binary operations on
the APS sentence preorder. They belong to a separate code or context layer,
while APS lives in the layer of propositions, entailment, provability, and
refutability.

The initial note was only a map. The mathematical content is that APS should be
viewed as the closed-sentence fibre of a richer indexed structure.
Sequentiality then supplies the fixed-point machinery that ordinary APS
deliberately does not contain.

## Three-Layer Decomposition of G2

The discussion decomposes the second incompleteness mechanism as:

$$
\text{Pair/Seq/Clone}\Rightarrow \text{Diagonalization},
$$

$$
\text{Diagonalization}+\text{representability of }\boxtimes
\Rightarrow
\exists p\,(p\simeq\boxtimes p),
$$

$$
\exists p\,(p\simeq\boxtimes p)+\text{APS axioms}
\Rightarrow
\mathrm{FG2},\mathrm{G2}.
$$

This is a useful separation:

- Visser/sequentiality supplies the internal coding needed for fixed points.
- APS extracts G2/FG2 consequences from the fixed point.
- Nonclassical or substructural settings may separate coding, self-substitution,
  and G2 behavior.

## Indexed/Fibred APS

The proposed categorical form is an indexed preorder:

$$
\mathcal P:\mathcal C^{op}\to \mathbf{Preord},
$$

where $\mathcal C$ is a base category of codes, contexts, variables, and finite
sequences. Each fibre $\mathcal P(c)$ contains propositions in context $c$.
Closed sentences live in $\mathcal P(1)$.

APS structure can then be added fibrewise:

$$
(\mathcal P(c),\le_c,\top_c,\bot_c,\Box_c,\boxtimes_c).
$$

This makes it possible to state substitution, quotation, diagonalization, and
pairing without confusing code-pairing with conjunction or product in the
sentence preorder.

## Research Reading

The thread suggests that "Sequential APS" should be a two-layer or fibred
structure, not a one-sorted enrichment of APS:

- code objects and finite sequences live in $\mathcal C$;
- formulas live in fibres $\mathcal P(c)$;
- fixed-point operators arise from substitution/diagonalization;
- G2/FG2 extraction remains the APS part.

This also helps explain why fixed-point existence is not an APS axiom: APS needs
an external or fibred syntax apparatus to supply self-reference.

## Definition: Fibred APS

Let $\mathcal C$ be a base category of contexts, codes, substitutions, and finite
sequences. A fibred pre-APS is an indexed preorder:

$$
\mathcal P:\mathcal C^{op}\to \mathbf{Preord}
$$

together with, for each object $c\in\mathcal C$, designated elements

$$
\top_c,\bot_c\in\mathcal P(c)
$$

and modalities

$$
\Box_c,\boxtimes_c:\mathcal P(c)\to\mathcal P(c).
$$

For every arrow $f:c\to d$, reindexing

$$
f^*:\mathcal P(d)\to\mathcal P(c)
$$

should preserve enough structure to interpret substitution:

$$
f^*(\top_d)=\top_c,\qquad
f^*(\bot_d)=\bot_c,
$$

and at least satisfy comparison maps

$$
f^*(\Box_d x)\le \Box_c f^*(x),
\qquad
f^*(\boxtimes_d x)\le \boxtimes_c f^*(x),
$$

or equalities when strict substitution stability is intended.

The ordinary APS is recovered at the terminal context:

$$
S=\mathcal P(1).
$$

## Sequential Structure

The code layer should contain:

1. a code object $\mathsf{Code}$;
2. pairing and projections:

   $$
   \langle-,-\rangle:\mathsf{Code}\times\mathsf{Code}\to\mathsf{Code},
   $$

   $$
   \pi_1,\pi_2:\mathsf{Code}\to\mathsf{Code};
   $$

3. finite sequence operations:

   $$
   \mathsf{nil},\qquad
   \mathsf{cons}:\mathsf{Code}\times\mathsf{Seq}\to\mathsf{Seq};
   $$

4. a substitution or evaluation operation:

   $$
   \operatorname{Sub}(e,x)
   $$

   reading "substitute the code $x$ into the expression coded by $e$."

These are not operations on closed propositions. They are operations in
$\mathcal C$ or in a code object internal to $\mathcal C$.

## Diagonalization Principle

A diagonal operator is a map, or represented operation,

$$
\Delta:\mathsf{Code}\to\mathsf{Code}
$$

such that if $e$ codes a one-variable formula/context operation $F$, then
$\Delta(e)$ codes the self-application instance:

$$
\Delta(e)\simeq F(\Delta(e)).
$$

In the fibre language, for a definable operation

$$
F:\mathcal P(1)\to\mathcal P(1),
$$

diagonalization supplies a closed sentence $p\in\mathcal P(1)$ with

$$
p\simeq F(p).
$$

Taking $F=\boxtimes$ gives a Jeroslow-style fixed point:

$$
p\simeq\boxtimes p.
$$

## Theorem Schema: Sequentiality Plus APS Gives G2

Assume:

1. the code layer is sequential enough to represent $\boxtimes$ and produce a
   fixed point $p\simeq\boxtimes p$;
2. the closed fibre $\mathcal P(1)$ satisfies the APS axioms A1--A4;
3. the fixed point equivalence is strong enough to be used in the APS order.

Then the usual APS theorem yields:

$$
\mathrm{FG2}:\quad \boxtimes\boxtimes T\le\boxtimes T
$$

and

$$
\mathrm{G2}:\quad \boxtimes T\le\bot\Rightarrow T\le\bot.
$$

Proof sketch. Sequentiality supplies the fixed point. The APS theorem then
uses A1--A4 to derive FG2 from that fixed point. Finally, A1 and A2 derive G2
from FG2 as in [formalized-g2-implicational-aps.md](formalized-g2-implicational-aps.md).

The point is modularity:

$$
\text{sequentiality}
\quad\text{and}\quad
\text{APS extraction}
$$

are separate hypotheses.

## Why One-Sorted Pairing Is Not Enough

If one adds a binary operation

$$
\langle-,-\rangle:L\times L\to L
$$

directly to the sentence preorder, it is ambiguous whether this means:

- conjunction of propositions;
- product of resources;
- syntactic pairing of Gödel codes;
- ordered pair in a model of arithmetic.

Sequential theory requires the third or fourth reading. APS order usually lives
at the first or second level. Therefore a one-sorted operation on $L$ risks
proving the wrong theorem. The fibred formulation prevents this collapse.

## Relation to Existing Notes

This note refines [indexed-aps-fibred-algebra.md](indexed-aps-fibred-algebra.md)
by isolating the role of sequentiality. The older indexed-APS note focuses on
fibred algebra and diagonal operators; the present note says what additional
coding structure must exist before diagonal operators are mathematically
available.

## Next Tasks

- Define fibred APS precisely enough to state reindexing and fibrewise A1--A4.
- Identify the minimal sequentiality/pairing condition that yields a
  Jeroslow-style fixed point.
- Connect this note with [indexed-aps-fibred-algebra.md](indexed-aps-fibred-algebra.md).
- Keep the code layer separate from the proposition/order layer in future
  definitions.
- Compare Visser's SEQ construction with a reflective or idempotent-monad
  presentation of the code layer.
