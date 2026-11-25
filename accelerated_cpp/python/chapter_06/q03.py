# Chapter 6, exercise 3: copying into an empty container.
# In C++, copy(u.begin(), u.end(), v.begin()) on an empty v is undefined
# behaviour; an inserter (back_inserter) is needed. In Python, slice
# assignment or extend grows the list for us.


def main():
    u = [100] * 10
    v = []
    # v[0:len(u)] = u would also work; extend is the back_inserter analogue
    v.extend(u)
    print(v)


if __name__ == "__main__":
    main()
