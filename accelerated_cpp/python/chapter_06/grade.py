# Code taken from §4.1/52, §4.1.2/54 and §4.2.2/63.
from median import median


def grade(*args):
    """grade(student) | grade(midterm, final, homework)
    where homework is a number or a list of grades."""
    if len(args) == 1:
        s = args[0]
        return grade(s.midterm, s.final, s.homework)
    midterm, final, homework = args
    if isinstance(homework, (list, tuple)):
        if len(homework) == 0:
            raise ValueError("student has done no homework")
        homework = median(homework)
    return 0.2 * midterm + 0.4 * final + 0.4 * homework
