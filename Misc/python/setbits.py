"""
Exercise 2-6. Write a function setbits(x,p,n,y) that returns x with the n
bits that begin at position p set to the rightmost n bits of y, leaving the
other bits unchanged.
"""


def setbits(x, p, n, y):
    nbits = ~(~0 << n)  # mask to extract the rightmost n bits
    return ((x & ~(nbits << p)) | ((y & nbits) << p)) & 0xFFFFFFFF


def main():
    x = 0xF8FF
    y = 0xF0A2
    p = 8  # starting position of bits
    n = 8  # number of bits to set
    print(f"{setbits(x, p, n, y):x}")


if __name__ == "__main__":
    main()
