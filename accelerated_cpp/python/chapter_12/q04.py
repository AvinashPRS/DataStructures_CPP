# Chapter 12, exercise 4: equality and inequality.
from str_class import Str


def main():
    s1 = Str("Hello, world!")
    s2 = Str("Goodbye, world!")
    s3 = Str("Hello, world!")
    print(f"s1 and s2 are {'equal' if s1 == s2 else 'not equal'}")
    print(f"s1 and s3 are {'equal' if s1 == s3 else 'not equal'}")


if __name__ == "__main__":
    main()
