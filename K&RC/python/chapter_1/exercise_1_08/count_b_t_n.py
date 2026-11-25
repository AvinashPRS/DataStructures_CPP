"""Exercise 1-8: count blanks, tabs and newlines."""
import sys


def main():
    blanks_nr = 0
    tabs_nr = 0
    newlines_nr = 0

    for c in sys.stdin.read():
        if c == " ":
            blanks_nr += 1
        elif c == "\t":
            tabs_nr += 1
        elif c == "\n":
            newlines_nr += 1

    print("blanks_nr: %d\ntabs_nr: %d\nnewlines_nr: %d"
          % (blanks_nr, tabs_nr, newlines_nr))


if __name__ == "__main__":
    main()
