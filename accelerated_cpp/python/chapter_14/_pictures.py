# split/frame/vcat/hcat over any Str class (used by exercises 14-5, 14-6).


def make_picture_functions(Str):
    def split(s):
        ret = []
        i = 0
        while i != s.size():
            while i != s.size() and s[i].isspace():
                i += 1
            j = i
            while j != s.size() and not s[j].isspace():
                j += 1
            if i != j:
                ret.append(Str([s[k] for k in range(i, j)]))
                i = j
        return ret

    def other_split(s):
        chars = list(s)
        ret = []
        i = 0
        while i != len(chars):
            while i != len(chars) and chars[i].isspace():
                i += 1
            j = i
            while j != len(chars) and not chars[j].isspace():
                j += 1
            if i != len(chars):
                ret.append(Str(chars[i:j]))
            i = j
        return ret

    def width(v):
        return max((x.size() for x in v), default=0)

    def frame(v):
        maxlen = width(v)
        border = Str(maxlen + 4, "*")
        ret = [border]
        for x in v:
            ret.append("* " + x + Str(maxlen - x.size(), " ") + " *")
        ret.append(border)
        return ret

    def vcat(top, bottom):
        return list(top) + list(bottom)

    def hcat(left, right):
        ret = []
        width1 = width(left) + 1
        i = j = 0
        while i != len(left) or j != len(right):
            s = Str()
            if i != len(left):
                s = Str(left[i])
                i += 1
            s += Str(width1 - s.size(), " ")
            if j != len(right):
                s += right[j]
                j += 1
            ret.append(s)
        return ret

    def demo():
        f1 = frame(split(Str("Hello, world!")))
        f2 = frame(other_split(Str("Goodbye, world!")))
        for line in vcat(f1, f2):
            print(line)
        for line in hcat(f1, f2):
            print(line)

    return demo
