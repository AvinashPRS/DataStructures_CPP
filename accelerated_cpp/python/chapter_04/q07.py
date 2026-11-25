# Chapter 4, exercise 7: average of the numbers read.
import sys


def main():
    print("Enter doubles, followed by end-of-file: ")
    doubles = [float(t) for t in sys.stdin.read().split()]
    if not doubles:
        print("No numbers were entered.")
        return
    print(f"The average is: {sum(doubles) / len(doubles):g}")


if __name__ == "__main__":
    main()
