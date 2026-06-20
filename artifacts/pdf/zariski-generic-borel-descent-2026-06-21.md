# Zariski/Generic Borel Descent

Autonomous discussion Pass 92 relocates the Pass-91 Borel descent obstruction
from the discrete singleton-prime cover to the finite Zariski/generic-point
site.

Let
$$
X_S=\{\eta\}\cup\{(p):p\in S\}
$$
with the generic-point topology, and let
$j:\{\eta\}\hookrightarrow X_S$ be the open generic point.  The cover
$U_p=\{\eta,(p)\}$ has full-simplex nerve, so constant coefficients are
connected and have no horizontal $H^1$ defect.

The Rosser/Borel obstruction is instead the unipotent $j_!$ class:
$$
H^1(X_S,j_!\underline{\mathbb Z})
\cong \operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^S)
\cong \mathbb Z^S/\Delta\mathbb Z
\cong \mathbb Z^{|S|-1}.
$$

Thus the Borel analogue of the Pass-63 ghost line is the low-degree semidirect
coefficient
$$
\mathfrak b_{j!}(S)=
\underline{\mathbb Q^\times}\ltimes j_!\underline{\mathbb Z}.
$$
The Levi remains degree-$0$ global data, while the unipotent radical carries
the $j_!$ cohomology.

Modulo $N$,
$$
|H^1(X_S,j_!\mathbb Z/N)|=N^{|S|-1},
$$
matching the finite diagonal descent kernel found in Pass 91.

With the dilation coefficient $\mathcal V$, the horizontal ghost embeds into
the total phantom
$$
H^1(X_S,j_!\mathcal V)\cong\widehat{\mathbb Z}_S/\mathbb Z.
$$
Pushing out along $\mathbb Z\to\mathbb Q$ gives the finite-adele extension
line, while the hyperbolic Borel
$\mathbb Q^\times\ltimes\epsilon$ realizes the same datum as a shear orbit.
The Levi rescales representatives and shear translates them, but neither
chooses a canonical zero section.

The finite checker
`artifacts/reports/pass92-zariski-generic-borel-descent-check.json` verifies
constant-coefficient vanishing, the $j_!$ rank $|S|-1$, finite mod-$N$ class
sizes, and the comparison with the finite-adele and hyperbolic Borel forms.
