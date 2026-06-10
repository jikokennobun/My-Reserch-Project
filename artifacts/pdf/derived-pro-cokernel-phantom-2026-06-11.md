# Derived Pro-Cokernel Recovery of the Loeb-Rosser Phantom

Date: 2026-06-11

## Abstract

Pass 68 explains why the all-prime phantom is invisible at every fixed finite conductor but
nonzero after applying the derived inverse limit.  The quotient
$$\widehat{\mathbb Z}/\mathbb Z$$
is recovered as a derived pro-cokernel.

## Main Result

Let
$$N_n=\operatorname{lcm}(1,\ldots,n).$$
At each level there is an exact sequence
$$0\to N_n\mathbb Z\to\mathbb Z\to\mathbb Z/N_n\mathbb Z\to0.$$
The finite map $\mathbb Z\to\mathbb Z/N_n\mathbb Z$ is surjective, and CRT identifies
$$\mathbb Z/N_n\mathbb Z\cong\prod_{p\mid N_n}\mathbb Z/p^{v_p(N_n)}\mathbb Z.$$
So the finite quotient by the diagonal is zero at every level.

The kernel tower $K_n=N_n\mathbb Z$ is non-Mittag-Leffler, with
$$\varprojlim K_n=0.$$
Applying the derived inverse limit gives
$$0\to\mathbb Z\to\varprojlim_n\mathbb Z/N_n\mathbb Z\to
\varprojlim\nolimits^1 K_n\to0.$$
Since $\varprojlim_n\mathbb Z/N_n\mathbb Z=\widehat{\mathbb Z}$,
$$\varprojlim\nolimits^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z.$$

## Verification

The checker `code/scripts/check-pass68.py` generated
`artifacts/reports/pass68-derived-pro-cokernel-phantom-check.json`.

Verified facts:

- the lcm tower is cofinal for moduli $1,\ldots,24$;
- CRT makes the finite cokernel zero at sampled levels;
- the kernel tower has unbounded image indices and is non-Mittag-Leffler;
- the kernel inverse limit is zero;
- completion prefixes grow while the finite cokernel remains zero.

## Remaining Gap

Pass 69 should identify this derived pro-cokernel class with the earlier Loeb-Rosser boundary
$\epsilon$ from the bicomplex/recollement construction, including the signed duality law
$D(\epsilon)=-\epsilon^\vee$.
