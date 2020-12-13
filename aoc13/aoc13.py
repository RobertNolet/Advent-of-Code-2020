#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 10:00:58 2020

@author: robertnolet
"""

from itertools import combinations
from math import gcd

# Read Data
file = open('input.txt')
dept = int(file.readline())
line = file.readline().strip()
data = sorted((int(t), i) for (i,t) in enumerate(line.split(',')) if t != 'x')

# Part 1
wait, bus = min(( (-dept) % t, t) for (t,i) in data)
print(wait*bus)

# Extended Euclidian Algorithm
def bezout(a,b):
    oldr, r = a,b
    olds, s = 1,0
    oldt, t = 0,1
    while (r != 0):
        q = oldr//r
        oldr, r = r, oldr - q*r
        olds, s = s, olds - q*s
        oldt, t = t, oldt - q*t
    return olds, oldt

# Use the Chinese Remainder Theorem to find a solution x to the system:
#   x = a[i] mod n[i] for all i.
def solveCRT(a, n):
    # A system of one equation has a trivial solution
    if min(len(a), len(n)) == 1: return a[0]%n[0] 
    
    # Solve the system of the first two equations    
    m0, m1 = bezout(n[0], n[1])
    x = a[0]*m1*n[1] + a[1]*m0*n[0]
    
    # Substitute this solution for the first two equations and repeat
    return solveCRT([x] + a[2:], [n[0]*n[1]] + n[2:])
    
# Check if all times are coprime, so we can use the Chinese Remainder Theorem
print(max(gcd(x,y) for (x,i),(y,j) in combinations(data,2)) == 1)

# Part 2
print(solveCRT([t-i for (t,i) in data], [t for (t,i) in data]))

