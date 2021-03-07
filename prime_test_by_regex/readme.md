# Test for prime numbers by regular expressions

Tests whether a number is prime using regular expressions.

First, the value is converted to a unary string. 

The LHS of the regex, `^1?$`, tests whether the string is string `1` or the empty string, meaning the value is zero.

The RHS of the regex tests for groups of 1s (ie, factors) by `^(11+?)`, and whether there are any remainders after detecting the groups by `\\1+?$`.
