# Chapter 15, exercise 1: build and print a composite picture.
from pic import Picture, frame, hcat, vcat


def main():
    p = Picture(["Hello,", "World!"])
    q = frame(p)
    r = hcat(p, q)
    s = vcat(q, r)
    print(frame(hcat(s, vcat(r, q))))


if __name__ == "__main__":
    main()
