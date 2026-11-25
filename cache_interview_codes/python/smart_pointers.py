"""
Smart pointers (port of smart_pointers.cpp).

C++                     Python analogue
---------------------   -----------------------------------------------
std::unique_ptr         a single owning reference, "moved" by rebinding
std::shared_ptr         ordinary references (CPython is reference counted)
use_count()             sys.getrefcount(obj) - 1 (minus the temp arg ref)
std::weak_ptr / lock()  weakref.ref(obj) / calling the weakref
"""
import sys
import weakref


class Resource:
    def __init__(self):
        print("Resource acquired")

    def __del__(self):
        print("Resource destroyed automatically")

    def doWork(self):
        print("Unique pointer working")


class Int:
    """Boxed int: plain ints can't be weak-referenced in Python."""
    def __init__(self, v):
        self.value = v


def use_count(obj):
    # getrefcount includes the temporary reference made by the call itself
    return sys.getrefcount(obj) - 1


# main code harness:
def main():
    # unique_ptr: exclusive ownership; cannot be copied, only moved.
    ptr1 = Resource()
    ptr1.doWork()

    # Transferring ownership ("move semantics")
    ptr2, ptr1 = ptr1, None
    if not ptr1:
        print("ptr1 is now null, ownership moved to ptr2")

    # shared_ptr: reference counted; memory freed when the count drops to 0.
    shared1 = Int(42)
    # CPython's raw refcount includes interpreter-internal references, so we
    # report counts relative to this baseline (one owner = count 1).
    baseline = use_count(shared1)
    print(f"Initial Reference Count: {use_count(shared1) - baseline + 1}")

    shared2 = shared1  # Copy the shared reference (count goes up to 2)
    print(f"Inside block Count: {use_count(shared1) - baseline + 1}")
    print(f"Value via shared2: {shared2.value}")
    del shared2  # shared2 goes out of scope here (count drops back to 1)

    # weak_ptr: does not increment the count; must be "locked" to access data.
    shared = Int(100)
    weak = weakref.ref(shared)  # weak observes shared

    # Accessing data: lock() succeeds because 'shared' is still alive
    tempShared = weak()
    if tempShared is not None:
        print(f"Value is still valid: {tempShared.value}")
    del tempShared
    del shared  # 'shared' goes out of scope, object is freed.

    # Accessing data after deletion: lock() fails and returns None
    tempShared = weak()
    if tempShared is not None:
        print("This won't print.")
    else:
        print("Resource is gone. weak_ptr safely detected expiration!")

    del ptr2  # ptr2 goes out of scope here: Resource is safely destroyed.


if __name__ == "__main__":
    main()
