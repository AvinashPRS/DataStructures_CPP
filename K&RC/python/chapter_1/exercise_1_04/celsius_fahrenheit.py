"""Exercise 1-4: print a Celsius-Fahrenheit table.

for celsius = 0, 20, ... 300 (floating point version)
"""


def main():
    lower = 0
    upper = 300
    step = 20

    print("Celsius\tFahr")
    print("---------------")

    celsius = float(lower)
    while celsius <= upper:
        fahr = (9.0 / 5.0) * celsius + 32.0
        print("%3.0f\t\t%6.1f" % (celsius, fahr))
        celsius = celsius + step


if __name__ == "__main__":
    main()
