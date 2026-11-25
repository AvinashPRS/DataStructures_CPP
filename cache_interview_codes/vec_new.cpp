#include <algorithm>  // std::max
#include <cstddef>    // std::size_t, std::ptrdiff_t
#include <memory>     // std::allocator, std::uninitialized_copy, std::uninitialized_fill
#include <iostream>
#include <string>
//#include "Vec.h"


#ifndef GUARD_VEC_H
#define GUARD_VEC_H


template <class T>
class Vec {
public:
    // Type definitions required for standard library compatibility
    typedef T* iterator;
    typedef const T* const_iterator;
    typedef std::size_t size_type;
    typedef T value_type;
    typedef T& reference;
    typedef const T& const_reference;
   // typedef std::ptrdiff_t difference_type;

    // Constructors, Copy Control, and Destructor
    Vec() { create(); }
    explicit Vec(size_type n, const T& val = T()) { create(n, val); }
    Vec(const Vec& v) { create(v.begin(), v.end()); }
    Vec& operator=(const Vec&);
    ~Vec() { uncreate(); }

    // Element access
    T& operator[](size_type i) { return data[i]; }
    const T& operator[](size_type i) const { return data[i]; }

    // Mutators and capacity
    void push_back(const T& val) {
        if (avail == limit) {
            grow();
        }
        unchecked_append(val);
    }

    size_type size() const { return avail - data; }

    // Iterators
    iterator begin() { return data; }
    const_iterator begin() const { return data; }

    iterator end() { return avail; }
    const_iterator end() const { return avail; }

    void clear() { uncreate(); }

private:
    iterator data;   // First element in the Vec
    iterator avail;  // One past the last constructed element
    iterator limit;  // One past the allocated memory

    // Facilities for memory allocation
    std::allocator<T> alloc;

    // Allocate and initialize the underlying array
    void create();
    void create(size_type, const T&);
    void create(const_iterator, const_iterator);

    // Destroy the elements in the array and free the memory
    void uncreate();

    // Support functions for push_back
    void grow();
    void unchecked_append(const T&);
};

// Assignment operator
template <class T>
Vec<T>& Vec<T>::operator=(const Vec& rhs) {
    // Check for self-assignment
    if (&rhs != this) {
        // Free the array in the left-hand side
        uncreate();
        // Copy elements from the right-hand side to the left-hand side
        create(rhs.begin(), rhs.end());
    }
    return *this;
}

// 1. Default create: empty Vec
template <class T>
void Vec<T>::create() {
    data = avail = limit = 0;
}

// 2. Fill create: uses std::uninitialized_fill
template <class T>
void Vec<T>::create(size_type n, const T& val) {
    data = alloc.allocate(n);
    limit = avail = data + n;
    std::uninitialized_fill(data, limit, val);
}

// 3. Range create: uses std::uninitialized_copy
template <class T>
void Vec<T>::create(const_iterator i, const_iterator j) {
    data = alloc.allocate(j - i);
    limit = avail = std::uninitialized_copy(i, j, data);
}

// Destroy elements in reverse order and deallocate buffer
template <class T>
void Vec<T>::uncreate() {
    if (data) {
        // Destroy (in reverse order) the elements that were constructed
        iterator it = avail;
        while (it != data) {
            alloc.destroy(--it);
        }
        // Return all the space that was allocated
        alloc.deallocate(data, limit - data);
    }
    // Reset pointers to indicate that the Vec is empty again
    data = limit = avail = 0;
}


// Reallocate with double capacity when avail == limit
template <class T>
void Vec<T>::grow() {
    // When growing, allocate twice as much space as currently in use
    size_type new_size = std::max(2 * (limit - data), ptrdiff_t(1));          // 

    // Allocate new space and copy existing elements to the new space
    iterator new_data = alloc.allocate(new_size);
    iterator new_avail = std::uninitialized_copy(data, avail, new_data);

    // Return the old space
    uncreate();

    // Reset pointers to point to the newly allocated space
    data = new_data;
    avail = new_avail;
    limit = data + new_size;
}

// Construct a single element at avail (assumes allocated space exists)
template <class T>
void Vec<T>::unchecked_append(const T& val) {
    alloc.construct(avail++, val);
}

#endif


template <class T>
void print_vec(const std::string& label, const Vec<T>& v) {
    std::cout << label << " (size=" << v.size() << "): [ ";
    for (typename Vec<T>::const_iterator it = v.begin(); it != v.end(); ++it) {
        std::cout << *it << ' ';
    }
    std::cout << "]\n";
}


// main code harness:
int main(int argc, char** argv) {
    // 1. Default constructor (empty Vec)
    Vec<std::string> v1;
    print_vec("1. Default constructor", v1);

    // 2. push_back() -> triggers grow() and unchecked_append()
    v1.push_back("Alpha");
    v1.push_back("Beta");
    v1.push_back("Gamma");
    print_vec("2. After push_back", v1);

    // 3. Fill constructor Vec(n, val) -> uses std::uninitialized_fill
    Vec<std::string> v2(4, "Init");
    print_vec("3. Fill constructor", v2);

    // 4. Copy constructor Vec(const Vec&) -> uses std::uninitialized_copy
    Vec<std::string> v3(v1);
    print_vec("4. Copy constructor (v3 from v1)", v3);

    // 5. Index access operator[]
    v3[1] = "Modified";
    std::cout << "5. v3[1] after modification: " << v3[1] << '\n';
    print_vec("   v1 remains unchanged", v1);

    // 6. Copy assignment operator= -> calls uncreate() then create()
    v2 = v3;
    print_vec("6. Copy assignment (v2 = v3)", v2);

    // 7. Self-assignment check
    v2 = v2;
    print_vec("7. After self-assignment (v2 = v2)", v2);

    // 8. Clear -> calls uncreate()
    v2.clear();
    print_vec("8. After v2.clear()", v2);

    return 0;
}

