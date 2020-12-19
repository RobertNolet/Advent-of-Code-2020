#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:10:07 2020

@author: robertnolet
"""

def parse(s):
    n, parts = s.split(': ')
    return n, [[s.strip('\"') for s in part.split()] for part in parts.split(' | ')]

# Check if the start of string s matches the sequence of rules or characters in ns.
# Return the result (True/False) and the part of s left over (empty if no match.)
def matchsequence(s, ns, rules):
    if s == '' and len(ns) > 0: return False, ''
    for n in ns:
        if n.isnumeric():
            result, s = partialmatch(s, n, rules)
        else:
            result = (s[0] == n)
            s = s[1:]
        if not result: return False, ''
    return True, s

# Check if the start of string s matches rule n. Return the result (True/False)
# and the part of s left over (empty if no match.)
def partialmatch(s, n, rules):
    for part in rules[n]:
        result, rest = matchsequence(s, part, rules)
        if result:
            return True, rest
    return False, ''
        
# The new rules consist of
# 0: 8 11
# 8: 41 | 41 8
# 11: 42 31 | 42 11 31
# This translates to a number a of 42's, followed by a lesser number b 31's.
# So we partially match and count rule 42, then do the same for rule 31.    
def matchrulezero(s, rules):
    a = 0 # number of times rule 42 was applied
    b = 0 # number of times rules 31 was applied
    # Apply rule 42 until we can't continue.
    cont = True
    while (cont):
        cont, rest = partialmatch(s, '42', rules)
        if cont: 
            s = rest
            a += 1
    # Apply rule 31 until we can't continue
    cont = True
    while(cont):
        cont, rest = partialmatch(s, '31', rules)
        if cont:
            s = rest
            b += 1
    return a > 0 and b > 0 and a > b and s == ''
                
                
    
rawrules, msgs = [data.split('\n') for data in map(str.strip, open('input.txt').read().split('\n\n'))]
rules = {n:parts for n,parts in map(parse, rawrules)}

print(sum(partialmatch(msg, '0', rules) == (True, '') for msg in msgs))

print(sum(matchrulezero(msg, rules) for msg in msgs))

