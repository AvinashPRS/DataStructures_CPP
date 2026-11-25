# Chapter 5, exercise 2 (vector version): time extract_fails on a list.
# Usage: python q02_1.py < 1000.txt
import time

import _ch04  # noqa: F401
from student_info import read_students


def extract_fails(students):
    """Erase failing students one at a time (expensive for array lists)."""
    fails = []
    i = 0
    while i != len(students):
        if students[i].final_grade < 60:
            fails.append(students[i])
            del students[i]
        else:
            i += 1
    return fails


def main():
    students = read_students()
    count = len(students)

    begin = time.process_time()
    extract_fails(students)
    end = time.process_time()

    print(f"Extracting fails for {count} students took {end - begin:g} seconds.")


if __name__ == "__main__":
    main()
