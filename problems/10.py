def solve():
    primes = [2]
    n = 3

    while n < 2_000_000:
        for prime in primes:
            if n % prime == 0:
                break
            elif prime**2 > n:
                primes.append(n)
                break

        n += 1

    return sum(primes)
