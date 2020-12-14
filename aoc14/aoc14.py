#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:27:59 2020

@author: robertnolet
"""

import re
from functools import reduce
from itertools import combinations

def setBit(x, i, to):
    if to == 0: return x & (2**36-1-2**(35-i))
    if to == 1: return x | 2**(35-i)
    return x
    
def maskValue(mask, value):
    return reduce(lambda x,y: setBit(x, *y), [(i,int(c)) for i,c in enumerate(mask) if c != 'X'], value)

def maskAddrs(mask, addr, start=0):
    if start >= len(mask): return {addr}
    if mask[start] == '0': return maskAddrs(mask, addr, start+1)
    if mask[start] == '1': return maskAddrs(mask, setBit(addr, start, 1), start+1)
    return maskAddrs(mask, setBit(addr, start, 0), start+1).union(maskAddrs(mask, setBit(addr, start, 1), start+1))
    
    
def maskAddr(mask, addr):
    return ''.join(m if m in '1X' else a for m, a in zip(mask, format(addr, '036b')))

def cover(addrs):
    if len(addrs) == 1: return 2**sum(c == 'X' for c in addr)
    if any(c1+c2 in ['01','10'] for c1,c2 in zip(*addrs[0:2])): return 0
    merge = [c1 if c2 == 'X' else c2 for c1,c2 in zip(*addrs[0:2])]
    return cover([merge]+addrs[2:])
    
    
def addrEqual(addr1, addr2):
    return all(c1 == c2 for c1,c2 in zip(addr1, addr2) if c1 != 'X' and c2 != 'X')
                
pat = re.compile(r'mask = ([01X]{36})|mem\[(\d+)\] = (\d+)$')

data = []
for r in map(pat.match, open('input.txt')):
    if r.group(1): mask = r.group(1)
    elif r.group(2) and r.group(3):
        data.append((mask, int(r.group(2)), int(r.group(3))))
    else:
        print('Parsing error!')
        
print(sum({addr:maskValue(mask, val) for mask,addr,val in data}.values()))

memory = {}
for mask, addr, val in data:
    memory.update({a:val for a in maskAddrs(mask, addr)})
print(sum(memory.values()))
 
