# Chapter 13, exercise 1: trace which constructors run.
import student_info
from student_info import Core, Grad


def main():
    student_info.TRACE = True
    print("Core* p1 = new Core:")
    p1 = Core()
    print("Core* p2 = new Grad:")
    p2 = Grad()
    print("Core s1:")
    s1 = Core()
    print("Grad s2:")
    s2 = Grad()
    del p1, p2, s1, s2


if __name__ == "__main__":
    main()
