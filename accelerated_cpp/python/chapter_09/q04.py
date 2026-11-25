# Chapter 9, exercise 4: check valid() before grading.
from student_info import StudentInfo


def main():
    student = StudentInfo()
    if student.valid():
        student.grade()


if __name__ == "__main__":
    main()
