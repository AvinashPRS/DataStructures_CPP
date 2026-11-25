# Make the chapter 4 modules (student_info, grade, median) importable.
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "chapter_04"))
