#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:33:41 2020

@author: robertnolet
"""

import re

# Read data
pat = re.compile(r'(\w{3}) ([+-]?\d+)$')
code = [(r.group(1), int(r.group(2))) for r in map(pat.match, open('input.txt'))]

# Given an operation, return a function of one argument, which returns
# a pair of changes (di, da) to the index and the accumulator.
ops = {'acc' : lambda x: (1, x),
       'jmp' : lambda x: (x, 0),
       'nop' : lambda x: (1, 0)}

# Run the code, from index i and starting with accumulator value acc.
# Return the value of the accuulator, and whether the code
# terminated succesfully (True) or started looping (False)
def run(code, i = 0, acc = 0):
    vis = [False]*len(code) # Is an instruction already visited?
    
    # Terminate either if end of code is visited or a loop is detected.
    while i < len(code) and not vis[i]:
        vis[i] = True
        op, arg = code[i]
        di, da = ops[op](arg)
        i += di
        acc += da
    return acc, i >= len(code)

# Part 1
print(run(code))    

# Part 2
switch = {'jmp':'nop', 'nop':'jmp'}

for i, (op, arg) in enumerate(code):
    if op in {'jmp', 'nop'}:
        code[i] = (switch[op], arg)  # Switch jmp and nop instructions
        acc, term = run(code)
        code[i] = (op, arg)          # Switch back
    if term: break

print(acc, term)
        