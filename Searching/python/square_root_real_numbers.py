"""Square root of a real number using Newton's method (and binary search alternative)."""
import math


def find_square_root(n, epsilon=1e-12):
    """
    Calculate the square root of a real number using Newton's method.
    Time Complexity: O(log(log(N/epsilon))) - converges extremely fast
    """
    # Base corner cases
    if n < 0:
        return math.nan  # Not-A-Number for negative values
    if n == 0 or n == 1:
        return n

    # Initial guess setup (n / 2.0 works well for numbers >= 1)
    guess = n / 2.0
    next_guess = 0.5 * (guess + n / guess)

    # Iterate until the difference between consecutive guesses is smaller
    # than the precision threshold (epsilon)
    while abs(guess - next_guess) > epsilon:
        guess = next_guess
        next_guess = 0.5 * (guess + n / guess)

    return next_guess


def find_square_root_binary_search(n, epsilon=1e-12):
    """
    Calculate the square root of a real number using binary search.
    Time Complexity: O(log((high - low) / epsilon))
    (This was the commented-out alternative in the C++ version.)
    """
    if n < 0:
        return math.nan
    if n == 0 or n == 1:
        return n

    low = 0.0
    high = n

    # CRUCIAL CORNER CASE: If n < 1 (e.g., 0.25), its square root is LARGER
    # than n (sqrt(0.25) = 0.5). Therefore, the upper boundary must be 1.0.
    if n < 1.0:
        high = 1.0

    # Loop until our search window is smaller than our desired precision
    while (high - low) > epsilon:
        mid = low + (high - low) / 2.0
        if mid * mid > n:
            high = mid  # Root is in the lower half
        else:
            low = mid  # Root is in the upper half

    return low


if __name__ == "__main__":
    test_numbers = [2.0, 0.25, 12345.6789, 0.00004]

    print("--- Square Root App Execution ---")
    for num in test_numbers:
        custom_res = find_square_root(num)
        library_res = math.sqrt(num)  # Standard library reference

        print(f"Number: {num:.10f}")
        print(f"  Custom Algo : {custom_res:.10f}")
        print(f"  math.sqrt() : {library_res:.10f}")
        print(f"  Abs Error   : {abs(custom_res - library_res):.10f}\n")

    print("--- Square Root via Binary Search ---")
    for num in test_numbers:
        custom_res = find_square_root_binary_search(num)
        library_res = math.sqrt(num)

        print(f"Number: {num:.10f}")
        print(f"  Binary Search: {custom_res:.10f}")
        print(f"  math.sqrt()  : {library_res:.10f}")
        print(f"  Abs Error    : {abs(custom_res - library_res):.10f}\n")
