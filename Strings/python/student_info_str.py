"""
Read student records and extract the failing students
(code adapted from Accelerated C++ §4 and §5).

Input format on standard input, one student after another:
    name midterm final hw1 hw2 hw3 ...
e.g.
    echo "alice 90 80 70 60 bob 40 50 30 20 carol 70 75 80" | python3 student_info_str.py
"""
import sys
import time
from dataclasses import dataclass


@dataclass
class StudentInfo:
    name: str
    final_grade: float


def median(vec):
    """Compute the median of a list of numbers (does not modify vec)."""
    size = len(vec)
    if size == 0:
        raise ValueError("median of an empty vector")

    vec = sorted(vec)
    mid = size // 2
    return (vec[mid] + vec[mid - 1]) / 2 if size % 2 == 0 else vec[mid]


def grade(midterm, final, homework):
    """
    Compute a student's overall grade from midterm and final exam grades and
    either a single homework grade or a list of homework grades.
    """
    if isinstance(homework, (list, tuple)):
        if len(homework) == 0:
            raise ValueError("student has done no homework")
        homework = median(homework)
    return 0.2 * midterm + 0.4 * final + 0.4 * homework


def compare(x):
    """Sort key: students are ordered by name"""
    return x.name


def _is_number(tok):
    try:
        float(tok)
        return True
    except ValueError:
        return False


def read_hw(tokens, pos):
    """Read homework grades starting at tokens[pos] until a non-number is reached.
    Returns (homework list, next position)."""
    hw = []
    while pos < len(tokens) and _is_number(tokens[pos]):
        hw.append(float(tokens[pos]))
        pos += 1
    return hw, pos


def read_students(tokens):
    """Read all the student records from a list of tokens"""
    students = []
    pos = 0
    while pos + 2 < len(tokens):
        name = tokens[pos]
        midterm = float(tokens[pos + 1])
        final = float(tokens[pos + 2])
        homework, pos = read_hw(tokens, pos + 3)
        # save only the final grade
        students.append(StudentInfo(name, grade(midterm, final, homework)))
    return students


def extract_fails(students):
    """Extract all the students who have failed, removing them from students."""
    fails = []
    i = 0
    # invariant: elements [0, i) of students represent passing grades
    while i != len(students):
        if students[i].final_grade < 60:
            fails.append(students.pop(i))
        else:
            i += 1
    return fails


def extract_fails_pythonic(students):
    """Same as extract_fails, but rebuilds the list in a single pass (O(n))."""
    fails = [s for s in students if s.final_grade < 60]
    students[:] = [s for s in students if s.final_grade >= 60]
    return fails


def main():
    students = read_students(sys.stdin.read().split())

    # save the original size
    count = len(students)

    begin = time.perf_counter()
    fails = extract_fails(students)
    end = time.perf_counter()

    print(f"Extracting fails for {count} students took {end - begin} seconds.")
    print("Failed: " + ", ".join(s.name for s in sorted(fails, key=compare)))
    print("Passed: " + ", ".join(s.name for s in sorted(students, key=compare)))


if __name__ == "__main__":
    main()
