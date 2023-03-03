from itertools import pairwise


def task1(fn):
    with open(fn) as fh:
        lines = [int(n) for n in fh.read().splitlines()]

    inc = 0
    for a, b in pairwise(lines):
        if a < b:
            inc += 1

    return inc


def task2(fn):
    with open(fn) as fh:
        lines = [int(n) for n in fh.read().splitlines()]

    inc = 0
    for i in range(len(lines)-2):
        lines[i] = sum(lines[i:i+3])
    lines = lines[:-2]

    inc = 0
    for a, b in pairwise(lines):
        if a < b:
            inc += 1

    return inc


print(task1('input.txt'))

assert task2('test_input.txt') == 5
print(task2('input.txt'))
