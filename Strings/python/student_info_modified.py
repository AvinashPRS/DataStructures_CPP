"""
Compare grading schemes for students who did and didn't do all their homework
(code adapted from Accelerated C++ §4 and §6.2).

Input format on standard input, one student after another:
    name midterm final hw1 hw2 hw3 ...
e.g.
    echo "alice 90 80 70 60 bob 40 50 0 20 carol 70 75 80 dave 60 65 0 0" | python3 student_info_modified.py
"""
import sys
from dataclasses import dataclass, field


@dataclass
class StudentInfo:
    name: str
    midterm: float
    final: float
    homework: list = field(default_factory=list)


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
        students.append(StudentInfo(name, midterm, final, homework))
    return students


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


def grade_student(s):
    return grade(s.midterm, s.final, s.homework)


def analysis(students, metric):
    """Median of metric(s) over all students"""
    return median([metric(s) for s in students])


def optimistic_median(s):
    """
    Median of the nonzero elements of s.homework, or 0 if no such elements exist.
    Calculates a student's final grade by taking the median of only their submitted
    (non-zero) homework assignments, ignoring any missed assignments scored as 0.
    """
    nonzero = [h for h in s.homework if h != 0]

    if not nonzero:
        return grade(s.midterm, s.final, 0)
    return grade(s.midterm, s.final, median(nonzero))


def optimistic_median_analysis(students):
    return analysis(students, optimistic_median)


def grade_aux(s):
    try:
        return grade_student(s)
    except ValueError:
        return grade(s.midterm, s.final, 0)


def median_analysis(students):
    return analysis(students, grade_aux)


def average(v):
    return sum(v) / len(v)


def average_grade(s):
    return grade(s.midterm, s.final, average(s.homework))


def average_analysis(students):
    return analysis(students, average_grade)


def did_all_hw(s):
    return 0 not in s.homework


def write_analysis(out, name, analysis_fn, did, didnt):
    out.write(f"{name}: median(did) = {analysis_fn(did)}, "
              f"median(didnt) = {analysis_fn(didnt)}\n")


def main():
    # students who did and didn't do all their homework
    did, didnt = [], []

    # read the student records and partition them
    for student in read_students(sys.stdin.read().split()):
        (did if did_all_hw(student) else didnt).append(student)

    # verify that the analyses will show us something
    if not did:
        print("No student did all the homework!")
        return 1
    if not didnt:
        print("Every student did all the homework!")
        return 1

    # do the analyses
    write_analysis(sys.stdout, "median", median_analysis, did, didnt)
    write_analysis(sys.stdout, "average", average_analysis, did, didnt)
    write_analysis(sys.stdout, "median of homework turned in",
                   optimistic_median_analysis, did, didnt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
