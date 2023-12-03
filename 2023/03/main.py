from collections import defaultdict
from itertools import product


def task1(fn):
    data = defaultdict(str)
    with open(fn) as fh:
        for row, line in enumerate(fh.read().splitlines()):
            n = None
            for col, char in enumerate(line):
                if char.isnumeric():
                    if n is None:
                        n = ''
                    n = n + char
                    continue
                else:
                    if n is None:
                        pass
                    else:
                        ndigits = len(str(n))
                        data[(row, col-ndigits)] = n
                        n = None
                if char != '.':
                    data[(row, col)] = char


    # check all numbers if they have non numeric neighbors
    s = 0
    for (row, col), val in filter(lambda x: x[-1].isnumeric(), list(data.items())):
        digits = len(val)
        for x, y in product(range(digits+2), (-1, 0, 1)):
            c = data[(row+y, col-1+x)]
            if c and not c.isnumeric():
                s += int(val)
                print(val)
                break

    print(s)
    return s


assert task1('test_input.txt') == 4361
print(task1('input.txt'))
