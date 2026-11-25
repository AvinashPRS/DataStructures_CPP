# Chapter 11, exercise 5 (part 3): extract_didnt with lifecycle tracing.
from _ch06 import analysis
from student_info import read_students
from token_stream import TokenStream


def extract_didnt(students):
    didnt = []
    i = 0
    while i != len(students):
        if not analysis.did_all_hw(students[i]):
            didnt.append(students[i])
            del students[i]
        else:
            i += 1
    return didnt


def names(students):
    return ", ".join(s.name() for s in students) + "." if students else ""


def main():
    students = read_students(TokenStream())
    didnt = extract_didnt(students)
    print("Students who did all their homework are: " + names(students))
    print("Students who did not do all their homework are: " + names(didnt))


if __name__ == "__main__":
    main()
