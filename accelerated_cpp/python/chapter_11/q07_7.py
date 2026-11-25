# Chapter 11, exercise 7 (redo 5-8 with Vec): hcat with `s` outside the loop.
from vec import Vec


def width(v):
    return max((len(s) for s in v), default=0)


def hcat(left, right):
    ret = Vec()
    width1 = width(left) + 1
    i = j = 0
    s = ""
    while i != left.size() or j != right.size():
        if i != left.size():
            s = left[i]
            i += 1
        s += " " * (width1 - len(s))
        if j != right.size():
            s += right[j]
            j += 1
        ret.push_back(s)
    return ret


def main():
    picture = Vec(iterable=[
        "*************",
        "* hello     *",
        "* my name   *",
        "* is Altug! *",
        "*************",
    ])
    another_picture = Vec(iterable=[
        "***************",
        "* I am        *",
        "* programming *",
        "* in Python!  *",
        "***************",
        "  (extra row)  ",
    ])
    for line in hcat(picture, another_picture):
        print(line)


if __name__ == "__main__":
    main()
