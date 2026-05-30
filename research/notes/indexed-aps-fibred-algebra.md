# Indexed APS / Fibred Algebra

Source: https://chatgpt.com/share/6a091206-9c54-83e8-8c17-602c5572e247

Imported from Research Project handoff: 2026-05-22

## Topic

Indexed APS, indexed preorder, fibred algebra, and diagonal operators.

## Working Summary

This belongs to the same direction as fibered Res-APS: replace a one-sorted APS by a family of preorder/algebraic fibers indexed by contexts, theories, realizability data, or syntactic parameters.

## Detailed Reconstruction

The Project discussion identifies indexed APS with the categorical technology of
indexed preorders, hyperdoctrines, and fibred algebra. The basic correction is
variance: if $C$ is a category of contexts, an indexed preorder should be a
contravariant functor

$$
F:C^{op}\to\mathbf{Preord}.
$$

For every object $c\in C$, there is a fibre

$$
F(c)=(P_c,\le_c),
$$

and for every arrow $f:c\to d$, there is reindexing

$$
f^\ast:P_d\to P_c.
$$

Functoriality gives:

$$
(\mathrm{id}_c)^\ast=\mathrm{id}_{P_c},
$$

$$
(g\circ f)^\ast=f^\ast\circ g^\ast.
$$

This is the correct categorical form of substitution: formulas over $d$ can be
pulled back along a map from $c$ to $d$.

## Constant Indexed Preorder

For any preorder $A$, the constant indexed preorder is:

$$
\Delta A:C^{op}\to\mathbf{Preord},
$$

$$
(\Delta A)(c)=A,\qquad f^\ast=\mathrm{id}_A.
$$

This is useful as a degenerate baseline: it says that context does not matter.
It is too weak for syntax, quantification, or diagonalization, because it
cannot distinguish substitution, variable binding, or change of namespace.

## Indexed APS

An indexed APS should consist of an indexed preorder

$$
F:C^{op}\to\mathbf{Preord}
$$

such that each fibre carries APS-like structure:

$$
F(c)=
(P_c,\le_c,T_c,\bot_c,\Box_c,\boxtimes_c).
$$

The fibrewise A1 condition should read:

$$
x\le_c y
\Rightarrow
\Box_c x\le_c\Box_c y
\quad\text{and}\quad
\boxtimes_c y\le_c\boxtimes_c x.
$$

Reindexing should be compatible with the modalities. The strict version is:

$$
f^\ast(\Box_d x)=\Box_c(f^\ast x),
$$

$$
f^\ast(\boxtimes_d x)=\boxtimes_c(f^\ast x).
$$

A weaker lax version only requires comparison maps or inequalities. Which
version is appropriate depends on whether provability/refutability commutes
strictly with substitution in the intended syntax.

## Hyperdoctrine Extension

If $C$ has finite products and projections

$$
\pi:c\times d\to c,
$$

then quantifiers are modeled as adjoints to reindexing:

$$
\exists_\pi\dashv \pi^\ast\dashv \forall_\pi.
$$

This is the bridge to first-order logic. For APS, it allows one to state
parameterized fixed-point lemmas and compare:

$$
\exists p\,(p\simeq\boxtimes p)
$$

with parameterized forms:

$$
\forall a\,\exists p\,\bigl(p\simeq \varphi(p,a)\bigr).
$$

## Diagonalization Requirement

A diagonal/fixed-point operator cannot be obtained from the indexed preorder
alone. One needs additional structure:

- a code object or syntactic universe;
- quotation of formulas as codes;
- substitution/evaluation;
- compatibility between substitution and reindexing.

Thus, the path is:

$$
\text{indexed preorder}
\quad\leadsto\quad
\text{hyperdoctrine}
\quad\leadsto\quad
\text{indexed APS}
\quad\leadsto\quad
\text{diagonalizing indexed APS}.
$$

The last step is where G2-style fixed points enter.

## Next Tasks

- Extract the intended base category and fiber structure.
- Compare with [bs16-fiber-residuated-aps.md](bs16-fiber-residuated-aps.md).
- Formalize diagonal operators as fiberwise or reindexing-sensitive structure.
