#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 08:12:19 2020

@author: robertnolet
"""

import re

pat = re.compile(r'(\D+) \(contains (\D+)\)$')

data = [(set(r.group(1).split()), set(r.group(2).split(', '))) for r in map(pat.match, open('input.txt'))]

# For each allergen, make a set of possible ingredients that might contain it.
sol = {}
for ingrs, allergens in data:
    for allergen in allergens:
        if allergen in sol:
            sol[allergen] = sol[allergen].intersection(ingrs)
        else:
            sol[allergen] = ingrs
# Any singleton sets are definite, and can be removed from all other allergen sets.
while(any(len(sol[allergen]) > 1 for allergen in sol)):
    for allergen in sol:
        if len(sol[allergen]) == 1:
            for a in sol:
                if a != allergen: sol[a] -= sol[allergen]
known = set.union(*sol.values())

# Part 1
print(sum(len(ingrs - known) for ingrs, allergens in data))                

# Part 2
print(','.join([sol[allergen].pop() for allergen in sorted(sol)]))
