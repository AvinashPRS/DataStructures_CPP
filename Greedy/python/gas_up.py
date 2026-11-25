"""
There are 'n' cities lying on circumference of a circular road. Each of the cities has a gas
station. Now total gas combined from all the stations is equal to the amount
required for covering the circular road once. The car can run 1km per litre.

There is one city from which if we start and then refill the tank at each station, then
we will be able to reach that station again while moving in the circular path covering other
cities. Find that station.

Input: list of gas amount for each city,
       list of gas required for reaching the next city
Output: the starting city

Solution:
    1. If there exists any such city then the total sum of all (gas[i] - cost[i]) >= 0. If this is not the
       case then no such city can exist.
    2. Once we start traversing, if at pos 'i' remaining gas becomes < 0, then all cities from
       current start city till 'i' cannot be the starting point. So the next city to pick is 'i+1'.

NOTE: This is a generalized algo where it is not necessary that such a city exists.
TC: O(n)

Reference:
https://roy3221.gitbooks.io/algorithms/content/ch8_greedy/leetcode_134_gas_station.html
"""


def is_possible_city_coverage(gas, cost):
    """Returns the index of starting city if coverage is possible else returns -1."""
    total = 0
    remaining = 0
    start = 0
    n = len(gas)

    for i in range(n):
        total += gas[i] - cost[i]
        # current fuel
        remaining += gas[i] - cost[i]

        # if there is no remaining gas, change the start point to i+1
        if remaining < 0:
            start = (i + 1) % n
            # make the surplus fuel 0 again, since journey starts from here
            remaining = 0

    # coverage is only possible if the total is +ve
    return -1 if total < 0 else start


if __name__ == "__main__":
    gas = [6, 3, 7]
    cost = [4, 6, 3]
    print(is_possible_city_coverage(gas, cost))
