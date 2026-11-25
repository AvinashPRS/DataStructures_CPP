"""
Sort employees by three rules:
  1. Department alphabetically (primary sort) -- direction toggled by a variable
  2. Performance rating highest to lowest (secondary)
  3. Salary lowest to highest (tertiary tie-breaker)

Quick reference:
    Ascending : items.sort(key=lambda x: x.prop)
    Descending: items.sort(key=lambda x: x.prop, reverse=True)
"""
from dataclasses import dataclass
from functools import cmp_to_key


@dataclass
class Employee:
    id: int
    name: str
    department: str
    performance_rating: int  # scale of 1 to 5 (5 being best)
    salary: float


def make_comparator(sort_dept_ascending):
    """Returns a comparator that captures sort_dept_ascending (like a C++ lambda capture)."""
    def compare(a, b):
        # Rule 1: departments differ -> they decide the order
        if a.department != b.department:
            if sort_dept_ascending:
                return -1 if a.department < b.department else 1  # A-Z
            return -1 if a.department > b.department else 1      # Z-A

        # Rule 2: same department -> higher rating first
        if a.performance_rating != b.performance_rating:
            return -1 if a.performance_rating > b.performance_rating else 1

        # Rule 3: same department and rating -> lower salary first
        return (a.salary > b.salary) - (a.salary < b.salary)
    return compare


if __name__ == "__main__":
    staff = [
        Employee(101, "Alice", "Engineering", 5, 120000.0),
        Employee(102, "Bob", "Engineering", 4, 95000.0),
        Employee(103, "Charlie", "Marketing", 5, 85000.0),
        Employee(104, "David", "Engineering", 5, 110000.0),  # same dept & rating as Alice, lower salary
        Employee(105, "Eva", "Marketing", 3, 90000.0),
        Employee(106, "Frank", "Sales", 4, 75000.0),
    ]

    # A runtime configuration variable captured by the comparator
    sort_dept_ascending = True
    staff.sort(key=cmp_to_key(make_comparator(sort_dept_ascending)))

    # The same ordering with a key tuple (when dept is ascending):
    # staff.sort(key=lambda e: (e.department, -e.performance_rating, e.salary))

    print(f"{'Dept':<12}{'Name':<10}{'Rating':<8}Salary")
    print("-" * 40)
    for emp in staff:
        print(f"{emp.department:<12}{emp.name:<10}{emp.performance_rating:<8}${emp.salary:.2f}")

    # Simpler example: students by grade, descending
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
    students.sort(key=lambda s: s[1], reverse=True)
    print("--- Student Rankings ---")
    for name, grade in students:
        print(f"{name}: {grade}")
