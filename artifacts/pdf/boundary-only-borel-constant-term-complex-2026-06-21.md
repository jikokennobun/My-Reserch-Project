# Boundary-Only Borel Constant-Term Complex

Autonomous discussion Pass 95 packages the all-prime Borel boundary shadow as
a two-term constant-term complex.

The complex is
$$
C_B=\mathbb Q^\times\ltimes[\mathbb Q\to\mathbb A_f],
$$
with cohomological degrees $0\to1$.  The map is the diagonal inclusion
$\mathbb Q\hookrightarrow\mathbb A_f$, and the global Levi
$\mathbb Q^\times$ acts by scalar multiplication.

Its all-prime solid cohomology is
$$
H^0(C_B)=0,
\qquad
H^1(C_B)=\mathbb A_f/\mathbb Q
\cong\widehat{\mathbb Z}/\mathbb Z=\epsilon.
$$
Thus $C_B$ carries the Pass-94 boundary-only functional-equation shadow.

At finite conductor $N$, the shadow is
$$
C_{B,N}=(\mathbb Z/N)^\times\ltimes
\left[\mathbb Z/N\to\prod_{p^e\parallel N}\mathbb Z/p^e\right].
$$
The diagonal map is an isomorphism by the Chinese remainder theorem, so every
fixed finite conductor shadow is ordinary-acyclic.  The phantom is not a
finite-level cokernel; it is the all-prime solid boundary.

Naturality has two directions.  If $N\mid M$, conductor reduction gives a
commuting square of two-term complexes and preserves the Borel unit class.
For finite supports $S\subseteq T$, projection $T\to S$ is canonical.  Support
enlargement $S\to T$ is only a finite-conductor CRT choice or span: exact
zero-insertion does not preserve the all-prime diagonal copy of $\mathbb Z$.

This gives a precise "functional equation without Weyl operator" theorem.
The signed boundary and constant term survive, but there is no nontrivial
Whittaker coefficient and no standard Weyl/Fourier intertwiner.

The finite checker
`artifacts/reports/pass95-boundary-only-borel-constant-term-complex-check.json`
verifies finite conductor acyclicity, conductor naturality, support projection
behavior, and the all-prime constant-term row with solid boundary
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$.
