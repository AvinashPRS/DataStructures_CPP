"""Find the gas station from which a circular trip can be completed."""
import random
import sys

MAX_NUM_TESTS = 100
MAX_NUM_STATIONS = 10
MAX_DISTANCE = 100


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_array(a):
    print(" ".join(str(x) for x in a) + " ")


def find_starting_gas_station(gas, distance, mileage):
    """
    gas: the amount of gas available at each gas station. The total gas in all
        stations should be sufficient to complete the circular trip
    distance: distance[i] has the distance between gas station i and i+1
    mileage: how much distance can the car travel for 1 unit of gas consumed
    Return value: station from where to start so that we don't run out of fuel and
        complete the circular trip around all stations
    """
    num_stations = len(gas)

    # Station from where to start the journey so that we don't run out of fuel
    starting_station = 0

    least_gas = 0    # Tracks the least amount of gas in fuel tank
    gas_in_tank = 0  # Tracks how much fuel is currently present in fuel tank
    for i in range(num_stations):
        gas_required = distance[i] // mileage

        # At station i, we fill up gas[i] and then as we drive, we consume
        # gas_required to reach the destination station = (i+1) % num_stations
        gas_in_tank += gas[i] - gas_required
        if gas_in_tank < least_gas:
            least_gas = gas_in_tank
            # The starting station is the station where we have
            # the least amount of gas in the tank just before we fill up
            starting_station = (i + 1) % num_stations

    return starting_station


def verify(starting_station, gas, distance, mileage):
    """Verifies that starting at starting_station, we complete the journey without running out of fuel."""
    num_stations = len(gas)

    # Check if starting_station is out of range
    if starting_station < 0 or starting_station >= num_stations:
        handle_error()

    cur_station = starting_station
    gas_in_tank = 0
    for _ in range(1, num_stations):
        gas_required = distance[cur_station] // mileage
        gas_in_tank += gas[cur_station] - gas_required

        # gas in the fuel tank should always be >= 0
        if gas_in_tank < 0:
            handle_error()

        cur_station = (cur_station + 1) % num_stations


def test():
    # Randomly pick the number of gas stations
    num_stations = 1 + random.randrange(MAX_NUM_STATIONS)

    # Randomly pick the distance between the gas stations between 1 and 10
    distance = [1 + random.randrange(10) for _ in range(num_stations)]
    total_distance = sum(distance)

    # We are fixing the mileage to 1 mile/gallon since we will
    # not have to deal with fractional values
    mileage = 1

    # Compute the gas needed to complete the journey around all stations
    total_gas = total_distance // mileage

    # Randomly distribute the total_gas among the gas stations
    gas = [0] * num_stations
    remaining_gas = total_gas
    per_station_quota = remaining_gas // num_stations
    for i in range(num_stations):
        gas[i] = random.randrange(per_station_quota) if remaining_gas > 0 else 0
        remaining_gas -= gas[i]

    # If there is any gas left over, then distribute the
    # remaining gas equally among the gas stations
    i = 0
    per_station_quota = remaining_gas // num_stations
    while remaining_gas > 0 and i < num_stations - 1:
        gas[i] += per_station_quota
        remaining_gas -= per_station_quota
        i += 1
    # If there is still any gas left over, give it to the last gas station
    gas[num_stations - 1] += remaining_gas

    print("Gas      : ", end="")
    print_array(gas)

    print("Distance : ", end="")
    print_array(distance)

    # Find the gas station from where to start the journey
    # IMPORTANT: the sum of gas in all the stations should be sufficient to complete the journey
    starting_station = find_starting_gas_station(gas, distance, mileage)

    print(f"Starting station = {starting_station}")

    verify(starting_station, gas, distance, mileage)

    print("____________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
