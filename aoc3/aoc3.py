#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:23:40 2020

@author: robertnolet
"""

import numpy as np
from functools import reduce

# Read data
data = np.array([list(line.strip()) for line in open('input.txt')])
length, width = data.shape

# Count trees
def treesOnSlope(dy, dx):
    y = dy*np.arange(length//dy)
    x = dx*np.arange(length//dy)%width
    return sum(data[y,x] == '#')

# Part 1    
print(treesOnSlope(1,3))

# Part 2
slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
print(reduce(lambda x,y: x*y, [treesOnSlope(dy,dx) for dy,dx in slopes]))
