#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:14:01 2020

@author: robertnolet
"""

from itertools import combinations
from functools import reduce

# Load puzzle input.
data = [int(line) for line in open('input.txt')]


def solve(part):
    for s in combinations(data, part+1): 
        if sum(s) == 2020:
            print(reduce(lambda x,y: x*y, s, 1))
            return

# Solve part 1
solve(1)

# Solve part 2
solve(2)
        