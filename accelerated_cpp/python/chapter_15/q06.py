# Chapter 15, exercise 6: pictures using Vec<Str> instead of list[str].
from pic_re import Picture, Str, Vec, frame, hcat, vcat


def main():
    init = Vec()
    init.push_back(Str("Hello,"))
    init.push_back(Str("World!"))

    p = Picture(init)
    q = frame(p)
    r = hcat(p, q)
    s = vcat(q, r)
    t = frame(hcat(s, vcat(r, q)))
    print(t)
    t.reframe("#", "&", "<")
    print(t)


if __name__ == "__main__":
    main()
