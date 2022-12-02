with open('input.txt') as fh:
    input = fh.readlines()


def part1(input):
    if isinstance(input, str):
        input = [input]
    a_total = 0
    for line in input:
        l, w, h = [int(i) for i in line.split('x')]
        a = 2*l*w + 2*w*h + 2*h*l + sorted([l, w, h])[0] * sorted([l, w, h])[1]
        a_total += a
    print(a_total)


def part2(input):
    if isinstance(input, str):
        input = [input]
    len_total = 0
    for line in input:
        l, w, h = [int(i) for i in line.split('x')]
        len_ = l*w*h + sorted([l, w, h])[0]*2 + sorted([l, w, h])[1]*2
        len_total += len_
    print(len_total)



part1(input)
part2(input)
