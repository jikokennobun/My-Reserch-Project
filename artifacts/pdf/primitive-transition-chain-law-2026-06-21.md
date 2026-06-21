# Primitive Transition Chain Law

Autonomous discussion Pass 110 studies the primitive vectors obtained by
clearing barycentric transition denominators.

For finite supports $S\subset T$, define
$$
L_{S,T}=\operatorname{lcm}(|S|,|T|),
\qquad
\eta_{S,T}=L_{S,T}\tau_{S,T}.
$$
If $|S|=n$, $|T|=m$, and $g=\gcd(n,m)$, then $\eta_{S,T}$ has entries
$(m-n)/g$ on $S$ and $-n/g$ on $T\setminus S$.  It is an integral primitive
zero-sum vector in $K_T$.

For a chain $S\subset T\subset U$, let
$$
C=\operatorname{lcm}(L_{S,T},L_{T,U},L_{S,U}).
$$
Multiplying the rational coboundary identity by $C$ gives the exact integral
rescaling law

$$
\begin{aligned}
\frac{C}{L_{S,T}}e_{T,U}\eta_{S,T}
+\frac{C}{L_{T,U}}\eta_{T,U}
&=
\frac{C}{L_{S,U}}\eta_{S,U}.
\end{aligned}
$$

Thus primitive transition vectors do not usually compose strictly.  Strict
primitive composition occurs only in equal-conductor cases; otherwise the
coefficients $C/L_{A,B}$ are essential.  The useful support-edge datum is
therefore the weighted pair $(L_{S,T},\eta_{S,T})$, equivalently the rational
transition $\tau_{S,T}$, not the primitive line alone.

This mirrors the primitive repair torsor issue.  The rescaled chain law is
closed in the additive kernel $K_U$, but the common-conductor sum can be a
nonprimitive multiple of the endpoint vector.  Primitivity is an arithmetic
normalization inside additive kernel data, not a sub-cocycle condition.

The checker
`artifacts/reports/pass110-primitive-transition-chain-law-check.json`
verifies edge-vector primitivity, the weighted common-conductor chain law,
the strict-composition classification, failure of primitive lines to be
sufficient in general, and compatibility with the Pass-107 repair-torsor
warning.

The next task is to incorporate the Claude Code MacNeille reflection checker
review: add the non-lattice witness, correct or separate the antitone
completion closure rule, and record reflected/principal-unreflected
classifications.
