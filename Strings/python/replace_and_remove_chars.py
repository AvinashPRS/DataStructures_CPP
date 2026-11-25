"""
Problem:
    Given an array of characters. There are two operations to be performed on these characters:
    'a': replace it with 'dd'
    'b': remove the character from the string
    Also given is the size of the array currently having the characters.

Input:
    chars: list of chars
    n: no. of characters

Output:
   list of chars with applied ops

TC: O(n)
"""


def replace_and_remove(chars, n):
    """
    First we remove 'b's from the string,
    then we start the traversal from the back and scan the characters:
    if a character is 'a', then we write 'd' two times,
    else we write any other character once.
    """
    # remove all the 'b's
    write_idx = 0
    a_count = 0
    for i in range(n):
        if chars[i] != "b":
            chars[write_idx] = chars[i]
            write_idx += 1
        if chars[i] == "a":
            a_count += 1

    # resultant array size; grow the list if it isn't large enough
    new_size = write_idx + a_count
    if len(chars) < new_size:
        chars.extend([""] * (new_size - len(chars)))

    # now we traverse from the back and do operations for 'a'
    i = new_size - 1
    for j in range(write_idx - 1, -1, -1):
        if chars[j] == "a":
            # write 'd' two times
            chars[i] = "d"
            chars[i - 1] = "d"
            i -= 2
        else:
            chars[i] = chars[j]
            i -= 1

    del chars[new_size:]
    return chars


if __name__ == "__main__":
    print("".join(replace_and_remove(list("aaa"), 3)))
    print("".join(replace_and_remove(list("acdbbca"), 7)))
