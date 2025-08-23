def n_to_w(n):
    roots = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    if n < len(roots):
        return roots[n]

    if n < 100:
        return tens[n // 10] + n_to_w(n % 10)

    if n < 1000:
        return (
            n_to_w(n // 100)
            + "hundred"
            + ("and" if not n % 100 == 0 else "")
            + n_to_w(n % 100)
        )

    return "onethousand"


def solve():
    return sum([len(n_to_w(n)) for n in range(1, 1001)])
