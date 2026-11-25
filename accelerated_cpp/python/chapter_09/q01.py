# Chapter 9, exercise 1: store the final grade instead of the raw grades (§9.6/166).
from _read_all import read_all
from student_info_ex import StudentInfo, compare


def main():
    students, maxlen = read_all(StudentInfo)
    students.sort(key=compare)
    for s in students:
        print(s.name() + " " * (maxlen + 1 - len(s.name())), end="")
        try:
            print(f"{s.grade():.3g}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
