def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    maze = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            maze[x, y] = char

    xs, ys = zip(*maze.keys())
    x, y = 0, 0
    trees = 0
    while y <= max(ys):
        if maze[x, y] == '#':
            trees += 1
        y += 1
        x += 3
        x %= max(xs)+1
    return trees


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    maze = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            maze[x, y] = char

    xs, ys = zip(*maze.keys())

    trees2 = 1
    for dx, dy in (1, 1), (3, 1), (5, 1), (7, 1), (1, 2):
        x, y = 0, 0
        trees = 0
        while y <= max(ys):
            if maze[x, y] == '#':
                trees += 1
            x += dx
            y += dy
            x %= max(xs)+1
        trees2 *= trees

    return trees2


assert task1('test_input0.txt') == 7
print(task1('input.txt'))

assert task2('test_input0.txt') == 336
print(task2('input.txt'))
