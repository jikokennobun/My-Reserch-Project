# Signed Boundary Naturality Under Conductor Reduction

Autonomous discussion Pass 103 packages the signed boundary class as a natural
finite-conductor system and compares it with the Pass-95 CRT-acyclic
constant-term complexes.

For finite conductor $N$, write the signed finite Bockstein class as
$$
b_N^\sigma=\sigma\in\mathbb Z/N,\qquad \sigma\in\{\pm1\}.
$$
If $M\mid N$, conductor reduction satisfies
$$
\rho_{N,M}(b_N^\sigma)=b_M^\sigma.
$$
The sign local system is therefore natural over finite conductor reductions.
The only finite reduction that erases the sign is the target modulus $2$,
where $1=-1$.

The signed finite conductor form of the Pass-95 constant-term complex is
$$
C^\sigma_{B,N}=(\mathbb Z/N)^\times\ltimes
\left[\mathbb Z/N
\xrightarrow{d_N^\sigma}
\prod_{p^e\parallel N}\mathbb Z/p^e\right],
$$
with
$$
d_N^\sigma(x)=(\sigma x\bmod p^e)_{p^e\parallel N}.
$$
Since $\sigma=\pm1$ is a unit, $d_N^\sigma$ is still a CRT isomorphism.
Therefore every fixed signed finite conductor shadow is acyclic:
$$
H^0(C^\sigma_{B,N})=H^1(C^\sigma_{B,N})=0.
$$

For $M\mid N$, the signed CRT squares commute.  Reducing the source first and
then applying $d_M^\sigma$ gives the same result as applying $d_N^\sigma$ and
then reducing each prime-power coordinate.  Thus conductor reduction
introduces no sign-twisted finite obstruction beyond the known mod-$2$
collapse.

This does not alter the support warning from Pass 95: support projection is
canonical, but support enlargement remains only a finite CRT choice/span and
not a canonical all-prime diagonal-preserving map.

The next task is to assemble the signed finite conductor system into a
pro/solid all-prime boundary object and decide whether the orientation double
cover survives the all-prime limit or is absorbed by the local system on
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$.

The checker
`artifacts/reports/pass103-signed-boundary-conductor-naturality-check.json`
verifies signed finite CRT acyclicity, conductor-reduction naturality of
signed Bockstein classes, commutation of signed CRT squares, target-$2$ sign
collapse, and persistence of the support-enlargement caveat.
