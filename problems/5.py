from functools import reduce


def solve():
    needs_to_divide_by = range(11, 21)  # 11-20 covers 1-10 also

    i = 20
    while True:
        smallest_multiple = True
        for req in needs_to_divide_by:
            if i % req != 0:
                smallest_multiple = False
                break
        if smallest_multiple:
            return i

        i += 20
