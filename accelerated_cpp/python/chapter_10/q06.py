# Chapter 10, exercise 6: split a sentence into a StringList.
from split import split


def main():
    lst = split("string list test")
    print("Values: " + ", ".join(lst))


if __name__ == "__main__":
    main()
