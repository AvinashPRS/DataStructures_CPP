# Chapter 12, exercise 6: using a Str in a condition.
from str_class import Str


def main():
    s1 = Str()
    s2 = Str("Hello, world!")
    print(f"s1 is {'not empty' if s1 else 'empty'}")
    print(f"s2 is {'not empty' if s2 else 'empty'}")


if __name__ == "__main__":
    main()
