#!/usr/bin/env python3

def main():
    f = open("day02_input.txt","r")
    lines = f.read().splitlines()
    allowedPasswords = 0

    for line in lines:
        l = line.split()

        counts = l[0].split('-')
        char = l[1].strip(':')
        string = l[2]
        
        count = string.count(char)
        
        if count >= int(counts[0]) and count <= int(counts[1]):
                allowedPasswords = allowedPasswords + 1

    print(allowedPasswords)


''''
    for l in lines:
        count = 0
        for ch in l[]
        '''

if __name__ == "__main__":
    main()