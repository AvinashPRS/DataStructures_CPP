"""Exercise 5-4: strend(s, t) returns 1 if t occurs at the end of s, else 0."""


def strend(s, t):
    i = len(s) - 1
    j = len(t) - 1
    t_length = len(t)

    # Check backwards if each character from t occurs in s
    while i >= 0 and j >= 0 and s[i] == t[j]:
        t_length -= 1
        i -= 1
        j -= 1

    return int(t_length == 0)


def main():
    s = "This si a simple string"
    t1 = "string"
    t2 = "random string"

    if strend(s, t1):
        print("The string t1 orrurs at the end of the string s.")
    else:
        print("The string t1 doesn't orrur at the end of the string s.")

    if strend(s, t2):
        print("The string t2 orrurs at the end of the string s.")
    else:
        print("The string t2 doesn't orrur at the end of the string s.")


if __name__ == "__main__":
    main()
