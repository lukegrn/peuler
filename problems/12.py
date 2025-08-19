def solve():
    i = 1
    while True:
        next_tri = sum(range(1, i + 1))
        i += 1
        factors = [f for f in range(1, i + 1 // 2) if next_tri % f == 0]
        other_side = [next_tri // f for f in factors]

        if len(set([*factors, *other_side])) > 500:
            return next_tri
