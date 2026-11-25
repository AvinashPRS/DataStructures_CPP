# Chapter 15, exercise 2: frame with separate corner and side characters.
from pic import Picture, frame


def main():
    print(frame(Picture(["Hello,", "World!"])))


if __name__ == "__main__":
    main()
