#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:06:22 2020

@author: robertnolet
"""

repl = {'F':'0', 'B':'1', 'L':'0', 'R':'1', '\n':''}
data = [int(''.join(map(lambda c: repl[c], s)), base=2) for s in open('input.txt')]

# Part 1
print(max(data))

# Part 2 -- Find all empty (seat+1) such that seat and (seat+2) are occupied.
print([seat+1 for seat in data if (seat+1) not in data and (seat+2) in data])