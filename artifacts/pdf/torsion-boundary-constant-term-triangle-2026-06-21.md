# Torsion Boundary to Constant-Term Triangle

Autonomous discussion Pass 99 constructs the exact bridge from the
finite-support torsion boundary to the all-prime constant-term complex.

The finite-support triangle is
$$
K_{\mathbb Z,S}\to K_{\mathbb Q,S}\to T_S\to K_{\mathbb Z,S}[1],
$$
where
$$
K_{\mathbb Z,S}=\mathbb Z^S/\Delta\mathbb Z,\qquad
K_{\mathbb Q,S}=\mathbb Q^S/\Delta\mathbb Q,\qquad
T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z).
$$

A collapse from $T_S$ to the one-generator boundary
$\mathbb Q/\mathbb Z$ is not canonical.  It requires a primitive zero-sum
functional
$$
c=(c_p)_{p\in S}\in\mathbb Z^S,\qquad
\sum_{p\in S}c_p=0,\qquad
\gcd_{p\in S}(c_p)=1.
$$
The zero-sum condition makes $c$ descend through the diagonal quotients, and
primitivity makes
$$
T_S\to\mathbb Q/\mathbb Z
$$
surjective.

For $r=|S|-1$ and finite level $N$, this gives
$$
T_S[N]\twoheadrightarrow(\mathbb Q/\mathbb Z)[N],
\qquad
|\ker|=N^{r-1}=N^{|S|-2}.
$$
Thus the chosen collapse preserves the one-generator finite shadow and records
the remaining finite-support degrees in the kernel.

After choosing $c$, the finite triangle maps to the unit extension
$$
\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to\mathbb Z[1],
$$
and then to the all-prime constant-term row
$$
[\mathbb Q\to\mathbb A_f],
\qquad
H^1=\epsilon=\mathbb A_f/\mathbb Q.
$$

The antipode sends $c$ to $-c$, so it negates the boundary class.  The sign is
visible over $\mathbb Z$ and invisible mod $2$, matching the finite signed-dual
behavior from Pass 94.  The target remains shifted through
$D\epsilon\simeq\mathbb Q[-1]$, so no degree-$0$ Weyl/Fourier map
$\epsilon\to\mathbb Q$ is produced.

The main new point is that the collapse from $|S|-1$ finite-support boundary
coordinates to one all-prime generator is an orientation choice, not a plain
support limit.  The next task is to track this orientation torsor under
support inclusions and projections.

The checker
`artifacts/reports/pass99-torsion-boundary-constant-term-triangle-check.json`
verifies the descent, surjectivity, finite kernel sizes, antipode sign, and
no-Weyl compatibility.
