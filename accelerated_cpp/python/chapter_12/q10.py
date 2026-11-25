# Chapter 12, exercise 10: construct a Str from a range of characters.
from str_vec import Str


def main():
    s1 = Str("Hello, world!")
    s2 = Str(s1[0:5])
    print(s2)


if __name__ == "__main__":
    main()
