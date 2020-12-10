#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:25:03 2020

@author: robertnolet
"""

import numpy as np

data = np.sort(list(map(int, open('input.txt'))) + [0])
diff = data[1:] - data[0:-1]

# Part 1
print(sum(diff == 1)*(sum(diff == 3)+1))

# Keep a cache of return value for the count function.
counts = {0:1}

# Count the number of ways a number n can written as a sum
# of values 1, 2, and 3.
def count(n):
    if n < 0: return 0
    if n in counts: return counts[n]
    result = count(n-1) + count(n-2) + count(n-3)
    counts[n] = result
    return result


n = 0 # Counts subsequences of 1's
c = 1 # Amount of arrangements
for d in diff:
    if d == 1:
        n += 1
    elif d == 3:
        # We just passed a subsequence of n 1 jolt differences. There are
        # count(n) ways in which these can be arranged in 1,2 or 3 jolt jumps.
        c = c*count(n) 
        n = 0 # Reset count
c = c*count(n) # Include last subsequence of 1's.

# Part 2
print(c)
