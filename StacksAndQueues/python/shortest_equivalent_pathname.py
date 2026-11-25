"""
Given a working path for file system. Find the shortest equivalent path for that.
eg: /d1/./../d2 equivalent to /d2
Input: string
Output: string

Solution:
    A path can start with '/', so first '/' shouldn't be ignored. Now for every '.' we ignore it, since it means current dir only
    For every '..' we can just remove the last dir if avail and ignore it else if there is no dir before it then
    keep it. It might mean a relative path.
    Note: if '..' appears after '/' then it is not possible to go before the root '/', so it won't be allowed
    TC: O(n), n: no. of elements
    SC: O(n)
"""


def shortest_equivalent_path(dir_path):
    """Finds the shortest equivalent path for a given input path."""
    if not dir_path:
        raise ValueError("Empty path")

    # for storing the filtered path
    path = []

    # root case: if the path starts from root then '/' shouldn't be ignored
    if dir_path[0] == "/":
        path.append("/")

    for token in dir_path.split("/"):
        # if token is other than "." and ".." and not empty add
        if token not in ("", ".", ".."):
            path.append(token)
        elif token == "..":
            # if there is nothing before this or again ".." then just add it
            if not path or path[-1] == "..":
                path.append(token)
            # if last token was root "/", then we can't go up to parent
            elif path[-1] == "/":
                raise ValueError("Wrong path")
            else:  # if there is a parent dir then remove that
                path.pop()

    if not path:
        return ""

    # join with "/", taking care not to add another '/' right after the root
    if path[0] == "/":
        return "/" + "/".join(path[1:])
    return "/".join(path)


if __name__ == "__main__":
    dir_path = "/."
    print(shortest_equivalent_path(dir_path))
