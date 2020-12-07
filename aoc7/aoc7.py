#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:46:42 2020

@author: robertnolet
"""

import re

pat = re.compile(r'(\d+) (\w+ \w+) bags{0,1}\.{0,1}')

bagdata = {}
for line in open('input.txt'):
    k, v = line.strip().split(' bags contain ')
    bagdata[k] = []
    if v != 'no other bags.':
        for item in v.split(', '):
            r = pat.match(item)
            bagdata[k].append((int(r.group(1)), r.group(2)))
            
def canContain(cont, bag):
    if bagdata[cont] == []: return False
    if bag in {b for n, b in bagdata[cont]}: return True
    return any(canContain(b, bag) for n, b in bagdata[cont])

def numContain(bag):
    if bagdata[bag] == []: return 0
    return sum(n + n*numContain(b) for n,b in bagdata[bag])

print(sum(canContain(b, 'shiny gold') for b in bagdata))

print(numContain('shiny gold'))                     
