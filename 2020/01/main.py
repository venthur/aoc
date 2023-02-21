from itertools import combinations


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines = [int(n) for n in lines]
    for a, b in combinations(lines, 2):
        if a + b == 2020:
            return a*b


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines = [int(n) for n in lines]
    for a, b, c in combinations(lines, 3):
        if a + b + c == 2020:
            return a*b*c


print(task1('input.txt'))
print(task2('input.txt'))
