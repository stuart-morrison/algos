# Import libraries
import numpy as np
import sympy as sp
import time
import pandas as pd
import matplotlib.pyplot as plt

#### Deterministic Miller-Rabin
def miller_rabin(p):
    """An implementation of the deterministic Miller-Rabin test for primality.

    Parameters:
    p (int): A positive integer

    Returns:
    bool: If p is a prime number

    """

    # Return false if p is 1
    if p == 1:
        return False

    # Return true if p is 2
    if p == 2:
        return True

    # Return false if p is even
    if p % 2 == 0:
        return False

    # Evaluate q = p - 1
    q = p - 1

    # Find d, s such that (2 ** s)d = q
    d = q // 2
    while d % 2 == 0:
        d //= 2
    
    s = (q // d).bit_length() - 1

    # Find the set of 'a' candidates
    # See: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
    if p < 2047:
        a_set = [2]
    elif p <  1373653:
        a_set = [2, 3]
    elif p < 9080191:
        a_set = [31, 73]
    elif p < 25326001:
        a_set = [2, 3, 5]
    elif p < 3215031751:
        a_set = [2, 3, 5, 7]
    elif p < 4759123141:
        a_set = [2, 7, 61]
    elif p < 1122004669633:
        a_set = [2, 13, 23, 1662803]
    elif p < 2152302898747:
        a_set = [2, 3, 5, 7, 11]
    elif p < 3474749660383:
        a_set = [2, 3, 5, 7, 11, 13]
    elif p < 341550071728321:
        a_set = [2, 3, 5, 7, 11, 13,  17]
    elif p < 3825123056546413051:
        a_set = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif p < 18446744073709551616:
        a_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif p < 318665857834031151167461:
        a_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif p < 3317044064679887385961981:
        a_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,  41]
    else:
        a_set = range(2, min(p - 2, math.floor(2 * np.log(float(p)) ** 2)))

    # Test over each candidate
    for a in a_set:

        # Set the initial boolean if we might have found a candidat
        found_one = True

        # Find x = a ** d mod p
        x = pow(a, d, p)

        # Test if a ** d mod == 1 or == -1
        if x == 1 or x == q:
            found_one = False
     
        # Keep going if we pass r = 0
        if found_one:
            # Loop over r in [1, ..., s - 1]
            r = 1
            while r < s:
                
                # Find a ** (2 **r * d) mod p
                x = pow(a, (2 ** r) * d, p)
                
                # If x == -1 mod p, we haven't found a candidate
                if x == q:
                    found_one = False
                    break                 

                r += 1
        # If x== 1 for r = 0, and x == -1 for all 0 <= r <= s-1 then
        # p is not prime!
        if found_one:
            return False

    # Otherwise, we've found a prime!
    return True

#### Testing against other implementations
for i in range(2, 1000001):
    my_test = miller_rabin(i)
    sympy_test = sp.isprime(i)
    
    if not my_test and sympy_test:
        print("How do you not thing %i isn't prime?".fmt(i))

    if my_test and not sympy_test:
        print("How do you not thing %i is prime?".fmt(i))

#### Timing my implementation
# Set up a dataframe for recording time
timing_data = pd.DataFrame()

# Pop over a decent range of numbers and test primality
prime_index_ = 1
for i in range(3, 100000, 2):
    start_time = time.time()
    is_prime_ = miller_rabin(i)
    solve_time = time.time() - start_time
    if is_prime_: prime_index_ += 1
    timing_data = timing_data.append({'number': i, 'solve_time': solve_time, 
                                    'is_prime': is_prime_, 'prime_index': prime_index_}, 
    ignore_index = True)

# Plot the solve time for each prime
plt.bar(timing_data[timing_data['is_prime'] == 1]['prime_index'],
        timing_data[timing_data['is_prime'] == 1]['solve_time'] * 1_000_000,
        col = (135, 94, 97))
plt.xticks([x * 1000 for x in range(1, max(timing_data['prime_index'] // 1000))])
plt.xlabel("Prime number index")
plt.ylabel("Time to determine primality\n(micro seconds)")
plt.show()


