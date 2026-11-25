# Chapter 6, exercise 8: extract_fails with a pluggable failing criterion.
from analysis import optimistic_median
from student_info import read_students


def fgrade(s):
    return optimistic_median(s) < 60


def extract_fails(students, criterion=fgrade):
    """§5.3/62"""
    fail = [s for s in students if criterion(s)]
    students[:] = [s for s in students if not criterion(s)]
    return fail


def names(students):
    return ", ".join(s.name for s in students) + "." if students else ""


def main():
    students = read_students()
    fails = extract_fails(students)
    print("Students who passed the class are: " + names(students))
    print("Students who failed the class are: " + names(fails))


if __name__ == "__main__":
    main()
