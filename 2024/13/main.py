import re
from math import modf


def read_data(fn):
    p = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)')
    linear_eqs = []
    with open(fn) as fh:
        for block in fh.read().split('\n\n'):
            groups = p.match(block)
            equ = [int(i) for i in groups.group(1, 3, 5, 2, 4, 6)]
            linear_eqs.append(equ)
    return linear_eqs


def solve(x1, x2, x3, y1, y2, y3):
    # use cramer's rule to solve the linear equations
    # a * x1 + b*x2 = x3
    # b * y1 + b*y2 = y3

    a = (x3 * y2 - x2 * y3) / (x1 * y2 - x2 * y1)
    b = (x1 * y3 - x3 * y1) / (x1 * y2 - x2 * y1)

    return (a, b)


def task1(fn):
    linear_eqs = read_data(fn)
    tokens = 0
    for eq in linear_eqs:
        a, b = solve(*eq)
        if modf(a)[0] == 0 and modf(b)[0] == 0 and a <= 100 and b <= 100:
            tokens += 3*int(a) + int(b)
    return tokens


def task2(fn):
    linear_eqs = read_data(fn)
    linear_eqs = [[x1, x2, x3+10000000000000, y1, y2, y3+10000000000000] for x1, x2, x3, y1, y2, y3 in linear_eqs]
    tokens = 0
    for eq in linear_eqs:
        a, b = solve(*eq)
        if modf(a)[0] == 0 and modf(b)[0] == 0:
            tokens += 3*int(a) + int(b)
    return tokens


assert task1('test_input.txt') == 480
print(task1('input.txt'))

print(task2('input.txt'))
