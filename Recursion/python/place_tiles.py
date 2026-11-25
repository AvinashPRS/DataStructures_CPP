"""
When you place a 1 x m tile on an n x m floor:
Placing a tile horizontally reduces the remaining height (n) by m (leaving an (n-m) x m space).
Placing a tile vertically reduces the remaining height (n) by 1 (leaving an (n-1) x m space).
"""


def place_tiles(n, m):
    # If the remaining floor height is less than the tile length,
    # the only option is to place all remaining tiles vertically (1 way).
    if n < m:
        return 1
    # If the remaining height exactly matches the tile length,
    # you can either place them all vertically OR all horizontally (2 ways).
    if n == m:
        return 2

    # Placing a tile vertically reduces the height by 1
    vertical_placements = place_tiles(n - 1, m)

    # Placing a tile horizontally reduces the height by m
    horizontal_placements = place_tiles(n - m, m)

    return vertical_placements + horizontal_placements


if __name__ == "__main__":
    n, m = 4, 2
    print(f"Total ways to place tiles: {place_tiles(n, m)}")  # Output: 5
