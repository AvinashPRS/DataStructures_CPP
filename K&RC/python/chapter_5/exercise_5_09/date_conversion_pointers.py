"""Exercise 5-9: day_of_year and month_day using "pointers" instead of
indexing (in Python: a list of references to two separate lists)."""

year_month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

daytab = [year_month_days, leap_year_month_days]


def is_leap(year):
    return int((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


def day_of_year(year, month, day):
    days = daytab[is_leap(year)]

    if month > 12 or month < 1:
        print("Error: a year has 12 months, so please choose a number "
              "betweeen 1 and 12.")
        return -1

    if day > days[month]:
        print("Error: the %d month has a maximum of %d days."
              % (month, days[month]))
        return -2

    return day + sum(days[1:month])


def month_day(year, yearday):
    leap = is_leap(year)
    days = daytab[leap]

    if yearday > (366 if leap else 365):
        print("Error: year %d has %d days." % (year, 366 if leap else 365))
        return 0, 0

    i = 0
    while yearday > days[i]:
        yearday -= days[i]
        i += 1

    return i, yearday


def main():
    day = day_of_year(2021, 2, 12)
    print("day of the year: %d" % day)

    if day_of_year(2021, 13, 1) == -1:
        print("Warning: invalid month detected.")

    if day_of_year(2021, 12, 32) == -2:
        print("Warning: invalid day detected.")

    for yd in (43, 365, 366):
        month, day_month = month_day(2021, yd)
        print("month: %d, day: %d" % (month, day_month))


if __name__ == "__main__":
    main()
