# Chapter 3, exercise 6: avoid division by zero when no homework is entered.
import sys


def main():
    name = input("Please enter your first name: ").split()[0]
    print(f"Hello, {name}!")

    midterm, final = map(float, input("Please enter your midterm and final exam grades: ").split()[:2])

    print("Enter all your homework grades, followed by end-of-file: ", end="", flush=True)
    grades = [float(t) for t in sys.stdin.read().split()]

    homework = sum(grades) / len(grades) if grades else 0
    print(f"Your final grade is {0.2 * midterm + 0.4 * final + 0.4 * homework:.3g}")


if __name__ == "__main__":
    main()
