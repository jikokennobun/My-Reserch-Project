# All-Prime Borel j_! Solid Dual

Autonomous discussion Pass 94 computes the Verdier/solid dual of the
all-prime Borel $j_!$ coefficient.

Pass 93 identified the all-prime coefficient as
$$
\mathfrak B^{\mathrm{cont}}_{j!}
=\mathbb Q^\times\ltimes
R\!\varprojlim_{S\Subset\mathbb P}j_{S,!}\mathcal V_S,
$$
whose unipotent cohomology is
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$

Solid duality gives
$$
D\epsilon\simeq\mathbb Q[-1].
$$
Therefore the dual unipotent is a shifted boundary object, not an opposite
degree-$0$ unipotent group.  Keeping the global Levi, the dual Borel shadow is
a Levi-marked boundary object with unipotent part $\mathbb Q[-1]$ and
contragredient $\mathbb Q^\times$ action.

The finite signed Verdier rule survives.  For the finite recollement boundary
$$
d_S:\mathbb Z^S\to\mathbb Z^{|S|-1},
$$
duality sends
$$
D(d_S)=-d_S^T,
\qquad
D^2(d_S)=d_S.
$$
The sign is visible over $\mathbb Z$ and invisible modulo $2$.

All-prime, the same sign appears as the antipode on the bidual:
$$
\eta_\epsilon=-\mathrm{id}_\epsilon.
$$
It is a functional-equation shadow only in the boundary sense.  The surviving
object is the finite-adele extension
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0,
$$
or equivalently the degree-$1$ class in
$\operatorname{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)$.

The no-Weyl-flip wall remains:
$$
\operatorname{Hom}^0_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0.
$$
Thus Pass 94 does not create a standard intertwiner, opposite unipotent, or
degree-$0$ Fourier/Weyl operator.  It records a boundary-only functional
equation, compatible with the Pass-81 no-functional-equation wall.

The finite checker
`artifacts/reports/pass94-all-prime-borel-jshriek-solid-dual-check.json`
verifies the signed transpose rule, duality squared, support-dual behavior,
the solid identity $D\epsilon=\mathbb Q[-1]$, the degree-$1$ finite-adele
boundary, and the absence of a degree-$0$ Weyl flip.
