# All-Prime Borel j_! Upgrade

Autonomous discussion Pass 93 upgrades the finite-support Borel $j_!$ class to
the honest all-prime $\mathrm{Spec}\,\mathbb Z$ setting.

The generic singleton $\{\eta\}$ is not open in honest
$\mathrm{Spec}\,\mathbb Z$: every nonempty basic open $D(n)$ contains all but
finitely many closed primes.  Thus the finite-support $j_!$ notation must be
read all-prime as a pro-open, continuous, or solid coefficient, not as ordinary
extension by zero from an open generic point.

The all-prime coefficient is
$$
\mathfrak B^{\mathrm{cont}}_{j!}
=\mathbb Q^\times\ltimes
R\!\varprojlim_{S\Subset\mathbb P}j_{S,!}\mathcal V_S,
$$
where $S$ ranges over finite prime supports and $\mathcal V_S$ is the dilation
coefficient from the finite recollement model.

For $S\subseteq T$, support restriction gives a surjection
$$
\mathbb Z^T/\Delta\mathbb Z\to\mathbb Z^S/\Delta\mathbb Z
$$
with kernel rank $|T|-|S|$; modulo $N$ its kernel has size
$N^{|T|-|S|}$.  The support direction is therefore Mittag-Leffler and adds no
new $\varprojlim^1$.  The nonzero derived content remains the per-prime
dilation tower inside $\mathcal V$.

The all-prime identity is:
$$
H^1_{\mathrm{cont}}(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)
\cong
\varprojlim_{S\Subset\mathbb P}H^1(X_S,j_{S,!}\mathcal V_S)
\cong
\widehat{\mathbb Z}/\mathbb Z.
$$

The global Levi $\mathbb Q^\times$ is retained.  Replacing it by a product of
local Levi factors would be the local Loeb sheafification, not the Rosser/Borel
torsor.  Pushing out along $\mathbb Z\to\mathbb Q$ gives
$$
0\to\mathbb Q\to\mathbb A_f\to\widehat{\mathbb Z}/\mathbb Z\to0,
$$
and the hyperbolic Borel $\mathbb Q^\times\ltimes\epsilon$ acts on this same
continuous shear class.

The finite checker
`artifacts/reports/pass93-all-prime-borel-jshriek-upgrade-check.json` verifies
the open-point distinction, support projection ranks, finite mod-$N$ kernels,
support-direction Mittag-Leffler behavior, and the all-prime Borel coefficient
with unipotent limit $\widehat{\mathbb Z}/\mathbb Z$.
