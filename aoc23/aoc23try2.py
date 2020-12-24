#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:26:19 2020

@author: robertnolet
"""

   
inp = "215694783"
tst = "389125467"
#tst = "123456789"

class Cup:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.minusone = None
        
    def __eq__(self, x):
        if type(x) == int: return self.value == x
        return self.value == x.value
    
    def __str__(self):
        return str(self.value)

def printcups(cup, n=8):
    result = ''
    for i in range(n):
        result += str(cup)
        cup = cup.next
    print(result)          
    
def play(cups, nrounds):
    curr = cups[0]    
    for rnd in range(nrounds):
        # Remove 3 cups clockwise of current cup
        crem = [curr.next, curr.next.next, curr.next.next.next]
        curr.next = crem[-1].next
        
        # Choose destination cup
        dest = curr.minusone
        while any(dest == cup for cup in crem): dest = dest.minusone
        
        # Insert 3 cups
        crem[-1].next = dest.next
        dest.next = crem[0]
        
        # Current cup advances one
        curr = curr.next


vals = [int(c) for c in inp]

# Part 1    
cups = [Cup(v) for v in vals]
n = len(cups)
for i in range(n):
    cups[i].next = cups[(i+1)%n]
    cups[i].minusone = cups[vals.index((vals[i]-2)%n+1)]

cupone = cups[vals.index(1)]
play(cups, 100)
printcups(cupone.next)

# Part 2
cups = [Cup(v) for v in vals]
for i in range(n-1): cups[i].next = cups[(i+1)%n]
for i in range(n): cups[i].minusone = cups[vals.index((vals[i]-2)%n+1)]
    
cupone = cups[vals.index(1)]

lastcup = Cup(10)
cups[-1].next = lastcup
lastcup.minusone = cups[vals.index(9)]
for v in range(11, 1000001):
    lastcup.next = Cup(v)
    lastcup.next.minusone = lastcup
    lastcup = lastcup.next
lastcup.next = cups[0]
cupone.minusone = lastcup

play(cups, 10000000)
print(cupone.next)
print(cupone.next.next)
print(cupone.next.value*cupone.next.next.value)
    