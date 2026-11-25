# Chapter 11, exercise 7 (redo 9-6 with Vec): passes listed before fails.
from _read_vec import read_all_vec
from student_info_pf_vec import StudentInfo, compare
from vec import Vec


def main():
    students, maxlen = read_all_vec(StudentInfo)
    students.sort(key=compare)

    passes, fails = Vec(), Vec()
    for s in students:
        (fails if s.grade() == "F" else passes).push_back(s)

    for group in (passes, fails):
        for s in group:
            print(s.name() + " " * (maxlen + 1 - len(s.name())) + s.grade())


if __name__ == "__main__":
    main()
