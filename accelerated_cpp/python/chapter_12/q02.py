# Chapter 12, exercise 2: c_str, data and copy.
from str_class import Str


def main():
    s = Str("Hello, world!")
    print(s.c_str())
    print(s.data())
    msg = s.copy(5)  # copy the first 5 characters
    print("".join(msg))


if __name__ == "__main__":
    main()
