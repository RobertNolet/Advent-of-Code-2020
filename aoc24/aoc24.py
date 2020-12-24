#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 10:01:17 2020

@author: robertnolet
"""

import re
from functools import reduce
from itertools import product

pat = re.compile(r'[sn]?[ew]')

dirs = { 'e':( 1, 0),
         'w':(-1, 0),
        'ne':( 1, 1),
        'nw':( 0, 1),
        'se':( 0,-1),
        'sw':(-1,-1)}

# Return a pair (x,y) of coordinates, give a route of directions.
def parseline(line):
    return reduce(lambda p,d: (p[0]+dirs[d][0],p[1]+dirs[d][1]), pat.findall(line), (0,0))

# Return a set of 6 adjacent coordinate pairs to the point (x,y)    
def adjacent(x,y):
    return {(x+dx,y+dy) for dx,dy in dirs.values()}

# Return the set of all adjacent tiles to the given set of tiles.
def alladjacent(tiles):
    return {(x+dx, y+dy) for (x,y),(dx,dy) in product(tiles, dirs.values())} - tiles

blacktiles = reduce(lambda ts, line: ts^{parseline(line.strip())}, open('input.txt'), set())

# Part 1        
print(len(blacktiles))

# Part 2
for i in range(100):
    flipwhite = {t for t in blacktiles if len(adjacent(*t) & blacktiles) not in [1,2]}
    flipblack = {t for t in alladjacent(blacktiles) if len(adjacent(*t) & blacktiles) == 2}
    blacktiles = blacktiles - flipwhite | flipblack
print(len(blacktiles))       
        
    