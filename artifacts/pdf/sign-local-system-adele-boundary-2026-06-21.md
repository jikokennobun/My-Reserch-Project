# Sign Local System Through the Finite-Adele Boundary

Autonomous discussion Pass 102 pushes the Pass-101 sign local system through
the primitive collapse and the all-prime constant-term boundary.

After a primitive collapse $T_S\to\mathbb Q/\mathbb Z$, the one-generator unit
extension is
$$
\beta=[0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0].
$$
The all-prime constant-term row is
$$
\delta_\epsilon=[0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0],
\qquad
\epsilon=\mathbb A_f/\mathbb Q.
$$

The $\mathbb Z/2$ sign local system acts by multiplying these boundary/Yoneda
classes:
$$
\beta\mapsto\sigma\beta,\qquad
\delta_\epsilon\mapsto\sigma\delta_\epsilon,
\qquad \sigma\in\{\pm1\}.
$$
Thus the sign is not a new boundary object.  It is the coefficient system on
the one-dimensional boundary line spanned by the extension class.

At finite level $N$, the unit extension has Bockstein shadow
$$
1\in\operatorname{Ext}^1(\mathbb Z/N,\mathbb Z)\cong\mathbb Z/N.
$$
The signed class is $\pm1\in\mathbb Z/N$.  This sign is visible exactly when
$N>2$ and collapses for $N=2$.

The finite-adele boundary morphism
$$
\partial_\epsilon:\epsilon\to\mathbb Q[1]
$$
is the shifted class behind
$$
D\epsilon\simeq\mathbb Q[-1].
$$
A one-sided sign change negates this class.  Applying the sign on both source
and target multiplies the class by $(-1)^2=1$, so biduality remains
involutive.

The coarse antipode quotient alone is still insufficient because it forgets
whether the class is $+\delta_\epsilon$ or $-\delta_\epsilon$.  The
$\mathbb Z/2$ local system is sufficient for the finite sign bookkeeping, and
it does not create a degree-$0$ Weyl/Fourier map $\epsilon\to\mathbb Q$.

The next task is to package this signed boundary class as a natural
transformation over finite conductor reductions and compare it with the
CRT-acyclic finite constant-term complexes.

The checker
`artifacts/reports/pass102-sign-local-system-adele-boundary-check.json`
verifies finite Bockstein sign classes, signed primitive collapse
surjectivity, support-transport preservation, one-sided Yoneda negation,
two-sided biduality involutivity, and sufficiency of the sign local system.
