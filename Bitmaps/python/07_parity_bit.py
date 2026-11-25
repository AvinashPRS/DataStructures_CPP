import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def compute_parity(x):
    """
    x: input integer
    Return value: parity bit, 1 if there are odd number of 1's, 0 otherwise
    """
    # for each bit set to 1 in x, toggle the parity bit
    parity = 0
    while x != 0:
        parity ^= 1
        x = x & (x - 1)
    return parity


def test(x, expected_result):
    result = compute_parity(x)

    print(f"Parity bit for 0x{x:x} = {result}")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test(0xB, 1)
    test(0xA, 0)

    print("Test passed")
