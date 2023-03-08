from itertools import permutations
from functools import reduce


def magnitude(x):
    while len(x) > 1:
        for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(x, x[1:])):
            if depth1 != depth2:
                continue
            val = num1 * 3 + num2 * 2
            x = x[:i] + [[val, depth1-1]]+x[i+2:]
            break
    return x[0][0]


def add(a, b):
    x = [[num, depth+1] for num, depth in a + b]
    while True:
        change, x = explode(x)
        if change:
            continue
        change, x = split(x)
        if not change:
            break
    return x


def explode(x):
    for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(x, x[1:])):
        if depth1 < 5 or depth1 != depth2:
            continue
        if i > 0:
            x[i-1][0] += num1
        if i < len(x) - 2:
            x[i+2][0] += num2
        return True, x[:i] + [[0, depth1-1]] + x[i+2:]

    return False, x


def split(x):
    for i, (num, depth) in enumerate(x):
        if num < 10:
            continue
        down = num // 2
        up = num - down
        return True, x[:i] + [[down, depth+1], [up, depth+1]] + x[i+1:]

    return False, x


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    flatlist = []
    for line in lines:
        flatline, depth = [], 0
        for char in line:
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
            elif char.isdigit():
                flatline.append([int(char), depth])
        flatlist.append(flatline)

    p1 = magnitude(reduce(add, flatlist))
    p2 = max(magnitude(add(a, b)) for a, b in permutations(flatlist, 2))

    return p1, p2

assert task1('test_input0.txt') == (4140, 3993)
print(task1('input.txt'))
