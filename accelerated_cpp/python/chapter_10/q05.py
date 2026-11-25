# Chapter 10, exercise 5: iterate over a StringList forwards and backwards.
from string_list import StringList


def main():
    lst = StringList()
    lst.push_back("test")
    lst.push_back("list")
    lst.push_back("string")

    print("Values: " + ", ".join(lst))
    print("Values: " + ", ".join(reversed(lst)))


if __name__ == "__main__":
    main()
