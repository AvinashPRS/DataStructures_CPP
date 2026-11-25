"""Print all interleavings of two strings (recursive and iterative versions)."""


def string_interleave(str1, str2, buffer=""):
    """
    str1, str2: two input strings that have to be interleaved
    buffer: string that contains the result of interleaving so far
    """
    # If we have finished processing both strings, print the result
    if not str1 and not str2:
        print(buffer)
        return

    # Include the next character of str1 into the buffer if available
    if str1:
        string_interleave(str1[1:], str2, buffer + str1[0])

    # Include the next character of str2 into the buffer if available
    if str2:
        string_interleave(str1, str2[1:], buffer + str2[0])


def string_interleave_iterative(str1, str2):
    """
    Non-recursive function to print all interleavings.
    Uses a binary bitmask combination method.
    """
    len1 = len(str1)
    len2 = len(str2)
    total_len = len1 + len2

    if total_len == 0:
        print()
        return

    # Total possible positional masks is 2^(len1 + len2).
    # Each bit in the mask represents a position in the final buffer.
    # A '1' bit means "take from str1", a '0' bit means "take from str2".
    for mask in range(1 << total_len):
        # We ONLY care about combinations where exactly len1 elements
        # are pulled from str1.
        if bin(mask).count("1") != len1:
            continue

        # Reconstruction phase using the valid positional map
        idx1 = idx2 = 0
        buffer = []
        for i in range(total_len):
            if (mask >> i) & 1:
                buffer.append(str1[idx1])
                idx1 += 1
            else:
                buffer.append(str2[idx2])
                idx2 += 1

        print("".join(buffer))


if __name__ == "__main__":
    print("Interleaving 'abcde' and '123':")
    string_interleave("abcde", "123")

    print("Iteratively interleaving 'abc' and '12':")
    string_interleave_iterative("abc", "12")

    print("\nTest passed")
