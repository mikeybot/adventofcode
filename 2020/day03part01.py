#!/usr/bin/env python3

f = open("day03_input.txt","r")
lines = f.read().splitlines()
counter = 0
hits = 0

for l in lines:
    if l[counter] == '#':
        hits = hits + 1
    counter = (counter + 3) % len(l)
print(hits)