'''
Get primes using a sieve. Ex: 18 -> [2,3,5,7,11,13,17]
'''

##returns numbers up to an including the number given that are prime
def get_primes(number):
    primes = []
    ##Everything starts out prime, but will be removed as we go
    is_prime = [False, False] + [True] * (number - 1) ##0 and 1 are not prime

    for p in range(2, number+1): ##inclusive boundary, so add one to index
        ##everything starts with a prime, so if we start with p (2 is the smallest
        ##prime so we start there), then we keep that.
        if is_prime[p]:
            primes.append(p)
            ##Now, we seive out any multiple of 2 by looping through all of the
            ##values in increments of p
            for i in range(p, number+1, p):
                is_prime[i] = False

    return primes

print(get_primes(180000))
#[Finished in 1.43s]

###From EPI
def get_primes_optimized(n):
    if n<2:
        return []

    size = (n - 3) // 2 + 1
    primes = [2]

    ##Again, everything starts prime, and then get rid of nonprimes
    is_prime = [True] * size

    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            for j in range(2*i**2 + 6*i + 3, size, p):
                is_prime[j] = False

    return primes

print(get_primes_optimized(180000))
#[Finished in 1.375s], slightly faster
