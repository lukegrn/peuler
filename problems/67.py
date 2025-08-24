import os

from utils.util import file

cache = {}


def max_path_value(tree: list[list[int]], x: int = 0, y: int = 0):
    if f"{x},{y}" not in cache:

        if y == len(tree) - 1:
            cache[f"{x},{y}"] = tree[y][x]
        else:
            cache[f"{x},{y}"] = tree[y][x] + max(
                [max_path_value(tree, x, y + 1), max_path_value(tree, x + 1, y + 1)]
            )

    return cache[f"{x},{y}"]


def solve():
    data = file()

    tree = [[int(i) for i in line.split(" ")] for line in data.strip().split("\n")]

    return max_path_value(tree)
