#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:53:13 2020

@author: robertnolet
"""

import re

patpar = re.compile(r'\(([0-9 +*]+)\)')
patadd = re.compile(r'(\d+) \+ (\d+)')
patmul = re.compile(r'(\d+) \* (\d+)')
patops = re.compile(r'(\d+) ([+*]) (\d+)')

ops = {'+': lambda x,y: str(int(x)+int(y)),
       '*': lambda x,y: str(int(x)*int(y))}

def evaluate(s, part):
    # First recursively evaluate and substitute all parenthesized expressions
    while patpar.search(s):
        s = patpar.sub(lambda r: evaluate(r.group(1), part), s)
    if part == 1:
        # Evaluate from left to right
        while patops.search(s):
            s = patops.sub(lambda r: ops[r.group(2)](*r.group(1,3)), s, count=1)
    elif part == 2:
        # Evaluate and substitute all additions 
        while patadd.search(s):
            s = patadd.sub(lambda r: ops['+'](*r.group(1,2)), s, count=1)
        # Evaluate and substitute all multiplications
        while patmul.search(s):
            s = patmul.sub(lambda r: ops['*'](*r.group(1,2)), s, count=1)
    return s

# Read Data           
data = [line.strip() for line in open('input.txt')]       

# Part 1            
print(sum(int(evaluate(s, 1)) for s in data)) 

# Part 2
print(sum(int(evaluate(s, 2)) for s in data))   
