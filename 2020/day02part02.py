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
        
        # ^ = XOR 
        if (string[int(counts[0])-1] == char) ^ (string[int(counts[1])-1] == char):
            allowedPasswords = allowedPasswords + 1
        
    print(allowedPasswords)


if __name__ == "__main__":
    main()