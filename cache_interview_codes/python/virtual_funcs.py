"""
Virtual vs non-virtual functions (port of virtual_funcs.cpp).

Key takeaways from the C++ original:
 * `virtual` in the base class enables runtime dispatch through the vtable.
 * Non-virtual functions are bound at compile time using the POINTER type,
   so `Animal* a = new Dog; a->sleep()` calls Animal::sleep.
 * Base classes with virtual functions need virtual destructors.

Python note: ALL methods are dynamically dispatched, so Python cannot
"hide" a method the way C++ non-virtual functions do. To reproduce the
C++ behaviour of calling the non-virtual function through a base pointer we
call the base implementation explicitly: Animal.sleep(obj).
"""


class Animal:
    # A "virtual" function - can be overridden by derived classes
    def makeNoise(self):
        print("Generic animal sound")

    # A "regular" (non-virtual) function
    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):
    # Overriding the virtual function
    def makeNoise(self):
        print("Woof! Woof!")

    # Redefining a non-virtual function (function hiding in C++)
    def sleep(self):
        print("Dog is snoring")


class Cat(Animal):
    def makeNoise(self):
        print("Meow!")


# main code harness:
def main():
    animal1 = Dog()
    animal2 = Cat()

    print("--- Testing Virtual Function (Runtime Polymorphism) ---")
    animal1.makeNoise()  # Outputs: Woof! Woof!
    animal2.makeNoise()  # Outputs: Meow!

    print("\n--- Testing Non-Virtual Function (Compile-time Binding) ---")
    # C++: animal1->sleep() through an Animal* calls Animal::sleep.
    Animal.sleep(animal1)  # Outputs: Animal is sleeping
    # (In Python, animal1.sleep() would print "Dog is snoring".)


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# Pure virtual functions / abstract classes in Python:
#
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def draw(self): ...
#
# class Circle(Shape):
#     def draw(self): print("Drawing a Circle")
#
# class Square(Shape):
#     def draw(self): print("Drawing a Square")
#
# # Shape()  -> TypeError: Can't instantiate abstract class
# for s in (Circle(), Square()):
#     s.draw()
# ---------------------------------------------------------------------------
