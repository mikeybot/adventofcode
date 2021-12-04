
def part1(lines):
    h = 0
    d = 0
    for line in lines:
        l = line.split(" ")
        if l[0] == 'forward':
            h += int(l[1])
        elif l[0] == 'up':
            d -= int(l[1])
        elif l[0] == 'down':
            d += int(l[1])

    print("Position: d = {d}, h = {h}, product = {p}".format(d=d,h=h, p=d*h))


def part2(lines):
    pass


def main():
    f = open("d02.txt","r")
    lines = f.read().splitlines()
    part1(lines=lines)
    part2(lines=lines)

if __name__ == "__main__":
    main()