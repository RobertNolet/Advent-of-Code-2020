#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 08:51:39 2020

@author: robertnolet
"""

import numpy as np
from itertools import product

# Part 1
dirs = list(product([-1,0,1],[-1,0,1],[-1,0,1]))
dirs.remove((0,0,0))
dirs = np.array(dirs)
dx,dy,dz = dirs[:,0], dirs[:,1], dirs[:,2]

data = np.full((22, 22, 15), '.')
data[7:15,7:15,7] = np.array([list(line.strip()) for line in open('input.txt')])

for t in range(6):
    newdata = np.full((22,22,15), '.')
    for x, y, z in product(range(1,21), range(1,21), range(1,14)):
        n = sum(data[x+dx,y+dy,z+dz] == '#')
        if data[x,y,z] == '#' and n in {2,3}: 
            newdata[x,y,z] = '#'
        if data[x,y,z] == '.' and n == 3:
            newdata[x,y,z] = '#'
    data = newdata

print(np.sum(data == '#'))

# Part 2
dirs = list(product([-1,0,1],[-1,0,1],[-1,0,1],[-1,0,1]))
dirs.remove((0,0,0,0))
dirs = np.array(dirs)
dx,dy,dz,dw = dirs[:,0], dirs[:,1], dirs[:,2], dirs[:,3]

data = np.full((22, 22, 15,15), '.')
data[7:15,7:15,7,7] = np.array([list(line.strip()) for line in open('input.txt')])

for t in range(6):
    newdata = np.full((22,22,15,15), '.')
    for x, y, z, w in product(range(1,21), range(1,21), range(1,14), range(1,14)):
        n = sum(data[x+dx,y+dy,z+dz, w+dw] == '#')
        if data[x,y,z,w] == '#' and n in {2,3}: 
            newdata[x,y,z,w] = '#'
        if data[x,y,z,w] == '.' and n == 3:
            newdata[x,y,z,w] = '#'
    data = newdata

print(np.sum(data == '#'))

