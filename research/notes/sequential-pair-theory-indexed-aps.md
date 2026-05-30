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

## Next Tasks

- Define fibred APS precisely enough to state reindexing and fibrewise A1--A4.
- Identify the minimal sequentiality/pairing condition that yields a
  Jeroslow-style fixed point.
- Connect this note with [indexed-aps-fibred-algebra.md](indexed-aps-fibred-algebra.md).
- Keep the code layer separate from the proposition/order layer in future
  definitions.
