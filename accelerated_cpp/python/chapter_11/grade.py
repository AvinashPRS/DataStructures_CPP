# grade() overloads, accepting a Vec of homework grades.
from median import median


def grade(*args):
    """grade(student) | grade(midterm, final, homework)"""
    if len(args) == 1:
        s = args[0]
        return grade(s.midterm, s.final, s.homework)
    midterm, final, homework = args
    if not isinstance(homework, (int, float)):
        if len(homework) == 0:
            raise ValueError("student has done no homework")
        homework = median(homework)
    return 0.2 * midterm + 0.4 * final + 0.4 * homework
