# Orientation Torsor Under Support Functoriality

Autonomous discussion Pass 100 studies how primitive collapse choices behave
when finite supports change.

For finite support $S$ with $|S|\ge2$, define the primitive orientation torsor
$$
\mathcal O_S=
\{c=(c_p)_{p\in S}\in\mathbb Z^S:
\sum_{p\in S}c_p=0,\ \gcd_{p\in S}(c_p)=1\}.
$$
An element $c\in\mathcal O_S$ represents a primitive collapse
$$
T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)
\twoheadrightarrow\mathbb Q/\mathbb Z.
$$
The antipode acts freely by $c\mapsto -c$.

For an inclusion $S\subseteq T$, the canonical operation is pullback along the
boundary projection $T_T\to T_S$.  On functionals this is zero-extension:
$$
e_{S,T}(c)_p=
\begin{cases}
c_p,&p\in S,\\
0,&p\in T\setminus S.
\end{cases}
$$
Zero-extension preserves zero-sum, primitivity, collapse compatibility, and
the antipode sign.  It is strictly functorial along support chains.

The reverse direction is not canonical.  Restriction of an orientation on a
larger support can fail to be zero-sum on the smaller support.  For example,
$$(1,1,-2)\in\mathcal O_{\{2,3,5\}}$$
restricts to $(1,1)$ on $\{2,3\}$, whose sum is nonzero.  Hence there is no
natural projection $\mathcal O_T\to\mathcal O_S$.

Finite kernels factor under zero-extension.  If $c\in\mathcal O_S$ is extended
to $T$, then the $N$-torsion kernel of the collapse on $T_T$ has size
$$
N^{|T|-2}=N^{|S|-2}\cdot N^{|T|-|S|}.
$$
The first factor is the old collapse kernel, and the second is the new support
kernel introduced by $T_T\to T_S$.

No support-symmetric primitive orientation exists.  A support-symmetric
integral functional is constant, and zero-sum forces it to be zero.  Therefore
the all-prime constant-term generator is obtained only after choosing,
quotienting, or forgetting the orientation torsor.

The next task is to package the oriented-support groupoid or stack explicitly
and compare its antipode quotient with the Pass-94 functional-equation sign.

The checker
`artifacts/reports/pass100-orientation-torsor-support-functoriality-check.json`
verifies zero-extension functoriality, restriction instability, kernel
factorization, antipode equivariance, and absence of a symmetric primitive
orientation.
