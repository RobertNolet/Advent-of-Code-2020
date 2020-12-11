#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:42:37 2020

@author: robertnolet
"""

import numpy as np
from itertools import count

data = np.array([list(line.strip()) for line in open('input.txt')])
ymax, xmax = data.shape

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

class Seat:
    def __init__(self, pos, occ = False):
        self.pos = pos
        self.adj = []
        self.vis = []
        self.reset()
    
    # Given a dict of seats with position as key, find which seats are adjacent    
    def setadj(self, seats):
        y,x = self.pos
        self.adj = [seats[y+dy,x+dx] for dy,dx in dirs if (y+dy,x+dx) in seats]

    # Given a dict of seats with position as key, find which seats are visible    
    def setvis(self, seats):
        y,x = self.pos
        for dy,dx in dirs:
            n=next(n for n in count(1) if 
                   x+n*dx < 0 or x+n*dx >= xmax or 
                   y+n*dy < 0 or y+n*dy >= ymax or 
                   (y+n*dy,x+n*dx) in seats)
            if (y+n*dy,x+n*dx) in seats: self.vis.append(seats[y+n*dy,x+n*dx])

    # Determine if this seat will change state next round
    def prepChange(self, part):
        if part == 1: 
            n = sum(seat.occ for seat in self.adj)
        elif part == 2:
            n = sum(seat.occ for seat in self.vis)    
        self.toc = (self.occ and n >= 3+part) or (not self.occ and n == 0)
    
    # Change state    
    def change(self):
        if self.toc: self.occ = not self.occ
    
    # Set seat to empty    
    def reset(self):
        self.toc = True
        self.occ=  False

# Make dictionary of seats, with position as key
seats = {pos:Seat(pos) for pos in zip(*np.where(data == 'L'))}
for seat in seats.values():
    seat.setadj(seats)
    seat.setvis(seats)

def solve(part):
    while(any(seat.toc for seat in seats.values())):
        for seat in seats.values(): seat.prepChange(part)
        for seat in seats.values(): seat.change()
    return sum(seat.occ for seat in seats.values())
                
# Part 1
print(solve(1))

# Part 2
for seat in seats.values(): seat.reset()
print(solve(2))    
    
    


