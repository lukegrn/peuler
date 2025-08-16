def fib_generator():
    m = 1
    n = 1

    while n < 4_000_000:
        yield n
        m, n = n, m + n


def solve():
    return sum([x for x in fib_generator() if x % 2 == 0])
