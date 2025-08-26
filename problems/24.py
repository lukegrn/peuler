def perms(chars: list[str]) -> list[list[str]]:
    if len(chars) == 1:
        return [chars]

    return [
        [start, *perm]
        for i, start in enumerate(chars)
        for perm in perms([char for j, char in enumerate(chars) if not j == i])
    ]


def solve():
    return "".join(
        perms(
            [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
            ]
        )[999_999]
    )
