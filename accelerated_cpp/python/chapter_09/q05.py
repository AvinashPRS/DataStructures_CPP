# Chapter 9, exercise 5: pass/fail grading.
from _read_all import read_all
from student_info_pf import StudentInfo, compare


def main():
    students, maxlen = read_all(StudentInfo)
    students.sort(key=compare)
    for s in students:
        print(s.name() + " " * (maxlen + 1 - len(s.name())) + s.grade())


if __name__ == "__main__":
    main()
