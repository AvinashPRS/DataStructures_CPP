"""Console Battleship game against a random-firing AI."""
import random

BOARD_SIZE = 10


class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hits = 0

    def is_sunk(self):
        return self.hits >= self.size


class Board:
    def __init__(self):
        # '~' water, 'S' ship, 'X' hit, 'O' miss
        self.display_grid = [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        # index of ship occupying the cell (-1 if none)
        self.ship_id_grid = [[-1] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.ships = [Ship("Carrier", 5), Ship("Battleship", 4),
                      Ship("Cruiser", 3), Ship("Submarine", 3),
                      Ship("Destroyer", 2)]

    def can_place_ship(self, row, col, size, horizontal):
        if horizontal:
            if col + size > BOARD_SIZE:
                return False
            return all(self.ship_id_grid[row][c] == -1 for c in range(col, col + size))
        if row + size > BOARD_SIZE:
            return False
        return all(self.ship_id_grid[r][col] == -1 for r in range(row, row + size))

    def place_ship(self, ship_idx, row, col, horizontal):
        size = self.ships[ship_idx].size
        cells = ([(row, c) for c in range(col, col + size)] if horizontal
                 else [(r, col) for r in range(row, row + size)])
        for r, c in cells:
            self.display_grid[r][c] = "S"
            self.ship_id_grid[r][c] = ship_idx

    def place_ships_randomly(self, rng):
        for i, ship in enumerate(self.ships):
            while True:
                r = rng.randint(0, BOARD_SIZE - 1)
                c = rng.randint(0, BOARD_SIZE - 1)
                horiz = rng.randint(0, 1) == 0
                if self.can_place_ship(r, c, ship.size, horiz):
                    self.place_ship(i, r, c, horiz)
                    break

    def receive_attack(self, row, col):
        """Returns (result, sunk_ship_name).
        result: -1 = already guessed, 0 = miss, 1 = hit, 2 = hit & sunk"""
        cell = self.display_grid[row][col]
        if cell in ("X", "O"):
            return -1, ""
        ship_id = self.ship_id_grid[row][col]
        if ship_id != -1:
            self.display_grid[row][col] = "X"
            ship = self.ships[ship_id]
            ship.hits += 1
            if ship.is_sunk():
                return 2, ship.name
            return 1, ""
        self.display_grid[row][col] = "O"
        return 0, ""

    def all_ships_sunk(self):
        return all(s.is_sunk() for s in self.ships)

    def print(self, hide_ships):
        print("   0 1 2 3 4 5 6 7 8 9")
        for r in range(BOARD_SIZE):
            row = ""
            for c in range(BOARD_SIZE):
                ch = self.display_grid[r][c]
                row += ("~" if hide_ships and ch == "S" else ch) + " "
            print(f" {chr(ord('A') + r)} {row}")


def parse_coordinate(text):
    """Parses e.g. 'B4' -> (1, 4). Returns None if invalid."""
    if len(text) != 2:
        return None
    r_char, c_char = text[0].upper(), text[1]
    if not ("A" <= r_char < chr(ord("A") + BOARD_SIZE)):
        return None
    if not ("0" <= c_char < chr(ord("0") + BOARD_SIZE)):
        return None
    return ord(r_char) - ord("A"), ord(c_char) - ord("0")


def manual_placement(player_board):
    for i, ship in enumerate(player_board.ships):
        while True:
            player_board.print(False)
            print(f"\nPlace your {ship.name} (size {ship.size}).")
            parts = input("Enter start coordinate (e.g., A0) and orientation (H/V): ").split()
            if len(parts) != 2:
                print("Invalid input. Try again.")
                continue
            pos = parse_coordinate(parts[0])
            direction = parts[1].upper()
            if pos is None or direction not in ("H", "V"):
                print("Invalid input. Try again.")
                continue
            horiz = direction == "H"
            if not player_board.can_place_ship(pos[0], pos[1], ship.size, horiz):
                print("Ship does not fit or overlaps another ship. Try again.")
                continue
            player_board.place_ship(i, pos[0], pos[1], horiz)
            break


def main():
    rng = random.Random()
    player_board = Board()
    ai_board = Board()

    print("=== BATTLESHIP ===")
    choice = input("Place ships manually (M) or randomly (R)? ").strip()
    if choice.upper().startswith("M"):
        manual_placement(player_board)
    else:
        player_board.place_ships_randomly(rng)
    ai_board.place_ships_randomly(rng)

    while True:
        print("\n--- ENEMY WATERS ---")
        ai_board.print(True)
        print("\n--- YOUR FLEET ---")
        player_board.print(False)

        # Player turn
        while True:
            text = input("\nEnter target coordinate (e.g., B4): ").strip()
            pos = parse_coordinate(text)
            if pos is None:
                print("Invalid format. Use A0 through J9.")
                continue
            result, sunk_name = ai_board.receive_attack(*pos)
            if result == -1:
                print("You already fired there. Pick another spot.")
            elif result == 0:
                print(f"MISS at {text}!")
                break
            elif result == 1:
                print(f"HIT at {text}!")
                break
            else:
                print(f"HIT! You sunk the enemy's {sunk_name}!")
                break

        if ai_board.all_ships_sunk():
            print("\n*** VICTORY! You destroyed the entire enemy fleet! ***")
            break

        # AI turn
        while True:
            ai_r = rng.randint(0, BOARD_SIZE - 1)
            ai_c = rng.randint(0, BOARD_SIZE - 1)
            result, sunk_name = player_board.receive_attack(ai_r, ai_c)
            if result != -1:
                msg = f"Enemy fires at {chr(ord('A') + ai_r)}{ai_c}: "
                if result == 0:
                    msg += "MISS!"
                elif result == 1:
                    msg += "HIT!"
                else:
                    msg += f"HIT! Your {sunk_name} was sunk!"
                print(msg)
                break

        if player_board.all_ships_sunk():
            print("\n*** DEFEAT! The enemy sunk all your ships! ***")
            break


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print()
