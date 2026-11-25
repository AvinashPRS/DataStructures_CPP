# Chapter 2, exercise 9: tell the user which of two numbers is larger.


def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print("The larger number is: ", end="")
    print(num1 if num1 > num2 else num2)


if __name__ == "__main__":
    main()
