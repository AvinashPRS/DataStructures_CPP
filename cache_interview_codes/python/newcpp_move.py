"""
Copy vs move semantics (port of newcpp_move.cpp).

Notes from the C++ original:
 * std::move doesn't actually move anything: it is a cast to an rvalue that
   lets the compiler pick the Move Constructor instead of the Copy Constructor.
 * The target type must support move semantics, otherwise it falls back to copy.
 * const objects cannot be moved (falls back to copy).
 * After a move, the source is in a valid but unspecified state.
 * Don't `return std::move(local)` -- it defeats RVO.
 * Inside a move constructor, the source pointer must be set to nullptr,
   otherwise its destructor frees the memory you just took over.

Python note: names are references, so plain assignment never copies.
"Copy" is an explicit deep copy of the buffer; "move" is handing over the
reference and clearing the source -- that is what we emulate here.
"""


class DynamicString:
    # Standard Constructor
    def __init__(self, string):
        print("[Created] Allocating buffer via standard constructor")
        self.m_Buffer = bytearray(string.encode())
        self.m_Size = len(self.m_Buffer)

    def __del__(self):
        print("[Destroyed] Cleaning up buffer")

    # 1. COPY CONSTRUCTOR (The Old, Slow Way)
    # Allocates new memory and copies every individual character.
    @classmethod
    def copy_from(cls, other):
        print("[Copied] Deep copy allocation! (Expensive)")
        obj = cls.__new__(cls)
        obj.m_Size = other.m_Size
        obj.m_Buffer = bytearray(other.m_Buffer)
        return obj

    # 2. MOVE CONSTRUCTOR (The Fast, Efficient Way)
    # Takes over the buffer reference rather than copying characters.
    @classmethod
    def move_from(cls, other):
        print("[Moved] Stealing pointer ownership! (Fast & Cheap)")
        obj = cls.__new__(cls)
        # Step 1: Copy the reference and size directly
        obj.m_Buffer = other.m_Buffer
        obj.m_Size = other.m_Size
        # Step 2: Clear the source object's reference
        other.m_Buffer = None
        other.m_Size = 0
        return obj

    def Print(self):
        if self.m_Buffer:
            print(self.m_Buffer.decode())
        else:
            print("(empty)")


# main code harness:
def main():
    print("--- Creating Initial Object ---")
    original = DynamicString("Hello World, this is a very long string stored on the heap!")

    print("\n--- Triggering a Copy ---")
    copyTarget = DynamicString.copy_from(original)  # "Copy Constructor"

    print("\n--- Triggering a Move ---")
    moveTarget = DynamicString.move_from(original)  # "Move Constructor"

    print("\n--- Verification Status ---")
    print("original: ", end="")
    original.Print()    # (empty) because its buffer was taken
    print("moveTarget: ", end="")
    moveTarget.Print()  # Hello World...

    print("\n--- Destruction Phase ---")
    # another example (std::string move):
    str1 = "Hello World, this is a very long string!"
    # Python strings are immutable references; "moving" = rebinding + clearing the source
    str2, str1 = str1, ""

    print(f"str2: {str2}")
    # str1 is now empty (like a moved-from std::string usually is)
    print(f"str1: {str1}")

    del copyTarget, moveTarget, original


if __name__ == "__main__":
    main()
