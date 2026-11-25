"""
Function pointers demonstration, in Python terms: functions are first-class
objects, so they can be stored in variables, lists, returned and passed as
callbacks.

YouTube lesson (C version): https://www.youtube.com/watch?v=f_uWOWViYc0
"""


def function(x):
    """prints int argument x"""
    print(f"x: {x}")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return int(x / y)  # C integer division truncates toward zero


def select_operation():
    """A function that *returns* a function."""
    print("Select An Operation: ")
    print("1) Subtract")
    print("2) Multiply")
    print("3) Divide")
    option = int(input("Enter: "))
    if option == 1:
        return subtract
    if option == 2:
        return multiply
    if option == 3:
        return divide
    return None


def freeze_C(temperature):
    """True if the temperature is freezing in Celsius."""
    return temperature <= 0


def freeze_F(temperature):
    """True if the temperature is freezing in Fahrenheit."""
    return temperature <= 32


def is_freezing(freeze_check):
    """freeze_check is a callback function used to test the temperature."""
    temperature = int(input("Enter Temperature: "))
    if freeze_check(temperature):
        print("It's freezing!")
    else:
        print("It's NOT freezing!")


def main():
    # ***** Example 1 - basic function "pointer" *****
    function_pointer = function
    function_pointer(4)

    # ***** Example 2 - call through a variable *****
    add_pointer = add
    a, b = 20.0, 30.0
    result = add_pointer(a, b)
    print(f"result: {result:f}")

    # ***** Example 3 - list of functions *****
    array = [subtract, multiply, divide]
    product = array[1](3, 15)
    print(f"product: {product}")

    # ***** Example 4 - function that returns a function *****
    operation = select_operation()
    print(f"answer: {operation(20, 5)}")

    # ***** Example 5 - function as an argument (callback) *****
    print("\nCelsius...\n")
    is_freezing(freeze_C)
    is_freezing(freeze_C)

    print("\nFahrenheit...\n")
    is_freezing(freeze_F)
    is_freezing(freeze_F)
    print()


if __name__ == "__main__":
    main()
