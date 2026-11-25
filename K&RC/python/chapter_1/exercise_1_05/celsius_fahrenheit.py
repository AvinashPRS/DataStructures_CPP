"""Exercise 1-5: Celsius-Fahrenheit table in reverse order using a for loop."""


def main():
    lower = 0
    upper = 300
    step = 20

    print("Celsius\tFahr")
    print("---------------")

    for celsius in range(upper, lower - 1, -step):
        fahr = (9.0 / 5.0) * celsius + 32.0
        print("%3.0f\t\t%6.1f" % (celsius, fahr))


if __name__ == "__main__":
    main()

# NOTE: Sometimes the for loop can be more explicit and more readable than the
# while loop because it's more compact. The initialization and the
# incrementation of the counter variable is done through the for loop params.
# However, the while loop can be, sometimes, more customizable.
