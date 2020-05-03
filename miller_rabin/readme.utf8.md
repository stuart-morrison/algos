# Determinstic Miller-Rabin primality test

For a prime number <img src="https://render.githubusercontent.com/render/math?math=p">, let <img src="https://render.githubusercontent.com/render/math?math=q = p-1"> such that <img src="https://render.githubusercontent.com/render/math?math=p">$q = 2^{s}\cdot d$ where <img src="https://render.githubusercontent.com/render/math?math=s"> is a positive integer and <img src="https://render.githubusercontent.com/render/math?math=d = 1 (\text{mod} 2)">, Then, for all <img src="https://render.githubusercontent.com/render/math?math=a \in \mathbb{Z}/n\mathbb{Z}">, then:
<img src="https://render.githubusercontent.com/render/math?math=a^{d} = 1 (\text{mod} p)">
or <img src="https://render.githubusercontent.com/render/math?math=\exists r \in [0, s-1]"> such that:
<img src="https://render.githubusercontent.com/render/math?math=a^{2^{r}\cdot d} = -1 (\text{mod} p)">

The deterministic Miller-Rabin tests the contrapositive, ie, if <img src="https://render.githubusercontent.com/render/math?math=\exists a \in \mathbb{Z}/n\mathbb{Z}"> such that <img src="https://render.githubusercontent.com/render/math?math=a^{d} \new 1 (\text{mod} p)"> and <img src="https://render.githubusercontent.com/render/math?math=a^{2^{r}\cdot d} = -1 (\text{mod} p) \forall r \in [0, s-1]">, then <img src="https://render.githubusercontent.com/render/math?math=p"> is not prime.

The test is required to test <img src="https://render.githubusercontent.com/render/math?math=a < 2(\log n)^{2}">. However, for <img src="https://render.githubusercontent.com/render/math?math=p < 3,317,044,064,679,887,385,961,981">, it is only necessary to test a handful of <img src="https://render.githubusercontent.com/render/math?math=a">.

Source: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
