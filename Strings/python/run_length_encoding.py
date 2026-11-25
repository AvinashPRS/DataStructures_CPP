"""
Problem:
    Run length encoding: Given a string consisting of chars, we represent
    each same successive chars by their number followed by that char.
    Eg: aaabcddda
        3a1b1c3d1a
        aaa
        3a
    Write functions for both encoding a string and decoding a run length encoded string
Input:
    s: string either encoded/decoded

Output:
    encoded string or decoded string

TC: O(n), n: no. of chars
"""


def encode_run_length(s):
    """Does run length encoding of the string"""
    if not s:
        return ""

    encoded = []
    char_count = 1

    for i in range(1, len(s)):
        # if the curr char is diff from the previous char, then write its count
        if s[i - 1] != s[i]:
            encoded.append(f"{char_count}{s[i - 1]}")
            # reset the count for the next char
            char_count = 1
        else:
            char_count += 1

    # deal with the last char
    encoded.append(f"{char_count}{s[-1]}")

    return "".join(encoded)


def decode_run_length(s):
    """For decoding run length encoded strings"""
    decoded = []
    char_count = 0
    i = 0

    while i < len(s):
        # if the current char is a digit, find the total number
        while s[i].isdigit():
            char_count = char_count * 10 + int(s[i])
            i += 1

        # write the characters
        decoded.append(s[i] * char_count)
        char_count = 0
        # get to the next number
        i += 1

    return "".join(decoded)


if __name__ == "__main__":
    enc_str = encode_run_length("aaabccd")
    print(f"String: aaabccd\nEncoded:{enc_str}\nDecoded:{decode_run_length(enc_str)}")

    enc_str = encode_run_length("")
    print(f"String: \nEncoded:{enc_str}\nDecoded:{decode_run_length(enc_str)}")
