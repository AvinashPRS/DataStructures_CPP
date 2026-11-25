# K&R C exercises — Python versions

Python 3 translations of the C solutions in the parent folder. The layout is the same:
`chapter_N/exercise_N_MM/<name>.py` matches `../chapter_N/exercise_N_MM/<name>.c`, and each
exercise's sample input files (`*.txt`) are copied next to it.

Run them the same way as the C programs, with `python3` in place of the binary:

```sh
cd chapter_5/exercise_5_13 && python3 tail.py -5 < file_in.txt
cd chapter_5/exercise_5_18 && python3 dcl.py < test.txt
cd chapter_7/exercise_7_07 && python3 find.py -n "Some people" file_1.txt file_2.txt
```

Notes on the translation:

- **Pointers / output parameters**: functions return values or tuples instead (e.g. `getint`,
  `month_day`).
- **EOF**: `None` (or `""` from `read(1)`) stands in for C's `-1`.
- **Fixed-width integers**: bit exercises (ch. 2) mask results to 32 bits to mimic `unsigned int`;
  hashes (ch. 6) mask to 64 bits to mimic `size_t`.
- **Header files** (`syscalls.h` in ch. 8) are merged into the matching `.py` file.
- **Memory allocators** (8-6 to 8-8) simulate the heap with a `bytearray` and integer "pointers",
  because Python has no raw memory access. `sbrk` grows that array.
- `exercise_4_05/math.c` is `math_functions.py` so it does not shadow Python's `math` module.
- `exercise_7_01/case.py` picks its mode from its own name (`upper`/`lower`) or from the first
  argument: `python3 case.py upper < file`.
- A few C originals have bugs (4-05 `clear()` leaves `sp = -1`, 4-11's lookahead is lost, 1-16
  counts the newline twice, 5-16/5-17 treat a prefix as an equal string). The Python versions
  behave correctly in those cases, so their output can differ.
