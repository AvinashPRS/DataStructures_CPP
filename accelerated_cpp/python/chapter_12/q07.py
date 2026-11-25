# Chapter 12, exercise 7: iterate over a Str.
from str_class import Str


def main():
    s = Str("Hello, world!")
    for c in s:
        print(c, end="")
    print()


if __name__ == "__main__":
    main()
