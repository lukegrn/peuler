def isAbundant(n: int) -> bool:
    return sum([div for div in range(1, (n // 2) + 1) if n % div == 0]) > n


def solve():
    abundants = [i for i in range(0, 28_124) if isAbundant(i)]
    cannot_be_sum = set(range(1, 28_124))

    for abundant_i in abundants:
        for abundant_j in abundants:
            cannot_be_sum.discard(abundant_i + abundant_j)

    return sum(cannot_be_sum)
