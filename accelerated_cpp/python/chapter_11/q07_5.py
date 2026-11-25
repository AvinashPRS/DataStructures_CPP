# Chapter 11, exercise 7 (redo 9-5 with Vec): pass/fail grades.
from _read_vec import read_all_vec
from student_info_pf_vec import StudentInfo, compare


def main():
    students, maxlen = read_all_vec(StudentInfo)
    students.sort(key=compare)
    for s in students:
        print(s.name() + " " * (maxlen + 1 - len(s.name())) + s.grade())


if __name__ == "__main__":
    main()
