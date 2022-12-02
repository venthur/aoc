
with open('input.txt') as fh:
    input = fh.read().strip()


def part1(input):
    up = input.count('(')
    down = input.count(')')
    return up - down


def part2(input):
    pos = 0
    for i, direction in enumerate(input):
        if direction == '(':
            pos += 1
        else:
            pos -= 1
        if pos < 0:
            return i + 1


print(part1(input))
print(part2(input))
