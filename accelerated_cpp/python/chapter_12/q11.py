# Chapter 12, exercise 11: split, frame, vcat and hcat using Str and Vec.
from str_class import Str
from vec import Vec


def split(s):
    ret = Vec()
    i = 0
    while i != s.size():
        while i != s.size() and s[i].isspace():
            i += 1
        j = i
        while j != s.size() and not s[j].isspace():
            j += 1
        if i != j:
            ret.push_back(Str(s._value[i:j]))
            i = j
    return ret


def other_split(s):
    """The find_if-based split from §6.1.1."""
    ret = Vec()
    chars = list(s)
    n = len(chars)
    i = 0
    while i != n:
        while i != n and chars[i].isspace():
            i += 1
        j = i
        while j != n and not chars[j].isspace():
            j += 1
        if i != n:
            ret.push_back(Str(chars[i:j]))
        i = j
    return ret


def width(v):
    return max((x.size() for x in v), default=0)


def frame(v):
    ret = Vec()
    maxlen = width(v)
    border = Str(maxlen + 4, "*")
    ret.push_back(border)
    for x in v:
        ret.push_back("* " + x + Str(maxlen - x.size(), " ") + " *")
    ret.push_back(border)
    return ret


def vcat(top, bottom):
    ret = Vec(iterable=top)
    for x in bottom:
        ret.push_back(x)
    return ret


def hcat(left, right):
    ret = Vec()
    width1 = width(left) + 1
    i = j = 0
    while i != left.size() or j != right.size():
        s = Str()
        if i != left.size():
            s = Str(left[i])
            i += 1
        s += Str(width1 - s.size(), " ")
        if j != right.size():
            s += right[j]
            j += 1
        ret.push_back(s)
    return ret


def main():
    f1 = frame(split(Str("Hello, world!")))
    f2 = frame(other_split(Str("Goodbye, world!")))
    for line in vcat(f1, f2):
        print(line)
    for line in hcat(f1, f2):
        print(line)


if __name__ == "__main__":
    main()
