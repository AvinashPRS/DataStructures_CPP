"""Exercise 7-1: convert upper case to lower or lower case to upper,
depending on the name it is invoked with, as found in argv[0].

run: ln -s case.py upper && python3 upper < case.py
     (or pass the mode explicitly: python3 case.py upper < case.py)
"""
import os
import sys


def parse_arg_list(argv):
    name = os.path.splitext(os.path.basename(argv[0]))[0]
    if len(argv) > 1:
        name = argv[1]
    if name == "lower":
        return str.lower
    if name == "upper":
        return str.upper
    return None


def main(argv):
    convert = parse_arg_list(argv)
    if convert is None:
        print("Error: invalid arguments.")
        return 1

    for c in iter(lambda: sys.stdin.read(1), ""):
        sys.stdout.write(convert(c))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
