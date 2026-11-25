"""
algorithms.py - Tsp class, which manages the data for the traveling salesman problem
algorithms. Cities are stored as two lists of City objects: original_list contains
the initial list of cities read from file and solution contains the order of the
current solution to the problem.
Python port of the C++ version written by Sam Best for CS325.
"""
import signal
import sys

from city import City

OUTPUT_FN = "mysolution.txt"

done = False


def end_opt(signum, frame):
    """Catches the SIGTERM signal and updates global variable done to end optimization loops"""
    global done
    print("\nOut of time")
    done = True


def copy_city_list(source):
    """Returns a copy of a list of cities"""
    return [c.copy() for c in source]


class Tsp:
    def __init__(self, filename=None, source=None):
        """Constructor that reads cities from filename, or copies from another Tsp"""
        self.original_list = []
        self.solution = []
        self.num_cities = 0
        if source is not None:
            self.original_list = copy_city_list(source.original_list)
            self.solution = copy_city_list(source.solution)
            self.num_cities = source.num_cities
        elif filename is not None:
            self.num_cities = self.read_file(filename)

    def read_file(self, filename):
        """Read city data from file into original_list, returns number of cities added"""
        self.original_list = []
        try:
            with open(filename) as f:
                nums = f.read().split()
        except OSError:
            print("error", end="")
            return 0  # file doesn't exist

        added = 0
        for i in range(0, len(nums) - 2, 3):
            id_read, x_read, y_read = int(nums[i]), int(nums[i + 1]), int(nums[i + 2])
            self.original_list.append(City(id_read, x_read, y_read, id_read, False))
            added += 1
        return added

    def brute_force_wrapper(self):
        """Public wrapper, calls recursive brute force function"""
        if not self.solution:
            self.nearest_neighbor_basic(0)

        best = {"path": [], "min_distance": 9999999}
        self._brute_force(best, self.num_cities)
        self.solution = copy_city_list(best["path"])  # copy best solution into solution

        distance = self.get_solution_distance()
        self.write_solution("bruteforce.txt")
        return distance

    def _brute_force(self, best, cities_left):
        """Recursive brute force: calculate all permutations of tours and find the optimal one"""
        signal.signal(signal.SIGTERM, end_opt)
        i = 0
        while not done and i < cities_left:
            self.rotate(cities_left - 1)
            current_dist = self.get_solution_distance()
            if current_dist < best["min_distance"]:
                best["min_distance"] = current_dist
                print(best["min_distance"])
                best["path"] = copy_city_list(self.solution)

            # shift ending position of rotation left 1 in each recursion
            self._brute_force(best, cities_left - 1)
            i += 1

    def rotate(self, pos):
        """Called by brute force. Moves solution[pos] to start of the solution list"""
        self.solution.insert(0, self.solution.pop(pos))

    def nearest_neighbor(self):
        """Finds an initial tour using nearest neighbor, optimizes with basic 2-opt"""
        self.solution = []
        best_start_distance = 9999999

        # Run through entire 2-opt optimization for each city, write best index
        i = 0
        while not done and i < self.num_cities:
            self.nearest_neighbor_basic(i)
            last_run = self.two_change()
            if last_run < best_start_distance:
                best_start_distance = last_run
                print(f"Writing solution {best_start_distance}")
                self.write_solution(OUTPUT_FN)  # write each time an improvement is found
            i += 1

        total_dist = self.get_solution_distance()
        if best_start_distance <= total_dist:
            return best_start_distance  # solution already written

        print(f"Writing solution {total_dist}")
        self.write_solution(OUTPUT_FN)  # write current solution (midway through 2-opt)
        return best_start_distance

    def nearest_neighbor_basic(self, start_index):
        """Generates nearest neighbor tour in solution from original_list, starting at start_index"""
        remaining = list(self.original_list)  # original list is left untouched

        self.solution = [remaining.pop(start_index)]  # move first city to solution
        total_dist = 0

        while remaining:  # loop until no cities remain
            closest = 9999999
            closest_index = 0
            for i, c in enumerate(remaining):
                current_dist = c.dist(self.solution[-1])
                if current_dist < closest:
                    closest_index = i
                    closest = current_dist

            total_dist += closest
            self.solution.append(remaining.pop(closest_index))

        return total_dist + self.solution[0].dist(self.solution[-1])

    def two_change(self):
        """2-opt neighbor solution check (semi-naive)"""
        min_distance = self.get_solution_distance()
        sol = self.solution

        # signal handler, ends optimization if it receives SIGTERM
        signal.signal(signal.SIGTERM, end_opt)
        while not done:
            start_over = False
            i = 1
            while i < self.num_cities and not start_over:
                j = i + 1
                while j < self.num_cities - 1 and not start_over:
                    # only check moves that will reduce distance
                    if (sol[i - 1].dist(sol[j]) + sol[i].dist(sol[j + 1]) <
                            sol[i - 1].dist(sol[i]) + sol[j].dist(sol[j + 1])):
                        self.swap_two(i, j)
                        min_distance = self.get_solution_distance()
                        start_over = True
                    j += 1
                i += 1

            if not start_over:
                break
        return min_distance

    def two_opt(self):
        """2-opt with neighbor list (NOT WORKING in the original either)"""
        min_distance = self.get_solution_distance()

        for i in range(1, self.num_cities):
            k = 1
            self.fix_positions()
            while (k <= 5 and self.solution[i].dist(self.solution[i].get_neighbor(k)) <
                   self.solution[i - 1].dist(self.solution[i])):
                self.swap_two(i, self.solution[i].get_neighbor_pos(k))
                min_distance = self.get_solution_distance()
                k += 1
                print(min_distance)
            self.fix_positions()

        return min_distance

    def swap_two(self, i, k):
        """Reverses the order of the cities from i to k"""
        self.solution[i:k + 1] = self.solution[i:k + 1][::-1]
        return 1

    def get_solution_distance(self):
        """Calculate the total distance of the tour in solution"""
        total_dist = 0
        for i in range(self.num_cities - 1):
            total_dist += self.solution[i].dist(self.solution[i + 1])
        total_dist += self.solution[0].dist(self.solution[self.num_cities - 1])
        return total_dist

    def write_solution(self, file_name):
        """Write solution to file_name"""
        distance = self.get_solution_distance()
        with open(file_name, "w") as write:
            write.write(f"{distance}\n")
            for i in range(self.num_cities):
                self.solution[i].write_out(write)

    def display_neighbor_lists(self):
        """Displays all the neighbor lists (used for testing)"""
        for i in range(self.num_cities):
            print(f"LIST {i}")
            self.solution[i].display_neighbor_list()

    def fix_positions(self):
        """Updates the stored positions of the cities to their current value"""
        for i in range(self.num_cities):
            self.solution[i].set_pos(i)
