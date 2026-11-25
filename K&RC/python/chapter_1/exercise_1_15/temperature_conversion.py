"""Exercise 1-15: temperature conversion program using a function."""


def celsius_to_fahrenheit(celsius):
    return (9.0 / 5.0) * int(celsius) + 32.0


def main():
    lower = 0
    upper = 300
    step = 30

    # Printing a heading above the table
    print("Celsius\t\tFahr.")
    print("----------------------")

    celsius = float(lower)
    while celsius <= upper:
        fahr = celsius_to_fahrenheit(celsius)
        print("%3.0f\t\t%6.1f" % (celsius, fahr))
        celsius += step


if __name__ == "__main__":
    main()
