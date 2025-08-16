from functools import reduce


def solve():
    primes = [2]
    n = 3

    while len(primes) < 10_001:
        for prime in primes:
            if n % prime == 0:
                isPrime = False
                break
            elif prime**2 > n:
                primes.append(n)
                break

        n += 1

    return primes[-1]
