#!/bin/python3
import math
import os
import random
import re
import sys

n = int(input())
tmp = " "
crosshatch = "#"
space = " "

for idx in range(n):
	prtf = space * (n-idx-1) + crosshatch * (idx+1)
	print(prtf)

