# Chapter 9, exercise 3 (part 2): catch the error instead.
from student_info import StudentInfo


def main():
    student = StudentInfo()
    try:
        student.grade()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
