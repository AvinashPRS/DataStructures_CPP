# Chapter 13, exercise 8: numeric and letter grades for every kind of student.
# Usage: python q08.py < student_list.txt
from student_info import StudentInfo, read_all
from token_stream import TokenStream


def main():
    students, maxlen = read_all(TokenStream())
    students.sort(key=StudentInfo.compare)
    for s in students:
        print(s.name() + " " * (maxlen + 1 - len(s.name())), end="")
        try:
            print(f"{s.grade():.3g}\t{s.letter_grade()}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
