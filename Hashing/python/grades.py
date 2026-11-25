"""
Accelerated C++ style grading program (map of letter grade -> students).

Reads records from stdin in the form:
    name midterm final hw1 hw2 hw3 ...
(one student per line), computes the final grade, then groups the students
by letter grade using a dict (ordered by key, like std::map).

Example:
    printf "Alice 90 95 100 90 98\\nBob 70 60 75 80\\n" | python3 grades.py
"""
import sys
from dataclasses import dataclass


def median(vec):
    """Compute the median of a list of numbers (copies its argument)."""
    if not vec:
        raise ValueError("median of an empty vector")
    vec = sorted(vec)
    mid = len(vec) // 2
    return (vec[mid] + vec[mid - 1]) / 2 if len(vec) % 2 == 0 else vec[mid]


def grade(midterm, final, homework):
    """
    Overall grade from midterm, final and homework.
    `homework` can be a single number or a list of homework grades.
    """
    if isinstance(homework, (list, tuple)):
        if not homework:
            raise ValueError("student has done no homework")
        homework = median(homework)
    return 0.2 * midterm + 0.4 * final + 0.4 * homework


@dataclass
class StudentInfo:
    name: str
    final_grade: float


def read(line):
    """Parse one record line into a StudentInfo, or return None if the line is empty."""
    tokens = line.split()
    if len(tokens) < 3:
        return None
    name = tokens[0]
    midterm, final = float(tokens[1]), float(tokens[2])
    homework = [float(x) for x in tokens[3:]]
    return StudentInfo(name, grade(midterm, final, homework))


def main():
    students = []
    for line in sys.stdin:
        record = read(line)
        if record is not None:
            students.append(record)

    # alphabetize the records
    students.sort(key=lambda s: s.name)

    # assign letter grades
    grades = {}
    for s in students:
        if s.final_grade > 90:
            letter = "A"
        elif s.final_grade > 80:
            letter = "B"
        elif s.final_grade > 70:
            letter = "C"
        elif s.final_grade > 60:
            letter = "D"
        else:
            letter = "F"
        grades.setdefault(letter, []).append(s)

    for letter in sorted(grades):
        article = "an " if letter in ("A", "F") else "a "
        names = ", ".join(s.name for s in grades[letter])
        print(f"The student(s) who got {article}{letter} are: {names}")


if __name__ == "__main__":
    main()
