#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:51:25 2020

@author: robertnolet
"""

import re

pat = re.compile('(\S+):(\S+)')
data = [{m.group(1):m.group(2) for m in pat.finditer(line)} for line in open('input.txt').read().split('\n\n')]

keys = {'hcl', 'pid', 'ecl', 'hgt', 'eyr', 'iyr', 'byr'}

# Is a passport valid for part 1
def valid1(passport):
    return keys.issubset(passport.keys())


# IS a passport valid for part 2
def valid2(passport):
    if not valid1(passport): return False
    if not 1920 <= int(passport['byr']) <= 2002: return False
    if not 2010 <= int(passport['iyr']) <= 2020: return False
    if not 2020 <= int(passport['eyr']) <= 2030: return False
    if passport['hgt'][-2:] == 'cm':
        if not 150 <= int(passport['hgt'][:-2]) <= 193: return False
    elif passport['hgt'][-2:] == 'in':
        if not 59 <= int(passport['hgt'][:-2]) <= 76: return False
    else: return False
    if passport['hcl'][0] != '#': return False
    try: int(passport['hcl'][1:], base=16)
    except ValueError: return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False
    if len(passport['pid']) != 9: return False
    if not passport['pid'].isdigit(): return False
    return True

# Part 1
print(sum(map(valid1, data)))

# Part 2
print(sum(map(valid2, data)))

