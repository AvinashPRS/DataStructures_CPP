"""
city.py - City class, which manages data relating to a single city. x is the x coord
of the city, y is the y coord. Distance to other cities is calculated using the
Euclidean distance formula rounded to the nearest integer.
Python port of the C++ version written by Sam Best for CS325.
"""
import math

LIST_SIZE = 5


class City:
    def __init__(self, id_in, x_in, y_in, pos_in, visited_in):
        self.id = id_in
        self.x = x_in
        self.y = y_in
        self.pos = pos_in
        self.visited = visited_in
        self.neighbor_list = []  # positions

    def copy(self):
        """Copy constructor equivalent"""
        new_city = City(self.id, self.x, self.y, self.pos, self.visited)
        new_city.neighbor_list = list(self.neighbor_list)
        return new_city

    def dist(self, city_in):
        """Calculates the Euclidean distance to city_in, rounded to nearest integer"""
        dx = city_in.x - self.x
        dy = city_in.y - self.y
        # Rounds down from 0.0 to .499_, rounds up from 0.5 to .99_
        return int(math.floor(math.sqrt(dx * dx + dy * dy) + 0.5))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_id(self):
        return self.id

    def get_pos(self):
        return self.pos

    def get_neighbor(self, index):
        return self.neighbor_list[index]

    def get_nl_size(self):
        return LIST_SIZE

    def set_pos(self, pos_in):
        self.pos = pos_in

    def display_coords(self):
        print(f"{self.id} {self.x} {self.y}", end="")

    def output_id(self, output):
        output.write(str(self.id))

    def write_out(self, write):
        """Writes the city id to an already-open file followed by newline"""
        if write is not None and not write.closed:
            write.write(f"{self.id}\n")
            return 1
        return 0

    def copy_city(self, city_in):
        """Copies in a city and its neighbor list"""
        if city_in is None:
            return 0
        self.id = city_in.id
        self.x = city_in.x
        self.y = city_in.y
        self.pos = city_in.pos
        self.visited = city_in.visited
        self.neighbor_list = list(city_in.neighbor_list)
        return 1

    def compare(self, city_in):
        """Returns 1 if id, x, y are equivalent to those in city_in, otherwise 0"""
        if city_in.id == self.id and city_in.x == self.x and city_in.y == self.y:
            return 1
        return 0

    def build_neighbor_list(self, cities, num_cities):
        """Builds a neighbor list from cities, sorted by distance"""
        from tree import Tree  # local import to avoid a circular import

        # Creates a tree with the current city as owner (to calculate distances for sorting)
        sorted_tree = Tree(self)
        self.neighbor_list = []  # Erase existing neighbor list

        for i in range(num_cities):
            sorted_tree += cities[i]  # Add cities to BST

        # Build neighbor list of size LIST_SIZE or num_cities, whichever is smaller
        # (issues with this because the tree doesn't correctly sort when the recursive
        # function is cut off before going through the whole tree)
        sorted_tree.build_neighbor_list(self.neighbor_list, min(LIST_SIZE, num_cities))

        print(f"{self.pos} NEIGHBOR LIST SIZE: {len(self.neighbor_list)}")
        sorted_tree.clear_tree()

    def nl_is_empty(self):
        return not self.neighbor_list

    def push_to_list(self, to_add):
        self.neighbor_list.append(to_add.copy())

    def display_neighbor_list(self):
        for i, neighbor in enumerate(self.neighbor_list):
            print(f"{self.dist(neighbor)}actual index: {i} stored pos: {neighbor.get_pos()}")

    def get_neighbor_pos(self, index):
        return self.neighbor_list[index].pos
