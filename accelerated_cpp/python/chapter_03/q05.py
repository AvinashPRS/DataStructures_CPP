# Chapter 3, exercise 5: keep track of grades for several students.
import sys


def main():
    hw_count = 3
    print("Please enter student name, followed by midterm grade, "
          f"final grade, and {hw_count} homework grades."
          " Send end-of-file to finish submitting.")

    tokens = sys.stdin.read().split()
    students = []
    grades = []
    i = 0
    record_len = 3 + hw_count
    while i + record_len <= len(tokens):
        students.append(tokens[i])
        midterm = float(tokens[i + 1])
        final = float(tokens[i + 2])
        hw_sum = sum(float(t) for t in tokens[i + 3:i + 3 + hw_count])
        grades.append(0.2 * midterm + 0.4 * final + 0.4 * hw_sum / hw_count)
        i += record_len

    for student, grade in zip(students, grades):
        print(f"Student {student}'s Final Grade: {grade:g}.")


if __name__ == "__main__":
    main()
