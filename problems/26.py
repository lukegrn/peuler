def get_cycle_len(n: int) -> int:
    len = 0
    repeats = False
    numerator = 10
    decs = []
    seen_numerators = []
    while numerator % n != 0:
        if numerator not in seen_numerators:
            seen_numerators.append(numerator)
            remainder = numerator % n
            decs.append(numerator // n)
            numerator = 10 * remainder
        else:
            repeats = True
            break

        len += 1

    return len if repeats else 0


def solve():
    max = 0
    d = 0
    for i in range(2, 1_001):
        len = get_cycle_len(i)
        d = i if len > max else d
        max = len if len > max else max
    return d
