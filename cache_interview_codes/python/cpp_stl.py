"""
STL algorithm examples (port of cpp_stl.cpp):
  * std::copy + back_inserter  -> list.extend
  * std::transform (unary)     -> map / list comprehension
  * std::transform (binary)    -> map with two iterables
  * transform over objects     -> comprehension extracting / mutating members
"""


def op_increase(i):
    return i + 1


def op_sum(i, j):
    return i + j


class Product:
    def __init__(self, n, p):
        self.name = n
        self.price = p


class Account:
    def __init__(self, b):
        self.balance = b

    # Apply interest rate in-place
    def applyInterest(self, rate):
        self.balance += self.balance * rate


def fmt(x):
    """print doubles like C++ default cout (e.g. 105 instead of 105.0)."""
    return f"{x:g}"


# main code harness:
def main():
    # Illustrating back_inserter in cpp:
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    # back_inserter:
    v2.extend(v1)  # copy(v1.begin(), v1.end(), back_inserter(v2))

    for x in v2:
        print(x, end=" ")

    # Incrementing all elements of vector by 1 (written into the front of v2)
    v2[:len(v1)] = [a + 1 for a in v1]

    for i in v2:
        print(i, end=" ")
    print()

    # ===============================================
    first = []

    # set some values:
    for i in range(1, 6):
        first.append(i * 10)  # first: 10 20 30 40 50

    second = list(map(op_increase, first))  # second: 11 21 31 41 51

    print("first contains:", end="")
    for it in first:
        print(f" {it}", end="")

    first = list(map(op_sum, first, second))  # first: 21 41 61 81 101

    print("first contains:", end="")
    for it in first:
        print(f" {it}", end="")
    print()

    # A list of Product class instances
    store = [
        Product("Apple", 1.25),
        Product("Banana", 0.75),
        Product("Coffee", 4.50),
    ]

    # Use transform (comprehension) to extract the price of each Product instance
    prices = [p.price for p in store]

    # Print the extracted prices
    for pr in prices:
        print(fmt(pr), end=" ")  # Output: 1.25 0.75 4.5

    # Another example:
    accounts = [Account(100.0), Account(200.0), Account(300.0)]

    # Apply a 5% interest rate to each Account instance in-place
    for acc in accounts:
        acc.applyInterest(0.05)

    for acc in accounts:
        print(fmt(acc.balance), end=" ")  # Output: 105 210 315
    print()


if __name__ == "__main__":
    main()
