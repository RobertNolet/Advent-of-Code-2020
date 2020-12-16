#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:39:06 2020

@author: robertnolet
"""

import re
import numpy as np
from itertools import combinations
from math import prod

# Read data, split into rules, my ticket and nearby tickets.
rawdata = open('input.txt').read().strip().split('\n\n')

pat = re.compile('(\D+): (\d+)-(\d+) or (\d+)-(\d+)')
rules = {r.group(1):list(map(int, r.group(2,3,4,5))) for r in map(pat.match, rawdata[0].split('\n'))}
nrules = len(rules)

myticket = list(map(int, rawdata[1].split('\n')[1].split(',')))

tickets = np.array([list(map(int, line.split(','))) for line in rawdata[2].split('\n')[1:]])

# Does a value satisfy a rule?
def applyrule(rule, value):
    return rule[0] <= value <= rule[1] or rule[2] <= value <= rule[3]

# Is there any rule for which a value is valid?
def valid(value):
    return any(applyrule(rule, value) for rule in rules.values())

# Is every value in a ticket valid for some rule?
def validticket(ticket):
    return all(map(valid,ticket))

# Are all values valid for a rule?
def validforrule(rule, values):
    return all(applyrule(rule, value) for value in values)

# Part 1
print(sum(value for value in tickets.flat if not valid(value)))

# Part 2
# Filter out invalied tickets
vtickets = np.array(list(filter(validticket, tickets)))

# For each position, identify the set of possible rules which are valid for all tickets
posrules = [{name for name, rule in rules.items() if validforrule(rule, vtickets[:,i])} for i in range(nrules)]

# Any singleton is a definite rule. It can't be a rule for any other position.
while(any(len(r) > 1 for r in posrules)):
    for i,j in combinations(range(nrules), 2):
        if len(posrules[i]) == 1 and posrules[i].issubset(posrules[j]):
            posrules[j] -= posrules[i]
        if len(posrules[j]) == 1 and posrules[j].issubset(posrules[i]):
            posrules[i] -= posrules[j]

# We now have a list of singleton sets, exrtact the one element for each position.
fields = [list(x)[0] for x in posrules]    

# Print part 2 solution
print(prod(x for x, field in zip(myticket, fields) if field.startswith('departure')))