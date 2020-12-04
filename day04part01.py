#!/usr/bin/env python3

f = (open("day04_input.txt","r").read()).split('\n\n')
count = 0
for line in f:
    if 'byr' in line and 'iyr' in line and 'eyr' in line and 'hgt' in line and 'hcl' in line and 'ecl' in line and 'pid' in line:
        count = count + 1

print(count)