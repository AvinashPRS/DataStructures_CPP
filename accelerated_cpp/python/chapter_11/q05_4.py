# Chapter 11, exercise 5 (part 4): extract_fails with lifecycle tracing.
from _ch06 import analysis
from student_info import read_students
from token_stream import TokenStream


def fgrade(s):
    return analysis.optimistic_median(s) < 60


def extract_fails(students):
    """§5.3/62"""
    fail = []
    i = 0
    while i != len(students):
        if fgrade(students[i]):
            fail.append(students[i])
            del students[i]
        else:
            i += 1
    return fail


def names(students):
    return ", ".join(s.name() for s in students) + "." if students else ""


def main():
    students = read_students(TokenStream())
    fails = extract_fails(students)
    print("Students who passed the class are: " + names(students))
    print("Students who failed the class are: " + names(fails))


if __name__ == "__main__":
    main()
