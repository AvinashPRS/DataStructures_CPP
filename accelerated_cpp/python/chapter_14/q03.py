# Chapter 14, exercise 3: Student_info built on Ptr (§13.5/247).
import copy

from student_info import StudentInfo
from token_stream import TokenStream


def main():
    stream = TokenStream()
    students = []
    record = StudentInfo()
    while record.read(stream):
        students.append(copy.copy(record))
    maxlen = max((len(s.name()) for s in students), default=0)

    students.sort(key=StudentInfo.compare)
    for s in students:
        print(s.name() + " " * (maxlen + 1 - len(s.name())), end="")
        try:
            print(f"{s.grade():.3g}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
