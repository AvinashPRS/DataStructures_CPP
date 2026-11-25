# Chapter 5, exercise 6: compare erase-based extract_fails against a
# version that copies passing records to the front and then resizes.
# Usage: python q06.py < 10000.txt
import copy
import time

import _ch04  # noqa: F401
from student_info import read_students


def extract_fails(students):
    """Code from §5.1.1/77, using the simplified student record."""
    fail = []
    i = 0
    while i != len(students):
        if students[i].final_grade < 60:
            fail.append(students[i])
            del students[i]
        else:
            i += 1
    return fail


def resizing_extract_fails(students):
    fail = []
    insert_pos = 0
    for s in students:
        if s.final_grade < 60:
            fail.append(s)
        else:
            students[insert_pos] = s
            insert_pos += 1
    del students[insert_pos:]
    return fail


def main():
    students = read_students()
    count = len(students)
    students_copy = copy.copy(students)

    begin = time.process_time()
    extract_fails(students)
    time_original = time.process_time() - begin

    begin = time.process_time()
    resizing_extract_fails(students_copy)
    time_modified = time.process_time() - begin

    print(f"Original function took {time_original:g} seconds and the modified "
          f"function took {time_modified:g} seconds for {count} students.")


if __name__ == "__main__":
    main()
