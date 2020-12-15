#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:52:07 2020

@author: robertnolet
"""

# Keep track of each number, and the last index where it was seen.
data = {int(n):i for i,n in enumerate(open('input.txt').read().split(','))}

def solve(data, n):
    # Initial data has no duplicates, next last number will be 0.
    last = 0 

    for j in range(len(data), n-1):
        if last in data:
            # We've seen the last number before, calculate the index difference.
            diff = j - data[last]
            data[last] = j
            last = diff
        else:
            # We've not seen the last number before, the new last number will be 0.
            data[last] = j
            last = 0
    return last

# Part 1        
print(solve(data.copy(), 2020))

# Part 2
print(solve(data.copy(), 30000000))