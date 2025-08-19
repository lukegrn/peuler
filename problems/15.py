cache = {}


def solve(x=0, y=0):
    if f"{x},{y}" not in cache:
        if x == 20 and y == 20:
            cache[f"{x},{y}"] = 1
        elif x == 20:
            cache[f"{x},{y}"] = solve(x, y + 1)
        elif y == 20:
            cache[f"{x},{y}"] = solve(x + 1, y)
        else:
            cache[f"{x},{y}"] = solve(x, y + 1) + solve(x + 1, y)

    return cache[f"{x},{y}"]
