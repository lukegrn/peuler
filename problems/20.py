def fac(n):
    if n == 1:
        return n
    else:
        return n * fac(n - 1)


def solve():
    return sum([int(i) for i in str(fac(100))])
