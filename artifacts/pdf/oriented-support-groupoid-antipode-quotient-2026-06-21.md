# Oriented-Support Groupoid and Antipode Quotient

Autonomous discussion Pass 101 packages primitive collapse choices as a signed
oriented-support action groupoid.

For finite support $S$ with $|S|\ge2$, keep the primitive orientation torsor
$$
\mathcal O_S=
\{c=(c_p)_{p\in S}\in\mathbb Z^S:
\sum_{p\in S}c_p=0,\ \gcd_{p\in S}(c_p)=1\}.
$$
An object is a pair $(S,c)$ with $c\in\mathcal O_S$.

For an inclusion $S\subseteq T$, a morphism
$(S,c)\to(T,d)$ is a sign $\sigma\in\{\pm1\}$ such that
$$
d=\sigma e_{S,T}(c),
$$
where $e_{S,T}$ is zero-extension.  Identities have sign $+1$, and
composition multiplies signs.  The antipode is the sign $-1$ morphism
$(S,c)\to(S,-c)$ over a fixed support, and it squares to the identity.

The coarse antipode quotient
$$
[c]=\{c,-c\}
$$
presents the primitive collapse line and hence the single all-prime generator,
but it loses the signed path label.  Therefore the plain quotient does not
retain the Pass-94 functional-equation sign.  The sign-preserving package is
the signed action groupoid itself, or equivalently the coarse quotient
equipped with its residual $\mathbb Z/2$ sign local system.

On finite $N$-torsion, the antipode acts by multiplication by $-1$ on
$(\mathbb Q/\mathbb Z)[N]$.  This sign is visible for $N>2$ and collapses at
$N=2$, matching the earlier finite signed-duality behavior.

The result preserves the sign of the shifted constant-term boundary generator
without creating a degree-$0$ Weyl/Fourier map $\epsilon\to\mathbb Q$.

The next task is to push this $\mathbb Z/2$ sign local system through
$[\mathbb Q\to\mathbb A_f]$ and identify the exact boundary or Yoneda class
representing biduality on $D\epsilon\simeq\mathbb Q[-1]$.

The checker
`artifacts/reports/pass101-oriented-support-groupoid-antipode-quotient-check.json`
verifies signed morphism closure, multiplicative composition, antipode
involutivity, coarse quotient sign loss, sign-local-system restoration, and
finite $N$-torsion sign visibility/collapse.
