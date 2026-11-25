# Student record with midterm, final and all homework grades (§4.2).
import sys
from dataclasses import dataclass, field


@dataclass
class StudentInfo:
    name: str = ""
    midterm: float = 0.0
    final: float = 0.0
    homework: list = field(default_factory=list)


def compare(x):
    """Sort key: order students by name (§4.4/69)."""
    return x.name


def _is_number(tok):
    try:
        float(tok)
        return True
    except ValueError:
        return False


def read_hw(tokens, pos):
    """Read homework grades from tokens[pos:] until a non-number (§4.1.3/57)."""
    hw = []
    while pos < len(tokens) and _is_number(tokens[pos]):
        hw.append(float(tokens[pos]))
        pos += 1
    return hw, pos


def read(tokens, pos):
    """Read one record starting at tokens[pos] (§4.2.2/62).
    Returns (StudentInfo, new_pos), or (None, pos) at end of input."""
    if pos + 3 > len(tokens):
        return None, pos
    s = StudentInfo(tokens[pos], float(tokens[pos + 1]), float(tokens[pos + 2]))
    s.homework, pos = read_hw(tokens, pos + 3)
    return s, pos


def read_students(stream=sys.stdin):
    tokens = stream.read().split()
    students = []
    pos = 0
    while True:
        s, pos = read(tokens, pos)
        if s is None:
            return students
        students.append(s)
