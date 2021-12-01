
def loop1(lines):
    previous = None
    increases = 0
    for line in lines:
        if previous is None:
            previous = line
            continue
        if int(line) > int(previous):
            increases += 1
        previous = line
    print("Individual Increases: {}".format(increases))

def loop2(lines):
    previous = [None, None, None]
    l_sum = None
    increases = 0
    for line in lines:
        previous.append(int(line))
        previous.pop(0)
        if None in previous:
            continue
        elif l_sum is None:
            l_sum = quicksum(*previous)
            continue
        else:
            sum = quicksum(*previous)
            if sum > l_sum:
                increases += 1
            l_sum = sum
    print("Sliding Windows Increases: {}".format(increases))

def quicksum(*nums):
    s = 0
    for n in nums:
        s += int(n)
    return s

def main():
    f = open("d01.txt","r")
    lines = f.read().splitlines()
    loop1(lines=lines)
    loop2(lines=lines)

if __name__ == "__main__":
    main()