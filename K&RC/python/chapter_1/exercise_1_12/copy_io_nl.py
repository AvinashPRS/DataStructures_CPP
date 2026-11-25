"""Exercise 1-12: print the input one word per line."""
import sys

BLANKS = (" ", "\t", "\n")


def main():
    previous_character = ""
    out = sys.stdout

    for character in sys.stdin.read():
        if character in BLANKS:
            if previous_character not in BLANKS:
                out.write("\n")
        else:
            out.write(character)

        previous_character = character


if __name__ == "__main__":
    main()
