def d(n):
    divisors = []
    for div in range(1, (n // 2) + 1):
        if n % div == 0:
            divisors.append(div)

    return sum(divisors)


def solve():
    amicables = []
    ns = [*range(1, 10_001)]
    for n in ns:
        b = d(n)
        a = d(b)
        if b != a and a == n:
            amicables.append(a)
            ns.remove(a)
            amicables.append(b)
            ns.remove(b)

    return sum(amicables)
