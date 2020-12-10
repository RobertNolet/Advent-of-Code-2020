#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:25:03 2020

@author: robertnolet
"""

from numpy import diff, prod
from itertools import groupby

data = diff([0] + sorted(map(int, open('input.txt'))))

# Part 1
print(sum(data == 1)*(sum(data == 3)+1))

# Keep a cache of return value for the count function.
counts = {0:1}

# Count the number of ways a number n can written as a sum
# of values 1, 2, and 3.
def count(n):
    if n < 0: return 0
    if n not in counts: counts[n] = count(n-1) + count(n-2) + count(n-3)
    return counts[n]

# Part 2 -- Group subsequences of 1 jolt differences, and count the
# number of ways they can be rearranged.
print(prod([count(len(list(g))) for v, g in groupby(data) if v == 1]))
