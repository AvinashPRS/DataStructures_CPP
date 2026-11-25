# Chapter 6, exercise 1: frame and hcat written with iterators.


def width(v):
    return max((len(s) for s in v), default=0)


def frame(v):
    maxlen = width(v)
    border = "*" * (maxlen + 4)
    return [border] + ["* " + s + " " * (maxlen - len(s)) + " *" for s in v] + [border]


def hcat(left, right):
    ret = []
    width1 = width(left) + 1
    it, jt = iter(left), iter(right)
    for _ in range(max(len(left), len(right))):
        s = next(it, "")
        s += " " * (width1 - len(s))
        s += next(jt, "")
        ret.append(s)
    return ret


def main():
    left = ["hello", "my name", "is Altug"]
    right = ["I am", "programming", "in Python!"]
    for line in hcat(frame(left), frame(right)):
        print(line)


if __name__ == "__main__":
    main()
