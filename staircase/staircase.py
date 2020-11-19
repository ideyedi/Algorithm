#!/bin/python3
import math
import os
import random
import re
import sys

n = int(input())
tmp = " "
crosshatch = "#"
for i in range(0, n):
    string = ""
    for j in range(0, n):
        count = n - 1 - i
        if j >= count:
            string += crosshatch
        else:
            string += tmp
    print(string)
