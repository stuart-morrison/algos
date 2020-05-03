# Import libraries
library(gmp)
library(iterators)
library(ggplot2)
library(dplyr)
library(tibble)

#### Deterministic Miller-Rabin
miller_rabin <- function(p) {

    # If p is submitted by a string, convert it to a big integer
    if (class(p) == "character") {
        p <- as.bigz(p)
    }
    
    # Return false if p is 1
    if (p == 1) return(FALSE)

    # Return true if p is 2
    if (p == 2) return(TRUE)

    # Return false if p is even
    if (p %% 2 == 0) return(FALSE)

    # Evaluate q = p - 1
    q = p - 1

    # Find d, s such that (2 ** s)d = q
    d = q %/% 2
    while (d %% 2 == 0){
        d = d %/% 2
    }

    s = log2(q %/% d)

    # Find the set of 'a' candidates
    # See) { https) {//en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
    if (p < 2047) {
        a_set = iter(c(2))
    } else if (p <  1373653) {
        a_set = iter(c(2, 3))
    } else if (p < 9080191) {
        a_set = iter(c(31, 73))
    } else if (p < 25326001) {
        a_set = iter(c(2, 3, 5))
    } else if (p < 3215031751) {
        a_set = iter(c(2, 3, 5, 7))
    } else if (p < 4759123141) {
        a_set = iter(c(2, 7, 61))
    } else if (p < 1122004669633) {
        a_set = iter(c(2, 13, 23, 1662803))
    } else if (p < 2152302898747) {
        a_set = iter(c(2, 3, 5, 7, 11))
    } else if (p < 3474749660383) {
        a_set = iter(c(2, 3, 5, 7, 11, 13))
    } else if (p < 341550071728321) {
        a_set = iter(c(2, 3, 5, 7, 11, 13,  17))
    } else if (p < 3825123056546413051) {
        a_set = iter(c(2, 3, 5, 7, 11, 13, 17, 19, 23))
    } else if (p < 18446744073709551616) {
        a_set = iter(c(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37))
    } else if (p < 318665857834031151167461) {
        a_set = iter(c(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37))
    } else if (p < 3317044064679887385961981) {
        a_set = iter(c(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,  41))
    } else {
        a_set = iter(seq(from = 2, to = as.integer(min(p - 2, floor(2 * log(p) ^ 2)))))
    }
    
    
    # Test over each candidate
    for (inx in 1:a_set$length) {
        a = nextElem(a_set)
        
        # Set the initial boolean if we might have found a candidat
        found_one = TRUE
    
        # Find x = a ** d mod p
        x = powm(a, d, p)
        
        # Test if a ** d mod == 1 or == -1
        if (x == 1 | x == q) found_one = FALSE
        
        # Keep going if we pass r = 0
        if (found_one) {
            # Loop over r in [1, ..., s - 1]
            r = 1
            while (r < s) {
                
                # Find a ** (2 **r * d) mod p
                x = powm(a, (2 ^ r) * d, p)
        
                # If x == -1 mod p, we haven't found a candidate
                if (x == q) {
                    found_one = FALSE
                    break                 
                }
                
                r = r + 1
                    
            }
            
            # If x== 1 for r = 0, and x == -1 for all 0 <= r <= s-1 then
            # p is not prime!
            if (found_one) return(FALSE)
        }
    }
    
    # Otherwise, we've found a prime!
    return(TRUE)
}


#### Testing timing
# Test over a whole bunch
iter_ = iter(seq(from = 3, to = 1000000, by = 2))

# Initialise the prime number index
prime_index = 1

# Initialise a data frame for data collection
timing_data <- tibble(number = 1:iter_$length,
                      prime_or_not = NA,
                      solve_time = NA_real_,
                      prime_index = NA_integer_)

# Record the time taken to determine primality
for (index in 1:iter_$length) {
    p = nextElem(iter_)
    start_time = Sys.time()
    is_prime = miller_rabin(p)
    time_taken = as.numeric(Sys.time() - start_time)
    
    if (is_prime) prime_index <- prime_index + 1
    
    timing_data$prime_or_not[index] <- is_prime
    timing_data$solve_time[index] <- time_taken
    timing_data$prime_index[index] <- prime_index
}

# Plot time taken
ggplot() +
    geom_col(data = timing_data %>% filter(prime_or_not),
             aes(x = prime_index, y = solve_time * 1000000),
             width = 1, fill = "#6bc5ac") +
    theme_bw() +
    labs(x = "Prime number index", y = "Time taken to determine if p is prime\n(micro seconds)")

























