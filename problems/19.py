def solve():
    day = 1
    count = 0

    for y in range(1900, 2001):
        months = [
            31,
            29 if (y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0)) else 28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31,
        ]

        for month in months:
            for day_of_month in range(0, month):
                if day % 7 == 0 and day_of_month == 0 and not y == 1900:
                    count += 1
                day += 1

    return count
