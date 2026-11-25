"""Sorting with lambdas (key functions) in Python."""
import math
from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    name: str
    salary: float


@dataclass
class Student:
    name: str
    grade: int


@dataclass
class Point:
    x: int
    y: int


if __name__ == "__main__":
    employees = [Employee(101, "Alice", 75000.0),
                 Employee(102, "Bob", 90000.0),
                 Employee(103, "Charlie", 60000.0)]

    # Sort by salary in descending order
    employees.sort(key=lambda e: e.salary, reverse=True)
    for emp in employees:
        print(f"{emp.name}: ${emp.salary:g}")

    # Multi-criteria sorting (tie-breaking): grade descending, then name alphabetically.
    # Negating a numeric key flips its direction while keeping the others ascending.
    students = [Student("Zack", 85), Student("Alice", 95),
                Student("Charlie", 85), Student("Bob", 95)]
    students.sort(key=lambda s: (-s.grade, s.name))
    for s in students:
        print(f"{s.name} ({s.grade})")

    # (C++ note in the original about std::weak_ptr: Python's equivalent is
    #  weakref.ref -- a non-owning reference that doesn't keep the object alive;
    #  call it to get the object, or None if it has been collected.)

    # Capture a variable in the lambda: sort points by distance from a reference point
    points = [Point(1, 1), Point(5, 5), Point(2, 2), Point(0, 3)]
    reference = Point(0, 0)
    points.sort(key=lambda p: math.hypot(p.x - reference.x, p.y - reference.y))
    for p in points:
        print(f"({p.x}, {p.y})")
