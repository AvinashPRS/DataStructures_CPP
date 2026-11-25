# Chapter 5, exercise 2 (list version): time extract_fails on a linked list.
# Python has no std::list, so collections.deque stands in for it; erasing
# is done by rotating through the deque, which is O(1) per element.
# Usage: python q02_2.py < 1000.txt
import time
from collections import deque

import _ch04  # noqa: F401
from student_info import read_students


def extract_fails(students):
    fails = deque()
    for _ in range(len(students)):
        s = students.popleft()
        if s.final_grade < 60:
            fails.append(s)
        else:
            students.append(s)
    return fails


def main():
    students = deque(read_students())
    count = len(students)

    begin = time.process_time()
    extract_fails(students)
    end = time.process_time()

    print(f"Extracting fails for {count} students took {end - begin:g} seconds.")


if __name__ == "__main__":
    main()
