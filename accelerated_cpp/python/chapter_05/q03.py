# Chapter 5, exercise 3: one program, container chosen by a single alias.
# Change `student_container` to `deque` to time the linked-list-like version.
import time
from collections import deque  # noqa: F401

import _ch04  # noqa: F401
from student_info import read_students

student_container = list
# student_container = deque


def extract_fails(students):
    fails = student_container()
    passes = student_container()
    for s in students:
        (fails if s.final_grade < 60 else passes).append(s)
    students.clear()
    students.extend(passes)
    return fails


def main():
    students = student_container(read_students())
    count = len(students)

    begin = time.process_time()
    extract_fails(students)
    end = time.process_time()

    print(f"Extracting fails for {count} students took {end - begin:g} seconds.")


if __name__ == "__main__":
    main()
