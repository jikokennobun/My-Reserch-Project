# Stackification Obstruction for Primitive Orientations

Autonomous discussion Pass 106 computes why primitive orientations over
finite supports do not form a restriction sheaf.

For $S\subseteq T$ and $d\in\mathcal O_T$, coordinate deletion has additive
defect
$$
\Delta_{T,S}(d)=\sum_{p\in S}d_p
=-\sum_{p\in T\setminus S}d_p.
$$
It lands in $\mathcal O_S$ only on the partial domain where this defect
vanishes and the deleted vector remains primitive.

The additive and primitivity obstructions are independent.  For example,
$$
(2,-2,1,-1)\in\mathcal O_{\{2,3,5,7\}}
$$
has zero additive defect on $\{2,3\}$, but restricts to $(2,-2)$, which is
not primitive.

Repairing a nonzero defect requires choosing a section of the summation map
$$
\Sigma_S:\mathbb Z^S\to\mathbb Z.
$$
There is no support-symmetric integer section for $|S|>1$, since such a
section would send $1$ to a constant vector $(k,\dots,k)$ and force
$|S|k=1$.  Based or ordered supports can make a repair choice, but the
basepoint or order is extra structure.

The correct universal statement is covariant.  The all-prime
primitive-orientation object is the zero-extension colimit
$$
\mathcal O_{\mathbb P}^{\mathrm{fin}}
=\operatorname*{colim}_S\mathcal O_S.
$$
Equivalently, it consists of primitive finitely supported zero-sum integer
functions on the set of all primes, modulo padded zero coordinates.  A family
of maps $F_S:\mathcal O_S\to X$ factors uniquely through this colimit exactly
when $F_T(e_{S,T}c)=F_S(c)$ for all $S\subseteq T$.

The antipode quotient $[c]=\{c,-c\}$ gives the coarse primitive orientation
line, but it forgets whether the boundary action is $+\delta_\epsilon$ or
$-\delta_\epsilon$.  The all-prime package must therefore retain the
$B\mathbb Z/2$ boundary-line local system.  No degree-$0$ Weyl/Fourier map
$\epsilon\to\mathbb Q$ is created.

The checker
`artifacts/reports/pass106-stackification-obstruction-primitive-orientations-check.json`
verifies the deletion-defect formula, partial restriction domain, nonunique
repairs, absence of support-symmetric sections, basepoint-dependence, the
zero-extension colimit universal property, and the antipode/local-system
distinction.

The next task is to model repair choices as torsors under $\ker\Sigma_S$ and
decide whether the support-defect data gives a genuine Cech/cosheaf
cohomology class or only an ordinary choice obstruction.
