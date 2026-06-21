# Integral Equivariant Obstruction for Repair Sections

Autonomous discussion Pass 108 isolates the finite obstruction to making a
support-defect repair section both integral and support-symmetric.

Let $S$ be a finite support of size $n>1$ and let
$$
\Sigma_S:\mathbb Z^S\to\mathbb Z,\qquad
\Sigma_S((a_p)_{p\in S})=\sum_{p\in S} a_p .
$$
The symmetric group $\operatorname{Sym}(S)$ acts on $\mathbb Z^S$ by
permuting coordinates, while it acts trivially on $\mathbb Z$.  A
support-symmetric section of $\Sigma_S$ must send $1$ to an invariant vector.
The invariant lattice is
$$
(\mathbb Z^S)^{\operatorname{Sym}(S)}
=\mathbb Z\cdot \mathbf 1_S,
$$
where $\mathbf 1_S=(1,\ldots,1)$.  Since
$$
\Sigma_S(k\mathbf 1_S)=nk,
$$
the image of the invariant lattice is $n\mathbb Z$.  Therefore no integral
$\operatorname{Sym}(S)$-equivariant section of $\Sigma_S$ exists when $n>1$.

Over $\mathbb Q$ the obstruction disappears.  The barycentric vector
$$
s_{\mathrm{bar}}(1)=\frac{1}{n}\mathbf 1_S
$$
is invariant and has sum $1$, so it gives a rational support-symmetric
section.  More generally, an equivariant integral lift of $m\in\mathbb Z$
exists exactly when $n$ divides $m$.  Equivalently, the obstruction group is
$$
\mathbb Z/\Sigma_S((\mathbb Z^S)^{\operatorname{Sym}(S)})
\cong \mathbb Z/n\mathbb Z.
$$

This explains the relation to the Pass-107 torsor picture.  Basepoint
splittings $s_b(m)=m e_b$ are integral, but they break support symmetry.
The barycentric splitting is support-symmetric, but it is rational and has
denominator $n$.  Thus the finite repair sequence is split after choosing a
basepoint, while its symmetric normalization has a genuine denominator
obstruction.

The antipode does not change this conclusion.  Multiplying the boundary line
by the scalar sign $\pm 1$ commutes with coordinate permutations, and it
replaces the barycenter by $\pm \mathbf 1_S/n$ without changing its
denominator.  Hence the obstruction is a finite equivariance/denominator
obstruction, not a new $B\mathbb Z/2$ local-system class.

The checker
`artifacts/reports/pass108-integral-equivariant-repair-section-check.json`
verifies the invariant-lattice calculation, exact divisibility criterion,
denominator obstruction, barycentric transition behavior under support
inclusions, antipode independence, and overall PASS verdict.

The next task is to compute the rational transition
$e_{S,T}s_{\mathrm{bar},S}-s_{\mathrm{bar},T}$ for support inclusions
$S\subset T$, record its denominator and kernel class, and compare that
bookkeeping with finite conductor and CRT denominator data.
