# Chapter 5, exercise 8: hcat with `s` declared outside the loop.
# Because `s` is not reset each iteration, once the left picture runs out
# the stale last row of the left picture is reused. (In C++ the width
# computation underflows and throws; in Python the padding just goes empty.)
from frame import width


def hcat(left, right):
    ret = []
    width1 = width(left) + 1
    i = j = 0
    s = ""  # defined outside the loop on purpose
    while i != len(left) or j != len(right):
        if i != len(left):
            s = left[i]
            i += 1
        s += " " * (width1 - len(s))
        if j != len(right):
            s += right[j]
            j += 1
        ret.append(s)
    return ret


def main():
    picture = [
        "*************",
        "* hello     *",
        "* my name   *",
        "* is Altug! *",
        "*************",
    ]
    another_picture = [
        "***************",
        "* I am        *",
        "* programming *",
        "* in Python!  *",
        "***************",
        "  (extra row)  ",
    ]

    for line in hcat(picture, another_picture):
        print(line)


if __name__ == "__main__":
    main()
