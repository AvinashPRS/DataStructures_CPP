"""Exercise 1-3: print a Fahrenheit-Celsius table with a heading.

for fahr = 0, 20, ... 300 (floating point version)
"""


def main():
    lower = 0
    upper = 300
    step = 20

    # Printing a heading above the table
    print("Fahr\tCelsius")
    print("---------------")

    fahr = float(lower)
    while fahr <= upper:
        celsius = (5.0 / 9.0) * (fahr - 32.0)
        print("%3.0f\t\t%6.1f" % (fahr, celsius))
        fahr = fahr + step


if __name__ == "__main__":
    main()

# NOTE: In Python 3 the "/" operator always performs true (floating point)
# division, while "//" performs floor (integer) division.
