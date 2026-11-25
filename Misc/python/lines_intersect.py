"""Check whether two lines y = m*x + c intersect."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def do_lines_intersect(slope1, c1, slope2, c2):
    """Returns True if the lines intersect (identical lines count too)."""
    epsilon = 0.0001
    if abs(slope1 - slope2) < epsilon:
        # Same slope: they intersect only if they are the same line
        return abs(c1 - c2) < epsilon
    # Different slopes always intersect
    return True


def test(slope1, c1, slope2, c2, expected_result):
    result = do_lines_intersect(slope1, c1, slope2, c2)
    print(f"Lines (slope = {slope1:f}, y-intercept = {c1:f}) and "
          f"(slope = {slope2:f}, y-intercept = {c2:f}) " +
          ("intersect" if result else "do NOT intersect"))
    if result != expected_result:
        handle_error()


def main():
    test(1.0, 1.0, 1.0, 2.0, False)  # same slope, different intercept
    test(2.0, 1.0, 1.0, 1.0, True)   # same intercept, different slope
    test(1.0, 3.0, 2.0, 4.0, True)   # different slope and intercept
    test(1.0, 1.0, 1.0, 1.0, True)   # identical lines
    print("Test passed")


if __name__ == "__main__":
    main()
