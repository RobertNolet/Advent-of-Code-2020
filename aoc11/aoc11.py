#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:32:01 2020

@author: robertnolet
"""

import numpy as np
from itertools import product, count

data = np.array([list(line.strip()) for line in open('input.txt')])
length, width = data.shape

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Count the number of occupied seats adjacent from every seat
def adjacent(seats):
    adj = np.zeros(seats.shape, dtype = int)
    for y,x  in product(range(length), range(width)):
        adj[y,x] = sum(seats[y+dy,x+dx] == '#' for dy,dx in dirs if 0 <= y+dy < length and 0 <= x+dx < width)
    return adj

# Count the number of occupied seats visible from position y, x
def visibleSeats(seats, y, x):
    result = 0
    for dy, dx in dirs:
        n=next(n for n in count(1) if not (0 <= y+n*dy < length and 0 <= x+n*dx < width and seats[y+n*dy,x+n*dx] == '.'))
        if 0 <= y+n*dy < length and 0 <= x+n*dx < width and seats[y+n*dy,x+n*dx] == '#': result += 1 
    return result

# Count the number of visible seats from every position    
def visible(seats):
    vis = np.zeros(seats.shape, dtype = int)
    for y,x in product(range(length), range(width)):
        vis[y,x] = visibleSeats(seats, y, x)
    return vis
    
def solve(data, rule, minseats):        
    cs = data.copy()
    
    change = True
    while (change):
        n = rule(cs)
        ns = cs.copy()
        ns[(cs == 'L') & (n == 0)] = '#'
        ns[(cs == '#') & (n >= minseats)] = 'L'
        change = np.any(cs != ns)
        cs = ns
    return np.sum(cs == '#')
    
print(solve(data, adjacent, 4))

print(solve(data, visible, 5))
    