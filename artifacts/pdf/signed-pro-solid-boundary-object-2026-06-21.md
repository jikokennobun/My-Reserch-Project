# Signed Pro/Solid All-Prime Boundary Object

Autonomous discussion Pass 104 assembles the finite signed conductor system
into the all-prime pro/solid boundary package.

For $\sigma\in\{\pm1\}$, the finite signed conductor classes
$$
b_N^\sigma=\sigma\bmod N
$$
are compatible under conductor reduction.  Their inverse limit is the
diagonal integer
$$
\{b_N^\sigma\}_N=\sigma\in\widehat{\mathbb Z}.
$$

Since $\sigma=\pm1$ lies in the diagonal copy of $\mathbb Z$, its image in
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z
$$
is zero.  Thus the two signs do not define two distinct points of
$\epsilon$, and the orientation double cover does not survive as a
nontrivial point-cover or torsor over the all-prime boundary group.

The sign survives as the $\mathbb Z/2$ local-system action on the
boundary/Yoneda line.  For
$$
\delta_\epsilon=[0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0],
$$
the action is
$$
\delta_\epsilon\mapsto\sigma\delta_\epsilon.
$$
Under the shifted-dual identification
$$
D\epsilon\simeq\mathbb Q[-1],
$$
this is the same sign action on the shifted boundary generator.

The minimal sign-preserving all-prime package is:

- the oriented-support action groupoid of pairs $(S,c)$;
- the finite-conductor pro-system of signed CRT-isomorphism complexes;
- a $B\mathbb Z/2$ local system on the boundary/Yoneda line.

This package records support, conductor, and sign, but it does not create a
degree-$0$ Weyl/Fourier map $\epsilon\to\mathbb Q$.

The next task is to compare this signed pro-boundary stack with support
projections and zero-extension spans, then isolate the exact descent/colimit
statement for all-prime primitive orientations.

The checker
`artifacts/reports/pass104-signed-pro-solid-boundary-object-check.json`
verifies conductor compatibility of the finite sign system, identifies the
pro-limit as the diagonal integer $\sigma$, verifies that both signs vanish as
points of $\epsilon$, records survival as a $\mathbb Z/2$ boundary action, and
checks that the minimal package does not create a degree-$0$ Weyl map.
