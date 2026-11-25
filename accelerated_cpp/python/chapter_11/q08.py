# Chapter 11, exercise 8: a simplified linked list class.
from lis import Lis


def main():
    lst = Lis()
    for v in (1, 2, 5, 4):
        lst.push_back(v)

    it = lst.begin()
    out = []
    while it != lst.end():
        out.append(str(it.get()))
        it.inc()
    print(" ".join(out) + " ")


if __name__ == "__main__":
    main()
