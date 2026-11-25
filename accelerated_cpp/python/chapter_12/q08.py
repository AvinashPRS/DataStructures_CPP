# Chapter 12, exercise 8: getline for Str.
from str_class import CharStream, Str, getline


def main():
    s = Str()
    getline(CharStream(), s)
    print(s)


if __name__ == "__main__":
    main()
