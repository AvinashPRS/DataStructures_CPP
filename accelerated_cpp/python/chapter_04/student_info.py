# Student record that stores only the final grade (chapter 4 exercise 6).
import sys
from dataclasses import dataclass

from grade import grade


@dataclass
class StudentInfo:
    name: str = ""
    final_grade: float = 0.0


def compare(x):
    """Sort key: students are ordered by name (§4.4/69)."""
    return x.name


def _is_number(tok):
    try:
        float(tok)
        return True
    except ValueError:
        return False


def read_hw(tokens, pos):
    """Read homework grades starting at tokens[pos] until a non-number is
    found (§4.1.3/57). Returns (homework, new_pos)."""
    hw = []
    while pos < len(tokens) and _is_number(tokens[pos]):
        hw.append(float(tokens[pos]))
        pos += 1
    return hw, pos


def read_students(stream=sys.stdin):
    """Read records of the form: name midterm final hw1 hw2 ..."""
    tokens = stream.read().split()
    students = []
    pos = 0
    while pos + 3 <= len(tokens):
        name = tokens[pos]
        midterm = float(tokens[pos + 1])
        final = float(tokens[pos + 2])
        homework, pos = read_hw(tokens, pos + 3)
        students.append(StudentInfo(name, grade(midterm, final, homework)))
    return students
