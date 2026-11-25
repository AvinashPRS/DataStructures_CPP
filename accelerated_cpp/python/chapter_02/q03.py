# Chapter 2, exercise 3: ask the user for the padding.
from framing import read_first_name, write_frame


def main():
    name = read_first_name()
    greeting = "Hello, " + name + "!"
    print()
    pad = int(input("Please enter the amount of spacing between the frame and the greeting: "))
    write_frame(greeting, pad, pad)


if __name__ == "__main__":
    main()
