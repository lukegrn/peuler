from importlib import import_module
import sys


def main():
    if len(sys.argv) != 2:
        print(
            "Incorrect number of arguments provided. Usage: python main.py <problem number>",
            file=sys.stderr,
        )

        exit(1)
    else:
        try:
            problem = import_module(f"problems.{sys.argv[-1]}")
        except ModuleNotFoundError:
            print(
                f"Unable to find problem {sys.argv[-1]}. Ensure module exists",
                file=sys.stderr,
            )
            exit(1)

        try:
            print(problem.solve())
        except AttributeError:
            print("Solve method not implemented", file=sys.stderr)
            exit(1)


if __name__ == "__main__":
    main()
