from itertools import count
from statistics import variance


def read_input(fn):
    data = []
    with open(fn) as fh:
        for line in fh:
            p, v = line.split()
            p = [int(i) for i in p.split('=')[-1].split(',')]
            v = [int(i) for i in v.split('=')[-1].split(',')]
            data.append([*p, *v])
    return data


def calculate_pos(p, v, steps):
    x = p[0] + v[0] * steps
    y = p[1] + v[1] * steps
    return x, y


def calculate_quadrant(p, v, steps, height, width):
    x, y = calculate_pos(p, v, steps)
    x = x % width
    y = y % height
    if x < width // 2:
        if y < height // 2:
            return 1
        elif y > height // 2:
            return 2
        else:
            return None
    elif x > width // 2:
        if y < height // 2:
            return 3
        elif y > height // 2:
            return 4
        else:
            return None
    else:
        return None


def task1(fn, height, width):
    data = read_input(fn)

    quadrants = [calculate_quadrant((px, py), (vx, vy), 100, height, width)
                 for px, py, vx, vy
                 in data
                 ]

    return quadrants.count(1) * quadrants.count(2) * quadrants.count(3) * quadrants.count(4)


def task2(fn, height, width):
    # assumption: the variance of x, y positions is minimal when the easter egg
    # appears
    data = read_input(fn)

    for i in count():
        positions = [calculate_pos((px, py), (vx, vy), i)
                     for px, py, vx, vy in data
                     ]
        positions = [(x % width, y % height) for x, y in positions]
        xvar = variance([x for x, _ in positions])
        yvar = variance([y for _, y in positions])
        if xvar < 400 and yvar < 400:
            return i


assert task1('test_input.txt', 7, 11) == 12
print(task1('input.txt', 103, 101))

print(task2('input.txt', 103, 101))
