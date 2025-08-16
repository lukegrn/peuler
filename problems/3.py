def is_prime(n, prime_lst):
    """
    Assumes that prime_lst contains all primes before n
    """
    for prime in prime_lst:
        if n % prime == 0:
            return False

    return True


def solve():
    num = 600_851_475_143
    prime_lst = [2]
    factors = []

    while num != 0:
        if prime_lst[-1] ** 2 > num:
            factors.append(num)
            break
        for prime in prime_lst:
            if num % prime == 0:
                factors.append(prime)
                num //= prime
            else:
                # calculate the next prime
                for n in range(prime, num):
                    if is_prime(n, prime_lst):
                        prime_lst.append(n)
                        break

    return factors[-1]
