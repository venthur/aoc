from itertools import pairwise, groupby
from math import prod


def task1(fn):
    with open(fn) as fh:
        numbers = [int(n) for n in fh.read().splitlines()]

    numbers.append(0)
    numbers.append(max(numbers) + 3)
    numbers.sort()

    diff = [b-a for a, b in pairwise(numbers)]
    return diff.count(1) * diff.count(3)


def task2(fn):
    with open(fn) as fh:
        numbers = [int(n) for n in fh.read().splitlines()]

    numbers.append(0)
    numbers.append(max(numbers) + 3)
    numbers.sort()

    diff = [b-a for a, b in pairwise(numbers)]
    fktrs = [
        2**(len(m) - 1) - (len(m) == 4)
        for v, g in groupby(diff)
        if v == 1 and len(m := list(g)) > 1
    ]
    return prod(fktrs)


assert task1('test_input0.txt') == 35
print(task1('input.txt'))

assert task2('test_input0.txt') == 8
assert task2('test_input1.txt') == 19208
print(task2('input.txt'))
