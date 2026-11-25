# Chapter 12, exercise 12: insert a range of characters into a Str.
from str_vec import Str


def main():
    s1 = Str("Hello, !")
    s2 = Str("world")
    s1.insert(7, s2)
    print(s1)


if __name__ == "__main__":
    main()
