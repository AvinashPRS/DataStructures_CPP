# Chapter 2, exercise 1: frame with no padding.
from framing import read_first_name, write_frame


def main():
    name = read_first_name()
    greeting = "Hello, " + name + "!"
    pad = 0
    write_frame(greeting, pad, pad)


if __name__ == "__main__":
    main()
