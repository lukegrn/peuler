from math import sqrt


def solve():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = sqrt(a**2 + b**2)

            if c.is_integer() and a + b + c == 1000:
                return int(a * b * c)
