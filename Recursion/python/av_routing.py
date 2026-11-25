"""
Autonomous Vehicle Routing Coding Challenge

Ride-hailing companies like Uber and Lyft have become ubiquitous means to get around cities. Efficient vehicle routing,
or figuring out the fastest and most efficient way to direct vehicles to pick up and drop off multiple passengers at a
time, has become a crucial component of their success.

In the near future you are the proud owner of an autonomous vehicle! You want to let some friends use it whenever they
want so you make an app to let them call the vehicle to come pick them up. In this problem you will develop a system to
keep track of the state of your car and your friends.

Here are some more constraints to help you code your solution:
The city is a grid of perpendicular blocks. At initialization your code should take as inputs the number of streets in
both the x and y directions (ex. x=10, y=10).

The car can move in any direction exactly 1 block at a time. For our purposes, we only care about when the car is at a
vertex of two intersecting streets, so continuing our example, a car can be at the intersection (0, 0) in the upper-left
corner of our city, or (9, 9) in the bottom-right corner.

There should be a function to advance time by one time-step (and hence the vehicle by one block in any direction). This
function should accept a list of ride requests from your friends. These ride requests come in the form of a list of JSON
elements like so:

{ requests: [
    {
      'name': 'Elon',
      'start': (3,5),
      'end': (8,7)
    },
    {
      'name': 'George',
      'start': (1,2),
      'end': (4,3)
    }
  ]
}

At each time step this list of requests can be an empty list (ex. []), or infinitely long. At each time step you should
print out the current position of the vehicle and the names of all of the passengers currently in the vehicle, as well
as anybody being dropped off or being picked up at this intersection. (We will assume your car can fit infinitely many
people at a time.)

Your goal is to schedule your car to get people where they want to go as fast as possible. Of course, you will likely
have to make some trade-offs in the process. There is no right answer, just make sure you explain your decisions clearly
in your write-up.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    """A 2D coordinate intersection."""
    x: int
    y: int


@dataclass
class Request:
    """A friend's ride request."""
    name: str
    start: Location
    end: Location
    is_picked_up: bool = False


class AutonomousVehicleSystem:
    def __init__(self, x_bound, y_bound):
        # Initialize the city bounds and start the car at (0, 0)
        self.city_width = x_bound
        self.city_height = y_bound
        self.car_pos = Location(0, 0)
        self.active_requests = []  # Tracks waiting and onboard passengers

    def advance_time_step(self, new_requests):
        """Advance time by 1 unit and accept new requests."""
        # 1. Ingest new requests into the global queue
        self.active_requests.extend(new_requests)

        # 2. Determine the next target location to move toward
        target = self._get_next_target()

        # 3. Move the vehicle 1 block toward the target (if a target exists)
        x, y = self.car_pos.x, self.car_pos.y
        if target != self.car_pos:
            if x != target.x:
                x += 1 if target.x > x else -1
            elif y != target.y:
                y += 1 if target.y > y else -1
        self.car_pos = Location(x, y)

        # 4. Process pickups and dropoffs at the NEW intersection
        picked_up_now = []
        dropped_off_now = []
        currently_onboard = []
        remaining = []

        for req in self.active_requests:
            # Dropoff check
            if req.is_picked_up and req.end == self.car_pos:
                dropped_off_now.append(req.name)
                continue  # Remove from tracking entirely
            # Pickup check
            if not req.is_picked_up and req.start == self.car_pos:
                req.is_picked_up = True
                picked_up_now.append(req.name)
            # If they are onboard after processing pickups
            if req.is_picked_up:
                currently_onboard.append(req.name)
            remaining.append(req)

        self.active_requests = remaining

        # 5. Print State Output
        self._print_state(currently_onboard, picked_up_now, dropped_off_now)

    @staticmethod
    def _manhattan_distance(a, b):
        """Manhattan distance on a grid."""
        return abs(a.x - b.x) + abs(a.y - b.y)

    def _get_next_target(self):
        """Routing Logic: Returns the optimal next coordinate target."""
        if not self.active_requests:
            return self.car_pos  # Stay put if no one needs a ride

        best_target = self.car_pos
        min_distance = float("inf")
        dropoff_available = False

        # Prioritize dropping people off who are already inside the car
        for req in self.active_requests:
            if req.is_picked_up:
                dist = self._manhattan_distance(self.car_pos, req.end)
                if not dropoff_available or dist < min_distance:
                    min_distance = dist
                    best_target = req.end
                    dropoff_available = True  # Hard lock focus onto dropping passengers off

        # If no one is onboard, find the closest person waiting to be picked up
        if not dropoff_available:
            for req in self.active_requests:
                dist = self._manhattan_distance(self.car_pos, req.start)
                if dist < min_distance:
                    min_distance = dist
                    best_target = req.start

        return best_target

    def _print_state(self, onboard, picked, dropped):
        def fmt(names):
            return "[ " + "".join(name + " " for name in names) + "]"

        print(f"Vehicle Position: ({self.car_pos.x}, {self.car_pos.y})")
        print(f"  Onboard: {fmt(onboard)}")
        print(f"  Picked Up: {fmt(picked)}")
        print(f"  Dropped Off: {fmt(dropped)}")
        print("-------------------------------------------")


if __name__ == "__main__":
    # Initialize a 10x10 Grid city
    av = AutonomousVehicleSystem(10, 10)

    print("--- Starting AV Routing Simulation ---\n")

    # Time-step 1: Elon and George make requests
    print("Time Step 1: Receiving requests from Elon and George")
    av.advance_time_step([
        Request("Elon", Location(3, 5), Location(8, 7)),
        Request("George", Location(1, 2), Location(4, 3)),
    ])

    # Time-step 2-5: Advance empty time steps while car drives toward George (closest)
    for i in range(2, 6):
        print(f"Time Step {i}:")
        av.advance_time_step([])

    # Time-step 6: Another request comes in mid-transit
    print("Time Step 6: Receiving request from Shivon")
    av.advance_time_step([Request("Shivon", Location(2, 2), Location(2, 5))])

    # Run until empty to watch the system clear out passenger goals
    for i in range(7, 21):
        print(f"Time Step {i}:")
        av.advance_time_step([])
