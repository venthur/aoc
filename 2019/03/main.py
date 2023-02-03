def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    paths = []
    for line in lines:
        x, y = 0, 0
        path = set()
        for direction in line.split(','):
            d, steps = direction[0], int(direction[1:])
            for s in range(steps):
                match d:
                    case "U":
                        y -= 1
                    case "R":
                        x += 1
                    case "D":
                        y += 1
                    case "L":
                        x -= 1
                path.add((x, y))
        paths.append(path)

    common = paths[0] & paths[1]
    closest = None
    for x, y in common:
        d = abs(x) + abs(y)
        if closest is None or d < closest:
            closest = d

    return closest


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    paths = []
    for line in lines:
        x, y = 0, 0
        path = list()
        for direction in line.split(','):
            d, steps = direction[0], int(direction[1:])
            for s in range(steps):
                match d:
                    case "U":
                        y -= 1
                    case "R":
                        x += 1
                    case "D":
                        y += 1
                    case "L":
                        x -= 1
                path.append((x, y))
        paths.append(path)

    common = set(paths[0]) & set(paths[1])
    closest = None
    for x, y in common:
        d = paths[0].index((x, y)) + paths[1].index((x, y)) + 2
        if closest is None or d < closest:
            closest = d

    return closest


assert task1('test_input0.txt') == 6
assert task1('test_input1.txt') == 159
print(task1('input.txt'))

assert task2('test_input1.txt') == 610
print(task2('input.txt'))
