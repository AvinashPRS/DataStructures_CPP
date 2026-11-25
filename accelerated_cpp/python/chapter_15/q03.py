# Chapter 15, exercise 3: user-chosen border characters.
from pic import Picture, frame


def main():
    print(frame(Picture(["Hello,", "World!"]), "-", "#", "@"))


if __name__ == "__main__":
    main()
