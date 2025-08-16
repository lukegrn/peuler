def is_palidromatic(n):
    lst = [x for x in str(n)]
    while len(lst) > 1:
        if lst[0] != lst[-1]:
            return False

        lst.pop(0)
        lst.pop()

    return True


def solve():
    return max(
        [
            x * y
            for x in range(100, 1000)
            for y in range(100, 1000)
            if is_palidromatic(x * y)
        ]
    )
