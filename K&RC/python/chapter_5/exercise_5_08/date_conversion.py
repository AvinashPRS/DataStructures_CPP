"""Exercise 5-8: day_of_year and month_day with error checking."""

daytab = [
    [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
]


def is_leap(year):
    return int((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


def day_of_year(year, month, day):
    leap = is_leap(year)

    # Additional checks for month.
    if month > 12 or month < 1:
        print("Error: a year has 12 months, so please choose a number "
              "betweeen 1 and 12.")
        return -1

    # Additional checks for day.
    if day > daytab[leap][month]:
        print("Error: the %d month has a maximum of %d days."
              % (month, daytab[leap][month]))
        return -2

    for i in range(1, month):
        day += daytab[leap][i]

    return day


def month_day(year, yearday):
    """Return (month, day); (0, 0) on error."""
    leap = is_leap(year)

    # Additional check for yearday.
    if yearday > (366 if leap else 365):
        print("Error: year %d has %d days." % (year, 366 if leap else 365))
        return 0, 0

    i = 0
    while yearday > daytab[leap][i]:
        yearday -= daytab[leap][i]
        i += 1

    return i, yearday


def main():
    day = day_of_year(2020, 10, 30)
    print("day of the year: %d" % day)

    if day_of_year(2020, 13, 1) == -1:
        print("Warning: invalid month detected.")

    if day_of_year(202, 12, 32) == -2:
        print("Warning: invalid day detected.")

    for yd in (304, 366, 367):
        month, day_month = month_day(2020, yd)
        print("month: %d, day: %d" % (month, day_month))


if __name__ == "__main__":
    main()
