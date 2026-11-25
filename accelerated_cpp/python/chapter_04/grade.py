# Code taken from §4.1/52 and §4.1.2/54.
from median import median


def grade(midterm, final, homework):
    """`homework` may be a single number or a list of homework grades."""
    if isinstance(homework, (list, tuple)):
        if len(homework) == 0:
            raise ValueError("student has done no homework")
        homework = median(homework)
    return 0.2 * midterm + 0.4 * final + 0.4 * homework
