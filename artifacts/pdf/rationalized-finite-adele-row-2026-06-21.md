# Rationalized Finite-Adele Row

Autonomous discussion Pass 97 lifts the compact local-Loebification comparison
to the rationalized finite-adele skeleton.

For finite support $S$, the rationalized map of two-term complexes is
$$
[\mathbb Q\to\prod_{p\in S}\mathbb Q_p]\to
[\mathbb Q^S\to\prod_{p\in S}\mathbb Q_p],
$$
diagonal in degree $0$ and identity in degree $1$.  The induced map on
$H^1$ is
$$
(\prod_{p\in S}\mathbb Q_p)/\Delta\mathbb Q
\to
\prod_{p\in S}(\mathbb Q_p/\mathbb Q).
$$
Its kernel is
$$
K_{\mathbb Q,S}=\mathbb Q^S/\Delta\mathbb Q.
$$

Thus rationalization does not kill the compact kernel
$$
K_{\mathbb Z,S}=\mathbb Z^S/\Delta\mathbb Z.
$$
It embeds $K_{\mathbb Z,S}$ into a divisible $\mathbb Q$-vector boundary of
dimension $|S|-1$.

The finite shadow is regraded.  Since $K_{\mathbb Q,S}$ is divisible,
$$
K_{\mathbb Q,S}/N K_{\mathbb Q,S}=0.
$$
But
$$
K_{\mathbb Q,S}/K_{\mathbb Z,S}
\cong
(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)
$$
has $N$-torsion of size
$$
N^{|S|-1}.
$$
So the old finite shadow survives as torsion in the rational/integral
boundary quotient, not as a finite quotient of the rational kernel itself.

Support projections remain surjective after rationalization.  If
$S\subseteq T$, the projection
$$
K_{\mathbb Q,T}\to K_{\mathbb Q,S}
$$
has kernel of $\mathbb Q$-dimension $|T|-|S|$, so the support direction remains
Mittag-Leffler.

The checker
`artifacts/reports/pass97-rationalized-finite-adele-row-check.json`
verifies the rational kernel dimensions, finite-shadow regrading, exact
sequence, and support-projection behavior.
