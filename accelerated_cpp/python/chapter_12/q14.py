# Chapter 12, exercise 14: construct a Vec<char> from a string.
from vec import Vec


def main():
    s = "Hello, world!"
    v = Vec(iterable=s)
    print("".join(v))


if __name__ == "__main__":
    main()
