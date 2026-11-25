# Chapter 9, exercise 6: list passing students before failing ones.
from _read_all import read_all
from student_info_pf import StudentInfo, compare


def main():
    students, maxlen = read_all(StudentInfo)
    students.sort(key=compare)

    passes = [s for s in students if s.grade() != "F"]
    fails = [s for s in students if s.grade() == "F"]

    for s in passes + fails:
        print(s.name() + " " * (maxlen + 1 - len(s.name())) + s.grade())


if __name__ == "__main__":
    main()
