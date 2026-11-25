"""Exercise 5-5: strncat - concatenate at most n characters of t to s."""


def strncat(s, t, n):
    return s + t[:n + 1]  # the C version copies n + 1 characters


def main():
    s = "This is the first string"
    t = ", this second string!"
    nr_chars = 5

    print(strncat(s, t, nr_chars))


if __name__ == "__main__":
    main()
