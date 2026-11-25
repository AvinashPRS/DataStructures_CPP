# Chapter 6, exercise 7: extract students who didn't do all their homework.
from analysis import did_all_hw
from student_info import read_students


def extract_didnt(students):
    didnt = [s for s in students if not did_all_hw(s)]
    students[:] = [s for s in students if did_all_hw(s)]
    return didnt


def names(students):
    return ", ".join(s.name for s in students) + "." if students else ""


def main():
    students = read_students()
    didnt = extract_didnt(students)
    print("Students who did all their homework are: " + names(students))
    print("Students who did not do all their homework are: " + names(didnt))


if __name__ == "__main__":
    main()
