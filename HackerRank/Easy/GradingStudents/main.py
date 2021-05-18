"""
/bin/python3
Written by eyedi
"""

import sys
import os
import random
import re
import math

def gradingStudents(grades):
    
    for i, g in enumerate(grades):
        if g < 38 or (g % 5 < 3):
            continue
        else:
            value = g // 5
            value = value + 1
            grades[i] = value * 5

    return grades


grades_count = int(input().strip())
grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)
print("\n".join(map(str, result)))
