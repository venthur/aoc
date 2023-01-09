from itertools import permutations


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines = [
        [int(n) for n in line.split()]
        for line
        in lines
    ]

    diff = 0
    for line in lines:
        diff += max(line) - min(line)

    return diff


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines = [
        [int(n) for n in line.split()]
        for line
        in lines
    ]

    diff = 0
    for line in lines:
        for a, b in permutations(line, 2):
            if a % b == 0:
                diff += a // b
                break

    return diff


assert task1('test_input.txt') == 18
print(task1('input.txt'))

assert task2('test_input2.txt') == 9
print(task2('input.txt'))
