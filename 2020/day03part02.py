#!/usr/bin/env python3

f = open("day03_input.txt","r")
slope = f.read().splitlines()


def run(over, lines):
    counter = 0
    hits = 0

    for l in lines:
        if l[counter] == '#':
            hits = hits + 1
        counter = (counter + over) % len(l)
    return hits

print(run(1,slope) * run(3,slope) * run(5,slope) * run(7,slope) * run(1,slope[::2]))