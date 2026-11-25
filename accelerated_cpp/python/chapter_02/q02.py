# Chapter 2, exercise 2: different vertical and horizontal padding.
from framing import read_first_name, write_frame


def main():
    name = read_first_name()
    greeting = "Hello, " + name + "!"
    pad_vertical = 1
    pad_horizontal = 2
    write_frame(greeting, pad_vertical, pad_horizontal)


if __name__ == "__main__":
    main()
