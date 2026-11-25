# Grading-scheme analyses from §6.2.
from grade import grade
from median import median


def analysis(students, metric):
    """Median of `metric` applied to every student."""
    return median([metric(s) for s in students])


def optimistic_median(s):
    """§6.2.4/116: median of the nonzero homework grades, or 0 if none."""
    nonzero = [x for x in s.homework if x != 0]
    if not nonzero:
        return grade(s.midterm, s.final, 0)
    return grade(s.midterm, s.final, median(nonzero))


def optimistic_median_analysis(students):
    return analysis(students, optimistic_median)


def grade_aux(s):
    """§6.2.2/113"""
    try:
        return grade(s)
    except ValueError:
        return grade(s.midterm, s.final, 0)


def median_analysis(students):
    return analysis(students, grade_aux)


def average(v):
    """§6.2.3/115"""
    return sum(v) / len(v)


def average_grade(s):
    return grade(s.midterm, s.final, average(s.homework))


def average_analysis(students):
    return analysis(students, average_grade)


def did_all_hw(s):
    """§6.2.1/110"""
    return 0 not in s.homework


def write_analysis(out, name, func, did, didnt, per_student=False):
    """§6.2.2/113. If per_student is True, `func` is a per-student metric
    and is wrapped with `analysis`; otherwise it analyses a whole list."""
    if per_student:
        a_did, a_didnt = analysis(did, func), analysis(didnt, func)
    else:
        a_did, a_didnt = func(did), func(didnt)
    out.write(f"{name}: median(did) = {a_did:g}, median(didnt) = {a_didnt:g}\n")
