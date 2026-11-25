"""
Problem:
    Given a string number, find all the valid IP addresses that can formed from the given number.
    Eg. 12389: 1.23.8.9, 12.3.8.9 ....

Input:
    Number: string

Output:
    All possible Ip addresses in string form

TC: O(2^32) or constant time O(1)
"""


def is_valid(part):
    """Checks if a byte position value is valid or not"""
    # no. of digits should be between 1 and 3
    if len(part) == 0 or len(part) > 3:
        return False

    # Also 0 is valid but 00 or 000 is invalid
    if len(part) > 1 and part[0] == "0":
        return False

    # a valid part lies between 0 - 255
    return 0 <= int(part) <= 255


def generate_ip_address(num):
    """
    The addresses can be formed by placing '.' between digits.
    A valid IP address consists of 4 8-bit numbers or a total of 32-bits.
    Each byte is separated by '.'. So each position can have value in range(0-255)

    We try every combination by placing '.' after 1, 2 or 3 digits.
    """
    ip_addr = []
    n = len(num)

    for i in range(1, min(4, n)):
        first = num[:i]
        if not is_valid(first):
            continue
        for j in range(1, 4):
            if i + j >= n:
                break
            second = num[i:i + j]
            if not is_valid(second):
                continue
            for k in range(1, 4):
                if i + j + k >= n:
                    break
                third = num[i + j:i + j + k]
                # the fourth part is whatever remains
                fourth = num[i + j + k:]
                if is_valid(third) and is_valid(fourth):
                    ip_addr.append(f"{first}.{second}.{third}.{fourth}")

    return ip_addr


if __name__ == "__main__":
    for addr in generate_ip_address("172267810"):
        print(addr)
