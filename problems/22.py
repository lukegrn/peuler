from utils import util


def worth(name: str) -> int:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return sum([letters.find(char) + 1 for char in name])


def solve():
    data = [name.replace('"', "").strip() for name in util.file().split(",")]
    return sum([(i + 1) * worth(name) for i, name in enumerate(sorted(data))])
