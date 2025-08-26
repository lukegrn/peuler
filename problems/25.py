cache = {}


def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1

    cache[n] = fib(n - 1) + fib(n - 2) if n not in cache else cache[n]
    return cache[n]


def solve():
    i = 1
    while len(str(fib(i))) < 1000:
        i += 1

    return i
