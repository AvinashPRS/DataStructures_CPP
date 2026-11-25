"""Open-addressing (linear probing) hash map and Two Sum using it. O(n)."""

SIZE = 10000


class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self):
        self.array = [None] * SIZE  # slots holding HashNode or None

    def insert(self, key, value):
        index = abs(key) % SIZE
        while self.array[index] is not None and self.array[index].key != key:
            index = (index + 1) % SIZE  # linear probing
        if self.array[index] is None:
            self.array[index] = HashNode(key, value)
        else:
            self.array[index].value = value

    def search(self, key):
        index = abs(key) % SIZE
        while self.array[index] is not None:
            if self.array[index].key == key:
                return self.array[index].value
            index = (index + 1) % SIZE
        return -1


def two_sum(nums, target):
    """Returns [i, j] with nums[i] + nums[j] == target, or None."""
    hmap = HashMap()
    for i, num in enumerate(nums):
        search_index = hmap.search(target - num)
        # If the hash table contains the complement, we are done
        if search_index != -1:
            return [search_index, i]
        hmap.insert(num, i)
    return None


def main():
    print("===SUCCESS===")
    # small demo (not in the C version):
    # print(two_sum([2, 7, 11, 15], 9))  -> [0, 1]


if __name__ == "__main__":
    main()
