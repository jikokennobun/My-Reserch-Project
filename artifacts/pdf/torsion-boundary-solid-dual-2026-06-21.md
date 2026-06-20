# Torsion Boundary and Solid Dual

Autonomous discussion Pass 98 compares the Pass-97 torsion boundary with the
Pass-94 all-prime solid dual.

For finite support $S$, the regraded torsion boundary is
$$
T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)
\cong K_{\mathbb Q,S}/K_{\mathbb Z,S}.
$$
It has finite shadows
$$
|T_S[N]|=N^{|S|-1}.
$$
This recovers the compact Pass-96 shadow after rationalization, while the
divisible rational kernel satisfies
$$
K_{\mathbb Q,S}/N K_{\mathbb Q,S}=0.
$$

The comparison with the solid dual is not raw object equality.  The Pass-94
all-prime boundary is
$$
D\epsilon\simeq\mathbb Q[-1],
\qquad
\epsilon=\widehat{\mathbb Z}/\mathbb Z,
$$
which is shifted.  By contrast, $T_S$ is a degree-$0$ torsion coefficient.

The bridge is the canonical unit extension
$$
0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0.
$$
Applying the extension/solid-dual passage sends each independent
$\mathbb Q/\mathbb Z$ coordinate in $T_S$ to one shifted
$\mathbb Q[-1]$ constant-term obstruction generator.  Therefore
$T_S\cong(\mathbb Q/\mathbb Z)^{|S|-1}$ presents $|S|-1$ finite-support copies
of the generator before the all-prime boundary is collapsed to its universal
form.

The finite multiplicity $|S|-1$ is local-support bookkeeping.  The
$\mathbb Q/\mathbb Z$ coefficient itself is not a separate artifact: it is the
torsion presentation of the same shifted constant-term obstruction whose
solid-dual form is $\mathbb Q[-1]$.  The bridge does not produce a degree-$0$
Weyl/Fourier map $\epsilon\to\mathbb Q$, so it remains compatible with the
Pass-94 no-Weyl wall.

The checker
`artifacts/reports/pass98-torsion-boundary-solid-dual-check.json`
verifies the torsion counts, support projections, raw non-equality with the
shifted solid dual, and compatibility with the canonical extension bridge.
