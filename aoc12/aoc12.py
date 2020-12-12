#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 08:57:32 2020

@author: robertnolet
"""

from functools import reduce

data = [(s[0], int(s[1:])) for s in open('input.txt')]

# Sine and cosine values for multiples of 90 degrees.
cos = {90:0, 180:-1, 270:0}
sin = {90:1, 180:0, 270:-1}

# For each instruction, define how the ship (x, y) and the waypoint (wx, wy)
# changes for value v and part p.
# If p=1, the ship moves and the waypoint will always stay at distance 1.
# If p=2, the waypoint moves.
move = {'N' : lambda x, y, wx, wy, v, p: (x, y+(2-p)*v, wx, wy+(p-1)*v),
        'S' : lambda x, y, wx, wy, v, p: (x, y-(2-p)*v, wx, wy-(p-1)*v),
        'E' : lambda x, y, wx, wy, v, p: (x+(2-p)*v, y, wx+(p-1)*v, wy),
        'W' : lambda x, y, wx, wy, v, p: (x-(2-p)*v, y, wx-(p-1)*v, wy),
        'F' : lambda x, y, wx, wy, v, p: (x+v*wx, y+v*wy, wx, wy),
        'R' : lambda x, y, wx, wy, v, p: (x, y, cos[v]*wx+sin[v]*wy, -sin[v]*wx+cos[v]*wy),
        'L' : lambda x, y, wx, wy, v, p: (x, y, cos[v]*wx-sin[v]*wy,  sin[v]*wx+cos[v]*wy)
        }

# Part 1
x, y, dx, dy = reduce(lambda s, i: move[i[0]](*s, i[1], 1), data, (0,0,1,0))
print(abs(x)+abs(y))

# Part 2
x, y, wx, wy = reduce(lambda s, i: move[i[0]](*s, i[1], 2), data, (0,0,10,1))
print(abs(x)+abs(y))
