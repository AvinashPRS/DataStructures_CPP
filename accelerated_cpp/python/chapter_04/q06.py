# Chapter 4, exercise 6: compute the final grade while reading.
from student_info import compare, read_students


def main():
    students = read_students()
    maxlen = max((len(s.name) for s in students), default=0)

    students.sort(key=compare)

    for s in students:
        print(s.name + " " * (maxlen + 1 - len(s.name)), end="")
        print(f"{s.final_grade:.3g}")
        print()


if __name__ == "__main__":
    main()
