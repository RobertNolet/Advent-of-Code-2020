#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:49:30 2020

@author: robertnolet
"""

from itertools import combinations as combs

# Read data
data = list(map(int, open('input.txt')))

# Part 1
i, s1 = next((i+25,d) for i,d in enumerate(data[25:]) if all(a+b != d for a,b in combs(data[i:i+25], 2)))

# Part 2
s2 = next(min(data[j:k])+max(data[j:k]) for j,k in combs(range(i), 2) if sum(data[j:k]) == s1)

print(f'Solution part 1: {s1}\nSolution part 2: {s2}')
                