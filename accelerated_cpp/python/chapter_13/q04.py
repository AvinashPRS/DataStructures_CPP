# Chapter 13, exercise 4: print letter grades.
# Usage: python q04.py < student_list.txt
from student_info import StudentInfo, read_all
from token_stream import TokenStream


def main():
    students, maxlen = read_all(TokenStream())
    students.sort(key=StudentInfo.compare)
    for s in students:
        print(s.name() + " " * (maxlen + 1 - len(s.name())), end="")
        try:
            print(s.letter_grade())
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
