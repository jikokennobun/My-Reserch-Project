# Conductor-Functorial Borel Torsors

Date: 2026-06-21

## Summary

Pass 90 makes the Pass-89 Borel-torsor theorem functorial across conductor and
radical supports.  The key correction is directional: support restriction is
canonical, but support enlargement is not a canonical map on the diagonal
quotient torsor.

For a finite prime support $S$, write
$$
P(S)=\left(\prod_{p\in S}\mathbb Z_p\right)/\Delta\mathbb Z.
$$
If $S\subseteq T$, coordinate projection descends to a well-defined
restriction $P(T)\to P(S)$.  Zero-insertion $P(S)\to P(T)$ does not descend
when new primes are added, because a diagonal shift in $S$ maps to a vector
with zeros in the new coordinates rather than to a diagonal shift in $T$.

## Main Claims

- **Support restriction.** For $S\subseteq T$, projection gives a canonical
  map $P(T)\to P(S)$.
- **No canonical insertion.** If $T\setminus S$ is nonempty, zero-insertion is
  a representative-level choice, not a quotient-level homomorphism
  $P(S)\to P(T)$.
- **Meet/join comparison.** Rad-incomparable supports compare by the meet span
  $P(S)\to P(S\cap T)\leftarrow P(T)$ and by a join arena $P(S\cup T)$ for
  gluing.
- **Finite Borel naturality.** The finite shadows
  $(\mathbb Z/N)^\times\ltimes\mathbb Z/N$ reduce along $N\mid N'$, preserving
  the unit class and singleton strict marked stabilizer.

## Machine Verification

`code/scripts/check-pass90.py` produced
`artifacts/reports/pass90-conductor-functorial-borel-torsors-check.json` with
overall PASS.  It checks radical support invariance, projection descent,
failure of zero-insertion under new primes, meet/join comparison rows, and
finite Borel reductions along conductor divisibility.

## Next Use

Pass 91 should decide whether the restriction/span Borel-torsor package is a
sheaf, stack, prestack, or descent-obstruction object over the finite
prime-cover site.
