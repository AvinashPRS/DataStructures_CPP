# Chapter 15, exercise 4: reframe an existing picture.
from pic import Picture, frame, hcat, vcat


def main():
    p = Picture(["Hello,", "World!"])
    q = frame(p)
    r = hcat(p, q)
    s = vcat(q, r)
    t = frame(hcat(s, vcat(r, q)))
    print(t)
    t.reframe("#", "&", "<")
    print(t)


if __name__ == "__main__":
    main()
