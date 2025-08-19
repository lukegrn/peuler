cache = {}


def handle(n):
    on_even = lambda n: n // 2
    on_odd = lambda n: 3 * n + 1

    if n not in cache:
        if n == 1:
            cache[n] = 1
        elif n % 2 == 0:
            cache[n] = handle(on_even(n)) + 1
        else:
            cache[n] = handle(on_odd(n)) + 1

    return cache[n]


def solve():
    return (
        max((v, i) for i, v in enumerate([handle(n) for n in range(1, 1_000_001)]))[1]
        + 1
    )
