# Chapter 12, exercise 13: Vec::assign from a range.
from vec import Vec


def main():
    v = Vec()
    v.assign_range("Hello, world!")
    print("".join(v))


if __name__ == "__main__":
    main()
