"""Python port of Source.cpp - demo of the BinarySearchTree."""
import random
import sys

from binary_search_tree import BinarySearchTree


def main():
    print("test 1")
    test = BinarySearchTree()
    for _ in range(10):
        test.insert(random.randrange(20))
    test.print(sys.stdout)

    print("Count:", test.get_count())
    print("Height:", test.get_height())

    print("iterative inorder walk: ", end="")
    test.iterative_inorder_walk()
    print("\ninorder walk: ", end="")
    test.inorder_walk()
    print("\nwalk by levels: ", end="")
    test.walk_by_levels()

    print("\n\nTest 2")
    test1 = BinarySearchTree()
    for v in (4, 2, 6, 1):
        test1.insert(v)
    test1.print(sys.stdout)

    print("Is 4 in tree:", int(test1.iterative_search(4)))
    print("Is 9 in tree:", int(test1.iterative_search(9)))
    print("Let's add 6", int(test1.insert(6)))
    print("Let's delete 6", int(test1.delete_key(6)))
    print("Let's delete 6", int(test1.delete_key(6)))
    print("Is 6 in tree:", int(test1.iterative_search(6)))
    print()
    test1.insert(6)

    print("Test 3")
    test2 = BinarySearchTree()
    for v in (4, 2, 6, 1):
        test2.insert(v)
    test2.print(sys.stdout)

    print("are similar tree 2 and tree 3:", int(test2.is_similar(test1)))
    print("are identical keys in tree 2 and tree 3:", int(test2.is_identical_key(test1)))
    print("Let's add 15 in tree 3", int(test2.insert(15)))
    print("are similar tree 2 and tree 3:", int(test2.is_similar(test1)))
    print("are identical keys in tree 2 and tree 3:", int(test2.is_identical_key(test1)))


if __name__ == "__main__":
    main()
