# Chapter 9, exercise 3 (part 1): grading a default-constructed student
# raises an uncaught error because there is no homework.
from student_info import StudentInfo


def main():
    student = StudentInfo()
    student.grade()


if __name__ == "__main__":
    main()
