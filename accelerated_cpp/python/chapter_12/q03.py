# Chapter 12, exercise 3: relational operators.
from str_class import Str


def main():
    s1, s2, s3 = Str("a"), Str("b"), Str("c")
    print(f"s1 is {'larger' if s1 > s2 else 'smaller'} than s2")
    print(f"s3 is {'smaller' if s3 < s1 else 'larger'} than s1")


if __name__ == "__main__":
    main()
