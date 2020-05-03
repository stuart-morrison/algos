# Determinstic Miller-Rabin primality test

For a prime number $p$, let $q = p-1$ such that $q = 2^{s}\cdot d$ where $s$ is a positive integer and $d = 1 (\text{mod} 2)$, Then, for all $a \in \mathbb{Z}/n\mathbb{Z}$, then:
$$a^{d} = 1 (\text{mod} p)$$
or $\exists r \in [0, s-1]$ such that:
$$a^{2^{r}\cdot d} = -1 (\text{mod} p)$$

The deterministic Miller-Rabin tests the contrapositive, ie, if $\exists a \in \mathbb{Z}/n\mathbb{Z}$ such that $a^{d} \new 1 (\text{mod} p)$ and $a^{2^{r}\cdot d} = -1 (\text{mod} p)$ $\forall r \in [0, s-1]$, then $p$ is not prime.

The test is required to test $a < 2(\log n)^{2}$. However, for $p < 3,317,044,064,679,887,385,961,981$, it is only necessary to test a handful of $a$.

Source: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test