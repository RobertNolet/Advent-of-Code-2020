#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:46:42 2020

@author: robertnolet
"""

import re

pat = re.compile(r'(\d+) (\w+ \w+) bags{0,1}\.{0,1}')

# Load input data as a dictionary. The key is the type of bag, the value is
# a list of tuples (n, b) where n is the number of bag type b contained.
data = {}
for line in open('input.txt'):
    k, v = line.strip().split(' bags contain ')
    if v == 'no other bags.':
        data[k] = []
    else:
        data[k] = [[(int(n),b) for n,b in [pat.match(item).groups()]][0] for item in v.split(', ')]
            
# Determine whether the bag 'cont' or one of its contents can contain the bag 'bag'
def canContain(cont, bag):
    return bag in {b for n, b in data[cont]} or any(canContain(b, bag) for n, b in data[cont])

# Determine the number of bags contains in 'bag'
def numContain(bag):
    return sum(n + n*numContain(b) for n,b in data[bag])

# Part 1
print(sum(canContain(b, 'shiny gold') for b in data))

# Part 2
print(numContain('shiny gold'))                     
