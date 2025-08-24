from pathlib import Path
from inspect import stack
from os import path


def file():
    """To be called specifically from a solutions/<n>.py file.
    Will return the raw text data from files/<n>.txt"""

    file = path.basename(Path(stack()[1][1])).replace("py", "txt")
    dir = path.dirname(path.realpath(__file__)).replace("utils", f"files/{file}")

    with open(dir) as data:
        return data.read()
