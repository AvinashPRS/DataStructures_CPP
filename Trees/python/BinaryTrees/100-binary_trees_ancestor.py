def binary_trees_ancestor(first, second):
    """Finds the lowest common ancestor of two nodes (None if none)."""
    if not first or not second:
        return None
    if first is second:
        return first
    mom, pop = first.parent, second.parent
    if first is pop or not mom or (not mom.parent and pop):
        return binary_trees_ancestor(first, pop)
    elif mom is second or not pop or (not pop.parent and mom):
        return binary_trees_ancestor(mom, second)
    return binary_trees_ancestor(mom, pop)
