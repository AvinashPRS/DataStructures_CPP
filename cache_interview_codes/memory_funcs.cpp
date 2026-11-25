#include <algorithm>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

void print_range(const std::string& label, const std::string* begin, const std::string* end) {
    std::cout << label << ": [ ";
    for (const std::string* p = begin; p != end; ++p) {
        std::cout << *p << ' ';
    }
    std::cout << "]\n";
}


// main code harness:
int main(int argc, char** argv) {
    std::allocator<std::string> alloc;        

    // =========================================================================
    // 1. std::uninitialized_fill & Full-Range Erase (std::destroy)
    // =========================================================================
    {
        const std::size_t size = 3;
        std::string* buffer = alloc.allocate(size);

        std::uninitialized_fill(buffer, buffer + size, "Init");
        print_range("1. uninitialized_fill", buffer, buffer + size);

        // Erase full range (reverts memory back to uninitialized state)
        std::destroy(buffer, buffer + size);
        alloc.deallocate(buffer, size);
    }

    // =========================================================================
    // 2. std::uninitialized_fill_n & Count-Based Erase (std::destroy_n)
    // =========================================================================
    {
        const std::size_t capacity = 5;
        const std::size_t count = 3;
        std::string* buffer = alloc.allocate(capacity);

        std::string* end_ptr = std::uninitialized_fill_n(buffer, count, "Item");
        print_range("2. uninitialized_fill_n", buffer, end_ptr);

        // Erase exact count of constructed elements
        std::destroy_n(buffer, count);
        alloc.deallocate(buffer, capacity);
    }

    // =========================================================================
    // 3. std::uninitialized_copy & Middle Element Erase (std::move + destroy_at)
    // =========================================================================
    {
        std::vector<std::string> src = {"Alpha", "Beta", "Gamma"};
        std::string* buffer = alloc.allocate(src.size());

        std::string* end_ptr = std::uninitialized_copy(src.begin(), src.end(), buffer);
        print_range("3a. uninitialized_copy", buffer, end_ptr);

        // Erase "Beta" at index 1
        std::string* pos = buffer + 1;
        std::string* new_end = std::move(pos + 1, end_ptr, pos); // Shift left
        std::destroy_at(new_end);                                 // Destroy trailing slot
        end_ptr = new_end;
        print_range("3b. After middle erase", buffer, end_ptr);

        std::destroy(buffer, end_ptr);
        alloc.deallocate(buffer, src.size());
    }

    // =========================================================================
    // 4. std::uninitialized_copy_n & Prefix Erase (std::move + std::destroy)
    // =========================================================================
    {
        std::vector<std::string> src = {"One", "Two", "Three", "Four"};
        const std::size_t copy_count = 4;
        std::string* buffer = alloc.allocate(copy_count);

        std::string* end_ptr = std::uninitialized_copy_n(src.begin(), copy_count, buffer);
        print_range("4a. uninitialized_copy_n", buffer, end_ptr);

        // Erase first 2 elements ("One", "Two")
        const std::size_t erase_count = 2;
        std::string* new_end = std::move(buffer + erase_count, end_ptr, buffer);
        std::destroy(new_end, end_ptr); // Destroy vacated slots at the end
        end_ptr = new_end;
        print_range("4b. After prefix erase", buffer, end_ptr);

        std::destroy(buffer, end_ptr);
        alloc.deallocate(buffer, copy_count);
    }

    // =========================================================================
    // 5. std::uninitialized_move & Pop Back Erase (std::destroy_at)
    // =========================================================================
    {
        std::vector<std::string> src = {"LargeString1", "LargeString2"};
        std::string* buffer = alloc.allocate(src.size());

        std::string* end_ptr = std::uninitialized_move(src.begin(), src.end(), buffer);
        print_range("5a. uninitialized_move", buffer, end_ptr);

        // Pop back ("LargeString2")
        --end_ptr;
        std::destroy_at(end_ptr);
        print_range("5b. After pop_back", buffer, end_ptr);

        std::destroy(buffer, end_ptr);
        alloc.deallocate(buffer, src.size());
    }



    // To erase a subrange [first, last) from the middle of an initialized raw buffer, 
    // you combine std::move (to shift the trailing elements left over the erased gap) with std::destroy (to destroy the leftover trailing elements at the old end).
    /*
    
    Breakdown of the Math

    • Original Active Count: 6 elements (index 0 through index 5), so end_ptr is buffer + 6.
    • Erased Subrange [first, last): first is buffer + 2 ("C"), and last is buffer + 5 ("F"). That is 5 - 2 = 3 elements erased.
    • Elements Shifted: std::move(last, end_ptr, first) takes the 1 remaining element in [last, end_ptr) ("F" at index 5) and moves it into first (index 2).
    • Resulting new_end: Because 1 element was written starting at buffer + 2, std::move returns first + 1, which is buffer + 3 (index 3).

    Why That Position Matters

    new_end acts as the exact dividing line between your surviving data and the leftover objects that need cleanup:
    • Before new_end ([buffer, new_end) / indices 0–2): Holds your 3 valid, surviving elements ("A", "B", "F").
    • From new_end onward ([new_end, end_ptr) / indices 3–5): Holds the 3 leftover objects ("D", "E", and the moved-from "") whose destructors must be called by std::destroy(new_end, end_ptr).

    */
    
    std::vector<std::string> src = {"A", "B", "C", "D", "E", "F"};
    // std::allocator<std::string> alloc;
    std::string* buffer = alloc.allocate(src.size());

    // 1. Construct initial elements in raw memory
    std::string* end_ptr = std::uninitialized_copy(src.begin(), src.end(), buffer);
    print_range("Before range erase", buffer, end_ptr);

    // 2. Define the half-open subrange [first, last) to erase: {"C", "D", "E"}
    std::string* first = buffer + 2; // Points to "C"
    std::string* last  = buffer + 5; // Points to "F" (one past "E")

    // 3. Shift elements after 'last' ("F") down to 'first' via move-assignment
    std::string* new_end = std::move(last, end_ptr, first);           // The return type of std::move(last, end_ptr, first) is OutputIt—the exact same iterator type as the third argument (first).

    // 4. Destroy the leftover moved-from objects in [new_end, end_ptr)
    std::destroy(new_end, end_ptr);

    // 5. Update logical end pointer
    end_ptr = new_end;
    print_range("After range erase ", buffer, end_ptr);

    // 6. Final cleanup
    std::destroy(buffer, end_ptr);
    alloc.deallocate(buffer, src.size());


    // some more cpp erases:
    // Capacity Is Unchanged. Calling erase() reduces vec.size() and runs destructors on removed
    // elements, but it does not deallocate memory (vec.capacity() stays the same).
    // 1. Erasing a Single Element (vec.erase(pos))
     
    std::vector<std::string> vec = {"Alpha", "Beta", "Gamma", "Delta"};

    // Erase "Beta" at index 1
    auto it = vec.erase(vec.begin() + 1);

    std::cout << "Returned iterator points to: " << *it << '\n'; // Output: Gamma <- note this

    for (const auto& s : vec) {
        std::cout << s << ' '; // Output: Alpha Gamma Delta
    }
    std::cout << '\n';

    // 2. Erasing a Range (vec.erase(first, last))
     std::vector<std::string> vec1 = {"A", "B", "C", "D", "E", "F"};

    // Erase {"C", "D", "E"} (indices 2, 3, and 4)
    auto first1 = vec1.begin() + 2; // Points to "C"
    auto last1  = vec1.begin() + 5; // Points to "F" (one past "E")

    auto it1 = vec1.erase(first1, last1);

    std::cout << "Returned iterator points to: " << *it1 << '\n'; // Output: F

    for (const auto& s : vec) {
        std::cout << s << ' '; // Output: A B F
    }
    std::cout << '\n';

    //3. Erasing While Looping (Safe Iterator Pattern)
    std::vector<int> nums = {1, 2, 3, 4, 5, 6};

    for (auto it = nums.begin(); it != nums.end(); ) {
        if (*it % 2 == 0) {
            it = nums.erase(it); // erase() advances 'it' to the next valid element
        } else {
            ++it;
        }
    }

    for (int n : nums) {
        std::cout << n << ' '; // Output: 1 3 5
    }
    std::cout << '\n';


    return 0;
}







