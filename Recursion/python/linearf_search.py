"""
Recursive Linear Search Function

@author
  Abhilash Muraleedharan<amuraleedharan13@gmail.com>
"""


def search(arr, length, e):
    """
    Recursive Linear Search Function
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if length == 0:
        return False
    if arr[length - 1] == e:
        return True
    return search(arr, length - 1, e)


if __name__ == "__main__":
    print("This program checks whether an element X is present in the given unsorted array of elements")
    length = int(input("Enter the length of the array: "))
    print("Enter the array elements")
    arr = []
    while len(arr) < length:
        arr.extend(int(x) for x in input().split())
    arr = arr[:length]
    print("Input array: ")
    print("[" + ",".join(str(x) for x in arr) + "]")
    element = int(input("Enter the element to search: "))

    if search(arr, length, element):
        print(f"Element {element} is found!")
    else:
        print(f"Element {element} is not found!")
