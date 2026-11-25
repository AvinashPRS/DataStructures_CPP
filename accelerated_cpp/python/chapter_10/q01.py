# Chapter 10, exercise 1: report letter grades (§10.3/178).
from _paths import use_chapter

use_chapter(9)
from _read_all import read_all  # noqa: E402
from student_info import StudentInfo, compare  # noqa: E402

NUMBERS = (97, 94, 90, 87, 84, 80, 77, 74, 70, 60, 0)
LETTERS = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F")


def letter_grade(grade):
    for number, letter in zip(NUMBERS, LETTERS):
        if grade >= number:
            return letter
    return "???"


def main():
    students, maxlen = read_all(StudentInfo)
    students.sort(key=compare)
    for s in students:
        print(s.name() + " " * (maxlen + 1 - len(s.name())), end="")
        try:
            print(letter_grade(s.grade()))
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
