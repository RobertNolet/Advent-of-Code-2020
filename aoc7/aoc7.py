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
def parse(line):
    k, v = line.strip().split(' bags contain ')
    if v == 'no other bags.': return k, []
    return k, [(int(r.group(1)), r.group(2)) for r in map(pat.match, v.split(', '))]

data = {k:v for k,v in map(parse, open('input.txt'))}
            
# Determine whether the bag 'cont' or one of its contents can contain the bag 'bag'
def canContain(cont, bag = 'shiny gold'):
    return any(b == bag or canContain(b, bag) for n,b in data[cont])

# Determine the number of bags contained in 'bag'
def numContain(bag = 'shiny gold'):
    return sum(n + n*numContain(b) for n,b in data[bag])

# Part 1
print(sum(map(canContain, data)))

# Part 2
print(numContain())                     
