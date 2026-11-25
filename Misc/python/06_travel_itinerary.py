"""Reconstruct a trip from a list of (source, destination) tickets."""
import sys


def handle_error():
    print("Error occured")
    sys.exit(1)


def reconstruct_trip(tickets):
    """
    tickets: list of [start_city, destination_city]. No loops in the trip.
    Returns the list of cities in the order of travel (None if no start).
    """
    next_hop = {}
    destinations = set()
    for src, dst in tickets:
        next_hop[src] = dst
        destinations.add(dst)

    # Only the first city of the entire trip will NOT be in destinations
    start = None
    for src, _ in tickets:
        if src not in destinations:
            start = src
            break
    if start is None:
        return None

    result = [start]
    city = start
    while city in next_hop:
        city = next_hop[city]  # destination becomes the next key
        result.append(city)
    return result


def verify(result, num_tickets):
    expected_result = ["LA", "SF", "TOKYO", "BEIJING", "DELHI", "ROME"]
    for i in range(num_tickets + 1):
        if result[i] != expected_result[i]:
            handle_error()


def test():
    tickets = [["TOKYO", "BEIJING"], ["LA", "SF"], ["DELHI", "ROME"],
               ["SF", "TOKYO"], ["BEIJING", "DELHI"]]
    for src, dst in tickets:
        print(f"{src} -> {dst}")
    result = reconstruct_trip(tickets)
    print("The order of visiting: " + "".join(f"{c} " for c in result))
    verify(result, len(tickets))


def main():
    test()
    print("Test passed ")


if __name__ == "__main__":
    main()
