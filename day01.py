#!/usr/bin/env python3

SUM = 2020

def check_sum(*n):
    s = 0
    for num in n:
        s = s + int(num)
    return s == SUM

# Loop for Part 1
def loop_part01(list):
    for i in list:
        for j in list:
            if check_sum(i,j):
                print(int(i)*int(j))
                return

# Loop for Part 2
def loop_part02(list):
    for i in list:
        for j in list:
            for k in list:
                if check_sum(i,j,k):
                    print(int(i)*int(j)*int(k))
                    return


def main():
    f = open("day01_input.txt","r")
    lines = f.read().splitlines()
    loop_part01(lines)
    loop_part02(lines)



if __name__ == "__main__":
    main()