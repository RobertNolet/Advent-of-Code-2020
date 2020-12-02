#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:08:59 2020

@author: robertnolet
"""

import re

# RegExp for the lines in the puzzle input.
pat = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

# Read data
data = []
for line in open('input.txt'):
    r = pat.match(line)
    data.append((int(r.group(1)), int(r.group(2)), r.group(3), r.group(4)))
    
# Is s a valid password for part 1?
def valid1(a, b, c, s):
    return a <= sum(char == c for char in s) <= b

# Is s a valid password for part 2?
def valid2(a, b, c, s):
    return (s[a-1]==c) + (s[b-1]==c) == 1

# Solve part 1
print(sum(valid1(*t) for t in data))

# Solve part 2
print(sum(valid2(*t) for t in data))

    