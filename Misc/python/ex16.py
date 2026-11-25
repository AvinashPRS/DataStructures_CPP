"""Structs and pointers demo ("Learn C the Hard Way" ex16) as a Python class.

Note: the C version frees `frank` and then prints/destroys it again
(use-after-free / double free). Python is garbage collected, so that bug
can't happen here; we simply drop the references at the end.
"""


class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def print(self):
        print(f"Name: {self.name}")
        print(f"\tAge: {self.age}")
        print(f"\tHeight: {self.height}")
        print(f"\tWeight: {self.weight}")


def main():
    # make two people
    joe = Person("Joe Alex", 32, 64, 140)
    frank = Person("Frank Blank", 20, 72, 180)

    # print them out and where they are in memory
    print(f"Joe is at memory location {hex(id(joe))}:")
    joe.print()
    print(f"Frank is at memory location {hex(id(frank))}:")
    frank.print()

    # make everyone age 20 years and print them again
    joe.age += 20
    joe.height -= 2
    joe.weight += 40
    joe.print()

    frank.age += 20
    frank.weight += 20
    frank.print()

    # "destroy" them both
    del joe
    del frank


if __name__ == "__main__":
    main()
