# Chapter 7, exercise 2: group students by letter grade.
from _paths import use_chapter

use_chapter(4)
from student_info import compare, read_students  # noqa: E402


def letter(final_grade):
    if final_grade > 90:
        return "A"
    if final_grade > 80:
        return "B"
    if final_grade > 70:
        return "C"
    if final_grade > 60:
        return "D"
    return "F"


def main():
    students = sorted(read_students(), key=compare)

    grades = {}
    for s in students:
        grades.setdefault(letter(s.final_grade), []).append(s)

    for g in sorted(grades):
        article = "an " if g in ("A", "F") else "a "
        print(f"The student(s) who got {article}{g} are: " + ", ".join(s.name for s in grades[g]))


if __name__ == "__main__":
    main()
