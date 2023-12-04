from collections import defaultdict
from itertools import product


def task1(fn):
    data = defaultdict(str)
    with open(fn) as fh:
        for row, line in enumerate(fh.read().splitlines()):
            for col, char in enumerate(line):
                if char.isdecimal():
                    if line[col-1].isdecimal():
                        continue
                    # read characters until we have a number
                    value = char
                    i = 1
                    while col+i <= len(line)-1 and line[col+i].isdecimal():
                        value = value + line[col+i]
                        i += 1
                    data[(row, col)] = value
                elif char != '.':
                    data[(row, col)] = char

    # check all numbers if they have non numeric neighbors
    s = 0
    for (row, col), val in filter(
        lambda x: x[-1].isdecimal(), list(data.items())
    ):
        digits = len(val)
        for x, y in product(range(col-1, col+1+digits), range(row-1, row+2)):
            c = data[(y, x)]
            if c and not c.isdecimal():
                s += int(val)
                break
        else:
            pass

    return s


def task2(fn):
    data = defaultdict(str)
    with open(fn) as fh:
        for row, line in enumerate(fh.read().splitlines()):
            for col, char in enumerate(line):
                if char.isdecimal():
                    if line[col-1].isdecimal():
                        continue
                    # read characters until we have a number
                    value = char
                    i = 1
                    while col+i <= len(line)-1 and line[col+i].isdecimal():
                        value = value + line[col+i]
                        i += 1
                    data[(row, col)] = value
                elif char == '*':
                    data[(row, col)] = char

    gears = {}
    for (row, col), val in filter(
        lambda x: x[-1].isdecimal(), list(data.items())
    ):
        digits = len(val)
        for x, y in product(range(col-1, col+1+digits), range(row-1, row+2)):
            c = data[(y, x)]
            if c and not c.isdecimal():
                gears[(y, x)] = gears.get((y, x), []) + [val]

    s = 0
    for (row, col), vals in gears.items():
        if len(vals) == 2:
            s += int(vals[0]) * int(vals[1])
    return s


assert task1('test_input.txt') == 4361
print(task1('input.txt'))

assert task2('test_input.txt') == 467835
print(task2('input.txt'))
