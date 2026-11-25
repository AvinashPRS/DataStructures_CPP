import sys


def handle_error():
    print("Error occured")
    sys.exit(1)


def reconstruct_trip(tickets):
    """
    tickets: list of [start_city, destination_city]. There should be no loop in the trip.
    Return value: list containing the names of cities in the order of travel (or None).
    """
    # starting city (key) -> destination city (value); destinations set
    next_hop = {}
    destinations = set()
    for src, dst in tickets:
        next_hop.setdefault(src, dst)
        destinations.add(dst)

    # Only the first city of the entire trip will NOT be in destinations
    start = next((src for src, _ in tickets if src not in destinations), None)
    if start is None:
        return None

    result = [start]
    city = start
    while city in next_hop:
        city = next_hop[city]  # destination becomes the key to find in the map
        result.append(city)
    return result


def verify(result, num_tickets):
    expected = ["LA", "SF", "TOKYO", "BEIJING", "DELHI", "ROME"]
    if result[:num_tickets + 1] != expected:
        handle_error()


def test():
    tickets = [["TOKYO", "BEIJING"], ["LA", "SF"], ["DELHI", "ROME"],
               ["SF", "TOKYO"], ["BEIJING", "DELHI"]]
    for a, b in tickets:
        print(f"{a} -> {b}")
    result = reconstruct_trip(tickets)
    print("The order of visiting:", " ".join(result))
    verify(result, len(tickets))


if __name__ == "__main__":
    test()
    print("Test passed ")
