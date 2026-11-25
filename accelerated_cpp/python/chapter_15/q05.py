# Chapter 15, exercise 5: hcat centers the shorter picture vertically.
from pic import frame, hcat


def main():
    p1 = frame(["Hello,", "World!"])
    p2 = frame(["Greetings", "to", "planet", "Earth!"])
    print(hcat(p1, p2))
    print(hcat(p2, p1))


if __name__ == "__main__":
    main()
