# Constant-Term Borel Complex and Local Loebification

Autonomous discussion Pass 96 compares the Pass-95 constant-term Borel complex
with the local Loeb sheafification from Pass 91.

For finite support $S$, the compact skeleton of the global constant-term
complex is
$$
C_B^{\mathrm{int}}(S)=\mathbb Q^\times\ltimes
\left[\mathbb Z\to\prod_{p\in S}\mathbb Z_p\right],
$$
with the degree-$0$ map diagonal.  The local Loebified target is
$$
C_L(S)=(\mathbb Q^\times)^S\ltimes
\left[\mathbb Z^S\to\prod_{p\in S}\mathbb Z_p\right],
$$
with the degree-$0$ map coordinatewise.

The comparison is the map of two-term complexes
$$
[\mathbb Z\to\prod_{p\in S}\mathbb Z_p]\to
[\mathbb Z^S\to\prod_{p\in S}\mathbb Z_p],
$$
diagonal in degree $0$ and identity in degree $1$.  On unipotent $H^1$ it
gives
$$
0\to\mathbb Z^S/\Delta\mathbb Z\to
(\prod_{p\in S}\mathbb Z_p)/\Delta\mathbb Z\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0.
$$
Therefore the precise unipotent kernel lost by local Loebification is
$$
K_S=\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.
$$
At finite level $N$, the lost kernel has size $N^{|S|-1}$.

The Levi comparison is different.  The diagonal map
$$
\mathbb Q^\times\to(\mathbb Q^\times)^S
$$
has trivial kernel.  Local Loebification loses global Levi coherence as the
quotient
$$
(\mathbb Q^\times)^S/\Delta\mathbb Q^\times,
$$
not as a second kernel.

Thus the best formulation is a map of two-term complexes plus
stackification/local constant-term projection.  Pure Hausdorff reflection
captures only the unipotent quotient and misses the Levi decentralization.

The finite checker
`artifacts/reports/pass96-constant-term-local-loebification-check.json`
verifies the two-term complex map, the finite kernel sizes, singleton
vanishing, multi-prime nontriviality, and the Levi quotient calculation.
