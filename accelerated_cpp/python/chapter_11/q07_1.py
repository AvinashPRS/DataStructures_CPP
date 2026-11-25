# Chapter 11, exercise 7 (redo 9-1 with Vec).
from _read_vec import read_all_vec
from student_info_ex_vec import StudentInfo, compare


def main():
    students, maxlen = read_all_vec(StudentInfo)
    students.sort(key=compare)
    for s in students:
        print(s.name() + " " * (maxlen + 1 - len(s.name())), end="")
        try:
            print(f"{s.grade():.3g}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
