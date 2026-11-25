"""Print a number (0 to 999999999) in words."""

# basic_lookup[0] is empty. We want basic_lookup[1] to map to "One" and so on.
BASIC_LOOKUP = ["", "One", "Two", "Three", "Four", "Five", "Six",
                "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                "Eighteen", "Nineteen"]

# tens_lookup[0] and tens_lookup[1] are empty.
# We want tens_lookup[2] to map to "Twenty" and so on.
TENS_LOOKUP = ["", "", "Twenty", "Thirty", "Fourty", "Fifty",
               "Sixty", "Seventy", "Eighty", "Ninety"]


def print_3_digits(number):
    """
    Helper function to print number from 1 to 999
    number: number from 1 to 999
    """
    # Suppose number is 987, then hundreds_digit is 9
    hundreds_digit = number // 100
    if hundreds_digit > 0:
        print(f"{BASIC_LOOKUP[hundreds_digit]} Hundred ", end="")

    # Suppose number is 987, then remainder will be 87
    remainder = number % 100
    if remainder > 0:
        if remainder <= 19:
            print(f"{BASIC_LOOKUP[remainder]} ", end="")
        else:
            tens_digit = remainder // 10
            unit_digit = remainder % 10
            print(f"{TENS_LOOKUP[tens_digit]} ", end="")
            print(f"{BASIC_LOOKUP[unit_digit]} ", end="")


def print_num_in_words(number):
    """
    Main function to print the number in words
    number: any number from 0 to 999999999
    """
    # If number is 0, handle it here and return
    if number == 0:
        print("Zero ")
        return

    # Suppose number is 123456789, then millions = 123, remainder = 456789
    millions = number // 1000000
    remainder = number - (millions * 1000000)

    # Suppose remainder = 456789, then thousands = 456, remainder = 789
    thousands = remainder // 1000
    remainder = remainder - (thousands * 1000)

    if millions > 0:
        print_3_digits(millions)
        print("Million ", end="")

    if thousands > 0:
        print_3_digits(thousands)
        print("Thousand ", end="")

    if remainder > 0:
        print_3_digits(remainder)

    print()


def test(x):
    print(f"{x} in words = ", end="")
    print_num_in_words(x)


if __name__ == "__main__":
    for x in [0, 8, 15, 75, 100, 512, 987, 1001, 450012, 816280,
              1000001, 10011284, 90145012, 987654321]:
        test(x)

    print("Test passed")
