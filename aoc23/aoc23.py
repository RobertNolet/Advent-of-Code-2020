#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 10:00:37 2020

@author: robertnolet
"""

   
inp = "215694783"
tst = "389125467"
#tst = "123456789"

# Part 1
cups = [int(c) for c in inp]
n = len(cups)

curr = 0
for rnd in range(100):
    ccup = cups[curr]    
    dest = (ccup - 2)%n+1
    crem = [cups[(curr+i)%n] for i in range(1,4)]
    for cup in crem: cups.remove(cup)
    while dest in crem: dest = (dest-2)%n+1
    i = cups.index(dest)
    cups = cups[:i+1]+crem+cups[i+1:]
    curr = (cups.index(ccup)+1)%n

i1 = cups.index(1)
print(''.join(str(cups[(i1+i)%n]) for i in range(1,n)))

# Part 2 -- takes way too long
cups = [int(c) for c in tst] + list(range(10, 1000001))
n = len(cups)

curr = 0
for rnd in range(10000000):
    if (rnd%1000 == 0): print(f"Round: {rnd}")
    ccup = cups[curr]    
    dest = (ccup - 2)%n+1
    crem = [cups[(curr+i)%n] for i in range(1,4)]
    for cup in crem: cups.remove(cup)
    while dest in crem: dest = (dest-2)%n+1
    i = cups.index(dest)
    cups = cups[:i+1]+crem+cups[i+1:]
    curr = (cups.index(ccup)+1)%n
