#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:06:53 2020

@author: robertnolet
"""

import numpy as np
import re
from itertools import combinations, product
from math import prod

pat = re.compile(r'Tile (\d+):')

class Tile:
    def __init__(self, lines):
        self.ID = int(pat.match(lines[0]).group(1))
        self.tile = np.array([list(line) for line in lines[1:]])
        self.neighbours = []
        self.above = None
        self.below = None
        self.left  = None
        self.right = None
        
    def __str__(self):
        return '\n'.join(''.join(row) for row in self.tile)
    
    def __eq__(self, tile):
        return self.ID == tile.ID
    
    def __neq__(self, tile):
        return self.ID != tile.ID
    
    def edges(self):
        return [self.tile[ 0,:], self.tile[ 0,-1::-1],   # Top, Top Reversed
                self.tile[-1,:], self.tile[-1,-1::-1],   # Bottom, Bottom Reversed
                self.tile[:, 0], self.tile[-1::-1, 0],   # Left, Left Reversed
                self.tile[:,-1], self.tile[-1::-1,-1]]   # Right, Right Reversed
                         
    def match(self, tile):
        return any(np.all(e1 == e2) for e1, e2 in product(self.edges(), tile.edges()))
    
    def flip(self):
        for r in range(2):
            for a in range(4):
                m = []
                if self.above: m.append(any(np.all(self.tile[ 0, :] == e) for e in self.above.edges()))
                if self.below: m.append(any(np.all(self.tile[-1, :] == e) for e in self.below.edges()))
                if self.left:  m.append(any(np.all(self.tile[ :, 0] == e) for e in self.left.edges()))
                if self.right: m.append(any(np.all(self.tile[ :,-1] == e) for e in self.right.edges()))
                if all(m): return
                self.tile = self.tile.T[:,-1::-1]
            self.tile = self.tile[-1::-1,:]
        print("Can't find flip!")
    
    def iscorner(self):
        return len(self.neighbours) == 2
    
    def isedge(self):
        return len(self.neighbours) == 3
    
    def isinterior(self):
        return len(self.neighbours) == 4
    
    

class TileArray:
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols            
        self.tiles = [[None]*ncols for row in range(nrows)]
        
    def __getitem__(self, item):
        row, col = item
        return self.tiles[row][col]
    
    def __setitem__(self, item, value):
        row, col = item
        self.tiles[row][col] = value
        if row > 0 and self[row-1,col]: 
            self[row  ,col].above = self[row-1,col]
            self[row-1,col].below = self[row  ,col]
        if row < self.nrows-1 and self[row+1,col]:
            self[row  ,col].below = self[row+1,col]
            self[row+1,col].above = self[row  ,col]
        if col > 0 and self[row,col-1]:
            self[row,col  ].left  = self[row,col-1]
            self[row,col-1].right = self[row,col  ]
        if col < self.ncols-1 and self[row,col+1]:
            self[row,col  ].right = self[row,col+1]
            self[row,col+1].left  = self[row,col  ]
        
        
    def __str__(self):
        return '\n\n'.join('\n'.join(' '.join(''.join(self[j,i].tile[r,:] if self[j,i] else ' '*10) 
                                              for i in range(self.ncols)) 
                                     for r in range(10)) 
                           for j in range(self.nrows))
    
    def flipall(self):
        for j,i in product(range(self.nrows), range(self.ncols)): self[j,i].flip()
    
    def fullimage(self):
        r, c = self[0,0].tile.shape
        result = np.full(((r-2)*self.nrows, (c-2)*self.ncols), '.')
        for j,i in product(range(self.nrows), range(self.ncols)):
            result[j*(r-2):(j+1)*(r-2), i*(c-2):(i+1)*(c-2)] = self[j,i].tile[1:-1,1:-1]
        return result
    
def colormonsters(fullimg, monster):        
    h, w = fullimg.shape
    mh, mw = monster.shape
    done = False
    for r in range(2):
        for a in range(4):
            for j,i in product(range(h-mh), range(w-mw)):
                if np.all(fullimg[j:(j+mh),i:(i+mw)][monster == '#'] == '#'):
                    fullimg[j:(j+mh),i:(i+mw)][monster == '#'] = 'O'
                    done = True
            if done: return fullimg
            fullimg = fullimg.T[:,-1::-1]
        fullimg = fullimg[-1::-1,:]
    print("No monsters found!")
            
            


data = [Tile(block.split('\n')) for block in open('input.txt').read().split('\n\n')[:-1]]

# For each tile, find which other tiles connect
for tile1, tile2 in combinations(data, 2):
    if tile1.match(tile2):
        tile1.neighbours.append(tile2)
        tile2.neighbours.append(tile1)

# Sanity checks
print("Number of corners:",  sum(tile.iscorner()   for tile in data))
print("Number of edges:",    sum(tile.isedge()     for tile in data))
print("Number in interior:", sum(tile.isinterior() for tile in data))
print("Total:", len(data))

# Solve part 1
corners = [tile for tile in data if tile.iscorner()]
print("Part 1 solution:", prod(tile.ID for tile in corners))

# Solve jigsaw puzzle
image = TileArray(12,12)
# Top left corner
image[0,0] = corners[0]
image[0,1] = corners[0].neighbours[0]
image[1,0] = corners[0].neighbours[1]
# Top row
for i in range(2,11):
    image[0,i] = next(tile for tile in image[0,i-1].neighbours if tile.isedge() and tile != image[0,i-2])
# Top right corner
image[0,11] = next(tile for tile in image[0,10].neighbours if tile.iscorner())
image[1,11] = next(tile for tile in image[0,11].neighbours if tile != image[0,10])
# Left and right columns
for j in range(2,11):
    image[j, 0] = next(tile for tile in image[j-1, 0].neighbours if tile.isedge() and tile != image[j-2,0])
    image[j,11] = next(tile for tile in image[j-1,11].neighbours if tile.isedge() and tile != image[j-2,11])
# Bottom left corner
image[11,0] = next(tile for tile in image[10,0].neighbours if tile.iscorner())
image[11,1] = next(tile for tile in image[11,0].neighbours if tile != image[10,0])
# Bottom right corner
image[11,11] = next(tile for tile in image[10,11].neighbours if tile.iscorner())
image[11,10] = next(tile for tile in image[11,11].neighbours if tile != image[10,11])
# Bottom row
for i in range(2,10):
    image[11,i] = next(tile for tile in image[11,i-1].neighbours if tile.isedge() and tile != image[11,i-2])
# Interior
for j,i in product(range(1,11),range(1,11)):
    image[j,i] = next(tile for tile in image[j-1,i].neighbours if tile.ID in [t.ID for t in image[j,i-1].neighbours] and tile != image[j-1,i-1])

image.flipall()

fullimg = image.fullimage()
monster = np.array([list(line.strip('\n')) for line in open('monster.txt')])
result = colormonsters(fullimg, monster)
 
print(np.sum(result == '#'))
