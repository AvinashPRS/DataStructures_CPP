"""
Merge two files (f1.txt and f2.txt) into a third file (m.txt).

YouTube lesson (C version): https://www.youtube.com/watch?v=Vuz-1zNq8hc
"""
import sys


def main():
    try:
        f1 = open("f1.txt", "r")
        f2 = open("f2.txt", "r")
        merge = open("m.txt", "w")
    except OSError:
        print("Error opening files.")
        return 1

    # write the contents of each file one after the other to the third file
    with f1, f2, merge:
        merge.write(f1.read())
        merge.write(f2.read())
    return 0


if __name__ == "__main__":
    sys.exit(main())
