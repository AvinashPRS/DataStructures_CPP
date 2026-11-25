# Code taken from §5.8.1/92-93.


def width(v):
    return max((len(s) for s in v), default=0)


def frame(v):
    maxlen = width(v)
    border = "*" * (maxlen + 4)
    ret = [border]
    for s in v:
        ret.append("* " + s + " " * (maxlen - len(s)) + " *")
    ret.append(border)
    return ret
