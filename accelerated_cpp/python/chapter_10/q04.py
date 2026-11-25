# Chapter 10, exercise 4: use StringList; pop the values in reverse.
from string_list import StringList


def main():
    lst = StringList()
    lst.push_back("test")
    lst.push_back("list")
    lst.push_back("string")

    values = []
    while lst.size() > 0:
        values.append(lst.pop_back())
    print("values are: " + ", ".join(values))


if __name__ == "__main__":
    main()
