#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:06:22 2020

@author: robertnolet
"""

repl = {'F':'0', 'B':'1', 'L':'0', 'R':'1'}

def convert(s):
    for k,v in repl.items():
        s = s.replace(k,v)
    return int(s, base=2)

data = [convert(line) for line in open('input.txt')]

# Part 1
print(max(data))

# Part 2
for seat in range(min(data)+1, max(data)):
    if seat not in data and (seat-1) in data and (seat+1) in data: print(seat)