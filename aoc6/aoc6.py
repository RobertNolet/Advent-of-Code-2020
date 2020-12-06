#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:48:17 2020

@author: robertnolet
"""

from functools import reduce

data = [list(map(set, group.split())) for group in open('input.txt').read().split('\n\n')]

# Part 1
print(sum(len(reduce(lambda x,y: x.union(y), group)) for group in data))

# Part 2
print(sum(len(reduce(lambda x,y: x.intersection(y), group)) for group in data))
