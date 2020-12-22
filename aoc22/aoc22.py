#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:19:54 2020

@author: robertnolet
"""

from copy import deepcopy

def score(deck):
    return sum((i+1)*v for i,v in enumerate(reversed(deck)))

def play(decks, recursive = False):
    played = []
    while len(decks[0])>0 and len(decks[1])>0:
        if recursive:
            if any(decks == p for p in played): return 0, score(decks[0])
            played.append(deepcopy(decks))
            
        cards = [decks[0].pop(0), decks[1].pop(0)]
        if recursive and len(decks[0]) >= cards[0] and len(decks[1]) >= cards[1]:
            winner, sc = play([decks[0][:cards[0]].copy(), decks[1][:cards[1]].copy()], True)
        else:
            winner = 0 if cards[0] > cards[1] else 1
        decks[winner].extend([cards[winner], cards[1-winner]])
    return winner, score(decks[winner])
    
decks = [list(map(int,deck.split('\n')[1:])) for deck in open('input.txt').read().strip().split('\n\n')]
print(play(deepcopy(decks)))
print(play(deepcopy(decks), True))